import re,json,os,glob,shutil
from PIL import Image,ImageDraw,ImageFont
R='/home/claude/sacred-japan/'; SL='hakuto-jinja'; D=R+f'guides/{SL}/'
os.makedirs(D+'images',exist_ok=True); SRC=R+'culture/japanese-mythology/images/'
LIC={'by3':('CC BY 3.0','https://creativecommons.org/licenses/by/3.0/'),
     'by4':('CC BY 4.0','https://creativecommons.org/licenses/by/4.0/'),
     'by21jp':('CC BY 2.1 JP','https://creativecommons.org/licenses/by/2.1/jp/'),
     'cc0':('CC0 1.0','https://creativecommons.org/publicdomain/zero/1.0/'),
     'pd':('public domain','https://commons.wikimedia.org/wiki/Commons:Public_domain')}
def CS(t): return 'https://commons.wikimedia.org/w/index.php?search='+t.replace(' ','+')+'&title=Special:MediaSearch&type=image'
# slug:(source file, author, lic, commons link)  -- all re-used from culture/japanese-mythology (credits already verified there)
P={
'approach':('hakuto-approach','tme181','by3',CS('Hakuto Shrine Tottori approach')),
'rabbit-run':('hakuto-rabbit-run','tme181','by3',CS('Hakuto Shrine Tottori rabbit')),
'rabbit-path':('hakuto-rabbit-path','tme181','by3',CS('Hakuto Shrine Tottori rabbit')),
'rabbit-sea':('hakuto-rabbit-sea','tme181','by3',CS('Hakuto Shrine Tottori rabbit')),
'haiden':('hakuto-haiden','Cheetah.in.mac','pd',CS('Hakuto Shrine Tottori')),
'sign':('hakuto-sign','tme181','by3',CS('Hakuto Shrine Tottori sign')),
'coast-2012':('hakuto-coast-2012','荒川鯉師','by21jp',CS('Hakuto Coast Tottori')),
'coast-sunrise':('hakuto-coast-sunrise','rikky_photography (uploaded by Bioika0201)','by4',CS('Hakuto Coast morning Tottori')),
'okinoshima':('hakuto-okinoshima','rikky_photography (uploaded by Bioika0201)','by4',CS('Hakuto Coast Okinoshima Tottori')),
'yazu':('hakuto-yazu','Msht05','cc0',CS('Tottori Yazu Hakuto Shrine rabbit')),
}
for k,v in P.items():
    for ext in ('jpg','webp'):
        shutil.copyfile(SRC+v[0]+'.'+ext,D+f'images/{k}.{ext}')
SIZE={k:Image.open(D+f'images/{k}.jpg').size for k in P}
def fig2(k,alt,cap,date,hero=False):
    u,a,l,cl=P[k]; ln,lu=LIC[l]; w,h=SIZE[k]
    if hero: st='margin:0 0 48px;'; ld='eager'; ims='style="width:100%;max-height:420px;object-fit:cover;border-radius:4px;display:block;"'
    else:
        mw=min(420 if h>w else 760,w)
        st='margin:28px auto;max-width:%dpx;'%mw; ld='lazy'; ims='style="width:100%;height:auto;border-radius:4px;display:block;"'
    lic=f'<a href="{lu}" target="_blank" rel="noopener">{ln}</a>'
    return f'''<figure style="{st}"><picture><source srcset="/guides/{SL}/images/{k}.webp" type="image/webp"><img src="/guides/{SL}/images/{k}.jpg" alt="{alt}" width="{w}" height="{h}" loading="{ld}" {ims}></picture><figcaption style="font-size:13px;color:var(--enshu);margin-top:10px;text-align:center;line-height:1.6;">{cap}.<br>Photo: <a href="{cl}" target="_blank" rel="noopener">{a}</a>, {date}, {lic}, via Wikimedia Commons (resized)</figcaption></figure>
'''
fig=fig2
s=open(R+'guides/gifu-castle/index.html',encoding='utf-8').read()
i=s.index('<main>'); j=s.index('</main>'); head,tail=s[:i],s[j:]
TITLE="Hakuto Shrine Guide: The White Hare of Inaba, Stone Rabbits and Tottori's Hakuto Coast"
DESC="A licensed guide's guide to Hakuto Shrine in Tottori: the Kojiki's white hare of Inaba, the rabbit-lined approach, musubi stones, the Hakuto Coast and Oki no Shima, and how to get there by bus from Tottori Station."
TAG="The shrine of the white hare of Inaba in Tottori, shown in photos from the stone rabbits to the Hakuto Coast."
head=re.sub(r'<title>.*?</title>',f'<title>{TITLE} | Sacred Japan</title>',head,count=1)
head=re.sub(r'(<meta (?:name="description"|property="og:description"|name="twitter:description") content=")[^"]*(")',lambda m:m.group(1)+DESC+m.group(2),head)
head=re.sub(r'(<meta (?:property="og:title"|name="twitter:title") content=")[^"]*(")',lambda m:m.group(1)+TITLE+m.group(2),head)
head=re.sub(r'("headline": ")[^"]*(")',lambda m:m.group(1)+TITLE+m.group(2),head)
head=re.sub(r'("description": ")A licensed[^"]*(")',lambda m:m.group(1)+DESC+m.group(2),head)
head=re.sub(r'("date(?:Published|Modified)": ")[^"]*(")',lambda m:m.group(1)+'2026-11-25'+m.group(2),head)
head=re.sub(r'<meta name="keywords" content="[^"]*">','<meta name="keywords" content="Hakuto Shrine, Hakuto Jinja, white hare of Inaba, white rabbit of Inaba, Tottori shrine, Hakuto Coast, Okuninushi, Princess Yakami, matchmaking shrine Tottori, rabbit shrine Japan">',head)
head=head.replace('guides/gifu-castle',f'guides/{SL}').replace('guide_gifu_castle_','guide_hakuto_').replace('og-guides-gifu-castle',f'og-guides-{SL}')
head=head.replace('岐阜城','白兎神社').replace('Gifu Castle','Hakuto Shrine')
head=re.sub(r"<h1>.*?</h1>","<h1><em>Hakuto Shrine</em>: The White Hare of Inaba, Stone Rabbits and Tottori\'s Hakuto Coast</h1>",head,count=1,flags=re.S)
head=head.replace("Nobunaga's mountain castle above Gifu, with the keep closed until late 2027.",TAG)
head=head.replace('SACRED JAPAN GUIDES ／ 城','SACRED JAPAN GUIDES ／ 神社')
IL='class="inline-link"'
def a(u,t,ev): return f'<a href="{u}" {IL} onclick="trackEvent(\'click\',\'internal\',\'guide_hakuto_to_{ev}\')">{t}</a>'
faqs=[
("Who is enshrined at Hakuto Shrine?","The main deity is the White Hare God (Hakuto-kami), the hare of the Inaba story itself (Fun! JAPAN). It is an unusual shrine in that the god is the animal, not the hero who helped it. The Kojiki&rsquo;s own ending, as quoted on a Japanese shrine-description page, says the hare is now called the rabbit god."),
("What is Hakuto Shrine known for?","Two things. Because Okuninushi healed the hare, it is prayed to for burns, skin ailments and, according to Fun! JAPAN and the city of Tottori, animal and human medicine. Because the hare foretold Okuninushi&rsquo;s marriage to Princess Yakami, it is a matchmaking shrine and is certified as a &ldquo;sacred place for lovers&rdquo; (GLTJP)."),
("What are the musubi-ishi stones?","They are sets of five small white stones, each engraved with the character <span lang=\"ja\">縁</span> (<em>en</em>, a bond). GLTJP says you place them on the torii or the rabbit statues with a wish, or carry them as a charm. Fun! JAPAN says you throw one onto the top of the second torii. Check at the shrine office for the current price and how they want them used."),
("How do I get to Hakuto Shrine?","Take the Hinomaru bus from JR Tottori Station and get off at Hakuto Jinja-mae. Most sources give about 40 minutes (JNTO, GLTJP, Torican); GaijinPot says about 35. A GIGAZINE visit from early 2023 gives a fare of 610 yen on lines 41 or 41H from platform 4, but fares change. A taxi from the station takes about 20 minutes (Torican). The shrine is a few minutes&rsquo; walk from the bus stop."),
("Can I combine it with the Tottori Sand Dunes?","Yes. Torican suggests a 3.5-hour car itinerary of Hakuto Shrine, the Karoichi fish market and then the Tottori Sand Dunes. One map site puts the dunes about 11 km from the Hakuto Coast. If you rely on buses, check timetables carefully before you plan a combined day."),
("Is Hakuto Shrine connected to Izumo Taisha?","Through the story, yes. Okuninushi, whom the hare helped, is the god of Izumo Taisha, and Princess Yakami is the woman he marries; Fun! JAPAN notes there are white-rabbit statues at Izumo Taisha too. Hakuto Shrine is in Tottori, the old province of Inaba, so it is a natural stop on a trip between the two regions."),
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
      <li><a href="#opening">The Shrine of a Rabbit</a></li>
      <li><a href="#myth">The Story in Brief</a></li>
      <li><a href="#approach">The Rabbit-Lined Approach</a></li>
      <li><a href="#stones">Musubi-ishi, Charms and Omikuji</a></li>
      <li><a href="#hall">The Hall and the Pond</a></li>
      <li><a href="#coast">Hakuto Coast and Oki no Shima</a></li>
      <li><a href="#yazu">Another White Hare Shrine?</a></li>
      <li><a href="#visit">Visiting Hakuto Shrine</a></li>
      <li><a href="#faq">Frequently Asked Questions</a></li>
      <li><a href="#final">Before You Go</a></li>
    </ol>
  </aside>

  <article>

"""+fig('approach','Straight stone-paved path up a gentle slope between green hedges, with small white rabbit figures on short stone posts along both sides leading to a distant torii','The approach to Hakuto Shrine, with small white rabbits on stone posts along both sides of the path','5 December 2010',hero=True)+"""
    <p class="opening" id="opening">As a licensed guide, I find that many visitors know the Izumo story but few know the shrine where it begins. Hakuto Shrine in Tottori honours a rabbit. It is the White Hare of Inaba from the Kojiki, the creature that tricked a row of sharks, lost its fur, and became the matchmaker between a god and a princess.</p>
    <p>The shrine is small, and the walk from the torii to the hall takes only minutes. What makes it worth the bus ride is the path: stone rabbits in different poses, the pond where the hare is said to have washed, and a coast across the road where the story is set. This guide walks it in ten photos.</p>

    <h2 id="myth">The Story in Brief<span class="h2-jp">因幡の白兎</span></h2>
    <p>Fun! JAPAN tells it this way, following the Kojiki. Okuninushi and his many brothers, the Yasogami, travel to Inaba to court Princess Yakami. At Keta no Saki, the cape, they find a hare whose skin has been stripped. The hare had tricked sharks into lining up as a bridge so it could cross the sea (from the island of Oki, according to Wikipedia), and the last shark tore off its fur. The brothers, being cruel, tell the hare to bathe in seawater and lie in the wind, which only makes the pain worse. Okuninushi, walking behind them with the luggage, tells it instead to wash in fresh river water and lie on cattail pollen. The hare recovers, and it predicts that Princess Yakami will choose Okuninushi, not his brothers. She does.</p>
    <p>That is the mythical hook for everything you see here. For the wider story of Okuninushi, see our """+a('/culture/japanese-mythology/#okuninushi','Japanese mythology guide','mythology')+""" and the """+a('/guides/izumo-taisha/','Izumo Taisha guide','izumo')+""". The sea the hare crossed was probably the one in front of you; the Hakuto Coast is traditionally identified as Keta no Saki.</p>

    <h2 id="approach">The Rabbit-Lined Approach<span class="h2-jp">参道のうさぎ</span></h2>
    <p>Hakuto Shrine sits on a low hill above the beach, beside a roadside station. After the torii, the path is lined with stone rabbits, each in a different pose (Fun! JAPAN). GIGAZINE adds that at the start of the approach stand statues of Okuninushi and a white rabbit crossing on a shark, that rabbit motifs appear on the stair lights, and that a sand sculpture is renewed every twelve years, in the Year of the Rabbit. If that cycle holds, the next would be in 2035; that is my arithmetic, so check before you plan around it.</p>
"""+fig('rabbit-run','Grey granite rabbit in a stretched, leaping pose on a square stone post, with white pebbles marked in red characters and a few small coins scattered on the post, dark grass behind','A small granite rabbit caught mid-leap, with white pebbles marked in red laid on its post','5 December 2010')+"""
    <p>This rabbit is stretched out as if it were jumping across the sea. White pebbles with red characters sit on the post, and a few coins have been left. The character on the bigger pebbles looks like <span lang="ja">縁</span> (<em>en</em>, &ldquo;bond&rdquo;) as I read it. That fits the musubi-ishi described below, which visitors place on the rabbits and on the torii.</p>
"""+fig('rabbit-path','Small grey granite rabbit crouching on a stone post with white pebbles around it, looking up a blurred path toward a torii in the shade, with a pale rock wall on the right','A second rabbit, crouched on its post and facing a torii up a shaded path','5 December 2010')+"""
    <p>A second rabbit crouches and looks up a shaded path toward a torii. The Commons description gives only the shrine name, so I cannot say where along the grounds this post stands. Each rabbit has its own pose, and finding the one you like is part of the visit.</p>
"""+fig('rabbit-sea','Grey granite rabbit sitting upright in profile on a stone post, looking left past a blurred torii and car park toward a pale sea and sky, with a few white pebbles at its feet','A rabbit sitting upright and looking out toward the sea, with a blurred torii and the car park behind','5 December 2010')+"""
    <p>The third sits up in profile and looks out toward the water, with a blurred torii and the car park behind it. Facing the sea suits a story about crossing it, though that is my reading of the pose, not something the shrine says. It also shows how close the shared car park is to the shrine.</p>

    <h2 id="stones">Musubi-ishi, Charms and Omikuji<span class="h2-jp">結び石・お守り</span></h2>
    <p>The best-known item is the <em>musubi-ishi</em>, a set of five small white stones, each carved with <span lang="ja">縁</span>. GLTJP says you place them on the torii or on the rabbit statues with a wish, or keep them as a charm. Fun! JAPAN gives a slightly different method: throw one onto the top of the second torii, and take the rest home. Ask at the shrine office if you are unsure which they prefer.</p>
    <p>Fun! JAPAN also lists a heart-shaped rabbit ema, a large rabbit-ear matchmaking omamori and a white-rabbit omikuji. GLTJP confirms that goshuin are available and says the omikuji shaped like a white rabbit are sold at the shrine office. A 2010 Tottori city magazine describes a <em>kishomon</em>, a washi vow sheet in sets of three: one for each partner to take home and the third burned at the shrine. That was reported over a decade ago, so ask whether it is still offered. GLTJP says foreign-language pamphlets are not available, but the shrine has a foreign-language page on its official site (hakutojinja.jp).</p>

    <h2 id="hall">The Hall and the Pond<span class="h2-jp">拝殿と池</span></h2>
"""+fig('haiden','Front of a small shrine hall with a huge twisted rope hung across it under the eaves, and a gold-lettered plaque above it reading the shrine name','The worship hall of Hakuto Shrine, with a thick shimenawa hung across the front and the gold plaque with the shrine&rsquo;s name','16 August 2009')+"""
    <p>The hall is modest, with a thick shimenawa hanging across the front and a gold plaque bearing the shrine&rsquo;s name. Its main deity is the White Hare God, and its blessings follow the myth: skin diseases and burns, and matchmaking. GIGAZINE notes that the guardian dogs are ordinary komainu, not rabbits, but that the hand-washing basin uses a rabbit motif instead of the usual dragon. The 2009 photo is the only one of the hall I have a licence for; the hall may look different now.</p>
"""+fig('sign','Large grey wooden signboard under a green roof with big white painted characters reading the shrine name, and smaller text in columns below','The shrine&rsquo;s explanatory board','5 December 2010')+"""
    <p>The explanatory board gives the main deity as the white hare god and the address in Tottori City, and, as I read it, an annual festival on 17 April. It retells the hare story and says the shrine is known for medicine and for matchmaking. I could not confirm the festival date elsewhere, so ask the shrine before you plan a trip around it.</p>
    <p>The pond on the grounds is where the hare is said to have washed its wounds. Its name varies by source: GLTJP calls it Misoroi Pond, GIGAZINE writes Mimiarai, and a Japanese travel site writes <em>mitarashi</em> (the same sound as a purification pond). The point everyone agrees on is that the water level hardly changes, so it is also called <span lang="ja">不増不滅</span> (<em>fuzo-fumetsu</em>, &ldquo;neither increasing nor decreasing&rdquo;). GLTJP also mentions a grove of native trees west of the approach, designated a national natural monument; I found that in one source only.</p>

    <h2 id="coast">Hakuto Coast and Oki no Shima<span class="h2-jp">白兎海岸と淤岐ノ島</span></h2>
    <p>Across the road lies the sea. The roadside station <em>Shinwa no Sato Shirousagi</em>, &ldquo;Village of Myth: White Rabbit&rdquo;, stands between the shrine and the beach, and GIGAZINE says a pedestrian bridge near it leads to the beach. Torican lists winter hours of 8:30 to 18:00 (3 December to 28 February); other seasons may differ. Fun! JAPAN adds a second-floor restaurant overlooking the beach.</p>
"""+fig('coast-2012','Long sandy beach with waves rolling in under a clear blue sky, a small dark rock standing out in the surf in the distance and a strip of dry grass in the foreground','The Hakuto Coast in winter, looking northwest according to the Commons description','27 December 2012')+"""
    <p>A long strip of sand curves away, with a small dark rock out in the surf. Local sources treat this coast as the Keta no Saki of the Kojiki. The photo is from 2012 and only 800 pixels wide, so I have not enlarged it.</p>
"""+fig('coast-sunrise','Wide view of a curving beach with turquoise waves and white surf, heavy dark clouds above and a band of golden light at the horizon, pine branches in the lower left and a few buildings on the far shore','The Hakuto Coast in the morning light, from the FIND/47 project (Commons description)','25 January 2020')+"""
    <p>In January 2020 the Japan Sea was rough and the clouds were heavy, with only a thin band of gold at the horizon. It is a good picture of the coast in winter. Japan Experience calls the beach a good place to watch the sunset, so summer evenings should look very different.</p>
"""+fig('okinoshima','Dark rock island in a pale blue sea, with white surf swirling around it in a long exposure and a small light-coloured torii standing on its top beside a few pine branches','Oki no Shima (as the Commons title writes it), a rock just off the coast, shot in long exposure with a small torii on top','25 January 2020')+"""
    <p>This is the rock the Commons title calls <span lang="ja">淤岐ノ島</span> (<em>Oki no Shima</em>). Fun! JAPAN puts it about 150 metres offshore and says it looks like a jumping rabbit, and GIGAZINE says it resembles a rabbit when seen from the side. The name echoes the island of Oki in the Kojiki. A small torii stands on top. I could not confirm how local tradition links the rock to the story, so I show it as a place to look at, not a proven site of the myth.</p>
    <p>One caution: Japan Experience and Fun! JAPAN describe the beach as popular for summer swimming and surfing, but a Deep Experience page says swimming is currently prohibited. I cannot tell which is current, so check locally before you pack a swimsuit.</p>

    <h2 id="yazu">Another White Hare Shrine?<span class="h2-jp">八頭町の小さな社</span></h2>
"""+fig('yazu','Small wooden shrine on a stone platform in the middle of rice fields, with two grey stone rabbits on pedestals at the steps, one standing on its hind legs, and bare trees and a village behind','A small shrine with stone rabbits at its steps; the Commons title places it in Yazu Town, Tottori','25 December 2024')+"""
    <p>Tottori has more than one place where the hare is remembered. This small shrine in the rice fields has two stone rabbits at its steps, and the Commons title places it in Yazu Town, inland from the coast. It appears to be a different, much smaller shrine from the one on the coast. I could not confirm which tradition it follows, so treat it as a sign of how widely the story is loved rather than as an official sister shrine.</p>

    <h2 id="visit">Visiting Hakuto Shrine<span class="h2-jp">参拝案内</span></h2>
    <ul class="practical-list">
      <li><strong>Address:</strong> 603 Hakuto, Tottori City, Tottori 689-0206 (GLTJP). Phone 0857-59-0047.</li>
      <li><strong>By bus:</strong> from JR Tottori Station, take the Hinomaru bus and get off at Hakuto Jinja-mae; about 40 minutes (JNTO, GLTJP, Torican), 35 minutes in GaijinPot. The shrine and roadside station are a few minutes&rsquo; walk away. Check the timetable, as buses are not frequent in Tottori.</li>
      <li><strong>By taxi or car:</strong> about 20 minutes by taxi from Tottori Station (Torican). By car, about 20 minutes from the expressway exit; sources name different exits (Tottori IC and Tottori Nishi IC), so use your navigation. Parking is shared with the roadside station, free, with 125 spaces (Torican).</li>
      <li><strong>By train:</strong> Torican gives about 5 minutes by car or 45 minutes on foot from JR Hogi Station, as it spells the name.</li>
      <li><strong>Hours and fees:</strong> the grounds are open at any time and free. The shrine office is open 9:00 to 16:00. No credit cards, and no coin lockers (GLTJP).</li>
      <li><strong>Time needed:</strong> about an hour for the shrine and a short beach walk is my estimate, not an official figure. Add time for the roadside station.</li>
      <li><strong>Pair it with:</strong> the Tottori Sand Dunes; Torican&rsquo;s 3.5-hour car itinerary runs Hakuto Shrine, then the Karoichi fish market, then the dunes. Torican also lists the Tottori Inaba G Bus day tour, which includes the shrine (updated June 2025; check the current schedule).</li>
    </ul>
    <div class="key-callout">
      <p>&#127890; <strong>Plan your trip:</strong> Browse guided tours or find a stay in Tottori. <a href="https://www.viator.com/search/Tottori?pid=P00298374&amp;mcid=42383&amp;medium=link&amp;campaign=sacred-japan" target="_blank" rel="noopener" onclick="trackEvent('click','affiliate','viator_hakuto')">Book a Tour</a></p>
    </div>

    <h2 id="faq">Frequently Asked Questions<span class="h2-jp">よくあるご質問</span></h2>
    <div class="faq-stack">
"""+''.join(f"""    <details class="faq-item">
        <summary>{q}</summary>
        <div class="faq-answer">{a_}</div>
    </details>
""" for q,a_ in faqs)+"""    </div>

    <h2 id="final">Before You Go<span class="h2-jp">むすびに</span></h2>
    <p>Walk the rabbit path slowly, leave a stone with your wish if you want to, and then cross the road to the sea. Hakuto Shrine is easy to overlook on a map, but it is the one place where the Izumo story has a beach and a rabbit to go with it.</p>

    <div class="closing-block">
      <span class="torii">&#9961;&#65039;</span>
      <p>A small shrine, a famous rabbit, and the sea it crossed.</p>
    </div>

    <section class="related-section">
      <h2>Related Guides</h2>
      <span class="h2-jp">関連ガイド</span>
      <div class="related-grid">
        <a class="related-card" href="/culture/japanese-mythology/" onclick="trackEvent('click','internal','related_hakuto_to_mythology')">
          <div class="related-card-label">SACRED JAPAN ／ CULTURE</div>
          <div class="related-card-title">&#128302; Japanese Mythology &rarr;</div>
          <div class="related-card-desc">Okuninushi, the Kojiki and the shrines where each myth happens.</div>
        </a>
        <a class="related-card" href="/guides/izumo-taisha/" onclick="trackEvent('click','internal','related_hakuto_to_izumo')">
          <div class="related-card-label">SACRED JAPAN ／ GUIDES</div>
          <div class="related-card-title">&#9961;&#65039; Izumo Taisha &rarr;</div>
          <div class="related-card-desc">The shrine of Okuninushi, the god the hare helped.</div>
        </a>
        <a class="related-card" href="/culture/omamori-guide/" onclick="trackEvent('click','internal','related_hakuto_to_omamori')">
          <div class="related-card-label">SACRED JAPAN ／ CULTURE</div>
          <div class="related-card-title">&#127884; Omamori Guide &rarr;</div>
          <div class="related-card-desc">What each type of amulet is for, and how to use it.</div>
        </a>
      </div>
    </section>

  </article>

"""
tail=tail.replace('gifu-castle',SL).replace('gifu_castle','hakuto').replace('DGifu','DTottori').replace('search/Gifu','search/Tottori')
def L(u,l,t): return f'<a href="{u}" target="_blank" rel="noopener" style="color:var(--beni);text-decoration:underline;" onclick="trackEvent(\'click\',\'external\',\'{l}\')">{t}</a>'
src='Sources verified at time of writing: '+', '.join([
 L('https://gltjp.com/en/directory/item/15612','src_hk_gltjp','GLTJP'),
 L('https://fun-japan.jp/en/articles/13176','src_hk_fun','Fun! JAPAN'),
 L('https://gigazine.net/gsc_news/en/20230101-tottori-hakuto-shrine','src_hk_gigazine','GIGAZINE'),
 L('https://www.torican.jp/en/spot/detail_1003.html','src_hk_torican','Torican: Hakuto Shrine'),
 L('https://www.torican.jp/en/spot/detail_1073.html','src_hk_torican2','Torican: Shinwa-no-sato Shirousagi'),
 L('https://www.japan.travel/en/japans-local-treasures/hakuto-shrine-2022/','src_hk_jnto','JNTO'),
 L('https://www.japan-experience.com/all-about-japan/tottori/temples-shrines/hakutojinja','src_hk_je','Japan Experience'),
 L('https://travel.gaijinpot.com/hakuto-beach/','src_hk_gaijinpot','GaijinPot Travel'),
 L('https://www.deep-exp.com/en/tottori/spot/2903','src_hk_deep','Deep Experience'),
 L('https://www.city.tottori.lg.jp/www/contents/1290413124417/simple/common/other/4cea26a4004.pdf','src_hk_city','Tottori City magazine (Dec 2010)'),
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
l1="Hakuto Shrine Guide:"; l2="The White Hare of Inaba"; assert d.textlength(l2,font=f1)<1090
d.text((66,170),l1,font=f1,fill=(26,15,15)); d.text((66,238),l2,font=f1,fill=(26,15,15)); d.text((66,332),"白兎神社",font=f2,fill=(138,125,120))
im.save(R+f'images/og/og-guides-{SL}.jpg',quality=88)
b=Image.open(D+'images/approach.jpg'); w,h=b.size; ch=round(w*400/640); t=max(0,(h-ch)//2)
th=b.crop((0,t,w,t+ch)).resize((640,400),Image.LANCZOS); th.save(R+f'images/hub/{SL}.jpg',quality=84); th.save(R+f'images/hub/{SL}.webp',quality=80)
print('built',len(out))
