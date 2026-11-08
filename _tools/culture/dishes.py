import re, os, json
from PIL import Image
R='/home/claude/sacred-japan'
A='/mnt/user-data/attachments/fd332c08-3f6b-545a-883b-83277e19ff52/'
S='popular-dishes'
OUT=f'{R}/culture/{S}'
os.makedirs(OUT+'/images',exist_ok=True)
photos={'sukiyaki':('49dfefd0-image.jpg',1200),'tempura-shrimp':('ccf78fa5-image.jpg',1000),'tempura-kappo':('b94fcb14-image.jpg',1000),'tendon':('d724f688-image.jpg',800),'gyudon':('e6bfb76d-image.jpg',640),'oyakodon':('a0369d50-image.jpg',1000)}
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
BYSA2=lic('CC BY-SA 2.0','https://creativecommons.org/licenses/by-sa/2.0/')
VIA='via Wikimedia Commons (resized)'
f_suki=fig('sukiyaki','A shallow iron pot with raw marbled beef slices, napa cabbage, pale grilled tofu, halved leeks, thin clear noodles, green leaves and two golden rectangular pieces, sitting in dark sauce on a round metal ring','Sukiyaki in its shallow iron pot, before the cooking is finished.',f'Photo: pelican, {BYSA2}, 1 June 2012 (Flickr, license reviewed on Commons). Commons titles it "Sukiyaki". {VIA}',hero=True)
f_t1=fig('tempura-shrimp','A heap of golden tempura on white paper: a large shrimp with its tail up, a purple eggplant cut into a fan, a green pepper and a piece with a red coating, against a dark background','A tempura plate with shrimp, eggplant and a green pepper.',f'Photo: Nesnad, {CC0}, 31 December 2007. Commons says it was shared as a free-use image of tempura. {VIA}',maxw=700)
f_t2=fig('tempura-kappo','Tempura on a blue-and-white scalloped plate lined with white paper: shrimp with tails up, long slices of vegetable and a frilly green piece, with a small dish of dark dipping sauce behind','Mixed tempura with a small dish of dipping sauce.',f'Photo: Norio NAKAYAMA, {BYSA2}, 24 February 2014 (Flickr, license reviewed on Commons). Commons gives the venue as Kappo Uosen in Nagaoka, Niigata. {VIA}',maxw=700)
f_tendon=fig('tendon','A round bowl with a dark blue rim holding rice topped with a large shrimp tempura, slices of pumpkin and a green vegetable, all glazed in brown sauce','A tendon bowl: tempura glazed with sauce on rice.',f'Photo: 毒島みるく, {CC0}, 4 January 2019. Commons describes it as the tendon from Tenya, priced at 540 yen. {VIA}',maxw=520)
f_gyu=fig('gyudon','Sliced beef and onion in brown sauce on rice in a white bowl with a blue pattern, topped with a pile of red pickled ginger, with a small cup holding a raw egg in the upper right','Gyudon with red pickled ginger and a raw egg on the side.',f'Photo: jetalone, {BY2}, 2 October 2006 (Flickr, license reviewed on Commons). Commons says it is a regular-size bowl with an egg at a Yoshinoya near Higashi-Ginza, Tokyo. {VIA}',maxw=640)
f_oya=fig('oyakodon','A white bowl of chicken and softly set egg in a glossy brown sauce, topped with a three-leaf green garnish and chopped green onion, on a wooden tray with a small dish of pickles','Oyakodon: chicken and egg over rice.',f'Photo: Ocdp, {CC0}, 7 June 2019. Commons describes it as a Suigo chicken oyakodon at a restaurant called Suigo no Toriyasan in Katori, Chiba. {VIA}',maxw=640)
def link(href,txt,lab): return f'<a href="{href}" class="inline-link" onclick="trackEvent(\'click\',\'internal\',\'{lab}\')">{txt}</a>'
def ext(href,txt,lab): return f'<a href="{href}" target="_blank" rel="noopener" onclick="trackEvent(\'click\',\'external\',\'{lab}\')">{txt}</a>'
VI='https://www.viator.com/search/Japan+food+tour?pid=P00298374&amp;mcid=42383&amp;medium=link&amp;campaign=sacred-japan'
SA=ext('https://arigatojapan.co.jp/sukiyaki-contrasts-kansai-kanto/','Arigato Japan','dishes_arigato')
SW=ext('https://en.wikipedia.org/wiki/Sukiyaki','Wikipedia','dishes_wiki_sukiyaki')
TJ=ext('https://www.jeepe.jp/en/articles/tempura-basic-guide-1629','Jeepe','dishes_jeepe')
TK=ext('https://www.kikkoman.com/en/cookbook/glossary/tenpura.html','Kikkoman','dishes_kikkoman')
TON=ext('https://gov-online.go.jp/eng/publicity/book/hlj/html/201810/201810_08_en.html','Highlighting Japan (Government of Japan)','dishes_hlj_tonkatsu')
KJT=ext('https://japantimes.co.jp/life/2021/03/20/food/fried-chicken-kara-age-zangi','Japan Times','dishes_japantimes')
KFJ=ext('https://foodinjapan.org/japan/karaage','Food in Japan','dishes_foodinjapan')
GYU=ext('https://gov-online.go.jp/eng/publicity/book/hlj/html/201202/201202_07.html','Highlighting Japan (Government of Japan)','dishes_hlj_gyudon')
OYA=ext('https://en.wikipedia.org/wiki/Oyakodon','Wikipedia','dishes_wiki_oyakodon')
KAT=ext('https://en.wikipedia.org/wiki/Katsudon','Wikipedia','dishes_wiki_katsudon')
faqs=[
("What is the difference between tempura and karaage?","Tempura is seafood or vegetables coated in a thin batter of wheat flour, egg and cold water, and then deep-fried, according to Jeepe. Karaage is usually boneless chicken that is marinated, coated with flour or potato starch and deep-fried, and the Japan Times notes there is no batter."),
("Is tempura really from Portugal?","It is often said to be. Jeepe says tempura is said to trace back to the 16th century, when Portuguese traders introduced deep-frying, and presents this as tradition. Kikkoman says a predecessor first appeared in Nagasaki in the early Momoyama period (1568-1600) and later reached Osaka and then Edo, where it became street food. The origin of the name is uncertain."),
("What is the difference between Kanto and Kansai sukiyaki?","In the Kanto style, a sauce called warishita (soy sauce, sugar, sake and mirin) is heated first and everything is simmered in it. In the Kansai style, the beef is seared first and the sugar, sake and soy sauce go in afterward, with the vegetables added last. Both styles dip the cooked food in raw beaten egg."),
("Do I have to eat the raw egg with sukiyaki?","No rule says so, but it is the standard way, and both regional styles use it. Arigato Japan says the egg cools the hot meat and adds a creamy coating in Kansai, and softens the sweetness of the broth in Kanto. If you avoid raw egg, tell the staff when you order."),
("What does oyakodon mean?","Oyakodon (親子丼) is literally a parent-and-child rice bowl, because it uses both chicken and egg. Wikipedia says its origin is subject to several theories, and one widely cited account links it to the Tokyo restaurant Tamahide in 1891."),
("What is katsudon, and why do students eat it?","Katsudon is a pork cutlet over rice. In the standard version the cutlet is simmered in a dashi and soy broth with onion and beaten egg, and regional versions use a sauce instead. Wikipedia says students eat it before exams because katsu sounds like the word for winning, and presents this as a modern tradition."),
]
faq_html=''.join(f'''      <details class="faq-item">
        <summary>{q}</summary>
        <div class="faq-answer">{a}</div>
      </details>

''' for q,a in faqs)
faq_ld=json.dumps({"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in faqs]},ensure_ascii=False,indent=2)
TITLE="Popular Japanese Dishes Guide: Sukiyaki, Tempura, Tonkatsu, Karaage and Rice Bowls"
DESC="A licensed guide's English introduction to popular Japanese dishes: sukiyaki (Kanto and Kansai styles), tempura and tendon, tonkatsu, karaage, gyudon, oyakodon and katsudon, with photographs and ordering tips."
URL=f"https://sacred-japan.net/culture/{S}/"
OG="https://sacred-japan.net/images/og/og-culture-popular-dishes.jpg"
main=f'''<main>

  {f_suki}

  <aside class="toc" aria-label="Table of contents">
    <div class="toc-label">TABLE OF CONTENTS ／ 目次</div>
    <div class="toc-title">In This Guide</div>
    <ol>
      <li><a href="#opening">Opening: A Note from the Guide</a></li>
      <li><a href="#glance">The Dishes at a Glance</a></li>
      <li><a href="#sukiyaki">Sukiyaki: The Hot Pot with a Raw Egg</a></li>
      <li><a href="#tempura">Tempura: Light Batter, Fried to Order</a></li>
      <li><a href="#tonkatsu">Tonkatsu: A Western Dish Made Japanese</a></li>
      <li><a href="#karaage">Karaage: Japanese Fried Chicken</a></li>
      <li><a href="#donburi">Rice Bowls: Gyudon, Oyakodon, Katsudon and Tendon</a></li>
      <li><a href="#how">How to Order and Eat</a></li>
      <li><a href="#faq">Frequently Asked Questions</a></li>
      <li><a href="#final">Final Thoughts</a></li>
    </ol>
  </aside>

  <article>

    <section id="opening">
      <p class="opening">Sushi and ramen get the headlines, but a lot of what people eat in Japan every week is fried, simmered or piled on rice. These are the dishes I end up explaining most at the table.</p>
      <p>As a licensed guide, I find that visitors recognize the names (tempura, tonkatsu, sukiyaki) but not the differences between the styles. This guide covers the main ones, with photographs of the dishes where I have a good one, and it says where the sources disagree.</p>
    </section>

    <h2 id="glance">The Dishes at a Glance<span class="h2-jp">料理の種類</span></h2>
    <ul>
      <li><strong>Sukiyaki (<span class="jp">すき焼き</span>):</strong> thin beef, tofu and vegetables simmered at the table, dipped in raw egg.</li>
      <li><strong>Tempura (<span class="jp">天ぷら</span>):</strong> seafood and vegetables in a thin batter, deep-fried.</li>
      <li><strong>Tonkatsu (<span class="jp">とんかつ</span>):</strong> a breaded, deep-fried pork cutlet served with shredded cabbage.</li>
      <li><strong>Karaage (<span class="jp">唐揚げ</span>):</strong> marinated chicken pieces, lightly coated and deep-fried.</li>
      <li><strong>Donburi (<span class="jp">丼</span>):</strong> a bowl of rice with a topping: gyudon (beef), oyakodon (chicken and egg), katsudon (pork cutlet) and tendon (tempura).</li>
    </ul>

    <h2 id="sukiyaki">Sukiyaki: The Hot Pot with a Raw Egg<span class="h2-jp">すき焼き</span></h2>
    <p>Sukiyaki is thinly sliced beef cooked at the table in a shallow iron pot with other ingredients, then dipped into a bowl of beaten raw egg. The {SW} lists the usual ingredients as seared tofu, <em>negi</em> (a type of scallion), Chinese cabbage, <em>shungiku</em> (garland chrysanthemum leaves), shiitake and enokitake mushrooms, and <em>shirataki</em> noodles. The sauce is a mix of soy sauce, sugar and mirin, with sake and dashi added in the Kanto version.</p>
    <p>The photograph at the top of this page shows a pot before the cooking is done. Commons titles it simply "Sukiyaki." On the left are slices of well-marbled beef, then napa cabbage, pale blocks that look like grilled tofu, two halves of leek, clear noodles that look like shirataki and a sprig of green leaves. I cannot tell what the two golden rectangles with a stamped pattern are, so I will not guess.</p>
    <h3>Kanto and Kansai</h3>
    <p>The two regions cook it differently. In the Kanto style, a sauce called <em>warishita</em> (soy sauce, sugar, sake and mirin) is heated first and the meat and vegetables simmer in it from the start. In the Kansai style, the beef is seared first, then sugar, sake and soy sauce are added, and the vegetables go in later. {SA} describes the Kansai way as searing the beef in a lightly greased pan and letting the sugar and soy sauce form a glaze directly on the meat.</p>
    <p>Both styles dip the cooked food in raw beaten egg. {SA} says the egg cools the seared meat and adds a creamy coating in Kansai, and softens the sweetness of the broth in Kanto. If you do not eat raw egg, say so when you order.</p>
    <h3>A Short History</h3>
    <p>The {SW} says sukiyaki developed in the Meiji era (1868-1912), after centuries of restrictions on eating beef, and that it was previously known as <em>gyunabe</em>, "beef pot." Both it and {SA} say the Kansai style spread to Tokyo after the 1923 Great Kanto Earthquake. The name itself is unclear: one theory ties it to <em>suki</em>, a spade, but the Wikipedia article notes that some doubt this.</p>
    <p>It is a restaurant dish more than a quick meal. The two Tokyo specialists described by {SA} list ¥15,000 to ¥20,000 and ¥20,000 to ¥33,000, and the article does not say whether that is per person, so confirm when you book.</p>

    <h2 id="tempura">Tempura: Light Batter, Fried to Order<span class="h2-jp">天ぷら</span></h2>
    <p>{TJ} describes the batter as wheat flour, egg and ice-cold water, kept thin so the coating is light and crisp, in contrast to the panko breading of <em>katsu</em>. Typical seafood includes shrimp, squid, <em>kisu</em> (Japanese whiting) and <em>anago</em> (saltwater eel). Vegetables include pumpkin, sweet potato, eggplant, lotus root, shiitake, shishito peppers and shiso leaves.</p>
    {f_t1}
    <p>The plate above shows a shrimp standing tail-up, an eggplant cut into a fan, a green pepper and a piece with a red coating that I cannot identify. Commons says it was shared as a free-use image of tempura and does not say where it was taken.</p>
    <h3>Where It Comes From</h3>
    <p>{TJ} says tempura is said to trace back to the 16th century, when Portuguese traders brought deep-frying to Japan, and presents this as tradition. {TK} says a predecessor first appeared in Nagasaki in the early Momoyama period (1568-1600), reached Osaka as <em>tsuke-age</em>, which was fried in sesame oil, and then became a popular street food in Edo. Both sources say the origin of the name is uncertain. In the Edo period it was sold at stalls (<em>yatai</em>) before it moved into specialist restaurants.</p>
    {f_t2}
    <p>This second plate has shrimp, long slices of vegetable and a frilly green piece, with a small dish of dipping sauce behind. Commons gives the venue as Kappo Uosen in Nagaoka, Niigata, and I do not know which vegetables these are, so I will not name them.</p>
    <h3>How to Eat It</h3>
    <p>The usual dip is <em>tentsuyu</em>, made from dashi, soy sauce and mirin, often with grated daikon or ginger to stir in, according to {TJ}. Some restaurants offer flavored salts instead, such as matcha, curry or yuzu. The same page advises eating each piece right away because the batter loses its crispness, and using seasoning sparingly. At a counter restaurant the chef typically serves one piece at a time as it is fried, and it is polite to ask before taking photos.</p>
    <h3>Tendon: Tempura on Rice</h3>
    <p>Tendon is a bowl of rice topped with tempura and a sweet-savory sauce. It is one of the cheaper ways to eat tempura: {TJ} gives 500 to 1,500 yen for casual chains and station eateries in one section and 1,000 to 2,000 yen in another, so check the menu. The bowl below is labeled on Commons as a Tenya tendon at 540 yen in January 2019, so prices today may be higher.</p>
    {f_tendon}

    <h2 id="tonkatsu">Tonkatsu: A Western Dish Made Japanese<span class="h2-jp">とんかつ</span></h2>
    <p>Tonkatsu is a breaded, deep-fried pork cutlet, usually served with a heap of shredded cabbage. The {TON} says it was created at Rengatei, a Western-style restaurant in Ginza that opened in 1895, and that "pork cutlet" appeared on its menu in 1899. It descends from the French <em>côtelette</em> of veal, which Rengatei found too oily for Japanese tastes, so the chef deep-fried the breaded cutlet as in tempura and switched to soft fresh panko.</p>
    <p>The cabbage has a story too. The same article says Rengatei replaced the hand-cut potatoes and carrots that came with the meat by finely chopped cabbage, to deal with a lack of cooks. The demi-glace was replaced by a mix of two imported Worcestershire sauces, which suited Japanese tastes better. The article also says tonkatsu led to the <em>katsu</em> sandwich and katsu curry.</p>

    <h2 id="karaage">Karaage: Japanese Fried Chicken<span class="h2-jp">唐揚げ</span></h2>
    <p>Karaage is chicken pieces that are marinated, coated in flour or potato starch, and deep-fried. {KJT} says it is usually boneless chicken, coated with flour, potato starch (<em>katakuriko</em>) or both, and that it has no batter, which is one reason some people write the first character as 空, "air." {KFJ} gives a typical marinade of soy sauce, sake, ginger and often garlic, and says the pieces are fried twice, first at a lower temperature and then hotter for the crust.</p>
    <p>It shows up everywhere: convenience-store counters, izakaya, set meals and bento, and shops that sell it by weight. {KFJ} says it is usually served with lemon and shredded cabbage, and sometimes mayonnaise, especially in Kansai.</p>
    <h3>Where Did It Start?</h3>
    <p>{KJT} dates the first appearance of the dish to 1932, at Mikasa Kaikan, a chicken specialty restaurant in Ginza, but this comes from the Japan Karaage Association and the page gives no independent confirmation. {KFJ} calls it a frequently cited account. The city of Nakatsu in Oita calls itself the "sacred ground" of karaage, a claim made by the town itself, and the same page says local accounts trace boneless karaage to Chinese restaurants in nearby Usa after World War II.</p>
    <p>A close cousin is <em>tatsuta-age</em>, marinated in soy sauce and coated in potato starch only. The Japan Times reports disagreement about how it differs from karaage, since some karaage recipes use only potato starch too.</p>

    <h2 id="donburi">Rice Bowls: Gyudon, Oyakodon, Katsudon and Tendon<span class="h2-jp">丼</span></h2>
    <p><em>Donburi</em> means a bowl of rice with a topping. It is the dish you can eat alone, quickly and cheaply, and many chains specialize in one bowl.</p>
    <h3>Gyudon: Beef Bowl</h3>
    <p>Gyudon is sliced beef and onion in a sweet soy sauce on rice. The {GYU} says Yoshinoya was founded in 1899 at a fish market in Nihonbashi, Tokyo, and that beef eating spread in the Meiji period, which is when gyudon emerged as a way for ordinary people to eat beef. In the 1970s chains began selling it as fast food, and the article says more than 4,000 chain outlets operate nationwide, including Sukiya, Yoshinoya, Matsuya and Nakau.</p>
    {f_gyu}
    <p>The photo is an older one, from 2006, so menus and prices have changed. You can see the pile of red pickled ginger on top and a cup holding a raw egg, which is a common add-on.</p>
    <h3>Oyakodon: Chicken and Egg</h3>
    <p>The name 親子丼 means "parent-and-child bowl," because it uses chicken and egg together. According to the {OYA}, the chicken, egg and sliced scallion (sometimes onion) are simmered in a soy and stock sauce and served over rice. The page says the origins are subject to several theories. One widely cited account credits Toku, wife of the fifth-generation owner of the Tokyo restaurant Tamahide, who turned a customer's leftover chicken and egg dish into a full rice bowl in 1891. The same article mentions an 1884 Kobe newspaper ad that lists oyako-don dishes.</p>
    {f_oya}
    <h3>Katsudon: Pork Cutlet Bowl</h3>
    <p>In the standard version described on {KAT}, a tonkatsu cutlet is sliced and simmered in a broth of dashi, soy sauce and onion with beaten egg, then served over rice. The page gives no date or inventor for the dish. It lists regional sauce versions instead, with tonkatsu or Worcestershire sauce, in places such as Fukui, Kofu, Gunma, Aizuwakamatsu and Komagane. The same page says students eat katsudon before exams because <em>katsu</em> sounds like 勝つ, "to win," and presents this as a modern tradition.</p>
    <p>Tendon is covered in the tempura section above.</p>

    <h2 id="how">How to Order and Eat<span class="h2-jp">注文と食べ方</span></h2>
    <p>These are my own habits as a guide, not strict rules.</p>
    <ol>
      <li><strong>Mention allergies and raw egg.</strong> Shrimp, wheat and egg appear in many of these dishes, and sukiyaki and some bowls come with raw egg.</li>
      <li><strong>Eat fried food fast.</strong> Tempura, tonkatsu and karaage are best while the coating is crisp.</li>
      <li><strong>Check the style.</strong> Sukiyaki, katsudon and oyakodon vary by region and restaurant, so the menu photo is the best guide.</li>
      <li><strong>Confirm prices.</strong> Dishes like sukiyaki and counter tempura can cost much more than a chain bowl.</li>
    </ol>
    <div style="background:var(--washi-dark);border-left:4px solid var(--kin);padding:16px 20px;margin:24px 0;border-radius:2px;">
      <p style="margin:0;">&#127836; <strong>Plan your trip:</strong> Looking for a guide to the food scene? <a href="{VI}" target="_blank" rel="noopener sponsored" onclick="trackEvent('click','affiliate','viator_dishes_local')">Browse Japan food tours on Viator &rarr;</a></p>
    </div>

    <h2 id="faq">Frequently Asked Questions<span class="h2-jp">よくあるご質問</span></h2>

    <div class="faq-stack">

{faq_html}    </div>

    <h2 id="final">Final Thoughts<span class="h2-jp">むすびに</span></h2>
    <p>Learn five words (すき焼き, 天ぷら, とんかつ, 唐揚げ, 丼) and you can read most of a casual menu. Then pick one you have not had, and ask what the local style is.</p>
    <p>For more dishes tied to places, see our {link('/regional-food/','guide to regional cuisine','dishes_to_regional_food')}.</p>

    <div class="closing-block">
      <span class="torii">🍱</span>
      <p>A hot pot, a crisp batter and a bowl of rice.</p>
    </div>

    <section class="related-section">
      <h2>Related Guides</h2>
      <span class="h2-jp">関連ガイド</span>
      <div class="related-grid">
        <a class="related-card" href="/culture/noodles/" onclick="trackEvent('click','internal','related_dishes_to_noodles')">
          <div class="related-card-label">SACRED JAPAN ／ GUIDE</div>
          <div class="related-card-title">🍜 Japanese Noodles Guide →</div>
          <div class="related-card-desc">Soba, udon, yakisoba, somen and cold ramen, with photos.</div>
        </a>
        <a class="related-card" href="/culture/ramen/" onclick="trackEvent('click','internal','related_dishes_to_ramen')">
          <div class="related-card-label">SACRED JAPAN ／ GUIDE</div>
          <div class="related-card-title">🍥 Japanese Ramen Guide →</div>
          <div class="related-card-desc">Shoyu, miso, shio and tonkotsu explained, with a photo of each bowl.</div>
        </a>
        <a class="related-card" href="/regional-food/" onclick="trackEvent('click','internal','related_dishes_to_food')">
          <div class="related-card-label">SACRED JAPAN ／ GUIDE</div>
          <div class="related-card-title">🍽️ Japan's Regional Cuisine →</div>
          <div class="related-card-desc">Dishes from Hokkaido to Okinawa.</div>
        </a>
      </div>
    </section>

    <p style="font-size:14px;color:var(--enshu);line-height:1.7;margin-top:32px;"><strong>Sources:</strong> sukiyaki from {SA} and the {SW}; tempura from {TJ} and {TK}; tonkatsu from the {TON}; karaage from the {KJT} and {KFJ}; gyudon from the {GYU}; oyakodon and katsudon from Wikipedia ({OYA}, {KAT}). Photograph details come from the Wikimedia Commons descriptions. I have not verified current prices.</p>

  </article>

</main>'''
t=open(f'{R}/_tools/culture/tea.py',encoding='utf-8').read()
tail=t[t.index("s=open(f'{R}/culture/omamori-guide"):]
tail=tail.replace('<div class="hero-bg-kanji">茶道</div>','<div class="hero-bg-kanji">食</div>')
tail=tail.replace('<h1>The Japanese <em>Tea Ceremony</em> Guide</h1>','<h1>Popular Japanese <em>Dishes</em> Guide</h1>')
tail=tail.replace('<div class="hero-jp">茶道ガイド</div>','<div class="hero-jp">人気の日本料理ガイド</div>')
tail=tail.replace('What Happens, What to Do as a Guest, and Where to Try It','Sukiyaki, Tempura, Tonkatsu, Karaage and Rice Bowls')
tail=tail.replace('Tea Ceremony Guide','Dishes Guide')
tail=tail.replace('guide_tea','guide_dishes').replace('viator_guide_tea_sticky','viator_guide_dishes_sticky').replace('japanese+tea+ceremony','Japan+food+tour')
tail=re.sub(r'(<meta name="keywords" content=")[^"]*(")',r'\1Japanese dishes, sukiyaki, tempura, tendon, tonkatsu, karaage, gyudon, oyakodon, katsudon, popular Japanese food\2',tail)
exec(tail)
