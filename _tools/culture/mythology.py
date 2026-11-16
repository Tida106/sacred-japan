import re, os, json
R='/home/claude/sacred-japan'
S='japanese-mythology'
OUT=f'{R}/culture/{S}'
os.makedirs(OUT,exist_ok=True)

def link(href,txt,lab): return f'<a href="{href}" class="inline-link" onclick="trackEvent(\'click\',\'internal\',\'{lab}\')">{txt}</a>'
def ext(href,txt,lab): return f'<a href="{href}" target="_blank" rel="noopener" onclick="trackEvent(\'click\',\'external\',\'{lab}\')">{txt}</a>'
VI='https://www.viator.com/search/takachiho?pid=P00298374&amp;mcid=42383&amp;medium=link&amp;campaign=sacred-japan'
EX='https://expedia.com/affiliate?siteid=1&amp;landingPage=https%3A%2F%2Fwww.expedia.co.jp%2FHotel-Search%3Fdestination%3DIzumo&amp;camref=1101l5JmFa&amp;creativeref=1011l87782&amp;adref=PZf6lQ77e8'
FUN='https://www.fun-japan.jp/en/articles/12617'
WH='https://www.worldhistory.org/Kojiki'
COL='https://www.thecollector.com/foundational-shinto-myths/'
NWE='https://www.newworldencyclopedia.org/entry/Japanese_folklore_and_mythology'
BISH='https://jamesbishopblog.com/2022/06/05/a-summary-of-the-kojikis-creation-myth-and-the-story-of-izanagi-and-izanami/'
TSU='https://tsunagujapan.com/12-shrines-related-to-japanese-mythology'
JT='https://int.japanesetaste.com/blogs/japanese-taste-blog/10-shinto-gods-to-know-when-visiting-japan-s-shrines'
JAL='https://www.jal.co.jp/ar/en/guide-to-japan/destinations/articles/miyazaki/land-of-mythology/'
JALIW='https://jal.japantravel.com/article/amano-iwato-and-amano-yasukawa/45104'
MLITIW='https://www.mlit.go.jp/tagengo-db/common/001560303.pdf'
JEIW='https://www.japan-experience.com/all-about-japan/kumamoto/temples-shrines/amano-iwato'
JGIW='https://japan-guide.com/e/e8054.html'
TWIW='https://www.tokyoweekender.com/?p=288076'
HAK='https://www.japan-experience.com/all-about-japan/tottori/temples-and-shrines-in-japan/hakuto-shrine'
WIKIHARE='https://en.wikipedia.org/wiki/White_Hare_of_Inaba'
FUNHARE='https://www.fun-japan.jp/en/articles/14088'
MLITKA='https://www.mlit.go.jp/tagengo-db/en/R3-00199.html'
MLITKA2='https://www.mlit.go.jp/tagengo-db/R3-00191.html'
JNTOKA='https://www.japan.travel/en/sg/story/japan-festival-izumo-taisha-kamiari'
WATA='https://watabi.org/en/articles/izumo-kamiarizuki-guide'
IZ='https://izumooyashiro.or.jp/en/archives/religious/religious-events-at-izumo-oyashiro-shrine'
KANN='https://japanese-wiki-corpus.github.io/Shinto/Kannazuki.html'
JJ='https://jinjajourney.azurewebsites.net/?p=2982'
KIJI='https://this.kiji.is/966506244640751616'
YUU='https://yuugenguide.squarespace.com/shrines/tag/Awaji+Island'
JACT='https://japanactivity.com/attractions/takachiho/amano-iwato-shrine'

faqs=[
("What is the difference between the Kojiki and the Nihon Shoki?","Both are early eighth-century records, and they tell many of the same myths. The Collector says they were commissioned in 712 and 720. World History Encyclopedia calls the Kojiki the oldest book of Japanese history, and says the Nihon Shoki, written by a committee of court scholars in 720, repeats many of its myths but often from a different viewpoint and with changes in detail. Fun! JAPAN adds that the Nihon Shoki is the oldest official history of the nation and runs up to the year 697."),
("Where do Japan's islands come from in the myth?","From a spear. In the Kojiki as quoted by World History Encyclopedia, brine dripped from the spear of Izanagi and Izanami and piled up to become the island of Onogoro. The couple then produced the other islands, which Fun! JAPAN counts as eight children. Which real island Onogoro was is not settled; Awaji Island in Hyogo is the traditional candidate, and its shrines are described below."),
("Is the Emperor descended from Amaterasu?","In the myths, yes: Fun! JAPAN calls the sun goddess the ancestor of the Imperial Family, and Japanese Taste traces the line through her descendant Ninigi, who came down to Takachiho. New World Encyclopedia notes that the myths gave the Imperial family divine origins. I present this as what the myths say, not as history; the Ise shrine is where the Imperial link is still honored in ritual."),
("Which shrine should I visit for Amaterasu?","Ise. Japanese Taste says her divine status is honored at the Ise Grand Shrine, which it calls the most important Imperial Shinto shrine in Japan. For the cave story itself, go to Amano Iwato Shrine in Takachiho."),
("Why is Izumo's tenth month the month with gods?","In the lunar tenth month, most of Japan calls the month <em>kannazuki</em>, the month without gods, because the gods are believed to have left for Izumo. In Izumo it is <em>kamiarizuki</em>, the month with gods. The Ministry of Land (MLIT) multilingual database says the myriad deities gather there to decide the relationships people will form in the coming year."),
("Can I actually visit Amaterasu's cave?","Not the cave itself. JAL's travel guide says you cannot go to Amano Iwato, the cave where she hid, which is across the gorge behind the shrine's west sanctuary. What you can visit is Amano Yasukawara, the riverside cave where the gods met to plan, about a ten-minute walk from the shrine according to japan-guide."),
("If I only have two days, where do I start?","My suggestion is Takachiho, because several stories sit close together: Amano Iwato and Amano Yasukawara for the cave myth, Takachiho Shrine for Ninigi's descent and the evening kagura, and the gorge nearby. Our Takachiho guide has the logistics. Izumo is the second choice if you want Okuninushi and the gods' meeting."),
]
faq_html=''.join(f"""      <details class="faq-item">
        <summary>{q}</summary>
        <div class="faq-answer">{a}</div>
      </details>

""" for q,a in faqs)
faq_ld=json.dumps({"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":re.sub('<[^>]+>','',a)}} for q,a in faqs]},ensure_ascii=False,indent=2)

TITLE="Japanese Mythology Guide: Kojiki Gods, Famous Myths and the Shrines Where They Happen"
DESC="A licensed guide's English introduction to Japanese mythology: the Kojiki and Nihon Shoki, Izanagi and Izanami, Amaterasu's cave, Okuninushi and the white hare, and the real shrines in Takachiho, Izumo and Awaji where each story is set."
URL=f"https://sacred-japan.net/culture/{S}/"
OG="https://sacred-japan.net/images/og/og-culture-japanese-mythology.jpg"

CAPST='font-size:13px;color:var(--enshu);margin-top:10px;text-align:center;line-height:1.6;'
LA='style="color:var(--enshu);"'
def lk(t,u): return f'<a href="{u}" target="_blank" rel="noopener" {LA}>{t}</a>'
def csearch(q): return 'https://commons.wikimedia.org/w/index.php?search='+q+'&title=Special:MediaSearch&type=image'
def cm(q): return lk("Wikimedia Commons",csearch(q))
PDL=lk("public domain","https://commons.wikimedia.org/wiki/Commons:Public_domain")
CC0L=lk("CC0","https://creativecommons.org/publicdomain/zero/1.0/")
CCBYSA4=lk("CC BY-SA 4.0","https://creativecommons.org/licenses/by-sa/4.0/")
KOK='https://d-museum.kokugakuin.ac.jp/eos/detail/?id=9351'
def mfig(src,alt,desc,cred,mw=760,hero=False):
    ld='eager' if hero else 'lazy'
    mg='0 auto 48px' if hero else '36px auto'
    return (f'<figure style="margin:{mg};max-width:{mw}px;">\n      <picture><source srcset="/culture/japanese-mythology/images/{src}.webp" type="image/webp"><img src="/culture/japanese-mythology/images/{src}.jpg" alt="{alt}" loading="{ld}" style="width:100%;height:auto;border-radius:4px;display:block;"></picture>\n      <figcaption style="{CAPST}">{desc}<br>{cred}</figcaption>\n    </figure>')

f_hero=mfig('cave-dance-triptych','Three-panel colour woodblock print on a red ground: at the centre a woman in orange and white dances on an upturned tub with orange rays fanning out behind her, while gods in armour, robes and long hair crowd both side panels, laughing and cheering',
 'The cave story as a Meiji-era triptych, <em>Origin of the Cave Door Dance</em> (1889). Ame no Uzume dances in the middle, and the gods around her are in an uproar; the sun goddess, hiding behind the stone door, is about to look out. The full story is in the cave section below.',
 f'Shunsai Toshimasa, 1889, MAK (Museum of Applied Arts), Vienna. {PDL}, via {cm("Shunsai Toshimasa Origin of the cave door dance")} (resized)',mw=900,hero=True)
f_suke=mfig('sukenobu-izanagi-izanami','Hanging scroll painting of two figures in white robes standing on a swirl of golden cloud above a pale sea, with a tiny dark island below them, framed by a patterned textile mount',
 'Izanagi and Izanami on the clouds, painted in the early 1700s. The island below is the small first land of the myth. Note how calm it is: the Edo painter shows two courtly figures, not a creation battle.',
 f'Nishikawa Sukenobu, <em>The God Izanagi and Goddess Izanami</em>, c. 1700&ndash;1750, The Metropolitan Museum of Art (2015.300.115). {PDL}, via {cm("Nishikawa Sukenobu Izanagi Izanami Metropolitan Museum")} (resized)')
f_kyo=mfig('kyosai-island-birth','Painting of a bearded god in white robes and orange armour plates striding over churning waves and rocks with a long spear, while a woman in a pink robe clings behind him; stormy dark clouds fill the background',
 'Izanagi and Izanami stirring the sea with the jewelled spear, after Kawanabe Kyosai (about 1870). The Commons description says the spear is Ame no Nuboko and that the image reached us through a 1925 magazine reproduction, so treat the colours as the printer&rsquo;s, not necessarily the painter&rsquo;s.',
 f'After Kawanabe Kyosai, c. 1870, reproduced in <em>The Connoisseur</em>, 1925. {PDL}, via {cm("Izanagi and Izanami giving birth to Japan Kawanabe Kyosai")} (resized)',mw=420)
f_susa=mfig('chikanobu-susanoo-kushinada','Colour woodblock print: a bearded god in a pale robe with a sword at his hip kneels beside a woman in a bright pink kimono and an older figure in green, while a small inset at the top shows a green dragon thrashing in a stormy sea',
 'Susanoo rescues Princess Kushinada from the dragon, 1886. The dragon is the Yamata no Orochi; here it appears in the small panel at the top. The Commons description gives this as one print in a series on the Contest of Day and Night.',
 f'Toyohara Chikanobu, 1886, San Diego Museum of Art (1966.202.11). {PDL}, via {cm("Susanoo rescues Kushinada Hime from the dragon Chikanobu")} (resized)',mw=420)
f_state=mfig('chikanobu-1878-state-shinto','Wide three-panel colour woodblock print on a red ground showing many figures in Western chairs, court robes and armour grouped across the panels, with golden sunrays at the upper right',
 'A Meiji print that puts the myths and the monarchy in one picture. According to the Commons description, the central panel shows Emperor Meiji and Empress Shoken in Western-style chairs, with the kami Izanami, Kunitokotachi and Izanagi behind them, and the side panels group other emperors with Amaterasu and Ninigi. This is the &ldquo;divine origins&rdquo; idea in visual form.',
 f'Toyohara Chikanobu, 1878 (higher-quality version, uploaded 2020). {PDL}, via {cm("Chikanobu 1878 State Shinto Meiji emperor Izanagi Izanami Amaterasu")} (resized)',mw=900)
IZ='Izanagi Jingu Awaji'
f_otorii19=mfig('izanagi-otorii-2019','Pale stone torii with two crossbars standing in a gravel forecourt beside a tall stone pillar carved with the shrine name, with a small stone lantern, a roofed water pavilion and green trees behind',
 'The big torii and shrine-name pillar at Izanagi Jingu in April 2019. The long banner on the right pillar reads, as far as I can tell, &ldquo;celebrating the 30th year of His Majesty&rsquo;s reign&rdquo;, which fits that year.',
 f'Saigen Jiro, 27 April 2019, {CC0L}, via {cm(IZ+" otorii Saigen Jiro")} (resized)')
f_torii09=mfig('izanagi-torii-2009','Wide view of a pale stone torii with a vertical banner on its right pillar, stone lanterns and komainu guardian lions on either side, and a long gravel approach leading to a second torii in the distance',
 'The same approach in April 2009, looking down the path toward a second torii. The banner on the pillar appears to read &ldquo;20th year of His Majesty&rsquo;s accession&rdquo;, the 2009 counterpart of the 2019 banner above, so the two photos are almost exactly ten years apart. The shrine has not moved, but street fittings and signs may have changed.',
 f'弥 (Wikimedia Commons user), 12 April 2009, {PDL}, via {cm(IZ+" torii 2009")} (resized)')
f_shinmon19=mfig('izanagi-shinmon-2019','Front gate of a shrine with a deep brown tiled roof, a thick rope across the opening, white paper streamers hanging from it, white and blue banners and a bright sky above',
 'The front gate (<em>omote shinmon</em>), the gate between the forecourt and the inner shrine. The shimenawa rope and white streamers mark the passage from the everyday world into sacred ground, which is the same border the Yomi story is about, only dressed for living people.',
 f'Saigen Jiro, 27 April 2019, {CC0L}, via {cm(IZ+" omote shinmon Saigen Jiro")} (resized)')
f_gate26=mfig('izanagi-gate-2026','Looking through the shaded wooden front gate of a shrine: a thick shimenawa rope with white streamers hangs above, round lanterns with chrysanthemum crests hang on both sides, and visitors walk toward a distant hall',
 'The same gate seen from the inside edge, in April 2026. The round lanterns carry a chrysanthemum crest, as far as I can see, and through the opening you can see people walking up the white-paved path toward the worship hall.',
 f'明芳 松岡, 5 April 2026, {CCBYSA4}, via {cm(IZ+" front gate 2026")} (resized)')
f_haiden19=mfig('izanagi-haiden-2019','Wide, symmetrical view of a worship hall with a long green-grey roof and dark wooden walls, approached by a straight white stone path across an open gravel yard, with trees on both sides and a blue sky',
 'The worship hall (<em>haiden</em>) in April 2019. This is where you stand to bow and pray; the long straight path is a good place to slow down before reaching the hall.',
 f'Saigen Jiro, 27 April 2019, {CC0L}, via {cm(IZ+" haiden Saigen Jiro")} (resized)')
f_haiden09=mfig('izanagi-haiden-2009','A worship hall with a wide green-grey roof seen from the side across a gravel yard, with a large drum on the ground at the left, stone and bronze lanterns on both sides and tall trees behind',
 'The haiden from a different angle in April 2009, with a large drum on the ground at the left and a few people near the steps. The photo is old, so details may differ from what you will find today.',
 f'弥 (Wikimedia Commons user), 12 April 2009, {PDL}, via {cm(IZ+" haiden 2009")} (resized)')
f_honden19=mfig('izanagi-honden-2019','Small wooden shrine building with a layered tiled roof, a thick rope with white streamers across its front, a short flight of stone steps and a low white fence, surrounded by trees',
 'The main sanctuary (<em>honden</em>), as the Commons description labels it. Jinja Journey says Izanagi built a hidden palace on Awaji, and the shrine presents itself as his place of rest; I could not confirm what visitors can enter, so treat this as a look from the outside.',
 f'Saigen Jiro, 27 April 2019, {CC0L}, via {cm(IZ+" honden Saigen Jiro")} (resized)')
f_amulet=mfig('izanagi-amulet-office-2026','The wooden counter of a shrine office with several visitors queuing, a dark wooden sign above reading the shrine name, and a long white board of amulet names and prices fixed under the eaves',
 'The amulet and charm office in April 2026. On the price board I can make out a &ldquo;peach-fruit amulet&rdquo; (<em>momo no mi omamori</em>) and other items with the character 桃 (peach). That would suit the myth: Kokugakuin&rsquo;s Encyclopedia of Shinto says Izanagi threw three peaches at his pursuers from Yomi, and gave the peach a divine name. Please check items and prices at the office, since the board is only a snapshot.',
 f'明芳 松岡, 5 April 2026, {CCBYSA4}, via {cm(IZ+" amulet office 2026")} (resized)')

main=f"""<main>

  {f_hero}

  <!-- TABLE OF CONTENTS -->
  <aside class="toc" aria-label="Table of contents">
    <div class="toc-label">TABLE OF CONTENTS ／ 目次</div>
    <div class="toc-title">In This Guide</div>
    <ol>
      <li><a href="#opening">Opening: A Note from the Guide</a></li>
      <li><a href="#books">Two Books, 712 and 720</a></li>
      <li><a href="#creation">A Spear, a Drop and the First Island</a></li>
      <li><a href="#yomi">Yomi and the Three Children</a></li>
      <li><a href="#sun">The Sun Goddess, the Storm God and the Cave</a></li>
      <li><a href="#okuninushi">Okuninushi, the White Hare and the Land Transfer</a></li>
      <li><a href="#descent">The Descent to Takachiho</a></li>
      <li><a href="#kamiarizuki">Kamiarizuki: The Month the Gods Meet</a></li>
      <li><a href="#map">A Shrine Map of the Myths</a></li>
      <li><a href="#trip">Planning a Myth Trip</a></li>
      <li><a href="#faq">Frequently Asked Questions</a></li>
      <li><a href="#final">Final Thoughts</a></li>
    </ol>
  </aside>

  <article>

    <section id="opening">
      <p class="opening">A man turns around in the dark of the underworld, lifts a torch, and sees what he promised not to look at. Everything that follows in Japanese mythology, the sun, the moon, the storm, the imperial line, grows out of that one broken promise. These stories are not dusty. You can stand on the beach where the gods are said to arrive this very month, and you can walk down a river to the cave where they once held a meeting.</p>
      <p>As a licensed guide, I find that most visitors meet these gods first as names on shrine signs, and the stories are the key that makes those signs readable. This guide gives you the main plot in the order the old books tell it, flags where the sources disagree, and ends with a map of the real places where each story is set. Our guides to the {link('/culture/three-sacred-treasures/','Three Sacred Treasures','myth_to_treasures')} and the {link('/guides/izumo-taisha/','Izumo Taisha','myth_to_izumo')} go deeper on two of the threads below.</p>
    </section>

    <h2 id="books">Two Books, 712 and 720<span class="h2-jp">古事記と日本書紀</span></h2>
    <p>Almost everything below comes from two works. {ext(COL,'The Collector','myth_collector_books')} says most of what we know about Shinto belief traces back to two documents commissioned in 712 and 720: the Kojiki (Record of Ancient Matters) and the Nihon Shoki (Chronicle of Japan). {ext(WH,'World History Encyclopedia','myth_worldhistory_kojiki')} calls the Kojiki the oldest book of Japanese history and the oldest text of any kind from Japan, written in Chinese characters with some Japanese adaptations, and with poems and songs inserted into the prose.</p>
    <p>The Nihon Shoki came later, written by a committee of court scholars in 720. The same source says it repeats many of the Kojiki's myths but often from a different viewpoint and with changed details. {ext(FUN,'Fun! JAPAN','myth_funjapan_books')} adds that it is the oldest official history of the nation, running from mythical beginnings to the year 697. That is why you will see two versions of some stories, and why I note below where they split.</p>
    <p>One more point of context: {ext(NWE,'New World Encyclopedia','myth_nwe_origin')} notes that the myths gave Japan a creation story and attributed divine origins to the Imperial family. Keep that in mind when you read them; they are religion, literature and a family tree at the same time.</p>
    {f_state}

    <h2 id="creation">A Spear, a Drop and the First Island<span class="h2-jp">国生み</span></h2>
    <p>Before Japan there was, in {ext(COL,'The Collector','myth_collector_chaos')}'s words, undifferentiated chaos, from which a line of gods appeared. The last pair were Izanagi and Izanami, whose names Fun! JAPAN translates as "he who invites" and "she who invites". The other gods handed them a spear and told them to consolidate the world, according to a Kojiki summary on {ext(BISH,"James Bishop's blog",'myth_bishop_spear')}. They stood on the Floating Bridge of Heaven and stirred.</p>
    {f_suke}
    <p>The result, in the Kojiki passage quoted by World History Encyclopedia, is that the spear's drips piled up and became the island of Onogoro. The couple then produced the islands of the archipelago; Fun! JAPAN counts eight children. Izanagi greeted Izanami first, in the Collector's retelling, and that is why the next children were the other islands, a detail that says a lot about what the compilers thought of correct manners.</p>
    {f_kyo}
    <p>Where was Onogoro? The myth does not say, but tradition points to Awaji Island in Hyogo, and several shrines there claim the story, as the map below shows.</p>

    <h2 id="yomi">Yomi and the Three Children<span class="h2-jp">黄泉の国と三貴子</span></h2>
    <p>Giving birth to the fire god killed Izanami. Fun! JAPAN says the grieving Izanagi killed his own child in revenge and then went to find her in Yomi, the underworld. The Collector says she asked him to wait and under no circumstances to look at her. Like Orpheus, he looked. Bishop's summary of the Kojiki says she had already eaten food from the furnace of Yomi, and that after her army was driven back she pursued him herself, until Izanagi blocked the Even Pass of Yomi with a boulder the book calls the Thousand-Draught Rock.</p>
    <p>Defiled by death, he washed. The Collector says the gods who came from the washing include the three most important in the pantheon: the sun goddess Amaterasu from his left eye, the moon god Tsukuyomi from his right, and the storm god Susanoo from his nose. Fun! JAPAN tells it with a tear from the left eye; the sources vary, and the washing is the version I will use. The Collector adds that Amaterasu was given the heavens, Tsukuyomi the night and Susanoo the seas.</p>
    <p>If you ever wondered why Shinto cares so much about purification, this is the origin story. The rite you perform at a water basin is a small copy of a god cleaning himself after the underworld. Our {link('/culture/shrine-etiquette/','shrine etiquette guide','myth_to_etiquette')} shows how to do it.</p>

    <h2 id="sun">The Sun Goddess, the Storm God and the Cave<span class="h2-jp">天岩戸とヤマタノオロチ</span></h2>
    <p>The Collector says the two siblings Amaterasu and Susanoo had a rivalry, and that the Kojiki and Nihon Shoki differ in their versions, but the gist is a dispute over which gods spawned from her sword and his necklace would serve whom. The sun goddess withdrew into a cave and the world went dark.</p>
    <p>The ministry's multilingual guide (MLIT) tells the rescue clearly. The gods gathered, made a mirror from heavenly metal, and one of them, Ame no Uzume, began a dance that so pleased the assembly that they filled the air with laughter. Amaterasu, puzzled, opened the stone door a crack to ask why. Japan Experience adds that the strongman Tajikarao then pulled the rock aside. The dance is said to be the first kagura, the sacred dance still performed at shrines, which is why the story is told every night in Takachiho (more below).</p>
    <p>Susanoo, banished, goes down to Izumo and kills the eight-headed serpent. In the Kojiki as quoted by World History Encyclopedia, his sword broke on the middle tail, and when he cut into the flesh he found "a sharp great sword". That sword becomes part of the regalia; the full story is in our {link('/culture/three-sacred-treasures/','Three Sacred Treasures guide','myth_sun_to_treasures')}, and Tsunagu Japan says it is kept at {link('/guides/atsuta-shrine/','Atsuta Shrine','myth_to_atsuta')}.</p>
    {f_susa}

    <h2 id="okuninushi">Okuninushi, the White Hare and the Land Transfer<span class="h2-jp">大国主と因幡の白兎</span></h2>
    <p>The next hero is a kind one. In the Kojiki, Okuninushi (called Onamuji then) trails behind his eighty brothers on the way to court Princess Yagami of Inaba, as Wikipedia puts it. Fun! JAPAN calls him a kind-hearted descendant of Susanoo; the sources differ on how many generations. On the beach they find a flayed hare.</p>
    <p>Wikipedia says the hare had tricked sharks (in the San'in region, <em>wani</em> means the common shark) into lining up as a bridge from the island of Oki to Cape Keta, and the last shark tore off its fur. The brothers' advice makes it worse, and Onamuji's kindness cures it. Cape Keta is now identified with the Hakuto Coast in Tottori. Fun! JAPAN reads the tale as a sign of Okuninushi's medical skill, and says Hakuto Shrine is believed to help with skin diseases and burns. Japan Experience describes it as a favorite for matchmaking, noting the claim that this is the first love story in Japan's ancient myths. The hare prophesies that Yagami will choose him, and she does.</p>
    <p>The jealous brothers then try to kill him more than once; in the Fun! JAPAN version one trap is a split tree, and he is sent to Susanoo for trials. The story ends in what the MLIT database calls <em>kuni-yuzuri</em>, "relinquishing the land": Okuninushi hands the country to Amaterasu's line. Tsunagu Japan says Izumo Taisha was built as a condition of that handover. It is the founding bargain of Japanese mythology: the visible world goes to the sun goddess's family, and the hidden world, in later tradition, stays with Okuninushi.</p>
    <p>That hidden world is the matchmaking job. The next section shows what happens in Izumo when the gods report to him.</p>

    <h2 id="descent">The Descent to Takachiho<span class="h2-jp">天孫降臨</span></h2>
    <p>Amaterasu sends her grandson Ninigi down to rule (Tsunagu Japan says grandchild). Japanese Taste says he descended on Mount Takachiho in Kyushu with the three sacred objects, a mirror, a jewel and a sword, and that Kirishima Shrine and Kushifuru Shrine nearby celebrate the event. Tsunagu Japan adds that Takachiho Shrine is said to be the spot. Our {link('/guides/takachiho/','Takachiho guide','myth_to_takachiho')} covers the gorge and the evening kagura.</p>
    <p>Two romances follow, both with real shrines. Tsunagu Japan says Princess Konohanasakuya, daughter of the mountain god, married Ninigi, and that Fujisan Hongu Sengen Taisha in Shizuoka enshrines her. It also says Udo Shrine in Miyazaki is where Princess Toyotama gave birth in a sea cave, a story it ties to the Hoori and Hoderi tale and to the folktale of Urashima Taro. I have not checked those links myself, so treat them as the source's reading.</p>

    <h2 id="kamiarizuki">Kamiarizuki: The Month the Gods Meet<span class="h2-jp">神在月</span></h2>
    <p>Here the myths become a live event. In the lunar tenth month, most of Japan calls the month <em>kannazuki</em>, the month without gods, and Izumo calls it <em>kamiarizuki</em>, the month with gods. The MLIT database says the myriad deities gather in Izumo to determine the relationships people will form in the coming year. {ext(JNTOKA,'JNTO','myth_jnto_kamiari')} says the welcome rite, <em>kami-mukae-sai</em>, is held after sunset at Inasa Beach on the 10th day of the 10th lunar month, and the Kamiari Festival runs from the 11th to the 17th. The MLIT database adds that the gods are guided ashore by a dragon-serpent called Seguroumihebi.</p>
    <div class="key-callout" style="background:#fff8e6;border-left:4px solid var(--kin);padding:16px 20px;margin:28px 0;border-radius:2px;">
      <p style="margin:0;"><strong>2026 dates:</strong> {ext(WATA,'Watabi','myth_watabi_2026')} reports, from Izumo Taisha's official calendar, that the gods are welcomed at Inasa Beach on the night of November 18, 2026, and that Sata Shrine holds its own rite from November 20 to 25. By my arithmetic, since the lunar tenth month begins November 9, the Kamiari Festival days of the 11th to 17th fall on November 19 to 25. The date moves every year with the lunar calendar, so please confirm on the {ext(IZ,'Izumo Taisha website','myth_izumo_official')} before you travel.</p>
    </div>
    <p>I would not treat this as a spectacle. Watabi's own guide describes the month in Izumo as one where a district deliberately goes quiet, and some of the rites are held out of public view. Go to listen, not to photograph.</p>

    <h2 id="map">A Shrine Map of the Myths<span class="h2-jp">神話ゆかりの神社</span></h2>
    <p>Tsunagu Japan lists twelve shrines tied to the myths. Here is that list reorganized by story, with extra detail from other sources where I found it. Where a shrine's link to a story is the shrine's own claim, I say so.</p>
    <h3>Creation (Awaji Island, Hyogo)</h3>
    <ul>
      <li><strong>Onokoro Shrine:</strong> honors Izanagi and Izanami and the first island they made, per Tsunagu Japan. Yuugen Guide describes Onokorojima Jinja as in Minamiawaji, in the middle of the island.</li>
      <li><strong>Izanagi Jingu:</strong> in Taga on Awaji Island. Jinja Journey says Izanagi chose this first island for his last years and built a hidden palace here. KIJI describes it as the only grand shrine (<em>jingu</em>) in Hyogo. Yuugen Guide could find no firm record of when it was built.</li>
    </ul>
    <h3>A Closer Look at Izanagi Jingu</h3>
    <p>Because the shrine on Awaji is the one place on this map that claims to be Izanagi's own, I want to walk you through it in the order you would meet it. The Commons descriptions of the photos below name each building; the comments on them are mine. Jinja Journey says Izanagi chose Awaji for his last years and built a hidden palace here, and that is the story the shrine tells about itself.</p>
    {f_otorii19}
    {f_torii09}
    <p>Start at the big torii. The next two photos show the front gate, with its rope and white streamers.</p>
    {f_shinmon19}
    {f_gate26}
    <p>Past the gate, a straight path leads to the worship hall. This is the place to bow, and behind it stands the main sanctuary.</p>
    {f_haiden19}
    {f_haiden09}
    {f_honden19}
    <p>Last, the office where amulets are given out. The board in this photo lists charms for matchmaking, safe birth, exams and travel, among others.</p>
    {f_amulet}
    <h3>The underworld and the washing</h3>
    <ul>
      <li><strong>Iya Shrine (Shimane):</strong> said to mark Yomi Tsuhirasaka, the boundary between the living and the dead (Tsunagu Japan).</li>
      <li><strong>Eda Shrine (Miyazaki):</strong> said to be where Izanagi purified himself after returning, according to Tsunagu Japan; JAL lists it as the place where Izanagi and Izanami are enshrined.</li>
    </ul>
    <h3>The three children</h3>
    <ul>
      <li><strong>Ise Grand Shrine (Mie):</strong> Amaterasu. See our {link('/guides/ise-grand-shrine/','Ise guide','myth_map_ise')}.</li>
      <li><strong>Tsukiyomi Shrine (Kyoto):</strong> the moon god, also a place to pray for safe childbirth (Tsunagu Japan).</li>
      <li><strong>Yaegaki Shrine (Shimane):</strong> Susanoo, with a mirror pond used for marriage fortune-telling (Tsunagu Japan).</li>
    </ul>
    <h3>The cave and the serpent</h3>
    <ul>
      <li><strong>Amano Iwato Shrine (Takachiho, Miyazaki):</strong> the cave where Amaterasu hid. See the trip section below.</li>
      <li><strong>Atsuta Shrine (Aichi):</strong> the sword found in the serpent, per Tsunagu Japan. Our {link('/guides/atsuta-shrine/','Atsuta guide','myth_map_atsuta')} has the visit.</li>
    </ul>
    <h3>Okuninushi and the descent</h3>
    <ul>
      <li><strong>Hakuto Shrine (Tottori):</strong> the white hare. Japan Experience says it is 40 minutes by bus from Tottori Station, and that small rabbit statues stand around it and nearby.</li>
      <li><strong>Izumo Taisha (Shimane):</strong> Okuninushi and the annual gods' meeting. See our {link('/guides/izumo-taisha/','Izumo Taisha guide','myth_map_izumo')}.</li>
      <li><strong>Takachiho Shrine (Miyazaki), Fujisan Hongu Sengen Taisha (Shizuoka), Udo Shrine (Miyazaki):</strong> Ninigi, Konohanasakuya and Toyotama, as above.</li>
    </ul>

    <h2 id="trip">Planning a Myth Trip<span class="h2-jp">旅のモデルコース</span></h2>
    <p>My suggestion for a first trip is Takachiho, because the cave myth is spread over a few kilometers. Japan-guide says Amano Iwato Shrine is about ten kilometers outside central Takachiho, with a bus from Takachiho Bus Center (15 minutes, 200 yen one way, one bus every one to two hours) and a taxi at about 2,700 yen one way. Amano Yasukawara, the cave where the gods met, is a ten-minute walk along the river, and japan-guide says the stone piles become thousands as you approach it. Japan Experience says admission is free and that if you knock a pile over, tradition says you build two to make up for it.</p>
    <p>JAL's guide says you cannot actually go to the cave where Amaterasu hid; the shrine's west sanctuary gives a view toward it. On timing, one source (Japan Activity) says Takachiho Shrine in town stages a 50-minute evening kagura at 20:00 with four dances, and Tokyo Weekender mentions a 33-dance night kagura; schedules and seasons differ, so check the current program.</p>
    <p>The second trip I would suggest is Shimane: Izumo Taisha, then Iya and Yaegaki, which Tsunagu Japan lists as nearby shrines in the same prefecture. Tottori's Hakuto Shrine can be added from Tottori City. Awaji, for the creation story, is a day trip I would leave for a Kansai stay.</p>
    <div class="key-callout" style="background:#fff8e6;border-left:4px solid var(--kin);padding:16px 20px;margin:28px 0;border-radius:2px;">
      <p style="margin:0;">&#9961;&#65039; <strong>Plan your trip:</strong> Browse Takachiho tours, or find a stay in Izumo. <a href="{VI}" target="_blank" rel="noopener sponsored" onclick="trackEvent('click','affiliate','viator_mythology_local')">Browse Takachiho tours on Viator</a> &middot; <a href="{EX}" target="_blank" rel="noopener sponsored" onclick="trackEvent('click','affiliate','expedia_mythology_local')">Find hotels in Izumo</a></p>
    </div>

    <h2 id="faq">Frequently Asked Questions<span class="h2-jp">よくあるご質問</span></h2>

    <div class="faq-stack">

{faq_html}    </div>

    <h2 id="final">Final Thoughts<span class="h2-jp">むすびに</span></h2>
    <p>If you remember one thing, remember the broken promise at the gate of Yomi. Light, water, purification and the three great gods all come out of it, and once you know it, the water basin, the shimenawa and the festival calendar start to read as one story. Start with the cave in Takachiho, then follow the plot to Izumo.</p>

    <section>
      <h2>Related Guides</h2>
      <span class="h2-jp">関連ガイド</span>
      <div class="related-grid">
        <a class="related-card" href="/culture/three-sacred-treasures/" onclick="trackEvent('click','internal','related_myth_to_treasures')">
          <div class="related-card-label">SACRED JAPAN ／ GUIDE</div>
          <div class="related-card-title">&#128222; Three Sacred Treasures →</div>
          <div class="related-card-desc">The mirror, jewel and sword, and the lost sword at Dannoura.</div>
        </a>
        <a class="related-card" href="/guides/izumo-taisha/" onclick="trackEvent('click','internal','related_myth_to_izumo')">
          <div class="related-card-label">SACRED JAPAN ／ GUIDE</div>
          <div class="related-card-title">&#9961;&#65039; Izumo Taisha →</div>
          <div class="related-card-desc">Okuninushi's shrine and the gods' annual meeting.</div>
        </a>
        <a class="related-card" href="/guides/takachiho/" onclick="trackEvent('click','internal','related_myth_to_takachiho')">
          <div class="related-card-label">SACRED JAPAN ／ GUIDE</div>
          <div class="related-card-title">&#127956;&#65039; Takachiho →</div>
          <div class="related-card-desc">The gorge, the cave shrines and the night kagura.</div>
        </a>
        <a class="related-card" href="/culture/what-is-shinto/" onclick="trackEvent('click','internal','related_myth_to_shinto')">
          <div class="related-card-label">SACRED JAPAN ／ GUIDE</div>
          <div class="related-card-title">&#9961;&#65039; What Is Shinto? →</div>
          <div class="related-card-desc">The faith these stories belong to.</div>
        </a>
      </div>
    </section>

    <p style="font-size:14px;color:var(--enshu);line-height:1.7;margin-top:32px;"><strong>Sources:</strong> {ext(WH,'World History Encyclopedia: Kojiki','myth_src_wh')}; {ext(COL,'The Collector: Six Foundational Shinto Myths','myth_src_col')}; {ext(FUN,'Fun! JAPAN: Japanese Mythology','myth_src_fun')}; {ext(NWE,'New World Encyclopedia','myth_src_nwe')}; {ext(BISH,'Kojiki creation summary','myth_src_bishop')}; {ext(TSU,'Tsunagu Japan: 12 shrines','myth_src_tsunagu')}; {ext(JT,'Japanese Taste: 10 Shinto gods','myth_src_jt')}; {ext(MLITIW,'MLIT: Opening Amano Iwato','myth_src_mlit_iwato')}; {ext(MLITKA,'MLIT: Kamiarizuki','myth_src_mlit_kami')}; {ext(JNTOKA,'JNTO: Kamiari Festival','myth_src_jnto')}; {ext(WATA,'Watabi: Kamiarizuki 2026','myth_src_watabi')}; {ext(WIKIHARE,'Wikipedia: White Hare of Inaba','myth_src_wikihare')}; {ext(FUNHARE,'Fun! JAPAN: White Rabbit of Inaba','myth_src_funhare')}; {ext(HAK,'Japan Experience: Hakuto Shrine','myth_src_hakuto')}; {ext(JGIW,'japan-guide: Amano Iwato','myth_src_jg')}; {ext(JEIW,'Japan Experience: Amano Iwato','myth_src_jeiw')}; {ext(JALIW,'JAL Japan Travel: Amano Iwato','myth_src_jal')}; {ext(JAL,'JAL: Miyazaki land of mythology','myth_src_jalmiya')}; {ext(JJ,'Jinja Journey: Izanagi Jingu','myth_src_jj')}; {ext(KIJI,'KIJI: Izanagi Shrine','myth_src_kiji')}; {ext(YUU,'Yuugen Guide: Awaji Island','myth_src_yuugen')}; {ext(JACT,'Japan Activity: Amano Iwato','myth_src_jact')}; {ext(KOK,'Kokugakuin Encyclopedia of Shinto: Ōkamuzumi (peaches)','myth_src_kok')}. Prices, bus times and festival dates are as reported at the time of writing; please check official pages before you travel.</p>

  </article>

</main>"""

t=open(f'{R}/_tools/culture/tea.py',encoding='utf-8').read()
tail=t[t.index("s=open(f'{R}/culture/omamori-guide"):]
tail=tail.replace('<div class="hero-bg-kanji">茶道</div>','<div class="hero-bg-kanji">神話</div>')
tail=tail.replace('<h1>The Japanese <em>Tea Ceremony</em> Guide</h1>','<h1>Japanese <em>Mythology</em> Guide</h1>')
tail=tail.replace('<div class="hero-jp">茶道ガイド</div>','<div class="hero-jp">日本神話ガイド</div>')
tail=tail.replace('What Happens, What to Do as a Guest, and Where to Try It','Kojiki Gods, Famous Myths and the Shrines Where They Happen')
tail=tail.replace('Tea Ceremony Guide','Japanese Mythology Guide')
tail=tail.replace('guide_tea','guide_mythology').replace('viator_guide_tea_sticky','viator_guide_mythology_sticky').replace('japanese+tea+ceremony','takachiho')
tail=re.sub(r'(<meta name="keywords" content=")[^"]*(")',r'\1Japanese mythology, Kojiki, Nihon Shoki, Izanagi and Izanami, Amaterasu, Susanoo, Okuninushi, white hare of Inaba, Kamiarizuki, Amano Iwato, Takachiho, Izumo Taisha\2',tail)
tail=tail.replace('"datePublished":"2026-11-08","dateModified":"2026-11-08"','"datePublished":"2026-11-16","dateModified":"2026-11-16"')
exec(tail)
