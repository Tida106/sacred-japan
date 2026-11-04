import re,json,os,glob
from PIL import Image,ImageDraw,ImageFont
R='/home/claude/sacred-japan/'; SL='kanazawa-castle'
s=open(R+'guides/kochi-castle/index.html',encoding='utf-8').read()
i=s.index('<main>'); j=s.index('</main>'); head,tail=s[:i],s[j:]
TITLE="Kanazawa Castle Guide: Lead-Tile Turrets, a 1788 Gate and the Park Next to Kenrokuen"
DESC="A licensed guide's guide to Kanazawa Castle Park in Ishikawa: the Maeda family's seat, why the keep was never rebuilt, the 1788 Ishikawa Gate, the rebuilt turrets, Gyokusen'inmaru Garden and how to visit with Kenrokuen."
head=re.sub(r'<title>.*?</title>',f'<title>{TITLE} | Sacred Japan</title>',head,count=1)
head=re.sub(r'(<meta (?:name="description"|property="og:description"|name="twitter:description") content=")[^"]*(")',lambda m:m.group(1)+DESC+m.group(2),head)
head=re.sub(r'(<meta (?:property="og:title"|name="twitter:title") content=")[^"]*(")',lambda m:m.group(1)+TITLE+m.group(2),head)
head=re.sub(r'("headline": ")[^"]*(")',lambda m:m.group(1)+TITLE+m.group(2),head)
head=re.sub(r'("description": ")A licensed[^"]*(")',lambda m:m.group(1)+DESC+m.group(2),head)
head=re.sub(r'<meta name="keywords" content="[^"]*">','<meta name="keywords" content="Kanazawa Castle, Kanazawa Castle Park, Ishikawa Gate, Hishi Yagura, Kanazawa Castle admission, Kanazawa Castle hours, Kenrokuen, Maeda clan, Kanazawa Castle Kenrokuen">',head)
head=head.replace('guides/kochi-castle','guides/kanazawa-castle').replace('guide_kochi_','guide_kanazawa_').replace('og-guides-kochi-castle','og-guides-kanazawa-castle')
head=head.replace('高知城','金沢城').replace('Kochi Castle','Kanazawa Castle')
head=re.sub(r"<h1>.*?</h1>","<h1><em>Kanazawa Castle</em>: Lead-Tile Turrets, a 1788 Gate and the Park Next to Kenrokuen</h1>",head,count=1,flags=re.S)
head=head.replace("Shikoku's original keep, and the only castle where the lord's palace still stands beside it.","The Maeda family's seat in Ishikawa: no keep since 1602, but a 1788 gate, turrets rebuilt in wood and lead tile, and a free park beside Kenrokuen.")
faqs=[
("Is there a keep at Kanazawa Castle?","No. Kanazawa Station's castle guide says the castle tower burned down in 1602 and was never replaced. GLTJP says the same in a user review, which adds lightning as the cause, so I would treat the cause as unconfirmed. What you see now is the Ishikawa Gate, rebuilt turrets and storehouses, and the stone walls."),
("Is Kanazawa Castle Park free?","Yes. GLTJP, Visit Kanazawa and Kanazawa Station's guide all say the park is free to enter. The rebuilt Hishi Yagura, Gojikken Nagaya and Hashizume-mon Tsuzuki Yagura charge 320 yen for adults and 100 yen for children aged 6 to 17 (Visit Kanazawa, Kanazawa Station), while Japan Experience gives 300 yen. People 65 or over are free with ID, according to Visit Kanazawa. Please confirm officially."),
("What are the opening hours?","The park is open every day: 7:00 to 18:00 from March 1 to October 15, and 8:00 to 17:00 from October 16 to the end of February (GLTJP, Visit Kanazawa). The turrets and storehouse are open 9:00 to 16:30, with last entry at 16:00 (Visit Kanazawa, Kanazawa Station). Hours vary by facility, so please check the official site."),
("How do I get there from Kanazawa Station?","Kanazawa Station's guide says to take the Kanazawa Loop Bus from the East Gate bus stop 7; the right-hand route takes roughly 18 minutes and costs 220 yen, while Japan Experience gives 200 yen. Visit Kanazawa says it is about 5 minutes on foot from the Kenrokuen Garden and Kanazawa Castle Park stop. Japan Experience says it is a 20 to 25 minute walk southeast of the station. There is no parking at the park (GLTJP, Visit Kanazawa)."),
("Can I visit Kenrokuen on the same day?","Yes. Kanazawa Station's guide says Kenrokuen is directly across the road from the castle, and Japan Experience says it is across the Ishikawa Bridge. GLTJP lists it about 540 meters away, and a reviewer there suggests half a day to a full day for both. Visit Kanazawa does not describe the garden as part of the castle park, so I would treat them as two separate sites."),
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
assert not re.search('Kochi|Shikoku|kochi',hh)
main='''<main>

  <!-- TABLE OF CONTENTS -->
  <aside class="toc" aria-label="Table of contents">
    <div class="toc-label">TABLE OF CONTENTS ／ 目次</div>
    <div class="toc-title">In This Guide</div>
    <ol>
      <li><a href="#opening">A Castle Rebuilt Piece by Piece</a></li>
      <li><a href="#history">From Temple Stronghold to the Maeda Seat</a></li>
      <li><a href="#fires">Fires, Barracks and a University</a></li>
      <li><a href="#gate">The Ishikawa Gate</a></li>
      <li><a href="#rebuilt">The Rebuilt Turrets and Storehouse</a></li>
      <li><a href="#garden">Gyokusen'inmaru Garden and the Walls</a></li>
      <li><a href="#visit">Visiting Kanazawa Castle Park</a></li>
      <li><a href="#stay">Making It a Trip</a></li>
      <li><a href="#faq">Frequently Asked Questions</a></li>
      <li><a href="#final">A Castle Being Put Back Together</a></li>
    </ol>
  </aside>

  <article>

    <section id="opening">
      <p class="opening">As a licensed guide, I tell visitors that Kanazawa Castle is a castle being put back together. The keep burned in 1602 and was never rebuilt, almost everything else burned later, and then the grounds became a barracks and a university campus. Since the park opened to the public, the city has rebuilt turrets, a storehouse and gates in wood, and one real gate from 1788 stands among them.</p>
      <p>This guide covers the castle's history, what is original and what is rebuilt, the garden, the practical details and how to pair it with Kenrokuen across the road. Where my sources disagree, I say so.</p>
    </section>

    <h2 id="history">From Temple Stronghold to the Maeda Seat<span class="h2-jp">前田家の居城へ</span></h2>
    <p>The hill was a power base before it was a castle. Kanazawa Station's guide says a fortified Buddhist temple, Kanazawa Mido (Oyama Gobo), was built there in 1546 and became the stronghold of an independent &ldquo;Peasants' Kingdom.&rdquo; In 1580 Sakuma Morimasa, serving Oda Nobunaga, captured the temple and began developing the castle.</p>
    <p>In 1583, after the Battle of Shizugatake, Maeda Toshiie entered the castle, and the Maeda family ruled the Kaga domain from here until the early Meiji period (GLTJP, Kanazawa Station). Japan Experience says Toshiie began construction and that his son Toshinaga completed it. Visit Kanazawa says the Maeda governed Kaga for more than 280 years. Every June the Hyakumangoku Festival parade marks Toshiie's entry into the castle (Kanazawa Station).</p>

    <h2 id="fires">Fires, Barracks and a University<span class="h2-jp">火災と軍用地</span></h2>
    <p>The castle burned several times. Kanazawa Station's guide gives 1602 for the loss of the keep, 1759 for the Great Kanazawa Fire that nearly destroyed the castle, and 1881 for fires that destroyed more buildings. GLTJP, in user reviews, also lists fires in 1631 and 1808, which I have not confirmed elsewhere.</p>
    <p>After the Maeda, the grounds became a military barracks and the moats were filled in, according to Kanazawa Station. Visit Kanazawa says the site later served as a Kanazawa University campus, and Japan Experience says the university moved out in 1995. Kanazawa Station says the local government took control of the site in 1996 and that many buildings have been rebuilt and part of the moat restored since. Visit Kanazawa says the site was designated a National Historic Site in 2008.</p>

    <h2 id="gate">The Ishikawa Gate<span class="h2-jp">石川門</span></h2>
    <p>The Ishikawa Gate is the original. Kanazawa Station and Japan Experience date it to 1788, and Japan Experience says it has ishiotoshi holes for dropping stones on attackers. Visit Kanazawa says it was rebuilt in 1788 and designates it, with the Sanjikken Nagaya, as an important cultural property. It gives 1858 for the Sanjikken Nagaya, while Japan Experience says the gate and the Sanjikken Nagaya are the only buildings surviving from the original construction, which does not match 1858 as a rebuild date, so I would not give a single date for the Nagaya.</p>

    <h2 id="rebuilt">The Rebuilt Turrets and Storehouse<span class="h2-jp">復元建築</span></h2>
    <p>Between 1999 and 2001 the city rebuilt the Hishi Yagura, the Gojikken Nagaya storehouse and the Hashizume-mon Tsuzuki Yagura (Kanazawa Station, GLTJP, Japan Experience). GLTJP and Visit Kanazawa describe large wooden buildings with white plaster walls and flat tiles, and lead roof tiles. Japan Experience says the Gojikken Nagaya is about 90 meters long, and that its name refers to fifty ken, with one ken roughly 1.8 meters. It adds that Kyoto carpenters trained local craftsmen, and that the work followed traditional methods based on original plans.</p>
    <p>Kanazawa Station says the Kahoku-mon Gate, the Maeda-era main entrance, was rebuilt in 2010 with a wooden frame and a lead-tile roof. GLTJP says the Nezumi-mon gate and bridge were completely rebuilt in 2020, which is a single-source detail I have not confirmed elsewhere. The interior of the Gojikken Nagaya is open to visitors, and GLTJP says the three buildings are wheelchair accessible.</p>

    <h2 id="garden">Gyokusen'inmaru Garden and the Walls<span class="h2-jp">玉泉院丸庭園と石垣</span></h2>
    <p>Visit Kanazawa says the third Maeda lord began building Gyokusen'inmaru Garden in 1634, that it was destroyed at the end of the feudal period, and that it was reconstructed in 2015. It says there is a light show after sunset on Saturdays and on designated dates. GLTJP says the park is lit in the evening from sunset to 9 p.m., which is not the same as a Saturday-only show, so please check the schedule.</p>
    <p>Visit Kanazawa says the stone walls differ across the site and the oldest are over 400 years old. GLTJP says the stones were placed in particular orientations, reportedly to avoid unlucky directions, which I have not confirmed elsewhere. I would walk the walls slowly, since they are the part of the castle that has never been rebuilt in timber.</p>

    <h2 id="visit">Visiting Kanazawa Castle Park<span class="h2-jp">アクセス</span></h2>
    <ul class="practical-list"><li><strong>Park admission:</strong> free (GLTJP, Visit Kanazawa, Kanazawa Station).</li><li><strong>Turrets and storehouse:</strong> 320 yen for adults and 100 yen for ages 6 to 17, free for 65 and over with ID (Visit Kanazawa, Kanazawa Station). Japan Experience gives 300 yen. Please confirm officially.</li><li><strong>Park hours:</strong> 7:00 to 18:00 from March 1 to October 15, and 8:00 to 17:00 from October 16 to the end of February; open every day (GLTJP, Visit Kanazawa).</li><li><strong>Turret hours:</strong> 9:00 to 16:30, last entry 16:00 (Visit Kanazawa, Kanazawa Station).</li><li><strong>Bus:</strong> Kanazawa Loop Bus from the station's East Gate, roughly 18 minutes on the right-hand route and 220 yen (Kanazawa Station); Japan Experience gives 200 yen. About 5 minutes on foot from the bus stop (Visit Kanazawa).</li><li><strong>Walk:</strong> 20 to 25 minutes southeast of the station (Japan Experience).</li><li><strong>Parking:</strong> none (GLTJP, Visit Kanazawa). Lockers are available (GLTJP).</li><li><strong>Address:</strong> 1-1 Marunouchi, Kanazawa, Ishikawa (GLTJP, Visit Kanazawa).</li></ul>

    <h2 id="stay">Making It a Trip<span class="h2-jp">滞在</span></h2>
    <p>Kenrokuen is across the road, so most people see both in one outing. If you want another castle where parts were rebuilt in wood, our <a href="/guides/nagoya-castle/" class="inline-link" onclick="trackEvent('click','internal','guide_kanazawa_to_nagoya')">Nagoya Castle guide</a> covers a rebuilt palace, and our <a href="/guides/himeji-castle/" class="inline-link" onclick="trackEvent('click','internal','guide_kanazawa_to_himeji')">Himeji Castle guide</a> covers one that survived whole.</p>
    <div class="key-callout">
      <p>&#127890; <strong>Plan your trip:</strong> Browse guided tours, or plan a stay in Kanazawa. <a href="https://www.viator.com/search/Kanazawa?pid=P00298374&amp;mcid=42383&amp;medium=link&amp;campaign=sacred-japan" target="_blank" rel="noopener sponsored" onclick="trackEvent('click','affiliate','viator_kanazawa_local')">Browse Kanazawa tours &rarr;</a></p>
    </div>

    <h2 id="faq">Frequently Asked Questions<span class="h2-jp">よくあるご質問</span></h2>
    <div class="faq-stack">
'''+''.join(f'''    <details class="faq-item">
        <summary>{q}</summary>
        <div class="faq-answer">{a}</div>
    </details>
''' for q,a in faqs)+'''    </div>

    <h2 id="final">A Castle Being Put Back Together<span class="h2-jp">むすびに</span></h2>
    <p>Kanazawa Castle is worth a visit if you like to see how a castle is rebuilt. Go through the Ishikawa Gate, step inside the Gojikken Nagaya, walk the walls, and then cross the road to Kenrokuen.</p>

    <div class="closing-block">
      <span class="torii">&#9961;&#65039;</span>
      <p>The keep is gone. The gate stands, and the rest is being rebuilt.</p>
    </div>

    <!-- RELATED GUIDES -->
    <section class="related-section">
      <h2>Related Guides</h2>
      <span class="h2-jp">関連ガイド</span>

      <div class="related-grid">

        <a class="related-card" href="/guides/nagoya-castle/" onclick="trackEvent('click','internal','related_kanazawa_to_nagoya')">
          <div class="related-card-label">SACRED JAPAN ／ GUIDES</div>
          <div class="related-card-title">&#127983; Nagoya Castle Guide &rarr;</div>
          <div class="related-card-desc">Golden shachi and a rebuilt palace.</div>
        </a>

        <a class="related-card" href="/guides/himeji-castle/" onclick="trackEvent('click','internal','related_kanazawa_to_himeji')">
          <div class="related-card-label">SACRED JAPAN ／ GUIDES</div>
          <div class="related-card-title">&#127983; Himeji Castle Guide &rarr;</div>
          <div class="related-card-desc">The castle that survived whole.</div>
        </a>

        <a class="related-card" href="/castles/" onclick="trackEvent('click','internal','related_kanazawa_to_castles')">
          <div class="related-card-label">SACRED JAPAN ／ CASTLES</div>
          <div class="related-card-title">&#127983; Japan's Castles &rarr;</div>
          <div class="related-card-desc">Every castle guide, with photos and official links.</div>
        </a>

      </div>
    </section>

  </article>

'''
tail=tail.replace('kochi-castle',SL).replace('_kochi_','_kanazawa_').replace('DKochi','DKanazawa').replace('search/Kochi','search/Kanazawa')
def L(u,l,t): return f'<a href="{u}" target="_blank" rel="noopener" style="color:var(--beni);text-decoration:underline;" onclick="trackEvent(\'click\',\'external\',\'{l}\')">{t}</a>'
src='Sources verified at time of writing: '+', '.join([
 L('https://www.gltjp.com/en/directory/item/12566','src_kanazawa_gltjp','GLTJP'),
 L('https://visitkanazawa.jp/en/attractions/detail_10060.html','src_kanazawa_visit','Visit Kanazawa'),
 L('https://www.kanazawastation.com/kanazawa-castle-and-kanazawa-castle-park/','src_kanazawa_station','Kanazawa Station guide'),
 L('https://www.japan-experience.com/all-about-japan/kanazawa/attractions-and-excursions/kanazawa-castle','src_kanazawa_jexp','Japan Experience'),
])+'. Hours, prices and availability change'
tail,n=re.subn(r'Sources verified at time of writing:.*?Hours, prices and availability change',lambda m:src,tail,flags=re.S); assert n==1
out=head+main+tail
assert not re.search('Kochi|Shikoku|kochi|Uwajima',re.sub(r'"mainEntity": \[.*','',out,flags=re.S)),re.findall('.{30}Kochi.{20}',out)
os.makedirs(R+f'guides/{SL}',exist_ok=True); open(R+f'guides/{SL}/index.html','w',encoding='utf-8').write(out)
for tg in ['div','figure','picture','p','a','ul','li','details','section','h2']:
    assert len(re.findall(f'<{tg}[ >]',out))==len(re.findall(f'</{tg}>',out)),tg
for m in re.findall(r'<script type="application/ld\+json">(.*?)</script>',out,re.S): json.loads(m)
im=Image.open(R+'images/og/og-guides-matsue-castle.jpg').convert('RGB'); d=ImageDraw.Draw(im)
d.rectangle([40,150,1170,380],fill=(252,240,242))
f1=ImageFont.truetype(glob.glob('/usr/share/fonts/**/DejaVuSerif-Bold.ttf',recursive=True)[0],48)
f2=ImageFont.truetype(glob.glob('/usr/share/fonts/**/NotoSerifCJK-Bold.ttc',recursive=True)[0],28,index=0)
l1="Kanazawa Castle Guide:"; l2="Lead Tiles and a 1788 Gate"; print(d.textlength(l2,font=f1)); assert d.textlength(l2,font=f1)<1090
d.text((66,170),l1,font=f1,fill=(26,15,15)); d.text((66,238),l2,font=f1,fill=(26,15,15)); d.text((66,332),"金沢城",font=f2,fill=(138,125,120))
im.save(R+f'images/og/og-guides-{SL}.jpg',quality=88); print('built',len(out))
