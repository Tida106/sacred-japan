import re,csv,json
from PIL import Image
R='/home/claude/sacred-japan/'; A='/mnt/user-data/attachments/53e3d492-4bf8-5cd9-a0ec-63a7cbefb1d9/'
SL='kanazawa-castle'; D=R+f'guides/{SL}/images/'
import os; os.makedirs(D,exist_ok=True)
L={'S4':('CC BY-SA 4.0','https://creativecommons.org/licenses/by-sa/4.0/'),
   'S1':('CC BY-SA 1.0','https://creativecommons.org/licenses/by-sa/1.0/'),
   'B2':('CC BY 2.0','https://creativecommons.org/licenses/by/2.0/'),
   'SA2':('CC BY-SA 2.0','https://creativecommons.org/licenses/by-sa/2.0/'),
   'C0':('CC0 1.0','https://creativecommons.org/publicdomain/zero/1.0/'),
   'PD':('Public domain (released by the author)','https://commons.wikimedia.org/wiki/Template:PD-self')}
G1="rougher walls elsewhere in the park.</p>"
G2="so please check the schedule.</p>"
G3="that has never been rebuilt in timber.</p>"
R2="and GLTJP says the three buildings are wheelchair accessible.</p>"
P=[
('kahoku-first-gate','def454bf','そらみみ','S4',
 'A small tiled gate between white plaster walls with square openings, with a lawn beyond, snow banked at the side, and a tall white building on a stone base at the right',
 'The first gate of the Kahoku-mon, 20 January 2015.',
 "Commons titles this 金沢城河北門・一の門, the first gate of the Kahoku-mon, taken at 4:23 in the afternoon. A small tiled gate stands between white plaster walls with square openings, and beyond it you can see across to a lawn. At the right is a tall white building on a base of many-sided, tightly fitted stones. Patches of snow are banked at the edges, which is a reminder that the park is open in winter too. The Kahoku-mon is the gate Kanazawa Station says was rebuilt in 2010, as described above.",
 R2,False),
('kahoku-second-gate','f9f3015d','そらみみ','S4',
 'A long white gate building with a tiled roof on a sloped stone base, a green signboard in the foreground, and a wooden staircase at the right',
 'The second gate of the Kahoku-mon, 20 January 2015.',
 "Commons titles this 金沢城河北門・二の門, the second gate, taken a minute before the first-gate photo. A long white building with a tiled roof sits on a sloped base of fitted stones, with a wooden staircase at its right. The green signboard in the foreground reads &ldquo;Kahokumon Ninomon Gate,&rdquo; free admission, opening hours 9:00 to 16:30. That is what the sign said in 2015, so please confirm the current hours.",
 None,False),
('hashizume-gate','167c8e16','Benh LIEU SONG','SA2',
 'A large gate with black iron-banded pillars and doors made of vertical wooden bars, a tiled roof with round eave tiles above, and a paved path and trees beyond',
 'The Hashizume-mon, 19 October 2018.',
 "Commons describes this as the Hashizume-mon, the main gate of the Ninomaru area of Kanazawa Castle, taken on 19 October 2018. The doors and pillars are made of vertical wooden bars strapped with black iron, with round studs and decorative metal fittings, and the underside of the roof shows the timber frame in warm orange. Through the opening, a paved path climbs between lawns and pines. It is a good place to see how much of the rebuilt castle is craft detail.",
 None,False),
('cherry-turret-lantern','f513806a','Zairon','S4',
 'A white turret and wall behind a mass of cherry trees in bloom, with a stone lantern post standing in the right foreground',
 'Cherry blossoms in front of a turret, 9 April 2019.',
 "Commons titles this &ldquo;Cherry Blossom at Kanazawa Castle,&rdquo; taken at 9:15. A white turret and a patterned wall rise behind a mass of cherry trees in full bloom, and a stone lantern post stands in the right foreground. The turret looks like the Ishikawa Gate area to me, but Commons names only the castle. Bloom timing changes from year to year, so please treat 9 April as one year's example.",
 G1,False),
('cherry-bridge','3c5b9d93','Zairon','S4',
 'A wide stone bridge with pale green railings leading to a white turret and gate under an arch of cherry blossoms, with visitors on the bridge',
 'The bridge approach under cherry blossoms, 9 April 2019.',
 "Commons gives this the same title, taken at 9:15 as well. A wide stone bridge with pale green railings leads toward a white turret and a gate roof, and the cherry trees arch over the path beyond. The bridge looks like the one in the 2001 photo above, though Commons does not name it. Visitors are stopping to take pictures, which gives a sense of how popular the spot is in bloom.",
 None,False),
('cherry-wall-gate','916fd918','Zairon','S4',
 'A white turret and a gate roof rising above a high stone wall and a patterned white wall, framed by cherry trees in bloom and small signboards on a lawn',
 'The turret above the stone wall, framed by cherry trees, 9 April 2019.',
 "Taken at 9:09, the earliest of the three. A white turret and a gate roof rise above a long stone wall and a white wall with a grid of dark square tiles, framed by cherry trees. Small signboards stand on the lawn in front. Please read this one as an illustration of how the turret and the wall work together.",
 None,False),
('gyokusen-garden','4455ea3a','Abasaa (あばさー)','PD',
 'A garden of ponds, arched bridges and pine-covered islands seen from above, with a thatched-roof teahouse at the back and tall buildings beyond the trees',
 'Gyokusen\'inmaru Garden, 9 September 2016.',
 "Commons titles this Gyokusen Inmaru Garden, taken on 9 September 2016, and the author has released it into the public domain. Looking down from the slope, you see ponds with arched bridges, islands planted with pines, stepping paths, and a thatched-roof building at the back. Tall city buildings show above the trees, which is a reminder that the garden sits in the middle of Kanazawa. The garden was rebuilt in 2015 according to Visit Kanazawa, so this was taken about a year after.",
 G2,False),
('stone-wall-terraces','f932d266','Asanagi','C0',
 'Two tiers of stone wall, the lower made of rounded fitted stones and the upper of rougher angular stones, rising behind a lawn and trees',
 'Two tiers of stone wall, 29 September 2006.',
 "Commons titles this &ldquo;Stone wall of Kanazawa Castle,&rdquo; taken on 29 September 2006, and the photographer has dedicated it to the public domain. It shows two tiers of wall with different stonework: the lower tier uses rounded, closely fitted stones, and the upper tier looks rougher and more angular. This is the kind of difference Visit Kanazawa means when it says the walls vary across the site. The photo is from 2006, so the planting in front may have changed.",
 G3,False),
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
