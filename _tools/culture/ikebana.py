import re, os, json
from PIL import Image
R='/home/claude/sacred-japan'
A='/mnt/user-data/attachments/fd332c08-3f6b-545a-883b-83277e19ff52/'
S='ikebana'
OUT=f'{R}/culture/{S}'
os.makedirs(OUT+'/images',exist_ok=True)
photos={ # key: (file, maxwidth, crop)
 'gold-screen':('526db485-image.jpg',1200,None),
 'quince-alcove':('9588b1df-image.jpg',1200,None),
 'hidasuki-vase':('040115f3-image.jpg',1200,None),
 'shelf-orchid':('d001d08d-image.jpg',1200,None),
 'shelf-pillar':('f8d850d0-image.jpg',1200,None),
 'gallery-piece':('feadcbd3-image.jpg',1000,None),
 'black-cabinet':('dd3870d0-image.jpg',900,None),
 'exhibition-room':('477348a0-image.jpg',1200,(0,0,2200,1319)),
}
U='/mnt/user-data/uploads/'
photos.update({
 'home-tools':('59a998e1-image.jpg',1200,None),
 'home-hands':('4dc0c549-image.jpg',1200,None),
})
for k,(f,mw,crop) in photos.items():
    src=U+f if k.startswith('home-') else A+f
    if not os.path.exists(src): continue
    im=Image.open(src).convert('RGB')
    if crop: im=im.crop(crop)
    w,h=im.size
    if w>mw: im=im.resize((mw,round(h*mw/w)),Image.LANCZOS)
    im.save(f'{OUT}/images/{k}.jpg',quality=84,optimize=True); im.save(f'{OUT}/images/{k}.webp',quality=80)

def fig(k,alt,cap,credit,hero=False,maxw=760,pos=None):
    st='margin:0 0 48px;' if hero else f'margin:36px auto;max-width:{maxw}px;'
    op=f'object-position:{pos};' if pos else ''
    img_st=f'width:100%;max-height:420px;object-fit:cover;{op}border-radius:4px;display:block;' if hero else 'width:100%;height:auto;border-radius:4px;display:block;'
    ld='eager' if hero else 'lazy'
    return f'''<figure style="{st}">
      <picture><source srcset="/culture/{S}/images/{k}.webp" type="image/webp"><img src="/culture/{S}/images/{k}.jpg" alt="{alt}" loading="{ld}" style="{img_st}"></picture>
      <figcaption style="font-size:13px;color:var(--enshu);margin-top:10px;text-align:center;line-height:1.6;">{cap}<br>{credit}</figcaption>
    </figure>'''
CC0='<a href="https://creativecommons.org/publicdomain/zero/1.0/" target="_blank" rel="noopener" style="color:var(--enshu);">CC0</a>'
GRY='<a href="https://commons.wikimedia.org/wiki/User:Gryffindor" target="_blank" rel="noopener" style="color:var(--enshu);">Gryffindor</a>'
HK='<a href="https://creativecommons.org/licenses/by-sa/4.0/" target="_blank" rel="noopener" style="color:var(--enshu);">CC BY-SA 4.0</a>'
def crh(date): return f'Photo: Henry Kellner, {HK}, {date}, via Wikimedia Commons (resized)'
def cr(date,extra=''): return f'Photo: {GRY}, {CC0}, {date}{extra}, via Wikimedia Commons (resized)'

f_gold=fig('gold-screen','A tall arrangement of white-painted bare branches, orange flowers and red berries in a rugged blue-grey vase, in front of a gold folding screen on a red carpet','A large arrangement in front of a gold screen, shown at the Meguro Gajoen exhibition.',cr('13 November 2018'),hero=True,pos='50% 34%')
f_quince=fig('quince-alcove','An alcove with a broad-leaved plant in a bronze trough on the left and thorny branches with orange and white blossoms in a brown vase on the right','Two arrangements in one alcove, with the branch shadows thrown on the wall.',cr('13 November 2018'),maxw=760)
f_hid=fig('hidasuki-vase','A cream vase streaked with orange-red lines holding a long arching branch of red berries and small yellow flowers, on a black lacquer board with a round lid beside it','An arrangement in a water jar with red streaks, from the Saga Go-ryu.',cr('13 November 2018'))
f_orch=fig('shelf-orchid','Staggered wooden shelves holding a pink-and-white orchid with pine in an ornate yellow vessel, a small pine bonsai in a green dish, and a dark stone on a stand','Small works on staggered shelves, with gold-leaf doors below.',cr('13 November 2018'))
f_pill=fig('shelf-pillar','A shelf unit with several small arrangements, among them yellow chrysanthemums in a deep red vase, beside a carved wooden pillar and a green bamboo bar on the floor','Several small arrangements on one shelf unit beside a carved pillar.',cr('13 November 2018'))
f_gal=fig('gallery-piece','A tall arrangement of red berries, white chrysanthemums, maple-like leaves and curved bamboo strips in two vases, one of them woven bamboo, on a white plinth','A modern piece in a gallery, from the Shinsei-ryu.',cr('4 November 2018'),maxw=640)
f_cab=fig('black-cabinet','A colorful porcelain vase on a carved stand holding purple and dark red orchids and pine branches, on a black lacquer cabinet inlaid with birds and flowers, in front of a dark wooden lattice','Orchids and pine in a painted vase on a lacquer cabinet.',cr('13 November 2018'),maxw=420)
f_room=fig('exhibition-room','A tatami room with fan-shaped flower paintings along the upper walls, carved log pillars, several alcoves with flower arrangements, and green bamboo bars laid on the floor','A wide view of the exhibition room, with arrangements in the alcoves and bamboo bars on the floor (cropped at the right edge).',cr('13 November 2018'))

f_tools=fig('home-tools','A wooden table with three bowls (pale grey, brown-glazed and black on a foot), a round pin holder, a cup of water, a leafy branch with buds, and red-handled shears on a white cloth','The basic kit laid out: three bowls, a pin holder, water, a branch and shears.',crh('3 November 2017'))
f_hands=fig('home-hands','Two hands pressing the stem of a cream-and-peach rose onto a pin holder in a brown bowl, beside a leafy branch already standing upright, with shears on a white cloth and fallen leaves on the table','Adding a rose to the pin holder after the branch is in place.',crh('3 November 2017'))

def link(href,txt,lab): return f'<a href="{href}" class="inline-link" onclick="trackEvent(\'click\',\'internal\',\'{lab}\')">{txt}</a>'
def ext(href,txt,lab): return f'<a href="{href}" target="_blank" rel="noopener" onclick="trackEvent(\'click\',\'external\',\'{lab}\')">{txt}</a>'
VI='https://www.viator.com/search/ikebana?pid=P00298374&amp;mcid=42383&amp;medium=link&amp;campaign=sacred-japan'
EX='https://expedia.com/affiliate?siteid=1&amp;landingPage=https%3A%2F%2Fwww.expedia.co.jp%2FHotel-Search%3Fdestination%3DKyoto&amp;camref=1101l5JmFa&amp;creativeref=1011l87782&amp;adref=PZf6lQ77e8'

faqs=[
("What is ikebana?","Ikebana (生け花) is the Japanese art of arranging flowers, branches, leaves and berries. It is also called kado (華道), the way of flowers. It grew out of flower offerings made at Buddhist altars and is now taught by many schools."),
("Is ikebana the same as flower arranging in the West?","Not quite. A Western bouquet is usually about fullness. Ikebana usually works with line, space, the container and seasonal material, and a good arrangement often looks as much like a drawing as a bouquet. The photographs in this guide show the range, from a huge branch display to a single branch of berries."),
("What do heaven, human and earth mean in ikebana?","In some arrangements the main stems form a scalene triangle of three points that stand for heaven, human and earth (or sun, moon and earth). In the seika style they are called ten, chi and jin. Not every school or style uses this."),
("How is ikebana related to the tea ceremony?","Both belong to the alcove (tokonoma) tradition, and the flowers used in a tea room are called chabana. Wikipedia describes chabana as separate from ikebana, but notes that its simplicity helped create the nageire style."),
("Do I need experience to try a lesson?","The visitor trial lesson that Ikenobo lists on its English page is aimed at visitors and offers a guide in English or Chinese. The page does not state any experience requirement. Please check the current details before you book."),
("What do I need to try ikebana at home?","The photographs in this guide show a simple setup: a bowl, a pin holder (kenzan) to hold the stems, water, sharp shears, a cloth and a branch or two. Schools differ in their tools and rules, so a lesson is the best way to learn the forms."),
("Where can I see ikebana without taking a lesson?","Exhibitions are the easiest way. The photographs in this guide were taken at exhibitions at Meguro Gajoen in Tokyo and in Nagoya in 2018. Those were temporary shows, so check what is on when you travel.")]
faq_html=''.join(f'''      <details class="faq-item">
        <summary>{q}</summary>
        <div class="faq-answer">{a}</div>
      </details>

''' for q,a in faqs)
faq_ld=json.dumps({"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in faqs]},ensure_ascii=False,indent=2)

TITLE="Ikebana Guide: Japanese Flower Arranging, Its Schools and Where to Try It"
DESC="A licensed guide's English introduction to ikebana, Japanese flower arranging: its history from temple offerings, the main schools, how to look at an arrangement, and where to see and try it, with photographs from real exhibitions."
URL=f"https://sacred-japan.net/culture/{S}/"
OG="https://sacred-japan.net/images/og/og-culture-ikebana.jpg"
WIKI='<a href="https://en.wikipedia.org/wiki/Ikebana" target="_blank" rel="noopener" style="color:var(--enshu);">Wikipedia: Ikebana</a>'

main=f'''<main>

  {f_gold}

  <!-- TABLE OF CONTENTS -->
  <aside class="toc" aria-label="Table of contents">
    <div class="toc-label">TABLE OF CONTENTS ／ 目次</div>
    <div class="toc-title">In This Guide</div>
    <ol>
      <li><a href="#opening">Opening: A Note from the Guide</a></li>
      <li><a href="#what">What Ikebana Is</a></li>
      <li><a href="#history">A Short History</a></li>
      <li><a href="#tea">Tea, the Alcove and the Flower</a></li>
      <li><a href="#schools">The Schools</a></li>
      <li><a href="#look">Seven Arrangements to Look At</a></li>
      <li><a href="#how">How to Look at an Arrangement</a></li>
      <li><a href="#home">Try It at Home: The Basic Kit</a></li>
      <li><a href="#try">Where to See and Try Ikebana</a></li>
      <li><a href="#faq">Frequently Asked Questions</a></li>
      <li><a href="#final">Final Thoughts</a></li>
    </ol>
  </aside>

  <article>

    <section id="opening">
      <p class="opening">When travelers ask me about ikebana, they usually expect a bouquet. What they find is closer to a drawing made with plants: a few branches, a container chosen with care, and a lot of empty space around them.</p>
      <p>As a licensed guide, I think ikebana is one of the easiest ways to understand how Japanese taste works. You do not need to read a word of Japanese to enjoy it. You only need to learn what to look at. This guide shows you, using photographs from real exhibitions.</p>
    </section>

    <h2 id="what">What Ikebana Is<span class="h2-jp">生け花とは</span></h2>
    <p>Ikebana (<span class="jp">生け花</span>) is often translated as "making flowers live." It is also called <em>kado</em> (<span class="jp">華道</span>), "the way of flowers." Arrangements use flowers, but also bare branches, leaves, berries and grasses, and the container is part of the design.</p>
    <p>The roots are religious. {WIKI} describes how ancient Japanese decorated evergreen trees with flowers as <em>yorishiro</em>, objects that invite the gods, and how Buddhism later made flower offerings at altars common.</p>
    <p>Some arrangements are built on three main points, a scalene triangle that stands for heaven, human and earth. Others, like the huge piece at the top of this page, ignore that structure and use the whole room.</p>

    <h2 id="history">A Short History<span class="h2-jp">生け花の歴史</span></h2>
    <ul>
      <li><strong>Ancient times:</strong> evergreens decorated with flowers are used as <em>yorishiro</em> to invite the gods.</li>
      <li><strong>Buddhist altars:</strong> flower offerings spread. The Ikenobo school traces its beginnings to the Rokkaku-do temple in Kyoto, said to have been built in 587 by Prince Shotoku.</li>
      <li><strong>Mid-1400s:</strong> the <em>rikka</em> ("standing flowers") style takes shape, a Buddhist expression of landscape beauty built around nine branches.</li>
      <li><strong>1500s:</strong> <em>nageire</em> ("thrown-in flowers"), a looser style, becomes independent.</li>
      <li><strong>Edo period:</strong> nageire is formalized into <em>shoka</em> for the tokonoma alcove. The fixed-model <em>seika</em> style develops after the 1780s, with three main parts: ten (heaven), chi (earth) and jin (human).</li>
      <li><strong>1895:</strong> Ohara Unshin founds the Ohara school.</li>
      <li><strong>1927:</strong> Teshigahara Sofu founds the Sogetsu school.</li>
    </ul>

    <h2 id="tea">Tea, the Alcove and the Flower<span class="h2-jp">茶室と花</span></h2>
    <p>If you have read our {link('/culture/tea-ceremony/','tea ceremony guide','ikebana_to_tea')}, you know the alcove, the <em>tokonoma</em>: the place of honor in a tea room, where a hanging scroll and a few flowers are set out. Arrangements were made for exactly this space. The flowers used in a tea room are called <em>chabana</em>. {WIKI} treats chabana as separate from ikebana, but says its simplicity helped create the nageire style.</p>
    {f_hid}
    <p>This photograph connects the two arts. Commons describes it as an arrangement in a <em>mizusashi</em>, the water jar that a tea host uses, with <em>hidasuki</em> markings, the red streaks left on the clay in firing. It is from the Saga Go-ryu, in a room called the Seisui no ma. A long branch of red hips arches across the picture, and a few small yellow flowers, which look like chrysanthemums to me, sit low in the jar. The round lid stands beside the jar, as it would in a tea room. Notice the shadow: the branch is drawn twice, once in the air and once on the wall.</p>

    <h2 id="schools">The Schools<span class="h2-jp">流派</span></h2>
    <p>Ikebana is taught by many schools, each with its own forms and vocabulary. Three names you will meet often are <strong>Ikenobo</strong>, the school tied to the Rokkaku-do temple in Kyoto, <strong>Ohara</strong> (founded 1895) and <strong>Sogetsu</strong> (founded 1927).</p>
    <p>The photographs below come mostly from an exhibition in November 2018 at Meguro Gajoen in Tokyo. According to the Commons descriptions, 57 schools belonging to the Japan Ikebana Art Association showed their work there, in exhibitions that changed weekly, from traditional arrangements with autumn flowers and fruit to free-style pieces that used a whole room. The school names in the captions come from those descriptions.</p>

    <h2 id="look">Seven Arrangements to Look At<span class="h2-jp">作品を見る</span></h2>

    <h3>Big and Bold: Branches Against Gold</h3>
    <p>The photograph at the top of this page is a large arrangement from the Shozan Enshu-ryu, shown in a room called the Kiyokata no ma, according to Commons. Bare branches painted white fan out wide, with orange flowers that look like bird-of-paradise and red-orange berries on long dark branches reaching out to the sides. The vase is tall, rough and blue-grey. Behind it stands a gold-leaf folding screen, and the branches throw their shadows across it. On the red carpet lie a green fruit and a few fallen leaves, which I read as part of the composition. The name card in front appears to read the maker's name, 西崎一梨, under the school name.</p>

    <h3>Spring Blossoms in an Alcove</h3>
    {f_quince}
    <p>This is from the Senke Koryu Fuyokai, also in the Kiyokata no ma, per Commons. In one alcove there are two arrangements. On the left, a spiky, pale-edged green plant sits in a bronze trough on a black lacquer stand. On the right, thorny bare branches carry orange-red and white blossoms, which look to me like flowering quince, in a brown vase on a lacquer tray. Look at the right side of the wall: the shadow of the thorny branches is as much part of the picture as the blossoms.</p>

    <h3>Shelves and Small Worlds</h3>
    {f_orch}
    <p>Traditional rooms have staggered shelves, and ikebana fills them with small works. I match this photograph, by its thumbnail, to Commons' entry for the Ohara-ryu in the Chojo no ma, the top-floor room. On the upper shelf at left, a pink-and-white orchid and pine sit in an ornate yellow vessel. At right, a small pine bonsai grows in a shallow green dish, next to a dark stone on a carved stand. A curved dark object on a lacquer tray at lower left is something I cannot identify. Gold-leaf sliding doors fill the bottom.</p>
    {f_pill}
    <p>Here several small arrangements share one shelf unit. I match it by thumbnail to the Saga Go-ryu's smaller arrangements in the Seisui no ma. A trailing green plant with small yellow flowers sits in an olive-glazed trough. Yellow chrysanthemums with red-green leaves rest in a deep red vase. A slim white vase holds pink-purple flowers. To the right is a pillar carved to look like a rough trunk. The green bamboo bar on the floor is, I take it, a simple barrier that keeps visitors back, though I have not seen a caption that says so.</p>

    <h3>A Modern Gallery Piece</h3>
    {f_gal}
    <p>Not every arrangement lives in an alcove. Commons says this one is from the Shinsei-ryu by Nishikawa Suishun, shown at the Nagoya Ikebana Art Exhibition in the Citizens' Gallery Sakae, in November 2018. The name card on the plinth reads 真生流. Two vases stand side by side, one cream and one woven bamboo, and curved bamboo strips sweep around them. Red and orange berries, white spider chrysanthemums, maple-like leaves and grey-green hydrangea heads fill the space. It reads as an autumn piece.</p>

    <h3>Flowers Against Black Lacquer</h3>
    {f_cab}
    <p>Orchids and pine make an unusual pair here. Spikes of purple and dark red orchids rise from a colorful painted porcelain vase on a carved stand, with pine branches reaching out on both sides. The vase sits on a black lacquer cabinet inlaid with birds and flowers, one of which looks like a pheasant. Behind is a dark wooden lattice. I could not match this photograph to its Commons description with certainty, so I do not name the school here.</p>

    <h3>The Whole Room</h3>
    {f_room}
    <p>Stepping back, you see how the arrangements and the building work together: fan-shaped flower paintings along the upper walls, carved log pillars, gold-leaf doors, and a different arrangement in every alcove. The green bamboo bars laid along the floor look like markers that keep visitors back from the alcoves. The Commons description for this file was cut off on my screen, so I do not name the room, but the pillars and shelves look like those in the shelf photograph above.</p>

    <h2 id="how">How to Look at an Arrangement<span class="h2-jp">鑑賞のコツ</span></h2>
    <p>These are my own habits as a guide, not rules from a school.</p>
    <ol>
      <li><strong>Find the longest line.</strong> Follow the main branch from the vase to its tip. Most arrangements are built around it.</li>
      <li><strong>Look at the container.</strong> It is chosen as carefully as the flowers, as with the red-streaked water jar earlier.</li>
      <li><strong>Notice what is left out.</strong> The empty space around the branches is part of the design.</li>
      <li><strong>Look at the shadow.</strong> In several photographs here, the shadow on the wall is half the picture.</li>
      <li><strong>Read the name card.</strong> It usually gives the school and the maker. You can see one in the photographs of the gold screen and the gallery piece.</li>
    </ol>

    <h2 id="home">Try It at Home: The Basic Kit<span class="h2-jp">用具と生け方</span></h2>
    <p>Not every arrangement needs a gallery. These two photographs by Henry Kellner show a simple home setup. Commons describes both only as "Ikebana", so I treat them as a demonstration of the basic method and do not attach them to any school.</p>
    {f_tools}
    <p>Here is the kit laid out on a pale wooden table. Along the top are three bowls: a pale grey one, a brown one with a green-edged glaze, and a black one on a small foot. In front of them sits a round <strong>pin holder</strong>, called a <em>kenzan</em> in Japanese, a dense bed of metal pins that holds stems upright. To its right are a clear cup of water and a pair of red-handled shears resting on a white cloth. The branch lying across the middle, with leaves and small buds, is the raw material. Choosing which bowl suits the branch is the first decision.</p>
    {f_hands}
    <p>In the second photograph the work has started. The pin holder sits in the brown bowl with a little water, and the leafy branch already stands on the pins. Two hands are pressing the stem of a cream-and-peach rose onto them, with a small bud on a short side stem still to place. The shears and cloth are within reach at the upper right, and cut leaves and a few petals lie on the table. This is what I mean by looking at the line: the tall branch sets the line, and the rose is added low and close to it.</p>

    <h2 id="try">Where to See and Try Ikebana<span class="h2-jp">鑑賞・体験するには</span></h2>
    <h3>Meguro Gajoen's Hyakudan Kaidan, Tokyo</h3>
    <p>Most of the photographs above were taken in the Hyakudan Kaidan ("hundred-step staircase") at Meguro Gajoen. {ext('https://en.japantravel.com/tokyo/meguro-gajoen-and-the-hyakudan-kaidan/60386','Japan Travel','ikebana_japantravel_gajoen')} says it was built as a wedding hall in the 1930s, is registered as a Tangible Cultural Asset of Tokyo, and has 99 wooden steps and seven function rooms. A recent {ext('https://www.timeout.com/tokyo/news/the-extravagant-hyakudan-kaidan-in-meguro-has-reopened-after-a-yearlong-closure-101626','Time Out Tokyo','ikebana_timeout_gajoen')} report says it reopened on October 1 after a year-long closure, with daytime tickets from ¥1,800. Please check the official site before you go, because prices, hours and exhibitions change. The ikebana exhibition in my photographs was a temporary event in 2018, so do not expect to find those arrangements today.</p>
    <h3>Lessons in Kyoto</h3>
    <p>Ikenobo's English page lists an {ext('https://www.ikenobo.jp/english/lesson','ikebana trial lesson for visitors','ikebana_ikenobo_lesson')} at the Rokkaku-do temple: Thursdays from 13:30 to 15:30 except national holidays, with a guide in English or Chinese, ¥7,000 per person, for groups of 2 to 10, booked by email. These details were on the page when I checked, so please confirm them. {ext('https://kyoto.travel/en/see-and-do/experience_firsthand_traditional_ikebana.html','Kyoto Travel','ikebana_kyoto_travel')} also describes a lesson with an Ikenobo instructor at Sakura Japanese Cultural Experience near Nijo Castle, with English-speaking staff. It does not give a price or length.</p>
    <div style="background:var(--washi-dark);border-left:4px solid var(--kin);padding:16px 20px;margin:24px 0;border-radius:2px;">
      <p style="margin:0;">&#127802; <strong>Plan your trip:</strong> Browse ikebana experiences, or find a stay in Kyoto. <a href="{VI}" target="_blank" rel="noopener sponsored" onclick="trackEvent('click','affiliate','viator_ikebana_local')">Browse ikebana experiences on Viator</a> &middot; <a href="{EX}" target="_blank" rel="noopener sponsored" onclick="trackEvent('click','affiliate','expedia_ikebana_local')">Find stays in Kyoto</a></p>
    </div>

    <h2 id="faq">Frequently Asked Questions<span class="h2-jp">よくあるご質問</span></h2>

    <div class="faq-stack">

{faq_html}    </div>

    <h2 id="final">Final Thoughts<span class="h2-jp">むすびに</span></h2>
    <p>Ikebana asks you to slow down and look at a few things closely. A branch, a vase, a shadow on a wall: that is the whole lesson. If you enjoy it, pair it with a tea gathering, where the same alcove holds a scroll and a few flowers.</p>
    <p>The same attention to humble, imperfect objects appears in the repair art of {link('/guides/kintsugi/','kintsugi','ikebana_to_kintsugi')} and in pottery such as {link('/guides/bizen-ware/','Bizen ware','ikebana_to_bizen')}, whose clay is also used for vases.</p>

    <div class="closing-block">
      <span class="torii">🌸</span>
      <p>A few branches, a vase and the space between them.</p>
    </div>

    <section class="related-section">
      <h2>Related Guides</h2>
      <span class="h2-jp">関連ガイド</span>
      <div class="related-grid">
        <a class="related-card" href="/culture/tea-ceremony/" onclick="trackEvent('click','internal','related_ikebana_to_tea')">
          <div class="related-card-label">SACRED JAPAN ／ GUIDE</div>
          <div class="related-card-title">🍵 The Japanese Tea Ceremony Guide →</div>
          <div class="related-card-desc">The room, the small door and the alcove where the flowers sit.</div>
        </a>
        <a class="related-card" href="/guides/kintsugi/" onclick="trackEvent('click','internal','related_ikebana_to_kintsugi')">
          <div class="related-card-label">SACRED JAPAN ／ GUIDE</div>
          <div class="related-card-title">🏺 Kintsugi: The Art of Golden Repair →</div>
          <div class="related-card-desc">How broken bowls and dishes are repaired with lacquer and gold.</div>
        </a>
        <a class="related-card" href="/guides/bizen-ware/" onclick="trackEvent('click','internal','related_ikebana_to_bizen')">
          <div class="related-card-label">SACRED JAPAN ／ GUIDE</div>
          <div class="related-card-title">🏺 Bizen Ware →</div>
          <div class="related-card-desc">Unglazed pottery from Okayama, prized for its earthy character.</div>
        </a>
        <a class="related-card" href="/culture/shrine-etiquette/" onclick="trackEvent('click','internal','related_ikebana_to_etiquette')">
          <div class="related-card-label">SACRED JAPAN ／ GUIDE</div>
          <div class="related-card-title">⛩️ Shrine Etiquette →</div>
          <div class="related-card-desc">Manners for a shrine visit, in the same spirit of quiet attention.</div>
        </a>
      </div>
    </section>

    <p style="font-size:14px;color:var(--enshu);line-height:1.7;margin-top:32px;"><strong>Sources:</strong> history and styles are drawn from {WIKI}. Exhibition details, school names and room names come from the Wikimedia Commons descriptions of each photograph. Meguro Gajoen: <a href="https://en.japantravel.com/tokyo/meguro-gajoen-and-the-hyakudan-kaidan/60386" target="_blank" rel="noopener" style="color:var(--enshu);">Japan Travel</a> and <a href="https://www.timeout.com/tokyo/news/the-extravagant-hyakudan-kaidan-in-meguro-has-reopened-after-a-yearlong-closure-101626" target="_blank" rel="noopener" style="color:var(--enshu);">Time Out Tokyo</a>. Lessons: <a href="https://www.ikenobo.jp/english/lesson" target="_blank" rel="noopener" style="color:var(--enshu);">Ikenobo</a> and <a href="https://kyoto.travel/en/see-and-do/experience_firsthand_traditional_ikebana.html" target="_blank" rel="noopener" style="color:var(--enshu);">Kyoto Travel</a>. Prices and schedules change, so please confirm before you go.</p>

  </article>

</main>'''

# reuse the shared head/hero/tail builder from the tea guide script
t=open(f'{R}/_tools/culture/tea.py',encoding='utf-8').read()
tail=t[t.index("s=open(f'{R}/culture/omamori-guide"):]
tail=tail.replace('<div class="hero-bg-kanji">茶道</div>','<div class="hero-bg-kanji">華道</div>')
tail=tail.replace('<h1>The Japanese <em>Tea Ceremony</em> Guide</h1>','<h1>The Japanese Art of <em>Ikebana</em></h1>')
tail=tail.replace('<div class="hero-jp">茶道ガイド</div>','<div class="hero-jp">生け花・華道ガイド</div>')
tail=tail.replace('What Happens, What to Do as a Guest, and Where to Try It','History, Schools and Where to See and Try It')
tail=tail.replace('Tea Ceremony Guide','Ikebana Guide')
tail=tail.replace('guide_tea','guide_ikebana').replace('viator_guide_tea_sticky','viator_guide_ikebana_sticky').replace('japanese+tea+ceremony','ikebana+flower+arranging')
tail=re.sub(r'(<meta name="keywords" content=")[^"]*(")',r'\1Ikebana, Japanese flower arranging, kado, Ikenobo, Ohara, Sogetsu, rikka, chabana, ikebana lesson Kyoto, Meguro Gajoen\2',tail)
tail=tail.replace('"dateModified":"2026-11-08"','"dateModified":"2026-11-13"')
exec(tail)
