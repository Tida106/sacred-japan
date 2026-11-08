import re, os, json
from PIL import Image
R='/home/claude/sacred-japan'
A='/mnt/user-data/attachments/fd332c08-3f6b-545a-883b-83277e19ff52/'
S='bread'
OUT=f'{R}/culture/{S}'
os.makedirs(OUT+'/images',exist_ok=True)
photos={'melon':('a979011d-image.jpg',1200),'anpan':('60f4abb2-image.jpg',1000),'curry':('5cbe84b8-image.jpg',1000),'yakisoba':('5b6ab78a-image.jpg',1000),'agepan':('c776a767-image.jpg',1000),'croquette':('923ce486-image.jpg',1000),'cornet':('0e15151b-image.jpg',700),'menchi':('e47dc74b-image.jpg',640),'tamago':('1cf92e48-image.jpg',1000),'fruit':('82f76ef5-image.jpg',689),'ogura':('896abc06-image.jpg',900)}
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
BY2=lic('CC BY 2.0','https://creativecommons.org/licenses/by/2.0/')
BY4=lic('CC BY 4.0','https://creativecommons.org/licenses/by/4.0/')
BYSA2=lic('CC BY-SA 2.0','https://creativecommons.org/licenses/by-sa/2.0/')
BYSA21=lic('CC BY-SA 2.1 JP','https://creativecommons.org/licenses/by-sa/2.1/jp/')
BYSA4=lic('CC BY-SA 4.0','https://creativecommons.org/licenses/by-sa/4.0/')
BYSA3=lic('CC BY-SA 3.0','https://creativecommons.org/licenses/by-sa/3.0/')
VIA='via Wikimedia Commons (resized)'
def link(href,txt,lab): return f'<a href="{href}" class="inline-link" onclick="trackEvent(\'click\',\'internal\',\'{lab}\')">{txt}</a>'
def ext(href,txt,lab): return f'<a href="{href}" target="_blank" rel="noopener" onclick="trackEvent(\'click\',\'external\',\'{lab}\')">{txt}</a>'
NP=ext('https://www.nippon.com/en/guide-to-japan/cs00023/','Nippon.com (anpan)','bread_nippon_anpan')
JT=ext('https://www.japan.travel/en/gastronomy/article-bread-evolved-in-japan/','Japan National Tourism Organization (bread in Japan)','bread_jnto')
TW=ext('https://www.tokyoweekender.com/food-and-drink/melon-pan/','Tokyo Weekender (melon pan)','bread_tw_melon')
FIJ=ext('https://www.foodinjapan.org/kanto/tokyo/curry-bread','Food in Japan (curry bread)','bread_foodinjapan_curry')
FIK=ext('https://www.foodinjapan.org/kanto/tokyo-en/crockett-bread','Food in Japan (korokke pan)','bread_foodinjapan_korokke')
TTK=ext('https://www.tastingtable.com/1165772/japans-korokke-pan-is-a-mashed-potato-hot-dog-sandwich-hybrid','Tasting Table (korokke pan)','bread_tt_korokke')
TT=ext('https://www.tastingtable.com/stories/yakisoba-pan-is-the-japanese-noodle-sandwich-you-should-try/','Tasting Table (yakisoba pan)','bread_tt_yakisoba')
NPL=ext('https://www.nippon.com/en/japan-topics/g02481/','Nippon.com (school lunches)','bread_nippon_lunch')
JP=ext('https://www.jeepe.jp/fr/articles/nagoya-ogura-toast-1418','Jeepe (ogura toast)','bread_jeepe_ogura')
TTF=ext('https://tastingtable.com/897883/the-history-of-japans-iconic-fruit-sandwich-is-rooted-in-luxury','Tasting Table (fruit sandwich)','bread_tt_fruit')
JTA=ext('https://japanesetaste.com/blogs/japanese-taste-blog/spreading-the-news-the-world-of-japanese-sandwiches','Japanese Taste (sandwiches)','bread_jtaste')

f_melon=fig('melon','A woven basket of round buns with a pale golden, diamond cross-hatched crust, packed closely together','Melonpan: a soft bun under a cracked, cross-hatched cookie crust.',f'Photo: Sakurai Midori, {BYSA21}, 3 September 2006. {VIA}',hero=True)
f_anpan=fig('anpan','Two round buns with seeds on top on a white background; the one on the right is cut open to show a dark, smooth bean-paste filling','Anpan, whole and cut open: a soft bun around sweet red bean paste.',f'Photo: Ocdp, {CC0}, 4 November 2016. {VIA}')
f_curry=fig('curry','Two halves of a golden, breadcrumb-coated fried bun, each opened to show a thick brown curry filling inside soft white bread','Curry bread, cut open: a breaded, deep-fried bun with curry inside.',f'Photo: Laitr Keiows, {BYSA3}, 7 August 2010. {VIA}')
f_yaki=fig('yakisoba','A long, soft golden roll split open and packed with orange-tinged fried noodles, with red ginger and a sprinkle of green on top','Yakisoba-pan: fried noodles in a long roll.',f'Photo: Ocdp, {CC0}, 13 November 2016. {VIA}')
f_age=fig('agepan','Two long, golden rolls on a cooling rack, one with a sugar-coated crust in front and one with a pale brown powder coating behind','Agepan: a fried roll coated in sugar or kinako.',f'Photo: Quercus acuta, {CC0}, 16 April 2017. {VIA}')
f_croq=fig('croquette','A white plate with a round, dark, fried curry bread and a long korokke pan roll with a breaded croquette on it, next to a white mug of black coffee on a wooden slatted table','Curry bread (round, left) and korokke pan (the long roll) with coffee.',f'Photo: Ocdp, {CC0}, 21 May 2017. {VIA}')
f_corn=fig('cornet','A glossy golden-brown spiral-shaped bun with a dark filling visible at the open end, in a clear wrapper','A chocolate cornet: a spiral bun with a dark filling.',f'Photo: yto (Flickr, uploaded by Psihedelisto), {BY2}, uploaded 8 October 2021. {VIA}',maxw=420)
f_men=fig('menchi','An orange box holding a sandwich cut into pieces: thick breaded minced-meat patties with sauce between slices of white bread','A menchi-katsu sandwich in its box.',f'Photo: jetalone, {BY2}, 16 December 2006. {VIA}',maxw=560)
f_tam=fig('tamago','A tray of sandwiches on white bread cut to show a bright yellow filling, with a small green garnish at the lower left','Tamago sando: a soft, bright yellow egg filling in white bread.',f'Photo: くろふね (Jranar), {BYSA4}, 8 May 2019. {VIA}')
f_fru=fig('fruit','Sandwiches on a white plate cut to show cream with strawberries, orange segments and pale green fruit between slices of white bread','Fruit sando: cut fruit set in whipped cream.',f'Photo: Araisyohei, {BY4}, 29 June 2022. {VIA}',maxw=560)
f_ogu=fig('ogura','Thick toast on a white plate with a mound of dark red bean paste topped with a pat of butter, a boiled egg beside it and butter portions at the lower left','Ogura toast with a boiled egg, a coffee-shop set.',f'Photo: akira yamada, {BYSA2}, 24 May 2013. {VIA}',maxw=620)

faqs=[
("What is the most famous Japanese bread?","Anpan, a soft bun filled with sweet red bean paste, is often named as the first bread to become popular in Japan, and the JNTO article calls it that. Melonpan and curry bread are the other two names most visitors meet first."),
("Does melonpan taste like melon?","Usually not. Tokyo Weekender says it is named for its looks, since the cross-hatched crust resembles a muskmelon's skin, and that it is almost never flavored with melon. Some bakeries do add a melon flavor or fill it, so check the label."),
("Who invented curry bread?","Nobody can say for certain. Food in Japan lists several accounts: the Cattlea bakery in Tokyo (1927) is said to have invented it, a different Tokyo bakery filed a 1927 utility model for a fried bread idea that did not mention curry, and another bakery in Nerima says it fried curry sandwiches from 1934. Treat any single answer as a claim, not a fact."),
("What is the difference between agepan and curry bread?","Both are fried, but agepan is a plain roll fried and coated in sugar or kinako (roasted soybean flour), and it is a sweet school-lunch nostalgia food. Curry bread is a savory filled bun with a breadcrumb coat."),
("Is yakisoba-pan a carb on carb?","Yes, and that is the point. Noodles go in a long soft roll, and Tasting Table describes it as a nostalgic school-lunch item that convenience stores also sell. Accounts of its origin conflict, with the 1950s mentioned."),
("Where do I find these breads?","Most bakeries (panya) carry anpan, melonpan and curry bread, and convenience stores sell sandwiches and yakisoba-pan. Fruit sando is a fruit parlor and cafe item, and ogura toast is a Nagoya coffee-shop classic. I have not verified current shop hours or prices."),
]
faq_html=''.join(f'''      <details class="faq-item">
        <summary>{q}</summary>
        <div class="faq-answer">{a}</div>
      </details>

''' for q,a in faqs)
faq_ld=json.dumps({"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in faqs]},ensure_ascii=False,indent=2)
TITLE="Japanese Bread Guide: Anpan, Melonpan, Curry Bread and Sandwiches"
DESC="A licensed guide's English introduction to Japanese bakery bread: anpan, melonpan, curry bread, yakisoba-pan, agepan, plus tamago sando, fruit sando and Nagoya's ogura toast, with photographs."
URL=f"https://sacred-japan.net/culture/{S}/"
OG="https://sacred-japan.net/images/og/og-culture-bread.jpg"
VI='https://www.viator.com/search/Japan+food+tour?pid=P00298374&amp;mcid=42383&amp;medium=link&amp;campaign=sacred-japan'
main=f'''<main>

  {f_melon}

  <aside class="toc" aria-label="Table of contents">
    <div class="toc-label">TABLE OF CONTENTS ／ 目次</div>
    <div class="toc-title">In This Guide</div>
    <ol>
      <li><a href="#opening">Opening: A Note from the Guide</a></li>
      <li><a href="#sweet">Sweet Buns: Anpan, Melonpan, Cornet</a></li>
      <li><a href="#savory">Savory and Fried: Curry Bread, Yakisoba-pan, Agepan, Korokke Pan</a></li>
      <li><a href="#sando">Sandwiches and Toast</a></li>
      <li><a href="#faq">Frequently Asked Questions</a></li>
      <li><a href="#final">Final Thoughts</a></li>
    </ol>
  </aside>

  <article>

    <section id="opening">
      <p class="opening">Walk into a Japanese bakery with a tray and tongs and you will find a bun with red bean paste, one with curry, and one with noodles, all within arm's reach.</p>
      <p>As a licensed guide, I like to start visitors here because the bread tells you how Japan takes a foreign food and rebuilds it. This guide covers the classics, with photographs, and it says where the sources disagree on who invented what.</p>
    </section>

    <h2 id="sweet">Sweet Buns<span class="h2-jp">甘いパン</span></h2>

    <h3>Anpan</h3>
    <p>The JNTO article says bread arrived with Portuguese traders in the 16th century, disappeared during the isolation period, and came back in the 19th century as a hard loaf that Japanese customers did not like. Baker Kimura Yasubei adapted it into a soft bun filled with sweet bean paste. {NP} dates the invention to 1874 at Kimuraya, and says the bread was presented to Emperor Meiji in 1875 for an April cherry-blossom outing. {JT} adds that the Ginza shop still uses a salt-pickled cherry blossom topping on its anpan.</p>
    {f_anpan}
    <p>The pair shows the whole idea: a round, shiny bun and, cut open, a dark, smooth filling. Seeds sit on top; to my eye they look like poppy seeds, though Nippon.com mentions sesame as a common topping. Fillings and toppings vary by bakery.</p>

    <h3>Melonpan</h3>
    <p>The name comes from the look, not the taste. {TW} says the cracked, cross-hatched crust resembles a muskmelon's skin and that the bun is almost never melon-flavored. Where it was invented is not settled: the article lists claims from a Kobe bakery, a Kure bakery and others, and calls a popular story about a Russian-trained baker questionable. I will not give you one inventor.</p>
    <p>The hero photograph at the top shows a basket of them. The top is a thin cookie-like layer baked over soft bread, which is why the crust cracks into that pattern.</p>

    <h3>Chocolate Cornet</h3>
    {f_corn}
    <p>The cornet is a spiral roll, shaped like a cone, and bakeries often fill it with cream or chocolate. In this photograph a dark filling is visible at the open end, which suggests chocolate, but the wrapper hides the label, so I will not claim a flavor. I did not find a reliable source for its history, so I will leave that blank.</p>

    <h2 id="savory">Savory and Fried<span class="h2-jp">惣菜パンと揚げパン</span></h2>

    <h3>Curry Bread</h3>
    <p>This is the bun that visitors fall for. It is a bread dough around curry, coated in crumbs and deep-fried. {FIJ} gives several competing origin accounts: the Cattlea bakery in Tokyo (1927) is said to have invented it, another Tokyo bakery filed a 1927 utility model for frying bread with fillings such as tonkatsu but without curry, and a bakery in Nerima says its founder fried curry sandwiches from 1934. Take all of them as claims.</p>
    {f_curry}
    <p>Cut open, the golden coat gives way to a thick brown curry that fills most of the bun. Fillings range from mild to spicy by shop.</p>

    <h3>Yakisoba-pan</h3>
    <p>Fried noodles in a long roll. Tasting Table says it is said to have been invented in the 1950s in a diner, but accounts of its exact origin conflict, and no shop is named. It is a school-lunch nostalgia item, and widely sold in convenience stores.</p>
    {f_yaki}
    <p>Here the noodles carry a light orange tint, with red pickled ginger and a green sprinkle on top. It is a carb on a carb, and that is the charm.</p>

    <h3>Agepan and the School Lunch Story</h3>
    <p>Agepan is a roll that is fried and then coated, usually in sugar and kinako (roasted soybean flour). {NPL} says a Tokyo school cook invented it in 1952 and that it spread nationwide in the early 1960s. The same article says bread and powdered milk were provided from 1946, and that rice only became a standard part of school meals in the 1970s, which explains why bread is so tied to childhood memory.</p>
    {f_age}
    <p>Commons describes this pair as deep-fried koppe-pan, sugar on the front one and kinako on the back one, and the two powdery coats are easy to tell apart in the photograph.</p>

    <h3>Korokke Pan, with Curry Bread Beside It</h3>
    {f_croq}
    <p>The round, dark bun on this plate is curry bread. The long roll with the breaded piece on it is <strong>korokke pan</strong>, croquette bread, and it is the plainer of the two to explain: a fried potato croquette served in a soft roll.</p>
    <p>{FIK} describes it as a deep-fried korokke tucked into a soft, elongated roll called koppepan, and calls it a good example of <em>sozai pan</em>, the savory "side-dish" breads. The Japanese korokke is mainly mashed potato, often mixed with ground beef and vegetables, coated in panko and fried. It is a cheap, filling food, which is the reason it works so well inside bread. {TTK} describes the same idea as a mashed-potato hot dog, with a milk-bread bun.</p>
    <p>Sources differ on the finishing touches. {FIK} says the croquette gets a sweet, tangy sauce such as tonkatsu sauce, while {TTK} lists Worcestershire sauce, mayonnaise, and tomato or shredded cabbage. In practice it depends on the bakery, so look at what the counter shows. The same article says Choshiya, a Ginza shop founded in 1927 behind the Kabuki-za, claims to be the birthplace, and that the sandwich was invented in 1927. That is a single source and the shop's own claim, so I would treat it as the story told there, not settled history. Curry bread has a 1927 origin story too, so the date is not a clean marker for either bread.</p>
    <p>For a visitor the practical point is simple. Both are fried, both are cheap, and a bakery or convenience store will often have the pair. Korokke pan is the gentler choice if you want potato and crunch without any spice.</p>

    <h2 id="sando">Sandwiches and Toast<span class="h2-jp">サンドイッチとトースト</span></h2>
    <p>Most Japanese sandwiches use shokupan, the soft, lightly sweet, rectangular loaf, usually with the crusts trimmed. {JTA} covers the main ones.</p>

    <h3>Tamago Sando</h3>
    <p>A soft, slightly sweet egg filling, often made with Kewpie mayonnaise, between thin slices of shokupan. It is the sandwich visitors keep coming back to from convenience stores.</p>
    {f_tam}
    <p>This tray shows the filling cut open as a bright yellow mass. The sandwiches are cut into pieces, with a small green garnish at the corner.</p>

    <h3>Menchi-katsu Sando</h3>
    {f_men}
    <p>A breaded, fried minced-meat patty with sauce between slices of white bread. The Commons description mentions a menchi-katsu sandwich from Asakusa Imahan, bought at Naha Airport, so this is a boxed take-home version. I am not claiming this is how every shop serves it.</p>

    <h3>Fruit Sando</h3>
    <p>Cut fruit set in whipped cream between slices of white bread. {TTF} says fruit was once an expensive luxury, which is why it ended up between bread as an affordable treat. It places the first fruit sandos in the Taisho era (1912-1926), but notes that a Ginza fruit parlor's spokesperson guesses the 1940s, so the date is not settled.</p>
    {f_fru}
    <p>The slices show whipped cream around strawberry, orange segments and pale green fruit. Commons gives the cafe as Da Cafe in Ebisu, in a June 2022 photograph.</p>

    <h3>Ogura Toast</h3>
    <p>Thick toast with butter and sweet azuki paste (ogura-an), most associated with Nagoya's coffee-shop morning sets. {JP} says it is thought to date from about 1921 and credits the Mitsuba cafe in Sakae, but it hedges that and cites no source, so treat it as a story. It also gives about 500 to 800 yen for a morning set, which is only an estimate.</p>
    {f_ogu}
    <p>The photograph shows a mound of bean paste with butter on thick toast and a boiled egg beside it. Butter portions are visible at the lower left, a reminder that the set is built around a drink. The Commons description calls it a Nagoya morning set; hours vary by cafe.</p>
    <p>If you would rather have someone lead you through a market and bakery street, a {ext(VI,'local food tour','bread_viator_food_tour')} is one option.</p>

    <h2 id="faq">Frequently Asked Questions<span class="h2-jp">よくあるご質問</span></h2>

    <div class="faq-stack">

{faq_html}    </div>

    <h2 id="final">Final Thoughts<span class="h2-jp">むすびに</span></h2>
    <p>Start with anpan and curry bread, add a melonpan for contrast, and finish with a sandwich or a Nagoya toast set. For dishes beyond bread, see our {link('/culture/popular-dishes/','guide to popular Japanese dishes','bread_to_dishes')} and our {link('/culture/noodles/','noodles guide','bread_to_noodles')}.</p>

    <div class="closing-block">
      <span class="torii">🥐</span>
      <p>A tray, a pair of tongs and a bakery that smells of butter.</p>
    </div>

    <section class="related-section">
      <h2>Related Guides</h2>
      <span class="h2-jp">関連ガイド</span>
      <div class="related-grid">
        <a class="related-card" href="/culture/popular-dishes/" onclick="trackEvent('click','internal','related_bread_to_dishes')">
          <div class="related-card-label">SACRED JAPAN ／ GUIDE</div>
          <div class="related-card-title">🍱 Popular Japanese Dishes Guide →</div>
          <div class="related-card-desc">Sukiyaki, tempura, tonkatsu, karaage, rice bowls and sushi.</div>
        </a>
        <a class="related-card" href="/culture/noodles/" onclick="trackEvent('click','internal','related_bread_to_noodles')">
          <div class="related-card-label">SACRED JAPAN ／ GUIDE</div>
          <div class="related-card-title">🍜 Japanese Noodles Guide →</div>
          <div class="related-card-desc">Soba, udon, yakisoba, somen and cold ramen, with photos.</div>
        </a>
        <a class="related-card" href="/culture/yakitori/" onclick="trackEvent('click','internal','related_bread_to_yakitori')">
          <div class="related-card-label">SACRED JAPAN ／ GUIDE</div>
          <div class="related-card-title">🍢 Yakitori Guide →</div>
          <div class="related-card-desc">Cuts, salt versus sauce and how to order at an izakaya.</div>
        </a>
      </div>
    </section>

    <p style="font-size:14px;color:var(--enshu);line-height:1.7;margin-top:32px;"><strong>Sources:</strong> anpan from {NP} and {JT}; melonpan from {TW}; curry bread from {FIJ}; yakisoba-pan from {TT}; agepan from {NPL}; korokke pan from {FIK} and {TTK}; sandwiches from {JTA} and {TTF}; ogura toast from {JP}. Photograph details come from the Wikimedia Commons descriptions. I have not verified current shop details or prices.</p>

  </article>

</main>'''

t=open(f'{R}/_tools/culture/tea.py',encoding='utf-8').read()
tail=t[t.index("s=open(f'{R}/culture/omamori-guide"):]
tail=tail.replace('<div class="hero-bg-kanji">茶道</div>','<div class="hero-bg-kanji">パン</div>')
tail=tail.replace('<h1>The Japanese <em>Tea Ceremony</em> Guide</h1>','<h1>The <em>Bread</em> Guide</h1>')
tail=tail.replace('<div class="hero-jp">茶道ガイド</div>','<div class="hero-jp">パンガイド</div>')
tail=tail.replace('What Happens, What to Do as a Guest, and Where to Try It','Anpan, Melonpan, Curry Bread and Sandwiches')
tail=tail.replace('Tea Ceremony Guide','Bread Guide')
tail=tail.replace('guide_tea','guide_bread').replace('viator_guide_tea_sticky','viator_guide_bread_sticky').replace('japanese+tea+ceremony','Japan+food+tour')
tail=re.sub(r'(<meta name="keywords" content=")[^"]*(")',r'\1Japanese bread, anpan, melonpan, curry bread, yakisoba pan, agepan, tamago sando, fruit sando, ogura toast\2',tail)
exec(tail)
