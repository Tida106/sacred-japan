import re, csv, os
from PIL import Image
R='/home/claude/sacred-japan/'; A='/mnt/user-data/attachments/fd332c08-3f6b-545a-883b-83277e19ff52/'
SL='kumamoto-castle'
L={'S2':('CC BY-SA 2.0','https://creativecommons.org/licenses/by-sa/2.0/'),'S4':('CC BY-SA 4.0','https://creativecommons.org/licenses/by-sa/4.0/'),'B3':('CC BY 3.0','https://creativecommons.org/licenses/by/3.0/'),'B4':('CC BY 4.0','https://creativecommons.org/licenses/by/4.0/'),'S3':('CC BY-SA 3.0','https://creativecommons.org/licenses/by-sa/3.0/'),'B2':('CC BY 2.0','https://creativecommons.org/licenses/by/2.0/'),'C0':('CC0 1.0','https://creativecommons.org/publicdomain/zero/1.0/')}
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
# before the walls section: pre-quake panorama
a=blk('prequake-wide','e21ca402','z tanuki','B3','A long stone wall with a turret rising behind it and a white car and a few people on a plaza in front','The Uto turret and its stone wall from the street side, 28 December 2014 (Commons: Kumamoto castle).',
 "This is the view that most people remember from before 2016: a tall turret standing on a long stone base, with an ordinary car park and street in front of it. It shows how large the walls are compared with the people and cars. The photo is from 2014, so the scene has changed since the earthquakes.")
before('<h2 id="walls">',a)
# walls
w=blk('walls-663','fcb67913','663highland','S3','A huge flared stone wall in the foreground with the black keep behind it and visitors walking along the gravel path','The curve of the wall with the keep behind it, 10 May 2009.',
 "This is the wall in action. The stones start with a gentle slope and then rise toward the vertical, and the keep sits well behind and above the visitors on the path. It was photographed in 2009, before the earthquakes, so some of these walls were later damaged and rebuilt.")
w+=blk('turrets-reggaeman','499f9822','Reggaeman','S3','A long two-storey white and black turret standing on a tall curved stone wall with trees behind','A turret on its stone base, 6 October 2012 (Commons: Yonken-yagura (left) and Gennoshin-yagura).',
 "The Commons description names two turrets, the Yonken-yagura on the left and the Gennoshin-yagura, both Important Cultural Properties, so I treat this as one of that pair. Look at the dark boards and small openings under the white plaster: these were designed for defenders to fire from. The image is from 2012, before the earthquakes.")
w+=blk('turret-smiley','cec056c7','Smiley.toerist','S4','A turret with white plaster and dark timber boards on a tall stone base, with green trees and a bus-stop sign in the foreground','A turret on a stone base photographed on 27 May 2024 (Commons: Kasteeltoren van de Kumamotokasteel).',
 "This is a more recent view, from May 2024. The tall stone base and the timber-clad turret above it show the castle's typical profile, and the green fencing and the bus-stop sign at the bottom show that this is a visitor route. The Commons description only says it is a castle tower, so I do not name the turret.")
before('<h2 id="quake">',w)
# quake
q=blk('uto-damaged','0ba55d36','Drivephotographer','C0','A damaged turret standing on a corner of a stone wall under heavy grey clouds, with wire netting over part of the wall','The Uto turret after the 2016 earthquakes, 29 December 2021 (Commons: Kumamoto Castle Udo turret).',
 "This is the turret that became the symbol of the damage. The turret sits on a narrow corner of stone, with netting over the wall at the right and some plaster missing from the walls. Commons calls it the Udo turret, which is the Uto turret in my text. The photo is from December 2021, and the situation may have changed since.")
q+=blk('damage-hyppolyte','b5e05e24','Hyppolyte de Saint-Rambert','B4','A tall dark stone wall with the keep and a long tiled building above it and a bare plum garden below on an overcast day','The walls and buildings near the keep, 15 January 2026 (Commons: iconography related to damage from the 2016 earthquake).',
 "The Commons description for this image mentions the damage from the 2016 earthquake. What you can see are the high stone walls, the keep and a long tiled building above them, and a bare garden of trees below. Several parts of the walls here appear to have been rebuilt or repaired, but I cannot confirm which. This is from January 2026, six months before the July earthquake.")
before('<h2 id="again">',q)
# restoration
r=blk('ginkgo-scaffold','b56fa545','Totti','S4','Golden ginkgo leaves beside the black keep, with scaffolding on the base and green fences in front of the visitors','The keep behind golden ginkgo leaves, with scaffolding at the base, 28 November 2020.',
 "Autumn colour and repair work in the same frame: the golden ginkgo stands beside the keep, while scaffolding and green fencing show that restoration was still going on in 2020. Commons describes the photo only as a ginkgo and Kumamoto Castle. I include it because it is exactly the kind of view the tour route gives you.")
r+=blk('keep-plaza-2026','424e0e61','Hyppolyte de Saint-Rambert','B4','The black keep with grey roof tiles and a small keep beside it across a stone plaza, with two fish-shaped roof ornaments and a bench in the foreground','The restored keep from the plaza, 15 January 2026 (Commons: au chateau de Kumamoto).',
 "This is the keep as it looked in January 2026. The two fish-shaped roof ornaments in the foreground are shachihoko, the same kind of ornament that was installed on the keep in 2018, and the plaque at the bottom reads &ldquo;Yomigaeru Kumamoto-jo&rdquo;, or roughly &ldquo;Kumamoto Castle Revives&rdquo;. All of this is before the July 2026 earthquake, so check the current state before you plan around it.")
r+=blk('interior-glow','deca83dd','Hyppolyte de Saint-Rambert','B4','A dim traditional hall seen through dark wooden pillars, with gold-leaf sliding screens painted with green pine branches','A gold-screen room seen through the pillars, 15 January 2026 (Commons: au chateau de Kumamoto).',
 "A gold-leaf room with pine painted on the screens, lit from inside and seen through dark pillars. The Commons description names only the castle, so I cannot say which building this is. It is a good reminder that the restoration covers painted interiors as well as stone walls.")
before('<h2 id="visit">',r)
# visit: spring
v=blk('cherry-sta','1c052591','STA3816','S3','A black turret above a curved stone wall seen through cherry blossoms against a blue sky','Cherry blossoms at the castle, 31 March 2011 (Commons: Cherry blossoms at Kumamoto Castle).',
 "Late March to early April is the time for cherry blossoms, and this photo shows them with the turret and the curved wall behind. It was taken in 2011 and is a reminder of the season, not of the current layout, since the walls here have been repaired in the years since.")
before('<h2 id="stay">',v)
assert s.count('"dateModified": "2026-11-01"')<=1
s=s.replace('"dateModified": "2026-11-01"','"dateModified": "2026-11-05"')
open(p,'w',encoding='utf-8').write(s)
with open(R+'PHOTO-CREDITS.csv','a',encoding='utf-8',newline='') as fh: csv.writer(fh,lineterminator='\r\n').writerows(rows)
print(len(rows))
for tg in ['div','figure','picture','p','a','ul','li','details','section','h2']:
    assert len(re.findall(f'<{tg}[ >]',s))==len(re.findall(f'</{tg}>',s)),tg
import json
for m in re.finditer(r'<script type="application/ld\+json">(.*?)</script>',s,re.S): json.loads(m.group(1))
print('ok')
