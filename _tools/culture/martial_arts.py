import sys
sys.path.insert(0, '/home/claude/sacred-japan/_tools/culture')
from shinobi_common import *

S = 'martial-arts'
TITLE = 'Japanese Martial Arts Guide: From Jujutsu to Judo, Kendo, Karate and Where to Try Them'
DESC = "A licensed guide's introduction to Japanese martial arts: how battlefield jujutsu became judo, what kendo, kyudo, karate and aikido are, and where visitors can watch or try them, from the Kodokan to koryu sword classes."
KEYWORDS = 'Japanese martial arts, jujutsu history, judo history, Kodokan, Kano Jigoro, koryu, kobudo, kendo, kyudo, karate, aikido, iaido, Butokuden Kyoto, martial arts experience Japan, samurai training'

WIKI_JJ = ext('https://en.wikipedia.org/wiki/Jujutsu', 'Wikipedia (Jujutsu)', 'martial_src_wiki_jujutsu')
WIKI_JMA = ext('https://en.wikipedia.org/wiki/Japanese_martial_arts', 'Wikipedia (Japanese martial arts)', 'martial_src_wiki_jma')
WIKI_BUJ = ext('https://en.wikipedia.org/wiki/Bujutsu', 'Wikipedia (Bujutsu)', 'martial_src_wiki_bujutsu')
ENC = ext('https://encyclopedia.pub/entry/37088', 'encyclopedia.pub', 'martial_src_encyclopedia')
TRIP = ext('https://www.triptojapan.com/es/blog/judo-in-japan-kodokan', 'Trip to Japan\'s judo article', 'martial_src_triptojapan_judo')
WIKI_KD = ext('https://en.wikipedia.org/wiki/Kodokan', 'Wikipedia (Kodokan)', 'martial_src_wiki_kodokan')
KIDS = ext('https://web-japan.org/kidsweb/virtual/judo/judo01.html', 'Kids Web Japan', 'martial_src_kidsweb')
JG = ext('https://www.japan-guide.com/e/e2084.html', 'japan-guide.com', 'martial_src_japanguide')
KDK = ext('https://kdkjd.org/judo-museum-library/', 'the Kodokan website', 'martial_src_kodokan_museum')
KDK2 = ext('https://kdkjd.org/%E8%AC%9B%E9%81%93%E9%A4%A8%E3%81%A7%E5%AD%A6%E3%81%B6/', 'Practice at the Kodokan', 'martial_src_kodokan_practice')
TT = ext('https://www.taipeitimes.com/News/sport/archives/2020/02/19/2003731242', 'AFP (via Taipei Times)', 'martial_src_taipeitimes')
EMB = ext('https://www.az.emb-japan.go.jp/files/000180848.pdf', 'Web Japan\'s martial arts fact sheet', 'martial_src_webjapan_pdf')
JT = ext('https://japanesetaste.com/blogs/japanese-taste-blog/japanese-martial-arts-complete-guide-to-karate-judo-aikido-kendo-more', 'Japanese Taste', 'martial_src_japanesetaste')
JZ = ext('https://japan-zone.com/omnibus/martial.shtml', 'Japan-zone', 'martial_src_japanzone')
RYU = ext('https://ryukyu-bugei.com/?p=10684', 'Ryukyu Bugei', 'martial_src_ryukyubugei')
K247 = ext('https://kenshi247.net/blog/2009/03/31/kendo-places-3-butokuden/', 'Kenshi 24/7', 'martial_src_kenshi247')
BJ = ext('https://budojapan.com/?p=27627', 'Budo Japan', 'martial_src_budojapan')
KANPAI = ext('https://www.kanpai-japan.com/kyoto/butokuden', 'Kanpai Japan', 'martial_src_kanpai')
LJ = ext('https://livejapan.com/en/in-tokyo/in-pref-tokyo/in-shimbashi/activity-classes_and_workshops/vt5492968P1', 'Live Japan', 'martial_src_livejapan')
TTJ = ext('https://www.triptojapan.com/tours/koryu-swordsmanship-2-hour-traditional-experience/Aau1Ri6PR_OkwXrmO_POHQ', 'Trip to Japan', 'martial_src_triptojapan')
ABR = ext('https://theabroadguide.com/?p=3173814', 'The Abroad Guide', 'martial_src_abroadguide')
JUDOINFO = ext('https://medium.com/@harrysuke/history-of-judo-8c528433b23e', 'a history of judo reposted from Judoinfo', 'martial_src_judoinfo')
VI = viator('Japan+martial+arts+experience')
VI_KORYU = viator('Tokyo+koryu+samurai+sword')

faqs = [
 ("Is jujutsu the same as judo?",
  f"No. Jujutsu is the older family of grappling arts that samurai schools taught, and judo is the school Kano Jigoro founded in 1882 by combining the best elements of several of them ({KIDS}). Judo sparring leaves out strikes to lower the risk of injury, while strikes survive mainly in prearranged kata ({JG})."),
 ("Why did jujutsu begin on the battlefield?",
  f"{WIKI_JJ} describes the Sengoku-period (1467 to 1603) systems as ways for a lightly armed or unarmed warrior to deal with a heavily armed and armored enemy, since striking an armored opponent was ineffective. After the Edo period began, schools for fighting in ordinary clothes became common."),
 ("What is the difference between jutsu and do?",
  f"{JT} describes koryu as traditional arts that existed before the Meiji Restoration and gendai budo as modern arts that appeared afterward, with \"jutsu\" (technique) replaced by \"do\" (way) to stress self-development. Kano's choice of the name judo rather than jujutsu is one of the best-known examples ({WIKI_BUJ})."),
 ("Can a tourist watch judo practice at the Kodokan?",
  f"Yes. {JG} says spectating is free from the 8th-floor seating area, on weekdays and Saturdays from 16:30 to 19:30, with no reservation needed. Schedules can change, so check the Kodokan's own site before you go."),
 ("Can a complete beginner try a martial art in Japan?",
  "Yes, there are English-language experiences for beginners, mostly sword classes (koryu swordsmanship, iaido) and aiki-jujutsu sessions in Tokyo and Kyoto, plus the Kodokan's beginner judo classes. Listings and prices change, so use the section below as a starting point and confirm on each page."),
 ("Is karate Japanese?",
  f"It is practiced and organized throughout Japan, but its roots are in Okinawa, with influence from early Chinese fighting arts according to {JT}. It joined the Olympic program at the Tokyo 2020 Games, in the city that had hosted judo's Olympic debut in 1964 ({KIDS})."),
]
faq_html, faq_ld = faq_blocks(faqs)

copy_photos(S, {'kano-statue':'/mnt/user-data/uploads/c54c24a0-image.jpg',
                'kodokan-building':'/mnt/user-data/uploads/7c666f3a-image.jpg',
                'judo-throw':'/mnt/user-data/uploads/a2de8a84-image.jpg',
                'kendo-noma':'/mnt/user-data/uploads/a6076ed7-image.jpg',
                'kyudo-paris':'/mnt/user-data/uploads/15afe94f-image.jpg'})
fig = make_fig(S)
F_KENDO = fig('kendo-noma','Kendo practitioners in armor practicing in a wooden-floored dojo',
  'Kendo practice at the Noma Dojo in Tokyo.',
  f'Photo: Wang Ming, {BYSA3}, 2007-08-06. {VIA}')
F_KYUDO = fig('kyudo-paris','Kyudo archers at full draw on a gym floor in white tops and black hakama',
  'Team competition at the Second Kyudo World Cup, Paris.',
  f'Photo: Pierre-Yves Beaudouin, {BYSA4}, 2014-07-20. {VIA}')
F_STATUE = fig('kano-statue','Bronze statue of Kano Jigoro on a stone base in front of a lattice wall',
  'Statue of Kano Jigoro, founder of judo.',
  f'Photo: 三人日, {BYSA3}, 2011-08-06. {VIA}', maxw=420)
F_BUILD = fig('kodokan-building','The Kodokan building in Tokyo seen from the street',
  'The Kodokan building in Bunkyo ward, Tokyo.',
  f'Photo: Miyuki Meinaka, {BYSA4}, 2019-06-17. {VIA}', maxw=560)
F_THROW = fig('judo-throw','Two judoka during a throw at the Kodokan',
  'A judo throw demonstrated at the Kodokan.',
  f'Photo: Presidential Press and Information Office (Kremlin.ru), {BY4}, 2000-09-05. {VIA}', maxw=500)

main = f'''<main>

  <aside class="toc" aria-label="Table of contents">
    <div class="toc-label">TABLE OF CONTENTS ／ 目次</div>
    <div class="toc-title">In This Guide</div>
    <ol>
      <li><a href="#opening">Opening: A Note from the Guide</a></li>
      <li><a href="#terms">Budo, Bujutsu and Koryu: Three Words</a></li>
      <li><a href="#jujutsu">Jujutsu: Grappling in Armor</a></li>
      <li><a href="#judo">Judo: Kano Jigoro and the Kodokan</a></li>
      <li><a href="#others">Kendo, Kyudo, Karate and Aikido</a></li>
      <li><a href="#modern">How Budo Was Rebuilt After 1868</a></li>
      <li><a href="#kodokan">Visiting the Kodokan, Tokyo</a></li>
      <li><a href="#butokuden">The Butokuden in Kyoto</a></li>
      <li><a href="#try">Where to Try a Class</a></li>
      <li><a href="#faq">Frequently Asked Questions</a></li>
      <li><a href="#final">Final Thoughts</a></li>
    </ol>
  </aside>

  <article>

    <section id="opening">
      <p class="opening">Judo, the gentle way, grew out of a fighting style meant for men in armor on a battlefield, who had lost their weapons and had only their hands left.</p>
      <p>As a licensed guide, I find that this one fact changes how people look at martial arts in Japan. Jujutsu was an answer to a very practical problem, and judo, kendo and the rest of the modern arts are what later generations made of that old toughness. This guide follows that line from the battlefield to the modern dojo, and then points to places where you can watch or try a class. Where a fact comes from a single source I say so.</p>
    </section>

    <h2 id="terms">Budo, Bujutsu and Koryu: Three Words<span class="h2-jp">武道・武術・古流</span></h2>
    <p>{WIKI_JMA} lists three terms that are used interchangeably in English for Japanese martial arts: <span class="jp">武道</span> budo (the martial way), <span class="jp">武術</span> bujutsu (martial technique or the craft of war) and <span class="jp">武芸</span> bugei (martial art). The same entry explains <span class="jp">古流</span> koryu, "old school," as a school that began before the Meiji Restoration.</p>
    <p>The key shift is from <em>jutsu</em> to <em>do</em>. {JT} describes arts that existed before the Restoration as koryu and those that appeared afterward as gendai budo, "modern martial arts," with the ending changed from technique (jutsu) to way (do) to stress self-development. That is why you will see jujutsu next to judo, kenjutsu next to kendo and kyujutsu next to kyudo.</p>

    <h2 id="jujutsu">Jujutsu: Grappling in Armor<span class="h2-jp">柔術</span></h2>
    <p>{WIKI_JJ} separates two broad kinds of school. Sengoku-period (1467 to 1603) systems were <em>katchu bujutsu</em> or <em>yoroi kumiuchi</em>, fighting or grappling while wearing armor. Edo-period (1603 to 1867) systems were <em>suhada bujutsu</em>, fighting in ordinary clothes. It adds that on the battlefield, striking an armored opponent did not work well, so the techniques favored holds, throws and joint locks, often with a short weapon.</p>
    <p>{KIDS} tells the same story from the samurai side: besides swords, bows and arrows, they developed jujutsu for close fighting on the battlefield, called <em>kumi-uchi</em>, and by the start of the Edo period several styles had appeared and hand-to-hand combat had become important military training. It also says the roots of jujutsu lie in sumo, which appears in the <em>Kojiki</em> (712) and the <em>Nihon Shoki</em> (720). {WIKI_JJ} dates the Takenouchi school to the 1530s, among the early schools it names.</p>
    <p>One detail I like: the word <span class="jp">柔道</span> already appears as an alternative name for jujutsu in the early 1700s. The Wikipedia-based entry on {ENC} dates it to as early as 1724, almost two centuries before Kano. I rely on that single entry for the date.</p>

    <h2 id="judo">Judo: Kano Jigoro and the Kodokan<span class="h2-jp">柔道</span></h2>
    <p>The Meiji Restoration of 1868 ended samurai rule and Western culture spread. {KIDS} says jujutsu declined and nearly disappeared, until a young man named Kano Jigoro began training at 17 to build his strength. In May 1882, at 21, he combined the best elements of several jujutsu styles into one new school, with nine students in a 12-mat dojo at a temple. {WIKI_KD} identifies the temple as Eishoji in Ueno.</p>
    <p>{JUDOINFO} says Kano was born on October 28, 1860 in Mikage near Kobe, studied Tenjin Shinyo-ryu and then Kito-ryu, and called his new method judo. I rely on that page for those details, which I have not checked elsewhere.</p>
    <p>The result spread fast. According to {KIDS}, Kano visited Europe in 1889, later served on the International Olympic Committee, and judo became an official Olympic event for men in Tokyo in 1964, with women's judo official in 1992. The Olympic format uses weight classes. As {JG} describes it, the art covers throwing, grappling and, in kata, striking, and learning to fall is an important part of training.</p>
    {F_THROW}
    <p>The photo above shows a throw demonstrated at the Kodokan, as described on Commons; it was taken during an official visit in 2000, not at a regular practice. Even so, it shows the heart of judo clearly: one player's balance is broken and the other uses it, rather than force, to bring the partner to the mat.</p>
    <p>{WIKI_JJ} also lists Brazilian jiu-jitsu and sambo among arts descended from jujutsu through judo, which is a useful thing to know if you meet a traveler on the same trip who trains in either.</p>

    <h2 id="others">Kendo, Kyudo, Karate and Aikido<span class="h2-jp">剣道・弓道・空手・合気道</span></h2>
    <ul>
      <li><strong>Kendo (<span class="jp">剣道</span>):</strong> "the way of the sword," it evolved from kenjutsu ({JT}). {EMB} says the All Japan Kendo Federation was established in 1952, after which kendo returned as a sport and school subject. The "sword" is a <em>shinai</em> of bamboo, and points are scored by striking the head, trunk or wrist, or thrusting at the throat; two out of three points win a match.</li>
      <li><strong>Kyudo (<span class="jp">弓道</span>):</strong> Japanese archery, with a strong mental and spiritual side. {JT} says it is rooted in Zen Buddhism and Shinto and calls it "moving meditation," using an asymmetrical bamboo bow gripped about a third of the way up. The Web Japan fact sheet gives 1949 as the year the All Nippon Kyudo Federation began, which opened a new period for it as a sport.</li>
      <li><strong>Karate (<span class="jp">空手</span>):</strong> originated in Okinawa, influenced by early Chinese fighting arts, with Shotokan as the most popular of four major styles. It became an Olympic sport at the Tokyo 2020 Games ({JT}). To see the Okinawan side of the story, our {link('/guides/shuri-castle/', 'Shuri Castle guide', 'martial_to_shuri')} covers the Ryukyu Kingdom's palace.</li>
      <li><strong>Aikido (<span class="jp">合気道</span>):</strong> a self-defense art that avoids harming the attacker, using joint holds and throws that redirect the attacker's energy. {JZ} says its founder had developed his own techniques, which he called aiki bujutsu, by 1922, and later renamed them aikido; its source is a single page, so please treat the date as approximate.</li>
      <li><strong>Iaido (<span class="jp">居合道</span>):</strong> drawing the sword from the scabbard and cutting in one motion at an imagined opponent, practiced largely solo, sometimes from a seated position ({JT}).</li>
    </ul>
    {F_KENDO}
    <p>This is kendo practice at the Noma Dojo in Tokyo, as described on Commons. The players wear the full armor, a mask, a padded jacket and gloves over a dark hakama, and hold bamboo swords. Spare armor hangs in a row along the wall, and the long wooden floor is bright with skylights and tall windows. It is a useful picture of what a visitor will see: a large hall, a lot of footwork, and no one standing still.</p>
    {F_KYUDO}
    <p>Kyudo looks very different. The photo shows a team competition at the Second Kyudo World Cup, held in Paris in July 2014 according to Commons, and the poster on the left wall appears to say the same. The archers wear white tops and black hakama, and the bows are very long and held asymmetrically, with the grip well below the middle. Several are at full draw at once, while a seated official in a grey jacket watches from the front. It is also a reminder that kyudo is practiced far beyond Japan.</p>
How Budo Was Rebuilt After 1868<span class="h2-jp">武道の再建</span></h2>
    <p>The arts did not simply survive the end of the samurai class. {EMB} says that after the Sino-Japanese War, in 1895, a national organization called the Dai Nippon Butokukai (Great Japan Martial Virtue Association) centralized martial arts and oversaw their introduction into education. The same fact sheet says the occupation authorities banned the arts for five years after the Second World War, until 1950, because the prewar revival was seen as feeding militarism; the arts were then promoted as sports. {RYU} adds that the Butokukai was dissolved in 1946 by an Occupation directive, and that the All Japan Kendo Federation, established in 1952, became its de facto successor.</p>

    <h2 id="kodokan">Visiting the Kodokan, Tokyo<span class="h2-jp">講道館</span></h2>
    <p>The Kodokan Judo Institute is the headquarters of the world judo community, founded in 1882 by Kano and now an eight-story building in Bunkyo ward ({WIKI_KD}). The address is 1-16-30 Kasuga, a one-minute walk from exits A1 and A2 of Kasuga Station on the Mita and Oedo lines, according to {TRIP}.</p>
    <ul>
      <li><strong>Watching practice:</strong> {JG} says spectating is free from the 8th floor, on weekdays and Saturdays, 16:30 to 19:30, with no reservation.</li>
      <li><strong>Museum:</strong> a small judo exhibit on the 2nd floor, free. {JG} lists weekday hours of 11:00 to 18:00; {KDK} says it is closed on Saturdays, Sundays and national holidays, and also during summer and year-end breaks.</li>
      <li><strong>Training:</strong> {KDK2} says randori classes accept trainees with a certain amount of judo experience, and beginners can study from the basics in the judo school.</li>
      <li><strong>Manners:</strong> {TT} reports that foreign visitors who train there bow to the statue of Kano before stepping on the tatami, and are not excused from roll call or the group warm-up.</li>
    </ul>
    {F_BUILD}
    <p>This is the building you are looking for: a pale block with a grid of windows, easy to pick out among the street trees. The lettering on the windows reads, as I read it, 講道館ビル along with the names of clinics on other floors. Spectators head for the 8th floor, as {JG} describes.</p>
    {F_STATUE}
    <p>The bronze figure in hakama and a long jacket, standing on a stone base, is catalogued on Commons as Kano Jigoro. The wall behind it carries a signboard that reads 講道館, right to left. I cannot say from the photo whether this is the statue that visitors bow to in the {TT} report, since I have not confirmed which statue that article means.</p>
    <p>Hours and class details change, so please check the Kodokan's website for the current schedule before you plan your day around it.</p>

    <h2 id="butokuden">The Butokuden in Kyoto<span class="h2-jp">武徳殿</span></h2>
    <p>Beside Heian Jingu (see our {link('/guides/best-shrines-kyoto/', 'Kyoto shrines guide', 'martial_to_heian')}) stands the Butokuden, the main hall of Kyoto's Budo Center. {K247} says it was completed in 1899 on the north-west side of the Heian Jingu grounds as a demonstration hall for the Butokukai, and that every May 2 to 5 it hosts the Kyoto Taikai (the All Japan Kendo Enbu Taikai); {BJ} says the event was first held in 1895. {KANPAI} says kendo is the main discipline there, with an archery range for kyudo and a sumo hall, and calls it a must-see for martial arts enthusiasts.</p>
    <p>{KANPAI} gives 1895 as the year the hall was built, which does not match the 1899 completion given by {K247}, so I use 1899 for the building and 1895 for the first taikai. Whether you can watch practice on a given day depends on the schedule, so I would treat the grounds as a pleasant stop beside Heian Jingu and check ahead if you want to see a session.</p>

    <h2 id="try">Where to Try a Class<span class="h2-jp">体験できる場所</span></h2>
    <p>Koryu schools (the old, pre-Meiji lineages) are small and traditional, but several teach visitors in English. These are listings I found; I have not tried them, so please check each page for the current program, price and reviews.</p>
    <ul>
      <li><strong>Tokyo, Kojimachi: Tsurugi Goshin Budo.</strong> {TTJ} lists a 2-hour hands-on koryu swordsmanship session in English or Japanese at the Tokyo headquarters (B2F, MK Kojimachi Building), and a separate 2-hour self-defense session based on aiki-jujutsu. {LJ} shows a Viator version of the sword experience at 12,000 yen, and a related listing says the training is based on Daito-ryu Aiki Jujutsu.</li>
      <li><strong>Tokyo, Shinjuku: Koshu-ryu Jujutsu.</strong> A Live Japan listing says you receive direct instruction in Koshu-ryu jujutsu from Master Haibara Yukiji.</li>
      <li><strong>Tokyo: swordsmanship and horseback archery.</strong> A Trip.com listing says the Toyama-ryu Bizen Association teaches both swordsmanship and traditional horseback archery (<em>yabusame</em>) in one class.</li>
      <li><strong>Kyoto: Asayama Ichiden-ryu.</strong> {ABR} describes a roughly three-hour evening class (starting 6:30 pm) at the Kyoto branch of this lineage, practicing iaijutsu and kenjutsu with wooden swords in a traditional dojo, for up to four travelers, at a reported price of about $33. I have only this one source for the price.</li>
      <li><strong>Tokyo, Kuramae: Mugai-ryu iaido.</strong> {JG} mentions a 1-hour Klook "samurai experience" at 22,200 yen.</li>
    </ul>
    <p>To compare more, see all {aff(VI, 'martial arts experiences on Viator', 'martial_viator_experience')}, or search {aff(VI_KORYU, 'koryu and samurai sword classes in Tokyo', 'martial_viator_koryu')}. For the people behind these arts, our {link('/culture/samurai/', 'samurai guide', 'martial_to_samurai')} covers armor and swords, and the {link('/culture/ninja/', 'ninja guide', 'martial_to_ninja')} covers Iga and Koka.</p>

    <h2 id="faq">Frequently Asked Questions<span class="h2-jp">よくあるご質問</span></h2>

    <div class="faq-stack">

{faq_html}    </div>

    <h2 id="final">Final Thoughts<span class="h2-jp">むすびに</span></h2>
    <p>If you have one evening in Tokyo, sit on the 8th floor of the Kodokan and watch the throws; if you have a free afternoon in Kyoto, walk past the Butokuden beside Heian Jingu. If you want something in your own hands, a koryu sword class is the closest thing to the way the samurai learned. Once you know that jujutsu began as a way to fight in armor, every judo mat and every kendo bamboo sword has a longer story behind it.</p>

    <div class="closing-block">
      <span class="torii">🥋</span>
      <p>From a battlefield habit to a way of life, one throw at a time.</p>
    </div>

    <section class="related-section">
      <h2>Related Guides</h2>
      <span class="h2-jp">関連ガイド</span>
      <div class="related-grid">
        <a class="related-card" href="/culture/samurai/" onclick="trackEvent('click','internal','related_martial_to_samurai')">
          <div class="related-card-label">SACRED JAPAN ／ GUIDE</div>
          <div class="related-card-title">⚔️ Samurai Guide →</div>
          <div class="related-card-desc">History, armor, swords and samurai towns.</div>
        </a>
        <a class="related-card" href="/culture/ninja/" onclick="trackEvent('click','internal','related_martial_to_ninja')">
          <div class="related-card-label">SACRED JAPAN ／ GUIDE</div>
          <div class="related-card-title">🥷 Ninja Guide →</div>
          <div class="related-card-desc">Iga and Koka, museums, a festival and the manga behind the myth.</div>
        </a>
        <a class="related-card" href="/culture/sumo/" onclick="trackEvent('click','internal','related_martial_to_sumo')">
          <div class="related-card-label">SACRED JAPAN ／ GUIDE</div>
          <div class="related-card-title">Sumo Guide →</div>
          <div class="related-card-desc">Shinto rituals, tournaments and morning practice.</div>
        </a>
        <a class="related-card" href="/culture/samurai-and-ninja/" onclick="trackEvent('click','internal','related_martial_to_hub')">
          <div class="related-card-label">SACRED JAPAN ／ FEATURE</div>
          <div class="related-card-title">⚔️ Samurai &amp; Ninja Feature →</div>
          <div class="related-card-desc">Both guides, side by side, with places and events.</div>
        </a>
      </div>
    </section>

    <p style="font-size:14px;color:var(--enshu);line-height:1.7;margin-top:32px;"><strong>Sources:</strong> jujutsu history from {WIKI_JJ} and {KIDS}; terms from {WIKI_JMA} and {JT}; judo and the Kodokan from {KIDS}, {JG}, {WIKI_KD}, {KDK}, {KDK2} and {TT}; kendo, kyudo and the post-1868 revival from {EMB}, {JZ} and {RYU}; the Butokuden from {K247}, {BJ} and {KANPAI}; experiences from {TTJ}, {LJ}, {ABR} and {JG}. Prices and schedules were as listed when I checked and may have changed.</p>

  </article>

</main>'''

url = finish(S, TITLE, DESC, KEYWORDS, '武道', 'The Japanese <em>Martial Arts</em> Guide', '武道ガイド',
             'Jujutsu, Judo, Kendo, Karate and Where to Try Them', 'Martial Arts Guide', 'guide_martial',
             'Japan+martial+arts+experience', main, faq_ld, published='2026-11-27')
print(url)
