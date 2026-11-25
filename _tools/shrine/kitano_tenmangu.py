import re,json,os,glob,shutil
from PIL import Image,ImageDraw,ImageFont
R='/home/claude/sacred-japan/'; SL='kitano-tenmangu'; D=R+f'guides/{SL}/'
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
PAN='https://web.archive.org/web/2016%s/http://www.panoramio.com/photo/%s'
P={
'approach':('48bd15e7','663highland','bysa3','https://commons.wikimedia.org/wiki/User:663highland'),
'torii':('65e2a84b','z tanuki','by3',PAN%('1025044549','84715938')),
'sankomon':('4101e2e0','Hyppolyte de Saint-Rambert','by4','https://commons.wikimedia.org/wiki/User:Hyppolyte_de_Saint-Rambert'),
'komainu':('a5cffb7a','z tanuki','by3',PAN%('1027104920','84759953')),
'hall-front':('81be93d1','くろふね','bysa4','https://commons.wikimedia.org/wiki/User:%E3%81%8F%E3%82%8D%E3%81%B5%E3%81%AD'),
'hall-side':('e2a007db','Motokoka','bysa4','https://commons.wikimedia.org/wiki/User:Motokoka'),
'hall-pano':('15abfcf9','z tanuki','by3',PAN%('1025221513','84759960')),
'maple':('648cdc9e','くろふね','bysa4','https://commons.wikimedia.org/wiki/User:%E3%81%8F%E3%82%8D%E3%81%B5%E3%81%AD'),
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
TITLE="Kitano Tenmangu Guide: Kyoto's Tenjin Shrine, Plum Blossoms, Maple Garden and the 25th Market"
DESC="A licensed guide's guide to Kitano Tenmangu in Kyoto: how Sugawara no Michizane became Tenjin, the National Treasure main hall, the ox statues, the plum and maple gardens, the monthly 25th market, fees and how to get there by bus."
TAG="The head shrine of Tenjin in Kyoto: the gate, the oxen, the plum garden, the maples and the market on the 25th."
head=re.sub(r'<title>.*?</title>',f'<title>{TITLE} | Sacred Japan</title>',head,count=1)
head=re.sub(r'(<meta (?:name="description"|property="og:description"|name="twitter:description") content=")[^"]*(")',lambda m:m.group(1)+DESC+m.group(2),head)
head=re.sub(r'(<meta (?:property="og:title"|name="twitter:title") content=")[^"]*(")',lambda m:m.group(1)+TITLE+m.group(2),head)
head=re.sub(r'("headline": ")[^"]*(")',lambda m:m.group(1)+TITLE+m.group(2),head)
head=re.sub(r'("description": ")A licensed[^"]*(")',lambda m:m.group(1)+DESC+m.group(2),head)
head=re.sub(r'("date(?:Published|Modified)": ")[^"]*(")',lambda m:m.group(1)+'2026-11-25'+m.group(2),head)
head=re.sub(r'<meta name="keywords" content="[^"]*">','<meta name="keywords" content="Kitano Tenmangu, Kitano Tenmangu Shrine, Kyoto shrine, Sugawara no Michizane, Tenjin, plum blossoms Kyoto, Momiji-en, Tenjin-san market, exam shrine Kyoto">',head)
head=head.replace('guides/gifu-castle',f'guides/{SL}').replace('guide_gifu_castle_','guide_kitano_').replace('og-guides-gifu-castle',f'og-guides-{SL}')
head=head.replace('岐阜城','北野天満宮').replace('Gifu Castle','Kitano Tenmangu')
head=re.sub(r"<h1>.*?</h1>","<h1><em>Kitano Tenmangu</em>: Kyoto\\'s Tenjin Shrine, Plum Blossoms, Maple Garden and the 25th Market</h1>",head,count=1,flags=re.S)
head=head.replace("Nobunaga's mountain castle above Gifu, with the keep closed until late 2027.",TAG)
head=head.replace('SACRED JAPAN GUIDES ／ 城','SACRED JAPAN GUIDES ／ 神社')
IL='class="inline-link"'
def a(u,t,ev): return f'<a href="{u}" {IL} onclick="trackEvent(\'click\',\'internal\',\'guide_kitano_to_{ev}\')">{t}</a>'

faqs=[
("Who is enshrined at Kitano Tenmangu?","Sugawara no Michizane (845&ndash;903), a scholar, poet and statesman of the Heian period who was exiled to Dazaifu in 901 and died there (Discover Kyoto, MLIT). After disasters in the capital were blamed on his spirit, the court founded this shrine in 947, and the shrine itself says it was the first in Japan to enshrine a real person as a deity. He is worshipped as Tenjin, the god of learning."),
("Why are there ox statues everywhere?","MLIT says the link comes from Michizane having been born in the year of the ox. Discover Kyoto says oxen are Tenjin&rsquo;s messengers and are always shown lying down. GLTJP says to rub the ox&rsquo;s head if you are praying for academic success, and Discover Kyoto lists other body parts for other wishes."),
("When are the plum blossoms and the maple leaves?","GLTJP gives early February to late March for the plum garden (its FAQ says mid-March), and japan-guide says the trees bloom from February to March. For maples, GLTJP gives mid-November to early December. In 2026 the maple garden is listed as open from 31 October to 6 December, with evening lighting from 13 November (Kyoto Travel)."),
("How much does it cost?","The shrine grounds are free (GLTJP, japan-guide). The gardens charge separately, and sources disagree on the plum garden: 700 yen (Discover Kyoto, GaijinPot) or 3,000 yen (japan-guide, which does not say why). The 2026 maple garden fee is 1,500 yen for adults and 700 yen for children (Weathernews, NTA), up from 1,200 yen in 2025 (Walkerplus). Check the shrine&rsquo;s site for the current price."),
("What is the market on the 25th?","Tenjin-san, a street market held on the 25th of each month on the grounds and in the streets around them. The shrine says it has its roots in the anniversary of Michizane&rsquo;s birth and death, and runs from 6 a.m. until sunset. Discover Kyoto says the markets in January and December are the largest. Weathernews says parking is not available on the 25th."),
("How do I get to Kitano Tenmangu?","Take City Bus 50 from Kyoto Station to Kitano Tenmangu-mae: 230 yen and about 30 minutes (japan-guide), or about 35 (GLTJP). Discover Kyoto also lists Bus 101, and Route 203 from Demachiyanagi. The Randen Kitano Line&rsquo;s Kitano-Hakubaicho Station is a 5 minute walk (Weathernews) or 10 (Discover Kyoto)."),
]

faq_json=',\n'.join("""    {
      "@type": "Question",
      "name": %s,
      "acceptedAnswer": {
        "@type": "Answer",
        "text": %s
      }
    }"""%(json.dumps(re.sub('<[^>]+>','',q)),json.dumps(re.sub('&ldquo;|&rdquo;','"',re.sub('&rsquo;','’',re.sub('<[^>]+>','',a_))))) for q,a_ in faqs)
head=re.sub(r'("mainEntity": \[\n).*?(\n  \]\n\}\n</script>\n\n<!-- ── GOOGLE)',lambda m:m.group(1)+faq_json+m.group(2),head,flags=re.S)
hh=re.sub(r'"mainEntity": \[.*','',head,flags=re.S)
assert not re.search('Gifu|Nobunaga|castle|Castle',re.sub(r'<nav>.*?</nav>','',hh,flags=re.S).replace('Castles','')),re.findall('.{30}(?:Gifu|Nobunaga|astle).{20}',hh)

main="""<main>

  <aside class="toc" aria-label="Table of contents">
    <div class="toc-label">TABLE OF CONTENTS ／ 目次</div>
    <div class="toc-title">In This Guide</div>
    <ol>
      <li><a href="#opening">The Original Tenjin Shrine</a></li>
      <li><a href="#michizane">How a Man Became a God</a></li>
      <li><a href="#gate">The Torii, the Gate and the Oxen</a></li>
      <li><a href="#hall">The National Treasure Main Hall</a></li>
      <li><a href="#plum">Plum Blossoms and the Tea Gathering</a></li>
      <li><a href="#maple">The Maple Garden on Hideyoshi&rsquo;s Earthwork</a></li>
      <li><a href="#market">Tenjin-san: The Market on the 25th</a></li>
      <li><a href="#visit">Visiting Kitano Tenmangu</a></li>
      <li><a href="#faq">Frequently Asked Questions</a></li>
      <li><a href="#final">Before You Go</a></li>
    </ol>
  </aside>

  <article>

"""+fig('approach','Stone-paved approach at Kitano Tenmangu with visitors walking toward the dark-roofed gate and the shrine buildings, trees on both sides','The paved approach toward the gate of Kitano Tenmangu',"2011-05-22",hero=True)+"""
    <p class="opening" id="opening">As a licensed guide, I send students here first, then everyone else. Kitano Tenmangu in northwest Kyoto is the original shrine of Tenjin, the god of learning, and it keeps the habits of a place that has been asked for good marks, and for good health, for about a thousand years.</p>
    <p>It also works as a visit in any season. There are plum blossoms in February and March, maple leaves into early December, and a street market on the 25th of every month. This guide covers who is enshrined, what to look for at the gate and the main hall, what the oxen are about and the practical side: fees that differ between sources, and the bus from Kyoto Station.</p>

    <h2 id="michizane">How a Man Became a God<span class="h2-jp">菅原道真と天神信仰</span></h2>
    <p>Discover Kyoto gives the outline: Sugawara no Michizane (845&ndash;903), a scholar and statesman, was demoted to a low post in Dazaifu in Kyushu in 901 and died there in 903 without returning to Kyoto. After disasters struck the capital, his spirit was blamed. The shrine was founded in the Kitano area in 947, and he was later deified as Tenman Tenjin in 987 (Discover Kyoto). MLIT calls it the first shrine in Japan to enshrine a real person as a deity, and the shrine says the same.</p>
    <p>The shrine says there are as many as 12,000 shrines dedicated to Michizane in Japan, with Kitano Tenmangu as the origin and the main shrine. For the other end of the story, see our """+a('/guides/dazaifu-tenmangu/','Dazaifu Tenmangu guide','dazaifu')+""", and for the Tokyo shrine famous for exam season, the """+a('/guides/yushima-tenmangu/','Yushima Tenmangu guide','yushima')+""".</p>

    <h2 id="gate">The Torii, the Gate and the Oxen<span class="h2-jp">鳥居・三光門・牛</span></h2>
"""+fig('torii','Large stone torii with a plaque at its top, a stone komainu on a pedestal on each side, a blue notice board at right, two black taxis at the edges and pine trees behind','The large stone torii at the approach, flanked by komainu',"2013-01-13")+"""
    <p>From the bus stop you come to a large stone torii with a plaque I read as 天満宮, a stone komainu on a pedestal on each side, and a blue notice board at the right. Two black taxis frame the shot at the edges. The photo is a stretched panorama, and the Commons description does not say which torii it is.</p>
"""+fig('sankomon','Close view of the central gate of Kitano Tenmangu with a gold-lettered plaque, a curtain with a crest across the doorway, a stone komainu to each side and a crowd of visitors in front','The central gate, with a gold-lettered plaque and visitors',"2023-12-25")+"""
    <p>The central gate, the Sankomon, is the one to look at. GLTJP says it was built in the Momoyama style and is an Important Cultural Property. The Commons file calls it the Chumon, which I take to be the same gate. Its name is the &ldquo;Gate of Three Lights&rdquo; (Discover Kyoto), and GLTJP lists it among the Seven Mysteries of Tenjin-sama: the &ldquo;star-missing&rdquo; gate, which has carvings of only the sun and the moon. Discover Kyoto adds that it carries carved animals and figures from Chinese mythology. In the photo, a stone komainu stands at each side and a curtain with a crest hangs across the doorway; I could not read the crest.</p>
"""+fig('komainu','Stone komainu on a stone base beside a white paper lantern painted with pine branches, with a small round crest on the gable above','A stone komainu beside a paper lantern',"2013-01-13")+"""
    <p>Komainu like this one flank the gate. The lantern is painted with pine branches, and the small round mark on the gable above looks to me like a five-petal plum crest, though the Commons description says only that it is a komainu at the shrine.</p>
    <p>The oxen are the signature of every Tenmangu. MLIT says the link comes from Michizane having been born in the year of the ox. Discover Kyoto says the oxen are his messengers and are always shown lying down, as the legendary ox did, and that the largest statue kneels near the central gate beneath a white plum tree. GLTJP says to rub the head if you are praying for academic success; Discover Kyoto lists other body parts for other wishes. Our """+a('/culture/sacred-animals/','sacred animals guide','animals')+""" covers the ox among the other shrine animals.</p>
    <p>GLTJP also lists, among the Seven Mysteries, a Main Hall set off-axis with a smaller shrine straight ahead, the only standing ox, carved into the transom of the worship hall, and a pine where Tenjin is said to descend after the first snow.</p>

    <h2 id="hall">The National Treasure Main Hall<span class="h2-jp">国宝の御本殿</span></h2>
    <p>GLTJP says the present Main Hall was built in 1607 by Toyotomi Hideyori, that it is a National Treasure and that it is a rare surviving example of the Momoyama style. Discover Kyoto instead gives 1607 for the Sankomon and says Hideyori also built the main building, without a date; the prefecture says Hideyori set up the present precinct. I would treat 1607 as the approximate date of the Hideyori work and check the shrine&rsquo;s own account if the year matters.</p>
    <p>The architecture is the interesting part. GLTJP describes it as <em>yattsumune-zukuri</em>, also called gongen-zukuri, and says it became the model for the gongen-zukuri style that spread in the Edo period. Our """+a('/culture/shrine-architecture/','shrine architecture guide','architecture')+""" explains the layout, with a worship hall and a main hall joined under a single roof.</p>
"""+fig('hall-front','Wide view of the red and gold front of the main buildings of Kitano Tenmangu across a gravel courtyard, with a tall pine to the right, paper lanterns hanging under the eaves, a deep blue sky and visitors walking toward it','The front of the main buildings from the courtyard, in a strongly processed photo',"2015-11-21")+"""
    <p>This photograph is strongly processed, so the sky and the gravel are more intense than they look on a normal day. I read the building as the main worship hall front, with its red-painted eaves, hanging lanterns and a tall pine at right, but the Commons description only names the shrine.</p>
"""+fig('hall-side','Close view of the carved and gilded side of the shrine building, a large golden lantern hanging at the front, wooden notice boards on a stand and a few visitors reading them','The carved eaves, a golden lantern and notice boards at the side of the hall',"2009-06-06")+"""
    <p>Up close the eaves are carved and gilded, with golden lanterns hanging along the front. Discover Kyoto says visitors ring the bell, toss in a coin and pray here, and that the carvings are attributed to the legendary artisan Hidari Jingoro, which I would read as tradition, not a documented attribution. In the photo a few visitors read the notice boards at the side.</p>
"""+fig('hall-pano','Wide view of the front of the main hall with its curved gable, hanging lanterns, stacked sake barrels at the left and a pine at the right, with bare branches at the far left and visitors in the foreground','The front of the hall in winter, with bare branches at the left',"2013-01-13")+"""
    <p>This winter view shows the front of the hall with its curved gable, rows of hanging lanterns, stacked barrels at the left and a pine at the right, and a crowd gathering before it. Bare branches at the far left are probably a plum, but I cannot confirm that from the file. It is a stretched panorama, so the proportions are exaggerated sideways.</p>

    <h2 id="plum">Plum Blossoms and the Tea Gathering<span class="h2-jp">梅苑と北野大茶湯</span></h2>
    <p>Michizane loved plum trees, and japan-guide says one, the <em>tobiume</em> or flying plum, is said to have followed him from Kyoto to his exile in Kyushu. That is why a plum tree stands in front of the worship hall at Tenmangu shrines. The garden has plums in large numbers: GLTJP and Discover Kyoto say about 1,500 trees of roughly 50 varieties, while japan-guide says nearly 2,000. GLTJP puts the best viewing at early February to late March.</p>
    <p>Admission is where sources split. Discover Kyoto and GaijinPot give 700 yen for adults; japan-guide gives 3,000 yen without saying what it covers. Treat both as old or incomplete and check the shrine&rsquo;s website in the weeks before you go.</p>
    <p>On 25 February the shrine holds the Baika-sai, a tea ceremony in the plum grove where geiko and maiko of Kamishichiken serve matcha and sweets (shrine, japan-guide). Discover Kyoto traces it to the 1587 tea gathering that Toyotomi Hideyoshi hosted on these grounds with Sen no Rikyu, a claim I found only there. Our """+a('/culture/tea-ceremony/','tea ceremony guide','tea')+""" has more on Hideyoshi and Rikyu.</p>

    <h2 id="maple">The Maple Garden on Hideyoshi&rsquo;s Earthwork<span class="h2-jp">史跡御土居のもみじ苑</span></h2>
"""+fig('maple','A narrow stone-lined stream channel under maple trees in red, orange and yellow, with a bamboo railing on one side and visitors walking along a path','Autumn maples along a stream, in a strongly processed photo',"2015-11-21")+"""
    <p>In autumn the second garden opens. The Odoi is an earthwork that Toyotomi Hideyoshi built around Kyoto and is a designated historic site (Kyoto Travel, in Japanese); the Kitano section is said to be closest to the original form. About 350 maples colour beside the Kamiya River, and the vermilion Uguisu Bridge is the usual photo spot (Kyoto Travel, Weathernews). The photo above shows a stream channel with a bamboo railing under red and yellow maples, which fits that setting to my eye, though the Commons description names only the shrine. It is strongly processed, so the colours are more intense than a normal day.</p>
    <p>For 2026, Kyoto Travel gives 31 October to 6 December, with evening lighting from 13 November. NTA lists hours of 9:00 to 16:00, with 9:00 to 20:00 and last entry 19:40 during the lighting (the Walkerplus 2025 page gives the same last entry), and 1,500 yen for adults and 700 for children with tea and sweets (NTA, Weathernews); 2025 was 1,200 and 600 (Walkerplus). Colour is best from mid-November to early December (GLTJP).</p>

    <h2 id="market">Tenjin-san: The Market on the 25th<span class="h2-jp">天神さん（毎月25日の縁日）</span></h2>
    <p>On the 25th of every month there is a street market on the grounds and around them. The shrine says it has its roots in the anniversary of Michizane&rsquo;s birth and death, and that it runs from 6 a.m. until sunset. Japan-guide says stalls sell plants, antiques, tools, toys and crafts, plus festival food such as yakisoba, karaage and takoyaki. Discover Kyoto says the January and December markets are the largest; the December one is called Shimai Tenjin, the last Tenjin-san of the year.</p>
    <p>It is the busiest day for the shrine and the worst for cars: Weathernews says parking is not available on the 25th. The shrine&rsquo;s museum also opens on the 25th, at 9:00 to 16:00 with adult admission of 1,000 yen on the shrine&rsquo;s page, although Discover Kyoto still lists 300 yen. Treat the shrine&rsquo;s figure as current.</p>

    <h2 id="visit">Visiting Kitano Tenmangu<span class="h2-jp">参拝案内</span></h2>
    <ul class="practical-list">
      <li><strong>Address:</strong> Bakurocho, Kamigyo Ward, Kyoto 602-8386. Phone 075-461-0005 (shrine).</li>
      <li><strong>By bus:</strong> City Bus 50 from Kyoto Station to Kitano Tenmangu-mae: 230 yen, about 30 minutes (japan-guide) or about 35 (GLTJP). Discover Kyoto also lists Bus 101, and Route 203 from Demachiyanagi.</li>
      <li><strong>By tram:</strong> Randen Kitano Line to Kitano-Hakubaicho Station, 5 minutes on foot (Weathernews) or 10 (Discover Kyoto).</li>
      <li><strong>Hours:</strong> the shrine&rsquo;s page has shown 7:00 to 17:00 and 7:00 to 20:00 at different times, with prayer from 9:00 to 16:00. Hours vary by season, so check before you go. Entry is free.</li>
      <li><strong>Nearby:</strong> Japan Travel (JAL) places it near Kinkaku-ji; see our """+a('/guides/kinkakuji/','Kinkaku-ji guide','kinkakuji')+""".</li>
      <li><strong>In autumn:</strong> our """+a('/guides/kyoto-illuminations/','Kyoto illuminations guide','illuminations')+""" and """+a('/guides/autumn-sanctuaries/','autumn sanctuaries guide','autumn')+""" cover the evening lighting and other maple spots.</li>
    </ul>
    <div class="key-callout">
      <p>&#127890; <strong>Plan your trip:</strong> Browse guided tours or find a stay in Kyoto. <a href="https://www.viator.com/search/Kyoto?pid=P00298374&amp;mcid=42383&amp;medium=link&amp;campaign=sacred-japan" target="_blank" rel="noopener" onclick="trackEvent('click','affiliate','viator_kitano')">Book a Tour</a></p>
    </div>

    <h2 id="faq">Frequently Asked Questions<span class="h2-jp">よくあるご質問</span></h2>
    <div class="faq-stack">
"""+''.join(f"""    <details class="faq-item">
        <summary>{q}</summary>
        <div class="faq-answer">{a_}</div>
    </details>
""" for q,a_ in faqs)+"""    </div>

    <h2 id="final">Before You Go<span class="h2-jp">むすびに</span></h2>
    <p>Go with a bow at the gate and a pat on the ox, then pick a season: plum in February, maples in late November, or the 25th for the market. Whichever you choose, read the current fees on the shrine&rsquo;s site first.</p>

    <div class="closing-block">
      <span class="torii">&#9961;&#65039;</span>
      <p>The first shrine to a man who became a god, still crowded with people asking for a good result.</p>
    </div>

    <section class="related-section">
      <h2>Related Guides</h2>
      <span class="h2-jp">関連ガイド</span>
      <div class="related-grid">
        <a class="related-card" href="/guides/dazaifu-tenmangu/" onclick="trackEvent('click','internal','related_kitano_to_dazaifu')">
          <div class="related-card-label">SACRED JAPAN ／ GUIDES</div>
          <div class="related-card-title">&#9961;&#65039; Dazaifu Tenmangu &rarr;</div>
          <div class="related-card-desc">Where Michizane was exiled and is buried.</div>
        </a>
        <a class="related-card" href="/guides/yushima-tenmangu/" onclick="trackEvent('click','internal','related_kitano_to_yushima')">
          <div class="related-card-label">SACRED JAPAN ／ GUIDES</div>
          <div class="related-card-title">&#9961;&#65039; Yushima Tenmangu &rarr;</div>
          <div class="related-card-desc">Tokyo&rsquo;s exam-season shrine and its wall of ema.</div>
        </a>
        <a class="related-card" href="/guides/kinkakuji/" onclick="trackEvent('click','internal','related_kitano_to_kinkakuji')">
          <div class="related-card-label">SACRED JAPAN ／ GUIDES</div>
          <div class="related-card-title">&#127983; Kinkaku-ji &rarr;</div>
          <div class="related-card-desc">The Golden Pavilion, a short trip from Kitano.</div>
        </a>
      </div>
    </section>

  </article>

"""

tail=tail.replace('gifu-castle',SL).replace('gifu_castle','kitano').replace('DGifu','DKyoto').replace('search/Gifu','search/Kyoto')
def L(u,l,t): return f'<a href="{u}" target="_blank" rel="noopener" style="color:var(--beni);text-decoration:underline;" onclick="trackEvent(\'click\',\'external\',\'{l}\')">{t}</a>'
src='Sources verified at time of writing: '+', '.join([
 L('https://kitanotenmangu.or.jp/en/','src_kt_official','Kitano Tenmangu (official)'),
 L('https://www.gltjp.com/en/article/item/20343/','src_kt_gltjp','GLTJP'),
 L('https://japan-guide.com/e/e3939.html','src_kt_jg','japan-guide'),
 L('https://www.discoverkyoto.com/places-go/kitano-tenmangu/','src_kt_dk','Discover Kyoto'),
 L('https://www.mlit.go.jp/tagengo-db/common/001564973.pdf','src_kt_mlit','MLIT'),
 L('https://ja.kyoto.travel/event/single.php?event_id=5054','src_kt_kt','Kyoto Travel (JP)'),
 L('https://www.nta.co.jp/kokunai/special/eventinfo/10643550.htm','src_kt_nta','NTA'),
 L('https://weathernews.jp/koyo/spot/26132/','src_kt_wn','Weathernews'),
 L('https://koyo.walkerplus.com/detail/ar0726e154656/data.html','src_kt_wp','Walkerplus'),
 L('https://travel.gaijinpot.com/kitano-tenmangu-shrine/','src_kt_gp','GaijinPot'),
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
l1="Kitano Tenmangu Guide:"; l2="Tenjin, Plums and Maples"; assert d.textlength(l2,font=f1)<1090
d.text((66,170),l1,font=f1,fill=(26,15,15)); d.text((66,238),l2,font=f1,fill=(26,15,15)); d.text((66,332),"北野天満宮",font=f2,fill=(138,125,120))
im.save(R+f'images/og/og-guides-{SL}.jpg',quality=88)
b=Image.open(D+'images/approach.jpg'); w,h=b.size; ch=round(w*400/640); t=max(0,(h-ch)//2)
th=b.crop((0,t,w,t+ch)).resize((640,400),Image.LANCZOS); th.save(R+f'images/hub/{SL}.jpg',quality=84); th.save(R+f'images/hub/{SL}.webp',quality=80)
print('built',len(out))
