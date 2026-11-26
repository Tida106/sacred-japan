import sys; sys.path.insert(0,'/home/claude/sacred-japan/_tools/shrine')
from shrine_common import *
M='/home/claude/sacred-japan/culture/japanese-mythology/images/'
def cs(t): return 'https://commons.wikimedia.org/w/index.php?search=%s&title=Special:MediaSearch&type=image'%t.replace(' ','+')
P={
'main-hall':(M+'udo-main-hall.jpg','MaedaAkihiko','bysa4',cs('Udo Shrine main hall sea cave')),
'panorama':(M+'udo-panorama.jpg','z tanuki','by3',cs('Udo Shrine Nichinan panorama')),
'tamabashi':(M+'udo-tamabashi.jpg','Sanjo','bysa3',cs('Udo Jingu from Tamabashi')),
'stairs':(M+'udo-stairs.jpg','Raita Futo','by2',cs('Udo Shrine Nichinan Miyazaki')),
'overlook':(M+'udo-overlook.jpg','Raita Futo','by2',cs('Udo Shrine Nichinan Miyazaki')),
'gate-ceremony':(M+'udo-gate-ceremony.jpg','そらみみ','bysa4',cs('Gate in front of Gishikiden Hall of Udo Shrine')),
'romon-2008':(M+'udo-romon-2008.jpg','TAKA@P.P.R.S','bysa2',cs('Udo Shrine gate Nichinan Miyazaki')),
'romon-2009':(M+'udo-romon-2009.jpg','z tanuki','by3',cs('Udo Shrine Nichinan Miyazaki')),
'romon-sign':(M+'udo-romon-sign-2009.jpg','z tanuki','by3',cs('Udo Shrine Nichinan Miyazaki')),
}
faqs=[
("What is Udo Shrine?","Udo Shrine (Udo Jingu) in Nichinan, Miyazaki, is a Shinto shrine whose main hall stands inside a sea cave in a cliff facing the Hyuga Sea (Tokyo Weekender, GLTJP). It is dedicated to Ugayafukiaezu, the father of Emperor Jimmu, the legendary first emperor (MLIT, japan-guide). Local belief holds that he was born in this cave (MLIT)."),
("What is the legend behind the cave?","Toyotama, daughter of the sea god, came ashore to give birth to Hoori&rsquo;s child in a hut roofed with cormorant feathers. She asked her husband not to look; he did, and saw her in her true form, which the MLIT text gives as a giant shark. She returned to the sea and left the newborn, named Ugayafukiaezu after the unfinished roof (MLIT, Japan Today). More Than Tokyo glosses the name Udo as &ldquo;cormorant dwelling&rdquo;."),
("What is the undama toss?","You buy small clay balls (<em>undama</em>) at the shrine and throw them at a rope-ringed hollow on the back of Kameishi, the turtle-shaped rock below the cliff. Men throw with the left hand and women with the right; a ball that lands in the hollow is said to grant a wish (japan-guide, MLIT). The price is given as 200 yen for five (Jeepe) and as 100 yen for five in older sources (Japan Today, Lonely Planet), so check at the shrine. Nippon.com adds that local schoolchildren make the balls and the money goes to school costs."),
("How do I get to Udo Shrine without a car?","japan-guide says a bus from Miyazaki Station takes about 90 minutes and costs about 1,570 yen one way, with a 10-minute walk from the Udo Jingu stop; Japan Today gives about 70 minutes. From the JR Nichinan Line, buses run from Aburatsu or Ibii Station in about 20 minutes (Japan Rail and Travel, JORUDAN). Buses are infrequent, so check the timetable before you go (GLTJP)."),
("How long should I allow?","Jeepe suggests 30 to 40 minutes for the main hall alone, about an hour with photos and the undama toss, and 1.5 to 2 hours with nearby sights. Tokyo Weekender suggests at least 30 to 60 minutes."),
("What are the hours and fees?","Entry is free (japan-guide, GLTJP). Hours differ by source: 6:00 to 18:00 (japan-guide, GLTJP, Miyazaki tourism), 6:00 to 19:00 (Japan Travel) and seasonal hours of 6:00 to 19:00 from April to September and 7:00 to 18:00 from October to March (Japan Rail and Travel). No closing days are listed (japan-guide, GLTJP); confirm the hours before you go."),
("Is it suitable for visitors with limited mobility?","Not easy. You reach the cave by descending steps cut into the cliff, and the stones can be slippery in the rain (Jeepe). Japan Today reports no special access for mobility-impaired visitors, and describes the stairs as about three storeys down."),
]
def body(fig,a): return """<main>

"""+fig('main-hall','Red and turquoise-green shrine hall built right under a huge overhanging cliff, with painted decorations and carved details, a curtain, a drum and a blue banner at the front','The main hall inside the sea cave at Udo Shrine, May 2023',hero=True)+"""
  <aside class="toc" aria-label="Table of contents">
    <div class="toc-label">TABLE OF CONTENTS ／ 目次</div>
    <div class="toc-title">In This Guide</div>
    <ol>
      <li><a href="#opening">A Shrine You Walk Down To</a></li>
      <li><a href="#legend">The Birth in the Cave</a></li>
      <li><a href="#walk">The Walk Down to the Cave</a></li>
      <li><a href="#cave">Inside the Cave: Breast Rocks and Turtle Rock</a></li>
      <li><a href="#undama">Throwing an Undama</a></li>
      <li><a href="#visit">Visiting Udo Shrine</a></li>
      <li><a href="#faq">Frequently Asked Questions</a></li>
      <li><a href="#final">Before You Go</a></li>
    </ol>
  </aside>

  <article>

    <p class="opening" id="opening">As a licensed guide, I like shrines that make you work for the view, and Udo Shrine does it the other way round: you walk <em>down</em> to it, through red railings and a gate, to a hall tucked under a cliff at the edge of the sea.</p>
    <p>Udo Shrine sits on the Nichinan Coast of Miyazaki, about 40 km south of Miyazaki City (japan-guide). Its main hall stands inside a sea cave, and the story told about that cave is one of the oldest in Japanese mythology: the birth of the father of the first emperor. The photographs here come from Wikimedia Commons, so you can see what each stage of the walk looks like. This guide covers the legend, the walk, the things people do in and below the cave, and how to get there.</p>

"""+fig('panorama','Very wide panorama of a rocky sea coast: red-railed steps and a small shrine under a cliff overhang on the left, dark spiky rock stacks in the middle and the open ocean beyond','The shrine and its sea cliff from the rocks, May 2009')+"""
    <h2 id="legend">The Birth in the Cave<span class="h2-jp">鵜戸の伝説</span></h2>
    <p>According to the MLIT multilingual guide, the shrine is dedicated to Ugayafukiaezu, who plays a key role in the myths as the father of Emperor Jimmu. The story goes like this. Hoori, a skilled hunter also called Yamasachihiko, married Toyotama, the daughter of the sea god. When her time came, she went ashore to give birth and began roofing a birth hut with cormorant feathers; labour started before it was finished. She asked her husband not to look. He looked, and saw her in her true form, which MLIT gives as a giant shark. She went back to the sea and left the baby behind. He was named for the unfinished roof, a name that roughly means &ldquo;the one whose cormorant-feather thatch was never completed&rdquo; (MLIT, Japan Today).</p>
    <p>The local belief is that the birth took place in the cave where the shrine now stands (MLIT). Our """+a('/culture/japanese-mythology/','Japanese mythology guide','mythology')+""" tells the story of Hoori and Toyotama in more detail,, and our """+a('/guides/takachiho/','Takachiho guide','takachiho')+""" covers another Miyazaki site from the same early myths.</p>
    <p>On the historical side, MLIT reports that a priest named Kaikyu founded a Buddhist temple here in 782 to look after the shrine, that the Ito family, lords of the Obi domain, supported it in the Edo period, and that they built the present main hall in 1711. The same source says the hall still has Buddhist elements, such as a window shaped like a temple bell, since mixing Shinto and Buddhist practice was normal until the end of the Edo period. Today the site is purely Shinto. Jeepe also gives 1711 for the rebuilding. Tabi-mag reports that the shrine&rsquo;s own tradition places its founding in the reign of Emperor Sujin, which is legend and not a documented date.</p>

    <h2 id="walk">The Walk Down to the Cave<span class="h2-jp">下り宮</span></h2>
    <p>Udo Shrine is called a <em>kudari-miya</em>, a &ldquo;descending shrine&rdquo;, because you walk down to the main hall instead of climbing up to it (Jeepe). From the car park the approach runs along the coast between sago palms, past the gate and the two-storey tower gate, then across a red bridge toward the cliff (Jeepe).</p>
"""+fig('tamabashi','Red-railed stone-paved path leading to a green-roofed shrine hall under a cliff overhang, with a few visitors, waves breaking on dark rocks to the right and a sago palm in the lower corner','The shrine seen from the direction of the Tamabashi bridge (Commons title), April 2008')+"""
    <p>The tower gate is the first landmark. In the 2008 photograph a framed picture of a white rat hangs under the upper floor; in the 2009 picture below it shows an ox, so it looks like a yearly zodiac picture, which I have not confirmed.</p>
"""+fig('romon-2008','Large red two-storey tower gate with a grey roof, a framed picture of a white rat on a gold ground hung under the upper floor, stone lanterns on both sides and visitors walking up the steps','The tower gate (romon) in August 2008')+fig('romon-2009','Red two-storey tower gate with a grey-green roof, a framed picture of a black ox under the upper floor, visitors on the stone path in front and blue sky behind','The same gate in May 2009')+fig('romon-sign','Wide view of a red tower gate with a dark curved roof, a thick rope across the opening, stone lanterns on both sides, a few visitors walking through and a tall white signboard with large black characters at the right','The gate area in a May 2009 panorama. The board at the right reads 鵜戸神宮; I read the smaller text as naming the deity as Ugayafukiaezu and giving a festival day of 1 February, which you should confirm with the shrine')+"""
    <p>Past the gate, the path turns to steps cut into the cliff. The staircase below is the one that takes you down to the hall. Jeepe says to expect many steps and uneven ground, and warns that the stone can be slippery in the rain. Japan Today describes the drop as about three storeys. GLTJP&rsquo;s Japanese page says the descent involves about 800 metres of stone steps, which does not match the other accounts, so treat the length as approximate.</p>
"""+fig('stairs','Looking down a long stone staircase with bright orange railings and stone lanterns toward a small green-roofed hall tucked under a rock overhang beside the sea','The staircase down to the cave shrine, May 2020')+fig('overlook','Aerial-style view down onto a paved yard with orange railings, trunks of sago palms in the foreground and a pair of rocks and the sea beyond','Looking down on the yard beside the hall, May 2020')+fig('gate-ceremony','Red wooden gate with a curved copper-looking roof framing a view of white-walled courtyard, orange railings and the grey ocean behind, with stone walls and bushes on both sides','The gate in front of the ceremony hall (Commons title: Gate in front of the Gishikiden Hall), March 2017')+"""
    <h2 id="cave">Inside the Cave: Breast Rocks and Turtle Rock<span class="h2-jp">洞窟・お乳岩・亀石</span></h2>
    <p>The cave measures about 38 m east to west, 29 m north to south and 8.5 m high (Tabi-mag, Jeepe), and the red hall fills a small part of it. In the photograph at the top the rock roof sits close above the tiles.</p>
    <p><strong>Ochichi Iwa, the breast rocks.</strong> The legend says Toyotama left her breasts on the wall so that her son could be fed. At the back of the cave there are two rocks of that shape, from which water drips (Japan Today, Nippon.com). MLIT says visitors touch them to pray for safe childbirth, healthy children and the health of mothers, and the shrine sells a milk candy, <em>ochichi ame</em>, associated with this water (Tabi-mag, Japan Travel). japan-guide adds that drinking the dripping water is thought to be good for pregnancy, birth and nursing, and that the shrine is also considered fortunate for couples and newlyweds.</p>
    <p><strong>Kameishi, the turtle rock.</strong> Below the terrace, a rock shaped like a turtle with a rope around a hollow on its back is said to be the turtle that carried Toyotama from the sea (Nippon.com). Another MLIT page gives a second version in which the turtle carried the baby&rsquo;s aunt, who came to raise him after he was left behind. The two retellings differ, and I would take the turtle itself as the fixed part of the story.</p>

    <h2 id="undama">Throwing an Undama<span class="h2-jp">運玉投げ</span></h2>
    <p>The best-known thing to do is the undama toss. You buy five small clay balls at the shrine, make a wish and throw them down from the terrace at the rope-ringed hollow on Kameishi. Men throw with the left hand and women with the right (japan-guide, MLIT). A ball that stays in the ring is said to grant the wish.</p>
    <p>Sources disagree on the details. The price is 200 yen for five (Jeepe) or 100 yen for five (Japan Today, Lonely Planet, probably older). Jeepe puts the distance at roughly 10 m; Nippon.com gives a target about 60 cm wide and about 12 m from the cliff. MLIT says people used to throw coins until the 1950s, but children climbed down to collect them, so the shrine switched to clay. Nippon.com adds that local schoolchildren make the balls and the money goes toward school costs. I have not tried it myself and would keep expectations low: it is harder than it looks.</p>
    <p>You will also see rabbit images around the shrine. Japan Today suggests this is because the Japanese word for rabbit shares its first sound with <em>u</em>, cormorant, and because rabbits symbolise fertility. I have not found a shrine source for that reading, so take it as one author&rsquo;s guess.</p>

    <h2 id="visit">Visiting Udo Shrine<span class="h2-jp">参拝案内</span></h2>
    <ul class="practical-list">
      <li><strong>Address:</strong> 3232 Miyaura, Nichinan, Miyazaki 887-0101.</li>
      <li><strong>Fee:</strong> free (japan-guide, GLTJP).</li>
      <li><strong>Hours:</strong> 6:00 to 18:00 (japan-guide, GLTJP, Miyazaki tourism), 6:00 to 19:00 (Japan Travel) or seasonal (6:00 to 19:00 from April to September, 7:00 to 18:00 from October to March, per Japan Rail and Travel). Check before you go.</li>
      <li><strong>By car:</strong> the easiest way (japan-guide). About 50 minutes from central Miyazaki via Route 220 (Jeepe). Free parking, about 400 spaces (Jeepe); JORUDAN says 450.</li>
      <li><strong>By bus from Miyazaki:</strong> about 90 minutes and about 1,570 yen one way, then about 10 minutes on foot from the Udo Jingu stop (japan-guide). Japan Today gives about 70 minutes. The bus also stops at Aoshima.</li>
      <li><strong>By train and bus:</strong> JR Nichinan Line to Aburatsu or Ibii, then a bus of about 20 minutes (Japan Rail and Travel, JORUDAN). Buses are infrequent (GLTJP).</li>
      <li><strong>Time to allow:</strong> 30 to 40 minutes for the hall alone, about an hour with the undama, 1.5 to 2 hours with nearby sights (Jeepe).</li>
      <li><strong>Nearby:</strong> Namikiri Shrine, a small shrine in a sea cave, about 20 minutes&rsquo; walk beyond the Udo gate (Miyazaki tourism); Aoshima; Cape Toi (Jeepe).</li>
      <li><strong>Notes:</strong> wear shoes with grip. Early morning or late afternoon is quieter (Jeepe).</li>
    </ul>
    <div class="key-callout">
      <p>&#127890; <strong>Plan your trip:</strong> Browse guided tours around Miyazaki and the Nichinan Coast. <a href="https://www.viator.com/search/Miyazaki?pid=P00298374&amp;mcid=42383&amp;medium=link&amp;campaign=sacred-japan" target="_blank" rel="noopener" onclick="trackEvent('click','affiliate','viator_udo_jingu')">Book a Tour</a></p>
    </div>

    <h2 id="faq">Frequently Asked Questions<span class="h2-jp">よくあるご質問</span></h2>
    <div class="faq-stack">
@@FAQ@@    </div>

    <h2 id="final">Before You Go<span class="h2-jp">むすびに</span></h2>
    <p>Udo Shrine pairs well with Kirishima and Takachiho on a trip through the mythological south of Kyushu; our """+a('/guides/kirishima-jingu/','Kirishima Jingu guide','kirishima')+""" covers the shrine of Ninigi, Hoori&rsquo;s father. Go early, wear grip shoes, and give yourself time for the walk down.</p>

    <div class="closing-block">
      <span class="torii">&#9961;&#65039;</span>
      <p>A shrine you walk down to, built where, the story says, the first emperor&rsquo;s father was born.</p>
    </div>

    <section class="related-section">
      <h2>Related Guides</h2>
      <span class="h2-jp">関連ガイド</span>
      <div class="related-grid">
        <a class="related-card" href="/culture/japanese-mythology/" onclick="trackEvent('click','internal','related_udo_to_mythology')">
          <div class="related-card-label">SACRED JAPAN ／ CULTURE</div>
          <div class="related-card-title">&#128214; Japanese Mythology &rarr;</div>
          <div class="related-card-desc">Kojiki gods, famous myths and the shrines where they happen.</div>
        </a>
        <a class="related-card" href="/guides/takachiho/" onclick="trackEvent('click','internal','related_udo_to_takachiho')">
          <div class="related-card-label">SACRED JAPAN ／ GUIDES</div>
          <div class="related-card-title">&#127748; Takachiho &rarr;</div>
          <div class="related-card-desc">The cave where Amaterasu hid, in Miyazaki&rsquo;s mountains.</div>
        </a>
        <a class="related-card" href="/guides/kirishima-jingu/" onclick="trackEvent('click','internal','related_udo_to_kirishima')">
          <div class="related-card-label">SACRED JAPAN ／ GUIDES</div>
          <div class="related-card-title">&#9961;&#65039; Kirishima Jingu &rarr;</div>
          <div class="related-card-desc">The shrine of Ninigi, on the road to Takachiho.</div>
        </a>
      </div>
    </section>

  </article>

"""
build(dict(slug='udo-jingu',ev='udo_jingu',jp='鵜戸神宮',en='Udo Shrine',dest='Miyazaki',thumb='main-hall',photos=P,faqs=faqs,body=body,
 title="Udo Shrine Guide: The Cave Shrine in Miyazaki, Turtle Rock and the Lucky Undama Toss",
 desc="A licensed guide's guide to Udo Shrine (Udo Jingu) in Nichinan, Miyazaki: the main hall inside a sea cave, the myth of Toyotama and the father of Emperor Jimmu, Turtle Rock and the undama toss, hours, fees and how to get there.",
 tag="A Miyazaki shrine whose red main hall sits inside a sea cave, with the myth of the first emperor's father and a lucky stone toss.",
 kw="Udo Shrine, Udo Jingu, Miyazaki cave shrine, Nichinan Coast, undama, Turtle Rock, Kameishi, Ugayafukiaezu, Toyotama, Kojiki shrine, Kyushu shrine",
 h1="<h1><em>Udo Shrine</em>: The Cave Shrine in Miyazaki, Turtle Rock and the Lucky Undama Toss</h1>",
 og=("Udo Shrine Guide:","A Cave Shrine by the Sea"),
 sources=[('https://www.japan-guide.com/e/e8032.html','japanguide','japan-guide'),('https://www.gltjp.com/en/directory/item/11580/','gltjp','GLTJP'),('https://www.mlit.go.jp/tagengo-db/common/001565652.pdf','mlit','MLIT multilingual guide'),('https://www.mlit.go.jp/tagengo-db/en/R2-02103.html','mlit_undama','MLIT (Undama)'),('https://www.jeepe.jp/en/articles/udojingu-miyazaki-1465','jeepe','Jeepe'),('https://nippon.com/en/guide-to-japan/gu022005','nippon','Nippon.com'),('https://japantoday.com/category/features/travel/udo-shrine-%E2%80%93-origin-myths-in-a-cliff-side-cave-2','japantoday','Japan Today'),('https://www.kanko-miyazaki.jp/en/sightseeing/1003','kanko','Miyazaki tourism'),('https://www.tokyoweekender.com/location/udo-shrine/','tw','Tokyo Weekender'),('https://tabi-mag.jp/mz0087/','tabimag','Tabi-mag'),('https://www.morethantokyo.com/udo-shrine-miyazaki/','mtt','More Than Tokyo'),('https://www.lonelyplanet.com/points-of-interest/udo-jingu/1234904','lp','Lonely Planet'),('https://japanrailandtravel.com/?p=6125','jr','Japan Rail and Travel'),('https://sp.jorudan.co.jp/newyear/spot_47732.html','jorudan','JORUDAN')]))
