import re,csv,json
from PIL import Image
R='/home/claude/sacred-japan/'; A='/mnt/user-data/attachments/53e3d492-4bf8-5cd9-a0ec-63a7cbefb1d9/'
SL='kanazawa-castle'; D=R+f'guides/{SL}/images/'
import os; os.makedirs(D,exist_ok=True)
L={'S4':('CC BY-SA 4.0','https://creativecommons.org/licenses/by-sa/4.0/'),
   'S1':('CC BY-SA 1.0','https://creativecommons.org/licenses/by-sa/1.0/'),
   'B2':('CC BY 2.0','https://creativecommons.org/licenses/by/2.0/'),
   'SA2':('CC BY-SA 2.0','https://creativecommons.org/licenses/by-sa/2.0/'),
   'B4':('CC BY 4.0','https://creativecommons.org/licenses/by/4.0/'),
   'C0':('CC0 1.0','https://creativecommons.org/publicdomain/zero/1.0/'),
   'PD':('Public domain (released by the author)','https://commons.wikimedia.org/wiki/Template:PD-self')}
P=[
('night-gate-bridge','c83fc190','くろふね','B4',
 'A two-storey tiled gate building lit from within by orange lattice windows at night, at the end of a wooden bridge with glass side panels and low lights along its edges',
 'A gate and wooden bridge lit at night, 5 November 2022.',
 "Commons titles this only &ldquo;夜の金沢城,&rdquo; night Kanazawa Castle, taken at 6:55 in the evening on 5 November 2022. A two-storey gate with a grid of dark square tiles glows from inside through its lattice windows, and a wooden bridge with glass side panels and low lights leads up to it. The gate and bridge look like the Nezumi-mon and its bridge, which GLTJP says were rebuilt in 2020, but that is my reading and Commons does not say so. A few visitors are walking through the gate. Evening lighting varies by date, so please check the schedule above.",
 "how much of the rebuilt castle is craft detail.</p>",False),
]
def mk(k,f,au,lic,alt,cap,hero,small):
    im=Image.open(A+f+'-image.jpg').convert('RGB')
    if im.width>1200: im=im.resize((1200,round(im.height*1200/im.width)),Image.LANCZOS)
    im.save(D+k+'.jpg',quality=84,optimize=True); im.save(D+k+'.webp',quality=80)
    l=L[lic]; ld='eager' if hero else 'lazy'
    st=('width:100%;max-height:420px;object-fit:cover;object-position:center 30%;border-radius:4px;display:block;' if hero else 'width:100%;height:auto;border-radius:4px;display:block;')
    img=f'<picture><source srcset="/guides/{SL}/images/{k}.webp" type="image/webp"><img src="/guides/{SL}/images/{k}.jpg" alt="{alt}" width="{im.width}" height="{im.height}" loading="{ld}" style="{st}"></picture>'
    fc=f'<figcaption style="font-size:13px;color:var(--enshu);margin-top:10px;text-align:center;line-height:1.6;">{cap}<br>Photo: {au}, <a href="{l[1]}" target="_blank" rel="noopener" style="color:var(--enshu);">{l[0]}</a>, via Wikimedia Commons (resized)</figcaption>'
    return im,l,img,fc
p=R+f'guides/{SL}/index.html'; s=open(p,encoding='utf-8').read()
groups=[]
for t in P:
    if t[7] is None: groups[-1].append(t)
    else: groups.append([t])
rows=[];sizes={}
for g in groups:
    html=''
    for (k,f,au,lic,alt,cap,para,anc,small) in g:
        hero=False
        im,l,img,fc=mk(k,f,au,lic,alt,cap,hero,small); sizes[k]=im.size
        if False: pass
        else:
            mw='420px' if im.height>im.width else '760px'
            html+=f'\n    <figure style="margin:28px auto;max-width:{mw};">{img}{fc}</figure>\n    <p>{para}</p>'
        rows.append([f'guides/{SL}',f'/guides/{SL}/images/{k}.jpg',l[0],l[1],l[1],re.sub('&amp;','&',cap)+f' Photo: {au}, {l[0]}, via Wikimedia Commons (resized)'])
    anc=g[0][7]
    if anc=='HERO':
        a='  <!-- TABLE OF CONTENTS -->'; assert s.count(a)==1; s=s.replace(a,html+a)
    else:
        assert s.count(anc)==1,anc; s=s.replace(anc,anc+html)
open(p,'w',encoding='utf-8').write(s)
with open(R+'PHOTO-CREDITS.csv','a',encoding='utf-8',newline='') as fh:
    w=csv.writer(fh,lineterminator='\r\n')
    for r in rows: w.writerow(r)
for tg in ['div','figure','picture','p','a','ul','li','details','section','h2']:
    assert len(re.findall(f'<{tg}[ >]',s))==len(re.findall(f'</{tg}>',s)),tg
for m in re.findall(r'<script type="application/ld\+json">(.*?)</script>',s,re.S): json.loads(m)
print('ok',s.count('<figure'),sizes)
