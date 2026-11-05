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


x=blk('room-flash-tanuki','5967586b','z tanuki','B3','A tatami room with painted gold wall panels and a gold coffered ceiling, with a small sign standing on the floor','A painted room with a coffered ceiling and a visitor sign, 28 December 2014.',
 "A fuller view of one of these rooms: painted wall panels at eye level, the gold-grid ceiling above and a small sign standing on the tatami. The sign appears to be a notice for visitors, and I read it as a no-flash reminder, but I cannot be sure of the wording at this size. Commons describes the photo only as Kumamoto castle, so I do not name the room, and the 2014 date means it predates the 2016 earthquakes.")
put('so I only describe the ceiling.</p>',x)
open(p,'w',encoding='utf-8').write(s)
with open(R+'PHOTO-CREDITS.csv','a',encoding='utf-8',newline='') as fh: csv.writer(fh,lineterminator='\r\n').writerows(rows)
import json
for tag in ['div','figure','picture','p','a','ul','li','details','section','h2']:
    o=len(re.findall(r'<%s[\s>]'%tag,s)); c=len(re.findall(r'</%s>'%tag,s)); assert o==c,(tag,o,c)
for m_ in re.finditer(r'<script type="application/ld\+json">(.*?)</script>',s,re.S): json.loads(m_.group(1))
print(len(rows),'ok')
