import sys; sys.path.insert(0,'/home/claude/sacred-japan/_tools/shrine')
from shrine_common import *
P={
'nakatsunomiya':('19905d13','Daderot','cc0','https://commons.wikimedia.org/wiki/User:Daderot'),
'hetsunomiya':('f73e4961','Daderot','cc0','https://commons.wikimedia.org/wiki/User:Daderot'),
'torii-stairs':('2caec33a','Guilhem Vellut','by2','https://commons.wikimedia.org/wiki/User:Guilhem_Vellut'),
'zuishinmon':('d4812197','AMANO Jun-ichi','by3','https://web.archive.org/web/20161024093952/http://www.panoramio.com/photo/71994673'),
'musubi-ema':('4746d5e7','Wei-Te Wong','bysa2','https://www.flickr.com/people/65947222@N00/'),
}
faqs=[
("What is Enoshima Shrine?","It is a general name for three shrines, Hetsunomiya, Nakatsunomiya and Okutsunomiya, on Enoshima island in Fujisawa (Kanagawa tourism). Each enshrines three sister goddesses along with eight-armed Benzaiten and Myoon Benzaiten, one of Japan&rsquo;s three major Benzaiten (Kanagawa tourism). Shrine tradition dates the first shrine to 552, in the Iwaya caves, on the order of Emperor Kinmei (Discover Fujisawa)."),
("What is the legend of the five-headed dragon?","According to the Enoshima Engi, villagers were plagued for a thousand years by the five-headed dragon Gozuryu, until in 552 the goddess Benzaiten raised Enoshima from the sea as her home (Wikipedia, Tokyo Weekender). LIVE JAPAN says the dragon fell in love with her, she persuaded him to repent, and he became the area&rsquo;s protector by turning into a hill."),
("Do I need to take the escalator?","No. It is an option on the climb: the Enoshima Escar, opened in 1959 as Japan&rsquo;s first outdoor escalator, runs from 8:50 to 19:05 (GLTJP, LIVE JAPAN). LIVE JAPAN gives 360 yen for the full ride and about 4 minutes, against about 20 minutes on foot, while Discover Fujisawa lists 500 yen, so check the current fare. It only goes up."),
("How long does it take to walk from the station?","About 14 to 15 minutes from Katase-Enoshima Station to the shrine (GLTJP, LIVE JAPAN), including crossing the bridge, which takes about 5 minutes (LIVE JAPAN). Tokyo to Katase-Enoshima takes about an hour on the Odakyu Line (LIVE JAPAN)."),
("What are the hours and fees?","The shrine grounds are free. Opening hours differ by source: 8:30 to 17:00 (Kanagawa tourism), 9:00 to 17:00 (GLTJP) and 8:30 to 16:30 (Tokyo Tourism), so check on the day. To see the Benzaiten statues in the Hoanden you pay a small fee: 200 yen for adults, 100 for junior high and high school students and 50 for children (Kanagawa tourism)."),
("What is the &ldquo;Hadaka Benten&rdquo;?","Myoon Benzaiten, popularly known as Hadaka (Naked) Benzaiten, is one of the two Benzaiten statues kept at Hetsunomiya (Discover Fujisawa). The same source says Happi Benzaiten was donated by Minamoto no Yoritomo in 1182, and that the Hadaka statue was donated later, in the Edo period, though it is believed to have been made in the Kamakura period."),
]
def body(fig,a): return """<main>

"""+fig('nakatsunomiya','The vermilion front of Nakatsunomiya with a curved gable, gold fittings, white paper streamers on the rope, a donation box in front and green trees behind','Nakatsunomiya, the middle shrine',hero=True)+"""
  <aside class="toc" aria-label="Table of contents">
    <div class="toc-label">TABLE OF CONTENTS ／ 目次</div>
    <div class="toc-title">In This Guide</div>
    <ol>
      <li><a href="#opening">A Shrine on an Island</a></li>
      <li><a href="#legend">The Dragon and the Goddess</a></li>
      <li><a href="#three">The Three Shrines</a></li>
      <li><a href="#luck">Wishes and Luck</a></li>
      <li><a href="#visit">Visiting Enoshima Shrine</a></li>
      <li><a href="#faq">Frequently Asked Questions</a></li>
      <li><a href="#final">Before You Go</a></li>
    </ol>
  </aside>

  <article>

    <p class="opening" id="opening">As a licensed guide, I like shrines you have to cross water to reach, and Enoshima Shrine is one: a bridge, a shopping street and a climb up a hill in the sea.</p>
    <p>Enoshima Shrine is really three shrines spread along the island, all connected with the goddess Benzaiten. It is about an hour from Tokyo. This guide covers the founding legend, what each of the three shrines is, the things people come for (a Hadaka Benzaiten statue, a pair of trees, a money-washing pond) and the practical side.</p>

    <h2 id="legend">The Dragon and the Goddess<span class="h2-jp">五頭龍と弁財天</span></h2>
    <p>The island has a legend. Per the Enoshima Engi, a five-headed dragon called Gozuryu terrorised the nearby villagers for about a thousand years, until in 552 the goddess Benzaiten raised Enoshima from the bay as her home (Wikipedia). Tokyo Weekender says the Engi was written in 1047 by a monk named Kokei. LIVE JAPAN adds that the dragon fell in love with her, she persuaded him to repent, and he turned into a hill that protects the area.</p>
    <p>Discover Fujisawa says the shrine was first built at Iwaya in 552 on the order of Emperor Kinmei, and that the shrine crest, three scales surrounded by waves, comes from the Legend of the Three Scales. Treat 552 as the shrine&rsquo;s tradition rather than documented history. Our """+a('/guides/itsukushima-shrine/','Itsukushima Shrine guide','itsukushima')+""" covers another of the three major Benzaiten shrines.</p>

    <h2 id="three">The Three Shrines<span class="h2-jp">辺津宮・中津宮・奥津宮</span></h2>
"""+fig('torii-stairs','A vermilion torii at the top of a wide stone staircase, with red lanterns, a biwa-shaped sign, a small white tunnel gate behind it and visitors on the steps','The torii and stairs at Enoshima Shrine')+fig('zuishinmon','A white-walled gate with a tiled hip-and-gable roof among bright green maple trees, a stone marker in front and a red lantern at the side','The Zuishinmon, as titled by the photographer')+"""
    <p>The Zuishinmon is the white gate at the foot of the climb. Tokyo Weekender says that beyond it is a stone carving of Benzaiten and Gozuryu made for the shrine&rsquo;s 1,450th anniversary. I have not checked that the gate in this photo and the carving are in the same spot.</p>
"""+fig('hetsunomiya','The front of Hetsunomiya with a curved gable, a plaque reading Hetsunomiya, gold fittings, white paper lanterns and a biwa-shaped sign, visitors at the offering box','Hetsunomiya, the first of the three shrines')+"""
    <p>Hetsunomiya, nearest the entrance, is the shrine most visitors reach first. Kanpai Japan says it was built in 1206 and renovated in 1976; Tokyo Weekender calls it the most picturesque of the three, with a grass purification wheel and a dragon pond. The two Benzaiten statues are kept in the Hoanden here, for a small fee (Kanagawa tourism, Discover Fujisawa).</p>
    <p>Nakatsunomiya, halfway up, is the vermilion one in the first photo; Kanpai Japan says it dates to 853 and was last renovated in 1996. Okutsunomiya is more rustic and has an unknown founding date, near the Iwaya caves, and enshrines Takirihime, a deity who protects the sea (GLTJP). LIVE JAPAN also mentions Wadatsunomiya, built in 1994.</p>

    <h2 id="luck">Wishes and Luck<span class="h2-jp">縁結び・金運</span></h2>
"""+fig('musubi-ema','A pink wall of wishing plaques stacked on a stand, with two large rope-wrapped trunks on top, a signpost at the left and the sea haze behind','The wishing plaques at the Musubi no Ki (as labelled by the source)')+"""
    <p>LIVE JAPAN describes the Musubi no Ki as a tree whose two trunks share one stem, said to bring good fortune, with wishing plaques at 500 yen. The wall of pink plaques in the photo is labelled with that name by its photographer; I read the rope-wrapped trunks on top as part of the same spot, but the source does not say so.</p>
    <p>Near the main hall is the Zeniarai pond, where visitors wash money with water from a spring to increase it (LIVE JAPAN, GLTJP names the spot Zeniarai Hakuryuoh). I have not tried it. Plaques and charms cost around the figures LIVE JAPAN gives, so check at the office.</p>

    <h2 id="visit">Visiting Enoshima Shrine<span class="h2-jp">参拝案内</span></h2>
    <ul class="practical-list">
      <li><strong>Address:</strong> 2-3-8 Enoshima, Fujisawa, Kanagawa 251-0036 (Japan Documented).</li>
      <li><strong>On foot:</strong> about 14 to 15 minutes from Katase-Enoshima Station, over the bridge and up the Nakamise street (GLTJP, LIVE JAPAN). Kanagawa tourism also lists Shonan-Enoshima Station on the Enoden and the Shonan Monorail.</li>
      <li><strong>The climb:</strong> about 20 minutes on foot or about 4 minutes by escalator (LIVE JAPAN); GLTJP gives about 5 minutes. The Escar runs 8:50 to 19:05; fares in the sources differ (360 or 500 yen).</li>
      <li><strong>Hours:</strong> 8:30 to 17:00 (Kanagawa tourism), 9:00 to 17:00 (GLTJP) or 8:30 to 16:30 (Tokyo Tourism); check on the day.</li>
      <li><strong>Hoanden fee:</strong> 200 yen adults, 100 yen junior high and high school, 50 yen children (Kanagawa tourism).</li>
      <li><strong>Iwaya caves:</strong> about a 30-minute walk from the station; a 152 m lit route open about 9:00 to 16:00 (GLTJP). The eno=pass includes the Escar, the caves and two other attractions (GLTJP).</li>
      <li><strong>Time to allow:</strong> about 30 minutes for the three shrines alone (Kanagawa tourism); more with the caves.</li>
    </ul>
    <div class="key-callout">
      <p>&#127890; <strong>Plan your trip:</strong> Browse guided tours around Kamakura and Enoshima. <a href="https://www.viator.com/search/Enoshima?pid=P00298374&amp;mcid=42383&amp;medium=link&amp;campaign=sacred-japan" target="_blank" rel="noopener" onclick="trackEvent('click','affiliate','viator_enoshima')">Book a Tour</a></p>
    </div>

    <h2 id="faq">Frequently Asked Questions<span class="h2-jp">よくあるご質問</span></h2>
    <div class="faq-stack">
@@FAQ@@    </div>

    <h2 id="final">Before You Go<span class="h2-jp">むすびに</span></h2>
    <p>Go early on a weekend, since the Nakamise street gets busy. Kamakura is close, and our """+a('/guides/tsurugaoka-hachimangu/','Tsurugaoka Hachimangu guide','tsurugaoka')+""" covers its main shrine.</p>

    <div class="closing-block">
      <span class="torii">&#9961;&#65039;</span>
      <p>Three shrines for one goddess, up a hill that the legend says was once a dragon.</p>
    </div>

    <section class="related-section">
      <h2>Related Guides</h2>
      <span class="h2-jp">関連ガイド</span>
      <div class="related-grid">
        <a class="related-card" href="/guides/tsurugaoka-hachimangu/" onclick="trackEvent('click','internal','related_enoshima_to_tsurugaoka')">
          <div class="related-card-label">SACRED JAPAN ／ GUIDES</div>
          <div class="related-card-title">&#9961;&#65039; Tsurugaoka Hachimangu &rarr;</div>
          <div class="related-card-desc">Kamakura&rsquo;s main shrine, a short train ride away.</div>
        </a>
        <a class="related-card" href="/guides/itsukushima-shrine/" onclick="trackEvent('click','internal','related_enoshima_to_itsukushima')">
          <div class="related-card-label">SACRED JAPAN ／ GUIDES</div>
          <div class="related-card-title">&#9961;&#65039; Itsukushima Shrine &rarr;</div>
          <div class="related-card-desc">Another shrine linked to Benzaiten, on its own island.</div>
        </a>
        <a class="related-card" href="/culture/japanese-mythology/" onclick="trackEvent('click','internal','related_enoshima_to_mythology')">
          <div class="related-card-label">SACRED JAPAN ／ CULTURE</div>
          <div class="related-card-title">&#128214; Japanese Mythology &rarr;</div>
          <div class="related-card-desc">Gods, dragons and the stories behind the shrines.</div>
        </a>
      </div>
    </section>

  </article>

"""
build(dict(slug='enoshima-jinja',ev='enoshima',jp='江島神社',en='Enoshima Shrine',dest='Kamakura',thumb='nakatsunomiya',photos=P,faqs=faqs,body=body,
 title="Enoshima Shrine Guide: Three Shrines, the Five-Headed Dragon and Hadaka Benzaiten",
 desc="A licensed guide's guide to Enoshima Shrine in Kanagawa: the three shrines (Hetsunomiya, Nakatsunomiya, Okutsunomiya), the legend of Benzaiten and the five-headed dragon, the escalator, fees and how to get there from Tokyo.",
 tag="Three shrines on an island hill, tied to a goddess and a dragon, a bridge and an escalator away from the mainland.",
 kw="Enoshima Shrine, Enoshima Jinja, Benzaiten, Hadaka Benzaiten, Hetsunomiya, Nakatsunomiya, Okutsunomiya, Enoshima escalator, Kamakura day trip, Kanagawa shrine",
 h1="<h1><em>Enoshima Shrine</em>: Three Shrines, the Five-Headed Dragon and Hadaka Benzaiten</h1>",
 og=("Enoshima Shrine Guide:","Three Shrines and a Dragon"),
 sources=[('https://www.gltjp.com/en/article/item/20176/','gltjp','GLTJP'),('https://trip.pref.kanagawa.jp/ja/destination/enoshima-shrine/591','kanagawa','Kanagawa tourism'),('https://livejapan.com/ms/in-tokyo/in-pref-kanagawa/in-kamakura/article-a0002023/','livejapan','LIVE JAPAN'),('https://discover-fujisawa.jp/en/?p=365','fujisawa','Discover Fujisawa'),('https://en.wikipedia.org/wiki/Enoshima_Engi','wiki','Wikipedia'),('https://www.tokyoweekender.com/?p=145352','tw','Tokyo Weekender'),('https://www.kanpai-japan.com/enoshima/jinja','kanpai','Kanpai Japan'),('https://www.tokyotourism.org/?p=1536','tt','Tokyo Tourism'),('https://japan-documented.com/places/enoshima-shrine/','jd','Japan Documented')]))
