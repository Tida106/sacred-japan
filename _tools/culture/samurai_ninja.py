import sys
sys.path.insert(0, '/home/claude/sacred-japan/_tools/culture')
from shinobi_common import *

S = 'samurai-and-ninja'
copy_photos(S, {'sword': 'guides/okayama-castle/images/sword.jpg'})
fig = make_fig(S)

VI_SAM = viator('Japan+samurai+experience')
VI_NIN = viator('Japan+ninja+experience')

f_hero = fig('sword', 'A long sword in a gold-fitted scabbard wrapped with beaded cord lies on a clear stand, with a large gold ring at the hilt end',
             'An ornate sword on display at Okayama Castle.',
             f'Photo: Zairon, {BY4}, via Wikimedia Commons (resized)', hero=True)

faqs = [
    ("Which should I visit first, a samurai site or a ninja site?",
     "It depends on where you are. Samurai history is spread across castles and former samurai districts all over Japan, so there is usually one near your route. The ninja sites are concentrated in Iga (Mie) and Koka (Shiga), so they need a dedicated half or full day."),
    ("What is the best season for a samurai-and-ninja trip?",
     "Late spring and late summer have festivals: the Iga Ueno Ninja Festa runs from about April 1 to May 6, and the Soma Nomaoi is held at the end of July. Kakunodate's samurai houses are closed from November to early April, according to Kyuhoshi, so winter suits other places better. Always confirm dates locally."),
    ("Can I book an English-language experience?",
     "Several operators list samurai and ninja experiences in Tokyo and Kyoto. You can compare current options on Viator, and please read recent reviews, since details change. Our guides explain which museums and villages you can visit on your own."),
]
faq_html, faq_ld = faq_blocks(faqs)

main = f'''<main>

  {f_hero}

  <aside class="toc" aria-label="Table of contents">
    <div class="toc-label">TABLE OF CONTENTS ／ 目次</div>
    <div class="toc-title">In This Feature</div>
    <ol>
      <li><a href="#opening">Opening: A Note from the Guide</a></li>
      <li><a href="#glance">Samurai and Ninja at a Glance</a></li>
      <li><a href="#go">Places to Go</a></li>
      <li><a href="#do">Experiences and Festivals</a></li>
      <li><a href="#when">When to Go</a></li>
      <li><a href="#media">Manga and Anime to Read First</a></li>
      <li><a href="#faq">Frequently Asked Questions</a></li>
    </ol>
  </aside>

  <article>

    <section id="opening">
      <p class="opening">Samurai and ninja are the two figures visitors ask me about most, and they are easy to mix up.</p>
      <p>This feature puts our two full guides side by side: the {link('/culture/samurai/', 'samurai guide', 'hub_to_samurai')} and the {link('/culture/ninja/', 'ninja guide', 'hub_to_ninja')}. Use this page to choose where to go, and the guides for the history, photos and sources.</p>
    </section>

    <h2 id="glance">Samurai and Ninja at a Glance<span class="h2-jp">侍と忍者</span></h2>
    <ul>
      <li><strong>Samurai (<span class="jp">侍</span>):</strong> Japan's warrior class, which ruled for nearly 700 years and became administrators in the Edo period (1603 to 1868). The class ended in the early Meiji reforms, with a sword ban in 1876.</li>
      <li><strong>Ninja (<span class="jp">忍者</span>):</strong> covert operatives from Iga (Mie) and Koka (Shiga), prominent in the Sengoku period (1467 to 1568), working in espionage for their lords.</li>
      <li><strong>Where to see them:</strong> samurai in castles and former samurai districts across the country; ninja in two neighboring areas near Kyoto, plus a dojo in Tokyo.</li>
    </ul>

    <h2 id="go">Places to Go<span class="h2-jp">行き先</span></h2>
    <p><strong>For samurai:</strong></p>
    <ul>
      <li>Castle displays of armor and swords: {link('/guides/matsue-castle/', 'Matsue', 'hub_to_matsue')}, {link('/guides/matsuyama-castle/', 'Matsuyama', 'hub_to_matsuyama')} and {link('/guides/okayama-castle/', 'Okayama', 'hub_to_okayama')}.</li>
      <li>Samurai districts: Kakunodate, Nagamachi in Kanazawa, Chiran, Hagi, Usuki, Kitsuki, and Matsue and Tsuwano, all in the {link('/culture/samurai/#towns', 'samurai guide', 'hub_to_samurai_towns')}.</li>
      <li>More castles: {link('/guides/best-castles-japan/', 'Best Castles in Japan', 'hub_to_castles')}.</li>
    </ul>
    <p><strong>For ninja:</strong></p>
    <ul>
      <li>The Ninja Museum of Igaryu in Iga Ueno, and Koka Ninja Village and a Koka trick-house residence, with hours and admission in the {link('/culture/ninja/#visit', 'ninja guide', 'hub_to_ninja_visit')}.</li>
      <li>Iga and Koka are neighbors, and day trips from Osaka or Kyoto are possible, according to Japan's tourism organization.</li>
    </ul>

    <h2 id="do">Experiences and Festivals<span class="h2-jp">体験とお祭り</span></h2>
    <ul>
      <li><strong>Armor try-on and sword demonstration:</strong> the Samurai Museum in Shinjuku, Tokyo (a 2018 review; check current details).</li>
      <li><strong>Mounted-warrior festival:</strong> Soma Nomaoi in Minamisoma, Fukushima, at the end of July.</li>
      <li><strong>Ninja training in Tokyo:</strong> the Ninja Information Centre Tokyo &amp; Dojo in Asakusa (a 2021 report; check current courses).</li>
      <li><strong>Ninja festival:</strong> the Iga Ueno Ninja Festa, about April 1 to May 6.</li>
      <li><strong>Booked experiences:</strong> compare current {aff(VI_SAM, 'samurai experiences', 'hub_viator_samurai')} and {aff(VI_NIN, 'ninja experiences', 'hub_viator_ninja')} on Viator.</li>
    </ul>

    <h2 id="when">When to Go<span class="h2-jp">時期</span></h2>
    <ul>
      <li><strong>April 1 to May 6:</strong> Iga Ueno Ninja Festa.</li>
      <li><strong>Late July:</strong> Soma Nomaoi (last weekend of the month).</li>
      <li><strong>Winter:</strong> Kakunodate's samurai houses are closed from November to early April, so choose another district then.</li>
    </ul>
    <p>These dates come from the sources listed in each guide and can change, so please confirm with the organizers.</p>

    <h2 id="media">Manga and Anime to Read First<span class="h2-jp">漫画・アニメ</span></h2>
    <ul>
      <li><strong>Naruto</strong> (Masashi Kishimoto, 1999 to 2014): an outcast ninja who wants to become Hokage. See the {link('/culture/ninja/#media', 'ninja guide', 'hub_media_naruto')}.</li>
      <li><strong>Basilisk</strong> (from Futaro Yamada's 1959 novel): the Iga and Kouga clans fight over the Tokugawa succession. See the {link('/culture/ninja/#media', 'ninja guide', 'hub_media_basilisk')}.</li>
      <li><strong>Rurouni Kenshin</strong> (Nobuhiro Watsuki, from 1994): a wandering former assassin in 1878. See the {link('/culture/samurai/#media', 'samurai guide', 'hub_media_kenshin')}.</li>
      <li><strong>Vagabond</strong> (Takehiko Inoue, from 1998): the life of the swordsman Miyamoto Musashi. See the {link('/culture/samurai/#media', 'samurai guide', 'hub_media_vagabond')}.</li>
    </ul>
    <p>More series with real locations are in our {link('/anime/', 'anime pilgrimage hub', 'hub_to_anime')}.</p>

    <h2 id="faq">Frequently Asked Questions<span class="h2-jp">よくあるご質問</span></h2>

    <div class="faq-stack">

{faq_html}    </div>

    <div class="closing-block">
      <span class="torii">⚔️</span>
      <p>Two worlds, one trip.</p>
    </div>

    <section class="related-section">
      <h2>Related Guides</h2>
      <span class="h2-jp">関連ガイド</span>
      <div class="related-grid">
        <a class="related-card" href="/culture/samurai/" onclick="trackEvent('click','internal','related_hub_to_samurai')">
          <div class="related-card-label">SACRED JAPAN ／ GUIDE</div>
          <div class="related-card-title">⚔️ Samurai Guide →</div>
          <div class="related-card-desc">History, armor, samurai towns and festivals.</div>
        </a>
        <a class="related-card" href="/culture/ninja/" onclick="trackEvent('click','internal','related_hub_to_ninja')">
          <div class="related-card-label">SACRED JAPAN ／ GUIDE</div>
          <div class="related-card-title">🥷 Ninja Guide →</div>
          <div class="related-card-desc">Iga and Koka, museums, a festival and the manga.</div>
        </a>
        <a class="related-card" href="/guides/best-castles-japan/" onclick="trackEvent('click','internal','related_hub_to_castles')">
          <div class="related-card-label">SACRED JAPAN ／ GUIDE</div>
          <div class="related-card-title">🏯 Best Castles in Japan →</div>
          <div class="related-card-desc">Original keeps and where to see them.</div>
        </a>
        <a class="related-card" href="/anime/" onclick="trackEvent('click','internal','related_hub_to_anime')">
          <div class="related-card-label">SACRED JAPAN ／ HUB</div>
          <div class="related-card-title">🎬 Anime Pilgrimage →</div>
          <div class="related-card-desc">Real places behind favorite series.</div>
        </a>
      </div>
    </section>

    <p style="font-size:14px;color:var(--enshu);line-height:1.7;margin-top:32px;"><strong>Sources:</strong> see the sources lists in our {link('/culture/samurai/', 'samurai guide', 'hub_src_samurai')} and {link('/culture/ninja/', 'ninja guide', 'hub_src_ninja')}. I have not verified current prices, hours or event dates.</p>

  </article>

</main>'''

TITLE = 'Samurai and Ninja in Japan: Where to Go, What to Do and Manga to Read'
DESC = "A licensed guide's English feature on samurai and ninja: where to see them, experiences and festivals, when to go, and the manga and anime to read first, with links to our full guides."
KEYWORDS = 'samurai and ninja, samurai ninja Japan, ninja museum, samurai museum, Iga, Koka, Soma Nomaoi, ninja experience Japan, samurai experience Japan, Naruto, Rurouni Kenshin, Basilisk, Vagabond'
url = finish(S, TITLE, DESC, KEYWORDS, '侍忍', '<em>Samurai</em> &amp; <em>Ninja</em> in Japan', '侍と忍者',
             'Where to Go, What to Do and What to Read', 'Samurai and Ninja Feature', 'guide_samurai_ninja',
             'Japan+ninja+experience', main, faq_ld)
print(url)
