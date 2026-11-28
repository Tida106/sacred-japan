import sys
sys.path.insert(0, '/home/claude/sacred-japan/_tools/culture')
from shinobi_common import *

S = 'manga-anime-history'
TITLE = 'Manga & Anime History: From Choju-giga at Kozan-ji to Pokemon'
DESC = "A licensed guide's short history of manga and anime: the 12th-century Choju-giga scrolls at Kozan-ji in Kyoto, Hokusai Manga, Tezuka and Astro Boy, Shonen Jump, Ghibli and Pokemon, plus museums worth visiting."
KEYWORDS = 'manga history, anime history, Choju-giga, Kozan-ji, Hokusai Manga, Tezuka Osamu, Astro Boy, Weekly Shonen Jump, Studio Ghibli, Kyoto International Manga Museum, Tezuka Osamu Manga Museum, Mizuki Shigeru Road'

W_CJ = ext('https://en.wikipedia.org/wiki/Ch%C5%8Dj%C5%AB-jinbutsu-giga', 'Wikipedia (Choju-jinbutsu-giga)', 'manga_src_wiki_choju')
W_HM = ext('https://en.wikipedia.org/wiki/Hokusai_Manga', 'Wikipedia (Hokusai Manga)', 'manga_src_wiki_hokusai')
W_KR = ext('https://en.wikipedia.org/wiki/Kitazawa_Rakuten', 'Wikipedia (Kitazawa Rakuten)', 'manga_src_wiki_rakuten')
W_KS = ext('https://en.wikipedia.org/wiki/Kamishibai', 'Wikipedia (Kamishibai)', 'manga_src_wiki_kamishibai')
W_NT = ext('https://en.wikipedia.org/wiki/New_Treasure_Island', 'Wikipedia (New Treasure Island)', 'manga_src_wiki_shintakarajima')
W_HK = ext('https://en.wikipedia.org/wiki/Panda_and_the_Magic_Serpent', 'Wikipedia (Hakujaden)', 'manga_src_wiki_hakujaden')
W_AB = ext('https://en.wikipedia.org/wiki/Astro_Boy_(1963_TV_series)', 'Wikipedia (Astro Boy, 1963)', 'manga_src_wiki_astroboy')
W_SJ = ext('https://en.wikipedia.org/wiki/Weekly_Sh%C5%8Dnen_Jump', 'Wikipedia (Weekly Shonen Jump)', 'manga_src_wiki_jump')
W_GH = ext('https://en.wikipedia.org/wiki/Studio_Ghibli', 'Wikipedia (Studio Ghibli)', 'manga_src_wiki_ghibli')
W_SA = ext('https://en.wikipedia.org/wiki/Spirited_Away', 'Wikipedia (Spirited Away)', 'manga_src_wiki_spirited')
KMM = ext('https://www.kyotomm.jp/en/', 'the Kyoto International Manga Museum site', 'manga_src_kyotomm')
KOZ = ext('https://www.kosanji.com/', 'Kozan-ji', 'manga_src_kozanji')
TZK = ext('https://www.city.takarazuka.hyogo.jp/tezuka/', 'the Takarazuka museum site', 'manga_src_tezuka')
GHM = ext('https://ghibli-museum.jp/en/ticket-information/', 'the Ghibli Museum ticket page', 'manga_src_ghibli_museum')
MZK = ext('https://www.gltjp.com/en/directory/item/12141/', 'GLTJP', 'manga_src_gltjp_mizuki')
MZ2 = ext('https://www.mlit.go.jp/tagengo-db/en/R2-01660.html', 'the MLIT multilingual database', 'manga_src_mlit_mizuki')
VI = viator('Kyoto+manga+anime+tour')

faqs = [
 ("What is the oldest manga in Japan?",
  f"There is no single agreed answer, because it depends on how you define manga. The most common starting point is the Choju-jinbutsu-giga (the \"frolicking animals\" scrolls) kept at Kozan-ji in Kyoto, in which rabbits, frogs and monkeys act like people. {W_CJ} dates them to the 12th and 13th centuries, though some popular sources give a slightly earlier range."),
 ("Who invented the word manga?",
  f"The word was in use in the Edo period. Hokusai's sketchbooks, titled Hokusai Manga from 1814, helped spread it ({W_HM}), and cartoonists such as Kitazawa Rakuten used it for satirical comics in the early 1900s ({W_KR})."),
 ("Why is Osamu Tezuka called the god of manga?",
  f"He drew the hit New Treasure Island in 1947 ({W_NT}), built a cinematic style of panel layout, and later produced Astro Boy, which began on television on 1 January 1963 ({W_AB}). Many later artists say they grew up on his work."),
 ("Was Astro Boy the first anime?",
  "No. Animated films existed in Japan decades earlier, and Toei's Hakujaden (1958) was a feature in color. Astro Boy is usually described as the first long-running, popular weekly TV anime series, which is the safer claim."),
 ("Can I see the Choju-giga scrolls in person?",
  f"The scrolls are National Treasures and are rarely on public display, and when they are shown it is usually in museum exhibitions. {KOZ} is a working temple in the mountains north-west of Kyoto, so check its own site for what visitors can see on the day."),
 ("Which museum is best for a first visit?",
  f"For history, the Kyoto International Manga Museum ({KMM}) is a good start, since it holds a large archive of manga. For one artist, the Osamu Tezuka Manga Museum in Takarazuka ({TZK}) is the classic choice. The Ghibli Museum in Mitaka is reservation-only ({GHM}), so book ahead."),
]
faq_html, faq_ld = faq_blocks(faqs)

fig = make_fig(S)
PD = 'Public domain (old work), via Wikimedia Commons (resized)'
_PH = {
    'kozanji': '/mnt/user-data/uploads/a4f6fec4-image.jpg',
    'choju-sumo': '/mnt/user-data/uploads/a7255900-image.jpg',
    'choju-sumo-close': '/mnt/user-data/uploads/384823c4-image.jpg',
    'choju-archery': '/mnt/user-data/uploads/85503c37-image.jpg',
    'choju-water': '/mnt/user-data/uploads/25b63b94-image.jpg',
    'choju-procession': '/mnt/user-data/uploads/f606d248-image.jpg',
    'hokusai-v8': '/mnt/user-data/uploads/dfd70b27-image.jpg',
    'hokusai-faces': '/mnt/user-data/uploads/81558a6d-image.jpg',
    'hokusai-swim': '/mnt/user-data/uploads/1f749ce3-image.jpg',
    'museum-building': '/mnt/user-data/uploads/5f5bd7eb-image.jpg',
    'museum-shelf': '/mnt/user-data/uploads/bde0bdcb-image.jpg',
    'yokai-space': '/mnt/user-data/uploads/08903e41-image.jpg',
}
copy_photos(S, {k: v for k, v in _PH.items() if os.path.exists(v) and not os.path.exists(f'{R}/culture/{S}/images/{k}.jpg')})

main = f'''<main>

  <aside class="toc" aria-label="Table of contents">
    <div class="toc-label">TABLE OF CONTENTS ／ 目次</div>
    <div class="toc-title">In This Guide</div>
    <ol>
      <li><a href="#opening">Opening: A Note from the Guide</a></li>
      <li><a href="#scrolls">The Scrolls at Kozan-ji</a></li>
      <li><a href="#edo">Hokusai and the Word Manga</a></li>
      <li><a href="#meiji">Satire, Magazines and Paper Theater</a></li>
      <li><a href="#tezuka">Tezuka, Toei and Astro Boy</a></li>
      <li><a href="#jump">Weekly Shonen Jump and the Boom</a></li>
      <li><a href="#global">Ghibli, Pokemon and the World</a></li>
      <li><a href="#visit">Where to Visit</a></li>
      <li><a href="#faq">Frequently Asked Questions</a></li>
      <li><a href="#final">Final Thoughts</a></li>
    </ol>
  </aside>

  <article>

    <section id="opening">
      <p class="opening">Some of the oldest comic art in Japan is kept in a mountain temple in Kyoto, and it stars a rabbit and a frog.</p>
      <p>As a licensed guide, I like to start manga and anime history at a temple, because it shows how long the habit of telling stories in pictures has lasted here. This page follows that thread from medieval scrolls to Pokemon in a few steps. The pictures here are old scrolls and prints in the public domain and photos of places; modern characters are protected by copyright, so for them I point you to official sites and museums.</p>
    </section>

    <h2 id="scrolls">The Scrolls at Kozan-ji<span class="h2-jp">鳥獣戯画</span></h2>
    <p>The <em>Choju-jinbutsu-giga</em>, usually called Choju-giga, is a set of four ink scrolls in which rabbits, frogs, monkeys and other animals wrestle, swim, race and parody monks. {W_CJ} dates the scrolls to the 12th and 13th centuries and notes that the usual attribution to the priest Toba Sojo is uncertain. They belong to Kozan-ji, a temple at Toganoo in the hills north-west of Kyoto ({KOZ}), and are designated National Treasures.</p>
    {fig('kozanji', 'The Kaizando hall at Kozan-ji with a gray roof among autumn maples', 'The Kaizando at Kozan-ji, Kyoto', f'Photo: KimonBerlin, {BYSA2}, {VIA}', maxw=760)}
    <p>This is a hall at Kozan-ji in autumn. The sign in front reads <em>Kaizando</em> and <em>Myoe Shonin</em> (as I read it), which points to the priest the temple regards as its founder. Notice how plain the building is: a low gray roof, white plaster, and maples behind it. The scrolls were not made for tourists; they have been kept in a quiet mountain temple like this one.</p>
    {fig('choju-sumo', 'Frogs and rabbits wrestling in a Choju-giga scroll', 'A wrestling scene from the Choju-giga scrolls', PD, maxw=760)}
    <p>This is the scene most people picture first: frogs and rabbits in a wrestling match. On the left a frog has thrown a rabbit onto its back, and on the right two rabbits seem to cheer or flinch while another is held in a frog's embrace. The vertical red-and-black stamps on the paper are marks of Kozan-ji. This image is a scan from a printed reproduction, so it is gray-toned and not a photo of the original ink.</p>
    {fig('choju-sumo-close', 'Close view of a frog throwing a rabbit in Choju-giga', 'Close-up of the same wrestling scene', PD, maxw=563)}
    <p>A closer view of the left half. The frog on the right raises a hand with a look of triumph, while the rabbit is flipped over with its legs in the air. The fun is in the expressions and the movement: animals behaving like people, drawn with a few quick brush lines.</p>
    <p>Dates for the designation differ between sources (1905 in one, 1952 in another), so I will leave the year out. What matters for this story is the style: lively lines, humor, and a sequence that you read as you unroll it. Many people call it the ancestor of manga, which is a fair way to see it, though it is a claim of influence and not a family tree.</p>

    {fig('choju-archery', 'Rabbits and frogs with bows and a fox holding a torch in a Choju-giga scroll', 'Archery and a torch-bearing fox in a Choju-giga scroll', PD, maxw=760)}
    <p>In this long strip, rabbits and frogs hold bows and a round leaf stands as a target on a stick. At right, a fox carries what looks like a blazing torch next to a rabbit. I read it as a game or contest, but I cannot name the exact episode, so I only describe what the drawing shows.</p>
    {fig('choju-water', 'Rabbits and monkeys playing in a stream in a Choju-giga scroll', 'Rabbits and monkeys by a stream in a Choju-giga scroll', PD, maxw=760)}
    <p>Here the animals are in and around a stream drawn with fine wavy lines. Rabbits and monkeys swim, sit on rocks and seem to play, and the landscape of bare trees and rocks fills the left side. It shows that the artist could handle water and scenery as well as comic action.</p>
    {fig('choju-procession', 'Rabbits and frogs carrying boxes and a litter in a Choju-giga scroll', 'A procession of rabbits and frogs in a Choju-giga scroll', PD, maxw=760)}
    <p>A parade of rabbits and frogs carries a box on a head, a covered chest and a flat litter, while a rabbit at the far end waves a fan. The thin seams in the image are joins between sheets of the scroll or the scan. I describe it as a procession, but the scene's meaning is not something I can confirm from the picture.</p>

    <h2 id="edo">Hokusai and the Word Manga<span class="h2-jp">北斎漫画</span></h2>
    <p>Picture scrolls (<em>emaki</em>) became woodblock-printed books in the Edo period. Katsushika Hokusai's sketchbooks, called <em>Hokusai Manga</em>, began appearing in 1814 and filled many volumes with people, animals, spirits and everyday scenes ({W_HM}). They were drawing manuals, not comics in the modern sense, but they helped make the word <span class="jp">漫画</span> familiar. For more on the prints of this era, see the <a class="inline-link" href="/culture/ukiyo-e/">ukiyo-e guide</a>.</p>

    {fig('hokusai-v8', 'Cover and a page of Hokusai Manga volume 8 with butterflies and small figure scenes', 'Hokusai Manga, volume 8: the cover and a page of small scenes', PD, maxw=620)}
    <p>On the right is the cover of a volume of <em>Hokusai Manga</em>, with the title in large characters over diagonal stripes and a few leaves and butterflies. On the left, a page is divided into small boxes, each with a figure or a pair of figures. This is the sketchbook format: one subject after another, to be copied or enjoyed.</p>
    {fig('hokusai-faces', 'Two pages of Hokusai Manga with rows of faces in a grid', 'Two pages of faces from Hokusai Manga', PD, maxw=760)}
    <p>Two pages made of faces in a grid. Each box shows a different person, young, old, smiling, frowning, with different hair and clothes. The page is a scan from a printed edition, and a printed page label can be seen at the bottom edge. For me it is the clearest sign that these books were about observing expression, which later manga artists made central.</p>
    {fig('hokusai-swim', 'Two pages of Hokusai Manga with people swimming underwater and a horse', 'Swimmers and a horse in Hokusai Manga', PD, maxw=700)}
    <p>People swim under a pattern of waves, some with floats, with fish and a horse among them. A title on the right page appears to read <em>Ukihara</em> (as I read it), but I will not claim more. What stands out is the range of poses: bodies seen from above, upside down and twisting, which shows why artists still study these pages.</p>

    <h2 id="meiji">Satire, Magazines and Paper Theater<span class="h2-jp">風刺漫画と紙芝居</span></h2>
    <p>After 1868, Western-style newspapers and humor magazines arrived. Kitazawa Rakuten drew satirical cartoons and is linked with the magazine <em>Tokyo Puck</em>, launched in 1905 ({W_KR}). In the 1930s, street storytellers used <em>kamishibai</em>, picture cards slid in a small wooden stage, to sell sweets and tell serial stories to children ({W_KS}). After the war, cheap rental comics (<em>kashihon</em>) carried on the habit of reading serial stories on paper.</p>

    <h2 id="tezuka">Tezuka, Toei and Astro Boy<span class="h2-jp">手塚治虫</span></h2>
    <p>Osamu Tezuka's <em>New Treasure Island</em> (1947) is often marked as the start of postwar story manga ({W_NT}). Its movie-like panels and long plots set a pattern. In 1958 Toei released <em>Hakujaden</em>, a color feature based on a Chinese legend ({W_HK}). Then on 1 January 1963 <em>Astro Boy</em> began on Japanese television ({W_AB}). Earlier TV animation existed, so I call it the first long-running popular weekly TV anime, not the first of all.</p>
    <p>A tip for visitors: Tezuka spent his youth in Takarazuka, Hyogo, and the museum there opened in 1994 ({TZK}).</p>

    <h2 id="jump">Weekly Shonen Jump and the Boom<span class="h2-jp">週刊少年ジャンプ</span></h2>
    <p><em>Weekly Shonen Jump</em> was launched by Shueisha in 1968 (sources give slightly different first-issue dates), and its peak circulation, reported as about 6.5 million copies in the mid-1990s, remains a record for a manga magazine ({W_SJ}). Those years produced Dragon Ball and many others, and manga became a mass medium for readers of every age.</p>

    <h2 id="global">Ghibli, Pokemon and the World<span class="h2-jp">世界へ</span></h2>
    <p>Studio Ghibli was founded in 1985 ({W_GH}). <em>Spirited Away</em> won the Golden Bear in Berlin in 2002 and the Academy Award for Best Animated Feature in 2003 ({W_SA}). The Pokemon anime began in Japan in 1997 and became a worldwide franchise. More recently, <em>Demon Slayer: Mugen Train</em> (2020) became one of the biggest box-office hits in Japanese history, though the exact totals differ by source, so I will not quote one. If you want to see real places behind these stories, start with the <a class="inline-link" href="/anime/">anime pilgrimage guides</a>.</p>

    <h2 id="visit">Where to Visit<span class="h2-jp">訪ねる</span></h2>
    <ul>
      <li><strong>Kozan-ji, Kyoto.</strong> The temple that keeps Choju-giga. Check {KOZ} for what is on view and for opening hours.</li>
      <li><strong>Kyoto International Manga Museum.</strong> A large manga archive in a former school building; see {KMM} for hours and closed days, which vary by source.</li>
      <li><strong>Osamu Tezuka Manga Museum, Takarazuka.</strong> Around a 10-minute walk from Takarazuka Station according to the city's tourist listings; the museum is closed on Mondays in several listings, so confirm on {TZK}.</li>
      <li><strong>Ghibli Museum, Mitaka, Tokyo.</strong> Entry by advance reservation only ({GHM}).</li>
      <li><strong>Mizuki Shigeru Road, Sakaiminato, Tottori.</strong> A street of about 800 meters lined with bronze yokai statues from GeGeGe no Kitaro; the count varies from about 150 to 178 by source ({MZK}, {MZ2}).</li>
    </ul>
    <p>For a guided option in Kyoto, you can browse <a class="inline-link" href="{VI}" target="_blank" rel="noopener sponsored">manga and anime tours on Viator</a>. I have not tried them, so check each page.</p>
    {fig('museum-building', 'The Kyoto International Manga Museum seen across a lawn', 'The Kyoto International Manga Museum from the lawn', f'Photo: 珈琲ルンバ, {BYSA3}, {VIA}', maxw=760)}
    <p>The museum occupies a former elementary school in central Kyoto. A banner on the right says it is open, so the picture was probably taken around its opening period, and the building or grounds may look different now. The wide lawn is a good place to sit and read, which is part of the idea.</p>
    {fig('museum-shelf', 'Visitors reading manga in front of a wall of shelves at the Kyoto International Manga Museum', 'Visitors at the manga wall of the Kyoto International Manga Museum', f'Photo: Peat Bakke, {BY2}, {VIA}', maxw=760)}
    <p>A long wall of shelves with the museum's name above it, and visitors standing and reading. This photo is from 2007, so I would not use it to describe the current layout, but it shows what makes the place different from a normal gallery: you are allowed to pick up manga and read.</p>
    {fig('yokai-space', 'Yokai Square in Sakaiminato with eyeball lamp posts and a thatched umbrella-shaped roof', 'Yokai Square on Mizuki Shigeru Road, Sakaiminato', f'Photo: Motokoka, {BYSA4}, {VIA}', maxw=760)}
    <p>A small plaza with lamp posts topped by round white globes, one of them with an orange eye, and a green thatched roof shaped like a giant umbrella. The signboard to the right is not readable here, and I cannot say which yokai the roof refers to, but the whole street is built around this kind of playful folklore imagery.</p>

    <h2 id="faq">Frequently Asked Questions<span class="h2-jp">よくある質問</span></h2>
    <div class="faq-stack">{faq_html}</div>

    <h2 id="final">Final Thoughts<span class="h2-jp">むすびに</span></h2>
    <p>From a frog and a rabbit wrestling on a scroll to a worldwide industry, the story is one long line of artists who liked to draw people and animals in motion. If you only have time for one stop, make it Kozan-ji in the quiet hills of Kyoto.</p>

    <div class="closing-block">
      <span class="torii">📜</span>
      <p>A rabbit, a frog and eight centuries of drawing.</p>
    </div>

    <section class="related-section">
      <h2>Related Guides</h2>
      <span class="h2-jp">関連ガイド</span>
      <div class="related-grid">
        <a class="related-card" href="/culture/ukiyo-e/" onclick="trackEvent('click','internal','related_manga_to_ukiyoe')">
          <div class="related-card-label">SACRED JAPAN ／ GUIDE</div>
          <div class="related-card-title">Ukiyo-e Guide →</div>
          <div class="related-card-desc">Woodblock prints, the Great Wave and where to see them.</div>
        </a>
        <a class="related-card" href="/anime/" onclick="trackEvent('click','internal','related_manga_to_anime')">
          <div class="related-card-label">SACRED JAPAN ／ HUB</div>
          <div class="related-card-title">Anime Pilgrimage →</div>
          <div class="related-card-desc">Real shrines and temples behind your favorite series.</div>
        </a>
        <a class="related-card" href="/culture/japanese-mythology/" onclick="trackEvent('click','internal','related_manga_to_mythology')">
          <div class="related-card-label">SACRED JAPAN ／ GUIDE</div>
          <div class="related-card-title">Japanese Mythology →</div>
          <div class="related-card-desc">The myths that anime keeps borrowing.</div>
        </a>
        <a class="related-card" href="/culture/kabuki/" onclick="trackEvent('click','internal','related_manga_to_kabuki')">
          <div class="related-card-label">SACRED JAPAN ／ GUIDE</div>
          <div class="related-card-title">Kabuki Guide →</div>
          <div class="related-card-desc">Another old stage of Japanese storytelling.</div>
        </a>
      </div>
    </section>

    <p style="font-size:14px;color:var(--enshu);line-height:1.7;margin-top:32px;"><strong>Sources:</strong> {W_CJ}, {W_HM}, {W_KR}, {W_KS}, {W_NT}, {W_HK}, {W_AB}, {W_SJ}, {W_GH} and {W_SA}; places from {KOZ}, {KMM}, {TZK}, {GHM}, {MZK} and {MZ2}. Hours, fees and counts differ between sources and may have changed.</p>

  </article>

</main>'''

url = finish(S, TITLE, DESC, KEYWORDS, '漫画とアニメ', 'Manga &amp; <em>Anime</em> History', '漫画・アニメの歴史',
             'From Choju-giga at Kozan-ji to Pokemon', 'Manga and Anime History', 'guide_manga_anime',
             'Kyoto+manga+anime+tour', main, faq_ld, published='2026-11-28')
print(url)
