import sys
sys.path.insert(0, '/home/claude/sacred-japan/_tools/culture')
from shinobi_common import *

S = 'ninja'
# No photos yet: the repo has no ninja photographs. Add them here (copy_photos + fig) when sent.

JTR = ext('https://www.japan.travel/en/japan-magazine/discover-origins-ninja-iga-koka/', 'Japan National Tourism Organization (JNTO)', 'ninja_src_jnto')
IGA = ext('https://iganinja.jp/en/museum', 'the museum\'s official English page', 'ninja_src_iga_official')
JG = ext('https://japan-guide.com/e/e4351.html', 'japan-guide.com', 'ninja_src_japanguide')
GLT = ext('https://www.gltjp.com/en/directory/item/11744/', 'GLTJP', 'ninja_src_gltjp')
KWJ = ext('https://web-japan.org/kidsweb/travel/ninja/ninja02.html', 'Kids Web Japan', 'ninja_src_kidsweb')
TO = ext('https://www.timeout.com/tokyo/news/japan-ninja-council-now-offers-ninja-courses-in-asakusa-071621', 'Time Out Tokyo', 'ninja_src_timeout')
FESTA = ext('https://en.wikipedia.org/wiki/Iga_Ueno_Ninja_Festa', 'Wikipedia', 'ninja_src_festa')
ANN_K = ext('https://www.animenewsnetwork.com/encyclopedia/people.php?id=8036', 'Anime News Network', 'ninja_src_ann')
NARU = ext('https://naruto-official.com/en/about', 'the official Naruto site', 'ninja_src_naruto')
BASI = ext('https://animenewsnetwork.com/news/2017-07-19/basilisk-sequel-novels-get-tv-anime-manga/.119037', 'Anime News Network', 'ninja_src_basilisk')
VI_NIN = viator('Japan+ninja+experience')

faqs = [
    ("Where did the ninja come from?",
     "Japan's tourism organization says Iga (Mie Prefecture) and Koka (Shiga Prefecture), neighboring areas in the Kinki region, are the birthplaces of the ninja, and that ninja rose to prominence in the Sengoku period (1467 to 1568), working as covert operatives and spies for their lords. The same page is tourism promotion and hedges many claims with \"said to,\" so treat the colorful details as local tradition."),
    ("What is the difference between Iga and Koka?",
     "They are two neighboring areas, Iga in Mie and Koka in Shiga, with Koka to the north. Each has its own ninja sites: the Ninja Museum of Igaryu in Iga Ueno, and the Koka Ninja Village and a trick-house residence in Koka."),
    ("Is the ninja show at the Iga museum in English?",
     "japan-guide.com says the show is in Japanese only, but that the action, including a throwing-star demonstration, is easy to follow without the language. The exhibition signs are in Japanese and English."),
    ("How much does the Ninja Museum of Igaryu cost?",
     "Sources differ. The museum's official English page lists adults at 1,000 yen and the show at 600 yen, with six shuriken throws for 300 yen. japan-guide.com lists 800 yen for the museum and 500 yen for the show. Neither page is dated clearly, so check the museum before you go."),
    ("Can I try ninja training in Tokyo?",
     "In 2021 Time Out Tokyo reported courses at the Ninja Information Centre Tokyo & Dojo in Asakusa, run by the Japan Ninja Council, from a 40-minute experience at 2,200 yen to a 90-minute course at 9,900 yen. That is an old report, so please confirm what is offered now."),
    ("When is the Iga Ueno Ninja Festa?",
     "Wikipedia gives it as an annual, family-friendly festival running from April 1 to May 6 in Iga, and says people in ninja costume ride Iga train lines free. Dates can change, so check the local tourism information."),
    ("Are ninja and samurai the same?",
     "No. Samurai were the warrior class; the ninja described here were covert operatives from Iga and Koka. Our samurai guide covers the warrior class and the end of their era."),
]
faq_html, faq_ld = faq_blocks(faqs)

main = f'''<main>

  <aside class="toc" aria-label="Table of contents">
    <div class="toc-label">TABLE OF CONTENTS ／ 目次</div>
    <div class="toc-title">In This Guide</div>
    <ol>
      <li><a href="#opening">Opening: A Note from the Guide</a></li>
      <li><a href="#who">Who the Ninja Were</a></li>
      <li><a href="#iga-koka">Iga and Koka</a></li>
      <li><a href="#visit">Places to Visit</a></li>
      <li><a href="#experience">Experiences and the Ninja Festa</a></li>
      <li><a href="#media">Ninja in Manga and Anime</a></li>
      <li><a href="#faq">Frequently Asked Questions</a></li>
      <li><a href="#final">Final Thoughts</a></li>
    </ol>
  </aside>

  <article>

    <section id="opening">
      <p class="opening">Ask a visitor to draw a ninja and you will get a figure in black, throwing stars. Ask a historian and the answer is quieter, and tied to two valleys near Kyoto.</p>
      <p>As a licensed guide, I can tell you which places let you see how the real ninja houses worked, and which parts of the popular image come from fiction. This guide covers Iga and Koka, the museums and trick houses, a festival, and the manga that made the ninja famous. It also marks where my sources lean on tradition. For the warrior class they are often confused with, see our {link('/culture/samurai/', 'samurai guide', 'ninja_to_samurai')}.</p>
    </section>

    <h2 id="who">Who the Ninja Were<span class="h2-jp">忍者とは</span></h2>
    <p>Ninja (<span class="jp">忍者</span>), also called shinobi, were covert operatives. {JTR} describes them as covert warriors who came to prominence in the Sengoku period (1467 to 1568), working in espionage and other secret operations for their lords. It names the Fujibayashi family as specialists in fire and gunpowder-related techniques.</p>
    <p>A word on that source: it is a tourism-promotion page, and it hedges many claims with "said to." For example, it says the famous manual <em>Bansenshukai</em> is "said to have been written" in 1676. I will not repeat the more colorful claims, because I cannot confirm them. What the page, and the museums it points to, do agree on is the picture below: houses built to defend against intruders and a culture of information gathering.</p>

    <h2 id="iga-koka">Iga and Koka<span class="h2-jp">伊賀と甲賀</span></h2>
    <p>{JTR} says Iga City (Mie) and Koka City (Shiga) sit next to each other in the Kinki region, with Koka to the north, and calls them the birthplaces of the ninja. It also says the two areas were self-governing in the Sengoku period, run by local families and samurai without a daimyo's authority, and that village codes called for deciding things by discussion. The two regions are also recognized as a Japan Heritage site with the name "Exploring the Birthplace of the Real Ninja."</p>
    <p>If you are planning a trip, the same page says day trips are possible from Osaka or Kyoto by train. For Iga you can take the Tokaido Shinkansen to Nagoya, and for Koka to Kyoto, and it mentions a Ninja Train on the Iga Railway from Kintetsu Iga-Kambe or JR Iga-Ueno.</p>

    <h2 id="visit">Places to Visit<span class="h2-jp">見学先</span></h2>

    <h3>Ninja Museum of Igaryu (Iga Ueno, Mie)</h3>
    <p>{JG} says the museum is in Ueno Park, a 5 to 10 minute walk north of Uenoshi Station. It has three parts: a ninja residence that looks ordinary outside but has revolving walls, trap doors and hidden compartments, explained on a guided tour; two exhibition halls of tools, costumes and weapons with Japanese and English signs; and a ninja show with real weapons. {IGA} adds that the exhibits include more than 400 ninja tools and that some can be tried. {JTR} says it stands on the site of the former Heirakuji Temple.</p>
    <ul>
      <li><strong>Hours:</strong> 10:00 to 16:00 on weekdays (last entry 15:30) and 10:00 to 16:30 on weekends and holidays (last entry 16:00), per the official page. It lists a closure from December 29 to January 1.</li>
      <li><strong>Admission:</strong> adults 1,000 yen and children 700 yen, with the show at 600 yen and six shuriken throws at 300 yen, according to the official page. japan-guide.com gives lower figures (800 yen and 500 yen), so please confirm before you go.</li>
    </ul>

    <h3>Koka Ninja Village (Koka, Shiga)</h3>
    <p>{GLT} (listing updated in May 2026) describes a village at the foot of the Suzuka Mountains with a ninjutsu museum in a thatched house believed to have belonged to Koka ninja, a trick house that is the relocated home of the Fujibayashi family, with a flipping wall, hidden stairs and an escape hole under a hearth, and a ninja dojo with nine practice places.</p>
    <ul>
      <li><strong>Hours:</strong> 10:00 to 17:00, last entry 16:00, closed Mondays (the next day if Monday is a holiday).</li>
      <li><strong>Admission:</strong> 2,000 yen for adults and 1,500 yen for children. Credit cards are not accepted, so bring cash.</li>
      <li><strong>Getting there:</strong> a free shuttle of about 5 minutes from Koka Station on the JR Kusatsu Line.</li>
    </ul>

    <h3>Koka-ryu Ninjutsu Yashiki (Koka, Shiga)</h3>
    <p>{KWJ} describes a samurai residence built about 300 years ago that looks like a single-story thatched house but has three stories, with a pitfall trap, a revolving wall for vanishing quickly and a rope ladder from the third floor to the ground-floor entrance. {JTR} dates it to the Genroku era and says it is within walking distance of Konan Station, and the Kids Web Japan page gives the route as the JR Tokaido Line from Kyoto, changing at Kusatsu to the Kusatsu Line.</p>

    <h3>Other places in Iga and Koka</h3>
    <p>{JTR} also lists Iga Ueno Castle, whose reconstructed keep stands behind a stone wall about 30 meters high; Matsumoto-in Temple in Iga (built 1616, a Shugendo temple); and Aburahi Shrine in Koka, where a corridor built in 1566 was once a meeting place for Koka samurai. These are good additions if you stay overnight in the area.</p>

    <h2 id="experience">Experiences and the Ninja Festa<span class="h2-jp">体験とお祭り</span></h2>
    <ul>
      <li><strong>Ninja training in Tokyo.</strong> {TO} reported in July 2021 that the Japan Ninja Council runs courses at the Ninja Information Centre Tokyo &amp; Dojo in Asakusa: a 40-minute experience (shuriken, hand signs, an explanation of spy gear) at 2,200 yen, with costume rental at 1,100 yen extra, and longer courses of 60 and 90 minutes at 7,700 and 9,900 yen. It recommends booking. That report is old, so confirm current courses and prices.</li>
      <li><strong>Iga Ueno Ninja Festa.</strong> {FESTA} describes an annual family-friendly festival in Iga running from April 1 to May 6, with ninja-themed performances and contests. It says passengers in ninja costume ride Iga train lines free, and that since 2001 the mayor and city council have held a yearly session dressed as ninja. Treat the dates as a guide and confirm locally.</li>
      <li><strong>The NARUTO x BORUTO village on Awaji Island.</strong> For the fictional side, Nijigen no Mori in Hyogo recreates the Hidden Leaf Village with the 11-meter Hokage Rock, a three-story Heavenly Scroll attraction and a night projection show. Park entry is free and each attraction is ticketed; see our {link('/culture/nijigen-no-mori/', 'Nijigen no Mori guide', 'ninja_to_nijigen')} for tickets, rules and access.</li>
      <li><strong>Guided or hands-on tours.</strong> If you prefer a booked, English-language option, you can compare current {aff(VI_NIN, 'ninja experiences on Viator', 'ninja_viator_experience')}. I have not tried them myself, so please read recent reviews.</li>
    </ul>

    <h2 id="media">Ninja in Manga and Anime<span class="h2-jp">漫画・アニメ</span></h2>
    <p><strong>Naruto</strong> by Masashi Kishimoto ran in <em>Weekly Shonen Jump</em> from 1999 to 2014, and {NARU} says it follows Naruto Uzumaki, an outcast ninja from the Hidden Leaf Village, who wants to become Hokage. It lists 700 chapters, more than 250 million print copies worldwide, and an anime that began in 2002. {ANN_K} lists Kishimoto as born in 1974 in Okayama; if you visit that city, our {link('/guides/okayama-castle/', 'Okayama Castle guide', 'ninja_to_okayama')} covers its castle. I have no source tying the series' village to a real place, so I will not claim one. If you want to walk through a recreation of it, see our {link('/culture/nijigen-no-mori/', 'Nijigen no Mori guide', 'ninja_naruto_to_nijigen')}.</p>
    <p><strong>Basilisk</strong> comes closest to the real map. {BASI} says it adapts Futaro Yamada's 1959 novel <em>Koga Ninpocho</em> (<em>The Kouga Ninja Scrolls</em>) as a 2003 manga by Masaki Segawa, followed by a TV anime in 2005. The Iga and Kouga clans, sworn enemies for more than 400 years, are ordered under Ieyasu Tokugawa to send ten ninja each to fight for the succession, and the lovers Oboro (Iga) and Gennosuke (Kouga) are on opposite sides. "Kouga" is the story's spelling of the area this page writes as Koka, so the clans in the story are the two neighbors above.</p>
    <p>For samurai stories such as <em>Rurouni Kenshin</em> and <em>Vagabond</em>, see our {link('/culture/samurai/', 'samurai guide', 'ninja_media_to_samurai')}. Other series with real locations are in our {link('/anime/', 'anime pilgrimage hub', 'ninja_to_anime')}.</p>

    <h2 id="faq">Frequently Asked Questions<span class="h2-jp">よくあるご質問</span></h2>

    <div class="faq-stack">

{faq_html}    </div>

    <h2 id="final">Final Thoughts<span class="h2-jp">むすびに</span></h2>
    <p>If you have time for one stop, start with the Ninja Museum of Igaryu in Ueno Park. If you are in Shiga or coming from Kyoto, the Koka sites add the trick houses. Read <em>Basilisk</em> or watch its anime before you go and the two valleys will feel like places from a story.</p>

    <div class="closing-block">
      <span class="torii">🥷</span>
      <p>A turning wall, a hidden stair and a story told by shadows.</p>
    </div>

    <section class="related-section">
      <h2>Related Guides</h2>
      <span class="h2-jp">関連ガイド</span>
      <div class="related-grid">
        <a class="related-card" href="/culture/samurai/" onclick="trackEvent('click','internal','related_ninja_to_samurai')">
          <div class="related-card-label">SACRED JAPAN ／ GUIDE</div>
          <div class="related-card-title">⚔️ Samurai Guide →</div>
          <div class="related-card-desc">History, armor, samurai towns and festivals.</div>
        </a>
        <a class="related-card" href="/culture/samurai-and-ninja/" onclick="trackEvent('click','internal','related_ninja_to_hub')">
          <div class="related-card-label">SACRED JAPAN ／ FEATURE</div>
          <div class="related-card-title">🥷 Samurai &amp; Ninja Feature →</div>
          <div class="related-card-desc">Both guides, side by side, with places and events.</div>
        </a>
        <a class="related-card" href="/guides/best-castles-japan/" onclick="trackEvent('click','internal','related_ninja_to_castles')">
          <div class="related-card-label">SACRED JAPAN ／ GUIDE</div>
          <div class="related-card-title">🏯 Best Castles in Japan →</div>
          <div class="related-card-desc">Original keeps and where to see them.</div>
        </a>
        <a class="related-card" href="/anime/" onclick="trackEvent('click','internal','related_ninja_to_anime')">
          <div class="related-card-label">SACRED JAPAN ／ HUB</div>
          <div class="related-card-title">🎬 Anime Pilgrimage →</div>
          <div class="related-card-desc">Real places behind favorite series.</div>
        </a>
      </div>
    </section>

    <p style="font-size:14px;color:var(--enshu);line-height:1.7;margin-top:32px;"><strong>Sources:</strong> origins and sites from {JTR}; the Iga museum from {IGA} and {JG}; Koka Ninja Village from {GLT}; the Koka residence from {KWJ}; Tokyo courses from {TO}; the festival from {FESTA}; Naruto from {NARU} and {ANN_K}; Basilisk from {BASI}. I have not verified current prices, hours or event dates.</p>

  </article>

</main>'''

TITLE = 'Ninja Guide: Iga, Koka, Ninja Museums, Experiences and Manga'
DESC = "A licensed guide's English introduction to the ninja: Iga and Koka, the Ninja Museum of Igaryu and Koka Ninja Village, trick houses, ninja experiences, the Ninja Festa, and Naruto and Basilisk."
KEYWORDS = 'ninja, ninja guide, Iga ninja, Koka ninja, Ninja Museum of Igaryu, Iga-ryu Ninja Museum, Koka Ninja Village, ninja experience Japan, Iga Ueno Ninja Festa, Naruto, Basilisk, shinobi'
url = finish(S, TITLE, DESC, KEYWORDS, '忍', 'The <em>Ninja</em> Guide', '忍者ガイド',
             'Iga, Koka, Museums, Experiences and Manga', 'Ninja Guide', 'guide_ninja',
             'Japan+ninja+experience', main, faq_ld)
print(url)
