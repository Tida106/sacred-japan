import sys
sys.path.insert(0, '/home/claude/sacred-japan/_tools/culture')
from shinobi_common import *

S = 'nijigen-no-mori'
# No photos yet. Add copy_photos + fig here when sent.

SHZ = ext('https://nijigennomori.com/en/?p=174126', 'the official Shinobi-zato page', 'nijigen_src_shinobizato')
VIP = ext('https://nijigennomori.com/en/?p=185256', 'the official VIP Journey Pass page', 'nijigen_src_vip')
HYO = ext('https://www.hyogo-tourism.jp/world/spot/detail_1067.html', 'Hyogo Tourism', 'nijigen_src_hyogo')
PAS = ext('https://en.awajiisland.pasonagroup.co.jp/?p=31475', 'the Pasona Group Awaji Island site', 'nijigen_src_pasona')
VI_NJ = viator('Nijigen+no+Mori')

faqs = [
    ("Is entry to Nijigen no Mori free?",
     "Hyogo Tourism says park entry is free and that each attraction needs its own paid ticket. The park is listed as open 10:00 to 22:00, but each attraction has its own last-entry and closing times."),
    ("How much is the NARUTO x BORUTO Shinobi-zato ticket?",
     "The official page lists Light Tickets at 3,300 to 4,100 yen for adults (12 and over) and 1,800 to 2,200 yen for children (5 to 11), with Golden Tickets from 4,800 to 5,600 yen and premium passes up to 15,100 yen. Prices vary by season, so check the official ticket page before you book."),
    ("How long does Shinobi-zato take?",
     "The official page estimates about 60 minutes for the Heavenly Scroll and about 30 minutes for the Earth Scroll, plus about 60 minutes for the optional Earth Scroll Side Story, which needs an extra ticket. The Hokage Rock projection mapping runs at night, starting at dusk."),
    ("Can I bring a stroller or wheelchair?",
     "The official Shinobi-zato page says wheelchairs and strollers are not allowed inside because of steep slopes. A stroller parking area is near the information desk. Children aged 4 and under enter free, and under-2s cannot do the Heavenly Scroll."),
    ("How do I get there from Kobe or Osaka?",
     "Hyogo Tourism lists highway buses of roughly 50 to 60 minutes from Kobe's Sannomiya or Shin-Kobe stations and about 90 minutes from Osaka's Umeda, and the Pasona page gives about 40 minutes from Sannomiya on the morning express. By car, Awaji IC is about 3 minutes away. Bus times and stop names differ by source, so check the operator."),
    ("Is there Dragon Quest here too?",
     "Yes. Dragon Quest Island is described by the Pasona Group site as a field RPG attraction that combines the real and digital worlds, with its own tickets and hours. See the section below."),
]
faq_html, faq_ld = faq_blocks(faqs)

main = f'''<main>

  <aside class="toc" aria-label="Table of contents">
    <div class="toc-label">TABLE OF CONTENTS ／ 目次</div>
    <div class="toc-title">In This Guide</div>
    <ol>
      <li><a href="#opening">Opening: A Note from the Guide</a></li>
      <li><a href="#what">What Nijigen no Mori Is</a></li>
      <li><a href="#shinobi">NARUTO x BORUTO Shinobi-zato</a></li>
      <li><a href="#tickets">Tickets and Rules</a></li>
      <li><a href="#dq">Dragon Quest Island</a></li>
      <li><a href="#access">Getting There</a></li>
      <li><a href="#faq">Frequently Asked Questions</a></li>
      <li><a href="#final">Final Thoughts</a></li>
    </ol>
  </aside>

  <article>

    <section id="opening">
      <p class="opening">Most ninja sites in Japan are real houses with trap doors. This one is a village from a manga, rebuilt in a forest on Awaji Island, and you are the ninja.</p>
      <p>As a licensed guide, I recommend it to readers of our {link('/culture/ninja/', 'ninja guide', 'nijigen_to_ninja')} who want the fictional side of the story. This guide covers what the Shinobi-zato area offers, what the tickets and rules are, and how to reach the park from Kobe and Osaka. Prices and times change by season, so I link the official pages for you to check.</p>
    </section>

    <h2 id="what">What Nijigen no Mori Is<span class="h2-jp">ニジゲンノモリとは</span></h2>
    <p>Nijigen no Mori ("Forest of the Second Dimension") is a theme park inside Hyogo Prefectural Awaji Island Park, in Awaji City, Hyogo. {VIP} gives the park's size as 134.8 hectares, and says the operator, Pasona Group, began regional work on Awaji Island in 2008 and that its "Awaji Manga &amp; Anime Island Project" was selected by Hyogo Prefecture in 2013.</p>
    <p>{HYO} lists two main attractions: Shinobi-zato, based on the world of NARUTO and BORUTO, with ninja-style athletic challenges, and Dragon Quest Island. It also mentions limited-time collaborations and nighttime projection mapping. Park entry is free, but each attraction needs its own ticket.</p>

    <h2 id="shinobi">NARUTO x BORUTO Shinobi-zato<span class="h2-jp">忍里</span></h2>
    <p>{SHZ} describes the area as a recreation of the Hidden Leaf Village, with the roughly 11-meter Hokage Rock at its center. These are the main experiences:</p>
    <ul>
      <li><strong>Heavenly Scroll (<span class="jp">天の巻</span>):</strong> a three-story attraction behind Hokage Rock. You collect stamps, combine hand seals to activate magic, and break through a closed door to reach the third-floor goal. The estimated time is 60 minutes.</li>
      <li><strong>Earth Scroll (<span class="jp">地の巻</span>):</strong> a mission to collect 12 signs around the village and seal a giant enemy in a legendary cave, estimated at 30 minutes.</li>
      <li><strong>Earth Scroll Side Story:</strong> a puzzle-kit mystery of about 60 minutes. It needs a separate Chi no Maki Gaiden ticket in addition to admission.</li>
      <li><strong>Hokage Rock projection mapping:</strong> a night-only show, starting at dusk. {VIP} says it lasts about 10 minutes.</li>
      <li><strong>AR ninjutsu:</strong> a free app called "Aim to be the Hokage!" Mastering five techniques makes your face appear on Hokage Rock, according to the page.</li>
    </ul>
    <p>The VIP Journey Pass page also lists extra missions, such as a Kids Ninja Course of 30 minutes, and says some missions run for a limited period only. Which ones are on offer will change, so check the current list.</p>

    <h2 id="tickets">Tickets and Rules<span class="h2-jp">チケットと注意点</span></h2>
    <p>The official page lists these prices for Shinobi-zato, tax included, and says they vary by season:</p>
    <ul>
      <li><strong>Light Ticket:</strong> adults (12 and over) 3,300 to 4,100 yen; children (5 to 11) 1,800 to 2,200 yen.</li>
      <li><strong>Golden Ticket:</strong> adults 4,800 to 5,600 yen; children 3,100 to 3,500 yen.</li>
      <li><strong>Premium tickets and VIP Journey Pass:</strong> adults 11,300 to 15,100 yen. The VIP Journey Pass includes a premium bag or backpack, according to its official page.</li>
    </ul>
    <ul>
      <li><strong>Hours:</strong> 10:00 to 20:00, last entry 18:00, with hours changing by season.</li>
      <li><strong>Children:</strong> 4 and under enter free; ages 5 to 11 must be accompanied by a guardian who also buys an attraction ticket; under-2s cannot do the Heavenly Scroll.</li>
      <li><strong>Strollers and wheelchairs:</strong> not allowed inside because of steep slopes.</li>
      <li><strong>Pets:</strong> not allowed unless in a locked cage.</li>
    </ul>
    <p>{VIP} recommends buying tickets online in advance for smoother entry. If you want to stay on site, it also mentions the Hokage's Villa, a themed accommodation at Grand Chariot that is booked through its own site. If you would rather compare booked tickets or tours, you can look at {aff(VI_NJ, 'Nijigen no Mori options on Viator', 'nijigen_viator')}, though I have not tested them myself.</p>

    <h2 id="dq">Dragon Quest Island<span class="h2-jp">ドラゴンクエストアイランド</span></h2>
    <p>{PAS} describes Dragon Quest Island as a field RPG attraction that combines real and digital worlds. It lists hours of 10:00 to 20:30 on weekdays (last entrance 18:00) and 10:00 to 22:00 on weekends and holidays (last entrance 19:30), and these prices:</p>
    <ul>
      <li><strong>Light Ticket (admission and main quest):</strong> adults 3,400 to 4,500 yen; children (5 to 11) 1,800 to 2,500 yen.</li>
      <li><strong>Gold Ticket (adds a side quest):</strong> adults 5,400 to 6,500 yen; children 3,100 to 3,800 yen.</li>
      <li><strong>Premium Ticket (adds premium goods):</strong> adults 12,400 to 13,500 yen; children 10,800 to 11,500 yen.</li>
    </ul>
    <p>That page was last modified in February 2026, so please check the official ticket page for current prices.</p>

    <h2 id="access">Getting There<span class="h2-jp">アクセス</span></h2>
    <ul>
      <li><strong>By car:</strong> about 3 minutes from Awaji IC on the Kobe-Awaji-Naruto Expressway, with parking for about 1,300 cars, according to {HYO}. The Highway Oasis car park is paid.</li>
      <li><strong>By highway bus from Kobe:</strong> the same source lists about 50 minutes from Sannomiya and about 60 minutes from Shin-Kobe, while {PAS} gives about 40 minutes from Sannomiya on a morning express.</li>
      <li><strong>By highway bus from Osaka:</strong> about 90 minutes from Umeda and about 120 minutes from Namba (Hyogo Tourism).</li>
      <li><strong>By boat:</strong> about 15 minutes from Akashi Port to Iwaya Port, then about 15 minutes by shuttle bus (Hyogo Tourism).</li>
    </ul>
    <p>Stop names are not consistent between sources: Hyogo Tourism says to get off at "Highway Oasis Nijigen no Mori Iriguchi," while the Pasona page names "NIJIGEN NO MORI F Parking Lot." Please confirm the stop and timetable with the bus operator before you travel.</p>

    <h2 id="faq">Frequently Asked Questions<span class="h2-jp">よくあるご質問</span></h2>

    <div class="faq-stack">

{faq_html}    </div>

    <h2 id="final">Final Thoughts<span class="h2-jp">むすびに</span></h2>
    <p>Pair it with the real thing: see the trick houses and museums in our {link('/culture/ninja/', 'ninja guide', 'nijigen_final_to_ninja')}, then spend a day here in the village from the manga. Book tickets ahead, wear shoes you can climb in, and check the season's hours.</p>

    <div class="closing-block">
      <span class="torii">🥷</span>
      <p>A forest, a Hokage Rock and a mission to finish.</p>
    </div>

    <section class="related-section">
      <h2>Related Guides</h2>
      <span class="h2-jp">関連ガイド</span>
      <div class="related-grid">
        <a class="related-card" href="/culture/ninja/" onclick="trackEvent('click','internal','related_nijigen_to_ninja')">
          <div class="related-card-label">SACRED JAPAN ／ GUIDE</div>
          <div class="related-card-title">🥷 Ninja Guide →</div>
          <div class="related-card-desc">Iga and Koka, museums, a festival and the manga.</div>
        </a>
        <a class="related-card" href="/culture/samurai-and-ninja/" onclick="trackEvent('click','internal','related_nijigen_to_hub')">
          <div class="related-card-label">SACRED JAPAN ／ FEATURE</div>
          <div class="related-card-title">⚔️ Samurai &amp; Ninja Feature →</div>
          <div class="related-card-desc">Where to go, what to do and what to read.</div>
        </a>
        <a class="related-card" href="/anime/" onclick="trackEvent('click','internal','related_nijigen_to_anime')">
          <div class="related-card-label">SACRED JAPAN ／ HUB</div>
          <div class="related-card-title">🎬 Anime Pilgrimage →</div>
          <div class="related-card-desc">Real places behind favorite series.</div>
        </a>
        <a class="related-card" href="/guides/japan-travel-planning/" onclick="trackEvent('click','internal','related_nijigen_to_planning')">
          <div class="related-card-label">SACRED JAPAN ／ GUIDE</div>
          <div class="related-card-title">🧭 Japan Travel Planning →</div>
          <div class="related-card-desc">Money, rail and the practical basics.</div>
        </a>
      </div>
    </section>

    <p style="font-size:14px;color:var(--enshu);line-height:1.7;margin-top:32px;"><strong>Sources:</strong> Shinobi-zato from {SHZ} and {VIP}; park, access and size from {HYO} and {PAS}. I have not verified current prices, hours or bus timetables.</p>

  </article>

</main>'''

TITLE = 'Nijigen no Mori Guide: NARUTO x BORUTO Shinobi-zato, Dragon Quest Island and Access'
DESC = "A licensed guide's English introduction to Nijigen no Mori on Awaji Island: the NARUTO x BORUTO Shinobi-zato village, tickets and rules, Dragon Quest Island, and how to get there from Kobe and Osaka."
KEYWORDS = 'Nijigen no Mori, Nijigen no Mori guide, NARUTO BORUTO Shinobi-zato, Naruto theme park Japan, Awaji Island, Hokage Rock, Dragon Quest Island, Naruto pilgrimage, Awaji Island Park, anime theme park Japan'
url = finish(S, TITLE, DESC, KEYWORDS, '忍里', 'The <em>Nijigen no Mori</em> Guide', 'ニジゲンノモリ ガイド',
             'NARUTO x BORUTO Shinobi-zato, Dragon Quest Island and Access', 'Nijigen no Mori Guide',
             'guide_nijigen', 'Nijigen+no+Mori', main, faq_ld)
print(url)
