import re, os, json
from PIL import Image
R='/home/claude/sacred-japan'
A='/mnt/user-data/attachments/fd332c08-3f6b-545a-883b-83277e19ff52/'
S='wagashi'
OUT=f'{R}/culture/{S}'
os.makedirs(OUT+'/images',exist_ok=True)
photos={'ichigo':('5e10bb4f-image.jpg',1200),'strawberry':('36b6e7e3-image.jpg',1000),'yokan':('23068ad2-image.jpg',1000),'uiro':('270a1761-image.jpg',650),'almond':('15cb0b50-image.jpg',900),'taiyaki1':('12c12445-image.jpg',1000),'taiyaki2':('197c48c9-image.jpg',1000),'raindrop':('1869be0b-image.jpg',1000),'shitatari':('fba835fc-image.jpg',848)}
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
FIJ=ext('https://www.foodinjapan.org/japan/fruit-daifuku','Food in Japan (fruit daifuku)','wagashi_foodinjapan_daifuku')
MT=ext('https://www.mlit.go.jp/tagengo-db/en/R2-01316.html','MLIT multilingual database (Kinseiken Daigahara shop)','wagashi_mlit_kinseiken')
SN=ext('https://soranews24.com/2014/06/04/this-amazing-water-cake-just-may-be-the-most-delicate-sweet-ever-created/','SoraNews24 (2014)','wagashi_soranews_raindrop')
TWK=ext('https://www.tokyoweekender.com/food-and-drink/history-of-taiyaki/','Tokyo Weekender (history of taiyaki)','wagashi_tw_taiyaki')
JY=ext('https://www.jeepe.jp/en/articles/yokan-basic-guide-1564','Jeepe (yokan basics)','wagashi_jeepe_yokan')
VI='https://www.viator.com/search/Japan+tea+ceremony?pid=P00298374&amp;mcid=42383&amp;medium=link&amp;campaign=sacred-japan'

f_ich=fig('ichigo','Two pale pink rice-cake sweets on a white plate; one is cut open to show a whole strawberry and dark bean paste inside','Ichigo daifuku, one cut open: a strawberry and bean paste inside soft pink mochi.',f'Photo: Ocdp, {CC0}, 5 December 2012. {VIA}',hero=True)
f_str=fig('strawberry','Two halves of a white mochi sweet cut open, each showing a red strawberry cross-section ringed by dark bean paste','The cross-section: strawberry, then a ring of paste, then mochi.',f'Photo: Janine (Flickr), {BY2}, 10 February 2008. {VIA}',maxw=620)
f_yok=fig('yokan','Two smooth, dark reddish-brown blocks of yokan stacked on a blue-and-white patterned plate','Two slices of yokan on a blue-and-white plate.',f'Photo: Ocdp, {CC0}, 10 March 2025. {VIA}')
f_uir=fig('uiro','Two small rectangular blocks, one pale brown and one darker reddish brown, on a green-and-brown glazed plate','Bite-size uiro, with the cut face shown.',f'Photo: 小太刀, {BYSA3}, 8 June 2006. {VIA}',maxw=650)
f_ta1=fig('taiyaki1','A golden fish-shaped griddle cake with scales and fins pressed into the crust, on a white plate with black calligraphy','Taiyaki, the fish-shaped griddle cake.',f'Photo: Ocdp, {CC0}, 3 November 2014. {VIA}',maxw=620)
f_ta2=fig('taiyaki2','A fish-shaped cake torn open on a white napkin and black plate, showing a dark red bean paste filling inside the golden shell','A taiyaki torn open to show the bean paste.',f'Photo: Andy Li, {CC0}, 23 September 2025. {VIA}',maxw=560)
f_rd=fig('raindrop','Top view of a clear, dome-shaped jelly in a wooden boat-shaped tray, with a pile of light brown powder on one side and dark syrup on the other','Raindrop cake with kinako and syrup.',f'Photo: T.Tseng (Flickr), {BY2}, 19 June 2016. {VIA}',maxw=760)
f_sh=fig('shitatari','Two translucent amber blocks of jelly on a clear glass dish placed on a pale wooden board','Two blocks of an amber water sweet.',f'Photo: Kykk wiki, {CC0}, 8 September 2023. {VIA}',maxw=640)
f_alm=fig('almond','A white bowl of jelly-like white cubes topped with orange peach slices, a few green pieces and a red cherry','Homemade almond tofu with fruit.',f'Photo: King of Hearts, {BYSA4}, 20 June 2020. {VIA}',maxw=560)

faqs=[
("What is wagashi?","Wagashi means traditional Japanese sweets. It is a broad word, so this guide covers only four things: ichigo daifuku, yokan, uiro, almond tofu, taiyaki, raindrop cake and shitatari, the ones I could show with photographs. The Jeepe article says yokan is eaten with green tea or matcha, and the same pairing is common for other sweets of this kind."),
("Who invented ichigo daifuku?","Nobody can say for certain. Food in Japan says the strawberry version emerged in the 1980s and that several shops have been linked to its origin, and the Tamaya shop claims on its own website that it created the original. The same article credits Toraya in Ginza with fruit daifuku in general in 1974, and it does not reconcile the two dates. Take every date as a claim."),
("Is ichigo daifuku seasonal?","The Food in Japan article says fruit daifuku is often seasonal, but it does not name a season for strawberry. Shops that use fresh strawberries tend to sell it when strawberries are at their best, so ask the shop."),
("How do I eat yokan?","Jeepe suggests slicing the bar to about 1 to 1.5 cm, eating small pieces slowly with green tea or matcha, and using a wagashi pick if you have one. It says coffee also works."),
("How long does yokan keep?","Jeepe says unopened neri-yokan can often keep for several months to about a year at room temperature, while mizu-yokan and mushi-yokan generally keep for less time. The label on your purchase is the thing to trust."),
("Why is taiyaki shaped like a fish?","Tokyo Weekender says the fish is a sea bream (tai), a symbol of good fortune, and that sea bream was once an expensive treat, so a cheap sweet in its shape had appeal. The same article credits Seijiro Kobe of Naniwaya Sohonten with the invention after an imagawayaki shop opened in 1909, but it gives no date for the first taiyaki, so the origin is a claim."),
("How long does raindrop cake last?","Very briefly. The MLIT page on Kinseiken says the cake melts after about 30 minutes at room temperature, and Kinseiken's original has been reported as an eat-in sweet. Eat it right away and check the shop's rules."),
("Is uiro the same as yokan?","They look alike as small blocks, but I did not find a source comparing them, so I will not give you a rule. The photograph in this guide is labeled by its photographer as uiro from Osu, and the quickest answer is to ask at the shop."),
]
faq_html=''.join(f'''      <details class="faq-item">
        <summary>{q}</summary>
        <div class="faq-answer">{a}</div>
      </details>

''' for q,a in faqs)
faq_ld=json.dumps({"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in faqs]},ensure_ascii=False,indent=2)
TITLE="Wagashi Guide: Ichigo Daifuku, Yokan, Uiro and Other Japanese Sweets"
DESC="A licensed guide's English introduction to wagashi, traditional Japanese sweets: ichigo daifuku (strawberry mochi), yokan, uiro, taiyaki, raindrop cake and almond tofu, with photographs and honest notes on what is claimed."
URL=f"https://sacred-japan.net/culture/{S}/"
OG="https://sacred-japan.net/images/og/og-culture-wagashi.jpg"
main=f'''<main>

  {f_ich}

  <aside class="toc" aria-label="Table of contents">
    <div class="toc-label">TABLE OF CONTENTS ／ 目次</div>
    <div class="toc-title">In This Guide</div>
    <ol>
      <li><a href="#opening">Opening: A Note from the Guide</a></li>
      <li><a href="#daifuku">Ichigo Daifuku</a></li>
      <li><a href="#yokan">Yokan</a></li>
      <li><a href="#more">Uiro and Almond Tofu</a></li>
      <li><a href="#taiyaki">Taiyaki, the Griddle Sweet</a></li>
      <li><a href="#water">Water Sweets: Raindrop Cake and Shitatari</a></li>
      <li><a href="#faq">Frequently Asked Questions</a></li>
      <li><a href="#final">Final Thoughts</a></li>
    </ol>
  </aside>

  <article>

    <section id="opening">
      <p class="opening">Cut an ichigo daifuku in half and the strawberry shows up like a small red sun inside a ring of dark bean paste.</p>
      <p>As a licensed guide, I send visitors to wagashi counters for exactly that kind of surprise. This guide covers a handful of sweets I can show you in photographs, and it says plainly where the origin stories disagree. Wagashi pairs naturally with tea, so if you want to see it in its home setting, read our {link('/culture/tea-ceremony/','tea ceremony guide','wagashi_to_tea')} too.</p>
    </section>

    <h2 id="daifuku">Ichigo Daifuku<span class="h2-jp">いちご大福</span></h2>
    <p>A whole strawberry is set in sweet bean paste and wrapped in soft mochi. {FIJ} says fruit daifuku varies by fruit, by the amount of paste, and by whether the fruit is fully enclosed or partly visible, and it lists mango, peach, kiwi and apple alongside strawberry.</p>
    <p>The origin is a tangle. The article credits Toraya in Ginza with fruit daifuku in 1974 and says the strawberry version emerged in the 1980s, with several shops linked to it. Tamaya says on its own website that it invented the original. Treat each as a claim, because the article does not reconcile them.</p>
    {f_str}
    <p>This cross-section is the whole appeal: red fruit, a ring of paste, then the white mochi. The pink one in the photograph at the top has a tinted mochi skin, and shops make both versions. Eat it soon after buying, since I have not found a shelf life for it and fresh fruit does not wait.</p>

    <h2 id="yokan">Yokan<span class="h2-jp">羊羹</span></h2>
    <p>Yokan is a firm, smooth bar of sweet bean paste. {JY} describes three types: neri-yokan, simmered with agar and kneaded, the most common and long-lasting; mizu-yokan, with more water, lighter and tied to summer; and mushi-yokan, steamed with wheat flour or kuzu starch for a chewier texture, which it calls the oldest form.</p>
    {f_yok}
    <p>The two slices here have the glossy, even look of a neri type, though the Commons description does not say which kind it is, so I will not claim one. The cut edges are clean because a good yokan holds its shape.</p>
    <p>On history, Jeepe says yokan derives from a Chinese lamb broth, and that Zen influence replaced the meat with plant ingredients such as azuki beans and wheat flour. It says yokan reached Japan between the Kamakura and Muromachi periods and became a tea-gathering sweet by the Sengoku period. The page itself notes its content may not be complete, so use it as an outline.</p>
    <p>To eat it, Jeepe suggests slicing about 1 to 1.5 cm and taking small pieces slowly with green tea. Unopened neri-yokan can keep for months, which is why individually wrapped pieces make easy gifts. Jeepe names Toraya and Shintsuruya (Suwa, Nagano) as shops worth knowing, and says to check the label for wheat if you have allergies.</p>

    <h2 id="more">Uiro and Almond Tofu<span class="h2-jp">ういろうと杏仁豆腐</span></h2>

    <h3>Uiro</h3>
    {f_uir}
    <p>The photographer's Japanese description calls these bite-size uiro from Osu, with the cut surface shown. I take the Osu in the label to mean the Osu area of Nagoya, but the description does not say so, and I have not sourced uiro's history or ingredients, so I will stay with what the picture shows: a pale block and a darker one, neatly cut, on a glazed plate. The photograph dates from 2006, so it tells you nothing about current shops.</p>

    <h3>Almond Tofu</h3>
    {f_alm}
    <p>Soft white cubes with peach, a few green pieces and a cherry. The Commons description calls this homemade almond tofu with mixed fruit, peach slices and a maraschino cherry. It is a jelly-like dessert and you will see it on Japanese dessert menus, but I have not sourced where it sits in the wagashi category, so I list it as a neighbor, not a classic.</p>
    <p>If you would like to eat wagashi where it is meant to be eaten, a {ext(VI,'tea ceremony experience','wagashi_viator_tea')} is one way to do it.</p>

    <h2 id="taiyaki">Taiyaki, the Griddle Sweet<span class="h2-jp">鯛焼き</span></h2>
    <p>Taiyaki is a fish-shaped griddle cake, usually filled with sweet red bean paste. It is a street-stall sweet rather than a tea-room one, so I list it as a neighbor of wagashi, not a strict member. {TWK} credits Seijiro Kobe, the first owner of the shop Naniwaya Sohonten, with inventing it. It says he opened an imagawayaki shop in 1909 (a thick round pancake with red bean paste), tried shapes such as turtles and airships that did not sell, and then settled on a fish mold. The article does not say that the 1909 shop was the exact birthplace, and it gives no date for the first taiyaki, so treat the story as a claim.</p>
    <p>The fish is a sea bream (<em>tai</em>), a symbol of good fortune. The same article says sea bream was an expensive delicacy in the early 1900s, which made a cheap sweet in its shape appealing.</p>
    {f_ta1}
    <p>Scales, a fin and a round eye are pressed into the crust, and the edges show the thin, crisp ring where batter met the mold. The Commons description (in Japanese) places this one at Taiyaki Wakaba in Yotsuya, Tokyo, and calls it a <em>tennen</em> taiyaki. I have not sourced what that term means, so I will only repeat the label.</p>
    {f_ta2}
    <p>Torn open, the shell is thin and golden outside, with a layer of soft cake inside and a dark band of bean paste in the middle. The Commons description gives no shop for this one, so I will not name one.</p>

    <h2 id="water">Water Sweets: Raindrop Cake and Shitatari<span class="h2-jp">水信玄餅としたたり</span></h2>

    <h3>Raindrop Cake</h3>
    <p>This is the clear dome that went viral abroad as raindrop cake. In Japan the best-known version is Kinseiken's <em>mizu shingen mochi</em> from Yamanashi. The {MT} says it is made from two things, Yamanashi water and agar, and is served with kuromitsu (black sugar syrup) and kinako (roasted soybean flour). It also says the cake melts after about 30 minutes at room temperature. That page gives no creation date, only that the Daigahara shop opened in 1902.</p>
    {f_rd}
    <p>The photograph shows the dome in a wooden tray with a pile of light brown powder on one side and dark syrup on the other, which matches that pairing. The Commons description places it in Los Angeles, and its source line names mizu shingen mochi with black syrup, so this is not the Yamanashi original. {SN} reported in 2014 that the Kinseiken original was sold on weekends and holidays from June to the end of September, and only to eat in. That is an old report, so check the shop before you plan a trip around it.</p>

    <h3>Shitatari</h3>
    {f_sh}
    <p>The Commons description (in Japanese) calls this <em>shitatari</em>, a sweet from the Kyoto wagashi shop Kamehiroei, and says it is linked to the Kikusui-hoko float of the Gion Festival. The photograph shows two amber, translucent blocks on a glass dish. I have not sourced the ingredients or the story behind the name, so all I can say is what the picture and the description say.</p>

    <h2 id="faq">Frequently Asked Questions<span class="h2-jp">よくあるご質問</span></h2>

    <div class="faq-stack">

{faq_html}    </div>

    <h2 id="final">Final Thoughts<span class="h2-jp">むすびに</span></h2>
    <p>Start with an ichigo daifuku in the season it was made for, then try a slice of yokan with tea. For sweets you can bring home, see our {link('/culture/japanese-sweets/','Japanese sweets souvenirs guide','wagashi_to_sweets')}, and for soft buns with bean paste, our {link('/culture/bread/','bread guide','wagashi_to_bread')}.</p>

    <div class="closing-block">
      <span class="torii">🍵</span>
      <p>A small sweet, a cup of tea and a slow minute in between.</p>
    </div>

    <section class="related-section">
      <h2>Related Guides</h2>
      <span class="h2-jp">関連ガイド</span>
      <div class="related-grid">
        <a class="related-card" href="/culture/japanese-sweets/" onclick="trackEvent('click','internal','related_wagashi_to_sweets')">
          <div class="related-card-label">SACRED JAPAN ／ GUIDE</div>
          <div class="related-card-title">🍬 Japanese Sweets Souvenirs →</div>
          <div class="related-card-desc">Ten inexpensive favorites a guide recommends bringing home.</div>
        </a>
        <a class="related-card" href="/culture/tea-ceremony/" onclick="trackEvent('click','internal','related_wagashi_to_tea')">
          <div class="related-card-label">SACRED JAPAN ／ GUIDE</div>
          <div class="related-card-title">🍵 Japanese Tea Ceremony Guide →</div>
          <div class="related-card-desc">What happens, what to do as a guest and where to try it.</div>
        </a>
        <a class="related-card" href="/culture/bread/" onclick="trackEvent('click','internal','related_wagashi_to_bread')">
          <div class="related-card-label">SACRED JAPAN ／ GUIDE</div>
          <div class="related-card-title">🥐 Japanese Bread Guide →</div>
          <div class="related-card-desc">Anpan, melonpan, curry bread and sandwiches.</div>
        </a>
      </div>
    </section>

    <p style="font-size:14px;color:var(--enshu);line-height:1.7;margin-top:32px;"><strong>Sources:</strong> ichigo daifuku from {FIJ}; yokan from {JY}; taiyaki from {TWK}; raindrop cake from {MT} and {SN}. Photograph details come from the Wikimedia Commons descriptions. I have not verified current shop details, prices or opening hours.</p>

  </article>

</main>'''

t=open(f'{R}/_tools/culture/tea.py',encoding='utf-8').read()
tail=t[t.index("s=open(f'{R}/culture/omamori-guide"):]
tail=tail.replace('<div class="hero-bg-kanji">茶道</div>','<div class="hero-bg-kanji">和菓子</div>')
tail=tail.replace('<h1>The Japanese <em>Tea Ceremony</em> Guide</h1>','<h1>The <em>Wagashi</em> Guide</h1>')
tail=tail.replace('<div class="hero-jp">茶道ガイド</div>','<div class="hero-jp">和菓子ガイド</div>')
tail=tail.replace('What Happens, What to Do as a Guest, and Where to Try It','Ichigo Daifuku, Yokan, Uiro and Other Japanese Sweets')
tail=tail.replace('Tea Ceremony Guide','Wagashi Guide')
tail=tail.replace('guide_tea','guide_wagashi').replace('viator_guide_tea_sticky','viator_guide_wagashi_sticky')
tail=re.sub(r'(<meta name="keywords" content=")[^"]*(")',r'\1wagashi, Japanese sweets, ichigo daifuku, yokan, uiro, almond tofu, Japanese confectionery\2',tail)
exec(tail)
