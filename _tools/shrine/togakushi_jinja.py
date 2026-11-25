import sys; sys.path.insert(0,'/home/claude/sacred-japan/_tools/shrine')
from shrine_common import *
CAR='https://web.archive.org/web/2016/http://www.panoramio.com/photo/%s'
P={
'cedar-avenue':('ac9c85a9','Koda6029','bysa4','https://commons.wikimedia.org/wiki/User:Koda6029'),
'okusha-torii':('e69b6433','TTTNIS','cc0','https://commons.wikimedia.org/wiki/User:TTTNIS'),
'chusha-torii':('404581e4','くろふね','by3',CAR%'98170254'),
'chusha-haiden':('e3edc82d','くろふね','by3',CAR%'98170264'),
'chusha-snow':('bb9c4e58','AT@wiki','bysa2','https://www.flickr.com/photos/alextojun/51752616478/'),
'hokosha-torii':('b1e4d7a1','AT@wiki','bysa2','https://www.flickr.com/photos/alextojun/51751549552/'),
'hokosha-haiden':('fa3aab8a','AT@wiki','bysa2','https://www.flickr.com/photos/alextojun/54513742486/'),
'hall-cedars':('2dcc3283','Opqr','bysa4','https://commons.wikimedia.org/wiki/User:Opqr'),
'soba':('f0184bdb','Komoro no kaze','bysa4','https://commons.wikimedia.org/wiki/User:Komoro_no_kaze'),
}
faqs=[
("What are the five shrines of Togakushi?","Hokosha, Hinomikosha, Chusha, Kuzuryusha and Okusha (GLTJP, go-nagano). Of the five, only Hinomikosha has been a Shinto shrine throughout its history; the others were temples of the Shugendo mountain-ascetic tradition for much of their past (MLIT)."),
("How long is the walk to Okusha?","The approach is about 2 km from the large torii to Okusha, with the Zuishinmon gate about halfway (MLIT, go-nagano). GLTJP puts the walk at about 40 minutes each way from the Okusha Iriguchi bus stop, and about 500 m of that is the cedar avenue itself."),
("Is Okusha open in winter?","No. Okusha and Kuzuryusha are closed from January 7 to late April (GLTJP, Togakushi Tourism Association). In winter you can still walk as far as the Zuishinmon gate, and entry beyond it is prohibited until mid-April for avalanche risk (Togakushi Tourism Association). Goshuin for all five shrines are available at Chusha in winter (GLTJP)."),
("How do I get to Togakushi from Nagano Station?","Take an Alpico bus from bus stop No. 7 at the Zenkoji exit (go-nagano). GLTJP gives about 1 hour 10 minutes to Hokosha, 1 hour 20 minutes to Chusha and about 1 hour to Okusha Iriguchi; other pages say about 60 to 65 minutes, so allow for traffic. I could not confirm current fares, so check the Alpico timetable. In winter the local bus does not stop at Okusha (go-nagano)."),
("Is there an entrance fee or opening time?","Entry is free, and GLTJP says you can visit anytime, though hours vary by hall. Goshuin are issued 9:00 to 17:00 outside winter, per GLTJP; confirm at the shrine."),
("Which shrine should I visit if I only have time for one?","Chusha, in the centre of the village, is open all year and has the soba restaurants and tourist office. If you came for the trees, take the bus to Okusha Iriguchi and walk the avenue (spring to autumn)."),
]
def body(fig,a): return """<main>

"""+fig('cedar-avenue','A path running between very tall cedar trees with thick reddish trunks, with mossy roots and a few fallen leaves beside the trail','The cedar-lined approach to Okusha',hero=True)+"""
  <aside class="toc" aria-label="Table of contents">
    <div class="toc-label">TABLE OF CONTENTS ／ 目次</div>
    <div class="toc-title">In This Guide</div>
    <ol>
      <li><a href="#opening">Five Shrines on One Mountain</a></li>
      <li><a href="#history">Why It Is Called Togakushi</a></li>
      <li><a href="#okusha">Okusha and the Cedar Avenue</a></li>
      <li><a href="#chusha">Chusha, the Centre</a></li>
      <li><a href="#hokosha">Hokosha and Hinomikosha</a></li>
      <li><a href="#visit">Visiting Togakushi</a></li>
      <li><a href="#faq">Frequently Asked Questions</a></li>
      <li><a href="#final">Before You Go</a></li>
    </ol>
  </aside>

  <article>

    <p class="opening" id="opening">As a licensed guide, I tell visitors to Togakushi that this is not one shrine but five, spread along a road at the foot of a mountain, and that the walk between them is the point.</p>
    <p>Togakushi, in Nagano City, is best known for the two-kilometre approach to Okusha, where old cedars stand on both sides of the path. But the other four shrines, a thatched red gate and a village of soba restaurants are part of the same visit. This guide covers what each shrine is, what to look for, and the practical side: buses, winter closures and the order I would walk them in.</p>

    <h2 id="history">Why It Is Called Togakushi<span class="h2-jp">戸隠の由来</span></h2>
    <p>The name means &ldquo;hidden door&rdquo;. Tradition ties it to the myth in which the sun goddess Amaterasu hides in a rock cave and the strong god Ame-no-Tajikarao throws the door away; our """+a('/culture/japanese-mythology/','Japanese mythology guide','mythology')+""" tells that story. MLIT says Okusha&rsquo;s origins are dated to 210 BCE, when Tajikarao was enshrined there.</p>
    <p>MLIT adds that in 849 a monk named Gakumon established Shugendo practice and built a temple called Togakushidera, later renamed Kenkoji. Okusha, Kuzuryusha, Chusha and Hokosha were temples for much of their history, and became Shinto shrines after the separation of Shinto and Buddhism in 1868. Only Hinomikosha was always a Shinto shrine. Kuzuryusha, a small shrine for the nine-headed dragon god of rain, water, marriage and toothache, is the oldest of the five, with an unknown founding date (MLIT).</p>

    <h2 id="okusha">Okusha and the Cedar Avenue<span class="h2-jp">奥社と杉並木</span></h2>
"""+fig('okusha-torii','A large dark wooden torii at the start of a gravel path, with a stone marker, a signboard, a small roofed hut and visitors walking in under bare early-spring trees','The torii at the entrance to the Okusha approach')+"""
    <p>The Okusha approach begins at a large torii, in the photo a plain dark-wood gate with a stone marker and signboard, with bare trees behind. MLIT says the path runs about two kilometres through sacred forest to Okusha. GLTJP gives about 40 minutes each way on foot from the Okusha Iriguchi bus stop.</p>
    <p>Halfway along stands the Zuishinmon, a gate dating from 1710 that originally housed Buddhist Nio guardians and now holds Shinto warrior-guardians (MLIT). Past it, the cedar avenue starts. GLTJP calls it about 500 m long; MLIT says more than 300 cedars planted about 400 years ago line the path, and that it is laid out so the morning sun shines along it twice a year, at the beginning of winter and spring. The forest is a Natural Monument of Nagano Prefecture (MLIT). The planting date varies by source: West JR says 1612, GLTJP says the early 1700s.</p>
    <p>At the end are Kuzuryusha and Okusha, where Tajikarao is enshrined and where people pray for good fortune and success in sports (GLTJP, MLIT). Both are closed from January 7 to late April (GLTJP). On a wet day the path is slippery; the cedars are most dramatic on a dry one.</p>

    <h2 id="chusha">Chusha, the Centre<span class="h2-jp">中社</span></h2>
"""+fig('chusha-torii','A large wooden torii with stone steps beneath it, lanterns and autumn maples in orange at its sides, and a stone marker at the left','The wooden torii at the entrance to Chusha, in autumn colour')+fig('chusha-haiden','The wide hall of Chusha with a curved gable roof and shimenawa across the front, visitors gathered on the gravel in front, and green trees behind','The hall of Chusha (the image has strong HDR processing)')+"""
    <p>Chusha sits in the middle of the village and enshrines Ame-no-Yagokoro-Omoikane, a deity of wisdom; students come here (GLTJP). GLTJP also mentions three cedars more than 800 years old in the grounds and a ceiling dragon painted by Kawanabe Kyosai, digitally restored in 2003. Chusha is open all year, and its office issues goshuin for all five shrines, including in winter (GLTJP).</p>
"""+fig('chusha-snow','The front of Chusha with a curved gable, a white curtain across the entrance and patches of melting snow on the paving and the ground at either side','Chusha with snow still on the ground')+"""
    <p>In the photo above, snow still lies at the edges of the paving. The Togakushi Tourism Association says winter visitors should avoid walking after 3 pm and be aware there are no convenience stores nearby.</p>
"""+fig('soba','A tray with a bowl of soba in dark broth topped with seaweed, a plate of tempura with a shrimp and vegetables, and four small side dishes in blue-and-white bowls','Tempura soba at a restaurant near Chusha')+"""
    <p>Togakushi is known for soba, served on round bamboo trays in the style called bocchi-mori. GLTJP names Uzuraya, in front of Chusha, with zaru soba around 1,000 yen, cash only, closed Wednesdays and often selling out. I have not tried it, and the restaurant in this photo, which shows tempura soba, is not named by the source, so check any restaurant&rsquo;s hours before you go.</p>

    <h2 id="hokosha">Hokosha and Hinomikosha<span class="h2-jp">宝光社と火之御子社</span></h2>
"""+fig('hokosha-torii','A wooden torii with a shimenawa at the top of a wide flight of stone steps, with tall stone pillars and a signboard at the sides and trees behind','The torii at the foot of the Hokosha steps')+fig('hokosha-haiden','The wooden hall of Hokosha seen from the side, with a long veranda, carved eaves and a white curtain at the front, among trees','The hall of Hokosha')+"""
    <p>Hokosha is the lowest of the five and the usual starting point, up about 270 stone steps (GLTJP). It enshrines Ame-no-Uwaharu, a child deity of Omoikane, and is prayed to for learning, the arts and safe childbirth. GLTJP says the building dates to 1861 and has ornate carvings by the shrine carpenter Kitamura Kiyomatsu and others.</p>
    <p>Hinomikosha, a short walk away, enshrines Ame-no-Uzume, the dancer of the cave myth, and is known for performing arts and matchmaking. Its Married Cedars are said to be over 500 years old (GLTJP). The walk from Hokosha is about 15 minutes (GLTJP, go-nagano); another source says 10. The Hokosha-to-Okusha route linking all five is about 5.5 km and takes 2.5 to 3 hours (go-nagano).</p>
"""+fig('hall-cedars','A low wooden hall with a shimenawa across the front and a lattice of glass-paned doors, stone lanterns on either side, among tall trees','A hall among cedars, with a shimenawa and stone lanterns')+"""
    <p>The source for this photo is only titled as a hall of Togakushi Shrine, so I cannot say which of the five it is.</p>

    <h2 id="visit">Visiting Togakushi<span class="h2-jp">参拝案内</span></h2>
    <ul class="practical-list">
      <li><strong>Address:</strong> 3506 Togakushi Chusha, Nagano City (Chusha, tel. 026-254-2001; GLTJP). Entry is free.</li>
      <li><strong>By bus:</strong> Alpico bus from Nagano Station, bus stop No. 7 at the Zenkoji exit (go-nagano). Hokosha about 1 hour 10 minutes, Chusha about 1 hour 20 minutes, Okusha Iriguchi about 1 hour (GLTJP); other pages say 50 to 65 minutes. Check fares and timetables with Alpico.</li>
      <li><strong>Winter:</strong> the local bus does not stop at Okusha; get off at Chusha, where it is about 30 minutes on foot to the Okusha entrance (go-nagano). The express bus does stop at Okusha (go-nagano, since December 2025).</li>
      <li><strong>By car:</strong> West JR gives 30 km and 60 minutes from Nagano IC. GLTJP lists about 150 spaces at Okusha, 165 at Chusha and 20 at Hokosha.</li>
      <li><strong>Closed in winter:</strong> Okusha and Kuzuryusha, January 7 to late April; Hokosha is also listed as closed in winter (GLTJP).</li>
      <li><strong>Goshuin:</strong> 9:00 to 17:00 outside winter (GLTJP); the Okusha office issues the Kuzuryusha seal.</li>
      <li><strong>Time to allow:</strong> half a day for Chusha plus Okusha; a full day for the five-shrine walk.</li>
    </ul>
    <div class="key-callout">
      <p>&#127890; <strong>Plan your trip:</strong> Browse guided tours around Nagano. <a href="https://www.viator.com/search/Togakushi?pid=P00298374&amp;mcid=42383&amp;medium=link&amp;campaign=sacred-japan" target="_blank" rel="noopener" onclick="trackEvent('click','affiliate','viator_togakushi')">Book a Tour</a></p>
    </div>

    <h2 id="faq">Frequently Asked Questions<span class="h2-jp">よくあるご質問</span></h2>
    <div class="faq-stack">
@@FAQ@@    </div>

    <h2 id="final">Before You Go<span class="h2-jp">むすびに</span></h2>
    <p>Check the season first: in winter the avenue ends at the Zuishinmon. If you also want another mountain shrine tied to the cave myth, our """+a('/guides/takachiho/','Takachiho guide','takachiho')+""" covers Amano Iwato in Miyazaki.</p>

    <div class="closing-block">
      <span class="torii">&#9961;&#65039;</span>
      <p>Five shrines, one straight avenue of cedars, and a bowl of soba in between.</p>
    </div>

    <section class="related-section">
      <h2>Related Guides</h2>
      <span class="h2-jp">関連ガイド</span>
      <div class="related-grid">
        <a class="related-card" href="/culture/japanese-mythology/" onclick="trackEvent('click','internal','related_togakushi_to_mythology')">
          <div class="related-card-label">SACRED JAPAN ／ CULTURE</div>
          <div class="related-card-title">&#128214; Japanese Mythology &rarr;</div>
          <div class="related-card-desc">The cave myth behind Togakushi&rsquo;s name.</div>
        </a>
        <a class="related-card" href="/guides/takachiho/" onclick="trackEvent('click','internal','related_togakushi_to_takachiho')">
          <div class="related-card-label">SACRED JAPAN ／ GUIDES</div>
          <div class="related-card-title">&#9961;&#65039; Takachiho &rarr;</div>
          <div class="related-card-desc">Amano Iwato and the gorge in Miyazaki.</div>
        </a>
        <a class="related-card" href="/guides/suwa-taisha/" onclick="trackEvent('click','internal','related_togakushi_to_suwa')">
          <div class="related-card-label">SACRED JAPAN ／ GUIDES</div>
          <div class="related-card-title">&#9961;&#65039; Suwa Taisha &rarr;</div>
          <div class="related-card-desc">Another Nagano shrine with an old mountain tradition.</div>
        </a>
      </div>
    </section>

  </article>

"""
build(dict(slug='togakushi-jinja',ev='togakushi',jp='戸隠神社',en='Togakushi Shrine',dest='Nagano',thumb='cedar-avenue',photos=P,faqs=faqs,body=body,
 title="Togakushi Shrine Guide: Five Shrines, the Cedar Avenue to Okusha and Winter Closures",
 desc="A licensed guide's guide to Togakushi Shrine in Nagano: the five shrines (Okusha, Chusha, Hokosha, Kuzuryusha, Hinomikosha), the two-kilometre approach with its cedar avenue, winter closures, buses from Nagano Station and soba.",
 tag="Five shrines at the foot of a mountain, linked by a path through old cedars, with a thatched red gate halfway to the innermost one.",
 kw="Togakushi Shrine, Togakushi Jinja, Okusha, Chusha, Hokosha, Nagano shrine, cedar avenue, Zuishinmon, Togakushi soba, Togakushi winter",
 h1="<h1><em>Togakushi Shrine</em>: Five Shrines, the Cedar Avenue to Okusha and Winter Closures</h1>",
 og=("Togakushi Shrine Guide:","Five Shrines and Cedars"),
 sources=[('https://www.gltjp.com/en/article/item/21549/','gltjp','GLTJP'),('https://www.mlit.go.jp/tagengo-db/common/001561997.pdf','mlit','MLIT'),('https://www.go-nagano.net/en/trip-idea/id19814','gonagano','go-nagano'),('https://www.go-nagano.net/en/trip-idea/togakushi-travel-guide','gonagano2','go-nagano (travel guide)'),('https://www.westjr.co.jp/global/en/ticket/hokuriku-arch-pass/Explore_Japan/spot/nagano/togakushi-shrine/index.html','westjr','West JR'),('https://togakushi-21.jp/system/wp-content/uploads/2024/12/冬の戸隠へご来訪されるみなさま（英）.pdf','winter','Togakushi Tourism Association')]))
