import re, json, os, html
R='/home/claude/sacred-japan'
T=open(R+'/anime/lucky-star/index.html',encoding='utf-8').read()
SLUG='golden-kamuy'
URL='https://sacred-japan.net/anime/golden-kamuy/'
TITLE='Golden Kamuy Pilgrimage: Otaru, Abashiri Prison and the Ainu Culture Behind the Story'
H1='Golden Kamuy Pilgrimage: Otaru, Abashiri and the <em>Ainu</em> Culture Behind the Story'
DESC=("Where is Golden Kamuy in real life? A licensed guide's map of the Hokkaido places behind the story: "
      "Otaru, the Historical Village of Hokkaido, Abashiri Prison Museum, Goryokaku, and Upopoy for the Ainu culture.")
OG='https://sacred-japan.net/images/og/og-anime-golden-kamuy.jpg'
FAQ=[
("Where is Golden Kamuy set in real life?",
 "It is set in Hokkaido in the years after the Russo-Japanese War, and the story also travels to Karafuto (Sakhalin). Fans visit Otaru, the Historical Village of Hokkaido in Sapporo, Abashiri Prison Museum and Goryokaku in Hakodate."),
("Which Golden Kamuy location is best for a first visit?",
 "If you have one day near Sapporo, the Historical Village of Hokkaido and Otaru are the easiest pairing. Abashiri is far to the northeast, so it needs its own trip."),
("Where can I learn about the Ainu culture shown in the series?",
 "Upopoy (National Ainu Museum and Park) in Shiraoi opened in 2020 as a national center for the revival and promotion of Ainu culture. Check the official site for current hours and tickets."),
("Are the filming locations of the live-action film the same as the manga locations?",
 "Only partly. Several buildings at the Historical Village of Hokkaido appear in the live-action film and are also described as models for places in the manga, but the two should not be treated as the same list."),
("Do I need to know the story before visiting?",
 "No. Most of these places are worth a visit on their own, from the Otaru canal district to a prison museum with real history behind it."),
]

def esc(s): return html.escape(s,quote=True)

# ---------- head ----------
head=T[:T.index('<body')]
head=head.replace('Lucky Star Pilgrimage: Washinomiya Shrine, Where Fans Changed a Shrine | Sacred Japan', esc(TITLE)+' | Sacred Japan')
old_desc="Where is the Lucky Star shrine in real life? A licensed guide's visit to Washinomiya Shrine in Saitama, the 2007 fan pilgrimage that changed a shrine, and the festival that followed."
head=head.replace(old_desc,esc(DESC))
head=head.replace('Lucky Star Pilgrimage: The Shrine That Fans Changed',TITLE)
head=head.replace('anime/lucky-star/',f'anime/{SLUG}/').replace('og-anime-lucky-star.jpg','og-anime-golden-kamuy.jpg')
head=head.replace('"datePublished": "2026-11-01"','"datePublished": "2026-11-13"').replace('"dateModified": "2026-11-01"','"dateModified": "2026-11-13"')
# FAQ JSON-LD
faq_ld={"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in FAQ]}
a=head.index('<script type="application/ld+json">\n{\n  "@context": "https://schema.org",\n  "@type": "FAQPage"')
b=head.index('</script>',a)+len('</script>')
head=head[:a]+'<script type="application/ld+json">\n'+json.dumps(faq_ld,indent=2,ensure_ascii=False)+'\n</script>'+head[b:]
head=head.replace('"name": "Lucky Star",','"name": "Golden Kamuy",')

# ---------- nav/mobile menu (reuse) ----------
bs=T.index('<body'); hs=T.index('<!-- ── HERO')
nav=T[bs:hs]

hero=f'''<!-- ── HERO ── -->
<section class="hero">
  <div class="hero-bg-kanji">聖地</div>
  <div class="hero-content">
    <div class="hero-label">SACRED JAPAN ANIME ／ アニメ聖地巡礼</div>
    <h1>{H1}</h1>
    <div class="hero-jp">ゴールデンカムイ 聖地巡礼</div>
    <p class="hero-subtitle">The Hokkaido places behind the gold hunt: an Otaru canal, a pioneer village, a prison museum, and where to meet the real Ainu culture</p>
    <div class="hero-author">
      WRITTEN BY <strong>SACRED JAPAN</strong> ／ LICENSED NATIONAL TOUR GUIDE (ENGLISH)
    </div>
  </div>
</section>

<!-- ── BREADCRUMB ── -->
<div role="navigation" aria-label="Breadcrumb" style="max-width:900px;margin:24px auto 0;padding:0 56px;font-size:15px;letter-spacing:0.5px;color:var(--sumi);">
  <a href="/" style="color:var(--sumi-light);text-decoration:underline;text-underline-offset:3px;" onclick="trackEvent('click','internal','guide_anime_golden_kamuy_to_home')">Home</a>
  <span style="margin:0 8px;color:var(--enshu);">›</span>
  <a href="/anime/" style="color:var(--sumi-light);text-decoration:underline;text-underline-offset:3px;" onclick="trackEvent('click','internal','guide_anime_golden_kamuy_to_hub')">Anime Pilgrimage</a>
  <span style="margin:0 8px;color:var(--enshu);">›</span>
  Golden Kamuy
</div>
'''

TD='padding:10px 12px;border:1px solid #d9c9cd;vertical-align:top;'
TH='padding:10px 12px;border:1px solid #d9c9cd;background:#f6e3e8;text-align:left;'
def table(rows):
    h=''.join(f'<th style="{TH}">{c}</th>' for c in ['In the story','Real place','How solid is it?'])
    b=''.join('<tr>'+''.join(f'<td style="{TD}">{c}</td>' for c in r)+'</tr>' for r in rows)
    return f'<div style="overflow-x:auto;margin:20px 0;"><table style="border-collapse:collapse;width:100%;min-width:620px;font-size:16px;line-height:1.6;"><thead><tr>{h}</tr></thead><tbody>{b}</tbody></table></div>'

rows=[
("Tsurumi's base and the soba shop from a Volume 2 scene","Historical Village of Hokkaido, Sapporo (the soba restaurant was moved there from Otaru)","Reported by SoraNews24 (2024). Several village buildings also appear in the live-action film."),
("Tsurumi tests imported guns (Vol. 4); the Lightning Bandit flees (Vol. 11)","Otaru Museum of History and Nature, near the Otaru Canal (a former warehouse)","Reported by SoraNews24. Matches are the author's, not an official list."),
("Hijikata robs a bank to retrieve a sword (Vol. 4)","Former Otaru Branch of Hyakujusan Bank, now the Otaru Romankan glass shop","Reported by SoraNews24: the twin windows match the scene."),
("A herring mansion interior and the piano scene (Vol. 5)","Former Aoyama Villa (Herring Mansion), Otaru","Reported by SoraNews24. Photography is not allowed inside."),
("The runaway train at the end of the story (Vol. 30)","Otaru City General Museum: the steam locomotive <em>Shizuka</em> inspired the exterior","Reported by SoraNews24 as inspiration, not a direct copy."),
("Sweet dumplings on a skewer (Vol. 2)","Otaru Niikuraya, which sells Hanazono dango","Reported by SoraNews24."),
("The prison where the tattoos begin the hunt for the gold","Abashiri Prison Museum, Abashiri","Widely cited. The museum covers the real prisoners who helped build Hokkaido's roads. A 2026 film about the Abashiri arc is listed on Wikipedia."),
("Hakodate and the final fort","Goryokaku, Hakodate","Widely cited. Hijikata Toshizo appears in the story; our <a class=\"inline-link\" href=\"/guides/goryokaku/\">Goryokaku guide</a> covers the real history."),
]

main=f'''<!-- ── MAIN ── -->
<main>

  <!-- TABLE OF CONTENTS -->
  <aside class="toc" aria-label="Table of contents">
    <div class="toc-label">TABLE OF CONTENTS ／ 目次</div>
    <div class="toc-title">In This Guide</div>
    <ol>
      <li><a href="#opening">Introduction</a></li>
      <li><a href="#scenes">Scene to Place: What You Can Visit</a></li>
      <li><a href="#otaru">Otaru: The Canal, the Bank and the Herring Mansion</a></li>
      <li><a href="#village">Historical Village of Hokkaido</a></li>
      <li><a href="#abashiri">Abashiri Prison Museum</a></li>
      <li><a href="#hakodate">Hakodate and Goryokaku</a></li>
      <li><a href="#ainu">Meeting the Real Ainu Culture</a></li>
      <li><a href="#local">Plan Your Trip</a></li>
      <li><a href="#faq">FAQ</a></li>
    </ol>
  </aside>

  <article>

    <section id="opening">
      <p class="opening">Most anime pilgrimages are about one shrine or one street. <em>Golden Kamuy</em> is different: it is a map of an entire island. Satoru Noda's manga, serialized in Weekly Young Jump from 2014 to 2022, follows a veteran of the Russo-Japanese War and an Ainu girl across Hokkaido in search of hidden gold. As a guide, I like it because every stop is a real place with real history, and because it has sent a lot of visitors toward the Ainu culture, which is the part of Hokkaido I most want you to meet.</p>
    </section>

    <div class="key-callout">
      <p><strong>💡 Quick Visitor Snapshot</strong></p>
      <ul>
        <li><strong>Easiest pairing:</strong> Otaru and the Historical Village of Hokkaido, both within reach of Sapporo.</li>
        <li><strong>Furthest stop:</strong> Abashiri Prison Museum in northeastern Hokkaido, facing the Sea of Okhotsk. Plan it as its own trip.</li>
        <li><strong>For the Ainu culture:</strong> Upopoy in Shiraoi, near Chitose Airport.</li>
        <li><strong>Best season:</strong> Summer for horse-drawn carriages at the village, winter for the snow scenes and horse-drawn sleighs.</li>
      </ul>
    </div>

    <h2 id="scenes">Scene to Place: What You Can Visit</h2>
    <p>Most matches below come from fan and travel writers rather than from the author. I have marked how solid each one is, and I am not inventing a complete official list.</p>{table(rows)}<p>One honest limit: volume numbers in this table follow the SoraNews24 article. If you are following the anime rather than the manga, scenes may sit in different episodes.</p>

    <h2 id="otaru">Otaru: The Canal, the Bank and the Herring Mansion</h2>
    <p>Otaru is where I would start. It has a history of Ainu settlements and a 19th-century herring boom that built grand fishermen's houses called <em>banya</em>. SoraNews24 describes Otaru as close to Asirpa's village and as Lieutenant Tsurumi's base of operations in the story, and says the author modeled many locations on real Otaru buildings.</p>
    <p>Walk the canal area first, then go five minutes to the former bank that is now the Otaru Romankan glass shop. Finish with a sweet dumpling at Otaru Niikuraya. The Former Aoyama Villa, the Herring Mansion, has an attached restaurant that serves herring soba, but photography is not allowed inside, so do not plan your photo stop there. For opening hours and fees, check each facility's official page, since the SoraNews24 article does not give them.</p>

    <h2 id="village">Historical Village of Hokkaido</h2>
    <p>This open-air museum on the edge of Sapporo holds relocated and restored buildings from Hokkaido's Meiji to early Showa years. Many buildings appear in the manga, including a soba shop, a hotel and a barber shop, and a winter night scene with a horse-drawn sleigh in the live-action film was shot here. Horse-drawn carriages run in summer and sleighs in winter. The village is about 30 minutes by car from central Sapporo, according to one local travel site; check the official page for the bus route and tickets.</p>
    <p>If you only have a day near Sapporo, this is the stop that feels most like walking into a page of the manga.</p>

    <h2 id="abashiri">Abashiri Prison Museum</h2>
    <p>The story begins with tattoos on prisoners' bodies that, together, show where the gold is hidden. The real Abashiri Prison in northeastern Hokkaido is now open as a museum about the prisoners who built roads and other facilities that helped develop the island. Treat it as a history museum first. The story is fiction; the labor was real.</p>
    <p>Abashiri is far from Sapporo, so I would not squeeze it into a day trip. Plan a night or two in the area.</p>

    <h2 id="hakodate">Hakodate and Goryokaku</h2>
    <p>The final chapters are tied to Hakodate, and the star-shaped Goryokaku fort, Japan's first Western-style fortress, is shown in the story. Hijikata Toshizo, who in history was a real commander of the last battle of the Boshin War, appears here as a living character. I would not try to match specific scenes; go for the fort itself. Our full <a class="inline-link" href="/guides/goryokaku/">Goryokaku guide</a> covers the real history, the tower and the cherry blossoms.</p>

    <h2 id="ainu">Meeting the Real Ainu Culture</h2>
    <p><em>Kamuy</em> is the Ainu word for deities, and the Ainu are the indigenous people of Hokkaido. The manga's Ainu language was supervised by Hiroshi Nakagawa, an Ainu-language linguist at Chiba University, and the series has been recognized for its social impact: it won the Social Impact Award in the Manga Division at the 24th Japan Media Arts Festival.</p>
    <p>A manga is still a manga, so if you want to learn about the Ainu people and their culture, go to a place built for that. Upopoy, the National Ainu Museum and Park in Shiraoi, opened in 2020 as a national center for the revival and promotion of Ainu culture. A tourism campaign tied to the series ran there from September 2025 to February 2026, but check the official site for current exhibitions, hours and tickets. Please go as a guest and listen first.</p>

    <h2 id="local">Plan Your Trip</h2>
    <p>Sapporo is the natural base for Otaru, the village and Upopoy. For Abashiri or Hakodate, plan separate legs.</p><div style="background:#fff;border-left:4px solid var(--beni);border-radius:4px;padding:18px 22px;margin:28px 0;box-shadow:0 1px 6px rgba(0,0,0,.06);">
      <p style="margin:0 0 6px;"><strong>Planning Your Trip?</strong><br>
      Find a place to stay in Sapporo, or add a local guided tour to your day.</p>
      <a href="https://expedia.com/affiliate?siteid=1&amp;landingPage=https%3A%2F%2Fwww.expedia.co.jp%2FHotel-Search%3Fdestination%3DSapporo%252C%2BHokkaido%252C%2BJapan&amp;camref=1101l5JmFa&amp;creativeref=1011l87782&amp;adref=PZf6lQ77e8" target="_blank" rel="noopener sponsored" onclick="trackEvent('click','affiliate','expedia_anime_goldenkamuy_local')" style="display:inline-block;padding:10px 18px;border-radius:6px;color:#fff;font-weight:600;text-decoration:none;margin:6px 8px 0 0;background:#00355f;">Find Stays in Sapporo →</a>
      <a href="https://www.viator.com/search/Otaru?pid=P00298374&amp;mcid=42383&amp;medium=link&amp;campaign=sacred-japan" target="_blank" rel="noopener sponsored" onclick="trackEvent('click','affiliate','viator_anime_goldenkamuy_local')" style="display:inline-block;padding:10px 18px;border-radius:6px;color:#fff;font-weight:600;text-decoration:none;margin:6px 8px 0 0;background:#c0392b;">Book a Tour from Otaru →</a>
    </div>

    <h2 id="faq">Frequently Asked Questions</h2>
    <div class="faq-stack">
{''.join(f"""    <details class="faq-item">
      <summary>{esc(q)}</summary>
      <div class="faq-answer">{esc(a)}</div>
    </details>
""" for q,a in FAQ)}  </div>

    <div class="closing-block">
      <span class="torii">⛩️</span>
      <p>The gold in the story is fiction, but the roads, the canal and the culture behind it are real. Follow the map, and then spend an hour at Upopoy listening to the people the story borrows from.</p>
    </div>

    <!-- RELATED GUIDES -->
    <section class="related-section">
      <h2>Related Guides</h2>
      <span class="h2-jp">関連ガイド</span>

      <div class="related-grid">

        <a class="related-card" href="/guides/goryokaku/" onclick="trackEvent('click','internal','related_anime_golden_kamuy_to_goryokaku')">
          <div class="related-card-label">SACRED JAPAN ／ GUIDE</div>
          <div class="related-card-title">🏯 Goryokaku Guide: Hakodate's Star Fort →</div>
          <div class="related-card-desc">The fort in the final chapters, the Republic of Ezo and the last battle of the Boshin War.</div>
        </a>

        <a class="related-card" href="/anime/" onclick="trackEvent('click','internal','related_anime_golden_kamuy_to_hub')">
          <div class="related-card-label">SACRED JAPAN ／ HUB</div>
          <div class="related-card-title">🎬 Anime Pilgrimage Guides →</div>
          <div class="related-card-desc">More real places behind your favorite anime, with how to get there.</div>
        </a>

        <a class="related-card" href="/anime/lucky-star/" onclick="trackEvent('click','internal','related_anime_golden_kamuy_to_lucky_star')">
          <div class="related-card-label">SACRED JAPAN ／ GUIDE</div>
          <div class="related-card-title">🎬 Lucky Star: The Shrine Fans Changed →</div>
          <div class="related-card-desc">Another pilgrimage where fans became part of a place's story.</div>
        </a>

        <a class="related-card" href="/culture/samurai-and-ninja/" onclick="trackEvent('click','internal','related_anime_golden_kamuy_to_samurai_ninja')">
          <div class="related-card-label">SACRED JAPAN ／ GUIDE</div>
          <div class="related-card-title">⚔️ Samurai and Ninja →</div>
          <div class="related-card-desc">Armor, swords and the real history behind the warriors.</div>
        </a>

      </div>
    </section>

  </article>

</main>

'''
tail=T[T.index('<!-- ── AI IMAGERY NOTE'):]
tail=tail.replace('lucky_star','golden_kamuy')
out=head+nav+hero+'\n'+main+tail
os.makedirs(R+'/anime/golden-kamuy',exist_ok=True)
open(R+'/anime/golden-kamuy/index.html','w',encoding='utf-8').write(out)
print(len(out))
