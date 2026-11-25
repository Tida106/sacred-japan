import re,json,os,glob,shutil
from PIL import Image,ImageDraw,ImageFont
R='/home/claude/sacred-japan/'; SL='mitsumine-jinja'; D=R+f'guides/{SL}/'
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
LIC['bysa2']=('CC BY-SA 2.0','https://creativecommons.org/licenses/by-sa/2.0/')
CAR='https://web.archive.org/web/2016%s/http://www.panoramio.com/photo/%s'
P={
'zuishin-snow':('f3443684','Carbonium','by3',CAR%('1028004010','101499236')),
'mitsu-torii':('c1dd97f1','Carbonium','by3',CAR%('1028155104','101499220')),
'zuishin-path':('ca5fb159','Manabu Itoh','bysa2','https://www.flickr.com/photos/s_freesia/30675788836/'),
'gate-dragons':('ea157e95','Carbonium','by3',CAR%('1028072108','101499280')),
'haiden-front':('95361e94','NY066','bysa3','https://commons.wikimedia.org/wiki/User:NY066'),
'haiden-trees':('0766bc65','Carbonium','by3',CAR%('1028072217','101499285')),
'haiden-carving':('899b2ee3','Carbonium','by3',CAR%('1029171719','101499290')),
'corner':('547d2de0','Adachi Masayuki','bysa3','https://web.archive.org/web/20161023210441/http://www.panoramio.com/photo/61736777'),
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
TITLE="Mitsumine Shrine Guide: Wolf Guardians, the Triple Torii and Chichibu's Mountain Shrine"
DESC="A licensed guide's guide to Mitsumine Shrine in Chichibu, Saitama: the legend of Yamato Takeru, the wolf guardians known as Oinu-sama, the triple torii, the carved Zuishinmon and worship hall, the bus from Seibu-Chichibu, the treasure hall and the hiking route."
TAG="A mountain shrine in Chichibu where wolves stand guard in place of the usual stone dogs, behind a triple torii and a gate carved in red and gold."
head=re.sub(r'<title>.*?</title>',f'<title>{TITLE} | Sacred Japan</title>',head,count=1)
head=re.sub(r'(<meta (?:name="description"|property="og:description"|name="twitter:description") content=")[^"]*(")',lambda m:m.group(1)+DESC+m.group(2),head)
head=re.sub(r'(<meta (?:property="og:title"|name="twitter:title") content=")[^"]*(")',lambda m:m.group(1)+TITLE+m.group(2),head)
head=re.sub(r'("headline": ")[^"]*(")',lambda m:m.group(1)+TITLE+m.group(2),head)
head=re.sub(r'("description": ")A licensed[^"]*(")',lambda m:m.group(1)+DESC+m.group(2),head)
head=re.sub(r'("date(?:Published|Modified)": ")[^"]*(")',lambda m:m.group(1)+'2026-11-25'+m.group(2),head)


head=re.sub(r'<meta name="keywords" content="[^"]*">','<meta name="keywords" content="Mitsumine Shrine, Mitsumine Jinja, Chichibu shrine, wolf shrine Japan, Oinu-sama, Mitsu-torii, triple torii, Yamato Takeru, Saitama shrine, Seibu-Chichibu bus, power spot Kanto">',head)
head=head.replace('guides/gifu-castle',f'guides/{SL}').replace('guide_gifu_castle_','guide_mitsumine_').replace('og-guides-gifu-castle',f'og-guides-{SL}')
head=head.replace('岐阜城','三峯神社').replace('Gifu Castle','Mitsumine Shrine')
head=re.sub(r"<h1>.*?</h1>","<h1><em>Mitsumine Shrine</em>: Wolf Guardians, the Triple Torii and Chichibu\\'s Mountain Shrine</h1>",head,count=1,flags=re.S)
head=head.replace("Nobunaga's mountain castle above Gifu, with the keep closed until late 2027.",TAG)
head=head.replace('SACRED JAPAN GUIDES ／ 城','SACRED JAPAN GUIDES ／ 神社')
IL='class="inline-link"'
def a(u,t,ev): return f'<a href="{u}" {IL} onclick="trackEvent(\'click\',\'internal\',\'guide_mitsumine_to_{ev}\')">{t}</a>'

faqs=[
("Who founded Mitsumine Shrine, and who is enshrined?","Tradition says Prince Yamato Takeru founded it on his campaign to the east, and that he dedicated it to the creator couple Izanagi and Izanami (Chichibu Omotenashi, MLIT). The founding date is legendary, and sources vary: about the first century (MLIT), about 1,900 years ago (JAL Japan Travel), or the second century (Japan Experience). Treat it as tradition, not documented history."),
("Why are there wolves instead of the usual stone dogs?","Mitsumine worships the Japanese wolf, now extinct, as a guardian against misfortune, and two stone wolves stand at the entrance in place of komainu (japan-guide). Chichibu Omotenashi says the practice goes back to 1720, when the priest Nikko Hoin saw wolves on the mountaintop, took them as an omen and began distributing wolf amulets against fire, robbery and crop damage."),
("How do I get to Mitsumine Shrine?","Take a bus from Seibu-Chichibu Station to the last stop, Mitsumine-jinja: about 75 minutes and 950 yen (japan-guide, JAL Japan Travel). From Mitsumineguchi Station it takes about 55 minutes and 690 yen (japan-guide). Buses are infrequent, so check the timetable first. The ropeway that once served the shrine stopped running in 2006 (Japan Visitor)."),
("What are the opening hours and fees?","Japan-guide gives 6:30 to 17:00 for the shrine, with no closing days and free entry. Other pages, including GLTJP and ANA, give 9:00 to 17:00 for the shrine office. The small treasure hall costs 300 yen, opens 9:00 to 16:00 and is closed on Tuesdays and from December to March (japan-guide). A goshuin with a wolf design is 500 yen (GLTJP)."),
("Can I hike up instead of taking the bus?","Yes. Take the bus to the Owa stop, where the trailhead is, and climb for about three hours on a steep, rocky dirt trail; proper footwear is needed (japan-guide). The Chichibu Omotenashi site describes the main approach trail on Mt. Mitsumine."),
("Can I stay overnight?","Japan Experience mentions the shrine&rsquo;s own hotel, with an onsen, and Chichibu Omotenashi says many visitors stay at K&#333;unkaku, a hot-spring inn near the shrine. I did not check availability, so book directly."),
]

faq_json=',\n'.join("""    {
      "@type": "Question",
      "name": %s,
      "acceptedAnswer": {
        "@type": "Answer",
        "text": %s
      }
    }"""%(json.dumps(re.sub('<[^>]+>','',q)),json.dumps(re.sub('&#333;','ō',re.sub('&ldquo;|&rdquo;','"',re.sub('&rsquo;','’',re.sub('&ndash;','-',re.sub('<[^>]+>','',a_))))))) for q,a_ in faqs)
head=re.sub(r'("mainEntity": \[\n).*?(\n  \]\n\}\n</script>\n\n<!-- ── GOOGLE)',lambda m:m.group(1)+faq_json+m.group(2),head,flags=re.S)
hh=re.sub(r'"mainEntity": \[.*','',head,flags=re.S)
assert not re.search('Gifu|Nobunaga|castle|Castle',re.sub(r'<nav>.*?</nav>','',hh,flags=re.S).replace('Castles','')),re.findall('.{30}(?:Gifu|Nobunaga|astle).{20}',hh)

main="""<main>

"""+fig('zuishin-snow','The vermilion Zuishinmon gate with gold carving and a black plaque, two wolf statues in purple cloth on pedestals and snow on the ground, visitors passing through','The Zuishinmon gate in snow, with wolves in purple cloth',"January 2014",hero=True)+"""
  <aside class="toc" aria-label="Table of contents">
    <div class="toc-label">TABLE OF CONTENTS ／ 目次</div>
    <div class="toc-title">In This Guide</div>
    <ol>
      <li><a href="#opening">Where the Wolves Stand Guard</a></li>
      <li><a href="#legend">Yamato Takeru and the Three Peaks</a></li>
      <li><a href="#wolves">Oinu-sama: The Wolf Guardians</a></li>
      <li><a href="#approach">The Triple Torii and the Zuishinmon</a></li>
      <li><a href="#haiden">The Worship Hall and Its Carvings</a></li>
      <li><a href="#visit">Visiting Mitsumine Shrine</a></li>
      <li><a href="#faq">Frequently Asked Questions</a></li>
      <li><a href="#final">Before You Go</a></li>
    </ol>
  </aside>

  <article>

    <p class="opening" id="opening">As a licensed guide, I notice what a shrine puts at its gate. Most have a pair of stone dogs; at Mitsumine Shrine in Chichibu, it is wolves, and the whole place is built around them.</p>
    <p>It sits high in the mountains of western Saitama, behind a rare triple torii, with a vermilion gate and a worship hall carved and painted in red, gold, blue and green. Getting there takes a long bus ride, which is part of why it feels removed from the city. This guide covers the founding legend, the wolf worship, what to look for in each building, and the practical side: buses, hours, the treasure hall and the hiking route.</p>

    <h2 id="legend">Yamato Takeru and the Three Peaks<span class="h2-jp">日本武尊と三峯</span></h2>
    <p>According to the story told by Chichibu Omotenashi, Prince Yamato Takeru, a son of Emperor Keiko, climbed a ridge while subduing clans in the east, was struck by the view and dedicated the place to Izanagi and Izanami, the creator couple of the myths. The emperor then named it Mitsumine, &ldquo;three peaks&rdquo;. Our """+a('/culture/japanese-mythology/','Japanese mythology guide','mythology')+""" tells more about the pair.</p>
    <p>The date is legendary, and sources vary. MLIT says about the first century, JAL Japan Travel says about 1,900 years ago, and Japan Experience says the second century. Japan Travel also notes that whether Yamato Takeru existed is debated. I would present it as the shrine&rsquo;s tradition.</p>

    <h2 id="wolves">Oinu-sama: The Wolf Guardians<span class="h2-jp">御眷属（おいぬ様）</span></h2>
    <p>Japan-guide says the shrine worships the Japanese wolf, now extinct, as a guardian against misfortune, and that two stone wolves stand at the entrance in place of the usual komainu. JAL Japan Travel retells the founding story with a white wolf that guided the lost prince out of the forest.</p>
    <p>The date the wolf cult took off is better documented. Chichibu Omotenashi says that in 1720 the priest Nikko Hoin saw wolves on the mountaintop, took them for an omen from the mountain&rsquo;s deity and began handing out wolf amulets against fire, robbery and crop damage. GLTJP adds that wolves appear on the amulets and goshuin seals, which makes them popular for their rarity. Japan-guide says a small treasure hall to the left of the torii shows the history of the shrine, wolves and wolf pelts, and documents on the imperial family&rsquo;s link to the shrine.</p>

    <h2 id="approach">The Triple Torii and the Zuishinmon<span class="h2-jp">三ツ鳥居と随身門</span></h2>
"""+fig('mitsu-torii','A white triple torii with gold fittings and a green and gold plaque, two stone wolves on pedestals engraved with characters, a banner of new year greetings and visitors walking up the path','The Mitsu-torii in winter, with a wolf on each side',"January 2014")+"""
    <p>Japan-guide calls the entrance a rare triple torii, the Mitsu-torii: one large gate with a smaller one attached on each side. In the photo the posts are white with gold fittings, and the plaque reads Mitsumine Jinja. A stone wolf sits on a pedestal on each side, engraved, as I read them, with the characters for &ldquo;boundless&rdquo; and &ldquo;divine virtue&rdquo;. A banner of new year greetings stands beside the gate, so this was taken in early January. Visitors walk up the path beyond.</p>
"""+fig('zuishin-path','A vermilion gate at the end of a gravel path lined on both sides with rows of stone lanterns inscribed with donors names, with tall cedar trees and visitors walking toward it','The path to the Zuishinmon, lined with stone lanterns',"November 2016")+"""
    <p>The path to the gate runs between rows of stone lanterns carved with donors&rsquo; names, under tall cedars. The red gate at the end carries a black plaque reading, as I read it, Mitsumine-san. The photo is from November, when the mountain trees start to turn.</p>
"""+fig('gate-dragons','Dragon carvings in green, red and white projecting from under the eaves of the gate, with a red-painted ceiling edged in gold','Painted dragons under the eaves of the gate',"January 2014")+"""
    <p>Look up under the eaves. Dragons with green scales and red-and-white striped bodies reach out from the brackets, and the ceiling is red with gold edging. Japan-guide says the Zuishinmon and the worship hall have ornate, brightly coloured carvings of creatures and flowers. Chichibu Omotenashi says the main gate was relacquered in 2002, though it does not say that this is the Zuishinmon, so I have not tied the date to this photo.</p>

    <h2 id="haiden">The Worship Hall and Its Carvings<span class="h2-jp">拝殿と彫刻</span></h2>
"""+fig('haiden-front','The front of the worship hall above a flight of stone steps, with a curved gable, gold fittings, verdigris-green lanterns on both sides, a plaque reading Mitsumine Jinja and a sign on the stairs','The worship hall seen from the stone steps',"September 2011")+"""
    <p>At the top of the steps stands the worship hall, with a curving gable, gold fittings and a plaque reading Mitsumine Jinja. Two verdigris-green lanterns flank the entrance, and the posts of the steps are inscribed with donors&rsquo; names. Japan-guide compares the shrine&rsquo;s richness to a handful of places in Japan, including Nikko&rsquo;s Toshogu, which our """+a('/guides/nikko-toshogu/','Nikko Toshogu guide','nikko')+""" covers. Chichibu Omotenashi says the worship hall and main sanctuary were renovated in 1964, though it does not give their names.</p>
"""+fig('haiden-trees','The worship hall seen past a large cedar trunk with a straw rope tied around it, a small roofed shrine in the foreground with stacked clay cups, and colourful carving beneath the roof','The hall past a rope-wrapped cedar',"January 2014")+"""
    <p>A huge cedar with a straw rope tied around it stands in front of the hall. In the foreground, a small stand holds stacked clay cups with painted faces; I could not find what they are for. Beneath the roof, the colour and carving continue across the whole front. Chichibu Geo mentions an 800-year-old sacred tree on the grounds, but I cannot say whether this is that tree.</p>
"""+fig('haiden-carving','Brightly coloured carved figures, animals and plants stacked along the beams under the eaves of the worship hall, with a plaque reading Mitsumine Jinja at the left and a new year banner at the center','Carvings under the eaves of the hall',"January 2014")+"""
    <p>This is the close-up that explains why people make the trip. Figures, lions, fruit and waves are carved in layers along the beams and painted in blue, red, green and gold. A new year banner stands at the center. I have not tried to name the figures.</p>
"""+fig('corner','The corner of an ornate red, black and gold building with a vermilion railing, carved beams and a pillar with gold roundels, with autumn leaves at the right','The corner of an ornate hall, with a vermilion railing',"November 2011")+"""
    <p>The source I used labels this building the shrine office, but its carving and gold roundels look to me like the worship hall, so treat the label with caution. What is clear is the colour: red railing, black pillars, gold fittings and carved beams under a deep roof, with orange leaves behind.</p>

    <h2 id="visit">Visiting Mitsumine Shrine<span class="h2-jp">参拝案内</span></h2>
    <ul class="practical-list">
      <li><strong>Address:</strong> 298-1 Mitsumine, Chichibu, Saitama 369-1902. Phone 0494-55-0241 (GLTJP).</li>
      <li><strong>By bus:</strong> from Seibu-Chichibu Station to the last stop, Mitsumine-jinja: about 75 minutes and 950 yen (japan-guide); Tokyo Cheapo says about 80. From Mitsumineguchi Station: about 55 minutes and 690 yen (japan-guide). ANA gives about 90 minutes for the express bus from Seibu-Chichibu, so check the timetable.</li>
      <li><strong>From Tokyo:</strong> JAL Japan Travel says the Seibu Line express from Ikebukuro to Seibu-Chichibu takes about 90 minutes; Japan Experience says the Red Arrow takes about 78.</li>
      <li><strong>No ropeway:</strong> the ropeway that used to serve the shrine stopped running in 2006 (Japan Visitor).</li>
      <li><strong>Hours:</strong> 6:30 to 17:00, no closing days, free entry (japan-guide). GLTJP and ANA give 9:00 to 17:00 for the shrine office; goshuin 500 yen (GLTJP).</li>
      <li><strong>Treasure hall:</strong> 9:00 to 16:00, 300 yen, closed Tuesdays and from December to March (japan-guide).</li>
      <li><strong>Time to allow:</strong> 45 to 90 minutes at the shrine (japan-guide); the bus ride is the bigger commitment.</li>
      <li><strong>Hiking:</strong> from the Owa bus stop, about three hours uphill on a steep, rocky trail (japan-guide).</li>
      <li><strong>Also in Chichibu:</strong> see our """+a('/anime/anohana/','Anohana pilgrimage guide','anohana')+""" for Chichibu Shrine and the town.</li>
    </ul>
    <div class="key-callout">
      <p>&#127890; <strong>Plan your trip:</strong> Browse guided tours or find a stay near Chichibu. <a href="https://www.viator.com/search/Chichibu?pid=P00298374&amp;mcid=42383&amp;medium=link&amp;campaign=sacred-japan" target="_blank" rel="noopener" onclick="trackEvent('click','affiliate','viator_mitsumine')">Book a Tour</a></p>
    </div>

    <h2 id="faq">Frequently Asked Questions<span class="h2-jp">よくあるご質問</span></h2>
    <div class="faq-stack">
"""+''.join(f"""    <details class="faq-item">
        <summary>{q}</summary>
        <div class="faq-answer">{a_}</div>
    </details>
""" for q,a_ in faqs)+"""    </div>

    <h2 id="final">Before You Go<span class="h2-jp">むすびに</span></h2>
    <p>Check the bus timetable the night before, dress for mountain weather and leave time to look up at the carving. If you are curious about the animals at other shrines, our """+a('/culture/sacred-animals/','sacred animals guide','animals')+""" puts Mitsumine&rsquo;s wolves next to the foxes, deer and others.</p>

    <div class="closing-block">
      <span class="torii">&#9961;&#65039;</span>
      <p>A long ride up the mountain to a gate guarded by wolves, and a hall carved so densely that you keep finding new figures.</p>
    </div>

    <section class="related-section">
      <h2>Related Guides</h2>
      <span class="h2-jp">関連ガイド</span>
      <div class="related-grid">
        <a class="related-card" href="/culture/sacred-animals/" onclick="trackEvent('click','internal','related_mitsumine_to_animals')">
          <div class="related-card-label">SACRED JAPAN ／ CULTURE</div>
          <div class="related-card-title">&#129418; Sacred Animals &rarr;</div>
          <div class="related-card-desc">Foxes, deer, wolves and the other shrine guardians.</div>
        </a>
        <a class="related-card" href="/guides/nikko-toshogu/" onclick="trackEvent('click','internal','related_mitsumine_to_nikko')">
          <div class="related-card-label">SACRED JAPAN ／ GUIDES</div>
          <div class="related-card-title">&#9961;&#65039; Nikko Toshogu &rarr;</div>
          <div class="related-card-desc">Another shrine covered in colour and carving.</div>
        </a>
        <a class="related-card" href="/anime/anohana/" onclick="trackEvent('click','internal','related_mitsumine_to_anohana')">
          <div class="related-card-label">SACRED JAPAN ／ ANIME</div>
          <div class="related-card-title">&#127912; Anohana &rarr;</div>
          <div class="related-card-desc">Chichibu Shrine and the town behind the anime.</div>
        </a>
      </div>
    </section>

  </article>

"""

tail=tail.replace('gifu-castle',SL).replace('gifu_castle','mitsumine').replace('DGifu','DChichibu').replace('search/Gifu','search/Chichibu')
def L(u,l,t): return f'<a href="{u}" target="_blank" rel="noopener" style="color:var(--beni);text-decoration:underline;" onclick="trackEvent(\'click\',\'external\',\'{l}\')">{t}</a>'
src='Sources verified at time of writing: '+', '.join([
 L('https://www.japan-guide.com/e/e6553.html','src_ms_jg','japan-guide'),
 L('https://www.chichibu-omotenashi.com/en/guide/spot_11.html','src_ms_co','Chichibu Omotenashi'),
 L('https://www.mlit.go.jp/tagengo-db/common/001561686.pdf','src_ms_mlit','MLIT'),
 L('https://www.gltjp.com/en/directory/item/10529/','src_ms_gltjp','GLTJP'),
 L('https://www.japanvisitor.com/japan-temples-shrines/mitsumine-shrine','src_ms_jv','Japan Visitor'),
 L('https://jal.japantravel.com/saitama/mitsumine-shrine-mt-mitsumine/68049','src_ms_jal','JAL Japan Travel'),
 L('https://www.japan-experience.com/all-about-japan/tokyo/temples-shrines/mitsumine-shrine','src_ms_je','Japan Experience'),
 L('https://en.japantravel.com/saitama/mitsumine-shrine-chichibu/1747','src_ms_jt','Japan Travel'),
 L('https://www.chichibu-geo.com/en/?p=251','src_ms_geo','Chichibu Geo'),
 L('https://www.ana.co.jp/en/us/japan-travel-planner/saitama/0000006.html','src_ms_ana','ANA'),
 L('https://tokyocheapo.com/place/mount-mitsumine/','src_ms_tc','Tokyo Cheapo'),
])+'. Hours, prices and availability change'
tail,n=re.subn(r'Sources verified at time of writing:.*?Hours, prices and availability change',lambda m:src,tail,flags=re.S); assert n==1

out=head+main+tail
assert not re.search('Gifu|Nobunaga|Kinka',re.sub(r'"mainEntity": \[.*','',out,flags=re.S))
open(D+'index.html','w',encoding='utf-8').write(out)
for tg in ['div','figure','picture','p','a','ul','li','details','section','h2']:
    assert len(re.findall(f'<{tg}[ >]',out))==len(re.findall(f'</{tg}>',out)),tg
for m_ in re.findall(r'<script type="application/ld\+json">(.*?)</script>',out,re.S): json.loads(m_)
im=Image.open(R+'images/og/og-guides-matsue-castle.jpg').convert('RGB'); d=ImageDraw.Draw(im)
d.rectangle([40,150,1170,380],fill=(252,240,242)); d.rectangle([1118,66,1160,96],fill=(252,240,242))
f1=ImageFont.truetype(glob.glob('/usr/share/fonts/**/DejaVuSerif-Bold.ttf',recursive=True)[0],48)
f2=ImageFont.truetype(glob.glob('/usr/share/fonts/**/NotoSerifCJK-Bold.ttc',recursive=True)[0],28,index=0)
l1="Mitsumine Shrine Guide:"; l2="Wolves and the Triple Torii"; assert d.textlength(l2,font=f1)<1090
d.text((66,170),l1,font=f1,fill=(26,15,15)); d.text((66,238),l2,font=f1,fill=(26,15,15)); d.text((66,332),"三峯神社",font=f2,fill=(138,125,120))
im.save(R+f'images/og/og-guides-{SL}.jpg',quality=88)
b=Image.open(D+'images/zuishin-snow.jpg'); w,h=b.size; ch=round(w*400/640); t=max(0,(h-ch)//2)
th=b.crop((0,t,w,t+ch)).resize((640,400),Image.LANCZOS); th.save(R+f'images/hub/{SL}.jpg',quality=84); th.save(R+f'images/hub/{SL}.webp',quality=80)
print('built',len(out))
