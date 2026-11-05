import re, csv, os
from PIL import Image
R='/home/claude/sacred-japan/'; A='/mnt/user-data/attachments/fd332c08-3f6b-545a-883b-83277e19ff52/'
SL='kumamoto-castle'
L={'PD':('Public domain','https://creativecommons.org/publicdomain/mark/1.0/'),'S2':('CC BY-SA 2.0','https://creativecommons.org/licenses/by-sa/2.0/'),'S4':('CC BY-SA 4.0','https://creativecommons.org/licenses/by-sa/4.0/'),'B3':('CC BY 3.0','https://creativecommons.org/licenses/by/3.0/'),'B4':('CC BY 4.0','https://creativecommons.org/licenses/by/4.0/'),'S3':('CC BY-SA 3.0','https://creativecommons.org/licenses/by-sa/3.0/'),'B2':('CC BY 2.0','https://creativecommons.org/licenses/by/2.0/'),'C0':('CC0 1.0','https://creativecommons.org/publicdomain/zero/1.0/')}
rows=[]
def blk(k,f,au,lic,alt,cap,para,maxw=760):
    im=Image.open(A+f+'-image.jpg').convert('RGB')
    if im.width>1200: im=im.resize((1200,round(im.height*1200/im.width)),Image.LANCZOS)
    D=R+f'guides/{SL}/images/'; os.makedirs(D,exist_ok=True)
    im.save(D+k+'.jpg',quality=84,optimize=True); im.save(D+k+'.webp',quality=80)
    l=L[lic]
    rows.append([f'guides/{SL}',f'/guides/{SL}/images/{k}.jpg',l[0],l[1],l[1],f'{cap} Photo: {au}, {l[0]}, via Wikimedia Commons (resized)'])
    return (f'\n    <figure style="margin:28px auto;max-width:{maxw}px;"><picture><source srcset="/guides/{SL}/images/{k}.webp" type="image/webp"><img src="/guides/{SL}/images/{k}.jpg" alt="{alt}" width="{im.width}" height="{im.height}" loading="lazy" style="width:100%;height:auto;border-radius:4px;display:block;"></picture>'
            f'<figcaption style="font-size:13px;color:var(--enshu);margin-top:10px;text-align:center;line-height:1.6;">{cap}<br>Photo: {au}, <a href="{l[1]}" target="_blank" rel="noopener" style="color:var(--enshu);">{l[0]}</a>, via Wikimedia Commons (resized)</figcaption></figure>\n    <p>{para}</p>')
p=R+f'guides/{SL}/index.html'; s=open(p,encoding='utf-8').read()
def put(anchor,html):
    global s
    assert s.count(anchor)==1,anchor
    s=s.replace(anchor,anchor+html)


def before(anchor,html):
    global s
    assert s.count(anchor)==1,anchor
    s=s.replace(anchor,html+'\n\n    '+anchor)

m=blk('gold-663','11c7ad9f','663highland','S3','A tatami room opening onto gold-leaf sliding screens painted with pine trees and a scene of figures beside a building','Gold-leaf screens painted with pines and figures, 10 May 2009.',
 "Gold ground, bright mineral colours and a figure scene in the middle: this is the kind of painted room that the palace restoration is about. The photo is from 2009, so it shows the state before the 2016 earthquakes. Commons gives the castle but not the room, so I do not name it.")
m+=blk('umenoma-sanjo','8ef2dca0','Sanjo','PD','A long empty tatami room with plain white walls and a wooden ceiling, with a small sign on the floor and a further room seen through the far opening','The Plum Room (Ume-no-ma) of the Honmaru Palace, 28 September 2008.',
 "By contrast, this room is plain: tatami, white walls, a wooden ceiling and a view through to the next room. The photo is small (about 850 pixels wide) and I have not enlarged it. It dates from 2008, so check the current opening status of the palace before you plan around any room.",maxw=640)
m+=blk('ceiling-tanuki','963b1a03','z tanuki','B3','A coffered ceiling in which each gold panel is painted with flowers and plants, seen from below at an angle','A coffered ceiling with a painted flower in every panel, 28 December 2014.',
 "Look up in these rooms. Each square of the ceiling carries its own painted plants and flowers on a gold ground, set in a dark lattice. The photo is from 2014 and Commons does not name the room, so I only describe the ceiling.")
put('as well as stone walls.</p>',m)
k=blk('keep-low-2026','2bd59b4b','Hyppolyte de Saint-Rambert','B4','The black keep seen from a stone plaza below, with its layered roofs against a pale sky and a few visitors at the base','The keep seen from the plaza below, 15 January 2026.',
 "This is the angle that makes the keep look as tall as it is: black boards, layered gabled roofs and a stone base, with a few visitors at the bottom for scale. It was taken in January 2026, before the July 2026 earthquake, so look at the current condition of the keep and the walls on the official site.")
put('check the current state before you plan around it.</p>',k)
t=blk('tunnel-2026','2c1da69c','Hyppolyte de Saint-Rambert','B4','A dark wooden passage with heavy beams running along a stone wall, lit by a single lantern','A dark timber passage beside a stone wall, 15 January 2026.',
 "Not everything on the tour is open air. This passage runs between heavy timber beams and a stone wall, and a single lantern lights it. Commons gives no name for this particular passage, so I only describe it. It is a useful change of scale from the walls seen from outside.")
t+=blk('roof-view-2026','024a67f7','Hyppolyte de Saint-Rambert','B4','Looking down from a high level past the end of a tiled roof ridge to a wide stone plaza with visitors and green fencing','Looking down past a roof ridge to the plaza, 15 January 2026.',
 "This view down from above the plaza, past the end of a tiled roof ridge, shows how large the open space in front of the keep is, with people reduced to small figures. Commons does not say from where in the castle it was taken, and what is open to visitors changes, so I do not promise this view.")
put('the walls here have been repaired in the years since.</p>',t)
s=s.replace('"dateModified": "2026-11-05"','"dateModified": "2026-11-05"')
open(p,'w',encoding='utf-8').write(s)
with open(R+'PHOTO-CREDITS.csv','a',encoding='utf-8',newline='') as fh: csv.writer(fh,lineterminator='\r\n').writerows(rows)
import json
for tag in ['div','figure','picture','p','a','ul','li','details','section','h2']:
    o=len(re.findall(r'<%s[\s>]'%tag,s)); c=len(re.findall(r'</%s>'%tag,s)); assert o==c,(tag,o,c)
for m_ in re.finditer(r'<script type="application/ld\+json">(.*?)</script>',s,re.S): json.loads(m_.group(1))
print(len(rows),'ok')
