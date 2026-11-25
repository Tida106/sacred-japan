import re,json,os,glob
from PIL import Image,ImageDraw,ImageFont
R='/home/claude/sacred-japan/'; SL='kirishima-jingu'; D=R+f'guides/{SL}/'
os.makedirs(D+'images',exist_ok=True); UP='/mnt/user-data/uploads/'
LIC={'by4':('CC BY 4.0','https://creativecommons.org/licenses/by/4.0/'),
     'bysa3':('CC BY-SA 3.0','https://creativecommons.org/licenses/by-sa/3.0/'),
     'bysa4':('CC BY-SA 4.0','https://creativecommons.org/licenses/by-sa/4.0/')}
def CS(t): return 'https://commons.wikimedia.org/w/index.php?search='+t+'&title=Special:MediaSearch&type=image'
YANO=CS('%E7%9F%A2%E9%87%8E%E5%BC%98%E5%B9%B8%20%E9%9C%A7%E5%B3%B6%E7%A5%9E%E5%AE%AE')
P={ # slug:(upload,author,lic,link)
'lanterns':('90b08dc7','MaedaAkihiko','bysa4',CS('MaedaAkihiko%20Kirishima')),
'torii-gate':('48fbba7c','Hiroyuki Yano','bysa4',YANO),
'great-torii':('35742b20','Hiroyuki Yano','bysa4',YANO),
'approach':('ae1316b2','Hiroyuki Yano','bysa4',YANO),
'haiden':('e38276a2','Hiroyuki Yano','bysa4',YANO),
'carving':('cc2c7bc0','Hiroyuki Yano','bysa4',YANO),
'sculpture':('f1e902c7','663highland','bysa3',CS('663highland%20Kirishima-jingu')),
'temizuya':('e5fd9176','Hyppolyte de Saint-Rambert','by4',CS('Kirishima-jingu%20temizuya')),
'crowd':('543e6446','663highland','bysa3',CS('663highland%20Kirishima-jingu')),
'courtyard':('baefdf2f','Hiroyuki Yano','bysa4',YANO),
'kagura-den':('41574c64','Hiroyuki Yano','bysa4',YANO),
'express':('9c137326','Tokkyu Nichirin','bysa3',CS('Kirishima%20Jingu%20Station')),
}
if not os.path.exists(D+'images/lanterns.jpg'):
    for k,v in P.items():
        im=Image.open(UP+v[0]+'-image.jpg').convert('RGB'); w,h=im.size
        if w>1200: im=im.resize((1200,round(h*1200/w)),Image.LANCZOS)
        im.save(D+f'images/{k}.jpg',quality=84); im.save(D+f'images/{k}.webp',quality=80)
SIZE={k:Image.open(D+f'images/{k}.jpg').size for k in P}
def fig2(k,alt,cap,hero=False):
    u,a,l,cl=P[k]; ln,lu=LIC[l]; w,h=SIZE[k]
    if hero: st='margin:0 0 48px;'; ld='eager'; ims='style="width:100%;max-height:420px;object-fit:cover;border-radius:4px;display:block;"'
    else:
        st='margin:28px auto;max-width:%s;'%('420px' if h>w else '760px'); ld='lazy'; ims='style="width:100%;height:auto;border-radius:4px;display:block;"'
    lic=f'public domain (photographic reproduction of a print)' if l=='pd' else f'<a href="{lu}" target="_blank" rel="noopener">{ln}</a>'
    return f'''<figure style="{st}"><picture><source srcset="/guides/{SL}/images/{k}.webp" type="image/webp"><img src="/guides/{SL}/images/{k}.jpg" alt="{alt}" width="{w}" height="{h}" loading="{ld}" {ims}></picture><figcaption style="font-size:13px;color:var(--enshu);margin-top:10px;text-align:center;line-height:1.6;">{cap}.<br>{'Artist' if l=='pd' else 'Photo'}: <a href="{cl}" target="_blank" rel="noopener">{a}</a>, {lic}, via Wikimedia Commons (resized)</figcaption></figure>
'''
fig=fig2
s=open(R+'guides/gifu-castle/index.html',encoding='utf-8').read()
i=s.index('<main>'); j=s.index('</main>'); head,tail=s[:i],s[j:]
TITLE="Kirishima Jingu Guide: Ninigi's Shrine, a National Treasure Hall and the Road to Takachiho"
DESC="A licensed guide's guide to Kirishima Jingu in Kagoshima: the god who descended to Mt. Takachiho, the vermilion halls rebuilt in 1715 and made a National Treasure in 2022, the 800-year-old cedar, Ryoma's honeymoon, and how to get there by train and bus."
TAG="Kyushu's vermilion mythology shrine, built for the god who came down to the mountain above it."
head=re.sub(r'<title>.*?</title>',f'<title>{TITLE} | Sacred Japan</title>',head,count=1)
head=re.sub(r'(<meta (?:name="description"|property="og:description"|name="twitter:description") content=")[^"]*(")',lambda m:m.group(1)+DESC+m.group(2),head)
head=re.sub(r'(<meta (?:property="og:title"|name="twitter:title") content=")[^"]*(")',lambda m:m.group(1)+TITLE+m.group(2),head)
head=re.sub(r'("headline": ")[^"]*(")',lambda m:m.group(1)+TITLE+m.group(2),head)
head=re.sub(r'("description": ")A licensed[^"]*(")',lambda m:m.group(1)+DESC+m.group(2),head)
head=re.sub(r'("date(?:Published|Modified)": ")[^"]*(")',lambda m:m.group(1)+'2026-11-25'+m.group(2),head)
head=re.sub(r'<meta name="keywords" content="[^"]*">','<meta name="keywords" content="Kirishima Jingu, Kirishima Shrine, Kirishima Jingu National Treasure, Ninigi, Mount Takachiho, Kagoshima shrine, Kirishima Jingu access, Ryoma honeymoon, Kyushu shrine">',head)
head=head.replace('guides/gifu-castle',f'guides/{SL}').replace('guide_gifu_castle_','guide_kirishima_jingu_').replace('og-guides-gifu-castle',f'og-guides-{SL}')
head=head.replace('岐阜城','霧島神宮').replace('Gifu Castle','Kirishima Jingu')
head=re.sub(r"<h1>.*?</h1>","<h1><em>Kirishima Jingu</em>: Ninigi's Shrine, a National Treasure Hall and the Road to Takachiho</h1>",head,count=1,flags=re.S)
head=head.replace("Nobunaga's mountain castle above Gifu, with the keep closed until late 2027.",TAG)
head=head.replace('SACRED JAPAN GUIDES ／ 城','SACRED JAPAN GUIDES ／ 神社')
IL='class="inline-link"'
def a(u,t,ev): return f'<a href="{u}" {IL} onclick="trackEvent(\'click\',\'internal\',\'guide_kirishima_jingu_to_{ev}\')">{t}</a>'
faqs=[
("Is Kirishima Jingu a National Treasure?","Yes. The main hall (<em>honden</em>), the offering hall (<em>heiden</em>) and the worship hall (<em>haiden</em>) were designated National Treasures on 9 February 2022 (Kagoshima Prefecture). They were the first buildings in the prefecture to receive the status (Tokyo Weekender). Some older English pages still call them Important Cultural Properties, which was their earlier rank."),
("Who is enshrined at Kirishima Jingu?","The main deity is Ninigi no Mikoto, the grandson of the sun goddess Amaterasu, who in the myths came down from heaven to rule the land and is said to have landed on Mt. Takachiho no mine, the peak above the shrine (japan-guide, Kagoshima Prefecture). The shrine is read as the place that worships that mountain from its foot."),
("How do I get to Kirishima Jingu without a car?","Take the JR Nippo Main Line to Kirishima-Jingu Station, then a bus of 10 to 15 minutes to the &ldquo;Kirishima Jingu&rdquo; stop. The station is more than 5 km from the shrine (japan-guide). From Kagoshima-Chuo, the limited express <em>Kirishima</em> takes about 50 minutes (Tokyo Weekender). Buses are infrequent, roughly one every one to four hours (japan-guide, GLTJP), so check the timetable before you go. Fares appear as &yen;240, &yen;290 and &yen;330 in different sources, so treat the figure as approximate."),
("Is there an admission fee or opening hours?","The grounds are free and listed as open at all times (GLTJP, Tokyo Weekender). The shrine office, where prayers and charms are handled, is open 8:00 to 17:00 (Jeepe, Tokyo Weekender). One site lists the whole shrine as 8:00 to 18:00, so check the official site if you plan an early or late visit."),
("How much time do I need?","About 20 to 30 minutes for the main halls, or about an hour with the goshuin office and a walk around the grounds (Jeepe). That is my own reading of their estimate; allow more if you go by bus and wait for the return."),
("Can I climb Mt. Takachiho from the shrine?","Not from the shrine itself. The trail to the summit starts at Takachigawara, higher on the mountain, near the earlier site of the shrine (Tabi-mag). Check current volcanic-activity and trail notices before you go; the Kirishima range is active and closures happen."),
]
faq_json=',\n'.join("""    {
      "@type": "Question",
      "name": %s,
      "acceptedAnswer": {
        "@type": "Answer",
        "text": %s
      }
    }"""%(json.dumps(re.sub('<[^>]+>','',re.sub('&rsquo;','’',q))),json.dumps(re.sub('&ldquo;|&rdquo;','"',re.sub('&yen;','¥',re.sub('&rsquo;','’',re.sub('<[^>]+>','',a_)))))) for q,a_ in faqs)
head=re.sub(r'("mainEntity": \[\n).*?(\n  \]\n\}\n</script>\n\n<!-- ── GOOGLE)',lambda m:m.group(1)+faq_json+m.group(2),head,flags=re.S)
hh=re.sub(r'"mainEntity": \[.*','',head,flags=re.S)
assert not re.search('Gifu|Nobunaga|castle|Castle',re.sub(r'<nav>.*?</nav>','',hh,flags=re.S).replace('Castles','')),re.findall('.{30}(?:Gifu|Nobunaga|astle).{20}',hh)
main="""<main>

  <aside class="toc" aria-label="Table of contents">
    <div class="toc-label">TABLE OF CONTENTS ／ 目次</div>
    <div class="toc-title">In This Guide</div>
    <ol>
      <li><a href="#opening">The God Who Came Down</a></li>
      <li><a href="#history">History: Moved Down the Mountain</a></li>
      <li><a href="#approach">The Approach and the Torii</a></li>
      <li><a href="#halls">The National Treasure Halls</a></li>
      <li><a href="#carvings">Carvings Under the Eaves</a></li>
      <li><a href="#grounds">Water, Crowds and the Courtyard</a></li>
      <li><a href="#ryoma">Ryoma and Oryo</a></li>
      <li><a href="#getting-there">Getting There</a></li>
      <li><a href="#visit">Visiting Kirishima Jingu</a></li>
      <li><a href="#faq">Frequently Asked Questions</a></li>
      <li><a href="#final">Before You Go</a></li>
    </ol>
  </aside>

  <article>

"""+fig('lanterns','The layered vermilion roofs of the Kirishima Jingu halls seen from the front, with stone lanterns in the foreground and forest behind','The vermilion halls of Kirishima Jingu, seen between stone lanterns (the photographer is credited as MaedaAkihiko)',hero=True)+"""
    <section id="opening">
      <p class="opening">As a licensed guide, I send people to Kirishima Jingu when they ask where the myth of the descent from heaven actually lands. The story says that Ninigi, grandson of the sun goddess, came down to the mountain called Takachiho no mine with the three sacred treasures, and this shrine is the one that worships him from the mountain&rsquo;s foot. It is also the brightest shrine in southern Kyushu: vermilion halls, gold crests, carved flowers and beasts under every eave, and since 2022 a National Treasure.</p>
      <p>This guide covers the history, the approach and the halls in photos, the carvings, Sakamoto Ryoma&rsquo;s honeymoon visit, the train-and-bus route, and the practical details.</p>
    </section>

    <h2 id="history">History: Moved Down the Mountain<span class="h2-jp">由緒</span></h2>
    <p>Tradition says the shrine began in the reign of Emperor Kinmei in the 6th century (Serai), and that a monk named Keiin first built it on the summit of Takachiho no mine (Tabi-mag). Eruptions repeatedly destroyed it. Tabi-mag adds that the monk Shoku moved it to the area of today&rsquo;s Takachigawara, and that in 1484 the lord Shimazu Tadamasa ordered it moved to its present site. Japan-guide gives a different, shorter story: first built in the Muromachi period at another site, repeatedly destroyed, and finished on the present site in 1715. These accounts do not match in detail, so I would treat all the early dates as tradition.</p>
    <p>What is solid is the building. Kagoshima Prefecture says the present halls were restored in 1715 by Shimazu Yoshitaka, the 4th lord of Satsuma, and designated National Treasures on 9 February 2022. Its description notes how the precinct climbs: from the imperial-messenger hall, up a covered stairway, through the worship and offering halls to the main hall at the highest point, with steep steps exaggerating the rise.</p>

    <h2 id="approach">The Approach and the Torii<span class="h2-jp">参道と鳥居</span></h2>
"""+fig('great-torii','A very large vermilion torii with black bases and a black top beam over a wide gravel road lined with cedars and stone lanterns','A very large vermilion torii over the gravel approach road')+"""
    <p>The first gate is a very large vermilion torii with black bases, standing over a wide gravel road between tall cedars and stone lanterns. The road runs straight on into the forest. Sources give different heights for the biggest torii here, about 22.4 m (Jeepe) and 23 m (Jorudan), and I cannot tell you whether this is that gate.</p>
"""+fig('torii-gate','A vermilion torii with a tiled roof and a red lantern on each side, with a paved path leading through trees to the vermilion halls in the distance','A second torii with red lanterns, and the halls glimpsed at the far end of the path')+"""
    <p>A second torii, this one with a tiled top beam and a red lantern on each side, opens onto a paved path through the trees. At the far end, small and bright, you can already see the vermilion halls. It is a good example of how the shrine uses the forest as a frame.</p>

    <h2 id="halls">The National Treasure Halls<span class="h2-jp">国宝の社殿</span></h2>
"""+fig('approach','The vermilion halls of Kirishima Jingu at the end of a granite path, with a small shrine on each side','The halls at the end of the granite path, with small shrines on either side')+"""
    <p>At the end of a granite path, the halls rise in layers, with a small shrine on either side of the path. This is the view the whole precinct is composed for. Jeepe counts about 80 steps on the main approach, which is why it recommends sturdy shoes.</p>
"""+fig('haiden','The front of the haiden with a black plaque, a gold chrysanthemum-type crest, red pillars and white lanterns','The front of the worship hall, with a black plaque and a gold crest')+"""
    <p>Up close, the worship hall shows a black plaque above the entrance and a gold crest that I read as a chrysanthemum, set between red pillars with white lanterns hanging. I would not rely on my reading of the plaque; it is for the shrine to say what it means. The feeling is of a building that has been built to look generous.</p>

    <h2 id="carvings">Carvings Under the Eaves<span class="h2-jp">彫刻</span></h2>
"""+fig('carving','Painted carvings under the eaves of the haiden showing birds on plum branches, peonies and pine, with lion-dog figures on the brackets','Painted carvings under the eaves of the worship hall')+"""
    <p>Look up. Under the eaves, painted relief carvings show what I read as birds on plum branches, peonies and a pine, and the brackets are carved into lion-dog figures. This colour is what earned Kirishima Jingu the name &ldquo;Nikko of the West&rdquo; (Jeepe, Japan National Tourism Organization), a comparison with the carved shrines of Nikko in the east. The 2022 designation notes carvings and paintings at the key points.</p>
"""+fig('sculpture','A carved lion-dog-like beast and an elephant-like beast painted in colour on a corner bracket of the hall','A corner bracket carved with a lion-dog and an elephant-like beast')+"""
    <p>On one corner bracket sit two beasts: a lion-dog, and a second animal with a trunk that looks like an elephant. The LSS article calls them a lion and an elephant, and that is also my reading, but I cannot say what the shrine says about them. Elephants, which Japanese carvers knew only from pictures, often appear in this kind of decorative carving.</p>

    <h2 id="grounds">Water, Crowds and the Courtyard<span class="h2-jp">境内</span></h2>
"""+fig('temizuya','Visitors rinsing their hands at a red-pillared water pavilion with a green roof','The water pavilion, where visitors rinse their hands')+"""
    <p>Before the hall comes the water pavilion, with red pillars and a green roof, where visitors rinse their hands and mouth. If you have not done it before, our """+a('/culture/shrine-etiquette/','shrine etiquette guide','etiquette')+""" covers the steps.</p>
"""+fig('crowd','Visitors climbing the front steps toward the worship hall, one holding an umbrella','Visitors on the steps in front of the worship hall')+"""
    <p>Here people climb the front steps to the worship hall, with one umbrella visible. Jeepe lists the busiest periods as New Year (1 to 3 January), the autumn colours (late November to early December) and Golden Week, and suggests 8:00 to 9:00 or a weekday morning for a quieter visit.</p>
"""+fig('courtyard','The side of the courtyard with vermilion corridors, a guardhouse sign and a gravel yard','The courtyard, seen from the side, with the guardhouse')+"""
    <p>This view shows the side of the courtyard, with vermilion corridors, gravel and a small building whose sign appears to read <span lang="ja">守衛舎</span>, a guardhouse. The buildings you see on the way in are only part of the precinct.</p>
"""+fig('kagura-den','The kagura-den, a large building with sweeping roofs and a prayer-reception sign','The kagura hall, which is also where prayers are received')+"""
    <p>The big building with sweeping roofs is the kagura hall, and the sign beside it appears to read <span lang="ja">神楽殿・祈願受付</span>, the prayer reception. The shrine office handles prayers and the goshuin from 8:00 to 17:00 (Jeepe). The cedar that stands in the grounds is called the sacred tree and is said to be about 800 years old (Tabi-mag).</p>

    <h2 id="ryoma">Ryoma and Oryo<span class="h2-jp">龍馬とお龍</span></h2>
    <p>Kirishima is also known as the setting for what is often called Japan&rsquo;s first honeymoon. After the Teradaya attack in 1866, Sakamoto Ryoma travelled to Satsuma with his wife Oryo, and the couple visited Kirishima (Japan National Tourism Organization). Tabi-mag says that on 29 March 1866 (Keio 2; 13 May in the Gregorian calendar) they climbed Takachiho no mine, then worshipped at this shrine and looked up at its great cedar. The details of their route vary between sources, so I would take the broad story and let the local walking maps fill in the rest.</p>

    <h2 id="getting-there">Getting There<span class="h2-jp">アクセス</span></h2>
"""+fig('express','A green limited express train marked KIRISHIMA EXPRESS standing at a station platform','The limited express <em>Kirishima</em>, photographed in 2007; the livery and train may since have changed')+"""
    <p>The usual route is the JR Nippo Main Line to Kirishima-Jingu Station. From Kagoshima-Chuo the limited express takes about 50 minutes, and from Miyazaki about 1 hour 20 minutes (Tokyo Weekender). The station is more than 5 km from the shrine (japan-guide), and a local bus takes 10 to 15 minutes (sources vary). Buses are infrequent, so plan the return before you step off.</p>

    <h2 id="visit">Visiting Kirishima Jingu<span class="h2-jp">参拝案内</span></h2>
    <ul class="practical-list">
      <li><strong>Address:</strong> 2608-5 Kirishima Taguchi, Kirishima City, Kagoshima.</li>
      <li><strong>Getting there:</strong> JR Kirishima-Jingu Station, then a 10 to 15 minute bus to the &ldquo;Kirishima Jingu&rdquo; stop. By car, about 35 to 40 minutes from Kagoshima Airport (ANA, Jeepe).</li>
      <li><strong>Fees and hours:</strong> grounds free and open at all times (GLTJP); shrine office 8:00 to 17:00 (Jeepe). Bus fares are given as &yen;240, &yen;290 and &yen;330 by different sources.</li>
      <li><strong>Parking:</strong> free; sources give about 350, 500 or 600 spaces, so treat the number as approximate.</li>
      <li><strong>Time needed:</strong> 20 to 30 minutes for the halls, about an hour with the grounds (Jeepe).</li>
      <li><strong>Wear:</strong> comfortable shoes and a light jacket; the shrine stands at about 500 m (Jeepe) with about 80 steps.</li>
      <li><strong>Pair it with:</strong> <a href="/guides/takachiho/" class="inline-link" onclick="trackEvent('click','internal','guide_kirishima_jingu_to_takachiho_pair')">Takachiho</a>, the mythology of the heavens and the cave, and our <a href="/culture/japanese-mythology/" class="inline-link" onclick="trackEvent('click','internal','guide_kirishima_jingu_to_mythology_pair')">Japanese mythology guide</a>.</li>
    </ul>
    <div class="key-callout">
      <p>&#127890; <strong>Plan your trip:</strong> Browse guided tours or find a stay near Kirishima. <a href="https://www.viator.com/search/Kirishima%20Kagoshima?pid=P00298374&amp;mcid=42383&amp;medium=link&amp;campaign=sacred-japan" target="_blank" rel="noopener" onclick="trackEvent('click','affiliate','viator_kirishima_jingu_inline')">Find tours on Viator &rarr;</a></p>
    </div>

    <h2 id="faq">Frequently Asked Questions<span class="h2-jp">よくあるご質問</span></h2>
    <div class="faq-stack">
"""+''.join(f"""    <details class="faq-item">
        <summary>{q}</summary>
        <div class="faq-answer">{a_}</div>
    </details>
""" for q,a_ in faqs)+"""    </div>

    <h2 id="final">Before You Go<span class="h2-jp">むすびに</span></h2>
    <p>Go early, walk up the steps slowly, and look at the carvings before you look at the god. The mountain behind the shrine is where the story says he landed.</p>

    <div class="closing-block">
      <span class="torii">&#9961;&#65039;</span>
      <p>The shrine sits low so that you can look up at the place the god came down.</p>
    </div>

    <section class="related-section">
      <h2>Related Guides</h2>
      <span class="h2-jp">関連ガイド</span>
      <div class="related-grid">
        <a class="related-card" href="/guides/takachiho/" onclick="trackEvent('click','internal','related_kirishima_jingu_to_takachiho')">
          <div class="related-card-label">SACRED JAPAN ／ GUIDES</div>
          <div class="related-card-title">&#127748; Takachiho &rarr;</div>
          <div class="related-card-desc">The cave, the gorge and the other half of the myth.</div>
        </a>
        <a class="related-card" href="/culture/japanese-mythology/" onclick="trackEvent('click','internal','related_kirishima_jingu_to_mythology')">
          <div class="related-card-label">SACRED JAPAN ／ CULTURE</div>
          <div class="related-card-title">&#128214; Japanese Mythology &rarr;</div>
          <div class="related-card-desc">Ninigi&rsquo;s descent in the context of the Kojiki.</div>
        </a>
        <a class="related-card" href="/culture/shrine-architecture/" onclick="trackEvent('click','internal','related_kirishima_jingu_to_architecture')">
          <div class="related-card-label">SACRED JAPAN ／ CULTURE</div>
          <div class="related-card-title">&#127983;&#65039; Shrine Architecture &rarr;</div>
          <div class="related-card-desc">How to read the roofs, halls and styles you have just seen.</div>
        </a>
      </div>
    </section>

  </article>

"""
tail=tail.replace('gifu-castle',SL).replace('gifu_castle','kirishima_jingu').replace('DGifu','DKirishima%20Kagoshima').replace('search/Gifu','search/Kirishima%20Kagoshima')
def L(u,l,t): return f'<a href="{u}" target="_blank" rel="noopener" style="color:var(--beni);text-decoration:underline;" onclick="trackEvent(\'click\',\'external\',\'{l}\')">{t}</a>'
src='Sources verified at time of writing: '+', '.join([
 L('https://kirishimajingu.or.jp','src_kj_official','Kirishima Jingu official site'),
 L('https://www.pref.kagoshima.jp/ba08/documents/101223_20221118112653-1.pdf','src_kj_pref','Kagoshima Prefecture'),
 L('https://www.gltjp.com/en/directory/item/11586/','src_kj_gltjp','GLTJP'),
 L('https://www.japan-guide.com/e/e4630.html','src_kj_jg','japan-guide'),
 L('https://www.tokyoweekender.com/location/kirishima-shrine/','src_kj_tw','Tokyo Weekender'),
 L('https://tabi-mag.jp/kg0205/','src_kj_tabimag','Tabi-mag'),
 L('https://www.jeepe.jp/ja/articles/kirishima-jingu-guide-1698','src_kj_jeepe','Jeepe'),
 L('https://www.japan.travel/en/spot/597/','src_kj_jnto','JNTO'),
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
l1="Kirishima Jingu Guide:"; l2="Ninigi's Shrine in Kagoshima"; assert d.textlength(l2,font=f1)<1090
d.text((66,170),l1,font=f1,fill=(26,15,15)); d.text((66,238),l2,font=f1,fill=(26,15,15)); d.text((66,332),"霧島神宮",font=f2,fill=(138,125,120))
im.save(R+f'images/og/og-guides-{SL}.jpg',quality=88)
b=Image.open(D+'images/lanterns.jpg'); w,h=b.size; ch=round(w*400/640); t=max(0,(h-ch)//2)
th=b.crop((0,t,w,t+ch)).resize((640,400),Image.LANCZOS); th.save(R+'images/hub/kirishima-jingu.jpg',quality=84); th.save(R+'images/hub/kirishima-jingu.webp',quality=80)
print('built',len(out))
