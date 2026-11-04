import re,csv,json,os
from PIL import Image
R='/home/claude/sacred-japan/'; A='/mnt/user-data/attachments/53e3d492-4bf8-5cd9-a0ec-63a7cbefb1d9/'
SL='shuri-castle'; D=R+f'guides/{SL}/images/'; os.makedirs(D,exist_ok=True)
L={'B2':('CC BY 2.0','https://creativecommons.org/licenses/by/2.0/'),
   'S4':('CC BY-SA 4.0','https://creativecommons.org/licenses/by-sa/4.0/'),
   'S3':('CC BY-SA 3.0','https://creativecommons.org/licenses/by-sa/3.0/'),
   'B3':('CC BY 3.0','https://creativecommons.org/licenses/by/3.0/'),
   'B4':('CC BY 4.0','https://creativecommons.org/licenses/by/4.0/')}
SEE2="were largely untouched by the fire.</p>"
ZU="so please check on site.</p>"
P=[
(SEE2,[('sonohyan-utaki','ddfc9dfa','663highland','S3','A pale limestone gate with closed wooden double doors set in dark stone walls, topped by a carved stone roof with ornaments along the ridge, beside a paved road','Sonohyan-utaki Stone Gate, uploaded June 2011.',
 "Commons gives only &ldquo;at Shuri Castle&rdquo; as the description, and this is the Sonohyan-utaki Stone Gate described above, from the road side. The doors are shut, which fits K005 Powerspot's point that it is a gate for prayer, not a passageway. The pale limestone frame, the dark walls on either side and the carved stone roof with ornaments along its ridge make it quite different from the red timber gates elsewhere in the park. The upload is from June 2011, so details around it may have changed."),
 ('sonohyan-utaki-sign','c9f61388','Xiquinho Silva (xiquinhosilva)','B2','The Sonohyan-utaki Stone Gate in bright sun beside a black World Heritage plaque with Japanese and English text, with small information plates on a stone block in front','The Stone Gate and its World Heritage plaque, 5 August 2018.',
 "Commons dates this to 5 August 2018 and describes it as the World Heritage monument of the Sonohyan-utaki Stone Gate. The black plaque on the left is a UNESCO World Heritage marker in Japanese and English, naming the &ldquo;Sonohyan-utaki Ishimon (Stone Gate of the Sonohyan Shrine)&rdquo; and, as far as I can read it, recording its inscription in December 2000 as part of the Gusuku Sites and Related Properties of the Kingdom of Ryukyu. Smaller information plates stand on the stone block in front. The photo carries the photographer's name as a watermark.")]),
(ZU,[('zuisen-wall-cycads','ccdc7bd7','そらみみ (Soramimi)','S4','A long curved grey limestone wall rising above a slope of cycad plants and a path with visitors, with the red upper part of a gate showing above the wall','The wall and cycads in front of Zuisen Gate, 15 March 2015.',
 "The Japanese caption on Commons reads &ldquo;the castle wall and cycads in front of Zuisen Gate (Hikawa-gomon).&rdquo; This is the view that explains why the wall matters: a long, curving face of grey limestone, with the red roof of the gate peeking out above it, and a slope of cycads below. Visitors on the path on the left show how large the wall is. I find this slope as memorable as any of the buildings."),
 ('usai-gate','fd4ed6db','そらみみ (Soramimi)','S4','A red gate with a small tiled roof and a dark signboard at the end of a stone-topped wall walkway, with two people standing in its opening','A small red gate at the end of a wall walkway, 15 March 2015.',
 "Commons describes this as the wall seen from in front of Kofukumon Gate, with the gate it labels 右掖門 (the Japanese caption adds &ldquo;よそへちの御門&rdquo;). A narrow stone-topped walkway runs along the wall toward a small red gate with a tiled roof and a dark signboard, and two people stand in its opening. The sky is cloudy and the photo is from 2015, so I have not checked whether the walkway is open today."),
 ('wall-city-view','276ddc24','そらみみ (Soramimi)','S4','A view over the stone walls and two small gates with orange roofs toward the city of Naha, with the sea faintly visible on the horizon','The walls and Naha beyond, 15 March 2015.',
 "Commons describes this as the castle wall and the Naha cityscape seen from in front of Kofukumon Gate. From the top of the wall, a ribbon of grey stone curves around a patch of lawn, two small gates with orange roofs sit at either end, and the city of Naha spreads out below with the sea on the horizon. It shows why this hill was chosen for a palace: it looks over the city and the water.")]),
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
