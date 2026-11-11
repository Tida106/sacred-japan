import sys
sys.path.insert(0, '/home/claude/sacred-japan/_tools/culture')
from shinobi_common import *

S = 'samurai'
copy_photos(S, {
    'armor-case': 'guides/matsue-castle/images/armor-case.jpg',
    'armor-kato': 'guides/matsuyama-castle/images/armor-kato.jpg',
    'armor-red': 'guides/okayama-castle/images/armour-red.jpg',
    'helmet-horned': 'guides/matsue-castle/images/helmet-horned.jpg',
    'sword': 'guides/okayama-castle/images/sword.jpg',
    'shiomi-nawate': 'guides/matsue-castle/images/shiomi-nawate.jpg',
})
fig = make_fig(S)

TC = ext('https://www.thecollector.com/why-japan-abolished-the-samurai/', 'The Collector', 'samurai_src_collector')
KY = ext('https://www.kyuhoshi.com/samurai-districts-in-japan', 'Kyuhoshi', 'samurai_src_kyuhoshi')
CAF = ext('https://www.travelcaffeine.com/?p=5906', 'Travel Caffeine', 'samurai_src_travelcaffeine')
SOMA = ext('https://www.nippon.com/en/guide-to-japan/gu008005/fukushima%E2%80%99s-soma-nomaoi-a-thrilling-festival-of-mounted-samurai.html', 'Nippon.com', 'samurai_src_nippon_soma')
JT = ext('https://japantimes.co.jp/culture/2017/01/07/books/book-reviews/vagabond-epic-manga-based-life-17th-century-samurai', 'The Japan Times', 'samurai_src_japantimes')
SHIN = ext('https://shinsengumijapan.com/en/2021/05/02/rurounikenshin_1/', 'Shinsengumi Japan', 'samurai_src_shinsengumi')
VI_SAM = viator('Japan+samurai+experience')

f_hero = fig('armor-case', 'A suit of dark armor with gold-and-black lacing and a crested helmet stands in a glass case beside a stand of arrows, a long bow and smaller armor pieces',
             'Armor, arrows and a bow in a display case at Matsue Castle.',
             f'Photo: 江戸村のとくぞう, {BYSA4}, September 2015. {VIA}', hero=True)
f_kato = fig('armor-kato', 'A dark suit of armor with a flat black helmet topped by two long, curved bird feathers stands in a lit case between two information panels',
             'Armor and helmet said to have belonged to Kato Yoshiaki, founder of Matsuyama Castle.',
             f'Photo: Zairon, {BY4}, via Wikimedia Commons (resized). The label says "said to have belonged," so the attribution is the museum\'s, not a certainty.', maxw=480)
f_red = fig('armor-red', 'A suit of armor with bright red lacing, a black helmet and a large gold crescent ornament stands against a painted battle screen',
            'A red-laced armor on display at Okayama Castle.',
            f'Photo: Zairon, {BY4}, via Wikimedia Commons (resized)', maxw=460)
f_helm = fig('helmet-horned', 'A dark helmet with a fierce face ornament, two long horns and fan-shaped side pieces sits on a black lacquered box draped with purple cloth',
             'A helmet with a fierce ornament and two horns, Matsue Castle.',
             f'Photo: G41rn8, {BYSA4}, October 2016. {VIA}', maxw=420)
f_sword = fig('sword', 'A long sword in a gold-fitted scabbard wrapped with beaded cord lies on a clear stand, with a large gold ring at the hilt end',
              'An ornate sword on display at Okayama Castle.',
              f'Photo: Zairon, {BY4}, via Wikimedia Commons (resized)', maxw=780)
f_town = fig('shiomi-nawate', 'A quiet road beside a long white-and-dark-wood wall of old houses, with large pine trees at left and two visitors looking up at the right',
             'Shiomi Nawate, the old samurai street along the moat in Matsue.',
             f'Photo: 663highland, {BYSA3}, March 2015. {VIA}', maxw=760)

faqs = [
    ("When did the samurai era end?",
     "Over several steps in the early Meiji period. According to The Collector, the han (domain) system was abolished in 1871, a conscription law of 1873 made military service a duty for all healthy men regardless of class, and an edict of 1876 banned carrying swords in public. I have only this one source for the sequence, so please check a second one if you need exact dates."),
    ("Where can I see real samurai armor and swords?",
     "Many castle keeps display them. On this site, the Matsue, Matsuyama and Okayama castle guides show armor, helmets and a sword from their collections. Labels often say \"said to have belonged to\" a particular lord, which is the museum's attribution."),
    ("Are the armor and swords at the Samurai Museum in Shinjuku real?",
     "A 2018 Travel Caffeine review says the armor, helmets and swords are mostly reproductions modeled on Kamakura and Edo period originals. Collections change, so please check the museum's current information before you go."),
    ("Where can I walk through a former samurai district?",
     "Kyuhoshi lists Kakunodate, Nagamachi in Kanazawa, Chiran, Hagi, Usuki, Kitsuki, and Matsue and Tsuwano. Kakunodate's houses are closed from November to early April, according to that article, so season matters."),
    ("Can visitors watch a samurai event?",
     "The Soma Nomaoi in Minamisoma, Fukushima, is a three-day mounted-warrior festival held at the end of July. Nippon.com's 2018 article says tickets were needed only on the second day (¥1,000 same-day, ¥800 in advance). Please check the organizing committee for current details."),
    ("Are samurai and ninja the same thing?",
     "No. Samurai were the warrior class. Ninja, covered in our ninja guide, were covert operatives associated with the Iga and Koka regions during the Sengoku period, and the two overlapped less than pop culture suggests."),
]
faq_html, faq_ld = faq_blocks(faqs)

main = f'''<main>

  {f_hero}

  <aside class="toc" aria-label="Table of contents">
    <div class="toc-label">TABLE OF CONTENTS ／ 目次</div>
    <div class="toc-title">In This Guide</div>
    <ol>
      <li><a href="#opening">Opening: A Note from the Guide</a></li>
      <li><a href="#who">Who the Samurai Were</a></li>
      <li><a href="#end">How the Samurai Era Ended</a></li>
      <li><a href="#armor">Armor and Swords</a></li>
      <li><a href="#towns">Samurai Towns to Walk Through</a></li>
      <li><a href="#experiences">Experiences and Festivals</a></li>
      <li><a href="#media">Samurai in Manga and Anime</a></li>
      <li><a href="#faq">Frequently Asked Questions</a></li>
      <li><a href="#final">Final Thoughts</a></li>
    </ol>
  </aside>

  <article>

    <section id="opening">
      <p class="opening">Most visitors meet the samurai in a castle keep, in front of a glass case with a helmet and a handwritten label they cannot read.</p>
      <p>As a licensed guide, I find that a short history, a few things to look for in the armor, and a list of places where the samurai world is still easy to walk through make that glass case much more interesting. This guide gives you those three things, and it says where I am relying on a single source. For the covert side of the story, see our {link('/culture/ninja/', 'ninja guide', 'samurai_to_ninja')}.</p>
    </section>

    <h2 id="who">Who the Samurai Were<span class="h2-jp">侍とは</span></h2>
    <p>Samurai (<span class="jp">侍</span>) were Japan's warrior class. {TC} says they ruled Japan for nearly 700 years and shaped its politics, economy and moral thinking, which is why they are never far from any Japanese history.</p>
    <p>The Edo period (1603 to 1868) changed their job. The same article says the Tokugawa shogunate brought about two centuries of internal stability, and that by the mid-1600s samurai had moved from battlefield commanders to administrators. It puts the samurai class at roughly 2 million people, many of them living on fixed rice stipends from their lords and often poor. That is a useful corrective to the image of a sword in every hand: in the Edo period, many samurai were closer to salaried officials.</p>

    <h2 id="end">How the Samurai Era Ended<span class="h2-jp">侍の終わり</span></h2>
    <p>According to {TC}, the ending came in a few legal steps:</p>
    <ul>
      <li><strong>1871:</strong> the han system was abolished, and the daimyo became salaried officials instead of rulers.</li>
      <li><strong>Early 1870s:</strong> samurai stipends were taking close to half of national tax revenue, so the government stopped funding former samurai who lacked modern skills.</li>
      <li><strong>1873:</strong> a conscription law, passed on January 10, required healthy men of every status to serve, ending the warrior class's monopoly on fighting.</li>
      <li><strong>1876:</strong> the Haitorei edict banned carrying swords in public, which the article calls a major blow because the blade was considered sacred to samurai. It says the ban set off several armed uprisings, mainly around Satsuma.</li>
    </ul>
    <p>I have only this one source for the sequence, so if you need exact dates for a school paper or a talk, please check a second one.</p>

    <h2 id="armor">Armor and Swords<span class="h2-jp">甲冑と刀</span></h2>
    <p>A castle is the easiest place to see the gear. The pieces on this page come from three of our castle guides, and I describe only what the photos show.</p>

    {f_red}
    <p>This red-laced armor from Okayama Castle is the kind of piece that reads as "samurai" at a glance: a gold crescent rises from a black helmet, and the cords on the chest and skirt are a deep orange-red. Behind it is a painted screen of a battle with banners.</p>

    {f_kato}
    <p>This armor at Matsuyama Castle is described on its label as having belonged to the castle's founder, Kato Yoshiaki. It is much darker and plainer than the red piece. The flat black helmet carries two long, curved feathers, and the case is flanked by panels telling the lord's story in Japanese and English.</p>

    {f_helm}
    <p>Helmets are where makers had the most freedom. This one from Matsue Castle has a fierce face ornament, two horns and fan-shaped side pieces, and it sits on a lacquered box with a purple cloth. I would look for the helmet first in any display, because it often carries the owner's personality.</p>

    {f_sword}
    <p>This sword at Okayama Castle sits in a scabbard fitted with gold, wrapped in beaded cord, with a large ring at the hilt end. I cannot read its label with confidence from the photo, so I will not give its age or owner. In Japanese museums the displayed blade is often in its mounting, so the fittings may be the part that catches your eye.</p>

    <p>For more cases like these, see our {link('/guides/matsue-castle/', 'Matsue Castle', 'samurai_to_matsue')}, {link('/guides/matsuyama-castle/', 'Matsuyama Castle', 'samurai_to_matsuyama')} and {link('/guides/okayama-castle/', 'Okayama Castle', 'samurai_to_okayama')} guides, or the overview in {link('/guides/best-castles-japan/', 'Best Castles in Japan', 'samurai_to_best_castles')}.</p>

    <h2 id="towns">Samurai Towns to Walk Through<span class="h2-jp">武家屋敷</span></h2>
    <p>A castle shows you the lord; the districts around it show you where his retainers lived. {KY} lists these:</p>
    <ul>
      <li><strong>Kakunodate (Akita):</strong> about 80 samurai families once lived here, and several residences can be entered. The article says the houses are closed from November to early April.</li>
      <li><strong>Nagamachi (Kanazawa):</strong> earthen walls, canals and narrow lanes near the castle. The Nomura Residence is open to visitors, and the article lists a 500-yen museum and a free one.</li>
      <li><strong>Chiran (Kagoshima):</strong> seven garden-fronted samurai houses, with about 500 samurai families once living here, a 500-yen ticket for all seven gardens, and daily hours of 9:00 to 17:00 according to the article.</li>
      <li><strong>Hagi (Yamaguchi):</strong> a former castle town where many samurai turned to trade; the castle ruins and Kikuya Residence are the sights named.</li>
      <li><strong>Usuki and Kitsuki (Oita):</strong> a stone-paved lane in Usuki, and in Kitsuki a slope lined with samurai houses and a kimono rental at a former residence.</li>
      <li><strong>Matsue and Tsuwano (Shimane):</strong> Shiomi Nawate, a 500-meter street along the castle moat in Matsue, plus Matsue Buke Yashiki, and the Tonomachi district in Tsuwano.</li>
    </ul>

    {f_town}
    <p>This is Shiomi Nawate, the street along the moat in Matsue. A long wall of old houses runs along the right, pines lean over the road at left, and two visitors stand looking up at a roof. It is a quiet street, which is exactly how I would recommend taking it. Admission figures in the Kyuhoshi article are undated, so please check each site before you go.</p>
    <p>Hagi has its own guide here: {link('/guides/hagi-castle/', 'Hagi Castle', 'samurai_to_hagi')}, and so does {link('/guides/kanazawa-castle/', 'Kanazawa Castle', 'samurai_to_kanazawa')}, which sits beside Nagamachi.</p>

    <h2 id="experiences">Experiences and Festivals<span class="h2-jp">体験とお祭り</span></h2>
    <p>If you would rather do than look, there are three kinds of experience.</p>
    <ul>
      <li><strong>The Samurai Museum, Shinjuku (Tokyo).</strong> A 2018 {CAF} review places it in Kabukicho, with a 45-minute guided tour of about 700 years of history, a sword demonstration and an armor try-on, and an admission of 1,800 yen at the time. It adds that most of the armor and swords are reproductions. That review is old, so check the museum's current prices and programs.</li>
      <li><strong>Soma Nomaoi (Minamisoma, Fukushima).</strong> {SOMA} describes a three-day festival held on the last weekend of July, with about 500 riders in warrior dress, an armed horse race and a sacred-flag contest that is the climax. It says the festival is designated an Important Intangible Folk Cultural Property and that tickets were required only on the second day in 2018.</li>
      <li><strong>Guided samurai experiences.</strong> Several operators run sword and armor sessions in Tokyo and Kyoto. If you want a booked, English-language option, you can compare current {aff(VI_SAM, 'samurai experiences on Viator', 'samurai_viator_experience')}; I have not tested any of them myself, so please read the reviews.</li>
    </ul>

    <h2 id="media">Samurai in Manga and Anime<span class="h2-jp">漫画・アニメ</span></h2>
    <p>Two series make good companions for a trip, because each is anchored in a real period.</p>
    <p><strong>Rurouni Kenshin</strong> by Nobuhiro Watsuki began in <em>Weekly Shonen Jump</em> in 1994. {SHIN} says the story is set in 1878, the 11th year of Meiji, which places it in the years just after the 1876 sword ban described above. The protagonist, Himura Kenshin, is a former assassin who served the Choshu domain and now wanders with a reverse-blade sword, and the real Shinsengumi captain Saito Hajime appears under his historical identity. It is a good way to see why the end of the samurai era still moves Japanese readers.</p>
    <p><strong>Vagabond</strong> by Takehiko Inoue, the creator of <em>Slam Dunk</em>, is based on the life of the 17th-century swordsman Miyamoto Musashi and on Eiji Yoshikawa's 1935 novel <em>Musashi</em>. {JT} says it began in 1998 and runs to 37 volumes, with more than 80 million copies sold and translations into at least 12 languages. Musashi's Edo-period world is a long way from the warlords of the earlier centuries.</p>
    <p>For the ninja side, including <em>Naruto</em> and <em>Basilisk</em>, see our {link('/culture/ninja/', 'ninja guide', 'samurai_media_to_ninja')}. For other series with real-world locations, our {link('/anime/', 'anime pilgrimage hub', 'samurai_to_anime')} has more.</p>

    <h2 id="faq">Frequently Asked Questions<span class="h2-jp">よくあるご質問</span></h2>

    <div class="faq-stack">

{faq_html}    </div>

    <h2 id="final">Final Thoughts<span class="h2-jp">むすびに</span></h2>
    <p>Start with the glass case at a castle, then add a district such as Nagamachi or Shiomi Nawate, and if your dates match, the end of July in Fukushima. The labels will mean more once you know the Edo period turned warriors into officials and the Meiji reforms ended the class in a few years.</p>

    <div class="closing-block">
      <span class="torii">⚔️</span>
      <p>A helmet, a quiet street and a story with a long ending.</p>
    </div>

    <section class="related-section">
      <h2>Related Guides</h2>
      <span class="h2-jp">関連ガイド</span>
      <div class="related-grid">
        <a class="related-card" href="/culture/ninja/" onclick="trackEvent('click','internal','related_samurai_to_ninja')">
          <div class="related-card-label">SACRED JAPAN ／ GUIDE</div>
          <div class="related-card-title">🥷 Ninja Guide →</div>
          <div class="related-card-desc">Iga and Koka, museums, a festival and the manga behind the myth.</div>
        </a>
        <a class="related-card" href="/guides/best-castles-japan/" onclick="trackEvent('click','internal','related_samurai_to_castles')">
          <div class="related-card-label">SACRED JAPAN ／ GUIDE</div>
          <div class="related-card-title">🏯 Best Castles in Japan →</div>
          <div class="related-card-desc">Original keeps and where to see them.</div>
        </a>
        <a class="related-card" href="/guides/matsue-castle/" onclick="trackEvent('click','internal','related_samurai_to_matsue')">
          <div class="related-card-label">SACRED JAPAN ／ GUIDE</div>
          <div class="related-card-title">Matsue Castle →</div>
          <div class="related-card-desc">Armor, helmets and the moat-side samurai street.</div>
        </a>
        <a class="related-card" href="/culture/samurai-and-ninja/" onclick="trackEvent('click','internal','related_samurai_to_hub')">
          <div class="related-card-label">SACRED JAPAN ／ FEATURE</div>
          <div class="related-card-title">⚔️ Samurai &amp; Ninja Feature →</div>
          <div class="related-card-desc">Both guides, side by side, with places and events.</div>
        </a>
      </div>
    </section>

    <p style="font-size:14px;color:var(--enshu);line-height:1.7;margin-top:32px;"><strong>Sources:</strong> history and the Meiji reforms from {TC}; samurai districts from {KY}; the Samurai Museum from {CAF}; Soma Nomaoi from {SOMA}; Rurouni Kenshin from {SHIN}; Vagabond from {JT}. Photograph details come from the Wikimedia Commons descriptions and from the museum labels visible in the photos. I have not verified current prices, hours or event dates.</p>

  </article>

</main>'''

TITLE = 'Samurai Guide: History, Armor, Samurai Towns and Experiences in Japan'
DESC = "A licensed guide's English introduction to the samurai: who they were, how the era ended, armor and swords to see in castles, former samurai districts to walk through, and experiences such as the Soma Nomaoi."
KEYWORDS = 'samurai, samurai guide, samurai history, samurai armor, samurai sword, samurai district, Kakunodate, Nagamachi, Soma Nomaoi, samurai museum Tokyo, Rurouni Kenshin, Vagabond, Edo period'
url = finish(S, TITLE, DESC, KEYWORDS, '侍', 'The <em>Samurai</em> Guide', '侍ガイド',
             'History, Armor, Samurai Towns and Experiences', 'Samurai Guide', 'guide_samurai',
             'Japan+samurai+experience', main, faq_ld)
print(url)
