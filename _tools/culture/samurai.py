import sys
sys.path.insert(0, '/home/claude/sacred-japan/_tools/culture')
from shinobi_common import *

S = 'samurai'
copy_photos(S, {
    'armor-case': 'guides/matsue-castle/images/armor-case.jpg',
    'armor-kato': 'guides/matsuyama-castle/images/armor-kato.jpg',
    'armor-red': 'guides/okayama-castle/images/armour-red.jpg',
    'helmet-horned': 'guides/matsue-castle/images/helmet-horned.jpg',
    'sword': 'guides/okayama-castle/images/sword.jpg',
    'shiomi-nawate': 'guides/matsue-castle/images/shiomi-nawate.jpg',
    'odachi': '/mnt/user-data/attachments/10bb6ae3-4ce9-510b-a21d-16a428fc4d73/5414e4b3-image.png',
    'iwate_sword': '/mnt/user-data/attachments/10bb6ae3-4ce9-510b-a21d-16a428fc4d73/a70b17c3-image.jpg',
    'shosoin_copy': '/mnt/user-data/attachments/10bb6ae3-4ce9-510b-a21d-16a428fc4d73/ffc15e14-image.jpg',
    'lacma_swords': '/mnt/user-data/attachments/10bb6ae3-4ce9-510b-a21d-16a428fc4d73/27090b42-image.jpg',
    'met_wakizashi': '/mnt/user-data/attachments/10bb6ae3-4ce9-510b-a21d-16a428fc4d73/ecbeae21-image.png',
    'auckland_scabbard': '/mnt/user-data/attachments/10bb6ae3-4ce9-510b-a21d-16a428fc4d73/9663fdf1-image.jpg',
    'tsuba_brass': '/mnt/user-data/attachments/10bb6ae3-4ce9-510b-a21d-16a428fc4d73/26b7086d-image.jpg',
    'tsuba_fuji': '/mnt/user-data/attachments/10bb6ae3-4ce9-510b-a21d-16a428fc4d73/97b36e84-image.jpg',
    'tsuba_dragon': '/mnt/user-data/attachments/10bb6ae3-4ce9-510b-a21d-16a428fc4d73/a5324179-image.jpg',
    'tsuba_cranes': '/mnt/user-data/attachments/10bb6ae3-4ce9-510b-a21d-16a428fc4d73/2bf15f46-image.jpg',
    'met_front': '/mnt/user-data/attachments/10bb6ae3-4ce9-510b-a21d-16a428fc4d73/747a0622-image.jpg',
    'met_back': '/mnt/user-data/attachments/10bb6ae3-4ce9-510b-a21d-16a428fc4d73/0467600e-image.jpg',
    'met_side': '/mnt/user-data/attachments/10bb6ae3-4ce9-510b-a21d-16a428fc4d73/912c8c39-image.jpg',
    'met_close': '/mnt/user-data/attachments/10bb6ae3-4ce9-510b-a21d-16a428fc4d73/f8b71ca8-image.jpg',
    'chiba_stripe': '/mnt/user-data/attachments/10bb6ae3-4ce9-510b-a21d-16a428fc4d73/2f0de62d-image.jpg',
    'chiba_crescent': '/mnt/user-data/attachments/10bb6ae3-4ce9-510b-a21d-16a428fc4d73/72e35561-image.jpg',
    'chiba_horned': '/mnt/user-data/attachments/10bb6ae3-4ce9-510b-a21d-16a428fc4d73/937f7e63-image.jpg',
    'chiba_vcrest': '/mnt/user-data/attachments/10bb6ae3-4ce9-510b-a21d-16a428fc4d73/4cdecf07-image.jpg',
    'chiba_flame': '/mnt/user-data/attachments/10bb6ae3-4ce9-510b-a21d-16a428fc4d73/6f9b711b-image.jpg',
    'chiba_dragon': '/mnt/user-data/attachments/10bb6ae3-4ce9-510b-a21d-16a428fc4d73/40819a22-image.jpg',
    'chiba_oyoroi': '/mnt/user-data/attachments/10bb6ae3-4ce9-510b-a21d-16a428fc4d73/59088d76-image.jpg',
    'chiba_domaru': '/mnt/user-data/attachments/10bb6ae3-4ce9-510b-a21d-16a428fc4d73/2cef16e5-image.jpg',
    'guimet_helm': '/mnt/user-data/attachments/10bb6ae3-4ce9-510b-a21d-16a428fc4d73/0dc6caa3-image.jpg',
    'met_five': '/mnt/user-data/attachments/10bb6ae3-4ce9-510b-a21d-16a428fc4d73/12fbffa0-image.jpg',
    'dallas_three': '/mnt/user-data/attachments/10bb6ae3-4ce9-510b-a21d-16a428fc4d73/5e2a97e3-image.jpg',
    'glenbow_helm': '/mnt/user-data/attachments/10bb6ae3-4ce9-510b-a21d-16a428fc4d73/0a86e424-image.jpg',
    'glenbow_seated': '/mnt/user-data/attachments/10bb6ae3-4ce9-510b-a21d-16a428fc4d73/bce0f820-image.jpg',
    'guimet_purple': '/mnt/user-data/attachments/10bb6ae3-4ce9-510b-a21d-16a428fc4d73/397d0659-image.jpg',
    'lacma_antler': '/mnt/user-data/attachments/10bb6ae3-4ce9-510b-a21d-16a428fc4d73/0b1f948f-image.jpg',
})
fig = make_fig(S)

TC = ext('https://www.thecollector.com/why-japan-abolished-the-samurai/', 'The Collector', 'samurai_src_collector')
KY = ext('https://www.kyuhoshi.com/samurai-districts-in-japan', 'Kyuhoshi', 'samurai_src_kyuhoshi')
CAF = ext('https://www.travelcaffeine.com/?p=5906', 'Travel Caffeine', 'samurai_src_travelcaffeine')
SOMA = ext('https://www.nippon.com/en/guide-to-japan/gu008005/fukushima%E2%80%99s-soma-nomaoi-a-thrilling-festival-of-mounted-samurai.html', 'Nippon.com', 'samurai_src_nippon_soma')
JT = ext('https://japantimes.co.jp/culture/2017/01/07/books/book-reviews/vagabond-epic-manga-based-life-17th-century-samurai', 'The Japan Times', 'samurai_src_japantimes')
SHIN = ext('https://shinsengumijapan.com/en/2021/05/02/rurounikenshin_1/', 'Shinsengumi Japan', 'samurai_src_shinsengumi')
VI_SAM = viator('Japan+samurai+experience')

f_hero = fig('armor-case', 'A suit of dark armor with gold-and-black lacing and a crested helmet stands in a glass case beside a stand of arrows, a long bow and smaller armor pieces',
             'Armor, arrows and a bow in a display case at Matsue Castle.',
             f'Photo: 江戸村のとくぞう, {BYSA4}, September 2015. {VIA}', hero=True)
f_kato = fig('armor-kato', 'A dark suit of armor with a flat black helmet topped by two long, curved bird feathers stands in a lit case between two information panels',
             'Armor and helmet said to have belonged to Kato Yoshiaki, founder of Matsuyama Castle.',
             f'Photo: Zairon, {BY4}, via Wikimedia Commons (resized). The label says "said to have belonged," so the attribution is the museum\'s, not a certainty.', maxw=480)
f_red = fig('armor-red', 'A suit of armor with bright red lacing, a black helmet and a large gold crescent ornament stands against a painted battle screen',
            'A red-laced armor on display at Okayama Castle.',
            f'Photo: Zairon, {BY4}, via Wikimedia Commons (resized)', maxw=460)
f_helm = fig('helmet-horned', 'A dark helmet with a fierce face ornament, two long horns and fan-shaped side pieces sits on a black lacquered box draped with purple cloth',
             'A helmet with a fierce ornament and two horns, Matsue Castle.',
             f'Photo: G41rn8, {BYSA4}, October 2016. {VIA}', maxw=420)
f_sword = fig('sword', 'A long sword in a gold-fitted scabbard wrapped with beaded cord lies on a clear stand, with a large gold ring at the hilt end',
              'An ornate sword on display at Okayama Castle.',
              f'Photo: Zairon, {BY4}, via Wikimedia Commons (resized)', maxw=780)
f_town = fig('shiomi-nawate', 'A quiet road beside a long white-and-dark-wood wall of old houses, with large pine trees at left and two visitors looking up at the right',
             'Shiomi Nawate, the old samurai street along the moat in Matsue.',
             f'Photo: 663highland, {BYSA3}, March 2015. {VIA}', maxw=760)

f_c1 = fig('chiba_stripe', 'A suit of armor with horizontal stripes of lacing stands on a wooden stand', 'Armor with horizontal lacing on a stand, Chiba City Folk Museum.', f'Photo: Gary Todd, {CC0}, 1 October 2016. Chiba City Folk Museum. {VIA}', maxw=420)
f_c2 = fig('chiba_crescent', 'Armor with a large crescent-moon ornament on the helmet stands in a glass case', 'Armor with a crescent-moon helmet ornament, Chiba City Folk Museum.', f'Photo: Gary Todd, {CC0}, 1 October 2016. Chiba City Folk Museum. {VIA}', maxw=420)
f_c3 = fig('chiba_horned', 'A horned helmet with a red face mask above a green chest piece', 'A horned helmet with a red mask, Chiba City Folk Museum.', f'Photo: Gary Todd, {CC0}, 1 October 2016. Chiba City Folk Museum. {VIA}', maxw=420)
f_c4 = fig('chiba_vcrest', 'Black armor with a V-shaped crest on the helmet, with a sign on the wall behind', 'Black armor with a V-shaped crest, Chiba City Folk Museum.', f'Photo: Gary Todd, {CC0}, 1 October 2016. Chiba City Folk Museum. {VIA}', maxw=420)
f_c5 = fig('chiba_flame', 'A helmet with a red ring and flame-shaped ornament', 'A helmet with a red ring and flame-shaped ornament, Chiba City Folk Museum.', f'Photo: Gary Todd, {CC0}, 1 October 2016. Chiba City Folk Museum. {VIA}', maxw=760)
f_c6 = fig('chiba_dragon', 'A close-up of a helmet with a dragon-shaped crest', 'A helmet with a dragon-shaped crest, Chiba City Folk Museum.', f'Photo: Gary Todd, {CC0}, 1 October 2016. Chiba City Folk Museum. {VIA}', maxw=760)
f_c7 = fig('chiba_oyoroi', 'A suit of red-laced armor with a label reading Aka-ito-odoshi O-yoroi', 'A red-laced great armor (ō-yoroi) with its label, Chiba City Folk Museum.', f'Photo: Gary Todd, {CC0}, 1 October 2016. Chiba City Folk Museum. {VIA}', maxw=420)
f_c8 = fig('chiba_domaru', 'Armor with orange and purple lacing, with a label in Japanese', 'A multicolor-laced domaru armor, labeled as a reproduction, Chiba City Folk Museum.', f'Photo: Gary Todd, {CC0}, 1 October 2016. Chiba City Folk Museum. {VIA}', maxw=420)
f_g1 = fig('guimet_helm', 'A helmet with a leaf-shaped crest on a white background', 'A helmet with a leaf-shaped crest (displayed at the Guimet Museum, Paris, per the file name).', f'Photo: Pom², {BYSA3}, 4 September 2008 (edited by ish ishwar). {VIA}', maxw=480)
f_g2 = fig('met_five', 'Five suits of armor lit in orange light', 'Several gusoku-style armors at the Metropolitan Museum of Art, New York.', f'Photo: Lord Biro, {BYSA2}, 28 May 2008. {VIA}', maxw=760)
f_g3 = fig('dallas_three', 'Three suits of armor in a dark room', 'Armors at The Samurai Collection, Dallas.', f'Photo: Michael Barera, {BYSA4}, 15 September 2018. {VIA}', maxw=760)
f_g4 = fig('glenbow_helm', 'A gold dragon helmet against an orange background', 'A gold dragon helmet at the Glenbow Museum, Calgary.', f'Photo: Daderot, {CC0}, 21 September 2013. {VIA}', maxw=760)
f_g5 = fig('glenbow_seated', 'A seated suit of armor with a mustached face mask and a label', 'A seated armor at the Glenbow Museum, Calgary.', f'Photo: Daderot, {CC0}, 21 September 2013. {VIA}', maxw=420)
f_g6 = fig('guimet_purple', 'A suit of armor with purple lacing against a gray gradient', 'A purple-laced armor, Guimet Museum, Paris (MA 8102, 18th century).', f'Photo: Ash_Crow, {BYSA4}, 1 July 2018. {VIA}', maxw=420)
f_g7 = fig('lacma_antler', 'A suit of armor with an antler-shaped helmet crest', 'A gusoku-type armor, 18th century, Los Angeles County Museum of Art.', f'Photo: Team_A (Wikipedia Loves Art; photo by howcheng), <a href="https://creativecommons.org/licenses/by-sa/2.5/" target="_blank" rel="noopener" style="color:var(--enshu);">CC BY-SA 2.5</a>, February 2009. {VIA}', maxw=420)

f_m1 = fig('met_front', 'A seated suit of armor with a gold dragon-faced helmet crest, a gray mustache mask, and white and green lacing, on a wooden stand', 'Armor (haramaki), front view, Metropolitan Museum of Art.', f'Photo: The Metropolitan Museum of Art (Open Access), {CC0}, accession 36.25.43a–o, Bequest of George C. Stone, 1935. {VIA}', maxw=420)
f_m2 = fig('met_back', 'The back of the same armor, with a large orange knot and tassels below the helmet, seen from behind on a wooden stand', 'The same armor from behind.', f'Photo: The Metropolitan Museum of Art (Open Access), {CC0}, accession 36.25.43a–o, Bequest of George C. Stone, 1935. {VIA}', maxw=420)
f_m3 = fig('met_side', 'A three-quarter view of the seated armor with gold horned crest, striped lacing and fur-covered boots', 'The same armor from the side.', f'Photo: The Metropolitan Museum of Art (Open Access), {CC0}, accession 36.25.43a–o, Bequest of George C. Stone, 1935. {VIA}', maxw=420)
f_m4 = fig('met_close', 'A close-up of a helmet with a gold dragon face between two gold horns and a gold fan-shaped crest, above a mustache mask and orange cords', 'A close-up of the helmet crest and face mask.', f'Photo: The Metropolitan Museum of Art (Open Access), {CC0}, accession 36.25.43a–o, Bequest of George C. Stone, 1935. {VIA}', maxw=640)

f_s1 = fig('odachi', 'A very long sword with a wooden hilt lies on a wooden stand in a display case at a shrine', 'The Odachi Masayoshi, a very long sword displayed at Yahiko Shrine, Niigata.', f'Photo: Artanisen, {BYSA4}, 16 October 2019. {VIA}', maxw=760)
f_s2 = fig('iwate_sword', 'A sword with a plain wooden hilt rests on a white-draped stand with the blade fully visible', 'A sword in the Iwate Prefectural Museum, a work of Miyagawa Shuichi (Keio 3, 1867).', f'Photo: 掬茶, {BYSA4}, 3 November 2023. {VIA}', maxw=760)
f_s3 = fig('shosoin_copy', 'A sword in a dark red scabbard with silver openwork fittings set with red, blue and green stones, and two purple straps hanging above', 'A 19th-century copy of a Shosoin sword, with gilded silver fittings and inlay.', f'Photo: Tamura Sokichi (maker, 19th century), via ColBase: Integrated Collections Database of the National Museums, Japan, <a href="https://creativecommons.org/licenses/by/4.0/" target="_blank" rel="noopener" style="color:var(--enshu);">CC BY 4.0</a>. {VIA}', maxw=760)
f_s4 = fig('lacma_swords', 'A long sword and a short sword, each shown with its blade above its black lacquer scabbard decorated with gold leaves and flecks', 'Swords and scabbards, Los Angeles County Museum of Art (AC1999.186.1.1–.16).', f'Photo: Los Angeles County Museum of Art, public domain (LACMA mark), uploaded to Wikimedia Commons by Fæ, 19 July 2013. {VIA}', maxw=760)
f_s5 = fig('met_wakizashi', 'A bare blade on a black background above a mounted sword with a blue hilt wrapping and a gold-brown scabbard with chrysanthemum patterns', 'A wakizashi blade and its mounting, Metropolitan Museum of Art.', f'Photo: The Metropolitan Museum of Art (Open Access), {CC0}, uploaded 16 December 2020. {VIA}', maxw=760)
f_s6 = fig('auckland_scabbard', 'A long, slightly curved wooden sheath covered in small pale rounded dots, photographed on a white background', 'A sword sheath covered in a pale dotted skin, Auckland Museum.', f'Photo: Auckland Museum, <a href="https://creativecommons.org/licenses/by/4.0/" target="_blank" rel="noopener" style="color:var(--enshu);">CC BY 4.0</a>, uploaded to Wikimedia Commons by Fæ, 27 October 2019. {VIA}', maxw=760)
f_t1 = fig('tsuba_brass', 'A brass-colored sword guard with a raised oval ring at the top, cloud patterns and three small feet at the bottom', 'A jar-shaped tsuba of copper alloy, Metropolitan Museum of Art (33.40.26).', f'Photo: The Metropolitan Museum of Art (Open Access), {CC0}, uploaded 26 December 2017. {VIA}', maxw=420)
f_t2 = fig('tsuba_fuji', 'A round dark sword guard showing a snow-capped mountain at the top and a bald figure resting against a large gold-colored disc at the bottom right', 'A round tsuba with a mountain and a figure, Aberdeen Art Gallery & Museums.', f'Photo: Aberdeen Art Gallery & Museums (Aberdeen City Council), {CC0}, as a digital reproduction of a public-domain work. {VIA}', maxw=330)
f_t3 = fig('tsuba_dragon', 'A dark iron sword guard with scalloped edges, a gold dragon among clouds at the upper right, and two gold patterned panels', 'An iron tsuba with a gold dragon, Metropolitan Museum of Art (33.40.44).', f'Photo: The Metropolitan Museum of Art (Open Access), {CC0}, uploaded 31 December 2017. {VIA}', maxw=420)
f_t4 = fig('tsuba_cranes', 'A dark rounded-square sword guard showing two gold cranes flying over water and grasses', 'A tsuba with two flying cranes, Aberdeen Art Gallery & Museums.', f'Photo: Aberdeen Art Gallery & Museums (Aberdeen City Council), {CC0}, as a digital reproduction of a public-domain work. {VIA}', maxw=330)

faqs = [
    ("When did the samurai era end?",
     "Over several steps in the early Meiji period. According to The Collector, the han (domain) system was abolished in 1871, a conscription law of 1873 made military service a duty for all healthy men regardless of class, and an edict of 1876 banned carrying swords in public. I have only this one source for the sequence, so please check a second one if you need exact dates."),
    ("Where can I see real samurai armor and swords?",
     "Many castle keeps display them. On this site, the Matsue, Matsuyama and Okayama castle guides show armor, helmets and a sword from their collections. Labels often say \"said to have belonged to\" a particular lord, which is the museum's attribution."),
    ("Are the armor and swords at the Samurai Museum in Shinjuku real?",
     "A 2018 Travel Caffeine review says the armor, helmets and swords are mostly reproductions modeled on Kamakura and Edo period originals. Collections change, so please check the museum's current information before you go."),
    ("Where can I walk through a former samurai district?",
     "Kyuhoshi lists Kakunodate, Nagamachi in Kanazawa, Chiran, Hagi, Usuki, Kitsuki, and Matsue and Tsuwano. Kakunodate's houses are closed from November to early April, according to that article, so season matters."),
    ("Can visitors watch a samurai event?",
     "The Soma Nomaoi in Minamisoma, Fukushima, is a three-day mounted-warrior festival held at the end of July. Nippon.com's 2018 article says tickets were needed only on the second day (¥1,000 same-day, ¥800 in advance). Please check the organizing committee for current details."),
    ("Are samurai and ninja the same thing?",
     "No. Samurai were the warrior class. Ninja, covered in our ninja guide, were covert operatives associated with the Iga and Koka regions during the Sengoku period, and the two overlapped less than pop culture suggests."),
]
faq_html, faq_ld = faq_blocks(faqs)

main = f'''<main>

  {f_hero}

  <aside class="toc" aria-label="Table of contents">
    <div class="toc-label">TABLE OF CONTENTS ／ 目次</div>
    <div class="toc-title">In This Guide</div>
    <ol>
      <li><a href="#opening">Opening: A Note from the Guide</a></li>
      <li><a href="#who">Who the Samurai Were</a></li>
      <li><a href="#end">How the Samurai Era Ended</a></li>
      <li><a href="#armor">Armor and Swords</a></li>
      <li><a href="#towns">Samurai Towns to Walk Through</a></li>
      <li><a href="#experiences">Experiences and Festivals</a></li>
      <li><a href="#media">Samurai in Manga and Anime</a></li>
      <li><a href="#faq">Frequently Asked Questions</a></li>
      <li><a href="#final">Final Thoughts</a></li>
    </ol>
  </aside>

  <article>

    <section id="opening">
      <p class="opening">Most visitors meet the samurai in a castle keep, in front of a glass case with a helmet and a handwritten label they cannot read.</p>
      <p>As a licensed guide, I find that a short history, a few things to look for in the armor, and a list of places where the samurai world is still easy to walk through make that glass case much more interesting. This guide gives you those three things, and it says where I am relying on a single source. For the covert side of the story, see our {link('/culture/ninja/', 'ninja guide', 'samurai_to_ninja')}.</p>
    </section>

    <h2 id="who">Who the Samurai Were<span class="h2-jp">侍とは</span></h2>
    <p>Samurai (<span class="jp">侍</span>) were Japan's warrior class. {TC} says they ruled Japan for nearly 700 years and shaped its politics, economy and moral thinking, which is why they are never far from any Japanese history.</p>
    <p>The Edo period (1603 to 1868) changed their job. The same article says the Tokugawa shogunate brought about two centuries of internal stability, and that by the mid-1600s samurai had moved from battlefield commanders to administrators. It puts the samurai class at roughly 2 million people, many of them living on fixed rice stipends from their lords and often poor. That is a useful corrective to the image of a sword in every hand: in the Edo period, many samurai were closer to salaried officials.</p>

    <h2 id="end">How the Samurai Era Ended<span class="h2-jp">侍の終わり</span></h2>
    <p>According to {TC}, the ending came in a few legal steps:</p>
    <ul>
      <li><strong>1871:</strong> the han system was abolished, and the daimyo became salaried officials instead of rulers.</li>
      <li><strong>Early 1870s:</strong> samurai stipends were taking close to half of national tax revenue, so the government stopped funding former samurai who lacked modern skills.</li>
      <li><strong>1873:</strong> a conscription law, passed on January 10, required healthy men of every status to serve, ending the warrior class's monopoly on fighting.</li>
      <li><strong>1876:</strong> the Haitorei edict banned carrying swords in public, which the article calls a major blow because the blade was considered sacred to samurai. It says the ban set off several armed uprisings, mainly around Satsuma.</li>
    </ul>
    <p>I have only this one source for the sequence, so if you need exact dates for a school paper or a talk, please check a second one.</p>

    <h2 id="armor">Armor and Swords<span class="h2-jp">甲冑と刀</span></h2>
    <p>A castle is the easiest place to see the gear. The first pieces come from three of our castle guides, followed by museum photos from Chiba and from collections abroad. I describe only what the photos show.</p>

    {f_red}
    <p>This red-laced armor from Okayama Castle is the kind of piece that reads as "samurai" at a glance: a gold crescent rises from a black helmet, and the cords on the chest and skirt are a deep orange-red. Behind it is a painted screen of a battle with banners.</p>

    {f_kato}
    <p>This armor at Matsuyama Castle is described on its label as having belonged to the castle's founder, Kato Yoshiaki. It is much darker and plainer than the red piece. The flat black helmet carries two long, curved feathers, and the case is flanked by panels telling the lord's story in Japanese and English.</p>

    {f_helm}
    <p>Helmets are where makers had the most freedom. This one from Matsue Castle has a fierce face ornament, two horns and fan-shaped side pieces, and it sits on a lacquered box with a purple cloth. I would look for the helmet first in any display, because it often carries the owner's personality.</p>

    {f_sword}
    <p>This sword at Okayama Castle sits in a scabbard fitted with gold, wrapped in beaded cord, with a large ring at the hilt end. I cannot read its label with confidence from the photo, so I will not give its age or owner. In Japanese museums the displayed blade is often in its mounting, so the fittings may be the part that catches your eye.</p>

    <p>For more cases like these, see our {link('/guides/matsue-castle/', 'Matsue Castle', 'samurai_to_matsue')}, {link('/guides/matsuyama-castle/', 'Matsuyama Castle', 'samurai_to_matsuyama')} and {link('/guides/okayama-castle/', 'Okayama Castle', 'samurai_to_okayama')} guides, or the overview in {link('/guides/best-castles-japan/', 'Best Castles in Japan', 'samurai_to_best_castles')}.</p>

    <h3>Armor at the Chiba City Folk Museum</h3>
    <p>These eight photos were taken on 1 October 2016 at the Chiba City Folk Museum, whose Commons description says it is built in the style of Chiba Castle. The labels do not name owners, so I describe the pieces by what you can see.</p>

    {f_c1}
    <p>Horizontal bands of lacing run across the chest and skirt of this armor, which stands on a plain wooden stand.</p>

    {f_c2}
    <p>A large crescent-moon ornament rises from the helmet of this armor, shown in a glass case.</p>

    {f_c3}
    <p>This helmet has horns and a red face mask, set above a green chest piece. It shows how much color armor makers were willing to use.</p>

    {f_c4}
    <p>Black armor with a V-shaped crest on the helmet. A sign behind it appears to read 千葉氏の興亡と妙見信仰, about the Chiba clan and Myoken worship, but that is my reading of the photo.</p>

    {f_c5}
    <p>A helmet with a red ring and a flame-shaped ornament, photographed from the side.</p>

    {f_c6}
    <p>A close-up of a helmet crest shaped like a dragon, where you can see the sculpted details.</p>

    {f_c7}
    <p>The label reads 赤糸威大鎧 (aka-ito-odoshi ō-yoroi), meaning a great armor laced in red cord. Ō-yoroi is the large, boxy style associated with mounted warriors of earlier centuries.</p>

    {f_c8}
    <p>The label reads 色々縅胴丸（復元）, a multicolor-laced dōmaru that is marked as a reproduction. Reproductions are common in regional museums, so the label is worth reading.</p>


    <h3>Samurai Armor in Museums Abroad</h3>
    <p>Many fine suits sit in overseas collections. These are displayed in museums outside Japan, so you do not need a flight to see how varied the armor is.</p>

    {f_g1}
    <p>A helmet with a leaf-shaped crest on a white background. The file name points to the Guimet Museum in Paris.</p>

    {f_g2}
    <p>Five gusoku-style armors lit in warm light at the Metropolitan Museum of Art. Gusoku is the general term for a full set of armor.</p>

    {f_g3}
    <p>Three armors in a dark room. The Commons description for this photographer's Dallas photo names The Samurai Collection, but I matched this file to it by elimination, so please treat the location as likely, not certain.</p>

    {f_g4}
    <p>A gold dragon helmet on an orange background, photographed at the Glenbow Museum in Calgary.</p>

    {f_g5}
    <p>A seated armor with a mustached face mask and a label, probably the same armor as the helmet above.</p>

    {f_g6}
    <p>Purple lacing on a gray gradient. The Commons record gives the Guimet Museum, MA 8102, 18th century.</p>

    {f_g7}
    <p>This armor has an antler-shaped crest. The Commons title calls it a gusoku-type armor of the 18th century at the Los Angeles County Museum of Art.</p>


    <h3>One Armor, Four Views: A Haramaki at the Met</h3>
    <p>The Metropolitan Museum of Art titles this piece "Armor (Haramaki)," dated late 18th to 19th century, made of iron, lacquer, leather, gilt copper, silk and hair. A haramaki is a body armor that wraps around the torso. The four photos below are the museum's open-access images, so the front, back, side and a close-up are all available.</p>

    {f_m1}
    <p>From the front, the armor sits on a wooden stand. White and green lacing runs in bands across the chest and skirt, and fur-covered boots finish the figure.</p>

    {f_m2}
    <p>From behind, an orange cord is tied in a large knot with tassels, a detail you rarely see in a castle case, where armor usually faces the front.</p>

    {f_m3}
    <p>At an angle you can see the gilt horns and fan-shaped crest rising from the helmet, and how deep the skirt layers are.</p>

    {f_m4}
    <p>The helmet carries a gold dragon-like face between two horns, and below it the mask has a gray mustache of hair. I match this close-up to the same armor by its crest and cords, so treat that pairing as likely.</p>


    <h3>Swords in Japan and Abroad</h3>
    <p>Swords are shown in several ways. Some are bare blades on stands, and some are whole sets with their scabbards. I use the Commons descriptions for names and dates and mark what I am reading from the photo myself.</p>

    {f_s1}
    <p>The Commons description calls this the Odachi Masayoshi, one of the longest surviving Japanese swords, on display at Yahiko Shrine in Niigata. It says it was forged by the swordsmith Sanke Masayoshi in 1844, with a blade of about 225 cm. In the photo you can see how far the blade curves across the whole case.</p>

    {f_s2}
    <p>A bare blade on a white-draped stand in the Iwate Prefectural Museum. The Commons description says it is a sword held by the Morioka domain, made by Miyagawa Shuichi in Keio 3 (1867). With the blade shown alone on a stand, you can follow its gentle curve from tip to tang.</p>

    {f_s3}
    <p>This is a copy, not an original: the Commons record calls it a 19th-century copy of the "kara-tachi sword with gilded silver fittings and inlay" among the Shosoin Imperial Treasures. The scabbard is dark red, the silver-colored fittings are openwork set with red, blue and green stones, and two purple-and-white straps hang above it.</p>

    {f_s4}
    <p>The Commons record credits the maker as Yokoyama Sukenaga (active 1830 to 1851) and gives the museum number AC1999.186.1.1–.16. The photo shows a long and a short sword, each with its blade above its scabbard. The dark lacquer scabbards carry gold leaf shapes and flecks, and the hilts are wrapped in brown cord. I read them as a matched pair, but that is my reading.</p>

    {f_s5}
    <p>The Met's record says the wakizashi blade was made by Soshu Fusamune in the late 15th to early 16th century, and the mounting is 18th century. Above is the bare blade on black. Below is the mounted sword, with a blue hilt wrapping and gold chrysanthemum-like round motifs on the scabbard.</p>

    {f_s6}
    <p>The Commons record credits Auckland Museum (object number 1934.316). The object looks like a sword sheath covered in a pale, finely dotted skin, perhaps ray skin, but that is my reading of the photo, not a label.</p>


    <h3>Tsuba: The Sword Guards</h3>
    <p>A tsuba is the guard between the blade and the hilt. In the Edo period, when sword carrying was a mark of rank, tsuba became small canvases for metalwork. These four are in museums abroad, and the Commons records give the dates and materials.</p>

    {f_t1}
    <p>The Met's record lists copper alloy (sentoku), copper and gold. A raised oval ring sits at the top, with cloud scrolls below and three small feet along the bottom edge. The overall shape looks like a jar or gourd.</p>

    {f_t2}
    <p>Aberdeen's record says late Edo period, possibly 19th century, bronze (ABDMS024836). The plate is round. A snow-capped mountain sits at the top, and at the lower right a bald figure rests against a large gold-colored disc. I will not name the subject, because the record gives only a general description.</p>

    {f_t3}
    <p>The Met's record (33.40.44) describes an iron plate with gold. A gold dragon curls through carved clouds on one side, and two gold panels with a textured pattern flank the central hole.</p>

    {f_t4}
    <p>Aberdeen dates this one (ABDMS024059) to the late Edo period, 19th century, bronze. Two gold cranes fly over engraved water and grasses on a dark ground.</p>


    <h2 id="towns">Samurai Towns to Walk Through<span class="h2-jp">武家屋敷</span></h2>
    <p>A castle shows you the lord; the districts around it show you where his retainers lived. {KY} lists these:</p>
    <ul>
      <li><strong>Kakunodate (Akita):</strong> about 80 samurai families once lived here, and several residences can be entered. The article says the houses are closed from November to early April.</li>
      <li><strong>Nagamachi (Kanazawa):</strong> earthen walls, canals and narrow lanes near the castle. The Nomura Residence is open to visitors, and the article lists a 500-yen museum and a free one.</li>
      <li><strong>Chiran (Kagoshima):</strong> seven garden-fronted samurai houses, with about 500 samurai families once living here, a 500-yen ticket for all seven gardens, and daily hours of 9:00 to 17:00 according to the article.</li>
      <li><strong>Hagi (Yamaguchi):</strong> a former castle town where many samurai turned to trade; the castle ruins and Kikuya Residence are the sights named.</li>
      <li><strong>Usuki and Kitsuki (Oita):</strong> a stone-paved lane in Usuki, and in Kitsuki a slope lined with samurai houses and a kimono rental at a former residence.</li>
      <li><strong>Matsue and Tsuwano (Shimane):</strong> Shiomi Nawate, a 500-meter street along the castle moat in Matsue, plus Matsue Buke Yashiki, and the Tonomachi district in Tsuwano.</li>
    </ul>

    {f_town}
    <p>This is Shiomi Nawate, the street along the moat in Matsue. A long wall of old houses runs along the right, pines lean over the road at left, and two visitors stand looking up at a roof. It is a quiet street, which is exactly how I would recommend taking it. Admission figures in the Kyuhoshi article are undated, so please check each site before you go.</p>
    <p>Hagi has its own guide here: {link('/guides/hagi-castle/', 'Hagi Castle', 'samurai_to_hagi')}, and so does {link('/guides/kanazawa-castle/', 'Kanazawa Castle', 'samurai_to_kanazawa')}, which sits beside Nagamachi.</p>

    <h2 id="experiences">Experiences and Festivals<span class="h2-jp">体験とお祭り</span></h2>
    <p>If you would rather do than look, there are three kinds of experience.</p>
    <ul>
      <li><strong>The Samurai Museum, Shinjuku (Tokyo).</strong> A 2018 {CAF} review places it in Kabukicho, with a 45-minute guided tour of about 700 years of history, a sword demonstration and an armor try-on, and an admission of 1,800 yen at the time. It adds that most of the armor and swords are reproductions. That review is old, so check the museum's current prices and programs.</li>
      <li><strong>Soma Nomaoi (Minamisoma, Fukushima).</strong> {SOMA} describes a three-day festival held on the last weekend of July, with about 500 riders in warrior dress, an armed horse race and a sacred-flag contest that is the climax. It says the festival is designated an Important Intangible Folk Cultural Property and that tickets were required only on the second day in 2018.</li>
      <li><strong>Bookable samurai experiences on Viator.</strong> These are listings I found on Viator; I have not tried them, so please check each page for the current program, price, meeting point and reviews.
        <ul>
          <li>Kyoto: {aff(vtour('Kyoto/Small-Group-Samurai-Experience-in-Kyoto/d332-44484P1'), 'Small-Group Samurai Experience with Training Sword', 'samurai_viator_kyoto_small')}</li>
          <li>Kyoto: {aff(vtour('Kyoto/Samurai-School-Samurai-for-a-Day/d332-6911KYOPACK_C_A'), 'Samurai School: Samurai for a Day', 'samurai_viator_kyoto_school')}</li>
          <li>Kyoto: {aff(vtour('Kyoto/Samurai-Sword-Experience-in-Kyoto-Tameshigiri/d332-51440P52'), 'Samurai Sword Experience (Tameshigiri), with museum ticket', 'samurai_viator_kyoto_sword')}</li>
          <li>Tokyo: {aff(vtour('Tokyo/Kyoto-Samurai-Show-and-Samurai-Sword-Experience-in-Kyoto/d334-51440P77'), 'Samurai Sword Experience in Tokyo', 'samurai_viator_tokyo_sword')}</li>
        </ul>
        To compare more, see all {aff(VI_SAM, 'samurai experiences on Viator', 'samurai_viator_experience')}.</li>
    </ul>

    <h2 id="media">Samurai in Manga and Anime<span class="h2-jp">漫画・アニメ</span></h2>
    <p>Two series make good companions for a trip, because each is anchored in a real period.</p>
    <p><strong>Rurouni Kenshin</strong> by Nobuhiro Watsuki began in <em>Weekly Shonen Jump</em> in 1994. {SHIN} says the story is set in 1878, the 11th year of Meiji, which places it in the years just after the 1876 sword ban described above. The protagonist, Himura Kenshin, is a former assassin who served the Choshu domain and now wanders with a reverse-blade sword, and the real Shinsengumi captain Saito Hajime appears under his historical identity. It is a good way to see why the end of the samurai era still moves Japanese readers.</p>
    <p><strong>Vagabond</strong> by Takehiko Inoue, the creator of <em>Slam Dunk</em>, is based on the life of the 17th-century swordsman Miyamoto Musashi and on Eiji Yoshikawa's 1935 novel <em>Musashi</em>. {JT} says it began in 1998 and runs to 37 volumes, with more than 80 million copies sold and translations into at least 12 languages. Musashi's Edo-period world is a long way from the warlords of the earlier centuries.</p>
    <p>For the ninja side, including <em>Naruto</em> and <em>Basilisk</em>, see our {link('/culture/ninja/', 'ninja guide', 'samurai_media_to_ninja')}. For other series with real-world locations, our {link('/anime/', 'anime pilgrimage hub', 'samurai_to_anime')} has more.</p>

    <h2 id="faq">Frequently Asked Questions<span class="h2-jp">よくあるご質問</span></h2>

    <div class="faq-stack">

{faq_html}    </div>

    <h2 id="final">Final Thoughts<span class="h2-jp">むすびに</span></h2>
    <p>Start with the glass case at a castle, then add a district such as Nagamachi or Shiomi Nawate, and if your dates match, the end of July in Fukushima. The labels will mean more once you know the Edo period turned warriors into officials and the Meiji reforms ended the class in a few years.</p>

    <div class="closing-block">
      <span class="torii">⚔️</span>
      <p>A helmet, a quiet street and a story with a long ending.</p>
    </div>

    <section class="related-section">
      <h2>Related Guides</h2>
      <span class="h2-jp">関連ガイド</span>
      <div class="related-grid">
        <a class="related-card" href="/culture/ninja/" onclick="trackEvent('click','internal','related_samurai_to_ninja')">
          <div class="related-card-label">SACRED JAPAN ／ GUIDE</div>
          <div class="related-card-title">🥷 Ninja Guide →</div>
          <div class="related-card-desc">Iga and Koka, museums, a festival and the manga behind the myth.</div>
        </a>
        <a class="related-card" href="/guides/best-castles-japan/" onclick="trackEvent('click','internal','related_samurai_to_castles')">
          <div class="related-card-label">SACRED JAPAN ／ GUIDE</div>
          <div class="related-card-title">🏯 Best Castles in Japan →</div>
          <div class="related-card-desc">Original keeps and where to see them.</div>
        </a>
        <a class="related-card" href="/guides/matsue-castle/" onclick="trackEvent('click','internal','related_samurai_to_matsue')">
          <div class="related-card-label">SACRED JAPAN ／ GUIDE</div>
          <div class="related-card-title">Matsue Castle →</div>
          <div class="related-card-desc">Armor, helmets and the moat-side samurai street.</div>
        </a>
        <a class="related-card" href="/culture/samurai-and-ninja/" onclick="trackEvent('click','internal','related_samurai_to_hub')">
          <div class="related-card-label">SACRED JAPAN ／ FEATURE</div>
          <div class="related-card-title">⚔️ Samurai &amp; Ninja Feature →</div>
          <div class="related-card-desc">Both guides, side by side, with places and events.</div>
        </a>
      </div>
    </section>

    <p style="font-size:14px;color:var(--enshu);line-height:1.7;margin-top:32px;"><strong>Sources:</strong> history and the Meiji reforms from {TC}; samurai districts from {KY}; the Samurai Museum from {CAF}; Soma Nomaoi from {SOMA}; Rurouni Kenshin from {SHIN}; Vagabond from {JT}. Photograph details come from the Wikimedia Commons descriptions and from the museum labels visible in the photos. I have not verified current prices, hours or event dates.</p>

  </article>

</main>'''

TITLE = 'Samurai Guide: History, Armor, Samurai Towns and Experiences in Japan'
DESC = "A licensed guide's English introduction to the samurai: who they were, how the era ended, armor and swords to see in castles, former samurai districts to walk through, and experiences such as the Soma Nomaoi."
KEYWORDS = 'samurai, samurai guide, samurai history, samurai armor, samurai sword, samurai district, Kakunodate, Nagamachi, Soma Nomaoi, samurai museum Tokyo, Rurouni Kenshin, Vagabond, Edo period'
url = finish(S, TITLE, DESC, KEYWORDS, '侍', 'The <em>Samurai</em> Guide', '侍ガイド',
             'History, Armor, Samurai Towns and Experiences', 'Samurai Guide', 'guide_samurai',
             'Japan+samurai+experience', main, faq_ld)
print(url)
