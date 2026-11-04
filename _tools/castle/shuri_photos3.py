import re,csv,json,os
from PIL import Image
R='/home/claude/sacred-japan/'; A='/mnt/user-data/attachments/53e3d492-4bf8-5cd9-a0ec-63a7cbefb1d9/'
SL='shuri-castle'; D=R+f'guides/{SL}/images/'; os.makedirs(D,exist_ok=True)
L={'B2':('CC BY 2.0','https://creativecommons.org/licenses/by/2.0/'),
   'S4':('CC BY-SA 4.0','https://creativecommons.org/licenses/by-sa/4.0/'),
   'S3':('CC BY-SA 3.0','https://creativecommons.org/licenses/by-sa/3.0/'),
   'B3':('CC BY 3.0','https://creativecommons.org/licenses/by/3.0/'),
   'B4':('CC BY 4.0','https://creativecommons.org/licenses/by/4.0/')}
FIRE="so I will not give one.</p>"
P=[
(FIRE,[('seiden-before-fire','f747b1b6','CEphoto, Uwe Aranas','S3','The front of the red main hall with its curved gabled entrance porch, gold and green dragon ornaments on the roof ridge, grey dragon pillars beside the stairs and a red and white striped courtyard in front','The main hall before the 2019 fire, January 2016.',
 "Commons describes this only as the palace building of Shuri Castle and dates it to 5 January 2016. I take it to be the main hall as it stood before the 2019 fire, from the dragon ornaments on the ridge, the curved entrance porch and the red and white striped courtyard in front. Grey dragon pillars flank the stairs. This is the building that was destroyed in 2019 and has been rebuilt, so the new hall should look similar from the front, but I cannot say how closely, so please treat this as a picture of the earlier building.")]),
]
rows=[];sizes={}
def mk(k,f,au,lic,alt,cap,hero):
    im=Image.open(A+f+'-image.jpg').convert('RGB')
    if im.width>1200: im=im.resize((1200,round(im.height*1200/im.width)),Image.LANCZOS)
    im.save(D+k+'.jpg',quality=84,optimize=True); im.save(D+k+'.webp',quality=80)
    l=L[lic]; ld='eager' if hero else 'lazy'
    st=('width:100%;max-height:420px;object-fit:cover;object-position:center 30%;border-radius:4px;display:block;' if hero else 'width:100%;height:auto;border-radius:4px;display:block;')
    img=f'<picture><source srcset="/guides/{SL}/images/{k}.webp" type="image/webp"><img src="/guides/{SL}/images/{k}.jpg" alt="{alt}" width="{im.width}" height="{im.height}" loading="{ld}" style="{st}"></picture>'
    fc=f'<figcaption style="font-size:13px;color:var(--enshu);margin-top:10px;text-align:center;line-height:1.6;">{cap}<br>Photo: {au}, <a href="{l[1]}" target="_blank" rel="noopener" style="color:var(--enshu);">{l[0]}</a>, via Wikimedia Commons (resized)</figcaption>'
    sizes[k]=im.size
    rows.append([f'guides/{SL}',f'/guides/{SL}/images/{k}.jpg',l[0],l[1],l[1],cap+f' Photo: {au}, {l[0]}, via Wikimedia Commons (resized)'])
    return img,fc
p=R+f'guides/{SL}/index.html'; s=open(p,encoding='utf-8').read()
merged={}
for anc,g in P: merged.setdefault(anc,[]).extend(g)
for anc,g in merged.items():
    html=''
    for (k,f,au,lic,alt,cap,para) in g:
        img,fc=mk(k,f,au,lic,alt,cap,False)
        mw='420px' if sizes[k][1]>sizes[k][0] else '760px'
        html+=f'\n    <figure style="margin:28px auto;max-width:{mw};">{img}{fc}</figure>\n    <p>{para}</p>'
    assert s.count(anc)==1,anc; s=s.replace(anc,anc+html)
open(p,'w',encoding='utf-8').write(s)
with open(R+'PHOTO-CREDITS.csv','a',encoding='utf-8',newline='') as fh:
    w=csv.writer(fh,lineterminator='\r\n')
    for r in rows: w.writerow(r)
for tg in ['div','figure','picture','p','a','ul','li','details','section','h2']:
    assert len(re.findall(f'<{tg}[ >]',s))==len(re.findall(f'</{tg}>',s)),tg
for m in re.findall(r'<script type="application/ld\+json">(.*?)</script>',s,re.S): json.loads(m)
print('ok',s.count('<figure'),sizes)
