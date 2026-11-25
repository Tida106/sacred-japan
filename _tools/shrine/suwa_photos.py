import re,csv,io
from PIL import Image
R='/home/claude/sacred-japan/'; SL='suwa-taisha'
ZT='https://commons.wikimedia.org/w/index.php?search=%s&title=Special:MediaSearch&type=image'
LIC={'cc0':('CC0','https://creativecommons.org/publicdomain/zero/1.0/'),
 'by3':('CC BY 3.0','https://creativecommons.org/licenses/by/3.0/'),
 'bysa3':('CC BY-SA 3.0','https://creativecommons.org/licenses/by-sa/3.0/')}
F='https://commons.wikimedia.org/wiki/File:'
# key:(upload id, author, commons link, lic)
P={
'onb-maemiya':('d81f84e9','z tanuki',ZT%'Suwa+taisha+Kamisha+Maemiya+panoramio','by3'),
'onb-honmiya':('cdd38871','z tanuki',ZT%'Suwa+taisha+Kamisha+Honmiya+panoramio','by3'),
'onb-akimiya':('45c5c314','663highland','https://commons.wikimedia.org/wiki/User:663highland','bysa3'),
'onb-harumiya':('ed00acec','663highland','https://commons.wikimedia.org/wiki/User:663highland','bysa3'),
'onb-other':('3c7169a8','Mc43810','https://commons.wikimedia.org/wiki/User:Mc43810','cc0'),
'honmiya-gate':('1b0528e2','z tanuki',ZT%'Suwa+taisha+Kamisha+Honmiya+panoramio','by3'),
'honmiya-haisho-grounds':('f67368fc','z tanuki',ZT%'Suwa+taisha+Kamisha+Honmiya+panoramio','by3'),
'honmiya-carving':('a53c08b8','z tanuki',ZT%'Suwa+taisha+Kamisha+Honmiya+panoramio','by3'),
'honmiya-chokuganden':('ed0fdcce','Saigen Jiro',F+'Suwa-taisha_Kamisha_Honmiya_chokuganden.jpg','cc0'),
'honmiya-okuninushi':('6a0b2df5','Saigen Jiro',F+'Suwa-taisha_Kamisha_Honmiya_Okuninushi-sha.jpg','cc0'),
'maemiya-torii':('5944c385','Saigen Jiro',F+'Suwa-taisha_Kamisha_Maemiya_torii.jpg','cc0'),
'maemiya-jikkenro':('48b44c4f','Saigen Jiro',F+'Suwa-taisha_Kamisha_Maemiya_Jikkenrou-2.jpg','cc0'),
'maemiya-hall':('9973b98a','z tanuki',ZT%'Suwa+taisha+Kamisha+Maemiya+panoramio','by3'),
'akimiya-torii':('c7e4ea97','Saigen Jiro',F+'Suwa-taisha_Shimosha_Akimiya_torii-2.jpg','cc0'),
'akimiya-subshrines':('ac81dc65','Saigen Jiro',F+'Suwa-taisha_Shimosha_Akimiya_keidaisha.jpg','cc0'),
'harumiya-heihaiden':('ba0953de','Saigen Jiro','https://commons.wikimedia.org/wiki/User:Saigen_Jiro','cc0'),
'harumiya-eaves':('e0ee4676','z tanuki',ZT%'Suwa+taisha+Shimosha+Harumiya+panoramio','by3'),
'harumiya-manji':('0ba917b6','z tanuki',ZT%'Manji+no+Sekibutsu+panoramio','by3'),
}
SIZE={}
for k,(u,a,l,li) in P.items():
    im=Image.open(f'/mnt/user-data/uploads/{u}-image.jpg').convert('RGB')
    w,h=im.size; tw=min(900 if h>w else 1200,w); th=round(h*tw/w)
    im=im.resize((tw,th),Image.LANCZOS)
    d=R+f'guides/{SL}/images/{k}'
    im.save(d+'.jpg',quality=84,optimize=True); im.save(d+'.webp',quality=80)
    SIZE[k]=(tw,th)
def fig(k,alt,cap):
    u,a,l,li=P[k]; ln,lu=LIC[li]; w,h=SIZE[k]
    mw=min(420 if h>w else 760,w)
    return f'''<figure style="margin:28px auto;max-width:{mw}px;"><picture><source srcset="/guides/{SL}/images/{k}.webp" type="image/webp"><img src="/guides/{SL}/images/{k}.jpg" alt="{alt}" width="{w}" height="{h}" loading="lazy" style="width:100%;height:auto;border-radius:4px;display:block;"></picture><figcaption style="font-size:13px;color:var(--enshu);margin-top:10px;text-align:center;line-height:1.6;">{cap}<br>Photo: <a href="{l}" target="_blank" rel="noopener">{a}</a>, <a href="{lu}" target="_blank" rel="noopener">{ln}</a>, via Wikimedia Commons (resized)</figcaption></figure>
'''
def blk(k,alt,cap,text): return fig(k,alt,cap)+f'  <p>{text}</p>\n'
H=[]
H.append('  <h3 id="onbashira-up-close" style="margin-top:36px;">The Pillars Up Close</h3>\n')
H.append('  <p>Each of the four sites raises four pillars, numbered one to four, and a small sign beside each says which it is. These are the second and third pillars as they stand between festivals: bare, pale trunks held upright by a bundle of logs at the base and fenced off with paper streamers. The festival cycle is six years by the calendar, but Japanese counting includes both end years, which is why you will also see it called a seven-year festival.</p>\n')
H.append(blk('onb-maemiya','The third Onbashira pillar at Kamisha Maemiya inside a wooden frame hung with paper streamers','The third pillar at Kamisha Maemiya',"The third pillar at Kamisha Maemiya stands on open ground against the hills, ringed by a low wooden frame hung with streamers. Look at the base: a ring of upright logs holds the trunk, which is the part that disappears from the usual festival footage."))
H.append(blk('onb-honmiya','The second Onbashira at Kamisha Honmiya beside the roof of a covered corridor','The second pillar at Kamisha Honmiya',"The second pillar at Kamisha Honmiya, with the roof of the long covered corridor just visible at the left. The sign on the post reads <em>Honmiya Ninoonbashira</em>, the second pillar of Honmiya. The towering cedars behind it look small beside the trunk."))
H.append(blk('onb-akimiya','The second Onbashira at Shimosha Akimiya beside a shrine roof','The second pillar at Shimosha Akimiya',"At Shimosha Akimiya the second pillar rises beside a small hall, its sign reading <em>Akimiya Ninoonbashira</em>. The trunk is much taller than the nearby cedar, which is the point: these were once trees that had to be dragged down a mountain."))
H.append(blk('onb-harumiya','The second Onbashira at Shimosha Harumiya behind a fence with paper streamers','The second pillar at Shimosha Harumiya',"The second pillar at Shimosha Harumiya, fenced with streamers, with a shrine building and lanterns on the right. The Harumiya and Akimiya pillars are the ones you can see on the same trip along the north shore."))
H.append(blk('onb-other','A first Onbashira pillar at a smaller Suwa shrine, with a sign reading Suwa Jinja Ichinoonbashira','A first pillar at a smaller Suwa shrine elsewhere',"This one is not at the four Suwa Taisha sites. The sign reads <em>Suwa Jinja Ichinoonbashira</em>, the first pillar of a local Suwa shrine, a reminder that branch shrines of Suwa across Japan sometimes raise their own pillars. I do not know which town this one is in."))
H.append('  <h2 id="walk">Walking the Four Shrines</h2>\n')
H.append('  <p>The four sites feel quite different on the ground. These photos were taken in different seasons and years, and some show repair work, so the scenery you meet may not match exactly.</p>\n')
H.append('  <h3 id="honmiya" style="margin-top:32px;">Kamisha Honmiya: Corridors and Carvings</h3>\n')
H.append('  <p>Kamisha Honmiya is the largest of the four, with its buildings strung along a wooded slope: a gate, a long covered corridor, worship halls and a scatter of small shrines in the trees.</p>\n')
H.append(blk('honmiya-gate','The roofed gate at the head of the Nunobashi corridor with carved dragon and stone lanterns','The gate at the head of the Nunobashi corridor',"This is the gate at the head of the Nunobashi, the long covered corridor. A carved dragon coils across the beam, a pair of stone lanterns flanks the entrance and the white curtains carry a leaf crest that I read as the Suwa emblem. The corridor runs away from you toward the halls."))
H.append(blk('honmiya-haisho-grounds','The open grounds in front of the Honmiya worship hall with an ema rack and scaffolding behind','The grounds in front of the Honmiya worship hall',"The open gravel court in front of the worship hall, with a rack of ema wishing plaques at the right. Scaffolding behind the roof shows that repairs were under way when this was taken, so expect the view to vary with the work schedule."))
H.append(blk('honmiya-carving','Dragon and bird carvings on a wooden beam under the eaves at Kamisha Honmiya','Beam carvings under the eaves',"Look up under the eaves and the beams come alive: a dragon with a blue-tinted eye, a bird with spread wings and swirling clouds, carved in deep relief. I cannot tell from the photo which building this is, only that it is among the Honmiya buildings."))
H.append(blk('honmiya-chokuganden','The Chokuganden hall at Kamisha Honmiya among trees above stone steps','The Chokuganden',"The sign on this hall reads <em>Chokuganden</em>, which I understand as a hall for prayers offered on behalf of the emperor. It stands on a platform of stone steps in deep green woods, quiet compared with the main halls."))
H.append(blk('honmiya-okuninushi','The small Okuninushi-sha shrine with a sign explaining Takeminakata is recorded as his second child','The small Okuninushi-sha',"A tiny shrine to Okuninushi, the god of Izumo, beside moss-covered lanterns. The sign beside it notes that Takeminakata is recorded as Okuninushi's second child. So the loser of the wrestling match has his father's shrine here, and you can read more of that family story in the <a class=\"inline-link\" href=\"/guides/izumo-taisha/\">Izumo Taisha guide</a>."))
H.append('  <h3 id="maemiya" style="margin-top:32px;">Kamisha Maemiya: The Quieter Older Site</h3>\n')
H.append('  <p>Kamisha Maemiya is known as one of the oldest sites in the complex. It is smaller and calmer than Honmiya, and it sits a short way off.</p>\n')
H.append(blk('maemiya-torii','The bronze-coloured Maemiya torii with a shimenawa and guardian lion-dogs, stone steps beyond','The torii at Kamisha Maemiya',"The Maemiya torii with its shimenawa, flanked by guardian lion-dogs whose bases are marked with the characters for “offering”. Stone steps climb behind it, and the roof of the Jikkenro peeks out at the left."))
H.append(blk('maemiya-jikkenro','The Jikkenro, a long open hall with a shingle roof hung with paper streamers, at Kamisha Maemiya','The Jikkenro',"The Jikkenro is a long, open hall under a big shingle roof, with latticed sides and paper streamers hanging along the eaves. It is easy to walk past if you are heading for the main steps, so take a minute to look at the roof line."))
H.append(blk('maemiya-hall','The shrine building at the top of the stone steps at Kamisha Maemiya, with a no-smoking sign','The shrine building above the steps at Kamisha Maemiya',"The shrine building at the top of the steps, a shimenawa across its front and cedars all around. The sign in front reads <em>Keidai kinen</em>, a polite request not to smoke in the grounds."))
H.append('  <h3 id="akimiya" style="margin-top:32px;">Shimosha Akimiya: Torii, Bridge and Small Shrines</h3>\n')
H.append('  <p>Shimosha Akimiya is the one with the great shimenawa on the Kaguraden at the top of this page, and it also has smaller things worth stopping for.</p>\n')
H.append(blk('akimiya-torii','The bronze torii of Shimosha Akimiya beyond a small stone bridge with lanterns','The torii at Shimosha Akimiya',"The Akimiya torii stands beyond a short arched stone bridge, with lanterns on both sides and the approach stairs rising behind. The stone and bronze look much the same in every season, so it is the greenery that tells you when it was taken."))
H.append(blk('akimiya-subshrines','A row of auxiliary shrines in the Akimiya precincts with a Kashima-sha sign','Auxiliary shrines at Akimiya',"A row of small auxiliary shrines in the grounds. As I read the sign on the left, it says Kashima-sha, which would make it a shrine to Takemikazuchi, the thunder god who won the wrestling match against Takeminakata. The racks of metal objects hung beside the buildings are something I cannot identify from the photo."))
H.append('  <h3 id="harumiya" style="margin-top:32px;">Shimosha Harumiya: Carved Eaves and a Round Stone Buddha</h3>\n')
H.append('  <p>Shimosha Harumiya is the more rural of the two north-shore sites. The buildings are modest, but the carving is fine.</p>\n')
H.append(blk('harumiya-heihaiden','What appears to be the Heihaiden at Shimosha Harumiya with carved layered roofs and lower roofs to each side','The Heihaiden at Shimosha Harumiya',"What appears to be the Heihaiden of Harumiya from the front: a layered central roof with carved decoration and lower-roofed buildings reaching out to each side. There are no grand steps or crowds, which suits the place."))
H.append(blk('harumiya-eaves','Looking up at the eaves of the Harumiya Heihaiden with gilded fittings and carved beams','Looking up at the Heihaiden eaves',"Looking up under the eaves shows the gilded fittings and the carving around the beams, the part most visitors do not look at. It rewards a few minutes of craning your neck."))
H.append(blk('harumiya-manji','The rounded Manji Stone Buddha with stone basins in front','The Manji Stone Buddha',"The Manji Stone Buddha has a rounded, almost bell-shaped body and a distinctive, rather blunt face. A date for Manji 3 (1660) is said to be carved on it, and stone basins sit in front of it. It is one of the more unexpected things on a walk through the Suwa shrines."))
BLOCK=''.join(H)
p=R+f'guides/{SL}/index.html'
s=open(p,encoding='utf-8').read()
a='  <h2 id="getting-there">'
assert s.count(a)==1 and '#walk' not in s
s=s.replace(a,BLOCK+a)
t='      <li><a href="#onbashira">Onbashira: Riding Trees Down a Mountain</a></li>\n'
assert s.count(t)==1
s=s.replace(t,t+'      <li><a href="#walk">Walking the Four Shrines</a></li>\n')
s=s.replace('"dateModified": "2026-10-11"','"dateModified": "2026-11-25"')
open(p,'w',encoding='utf-8').write(s)
sm=open(R+'sitemap.xml',encoding='utf-8').read()
sm=sm.replace('suwa-taisha/</loc>\n    <lastmod>2026-10-11','suwa-taisha/</loc>\n    <lastmod>2026-11-25')
open(R+'sitemap.xml','w',encoding='utf-8').write(sm)
rows=[]
for k,(u,a_,l,li) in P.items():
    ln,lu=LIC[li]
    rows.append(['guides/suwa-taisha',f'/guides/{SL}/images/{k}.jpg',ln,lu,l,f'{k}: Photo: {a_}, {ln}, via Wikimedia Commons (resized)'])
b=io.StringIO(); csv.writer(b,lineterminator='\r\n').writerows(rows)
open(R+'PHOTO-CREDITS.csv','a',encoding='utf-8',newline='').write(b.getvalue())
print(len(P),SIZE)
