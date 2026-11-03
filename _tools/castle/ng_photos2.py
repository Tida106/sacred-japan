import re,os,csv,json,sys
sys.path.insert(0,'/home/claude/sacred-japan/_tools/castle')
from PIL import Image
R='/home/claude/sacred-japan/'; A='/mnt/user-data/attachments/53e3d492-4bf8-5cd9-a0ec-63a7cbefb1d9/'
SL='nagoya-castle'; D=R+f'guides/{SL}/images/'
S4=('CC BY-SA 4.0','https://creativecommons.org/licenses/by-sa/4.0/')
C0=('CC0','https://creativecommons.org/publicdomain/zero/1.0/')
def fig(k,au,lic,alt,cap,w,h):
    img=f'<picture><source srcset="/guides/{SL}/images/{k}.webp" type="image/webp"><img src="/guides/{SL}/images/{k}.jpg" alt="{alt}" width="{w}" height="{h}" loading="lazy" style="width:100%;height:auto;border-radius:4px;display:block;"></picture>'
    fc=f'<figcaption style="font-size:13px;color:var(--enshu);margin-top:10px;text-align:center;line-height:1.6;">{cap}<br>Photo: {au}, <a href="{lic[1]}" target="_blank" rel="noopener" style="color:var(--enshu);">{lic[0]}</a>, via Wikimedia Commons (resized)</figcaption>'
    mw='max-width:760px;' if w>=h else 'max-width:420px;'
    return f'<figure style="margin:28px auto;{mw}">{img}{fc}</figure>\n'
P=[
('palace','90613208','Mauricio V. Genta',S4,
 'A timber porch of a reconstructed palace with a curved dark shingle roof, red-brown beams and gold fittings, visitors walking on the gravel in front',
 'A porch of the palace buildings, 27 August 2023 (Commons: Castillo de Nagoya).',
 "This looks like the entrance porch of the Honmaru Palace, though Commons labels it only as Nagoya Castle. The roof sweeps in a deep curve over red-brown timber and white plaster panels, and black beams carry gold fittings with a three-leaf crest that resembles the Tokugawa hollyhock, which Commons does not confirm. Low bamboo-style barriers keep visitors off the stone step, and a stripe of pale pavement leads in. It is a good sign of how fresh the reconstruction is, because the wood has not yet weathered to grey."),
('keep-close','482f9244','Syced',C0,
 'Close view of the Nagoya Castle keep with tiers of green copper roofs, dark gables, barred windows and two golden shachi on the top roof',
 'The keep and its two golden shachi up close (Commons: Nagoya castle, a stitched image; the date given is the placeholder 1 January 1970).',
 "Here you can count the tiers and see why the keep photographs so well. Green copper roofs step upward, each tier with dark gables, and the barred windows sit in rows on the white walls. The two gold shachi stand at the ends of the top ridge. The lowest roof is covered in grey tiles rather than green copper. A plain pale structure at the lower right is attached to the keep and looks like a later addition, in keeping with the concrete rebuild, and bare branches at the bottom suggest early spring."),
]
H={};rows=[]
for k,f,au,lic,alt,cap,ps in P:
    im=Image.open(A+f+'-image.jpg').convert('RGB')
    if im.width>1200: im=im.resize((1200,round(im.height*1200/im.width)),Image.LANCZOS)
    im.save(D+k+'.jpg',quality=84,optimize=True); im.save(D+k+'.webp',quality=80)
    H[k]=fig(k,au,lic,alt,cap,im.width,im.height)+f'    <p>{ps}</p>\n'
    rows.append([f'guides/{SL}',f'/guides/{SL}/images/{k}.jpg',lic[0],lic[1],lic[1],f'{cap}Photo: {au}, {lic[0]}, via Wikimedia Commons (resized)'])
p=R+f'guides/{SL}/index.html'; s=open(p,encoding='utf-8').read()
def aft(s,a,t):
    assert s.count(a)==1,a; return s.replace(a,a+'\n'+t)
s=aft(s,'with no flash or tripod.</p>',H['palace'])
s=aft(s,'it is the building that has been closed since 2018.</p>',H['keep-close'])
open(p,'w',encoding='utf-8').write(s)
with open(R+'PHOTO-CREDITS.csv','a',encoding='utf-8',newline='') as f:
    w=csv.writer(f,lineterminator='\r\n'); [w.writerow(r) for r in rows]
for tg in ['div','figure','picture','p','a','ul','li','details','section','h2']:
    assert len(re.findall(f'<{tg}[ >]',s))==len(re.findall(f'</{tg}>',s)),tg
for m in re.findall(r'<script type="application/ld\+json">(.*?)</script>',s,re.S): json.loads(m)
print('ok',s.count('<figure'))
