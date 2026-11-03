import re,csv,json
from PIL import Image
R='/home/claude/sacred-japan/'; A='/mnt/user-data/attachments/53e3d492-4bf8-5cd9-a0ec-63a7cbefb1d9/'
SL='okayama-castle'; D=R+f'guides/{SL}/images/'
import os; os.makedirs(D,exist_ok=True)
S4=('CC BY-SA 4.0','https://creativecommons.org/licenses/by-sa/4.0/')
S3=('CC BY-SA 3.0','https://creativecommons.org/licenses/by-sa/3.0/')
S2=('CC BY-SA 2.0','https://creativecommons.org/licenses/by-sa/2.0/')
B4=('CC BY 4.0','https://creativecommons.org/licenses/by/4.0/')
C0=('CC0','https://creativecommons.org/publicdomain/zero/1.0/')
P=[
('hero','69c9cdea','663highland',S3,'A black-walled castle keep with several tiers of gray roofs and white gables under a deep blue sky, with a white turret at the left','The keep from the front, 31 January 2008.',None,'hero'),
('spring','4446c730','Reggaeman',S3,'A black castle keep with white gables rising above green trees and blossoming branches, seen from the north-west under a pale blue sky','The keep from the north-west in spring, 16 April 2005.',
 "This is the castle in spring, seen through fresh leaves and a few pale blossoms. The black siding is plain even from this angle, and the white gables and gold ornaments at the roof line pick it out against the pale sky. It is also a reminder of how the site works today: the keep stands above a wooded hill, so you often see it through trees.",'history'),
('moat','20b25a22','Lynn0927',S4,'A calm moat reflecting a blue sky and green banks, with a small black castle keep on the far right above the trees','The moat with the keep in the distance, 13 December 2015.',
 "Here is the water side of the story. The keep sits small at the right, and the river-fed moat fills most of the frame, with low wooded hills behind. Wikipedia says the outer moats were filled in between 1873 and 1882, so what you see here is what is left of the water, not the original ring.",'history'),
('autumn','5724cab5','Kimon Berlin',S2,'A black castle keep framed by orange and yellow autumn leaves, with a stone embankment and still water in the foreground','The keep through autumn leaves (Commons title: Okayama Castle from Korakuen).',
 "Commons titles this view as taken from Korakuen, the garden next door, and the dark keep framed by orange leaves is the reason I suggest pairing the two. I only have the file title and no shooting date, so I cannot say which season or year this is, but the colors suggest autumn.",'history'),
('shachi','c8d3c7c5','663highland',S3,'A large gold shachihoko with a fish-like head and curled tail on a roof ridge, with a moat, trees and city buildings far below','A gold shachihoko on the roof, with the moat and the city below.',
 "This is the gold I would count on. The shachihoko, the tiger-headed fish ornament on the roof ridge, is plated, and the moat, the trees and the city spread out behind it. Wikipedia says the roof ornaments were gilded in 1996 for the 400th anniversary, which fits what you see here: bright gold against a dark roof.",'black'),
('evening','45ed6925','Zairon',B4,'A black castle keep at dusk, with warm light on the upper floors and gilded roof edges against a pink and gray evening sky','The keep in the evening, 20 October 2023.',
 "At dusk the keep looks different. The upper floors catch a warm light, the roof edges look gilded, and the lower black walls fall into the shadow of the trees. A couple of dark shapes on the ridge look like birds, which I find fitting for a Crow Castle, though I cannot tell you what they are.",'black'),
('view','86e26820','Zairon',B4,'A view from a high floor over a dark curved roof tile at the right, a park with trees and paths below, and a city with low mountains beyond under a cloudy sky','The view from the keep, over the roof edge and the city.',
 "The reward for climbing the museum is this: from the top you look over a curved dark roof tile to the park, the river side and the city, with low mountains beyond. It gives you a sense of why a lord wanted this hill, and of how the castle town grew into the modern city.",'fire'),
('armour-red','704e2a13','Zairon',B4,'A suit of armor with red lacing, a gold crescent on the helmet and a black face mask, standing in a glass case in front of a painted screen','An armor on display at the keep.',
 "The exhibits include armor, and this one has red lacing and a large gold crescent on the helmet. As I read the label, it relates to Hanafusa Masanari, but the label is hard to read in my copy, so check it on site. Commons only calls it an armor at the keep.",'fire'),
('armour-seated','0d23d4d1','Zairon',B4,'A seated suit of black armor with white and gold lacing and a yellow tassel, in front of a painted screen with a crowd of small figures','Another armor on display, shown seated.',
 "This second armor is shown seated, in black with white and gold lacing and a yellow tassel, in front of a painted screen. Commons says only that it is an armor at the keep, and I cannot see a name for the owner, so I will not guess one.",'fire'),
('armour-lamellar','c9890c9d','Zairon',B4,'A tall glass case with a suit of dark armor with a round helmet, a gold-trimmed chest plate and boots, with a small label at the lower left','A third armor in a glass case.',
 "A third armor stands in a tall case with a small label at its foot. It has a rounded helmet and a pale chest plate. Again, Commons says only that it is an armor at the keep, so I cannot tell you whose it was.",'fire'),
('sword','e0ecda96','Zairon',B4,'A long ornate sheathed sword with gold fittings and a woven cord on a display shelf in front of a blue and gold panel','An ornate sword on display.',
 "This sword has a gold-fitted sheath wrapped in dark cord, and it lies on a shelf under a panel of blue and gold. The label is partly cut off, but it seems to mention Toshogu. I would not rely on that, so read the card in the case.",'fire'),
('sedan','80634d03','Zairon',B4,'A black lacquered palanquin with gold crests and red tassels on a stand in front of dark wooden walls','A black lacquered palanquin with gold crests.',
 "This black lacquered palanquin is covered in small gold crests, which look like butterflies to me. The owner is not named in the Commons description, so I will leave it at that. It is a good example of the kind of luxury goods the museum shows alongside the weapons.",'fire'),
('corridor-gate','333b4e48','Zairon',B4,'A white-walled gate with a tiled roof between a dark stone wall at the right and trees, with a gravel path leading through to steps beyond','The Corridor Gate (Commons title).',
 "Commons calls this the Corridor Gate. It has white plaster walls and a tiled roof, with a high stone wall at the right and a gravel path leading through to a flight of steps. I do not know whether this gate is original or rebuilt. Wikipedia says an adjacent gate was destroyed in 1945 and rebuilt with the keep, so check the signs on site.",'survives'),
('stone-gate','49fa9c8e','Daderot',C0,'A gatehouse with a white upper wall and a gray tile roof above a wall of large rough stones, with an open passage into the castle grounds, 8 December 2011','A gate in the stone walls, 8 December 2011.',
 "This is the stone I mean by the surviving walls. Large rough blocks make up the lower wall, and a white-walled gatehouse with a tiled roof sits above them. Commons does not name the gate in this file, so I will not put a name on it.",'survives'),
]
def fig(k,au,lic,alt,cap,hero,im):
    img=f'<picture><source srcset="/guides/{SL}/images/{k}.webp" type="image/webp"><img src="/guides/{SL}/images/{k}.jpg" alt="{alt}" width="{im.width}" height="{im.height}" loading="{"eager" if hero else "lazy"}" style="width:100%;{"max-height:420px;object-fit:cover;object-position:center 40%;" if hero else "height:auto;"}border-radius:4px;display:block;"></picture>'
    fc=f'<figcaption style="font-size:13px;color:var(--enshu);margin-top:10px;text-align:center;line-height:1.6;">{cap}<br>Photo: {au}, <a href="{lic[1]}" target="_blank" rel="noopener" style="color:var(--enshu);">{lic[0]}</a>, via Wikimedia Commons (resized)</figcaption>'
    return img,fc
p=R+f'guides/{SL}/index.html'; s=open(p,encoding='utf-8').read()
blocks={g:'' for g in ['history','black','fire','survives']}; hero=''; rows=[]
for k,f,au,lic,alt,cap,ps,g in P:
    im=Image.open(A+f+'-image.jpg').convert('RGB')
    if im.width>1200: im=im.resize((1200,round(im.height*1200/im.width)),Image.LANCZOS)
    im.save(D+k+'.jpg',quality=84,optimize=True); im.save(D+k+'.webp',quality=80)
    img,fc=fig(k,au,lic,alt,cap,g=='hero',im)
    if g=='hero': hero=f'<figure style="margin:0 0 48px;">{img}{fc}</figure>\n\n'
    else:
        mw=420 if im.height>im.width else 760
        blocks[g]+=f'\n    <figure style="margin:28px auto;max-width:{mw}px;">{img}{fc}</figure>\n    <p>{ps}</p>'
    rows.append([f'guides/{SL}',f'/guides/{SL}/images/{k}.jpg',lic[0],lic[1],lic[1],cap+f' Photo: {au}, {lic[0]}, via Wikimedia Commons (resized)'])
a='<!-- TABLE OF CONTENTS -->'; assert s.count(a)==1; s=s.replace(a,hero+'  '+a)
for g,a in [('history',"so the castle's walls gradually disappeared under the city.</p>"),('black','which looks sharpest against a clear sky.</p>'),('fire','though they add that exhibits and events change by season.</p>'),('survives','these two and the surviving walls are where to spend your time.</p>')]:
    assert s.count(a)==1,g; s=s.replace(a,a+blocks[g])
open(p,'w',encoding='utf-8').write(s)
with open(R+'PHOTO-CREDITS.csv','a',encoding='utf-8',newline='') as f: csv.writer(f,lineterminator='\r\n').writerows(rows)
for tg in ['div','figure','picture','p','a','ul','li','details','section','h2']:
    assert len(re.findall(f'<{tg}[ >]',s))==len(re.findall(f'</{tg}>',s)),tg
for m in re.findall(r'<script type="application/ld\+json">(.*?)</script>',s,re.S): json.loads(m)
print('ok',s.count('<figure'))
