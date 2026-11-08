import re, os, json
from PIL import Image
R='/home/claude/sacred-japan'
A='/mnt/user-data/attachments/fd332c08-3f6b-545a-883b-83277e19ff52/'
S='ramen'
OUT=f'{R}/culture/{S}'
os.makedirs(OUT+'/images',exist_ok=True)
photos={'shoyu-tsugaru':('8497ba38-image.jpg',1200),'miso-sapporo':('08fa4957-image.jpg',1000),'shio-bowl':('e86c8936-image.jpg',1000),'tonkotsu-bowl':('006bb829-image.jpg',1024)}
for k,(f,mw) in photos.items():
    im=Image.open(A+f).convert('RGB');w,h=im.size
    if w>mw: im=im.resize((mw,round(h*mw/w)),Image.LANCZOS)
    im.save(f'{OUT}/images/{k}.jpg',quality=84,optimize=True); im.save(f'{OUT}/images/{k}.webp',quality=80)
def fig(k,alt,cap,credit,hero=False,maxw=760):
    st='margin:0 0 48px;' if hero else f'margin:36px auto;max-width:{maxw}px;'
    img_st='width:100%;max-height:420px;object-fit:cover;border-radius:4px;display:block;' if hero else 'width:100%;height:auto;border-radius:4px;display:block;'
    ld='eager' if hero else 'lazy'
    return f'''<figure style="{st}">
      <picture><source srcset="/culture/{S}/images/{k}.webp" type="image/webp"><img src="/culture/{S}/images/{k}.jpg" alt="{alt}" loading="{ld}" style="{img_st}"></picture>
      <figcaption style="font-size:13px;color:var(--enshu);margin-top:10px;text-align:center;line-height:1.6;">{cap}<br>{credit}</figcaption>
    </figure>'''
CC0='<a href="https://creativecommons.org/publicdomain/zero/1.0/" target="_blank" rel="noopener" style="color:var(--enshu);">CC0</a>'
BYSA2='<a href="https://creativecommons.org/licenses/by-sa/2.0/" target="_blank" rel="noopener" style="color:var(--enshu);">CC BY-SA 2.0</a>'
VIA='via Wikimedia Commons (resized)'
f_shoyu=fig('shoyu-tsugaru','A white bowl of clear brown-soy ramen with thin curly noodles, bamboo shoots, a slice of pork, chopped scallions and a white fish cake with a pink swirl, with a white plastic spoon, on a light wooden table','Shoyu ramen: Tsugaru ramen at a shop in Aomori, northern Honshu.',f'Photo: Ocdp, {CC0}, 31 August 2020, {VIA}',hero=True)
f_miso=fig('miso-sapporo','A white bowl printed with Sapporo Ramen in blue brush lettering holding cloudy orange-brown miso ramen topped with a pile of shredded white leek, a thick slice of pork, bamboo shoots and dark green strands, with a black spoon, on a dark wooden table','Miso ramen in a bowl printed with the name of a Sapporo ramen shop.',f'Photo: 毒島みるく, {CC0}, 20 November 2019, {VIA}',maxw=640)
f_shio=fig('shio-bowl','A large white bowl with a blue-and-yellow floral border holding pale, clear shio ramen with bamboo shoots, sliced pork, a halved soft egg with an orange yolk and a pile of dark green leaves, with a white spoon, on an orange wooden table','Shio ramen: a pale, clear broth with a soft egg.',f'Photo: 毒島みるく, {CC0}, 24 January 2019, {VIA}',maxw=640)
f_tonk=fig('tonkotsu-bowl','A white bowl with a thin blue rim holding cloudy tan tonkotsu ramen with thin noodles, a slice of pork, a sheet of nori leaning against the rim, chopped scallions, sesame seeds and half a soft egg','Tonkotsu ramen with thin noodles, nori and sesame.',f'Photo: Charles Haynes, {BYSA2}, 15 February 2014 (Flickr, license reviewed on Commons), {VIA}' if False else f'Photo: Charles Haynes, {BYSA2}, 15 February 2014, {VIA}')

def link(href,txt,lab): return f'<a href="{href}" class="inline-link" onclick="trackEvent(\'click\',\'internal\',\'{lab}\')">{txt}</a>'
def ext(href,txt,lab): return f'<a href="{href}" target="_blank" rel="noopener" onclick="trackEvent(\'click\',\'external\',\'{lab}\')">{txt}</a>'
VI='https://www.viator.com/search/Japan+ramen+food+tour?pid=P00298374&amp;mcid=42383&amp;medium=link&amp;campaign=sacred-japan'
faqs=[
("What are the four main types of ramen?","The four you will see on almost every menu are shoyu (soy sauce), miso (fermented soybean paste), shio (salt) and tonkotsu (pork bone). The name usually describes the seasoning or the broth, and the same shop may offer more than one."),
("Which ramen should I try first?","If you want the most familiar, balanced taste, start with shoyu. If you are cold and hungry, try miso. If you like a light, clear broth, try shio. If you want the richest bowl, try tonkotsu."),
("Is it rude to slurp ramen?","No. Slurping is common in ramen shops, and it also cools the noodles as you eat. Eat soon after the bowl arrives, because the noodles keep softening in the hot broth."),
("Is ramen vegetarian?","Usually not. The broths are typically made from pork bones, chicken or fish, and toppings often include pork. If you do not eat meat or fish, ask the shop before you order, and check the menu for a dedicated vegetarian bowl."),
("How much does a bowl of ramen cost?","Prices vary by shop and city and change over time. As one example, the Sapporo miso ramen photographed for this guide was listed at 850 yen in 2019. Check the menu or ticket machine at the shop."),
]
faq_html=''.join(f'''      <details class="faq-item">
        <summary>{q}</summary>
        <div class="faq-answer">{a}</div>
      </details>

''' for q,a in faqs)
faq_ld=json.dumps({"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in faqs]},ensure_ascii=False,indent=2)
TITLE="Japanese Ramen Guide: Shoyu, Miso, Shio and Tonkotsu Explained"
DESC="A licensed guide's English introduction to the four main types of Japanese ramen, shoyu, miso, shio and tonkotsu, with a photograph of each bowl, where each style is known, and simple tips for ordering."
URL=f"https://sacred-japan.net/culture/{S}/"
OG="https://sacred-japan.net/images/og/og-culture-ramen.jpg"
MICH=ext('https://guide.michelin.com/en/article/features/ramen-types-guide-origin','Michelin Guide','ramen_michelin')
NIP=ext('https://www.nippon.com/en/articles/-/13802','Nippon.com','ramen_nippon')

main=f'''<main>

  {f_shoyu}

  <aside class="toc" aria-label="Table of contents">
    <div class="toc-label">TABLE OF CONTENTS ／ 目次</div>
    <div class="toc-title">In This Guide</div>
    <ol>
      <li><a href="#opening">Opening: A Note from the Guide</a></li>
      <li><a href="#four">The Four Types at a Glance</a></li>
      <li><a href="#shoyu">Shoyu: The Classic</a></li>
      <li><a href="#miso">Miso: Rich and Warming</a></li>
      <li><a href="#shio">Shio: Light and Clear</a></li>
      <li><a href="#tonkotsu">Tonkotsu: The Richest Bowl</a></li>
      <li><a href="#order">How to Order and Eat</a></li>
      <li><a href="#faq">Frequently Asked Questions</a></li>
      <li><a href="#final">Final Thoughts</a></li>
    </ol>
  </aside>

  <article>

    <section id="opening">
      <p class="opening">Almost every traveler I guide asks me the same thing sooner or later: where should I eat ramen? My honest answer begins with a question of my own: what taste do you want?</p>
      <p>As a licensed guide, I find that the easiest way into ramen is by taste. Menus in Japan are organized that way, and once you know four words, shoyu, miso, shio and tonkotsu, you can read almost any ramen menu. This guide goes through each one with a photograph of a real bowl.</p>
    </section>

    <h2 id="four">The Four Types at a Glance<span class="h2-jp">ラーメンの四つの味</span></h2>
    <ul>
      <li><strong>Shoyu (<span class="jp">醤油</span>):</strong> soy sauce seasoning. The classic, balanced taste.</li>
      <li><strong>Miso (<span class="jp">味噌</span>):</strong> fermented soybean paste. Rich, salty and warming.</li>
      <li><strong>Shio (<span class="jp">塩</span>):</strong> salt seasoning. A light, clear broth.</li>
      <li><strong>Tonkotsu (<span class="jp">豚骨</span>):</strong> pork bone broth. The richest, creamiest bowl.</li>
    </ul>
    <p>The {NIP} describes ramen as originally a continental import that became popular street food in Japan's postwar period. Regional styles then grew up around local climate and ingredients: cold Hokkaido added rich miso and lard to keep warm, while Kyushu developed pork bone broth, which Nippon.com links to the region's many pig farms.</p>

    <h2 id="shoyu">Shoyu: The Classic<span class="h2-jp">醤油ラーメン</span></h2>
    <p>Shoyu ramen is seasoned with soy sauce, and the broth is usually clear and brown. If you are unsure what to order, this is the safe choice. The {MICH} gives Asahikawa in Hokkaido as an example, where a thin film of flavored oil coats the surface to trap the heat.</p>
    <p>The bowl at the top of this page is a shoyu bowl, called Tsugaru ramen in Aomori. Commons describes it as ramen at a Chukasoba shop in Aomori City. You can see the thin, curly noodles, a slice of pork, bamboo shoots, scallions and a white fish cake with a pink swirl. The broth is clear and amber rather than cloudy. I add that I have not tasted this particular bowl, so I will not describe its flavor.</p>

    <h2 id="miso">Miso: Rich and Warming<span class="h2-jp">味噌ラーメン</span></h2>
    {f_miso}
    <p>Miso ramen has a rich, salty flavor from the fermented soybean paste. The {MICH} describes the Sapporo version with a knob of butter, seasonal seafood and a generous heap of sweet corn. It is a good bowl for a cold day, and it fits the Nippon.com note that Hokkaido ramen was made rich to keep people warm.</p>
    <p>This bowl is printed with the shop name in blue brush lettering, which reads Sapporo Ramen, and Commons lists it as a miso ramen at 850 yen in November 2019. It has an orange-brown cloudy broth, a pile of shredded white leek, a thick slice of pork, bamboo shoots and some dark green strands that I take to be seaweed. This photograph does not show corn or butter, so treat them as common toppings and not as a rule. If you are in Hokkaido, our {link('/regional-food/','regional cuisine guide','ramen_to_regional_food')} has more on Sapporo miso ramen.</p>

    <h2 id="shio">Shio: Light and Clear<span class="h2-jp">塩ラーメン</span></h2>
    {f_shio}
    <p>Shio ramen is seasoned with salt, and its broth looks pale and clear. The {MICH} uses Hakodate in Hokkaido as its example, a light, clear salt broth topped with preserved bamboo shoots, slices of pork and spring onions, and says it bursts with flavor despite looking restrained.</p>
    <p>Commons labels this bowl as a shio ramen from a restaurant called Yoshu Shonin, photographed in January 2019. The broth is almost transparent, which lets you see the noodles under it. On top are bamboo shoots, sliced pork, a halved soft egg with a bright orange yolk and a pile of dark green leaves. If you find other styles too heavy, this is the one to try.</p>

    <h2 id="tonkotsu">Tonkotsu: The Richest Bowl<span class="h2-jp">豚骨ラーメン</span></h2>
    {f_tonk}
    <p>Tonkotsu means pork bone. The {MICH} describes the Hakata style from Fukuoka, in which pork bones are boiled for around eight hours until the broth turns milky white and is suffused with pork flavor. It is the creamiest and heaviest of the four.</p>
    <p>The broth in this photograph is more tan than milky white, a reminder that tonkotsu varies from shop to shop. Commons titles it simply Tonkotsu Ramen and does not name the place. The thin noodles, a slice of pork, nori, scallions, sesame seeds and half a soft egg are all visible. Our {link('/regional-food/','regional cuisine guide','ramen_to_regional_food_2')} covers Hakata tonkotsu ramen in more detail.</p>

    <h2 id="order">How to Order and Eat<span class="h2-jp">注文と食べ方</span></h2>
    <p>These are my own habits as a guide, not strict rules.</p>
    <ol>
      <li><strong>Look for the taste word.</strong> Find shoyu, miso, shio or tonkotsu on the menu. Many menus also show pictures.</li>
      <li><strong>Expect a ticket machine in some shops.</strong> You choose and pay first, then hand the ticket to the staff. Photos on the buttons help.</li>
      <li><strong>Eat soon.</strong> The noodles keep cooking in the hot broth, so eat soon after the bowl arrives.</li>
      <li><strong>Slurp if you like.</strong> It is normal, and it cools the noodles.</li>
      <li><strong>Ask about extras.</strong> Some shops, especially tonkotsu ones, offer extra noodles or a choice of noodle firmness. Ask the staff or check the menu.</li>
    </ol>
    <div style="background:var(--washi-dark);border-left:4px solid var(--kin);padding:16px 20px;margin:24px 0;border-radius:2px;">
      <p style="margin:0;">&#127836; <strong>Plan your trip:</strong> Looking for a guide to the food scene? <a href="{VI}" target="_blank" rel="noopener sponsored" onclick="trackEvent('click','affiliate','viator_ramen_local')">Browse Japan food tours on Viator &rarr;</a></p>
    </div>

    <h2 id="faq">Frequently Asked Questions<span class="h2-jp">よくあるご質問</span></h2>

    <div class="faq-stack">

{faq_html}    </div>

    <h2 id="final">Final Thoughts<span class="h2-jp">むすびに</span></h2>
    <p>Learn four words and you can order a bowl almost anywhere in Japan. If you enjoy one, try another on the next day, because comparing them is half the fun. For more dishes tied to a place, see our {link('/regional-food/','guide to regional cuisine','ramen_to_regional_food_3')}.</p>

    <div class="closing-block">
      <span class="torii">🍜</span>
      <p>Four words, four bowls, and a good reason to eat again tomorrow.</p>
    </div>

    <section class="related-section">
      <h2>Related Guides</h2>
      <span class="h2-jp">関連ガイド</span>
      <div class="related-grid">
        <a class="related-card" href="/regional-food/" onclick="trackEvent('click','internal','related_ramen_to_food')">
          <div class="related-card-label">SACRED JAPAN ／ GUIDE</div>
          <div class="related-card-title">🍜 Japan's Regional Cuisine →</div>
          <div class="related-card-desc">Dishes from Hokkaido to Okinawa, including Sapporo miso and Hakata tonkotsu ramen.</div>
        </a>
        <a class="related-card" href="/culture/tea-ceremony/" onclick="trackEvent('click','internal','related_ramen_to_tea')">
          <div class="related-card-label">SACRED JAPAN ／ GUIDE</div>
          <div class="related-card-title">🍵 The Japanese Tea Ceremony Guide →</div>
          <div class="related-card-desc">A quieter side of Japanese food culture.</div>
        </a>
      </div>
    </section>

    <p style="font-size:14px;color:var(--enshu);line-height:1.7;margin-top:32px;"><strong>Sources:</strong> regional descriptions come from the {MICH} and {NIP}. Shop names, dates and prices come from the Wikimedia Commons descriptions of each photograph. I have not verified current prices or whether each shop is still open.</p>

  </article>

</main>'''

t=open(f'{R}/_tools/culture/tea.py',encoding='utf-8').read()
tail=t[t.index("s=open(f'{R}/culture/omamori-guide"):]
tail=tail.replace('<div class="hero-bg-kanji">茶道</div>','<div class="hero-bg-kanji">拉麺</div>')
tail=tail.replace('<h1>The Japanese <em>Tea Ceremony</em> Guide</h1>','<h1>Japanese <em>Ramen</em> Guide</h1>')
tail=tail.replace('<div class="hero-jp">茶道ガイド</div>','<div class="hero-jp">ラーメンガイド</div>')
tail=tail.replace('What Happens, What to Do as a Guest, and Where to Try It','Shoyu, Miso, Shio and Tonkotsu Explained')
tail=tail.replace('Tea Ceremony Guide','Ramen Guide')
tail=tail.replace('guide_tea','guide_ramen').replace('viator_guide_tea_sticky','viator_guide_ramen_sticky').replace('japanese+tea+ceremony','Japan+ramen+food+tour')
tail=re.sub(r'(<meta name="keywords" content=")[^"]*(")',r'\1Japanese ramen, ramen types, shoyu ramen, miso ramen, shio ramen, tonkotsu ramen, Sapporo ramen, Hakata ramen, how to order ramen in Japan\2',tail)
exec(tail)
