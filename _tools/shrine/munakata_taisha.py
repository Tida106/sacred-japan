import re,json,os,glob,shutil
from PIL import Image,ImageDraw,ImageFont
R='/home/claude/sacred-japan/'; SL='munakata-taisha'; D=R+f'guides/{SL}/'
os.makedirs(D+'images',exist_ok=True); 
LIC={'by3':('CC BY 3.0','https://creativecommons.org/licenses/by/3.0/'),
     'by4':('CC BY 4.0','https://creativecommons.org/licenses/by/4.0/'),
     'by21jp':('CC BY 2.1 JP','https://creativecommons.org/licenses/by/2.1/jp/'),
     'cc0':('CC0 1.0','https://creativecommons.org/publicdomain/zero/1.0/'),
     'pd':('public domain','https://commons.wikimedia.org/wiki/Commons:Public_domain')}
def CS(t): return 'https://commons.wikimedia.org/w/index.php?search='+t.replace(' ','+')+'&title=Special:MediaSearch&type=image'
UP='/mnt/user-data/uploads/'
LIC['bysa4']=('CC BY-SA 4.0','https://creativecommons.org/licenses/by-sa/4.0/')

LIC['bysa3']=('CC BY-SA 3.0','https://creativecommons.org/licenses/by-sa/3.0/')
SORA='https://commons.wikimedia.org/wiki/User:%E3%81%9D%E3%82%89%E3%81%BF%E3%81%BF'
HAPO='https://commons.wikimedia.org/wiki/User:%E3%83%8F%E3%83%9D%E3%83%8B%E3%82%A2%E3%83%A9'
P={
'shinmon':('b85e749a','Soramimi','bysa4',SORA),
'hetsu-haiden':('d01366cf','Soramimi','bysa4',SORA),
'sorei':('831e7846','Soramimi','bysa4',SORA),
'nakatsu-torii':('e67d1046','Soramimi','bysa4',SORA),
'nakatsu-haiden':('275fce1d','ハポニアラ (Haponiara)','by4',HAPO),
}
for k,v in P.items():
    im=Image.open(UP+v[0]+'-image.jpg').convert('RGB')
    if im.width>1200: im=im.resize((1200,round(im.height*1200/im.width)),Image.LANCZOS)
    im.save(D+f'images/{k}.jpg',quality=84); im.save(D+f'images/{k}.webp',quality=80)

SIZE={k:Image.open(D+f'images/{k}.jpg').size for k in P}
def fig2(k,alt,cap,date,hero=False):
    u,a,l,cl=P[k]; ln,lu=LIC[l]; w,h=SIZE[k]
    if hero: st='margin:0 0 48px;'; ld='eager'; ims='style="width:100%;max-height:420px;object-fit:cover;border-radius:4px;display:block;"'
    else:
        mw=min(420 if h>w else 760,w)
        st='margin:28px auto;max-width:%dpx;'%mw; ld='lazy'; ims='style="width:100%;height:auto;border-radius:4px;display:block;"'
    lic=f'<a href="{lu}" target="_blank" rel="noopener">{ln}</a>'
    return f'''<figure style="{st}"><picture><source srcset="/guides/{SL}/images/{k}.webp" type="image/webp"><img src="/guides/{SL}/images/{k}.jpg" alt="{alt}" width="{w}" height="{h}" loading="{ld}" {ims}></picture><figcaption style="font-size:13px;color:var(--enshu);margin-top:10px;text-align:center;line-height:1.6;">{cap}.<br>Photo: <a href="{cl}" target="_blank" rel="noopener">{a}</a>{(', '+date) if date else ''}, {lic}, via Wikimedia Commons (resized)</figcaption></figure>
'''
fig=fig2
s=open(R+'guides/gifu-castle/index.html',encoding='utf-8').read()
i=s.index('<main>'); j=s.index('</main>'); head,tail=s[:i],s[j:]
TITLE="Munakata Taisha Guide: Three Shrines, a Forbidden Island and the Sea Goddesses of Fukuoka"
DESC="A licensed guide's guide to Munakata Taisha in Fukuoka: the three shrines of Hetsumiya, Nakatsumiya and Okitsumiya, the World Heritage island of Okinoshima that only priests may enter, the Shinpokan museum, the ferry to Oshima, the Grand Autumn Festival and how to get there."
TAG="Fukuoka's World Heritage shrine of the three sea goddesses: the mainland shrine, the island across the water and the island nobody may enter."
head=re.sub(r'<title>.*?</title>',f'<title>{TITLE} | Sacred Japan</title>',head,count=1)
head=re.sub(r'(<meta (?:name="description"|property="og:description"|name="twitter:description") content=")[^"]*(")',lambda m:m.group(1)+DESC+m.group(2),head)
head=re.sub(r'(<meta (?:property="og:title"|name="twitter:title") content=")[^"]*(")',lambda m:m.group(1)+TITLE+m.group(2),head)
head=re.sub(r'("headline": ")[^"]*(")',lambda m:m.group(1)+TITLE+m.group(2),head)
head=re.sub(r'("description": ")A licensed[^"]*(")',lambda m:m.group(1)+DESC+m.group(2),head)
head=re.sub(r'("date(?:Published|Modified)": ")[^"]*(")',lambda m:m.group(1)+'2026-11-25'+m.group(2),head)

head=re.sub(r'<meta name="keywords" content="[^"]*">','<meta name="keywords" content="Munakata Taisha, Munakata Shrine, Okinoshima, Hetsumiya, Nakatsumiya, Okitsumiya, Fukuoka shrine, World Heritage Japan, Oshima ferry, Shinpokan, three Munakata goddesses">',head)
head=head.replace('guides/gifu-castle',f'guides/{SL}').replace('guide_gifu_castle_','guide_munakata_').replace('og-guides-gifu-castle',f'og-guides-{SL}')
head=head.replace('岐阜城','宗像大社').replace('Gifu Castle','Munakata Taisha')
head=re.sub(r"<h1>.*?</h1>","<h1><em>Munakata Taisha</em>: Three Shrines, a Forbidden Island and the Sea Goddesses of Fukuoka</h1>",head,count=1,flags=re.S)
head=head.replace("Nobunaga's mountain castle above Gifu, with the keep closed until late 2027.",TAG)
head=head.replace('SACRED JAPAN GUIDES ／ 城','SACRED JAPAN GUIDES ／ 神社')
IL='class="inline-link"'
def a(u,t,ev): return f'<a href="{u}" {IL} onclick="trackEvent(\'click\',\'internal\',\'guide_munakata_to_{ev}\')">{t}</a>'

faqs=[
("What is Munakata Taisha?","A set of three shrines that worship three goddesses: Tagorihime at Okitsumiya on the island of Okinoshima, Tagitsuhime at Nakatsumiya on Oshima island, and Ichikishimahime at Hetsumiya on the Kyushu mainland (Nippon.com). Nippon.com calls them daughters of Amaterasu and Susanoo. The shrines, the island and nearby tombs were inscribed as a UNESCO World Heritage Site in 2017."),
("Can I visit Okinoshima?","No. The island is closed to the public, and only priests of Munakata Taisha may land, after purifying themselves by bathing in the sea (MLIT). Japan-guide says the one chance for outsiders used to be an annual festival in May, with selected male visitors who undressed and purified themselves in the sea first; I could not confirm whether that still happens."),
("How can I see Okinoshima, then?","On a clear day you can see it from Okitsumiya Yohaisho on Oshima, a hall for praying toward the island (MLIT, GLTJP). Many of the ritual objects found on Okinoshima are shown at the Shinpokan Museum at Hetsumiya (MLIT)."),
("How much is the Shinpokan Museum?","Adults 800 yen, high school and university students 500 yen, and elementary and junior high school students 400 yen. Hours are 9:00 to 16:30 with last entry at 16:00, and it is open all year (the museum&rsquo;s page, GLTJP). Groups of 20 or more and visitors over 65 get 200 yen off (okinoshima-heritage.jp)."),
("How do I get to Hetsumiya and to Oshima?","Take a train to JR Togo Station, then a bus toward Konominato. Japan-guide gives about 10 minutes and 260 yen to the Munakata Taisha-mae stop, and an MLIT regional page gives about 12 minutes. Buses run about once an hour. For Oshima, continue to Konominato Port (20 minutes, 410 yen) and take the ferry, which runs every 1&ndash;2 hours, takes 15&ndash;25 minutes and costs 570 yen one way (japan-guide)."),
("When is the main festival?","The Grand Autumn Festival runs from 1 to 3 October each year and is the most important ritual of Munakata Taisha. It opens with the Miare Festival, in which boats carry portable shrines of Tagorihime and Tagitsuhime to Hetsumiya, where the three goddesses meet (okinoshima-heritage.jp, Government of Japan)."),
]

faq_json=',\n'.join("""    {
      "@type": "Question",
      "name": %s,
      "acceptedAnswer": {
        "@type": "Answer",
        "text": %s
      }
    }"""%(json.dumps(re.sub('<[^>]+>','',q)),json.dumps(re.sub('&ldquo;|&rdquo;','"',re.sub('&rsquo;','’',re.sub('&ndash;','-',re.sub('<[^>]+>','',a_)))))) for q,a_ in faqs)
head=re.sub(r'("mainEntity": \[\n).*?(\n  \]\n\}\n</script>\n\n<!-- ── GOOGLE)',lambda m:m.group(1)+faq_json+m.group(2),head,flags=re.S)
hh=re.sub(r'"mainEntity": \[.*','',head,flags=re.S)
assert not re.search('Gifu|Nobunaga|castle|Castle',re.sub(r'<nav>.*?</nav>','',hh,flags=re.S).replace('Castles','')),re.findall('.{30}(?:Gifu|Nobunaga|astle).{20}',hh)

main="""<main>

"""+fig('shinmon','Green copper-roofed gate at Hetsumiya with a stone pillar and stone lanterns in front, visitors walking toward the worship hall beyond','The Shinmon gate at Hetsumiya, with the worship hall beyond',"",hero=True)+"""
  <aside class="toc" aria-label="Table of contents">
    <div class="toc-label">TABLE OF CONTENTS ／ 目次</div>
    <div class="toc-title">In This Guide</div>
    <ol>
      <li><a href="#opening">A Shrine in Three Places</a></li>
      <li><a href="#three">Three Shrines, Three Goddesses</a></li>
      <li><a href="#hetsumiya">Hetsumiya: The Shrine You Can Walk To</a></li>
      <li><a href="#oshima">Nakatsumiya and the Ferry to Oshima</a></li>
      <li><a href="#okinoshima">Okinoshima: The Island Nobody May Enter</a></li>
      <li><a href="#festival">The Grand Autumn Festival</a></li>
      <li><a href="#visit">Visiting Munakata Taisha</a></li>
      <li><a href="#faq">Frequently Asked Questions</a></li>
      <li><a href="#final">Before You Go</a></li>
    </ol>
  </aside>

  <article>

    <p class="opening" id="opening">As a licensed guide, I like shrines that leave something out on purpose. Munakata Taisha in Fukuoka is one shrine in three places, and the most important place is an island that you are not allowed to set foot on.</p>
    <p>Only priests may land on Okinoshima, and they must bathe in the sea first. The other two shrines are open: Hetsumiya on the mainland, where you can walk in, and Nakatsumiya on the island of Oshima, a short ferry ride away. This guide covers how the three fit together, what to look for at each, and the practical side: a museum fee, a bus, a ferry and an October festival.</p>

    <h2 id="three">Three Shrines, Three Goddesses<span class="h2-jp">三宮と三女神</span></h2>
    <p>Nippon.com explains the arrangement. Okitsumiya, on Okinoshima in the middle of the Genkai Sea, worships Tagorihime. Nakatsumiya, on the island of Oshima, worships Tagitsuhime. Hetsumiya, on the Kyushu mainland at Tajima, worships Ichikishimahime. The three are described as daughters of Amaterasu and Susanoo, whose story is part of our """+a('/culture/japanese-mythology/','Japanese mythology guide','mythology')+""".</p>
    <p>The line of shrines runs out across the sea toward Korea. Japan-guide says Okinoshima lies about a third of the way to Busan and has been a place to pray for safe travel since the fourth century. The Government of Japan describes ancient Yamato traffic across the Genkai Sea using the island as a kind of guidepost. The World Heritage council&rsquo;s leaflet says the goddesses were originally guardians of the ships that used those routes.</p>
    <p>The whole group was inscribed as a UNESCO World Heritage Site in 2017 as the Sacred Island of Okinoshima and Associated Sites in the Munakata Region. MLIT says it includes the three shrines, the island and about 40 ancient burial mounds of the Munakata family, which governed the area.</p>

    <h2 id="hetsumiya">Hetsumiya: The Shrine You Can Walk To<span class="h2-jp">辺津宮</span></h2>
    <p>Japan.travel calls Hetsumiya the largest and the easiest to visit of the three shrines. Free parking is provided on the grounds (japan-guide), and the Shinpokan Museum stands within them. The photos show the way in.</p>
    <p>The gate in the photo at the top of this page is the Shinmon, with a green copper roof and heavy dark pillars. A stone lantern on each side is marked with the characters for &ldquo;offered light&rdquo;, and a tall stone pillar at the left reads, as I read it, that members of the imperial family dismount here. Beyond the gate, visitors walk toward the worship hall. The gate frames a view of the worship hall&rsquo;s gable.</p>
"""+fig('hetsu-haiden','The Hetsumiya worship hall with a thick twisted shimenawa rope with white paper streamers across its front, a green copper roof over the porch, an offering box with a gold crest and an omikuji stand at the right','The worship hall at Hetsumiya, with its thick shimenawa',"")+"""
    <p>The worship hall is the centre of a visit. A thick twisted rope hangs across the front with white paper streamers, and a green copper roof covers the porch. On the gable above, the plaque reads, as I read it, 宗像宮, the shrine&rsquo;s name. The offering box in front carries a round gold crest that looks like a chrysanthemum. An omikuji stand and a rack of wooden ema stand at the sides.</p>
"""+fig('sorei','A small wooden shrine hall with latticed doors, a rope across the front, a stone lantern on each side and an ornamental ridge end','A small shrine on the grounds, titled Sorei Shrine on Commons',"")+"""
    <p>Commons titles this small shrine the Munakata Sorei Shrine, on the grounds of Hetsumiya. It has latticed doors, a rope across the front, a stone lantern on each side marked with the characters for &ldquo;dedicated&rdquo;, and a carved ornament at the ridge. I could not find who is enshrined here, so check the notice board on site.</p>
    <p>Do not skip the museum. The Shinpokan holds a large part of what was found on Okinoshima: MLIT says there are around 80,000 ritual objects and treasures, and many are on display here. GLTJP describes the collection as National Treasures. Admission and hours are in the practical list below.</p>

    <h2 id="oshima">Nakatsumiya and the Ferry to Oshima<span class="h2-jp">中津宮と大島</span></h2>
    <p>Japan.travel says Oshima lies about 10 kilometres off the coast. The ferry runs from Konominato Port every one or two hours, takes 15 to 25 minutes and costs 570 yen one way (japan-guide). Japan.travel adds that the present shrine buildings go back to the 16th century.</p>
"""+fig('nakatsu-torii','The stone torii at the entrance to Nakatsumiya on Oshima with two komainu on pedestals, a red railing, a flight of stone steps, a Japanese flag and a bicycle in front','The entrance to Nakatsumiya, a stone torii above a flight of steps',"")+"""
    <p>The entrance has a stone torii at the head of a broad flight of steps, with a red railing on each side and a komainu on a pedestal marked with the characters for &ldquo;offered&rdquo;. A tall stone pillar at the left carries the shrine&rsquo;s name. As I read the inscriptions on the torii&rsquo;s own pillars, they refer to the Meiji 37&ndash;38 years and to a war-service memorial by the reservists of Oshima village, so this gate seems to date from after the Russo-Japanese War; I could not confirm that. A Japanese flag flies beside it and a bicycle leans in front, which gives the place a lived-in feel.</p>
"""+fig('nakatsu-haiden','The Nakatsumiya worship hall seen from the front, with a twisted shimenawa and white streamers across its open porch, a drum at the left, an offering box in front and a plaque on the back wall','The worship hall at Nakatsumiya, with a drum inside',"")+"""
    <p>The worship hall at Nakatsumiya is open at the front, with a thick twisted rope and white paper streamers across it. Inside there is a drum at the left, a wooden offering box in front and a dark plaque on the back wall whose characters I can only partly read. A border of purple-grey pebbles runs along the base.</p>
    <p>The island also has Okitsumiya Yohaisho, a hall for praying toward Okinoshima. It sits at the foot of a mountain on the north side of the island, and on a clear day you can see Okinoshima from here (MLIT, japan.travel). MLIT says the hall itself is opened only a few times a year, including at the spring and autumn festivals, and a path leads up to a viewing area above it. GLTJP and japan.travel present it as a place to pray, so check what is open on the day. Oshima Koryukan, a small museum about the island, is also here (MLIT).</p>

    <h2 id="okinoshima">Okinoshima: The Island Nobody May Enter<span class="h2-jp">沖ノ島</span></h2>
    <p>The island is about 60 kilometres off the coast according to japan-guide and MLIT, and about 50 according to Nippon.com, so I would say roughly 50 to 60 kilometres. The whole island is the shrine. Only priests of Munakata Taisha are allowed to visit, and before they step ashore they purify themselves by bathing in the sea, a rite called misogi (MLIT).</p>
    <p>That ban is the reason the island matters. MLIT says the strict taboo has kept the heritage exceptionally well preserved and gives a valuable record of the rituals performed there, which is why it earned World Heritage status. Nippon.com dates the cultural exchange it documents to the fourth to ninth centuries.</p>
    <p>You cannot go, but you can look: from Oshima on a clear day, and through the objects at the Shinpokan.</p>

    <h2 id="festival">The Grand Autumn Festival<span class="h2-jp">秋季大祭とみあれ祭</span></h2>
    <p>The Grand Autumn Festival runs from 1 to 3 October and is the most important ritual of Munakata Taisha (okinoshima-heritage.jp). It begins with the Miare Festival, when special boats carry portable shrines of Tagorihime and Tagitsuhime across the sea to Hetsumiya. The Government of Japan describes the festival as the time when the three goddesses come together there. Fishing boats join the procession on the Genkai Sea with their banners flying, which the heritage site calls a magnificent sight.</p>
    <p>If your dates allow it, October is the time to go. Check the shrine&rsquo;s own schedule for the exact times and any viewing arrangements before you plan around it.</p>

    <h2 id="visit">Visiting Munakata Taisha<span class="h2-jp">参拝案内</span></h2>
    <ul class="practical-list">
      <li><strong>Address (Hetsumiya):</strong> 2331 Tajima, Munakata, Fukuoka (some sources spell it Tashima). Phone 0940-62-1311.</li>
      <li><strong>By train and bus:</strong> JR Kagoshima Line to Togo Station (from Kokura, per japan.travel), then a bus toward Konominato to the Munakata Taisha-mae stop: about 10 minutes and 260 yen (japan-guide) or 12 minutes (MLIT). A 2019 MLIT regional page also lists about 62 minutes by Nishitetsu bus from Tenjin in Fukuoka.</li>
      <li><strong>By car:</strong> about 20 minutes from Wakamiya Interchange on the Kyushu Expressway, with free parking at Hetsumiya (the museum&rsquo;s page).</li>
      <li><strong>Hours:</strong> prayer reception 9:00 to 17:00 except at New Year (NAVITIME); one older English page lists 6:00 to 17:00 for the grounds. Check before you go. Entry to the grounds is free (GLTJP).</li>
      <li><strong>Shinpokan Museum:</strong> 9:00 to 16:30, last entry 16:00, open all year; adults 800 yen, students 500 yen, children 400 yen (the museum&rsquo;s page, GLTJP).</li>
      <li><strong>Oshima:</strong> ferry from Konominato Port, 15&ndash;25 minutes, 570 yen one way, every 1&ndash;2 hours; bus from Togo to Konominato takes 20 more minutes and costs 410 yen (japan-guide). A car on the ferry costs about 5,000 yen one way.</li>
      <li><strong>Also nearby:</strong> a self-guided tour of the World Heritage components is described at okinoshima-heritage.jp.</li>
      <li><strong>Related:</strong> our """+a('/guides/itsukushima-shrine/','Itsukushima Shrine guide','itsukushima')+""" covers another famous sea shrine, and our """+a('/guides/dazaifu-tenmangu/','Dazaifu Tenmangu guide','dazaifu')+""" covers another Fukuoka shrine.</li>
    </ul>
    <div class="key-callout">
      <p>&#127890; <strong>Plan your trip:</strong> Browse guided tours or find a stay in Fukuoka. <a href="https://www.viator.com/search/Fukuoka?pid=P00298374&amp;mcid=42383&amp;medium=link&amp;campaign=sacred-japan" target="_blank" rel="noopener" onclick="trackEvent('click','affiliate','viator_munakata')">Book a Tour</a></p>
    </div>

    <h2 id="faq">Frequently Asked Questions<span class="h2-jp">よくあるご質問</span></h2>
    <div class="faq-stack">
"""+''.join(f"""    <details class="faq-item">
        <summary>{q}</summary>
        <div class="faq-answer">{a_}</div>
    </details>
""" for q,a_ in faqs)+"""    </div>

    <h2 id="final">Before You Go<span class="h2-jp">むすびに</span></h2>
    <p>Start at Hetsumiya and see the objects in the museum. If you have time, take the ferry to Oshima and look out toward the island nobody may enter. If you want crowds and boats, go in early October. Whatever you choose, check the current times and fares first.</p>

    <div class="closing-block">
      <span class="torii">&#9961;&#65039;</span>
      <p>One shrine in three places, and the most sacred of them is the one you can only look at from across the water.</p>
    </div>

    <section class="related-section">
      <h2>Related Guides</h2>
      <span class="h2-jp">関連ガイド</span>
      <div class="related-grid">
        <a class="related-card" href="/guides/itsukushima-shrine/" onclick="trackEvent('click','internal','related_munakata_to_itsukushima')">
          <div class="related-card-label">SACRED JAPAN ／ GUIDES</div>
          <div class="related-card-title">&#9961;&#65039; Itsukushima Shrine &rarr;</div>
          <div class="related-card-desc">The famous shrine standing in the sea.</div>
        </a>
        <a class="related-card" href="/culture/japanese-mythology/" onclick="trackEvent('click','internal','related_munakata_to_mythology')">
          <div class="related-card-label">SACRED JAPAN ／ CULTURE</div>
          <div class="related-card-title">&#128214; Japanese Mythology &rarr;</div>
          <div class="related-card-desc">Amaterasu, Susanoo and the shrines of the old stories.</div>
        </a>
        <a class="related-card" href="/guides/dazaifu-tenmangu/" onclick="trackEvent('click','internal','related_munakata_to_dazaifu')">
          <div class="related-card-label">SACRED JAPAN ／ GUIDES</div>
          <div class="related-card-title">&#9961;&#65039; Dazaifu Tenmangu &rarr;</div>
          <div class="related-card-desc">Fukuoka&rsquo;s shrine of the scholar who became a god.</div>
        </a>
      </div>
    </section>

  </article>

"""

tail=tail.replace('gifu-castle',SL).replace('gifu_castle','munakata').replace('DGifu','DFukuoka').replace('search/Gifu','search/Fukuoka')
def L(u,l,t): return f'<a href="{u}" target="_blank" rel="noopener" style="color:var(--beni);text-decoration:underline;" onclick="trackEvent(\'click\',\'external\',\'{l}\')">{t}</a>'
src='Sources verified at time of writing: '+', '.join([
 L('https://munakata-taisha.or.jp/shimpokan_en.html','src_mk_official','Munakata Taisha (museum page)'),
 L('https://www.nippon.com/en/guide-to-japan/gu009008/','src_mk_nippon','Nippon.com'),
 L('https://japan-guide.com/e/e4840.html','src_mk_jg','japan-guide'),
 L('https://www.gltjp.com/en/directory/item/12874/','src_mk_gltjp','GLTJP'),
 L('https://www.japan.travel/en/spot/271/','src_mk_jt','Japan Travel'),
 L('https://www.mlit.go.jp/tagengo-db/en/R1-00736.html','src_mk_mlit','MLIT'),
 L('https://okinoshima-heritage.jp/en/visit','src_mk_heritage','okinoshima-heritage.jp'),
 L('https://www.gov-online.go.jp/eng/publicity/book/hlj/html/201804/201804_08_en.html','src_mk_gov','Government of Japan'),
 L('https://japantravel.navitime.com/en/area/jp/spot/02301-1600220/','src_mk_navitime','NAVITIME'),
])+'. Hours, prices and availability change'
tail,n=re.subn(r'Sources verified at time of writing:.*?Hours, prices and availability change',lambda m:src,tail,flags=re.S); assert n==1

out=head+main+tail
assert not re.search('Gifu|Nobunaga|Kinka',re.sub(r'"mainEntity": \[.*','',out,flags=re.S))
open(D+'index.html','w',encoding='utf-8').write(out)
for tg in ['div','figure','picture','p','a','ul','li','details','section','h2']:
    assert len(re.findall(f'<{tg}[ >]',out))==len(re.findall(f'</{tg}>',out)),tg
for m in re.findall(r'<script type="application/ld\+json">(.*?)</script>',out,re.S): json.loads(m)
im=Image.open(R+'images/og/og-guides-matsue-castle.jpg').convert('RGB'); d=ImageDraw.Draw(im)
d.rectangle([40,150,1170,380],fill=(252,240,242)); d.rectangle([1118,66,1160,96],fill=(252,240,242))
f1=ImageFont.truetype(glob.glob('/usr/share/fonts/**/DejaVuSerif-Bold.ttf',recursive=True)[0],48)
f2=ImageFont.truetype(glob.glob('/usr/share/fonts/**/NotoSerifCJK-Bold.ttc',recursive=True)[0],28,index=0)
l1="Munakata Taisha Guide:"; l2="Three Shrines, One Sacred Isle"; assert d.textlength(l2,font=f1)<1090
d.text((66,170),l1,font=f1,fill=(26,15,15)); d.text((66,238),l2,font=f1,fill=(26,15,15)); d.text((66,332),"宗像大社",font=f2,fill=(138,125,120))
im.save(R+f'images/og/og-guides-{SL}.jpg',quality=88)
b=Image.open(D+'images/shinmon.jpg'); w,h=b.size; ch=round(w*400/640); t=max(0,(h-ch)//2)
th=b.crop((0,t,w,t+ch)).resize((640,400),Image.LANCZOS); th.save(R+f'images/hub/{SL}.jpg',quality=84); th.save(R+f'images/hub/{SL}.webp',quality=80)
print('built',len(out))
