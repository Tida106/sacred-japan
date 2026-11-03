import re,os,csv,json
from PIL import Image
R='/home/claude/sacred-japan/'; A='/mnt/user-data/attachments/49b96ec1-728b-5ea6-b8b2-6e6ae280fb4e/'
SL='osaka-castle'; D=R+f'guides/{SL}/images/'; os.makedirs(D,exist_ok=True)
S4=('CC BY-SA 4.0','https://creativecommons.org/licenses/by-sa/4.0/')
S3=('CC BY-SA 3.0','https://creativecommons.org/licenses/by-sa/3.0/')
B3=('CC BY 3.0','https://creativecommons.org/licenses/by/3.0/')
B4=('CC BY 4.0','https://creativecommons.org/licenses/by/4.0/')
C0=('CC0','https://creativecommons.org/publicdomain/zero/1.0/')

def fig(k,au,lic,alt,cap,w,h,hero=False):
    img=f'<picture><source srcset="/guides/{SL}/images/{k}.webp" type="image/webp"><img src="/guides/{SL}/images/{k}.jpg" alt="{alt}" width="{w}" height="{h}" loading="{"eager" if hero else "lazy"}" style="{"width:100%;max-height:420px;object-fit:cover;object-position:center 30%;border-radius:4px;display:block;" if hero else "width:100%;height:auto;border-radius:4px;display:block;"}"></picture>'
    fc=f'<figcaption style="font-size:13px;color:var(--enshu);margin-top:10px;text-align:center;line-height:1.6;">{cap}<br>Photo: {au}, <a href="{lic[1]}" target="_blank" rel="noopener" style="color:var(--enshu);">{lic[0]}</a>, via Wikimedia Commons (resized)</figcaption>'
    mw='max-width:760px;' if w>=h else 'max-width:420px;'
    return f'<figure style="{"margin:0 0 48px;" if hero else "margin:28px auto;"+mw}">{img}{fc}</figure>\n'


S2=('CC BY-SA 2.0','https://creativecommons.org/licenses/by-sa/2.0/')
B2=('CC BY 2.0','https://creativecommons.org/licenses/by/2.0/')
P=[
('hero','04eca8a6','Otto Domes',S4,'Osaka Castle keep rising above a mossy stone wall and a still green moat under a grey sky',
 'The keep above the stone walls, 23 May 2018 (Commons: Osaka Castle in Osaka, Japan).',None),
('keep-south','9b6989aa','DXR',S4,'Low-angle view of the Osaka Castle keep with white gables, green tiles and gold ornaments above a stone base',
 'The keep from the south, 15 April 2019 (Commons description).',
 "From the south the keep's tiers stack up above its stone base, each roof ending in gold-tipped gables over green tiles. The topmost floor is black, with gold tiger figures on its walls. None of my sources explain the tigers, so I will not guess at their meaning. The photo is a good way to count the outer tiers that Wikipedia says number five."),
('keep-deck','e62216f2','dconvertini',S2,'Osaka Castle keep framed by tree branches, with visitors standing on the glass-screened top-floor deck below two gold tigers',
 'The keep seen through trees, 28 May 2019 (Commons: Osaka Castle).',
 "Look at the top: people stand along a railed deck behind a glass screen, which fits the eighth-floor observation deck that the sources describe. The two gold tigers on the black wall below it are clear in this shot, one on each side. The photo gives a sense of how high the deck sits above the park."),
('keep-night','8c6b2f58','Manish Prabhune',S4,'Osaka Castle keep lit up at dusk under a purple sky with warm light from every window and a glass tower at the base',
 'The keep lit in the evening, 31 July 2011 (Commons).',
 "The windows glow and floodlights wash the white walls orange, with the green roofs and gold ornaments standing out. A glass tower at the foot of the keep looks like the elevator shaft, which would fit Wikipedia's note that the keep has elevators, though I cannot confirm it from the photo. The colors look strongly enhanced, so treat the purple sky as the photographer's style, not what you will necessarily see."),
('walls-moat','7c993911','Joli Rumi',S4,'A yellow-roofed boat full of passengers on the inner moat below tall stone walls with autumn-colored plants and the green keep roof above',
 'The inner moat and its walls, 10 November 2025 (Commons: Inner moat at Osaka Castle).',
 "A yellow-roofed boat full of passengers moves along the foot of a tall wall. That fits the roughly 20-minute Gozabune moat cruise that one guide describes, though Commons does not name the boat. The wall's corners step out in sharp angles, and early autumn color shows in the plants on its slope. A bit of the keep's green roof appears at the top right."),
('sakuramon','5c26ac78','Zairon',S4,'Visitors walking through Osaka Castle Cherry Blossom Gate with iron-studded black doors and huge stones, the keep visible in the opening',
 'The Sakuramon (Cherry Blossom Gate), 12 April 2018 (Commons description).',
 "Wikipedia lists the Sakuramon among the gates designated as important cultural properties. Here a tour group walks toward it with the keep's upper floors framed in the opening. The black doors are studded with iron, and the walls beside them are built of very large, closely fitted blocks. The white plaster above has small round openings that look like gun ports, but I cannot confirm that."),
('otemon','cfe880a7','Zairon',S4,'The Ote Gate of Osaka Castle with black iron-studded doors under a white plaster upper wall and huge flat stones on both sides',
 'The Otemon (Ote Gate), 12 April 2018 (Commons description).',
 "Japan-guide recommends entering the park by the Otemon. The gate has black doors under a white-plastered upper floor with a long barred window, and enormous flat stones form the walls on both sides. A few visitors and a cyclist pass through the opening, which shows how large it is."),
('otemon-turret','3cd498ad','inoue-hiro',('CC BY-SA 3.0','https://creativecommons.org/licenses/by-sa/3.0/'),'Roofed gate and a white turret behind trimmed pines under a deep blue sky',
 'The Otemon and Sengan Yagura, 24 July 2007 (Commons description).',
 "This older, small photo shows the roofed gate at right and the white Sengan Yagura turret beyond, with trimmed pines in front under a deep blue sky. Commons names the turret, but I could not match it to the cultural-property list in my sources. It dates from 2007, so details around the gate may have changed."),
('moat-turret','37285ffb','Francisco Anzola',B3,'A white corner turret on top of a stepped stone wall reflected in still water, with autumn leaves on the right bank',
 'A moat and corner turret, 31 October 2015 (Commons: Osaka Castle Moat).',
 "A white turret sits at the top of a wall whose corners are cut in sharp steps, and wall and turret are mirrored almost perfectly in the still water. Autumn color shows on the right bank. Commons does not say which moat or turret this is, so I will not name it."),
('aerial','117b334f','Saigen Jiro',C0,'Aerial view of Osaka Castle moats, stepped stone walls, white turrets and a gate, with the keep small in the distance and city towers behind',
 'The castle grounds seen from above, 27 May 2017 (Commons caption, translated).',
 "From above, the moat zigzags around stepped stone walls with a white turret and a gate at the corners, and a green belt of park separates them from the city towers behind. The keep is the small green-roofed building near the top center. It shows what Japan-guide means by a castle surrounded by citadels, gates, turrets, stone walls and moats."),
('pond','7e42887b','Nacaru',S4,'A stone lantern beside a still pond with trimmed pines and the Osaka Castle keep rising behind, reflected in the water',
 'A pond and garden in front of the keep, 26 February 2024 (Commons caption).',
 "A stone lantern stands at the edge of a still pond, with trimmed pines in the foreground and the keep rising behind, reflected in the water. A modern tower stands at the right, outside the castle. Commons does not name the garden, so I cannot say it is Nishinomaru, though Japan-guide says that garden gives views up at the keep."),
('lawn','279d67e5','663highland',S3,'Tall trees in late-summer green shading a wide open lawn where two people sit far in the background',
 'Nishinomaru Garden, 5 September 2009 (Commons: Nishinomaru Garden of Osaka Castle).',
 "Tall trees shade a wide open lawn, with two people sitting in the distance. That matches Japan-guide's description of Nishinomaru as a lawn garden, though I do not know which part this is. It is a 2009 photo, so the garden may look different now."),
('bridge','98ff95f1','Sakai Yayoi',C0,'A curved wooden-railed bridge over a green moat with the Osaka Castle keep rising above trees and a stone wall',
 'Osaka Castle and Gokuraku-bashi Bridge, 31 August 2026 (Commons caption).',
 "A bridge with wooden railings curves over the moat, and the keep rises above the trees and a stone wall at the upper left. Commons calls it Gokuraku-bashi, which I could not match to any of my other sources, so I will not describe its history. In late summer the moat water is a bright green."),
('sakura-day','2f6647e5','Tom Purves',B2,'The top floors of the Osaka Castle keep above a mass of cherry blossoms',
 'The keep above cherry blossoms, 8 April 2006 (Commons: Osaka castle and cherry blossoms).',
 "Dense blossoms fill the foreground, and only the keep's top floors show above them, with the black wall, gold tigers and green roof. Japan-guide says blossoms usually appear in late March and early April, and this early-April photo is typical of that. It is from 2006, so use it as a mood, not a forecast."),
('sakura-night','3c8d0352','Mc681',S4,'Floodlit Osaka Castle keep behind illuminated cherry trees and glowing light sculptures of a horse with a rider, a fan, paper cranes and a heart',
 'Night lighting among the cherry trees, 5 April 2015 (Commons).',
 "Lit blossoms glow purple-white around the floodlit keep, and in front stand glowing sculptures of a gold horse with a rider, a fan, paper cranes and a heart frame. Commons does not name the event and this is from 2015, so check whether a similar display runs on your dates. Japan-guide says Nishinomaru Garden stays open until 21:00 in the blossom season."),
]

def fig2(k,au,lic,alt,cap,w,h,hero=False):
    return fig(k,au,lic,alt,cap,w,h,hero)
H={};rows=[]
for k,f,au,lic,alt,cap,ps in P:
    im=Image.open(A+f+'-image.jpg').convert('RGB'); print(k,im.size)
    if im.width>1200: im=im.resize((1200,round(im.height*1200/im.width)),Image.LANCZOS)
    im.save(D+k+'.jpg',quality=84,optimize=True); im.save(D+k+'.webp',quality=80)
    H[k]=fig(k,au,lic,alt,cap,im.width,im.height,k=='hero')+(f'    <p>{ps}</p>\n' if ps else '')
    rows.append([f'guides/{SL}',f'/guides/{SL}/images/{k}.jpg',lic[0],lic[1],lic[1],f'{cap}Photo: {au}, {lic[0]}, via Wikimedia Commons (resized)'])
p=R+f'guides/{SL}/index.html'; s=open(p,encoding='utf-8').read()
def aft(s,a,t):
    assert s.count(a)==1,a; return s.replace(a,a+'\n'+t)
s=s.replace('<main>\n','<main>\n\n'+H['hero'],1)
s=aft(s,'registered as a tangible cultural property.</p>',H['keep-south'])
s=aft(s,'though another guide says that may be paid, so check on the day.</p>',H['keep-deck'])
s=aft(s,'The modern keep is white with green tiles and gold ornaments.</p>',H['keep-night'])
s=aft(s,'so I will not quote one.</p>',H['walls-moat'])
s=aft(s,'confirm what you can see at the official site.</p>',H['sakuramon'])
s=aft(s,'than the tower does.</p>',H['otemon']+H['otemon-turret'])
s=aft(s,'a multi-purpose arena and a shrine dedicated to Hideyoshi.</p>',H['moat-turret']+H['aerial'])
s=aft(s,'which I could not verify further.</p>',H['pond']+H['lawn']+H['bridge']+'    <p>Cherry blossom season is the park\'s busiest time. Japan-guide calls Osaka Castle Park one of the city\'s most popular hanami spots, with blossoms usually appearing in late March and early April.</p>\n'+H['sakura-day']+H['sakura-night'])
open(p,'w',encoding='utf-8').write(s)
import csv
with open(R+'PHOTO-CREDITS.csv','a',encoding='utf-8',newline='') as f:
    w=csv.writer(f,lineterminator='\r\n'); [w.writerow(r) for r in rows]
for tg in ['div','figure','picture','p','a','ul','li','details','section','h2']:
    assert len(re.findall(f'<{tg}[ >]',s))==len(re.findall(f'</{tg}>',s)),tg
for m in re.findall(r'<script type="application/ld\+json">(.*?)</script>',s,re.S): json.loads(m)
print('ok',s.count('<figure'))
