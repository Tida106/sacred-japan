import re,json,os,glob
from PIL import Image,ImageDraw,ImageFont
R='/home/claude/sacred-japan/'; SL='kumano-hongu-taisha'; D=R+f'guides/{SL}/'
os.makedirs(D+'images',exist_ok=True)
UP='/mnt/user-data/uploads/'
# slug: (upload id, author, license key, month-year, alt)
LIC={'bysa4':('CC BY-SA 4.0','https://creativecommons.org/licenses/by-sa/4.0/'),
     'bysa3':('CC BY-SA 3.0','https://creativecommons.org/licenses/by-sa/3.0/'),
     'bysa2':('CC BY-SA 2.0','https://creativecommons.org/licenses/by-sa/2.0/'),
     'by3':('CC BY 3.0','https://creativecommons.org/licenses/by/3.0/')}
P={
'banners':('8971b319','Nekosuki','bysa4','March 2013'),
'monument-torii':('6ea98642','Nekosuki','bysa4','March 2013'),
'torii-forest':('279b9902','Nekosuki','bysa4','January 2014'),
'shinmon':('f0de2853','Nekosuki','bysa4','January 2014'),
'temizuya':('1a53d027','Nekosuki','bysa4','March 2013'),
'haiden':('f3ac231a','Nekosuki','bysa4','March 2013'),
'three':('daf674e3','Nekosuki','bysa4','January 2014'),
'front':('7cd3d22f','Nekosuki','bysa4','January 2014'),
'close':('1a69b524','Nekosuki','bysa4','March 2013'),
'crowd':('f8075740','popsaurus','by3','undated (Panoramio)'),
'notari':('be7ec748','Tim Notari','bysa2','September 2006'),
'yatagarasu':('10b823cb','Yanajin33','bysa3','January 2013'),
'daikoku':('3138dce4','Yanajin33','bysa3','January 2013'),
}
for k,(u,a,l,d) in P.items():
    p=UP+u+'-image.jpg'
    if not os.path.exists(p): p=glob.glob(UP+u+'*')[0]
    im=Image.open(p).convert('RGB'); w,h=im.size
    if w>1200: im=im.resize((1200,round(h*1200/w)),Image.LANCZOS)
    im.save(D+f'images/{k}.jpg',quality=84); im.save(D+f'images/{k}.webp',quality=80)
SIZE={k:Image.open(D+f'images/{k}.jpg').size for k in P}
def fig(k,alt,cap,hero=False):
    u,a,l,d=P[k]; ln,lu=LIC[l]; w,h=SIZE[k]
    if hero: st='margin:0 0 48px;'; ld='eager'; mw=''
    elif h>w: st='margin:28px auto;max-width:420px;'; ld='lazy'
    else: st='margin:28px auto;max-width:760px;'; ld='lazy'
    ims='style="width:100%;height:auto;border-radius:4px;display:block;"'
    if hero: ims='style="width:100%;max-height:420px;object-fit:cover;border-radius:4px;display:block;"'
    return f'''<figure style="{st}"><picture><source srcset="/guides/{SL}/images/{k}.webp" type="image/webp"><img src="/guides/{SL}/images/{k}.jpg" alt="{alt}" width="{w}" height="{h}" loading="{ld}" {ims}></picture><figcaption style="font-size:13px;color:var(--enshu);margin-top:10px;text-align:center;line-height:1.6;">{cap}, {d}.<br>Photo: {a}, <a href="{lu}" target="_blank" rel="noopener" style="color:var(--enshu);">{ln}</a>, via Wikimedia Commons (resized)</figcaption></figure>'''
s=open(R+'guides/gifu-castle/index.html',encoding='utf-8').read()
i=s.index('<main>'); j=s.index('</main>'); head,tail=s[:i],s[j:]
TITLE="Kumano Hongu Taisha Guide: The Shrine That Moved After the 1889 Flood, and the Three-Legged Crow"
DESC="A licensed guide's guide to Kumano Hongu Taisha: the 158 stone steps, the 1889 flood that moved the shrine, the giant torii at Oyunohara, the Yatagarasu crow, and how to get there from Kii-Tanabe."
TAG="The head shrine of Kumano: 158 stone steps, a flood, and a crow that guides."
head=re.sub(r'<title>.*?</title>',f'<title>{TITLE} | Sacred Japan</title>',head,count=1)
head=re.sub(r'(<meta (?:name="description"|property="og:description"|name="twitter:description") content=")[^"]*(")',lambda m:m.group(1)+DESC+m.group(2),head)
head=re.sub(r'(<meta (?:property="og:title"|name="twitter:title") content=")[^"]*(")',lambda m:m.group(1)+TITLE+m.group(2),head)
head=re.sub(r'("headline": ")[^"]*(")',lambda m:m.group(1)+TITLE+m.group(2),head)
head=re.sub(r'("description": ")A licensed[^"]*(")',lambda m:m.group(1)+DESC+m.group(2),head)
head=re.sub(r'("date(?:Published|Modified)": ")[^"]*(")',lambda m:m.group(1)+'2026-11-25'+m.group(2),head)
head=re.sub(r'<meta name="keywords" content="[^"]*">','<meta name="keywords" content="Kumano Hongu Taisha, Oyunohara torii, Yatagarasu, Kumano Kodo, Kumano Sanzan, Kii-Tanabe, Wakayama shrine, Hosshinmon-oji">',head)
head=head.replace('guides/gifu-castle',f'guides/{SL}').replace('guide_gifu_castle_','guide_kumano_hongu_').replace('og-guides-gifu-castle',f'og-guides-{SL}')
head=head.replace('岐阜城','熊野本宮大社').replace('Gifu Castle','Kumano Hongu Taisha')
head=re.sub(r"<h1>.*?</h1>","<h1><em>Kumano Hongu Taisha</em>: The Shrine That Moved After the 1889 Flood, and the Three-Legged Crow</h1>",head,count=1,flags=re.S)
head=head.replace("Nobunaga's mountain castle above Gifu, with the keep closed until late 2027.",TAG)
head=head.replace('SACRED JAPAN GUIDES ／ 城','SACRED JAPAN GUIDES ／ 神社')
IL='class="inline-link"'
faqs=[
("Is Kumano Hongu Taisha free to enter?","The grounds are free (tb-kumano). The shrine office is listed as open 8:00 to 17:00 (tb-kumano), while another listing gives worship hours of 7:00 to 17:00 (NAVITIME), so please check the shrine's official page. The Homotsuden Treasure Hall is a separate ticket: 300 yen for adults, 100 yen for ages 12 to 15, free for 11 and under, 9:00 to 16:00 (tb-kumano)."),
("How do I get to Kumano Hongu Taisha?","By bus from JR Kii-Tanabe Station: japan-guide gives 90 to 135 minutes and 2,100 yen one way, roughly every two hours. Get off at Hongu Taisha-mae, next to the Kumano Hongu Heritage Center. From Shingu it is about 1 hour 20 minutes, and from Gojo about 4 hours (japan.travel and tb-kumano). By car it is about 75 minutes from Nanki-Tanabe IC (ANA). Timetables change, so check before you go."),
("How many steps are there?","158 stone steps lead from the entrance up to the main halls, lined with banners reading Kumano Daigongen (ANA). Allow time for a slow climb; the steps are uneven and can be slippery after rain."),
("Where is the giant torii?","It stands at Oyunohara, the old shrine site, about 1 km from the present shrine (Kanpai Japan). It was erected in 2000 and is 33.9 m tall and 42 m wide (Lonely Planet, Wikipedia), which makes it the largest torii in Japan. It is a separate stop from the shrine on the hill."),
("What is the Yatagarasu?","A three-legged crow from the legends of Emperor Jimmu. MLIT's database says it was sent to guide him from Kumano to present-day Nara. It is the symbol of the Japan Football Association and appears all over the shrine. You will find a black Yatagarasu post box on the grounds; NAVITIME says the shrine office sells votive plaques that can be mailed as postcards."),
("Do I have to hike the Kumano Kodo to visit?","No. Buses reach the shrine directly. If you want a taste of the trail, the walk from Hosshinmon-oji to the shrine is about 7.5 km and 2 to 3 hours (tb-kumano), mostly downhill. A bus runs from Hongu Taisha-mae to Hosshinmon-oji; Lonely Planet gives 460 yen and 15 minutes, but that listing may be dated. Our <a href=\"/guides/kumano-kodo/\" "+IL+">Kumano Kodo guide</a> covers the full pilgrimage."),
]
faq_json=',\n'.join('''    {
      "@type": "Question",
      "name": %s,
      "acceptedAnswer": {
        "@type": "Answer",
        "text": %s
      }
    }'''%(json.dumps(q),json.dumps(re.sub('<[^>]+>','',a))) for q,a in faqs)
head=re.sub(r'("mainEntity": \[\n).*?(\n  \]\n\}\n</script>\n\n<!-- ── GOOGLE)',lambda m:m.group(1)+faq_json+m.group(2),head,flags=re.S)
hh=re.sub(r'"mainEntity": \[.*','',head,flags=re.S)
assert not re.search('Gifu|Nobunaga|Kinka|castle|Castle',re.sub(r'<nav>.*?</nav>','',hh,flags=re.S).replace('Castles','')),re.findall('.{30}(?:Gifu|Nobunaga|Kinka|astle).{20}',hh)
def pp(t): return f'<p>{t}</p>'
main='''<main>

  <aside class="toc" aria-label="Table of contents">
    <div class="toc-label">TABLE OF CONTENTS ／ 目次</div>
    <div class="toc-title">In This Guide</div>
    <ol>
      <li><a href="#opening">A Shrine That Walked Uphill</a></li>
      <li><a href="#flood">The Flood and Oyunohara</a></li>
      <li><a href="#steps">The 158 Steps</a></li>
      <li><a href="#grounds">Inside the Grounds</a></li>
      <li><a href="#crow">The Crow That Guides</a></li>
      <li><a href="#torii">The Giant Torii</a></li>
      <li><a href="#visit">Visiting Kumano Hongu Taisha</a></li>
      <li><a href="#faq">Frequently Asked Questions</a></li>
      <li><a href="#final">Before You Climb</a></li>
    </ol>
  </aside>

  <article>

'''+fig('banners','Stone steps climbing between tall cedars, lined on both sides with tall banners reading Kumano Daigongen','The stone steps up to the main halls, lined with banners',hero=True)+'''
    <section id="opening">
      <p class="opening">As a licensed guide, I like to tell people that Kumano Hongu Taisha is a shrine that had to walk uphill. For centuries it stood on a sandbar where two rivers meet. In 1889 the water came, and what the flood left was carried to the ridge where the shrine stands today. That is why the place feels like two sites: the climb and the halls on the hill, and an empty riverbank a short walk away, guarded by the largest torii in Japan.</p>
      <p>Hongu is the center of the three grand shrines of Kumano (JR Central) and, according to tb-kumano, the head shrine of more than 3,000 Kumano shrines across Japan. It is also where the Nakahechi route of the <a href="/guides/kumano-kodo/" '''+IL+''' onclick="trackEvent('click','internal','guide_kumano_hongu_to_kumano_kodo')">Kumano Kodo</a> arrives. This guide covers what to see, the flood story, the three-legged crow, and how to get here.</p>
    </section>

    <h2 id="flood">The Flood and Oyunohara<span class="h2-jp">大斎原</span></h2>
    <p>Before 1889 the shrine stood at Oyunohara, a sandbar at the confluence of the Kumano and Otonashi rivers (tb-kumano, Wikipedia). In 1889 a flood destroyed most of the buildings there. The surviving halls were moved to higher ground, to the present site about 1 km away, in 1891 (Wikipedia, Kanpai Japan). Sources disagree on exactly how many buildings were lost: japan.travel says three of six were swept away, while others give different counts, so I say only that most were destroyed.</p>
    <p>The old site is still sacred. Wikipedia says four of the deities were moved to the new site and the rest remain enshrined at Oyunohara in two stone monuments. Today it is a quiet field of earth and small stone shrines, and I find it affecting precisely because nothing is there.</p>
'''+fig('monument-torii','A tall stone monument carved with Japanese characters beside a wooden torii gate in front of cedar trees','The torii and the stone monument at the foot of the steps (the carved characters read as &ldquo;Nihon dai-ichi reigenjo&rdquo;, as I read them)')+'''
    <p>The tall stone at the entrance carries large characters that I read as <em>Nihon dai-ichi reigenjo</em>, roughly &ldquo;Japan&rsquo;s foremost place of miraculous power.&rdquo; Read it as a statement of how the pilgrims saw this shrine. The wooden torii beside it is your first sign that you are crossing from the road into sacred ground.</p>

    <h2 id="steps">The 158 Steps<span class="h2-jp">石段</span></h2>
    <p>ANA and other listings give 158 stone steps from the entrance to the main halls, lined on both sides with banners reading <em>Kumano Daigongen</em> and shaded by tall cedars. Take them slowly. The climb is part of the experience, and the banners are the shrine&rsquo;s way of announcing itself from the bottom.</p>
'''+fig('torii-forest','A plain wooden torii gate standing among tall cedar trees with warning signs beside it','A plain wooden torii among the cedars')+'''
    <p>Near the approach stands a plain, unpainted wooden torii among the trees, with small warning signs beside it. The warnings are the usual ones for a mountain site (watch your footing, mind the weather), and I read the photo as a reminder that this is a working shrine in a forest, not a theme park. Please follow any posted signs.</p>

    <h2 id="grounds">Inside the Grounds<span class="h2-jp">境内</span></h2>
    <p>At the top, a gate hung with a rope and white curtains leads into the sacred enclosure.</p>
'''+fig('shinmon','A gate hung with a thick straw rope and white curtains, with a horse plaque above it','The gate before the main enclosure, with its rope and white curtains')+'''
    <p>The plaque in this photo shows a horse, which I take to be the zodiac animal of that year, as shrines often display at New Year; this was photographed in January 2014. Kanpai Japan calls this the Shinmon gate before the main sacred enclosure.</p>
'''+fig('temizuya','A stone water basin with a bronze dragon spout and a flowering shrub beside it','The purification basin with its bronze dragon, in March')+'''
    <p>Before you go on, rinse your hands and mouth at the water basin. Here a bronze dragon spouts the water, and in this March photo a flowering shrub (pieris, according to the original caption) is in bloom beside it. The dragon is a water guardian, a fitting choice for a shrine that was moved by a flood.</p>
'''+fig('haiden','A wooden hall hung with large calligraphy and round carvings of a crow','The hall hung with large calligraphy and round crow carvings')+'''
    <p>The first hall is hung with large calligraphy, and on the walls you can see round carvings of the three-legged crow. tb-kumano describes the buildings as a mix of Kasuga and Taisha styles. The plain wood and bark roofs are what make them look so much like the forest around them.</p>
'''+fig('three','A row of three halls with thick bark roofs and visitors praying in front','Three halls in a row, with visitors praying')+'''
    <p>The halls stand side by side under thick, layered roofs. In this photo visitors are praying in front of them. sekaiisan-wakayama.jp says the three main halls are Important Cultural Properties and that the precincts and Oyunohara are historic sites. Follow the usual routine at the offering box: a coin, two bows, two claps, a silent prayer, one bow (Kanpai Japan).</p>
'''+fig('front','The front of a shrine hall with visitors praying, golden lanterns and curtains with a chrysanthemum crest','The hall front, with golden lanterns and crest curtains')+'''
    <p>Look up at the hall front: golden lanterns hang from the eaves, and the curtains carry a chrysanthemum crest. In January the crowd is thick, because New Year visits (hatsumode) are popular here. If you can, come on a weekday morning outside the holidays.</p>
'''+fig('close','A close view of a hall front with a thick bell rope and offering box','A closer look at the hall front and the bell rope')+'''
    <p>A close look shows the thick rope for ringing the bell above the offering box. I like the simplicity: no gilding on the structure, just aged wood.</p>
'''+fig('crowd','A crowded courtyard with a tent selling amazake','The courtyard on a busy day, with an amazake tent')+'''
    <p>On busy days the courtyard fills up, and a tent sells <em>amazake</em>, a warm, sweet fermented rice drink. I could not verify when the tent operates, so treat it as a seasonal extra.</p>
'''+fig('notari','Visitors in front of a shrine hall with a thick, sweeping roofline','Visitors before the hall, with its sweeping roofline')+'''
    <p>This 2006 photo catches the roofline well: thick, sweeping and unlacquered. When I bring guests here, this is the angle I point out, because it shows why Hongu looks so different from the red-and-white shrines of the cities.</p>

    <h2 id="crow">The Crow That Guides<span class="h2-jp">八咫烏</span></h2>
    <p>The three-legged crow, Yatagarasu, is everywhere at Hongu. MLIT&rsquo;s database says it was sent to guide the legendary first emperor, Jimmu, from Kumano to present-day Nara, where he founded the first capital. It is the emblem of the Japan Football Association, and you will see it on lanterns, amulets and carvings. For the wider legend, see our <a href="/culture/japanese-mythology/" '''+IL+''' onclick="trackEvent('click','internal','guide_kumano_hongu_to_mythology')">Japanese mythology guide</a> and our page on <a href="/culture/sacred-animals/" '''+IL+''' onclick="trackEvent('click','internal','guide_kumano_hongu_to_sacred_animals')">sacred animals</a>.</p>
'''+fig('yatagarasu','A stone monument carved with a circular crow design, standing on a stone base','The Yatagarasu stone monument')+'''
    <p>This stone monument carries a circular carving of the crow, and the base reads, as I read it, <em>Hongu Yatagarasu</em>. The three legs are often explained as heaven, earth and humanity, but Wikipedia attributes that reading to a Kumano interpretation, so I offer it as one explanation among others.</p>
    <p>There is also a black Yatagarasu post box on the grounds. NAVITIME says the shrine office sells votive plaques that can be mailed as postcards and will give commemorative stamps to travelers. I suggest buying a plaque and sending one to yourself as a souvenir.</p>
'''+fig('daikoku','A rounded stone resting among white pebbles','The Daikoku-seki stone, among white pebbles')+'''
    <p>Nearby, a rounded stone sits among white pebbles; the original caption names it Daikoku-seki. I have not been able to verify its significance, so I will only say that it is the sort of quiet detail that rewards a slow look.</p>

    <h2 id="torii">The Giant Torii<span class="h2-jp">大斎原の大鳥居</span></h2>
    <p>The giant torii at Oyunohara is 33.9 m tall and 42 m wide and was erected in 2000 (Lonely Planet, Wikipedia). It weighs about 172 tons (JAL travel) and is Japan&rsquo;s largest. Wikipedia and japan.travel say it marks the division between the secular and the spiritual world. I recommend walking down to it after the shrine, not before: you will understand why the shrine used to be there.</p>

    <h2 id="visit">Visiting Kumano Hongu Taisha<span class="h2-jp">アクセス</span></h2>
    <ul class="practical-list">
      <li><strong>Bus from Kii-Tanabe:</strong> 90 to 135 minutes, 2,100 yen one way, about every two hours (japan-guide). From Shingu about 1 hour 20 minutes, from Gojo about 4 hours (tb-kumano, japan.travel). Get off at Hongu Taisha-mae.</li>
      <li><strong>By car:</strong> about 75 minutes from Nanki-Tanabe IC (ANA). NAVITIME lists about 40 spaces on the grounds and about 600 on the riverbed.</li>
      <li><strong>Hours and fees:</strong> grounds free. Shrine office 8:00 to 17:00 (tb-kumano); NAVITIME gives worship times of 7:00 to 17:00. Treasure hall 300 yen, 9:00 to 16:00 (tb-kumano). Please check the official site.</li>
      <li><strong>Walk the trail:</strong> Hosshinmon-oji to the shrine is about 7.5 km, 2 to 3 hours, mostly downhill (tb-kumano). Buses to Hosshinmon-oji are infrequent, so plan carefully.</li>
      <li><strong>Next stop:</strong> Yunomine Onsen is about 10 minutes by bus for 310 yen, according to the prefecture bus map I checked.</li>
      <li><strong>Festivals:</strong> the spring festival and the Yata-no-Hi fire festival in August at Oyunohara (japan.travel, tb-kumano).</li>
    </ul>
    <div class="key-callout">
      <p>&#127890; <strong>Plan your trip:</strong> Browse guided tours or plan a stay near Hongu. <a href="https://www.viator.com/search/Kumano%20Kodo?pid=P00298374&amp;mcid=42383&amp;medium=link&amp;campaign=sacred-japan" target="_blank" rel="noopener" onclick="trackEvent('click','affiliate','viator_kumano_hongu_inline')">Find tours on Viator &rarr;</a></p>
    </div>

    <h2 id="faq">Frequently Asked Questions<span class="h2-jp">よくあるご質問</span></h2>
    <div class="faq-stack">
'''+''.join(f'''    <details class="faq-item">
        <summary>{q}</summary>
        <div class="faq-answer">{a}</div>
    </details>
''' for q,a in faqs)+'''    </div>

    <h2 id="final">Before You Climb<span class="h2-jp">むすびに</span></h2>
    <p>Climb the 158 steps slowly, then walk down to the empty riverbank and look back at the torii. The shrine moved, but the place did not forget where it began.</p>

    <div class="closing-block">
      <span class="torii">&#9961;&#65039;</span>
      <p>A flood moved the buildings, but the crow still points the way.</p>
    </div>

    <section class="related-section">
      <h2>Related Guides</h2>
      <span class="h2-jp">関連ガイド</span>
      <div class="related-grid">
        <a class="related-card" href="/guides/kumano-kodo/" onclick="trackEvent('click','internal','related_kumano_hongu_to_kumano_kodo')">
          <div class="related-card-label">SACRED JAPAN ／ GUIDES</div>
          <div class="related-card-title">&#127794; Kumano Kodo Guide &rarr;</div>
          <div class="related-card-desc">The pilgrimage routes that lead to Hongu.</div>
        </a>
        <a class="related-card" href="/culture/japanese-mythology/" onclick="trackEvent('click','internal','related_kumano_hongu_to_mythology')">
          <div class="related-card-label">SACRED JAPAN ／ CULTURE</div>
          <div class="related-card-title">&#9961;&#65039; Japanese Mythology Guide &rarr;</div>
          <div class="related-card-desc">Kojiki gods and the shrines where the myths happen.</div>
        </a>
        <a class="related-card" href="/guides/ise-grand-shrine/" onclick="trackEvent('click','internal','related_kumano_hongu_to_ise')">
          <div class="related-card-label">SACRED JAPAN ／ GUIDES</div>
          <div class="related-card-title">&#9961;&#65039; Ise Grand Shrine Guide &rarr;</div>
          <div class="related-card-desc">Another great shrine of the Kii region.</div>
        </a>
      </div>
    </section>

  </article>

'''
tail=tail.replace('gifu-castle',SL).replace('gifu_castle','kumano_hongu').replace('DGifu','DKumano%20Hongu').replace('search/Gifu','search/Kumano%20Kodo')
def L(u,l,t): return f'<a href="{u}" target="_blank" rel="noopener" style="color:var(--beni);text-decoration:underline;" onclick="trackEvent(\'click\',\'external\',\'{l}\')">{t}</a>'
src='Sources verified at time of writing: '+', '.join([
 L('https://www.tb-kumano.jp/en/kumano-kodo/world-heritage/kumano-hongu-taisha/','src_hongu_tb','Tanabe City Kumano Tourism Bureau'),
 L('https://www.japan-guide.com/e/e4953.html','src_hongu_jg','japan-guide'),
 L('https://www.ana.co.jp/en/it/japan-travel-planner/wakayama/0000020.html','src_hongu_ana','ANA'),
 L('https://www.mlit.go.jp/tagengo-db/en/R2-00214.html','src_hongu_mlit','MLIT multilingual database'),
 L('https://www.kanpai-japan.com/kumano-kodo/kumano-hongu-taisha','src_hongu_kanpai','Kanpai Japan'),
 L('https://www.lonelyplanet.com/points-of-interest/otorii/1612345','src_hongu_lp','Lonely Planet'),
 L('https://japantravel.navitime.com/en/area/jp/spot/02301-t1618/','src_hongu_navitime','NAVITIME'),
])+'. Hours, prices and availability change'
tail,n=re.subn(r'Sources verified at time of writing:.*?Hours, prices and availability change',lambda m:src,tail,flags=re.S); assert n==1
out=head+main+tail
assert not re.search('Gifu|Nobunaga|Kinka',re.sub(r'"mainEntity": \[.*','',out,flags=re.S)),re.findall('.{30}(?:Gifu|Nobunaga|Kinka).{20}',out)
open(D+'index.html','w',encoding='utf-8').write(out)
for tg in ['div','figure','picture','p','a','ul','li','details','section','h2']:
    assert len(re.findall(f'<{tg}[ >]',out))==len(re.findall(f'</{tg}>',out)),tg
for m in re.findall(r'<script type="application/ld\+json">(.*?)</script>',out,re.S): json.loads(m)
# OGP
im=Image.open(R+'images/og/og-guides-matsue-castle.jpg').convert('RGB'); d=ImageDraw.Draw(im)
d.rectangle([40,150,1170,380],fill=(252,240,242)); d.rectangle([1118,66,1160,96],fill=(252,240,242))
f1=ImageFont.truetype(glob.glob('/usr/share/fonts/**/DejaVuSerif-Bold.ttf',recursive=True)[0],48)
f2=ImageFont.truetype(glob.glob('/usr/share/fonts/**/NotoSerifCJK-Bold.ttc',recursive=True)[0],28,index=0)
l1="Kumano Hongu Taisha Guide:"; l2="The Shrine That Moved"; assert d.textlength(l1,font=f1)<1090
d.text((66,170),l1,font=f1,fill=(26,15,15)); d.text((66,238),l2,font=f1,fill=(26,15,15)); d.text((66,332),"熊野本宮大社",font=f2,fill=(138,125,120))
im.save(R+f'images/og/og-guides-{SL}.jpg',quality=88)
# hub thumb 640x400 from banners
b=Image.open(D+'images/banners.jpg'); w,h=b.size; ch=round(w*400/640); t=(h-ch)//2
th=b.crop((0,t,w,t+ch)).resize((640,400),Image.LANCZOS); th.save(R+'images/hub/kumano-hongu-taisha.jpg',quality=84); th.save(R+'images/hub/kumano-hongu-taisha.webp',quality=80)
print('built',len(out))
