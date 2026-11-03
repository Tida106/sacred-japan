import re,os,csv,json
from PIL import Image
R='/home/claude/sacred-japan/'; A='/mnt/user-data/attachments/53e3d492-4bf8-5cd9-a0ec-63a7cbefb1d9/'
SL='nagoya-castle'; D=R+f'guides/{SL}/images/'; os.makedirs(D,exist_ok=True)
S3=('CC BY-SA 3.0','https://creativecommons.org/licenses/by-sa/3.0/')
B4=('CC BY 4.0','https://creativecommons.org/licenses/by/4.0/')
C0=('CC0','https://creativecommons.org/publicdomain/zero/1.0/')

def fig(k,au,lic,alt,cap,w,h,hero=False):
    img=f'<picture><source srcset="/guides/{SL}/images/{k}.webp" type="image/webp"><img src="/guides/{SL}/images/{k}.jpg" alt="{alt}" width="{w}" height="{h}" loading="{"eager" if hero else "lazy"}" style="{"width:100%;max-height:420px;object-fit:cover;object-position:center 30%;border-radius:4px;display:block;" if hero else "width:100%;height:auto;border-radius:4px;display:block;"}"></picture>'
    fc=f'<figcaption style="font-size:13px;color:var(--enshu);margin-top:10px;text-align:center;line-height:1.6;">{cap}<br>Photo: {au}, <a href="{lic[1]}" target="_blank" rel="noopener" style="color:var(--enshu);">{lic[0]}</a>, via Wikimedia Commons (resized)</figcaption>'
    mw='max-width:760px;' if w>=h else 'max-width:420px;'
    return f'<figure style="{"margin:0 0 48px;" if hero else "margin:28px auto;"+mw}">{img}{fc}</figure>\n'

P=[
('hero','ac2a6eb4','Noodle snacks (Base64 edit)',S3,
 'Nagoya Castle keep with green copper roofs and two golden shachi on the top roof, beside a smaller white tower, above a tall stone base',
 'The keep and its golden shachi, 9 August 2008 (Commons: a stitched mosaic of nine frames).',None),
('keep-low','de83326e','Syced',C0,
 'Low-angle view of the Nagoya Castle keep with stacked green roofs and a gold shachi on top, visitors gathered on the gravel below and bare cherry branches on the right',
 'The keep from the grounds, 23 March 2025 (Commons: Nagoya Castle, date from Exif data).',
 "From the foot of the walls the keep rises in stacked tiers of green roofs, with one gold shachi just visible on the top ridge. Visitors gather on the gravel in front, but this was taken while the keep was already closed, so the crowd is here for the outside view and the grounds. The cherry branches on the right are still bare, which fits a late-March date. The stone base flares outward as it climbs. A plain white structure at the right side of the keep looks like a later addition, in keeping with the concrete rebuild, though Commons does not label it."),
('aerial','7fda49b2','BobTanGo',B4,
 'Wide aerial panorama of Nagoya Castle with the green-roofed keep at the center, a moat curving to the right, autumn-colored trees and the city beyond',
 'The castle and the city from above, 17 December 2024 (Commons: Nagoya Castle aerial panorama).',
 "From the air you can see how the castle sits in the city. The green-roofed keep stands at the center, the moat curves down the right side of the picture, and the towers of central Nagoya fill the far left. The long, low dark roofs at the foot of the keep appear to be the Honmaru Palace, though Commons gives no labels, and a small white turret stands on the stone wall to their left. The trees along the moat show December autumn color, so this is a good picture of the grounds in the last weeks of the season."),
('sakura','3c2d411d','Hiroaki Kaneko',S3,
 'The Nagoya Castle keep rising above cherry blossoms in the foreground, with green roofs and a gold shachi against a clear blue sky',
 'The keep through cherry blossoms, 31 March 2016 (Commons: Nagoya Castle with cherry blossoms; first posted on Panoramio).',
 "Pale pink blossoms hang over the path, and the keep rises behind them with its green roofs and the gold shachi at the top against a clear sky. A long stone wall runs along the right, and a few people near the bottom show how large the building is. The photo is from 2016, two years before the keep closed, so the view from the path is what you will still see today, while the inside is not open. GLTJP counts about 1,000 cherry trees on the grounds, so there are plenty of places to frame a shot like this."),
]
H={};rows=[]
for k,f,au,lic,alt,cap,ps in P:
    im=Image.open(A+f+'-image.jpg').convert('RGB'); print(k,im.size)
    if im.width>1200: im=im.resize((1200,round(im.height*1200/im.width)),Image.LANCZOS)
    im.save(D+k+'.jpg',quality=84,optimize=True); im.save(D+k+'.webp',quality=80)
    H[k]=fig(k,au,lic,alt,cap,im.width,im.height,k=='hero')+(f'    <p>{ps}</p>\n' if ps else '')
    rows.append([f'guides/{SL}',f'/guides/{SL}/images/{k}.jpg',lic[0],lic[1],lic[1],f'{cap}Photo: {au}, {lic[0]}, via Wikimedia Commons (resized)'])
p=R+f'guides/{SL}/index.html'; s=open(p,encoding='utf-8').read()
assert '<figure' not in s
def aft(s,a,t):
    assert s.count(a)==1,a; return s.replace(a,a+'\n'+t)
s=s.replace('<main>\n','<main>\n\n'+H['hero'],1)
s=aft(s,'burned and replaced.</p>',H['keep-low'])
s=aft(s,'from outside, from the moat side.</p>',H['aerial'])
s=aft(s,'runs from late March to late April.</p>',H['sakura'])
open(p,'w',encoding='utf-8').write(s)
with open(R+'PHOTO-CREDITS.csv','a',encoding='utf-8',newline='') as f:
    w=csv.writer(f,lineterminator='\r\n'); [w.writerow(r) for r in rows]
for tg in ['div','figure','picture','p','a','ul','li','details','section','h2']:
    assert len(re.findall(f'<{tg}[ >]',s))==len(re.findall(f'</{tg}>',s)),tg
for m in re.findall(r'<script type="application/ld\+json">(.*?)</script>',s,re.S): json.loads(m)
print('ok',s.count('<figure'))
