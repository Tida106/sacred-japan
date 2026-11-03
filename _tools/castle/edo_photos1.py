import re,csv,json
from PIL import Image
R='/home/claude/sacred-japan/'; A='/mnt/user-data/attachments/53e3d492-4bf8-5cd9-a0ec-63a7cbefb1d9/'
SL='edo-castle'; D=R+f'guides/{SL}/images/'
S4=('CC BY-SA 4.0','https://creativecommons.org/licenses/by-sa/4.0/')
S3=('CC BY-SA 3.0','https://creativecommons.org/licenses/by-sa/3.0/')
B2=('CC BY 2.0','https://creativecommons.org/licenses/by/2.0/')
PD=('Public domain','https://commons.wikimedia.org/wiki/Template:PD-self')
# key, file, author, lic, alt, caption, para, group
P=[
('hero','0bc1fc6f','Another Believer',S4,'A white three-story turret with dark tiled roofs and a curved gable, standing on a high dry-stone wall under a clear blue sky','A three-story turret on a stone base, 29 November 2019 (Commons title: Tokyo, 2019).',None,'hero'),
('fujimi-low','836fb1b9','Fg2',PD,'A white turret with three layers of dark roofs seen from below, rising from a wall of dark stone, with pine branches at the left','The turret seen from lower down, 24 December 2005 (Commons: Turret of Edo Castle).',
 "This is the same kind of tower from lower on the slope, and it shows what the stone base does. It takes up nearly half the frame, with the white plaster walls stepping back above it under three layers of dark roofs and a curved gable on the middle level. Wikipedia lists a three-story turret, Fujimi-yagura, among the surviving structures, and the building in the photo at the top of this page and this one look like that tower. Commons titles them only as a turret, though, so check the sign on site before naming it.",'survives'),
('hyakunin','a4dd15aa','Celuici',S3,'A long low wooden guardhouse with two tiers of gray tile roof and dark wooden walls, behind a low fence and a gravel yard, with glass office towers beyond','Hyakunin Bansho Guardhouse, 20 May 2017 (Commons title).',
 "Commons calls this the Hyakunin Bansho, a name that means roughly a hundred-person guardhouse. It is one of the three guardhouses GLTJP counts in the East Gardens. The building is very long and low, with two tiers of gray tile roofing over dark timber walls and a few white plaster panels, and a low fence keeps you back from it across the raked gravel. The glass towers behind it make the point of this whole place: a guard post of the shogun's government with a modern business district rising above its roof.",'survives'),
('garden-pano','8b0f1e28','Don Ramey Logan',S4,'A wide view across a still pond with a small wooden bridge, a stone lantern on a gravel shore, trimmed hedges and pines, and an orange and pink sunset sky reflected in the water','A pond garden with a bridge and lantern (Commons file uploaded 22 May 2022).',
 "This is the kind of scene I mean by a place to sit after the stone. A small wooden bridge crosses the left side of the pond, a stone lantern stands on a gravel shore at the right, and clipped hedges and pines run along the far bank. Commons did not show me a description for this file, so I cannot tell you which part of the gardens it is, and the sunset colors look strongly enhanced, so expect something calmer in person.",'garden'),
('garden-pond','ee9c789c','Guilhem Vellut',B2,'A dark pond with water lilies in front of dense green trees, pink and white flowering shrubs and a vine-covered wooden shelter on the far bank','The garden pond in summer, 14 August 2013 (Commons: Imperial Palace East Garden).',
 "In mid-August the same kind of pond garden is all green. Pink and white flowering shrubs, which I take to be crape myrtle, stand out on the far bank next to a vine-covered shelter, and water lilies float on the surface in front. It is a reminder that the gardens change with the season, and that the stone ruins are only half of the reason to come.",'garden'),
('pine-road','7c3584f7','Guilhem Vellut',B2,'A wide paved path between tall pines in autumn, with a stone wall at the left, a few visitors in the distance and office towers beyond','A path lined with pines, 26 November 2013 (Commons: Imperial Palace East Garden @ Tokyo).',
 "Late November is a useful test of what to expect. This broad path runs between tall pines, with an angled stone wall at the left, and a few orange maples at the far end are the only strong autumn color. Most of what you see is evergreen, which is why I describe the East Gardens as a place for stone, space and quiet rather than for peak foliage.",'visit'),
('gate-aerial','026cd2a5','WPPilot',S3,'Aerial view of a bridge crossing a moat to a gateway with white walls and a gray tile roof, with an inner gate and a guard hut, surrounded by trees','A bridge over the moat to a gate with a white-walled enclosure (Commons file uploaded 20 November 2020).',
 "From above you can see how a castle gate was built to be hard to rush. A single causeway crosses the moat, and instead of leading straight in, it ends at a small outer gate and a walled square, with the main gatehouse set off at an angle along the right-hand wall. Commons did not show me the name of the gate in this file, so I will not guess, but the East Gardens' gates share this kind of layout. The photo is credited to the uploader, WPPilot, who marked it as their own work.",'visit'),
('gate-skyline','a9b78643','Don Ramey Logan',S4,'A tiled gatehouse and white walls across a moat, with tour groups on the bridge in front of them and Tokyo office towers rising behind','A gate and bridge, with the city behind (Commons file uploaded 3 September 2022).',
 "Here the setting is wider. A gatehouse with a gray tile roof and white walls sits at the end of a bridge, a long line of visitors is crossing it, and the office towers of the city rise right behind the trees. Commons did not give me the name of the gate here either. I include it because this contrast is the real experience of the East Gardens: you enter through the old gate and the modern city is still in view.",'visit'),
]
def fig(k,au,lic,alt,cap,w,hero,im):
    img=f'<picture><source srcset="/guides/{SL}/images/{k}.webp" type="image/webp"><img src="/guides/{SL}/images/{k}.jpg" alt="{alt}" width="{im.width}" height="{im.height}" loading="{"eager" if hero else "lazy"}" style="width:100%;{"max-height:420px;object-fit:cover;object-position:center 40%;" if hero else "height:auto;"}border-radius:4px;display:block;"></picture>'
    fc=f'<figcaption style="font-size:13px;color:var(--enshu);margin-top:10px;text-align:center;line-height:1.6;">{cap}<br>Photo: {au}, <a href="{lic[1]}" target="_blank" rel="noopener" style="color:var(--enshu);">{lic[0]}</a>, via Wikimedia Commons (resized)</figcaption>'
    return img,fc
p=R+f'guides/{SL}/index.html'; s=open(p,encoding='utf-8').read()
blocks={'survives':'','garden':'','visit':''}; hero=''
rows=[]
for k,f,au,lic,alt,cap,ps,g in P:
    im=Image.open(A+f+'-image.jpg').convert('RGB')
    if im.width>1200: im=im.resize((1200,round(im.height*1200/im.width)),Image.LANCZOS)
    im.save(D+k+'.jpg',quality=84,optimize=True); im.save(D+k+'.webp',quality=80)
    img,fc=fig(k,au,lic,alt,cap,760,g=='hero',im)
    if g=='hero': hero=f'<figure style="margin:0 0 48px;">{img}{fc}</figure>\n\n'
    else: blocks[g]+=f'\n    <figure style="margin:28px auto;max-width:760px;">{img}{fc}</figure>\n    <p>{ps}</p>'
    rows.append([f'guides/{SL}',f'/guides/{SL}/images/{k}.jpg',lic[0],lic[1],lic[1],cap+f' Photo: {au}, {lic[0]}, via Wikimedia Commons (resized)'])
a='<!-- TABLE OF CONTENTS -->'; assert s.count(a)==1; s=s.replace(a,hero+'  '+a)
a='so I would not promise to see them all on one visit.</p>'; assert s.count(a)==1; s=s.replace(a,a+blocks['survives'])
a='Jeepe describes it with ponds and mixed woodland.</p>'; assert s.count(a)==1; s=s.replace(a,a+blocks['garden'])
i=s.index('</ul>',s.index('id="visit"'))+5; s=s[:i]+blocks['visit']+s[i:]
open(p,'w',encoding='utf-8').write(s)
with open(R+'PHOTO-CREDITS.csv','a',encoding='utf-8',newline='') as f: csv.writer(f,lineterminator='\r\n').writerows(rows)
for tg in ['div','figure','picture','p','a','ul','li','details','section','h2']:
    assert len(re.findall(f'<{tg}[ >]',s))==len(re.findall(f'</{tg}>',s)),tg
for m in re.findall(r'<script type="application/ld\+json">(.*?)</script>',s,re.S): json.loads(m)
print('ok',s.count('<figure'))
