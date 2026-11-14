import re, os, json
R='/home/claude/sacred-japan'
S='ukiyo-e'
OUT=f'{R}/culture/{S}'
os.makedirs(OUT,exist_ok=True)

def link(href,txt,lab): return f'<a href="{href}" class="inline-link" onclick="trackEvent(\'click\',\'internal\',\'{lab}\')">{txt}</a>'
def ext(href,txt,lab): return f'<a href="{href}" target="_blank" rel="noopener" onclick="trackEvent(\'click\',\'external\',\'{lab}\')">{txt}</a>'
VI='https://www.viator.com/search/ukiyo-e?pid=P00298374&amp;mcid=42383&amp;medium=link&amp;campaign=sacred-japan'
EX='https://expedia.com/affiliate?siteid=1&amp;landingPage=https%3A%2F%2Fwww.expedia.co.jp%2FHotel-Search%3Fdestination%3DTokyo&amp;camref=1101l5JmFa&amp;creativeref=1011l87782&amp;adref=PZf6lQ77e8'
NIP='https://www.nippon.com/en/articles/-/12442'
JG='https://www.japan-guide.com/e/e2291.html'
FAA='https://blog.fineartamerica.com/what-is-ukiyo-e/'
WB='https://www.woodblock-print.eu/what-is-japanese-woodblock-printing.html'
LT='https://human.libretexts.org/Bookshelves/Art/Art_History_and_Theory/Asian_Art_History_(Gustlin_and_Gustlin)/10%3A_Global_Impact_(1700_CE__1900_CE)/10.3%3A_Ukiyo-e_(1636-1911)'


CAPST='font-size:13px;color:var(--enshu);margin-top:10px;text-align:center;line-height:1.6;'
LA='style="color:var(--enshu);"'
CMB='https://commons.wikimedia.org/wiki/File:'
def lk(t,u): return f'<a href="{u}" target="_blank" rel="noopener" {LA}>{t}</a>'
def ufig(src,alt,desc,by,fn,extra=''):
    cred=f'{by}, {lk("public domain","https://commons.wikimedia.org/wiki/Commons:Public_domain")}{extra}, via {lk("Wikimedia Commons",CMB+fn)} (resized)'
    return (f'<figure style="margin:36px auto;max-width:760px;">\n      <picture><source srcset="/culture/ukiyo-e/images/{src}.webp" type="image/webp"><img src="/culture/ukiyo-e/images/{src}.jpg" alt="{alt}" loading="lazy" style="width:100%;height:auto;border-radius:4px;display:block;"></picture>\n      <figcaption style="{CAPST}">{desc}<br>{cred}</figcaption>\n    </figure>')
FN_WAVE='Tsunami_by_hokusai_19th_century.jpg'
FN_FUJI='Red_Fuji_southern_wind_clear_morning.jpg'
FN_YOSH='Yoshiwara,_Station_15,_from_the_Fifty-Three_Stations_of_the_Tokaido_Road_(Reisho_edition),_by_Utagawa_Hiroshige,_1848-1849,_from_the_Hood_Museum_of_Art_-_PR.972.64.15.tif'
FN_SANJ='Print,_Sanjo_Bridge,_Kyoto,_in_The_Fifty-Three_Stations_of_the_Tokaido_Road_(Tokaido_Gojusan_Tsugi-no_Uchi),_ca._1834_(CH_18608919).jpg'
FN_SUSA='Yoshitoshi_Nihon-ryakushi_Susanoo-no-mikoto.jpg'
f_wave=ufig('wave','Woodblock print of a huge dark-blue wave with claw-like white foam curling over three narrow boats, with a small snow-capped Mount Fuji in the trough between the waves','The Great Wave off Kanagawa, from <em>Thirty-six Views of Mount Fuji</em>. The Metropolitan Museum of Art copy, JP1847.','Katsushika Hokusai',FN_WAVE,'; first published about 1830-1832 according to the Commons record')
f_fuji=ufig('redfuji','Woodblock print of a red-brown Mount Fuji with white snow streaks against a blue sky full of white cloud strips, with a dark green forest at the foot of the mountain','South Wind, Clear Sky (<em>Gaifu kaisei</em>), the "Red Fuji", from <em>Thirty-six Views of Mount Fuji</em>. This copy is an edition made around 1930, according to the Commons description.','Katsushika Hokusai',FN_FUJI,'; design first published about 1830')
f_yosh=ufig('yoshiwara','Woodblock print of travelers on a road under tall pine trees, with a white-capped Mount Fuji behind them, a woman riding a horse led by a boy, and two straw stacks in the fields to the left','Yoshiwara, Station 15 of the Tokaido, from the Fifty-Three Stations of the Tokaido Road (Reisho edition), 1848-1849. Hood Museum of Art, Dartmouth College, PR.972.64.15.','Utagawa Hiroshige',FN_YOSH,'; uploaded to Commons by Daderot in 2024')
f_sanj=ufig('sanjo','Woodblock print of a long wooden trestle bridge across a river with travelers, porters and women with umbrellas crossing it, and a town and many-peaked hills behind under an orange band of sky','Sanjo Bridge, Kyoto, from the Fifty-Three Stations of the Tokaido Road, about 1834. Cooper Hewitt, Smithsonian Design Museum, 1948-134-55 (gift of Mary Rutherford Jay).','Utagawa Hiroshige',FN_SANJ,'; the Commons record notes a Hoeido seal')
f_susa=ufig('susanoo','Dark woodblock triptych of a wild-haired warrior in torn white robes with a sword in his right hand, standing in white-capped waves in front of a blue serpent with an open red mouth','A triptych from the series <em>Nihon ryakushi</em> (日本略史), "Outline History of Japan", showing Susanoo and the eight-headed serpent.','Yoshitoshi (as named in the Commons file title)',FN_SUSA,'; Commons says the copyright term has expired in Japan; higher-resolution upload by Artanisen, 2020')

faqs=[
("What does ukiyo-e mean?","Ukiyo-e (浮世絵) means \"pictures of the floating world.\" The \"floating world\" was the city life of the Edo period: theaters, teahouses, fashion and the pleasure quarters. The prints were made for ordinary townspeople, not for temples or the court."),
("Is ukiyo-e a painting or a print?","Mostly a print. Some artists did paint, but most ukiyo-e that survive and travel are woodblock prints, made by a team and sold in editions. The Great Wave, for example, is a color woodblock print, not a painting."),
("Who are the most famous ukiyo-e artists?","For beginners I suggest six names: Hishikawa Moronobu (the early pioneer), Suzuki Harunobu (full-color prints), Kitagawa Utamaro (beautiful women), Toshusai Sharaku (kabuki actors), Katsushika Hokusai (the Great Wave) and Utagawa Hiroshige (Tokaido landscapes)."),
("Were ukiyo-e expensive?","Not by the time they were everywhere. Nippon.com says that multicolor prints were costly at first, but their price fell until they cost about as much as a bowl of noodles. They were sold as souvenirs, advertisements and entertainment, not as luxury objects."),
("Where can I see ukiyo-e in Japan?","In Tokyo, the Ota Memorial Museum of Art in Harajuku and the Sumida Hokusai Museum are the two I would put first, and the Tokyo National Museum also shows prints. Outside Tokyo, japan-guide lists museums in Matsumoto, Shizuoka, Obuse, Osaka and Atami. Exhibits rotate, so check each museum's site before you go."),
("Why did ukiyo-e become famous in Europe?","After Japan opened up, prints reached Europe, where they influenced Impressionist painters. japan-guide mentions this effect, and it is often called Japonisme. Inside Japan, interest dropped in the Meiji period as photography and other Western technology arrived."),
]
faq_html=''.join(f'''      <details class="faq-item">
        <summary>{q}</summary>
        <div class="faq-answer">{a}</div>
      </details>

''' for q,a in faqs)
faq_ld=json.dumps({"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in faqs]},ensure_ascii=False,indent=2)

TITLE="Ukiyo-e Guide: The Floating World, the Great Wave and Where to See the Prints"
DESC="A licensed guide's English introduction to ukiyo-e, Japanese woodblock prints: what the floating world was, how a print was made by four people, the masters from Moronobu to Hiroshige, and where to see them in Japan."
URL=f"https://sacred-japan.net/culture/{S}/"
OG="https://sacred-japan.net/images/og/og-culture-ukiyoe.jpg"

main=f'''<main>

  {f_wave}

  <!-- TABLE OF CONTENTS -->
  <aside class="toc" aria-label="Table of contents">
    <div class="toc-label">TABLE OF CONTENTS ／ 目次</div>
    <div class="toc-title">In This Guide</div>
    <ol>
      <li><a href="#opening">Opening: A Note from the Guide</a></li>
      <li><a href="#what">What the Floating World Was</a></li>
      <li><a href="#made">Four People Behind Every Print</a></li>
      <li><a href="#life">What Prints Did in Edo Life</a></li>
      <li><a href="#history">From Black Ink to Full Color</a></li>
      <li><a href="#masters">Six Masters to Know</a></li>
      <li><a href="#wave">The Great Wave</a></li>
      <li><a href="#west">How the Prints Reached the West</a></li>
      <li><a href="#see">Where to See Ukiyo-e in Japan</a></li>
      <li><a href="#faq">Frequently Asked Questions</a></li>
      <li><a href="#final">Final Thoughts</a></li>
    </ol>
  </aside>

  <article>

    <section id="opening">
      <p class="opening">Think of the most famous picture of Japan: a huge wave curling over three small boats, with Mount Fuji sitting calmly behind. It was not made for a museum. It was sold in Edo as an affordable print, and people probably bought it the way we buy a postcard.</p>
      <p>As a licensed guide, I find ukiyo-e the quickest way to meet the Edo period face to face: actors, wrestlers, travelers, ghosts and shopkeepers all appear in them. This guide explains what the prints were, who made them, and where you can stand in front of the real thing.</p>
    </section>

    <h2 id="what">What the Floating World Was<span class="h2-jp">浮世とは</span></h2>
    <p>Ukiyo-e (<span class="jp">浮世絵</span>) means "pictures of the floating world." {ext(LT,'A college art-history text','ukiyoe_libretexts')} explains that in the Edo period the word "floating" stood for savoring the present moment, a carefree realm away from daily worries, and that ukiyo-e recorded the lives of the townspeople and of those who entertained them.</p>
    <p>One popular account, repeated by a print dealer's blog, says that <em>ukiyo</em> was first a Buddhist word for the sorrowful, passing world, and that Edo writers kept the sound but changed the characters so that it meant "floating." I found that in only one source, so take it as a common explanation rather than a settled fact (see {ext(FAA,'Fine Art America','ukiyoe_faa')}).</p>
    <p>What is clear is the cast of characters. According to {ext(JG,'japan-guide','ukiyoe_japanguide')}, the subjects included kabuki actors, sumo wrestlers and geisha. Landscapes, ghost stories, warriors and flowers followed. If you have read our guide to the {link('/culture/samurai/','samurai','ukiyoe_to_samurai')}, you will meet many of the same warriors on the print sheets.</p>

    <h2 id="made">Four People Behind Every Print<span class="h2-jp">版画の作り方</span></h2>
    <p>The name on a print is the designer's, but the designer is only one of the people who made it. {ext(NIP,'Nippon.com','ukiyoe_nippon')} describes the steps:</p>
    <ol>
      <li><strong>The publisher</strong> commissioned a painter to draw the design in black ink on thin paper, called <em>hanshita-e</em>.</li>
      <li><strong>The censors</strong> reviewed the design.</li>
      <li><strong>The carver</strong> pasted the design onto a block of wood and cut it away.</li>
      <li><strong>The printer</strong> pulled the prints.</li>
    </ol>
    <p>The publisher mattered more than people realize. Nippon.com says that Tsutaya Juzaburo (1750-1797) employed Utamaro, Hokusai and Sharaku. A fine-print blog also notes that a print carried a censor's seal, which makes the sheet closer to a magazine cover than to a painting (per {ext(FAA,'Fine Art America','ukiyoe_faa_seal')}).</p>
    <p>For color, each color needed its own block, and the printer had to line up every block on the same sheet. {ext(WB,'One printmaking site','ukiyoe_woodblock_eu')} explains that a registration mark called <em>kento</em> made multicolor printing precise, and that Harunobu designed prints using more than twenty blocks.</p>

    <h2 id="life">What Prints Did in Edo Life<span class="h2-jp">江戸の暮らしの中で</span></h2>
    <p>Nippon.com lists several jobs for these sheets, and they are a good reminder that "art" was only one of them:</p>
    <ul>
      <li><strong>Souvenirs:</strong> prints were "not heavy or bulky," so travelers took them home. This lasted until photography arrived in the nineteenth century.</li>
      <li><strong>Advertising:</strong> prints promoted restaurants, clothing shops (including Hiroshige's view of the Daimaru kimono shop, forerunner of today's Daimaru department store) and cosmetics such as white face powder and lip rouge.</li>
      <li><strong>Education:</strong> children used them to learn to read and to name birds and flowers, and to play with cut-outs, board games and puzzles.</li>
      <li><strong>News:</strong> before national newspapers, prints carried word of a kabuki actor's death, a disaster or a crime to faraway places.</li>
    </ul>
    <p>As for price, Nippon.com says multicolor prints were expensive at first, but the price fell until a print cost about as much as a bowl of noodles. I like this fact more than any museum label, because it tells you who the audience was: everyone.</p>

    <h2 id="history">From Black Ink to Full Color<span class="h2-jp">モノクロから多色刷りへ</span></h2>
    <ul>
      <li><strong>1670s:</strong> Hishikawa Moronobu (1618-1694) is usually credited with establishing the single-sheet print. Early sheets were black ink, sometimes colored by hand.</li>
      <li><strong>By the mid-1700s:</strong> artisans made two- and three-color prints, called <em>benizuri-e</em>.</li>
      <li><strong>1760s:</strong> Suzuki Harunobu (1725-1770) made multicolor prints called <em>nishiki-e</em>, "brocade pictures." One source dates his breakthrough to 1765 and another says the 1760s; I use the wider range.</li>
      <li><strong>Late 1700s:</strong> Utamaro, Sharaku and others produce the portraits of beauties and actors that many people picture first.</li>
      <li><strong>1830s-1850s:</strong> the landscape masterpieces of Hokusai and Hiroshige.</li>
      <li><strong>Meiji period (1868-1912):</strong> photography and Western technology lowered interest in ukiyo-e in Japan itself.</li>
    </ul>

    <h2 id="masters">Six Masters to Know<span class="h2-jp">六人の絵師</span></h2>

    <h3>Hishikawa Moronobu (1618-1694): The Pioneer</h3>
    <p>He turned the print into an independent product. By 1672 his success was such that he began to sign his work, the first of the book illustrators to do so according to one summary of the genre. His subjects included scenes of the Yoshiwara, Edo's licensed pleasure quarter.</p>

    <h3>Suzuki Harunobu (1725-1770): The Color Revolution</h3>
    <p>Harunobu's brocade prints made full-color printing standard, with ten or more blocks behind a single print according to one history of the genre.</p>

    <h3>Kitagawa Utamaro (1753-1806): The Portraitist of Beauties</h3>
    <p>Utamaro is best known for figures rather than landscapes, in particular for fine portraits of beautiful women, as the sources agree. The publisher Tsutaya Juzaburo, mentioned above, employed him.</p>

    <h3>Toshusai Sharaku: The Mystery Man</h3>
    <p>Sharaku was active only in 1794-1795, the college text says. In that short time he produced striking portraits of kabuki actors. Little else is certain, so I will not guess about him.</p>

    <h3>Katsushika Hokusai (1760-1849): The Restless Genius</h3>
    <p>Hokusai spent most of his long life in what is now Sumida Ward in Tokyo, and the ward now has a museum dedicated to him (see the last section). His landscapes and his ghost-story prints are both famous.</p>

    <h3>Utagawa Hiroshige (1797-1858): The Poet of Travel</h3>
    <p>Hiroshige is known for the serene, atmospheric landscape, and for <em>The Fifty-three Stations of the Tokaido</em>, the road between Edo and Kyoto. Nippon.com notes that journeys and pilgrimages became popular from the early nineteenth century, and the landscape prints of Hokusai and Hiroshige grew out of that boom.</p>
    {f_yosh}
    <p>This is Yoshiwara, the fifteenth station of the Tokaido, from a later edition of the Fifty-Three Stations dated 1848-1849 in the Hood Museum of Art. Do not confuse it with Edo's pleasure quarter of the same name; here it is a post town on the road, and what the picture sells is Mount Fuji. White-capped Fuji stands behind tall, twisted pines. A woman in a flat hat rides a horse led by a boy, a traveler with a staff turns to look back, and a man with a pack walks on at the right. Two straw stacks sit in the fields at the left. The pines frame the mountain so that you look through the trees to it, as a real traveler would.</p>
    {f_sanj}
    <p>The road ended in Kyoto. In this print the last scene is the long wooden trestle bridge at Sanjo, with porters carrying boxes on poles, women under umbrellas and travelers in hats streaming across it. Behind the river lie the city roofs and, as the Commons record puts it, a range of many-peaked hills. I read the characters 大尾 near the title, which I take to mean "the end" of the series, but that is my reading, not the museum's. The record also lists a Hoeido seal, the publisher whose name is linked to this famous set.</p>
    <p>Utagawa Kuniyoshi (1798-1861) deserves a mention too. The woodblock prints of the Dan-no-ura sea battle in our {link('/culture/three-sacred-treasures/','guide to the Three Sacred Treasures','ukiyoe_to_treasures')} come from the same print tradition, although I cannot say which artists made those particular sheets.</p>
    {f_susa}
    <p>Many prints retell the myths too. This dark triptych shows the storm god Susanoo in the middle of the sheet, wild-haired and in torn white robes, with a sword in his right hand, while an enormous blue serpent rears at the right with its mouth wide open. The white wave crests that fill the bottom remind me of Hokusai's style. At the upper left, a smaller figure in red and white seems to be wrapped in pine boughs and rope; I think it may be the princess of the story, but I cannot confirm it from the print. The label at the upper right appears to give Susanoo's name and the words "eight-headed serpent"; I am reading that, not translating it from a catalogue. You can read the story behind it in our {link('/culture/three-sacred-treasures/#serpent','guide to the Three Sacred Treasures','ukiyoe_to_orochi')}.</p>

    <h2 id="wave">The Great Wave<span class="h2-jp">神奈川沖浪裏</span></h2>
    <p>The wave is a print, not a painting. The museum record that Wikimedia Commons quotes dates its first publication to between about 1830 and 1832 and lists it as part of Hokusai's series <em>Thirty-six Views of Mount Fuji</em>. A print-dealer's blog adds that thousands of impressions were pulled over the years; I found that edition claim in only one source, so I treat it as likely rather than proven.</p>
    <p>The same Commons description corrects a popular idea. The wave is often used in books about tsunami, but it says there is no reason to think Hokusai meant it that way, and that the waves are more accurately <em>okinami</em> (<span class="jp">沖波</span>), great waves out at sea. Look at the three boats at the bottom and the right: crouching figures hug the hulls, and the sea is about to fall on them.</p>
    <p>If you see it in Japan, notice how small the boats and the mountain are. The sea takes up the page. I think that choice, with the mountain far away and the water in front, is why the picture still works as well as a poster as it did as a print.</p>
    <p>Hokusai's other great Fuji design is the opposite mood. <em>South Wind, Clear Sky</em>, nicknamed the "Red Fuji", shows the mountain in clear morning light.</p>
    {f_fuji}
    <p>The color is the whole story here: a red-brown mountain, a deep blue sky broken into white strips of cloud, and a green forest at the foot that fades into the red. Because this is a copy printed around 1930, it is a good reminder that these designs were printed again and again. A Commons note on this file says the skill and care of an edition from about 1930 were the same as around 1830, that the woodcutter and printer matter as much as the artist, and that only experts can tell the many versions apart, mainly by differences in the frame around the title.</p>

    <h2 id="west">How the Prints Reached the West<span class="h2-jp">西洋への影響</span></h2>
    <p>While interest dropped inside Japan in the Meiji period, japan-guide says the prints gained prominence in Europe, where they influenced Impressionist painters. A history of the genre adds the names Vincent van Gogh and Henri de Toulouse-Lautrec, and calls the fashion for Japanese art Japonisme.</p>
    <p>The tradition did not die. Woodblock-print makers later tried to keep it alive with <em>shin hanga</em>, "new prints," published by firms such as Watanabe that kept the old team method of designer, carver and printer, according to the printmaking site mentioned earlier.</p>

    <h2 id="see">Where to See Ukiyo-e in Japan<span class="h2-jp">浮世絵を見に行く</span></h2>
    <p>Prints fade in strong light, so museums change what is on display often. The notes below say what each place is, not what is on this month. Please check each museum's official site for hours, closed days and admission, because the sources I used differ on them.</p>

    <h3>Ota Memorial Museum of Art, Harajuku, Tokyo</h3>
    <p>The museum was founded in 1980 after the death of the collector Ota Seizo, whose dying wish was to make his private collection public, according to {ext('https://www.gotokyo.org/en/spot/130/','GO TOKYO','ukiyoe_gotokyo_ota')}. Sources give its size as between 10,000 and 15,000 works, so I will just say "well over ten thousand." {ext(JG,'japan-guide','ukiyoe_japanguide_ota')} says exhibits change monthly. Lonely Planet adds that you swap your shoes for slippers and calls it the best place in Tokyo to see ukiyo-e; it also says the museum closes for the last few days of each month between exhibitions.</p>

    <h3>Sumida Hokusai Museum, Ryogoku, Tokyo</h3>
    <p>It opened in 2016 in Sumida Ward, Hokusai's birthplace and home for most of his life. According to {ext('https://www.gltjp.com/en/directory/item/19282/','GLTJP','ukiyoe_gltjp_sumida')}, it presents his career from several angles and relates it to Sumida's history and culture, has a library where anyone can browse the materials free of charge, and sits near the Ryogoku Kokugikan sumo stadium, which makes a good pairing for a day in Ryogoku.</p>

    <h3>More Museums Around Japan</h3>
    <p>japan-guide lists these without hours or fees:</p>
    <ul>
      <li><strong>Tokyo National Museum</strong> (Ueno Park): many ukiyo-e among its collection.</li>
      <li><strong>Japan Ukiyo-e Museum</strong> (Matsumoto): prints from the Sakai family collection, said to number over 100,000.</li>
      <li><strong>Tokaido Hiroshige Museum</strong> (Shizuoka): Hiroshige, including the Fifty-three Stations of the Tokaido.</li>
      <li><strong>Hokusai Museum</strong> (Obuse, Nagano): Hokusai, including the Thirty-six Views of Mount Fuji and the Great Wave.</li>
      <li><strong>MOA Museum of Art</strong> (Atami): periodic ukiyo-e displays.</li>
      <li><strong>Kamigata Ukiyo-e Museum</strong> (Namba, Osaka): prints of the Osaka and Kyoto school, often kabuki actors.</li>
    </ul>
    <p>One Tokyo travel blog also lists the Adachi Institute of Woodcut Prints in Itabashi as a place where visitors can try printmaking themselves. I could not confirm the current program, so please check before you plan around it.</p>
    <div style="background:var(--washi-dark);border-left:4px solid var(--kin);padding:16px 20px;margin:24px 0;border-radius:2px;">
      <p style="margin:0;">&#127754; <strong>Plan your trip:</strong> Browse ukiyo-e and printmaking experiences, or find a stay in Tokyo. <a href="{VI}" target="_blank" rel="noopener sponsored" onclick="trackEvent('click','affiliate','viator_ukiyoe_local')">Browse ukiyo-e experiences on Viator</a> &middot; <a href="{EX}" target="_blank" rel="noopener sponsored" onclick="trackEvent('click','affiliate','expedia_ukiyoe_local')">Find hotels in Tokyo</a></p>
    </div>

    <h2 id="faq">Frequently Asked Questions<span class="h2-jp">よくあるご質問</span></h2>

    <div class="faq-stack">

{faq_html}    </div>

    <h2 id="final">Final Thoughts<span class="h2-jp">むすびに</span></h2>
    <p>A good ukiyo-e print rewards a slow look: the grain of the wood in the sky, the tiny people, the censor's seal in the corner. These sheets were made by teams, sold cheaply and enjoyed by everyone, and that is exactly why they tell you so much about Edo.</p>
    <p>If you enjoy them, look next at the other Edo arts around the prints: the warriors in our {link('/culture/samurai/','samurai guide','ukiyoe_to_samurai2')}, the feudal capital in our {link('/guides/edo-castle/','Edo Castle guide','ukiyoe_to_edo')}, and the objects made by hand in our {link('/crafts/','crafts section','ukiyoe_to_crafts')}.</p>

    <div class="closing-block">
      <span class="torii">&#127754;</span>
      <p>A wave, a mountain and a bowl of noodles' worth of art.</p>
    </div>

    <section class="related-section">
      <h2>Related Guides</h2>
      <span class="h2-jp">関連ガイド</span>
      <div class="related-grid">
        <a class="related-card" href="/culture/samurai/" onclick="trackEvent('click','internal','related_ukiyoe_to_samurai')">
          <div class="related-card-label">SACRED JAPAN ／ GUIDE</div>
          <div class="related-card-title">&#9876;&#65039; The Samurai Guide →</div>
          <div class="related-card-desc">Armor, swords and the warriors who fill the print sheets.</div>
        </a>
        <a class="related-card" href="/culture/three-sacred-treasures/" onclick="trackEvent('click','internal','related_ukiyoe_to_treasures')">
          <div class="related-card-label">SACRED JAPAN ／ GUIDE</div>
          <div class="related-card-title">&#128302; The Three Sacred Treasures →</div>
          <div class="related-card-desc">The sea battle of Dan-no-ura, shown in woodblock triptychs.</div>
        </a>
        <a class="related-card" href="/guides/edo-castle/" onclick="trackEvent('click','internal','related_ukiyoe_to_edo')">
          <div class="related-card-label">SACRED JAPAN ／ GUIDE</div>
          <div class="related-card-title">&#127983;&#65039; Edo Castle Guide →</div>
          <div class="related-card-desc">The shogun's capital where these prints were published.</div>
        </a>
        <a class="related-card" href="/culture/tea-ceremony/" onclick="trackEvent('click','internal','related_ukiyoe_to_tea')">
          <div class="related-card-label">SACRED JAPAN ／ GUIDE</div>
          <div class="related-card-title">&#127861; The Japanese Tea Ceremony Guide →</div>
          <div class="related-card-desc">Another art of slow looking, in a small room.</div>
        </a>
      </div>
    </section>

    <p style="font-size:14px;color:var(--enshu);line-height:1.7;margin-top:32px;"><strong>Sources:</strong> {ext(NIP,'Nippon.com','ukiyoe_src_nippon')} (uses, price, production, publisher); {ext(JG,'japan-guide','ukiyoe_src_jg')} (history, museums); {ext(LT,'college art-history text','ukiyoe_src_lt')} (the floating world, artists); {ext(WB,'woodblock-print.eu','ukiyoe_src_wb')} (kento, shin hanga); {ext(FAA,'Fine Art America blog','ukiyoe_src_faa')} (single-source claims are flagged in the text); {ext('https://www.gotokyo.org/en/spot/130/','GO TOKYO','ukiyoe_src_gotokyo')} and {ext('https://www.gltjp.com/en/directory/item/19282/','GLTJP','ukiyoe_src_gltjp')} (museums).</p>

  </article>

</main>'''

t=open(f'{R}/_tools/culture/tea.py',encoding='utf-8').read()
tail=t[t.index("s=open(f'{R}/culture/omamori-guide"):]
tail=tail.replace('<div class="hero-bg-kanji">茶道</div>','<div class="hero-bg-kanji">浮世絵</div>')
tail=tail.replace('<h1>The Japanese <em>Tea Ceremony</em> Guide</h1>','<h1>Ukiyo-e: The <em>Floating World</em> in Woodblock Prints</h1>')
tail=tail.replace('<div class="hero-jp">茶道ガイド</div>','<div class="hero-jp">浮世絵ガイド</div>')
tail=tail.replace('What Happens, What to Do as a Guest, and Where to Try It','The Great Wave, the Masters and Where to See the Prints')
tail=tail.replace('Tea Ceremony Guide','Ukiyo-e Guide')
tail=tail.replace('guide_tea','guide_ukiyoe').replace('viator_guide_tea_sticky','viator_guide_ukiyoe_sticky').replace('japanese+tea+ceremony','ukiyo-e+woodblock+prints')
tail=re.sub(r'(<meta name="keywords" content=")[^"]*(")',r'\1ukiyo-e, Japanese woodblock prints, Great Wave off Kanagawa, Hokusai, Hiroshige, Utamaro, Sharaku, floating world, Ota Memorial Museum of Art, Sumida Hokusai Museum\2',tail)
tail=tail.replace('"datePublished":"2026-11-08","dateModified":"2026-11-08"','"datePublished":"2026-11-14","dateModified":"2026-11-14"')
exec(tail)
