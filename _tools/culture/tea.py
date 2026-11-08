import re, os, shutil
from PIL import Image
R='/home/claude/sacred-japan'
A='/mnt/user-data/attachments/fd332c08-3f6b-545a-883b-83277e19ff52/'
S='tea-ceremony'
OUT=f'{R}/culture/{S}'
os.makedirs(OUT+'/images',exist_ok=True)
photos={
 'gokokuji':'f1e4ff89-image.jpg','water-set':'786e1ffa-image.jpg','portable-set':'a0f3fdef-image.jpg',
 'hamarikyu-tray':'4c70b749-image.jpg','bowl-served':'4557e7c9-image.jpg','bowls-line':'98dda4e7-image.jpg','nago-lesson':'bf25dac5-image.jpg',
 'shofuso-room':'9fe4b79b-image.jpg','uji-tokonoma':'0ede41fb-image.jpg','nijiriguchi':'530e3b2e-image.jpg'}
for k,f in photos.items():
    im=Image.open(A+f).convert('RGB'); w,h=im.size
    if w>1200: im=im.resize((1200,round(h*1200/w)),Image.LANCZOS)
    im.save(f'{OUT}/images/{k}.jpg',quality=84,optimize=True); im.save(f'{OUT}/images/{k}.webp',quality=80)

def fig(k,alt,cap,credit,hero=False,maxw=760):
    st='margin:0 0 48px;' if hero else f'margin:36px auto;max-width:{maxw}px;'
    img_st='width:100%;max-height:420px;object-fit:cover;border-radius:4px;display:block;' if hero else 'width:100%;height:auto;border-radius:4px;display:block;'
    ld='eager' if hero else 'lazy'
    return f'''<figure style="{st}">
      <picture><source srcset="/culture/{S}/images/{k}.webp" type="image/webp"><img src="/culture/{S}/images/{k}.jpg" alt="{alt}" loading="{ld}" style="{img_st}"></picture>
      <figcaption style="font-size:13px;color:var(--enshu);margin-top:10px;text-align:center;line-height:1.6;">{cap}<br>{credit}</figcaption>
    </figure>'''
BYSA4='<a href="https://creativecommons.org/licenses/by-sa/4.0/" target="_blank" rel="noopener" style="color:var(--enshu);">CC BY-SA 4.0</a>'
BY4='<a href="https://creativecommons.org/licenses/by/4.0/" target="_blank" rel="noopener" style="color:var(--enshu);">CC BY 4.0</a>'
PD='<a href="https://commons.wikimedia.org/wiki/Template:PD-USGov-Military-Marines" target="_blank" rel="noopener" style="color:var(--enshu);">public domain</a>'
VIA='via Wikimedia Commons (resized)'

f_hero=fig('gokokuji','A tea host kneeling at a low shelf and lifting a bamboo ladle over an iron kettle while guests watch','A host prepares tea before seated guests at Gokokuji, a Buddhist temple in Tokyo.',f'Photo: KuboBella, {BYSA4}, {VIA}',hero=True)
f_tray=fig('hamarikyu-tray','Two bowls of bright green matcha on a black lacquer tray with two Japanese sweets on white paper, on tatami','Two bowls of matcha and two sweets, served in the Hamarikyu Gardens in Tokyo.',f'Photo: WorldContributor, {BYSA4}, 2016, {VIA}')
f_water=fig('water-set','A black iron kettle on a tile and a blue-and-white water jar on a wooden stand with a bamboo ladle, on tatami','The kettle (left) and the water jar (right), with a bamboo ladle resting on top of the stand.',f'Photo: Douglas Perkins, {BY4}, 2015, {VIA}')
f_port=fig('portable-set','A portable tea set on black lacquer boxes with a blue-and-white water jar, an iron kettle, a bowl with a whisk, and a tatami-topped stool','A portable tea set laid out on black lacquer boxes, with a stool for the guest.',f'Photo: Savannah Rivka, {BYSA4}, 2019, {VIA}')
f_bowl=fig('bowl-served','A host in a pink kimono sets a gold-patterned tea bowl of matcha on the tatami in front of a guest','A host sets a finished bowl down for the guest.',f'Photo: KuboBella, {BYSA4}, 2024, {VIA}')
f_line=fig('bowls-line','A row of tea bowls set along tatami mats while a host in a pale kimono places one more bowl','Bowls lined up along the mats as the host serves a row of guests.',f'Photo: KuboBella, {BYSA4}, 2024, {VIA}')
f_nago=fig('nago-lesson','A kimono-clad teacher kneeling beside three seated women who are drinking tea from bowls in a small tatami room','A tea-etiquette lesson for visitors in a small tatami room in Nago, Okinawa, September 2013.',f'Photo: Lance Cpl. Nicholas Ranum, U.S. Marine Corps, {PD}, {VIA}')

PDSELF='<a href="https://commons.wikimedia.org/wiki/Template:PD-self" target="_blank" rel="noopener" style="color:var(--enshu);">public domain</a>'
f_shofu=fig('shofuso-room','A tea room with a woven-strip ceiling, a hanging scroll with one large character in the alcove, and a small vase of flowers on the alcove floor','The tea house at the Shofuso Japanese House and Garden, with its alcove on the right.',f'Photo: <a href="https://commons.wikimedia.org/wiki/User:Gryffindor" target="_blank" rel="noopener" style="color:var(--enshu);">Gryffindor</a>, {BYSA4}, 4 August 2017, {VIA}')
f_uji=fig('uji-tokonoma','A tatami room with an alcove holding a tall calligraphy scroll and a small flower arrangement in a woven vase, with an iron kettle on a brazier and pale green utensils on the left','A tea room in Uji, set up for a gathering.',f'Photo: <a href="https://commons.wikimedia.org/wiki/User:Wicki" target="_blank" rel="noopener" style="color:var(--enshu);">Wicki</a>, {PDSELF}, 22 April 2009, {VIA}')
f_noji=fig('nijiriguchi','The inside of a small tea room with a low opening to a moss garden at left, shoji screens above it, and a taller sliding opening at right with a bamboo fence and stone lantern outside','Looking out of a small tea room (koma) at Shinkei-en, in Kurashiki.',f'Photo: <a href="https://commons.wikimedia.org/wiki/User:Miya" target="_blank" rel="noopener" style="color:var(--enshu);">Miya</a>, {BYSA4}, 27 July 2019, {VIA}')

def link(href,txt,lab): return f'<a href="{href}" class="inline-link" onclick="trackEvent(\'click\',\'internal\',\'{lab}\')">{txt}</a>'
VI='https://www.viator.com/search/japanese+tea+ceremony?pid=P00298374&amp;mcid=42383&amp;medium=link&amp;campaign=sacred-japan'
EX='https://expedia.com/affiliate?siteid=1&amp;landingPage=https%3A%2F%2Fwww.expedia.co.jp%2FHotel-Search%3Fdestination%3DKyoto&amp;camref=1101l5JmFa&amp;creativeref=1011l87782&amp;adref=PZf6lQ77e8'

faqs=[
("Do I need to know the rules before I go?","No. At a visitor-oriented session the host will tell you what to do, step by step, and nobody expects a first-timer to be fluent. Following the host's lead is the whole etiquette."),
("Do I have to sit on my knees?","The traditional posture is kneeling (seiza), but it is hard on unaccustomed legs. Many hosts will let visitors sit another way or offer a chair, and some venues are set up for chairs from the start. Say so when you book if you need it."),
("Which way do I turn the bowl, and how many times?","Schools differ on the details, so follow your host. The shared principle is simple: the front of the bowl faces the host, and as the guest you turn it slightly so that you do not drink from the front."),
("Do I eat the sweet before or after the tea?","Before. The sweet is meant to be eaten first, so its sweetness balances the bitterness of the matcha that follows."),
("What is the difference between thin tea and thick tea?","Thin tea (usucha) is the lighter, frothy bowl most visitors are served. Thick tea (koicha) is richer, and in a formal gathering one bowl is shared among guests, who each take a few sips and pass it on."),
("Why is the door of a tea room so small?","The crawl-in entrance (nijiriguchi) is only about 65 cm high and 60 cm wide, so everyone has to bend low and slip in, whatever their rank. Tradition credits Sen no Rikyu with introducing it. A taller entrance, the kininguchi, also exists, where guests bow only slightly."),
("Did samurai really leave their swords outside the tea room?","Sources describe a sword rack (katana-gake) near the tea room entrance where warriors were expected to leave their swords, and the small door is traditionally tied to the idea that everyone is equal inside. I have not found a written rule, so treat it as a custom rather than a law."),
("Is a tea ceremony religious?","It grew up alongside Zen Buddhism and still carries that atmosphere, which is one reason it is often held in temples, but you do not need to hold any belief to take part."),
]
faq_html=''.join(f'''      <details class="faq-item">
        <summary>{q}</summary>
        <div class="faq-answer">{a}</div>
      </details>

''' for q,a in faqs)
import json
faq_ld=json.dumps({"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in faqs]},ensure_ascii=False,indent=2)

TITLE="Japanese Tea Ceremony Guide: What Happens, What to Do and Where to Try It"
DESC="A licensed guide's English introduction to the Japanese tea ceremony (chanoyu): a short history, the crawl-in door and the sword rack, why warlords loved tea, what to do as a guest, and where to learn about the tools."
URL=f"https://sacred-japan.net/culture/{S}/"
OG="https://sacred-japan.net/images/og/og-culture-tea-ceremony.jpg"

main=f'''<main>

  {f_hero}

  <!-- TABLE OF CONTENTS -->
  <aside class="toc" aria-label="Table of contents">
    <div class="toc-label">TABLE OF CONTENTS ／ 目次</div>
    <div class="toc-title">In This Guide</div>
    <ol>
      <li><a href="#opening">Opening: A Note from the Guide</a></li>
      <li><a href="#what">What the Tea Ceremony Is</a></li>
      <li><a href="#history">A Short History: From Zen Monks to Rikyu</a></li>
      <li><a href="#room">The Room and the Garden</a></li>
      <li><a href="#doors">The Small Door and the Sword Rack</a></li>
      <li><a href="#politics">Why Warlords Loved Tea</a></li>
      <li><a href="#guest">What You Actually Do as a Guest</a></li>
      <li><a href="#kinds">Thin Tea, Thick Tea and the Longer Gathering</a></li>
      <li><a href="#tools">The Tools: Where to Learn More</a></li>
      <li><a href="#try">Trying It in Japan</a></li>
      <li><a href="#faq">Frequently Asked Questions</a></li>
      <li><a href="#final">Final Thoughts</a></li>
    </ol>
  </aside>

  <article>

    <section id="opening">
      <p class="opening">The first time I sat in a tea room as a guest, I was more worried about my knees than about the tea. Then the host set down a small bowl of bright green, frothy matcha, said almost nothing, and the room went quiet in a way I still remember.</p>
      <p>As a licensed guide, I am often asked whether the tea ceremony is "worth it" for a traveler. My answer is yes, if you go in knowing what it is. It is not a performance and it is not a test. It is a way of serving one bowl of tea with full attention, and of receiving it the same way.</p>
    </section>

    <h2 id="what">What the Tea Ceremony Is<span class="h2-jp">茶の湯とは</span></h2>
    <p>In Japanese it is called <em>chanoyu</em> (<span class="jp">茶の湯</span>), literally "hot water for tea," or <em>chadō</em> / <em>sadō</em> (<span class="jp">茶道</span>), "the way of tea." A host prepares powdered green tea, matcha, in front of the guests and serves it with a small sweet. The skill lies in the care of every movement, the choice of tools, and the setting.</p>
    <p>Four ideas are usually given as its core: <strong>wa</strong> (harmony), <strong>kei</strong> (respect), <strong>sei</strong> (purity) and <strong>jaku</strong> (tranquility). A fifth phrase travels with them, <em>ichigo ichie</em> (<span class="jp">一期一会</span>), the idea that each gathering happens only once and should be treasured. It is attributed to the tradition of Sen no Rikyu's own teacher, Takeno Jo-o.</p>
    {f_tray}
    <p>This is what most visitors receive: matcha with a seasonal sweet, set out on a lacquer tray. The photograph was taken in the Hamarikyu Gardens in Tokyo, where a tea house stands beside the pond. Notice that the sweet sits on its own sheet of paper with a small pick beside it, and the bowls are plain and slightly rough rather than glossy. That restraint is deliberate.</p>

    <h2 id="history">A Short History: From Zen Monks to Rikyu<span class="h2-jp">茶道の歴史</span></h2>
    <p>Tea came to Japan from China, and the story of chanoyu fits on a short timeline.</p>
    <ul>
      <li><strong>815:</strong> a Buddhist monk is said to have served tea to Emperor Saga, the earliest firm record.</li>
      <li><strong>Late 1100s:</strong> the monk Eisai brings powdered tea and tea seeds back from China.</li>
      <li><strong>1200s:</strong> tea-tasting parties become popular among the warrior class.</li>
      <li><strong>1400s:</strong> Murata Juko, who studied Zen under the monk Ikkyu, develops tea as a discipline rather than a pastime.</li>
      <li><strong>1500s:</strong> <strong>Sen no Rikyu</strong> redefines the tea house, garden, utensils and procedure around <em>wabi</em>, a beauty found in the plain and the imperfect: a smaller room and rustic bowls. He serves the warlords Oda Nobunaga and, later, Toyotomi Hideyoshi.</li>
      <li><strong>1587:</strong> Hideyoshi holds the Grand Kitano Tea Ceremony in Kyoto.</li>
      <li><strong>1591:</strong> Hideyoshi orders Rikyu to take his own life.</li>
      <li><strong>After Rikyu:</strong> his line splits into three schools run by his great-grandchildren, Omotesenke, Urasenke and Mushakojisenke, still the best-known names in tea.</li>
    </ul>
    <h3>The Samurai Tea Master: Kobori Enshu</h3>
    <p>A second branch grew among the warrior class. <strong>Kobori Enshu</strong> (1579 to 1647) was assigned to teach the third Tokugawa shogun, Iemitsu, the tea ceremony, and he designed tea houses, including the Bosen-seki at Koho-an, a sub-temple of Daitoku-ji in Kyoto. His style came to be called Enshu-ryu. Several of the photographs in this guide show the present-day Kobori Enshu school, taken at demonstrations in Tokyo.</p>

    <h2 id="room">The Room and the Garden<span class="h2-jp">茶室と露地</span></h2>
    <p>The ideal tea room (<em>chashitsu</em>) is small, about 4.5 tatami mats, with a low ceiling, a sunken hearth and an alcove for a hanging scroll or flowers. Around the house is a garden path, the <em>roji</em>, where guests rinse their hands and mouth at a stone basin before going in. How you get through the door is the next section.</p>
    {f_shofu}
    <p>This is a tea room in the form the books describe. According to the Commons description it is the tea house at the Shofuso Japanese House and Garden, which is in Philadelphia, not Japan. The alcove on the right is the <em>tokonoma</em>, the place of honor. It holds a hanging scroll with one large character that appears to read <span class="jp">麗</span> (<em>rei</em>, "beauty"), and a small vase of flowers on the alcove floor. Look up at the ceiling of woven strips and at the rough, unfinished log post beside the alcove. The wide-angle view bends the walls, so do not read the lean as the room's real shape.</p>
    {f_uji}
    <p>This second room is in Uji, near Kyoto, and the host's side is laid out on the left: a black brazier with an iron kettle, and pale green lidded pieces on a black lacquer tray. The alcove holds a tall scroll of calligraphy and a slim arrangement of grasses with a purple flower in a woven vase. I cannot tell from the picture what every utensil is, so I will only point out the kettle and the scroll. What matters is the arrangement: one scroll, one small bouquet, nothing more. The scroll and the flowers are chosen to suit the season and the day.</p>
    {f_water}
    <p>Here is the heart of the preparation. On the right is the water jar (<em>mizusashi</em>); using the bamboo ladle (<em>hishaku</em>), the host moves cold water into the iron kettle (<em>kama</em>) on the left, which keeps the water hot. The Commons description of this photograph says exactly that. Around them, a host works with a handful of simple tools: the tea bowl (<em>chawan</em>), a bamboo whisk (<em>chasen</em>), a bamboo scoop (<em>chashaku</em>) and a small lidded container for the powder.</p>
    {f_port}
    <p>Not every tea session happens in a tea house. This portable set was photographed in Japan, and it looks like a table-style arrangement: the lacquer boxes hold the kettle and water jar, the bowl and whisk sit in the middle, and a stool is placed for the guest. I am reading the setup from the picture, since the file description does not name the style. Table-style tea is common at events and in places where long kneeling is not realistic, and it is the form many visitors meet first.</p>

    <h2 id="doors">The Small Door and the Sword Rack<span class="h2-jp">躙口・貴人口・刀掛け</span></h2>
    <p>The first thing a tea room asks of you happens before you sit down. In a rustic-style room the guest entrance is the <em>nijiriguchi</em> (<span class="jp">躙口</span>), the "crawl-in entrance." The standard measure is about 65 cm high and 60 cm wide. You take off your footwear, kneel at the threshold, put your hands and head through, and slip in sideways. No one walks in upright, and that is the point.</p>
    {f_noji}
    <p>Commons labels this photograph as the nijiriguchi of a small tea room (<em>koma</em>) at Shinkei-en in Kurashiki's Bikan district. I take the low opening at the left, with shoji above it and a mossy garden beyond, to be that door seen from inside. The taller opening at the right, with a bamboo fence and a stone lantern outside, is a different kind of door.</p>
    <p>Tradition credits Sen no Rikyu with this entrance. One record, the <em>Nanboroku</em>, says he first made it in a two-mat tea room. Other records say he was struck by the small, rough entrance of a wharf near his home and used the idea in a small tea room.</p>
    <h3>The Tall Door for Important Guests: Kininguchi</h3>
    <p>Not every room makes the guest crawl. The <em>kininguchi</em> (<span class="jp">貴人口</span>) is a tall entrance whose name means "entrance for nobles and dignitaries." Guests enter by bowing only slightly. The sources I found describe the door and its name but do not explain how it was used, so my reading is that it spared high-ranking guests the crawl.</p>
    <h3>Leaving the Sword at the Door</h3>
    <p>Near the entrance of a tea room there was a sword rack, the <em>katana-gake</em> (<span class="jp">刀掛け</span>), where warriors were expected to leave their swords. One tea-school account says samurai had to take off their swords in front of the small door, which meant that everybody was equal inside, and adds that the tea room was often used for politically confidential talk in those days.</p>
    <p>I would add one thought of my own. Nobody inside was carrying a blade, and the door itself forced every guest into the same humble posture. It is easy to see why that made a safe place for a quiet conversation. The sources I found state the sword rack and the idea of equality, not a safety rule, so I give that part as my reading.</p>

    <h2 id="politics">Why Warlords Loved Tea<span class="h2-jp">戦国と茶の湯</span></h2>
    <p>This is the part of the story that surprises visitors. In the 1500s, while Japan's warlords fought for control of the country, tea was more than a quiet pastime. It was a mark of status and a way to talk.</p>
    <p>Oda Nobunaga is the clearest case. One account says he gave famous tea utensils to vassals who won battles, in place of the usual land, because land was limited, and that owning a celebrated piece carried a status comparable to a domain and a castle. The same account says he collected famous utensils, mostly from wealthy merchants, and that tea gatherings were treated as a privilege: Hideyoshi was reportedly one of only five top vassals allowed to hold them. It also tells of a general who was rewarded with a distant province but no tea set and complained that he had lost his taste for tea. I read that last one as a vivid anecdote, not a verified quotation.</p>
    <p>Other writers describe tea gatherings as a diplomatic tool, and note that tea diaries suggest the ceremonies played key roles in the political and business dealings of warlords and merchants. Put that beside the small, weapon-free room and the picture makes sense: this was a place for a private word.</p>
    <p>Hideyoshi took it further, in two directions. He had a Golden Tea Room built with Rikyu for a tea gathering for the emperor, a display of his wealth and authority. Then in 1587 he held the Grand Kitano Tea Ceremony, which was open to the public regardless of social status. One account reports more than 800 tea rooms, with participants of all classes assigned to rooms by lottery.</p>
    <p>Rikyu stood between these worlds. He was one of Hideyoshi's closest confidants, and in 1591 he was ordered to take his own life. Wikipedia notes that the exact reason is unknown, though differences of opinion and his independence are the usual explanations. When a host kneels to serve you one bowl in a quiet room, you are sitting in a form that grew up next to the powerful.</p>

    <h2 id="guest">What You Actually Do as a Guest<span class="h2-jp">客としての作法</span></h2>
    {f_bowl}
    <p>Here is the usual flow, in the order you will experience it.</p>
    <ol>
      <li><strong>Settle in.</strong> You are shown where to sit. Take off your shoes at the entrance and wear clean socks.</li>
      <li><strong>Eat the sweet first.</strong> It is placed in front of you on paper. Eat it before the tea. At a formal gathering the guest eats from a sheet of paper called <em>kaishi</em>.</li>
      <li><strong>Receive the bowl.</strong> The host sets the bowl in front of you or hands it to you. Bow slightly to thank the host.</li>
      <li><strong>Turn the bowl.</strong> The host presents the bowl with its front toward you, so you turn it slightly to avoid drinking from the front. Schools differ on the exact motion; copy the host.</li>
      <li><strong>Drink.</strong> Take it in a few sips and enjoy the bowl.</li>
      <li><strong>Wipe the rim and look.</strong> Wipe where your lips touched. In a formal gathering the bowl itself is something to admire, so it is normal to look closely at its shape and glaze.</li>
    </ol>
    {f_line}
    <p>At a longer gathering, you may find several guests served in a line, as above. The bowls are not matching. Each one is chosen on purpose, which is why the host may set down quite different bowls in a single row.</p>
    {f_nago}
    <p>And here is the reassuring truth: you will almost certainly be taught on the spot. This picture shows a teacher coaching a group of visitors through the etiquette in a small room, and everyone is clearly a beginner. A relaxed room is part of the point.</p>

    <h2 id="kinds">Thin Tea, Thick Tea and the Longer Gathering<span class="h2-jp">薄茶・濃茶・茶事</span></h2>
    <p>Two kinds of tea appear in the tradition. <strong>Thin tea</strong> (<em>usucha</em>) is the lighter, frothy bowl. <strong>Thick tea</strong> (<em>koicha</em>) is richer and, in the more formal setting, shared: each guest takes a few sips, wipes the rim and passes the bowl to the next person. That shared bowl is recorded in documents from 1586 and is considered Rikyu's invention.</p>
    <p>The settings differ too. A <em>chakai</em> is a simpler gathering with sweets, thin tea and perhaps a light meal. A <em>chaji</em> is the full formal occasion, with a meal, sweets, thick tea and thin tea, and it can last up to four hours. Visitors are almost always offered something much closer to the first.</p>

    <h2 id="tools">The Tools: Where to Learn More<span class="h2-jp">茶道具</span></h2>
    <p>Good, properly licensed photographs of tea utensils are hard to find, so instead of showing them I point you to the places where you can read about them or see them. Our own guides come first.</p>
    <ul>
      <li><strong>Tea bowl (<em>chawan</em>):</strong> the Raku family has made hand-kneaded, low-fired Raku bowls for about 450 years, and a Raku piece is often the main bowl at a tea gathering. The <a href="https://www.japan.travel/en/spot/1161/" target="_blank" rel="noopener" onclick="trackEvent('click','external','tea_raku_museum')">Raku Museum in Kyoto</a> shows pieces from the family collection; check its official site for hours and current exhibits. For other ceramic traditions, see our guides to {link('/guides/bizen-ware/','Bizen ware','tea_tools_bizen')} and {link('/guides/arita-ware/','Arita ware','tea_tools_arita')}, the {link('/crafts/','crafts hub','tea_tools_crafts')} for Hagi, Mino and Shigaraki, and {link('/guides/kintsugi/','kintsugi','tea_tools_kintsugi')} for mended bowls.</li>
      <li><strong>Whisk (<em>chasen</em>):</strong> Takayama tea whisks are made in Ikoma, Nara Prefecture. The craft's own page says the tradition goes back to the mid-Muromachi period, when the son of the Takayama lord is said to have made one for Murata Juko. Read more at <a href="https://kougeihin.jp/en/craft/0625/" target="_blank" rel="noopener" onclick="trackEvent('click','external','tea_takayama_chasen')">Kougeihin: Takayama Chasen</a>.</li>
      <li><strong>Tea caddy (<em>chazutsu</em>):</strong> Kaikado, in Kyoto, has made handmade tea caddies in tin, copper and brass since 1875, working from the same atelier for nearly 140 years according to <a href="https://www.jetro.go.jp/en/mjcompany/kaikado.html" target="_blank" rel="noopener" onclick="trackEvent('click','external','tea_kaikado')">JETRO's profile</a>.</li>
      <li><strong>Kettle (<em>kama</em>):</strong> our {link('/guides/nambu-tekki/','Nambu Tekki guide','tea_tools_nambu')} covers the iron-casting tradition of northern Japan. Note that it is about the iron kettle for the kitchen (<em>tetsubin</em>); a tea-ceremony kettle is its own type, so read it as background on iron casting, not a buying guide for a <em>kama</em>.</li>
    </ul>

    <h2 id="try">Trying It in Japan<span class="h2-jp">体験するには</span></h2>
    <p>There are three easy routes. First, <strong>garden tea houses</strong> such as the Hamarikyu Gardens in Tokyo, where you can sit with a bowl and a sweet and look at the water. Second, <strong>temples</strong>, where tea is sometimes served to visitors as part of a visit. Third, <strong>short guided sessions</strong> arranged in English, which are the best choice if you want an explanation of each step. I have not checked specific schedules or prices, so please read each listing for the language, the length, and whether chairs are offered.</p>
    <p>Practical points that hosts often ask of guests: wear clean socks, avoid strong perfume, and take off rings and watches that could knock a delicate bowl. If kneeling is difficult, tell the host in advance. If you like the idea of a quieter tea experience, pair it with a temple visit, for example one of the places in our {link('/guides/best-shrines-kyoto/','guide to Kyoto shrines','tea_to_best_shrines_kyoto')}.</p>
    <div style="background:var(--washi-dark);border-left:4px solid var(--kin);padding:16px 20px;margin:24px 0;border-radius:2px;">
      <p style="margin:0;">&#127861; <strong>Plan your trip:</strong> Browse tea ceremony experiences, or find a stay in Kyoto. <a href="{VI}" target="_blank" rel="noopener sponsored" onclick="trackEvent('click','affiliate','viator_tea_ceremony_local')">Browse tea ceremony experiences on Viator</a> &middot; <a href="{EX}" target="_blank" rel="noopener sponsored" onclick="trackEvent('click','affiliate','expedia_tea_ceremony_local')">Find stays in Kyoto</a></p>
    </div>

    <h2 id="faq">Frequently Asked Questions<span class="h2-jp">よくあるご質問</span></h2>

    <div class="faq-stack">

{faq_html}    </div>

    <h2 id="final">Final Thoughts<span class="h2-jp">むすびに</span></h2>
    <p>The tea ceremony is easy to over-explain and hard to describe. What stays with visitors is rarely the rules. It is the quiet, the sweetness followed by bitterness, and the feeling that someone prepared one bowl just for you.</p>
    <p>If you enjoy the tea, look for the bowls too. The same attention to humble, imperfect objects appears in the repair art of {link('/guides/kintsugi/','kintsugi','tea_to_kintsugi')} and in Japan's ceramic traditions such as {link('/guides/bizen-ware/','Bizen ware','tea_to_bizen')}.</p>

    <div class="closing-block">
      <span class="torii">🍵</span>
      <p>One bowl, one moment, offered with care.</p>
    </div>

    <section class="related-section">
      <h2>Related Guides</h2>
      <span class="h2-jp">関連ガイド</span>
      <div class="related-grid">
        <a class="related-card" href="/guides/kintsugi/" onclick="trackEvent('click','internal','related_tea_to_kintsugi')">
          <div class="related-card-label">SACRED JAPAN ／ GUIDE</div>
          <div class="related-card-title">🏺 Kintsugi: The Art of Golden Repair →</div>
          <div class="related-card-desc">How broken tea bowls and dishes are repaired with lacquer and gold.</div>
        </a>
        <a class="related-card" href="/guides/bizen-ware/" onclick="trackEvent('click','internal','related_tea_to_bizen')">
          <div class="related-card-label">SACRED JAPAN ／ GUIDE</div>
          <div class="related-card-title">🏺 Bizen Ware →</div>
          <div class="related-card-desc">Unglazed pottery from Okayama, prized for its earthy character.</div>
        </a>
        <a class="related-card" href="/culture/shrine-etiquette/" onclick="trackEvent('click','internal','related_tea_to_etiquette')">
          <div class="related-card-label">SACRED JAPAN ／ GUIDE</div>
          <div class="related-card-title">⛩️ Shrine Etiquette →</div>
          <div class="related-card-desc">Manners for a shrine visit, in the same spirit of quiet attention.</div>
        </a>
        <a class="related-card" href="/guides/temple-stay/" onclick="trackEvent('click','internal','related_tea_to_temple_stay')">
          <div class="related-card-label">SACRED JAPAN ／ GUIDE</div>
          <div class="related-card-title">🏯 Temple Stays →</div>
          <div class="related-card-desc">Sleep and eat in a working temple, where tea and Zen practice are close by.</div>
        </a>
      </div>
    </section>

    <p style="font-size:14px;color:var(--enshu);line-height:1.7;margin-top:32px;"><strong>Sources:</strong> history and etiquette points are drawn from <a href="https://en.wikipedia.org/wiki/Japanese_tea_ceremony" target="_blank" rel="noopener" style="color:var(--enshu);">Wikipedia: Japanese tea ceremony</a>, <a href="https://en.wikipedia.org/wiki/Kobori_Ensh%C5%AB" target="_blank" rel="noopener" style="color:var(--enshu);">Kobori Enshu</a> and <a href="https://en.wikipedia.org/wiki/Sen_no_Riky%C5%AB" target="_blank" rel="noopener" style="color:var(--enshu);">Sen no Rikyu</a>. The doors and sword rack: <a href="https://projects.mcah.columbia.edu/jaanus/record/nijiriguchi" target="_blank" rel="noopener" style="color:var(--enshu);">JAANUS, nijiriguchi</a>, <a href="https://japanpastandpresent.org/en/projects/teaching-tea-culture-history-practice-art/pedagogy/tea-architecture-terminology" target="_blank" rel="noopener" style="color:var(--enshu);">Japan Past and Present, tea architecture terminology</a> and <a href="https://teaceremony-kyoto.com/?p=716" target="_blank" rel="noopener" style="color:var(--enshu);">Tea Ceremony Koto</a> (a tea-school blog, one source). Tea and the warlords: <a href="https://chano-yu.com/samurais-tea-culture/" target="_blank" rel="noopener" style="color:var(--enshu);">chano-yu.com</a> (single-source anecdotes), <a href="https://ec.yamamotoyama.co.jp/en/blogs/column/reading287" target="_blank" rel="noopener" style="color:var(--enshu);">Yamamotoyama</a> and <a href="https://de.yunomi.life/blogs/ocha/tea-ceremony-politics" target="_blank" rel="noopener" style="color:var(--enshu);">Yunomi</a>. Details such as the turn of the bowl vary by school, so follow your host.</p>

  </article>

</main>'''

s=open(f'{R}/culture/omamori-guide/index.html',encoding='utf-8').read()
a=s.index('<!-- ── PRIMARY SEO'); b=s.index('<!-- ── STRUCTURED DATA: Article')
head=f'''<!-- ── PRIMARY SEO ── -->
<title>{TITLE} | Sacred Japan</title>
<meta name="description" content="{DESC}">
<meta name="keywords" content="Japanese tea ceremony, chanoyu, chado, sado, matcha ceremony, tea ceremony etiquette, Sen no Rikyu, Kobori Enshu, nijiriguchi, kininguchi, tea room, tea ceremony Kyoto, tea ceremony Tokyo">
<meta name="author" content="Sacred Japan">
<link rel="canonical" href="{URL}">
<link rel="alternate" hreflang="en" href="{URL}">
<meta name="robots" content="index, follow">

<!-- ── OPEN GRAPH ── -->
<meta property="og:type" content="article">
<meta property="og:url" content="{URL}">
<meta property="og:title" content="{TITLE}">
<meta property="og:description" content="{DESC}">
<meta property="og:image" content="{OG}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:site_name" content="Sacred Japan">
<meta property="og:locale" content="en_US">

<!-- ── TWITTER CARD ── -->
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:site" content="@sacredjapan">
<meta name="twitter:title" content="{TITLE}">
<meta name="twitter:description" content="{DESC}">
<meta name="twitter:image" content="{OG}">

'''
s=s[:a]+head+s[b:]
# JSON-LD replacements
a=s.index('<!-- ── STRUCTURED DATA: Article'); b=s.index('<!-- ── STRUCTURED DATA: BreadcrumbList')
art={"@context":"https://schema.org","@type":"Article","headline":TITLE,"description":DESC,"url":URL,"image":OG,"inLanguage":"en","datePublished":"2026-11-08","dateModified":"2026-11-08",
 "author":{"@type":"Organization","name":"Sacred Japan","url":"https://sacred-japan.net","description":"Sacred Japan is run by a Japanese national licensed by the government as a National Tour Guide (English), specializing in art and culture."},
 "publisher":{"@type":"Organization","name":"Sacred Japan","url":"https://sacred-japan.net","logo":{"@type":"ImageObject","url":"https://sacred-japan.net/images/logo-512.png"}}}
s=s[:a]+'<!-- ── STRUCTURED DATA: Article ── -->\n<script type="application/ld+json">\n'+json.dumps(art,ensure_ascii=False,indent=2)+'\n</script>\n\n'+s[b:]
s=s.replace('{"@type":"ListItem","position":3,"name":"Omamori Guide","item":"https://sacred-japan.net/culture/omamori-guide/"}',f'{{"@type":"ListItem","position":3,"name":"Tea Ceremony Guide","item":"{URL}"}}')
a=s.index('<!-- ── STRUCTURED DATA: FAQPage'); b=s.index('</script>',a)+len('</script>')
s=s[:a]+'<!-- ── STRUCTURED DATA: FAQPage ── -->\n<script type="application/ld+json">\n'+faq_ld+'\n</script>'+s[b:]
# hero + breadcrumb + main
a=s.index('<section class="hero">'); b=s.index('</main>')+len('</main>')
hero='''<section class="hero">
  <div class="hero-bg-kanji">茶道</div>
  <div class="hero-content">
    <div class="hero-label">SACRED JAPAN GUIDES ／ 文化ガイド</div>
    <h1>The Japanese <em>Tea Ceremony</em> Guide</h1>
    <div class="hero-jp">茶道ガイド</div>
    <p class="hero-subtitle">What Happens, What to Do as a Guest, and Where to Try It</p>
    <div class="hero-author">
      WRITTEN BY <strong>SACRED JAPAN</strong> ／ LICENSED NATIONAL TOUR GUIDE (ENGLISH)
    </div>
  </div>
</section>

<!-- ── BREADCRUMB ── -->
<div role="navigation" aria-label="Breadcrumb" style="max-width:900px;margin:24px auto 0;padding:0 56px;font-size:15px;letter-spacing:0.5px;color:var(--sumi);">
  <a href="/" style="color:var(--sumi-light);text-decoration:underline;text-underline-offset:3px;" onclick="trackEvent('click','internal','guide_tea_to_home')">Home</a>
  <span style="margin:0 8px;color:var(--enshu);">›</span>
  <a href="/culture/" style="color:var(--sumi-light);text-decoration:underline;text-underline-offset:3px;" onclick="trackEvent('click','internal','guide_tea_to_culture_hub')">Culture</a>
  <span style="margin:0 8px;color:var(--enshu);">›</span>
  Tea Ceremony Guide
</div>

<!-- ── MAIN ── -->
'''
s=s[:a]+hero+main+s[b:]
s=s.replace('viator_guide_omamori_sticky','viator_guide_tea_sticky').replace('https://www.viator.com/Japan/d334-ttd?','https://www.viator.com/search/japanese+tea+ceremony?')
s=s.replace('guide_omamori','guide_tea')
open(f'{OUT}/index.html','w',encoding='utf-8').write(s)
print(len(s))
