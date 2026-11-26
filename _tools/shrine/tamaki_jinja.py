import sys; sys.path.insert(0,'/home/claude/sacred-japan/_tools/shrine')
from shrine_common import *
from urllib.parse import quote
U=lambda n:'/mnt/user-data/uploads/%s-image.jpg'%n
def cf(f): return 'https://commons.wikimedia.org/wiki/File:'+quote(f)
P={
'honden-torii':(U('72e328ed'),'Kansai explorer','by3',cf('Tamaki_Jinja,_Totsukawa004.jpeg')),
'stone-torii':(U('258afba0'),'Kansai explorer','by3',cf('Tamaki_Jinja,_Totsukawa002.jpeg')),
'torii-plaque':(U('6187feb3'),'Tokiwokakeru','bysa4',cf('Tamaki_Shrine.jpg')),
'honden-steps':(U('09cc8808'),'Kansai explorer','by3',cf('Tamaki_Jinja,_Totsukawa005.jpeg')),
'cedars':(U('957a6876'),'Kansai explorer','by3',cf('Tamaki_Jinja,_Totsukawa010.jpeg')),
'michishirube':(U('569272a8'),'helohelon','bysa3',cf('玉置神社への道しるべ_-_panoramio.jpg')),
'boulder':(U('d7269706'),'Drivephotographer','cc0',cf('Tamaki_shrine.jpg')),
}
faqs=[
("What is Tamaki Shrine?","Tamaki Shrine (Tamaki Jinja) stands near the summit of Mt. Tamaki (1,076 m) in Totsukawa Village, southern Nara. It is traditionally dated to 37 BCE and is regarded as the inner sanctuary of the Kumano Sanzan; it was registered as a World Heritage site in 2004 as part of the Kii Mountain Range sacred sites (MLIT, GLTJP)."),
("Why do people say only those who are called can reach it?","The phrase is a popular saying (Visit Japan Vegetarian, a tour operator&rsquo;s listing). The practical reasons given are the narrow mountain road with many hairpin bends, snow in winter, and the walk from the car park (GLTJP, nara-sightseeing). Treat it as a saying about how hard the trip is, not as a shrine teaching."),
("Can I get there by public transport?","Barely. A bus from Gojo Station to Totsukawa Onsen takes about three hours (Rurubu), and you then need a taxi of about 30 minutes. On Saturdays, Sundays and public holidays from April to November, a reservation-only World Heritage bus (Mt. Tamaki course) runs to the shrine (GLTJP). Check the village&rsquo;s current timetable and reserve ahead."),
("How long is the walk from the car park?","Accounts give 10 minutes (Sparkle Travel), 15 minutes (Rurubu, Visit Japan Vegetarian) and 20 minutes (Japan Travel, nara-sightseeing). Plan on about 15 to 20 minutes each way on an earthen path that turns to stone steps."),
("How old is the Jindai-sugi?","The MLIT guide and GLTJP call it about 3,000 years old, and GLTJP says &ldquo;said to be&rdquo;. That is a traditional estimate, not a measured age. Hikers who copied the on-site sign report a trunk of about 8.3 m and a height of about 20 m."),
("What is Tamaishi-sha?","A small subordinate shrine between the main hall and the summit with no building: a partly buried black rock surrounded by white pebbles among cedars. MLIT says it is considered the origin of the shrine; GLTJP says it is the origin of the shrine&rsquo;s name and that practitioners of Shugendo traditionally pray there before the main hall."),
("Is it open in winter?","The grounds are open year-round (GLTJP), but snow is common and the road may require chains or be closed (GLTJP, Japan47go, nara-sightseeing). Check the road status with the shrine or Totsukawa Village before you go."),
]
def body(fig,a): return """<main>

"""+fig('honden-torii','Shrine hall with a blue-green roof seen beyond a wooden torii, standing on a stone wall at the top of steps among tall trees','The hall of Tamaki Shrine seen beyond a wooden torii',hero=True)+"""
  <aside class="toc" aria-label="Table of contents">
    <div class="toc-label">TABLE OF CONTENTS ／ 目次</div>
    <div class="toc-title">In This Guide</div>
    <ol>
      <li><a href="#opening">A Shrine You Have to Earn</a></li>
      <li><a href="#history">The Inner Sanctuary of Kumano</a></li>
      <li><a href="#walk">The Walk Up to the Hall</a></li>
      <li><a href="#trees">The Great Cedars</a></li>
      <li><a href="#tamaishi">Tamaishi-sha, the Shrine Without a Building</a></li>
      <li><a href="#office">The Shrine Office and Its Paintings</a></li>
      <li><a href="#visit">Visiting Tamaki Shrine</a></li>
      <li><a href="#faq">Frequently Asked Questions</a></li>
      <li><a href="#final">Before You Go</a></li>
    </ol>
  </aside>

  <article>

    <p class="opening" id="opening">As a licensed guide, I do not recommend a shrine lightly when the road to it is a winding one-lane mountain track, but Tamaki is one of the places that make the effort feel justified: a quiet hall in a forest of huge cedars, high above the Totsukawa valley.</p>
    <p>Tamaki Shrine sits just below the summit of Mt. Tamaki, at 1,076 metres, in Totsukawa Village in the south of Nara (MLIT). It is regarded as the inner sanctuary of the Kumano Sanzan, the three great shrines of Kumano, and it stands on the Omine Okugakemichi, the mountain pilgrimage route between Yoshino and Kumano (GLTJP, MLIT). A popular saying holds that only those who are called can reach it. This guide covers the history, the walk, the trees, the stone shrine near the summit, and how to get there.</p>

    <h2 id="history">The Inner Sanctuary of Kumano<span class="h2-jp">熊野三山の奥の院</span></h2>
    <p>The MLIT guide says the shrine is believed to have been founded in 37 BCE, during the reign of the legendary Emperor Sujin, to protect his castle from fire and evil spirits. It adds that the area&rsquo;s myths go back further: Emperor Jimmu, the first emperor of legend, is said to have passed through while a mythical crow guided him north from Kyushu. GLTJP says that on his eastern expedition Jimmu rested his troops here and prayed for victory. These are traditions, not documented dates.</p>
    <p>The historical record is firmer from the eighth century. MLIT names En no Gyoja (634 to 706), the founder of Shugendo, as an early visitor who chose Tamaki as one of the training sites along the mountain trail. From the Heian period (794 to 1185) the mountain flourished as a Shugendo training centre and an important stop on the Okugakemichi. When the government separated Shinto and Buddhism in the Meiji era, most Buddhist buildings on shrine grounds were destroyed, but Tamaki kept or repurposed some of its temple elements (MLIT).</p>
    <p>The main hall enshrines Kunitokotachi, the first deity to appear at the creation of heaven and earth, together with Izanagi, Izanami and Amaterasu (MLIT). Our """+a('/culture/japanese-mythology/','Japanese mythology guide','mythology')+""" tells the stories of those gods. Tamaki is part of the same Kii Mountain Range World Heritage listing as """+a('/guides/kumano-kodo/','the Kumano Kodo','kodo')+""" and """+a('/guides/kumano-hongu-taisha/','Kumano Hongu Taisha','hongu')+""", registered in 2004 (MLIT).</p>

    <h2 id="walk">The Walk Up to the Hall<span class="h2-jp">参道</span></h2>
    <p>You cannot drive to the shrine itself. Cars stop at a car park, and from there you walk an earthen path through the forest, then climb stone steps (the walk is given as 10, 15 or 20 minutes, depending on the source). The GLTJP entry warns that the road is narrow with many sharp bends and that snow is common in winter. It also notes that fog is frequent, which gives the grounds their atmosphere.</p>
"""+fig('michishirube','Weathered grey stone marker with carved characters standing at an angle in a bed of dry pine needles and twigs, with sunlight and shade across it','A stone waymarker beside the mountain path. The top characters read 玉置神社, Tamaki Shrine; I cannot read the distance inscription below them with confidence')+"""
    <p>The stone torii at the foot of the final steps carries a plaque reading 玉置神社. Paper streamers hang from the shimenawa, and the steps are fitted with a handrail.</p>
"""+fig('stone-torii','Stone torii with a rope across it at the bottom of a long flight of stone steps between stone lanterns, with a stone retaining wall at the sides and a hall roof peeking out at the top','The stone torii and the steps up to the hall')+fig('torii-plaque','Close view of a stone torii with a carved plaque, a thick rope hung with white paper streamers and a flight of stone steps with a handrail rising to a hall among trees','The plaque on the torii and the stone steps beyond, with a handrail on the right')+"""
    <p>At the top, the hall stands on a moss-covered stone wall. MLIT says the main hall is about 200 years old and built of keyaki (zelkova) wood; GLTJP describes it as a gabled hall of zelkova. Visitors in white sit on its veranda in the photograph below.</p>
"""+fig('honden-steps','Looking up wide stone steps framed by a thick rope with white paper streamers at the top of the picture, to a hall with a curved gabled roof and two visitors in white seated in front','Looking up the steps to the hall under the shimenawa')+fig('boulder','Large rounded boulder standing beside a small wooden torii and a flight of rough wooden steps, with forest and a corrugated metal wall behind it','A huge boulder beside a small torii and wooden steps. On Wikimedia Commons the photo is filed as &ldquo;Tamaki Ryujinsui&rdquo;; I have not confirmed what the boulder is called on site')+"""
    <h2 id="trees">The Great Cedars<span class="h2-jp">杉の巨木</span></h2>
    <p>The shrine&rsquo;s reputation rests on its trees. MLIT says a long ban on logging preserved the ancient cedars, naming the roughly 3,000-year-old Jindai-sugi, the O-sugi, and the Meoto-sugi, two trees joined at the trunk (<em>meoto</em> means &ldquo;wedded&rdquo;). GLTJP calls the Jindai-sugi &ldquo;said to be&rdquo; 3,000 years old, which is a traditional estimate.</p>
    <p>The figures for the O-sugi do not agree. MLIT gives it as about 50 metres tall with an 11-metre circumference. A hiker who copied the on-site sign reports about 40 metres, a girth of 8.7 metres and an age of about 1,000 years (YAMAP). For the Jindai-sugi the same hiker reports about 8.3 metres of girth and about 20 metres of height. Treat the sizes as approximate. In spring, rhododendrons bloom across the grounds (Rurubu).</p>
"""+fig('cedars','Tall cedar trunks rising along a pale gravel path that curves through the forest, with light coming through the branches','Tall cedars along the mountain path')+"""
    <h2 id="tamaishi">Tamaishi-sha, the Shrine Without a Building<span class="h2-jp">玉石社</span></h2>
    <p>Above the main hall, on the way to the summit, stands Tamaishi-sha. MLIT describes it as a subordinate shrine halfway between the main hall and the peak, with no building: a partly buried black rock surrounded by white pebbles in an enclosure among the cedars, which reflects the ancient worship of natural phenomena. MLIT says it is considered the origin of the shrine. GLTJP adds that it is said to hold a sacred stone placed by Emperor Jimmu, that it is the origin of the shrine&rsquo;s name, and that practitioners of Shugendo traditionally visit it before the main hall. A hiking report puts it about 15 minutes above the hall (Visit Japan Vegetarian).</p>

    <h2 id="office">The Shrine Office and Its Paintings<span class="h2-jp">社務所</span></h2>
    <p>The shrine office was built in 1804 as the main hall and kitchen of a former Buddhist temple, and it is an Important Cultural Property (MLIT). Its sliding doors carry late Edo-period paintings of plants and animals; Rurubu and GLTJP describe them as Kano-school work. Viewing them costs 500 yen (GLTJP, Rurubu). The MLIT text also notes that some buildings and artefacts are under long-term restoration and some areas may be closed, so check what is open.</p>

    <h2 id="visit">Visiting Tamaki Shrine<span class="h2-jp">参拝案内</span></h2>
    <ul class="practical-list">
      <li><strong>Address:</strong> 1 Tamakigawa, Totsukawa Village, Yoshino District, Nara 647-1582.</li>
      <li><strong>Hours:</strong> the grounds are always open (GLTJP). The shrine office is open 8:00 to 17:00 (Rurubu); Sparkle Travel gives 8:00 to 16:00. No closing days.</li>
      <li><strong>Fee:</strong> the grounds are free. The paintings in the office are 500 yen (GLTJP, Rurubu); Japan Experience gives 300 yen, which looks out of date.</li>
      <li><strong>By car:</strong> Rurubu says 2 hours 30 minutes from Katsuragi IC via Routes 24 and 168; Japan 47 Go says about 150 minutes from Gojo IC. From the Totsukawa Onsen bus stop it is about 30 minutes by car (Rurubu) or 40 minutes (GLTJP). Parking is free, for about 50 cars (Japan 47 Go) or 60 (Rurubu), and fills up at busy times.</li>
      <li><strong>By bus and taxi:</strong> JR Gojo Station to Totsukawa Onsen by Nara Kotsu express bus about 3 hours (Rurubu); from Shingu Station about 2 hours (Deep Experience). Then a taxi of about 30 minutes, or the reservation-only World Heritage bus on weekends and holidays from April to November (GLTJP).</li>
      <li><strong>Winter:</strong> snow is common and chains may be required (GLTJP, Japan 47 Go); road closures are reported (nara-sightseeing). Check ahead.</li>
      <li><strong>On foot:</strong> hikers combine Tamaki with Kumano Hongu Taisha on the Okugakemichi and the Kohechi trails (YAMAP trip report). That is a serious mountain walk and I have not checked current trail conditions.</li>
      <li><strong>Notes:</strong> wear shoes with grip. Bring a layer, as it is cold and often foggy at 1,076 metres.</li>
    </ul>
    <div class="key-callout">
      <p>&#127890; <strong>Plan your trip:</strong> Browse guided tours around Kumano and the Kii Peninsula. <a href="https://www.viator.com/search/Kumano?pid=P00298374&amp;mcid=42383&amp;medium=link&amp;campaign=sacred-japan" target="_blank" rel="noopener" onclick="trackEvent('click','affiliate','viator_tamaki_jinja')">Book a Tour</a></p>
    </div>

    <h2 id="faq">Frequently Asked Questions<span class="h2-jp">よくあるご質問</span></h2>
    <div class="faq-stack">
@@FAQ@@    </div>

    <h2 id="final">Before You Go<span class="h2-jp">むすびに</span></h2>
    <p>Tamaki is the quiet counterpart to Kumano Hongu Taisha: far fewer visitors, and a longer way in. Go on a clear weekday if you can, check the road first, and give yourself time for the cedars and the steps.</p>

    <div class="closing-block">
      <span class="torii">&#9961;&#65039;</span>
      <p>A hall among giant cedars on a Kumano mountaintop, reached by a road that makes you earn it.</p>
    </div>

    <section class="related-section">
      <h2>Related Guides</h2>
      <span class="h2-jp">関連ガイド</span>
      <div class="related-grid">
        <a class="related-card" href="/guides/kumano-kodo/" onclick="trackEvent('click','internal','related_tamaki_to_kodo')">
          <div class="related-card-label">SACRED JAPAN ／ GUIDES</div>
          <div class="related-card-title">&#129517; Kumano Kodo &rarr;</div>
          <div class="related-card-desc">Japan&rsquo;s answer to the Camino de Santiago.</div>
        </a>
        <a class="related-card" href="/guides/kumano-hongu-taisha/" onclick="trackEvent('click','internal','related_tamaki_to_hongu')">
          <div class="related-card-label">SACRED JAPAN ／ GUIDES</div>
          <div class="related-card-title">&#9961;&#65039; Kumano Hongu Taisha &rarr;</div>
          <div class="related-card-desc">The head shrine of the Kumano Sanzan, and the three-legged crow.</div>
        </a>
        <a class="related-card" href="/culture/japanese-mythology/" onclick="trackEvent('click','internal','related_tamaki_to_mythology')">
          <div class="related-card-label">SACRED JAPAN ／ CULTURE</div>
          <div class="related-card-title">&#128214; Japanese Mythology &rarr;</div>
          <div class="related-card-desc">Kojiki gods, famous myths and the shrines where they happen.</div>
        </a>
      </div>
    </section>

  </article>

"""
build(dict(slug='tamaki-jinja',ev='tamaki_jinja',jp='玉置神社',en='Tamaki Shrine',dest='Kumano',thumb='honden-torii',photos=P,faqs=faqs,body=body,
 title="Tamaki Shrine Guide: Kumano's Inner Sanctuary, Giant Cedars and a Hard Road in Nara",
 desc="A licensed guide's guide to Tamaki Shrine (Tamaki Jinja) in Totsukawa, Nara: the inner sanctuary of Kumano, the giant cedars, Tamaishi-sha, the Okugakemichi, hours, fees, the narrow road, winter snow and the reservation bus.",
 tag="A mountaintop shrine among giant cedars in southern Nara, the inner sanctuary of Kumano, reached by a hard road.",
 kw="Tamaki Shrine, Tamaki Jinja, Totsukawa shrine, Kumano inner sanctuary, Jindai-sugi, Tamaishi-sha, Omine Okugakemichi, Nara shrine, Kii Mountain Range World Heritage, Kumano Kodo",
 h1="<h1><em>Tamaki Shrine</em>: Kumano&rsquo;s Inner Sanctuary, Giant Cedars and a Hard Road in Nara</h1>",
 og=("Tamaki Shrine Guide:","Kumano's Inner Sanctuary"),
 sources=[('https://www.mlit.go.jp/tagengo-db/R5-00238.html','mlit1','MLIT multilingual guide (shrine)'),('https://www.mlit.go.jp/tagengo-db/R5-00239.html','mlit2','MLIT multilingual guide (Okugakemichi)'),('https://www.gltjp.com/en/directory/item/12939/','gltjp','GLTJP'),('https://rurubu.jp/andmore/spot/80031852','rurubu','Rurubu'),('https://www.japan47go.travel/en/detail/3faff9f1-eaed-473b-a576-bb85458d91dd','j47','Japan 47 Go'),('https://www.deep-exp.com/cn/nara/spot/979','deep','Deep Experience'),('https://www.sparkle.travel/en/place/8283efd6-dc5c-11ee-9b39-c7c8948f11a7','sparkle','Sparkle Travel'),('https://nara-sightseeing.com/blog/japans-oldest-shrine-tamaki-shrine-which-can-only-be-reached-by-being-called-by-the-gods/','nara','nara-sightseeing'),('https://visitjapan-vegetarian.com/?p=12354','vjv','Visit Japan Vegetarian'),('https://en.japantravel.com/nara/tamaki-shrine-in-totsukawa-nara/5920','jt','Japan Travel'),('https://yamap.com/activities/12245442/article','yamap','YAMAP'),('https://www.japan-experience.com/discover/nara/temple-shrines/tamaki-jinja-totsukawa-shrine','je','Japan Experience')]))
