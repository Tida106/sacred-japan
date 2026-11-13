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

CSS = """<style>
.sn-h{font-family:inherit;margin:0 0 4px;font-size:30px;line-height:1.2}
.sn-sub{margin:0 0 20px;color:var(--enshu);font-size:14px;letter-spacing:.08em}
.sn-grid{display:grid;gap:18px;margin:0 0 44px}
.sn-grid.two{grid-template-columns:1fr 1fr}
.sn-grid.three{grid-template-columns:repeat(3,1fr)}
.sn-card{position:relative;display:block;overflow:hidden;border-radius:6px;border:2px solid #c9971c;background:#2a1a1a;text-decoration:none;color:#fff;box-shadow:0 3px 12px rgba(80,40,20,.25);transition:transform .2s,box-shadow .2s}
.sn-card:hover{transform:translateY(-3px);box-shadow:0 8px 20px rgba(80,40,20,.35)}
.sn-card .ph{aspect-ratio:4/3;overflow:hidden}
.sn-card.big .ph{aspect-ratio:16/11}
.sn-card .ph img{width:100%;height:100%;object-fit:cover;display:block;transition:transform .4s}
.sn-card:hover .ph img{transform:scale(1.05)}
.sn-card .ov{position:absolute;left:0;right:0;bottom:0;padding:48px 18px 16px;background:linear-gradient(to top,rgba(20,8,8,.92) 0%,rgba(20,8,8,.6) 55%,rgba(20,8,8,0) 100%)}
.sn-card .kj{display:block;font-size:13px;letter-spacing:.3em;color:#f3d77c}
.sn-card .tt{display:block;font-size:26px;font-weight:700;line-height:1.2;margin:2px 0 4px;color:#fff;font-family:'Lora',serif}
.sn-card.big .tt{font-size:32px}
.sn-card .ds{display:block;font-size:14px;line-height:1.45;color:#f3e8dc;margin-bottom:10px}
.sn-btn{display:inline-block;padding:8px 16px;background:linear-gradient(135deg,#f9e9a8 0%,#e6c45a 28%,#c9971c 52%,#f3d77c 78%,#d6a92b 100%);color:#1a1a1a;font-weight:700;font-size:15px;border-radius:3px;border:1px solid #b8860b;box-shadow:inset 0 1px 0 rgba(255,255,255,.7);text-shadow:0 1px 0 rgba(255,245,200,.6)}
.sn-card.kanji{background:linear-gradient(135deg,#7a1f2b,#3b1020);min-height:100%}
.sn-card.kanji .bgk{position:absolute;right:10px;top:-8px;font-size:130px;color:rgba(243,215,124,.18);line-height:1}
.sn-card.kanji .ov{position:relative;background:none;padding:36px 18px 18px}
.sn-note{font-size:12px;color:var(--enshu);margin:-30px 0 40px;text-align:right}
@media(max-width:780px){.sn-grid.two,.sn-grid.three{grid-template-columns:1fr}.sn-card .ph,.sn-card.big .ph{aspect-ratio:16/10}.sn-card.big .tt{font-size:28px}}
</style>"""

def card(href, img, kj, title, desc, btn, lab, big=False, aff_=False, alt=''):
    rel = ' target="_blank" rel="noopener sponsored"' if aff_ else ''
    kind = 'affiliate' if aff_ else 'internal'
    return f"""<a class="sn-card{' big' if big else ''}" href="{href}"{rel} onclick="trackEvent('click','{kind}','{lab}')">
        <div class="ph"><picture><source srcset="{img}.webp" type="image/webp"><img src="{img}.jpg" alt="{alt}" loading="lazy"></picture></div>
        <div class="ov"><span class="kj">{kj}</span><span class="tt">{title}</span><span class="ds">{desc}</span><span class="sn-btn">{btn}</span></div>
      </a>"""

cards_html = CSS + f"""
  <h2 class="sn-h" id="start">Start Here</h2>
  <p class="sn-sub">侍と忍者 ／ PICK YOUR PATH</p>
  <div class="sn-grid two">
      {card('/culture/samurai/','/images/hub/samurai','侍','Samurai Guide','Armor, swords, samurai towns and the festival where riders still gallop.','Read the Samurai Guide →','hub_card_samurai',True,alt='Samurai armor on display')}
      {card('/culture/ninja/','/images/hub/ninja','忍者','Ninja Guide','Iga and Koka, trick houses, real tools and a festival.','Read the Ninja Guide →','hub_card_ninja',True,alt='A ninja house in Iga')}
  </div>

  <h2 class="sn-h">Try It Yourself</h2>
  <p class="sn-sub">体験 ／ BOOK AN EXPERIENCE</p>
  <div class="sn-grid three">
      {card(vtour('Kyoto/Small-Group-Samurai-Experience-in-Kyoto/d332-44484P1'),'/culture/samurai/images/armor-red','KYOTO','Samurai Experience','Small-group samurai session in Kyoto.','Check Dates on Viator →','hub_card_viator_kyoto',aff_=True,alt='Red samurai armor')}
      {card(vtour('Kyoto/Samurai-Experience-and-Guided-Tour-of-Samurai-Ninja-Museum/d332-51440P80'),'/culture/samurai/images/sword','TOKYO','Samurai Ninja Museum','Guided tour of the museum in Asakusa.','Check Dates on Viator →','hub_card_viator_tokyo',aff_=True,alt='A sword on display')}
      {card(VI_NIN,'/culture/ninja/images/shuriken','NINJA','Ninja Experiences','Compare current ninja activities on Viator.','See All Options →','hub_card_viator_ninja',aff_=True,alt='Shuriken throwing stars')}
  </div>
  <p class="sn-note">Photos are illustrative; credits are on the full guides. I have not tried these tours myself, so please read each listing.</p>

  <h2 class="sn-h">Keep Exploring</h2>
  <p class="sn-sub">もっと ／ CASTLES, ANIME AND THE NARUTO VILLAGE</p>
  <div class="sn-grid three">
      {card('/guides/best-castles-japan/','/images/hub/best-castles-japan','城','Best Castles in Japan','30 castles in photos, ranked.','See the Castles →','hub_card_castles',alt='Japanese castle')}
      {card('/anime/','/images/hub/culture-anime','聖地','Anime Pilgrimage','Real places behind favorite series.','Explore the Hub →','hub_card_anime',alt='Anime pilgrimage location')}
      <a class="sn-card kanji" href="/culture/nijigen-no-mori/" onclick="trackEvent('click','internal','hub_card_nijigen')"><span class="bgk">忍</span><div class="ov"><span class="kj">NARUTO × BORUTO</span><span class="tt">Nijigen no Mori</span><span class="ds">Walk through the Shinobi village on Awaji Island.</span><span class="sn-btn">Visit the Village →</span></div></a>
  </div>
"""

main = f'''<main>

  {cards_html}

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
      <li><strong>NARUTO x BORUTO village:</strong> Shinobi-zato at Nijigen no Mori on Awaji Island, with tickets, rules and access in our {link('/culture/nijigen-no-mori/', 'Nijigen no Mori guide', 'hub_to_nijigen')}.</li>
      <li><strong>Booked experiences:</strong> try a {aff(vtour('Kyoto/Small-Group-Samurai-Experience-in-Kyoto/d332-44484P1'), 'small-group samurai experience in Kyoto', 'hub_viator_kyoto_samurai')} or the {aff(vtour('Kyoto/Samurai-Experience-and-Guided-Tour-of-Samurai-Ninja-Museum/d332-51440P80'), 'Samurai Ninja Museum in Asakusa, Tokyo', 'hub_viator_tokyo_museum')}, or compare all {aff(VI_SAM, 'samurai experiences', 'hub_viator_samurai')} and {aff(VI_NIN, 'ninja experiences', 'hub_viator_ninja')} on Viator. I have not tried these myself, so please check each listing.</li>
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
      <li><strong>Naruto</strong> (Masashi Kishimoto, 1999 to 2014): an outcast ninja who wants to become Hokage. See the {link('/culture/ninja/#media', 'ninja guide', 'hub_media_naruto')}, and visit its village at {link('/culture/nijigen-no-mori/', 'Nijigen no Mori', 'hub_media_naruto_nijigen')}.</li>
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
