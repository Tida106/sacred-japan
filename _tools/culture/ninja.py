import sys
sys.path.insert(0, '/home/claude/sacred-japan/_tools/culture')
from shinobi_common import *

S = 'ninja'
A = '/mnt/user-data/attachments/10bb6ae3-4ce9-510b-a21d-16a428fc4d73/'
copy_photos(S, {'house': A+'26326240-image.jpg', 'costume': A+'060f8788-image.png', 'sign': A+'40ec3ad8-image.jpg',
                'panorama': A+'42e85883-image.jpg', 'show': A+'20cb774e-image.jpg', 'performer': A+'7ffdb7fc-image.jpg',
                'shuriken': A+'b0b747c1-image.jpg', 'castle1': A+'6c278486-image.jpg', 'castle2': A+'a434f596-image.jpg'})
fig = make_fig(S)

copy_photos(S, {'koka_village': A+'856ded55-image.jpg', 'yashiki_2009': A+'ee4942b0-image.jpg', 'yashiki_pano': A+'0754f8a7-image.jpg',
    'yashiki_attic': A+'6e896a39-image.jpg', 'ks_armor': A+'4e2bf04e-image.jpg', 'ks_haidate': A+'63962e40-image.jpg',
    'ks_gauntlet': A+'4363cbca-image.jpg', 'ks_fundo': A+'23d85393-image.jpg', 'ks_jitte_black': A+'6cc77561-image.jpg',
    'ks_small': A+'7acbcbfd-image.jpg', 'ks_rope': A+'3cf919e3-image.jpg', 'ks_hooks': A+'cb0a8f41-image.jpg',
    'ks_chain': A+'0c9db564-image.jpg', 'ks_bow': A+'39aeb925-image.jpg', 'ks_pipe': A+'e745feb3-image.jpg',
    'plala_gun': A+'9e86584b-image.jpg', 'plala_mail': A+'2c738889-image.jpg', 'aburahi': A+'7cb318fc-image.jpg'})
PD_SELF = 'public domain (released by the author)'
MOT = lambda d: f'Photo: Motokoka, {BYSA4}, {d}, {VIA}'
f_kv = fig('koka_village', 'A thatched house with a white wall, a gravel path and a small stone stair among trees, with a person on the stair',
  'The Koga-no-sato ninja village, as labeled on Commons.', f'Photo: z tanuki, {BY3}, 25 August 2012, {VIA}', maxw=900)
f_y09 = fig('yashiki_2009', 'A large thatched building with a tiled roof, two painted cut-out ninja boards and parked cars in front',
  'The entrance of the Koka-ryu Ninjutsu Yashiki in 2009.', f'Photo: Mocchy, {PD_SELF}, 23 August 2009, {VIA}')
f_ypano = fig('yashiki_pano', 'A wide view of a thatched house behind a wooden gate frame and a low wall, with a pink ninja cut-out board at the right',
  'A wide view of the same house from the gravel yard.', f'Photo: z tanuki, {BY3}, 25 August 2012, {VIA}', maxw=900)
f_att = fig('yashiki_attic', 'A dim attic under a thatched roof, where a masked visitor steps down through an opening in a wooden floor',
  'Inside the thatched house, April 2023.', f'Photo: m-louis, {BYSA2}, 1 April 2023, {VIA}')
f_arm = fig('ks_armor', 'A display case with a folded portable armor of dark lacquered plates joined by chain mail, with blue cords and red lacquered lower plates',
  'Portable ninja armor at the Kusuri Gakushukan, Koka.', MOT('15 September 2019'))
f_hai = fig('ks_haidate', 'A thigh guard made of chain mail on cloth, in three panels, with a small label reading haidate',
  'A haidate, a thigh guard, from the same set.', MOT('15 September 2019'))
f_gau = fig('ks_gauntlet', 'Two chain-mail gauntlets and a pair of shin guards with lacquered plates, in a red-lined case',
  'Chain gauntlets and shin guards.', MOT('15 September 2019'))
f_fun = fig('ks_fundo', 'A gourd-shaped iron weight on a dark cord, with a label reading nuke-fundo',
  'A gourd-shaped weight on a cord.', MOT('15 September 2019'))
f_jb = fig('ks_jitte_black', 'A black three-pronged jitte and a blade-shaped portable spear head on a red cloth, with two labels',
  'A black jitte and a portable spear.', MOT('15 September 2019'))
f_sm = fig('ks_small', 'A case with a four-point shuriken, a spiked iron ball on a wooden block, a kunai and a caltrop, each with a label',
  'Throwing and scattering tools.', MOT('15 September 2019'))
f_rope = fig('ks_rope', 'A case with a coiled rope and hook, a spiked finger lock, a long awl, a hand-worn blade and a scroll of rope-binding figures',
  'Rope, hook and hand tools.', MOT('15 September 2019'))
f_hook = fig('ks_hooks', 'A case with a forked hook, a jitte with a long tassel and a copy of a scroll with binding figures',
  'Hooks and a jitte.', MOT('15 September 2019'))
f_chain = fig('ks_chain', 'A case with a folding multi-bladed hook on a cord and a chain sickle with a weight, with labels',
  'A chain sickle and a collapsible hook.', MOT('15 September 2019'))
f_bow = fig('ks_bow', 'A case with a short bow wrapped in dark bands, a plain arrow and an arrow with a paper tube tied to the shaft',
  'A small bow and arrows.', MOT('15 September 2019'))
f_pipe = fig('ks_pipe', 'A slightly blurred photo of a long brass-ended pipe in a case, with a diagram card and three small iron balls',
  'A ninja pipe, with a diagram card.', MOT('15 September 2019'))
f_gun = fig('plala_gun', 'A dagger-like hilt and sheath on orange cloth, a bullet mold, a small ball and caltrops with labels',
  'A concealed gun, a bullet mold and caltrops at Shinobi no sato PLALA.', MOT('21 February 2016'))
f_mail = fig('plala_mail', 'A mannequin head in a chain-mail hood over a patterned cloth, with a mail shirt and gauntlets on a red display',
  'Chain mail at Shinobi no sato PLALA.', MOT('21 February 2016'))
f_abu = fig('aburahi', 'A long covered wooden corridor with thick round pillars and a plank floor, open to trees on one side',
  'The cloister of Aburahi Shrine in Koka.', MOT('15 September 2019'))
f_house = fig('house', 'A thatched-roof house behind pruned pines and a gravel path, with a low gate and tiled wall in front',
  'A thatched house in the grounds of the Ninja Museum of Igaryu, Iga Ueno.', f'Photo: z tanuki, {BY3}, 6 October 2013, {VIA}', hero=True)
f_costume = fig('costume', 'A museum case with dark ninja clothing, a hooded garment, straw sandals and a straw hat, with explanatory labels',
  'Ninja clothing and gear on display at the museum.', f'Photo: Jeremy Hall, {BY2}, 25 February 2006, {VIA}')
f_sign = fig('sign', 'A stone sign reading Igaryu Ninja Museum in front of a thatched building among tall pines',
  'The stone sign at the museum entrance.', f'Photo: Hide-sp, {BYSA3}, 5 September 2007, {VIA}')
f_pano = fig('panorama', 'A wide view of a gravel plaza with a red shrine gate at the left and a low tiled building with an awning at the right',
  'The plaza near the museum entrance, in a wide view.', f'Photo: z tanuki, {BY3}, {VIA}', maxw=900)
f_show = fig('show', 'An audience seated on benches watches a performer on a stage with red ninja characters on the backdrop',
  'The ninja show at the Iga museum.', f'Photo: John Gillespie, {BYSA2}, 17 May 2012, {VIA}')
f_perf = fig('performer', 'A performer in a brown ninja costume holds a sword and points ahead, in front of a red ninja character',
  'A performer during the show.', f'Photo: John Gillespie, {BYSA2}, 17 May 2012, {VIA}')
f_shuri = fig('shuriken', 'A smiling guide in a light costume holds a board showing eight throwing-star shapes, a ring and a spike',
  'A guide with a board of throwing tools.', f'Photo: specialoperations, {BYSA2}, 17 May 2012, {VIA}', maxw=420)
f_c1 = fig('castle1', 'A wide dusk view over green trees and a town toward a small white castle keep, with mountains behind',
  'A distant view toward what appears to be Iga Ueno Castle.', f'Photo: carloshonda, {BY3}, 12 April 2014, {VIA}')
f_c2 = fig('castle2', 'A castle keep on a hill above a high stone wall and a moat, with cherry trees and flat land beyond',
  'The keep and its high stone wall, from above.', f'Photo: carloshonda, {BY3}, 12 April 2014, {VIA}')

JTR = ext('https://www.japan.travel/en/japan-magazine/discover-origins-ninja-iga-koka/', 'Japan National Tourism Organization (JNTO)', 'ninja_src_jnto')
IGA = ext('https://iganinja.jp/en/museum', 'the museum\'s official English page', 'ninja_src_iga_official')
JG = ext('https://japan-guide.com/e/e4351.html', 'japan-guide.com', 'ninja_src_japanguide')
GLT = ext('https://www.gltjp.com/en/directory/item/11744/', 'GLTJP', 'ninja_src_gltjp')
KWJ = ext('https://web-japan.org/kidsweb/travel/ninja/ninja02.html', 'Kids Web Japan', 'ninja_src_kidsweb')
TO = ext('https://www.timeout.com/tokyo/news/japan-ninja-council-now-offers-ninja-courses-in-asakusa-071621', 'Time Out Tokyo', 'ninja_src_timeout')
FESTA = ext('https://en.wikipedia.org/wiki/Iga_Ueno_Ninja_Festa', 'Wikipedia', 'ninja_src_festa')
ANN_K = ext('https://www.animenewsnetwork.com/encyclopedia/people.php?id=8036', 'Anime News Network', 'ninja_src_ann')
NARU = ext('https://naruto-official.com/en/about', 'the official Naruto site', 'ninja_src_naruto')
BASI = ext('https://animenewsnetwork.com/news/2017-07-19/basilisk-sequel-novels-get-tv-anime-manga/.119037', 'Anime News Network', 'ninja_src_basilisk')
VI_NIN = viator('Japan+ninja+experience')

faqs = [
    ("Where did the ninja come from?",
     "Japan's tourism organization says Iga (Mie Prefecture) and Koka (Shiga Prefecture), neighboring areas in the Kinki region, are the birthplaces of the ninja, and that ninja rose to prominence in the Sengoku period (1467 to 1568), working as covert operatives and spies for their lords. The same page is tourism promotion and hedges many claims with \"said to,\" so treat the colorful details as local tradition."),
    ("What is the difference between Iga and Koka?",
     "They are two neighboring areas, Iga in Mie and Koka in Shiga, with Koka to the north. Each has its own ninja sites: the Ninja Museum of Igaryu in Iga Ueno, and the Koka Ninja Village and a trick-house residence in Koka."),
    ("Is the ninja show at the Iga museum in English?",
     "japan-guide.com says the show is in Japanese only, but that the action, including a throwing-star demonstration, is easy to follow without the language. The exhibition signs are in Japanese and English."),
    ("How much does the Ninja Museum of Igaryu cost?",
     "Sources differ. The museum's official English page lists adults at 1,000 yen and the show at 600 yen, with six shuriken throws for 300 yen. japan-guide.com lists 800 yen for the museum and 500 yen for the show. Neither page is dated clearly, so check the museum before you go."),
    ("Can I try ninja training in Tokyo?",
     "In 2021 Time Out Tokyo reported courses at the Ninja Information Centre Tokyo & Dojo in Asakusa, run by the Japan Ninja Council, from a 40-minute experience at 2,200 yen to a 90-minute course at 9,900 yen. That is an old report, so please confirm what is offered now."),
    ("When is the Iga Ueno Ninja Festa?",
     "Wikipedia gives it as an annual, family-friendly festival running from April 1 to May 6 in Iga, and says people in ninja costume ride Iga train lines free. Dates can change, so check the local tourism information."),
    ("Are ninja and samurai the same?",
     "No. Samurai were the warrior class; the ninja described here were covert operatives from Iga and Koka. Our samurai guide covers the warrior class and the end of their era."),
]
faq_html, faq_ld = faq_blocks(faqs)

main = f'''<main>

  {f_house}

  <aside class="toc" aria-label="Table of contents">
    <div class="toc-label">TABLE OF CONTENTS ／ 目次</div>
    <div class="toc-title">In This Guide</div>
    <ol>
      <li><a href="#opening">Opening: A Note from the Guide</a></li>
      <li><a href="#who">Who the Ninja Were</a></li>
      <li><a href="#iga-koka">Iga and Koka</a></li>
      <li><a href="#visit">Places to Visit</a></li>
      <li><a href="#experience">Experiences and the Ninja Festa</a></li>
      <li><a href="#media">Ninja in Manga and Anime</a></li>
      <li><a href="#faq">Frequently Asked Questions</a></li>
      <li><a href="#final">Final Thoughts</a></li>
    </ol>
  </aside>

  <article>

    <section id="opening">
      <p class="opening">Ask a visitor to draw a ninja and you will get a figure in black, throwing stars. Ask a historian and the answer is quieter, and tied to two valleys near Kyoto.</p>
      <p>As a licensed guide, I can tell you which places let you see how the real ninja houses worked, and which parts of the popular image come from fiction. This guide covers Iga and Koka, the museums and trick houses, a festival, and the manga that made the ninja famous. It also marks where my sources lean on tradition. For the warrior class they are often confused with, see our {link('/culture/samurai/', 'samurai guide', 'ninja_to_samurai')}.</p>
    </section>

    <h2 id="who">Who the Ninja Were<span class="h2-jp">忍者とは</span></h2>
    <p>Ninja (<span class="jp">忍者</span>), also called shinobi, were covert operatives. {JTR} describes them as covert warriors who came to prominence in the Sengoku period (1467 to 1568), working in espionage and other secret operations for their lords. It names the Fujibayashi family as specialists in fire and gunpowder-related techniques.</p>
    <p>A word on that source: it is a tourism-promotion page, and it hedges many claims with "said to." For example, it says the famous manual <em>Bansenshukai</em> is "said to have been written" in 1676. I will not repeat the more colorful claims, because I cannot confirm them. What the page, and the museums it points to, do agree on is the picture below: houses built to defend against intruders and a culture of information gathering.</p>
    <p>The museum's cases show the working side of that picture: dark, plain clothing, a hooded garment, straw sandals and a straw hat, each with a label in Japanese and English. Notice how ordinary most of it looks.</p>
    {f_costume}

    <h2 id="iga-koka">Iga and Koka<span class="h2-jp">伊賀と甲賀</span></h2>
    <p>{JTR} says Iga City (Mie) and Koka City (Shiga) sit next to each other in the Kinki region, with Koka to the north, and calls them the birthplaces of the ninja. It also says the two areas were self-governing in the Sengoku period, run by local families and samurai without a daimyo's authority, and that village codes called for deciding things by discussion. The two regions are also recognized as a Japan Heritage site with the name "Exploring the Birthplace of the Real Ninja."</p>
    <p>If you are planning a trip, the same page says day trips are possible from Osaka or Kyoto by train. For Iga you can take the Tokaido Shinkansen to Nagoya, and for Koka to Kyoto, and it mentions a Ninja Train on the Iga Railway from Kintetsu Iga-Kambe or JR Iga-Ueno.</p>

    <h2 id="visit">Places to Visit<span class="h2-jp">見学先</span></h2>

    <h3>Ninja Museum of Igaryu (Iga Ueno, Mie)</h3>
    <p>{JG} says the museum is in Ueno Park, a 5 to 10 minute walk north of Uenoshi Station. It has three parts: a ninja residence that looks ordinary outside but has revolving walls, trap doors and hidden compartments, explained on a guided tour; two exhibition halls of tools, costumes and weapons with Japanese and English signs; and a ninja show with real weapons. {IGA} adds that the exhibits include more than 400 ninja tools and that some can be tried. {JTR} says it stands on the site of the former Heirakuji Temple.</p>
    <ul>
      <li><strong>Hours:</strong> 10:00 to 16:00 on weekdays (last entry 15:30) and 10:00 to 16:30 on weekends and holidays (last entry 16:00), per the official page. It lists a closure from December 29 to January 1.</li>
      <li><strong>Admission:</strong> adults 1,000 yen and children 700 yen, with the show at 600 yen and six shuriken throws at 300 yen, according to the official page. japan-guide.com gives lower figures (800 yen and 500 yen), so please confirm before you go.</li>
    </ul>
    <p>The entrance is marked by a stone sign reading Igaryu Ninja Museum, set among tall pines in front of a thatched building. Beyond it a gravel plaza opens up, with a small red shrine gate on one side and a low tiled building with an awning on the other.</p>
    {f_sign}
    {f_pano}
    <p>The ninja show is performed on an open stage with benches, under a backdrop of red ninja characters, and the audience sits close. The performer shows weapons and moves with a sword, and the pointing gesture in the second photo shows how near the action is. A guide also explains throwing tools on a board; one of the shapes is a manji (卍), the swastika-like symbol used in Buddhism in Japan. Sources say the show is in Japanese, but the action is easy to follow.</p>
    {f_show}
    {f_perf}
    {f_shuri}

    <h3>Koka Ninja Village (Koka, Shiga)</h3>
    <p>{GLT} (listing updated in May 2026) describes a village at the foot of the Suzuka Mountains with a ninjutsu museum in a thatched house believed to have belonged to Koka ninja, a trick house that is the relocated home of the Fujibayashi family, with a flipping wall, hidden stairs and an escape hole under a hearth, and a ninja dojo with nine practice places.</p>
    <ul>
      <li><strong>Hours:</strong> 10:00 to 17:00, last entry 16:00, closed Mondays (the next day if Monday is a holiday).</li>
      <li><strong>Admission:</strong> 2,000 yen for adults and 1,500 yen for children. Credit cards are not accepted, so bring cash.</li>
      <li><strong>Getting there:</strong> a free shuttle of about 5 minutes from Koka Station on the JR Kusatsu Line.</li>
    </ul>
    <p>Commons labels this photo "Koga-no-sato Ninja village" (甲賀の里 忍術村). It shows a thatched house with a white wall, a gravel path and a small stone stair among trees, with one visitor coming down the stair. It is a 2012 photo, so details may have changed.</p>
    {f_kv}

    <h3>Koka-ryu Ninjutsu Yashiki (Koka, Shiga)</h3>
    <p>{KWJ} describes a samurai residence built about 300 years ago that looks like a single-story thatched house but has three stories, with a pitfall trap, a revolving wall for vanishing quickly and a rope ladder from the third floor to the ground-floor entrance. {JTR} dates it to the Genroku era and says it is within walking distance of Konan Station, and the Kids Web Japan page gives the route as the JR Tokaido Line from Kyoto, changing at Kusatsu to the Kusatsu Line.</p>
    <p>From the street the house looks like a large thatched farmhouse. In a 2009 photo, two painted cut-out boards of ninja stand in the gravel yard for visitors to pose behind, and a small stone nearby reads "entrance" (入口). Wooden posts carry the name Koka-ryu Ninjutsu Yashiki (甲賀流 忍術屋敷).</p>
    {f_y09}
    <p>A wider 2012 view shows the whole front: a thatched main roof with tiled eaves, a low wall and a wooden gate frame.</p>
    {f_ypano}
    <p>The interior photo below was taken in April 2023 and shows an attic space under the thatch, where a masked visitor steps down through an opening in the plank floor. It looks like a floor hatch, but Commons gives no explanation, so I will not claim how it was used.</p>
    {f_att}

    <h3>Ninja Tools in Koka: Kusuri Gakushukan and PLALA</h3>
    <p>Many of the photos of Koka ninja tools on Wikimedia Commons come from the Kusuri Gakushukan (甲賀市くすり学習館, a medicine museum) in Koka, and two more from Shinobi no sato PLALA. I have not verified the opening hours or admission of either place, so please check before you go. The labels in the cases end with a line reading 澤田平氏蔵, which I read as crediting the owner of the item, but I have not confirmed that. Every item below is described from its label, and the labels use short, practical wording.</p>
    <p><strong>Armor that folds.</strong> The label for this armor says it folds to about the size of one floor cushion (zabuton) and can be carried. The photo shows dark lacquered plates joined by chain mail, blue cords and red lacquered plates at the bottom.</p>
    {f_arm}
    <p>A haidate (佩盾) is a thigh guard. This one is chain mail on cloth in three panels, and it sits in the same case as the gauntlets.</p>
    {f_hai}
    <p>The label calls the set "Shinobi Sangu": chain gauntlets, haidate and shin guards (臑当), and says the set folds to the size of one floor cushion. On the left are lacquered shin guards joined by cord, and on the right two chain-mail gauntlets.</p>
    {f_gau}
    <p><strong>Hooks, jitte and binding.</strong> The label for the nanban-kagi says it is a ninja-specific weapon used to gouge eyes or hold down a wrist, and the label for the jitte says it is used to fight enemies and often appears in period dramas as a police tool. Behind them is a copy of a scroll, labeled as a document for passing on rope-binding methods.</p>
    {f_hook}
    <p>This case shows the hayanawa (a rope for binding criminals or enemies), the shinobi-kagi (a hook thrown and pulled when entering a building), the tsubokiri (an awl that makes holes in wooden houses and storehouses, labeled ninja-specific), the haya-tejo (a finger lock for gripping an opponent's wrist) and the shuto-ken (worn on the palm as a bare-hand weapon).</p>
    {f_rope}
    <p>The black jitte label says it defends against sword and spear attacks and can also serve as a weapon, since its tips are sharp. The "shinobi Kikuchi spear" next to it is labeled as a portable spear that you can tie to a stick or a branch with cord.</p>
    {f_jb}
    <p>The chain sickle is labeled as a farm sickle with a chain weight, used to tangle an opponent's weapon and then strike with the sickle. The folding tool on the left is labeled "Marohoshi" (an assembled jitte), described as a tool for catching an opponent's weapon and used in Miyamoto Musashi's two-sword style.</p>
    {f_chain}
    <p>The nuke-fundo is labeled as a gourd-shaped weight used by tangling it around a building or branch, with the advantage that it can be untied easily afterward.</p>
    {f_fun}
    <p><strong>Small things you throw or scatter.</strong> The case shows an itomaki shuriken (heavy, so labeled destructive), a spiked iron ball called tetsumari (thrown to hurt or stop an opponent), a kunai (for removing doors and shutters, also a weapon) and a makibishi (scattered so pursuers cannot follow; the label says its shape resembles a water-chestnut fruit).</p>
    {f_sm}
    <p>Caltrops are also on show at Shinobi no sato PLALA in the photo below, next to a dagger-like hilt that Commons describes as a knife concealing a gun, and a bullet mold. The labels read shikomi teppo (concealed gun), dangan igata (bullet mold), tetsubishi and shizenbishi, the last being natural caltrops made from plants.</p>
    {f_gun}
    <p><strong>Bow and arrows, and a pipe.</strong> The labels say the ninja bow and arrows are small because they were used to attack from the shadows, and that the "flying fire arrow" carries an explosive set alight and shot far by bow.</p>
    {f_bow}
    <p>The pipe photo is blurred, so I cannot read its label with confidence. Commons calls it a ninja pipe, and the diagram card beside it shows the inner shape of the pipe.</p>
    {f_pipe}
    <p>A last photo from PLALA shows a chain-mail hood on a mannequin, a mail shirt and gauntlets, called "kusari katabira" (鎖帷子, chain mail) on Commons.</p>
    {f_mail}

    <h3>Other places in Iga and Koka</h3>
    <p>{JTR} also lists Iga Ueno Castle, whose reconstructed keep stands behind a stone wall about 30 meters high; Matsumoto-in Temple in Iga (built 1616, a Shugendo temple); and Aburahi Shrine in Koka, where a corridor built in 1566 was once a meeting place for Koka samurai. These are good additions if you stay overnight in the area.</p>
    <p>These two aerial views, taken in April, show what appears to be Iga Ueno Castle: a small white keep over the town in the first, and the high stone wall and moat in the second. The photos carry a photographer's watermark, and Commons does not name the viewpoint, so treat the building as my reading.</p>
    {f_c1}
    {f_c2}
    <p>In Koka, the cloister of Aburahi Shrine shown below is described on Commons as a place where ninja are said to have met, which matches the corridor built in 1566 that {JTR} mentions. It is a long, covered wooden walkway with thick round pillars and a plank floor, open to the trees on one side.</p>
    {f_abu}

    <h2 id="experience">Experiences and the Ninja Festa<span class="h2-jp">体験とお祭り</span></h2>
    <ul>
      <li><strong>Ninja training in Tokyo.</strong> {TO} reported in July 2021 that the Japan Ninja Council runs courses at the Ninja Information Centre Tokyo &amp; Dojo in Asakusa: a 40-minute experience (shuriken, hand signs, an explanation of spy gear) at 2,200 yen, with costume rental at 1,100 yen extra, and longer courses of 60 and 90 minutes at 7,700 and 9,900 yen. It recommends booking. That report is old, so confirm current courses and prices.</li>
      <li><strong>Iga Ueno Ninja Festa.</strong> {FESTA} describes an annual family-friendly festival in Iga running from April 1 to May 6, with ninja-themed performances and contests. It says passengers in ninja costume ride Iga train lines free, and that since 2001 the mayor and city council have held a yearly session dressed as ninja. Treat the dates as a guide and confirm locally.</li>
      <li><strong>The NARUTO x BORUTO village on Awaji Island.</strong> For the fictional side, Nijigen no Mori in Hyogo recreates the Hidden Leaf Village with the 11-meter Hokage Rock, a three-story Heavenly Scroll attraction and a night projection show. Park entry is free and each attraction is ticketed; see our {link('/culture/nijigen-no-mori/', 'Nijigen no Mori guide', 'ninja_to_nijigen')} for tickets, rules and access.</li>
      <li><strong>Guided or hands-on tours.</strong> If you prefer a booked, English-language option, you can compare current {aff(VI_NIN, 'ninja experiences on Viator', 'ninja_viator_experience')}. I have not tried them myself, so please read recent reviews.</li>
    </ul>

    <h2 id="media">Ninja in Manga and Anime<span class="h2-jp">漫画・アニメ</span></h2>
    <p><strong>Naruto</strong> by Masashi Kishimoto ran in <em>Weekly Shonen Jump</em> from 1999 to 2014, and {NARU} says it follows Naruto Uzumaki, an outcast ninja from the Hidden Leaf Village, who wants to become Hokage. It lists 700 chapters, more than 250 million print copies worldwide, and an anime that began in 2002. {ANN_K} lists Kishimoto as born in 1974 in Okayama; if you visit that city, our {link('/guides/okayama-castle/', 'Okayama Castle guide', 'ninja_to_okayama')} covers its castle. I have no source tying the series' village to a real place, so I will not claim one. If you want to walk through a recreation of it, see our {link('/culture/nijigen-no-mori/', 'Nijigen no Mori guide', 'ninja_naruto_to_nijigen')}.</p>
    <p><strong>Basilisk</strong> comes closest to the real map. {BASI} says it adapts Futaro Yamada's 1959 novel <em>Koga Ninpocho</em> (<em>The Kouga Ninja Scrolls</em>) as a 2003 manga by Masaki Segawa, followed by a TV anime in 2005. The Iga and Kouga clans, sworn enemies for more than 400 years, are ordered under Ieyasu Tokugawa to send ten ninja each to fight for the succession, and the lovers Oboro (Iga) and Gennosuke (Kouga) are on opposite sides. "Kouga" is the story's spelling of the area this page writes as Koka, so the clans in the story are the two neighbors above.</p>
    <p>For samurai stories such as <em>Rurouni Kenshin</em> and <em>Vagabond</em>, see our {link('/culture/samurai/', 'samurai guide', 'ninja_media_to_samurai')}. Other series with real locations are in our {link('/anime/', 'anime pilgrimage hub', 'ninja_to_anime')}.</p>

    <h2 id="faq">Frequently Asked Questions<span class="h2-jp">よくあるご質問</span></h2>

    <div class="faq-stack">

{faq_html}    </div>

    <h2 id="final">Final Thoughts<span class="h2-jp">むすびに</span></h2>
    <p>If you have time for one stop, start with the Ninja Museum of Igaryu in Ueno Park. If you are in Shiga or coming from Kyoto, the Koka sites add the trick houses. Read <em>Basilisk</em> or watch its anime before you go and the two valleys will feel like places from a story.</p>

    <div class="closing-block">
      <span class="torii">🥷</span>
      <p>A turning wall, a hidden stair and a story told by shadows.</p>
    </div>

    <section class="related-section">
      <h2>Related Guides</h2>
      <span class="h2-jp">関連ガイド</span>
      <div class="related-grid">
        <a class="related-card" href="/culture/samurai/" onclick="trackEvent('click','internal','related_ninja_to_samurai')">
          <div class="related-card-label">SACRED JAPAN ／ GUIDE</div>
          <div class="related-card-title">⚔️ Samurai Guide →</div>
          <div class="related-card-desc">History, armor, samurai towns and festivals.</div>
        </a>
        <a class="related-card" href="/culture/samurai-and-ninja/" onclick="trackEvent('click','internal','related_ninja_to_hub')">
          <div class="related-card-label">SACRED JAPAN ／ FEATURE</div>
          <div class="related-card-title">🥷 Samurai &amp; Ninja Feature →</div>
          <div class="related-card-desc">Both guides, side by side, with places and events.</div>
        </a>
        <a class="related-card" href="/guides/best-castles-japan/" onclick="trackEvent('click','internal','related_ninja_to_castles')">
          <div class="related-card-label">SACRED JAPAN ／ GUIDE</div>
          <div class="related-card-title">🏯 Best Castles in Japan →</div>
          <div class="related-card-desc">Original keeps and where to see them.</div>
        </a>
        <a class="related-card" href="/anime/" onclick="trackEvent('click','internal','related_ninja_to_anime')">
          <div class="related-card-label">SACRED JAPAN ／ HUB</div>
          <div class="related-card-title">🎬 Anime Pilgrimage →</div>
          <div class="related-card-desc">Real places behind favorite series.</div>
        </a>
      </div>
    </section>

    <p style="font-size:14px;color:var(--enshu);line-height:1.7;margin-top:32px;"><strong>Sources:</strong> origins and sites from {JTR}; the Iga museum from {IGA} and {JG}; Koka Ninja Village from {GLT}; the Koka residence from {KWJ}; Tokyo courses from {TO}; the festival from {FESTA}; Naruto from {NARU} and {ANN_K}; Basilisk from {BASI}. I have not verified current prices, hours or event dates.</p>

  </article>

</main>'''

TITLE = 'Ninja Guide: Iga, Koka, Ninja Museums, Experiences and Manga'
DESC = "A licensed guide's English introduction to the ninja: Iga and Koka, the Ninja Museum of Igaryu and Koka Ninja Village, trick houses, ninja experiences, the Ninja Festa, and Naruto and Basilisk."
KEYWORDS = 'ninja, ninja guide, Iga ninja, Koka ninja, Ninja Museum of Igaryu, Iga-ryu Ninja Museum, Koka Ninja Village, ninja experience Japan, Iga Ueno Ninja Festa, Naruto, Basilisk, shinobi'
url = finish(S, TITLE, DESC, KEYWORDS, '忍', 'The <em>Ninja</em> Guide', '忍者ガイド',
             'Iga, Koka, Museums, Experiences and Manga', 'Ninja Guide', 'guide_ninja',
             'Japan+ninja+experience', main, faq_ld)
print(url)
