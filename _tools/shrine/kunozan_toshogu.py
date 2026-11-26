import sys; sys.path.insert(0,'/home/claude/sacred-japan/_tools/shrine')
from shrine_common import *
U=lambda n:'/mnt/user-data/uploads/%s-image.jpg'%n
S='/home/claude/sacred-japan/culture/shrine-architecture/images/'
def cs(t): return 'https://commons.wikimedia.org/w/index.php?search=%s&title=Special:MediaSearch&type=image'%t.replace(' ','+')
P={
'gate-front':(U('6b92a55c'),'Zairon','bysa4',cs('Kunozan Toshogu Zairon')),
'gate-low':(U('78e265f9'),'Zairon','bysa4',cs('Kunozan Toshogu Zairon')),
'gate-stairs':(U('bb72d335'),'Zairon','bysa4',cs('Kunozan Toshogu Zairon')),
'plaque':(U('45c189c2'),'Zairon','bysa4',cs('Kunozan Toshogu Zairon')),
'stairs-lanterns':(U('ade16ae4'),'Zairon','bysa4',cs('Kunozan Toshogu Zairon')),
'interior':(U('044416df'),'Zairon','bysa4',cs('Kunozan Toshogu Zairon')),
'hall-corner':(S+'kunozan-main-hall-corner.jpg','663highland','bysa4',cs('Kunozan Toshogu 663highland')),
'roofs':(S+'kunozan-main-hall-roofs.jpg','Zairon','bysa4',cs('Kunozan Toshogu Main Hall Zairon')),
'carving':(U('3ab05143'),'663highland','bysa4',cs('Kunozan Toshogu 663highland')),
'roof-tiles':(S+'kunozan-roof-tiles.jpg','baggio4ever','by3',cs('Kunozan Toshogu baggio4ever')),
}
faqs=[
("What is Kunozan Toshogu?","Kunozan Toshogu is the Shinto shrine on Mt. Kuno, east of Shizuoka City, where Tokugawa Ieyasu, the first Tokugawa shogun, is enshrined. Its own site calls it the first of the Toshogu shrines, and the first shrine buildings were put up on the orders of his successor, Hidetada, after Ieyasu&rsquo;s death in 1616 (shrine official site, Edo Legacy Travel)."),
("Is it a National Treasure?","Yes. The shrine&rsquo;s official site says the main shrine building, the <em>ishi-no-ma</em> and the worship hall were designated a National Treasure on 24 December 2010. The Romon gate is an Important Cultural Property."),
("Is Ieyasu buried here or at Nikko?","The two shrines tell the story differently. An MLIT text says Ieyasu asked for his body to be buried at Kunozan and his spirit to be enshrined at Nikko. Kunozan&rsquo;s official site says he is buried here, and the stone tower behind the hall is presented as his tomb. A Japanese government publication (Highlighting Japan) says he was entombed at Nikko a year later. Sources do not agree on what happened to the remains, so I would say only that this is his first resting place and the tower is his marked tomb."),
("How many steps are there?","The main stairway has 1,159 stone steps from the stone torii at the foot of the hill (official site, GLTJP). The first gate stands at step 909 (official site). Walking time is given as about 20 minutes (official access page), about 30 minutes (The Gate) and 30 to 40 minutes (Tokyo Weekender)."),
("What does it cost?","The official site lists shrine entry at 700 yen for adults, the museum at 600 yen, and a shrine-and-museum ticket at 1,200 yen (children 300, 300 and 500 yen). Older pages such as ANA still show 500 and 800 yen. The ropeway is extra; japan-guide gives 700 yen one way and 1,250 yen round trip. Confirm at the gate."),
("What are the opening hours?","9:00 to 17:00, open every day of the year, with last entry about ten minutes before closing (official site)."),
("Can I take the ropeway?","Yes. The Nihondaira Ropeway runs from the Nihondaira plateau to Kuno-zan in about five minutes (ANA). The official site says the stairs were the only route until the ropeway opened in 1957."),
]
def body(fig,a): return """<main>

"""+fig('gate-front','Red two-storey gate with a dark tiled roof, colourful painted brackets under the eaves, guardian statues at either side of the opening, visitors walking through and omamori stalls at the right','The red two-storey gate at Kunozan Toshogu, which I take to be the Romon (photographed September 2016)',hero=True)+"""
  <aside class="toc" aria-label="Table of contents">
    <div class="toc-label">TABLE OF CONTENTS ／ 目次</div>
    <div class="toc-title">In This Guide</div>
    <ol>
      <li><a href="#opening">The Shogun&rsquo;s First Shrine</a></li>
      <li><a href="#history">Ieyasu&rsquo;s Will and the First Shrine</a></li>
      <li><a href="#walk">The Stairway and the Gates</a></li>
      <li><a href="#hall">The National Treasure Halls</a></li>
      <li><a href="#tomb">The Tomb and the Museum</a></li>
      <li><a href="#visit">Visiting Kunozan Toshogu</a></li>
      <li><a href="#faq">Frequently Asked Questions</a></li>
      <li><a href="#final">Before You Go</a></li>
    </ol>
  </aside>

  <article>

    <p class="opening" id="opening">As a licensed guide, I like to send visitors to Kunozan before Nikko, because here you can see the first draft: the red-and-gold style that later made Nikko famous, on a hilltop above Suruga Bay, with far fewer people.</p>
    <p>Kunozan Toshogu stands on Mt. Kuno in Shizuoka and enshrines Tokugawa Ieyasu, who unified Japan and founded the shogunate that ruled for over 260 years (Edo Legacy Travel). Its official site calls it the first of the Toshogu shrines, and its main hall is in the <em>gongen-zukuri</em> style, the same layout used at Nikko (shrine official site). The halls were designated a National Treasure in 2010. This guide covers the history, the two ways up, what each building is, and the practical details. For the style itself, see our """+a('/culture/shrine-architecture/#styles','shrine architecture guide','architecture')+""".</p>

"""+fig('hall-corner','Side view of a vermilion and black lacquered shrine hall with gold fittings on its curved roofs, a red-railed stage in front and a National Treasure sign at the right','The worship hall seen at an angle, with a National Treasure sign at the right (photographed October 2023)')+"""
    <h2 id="history">Ieyasu&rsquo;s Will and the First Shrine<span class="h2-jp">家康の遺言</span></h2>
    <p>Ieyasu died at Sunpu Castle, now Shizuoka, on 17 April 1616 at the age of 75 (shrine official site, Trip.com). According to an MLIT text, he called his military and religious advisers together shortly before his death and told them to bury his body at Kunozan and enshrine his spirit at Nikko. His spirit was to be worshipped as Tosho Daigongen, the &ldquo;Great Shining Gongen of the East&rdquo;.</p>
    <p>His successor, Hidetada, ordered the shrine built here. The official site says construction began in May 1616 and took about one year and seven months, which by my arithmetic puts completion around the end of 1617. The builder was the master carpenter Nakai Masakiyo, and the official site describes the shrine as a masterpiece of his later years. Edo Legacy Travel says this made Kunozan the first of the many Toshogu shrines, including the more famous one at Nikko. Hidetada also built the first Nikko shrine in 1617 (Highlighting Japan), and the city of Nikko says its main buildings were rebuilt in 1636 under the third shogun, Iemitsu. Our """+a('/guides/nikko-toshogu/','Nikko Toshogu guide','nikko')+""" tells that part of the story.</p>
    <p>Where the remains lie is told differently by different sources, as the FAQ below sets out. What is clear is that Kunozan was Ieyasu&rsquo;s first resting place by his own request, and that the shrine presents the stone tower behind the hall as his tomb.</p>

    <h2 id="walk">The Stairway and the Gates<span class="h2-jp">石段と門</span></h2>
    <p>There are two ways up. The old one is the stone stairway from the foot of the hill, with <strong>1,159 steps</strong>; until the Nihondaira Ropeway opened in 1957 it was the only way to the shrine (official site, GLTJP). The first gate stands 909 steps up, and Visit Shizuoka says the view of Suruga Bay from there is worth the climb. The Gate counts 17 turns along the way. The ropeway takes about five minutes from Nihondaira (ANA) and is the sensible choice if you have limited time or knees. I would take the ropeway up and the steps down, or the other way round if you are fit, because the steps give the best sense of why Ieyasu was buried on a hilltop.</p>
"""+fig('stairs-lanterns','Wide stone stairway rising between bronze and stone lanterns to a gate with a green roof among tall trees, with a few visitors at the right','Bronze and stone lanterns at the foot of a stairway, with a gate at the top (photographed September 2016)')+"""
    <p>The official precinct guide lists the features in order from the entrance: the stairway, the first gate at step 909, the gatekeeper&rsquo;s house where a guard controlled entry in the Edo period, the two-storey <strong>Romon</strong>, the sacred stable, the drum tower, the former site of a five-storey pagoda (only the foundation stones remain, since the pagoda was dismantled in 1873), a hall that held framed poems, a storehouse modelled on the Shosoin at Todaiji, and a Hie shrine.</p>
    <p>The Romon is an Important Cultural Property and, according to the shrine, is said to be the model for the Yomeimon at Nikko. It carries the name &ldquo;Tosho Daigongen&rdquo; on its plaque.</p>
"""+fig('gate-low','Red two-storey gate seen from the bottom of a flight of steps, with a blue plaque in the middle, painted brackets under the eaves and pine and cedar trees on both sides','The gate seen from the steps below (photographed September 2016)')+fig('gate-stairs','Red two-storey gate seen from below among trees, with a blue plaque and brightly painted brackets under the upper eaves and a gap in the lower floor showing a stone-paved path beyond','The gate and its approach among the trees (photographed September 2016)')+fig('plaque','Close view under the roof of a red gate: dark blue plaque with gold characters in a gold frame, rows of red and white rafters above and blue, green and red painted brackets below','The plaque under the gate&rsquo;s upper eaves. The small gold characters are hard to read in the photo; the shrine says the gate bears the name Tosho Daigongen (photographed September 2016)')+"""
    <h2 id="hall">The National Treasure Halls<span class="h2-jp">国宝の社殿</span></h2>
    <p>The main shrine building, the <em>ishi-no-ma</em> and the worship hall were designated a National Treasure together on 24 December 2010 (shrine official site). In <em>gongen-zukuri</em> the main hall and worship hall are joined in an H-shaped plan by a stone-floored room between them; the Nikko city page describes the same arrangement for Nikko. At Kunozan, the official site says the main hall has three spaces, with Ieyasu in the centre and Oda Nobunaga and Toyotomi Hideyoshi on either side. Visit Shizuoka calls it the only National Treasure building in the prefecture.</p>
    <p>What strikes you first is the finish. The buildings are lacquered in black and red, with gold fittings, painted brackets and carved beasts under the eaves.</p>
"""+fig('roofs','Several curved tiled roofs with black lacquered gables and gold fittings seen from below beside a red eave and a blue sky','Roofs of the halls with their black lacquer and gold fittings, seen past a vermilion eave (photographed September 2016)')+fig('carving','Detail under the eaves of a black lacquered hall: golden dragon and lion heads project from blue, green and orange painted brackets, a gold roundel at lower left and a painted bird on the black wall','Carvings under the eaves. Gold dragon and lion heads project from painted brackets, a gold roundel at the lower left resembles the Tokugawa hollyhock crest (my reading), and a bird is painted on the black wall (photographed October 2023)')+fig('roof-tiles','Front of a hall with a black and gold gabled roof, red pillars, a patinated metal fitting hanging at the centre and green forest behind','The front of the halls with their black-and-gold gables (photographed May 2013)')+fig('interior','View into a hall between two black pillars: a gold gohei stands before gilded panels and an altar with hanging lanterns and tasselled curtains','Looking into the hall between two black pillars: a gold gohei stands in front of gilded decoration (photographed September 2016)')+"""
    <h2 id="tomb">The Tomb and the Museum<span class="h2-jp">神廟と博物館</span></h2>
    <p>Behind the main hall a path called the Byosho Sando leads to the <strong>Shinbyo</strong>, the tomb. Stone lanterns along the path were dedicated by Ieyasu&rsquo;s former military commanders, and the tomb itself is a stone tower about 5.5 metres tall that faces west, as Ieyasu instructed (official precinct guide). ANA says you climb about 40 steps from the mausoleum gate.</p>
    <p>The museum holds about 2,000 items (Visit Shizuoka), among them armor Ieyasu is said to have worn at Sekigahara and a National Treasure sword, plus a statue of Tosho Daigongen. Allow time for it, because the shrine and museum are separate tickets, though a combined one exists.</p>

    <h2 id="visit">Visiting Kunozan Toshogu<span class="h2-jp">参拝案内</span></h2>
    <ul class="practical-list">
      <li><strong>Address:</strong> 390 Negoya, Suruga Ward, Shizuoka City, Shizuoka (GLTJP, ANA).</li>
      <li><strong>Hours:</strong> 9:00 to 17:00, open every day, last entry about 10 minutes before closing (official site).</li>
      <li><strong>Admission (official site):</strong> shrine 700 yen, museum 600 yen, combined 1,200 yen for adults; children 300, 300 and 500 yen. ANA&rsquo;s older figures of 500 and 800 yen no longer match, so check at the gate.</li>
      <li><strong>Ropeway:</strong> Nihondaira Ropeway to Kuno-zan, about 5 minutes (ANA). japan-guide gives 700 yen one way, 1,250 yen round trip. The combined ropeway-and-admission ticket it lists (1,950 yen) is lower than the official prices add up to, so it may be out of date.</li>
      <li><strong>On foot:</strong> 1,159 steps from the foot of the hill; about 20 minutes (official), 30 minutes (The Gate) or 30 to 40 minutes (Tokyo Weekender). Tokyo Weekender says buses run from Shizuoka Station to the foot of the stairway; The Gate names the Kaidan-shita stop.</li>
      <li><strong>From Tokyo:</strong> the Tokaido Shinkansen reaches Shizuoka in about 60 to 75 minutes (Tokyo Weekender); Nihondaira is about 20 minutes by car from the Nihondaira-Kunozan Smart IC (Visit Shizuoka).</li>
      <li><strong>Time to allow:</strong> I would plan on one and a half to two hours with the museum and tomb, an estimate of mine.</li>
      <li><strong>Notes:</strong> if you climb, wear shoes with grip and allow rest stops; all 1,159 steps are stone.</li>
    </ul>
    <div class="key-callout">
      <p>&#127890; <strong>Plan your trip:</strong> Browse guided tours around Shizuoka and Mt. Fuji. <a href="https://www.viator.com/search/Shizuoka?pid=P00298374&amp;mcid=42383&amp;medium=link&amp;campaign=sacred-japan" target="_blank" rel="noopener" onclick="trackEvent('click','affiliate','viator_kunozan_toshogu')">Book a Tour</a></p>
    </div>

    <h2 id="faq">Frequently Asked Questions<span class="h2-jp">よくあるご質問</span></h2>
    <div class="faq-stack">
@@FAQ@@    </div>

    <h2 id="final">Before You Go<span class="h2-jp">むすびに</span></h2>
    <p>Pair Kunozan with the Nikko guide for the full Toshogu story, and with """+a('/guides/fujisan-hongu-sengen-taisha/','Fujisan Hongu Sengen Taisha','fujisan')+""" if you are staying in Shizuoka. Go in the morning, take the ropeway one way and the steps the other, and keep a little time for the tomb.</p>

    <div class="closing-block">
      <span class="torii">&#9961;&#65039;</span>
      <p>The first Toshogu: a shogun&rsquo;s first resting place, in red, black and gold above the bay.</p>
    </div>

    <section class="related-section">
      <h2>Related Guides</h2>
      <span class="h2-jp">関連ガイド</span>
      <div class="related-grid">
        <a class="related-card" href="/guides/nikko-toshogu/" onclick="trackEvent('click','internal','related_kunozan_to_nikko')">
          <div class="related-card-label">SACRED JAPAN ／ GUIDES</div>
          <div class="related-card-title">&#9961;&#65039; Nikko Toshogu &rarr;</div>
          <div class="related-card-desc">The golden shrine that made a shogun a god.</div>
        </a>
        <a class="related-card" href="/culture/shrine-architecture/" onclick="trackEvent('click','internal','related_kunozan_to_architecture')">
          <div class="related-card-label">SACRED JAPAN ／ CULTURE</div>
          <div class="related-card-title">&#127963;&#65039; Shrine Architecture &rarr;</div>
          <div class="related-card-desc">Styles, roofs, parts and how shrines are built.</div>
        </a>
        <a class="related-card" href="/guides/fujisan-hongu-sengen-taisha/" onclick="trackEvent('click','internal','related_kunozan_to_fujisan')">
          <div class="related-card-label">SACRED JAPAN ／ GUIDES</div>
          <div class="related-card-title">&#128507;&#65039; Fujisan Hongu Sengen Taisha &rarr;</div>
          <div class="related-card-desc">Mt. Fuji&rsquo;s head shrine, in Shizuoka.</div>
        </a>
      </div>
    </section>

  </article>

"""
build(dict(slug='kunozan-toshogu',ev='kunozan_toshogu',jp='久能山東照宮',en='Kunozan Toshogu',dest='Shizuoka',thumb='gate-front',photos=P,faqs=faqs,body=body,
 title="Kunozan Toshogu Guide: Ieyasu's First Shrine, 1,159 Steps and a National Treasure Hall",
 desc="A licensed guide's guide to Kunozan Toshogu in Shizuoka: Tokugawa Ieyasu's first shrine, the 1,159-step stairway and the Nihondaira Ropeway, the National Treasure gongen-zukuri halls, the tomb and museum, fees and hours.",
 tag="The first Toshogu shrine, on a hilltop above Suruga Bay, with National Treasure halls in red, black and gold.",
 kw="Kunozan Toshogu, Kunozan Toshogu Shrine, Tokugawa Ieyasu shrine, Shizuoka shrine, Nihondaira Ropeway, gongen-zukuri, National Treasure shrine, 1159 steps, Toshogu",
 h1="<h1><em>Kunozan Toshogu</em>: Ieyasu&rsquo;s First Shrine, 1,159 Steps and a National Treasure Hall</h1>",
 og=("Kunozan Toshogu Guide:","Ieyasu's First Shrine"),
 sources=[('https://www.toshogu.or.jp/english','official','Kunozan Toshogu official site'),('https://www.toshogu.or.jp/english/precincts/','precincts','Official precinct guide'),('https://www.toshogu.or.jp/english/access','access','Official access page'),('https://www.gltjp.com/en/directory/item/11865/','gltjp','GLTJP'),('https://www.visit-shizuoka.com/en/spot/detail_415.html','vs','Visit Shizuoka (steps)'),('https://www.visit-shizuoka.com/en/spot/detail_170.html','vs170','Visit Shizuoka (museum)'),('https://www.visit-shizuoka.com/en/spot/detail_21.html','vs21','Visit Shizuoka (ropeway)'),('https://www.ana.co.jp/en/fr/japan-travel-planner/shizuoka/0000016.html','ana','ANA'),('https://www.mlit.go.jp/tagengo-db/common/001565738.pdf','mlit','MLIT multilingual guide'),('https://gov-online.go.jp/eng/publicity/book/hlj/html/201606/201606_07_en.html','hlj','Highlighting Japan'),('https://www.city.nikko.lg.jp/soshiki/10/1041/1_1/2/6/1393.html','nikko','Nikko city'),('https://edolegacytravel.metro.tokyo.lg.jp/?p=694','edo','Edo Legacy Travel'),('https://japan-guide.com/e/e6353.html','jg','japan-guide'),('https://thegate12.com/article/47','gate','The Gate'),('https://www.tokyoweekender.com/?p=286188','tw','Tokyo Weekender'),('https://au.trip.com/moments/poi-kunouzan-toshogu-90400','trip','Trip.com')]))
