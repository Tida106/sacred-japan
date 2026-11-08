import re, os, json
from PIL import Image
R='/home/claude/sacred-japan'
A='/mnt/user-data/attachments/fd332c08-3f6b-545a-883b-83277e19ff52/'
S='yakitori'
OUT=f'{R}/culture/{S}'
os.makedirs(OUT+'/images',exist_ok=True)
photos={'set':('e9d47c76-image.jpg',1200),'negima':('483f4aa3-image.jpg',1000),'tsukune':('a4a9004d-image.jpg',1000),'seseri':('a635b0ea-image.jpg',1000),'sasami':('830f617d-image.jpg',1000),'beef':('9d38a312-image.jpg',1000),'shop':('94c1c1ca-image.jpg',1000),'kushiage':('c68f2df6-image.jpg',1000)}
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
def lic(n,u): return f'<a href="{u}" target="_blank" rel="noopener" style="color:var(--enshu);">{n}</a>'
CC0=lic('CC0','https://creativecommons.org/publicdomain/zero/1.0/')
BYSA4=lic('CC BY-SA 4.0','https://creativecommons.org/licenses/by-sa/4.0/')
BYSA3=lic('CC BY-SA 3.0','https://creativecommons.org/licenses/by-sa/3.0/')
VIA='via Wikimedia Commons (resized)'
def link(href,txt,lab): return f'<a href="{href}" class="inline-link" onclick="trackEvent(\'click\',\'internal\',\'{lab}\')">{txt}</a>'
def ext(href,txt,lab): return f'<a href="{href}" target="_blank" rel="noopener" onclick="trackEvent(\'click\',\'external\',\'{lab}\')">{txt}</a>'
FJ=ext('https://www.fun-japan.jp/en/articles/3109','FUN! JAPAN (how to enjoy yakitori)','yaki_funjapan_enjoy')
FJH=ext('https://www.fun-japan.jp/en/articles/8213','FUN! JAPAN (history of yakitori)','yaki_funjapan_history')
TC=ext('https://www.tablecheck.com/en/blog/yakitori-101-your-guide-to-japan-s-grilled-chicken-skewers/','TableCheck','yaki_tablecheck')

f_set=fig('set','Nine skewers laid side by side on a pale blue, wavy-edged plate: grilled chicken, a piece with a wedge of onion, darker meats, a red piece and three glazed meatballs, with bamboo-leaf-shaped handles at the bottom, on a light wooden table','A plate of mixed yakitori, seen from above.',f'Photo: N509FZ, {BYSA4}, 6 August 2023. Commons describes it as "A set of 6 for JPY 979, chicken with onion 176, chicken leg 198, pork harami 176." {VIA}',hero=True)
f_neg=fig('negima','Two skewers on a cream plate: glazed chunks of grilled chicken alternating with pieces of green onion, some charred, with dark sauce pooled on the plate','Negima: chicken pieces alternating with leek, with sauce.',f'Photo: Ocdp, {CC0}, 10 April 2015. Commons titles it "Negima Yakitori" and gives the Japanese name もも貴族焼, from the chain Torikizoku. {VIA}',maxw=700)
f_tsu=fig('tsukune','Six round, flattened chicken meatballs with charred stripes and green flecks, threaded on a skewer on a cream plate','Tsukune: minced-chicken patties, seasoned with salt.',f'Photo: Ocdp, {CC0}, 10 April 2015. Commons titles it "Tsukune Yakitori" and gives the Japanese name つくね塩, meaning the salt version. {VIA}',maxw=700)
f_ses=fig('seseri','Two skewers of crinkled, golden-brown grilled chicken pieces with charred edges on a cream plate','Seseri: chicken neck meat.',f'Photo: Ocdp, {CC0}, 10 April 2015. Commons titles it "Seseri Yakitori". {VIA}',maxw=700)
f_sas=fig('sasami','Two skewers of pale, tender-looking chicken pieces with a few grill marks and black pepper flecks on a cream plate','Sasami: the lean tenderloin, lightly grilled.',f'Photo: Ocdp, {CC0}, 10 April 2015. Commons titles it "Chicken tenderloin Yakitori". {VIA}',maxw=700)
f_beef=fig('beef','Several dark, glossy skewers of grilled beef with charred edges and sauce pooled on a cream plate','Beef skewers glazed with sauce.',f'Photo: Ocdp, {CC0}, 10 April 2015. Commons gives the English title "Spit-roasted beef" and the Japanese name 牛串たれ焼, meaning sauce-grilled beef skewers. {VIA}',maxw=700)
f_shop=fig('shop','The front of an izakaya with a large yellow sign reading TORIKIZOKU, dark wooden doors with small-pane windows, a pink bicycle parked at the entrance and a standing sign at the left','The street front of a yakitori izakaya chain.',f'Photo: L26, {BYSA3} (also offered under the GFDL), 13 September 2016. Commons describes it as an example of a Torikizoku store, the Abiko branch in Sumiyoshi Ward, Osaka. Signs and fronts change, so treat it as a 2016 example. {VIA}',maxw=700)
f_kush=fig('kushiage','A steel tray with a wire rack holding several skewers of breaded, deep-fried pieces and, at the right, a round slice with holes in it','Kushiage: breaded, deep-fried skewers.',f'Photo: Ocdp, {CC0}, 8 April 2017. Commons describes it as assorted kushiage (各種串揚げ) and gives no venue. The round slice with holes at the right looks like lotus root to me. {VIA}',maxw=700)

faqs=[
("Is yakitori always chicken?","The name means grilled bird, and chicken is the core of the menu, including organ cuts such as liver, heart and gizzard. Many menus add other meats, though. The photos on this page include a beef skewer, and Commons describes one set as including pork harami, so ask or check the menu."),
("Should I choose salt or sauce?","Shio is salt and tare is a sweet-savory sauce. FUN! JAPAN gives a rule of thumb: sauce for fatty cuts such as thigh, salt for lean cuts such as breast. TableCheck says staff typically ask which you prefer, so you can ask for their recommendation."),
("What is negima?","Negima is chicken pieces alternating with green onion or leek on a skewer. FUN! JAPAN describes it as thigh with green onion, and TableCheck says thigh or breast pieces, so the cut can vary by restaurant."),
("How many skewers should I order at once?","FUN! JAPAN says it is general etiquette to order at least two skewers of the same cut, since the chef cooks many at once. TableCheck advises ordering a few types at a time, not everything at once, so the skewers do not go cold."),
("Can I take the meat off the skewer?","Yes, at sit-down restaurants. TableCheck says eating straight off the skewer is fine and that sliding the pieces onto your plate with chopsticks is also acceptable. Put used skewers in the container provided, not on a shared platter."),
("How much does yakitori cost?","It varies a lot. The set in the photo at the top is described on Commons as six skewers for 979 yen in August 2023, with single skewers at 176 to 198 yen. A 2019 FUN! JAPAN article gave 120 to 160 yen per skewer, and TableCheck lists chef's courses from 2,980 yen to over 13,000 yen. These are undated or old, so please check the current menu."),
]
faq_html=''.join(f'''      <details class="faq-item">
        <summary>{q}</summary>
        <div class="faq-answer">{a}</div>
      </details>

''' for q,a in faqs)
faq_ld=json.dumps({"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in faqs]},ensure_ascii=False,indent=2)
TITLE="Yakitori Guide: Cuts, Salt vs Sauce and How to Order at an Izakaya"
DESC="A licensed guide's English introduction to yakitori: the main cuts (negima, tsukune, sasami, seseri and more), salt versus sauce, ordering etiquette at an izakaya and what it costs, with photographs."
URL=f"https://sacred-japan.net/culture/{S}/"
OG="https://sacred-japan.net/images/og/og-culture-yakitori.jpg"
VI='https://www.viator.com/search/Japan+food+tour?pid=P00298374&amp;mcid=42383&amp;medium=link&amp;campaign=sacred-japan'
main=f'''<main>

  {f_set}

  <aside class="toc" aria-label="Table of contents">
    <div class="toc-label">TABLE OF CONTENTS ／ 目次</div>
    <div class="toc-title">In This Guide</div>
    <ol>
      <li><a href="#opening">Opening: A Note from the Guide</a></li>
      <li><a href="#what">What Yakitori Is</a></li>
      <li><a href="#cuts">The Cuts to Know</a></li>
      <li><a href="#shio-tare">Salt or Sauce</a></li>
      <li><a href="#izakaya">At the Izakaya</a></li>
      <li><a href="#kushiage">Not to Confuse: Kushiage</a></li>
      <li><a href="#faq">Frequently Asked Questions</a></li>
      <li><a href="#final">Final Thoughts</a></li>
    </ol>
  </aside>

  <article>

    <section id="opening">
      <p class="opening">When a visitor asks me for an ordinary night out in Japan, one that is not a tasting menu and not a tourist show, I point them to a counter where someone is grilling skewers over charcoal.</p>
      <p>As a licensed guide, I find the menu is the hard part: a list of cut names, a choice between salt and sauce, and a few unwritten habits. This guide covers the cuts, how to choose, and how to order, and it says where the sources disagree.</p>
    </section>

    <h2 id="what">What Yakitori Is<span class="h2-jp">焼き鳥とは</span></h2>
    <p>Yakitori (<span class="jp">焼き鳥</span>) is small pieces of chicken, and often its organs, threaded on skewers and grilled over a charcoal fire, then seasoned with salt or brushed with sauce. The skewers are served a few at a time, which makes it easy food to share over drinks.</p>
    <p>On history, {FJH} says duck, quail and pheasant were eaten in Japan long before yakitori, that it first appears as a dish in a cookbook of 1682 in the Edo period, and that yakitori restaurants began to open in the Meiji period. It adds that early yakitori was mainly chicken organs and that broiler chickens, in 1954, made it cheap enough to spread. The article cites no sources, so I would treat the dates as approximate.</p>
    <p>The plate at the top shows what a mixed order looks like. I count nine skewers on a pale blue plate: chicken with a wedge of onion, darker meats, a deep-red piece and three glazed meatballs. Commons describes it as "A set of 6 for JPY 979" with single skewers at 176 and 198 yen, so the description probably covers only part of what is on the plate. I will not name each skewer, because I cannot tell them apart with confidence from the photo.</p>

    <h2 id="cuts">The Cuts to Know<span class="h2-jp">部位</span></h2>
    <p>Names vary by restaurant, but these are the ones {TC} and {FJ} describe most often:</p>
    <ul>
      <li><strong>Momo (<span class="jp">もも</span>):</strong> thigh, the default and juicy.</li>
      <li><strong>Mune (<span class="jp">むね</span>):</strong> breast, lean and mild.</li>
      <li><strong>Negima (<span class="jp">ねぎま</span>):</strong> chicken pieces alternating with green onion.</li>
      <li><strong>Tsukune (<span class="jp">つくね</span>):</strong> minced chicken formed into a patty or balls.</li>
      <li><strong>Sasami (<span class="jp">ささみ</span>):</strong> lean tenderloin, sometimes served with plum sauce, wasabi or shiso.</li>
      <li><strong>Seseri (<span class="jp">せせり</span>):</strong> neck meat, fatty and juicy.</li>
      <li><strong>Kawa (<span class="jp">皮</span>):</strong> skin.</li>
      <li><strong>Nankotsu (<span class="jp">なんこつ</span>):</strong> cartilage, chewy and crunchy.</li>
      <li><strong>Reba (<span class="jp">レバー</span>), hatsu (<span class="jp">ハツ</span>), sunagimo (<span class="jp">砂肝</span>):</strong> liver, heart and gizzard. TableCheck calls the liver rich and pâté-like, the heart meaty and softer, and the gizzard crisp.</li>
      <li><strong>Bonjiri (<span class="jp">ぼんじり</span>):</strong> tail meat, rare and fatty.</li>
      <li><strong>Tebasaki (<span class="jp">手羽先</span>):</strong> wings, which TableCheck calls a specialty of Nagoya.</li>
    </ul>

    {f_neg}
    <p>This is negima. Commons gives it the Japanese name <em>momo kizoku-yaki</em> (もも貴族焼), which points to thigh meat, though the sources differ on whether negima uses thigh or breast, so the cut can vary. In the photo the chicken and the leek are both well charred and glazed, and the sauce has pooled on the plate.</p>

    {f_tsu}
    <p>Tsukune is the one I suggest to anyone nervous about unfamiliar cuts. FUN! JAPAN says it is minced chicken with herbs, often served with a raw egg yolk for dipping, and recommends sauce. The photo is labeled as the salt version, so it is a good reminder that most cuts can be ordered either way.</p>

    {f_ses}
    <p>Seseri is the neck. TableCheck calls it fatty and juicy, and the crinkled surface in the photo, with its crisp edges, suggests how the fat renders over the fire. I will not say more about its texture than the sources do.</p>

    {f_sas}
    <p>Sasami looks very different: pale, lean and only lightly marked by the grill. These two skewers have a few grill marks and dark specks of seasoning. Because the meat is so lean, it is the cut where the accompaniments matter, and TableCheck mentions plum sauce, wasabi or shiso.</p>

    <h2 id="shio-tare">Salt or Sauce<span class="h2-jp">塩とタレ</span></h2>
    <p>When you order, you are usually asked whether you want <em>shio</em> (salt) or <em>tare</em> (sauce). {FJ} gives a rule of thumb: sauce for fatty cuts such as thigh, salt for lean cuts such as breast, and it says shio lets you taste the difference between cuts while tare shows off a restaurant's own sauce. {TC} says staff typically ask, so you can simply ask what they recommend.</p>
    {f_beef}
    <p>This is the sauce side. Commons calls these beef skewers, with the Japanese title meaning sauce-grilled beef, and they are a reminder that yakitori menus often go beyond chicken. The glaze is dark and glossy, and the sticks are charred at the ends from the grill.</p>

    <h2 id="izakaya">At the Izakaya<span class="h2-jp">居酒屋で</span></h2>
    <p>Yakitori is served at everything from a smoky counter with a handful of seats to a large chain. Prices follow: {TC} lists chef's-choice courses from about 2,980 yen up to more than 13,000 yen, though the article does not date them, while the photo at the top shows single skewers at 176 to 198 yen in 2023.</p>
    {f_shop}
    <p>This is the street front of a chain branch in Osaka, with a bright sign, dark wooden doors and a bicycle at the door. I include it to show what many casual yakitori izakaya look like from the outside, and it is a 2016 photograph, so the signs may have changed.</p>
    <p>A few habits from the two guides I have been quoting:</p>
    <ul>
      <li><strong>Eat them hot.</strong> Order a few kinds at a time, not everything at once, so the skewers do not go cold.</li>
      <li><strong>Order in pairs.</strong> FUN! JAPAN says it is general etiquette to order at least two of the same cut.</li>
      <li><strong>Off the skewer or onto the plate.</strong> Both are fine at a sit-down restaurant, according to TableCheck.</li>
      <li><strong>Used skewers.</strong> Put them in the container provided, not on a shared platter.</li>
      <li><strong>Drinks.</strong> TableCheck mentions beer, oolong tea or soda as common pairings, and wine or sake at some upscale places.</li>
    </ul>
    <p>If you would rather have a guide lead you, a {ext(VI,'local food tour','yaki_viator_food_tour')} is one way to try it in a neighborhood with someone who can read the menu.</p>

    <h2 id="kushiage">Not to Confuse: Kushiage<span class="h2-jp">串揚げ</span></h2>
    <p>Kushiage is a different dish that looks similar on a menu: skewered pieces that are breaded and deep-fried, not grilled. Many izakaya serve both, so check the word before you order.</p>
    {f_kush}
    <p>The tray holds an assortment, with golden crumb coatings and, at the right, a round slice with holes that looks like lotus root. Commons gives no venue. It is the same format as yakitori, small pieces on a stick, and a quick way to see how the cooking method changes the look.</p>

    <h2 id="faq">Frequently Asked Questions<span class="h2-jp">よくあるご質問</span></h2>

    <div class="faq-stack">

{faq_html}    </div>

    <h2 id="final">Final Thoughts<span class="h2-jp">むすびに</span></h2>
    <p>Start with negima or tsukune, add something lean like sasami and something richer like seseri, and ask the staff about salt or sauce. For more dishes, see our {link('/culture/popular-dishes/','guide to popular Japanese dishes','yaki_to_dishes')}.</p>

    <div class="closing-block">
      <span class="torii">🍢</span>
      <p>A charcoal fire, a skewer and a cold drink.</p>
    </div>

    <section class="related-section">
      <h2>Related Guides</h2>
      <span class="h2-jp">関連ガイド</span>
      <div class="related-grid">
        <a class="related-card" href="/culture/popular-dishes/" onclick="trackEvent('click','internal','related_yaki_to_dishes')">
          <div class="related-card-label">SACRED JAPAN ／ GUIDE</div>
          <div class="related-card-title">🍱 Popular Japanese Dishes Guide →</div>
          <div class="related-card-desc">Sukiyaki, tempura, tonkatsu, karaage, rice bowls and sushi.</div>
        </a>
        <a class="related-card" href="/culture/bread/" onclick="trackEvent('click','internal','related_yaki_to_bread')">
          <div class="related-card-label">SACRED JAPAN ／ GUIDE</div>
          <div class="related-card-title">🥐 Japanese Bread Guide →</div>
          <div class="related-card-desc">Anpan, melonpan, curry bread, sandwiches and ogura toast.</div>
        </a>
        <a class="related-card" href="/culture/noodles/" onclick="trackEvent('click','internal','related_yaki_to_noodles')">
          <div class="related-card-label">SACRED JAPAN ／ GUIDE</div>
          <div class="related-card-title">🍜 Japanese Noodles Guide →</div>
          <div class="related-card-desc">Soba, udon, yakisoba, somen and cold ramen, with photos.</div>
        </a>
        <a class="related-card" href="/regional-food/" onclick="trackEvent('click','internal','related_yaki_to_food')">
          <div class="related-card-label">SACRED JAPAN ／ GUIDE</div>
          <div class="related-card-title">🍽️ Japan's Regional Cuisine →</div>
          <div class="related-card-desc">Dishes from Hokkaido to Okinawa.</div>
        </a>
      </div>
    </section>

    <p style="font-size:14px;color:var(--enshu);line-height:1.7;margin-top:32px;"><strong>Sources:</strong> cuts, salt versus sauce and ordering from {FJ} and {TC}; history from {FJH}. Photograph details come from the Wikimedia Commons descriptions. I have not verified current prices.</p>

  </article>

</main>'''
t=open(f'{R}/_tools/culture/tea.py',encoding='utf-8').read()
tail=t[t.index("s=open(f'{R}/culture/omamori-guide"):]
tail=tail.replace('<div class="hero-bg-kanji">茶道</div>','<div class="hero-bg-kanji">串</div>')
tail=tail.replace('<h1>The Japanese <em>Tea Ceremony</em> Guide</h1>','<h1>The <em>Yakitori</em> Guide</h1>')
tail=tail.replace('<div class="hero-jp">茶道ガイド</div>','<div class="hero-jp">焼き鳥ガイド</div>')
tail=tail.replace('What Happens, What to Do as a Guest, and Where to Try It','Cuts, Salt vs Sauce and How to Order')
tail=tail.replace('Tea Ceremony Guide','Yakitori Guide')
tail=tail.replace('guide_tea','guide_yakitori').replace('viator_guide_tea_sticky','viator_guide_yakitori_sticky').replace('japanese+tea+ceremony','Japan+food+tour')
tail=re.sub(r'(<meta name="keywords" content=")[^"]*(")',r'\1yakitori, yakitori guide, negima, tsukune, sasami, seseri, shio, tare, izakaya, Japanese grilled chicken skewers\2',tail)
exec(tail)
