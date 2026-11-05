import re,json,os,glob
from PIL import Image,ImageDraw,ImageFont
R='/home/claude/sacred-japan/'; SL='sendai-castle'
s=open(R+'guides/kochi-castle/index.html',encoding='utf-8').read()
i=s.index('<main>'); j=s.index('</main>'); head,tail=s[:i],s[j:]
TITLE="Sendai Castle (Aoba Castle) Guide: Masamune's Keepless Hilltop Fort, the Stone Walls and the Loople Bus"
DESC="A licensed guide's guide to Sendai Castle (Aoba Castle ruins): Date Masamune's hilltop fort with no keep, the stone walls, the reconstructed turret, the mounted statue, the Aoba Castle Museum, fees and the Loople bus from the station."
TAG='A hilltop fort without a keep, Date Masamune on horseback and a view over Sendai, a short bus ride from the station.'
head=re.sub(r'<title>.*?</title>',f'<title>{TITLE} | Sacred Japan</title>',head,count=1)
head=re.sub(r'(<meta (?:name="description"|property="og:description"|name="twitter:description") content=")[^"]*(")',lambda m:m.group(1)+DESC+m.group(2),head)
head=re.sub(r'(<meta (?:property="og:title"|name="twitter:title") content=")[^"]*(")',lambda m:m.group(1)+TITLE+m.group(2),head)
head=re.sub(r'("headline": ")[^"]*(")',lambda m:m.group(1)+TITLE+m.group(2),head)
head=re.sub(r'("description": ")A licensed[^"]*(")',lambda m:m.group(1)+DESC+m.group(2),head)
head=re.sub(r'("date(?:Published|Modified)": ")[^"]*(")',lambda m:m.group(1)+'2026-11-05'+m.group(2),head)
head=re.sub(r'<meta name="keywords" content="[^"]*">','<meta name="keywords" content="Sendai Castle, Aoba Castle, Date Masamune, Sendai Castle ruins, Aoba Castle ruins, Date Masamune statue, Loople Sendai bus, Aoba Castle Museum, Sendai sightseeing, Japan castles">',head)
head=head.replace('guides/kochi-castle','guides/sendai-castle').replace('guide_kochi_','guide_sendai_castle_').replace('og-guides-kochi-castle','og-guides-sendai-castle')
head=head.replace('高知城','仙台城').replace('Kochi Castle','Sendai Castle')
head=re.sub(r"<h1>.*?</h1>","<h1><em>Sendai Castle</em>: Masamune&rsquo;s Keepless Hilltop Fort, the Stone Walls and the Loople Bus</h1>",head,count=1,flags=re.S)
head=head.replace("Shikoku's original keep, and the only castle where the lord's palace still stands beside it.",TAG)
faqs=[
("Is there a castle building at Sendai Castle?","No keep or main hall survives. Japan Visitor says the stone walls are all that remain of the original castle, plus a reconstructed turret. GLTJP describes that turret as the reconstructed side turret (wakiyagura) of the Otemon Gate, and Tokyo Weekender adds that the foundations of the Ohiroma hall are marked on the ground."),
("How much does it cost to visit?","The grounds are free (GLTJP, Tokyo Weekender). The Aoba Castle Museum is 770 yen for adults, 550 yen for junior and senior high school students and 330 yen for elementary students (GLTJP, Tokyo Weekender). The VR experience is 880 yen (japan-guide, GLTJP), though Nippon.com says 500 yen, and japan-guide lists a set ticket at 1,430 yen. Please check the day&rsquo;s prices."),
("Why does Sendai Castle have no keep?","Nippon.com says Masamune built no keep, reportedly to avoid arousing the Tokugawa shogunate&rsquo;s suspicions. Japan Visitor says a keep was planned but never built, and gives no reason. I would call the suspicion theory a reported explanation rather than a settled fact."),
("How do I get there from Sendai Station?","The Loople Sendai bus takes about 20 minutes to stop 6 for the castle grounds, or stop 5 for the Sendai City Museum (japan-guide). Tokyo Weekender says 20 to 25 minutes and gives the boarding point as Bus Pool Stop 16 at the West Exit. A single ride is 260 yen and a day pass is 630 yen (japan-guide, Tokyo Weekender). The Tozai subway to Kokusai Center takes about 5 minutes and 210 yen, followed by a walk of about 20 minutes uphill (japan-guide, Tokyo Weekender); GLTJP says 15 minutes."),
("How long should I allow?","That depends on whether you go into the museum, so this is my own estimate: about an hour for the grounds, the statue and the view, and a further hour for the museum. japan-guide says it is a 10 to 15 minute walk between the castle grounds and the Sendai City Museum if you want to combine them."),
("Can I visit at night?","Tokyo Weekender lists the site as open 24 hours and says the equestrian statue of Date Masamune is illuminated nightly until 22:00. GLTJP also says the statue is lit at night. I found those times in one source only, so please check before you plan an evening visit."),
]
faq_json=',\n'.join('''    {
      "@type": "Question",
      "name": %s,
      "acceptedAnswer": {
        "@type": "Answer",
        "text": %s
      }
    }'''%(json.dumps(q),json.dumps(re.sub('&rsquo;',"'",a))) for q,a in faqs)
head=re.sub(r'("mainEntity": \[\n).*?(\n  \]\n\}\n</script>\n\n<!-- ── GOOGLE)',lambda m:m.group(1)+faq_json+m.group(2),head,flags=re.S)
hh=re.sub(r'"mainEntity": \[.*','',head,flags=re.S)
assert not re.search('Kochi|Shikoku|kochi|Kanazawa|Shuri|Naha|Takeda|Asago|Machu|Odawara|Hojo|Aizu|Tsuruga|Goryokaku|Hakodate|Ezo',hh),re.findall('.{30}(?:Kochi|Shikoku|Kanazawa|Shuri|Naha|Aizu|Tsuruga|Goryokaku|Hakodate).{20}',hh)
IL='class="inline-link"'
main='''<main>

  <!-- TABLE OF CONTENTS -->
  <aside class="toc" aria-label="Table of contents">
    <div class="toc-label">TABLE OF CONTENTS ／ 目次</div>
    <div class="toc-title">In This Guide</div>
    <ol>
      <li><a href="#opening">A Castle Without a Castle</a></li>
      <li><a href="#history">Why Mount Aoba?</a></li>
      <li><a href="#fall">Fire, Demolition and the 1945 Raid</a></li>
      <li><a href="#see">What You Can See Today</a></li>
      <li><a href="#visit">Visiting Sendai Castle</a></li>
      <li><a href="#stay">Making It a Trip</a></li>
      <li><a href="#faq">Frequently Asked Questions</a></li>
      <li><a href="#final">Before You Go Up the Hill</a></li>
    </ol>
  </aside>

  <article>

    <section id="opening">
      <p class="opening">As a licensed guide, I always warn visitors about Sendai Castle before they board the bus: there is no castle to see. No keep, no main hall, no moat full of carp. What you get instead is a hilltop of massive stone walls, one reconstructed turret, an equestrian statue of the man who built it all, and a view over a city that he planned from this spot. For many people that turns out to be a better story than another white keep.</p>
      <p>This guide covers why Date Masamune chose this hill, why he never built a keep, how the site was lost, what remains, and the practical details of the Loople bus and the museum. Where my sources disagree I say so, and I mark claims I found in only one place.</p>
    </section>

    <h2 id="history">Why Mount Aoba?<span class="h2-jp">なぜ青葉山なのか</span></h2>
    <p>Nippon.com says Date Masamune was born at Yonezawa Castle, lost his right eye to smallpox as a child and earned the nickname Dokuganryu, the &ldquo;One-eyed Dragon.&rdquo; He sided with the Tokugawa forces at Sekigahara in 1600 and was later awarded the Sendai domain, which Nippon.com ranks third in wealth at 620,000 koku. Building began on Mount Aoba soon afterwards, but the sources give different years: japan-guide says 1600, Nippon.com and Tokyo Weekender say 1601, and Japan Visitor says 1602 and adds that Masamune&rsquo;s second son Tadamune completed it in 1637. I would say simply &ldquo;around 1601.&rdquo;</p>
    <p>The hill itself explains the choice. Nippon.com describes a wooded hill with the Hirose River to the north and east, the Tatsunokuchi Gorge to the south and deep forest to the west. The height above the town is given as about 100 metres by japan-guide, about 115 metres by Tokyo Weekender and 130 metres by Nippon.com, so I would just call it a steep hill above the city. GLTJP says the castle sat on a natural fort with cliffs to the east and south, and that it was the centre of clan government for 270 years; Tokyo Weekender says &ldquo;nearly 270 years.&rdquo;</p>
    <p>The question everyone asks is about the keep. Nippon.com says Masamune built no keep, reportedly to avoid arousing the Tokugawa shogunate&rsquo;s suspicions. Japan Visitor says a keep was planned but never built and gives no reason. Please treat the suspicion story as a reported explanation, not a settled fact.</p>

    <h2 id="fall">Fire, Demolition and the 1945 Raid<span class="h2-jp">焼失と取り壊し</span></h2>
    <p>Tokyo Weekender says earthquakes and fires damaged the castle repeatedly in the Edo period and that much of it was dismantled after the Meiji Restoration. GLTJP says the army used the site and demolished many buildings. japan-guide and Japan Visitor both mention a major fire in 1882. What remained was destroyed by air raids in World War II; Tokyo Weekender dates the raid to 10 July 1945, a date I found in one source only. GLTJP says that most of the remaining structures, including the Otemon Gate, were lost in the Sendai air raids.</p>
    <p>The ruins became a National Historic Site in 2003 and the castle was named one of Japan&rsquo;s 100 Fine Castles in 2006, according to Tokyo Weekender; again, I found those two dates in one source only.</p>

    <h2 id="see">What You Can See Today<span class="h2-jp">見どころ</span></h2>
    <p>The first thing is the <strong>stone walls</strong>. Nippon.com says one stretch rises to 17 metres, and japan-guide and Japan Visitor both call the walls what remains of the original. They are the best reason to come up the hill.</p>
    <p>Next is the <strong>reconstructed turret</strong>. GLTJP calls it the reconstructed side turret (wakiyagura) of the Otemon Gate and its photo caption says it was restored in 1964; Nippon.com says it is a replica built in 1967 and that the original was destroyed in the wartime bombing. I would say &ldquo;a postwar reconstruction in the mid-1960s.&rdquo; GLTJP also mentions an earthen wall on the north side of the gate, and Tokyo Weekender says the foundations of the Ohiroma hall are marked on the ground.</p>
    <p>Then there is the <strong>equestrian statue of Date Masamune</strong>, which GLTJP calls a symbol of Sendai and says is illuminated at night; Tokyo Weekender says the lights stay on until 22:00. From the high ground you look out over the city that GLTJP calls the &ldquo;City of Trees,&rdquo; and Tokyo Weekender says the view reaches the Pacific on clear summer days (one source only).</p>
    <p>The <strong>Aoba Castle Museum</strong> is next to the park. GLTJP says it shows actual materials, dioramas and CG reconstructions, and japan-guide describes models of the Edo-period castle, artefacts, a short Japanese-language film and VR goggles for a virtual walk. Tokyo Weekender adds armour, swords and documents written by Masamune. Be aware that the film is in Japanese (japan-guide).</p>
    <p>Two neighbours are worth knowing. Gokoku Shrine stands on the site of the inner compound (Nippon.com, GLTJP); Japan Visitor says it was established in 1902, honours Japan&rsquo;s war dead and has a small military history museum, and japan-guide says its museum has no English information. The Sendai City Museum stands on the outermost compound and holds about 97,000 items (Nippon.com); japan-guide gives admission as 460 yen and says it is closed on Mondays.</p>

    <h2 id="visit">Visiting Sendai Castle<span class="h2-jp">アクセス</span></h2>
    <ul class="practical-list"><li><strong>Grounds:</strong> free (GLTJP, Tokyo Weekender). Tokyo Weekender lists them as open 24 hours.</li><li><strong>Aoba Castle Museum hours:</strong> 9:00 to 17:00, or to 16:00 from November to March (japan-guide, GLTJP). Last entry is 20 minutes before closing (japan-guide) or 30 minutes (GLTJP). japan-guide says it is open every day, but the VR experience is not available on Wednesdays (one source only).</li><li><strong>Museum fees:</strong> adults 770 yen, junior and senior high school 550 yen, elementary 330 yen (GLTJP, Tokyo Weekender). VR 880 yen (japan-guide, GLTJP); Nippon.com says 500 yen. japan-guide lists a set ticket at 1,430 yen and says Loople day-pass holders get 110 yen off the museum or set ticket.</li><li><strong>Loople Sendai bus:</strong> from Sendai Station, about 20 minutes (japan-guide) or 20 to 25 minutes (Tokyo Weekender), to stop 6 for the grounds or stop 5 for the Sendai City Museum. Single ride 260 yen, day pass 630 yen (japan-guide, Tokyo Weekender).</li><li><strong>Subway:</strong> the Tozai Line to Kokusai Center takes about 5 minutes and 210 yen, followed by a walk uphill of about 20 minutes (japan-guide, Tokyo Weekender) or 15 minutes (GLTJP).</li><li><strong>Car:</strong> GLTJP says about 15 minutes from Sendai Miyagi IC.</li><li><strong>Time needed:</strong> my own estimate is an hour for the grounds, statue and view, plus about an hour for the museum.</li></ul>

    <h2 id="stay">Making It a Trip<span class="h2-jp">滞在</span></h2>
    <p>Sendai Castle works well as half a day in Sendai. If you like castles with a story from this region, our <a href="/guides/aizuwakamatsu-castle/" '''+IL+''' onclick="trackEvent('click','internal','guide_sendai_castle_to_aizuwakamatsu')">Aizuwakamatsu Castle guide</a> covers the Tohoku castle that fell in the Boshin War, and our <a href="/guides/hirosaki-castle/" '''+IL+''' onclick="trackEvent('click','internal','guide_sendai_castle_to_hirosaki')">Hirosaki Castle guide</a> covers the one that still has an original keep.</p>
    <div class="key-callout">
      <p>&#127890; <strong>Plan your trip:</strong> Browse guided tours or plan a stay around Sendai. <a href="https://www.viator.com/search/Sendai?pid=P00298374&amp;mcid=42383&amp;medium=link&amp;campaign=sacred-japan" target="_blank" rel="noopener sponsored" onclick="trackEvent('click','affiliate','viator_sendai_castle_local')">Browse Sendai tours &rarr;</a></p>
    </div>

    <h2 id="faq">Frequently Asked Questions<span class="h2-jp">よくあるご質問</span></h2>
    <div class="faq-stack">
'''+''.join(f'''    <details class="faq-item">
        <summary>{q}</summary>
        <div class="faq-answer">{a}</div>
    </details>
''' for q,a in faqs)+'''    </div>

    <h2 id="final">Before You Go Up the Hill<span class="h2-jp">むすびに</span></h2>
    <p>Go for the walls and the view, not for a building, and the visit will feel right. Stand beside the statue, look down at the city Masamune laid out below, and then walk back along the stone to the turret.</p>

    <div class="closing-block">
      <span class="torii">&#9961;&#65039;</span>
      <p>A castle without a keep, and a view that never needed one.</p>
    </div>

    <!-- RELATED GUIDES -->
    <section class="related-section">
      <h2>Related Guides</h2>
      <span class="h2-jp">関連ガイド</span>

      <div class="related-grid">

        <a class="related-card" href="/guides/aizuwakamatsu-castle/" onclick="trackEvent('click','internal','related_sendai_castle_to_aizuwakamatsu')">
          <div class="related-card-label">SACRED JAPAN ／ GUIDES</div>
          <div class="related-card-title">&#127983; Aizuwakamatsu Castle Guide &rarr;</div>
          <div class="related-card-desc">The red-roofed keep and the 1868 siege.</div>
        </a>

        <a class="related-card" href="/guides/hirosaki-castle/" onclick="trackEvent('click','internal','related_sendai_castle_to_hirosaki')">
          <div class="related-card-label">SACRED JAPAN ／ GUIDES</div>
          <div class="related-card-title">&#127983; Hirosaki Castle Guide &rarr;</div>
          <div class="related-card-desc">Tohoku&rsquo;s original keep, being moved on its base.</div>
        </a>

        <a class="related-card" href="/castles/" onclick="trackEvent('click','internal','related_sendai_castle_to_castles')">
          <div class="related-card-label">SACRED JAPAN ／ CASTLES</div>
          <div class="related-card-title">&#127983; Japan's Castles &rarr;</div>
          <div class="related-card-desc">Every castle guide, with photos and official links.</div>
        </a>

      </div>
    </section>

  </article>

'''
tail=tail.replace('kochi-castle',SL).replace('_kochi_','_sendai_castle_').replace('DKochi','DSendai').replace('search/Kochi','search/Sendai')
def L(u,l,t): return f'<a href="{u}" target="_blank" rel="noopener" style="color:var(--beni);text-decoration:underline;" onclick="trackEvent(\'click\',\'external\',\'{l}\')">{t}</a>'
src='Sources verified at time of writing: '+', '.join([
 L('https://japan-guide.com/e/e5152.html','src_sendai_jg','japan-guide'),
 L('https://www.gltjp.com/en/directory/item/13010/','src_sendai_gltjp','GLTJP'),
 L('https://nippon.com/en/guide-to-japan/gu900153','src_sendai_nippon','Nippon.com'),
 L('https://www.japanvisitor.com/japanese-castles/aoba-castle','src_sendai_jv','Japan Visitor'),
 L('https://www.tokyoweekender.com/location/sendai-castle-aoba-castle-ruins/','src_sendai_tw','Tokyo Weekender'),
])+'. Hours, prices and availability change'
tail,n=re.subn(r'Sources verified at time of writing:.*?Hours, prices and availability change',lambda m:src,tail,flags=re.S); assert n==1
out=head+main+tail
assert not re.search('Kochi|Shikoku|kochi|Kanazawa|Shuri|Naha|Takeda Castle|Asago|Machu|Goryokaku Tower|Republic of Ezo',re.sub(r'"mainEntity": \[.*','',out,flags=re.S)),re.findall('.{30}(?:Kochi|Kanazawa|Shuri|Naha|Asago|Machu).{20}',out)
os.makedirs(R+f'guides/{SL}',exist_ok=True); open(R+f'guides/{SL}/index.html','w',encoding='utf-8').write(out)
for tg in ['div','figure','picture','p','a','ul','li','details','section','h2']:
    assert len(re.findall(f'<{tg}[ >]',out))==len(re.findall(f'</{tg}>',out)),tg
for m in re.findall(r'<script type="application/ld\+json">(.*?)</script>',out,re.S): json.loads(m)
im=Image.open(R+'images/og/og-guides-matsue-castle.jpg').convert('RGB'); d=ImageDraw.Draw(im)
d.rectangle([40,150,1170,380],fill=(252,240,242)); d.rectangle([1118,66,1160,96],fill=(252,240,242))
f1=ImageFont.truetype(glob.glob('/usr/share/fonts/**/DejaVuSerif-Bold.ttf',recursive=True)[0],48)
f2=ImageFont.truetype(glob.glob('/usr/share/fonts/**/NotoSerifCJK-Bold.ttc',recursive=True)[0],28,index=0)
l1="Sendai Castle Guide:"; l2="Masamune's Hilltop, No Keep"; print(d.textlength(l2,font=f1),d.textlength(l1,font=f1)); assert d.textlength(l2,font=f1)<1090
d.text((66,170),l1,font=f1,fill=(26,15,15)); d.text((66,238),l2,font=f1,fill=(26,15,15)); d.text((66,332),"仙台城",font=f2,fill=(138,125,120))
im.save(R+f'images/og/og-guides-{SL}.jpg',quality=88); print('built',len(out))
