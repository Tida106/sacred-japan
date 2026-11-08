import re, os, json
R='/home/claude/sacred-japan'
S='japanese-sweets'
OUT=f'{R}/culture/{S}'
os.makedirs(OUT,exist_ok=True)
def link(href,txt,lab): return f'<a href="{href}" class="inline-link" onclick="trackEvent(\'click\',\'internal\',\'{lab}\')">{txt}</a>'
def ext(href,txt,lab): return f'<a href="{href}" target="_blank" rel="noopener" onclick="trackEvent(\'click\',\'external\',\'{lab}\')">{txt}</a>'
VI='https://www.viator.com/search/Japan+food+tour?pid=P00298374&amp;mcid=42383&amp;medium=link&amp;campaign=sacred-japan'
TRIP=ext('https://www.triptojapan.com/blog/best-japanese-snacks-to-bring-home-as-gifts','Trip to Japan','sweets_triptojapan')
BYF=ext('https://byfood.com/blog/culture/japanese-food-souvenirs-regional-omiyage','byFood','sweets_byfood')
JW=ext('https://jw-webmagazine.com/tips/best-japanese-snacks','JW Web Magazine','sweets_jw')
ZEN=ext('https://zenmarket.jp/en/blog/post/9219/best-japanese-snacks','ZenMarket','sweets_zenmarket')
FUN=ext('https://www.fun-japan.jp/en/articles/14647','FUN! JAPAN','sweets_funjapan')
SORA=ext('https://soranews24.com/2025/01/30/7-eleven-japans-most-popular-product-with-foreign-tourists-is-a-unique-chocolate-gummy/','SoraNews24','sweets_soranews')
JPB=ext('https://japanese-products.blog/2017/03/29/the-2016-popularity-ranking-of-japanese-snacks-and-sweets','Japanese Products blog','sweets_jpblog')
MG=ext('https://news.allabout.co.jp/articles/o/62538/','All About News','sweets_allabout')
TV=ext('https://www.travelvoice.jp/english/sweets-become-popular-as-souvenirs-for-japan-among-international-visitors/print','Travel Voice','sweets_travelvoice')
items=[
('pocky','Pocky','ポッキー','Glico makes Pocky: thin biscuit sticks coated in chocolate, with one end left bare so you can hold it. '+f'{TRIP} says it has been popular since 1966 and lists matcha, almond crush and cookies-and-cream among the flavors. {ZEN} names Glico as the maker and mentions Japan-only flavors. The same {TRIP} article puts a standard box at about $2-3 and gift boxes at $10-20, so it is an easy cheap present. Check the label if you buy a flavor you cannot read.'),
('kitkat','Kit Kat (Japan-only flavors)','キットカット','Kit Kat is made by Nestlé, but Japan has its own huge flavor list. '+f'{TRIP} reports over 300 flavors released since 2000, including matcha, sake and wasabi, and {ZEN} adds houjicha as a year-round flavor. The name sounds like <em>kitto katsu</em>, meaning "you will surely win," which is why it is a popular good-luck gift for students before exams. {ZEN} says airports and souvenir shops carry the most unusual flavors.'),
('hichew','Hi-Chew','ハイチュウ','Hi-Chew is made by Morinaga. '+f'{ZEN} describes it as a soft, chewy candy in many fruit and sour flavors, comparable to Starburst. It packs flat, does not melt easily compared with chocolate, and is cheap, so it suits a bag of small gifts. Morinaga has an English-language website for international buyers, per {ZEN}.'),
('tokyobanana','Tokyo Banana','東京ばな奈','Small banana-shaped sponge cakes with banana custard cream. '+f'{TRIP} calls it Tokyo\'s most famous souvenir and puts a box of 8 at about $8-12, available at major Tokyo stations, airports and souvenir shops; {BYF} calls it the official souvenir of Tokyo. {TRIP} says it lasts about a week, up to two weeks if kept cool, so check the date on the box.'),
('shiroikoibito','Shiroi Koibito','白い恋人','Thin biscuits sandwiching white chocolate, made by Ishiya of Hokkaido ('+f'{BYF}), and it is a classic Hokkaido gift. {JW} includes it and lists a mixed biscuit set at 3,314 yen as of its last update, so this is one of the pricier items here; check the current price.'),
('yatsuhashi','Yatsuhashi','八ッ橋','Kyoto\'s signature sweet, made from glutinous rice flour, sugar and cinnamon. '+f'{TRIP} separates the hard, crunchy baked kind (<em>kaki yatsuhashi</em>) from the soft, triangular <em>nama yatsuhashi</em> with red bean filling, and says fresh nama lasts 5-7 days while packaged versions last 2-3 weeks. The same article says it has been Kyoto\'s signature sweet for over 300 years, which I could not confirm in a second source. The baked kind travels better.'),
('dorayaki','Dorayaki','どら焼き','Two fluffy pancakes sandwiching sweet red bean paste, with modern fillings such as chocolate, custard and matcha cream, per '+f'{TRIP}. It is famous as the favorite food of the cartoon robot cat Doraemon. The article says packaged versions last longer than fresh ones and are sold at convenience stores and supermarkets, so a packaged one is the safer souvenir.'),
('daifuku','Daifuku','大福','Smooth mochi wrapped around a filling. '+f'{TRIP} lists red bean paste, custard and chocolate, and ichigo daifuku, a whole strawberry with white bean paste. It says fresh daifuku lasts only 2-4 days, so it is a treat for the trip, not a gift for home. Department store basements and shops in places such as Asakusa sell it, according to the same article.'),
('senbei','Senbei (Kameda Seika)','せんべい・亀田製菓','Rice crackers, salty or sweet-salty. The big name is Kameda Seika. On its own English site, the company says it holds a 30% share of the domestic rice cracker market and has been the top company since 1975, which is its own claim. It lists long-selling brands such as <em>Kameda Kaki-no-Tane</em> and <em>Happy Turn</em>, and says the peanut version of Kaki-no-Tane went on sale in 1966. You find them in supermarkets and convenience stores. '+f'{ZEN} also recommends black bean senbei, and {BYF} notes regional types such as Nambu senbei from Iwate, a thin salty cracker often with sesame or peanut bits. For a gift that lasts, this is the safest pick on the list.'),
('castella','Castella','カステラ','A moist, dense, honey-flavored sponge cake. '+f'{BYF} says the Portuguese introduced castella to Nagasaki in the 16th century. {TRIP} names Fukusaya and Bunmeido as makers, says it is often sold in wooden boxes, lasts about 2-3 weeks and packs well, and puts the price at about $15-25. It is the most expensive item on this list.'),
]
OFF={
'senbei':('https://www.kamedaseika.co.jp/en/company/rice-cracker-business/','Kameda Seika: rice cracker business (English)','official_kameda'),
'pocky':('https://www.pocky.com/','Pocky official site (Ezaki Glico USA)','official_pocky'),
'hichew':('https://morinaga.co.jp/hi-chew/en','Morinaga: Hi-Chew (English)','official_hichew'),
'tokyobanana':('https://www.tokyobanana.jp/language/en/','Tokyo Banana official site (English)','official_tokyobanana'),
'shiroikoibito':('https://www.shiroikoibitopark.jp/en/','Shiroi Koibito Park website (listed as the official site by WAmazing)','official_shiroikoibito'),
'yatsuhashi':('https://8284.co.jp/foreigners/en.pdf','Honke Nishio Yatsuhashi English brochure (PDF)','official_yatsuhashi'),
}
cards=''
for i,(k,n,jp,txt) in enumerate(items,1):
    off=''
    if k in OFF:
        u,l,t=OFF[k]
        off=f'\n    <p><strong>Official link:</strong> {ext(u,l,t)}</p>'
    cards+=f'''    <h3 id="{k}">{i}. {n} <span class="jp">{jp}</span></h3>
    <p>{txt}</p>{off}
'''
faqs=[
("What is a good cheap Japanese sweet to bring home?","From the list in this guide, Pocky, Hi-Chew and Kit Kat are the easiest: small, light and sold at many shops. Trip to Japan puts a standard box of Pocky at about $2-3. Prices change, so check the label."),
("Which Japanese sweets last the longest?","Packaged senbei, Pocky, Hi-Chew and Kit Kat keep well. Castella lasts about 2-3 weeks and packaged yatsuhashi 2-3 weeks according to Trip to Japan. Fresh daifuku lasts only 2-4 days."),
("Why is Kit Kat a good-luck gift in Japan?","The name sounds like kitto katsu, meaning you will surely win, so it is a popular gift for students taking exams."),
("Are these sweets ranked by sales?","No. They are my picks as a guide. Sales data I found covers only parts of the market, such as sweets at Tokyo Station and 7-Eleven Japan's best seller with foreign tourists."),
("What do Japanese people themselves like to snack on?","Two surveys I found point to Calbee snacks such as Jagariko and potato chips, plus Meiji and Kit Kat items. One is a 2016 TV survey of 10,000 people and the other a 2023 survey of 1,000 people, so treat them as hints."),
("Can I bring Japanese sweets through customs at home?","Rules differ by country and by ingredients such as meat, dairy and eggs. Check your own country's customs rules before you travel."),
]
faq_html=''.join(f'''      <details class="faq-item">
        <summary>{q}</summary>
        <div class="faq-answer">{a}</div>
      </details>

''' for q,a in faqs)
faq_ld=json.dumps({"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in faqs]},ensure_ascii=False,indent=2)
TITLE="Japanese Sweets Souvenirs: 10 Cheap Favorites a Guide Recommends"
DESC="A licensed guide's picks for 10 cheap, popular Japanese sweets to bring home: Pocky, Kit Kat, Hi-Chew, Tokyo Banana, Shiroi Koibito, yatsuhashi, dorayaki, daifuku, senbei and castella, with shelf-life tips, plus what Japanese people snack on."
URL=f"https://sacred-japan.net/culture/{S}/"
OG="https://sacred-japan.net/images/og/og-culture-japanese-sweets.jpg"
toc=''.join(f'<li><a href="#{k}">{n}</a></li>' for k,n,_,_ in items)
main=f'''<main>

  <aside class="toc" aria-label="Table of contents">
    <div class="toc-label">TABLE OF CONTENTS ／ 目次</div>
    <div class="toc-title">In This Guide</div>
    <ol>
      <li><a href="#opening">Opening: A Note from the Guide</a></li>
      <li><a href="#what-sells">What Sells to Visitors</a></li>
      <li><a href="#picks">The 10 Picks</a></li>
      <li><a href="#locals">What Japanese People Snack On</a></li>
      <li><a href="#faq">Frequently Asked Questions</a></li>
      <li><a href="#final">Final Thoughts</a></li>
    </ol>
  </aside>

  <article>

    <section id="opening">
      <p class="opening">Every guest I take around Japan asks the same thing near the end of the trip: what small sweet can I bring home that people will actually like?</p>
      <p>This is my answer: ten cheap, popular sweets, with the shelf life of each, since that decides what survives the flight. The order is mine, not a sales ranking.</p>
    </section>

    <h2 id="what-sells">What Sells to Visitors<span class="h2-jp">人気の背景</span></h2>
    <p>Sweets are a big part of what visitors buy to take home. A Ministry of Agriculture, Forestry and Fisheries survey for 2017, reported by {TV}, put visitors' spending on sweets at 158.9 billion yen, 46% of their food souvenir spending. That survey does not name individual products.</p>
    <p>Two narrower data points: a {FUN} ranking of Tokyo Station sweets, based on May 2026 sales of year-round Gransta Tokyo exclusives, is led by sand cookies, and {SORA} reported in January 2025 that 7-Eleven Japan's top seller with foreign tourists was a Shine Muscat grape gummy chocolate at 149 yen. Both cover only one shop or one station, so I use them as color and not as a ranking of my list.</p>

    <h2 id="picks">The 10 Picks<span class="h2-jp">お菓子10選</span></h2>
{cards}
    <h2 id="locals">What Japanese People Snack On<span class="h2-jp">日本人に人気のお菓子</span></h2>
    <p>Souvenir sweets are not what people here eat every day. For everyday snacks, I found two surveys. Both are limited, so please read them as hints.</p>
    <h3>A 2016 TV Survey of 10,000 People</h3>
    <p>The {JPB} reports a survey run by a TV program, which it does not name. Voters chose their favorites from about 1,700 kinds of snacks and candies, 10,000 people took part, and it was held in November 2016. The top 10 were:</p>
    <ol>
      <li>Calbee Jagariko Salad</li>
      <li>Calbee Potato Chips, lightly salted</li>
      <li>Nestlé Japan Kit Kat Minis</li>
      <li>Calbee Potato Chips Consommé Punch</li>
      <li>Calbee Kappa Ebisen</li>
      <li>Calbee Kata-Age Potato Chips, salt</li>
      <li>Koikeya Potato Chips Nori-Shio</li>
      <li>Meiji Takenoko no Sato</li>
      <li>Meiji Kajyu Gummy, grape</li>
      <li>Morinaga Hi-Chew</li>
    </ol>
    <p>That list is almost ten years old, so tastes may have moved.</p>
    <h3>A 2023 Survey by Maker</h3>
    <p>{MG} reports a survey by Model Hyakka (published on its MoneyGeek site) on April 24-25, 2023, of 1,000 people who said they always buy sweets when they buy food, chosen from a pre-survey of 6,000 people aged 17 to 84. The makers named were Calbee first (504 votes; Kappa Ebisen, potato chips, Jagariko and Jagabee), Meiji second (424 votes; Kajyu Gummy, chocolates, Kinoko no Yama and Takenoko no Sato) and Glico third. The page shows only part of the list.</p>
    <p>Two items from my 10 also appear in the 2016 list: Kit Kat and Hi-Chew. If you want to snack like a local, add a can of Jagariko and a bag of Calbee potato chips. These are savory, cheap and found at any convenience store.</p>

    <h2 id="tips">Packing Tips<span class="h2-jp">持ち帰りのコツ</span></h2>
    <ol>
      <li><strong>Buy fresh sweets last.</strong> Daifuku and nama yatsuhashi are for the trip.</li>
      <li><strong>Check the date.</strong> The box shows the best-before date.</li>
      <li><strong>Pack chocolate and cakes flat</strong> in your carry-on, away from heat.</li>
      <li><strong>Check customs rules</strong> for your country before you buy.</li>
    </ol>
    <div style="background:var(--washi-dark);border-left:4px solid var(--kin);padding:16px 20px;margin:24px 0;border-radius:2px;">
      <p style="margin:0;">&#127856; <strong>Plan your trip:</strong> Want a local to show you the food stalls? <a href="{VI}" target="_blank" rel="noopener sponsored" onclick="trackEvent('click','affiliate','viator_sweets_local')">Browse Japan food tours on Viator &rarr;</a></p>
    </div>

    <h2 id="faq">Frequently Asked Questions<span class="h2-jp">よくあるご質問</span></h2>

    <div class="faq-stack">

{faq_html}    </div>

    <h2 id="final">Final Thoughts<span class="h2-jp">むすびに</span></h2>
    <p>If you buy only three things, make them Pocky, a Japan-only Kit Kat and a box of senbei. They are cheap, they keep, and they travel well. For savory snacks and dishes tied to places, see our {link('/regional-food/','guide to regional cuisine','sweets_to_regional_food')} and our {link('/culture/noodles/','noodles guide','sweets_to_noodles')}.</p>

    <div class="closing-block">
      <span class="torii">🍡</span>
      <p>A small box from the trip, shared at home.</p>
    </div>

    <section class="related-section">
      <h2>Related Guides</h2>
      <span class="h2-jp">関連ガイド</span>
      <div class="related-grid">
        <a class="related-card" href="/regional-food/" onclick="trackEvent('click','internal','related_sweets_to_food')">
          <div class="related-card-label">SACRED JAPAN ／ GUIDE</div>
          <div class="related-card-title">🍽️ Japan's Regional Cuisine →</div>
          <div class="related-card-desc">Dishes from Hokkaido to Okinawa.</div>
        </a>
        <a class="related-card" href="/culture/noodles/" onclick="trackEvent('click','internal','related_sweets_to_noodles')">
          <div class="related-card-label">SACRED JAPAN ／ GUIDE</div>
          <div class="related-card-title">🍜 Japanese Noodles Guide →</div>
          <div class="related-card-desc">Soba, somen, hiyamugi and cold ramen.</div>
        </a>
      </div>
    </section>

    <p style="font-size:14px;color:var(--enshu);line-height:1.7;margin-top:32px;"><strong>Sources:</strong> {TRIP}; {BYF}; {JW}; {ZEN}; {TV}; {FUN}; {SORA}; {JPB}; {MG}. Product facts and prices come from these pages and may have changed, so check before you buy. The selection and order are the author's. Product names are trademarks of their owners, so this page links to official sites and does not show product packaging.</p>

  </article>

</main>'''
t=open(f'{R}/_tools/culture/tea.py',encoding='utf-8').read()
tail=t[t.index("s=open(f'{R}/culture/omamori-guide"):]
tail=tail.replace('<div class="hero-bg-kanji">茶道</div>','<div class="hero-bg-kanji">菓子</div>')
tail=tail.replace('<h1>The Japanese <em>Tea Ceremony</em> Guide</h1>','<h1>Japanese <em>Sweets</em> to Bring Home</h1>')
tail=tail.replace('<div class="hero-jp">茶道ガイド</div>','<div class="hero-jp">お土産お菓子ガイド</div>')
tail=tail.replace('What Happens, What to Do as a Guest, and Where to Try It','10 Cheap Favorites a Guide Recommends')
tail=tail.replace('Tea Ceremony Guide','Sweets Guide')
tail=tail.replace('guide_tea','guide_sweets').replace('viator_guide_tea_sticky','viator_guide_sweets_sticky').replace('japanese+tea+ceremony','Japan+food+tour')
tail=re.sub(r'(<meta name="keywords" content=")[^"]*(")',r'\1Japanese sweets, Japanese souvenirs, omiyage, Pocky, Kit Kat Japan, Hi-Chew, Tokyo Banana, Shiroi Koibito, yatsuhashi, castella, cheap souvenirs Japan\2',tail)
exec(tail)
