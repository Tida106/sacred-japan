import re,os,io,csv
from PIL import Image
R='/home/claude/sacred-japan/'; SL='sumiyoshi-taisha'; D=R+f'guides/{SL}/'; os.makedirs(D+'images',exist_ok=True)
L={'cc0':('CC0 1.0','https://creativecommons.org/publicdomain/zero/1.0/'),'by4':('CC BY 4.0','https://creativecommons.org/licenses/by/4.0/'),'bysa4':('CC BY-SA 4.0','https://creativecommons.org/licenses/by-sa/4.0/')}
# key: (upload, author, lic, date, alt, caption, paragraph)
P={
'hongu-chigi':('05f1194c','Hyppolyte de Saint-Rambert','by4','February 2024','A hall with a thick thatch-like roof and crossed finials on the ridge, behind a vermilion fence','A Hongu hall behind the vermilion fence',
 'Look at the ridge: a long straight line topped by crossed <em>chigi</em> and a row of <em>katsuogi</em> logs. The roof is thick and heavy, and it does not curve the way a temple roof does. This is the plain, strong profile that defines the style.'),
'hongu-queue':('73c3ff08','そらみみ (Soramimi)','bysa4','February 2019','Visitors lined up in front of a large thatched shrine hall with a sign for New Year prayers','The First Hongu during the New Year prayer period',
 'This was taken during the New Year prayer period, when visitors line up in front of the First Hongu. Crossed <em>chigi</em> rise above the large roof. Expect a queue like this in early January.'),
'sorihashi-green':('8a7c3279','Saigen Jiro','cc0','May 2016','The red arched Sorihashi bridge framed by green trees, with its reflection and white crossbeams in the pond','The Sorihashi in late spring, with its reflection in the pond',
 'In May the bridge stands as a bright red arc among green trees, with its reflection in the pond. Look at the white crossbeams and stone piers below the arch: they support the span, and their pale lines make the bridge look lighter than it is.'),
'sorihashi-front':('19436678','そらみみ (Soramimi)','bysa4','February 2019','The steps of the Sorihashi bridge seen from the plaza, with stone komainu on both sides and visitors climbing','From the foot of the bridge, with a komainu on each side',
 'This is the view that tells you how steep it is. A stone <em>komainu</em> guards each side, and visitors climb the steps one at a time. Hold the rail, take the steps slowly, and expect to wait if it is busy.'),
'sorihashi-side':('a2a01194','そらみみ (Soramimi)','bysa4','February 2019','The Sorihashi seen from the side, with stone piers and white beams under the steep red arch','The Sorihashi from the side',
 'From the side you can see how the bridge is built: a steep wooden arch on a row of stone piers, braced by white crossbeams.'),
'sorihashi-dusk':('acc2ef81','そらみみ (Soramimi)','bysa4','February 2019','The Sorihashi across a dark pond under a grey sky, its red reflection on the water','The Sorihashi on a grey winter afternoon',
 'Even under a cloudy winter sky, the bridge keeps its colour, and its red reflection shows on the dark water. It is a reminder that the bridge looks good in any weather, not only on a clear day.'),
'kouroku':('ca7497c3','Saigen Jiro','cc0','October 2017','A vermilion gate with a green tile roof and a blue plaque, with the open courtyard beyond','A vermilion gate whose plaque reads Koroku-mon',
 'A vermilion gate leads into the open courtyard. The plaque reads <em>Koroku-mon</em> (as I read it), and the green-tiled roof contrasts with the red frame. Gates like this mark the steps from the busy outer grounds into the main precinct.'),
'hatsutatsu':('d88412c2','Hyppolyte de Saint-Rambert','by4','February 2024','A vermilion gate with a green roof and a hanging banner, with a path lined with red banners beyond','A gate with a banner for the Hatsutatsu pilgrimage',
 'The banner at the gate refers to <em>Hatsutatsu</em>, a pilgrimage Sumiyoshi is known for. As I understand it, it is made on the first dragon day (<em>tatsu</em>) of the month, but please check the shrine for the details. Beyond the gate, a path is lined with red banners.'),
'bunko':('078b8750','そらみみ (Soramimi)','bysa4','February 2019','A white-walled storehouse with a curved roof and two lanterns reading Obunko, with a stone pillar beside it','The white-walled Obunko storehouse',
 'The white-walled storehouse with the curved roof is the <em>Obunko</em>. The stone pillar beside it is inscribed, as I read it, &ldquo;Osaka&rsquo;s oldest library.&rdquo; It is a quick stop, and a nice change from the red and black of the main halls.'),
'sessha':('7e2d9c63','Immanuelle','by4','August 2024','A small pink-vermilion shrine on a gravel court, with a rack of ema plaques at the right','A small subsidiary shrine, with ema plaques behind',
 'Small subsidiary shrines like this one stand around the grounds. A rack of <em>ema</em> wishing plaques is visible beside it. It is a good reminder that Sumiyoshi is not only the four great halls.'),
}
def fig(k,hero=False):
    u,a,l,d,alt,cap,par=P[k]; ln,lu=L[l]; w,h=Image.open(D+f'images/{k}.jpg').size
    st='margin:28px auto;max-width:420px;' if h>w else 'margin:28px auto;max-width:760px;'
    return f'''<figure style="{st}"><picture><source srcset="/guides/{SL}/images/{k}.webp" type="image/webp"><img src="/guides/{SL}/images/{k}.jpg" alt="{alt}" width="{w}" height="{h}" loading="lazy" style="width:100%;height:auto;border-radius:4px;display:block;"></picture><figcaption style="font-size:13px;color:var(--enshu);margin-top:10px;text-align:center;line-height:1.6;">{cap}, {d}.<br>Photo: {a}, <a href="{lu}" target="_blank" rel="noopener" style="color:var(--enshu);">{ln}</a>, via Wikimedia Commons (resized)</figcaption></figure>
    <p>{par}</p>
'''
for k,v in P.items():
    im=Image.open(f'/mnt/user-data/uploads/{v[0]}-image.jpg').convert('RGB'); w,h=im.size
    if w>1200: im=im.resize((1200,round(h*1200/w)),Image.LANCZOS)
    im.save(D+f'images/{k}.jpg',quality=84); im.save(D+f'images/{k}.webp',quality=80)
p=D+'index.html'; s=open(p,encoding='utf-8').read()
assert 'images/hongu-chigi' not in s
def after(s,marker,add):
    assert s.count(marker)==1,marker; return s.replace(marker,marker+add)
m1='<p>What you\'ll notice: straight, bold rooflines'
i=s.index(m1); j=s.index('</p>',i)+4
s=s[:j]+'\n    '+fig('hongu-chigi')+fig('hongu-queue')+s[j:]
m2='<h3>Crossing the Bridge</h3>'; i=s.index(m2); j=s.index('</p>',i)+4
s=s[:j]+'\n    '+''.join(fig(k) for k in ['sorihashi-green','sorihashi-front','sorihashi-side','sorihashi-dusk'])+s[j:]
m3='<!-- 6. PRACTICAL -->'; i=s.index(m3)
s=s[:i]+'    <h3>Gates, a Library and a Small Shrine</h3>\n    <p>Between the bridge and the halls, a few small stops are easy to miss.</p>\n    '+''.join(fig(k) for k in ['kouroku','hatsutatsu','bunko','sessha'])+'\n    '+s[i:]
s=re.sub(r'("dateModified": ")[^"]*(")',lambda m:m.group(1)+'2026-11-25'+m.group(2),s)
open(p,'w',encoding='utf-8').write(s)
for tg in ['div','figure','picture','p','a','ul','li','details','section','h2','h3']:
    assert len(re.findall(f'<{tg}[ >]',s))==len(re.findall(f'</{tg}>',s)),tg
# csv
b=open(R+'PHOTO-CREDITS.csv','rb').read().decode('utf-8-sig'); buf=io.StringIO(newline=''); w=csv.writer(buf,lineterminator='\r\n')
for k,v in P.items():
    ln,lu=L[v[2]]; w.writerow(['guides/sumiyoshi-taisha',f'/guides/sumiyoshi-taisha/images/{k}.jpg',ln,lu,'https://commons.wikimedia.org/w/index.php?search=Sumiyoshi taisha&title=Special:MediaSearch&type=image',f'{v[1]}, {v[5]} ({v[3]}), {ln}, via Wikimedia Commons'])
open(R+'PHOTO-CREDITS.csv','wb').write(('﻿'+b+buf.getvalue()).encode('utf-8')); print('ok')
