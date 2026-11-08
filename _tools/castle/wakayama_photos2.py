import re, csv, os
from PIL import Image
R='/home/claude/sacred-japan/'; A='/mnt/user-data/attachments/fd332c08-3f6b-545a-883b-83277e19ff52/'
SL='wakayama-castle'
L={'S3':('CC BY-SA 3.0','https://creativecommons.org/licenses/by-sa/3.0/'),'S25':('CC BY-SA 2.5','https://creativecommons.org/licenses/by-sa/2.5/'),'S4':('CC BY-SA 4.0','https://creativecommons.org/licenses/by-sa/4.0/'),'B4':('CC BY 4.0','https://creativecommons.org/licenses/by/4.0/'),'B2':('CC BY 2.0','https://creativecommons.org/licenses/by/2.0/'),'CC0':('CC0 1.0','https://creativecommons.org/publicdomain/zero/1.0/'),'PD':('Public Domain','https://commons.wikimedia.org/wiki/Template:PD-self')}
rows=[]
def mk(k,f,au,lic,alt,cap,hero=False,maxw=760):
    im=Image.open(A+f+'-image.jpg').convert('RGB')
    if im.width>1200: im=im.resize((1200,round(im.height*1200/im.width)),Image.LANCZOS)
    D=R+f'guides/{SL}/images/'; os.makedirs(D,exist_ok=True)
    im.save(D+k+'.jpg',quality=84,optimize=True); im.save(D+k+'.webp',quality=80)
    l=L[lic]
    rows.append([f'guides/{SL}',f'/guides/{SL}/images/{k}.jpg',l[0],l[1],l[1],f'{cap} Photo: {au}, {l[0]}, via Wikimedia Commons (resized)'])
    fs='margin:0 0 48px;' if hero else f'margin:28px auto;max-width:{maxw}px;'
    ld='eager' if hero else 'lazy'
    ex='max-height:420px;object-fit:cover;' if hero else ''
    return (f'<figure style="{fs}"><picture><source srcset="/guides/{SL}/images/{k}.webp" type="image/webp"><img src="/guides/{SL}/images/{k}.jpg" alt="{alt}" width="{im.width}" height="{im.height}" loading="{ld}" style="width:100%;height:auto;border-radius:4px;display:block;{ex}"></picture>'
            f'<figcaption style="font-size:13px;color:var(--enshu);margin-top:10px;text-align:center;line-height:1.6;">{cap}<br>Photo: {au}, <a href="{l[1]}" target="_blank" rel="noopener" style="color:var(--enshu);">{l[0]}</a>, via Wikimedia Commons (resized)</figcaption></figure>')
def blk(*a,para,maxw=760): return '\n    '+mk(*a,maxw=maxw)+f'\n    <p>{para}</p>'
p=R+f'guides/{SL}/index.html'; s=open(p,encoding='utf-8').read()
def put(anchor,html,before=False):
    global s
    assert s.count(anchor)==1,anchor
    s=s.replace(anchor,(html+anchor) if before else (anchor+html))


put("In February the trees are bare, so nothing hides the structure.</p>",
 blk('keep-autumn-wak89','02e21df6','Wak89','S3','A white keep with a long white wall and a stone base seen from below under a blue sky, with a pine in front and red autumn leaves at the right','The keep and a long white wall from below, 29 November 2010 (Commons: 曲輪, an enclosure of the castle).',
  para="Commons lists this under 曲輪 (kuruwa, an enclosure within the castle), photographed on 29 November 2010. A long white wall with slit windows runs along a stone base toward the keep, and a notice board stands at the lower right. The red leaves at the right edge match the late-November colour that GLTJP suggests. I did not confirm exactly where this stands.")+
 blk('keep-branches','98d399bd','Hyppolyte de Saint-Rambert','S4','A white keep with green copper roof ornaments seen between bare branches against a deep blue sky, above a stone base and a large dark rock','The keep through bare branches, 23 February 2020.',
  para="Photographed on 23 February 2020, the same day as the low-angle view above. Bare branches cross the frame, and the keep rises over its stone base with a dark boulder at the right. In winter the white walls and the blue sky are at their sharpest, and the stone base shows its mix of green and brown stones.")+
 blk('gate-turret','2f9afe2d','Hyppolyte de Saint-Rambert','S4','A white turret with dark tiled roofs and green copper ornaments above a gate opening, with a stone wall of orange and green stones below and a deep blue sky','A gate turret and its stone wall, 23 February 2020.',
  para="Same photographer and day. I read this as a gate with a turret above it, though I have not matched it to a named gate, so I do not name it. The dark roof tiles, the green ornaments on the ridges and the stones in orange, green and grey are all clear. The stone work is the part I would walk close to.")+
 blk('view-from-keep','6924407e','Hyppolyte de Saint-Rambert','S4','A view over the roofs of Wakayama from the keep, with a green copper roof ornament in the foreground and hills on the horizon','The view from the keep over the city, 23 February 2020.',
  para="This is the view from the upper part of the keep, taken on 23 February 2020, with the green copper ridge ornament in the foreground. Houses, trees and low hills spread out to the horizon, and at the right edge I can make out a small red torii and steps among the trees. This is the view the observation floor gives you."))
put("which is the look of the walls I mention above. Commons does not say where in the grounds this is.</p>",
 blk('moat-walls','97c5ceab','Hyppolyte de Saint-Rambert','S4','A calm moat reflecting pines, with a high rough stone wall and a lower stone wall running along its edge','The moat and its stone walls, 23 February 2020.',
  para="Photographed on 23 February 2020. A calm moat runs between a high stone wall with a sharp corner and a lower wall along the bank, and the pines are reflected in the water. Bands of a straw colour are wound around some of the trunks, but I do not know their purpose. The walls here are good for seeing how the stones are laid in rough courses."))
put("not just around it.</p>",
 blk('night-keep','ebc8c312','mk_is_here','B2','A floodlit white keep on a dark hill above trees and lawn, with a row of red lanterns and pale blossoms below, under a deep blue night sky','The lit keep at night, 4 April 2017 (Commons: night view of Wakayama Castle).',
  para="Commons has this as a night view from 4 April 2017. The keep and its tower glow white on the dark hill, and below them a row of red lanterns and pale blossoms in the trees suggest cherry season. The lawn in front is a good place to stand for this view. I have not confirmed the exact illumination hours for any year; GLTJP gives sunset to 23:00 in season, which is worth checking before you go."))
open(p,'w',encoding='utf-8').write(s)
with open(R+'PHOTO-CREDITS.csv','a',encoding='utf-8',newline='') as f: csv.writer(f,lineterminator='\r\n').writerows(rows)
print(len(rows))
for tg in ['div','figure','picture','p','a','ul','li','details','section','h2']:
    assert len(re.findall(f'<{tg}[ >]',s))==len(re.findall(f'</{tg}>',s)),tg
