import re, os, json
from PIL import Image
R='/home/claude/sacred-japan'
A='/mnt/user-data/attachments/fd332c08-3f6b-545a-883b-83277e19ff52/'
S='noodles'
OUT=f'{R}/culture/{S}'
os.makedirs(OUT+'/images',exist_ok=True)
photos={'mori-soba':('8a68f241-image.jpg',1200),'cha-soba':('1f32f253-image.jpg',1000),'somen-ice':('afeac011-image.jpg',800),'hiyamugi-bowl':('066797f8-image.jpg',1000)}
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
BYSA4=lic('CC BY-SA 4.0','https://creativecommons.org/licenses/by-sa/4.0/')
VIA='via Wikimedia Commons (resized)'
f_mori=fig('mori-soba','A square black frame holding a bamboo mat piled with grey-brown soba noodles, beside a black cup of dark dipping sauce with a red inside and a small black dish of chopped scallions and a dab of green wasabi, on a tray','Mori soba: cold noodles, dipping sauce, scallions and wasabi.',f'Photo: 毒島みるく, {CC0}, 31 August 2019, {VIA}',hero=True)
f_cha=fig('cha-soba','A tall pile of green-tinted soba noodles topped with shredded dark nori on a black plate with a white-and-black slatted rest','Green-tea-flavored soba, topped with shredded nori.',f'Photo: Pauloleong2002, {BYSA4}, 13 August 2022, {VIA}',maxw=640)
f_somen=fig('somen-ice','Thin white noodles piled in a glass dish with ice cubes, a green leaf and a halved cherry tomato, in front of a red lacquer tray with sesame seeds, a green citrus, chopped scallions and a pale condiment','Somen on ice, with condiments in a red lacquer tray.',f'Photo: a.koto, {BY2}, 21 August 2007 (Flickr, license reviewed on Commons), {VIA}',maxw=640)
f_hiya=fig('hiyamugi-bowl','Pale thin noodles with ice cubes in an octagonal glass bowl with a fern pattern, next to a small pale-green cup of brown dipping sauce with mushrooms and small puffed bits, on a wooden table with a checked cloth','Hiyamugi with ice, and a cup of dipping sauce.',f'Photo: RuinDig / Yuki Uchida, {BY4}, 28 August 2023, {VIA}',maxw=640)
def link(href,txt,lab): return f'<a href="{href}" class="inline-link" onclick="trackEvent(\'click\',\'internal\',\'{lab}\')">{txt}</a>'
def ext(href,txt,lab): return f'<a href="{href}" target="_blank" rel="noopener" onclick="trackEvent(\'click\',\'external\',\'{lab}\')">{txt}</a>'
VI='https://www.viator.com/search/Japan+food+tour?pid=P00298374&amp;mcid=42383&amp;medium=link&amp;campaign=sacred-japan'
JG=ext('https://www.japan-guide.com/r/e104.html','japan-guide','noodles_japanguide')
NIP=ext('https://www.nippon.com/en/japan-data/h02034/somen-and-hiyamugi-defining-japanese-summer-noodles.html','Nippon.com','noodles_nippon')
WK=ext('https://en.wikipedia.org/wiki/Ramen','Wikipedia','noodles_wiki_ramen')
RTE=ext('https://japan.recipetineats.com/hiyashi-chuka-cold-ramen/','RecipeTin Japan','noodles_rte')
PRODBLOG=ext('https://japanese-products.blog/2018/03/22/zaru-soba-mori-soba-seiro-soba','Japanese Products blog','noodles_products')
faqs=[
("What is the difference between soba, somen and hiyamugi?","Soba is made from buckwheat flour, and many shops add some wheat flour. Somen and hiyamugi are both thin wheat noodles. Under Japanese Agricultural Standards for machine-made dry noodles, somen is under 1.3 mm in diameter and hiyamugi is from 1.3 mm to under 1.7 mm."),
("What is the difference between zaru soba and mori soba?","Both are cold soba served with a dipping sauce. Today the main difference is that zaru soba is topped with shredded nori and mori soba is not, according to japan-guide. Some shops do not follow this rule, so check the menu."),
("What is cha soba?","Cha soba is soba flavored with green tea. The photograph in this guide is described on Wikimedia Commons as soba noodles in green tea flavor. It is a specialty, and not every soba shop serves it."),
("What is soba-yu?","Soba-yu is the water the noodles were boiled in. Some shops bring it in a small teapot near the end of the meal. You pour it into your leftover dipping sauce and drink it."),
("Is soba gluten-free?","Not necessarily. Many shops mix wheat flour with buckwheat, with the buckwheat share typically between 40 and 100 percent according to japan-guide. If you have an allergy to wheat or to buckwheat, tell the staff before you order."),
]
faq_html=''.join(f'''      <details class="faq-item">
        <summary>{q}</summary>
        <div class="faq-answer">{a}</div>
      </details>

''' for q,a in faqs)
faq_ld=json.dumps({"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in faqs]},ensure_ascii=False,indent=2)
TITLE="Japanese Noodles Guide: Soba, Somen, Hiyamugi and Cold Ramen"
DESC="A licensed guide's English introduction to Japanese noodles beyond ramen: soba, green tea soba, somen, hiyamugi, hiyashi chuka and chuka soba, with photographs and simple tips for ordering."
URL=f"https://sacred-japan.net/culture/{S}/"
OG="https://sacred-japan.net/images/og/og-culture-noodles.jpg"
main=f'''<main>

  {f_mori}

  <aside class="toc" aria-label="Table of contents">
    <div class="toc-label">TABLE OF CONTENTS ／ 目次</div>
    <div class="toc-title">In This Guide</div>
    <ol>
      <li><a href="#opening">Opening: A Note from the Guide</a></li>
      <li><a href="#glance">The Noodles at a Glance</a></li>
      <li><a href="#soba">Soba: Buckwheat Noodles</a></li>
      <li><a href="#cha-soba">Cha Soba: Green Tea Soba</a></li>
      <li><a href="#summer">Somen and Hiyamugi: Summer Wheat Noodles</a></li>
      <li><a href="#hiyashi">Hiyashi Chuka: Chilled Ramen Noodles</a></li>
      <li><a href="#chuka-soba">Chuka Soba: A Name for Ramen</a></li>
      <li><a href="#faq">Frequently Asked Questions</a></li>
      <li><a href="#final">Final Thoughts</a></li>
    </ol>
  </aside>

  <article>

    <section id="opening">
      <p class="opening">After ramen, the next question I hear from travelers is about the thin, cold noodles on a tray. Are they soba? Somen? Something else?</p>
      <p>As a licensed guide, I think these cold noodles are the best way to eat in Japanese summer, and they are cheap and quick. This guide separates the names you will see on menus, with a photograph of each where I have a good one.</p>
    </section>

    <h2 id="glance">The Noodles at a Glance<span class="h2-jp">麺の種類</span></h2>
    <ul>
      <li><strong>Soba (<span class="jp">蕎麦</span>):</strong> buckwheat noodles, often with some wheat flour. Hot or cold.</li>
      <li><strong>Cha soba (<span class="jp">茶そば</span>):</strong> soba flavored with green tea.</li>
      <li><strong>Somen (<span class="jp">素麺</span>):</strong> very thin white wheat noodles, served chilled in summer.</li>
      <li><strong>Hiyamugi (<span class="jp">冷麦</span>):</strong> thin wheat noodles, slightly thicker than somen.</li>
      <li><strong>Hiyashi chuka (<span class="jp">冷やし中華</span>):</strong> chilled ramen-style noodles with cold toppings.</li>
      <li><strong>Chuka soba (<span class="jp">中華そば</span>):</strong> a name for ramen, often the classic style.</li>
    </ul>

    <h2 id="soba">Soba: Buckwheat Noodles<span class="h2-jp">蕎麦</span></h2>
    <p>{JG} describes soba as noodles made of buckwheat flour, roughly as thick as spaghetti. Because pure buckwheat noodles tend to be brittle, many shops add wheat flour, and the buckwheat share typically falls between 40 and 100 percent depending on the shop. Soba can be served hot in broth or cold with a dipping sauce.</p>
    <p>The photograph at the top of this page shows <em>mori soba</em>, the plainest cold soba. Commons titles it as mori soba at a Fuji Soba shop, and you can see the noodles piled on a bamboo mat, a cup of dipping sauce and a small dish of chopped scallions with a dab of wasabi. This is the standard set-up: stir the scallions and wasabi into the sauce, dip the noodles and slurp.</p>
    <h3>Zaru or Mori?</h3>
    <p>Both are cold soba with a dipping sauce. According to {JG}, the main difference today is that zaru soba has shredded nori on top and mori soba does not. The {PRODBLOG} adds that the names once referred to the dish, a bamboo basket for zaru and piled noodles for mori, and that modern restaurants do not always follow the old rules. I would read the menu description, not the name.</p>
    <h3>The Sauce and Soba-yu</h3>
    <p>The dipping sauce, called <em>tsuyu</em>, is usually a mix of soup stock, water and mirin, served chilled. Some shops serve <em>soba-yu</em>, the water the noodles were boiled in, in a small teapot at the end. Pour some into your leftover sauce and drink it. Simple soba dishes typically cost 500 to 1,000 yen according to {JG}, which does not date the figure, so check the menu.</p>

    <h2 id="cha-soba">Cha Soba: Green Tea Soba<span class="h2-jp">茶そば</span></h2>
    {f_cha}
    <p>Cha soba is soba flavored with green tea. Commons describes this photograph simply as soba noodles in green tea flavor and does not name the shop. The noodles have a clear green-olive tint, and they are topped with shredded nori on a slatted rest, much like a zaru soba. I will not describe the taste, because I have not tried this bowl, but the color alone tells you it is different from plain soba. If you see 茶そば on a menu, this is what you are ordering.</p>

    <h2 id="summer">Somen and Hiyamugi: Summer Wheat Noodles<span class="h2-jp">素麺と冷麦</span></h2>
    <p>Somen and hiyamugi are both wheat noodles served chilled as a summer meal. The {NIP} says both are made from wheat flour, salt and water, and that somen dough is twisted and stretched to make it thinner. It also gives the size rule for machine-made dry noodles under Japanese Agricultural Standards: somen is under 1.3 mm in diameter, hiyamugi is 1.3 mm to under 1.7 mm, and udon is 1.7 mm and over.</p>
    <h3>Somen</h3>
    {f_somen}
    <p>Commons describes this photograph as a meal of the summer, very cold, somen. The thin white noodles sit on ice with a green leaf and a halved cherry tomato. In the red lacquer tray in front are sesame seeds, a green citrus that looks like a lime or sudachi, and chopped scallions. At the right edge there is something pale yellow that may be grated ginger, but I cannot be sure. You would squeeze the citrus, mix the condiments into the cold dipping sauce and dip the noodles.</p>
    <h3>Hiyamugi</h3>
    {f_hiya}
    <p>Commons titles this a photograph of hiyamugi. The noodles are pale and slightly thicker than somen, in a glass bowl with ice. The cup of sauce at right looks to me like it holds mushrooms and small crunchy bits of tempura batter, but Commons does not say. Nippon.com adds that the name comes from <em>kirimugi</em>, a flattened and finely cut noodle, and that the same noodle in hot broth is called <em>atsumugi</em>. In practice, the two look alike on a plate. If the menu offers both, the difference is mostly thickness.</p>

    <h2 id="hiyashi">Hiyashi Chuka: Chilled Ramen Noodles<span class="h2-jp">冷やし中華</span></h2>
    <p>Hiyashi chuka is the summer dish that confuses visitors most, because it is not cold ramen soup. {RTE} describes it as cold Chinese-style egg noodles with four or five thinly cut toppings arranged in separate groups, such as cucumber, shredded egg crepe, bean sprouts and ham, and sometimes tomato or wakame. The sauce is a sweet-tart vinegar dressing, usually made from soy sauce, vinegar, sake, sugar and sesame oil.</p>
    <p>The same source says that despite the Chinese name it is a Japanese dish developed in the early 1930s, and that <em>chuka</em> was used to distinguish it from cold soba. It is mainly eaten in summer, and many shops put it on the menu only in warm months, so ask before you plan a trip around it.</p>

    <h2 id="chuka-soba">Chuka Soba: A Name for Ramen<span class="h2-jp">中華そば</span></h2>
    <p>The {WK} notes that ramen was renamed <em>shina soba</em> in 1910, and that after World War II the word <em>shina</em> became pejorative and was replaced by <em>chuka</em> in many terms. Chuka soba and ramen can be used interchangeably, though chuka soba is often used for more classic styles, and it remains common in places such as Takayama.</p>
    <p>So if you see 中華そば on a sign, expect a bowl of ramen, not soba made from buckwheat. For the four main ramen flavors, see our {link('/culture/ramen/','ramen guide','noodles_to_ramen')}. The shoyu bowl at the top of that guide was photographed at a shop called Chukasoba in Aomori.</p>

    <h2 id="how">How to Order and Eat<span class="h2-jp">注文と食べ方</span></h2>
    <p>These are my own habits as a guide, not strict rules.</p>
    <ol>
      <li><strong>Check the word.</strong> 蕎麦 or そば is buckwheat, 素麺 and 冷麦 are thin wheat, and 中華 means ramen-style noodles.</li>
      <li><strong>Eat cold noodles quickly.</strong> Ice melts, and the noodles get soft in water.</li>
      <li><strong>Slurp.</strong> It is normal, and japan-guide says it enhances flavor and cools the noodles.</li>
      <li><strong>Use the condiments.</strong> Scallions, wasabi, ginger, sesame and citrus go into the dipping sauce.</li>
      <li><strong>Tell the staff about allergies.</strong> Soba is buckwheat and often contains wheat.</li>
    </ol>
    <div style="background:var(--washi-dark);border-left:4px solid var(--kin);padding:16px 20px;margin:24px 0;border-radius:2px;">
      <p style="margin:0;">&#127836; <strong>Plan your trip:</strong> Looking for a guide to the food scene? <a href="{VI}" target="_blank" rel="noopener sponsored" onclick="trackEvent('click','affiliate','viator_noodles_local')">Browse Japan food tours on Viator &rarr;</a></p>
    </div>

    <h2 id="faq">Frequently Asked Questions<span class="h2-jp">よくあるご質問</span></h2>

    <div class="faq-stack">

{faq_html}    </div>

    <h2 id="final">Final Thoughts<span class="h2-jp">むすびに</span></h2>
    <p>Learn the kanji for soba, somen, hiyamugi and chuka and you can read most noodle menus. In summer, try one cold noodle you have not met before. It costs little, and it tells you a lot about how Japanese food changes with the season.</p>
    <p>For more dishes tied to places, see our {link('/regional-food/','guide to regional cuisine','noodles_to_regional_food')}.</p>

    <div class="closing-block">
      <span class="torii">🍜</span>
      <p>Cold noodles, a cup of sauce and a hot afternoon.</p>
    </div>

    <section class="related-section">
      <h2>Related Guides</h2>
      <span class="h2-jp">関連ガイド</span>
      <div class="related-grid">
        <a class="related-card" href="/culture/ramen/" onclick="trackEvent('click','internal','related_noodles_to_ramen')">
          <div class="related-card-label">SACRED JAPAN ／ GUIDE</div>
          <div class="related-card-title">🍜 Japanese Ramen Guide →</div>
          <div class="related-card-desc">Shoyu, miso, shio and tonkotsu explained, with a photo of each bowl.</div>
        </a>
        <a class="related-card" href="/regional-food/" onclick="trackEvent('click','internal','related_noodles_to_food')">
          <div class="related-card-label">SACRED JAPAN ／ GUIDE</div>
          <div class="related-card-title">🍽️ Japan's Regional Cuisine →</div>
          <div class="related-card-desc">Dishes from Hokkaido to Okinawa, including Sanuki udon.</div>
        </a>
      </div>
    </section>

    <p style="font-size:14px;color:var(--enshu);line-height:1.7;margin-top:32px;"><strong>Sources:</strong> soba from {JG} and the {PRODBLOG}; somen and hiyamugi from {NIP}; hiyashi chuka from {RTE}; chuka soba from {WK}. Photograph details come from the Wikimedia Commons descriptions. I have not verified current prices.</p>

  </article>

</main>'''
t=open(f'{R}/_tools/culture/tea.py',encoding='utf-8').read()
tail=t[t.index("s=open(f'{R}/culture/omamori-guide"):]
tail=tail.replace('<div class="hero-bg-kanji">茶道</div>','<div class="hero-bg-kanji">麺</div>')
tail=tail.replace('<h1>The Japanese <em>Tea Ceremony</em> Guide</h1>','<h1>Japanese <em>Noodles</em> Guide</h1>')
tail=tail.replace('<div class="hero-jp">茶道ガイド</div>','<div class="hero-jp">麺ガイド</div>')
tail=tail.replace('What Happens, What to Do as a Guest, and Where to Try It','Soba, Somen, Hiyamugi and Cold Ramen')
tail=tail.replace('Tea Ceremony Guide','Noodles Guide')
tail=tail.replace('guide_tea','guide_noodles').replace('viator_guide_tea_sticky','viator_guide_noodles_sticky').replace('japanese+tea+ceremony','Japan+food+tour')
tail=re.sub(r'(<meta name="keywords" content=")[^"]*(")',r'\1Japanese noodles, soba, zaru soba, mori soba, cha soba, somen, hiyamugi, hiyashi chuka, chuka soba, cold noodles Japan\2',tail)
exec(tail)
