import re,csv,json
from PIL import Image
R='/home/claude/sacred-japan/'; A='/mnt/user-data/attachments/53e3d492-4bf8-5cd9-a0ec-63a7cbefb1d9/'
SL='kanazawa-castle'; D=R+f'guides/{SL}/images/'
import os; os.makedirs(D,exist_ok=True)
L={'S4':('CC BY-SA 4.0','https://creativecommons.org/licenses/by-sa/4.0/'),
   'S1':('CC BY-SA 1.0','https://creativecommons.org/licenses/by-sa/1.0/'),
   'B2':('CC BY 2.0','https://creativecommons.org/licenses/by/2.0/')}
G1="so I would not give a single date for the Nagaya.</p>"
R1="and that the work followed traditional methods based on original plans.</p>"
R2="and GLTJP says the three buildings are wheelchair accessible.</p>"
P=[
('hero-cherry-corner','64317865','Zairon','S4',
 'A white turret with layered tiled roofs rising from a sloping stone wall beside a moat, with cherry trees in bloom along the path on the right',
 'A turret rising from the stone wall beside the moat, with cherry trees in bloom. Commons titles it Higashi Yagura of Kanazawa Castle &amp; Cherry Blossom, 9 April 2019.',None,'HERO',False),
('ishikawa-bridge-2001','6c9d6ee9','Kagaland (WT-shared, via Wikivoyage)','S1',
 'A curved bridge with a green lamp post and pink flowers along the railing, leading to a white turret on a stone wall and a gabled gate roof beyond',
 'The approach to the Ishikawa Gate, 4 October 2001.',
 "Commons titles this simply &ldquo;Ishikawa Gate, Kanazawa Castle.&rdquo; It was taken in October 2001, around the time the rebuilding described below was finishing, and it came to Commons from Wikivoyage. A bridge with a green lamp post leads toward a white turret on a stone wall at the left and a gabled gate roof at the back. The pink flowers along the railing look like cosmos, though that is my reading. This is a small 1280 by 960 photo that is more than twenty years old, so please expect the planting and fittings to have changed.",
 G1,True),
('first-gate','8eccdf96','Zairon','S4',
 'A black timber gate with white plaster walls patterned with dark square tiles, a cherry tree in full bloom at the right, and a visitor walking away through the opening',
 'The first gate of the castle, 9 April 2019.',
 "Commons labels this &ldquo;First Gate Kanazawa Castle,&rdquo; taken at 9:16 in the morning. A black timber gate stands between white plaster walls set with a grid of dark square tiles, and a visitor walks away through the opening in the sun. The cherry tree at the right is in full bloom. I read this as the outer gate on the way in, but I am going by the Commons label.",
 None,False),
('ishikawa-gate','4d4dc42c','Zairon','S4',
 'A large black gate with round metal studs on its heavy pillars, a white upper storey with slit windows, a tiled roof, and a small information building visible through the opening',
 'The Ishikawa Gate, 9 April 2019.',
 "Commons labels this &ldquo;Ishikawa Gate of Kanazawa Castle,&rdquo; and it was taken about a minute after the first-gate photo above. The gate is black timber with round metal studs on its heavy pillars, under a white upper floor with slit windows and a tiled roof. Through the opening you can see a small building that appears to be an information office, with a few visitors beside it. The stone blocks at both sides are cut and fitted tightly, which is a good contrast with the rougher walls elsewhere in the park.",
 None,False),
('higashi-yagura-wide','6ed7b630','Zairon','S4',
 'A long white turret-and-storehouse building with a layered-roof turret at its left end, standing behind a wide paved plaza under a blue sky, with cherry blossoms along the horizon',
 'A long white building with a turret at one end, 9 April 2019.',
 "Commons labels this &ldquo;Higashi Yagura of Kanazawa Castle,&rdquo; taken at 9:30. A long white building with a layered turret at the left end stands beyond a wide, open plaza, with pines and cherry blossoms along the horizon. A sign marked 入口 stands near the building's entrance. I am following the Commons label for the name, and I have not matched it to the building names in my sources, so please read this as an illustration of the rebuilt turret-and-storehouse group.",
 R1,False),
('higashi-yagura-close','038dc677','Zairon','S4',
 'The same long white building seen close up, with a three-tier turret, a grid of black and white tiles on the lower wall, and layered grey roofs under a cloudy sky',
 'The turret and long wall up close, 9 April 2019.',
 "Commons labels this one Higashi Yagura as well, taken three minutes after the wide view. Up close you can see the layered grey roofs, the slit windows and the grid of dark square tiles on the lower wall. A single visitor walks along the base, which gives a sense of scale for a building of this length.",
 None,False),
('hishi-window','a6451dde','Andrea Schaffer','B2',
 'A projecting lattice window under a curved gable with a flower crest, set in a wall of dark square tiles on white plaster, with round eave tiles along the roof',
 'A projecting window under a curved gable, 27 July 2009.',
 "Commons gives the Japanese title 金沢城・菱櫓, meaning the Hishi Yagura, the turret the city rebuilt in 1999 to 2001. The photo shows a projecting lattice window under a curved gable, with a flower crest on the ridge tile and on the round eave tiles. The five-petal mark looks like the plum-blossom crest associated with the Maeda family, but Commons does not say so. The wall below is the same grid of dark square tiles on white plaster you see across the complex.",
 None,False),
('yagura-interior','694e9c69','Zairon','S4',
 'A long timber hall with exposed beams, a wide plank floor lit in patches by small windows, and a few display stands and a visitor in the distance',
 'Inside a turret, 9 April 2019.',
 "Commons labels this &ldquo;Interior of the Higashi Yagura,&rdquo; taken at 9:43. It is a long timber hall with exposed beams, a wide plank floor, and rows of small windows that throw patches of light across the boards. Small display stands and a screen stand along the walls, and a visitor is in the distance. I cannot tell from Commons which building this is, so please take it as the kind of space the rebuilt interiors offer.",
 R2,False),
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
        hero=(k.startswith('hero'))
        im,l,img,fc=mk(k,f,au,lic,alt,cap,hero,small); sizes[k]=im.size
        if hero: html=f'  <figure style="margin:0 0 48px;">{img}{fc}</figure>\n\n'
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
