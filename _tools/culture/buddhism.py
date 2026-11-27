import re, os, json
R='/home/claude/sacred-japan'
S='what-is-buddhism'
OUT=f'{R}/culture/{S}'
os.makedirs(OUT,exist_ok=True)

def link(href,txt,lab): return f'<a href="{href}" class="inline-link" onclick="trackEvent(\'click\',\'internal\',\'{lab}\')">{txt}</a>'
def ext(href,txt,lab): return f'<a href="{href}" target="_blank" rel="noopener" onclick="trackEvent(\'click\',\'external\',\'{lab}\')">{txt}</a>'
VI='https://www.viator.com/search/Kyoto+temple?pid=P00298374&amp;mcid=42383&amp;medium=link&amp;campaign=sacred-japan'

WIKI='https://en.wikipedia.org/wiki/Buddhism_in_Japan'
JG='https://japan-guide.com/e/e2055.html'
NIP='https://www.nippon.com/en/japan-topics/b10901/'
ENC='https://encyclopedia.com/religion/dictionaries-thesauruses-pictures-and-press-releases/buddhism-japan'
UGA='https://www.religion.uga.edu/sites/default/files/inline-files/japanese_buddhism.pdf'
COL='https://columbia.edu/cu/weai/exeas/resources/foundations-text-6.html'
WHE='https://worldhistory.org/article/1423'
COLL='https://www.thecollector.com/guide-japanese-temples/'
NG='https://www.nationalgeographic.com/travel/article/japan-shrines-temples-shinto-buddhism-history'

LA='style="color:var(--enshu);"'
def lk(t,u): return f'<a href="{u}" target="_blank" rel="noopener" {LA}>{t}</a>'
CAPST='font-size:13px;color:var(--enshu);margin-top:10px;text-align:center;line-height:1.6;'
L_BYSA3=lk("CC BY-SA 3.0","https://creativecommons.org/licenses/by-sa/3.0/")
L_BYSA4=lk("CC BY-SA 4.0","https://creativecommons.org/licenses/by-sa/4.0/")
L_BY4=lk("CC BY 4.0","https://creativecommons.org/licenses/by/4.0/")
L_BY2=lk("CC BY 2.0","https://creativecommons.org/licenses/by/2.0/")
L_CC0=lk("CC0","https://creativecommons.org/publicdomain/zero/1.0/")
VIA='via Wikimedia Commons (resized)'

def pfig(src,alt,desc,cred,mw=760,hero=False):
    st='margin:0 0 48px;' if hero else f'margin:36px auto;max-width:{mw}px;'
    img='width:100%;max-height:420px;object-fit:cover;border-radius:4px;display:block;' if hero else 'width:100%;height:auto;border-radius:4px;display:block;'
    ld='eager' if hero else 'lazy'
    return (f'<figure style="{st}">\n      <picture><source srcset="/images/{src}.webp" type="image/webp"><img src="/images/{src}.jpg" alt="{alt}" loading="{ld}" style="{img}"></picture>\n'
            f'      <figcaption style="{CAPST}">{desc}<br>{cred}</figcaption>\n    </figure>')

f_daibutsu=pfig('todaiji-buddha','The bronze Great Buddha seated in the Daibutsuden hall at Todaiji in Nara','The bronze Great Buddha of Todaiji, about fifteen meters high. Nippon.com names Dainichi (Vairocana) as the Buddha Japan knows best as the Great Buddha.',f'Photo: Gilles Desjardins, {L_BYSA4}, {VIA}')
f_zen=pfig('temple-stay-zazen-hall','People seated in rows facing the wall in a Zen meditation hall','Zazen, seated Zen meditation, in a practice hall (illustrative photo).',f'Photo: Daiko Shōgen, {L_CC0}, {VIA}')
f_enryaku=pfig('enryakuji-konponchudo','The Konpon Chudo main hall of Enryakuji on Mount Hiei among cedar trees','The Konpon Chudo on Mount Hiei, the Tendai headquarters. Several of the Kamakura reformers began their training here.','Photo: Daderot, public domain, '+VIA)
f_amida=pfig('enryakuji-amidado','The Amida-do hall at Enryakuji with a tiled roof and wooden veranda','The Amida-do on Mount Hiei, dedicated to Amida, the Buddha the Pure Land schools turn to.',f'Photo: Zairon, {L_BY4}, {VIA}')
f_koya=pfig('koyasan-pagoda','The vermilion Konpon Daito pagoda at Koyasan under a blue sky','The Konpon Daito pagoda on Koyasan, the Shingon center founded by Kukai.',f'Photo: 663highland, {L_BYSA3}, {VIA}')
f_kukai=pfig('shikoku-pilgrimage-kukai-statue','A bronze statue of Kobo Daishi with a staff and a hat at Motoyama-ji','A bronze statue of Kobo Daishi (Kukai) at Motoyama-ji, staff and hat in hand.',f'Photo: Toto-tarou, {L_BYSA3}, {VIA}')
f_nio=pfig('zenkoji-niomon','The two-story Niomon gate at Zenkoji with a tiled roof','The Niomon gate at Zenkoji, where the approach to the main hall begins.',f'Photo: Drivephotographer, {L_CC0}, {VIA}')
f_byodo=pfig('byodoin-hall','The Phoenix Hall of Byodoin on its pond island','The Phoenix Hall at Byodoin. The seated Amida Buddha inside, made by Jocho, is among the works Nippon.com names.',f'Photo: Dr.InSide, {L_BYSA4}, {VIA}')
f_incense=pfig('shrine-vs-temple-incense','A large bronze incense burner with smoke rising in front of a temple hall at Senso-ji','The great incense burner at Senso-ji, a purification step found at temples rather than shrines.',f'Photo: Dick Thomas Johnson, {L_BY2}, {VIA}')
f_meal=pfig('temple-stay-shukubo-meal','A vegetarian shojin ryori dinner tray with small dishes at a temple lodging on Koyasan','A shojin ryori vegetarian dinner tray at Kongosanmain, a temple lodging (shukubo) on Koyasan.',f'Photo: Szabolcs Arany, {L_BY2}, {VIA}')
f_stage=pfig('kiyomizu-dera-stage','The wooden stage of Kiyomizu-dera and its pagoda framed by autumn maples','Kiyomizu-dera in autumn: a main hall, a pagoda and a hillside, the kind of layout this guide teaches you to read.',f'Photo: Martin Falbisoner, {L_BYSA4}, {VIA}')
f_hero=pfig('todaiji-daibutsuden','The huge wooden Daibutsuden hall of Todaiji in Nara','The Daibutsuden at Todaiji in Nara, which Wikipedia describes as the head temple of the state temple network completed in 752.',f'Photo: 663highland, {L_BYSA3}, {VIA}',hero=True)

faqs=[
("Is Buddhism or Shinto the main religion of Japan?","Neither one replaces the other, and that is the honest answer. Japan Guide says that after early conflicts the two coexisted and complemented each other, and that roughly two-thirds of Japanese people consider themselves Buddhist, while Buddhism has little direct effect on daily life. Wikipedia notes that estimates of adherence vary widely by survey, from under 20% to about 46%, depending on how the question is asked. In practice, many families use shrines for festivals and good-luck prayers and temples for funerals and ancestors."),
("When did Buddhism come to Japan?","Traditionally in the 6th century. Wikipedia says the Nihon Shoki dates the official introduction to 552, when King Seong of Baekje sent Emperor Kinmei an image of the Buddha, ritual banners and sutras, and that other sources give 538; both dates are considered unreliable. Japan Guide says it came via Korea and China in the 6th century."),
("What are the main schools of Japanese Buddhism?","Tendai and Shingon (9th century, from China), Pure Land and True Pure Land, Zen (Rinzai and Soto) and Nichiren (all from the Kamakura era, 12th to 13th century). Wikipedia gives approximate follower numbers of 22 million for Pure Land, 10 million for Nichiren, 5.4 million for Shingon, 5.3 million for Zen and 2.8 million for Tendai."),
("What is the difference between a Buddha and a bodhisattva statue?","Nippon.com explains that a nyorai (Buddha) has completed training and reached enlightenment and wears simple monastic robes, while a bosatsu (bodhisattva) has vowed to pursue enlightenment and is still training, so it usually wears a crown and jewels. Kannon and Jizo are bodhisattvas, not Buddhas. See the section on statues above."),
("Can I visit a Japanese temple without being Buddhist?","Yes. Temples welcome visitors of any belief. Be quiet, follow the posted rules about photography inside halls, and see my "+link('/culture/shrine-vs-temple/','shrine vs temple guide','buddhism_faq_to_shrine_vs_temple')+" for the step-by-step prayer routine, which differs from a shrine."),
("Why are most Japanese funerals Buddhist?","Wikipedia says about 90% of Japanese funerals are conducted with Buddhist rites, and that in the 17th century the Tokugawa government required every household to register with a Buddhist temple. Wikipedia also says about 60% of Japanese families have a butsudan, a home Buddhist altar. Scholars call this \"funeral Buddhism\", a term coined in 1963."),
("Where is the best place to start seeing Buddhism in Japan?","Todaiji in Nara for the scale of early state Buddhism, Mount Koya for Shingon, Mount Hiei for Tendai, and a temple stay if you want to experience it rather than just look. My links are at the end of this guide."),
]
faq_html=''.join(f"""      <details class="faq-item">
        <summary>{q}</summary>
        <div class="faq-answer">{a}</div>
      </details>

""" for q,a in faqs)
faq_ld=json.dumps({"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":re.sub('<[^>]+>','',a)}} for q,a in faqs]},ensure_ascii=False,indent=2)

TITLE="What Is Buddhism in Japan? Schools, Statues and Temples Explained for Visitors"
DESC="A licensed guide's plain-English introduction to Japanese Buddhism: how it arrived, how it lives beside Shinto, the main schools (Zen, Pure Land, Shingon, Tendai, Nichiren), how to tell a Buddha from a bodhisattva, and how to read a temple."
URL=f"https://sacred-japan.net/culture/{S}/"
OG="https://sacred-japan.net/images/og/og-culture-what-is-buddhism.jpg"

main=f"""<main>

  <!-- TABLE OF CONTENTS -->
  <aside class="toc" aria-label="Table of contents">
    <div class="toc-label">TABLE OF CONTENTS ／ 目次</div>
    <div class="toc-title">In This Guide</div>
    <ol>
      <li><a href="#opening">Opening: A Note from the Guide</a></li>
      <li><a href="#arrival">How Buddhism Arrived</a></li>
      <li><a href="#shinto">Buddhism and Shinto: Mixed, Then Separated</a></li>
      <li><a href="#schools">The Main Schools</a></li>
      <li><a href="#statues">Who Is Who: Buddhas, Bodhisattvas and Guardians</a></li>
      <li><a href="#temple">How to Read a Temple</a></li>
      <li><a href="#daily">Buddhism in Everyday Life</a></li>
      <li><a href="#visit">Where to Start</a></li>
      <li><a href="#faq">Frequently Asked Questions</a></li>
      <li><a href="#final">Final Thoughts</a></li>
    </ol>
  </aside>

  <article>

    <section id="opening">
      <p class="opening">Here is a small puzzle I give my guests. A Japanese family prays at a shrine for a child's exams, gets married in front of a shrine priest, and then holds the grandmother's funeral at a temple. Which religion is that? Wikipedia says about 90% of Japanese funerals use Buddhist rites, and about 60% of families keep a home Buddhist altar, so the answer is: both, and nobody finds it strange.</p>
      <p>As a licensed guide, I find that Buddhism is the part of Japan visitors see most and explain least. Every large temple you visit, every serene statue and every vegetarian temple meal belongs to it. This guide gives you the short version: how it arrived, the main schools, how to tell the statues apart, and how to read a temple. If you want the Shinto side, start with {link('/culture/what-is-shinto/','What Is Shinto','buddhism_opening_to_shinto')}.</p>
    </section>

    {f_hero}

    <h2 id="arrival">How Buddhism Arrived<span class="h2-jp">仏教伝来</span></h2>
    <p>{ext(WIKI,'Wikipedia','buddhism_src_wiki_arrival')} says the <em>Nihon Shoki</em> dates the official introduction to 552, when King Seong of Baekje, a Korean kingdom, sent Emperor Kinmei an image of the Buddha, ritual banners and sutras. Other sources give 538, and the article calls both dates unreliable. {ext(JG,'Japan Guide','buddhism_src_jg_arrival')} puts it simply as the 6th century, a gift from Korea, which the ruling nobles adopted but which spread slowly among ordinary people because its theory was complex.</p>
    <p>Wikipedia names Hoko-ji (Asukadera) as the first temple, and records that the <em>Nihon Shoki</em> counted 46 Buddhist temples in 624. In 710 the capital moved to Nara, where the state built a network of provincial temples with {link('/guides/todaiji/','Todaiji','buddhism_to_todaiji')} (completed in 752) at its head; its Great Buddha is the symbol of that era.</p>
    <p>Japan Guide adds a detail I like: the large Nara monasteries gained so much political influence that it was one of the reasons the government moved the capital to Nagaoka in 784 and then to Kyoto in 794. Powerful monasteries remained a problem for centuries.</p>

    {f_daibutsu}

    <h2 id="shinto">Buddhism and Shinto: Mixed, Then Separated<span class="h2-jp">神仏習合と神仏分離</span></h2>
    <p>For most of history the two were not kept apart. Wikipedia calls this <em>shinbutsu shugo</em>, the long merging of kami worship and Buddhism, in which Buddhist monks often conducted rites for the kami. National Geographic quotes a Kokugakuin University professor saying that in some cases kami were explained as Buddhas in disguise.</p>
    <p>That changed in 1868. Wikipedia says the Kami and Buddhas Separation Order began a push to separate the two and promote Shinto as the state religion, followed by a persecution of Buddhism called <em>haibutsu kishaku</em>. It gives an estimate of about 40,000 Buddhist temples destroyed, with the worst violence in 1869 to 1871 and up to 80% of temples lost in some places. Japan Guide describes the same shift more gently: the early Meiji government favored Shinto, separated it from Buddhism and attacked Buddhist institutions.</p>
    <p>Wikipedia adds one more piece: in the 17th century the Tokugawa government required households to register with a Buddhist temple, first as a measure against Christianity and later as a kind of census. That system is a big reason temples are tied to funerals and family graves today. For the visual side of the story, my {link('/culture/shrine-vs-temple/','shrine vs temple guide','buddhism_to_shrine_vs_temple')} shows how to tell the two apart on the ground.</p>

    <h2 id="schools">The Main Schools<span class="h2-jp">主な宗派</span></h2>
    <p>Japanese Buddhism is not one thing. {ext(JG,'Japan Guide','buddhism_src_jg_schools')} gives the dates most visitors need: Tendai was brought from China in 805 by Saicho and Shingon in 806 by Kukai, and the Kamakura-era schools followed. Here is the family tree in plain terms.</p>
    <ul style="line-height:2;margin:16px 0 24px 22px;">
      <li><strong>Tendai (天台).</strong> Founded by Saicho (767-822), headquartered on Mount Hiei. Britannica notes that Mount Hiei and Mount Koya became the centers of Tendai and Shingon. See {link('/guides/enryakuji/','Enryaku-ji','buddhism_to_enryakuji')}.</li>
      <li><strong>Shingon (真言).</strong> Founded by Kukai (774-835), also known as Kobo Daishi, on Mount Koya. See {link('/guides/mount-koya/','Mount Koya','buddhism_to_mount_koya')} and the {link('/guides/shikoku-pilgrimage/','Shikoku pilgrimage','buddhism_to_shikoku')}.</li>
      <li><strong>Pure Land (浄土).</strong> Honen founded Jodo in 1175 and his pupil Shinran founded True Pure Land in 1224 (Japan Guide). The teaching is faith in Amida Buddha, simplified for everyone.</li>
      <li><strong>Zen (禅).</strong> Japan Guide says it came from China in 1191 and appealed to the military class. {ext(ENC,'Encyclopedia.com','buddhism_src_enc')} names Eisai (1141-1215) for Rinzai and Dogen (1200-53) for Soto. Meditation and self-discipline are the point.</li>
      <li><strong>Nichiren (日蓮).</strong> Founded by Nichiren in 1253 according to Japan Guide, centered on the Lotus Sutra; Japan Guide notes it was unusually intolerant of other schools.</li>
    </ul>
    <p>A University of Georgia course handout notes what the Kamakura schools had in common: roots in the Tendai tradition of Mt. Hiei, a simple method of salvation, and the belief that salvation is open to ordinary lay people, not only monks. The Columbia University overview adds a point that surprises many visitors: despite the Western fascination with Zen since the mid-20th century, Zen has never been the dominant form of Buddhism in Japan. Wikipedia's rough follower counts back that up, with Pure Land at about 22 million against about 5.3 million for Zen, though counts like these depend on how each school counts members.</p>

    {f_enryaku}
    {f_amida}
    {f_koya}
    {f_kukai}
    {f_zen}

    <h2 id="statues">Who Is Who: Buddhas, Bodhisattvas and Guardians<span class="h2-jp">仏像の見分け方</span></h2>
    <p>The most useful skill for a temple visit is knowing which kind of figure you are looking at. {ext(NIP,'Nippon.com','buddhism_src_nippon')} sorts Buddhist statues into four groups.</p>
    <ul style="line-height:2;margin:16px 0 24px 22px;">
      <li><strong>Nyorai (如来, Buddhas).</strong> Beings who completed training and reached enlightenment. Look for simple monastic robes. Examples: Shaka (the historical Buddha), Amida (Pure Land schools), Yakushi (the healing Buddha) and Dainichi (Vairocana), best known as the Great Buddha.</li>
      <li><strong>Bosatsu (菩薩, bodhisattvas).</strong> Beings who have vowed to reach enlightenment and are still training. Look for a jeweled crown, necklaces and symbolic objects. Examples: Kannon (mercy), Jizo (savior of souls in the underworld) and Miroku (the future Buddha).</li>
      <li><strong>Myoo (明王, wisdom kings).</strong> Protective deities with a wrathful appearance, who reach people unmoved by ordinary teaching. Examples: Fudo (the Immovable) and Aizen, who is red-skinned.</li>
      <li><strong>Ten (天, devas).</strong> Deities, many from Indian traditions, absorbed as guardians of the teachings. Examples: the Four Heavenly Kings, Benzaiten and Daikokuten. Nippon.com's rule of thumb: any figure that is not a buddha, bodhisattva or wisdom king is generally a deva.</li>
    </ul>
    <p>Nippon.com names famous examples you can visit: the Great Buddha at Todaiji, an early Shaka triad at Horyuji, the Ashura of Kofukuji, and the seated Amida Buddha in the Phoenix Hall at {link('/guides/byodoin/','Byodoin','buddhism_to_byodoin')}. At temple gates you will often meet fierce guardian figures; my {link('/guides/zenko-ji/','Zenko-ji guide','buddhism_to_zenkoji')} shows one such gate.</p>

    {f_nio}
    {f_byodo}

    <h2 id="temple">How to Read a Temple<span class="h2-jp">お寺の見方</span></h2>
    <p>Most temples follow a loose pattern. {ext(WHE,'World History Encyclopedia','buddhism_src_whe')} lists the principal buildings of most complexes: the main hall (<em>hondo</em> or <em>butsudo</em>) where the most sacred images are kept, a pagoda built to house relics, a meditation hall, a sutra repository, a founder's hall and a bell tower. {ext(COLL,'The Collector','buddhism_src_collector')} describes a traditional layout with a main gate (<em>sanmon</em>), a main hall, a lecture hall and a monks' hall, with bigger complexes adding a dining hall, a bell tower and a sutra repository.</p>
    <p>The practical route is simple. You enter through the main gate, walk to the main hall to pray, and the bell tower and pagoda sit along the way. A Japan MLIT multilingual guide to one temple describes exactly this order: main gate, then the stairs up to the main hall, with the bell tower beside the path. National Geographic adds that in the old days, before clocks were in every home, temple bells told the time to the local people.</p>

    {f_stage}
    {f_incense}

    <h2 id="daily">Buddhism in Everyday Life<span class="h2-jp">暮らしの中の仏教</span></h2>
    <p>Japan Guide says Buddhism has little direct effect on daily life, but funerals are usually Buddhist and many households keep a house altar for their ancestors. Wikipedia's numbers fit this picture: about 90% of funerals follow Buddhist rites, and about 60% of families have a butsudan. Wikipedia also records that scholars have a name for it, <em>soshiki bukkyo</em>, or funeral Buddhism, coined in 1963, and that the survey result that about 70% of people say they hold no religious beliefs (2013) coexists with all of this.</p>
    <p>The visitor-friendly side is different: temple lodgings, vegetarian temple cooking and the goshuin stamp books. A {link('/guides/temple-stay/','temple stay','buddhism_to_temple_stay')} lets you eat a monk's vegetarian dinner and join morning prayers, and my {link('/culture/goshuin-guide/','goshuin guide','buddhism_to_goshuin')} explains how temples and shrines hand out their calligraphy stamps.</p>

    {f_meal}

    <h2 id="visit">Where to Start<span class="h2-jp">はじめの一歩</span></h2>
    <p>If you only have time for a few places, I would pick by what you want to see.</p>
    <ul style="line-height:2;margin:16px 0 24px 22px;">
      <li>The scale of early state Buddhism: {link('/guides/todaiji/','Todaiji, Nara','buddhism_visit_todaiji')}.</li>
      <li>Esoteric Buddhism and a night in a temple: {link('/guides/mount-koya/','Mount Koya','buddhism_visit_koya')} and the {link('/guides/koyasan-temple-stay/','Koyasan temple stay guide','buddhism_visit_koyasan_stay')}.</li>
      <li>A mountain that trained many founders: {link('/guides/enryakuji/','Enryaku-ji','buddhism_visit_enryakuji')}.</li>
      <li>A famous Kyoto hall on a hillside: {link('/guides/kiyomizu-dera/','Kiyomizu-dera','buddhism_visit_kiyomizu')}, and Tokyo's {link('/guides/sensoji/','Senso-ji','buddhism_visit_sensoji')}.</li>
      <li>Zen gardens and golden pavilions: {link('/guides/ryoanji/','Ryoan-ji','buddhism_visit_ryoanji')} and {link('/guides/kinkakuji/','Kinkaku-ji','buddhism_visit_kinkakuji')}.</li>
      <li>A pilgrim's route: the {link('/guides/shikoku-pilgrimage/','Shikoku pilgrimage','buddhism_visit_shikoku')}.</li>
    </ul>
    <p>If you want a guided introduction, a local guide can explain the statues in front of you. <a href="{VI}" target="_blank" rel="noopener sponsored" onclick="trackEvent('click','affiliate','viator_buddhism_inline')">Browse guided temple tours in Kyoto on Viator</a>.</p>

    <h2 id="faq">Frequently Asked Questions<span class="h2-jp">よくあるご質問</span></h2>
    <div class="faq-list">
{faq_html}    </div>

    <section id="final">
      <h2>Final Thoughts<span class="h2-jp">おわりに</span></h2>
      <p>If you remember three things: Buddhism came from Korea and China in the 6th century, the main schools are Tendai, Shingon, Pure Land, Zen and Nichiren, and a statue with a crown is a bodhisattva while one in plain robes is a Buddha. With that, the next temple you visit will already make more sense.</p>
    </section>

    <section class="related-section" style="margin-top:56px;">
      <h2>Related Guides<span class="h2-jp">関連ガイド</span></h2>
      <div class="related-grid">
        <a class="related-card" href="/culture/shrine-vs-temple/" onclick="trackEvent('click','internal','related_buddhism_to_shrine_vs_temple')">
          <div class="related-card-label">SACRED JAPAN ／ GUIDE</div>
          <div class="related-card-title">&#9961;&#65039; Shrine vs Temple →</div>
          <div class="related-card-desc">How to tell them apart and how to pray at each.</div>
        </a>
        <a class="related-card" href="/culture/what-is-shinto/" onclick="trackEvent('click','internal','related_buddhism_to_shinto')">
          <div class="related-card-label">SACRED JAPAN ／ GUIDE</div>
          <div class="related-card-title">&#9961;&#65039; What Is Shinto →</div>
          <div class="related-card-desc">The other half of Japanese religious life.</div>
        </a>
        <a class="related-card" href="/guides/temple-stay/" onclick="trackEvent('click','internal','related_buddhism_to_temple_stay')">
          <div class="related-card-label">SACRED JAPAN ／ GUIDE</div>
          <div class="related-card-title">&#127968; Temple Stay Guide →</div>
          <div class="related-card-desc">Sleep, eat and pray in a working temple.</div>
        </a>
      </div>
    </section>

    <p style="font-size:14px;color:var(--enshu);line-height:1.7;margin-top:32px;"><strong>Sources:</strong> history, the 1868 separation and funeral statistics: {ext(WIKI,'Wikipedia, Buddhism in Japan','buddhism_src_wiki')}; schools and dates: {ext(JG,'Japan Guide','buddhism_src_jg')}, {ext(ENC,'Encyclopedia.com','buddhism_src_enc2')}, {ext(UGA,'University of Georgia handout','buddhism_src_uga')} and {ext(COL,'Columbia University overview','buddhism_src_col')}; statue categories: {ext(NIP,'Nippon.com, Encounters with Buddhist Art','buddhism_src_nippon2')}; temple layout: {ext(WHE,'World History Encyclopedia','buddhism_src_whe2')}, {ext(COLL,'The Collector','buddhism_src_collector2')} and {ext(NG,'National Geographic','buddhism_src_ng')}. Follower counts and dates vary by source; treat them as approximate.</p>

  </article>

</main>"""

t=open(f'{R}/_tools/culture/tea.py',encoding='utf-8').read()
tail=t[t.index("s=open(f'{R}/culture/omamori-guide"):]
tail=tail.replace('<div class="hero-bg-kanji">茶道</div>','<div class="hero-bg-kanji">仏教</div>')
tail=tail.replace('<h1>The Japanese <em>Tea Ceremony</em> Guide</h1>','<h1>What Is <em>Buddhism</em> in Japan?</h1>')
tail=tail.replace('<div class="hero-jp">茶道ガイド</div>','<div class="hero-jp">日本の仏教ガイド</div>')
tail=tail.replace('What Happens, What to Do as a Guest, and Where to Try It','Schools, Statues and Temples Explained for Visitors')
tail=tail.replace('Tea Ceremony Guide','What Is Buddhism in Japan')
tail=tail.replace('guide_tea','guide_buddhism').replace('viator_guide_tea_sticky','viator_guide_buddhism_sticky').replace('japanese+tea+ceremony','Kyoto+temple')
tail=re.sub(r'(<meta name="keywords" content=")[^"]*(")',r'\1Buddhism in Japan, Japanese Buddhism, Zen, Pure Land, Shingon, Tendai, Nichiren, Buddha statues, bodhisattva, Kannon, Jizo, Japanese temple guide, Buddhism and Shinto\2',tail)
tail=tail.replace('"datePublished":"2026-11-08","dateModified":"2026-11-08"','"datePublished":"2026-11-27","dateModified":"2026-11-27"')
exec(tail)
