import re, os, json
from PIL import Image
R='/home/claude/sacred-japan'
A='/mnt/user-data/attachments/fd332c08-3f6b-545a-883b-83277e19ff52/'
S='wagashi'
OUT=f'{R}/culture/{S}'
os.makedirs(OUT+'/images',exist_ok=True)
photos={'ichigo':('5e10bb4f-image.jpg',1200),'strawberry':('36b6e7e3-image.jpg',1000),'yokan':('23068ad2-image.jpg',1000),'uiro':('270a1761-image.jpg',650),'almond':('15cb0b50-image.jpg',900),'taiyaki1':('12c12445-image.jpg',1000),'taiyaki2':('197c48c9-image.jpg',1000),'raindrop':('1869be0b-image.jpg',1000),'shitatari':('fba835fc-image.jpg',848),'dora1':('1bc0bab7-image.jpg',1100),'dora2':('fdf50475-image.jpg',1100),'dora3':('52b956d5-image.jpg',800),'dora4':('1b56ea3e-image.jpg',687),'warabi1':('f7fe7879-image.jpg',1000),'warabi2':('c5f3c8ca-image.jpg',640),'monaka1':('0bb91696-image.jpg',900),'monaka2':('65072675-image.jpg',472),'neri':('697ef1fb-image.jpg',760),'gohei1':('9231308e-image.jpg',1000),'gohei2':('7bd10290-image.jpg',1000),'daigaku':('a0220884-image.jpg',760),'anmitsu1':('e3ca2236-image.jpg',540),'anmitsu2':('972e7784-image.jpg',900),'kori':('e4f7430a-image.jpg',800),'kintsuba1':('65c43d2a-image.jpg',1000),'kintsuba2':('6f610507-image.jpg',900),'amanatto':('0062d3f2-image.jpg',1000),'mamedai':('2ec063c3-image.jpg',900),'nanbu':('b82643bb-image.jpg',900),'beika':('e72f0b09-image.jpg',900)}
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
BY3=lic('CC BY 3.0','https://creativecommons.org/licenses/by/3.0/')
VIA='via Wikimedia Commons (resized)'
def link(href,txt,lab): return f'<a href="{href}" class="inline-link" onclick="trackEvent(\'click\',\'internal\',\'{lab}\')">{txt}</a>'
def ext(href,txt,lab): return f'<a href="{href}" target="_blank" rel="noopener" onclick="trackEvent(\'click\',\'external\',\'{lab}\')">{txt}</a>'
FIJ=ext('https://www.foodinjapan.org/japan/fruit-daifuku','Food in Japan (fruit daifuku)','wagashi_foodinjapan_daifuku')
MT=ext('https://www.mlit.go.jp/tagengo-db/en/R2-01316.html','MLIT multilingual database (Kinseiken Daigahara shop)','wagashi_mlit_kinseiken')
SN=ext('https://soranews24.com/2014/06/04/this-amazing-water-cake-just-may-be-the-most-delicate-sweet-ever-created/','SoraNews24 (2014)','wagashi_soranews_raindrop')
JD=ext('https://www.jeepe.jp/en/articles/dorayaki-origin-arrangements-1558','Jeepe (dorayaki)','wagashi_jeepe_dorayaki')
JW=ext('https://www.jeepe.jp/en/articles/warabi-mochi-guide-1563','Jeepe (warabi mochi)','wagashi_jeepe_warabi')
FM=ext('https://foodinjapan.org/japan/monaka/','Food in Japan (monaka)','wagashi_foodinjapan_monaka')
TWK=ext('https://www.tokyoweekender.com/food-and-drink/history-of-taiyaki/','Tokyo Weekender (history of taiyaki)','wagashi_tw_taiyaki')
JY=ext('https://www.jeepe.jp/en/articles/yokan-basic-guide-1564','Jeepe (yokan basics)','wagashi_jeepe_yokan')
JN=ext('https://www.jeepe.jp/en/articles/nerikiri-wagashi-guide-1756','Jeepe (nerikiri)','wagashi_jeepe_nerikiri')
FUN=ext('https://www.fun-japan.jp/en/articles/8192','FUN! JAPAN (Chubu local confectioneries)','wagashi_funjapan_gohei')
MAFF=ext('https://local-cuisine.maff.go.jp/en/recipe/448/','MAFF (Aichi gohei-mochi)','wagashi_maff_gohei')
FD=ext('https://foodinjapan.org/japan/daigaku-imo','Food in Japan (daigaku imo)','wagashi_foodinjapan_daigaku')
FAN=ext('https://www.foodinjapan.org/japan/anmitsu','Food in Japan (anmitsu)','wagashi_foodinjapan_anmitsu')
JPK=ext('https://japanese-products.blog/2018/12/26/kintsuba','Japanese Products blog (kintsuba)','wagashi_jp_kintsuba')
JPA=ext('https://japanese-products.blog/2017/05/08/amanatto-sweet-beans-like-raisins','Japanese Products blog (amanatto)','wagashi_jp_amanatto')
JPN=ext('https://japanese-products.blog/2019/04/09/nanbu-senbei','Japanese Products blog (nanbu senbei)','wagashi_jp_nanbu')
SZK=ext('https://www.suzukake.co.jp/?p=4495','Suzukake (shiomame daifuku)','wagashi_suzukake_mamedaifuku')
VI='https://www.viator.com/search/Japan+tea+ceremony?pid=P00298374&amp;mcid=42383&amp;medium=link&amp;campaign=sacred-japan'

f_ich=fig('ichigo','Two pale pink rice-cake sweets on a white plate; one is cut open to show a whole strawberry and dark bean paste inside','Ichigo daifuku, one cut open: a strawberry and bean paste inside soft pink mochi.',f'Photo: Ocdp, {CC0}, 5 December 2012. {VIA}',hero=True)
f_str=fig('strawberry','Two halves of a white mochi sweet cut open, each showing a red strawberry cross-section ringed by dark bean paste','The cross-section: strawberry, then a ring of paste, then mochi.',f'Photo: Janine (Flickr), {BY2}, 10 February 2008. {VIA}',maxw=620)
f_yok=fig('yokan','Two smooth, dark reddish-brown blocks of yokan stacked on a blue-and-white patterned plate','Two slices of yokan on a blue-and-white plate.',f'Photo: Ocdp, {CC0}, 10 March 2025. {VIA}')
f_uir=fig('uiro','Two small rectangular blocks, one pale brown and one darker reddish brown, on a green-and-brown glazed plate','Bite-size uiro, with the cut face shown.',f'Photo: 小太刀, {BYSA3}, 8 June 2006. {VIA}',maxw=650)
f_ta1=fig('taiyaki1','A golden fish-shaped griddle cake with scales and fins pressed into the crust, on a white plate with black calligraphy','Taiyaki, the fish-shaped griddle cake.',f'Photo: Ocdp, {CC0}, 3 November 2014. {VIA}',maxw=620)
f_ta2=fig('taiyaki2','A fish-shaped cake torn open on a white napkin and black plate, showing a dark red bean paste filling inside the golden shell','A taiyaki torn open to show the bean paste.',f'Photo: Andy Li, {CC0}, 23 September 2025. {VIA}',maxw=560)
f_rd=fig('raindrop','Top view of a clear, dome-shaped jelly in a wooden boat-shaped tray, with a pile of light brown powder on one side and dark syrup on the other','Raindrop cake with kinako and syrup.',f'Photo: T.Tseng (Flickr), {BY2}, 19 June 2016. {VIA}',maxw=760)
f_sh=fig('shitatari','Two translucent amber blocks of jelly on a clear glass dish placed on a pale wooden board','Two blocks of an amber water sweet.',f'Photo: Kykk wiki, {CC0}, 8 September 2023. {VIA}',maxw=640)
f_do1=fig('dora1','A round dorayaki and a second one cut open, showing two golden pancake layers with a thin line of dark red bean paste between them, on white','Two dorayaki: one whole, one cut to show the paste between the pancake layers.',f'Photo: Ocdp, {BYSA3}, 14 September 2021 (Quality image). {VIA}',maxw=700)
f_do2=fig('dora2','Two cream-filled dorayaki; the left one shows pink cream between the pancakes, the right one is cut open to show white cream and brown paste around a green piece','Dorayaki with cream: pink on the left, a cut one with white cream and a green piece on the right.',f'Photo: Ocdp, {CC0}, 20 March 2025. {VIA}',maxw=700)
f_do3=fig('dora3','A round dorayaki on a white plate on a red table, with a cartoon cat face branded onto the top of the pancake','A dorayaki with a cartoon face branded on the top.',f'Photo: Wagner Tamanaha (Flickr), {BYSA2}, 24 March 2012. {VIA}',maxw=520)
f_do4=fig('dora4','A dorayaki with a dark, scorched-looking top and a thick layer of white cream between the two pancakes, on a black square plate','A cream dorayaki with a dark-branded top, shown from the side.',f'Photo: Kykk wiki, {CC0}, 20 September 2022. {VIA}',maxw=560)
f_wa1=fig('warabi1','A blue glass bowl of translucent grey-purple warabimochi pieces covered in golden kinako powder and a few streaks of black syrup','Warabimochi in a blue glass bowl, with kinako and syrup.',f'Photo: Ocdp, {CC0}, 7 February 2022. {VIA}',maxw=700)
f_wa2=fig('warabi2','A small square plate of brown warabimochi pieces coated in kinako and dark syrup, with a bamboo pick resting on it','Warabimochi on a small plate with a bamboo pick.',f'Photo: Ichiro Kamiko, {BYSA3}, 13 July 2011. {VIA}',maxw=520)
f_mo1=fig('monaka1','A pale gold oval monaka shell with a patterned top, next to a half that is cut open to show smooth dark red bean paste inside a thin wafer','Monaka: the oval wafer shell, and a half cut to show the paste.',f'Photo: Ocdp, {CC0}, 28 June 2022. {VIA}',maxw=640)
f_mo2=fig('monaka2','An open monaka: a pale gold wafer lid lifted slightly over a thick pile of whole dark red beans in paste, sitting on a thin wafer base','An open monaka, with the lid resting over a chunky paste.',f'Photo: nyanya, {BYSA3}, 13 May 2007. {VIA}',maxw=472)
f_ne=fig('neri','Five small hand-shaped sweets on a silver tray: a white one with a yellow center and green leaf, a pink folded one, a green frilly one, a white one with purple grapes and a vine, a green striped watermelon, and a pink peach with a red dot','A tray of nerikiri-style sweets in a shop display, each shaped like a different flower or fruit.',f'Photo: Nesnad, {BY4}, 9 July 2021. {VIA}',maxw=640)
f_g1=fig('gohei1','Close-up of round flat slices of grilled rice on bamboo skewers, with a glossy dark brown glaze and charred spots','Gohei mochi freshly grilled: flattened rice on skewers with a brown glaze.',f'Photo: Kunmap, {BYSA4}, 28 October 2013. {VIA}',maxw=700)
f_g2=fig('gohei2','A single long oval gohei mochi on a flat bamboo skewer, resting on a white foam tray, with a dark glaze and burnt flecks','One oval skewer on a tray, the shape the MAFF page calls waraji.',f'Photo: 円周率３パーセント, {BYSA4}, 21 September 2024. {VIA}',maxw=760)
f_da=fig('daigaku','Pieces of glazed sweet potato dusted with black sesame seeds in a white bowl with blue painted leaves','Daigaku imo: fried sweet potato pieces in a shiny syrup, with black sesame.',f'Photo: Ocdp, {CC0}, 3 July 2021. {VIA}',maxw=620)
f_an1=fig('anmitsu1','A glass bowl on a wooden tray holding a scoop of ice cream, orange and yellow fruit and dark red bean paste, with a small glass of dark syrup beside it','Anmitsu with ice cream and fruit, and the dark syrup served on the side.',f'Photo: kumon (Flickr), {BY2}, 6 March 2005. {VIA}',maxw=540)
f_an2=fig('anmitsu2','A glass bowl on a red lacquer tray: a scoop of red bean paste in the center, surrounded by clear jelly cubes, pink and white sweets, a white dumpling, a green ball, orange and yellow fruit and a few beans','A fuller anmitsu: bean paste in the middle, then jelly cubes, dumplings and fruit.',f'Photo: jetalone (Flickr), {BY2}, 23 May 2007. {VIA}',maxw=700)
f_ko=fig('kori','A rustic bowl on a red lacquer tray, filled with bright green shaved ice with a patch of dark red bean paste and a white mochi piece at the front and a spoon resting on the rim','Green shaved ice with a mochi and bean-paste piece tucked in front.',f'Photo: 小太刀, {BYSA3}, 27 May 2007 (the original upload date). {VIA}',maxw=640)
f_ki1=fig('kintsuba1','Two kintsuba on a black lacquer plate with a tea cup behind: one whole round, grilled disc with brown spots, and one broken open to show chunky red bean paste','Kintsuba: a grilled disc, and one broken open to show the chunky paste.',f'Photo: katorisi, {BY3}, 21 October 2007. {VIA}',maxw=620)
f_ki2=fig('kintsuba2','A thick, dark round block of bean paste with a dusting of white and a few black sesame seeds on top, sitting on a white plate','A round, very dense kintsuba with black sesame on top.',f'Photo: Kawazure135, {BYSA4}, 15 April 2025. {VIA}',maxw=620)
f_am=fig('amanatto','A long beige tray with four small piles of sugar-dusted sweets: green beans, reddish-brown beans, dark purple-red beans and pale amber slices','Amanatto on one plate: four colors, each coated in a frosting of sugar.',f'Photo: Ocdp, {CC0}, 10 February 2022. {VIA}',maxw=700)
f_md=fig('mamedai','Two white mochi sweets on a blue-striped plate; the one on the right is cut open to show dark red bean paste and a large dark bean, and the one on the left shows dark beans under the flour-dusted skin','Mame daifuku, one cut open: mochi, paste and a whole bean.',f'Photo: Ocdp, {CC0}, 24 March 2022 (the file was re-shot in 2025). {VIA}',maxw=640)
f_nb=fig('nanbu','A flat, round, thick-rimmed pale brown cracker with reddish peanuts pressed into the center, on a wooden surface','A nanbu senbei: a wheat cracker with peanuts set into the middle.',f'Photo: Quercus acuta, {BYSA4}, 25 August 2024. {VIA}',maxw=700)
f_be=fig('beika','A rectangular baked rice cracker with a glossy pale surface and many brown roasted beans set into it','A bean-studded rice cracker.',f'Photo: Kropsoq, {BYSA3}, July 2005. {VIA}',maxw=640)
f_alm=fig('almond','A white bowl of jelly-like white cubes topped with orange peach slices, a few green pieces and a red cherry','Homemade almond tofu with fruit.',f'Photo: King of Hearts, {BYSA4}, 20 June 2020. {VIA}',maxw=560)

faqs=[
("What is wagashi?","Wagashi means traditional Japanese sweets. It is a broad word, so this guide covers only a handful: ichigo daifuku, yokan, uiro, almond tofu, taiyaki, dorayaki, warabimochi, monaka, nerikiri, raindrop cake and shitatari, plus anmitsu, kintsuba, amanatto, mame daifuku, senbei and two snacks, gohei mochi and daigaku imo, the ones I could show with photographs. The Jeepe article says yokan is eaten with green tea or matcha, and the same pairing is common for other sweets of this kind."),
("Who invented ichigo daifuku?","Nobody can say for certain. Food in Japan says the strawberry version emerged in the 1980s and that several shops have been linked to its origin, and the Tamaya shop claims on its own website that it created the original. The same article credits Toraya in Ginza with fruit daifuku in general in 1974, and it does not reconcile the two dates. Take every date as a claim."),
("Is ichigo daifuku seasonal?","The Food in Japan article says fruit daifuku is often seasonal, but it does not name a season for strawberry. Shops that use fresh strawberries tend to sell it when strawberries are at their best, so ask the shop."),
("How do I eat yokan?","Jeepe suggests slicing the bar to about 1 to 1.5 cm, eating small pieces slowly with green tea or matcha, and using a wagashi pick if you have one. It says coffee also works."),
("How long does yokan keep?","Jeepe says unopened neri-yokan can often keep for several months to about a year at room temperature, while mizu-yokan and mushi-yokan generally keep for less time. The label on your purchase is the thing to trust."),
("Why is taiyaki shaped like a fish?","Tokyo Weekender says the fish is a sea bream (tai), a symbol of good fortune, and that sea bream was once an expensive treat, so a cheap sweet in its shape had appeal. The same article credits Seijiro Kobe of Naniwaya Sohonten with the invention after an imagawayaki shop opened in 1909, but it gives no date for the first taiyaki, so the origin is a claim."),
("How long does raindrop cake last?","Very briefly. The MLIT page on Kinseiken says the cake melts after about 30 minutes at room temperature, and Kinseiken's original has been reported as an eat-in sweet. Eat it right away and check the shop's rules."),
("Why is dorayaki called that?","Jeepe says the best-known theory ties the name to the dora, a bronze gong, because of the round shape, and that some shops tell a legend about batter cooked on a heated gong. It treats the legend as a legend, so I do the same."),
("What is warabimochi made from?","Traditionally from bracken starch, according to Jeepe, which also says most commercial versions use other starches such as sweet potato, tapioca or kudzu because pure bracken starch is rare and laborious to produce. The label on your purchase is the thing to read."),
("What is monaka made of?","Food in Japan says the shell is made from glutinous rice flour and water, baked thin in iron molds, and filled most often with sweet azuki paste. It also lists white bean paste, chestnut and matcha cream, plus ice cream fillings."),
("What is nerikiri?","Jeepe describes nerikiri as a fresh sweet made mainly from white bean paste kneaded with a soft rice paste or yam, shaped by hand into seasonal motifs. It should be eaten the same day or the next, so it is a poor souvenir."),
("Is gohei mochi a wagashi?","Not in the tea-ceremony sense. It is a regional skewered rice snack grilled with a savory-sweet sauce, mostly from Nagano, Gifu and Aichi, according to FUN! JAPAN and the agriculture ministry. I include it because it is a traditional local sweet-and-savory snack."),
("Why is daigaku imo called university potato?","Nobody knows. Food in Japan lists theories about students, a shop near a university and a student selling it for tuition, and says none can be proven."),
("What is anmitsu?","Food in Japan describes a chilled dessert of agar jelly cubes with red bean paste, fruit and shiratama dumplings, with black sugar syrup served alongside. Without the bean paste it is closer to mitsumame."),
("What is kintsuba?","Sweet azuki paste, usually chunky, set with agar and wrapped in a thin wheat-flour dough, most often as a brick, according to the Japanese Products blog. Its mid-Edo history comes from that one page."),
("Is amanatto related to natto?","No. Beans are simmered in sugar syrup, coated in sugar and dried, according to the Japanese Products blog, so it is a sweet and unrelated to fermented natto."),
("Is nanbu senbei made of rice?","No, it is a wheat cracker from the Hachinohe area of Aomori, also made in Iwate, according to the Japanese Products blog. Aomori versions tend to be salty and Iwate versions sweeter."),
("Is uiro the same as yokan?","They look alike as small blocks, but I did not find a source comparing them, so I will not give you a rule. The photograph in this guide is labeled by its photographer as uiro from Osu, and the quickest answer is to ask at the shop."),
]
faq_html=''.join(f'''      <details class="faq-item">
        <summary>{q}</summary>
        <div class="faq-answer">{a}</div>
      </details>

''' for q,a in faqs)
faq_ld=json.dumps({"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in faqs]},ensure_ascii=False,indent=2)
TITLE="Wagashi Guide: Ichigo Daifuku, Yokan, Uiro and Other Japanese Sweets"
DESC="A licensed guide's English introduction to wagashi, traditional Japanese sweets: ichigo daifuku (strawberry mochi), yokan, uiro, taiyaki, dorayaki, warabimochi, monaka, nerikiri, raindrop cake and almond tofu, plus anmitsu, kintsuba, amanatto, mame daifuku, senbei, gohei mochi and daigaku imo, with photographs and honest notes on what is claimed."
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
      <li><a href="#nerikiri">Nerikiri</a></li>
      <li><a href="#taiyaki">Taiyaki, the Griddle Sweet</a></li>
      <li><a href="#dorayaki">Dorayaki</a></li>
      <li><a href="#warabimochi">Warabimochi</a></li>
      <li><a href="#monaka">Monaka</a></li>
      <li><a href="#water">Water Sweets: Raindrop Cake and Shitatari</a></li>
      <li><a href="#anmitsu">Anmitsu</a></li>
      <li><a href="#kintsuba">Kintsuba</a></li>
      <li><a href="#beans">Beans and Mochi: Amanatto and Mame Daifuku</a></li>
      <li><a href="#crackers">Senbei: The Salty-Sweet Crackers</a></li>
      <li><a href="#snacks">Not Quite Wagashi: Gohei Mochi and Daigaku Imo</a></li>
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

    <h2 id="nerikiri">Nerikiri<span class="h2-jp">練り切り</span></h2>
    <p>Nerikiri is the sweet shaped like a flower. {JN} describes it as a premium fresh sweet, <em>jo-namagashi</em>, made mainly from white bean paste kneaded with a binder, either <em>gyuhi</em> (a soft rice paste) or yam. Makers sculpt each piece by hand with small tools and give it a poetic name. It says pieces are typically 3 to 4 cm across and that the motifs follow the seasons: cherry blossoms in spring, hydrangeas and morning glories in summer, maple leaves and chrysanthemums in autumn, camellias in winter.</p>
    {f_ne}
    <p>This is a shop display, and the Commons description says only "wagashi," not what each piece is called. By eye I see a white piece with a yellow center and a green leaf, a pink folded one, a green frilly one with a dark curl, a white one with purple grapes and a vine, a green watermelon with dark stripes, and a pink peach with a red dot. The purple morning glories in the corner suggest a summer display, but I cannot confirm the season or the shop.</p>
    <p>Jeepe says nerikiri is eaten before the matcha, which it says softens the bitterness, and that you should look at the whole piece first and then eat it in small bites. It lists ¥400 to 700 per piece, sometimes over ¥1,000 at specialty shops, and says to eat it the same day or the next. That makes it a poor souvenir for a long trip. Some claims on that page, such as a cultural-property registration and the poem behind one piece's name, have no sources, so I have left them out.</p>

    <h2 id="taiyaki">Taiyaki, the Griddle Sweet<span class="h2-jp">鯛焼き</span></h2>
    <p>Taiyaki is a fish-shaped griddle cake, usually filled with sweet red bean paste. It is a street-stall sweet rather than a tea-room one, so I list it as a neighbor of wagashi, not a strict member. {TWK} credits Seijiro Kobe, the first owner of the shop Naniwaya Sohonten, with inventing it. It says he opened an imagawayaki shop in 1909 (a thick round pancake with red bean paste), tried shapes such as turtles and airships that did not sell, and then settled on a fish mold. The article does not say that the 1909 shop was the exact birthplace, and it gives no date for the first taiyaki, so treat the story as a claim.</p>
    <p>The fish is a sea bream (<em>tai</em>), a symbol of good fortune. The same article says sea bream was an expensive delicacy in the early 1900s, which made a cheap sweet in its shape appealing.</p>
    {f_ta1}
    <p>Scales, a fin and a round eye are pressed into the crust, and the edges show the thin, crisp ring where batter met the mold. The Commons description (in Japanese) places this one at Taiyaki Wakaba in Yotsuya, Tokyo, and calls it a <em>tennen</em> taiyaki. I have not sourced what that term means, so I will only repeat the label.</p>
    {f_ta2}
    <p>Torn open, the shell is thin and golden outside, with a layer of soft cake inside and a dark band of bean paste in the middle. The Commons description gives no shop for this one, so I will not name one.</p>

    <h2 id="dorayaki">Dorayaki<span class="h2-jp">どら焼き</span></h2>
    <p>Dorayaki is two soft, round pancakes with sweet bean paste between them. {JD} says the batter is wheat flour, eggs and sugar, sometimes with honey or mirin, and that the filling is either <em>tsubuan</em> (chunky) or <em>koshian</em> (smooth). Another griddle sweet, so I list it next to taiyaki rather than inside the strict tea-room tradition.</p>
    {f_do1}
    <p>The cut one shows how little paste there is compared with the cake: a thin dark line between two airy layers. The Commons description gives no shop for either one.</p>
    <p>The name is usually tied to the <em>dora</em>, a bronze gong, for the round shape. Jeepe presents that as the best-known theory, and says some shops tell a legend that the batter was first cooked on a heated gong, which it treats as a legend, not a fact. It says the Edo-period version is "said to have been" a single thin layer wrapped around the paste. Its FAQ adds that a third-generation owner of Baikado in Nihonbashi introduced the round form in the early Meiji era, and that later pancake culture from the West led to thicker, fluffier batter. Those last claims appear only in the FAQ, so take them as one source's account. In the Kinki region the same sweet is called <em>mikasa</em>, which Jeepe says is "believed" to come from Mount Mikasa in Nara.</p>
    {f_do3}
    <p>This one has a cartoon face branded on the pancake. I read it as the cat from the manga and anime Doraemon, who is the character most associated with dorayaki, but the Commons description only gives the title "Dorayaki @ Kanazawa Conveniencias," so I will not say where it was sold.</p>
    {f_do2}
    <p>Cream versions are common now. Jeepe describes <em>nama dorayaki</em> as fresh or whipped cream with bean paste, eaten chilled, and says it needs refrigeration and should be eaten soon. It also lists chestnut and matcha among recent fillings without details. The Commons descriptions for these two photographs mention matcha cream and strawberry cream, but I cannot tell you which is which from the pictures, so look at the colors and not the label.</p>
    {f_do4}
    <p>The Commons description (in Japanese) calls this fresh dorayaki served at a Kyoto wagashi shop, 臙八瑞雲堂. The filling looks like a thick layer of white cream, and the top is browned dark with a mark burned into it.</p>
    <p>Practical notes from Jeepe: unwrapped dorayaki is best the day you buy it or the next; individually wrapped ones with an oxygen absorber keep for roughly two to three weeks (the page also gives about 30 days, and does not reconcile the two), so read the label. It gives roughly ¥200 to 350 at specialty wagashi shops and ¥100 to 200 at convenience stores.</p>

    <h2 id="warabimochi">Warabimochi<span class="h2-jp">わらび餅</span></h2>
    <p>Warabimochi is a soft, jiggly chilled sweet, usually dusted with kinako (roasted soybean flour) or drizzled with kuromitsu (black sugar syrup), or both. {JW} says it is traditionally made from <em>warabi-ko</em>, starch from bracken fern roots, with water and sugar, heated and then cooled to set. It says pure bracken starch is rare and laborious to produce, and that most commercial versions use other starches such as sweet potato, tapioca or kudzu. A highly translucent one probably contains other starch, since the page describes the pure version as dark, glossy and strongly sticky.</p>
    {f_wa1}
    <p>These pieces look translucent and grey-violet, but the blue glass bowl is tinting them, so judge the color by the kinako and syrup, not by the pieces. The Commons description credits the maker as 明日香食品, a company name, and does not say what starch it uses.</p>
    {f_wa2}
    <p>A simpler plate: pieces coated in kinako with dark syrup over them and a bamboo pick to eat with. Jeepe suggests tasting it plain first, then with kinako, then with kuromitsu. It links warabimochi with summer because it is served cold, but also quotes the agriculture ministry as saying it is enjoyed year-round.</p>
    <p>On history, Jeepe lists warabimochi as a traditional Nara food and tells a local legend that monks at Todai-ji began making it from bracken roots on Mount Wakakusa and served it as a tea sweet. It presents this as legend. The page also warns that fresh warabimochi has a short shelf life and that a pure-starch one changes texture quickly, so eat it soon. Its prices disagree between sections: sweet shops are roughly ¥500 to 1,000 in one place and ¥600 to 1,200 in another, and store packs are cheaper.</p>

    <h2 id="monaka">Monaka<span class="h2-jp">最中</span></h2>
    <p>Monaka is a crisp wafer shell filled with sweet paste. {FM} says the shell is made from glutinous rice flour and water, baked thin in decorated iron molds, and that the texture is dry and crunchy, not soft. The classic filling is sweet azuki paste, and it also lists white bean paste, chestnut purée and matcha cream, plus ice cream versions in the same kind of shell.</p>
    {f_mo1}
    <p>The label on this photograph is <em>tawara</em> monaka, from the Commons description. <em>Tawara</em> means a straw rice bale, which I take to be the oval shape, though the description does not explain it. Cut open, the paste fills the shell almost to the edge.</p>
    {f_mo2}
    <p>An older photograph, from 2007, with the lid lifted to show a chunky paste with whole beans.</p>
    <p>On the name, Food in Japan says <em>monaka</em> comes from <em>monaka no tsuki</em>, "the moon in the middle," and that court nobles reportedly ate simple round rice wafers at moon-viewing banquets in the Edo period, with bean paste added in the Meiji era after molds improved. The page gives no sources for that history, so treat it as one account. It also says the dry shell and paste keep without refrigeration but gives no duration, so rely on the label.</p>

    <h2 id="water">Water Sweets: Raindrop Cake and Shitatari<span class="h2-jp">水信玄餅としたたり</span></h2>

    <h3>Raindrop Cake</h3>
    <p>This is the clear dome that went viral abroad as raindrop cake. In Japan the best-known version is Kinseiken's <em>mizu shingen mochi</em> from Yamanashi. The {MT} says it is made from two things, Yamanashi water and agar, and is served with kuromitsu (black sugar syrup) and kinako (roasted soybean flour). It also says the cake melts after about 30 minutes at room temperature. That page gives no creation date, only that the Daigahara shop opened in 1902.</p>
    {f_rd}
    <p>The photograph shows the dome in a wooden tray with a pile of light brown powder on one side and dark syrup on the other, which matches that pairing. The Commons description places it in Los Angeles, and its source line names mizu shingen mochi with black syrup, so this is not the Yamanashi original. {SN} reported in 2014 that the Kinseiken original was sold on weekends and holidays from June to the end of September, and only to eat in. That is an old report, so check the shop before you plan a trip around it.</p>

    <h3>Shitatari</h3>
    {f_sh}
    <p>The Commons description (in Japanese) calls this <em>shitatari</em>, a sweet from the Kyoto wagashi shop Kamehiroei, and says it is linked to the Kikusui-hoko float of the Gion Festival. The photograph shows two amber, translucent blocks on a glass dish. I have not sourced the ingredients or the story behind the name, so all I can say is what the picture and the description say.</p>

    <h2 id="anmitsu">Anmitsu<span class="h2-jp">あんみつ</span></h2>
    <p>{FAN} describes anmitsu as a chilled dessert built on cubes of <em>kanten</em> (agar jelly), topped with sweet red bean paste, fruit and shiratama dumplings, with <em>kuromitsu</em> (black sugar syrup) on the side so you can set the sweetness yourself. It says mitsumame is the closest relative, and that mitsumame becomes anmitsu once bean paste is added. Summer is the classic season, but shops use strawberry in spring and chestnut in autumn.</p>
    {f_an1}
    <p>Here the bowl has a scoop of ice cream and fruit with the syrup in a small glass, which is the <em>cream anmitsu</em> style the page lists. The Commons file gives no shop for this one.</p>
    {f_an2}
    <p>A fuller bowl, with the paste in the middle and clear jelly cubes, pink and white sweets, a white dumpling, a green ball and fruit around it. I will not name the items, since the Commons description does not.</p>
    {f_ko}
    <p>Not anmitsu, but the same cold-sweet idea: green shaved ice with a piece of mochi and bean paste. The Commons description says the green syrup is matcha and that the piece inside is the shop's own mochi sweet. I leave the shop out because it is a brand name, and the description is the only source I have.</p>
    <p>On origins, Food in Japan credits the Asakusa shop Funawa with the first mitsumame in 1903 and says "many sources" credit Ginza Wakamatsu with adding bean paste in 1930, with a rival claim from about 1938. It cites none of them clearly, so treat the story as uncertain. It also gives café prices of about ¥700 to 1,300.</p>

    <h2 id="kintsuba">Kintsuba<span class="h2-jp">きんつば</span></h2>
    <p>{JPK} describes kintsuba as sweet azuki paste, usually chunky, set with agar and wrapped in a thin layer of wheat-flour dough. The classic form is a brick, and the name is read as "gold sword guard," <em>tsuba</em> being the guard on a sword. It says the sweet began mid-Edo in Osaka with rice flour as <em>gintsuba</em> (silver), and that in Edo wheat flour replaced the rice flour and the name changed to kintsuba because gold is worth more. That history is the page's own account.</p>
    {f_ki1}
    <p>This disc is the round style, grilled on the flat faces, with one broken open so you can see the paste. The Commons file does not name the shop. I mention the shape because the brick form is the one the Japanese Products page calls most common.</p>
    {f_ki2}
    <p>A different look: a thick, dark, almost cake-like round with black sesame on top. The Commons file does not describe it, so I cannot say how it is made.</p>

    <h2 id="beans">Beans and Mochi: Amanatto and Mame Daifuku<span class="h2-jp">甘納豆と豆大福</span></h2>
    <p>{JPA} says amanatto is not related to natto: beans are simmered in sugar syrup, coated in sugar and dried. It lists azuki, broad beans, kidney beans, peanuts and black soybeans, and says it can replace raisins in bread or cake. It claims "over 150 years" of history in one place and "over a century" in another, and gives no origin for the name.</p>
    {f_am}
    <p>Four kinds on one plate, from left to right as I read them: a green bean, a reddish-brown bean, a dark purple-red bean and amber slices that I think are a root or a squash. The Commons file does not name them.</p>
    <p>Mame daifuku is a daifuku with beans in the mochi itself.</p>
    {f_md}
    <p>The cut piece shows smooth red paste and one large dark bean, and the whole one shows dark beans under the dusting. The Commons file says this is a typical example. For a salty-sweet version, {SZK} sells a shiomame daifuku with salted red peas set into the paste, made only on the day, but that is one shop's product, not a rule for the sweet.</p>

    <h2 id="crackers">Senbei: The Salty-Sweet Crackers<span class="h2-jp">せんべい</span></h2>
    <p>Senbei sits next to wagashi on shop shelves. {JPN} describes nanbu senbei as a wheat cracker, not a rice one, from Hachinohe in Aomori, made mainly in Aomori and Iwate. It has a crisp rim and a thick center where sesame, peanuts or walnuts are often set. The page says it keeps well and was originally an emergency food, and that Aomori versions tend to be salty while Iwate versions lean sweet.</p>
    {f_nb}
    <p>A peanut nanbu senbei, per the Commons description, made in Iwate. The raised rim and the peanuts pressed into the middle match the page's description.</p>
    {f_be}
    <p>A rice cracker with beans, which the Commons file calls <em>beika</em>. It is from 2005, and I have no source on how it is made, so I show it only as a contrast with the wheat cracker above.</p>

    <h2 id="snacks">Not Quite Wagashi: Gohei Mochi and Daigaku Imo<span class="h2-jp">五平餅と大学芋</span></h2>
    <p>Two sweet-and-savory snacks come up in any talk of traditional sweets, and both are closer to street or regional food than to tea-ceremony wagashi. I include them because I was sent good photographs, and I would rather say plainly what they are.</p>

    <h3>Gohei Mochi</h3>
    <p>{FUN} places gohei mochi mainly in the Kiso and Ina districts of Nagano, in Gifu, and in the Mikawa district of Aichi. It says cooked non-glutinous rice is crushed, pierced onto a bamboo skewer and grilled with soy sauce, miso or sesame sauces, and that shapes (round, flat, tube) vary by family. One skewer is about ¥200 there.</p>
    {f_g1}
    <p>Flattened rounds with a glossy brown glaze and charred edges, still on the skewers. The Commons description just says "finished gohei mochi," so I cannot tell you the sauce.</p>
    {f_g2}
    <p>This one is the long oval form. {MAFF} calls the most common shape a flat oval, <em>waraji</em>, after the straw sandal, and says the rice is dipped in a miso sauce that households and shops mix their own way, sometimes with walnuts, sesame, peanuts or green onion. The photograph's description gives only a place name in Shinshiro, Aichi, and the Commons file does not name the sauce, so treat this as an example of the shape.</p>
    <p>The MAFF page says it may date to the mid-Edo period, about 1700 to 1750, and that lumberjacks and hunters reportedly ate it before a mountain festival. It lists several theories for the name, so I will not pick one.</p>

    <h3>Daigaku Imo</h3>
    {f_da}
    <p>Daigaku imo means "university potato." {FD} describes chunks of sweet potato fried and tossed in a sugar syrup, usually finished with black sesame, as in this photograph. It says the name has no confirmed origin: theories about student customers, a shop near a university and a student selling it to pay tuition are all unproven. It is a natural autumn and early-winter snack, sold at specialty shops, food halls and festival stalls, served warm or at room temperature.</p>

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

    <p style="font-size:14px;color:var(--enshu);line-height:1.7;margin-top:32px;"><strong>Sources:</strong> ichigo daifuku from {FIJ}; yokan from {JY}; taiyaki from {TWK}; dorayaki from {JD}; warabimochi from {JW}; monaka from {FM}; nerikiri from {JN}; anmitsu from {FAN}; kintsuba from {JPK}; amanatto from {JPA}; mame daifuku from {SZK}; nanbu senbei from {JPN}; gohei mochi from {FUN} and {MAFF}; daigaku imo from {FD}; raindrop cake from {MT} and {SN}. Photograph details come from the Wikimedia Commons descriptions. I have not verified current shop details, prices or opening hours.</p>

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
tail=re.sub(r'(<meta name="keywords" content=")[^"]*(")',r'\1wagashi, Japanese sweets, ichigo daifuku, yokan, uiro, almond tofu, dorayaki, warabimochi, monaka, nerikiri, anmitsu, kintsuba, amanatto, senbei, gohei mochi, daigaku imo, Japanese confectionery\2',tail)
exec(tail)
