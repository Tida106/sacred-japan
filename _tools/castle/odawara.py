import re,json,os,glob
from PIL import Image,ImageDraw,ImageFont
R='/home/claude/sacred-japan/'; SL='odawara-castle'
s=open(R+'guides/kochi-castle/index.html',encoding='utf-8').read()
i=s.index('<main>'); j=s.index('</main>'); head,tail=s[:i],s[j:]
TITLE="Odawara Castle Guide: The Hojo Stronghold, a 1960 Keep and the Ninja Museum"
DESC="A licensed guide's guide to Odawara Castle in Kanagawa: the Hojo clan and the 1590 siege, the rebuilt keep, the samurai and ninja museums, cherry blossoms, fees and the walk from Odawara Station."
TAG="A 1960 reconstructed keep on the site of the Later Hojo stronghold in Odawara, ten minutes on foot from the station."
head=re.sub(r'<title>.*?</title>',f'<title>{TITLE} | Sacred Japan</title>',head,count=1)
head=re.sub(r'(<meta (?:name="description"|property="og:description"|name="twitter:description") content=")[^"]*(")',lambda m:m.group(1)+DESC+m.group(2),head)
head=re.sub(r'(<meta (?:property="og:title"|name="twitter:title") content=")[^"]*(")',lambda m:m.group(1)+TITLE+m.group(2),head)
head=re.sub(r'("headline": ")[^"]*(")',lambda m:m.group(1)+TITLE+m.group(2),head)
head=re.sub(r'("description": ")A licensed[^"]*(")',lambda m:m.group(1)+DESC+m.group(2),head)
head=re.sub(r'("date(?:Published|Modified)": ")[^"]*(")',lambda m:m.group(1)+'2026-11-04'+m.group(2),head)
head=re.sub(r'<meta name="keywords" content="[^"]*">','<meta name="keywords" content="Odawara Castle, Odawara Jo, Hojo clan, Odawara Kanagawa, Odawara Castle hours, Odawara Castle ninja museum, Odawara castle cherry blossoms, Hakone day trip">',head)
head=head.replace('guides/kochi-castle','guides/odawara-castle').replace('guide_kochi_','guide_odawara_').replace('og-guides-kochi-castle','og-guides-odawara-castle')
head=head.replace('高知城','小田原城').replace('Kochi Castle','Odawara Castle')
head=re.sub(r"<h1>.*?</h1>","<h1><em>Odawara Castle</em>: The Hojo Stronghold, a 1960 Keep and the Ninja Museum</h1>",head,count=1,flags=re.S)
head=head.replace("Shikoku's original keep, and the only castle where the lord's palace still stands beside it.",TAG)
faqs=[
("How much does it cost to enter Odawara Castle?","The main keep is 510 yen for adults and 200 yen for elementary and junior high students (japan-guide, Jeepe). The Ninja Museum is 310 yen and the Samurai Museum 200 yen, and a keep-plus-both-museums ticket is listed at 610 yen by japan-guide. Jeepe lists a keep-plus-Samurai-Museum combo at 610 yen, so the exact bundle differs between sources. The city's older English page shows 500 yen for the keep, which looks out of date. Please confirm at the gate or on the official site."),
("What are the opening hours of Odawara Castle?","The keep and the museums are open 9:00 to 17:00, with last entry at 16:30 (japan-guide, Jeepe, the city page). The keep is closed on the second Wednesday of December and on 31 December and 1 January; the museums close only on 31 December and 1 January (japan-guide)."),
("How do I get to Odawara Castle from Tokyo?","Odawara Station is about 35 minutes from Tokyo Station by Shinkansen (Jeepe), or about 75 minutes from Shinjuku on the Odakyu Romancecar (Jeepe; the same article also says about 1 hour 20 minutes elsewhere). From the station's East Exit the castle is a walk of about 10 minutes (japan-guide, Jeepe)."),
("How long should I spend at Odawara Castle?","japan-guide suggests 20 to 40 minutes for the keep itself, and Jeepe suggests 30 minutes to 1 hour for the keep, or 1.5 to 2 hours for the whole park with both museums. Add more time in cherry blossom season."),
("Is Odawara Castle an original castle?","The keep is not. It is a ferro-concrete reproduction built in 1960 from Edo-period drawings and models (japan-guide, Jeepe). The keep and other buildings were dismantled and sold in 1870 (japan-guide). The three main gates were restored in the following years."),
("When are the cherry blossoms at Odawara Castle?","Late March to early April (japan-guide, Jeepe). Jeepe counts about 300 Somei Yoshino trees, says the park is on Japan's Top 100 cherry blossom list, and says there are evening illuminations during the season. Dates move with the weather."),
("Can I combine Odawara Castle with Hakone?","Yes. Odawara is the usual gateway to Hakone, and both japan-guide and Jeepe suggest pairing them. The castle works well as a first stop before heading up into the mountains."),
]
faq_json=',\n'.join('''    {
      "@type": "Question",
      "name": %s,
      "acceptedAnswer": {
        "@type": "Answer",
        "text": %s
      }
    }'''%(json.dumps(q),json.dumps(a)) for q,a in faqs)
head=re.sub(r'("mainEntity": \[\n).*?(\n  \]\n\}\n</script>\n\n<!-- ── GOOGLE)',lambda m:m.group(1)+faq_json+m.group(2),head,flags=re.S)
hh=re.sub(r'"mainEntity": \[.*','',head,flags=re.S)
assert not re.search('Kochi|Shikoku|kochi|Kanazawa|Shuri|Naha|Takeda|Asago|Machu',hh),re.findall('.{30}(?:Kochi|Shikoku|Kanazawa|Shuri|Naha|Takeda|Asago|Machu).{20}',hh)
main='''<main>

  <!-- TABLE OF CONTENTS -->
  <aside class="toc" aria-label="Table of contents">
    <div class="toc-label">TABLE OF CONTENTS ／ 目次</div>
    <div class="toc-title">In This Guide</div>
    <ol>
      <li><a href="#opening">The Gateway Castle</a></li>
      <li><a href="#history">The Hojo, Hideyoshi and 1590</a></li>
      <li><a href="#keep">The Keep and the Museums</a></li>
      <li><a href="#grounds">Gates, Moat and Cherry Blossoms</a></li>
      <li><a href="#visit">Visiting Odawara Castle</a></li>
      <li><a href="#stay">Making It a Trip</a></li>
      <li><a href="#faq">Frequently Asked Questions</a></li>
      <li><a href="#final">Before You Board the Hakone Train</a></li>
    </ol>
  </aside>

  <article>

    <section id="opening">
      <p class="opening">As a licensed guide, I tell visitors that Odawara Castle is the one most people see from the Shinkansen window and then forget about. That is a mistake. This was the headquarters of the Later Hojo clan, who ruled the Kanto region from here for about a century, and it fell to Toyotomi Hideyoshi in 1590. The keep you climb today is a reproduction, but the story under it is not.</p>
      <p>This guide covers the history, what is actually inside the keep and the two small museums, the cherry blossoms, and the practical details. Where my sources disagree, I say so, and I mark claims I found in only one place.</p>
    </section>

    <h2 id="history">The Hojo, Hideyoshi and 1590<span class="h2-jp">北条氏と小田原攻め</span></h2>
    <p>Jeepe says the site began as a fortress built by the Omori clan in the mid-15th century, and that Hojo Soun took it around 1500. The city's English page agrees that an Omori predecessor stood here and that it became the seat of the Odawara Hojo in the Warring States period. Jeepe puts the Later Hojo rule at about 100 years across five generations.</p>
    <p>In 1590 Toyotomi Hideyoshi attacked and defeated the Hojo (japan-guide). Jeepe adds that an outer perimeter of about 9 kilometers was built during the siege. I have not seen the outcome of the siege detailed in these sources, so I will leave the story there and point you to the exhibits.</p>
    <p>In the Edo period, Jeepe says the lords were the Okubo and Inaba clans; japan-guide does not mention them, so treat that as a single source. japan-guide says an earthquake destroyed the castle in 1703 and it was quickly rebuilt, and that in 1870 the keep and other buildings were dismantled and sold.</p>

    <h2 id="keep">The Keep and the Museums<span class="h2-jp">天守と博物館</span></h2>
    <p>The keep was rebuilt in ferro-concrete in 1960, based on Edo-period models and drawings (japan-guide); Jeepe also gives 1960. It looks three stories tall from the outside and has four inside (japan-guide, the city page). The exhibits cover the castle&rsquo;s history, armor and swords, and the top floor has views over the park and the city.</p>
    <p>Two smaller museums sit nearby. The <strong>Samurai Museum</strong> is in the Tokiwaki Gate building, across from the keep, with armor and swords (japan-guide). The <strong>Ninja Museum</strong> is near the main entrance and has an obstacle course where you can try ninja skills (japan-guide). Jeepe says it is themed on the Fuma ninja, who supported the Hojo, and that you can try shuriken throwing. Jeepe also lists an armor-dressing experience for 500 yen (single source; please check the hours).</p>

    <h2 id="grounds">Gates, Moat and Cherry Blossoms<span class="h2-jp">城門と桜</span></h2>
    <p>japan-guide says the three major gates leading to the castle were restored in the years after the keep, and the grounds are a park with a moat. Jeepe describes the area as the castle ruins park and says it is a ten-minute walk from the station.</p>
    <p>For flowers, japan-guide lists cherry blossoms in late March to early April, plus plum, azalea, wisteria, iris, hydrangea and lotus at other times. Jeepe counts about 300 Somei Yoshino trees, a place on Japan&rsquo;s Top 100 cherry blossom spots, and illuminations during the season. The city page also names plum, cherry and hydrangea.</p>

    <h2 id="visit">Visiting Odawara Castle<span class="h2-jp">アクセス</span></h2>
    <ul class="practical-list"><li><strong>Admission (adult):</strong> keep 510 yen, Ninja Museum 310 yen, Samurai Museum 200 yen; keep plus both museums 610 yen (japan-guide). Jeepe lists a keep plus Samurai Museum combo at 610 yen, so please confirm the bundle at the gate.</li><li><strong>Hours:</strong> 9:00 to 17:00, last entry 16:30 (japan-guide, Jeepe, city page).</li><li><strong>Closed:</strong> keep on the second Wednesday of December, 31 December and 1 January; museums on 31 December and 1 January only (japan-guide).</li><li><strong>From Odawara Station:</strong> about 10 minutes on foot from the East Exit (japan-guide, Jeepe).</li><li><strong>From Tokyo:</strong> about 35 minutes from Tokyo Station by Shinkansen, about 75 minutes from Shinjuku on the Odakyu Romancecar, about 50 minutes from Yokohama on the JR Tokaido Line (Jeepe). The same article elsewhere gives slightly different times, so check a timetable.</li><li><strong>Time needed:</strong> 20 to 40 minutes for the keep (japan-guide); 1.5 to 2 hours for the whole park with both museums (Jeepe).</li><li><strong>By car:</strong> about 10 minutes from the Ogikubo Interchange on the Odawara-Atsugi Road (Jeepe).</li></ul>

    <h2 id="stay">Making It a Trip<span class="h2-jp">滞在</span></h2>
    <p>Odawara is the gateway to Hakone, so most visitors fit the castle into a half day before the mountains. If you like castles that have a missing keep, our <a href="/guides/edo-castle/" class="inline-link" onclick="trackEvent('click','internal','guide_odawara_to_edo')">Edo Castle guide</a> covers the Imperial Palace East Gardens, and our <a href="/guides/nagoya-castle/" class="inline-link" onclick="trackEvent('click','internal','guide_odawara_to_nagoya')">Nagoya Castle guide</a> covers another rebuilt keep.</p>
    <div class="key-callout">
      <p>&#127890; <strong>Plan your trip:</strong> Browse guided tours or plan a stay around Odawara and Hakone. <a href="https://www.viator.com/search/Odawara?pid=P00298374&amp;mcid=42383&amp;medium=link&amp;campaign=sacred-japan" target="_blank" rel="noopener sponsored" onclick="trackEvent('click','affiliate','viator_odawara_local')">Browse Odawara tours &rarr;</a></p>
    </div>

    <h2 id="faq">Frequently Asked Questions<span class="h2-jp">よくあるご質問</span></h2>
    <div class="faq-stack">
'''+''.join(f'''    <details class="faq-item">
        <summary>{q}</summary>
        <div class="faq-answer">{a}</div>
    </details>
''' for q,a in faqs)+'''    </div>

    <h2 id="final">Before You Board the Hakone Train<span class="h2-jp">むすびに</span></h2>
    <p>Give Odawara Castle an hour on your way to Hakone. Climb the keep for the view, try the ninja course if you have children with you, and remember that the keep is young but the site is not.</p>

    <div class="closing-block">
      <span class="torii">&#9961;&#65039;</span>
      <p>The keep is new. The stronghold under it ruled a region.</p>
    </div>

    <!-- RELATED GUIDES -->
    <section class="related-section">
      <h2>Related Guides</h2>
      <span class="h2-jp">関連ガイド</span>

      <div class="related-grid">

        <a class="related-card" href="/guides/edo-castle/" onclick="trackEvent('click','internal','related_odawara_to_edo')">
          <div class="related-card-label">SACRED JAPAN ／ GUIDES</div>
          <div class="related-card-title">&#127983; Edo Castle Guide &rarr;</div>
          <div class="related-card-desc">A missing keep and free ruins in Tokyo.</div>
        </a>

        <a class="related-card" href="/guides/nagoya-castle/" onclick="trackEvent('click','internal','related_odawara_to_nagoya')">
          <div class="related-card-label">SACRED JAPAN ／ GUIDES</div>
          <div class="related-card-title">&#127983; Nagoya Castle Guide &rarr;</div>
          <div class="related-card-desc">Golden shachi and a rebuilt palace.</div>
        </a>

        <a class="related-card" href="/castles/" onclick="trackEvent('click','internal','related_odawara_to_castles')">
          <div class="related-card-label">SACRED JAPAN ／ CASTLES</div>
          <div class="related-card-title">&#127983; Japan's Castles &rarr;</div>
          <div class="related-card-desc">Every castle guide, with photos and official links.</div>
        </a>

      </div>
    </section>

  </article>

'''
tail=tail.replace('kochi-castle',SL).replace('_kochi_','_odawara_').replace('DKochi','DOdawara').replace('search/Kochi','search/Odawara')
def L(u,l,t): return f'<a href="{u}" target="_blank" rel="noopener" style="color:var(--beni);text-decoration:underline;" onclick="trackEvent(\'click\',\'external\',\'{l}\')">{t}</a>'
src='Sources verified at time of writing: '+', '.join([
 L('https://japan-guide.com/e/e5222.html','src_odawara_jg','japan-guide'),
 L('https://www.jeepe.jp/en/articles/odawara-castle-travel-guide-1130','src_odawara_jeepe','Jeepe'),
 L('https://www.city.odawara.kanagawa.jp/kanko/language/english/castle.html','src_odawara_city','Odawara City'),
])+'. Hours, prices and availability change'
tail,n=re.subn(r'Sources verified at time of writing:.*?Hours, prices and availability change',lambda m:src,tail,flags=re.S); assert n==1
out=head+main+tail
assert not re.search('Kochi|Shikoku|kochi|Kanazawa|Shuri|Naha|Takeda|Asago|Machu',re.sub(r'"mainEntity": \[.*','',out,flags=re.S)),re.findall('.{30}(?:Kochi|Kanazawa|Shuri|Naha|Takeda|Asago|Machu).{20}',out)
os.makedirs(R+f'guides/{SL}',exist_ok=True); open(R+f'guides/{SL}/index.html','w',encoding='utf-8').write(out)
for tg in ['div','figure','picture','p','a','ul','li','details','section','h2']:
    assert len(re.findall(f'<{tg}[ >]',out))==len(re.findall(f'</{tg}>',out)),tg
for m in re.findall(r'<script type="application/ld\+json">(.*?)</script>',out,re.S): json.loads(m)
im=Image.open(R+'images/og/og-guides-matsue-castle.jpg').convert('RGB'); d=ImageDraw.Draw(im)
d.rectangle([40,150,1170,380],fill=(252,240,242))
f1=ImageFont.truetype(glob.glob('/usr/share/fonts/**/DejaVuSerif-Bold.ttf',recursive=True)[0],48)
f2=ImageFont.truetype(glob.glob('/usr/share/fonts/**/NotoSerifCJK-Bold.ttc',recursive=True)[0],28,index=0)
l1="Odawara Castle Guide:"; l2="The Hojo Stronghold"; print(d.textlength(l2,font=f1),d.textlength(l1,font=f1)); assert d.textlength(l2,font=f1)<1090 and d.textlength(l1,font=f1)<1090
d.text((66,170),l1,font=f1,fill=(26,15,15)); d.text((66,238),l2,font=f1,fill=(26,15,15)); d.text((66,332),"小田原城",font=f2,fill=(138,125,120))
im.save(R+f'images/og/og-guides-{SL}.jpg',quality=88); print('built',len(out))
