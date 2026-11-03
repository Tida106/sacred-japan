import re,os,csv,json
from PIL import Image
R='/home/claude/sacred-japan/'; A='/mnt/user-data/attachments/49b96ec1-728b-5ea6-b8b2-6e6ae280fb4e/'
SL='kochi-castle'; D=R+f'guides/{SL}/images/'; os.makedirs(D,exist_ok=True)
S4=('CC BY-SA 4.0','https://creativecommons.org/licenses/by-sa/4.0/')
S3=('CC BY-SA 3.0','https://creativecommons.org/licenses/by-sa/3.0/')
B3=('CC BY 3.0','https://creativecommons.org/licenses/by/3.0/')
B4=('CC BY 4.0','https://creativecommons.org/licenses/by/4.0/')
C0=('CC0','https://creativecommons.org/publicdomain/zero/1.0/')

P=[
('palace-keep','596a7d84','Taisyo',S3,'Kochi Castle keep rising behind a tiled-roof wooden building with gables, gravel court and clipped pines under blue sky',
 'The keep and the tiled building in front of it, 20 May 2007 (Commons caption, translated).',
 "Here the keep and the low tiled building in front of it read as one cluster of roofs: white-plastered gables of different sizes overlap, and the keep rises behind them with its dark railed balcony. This is the closeness GLTJP and Wikipedia describe between the keep and the lord's palace. Commons titles the photo only as the keep, so I cannot confirm which part of the palace this is, though a sign at the entrance reads as a student-group entrance. A wooden post at the left carries the date 20 May 2007 in the Japanese era format, matching the photo date. The ticket area and visitors on the right show how busy the entrance can be."),
]
def fig(k,au,lic,alt,cap,w,h,hero=False):
    img=f'<picture><source srcset="/guides/{SL}/images/{k}.webp" type="image/webp"><img src="/guides/{SL}/images/{k}.jpg" alt="{alt}" width="{w}" height="{h}" loading="{"eager" if hero else "lazy"}" style="{"width:100%;max-height:420px;object-fit:cover;object-position:center 30%;border-radius:4px;display:block;" if hero else "width:100%;height:auto;border-radius:4px;display:block;"}"></picture>'
    fc=f'<figcaption style="font-size:13px;color:var(--enshu);margin-top:10px;text-align:center;line-height:1.6;">{cap}<br>Photo: {au}, <a href="{lic[1]}" target="_blank" rel="noopener" style="color:var(--enshu);">{lic[0]}</a>, via Wikimedia Commons (resized)</figcaption>'
    mw='max-width:760px;' if w>=h else 'max-width:420px;'
    return f'<figure style="{"margin:0 0 48px;" if hero else "margin:28px auto;"+mw}">{img}{fc}</figure>\n'

H={};rows=[]
for k,f,au,lic,alt,cap,ps in P:
    im=Image.open(A+f+'-image.jpg').convert('RGB'); print(k,im.size)
    if im.width>1200: im=im.resize((1200,round(im.height*1200/im.width)),Image.LANCZOS)
    im.save(D+k+'.jpg',quality=84,optimize=True); im.save(D+k+'.webp',quality=80)
    H[k]=fig(k,au,lic,alt,cap,im.width,im.height)+f'    <p>{ps}</p>\n'
    rows.append([f'guides/{SL}',f'/guides/{SL}/images/{k}.jpg',lic[0],lic[1],lic[1],f'{cap}Photo: {au}, {lic[0]}, via Wikimedia Commons (resized)'])
p=R+f'guides/{SL}/index.html'; s=open(p,encoding='utf-8').read()
def aft(s,a,t):
    assert s.count(a)==1,a; return s.replace(a,a+'\n'+t)
s=aft(s,'The same source says admission to the palace is included with the keep ticket.</p>',H['palace-keep'])
open(p,'w',encoding='utf-8').write(s)
import csv
with open(R+'PHOTO-CREDITS.csv','a',encoding='utf-8',newline='') as f:
    w=csv.writer(f,lineterminator='\r\n'); [w.writerow(r) for r in rows]
for tg in ['div','figure','picture','p','a','ul','li','details','section','h2']:
    assert len(re.findall(f'<{tg}[ >]',s))==len(re.findall(f'</{tg}>',s)),tg
for m in re.findall(r'<script type="application/ld\+json">(.*?)</script>',s,re.S): json.loads(m)
print('ok',s.count('<figure'))
