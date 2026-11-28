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
      <p>As a licensed guide, I like to start manga and anime history at a temple, because it shows how long the habit of telling stories in pictures has lasted here. This page follows that thread from medieval scrolls to Pokemon in a few steps. It uses text and links rather than pictures of modern characters, which are protected by copyright, and it points you to official sites and museums instead.</p>
    </section>

    <h2 id="scrolls">The Scrolls at Kozan-ji<span class="h2-jp">鳥獣戯画</span></h2>
    <p>The <em>Choju-jinbutsu-giga</em>, usually called Choju-giga, is a set of four ink scrolls in which rabbits, frogs, monkeys and other animals wrestle, swim, race and parody monks. {W_CJ} dates the scrolls to the 12th and 13th centuries and notes that the usual attribution to the priest Toba Sojo is uncertain. They belong to Kozan-ji, a temple at Toganoo in the hills north-west of Kyoto ({KOZ}), and are designated National Treasures.</p>
    <p>Dates for the designation differ between sources (1905 in one, 1952 in another), so I will leave the year out. What matters for this story is the style: lively lines, humor, and a sequence that you read as you unroll it. Many people call it the ancestor of manga, which is a fair way to see it, though it is a claim of influence and not a family tree.</p>

    <h2 id="edo">Hokusai and the Word Manga<span class="h2-jp">北斎漫画</span></h2>
    <p>Picture scrolls (<em>emaki</em>) became woodblock-printed books in the Edo period. Katsushika Hokusai's sketchbooks, called <em>Hokusai Manga</em>, began appearing in 1814 and filled many volumes with people, animals, spirits and everyday scenes ({W_HM}). They were drawing manuals, not comics in the modern sense, but they helped make the word <span class="jp">漫画</span> familiar. For more on the prints of this era, see the <a class="inline-link" href="/culture/ukiyo-e/">ukiyo-e guide</a>.</p>

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
