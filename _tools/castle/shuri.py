import re,json,os,glob
from PIL import Image,ImageDraw,ImageFont
R='/home/claude/sacred-japan/'; SL='shuri-castle'
s=open(R+'guides/kochi-castle/index.html',encoding='utf-8').read()
i=s.index('<main>'); j=s.index('</main>'); head,tail=s[:i],s[j:]
TITLE="Shuri Castle Guide: Ryukyu's Red Palace, the Rebuilt Main Hall and Timed Tickets"
DESC="A licensed guide's guide to Shuri Castle in Naha, Okinawa: the Ryukyu Kingdom's red palace, the 2019 fire, the rebuilt main hall scheduled to open on 23 November 2026, how the timed tickets work and how to get there."
TAG="The Ryukyu Kingdom's red palace in Naha: burned in 2019, with the rebuilt main hall due to open on 23 November 2026 by timed ticket."
head=re.sub(r'<title>.*?</title>',f'<title>{TITLE} | Sacred Japan</title>',head,count=1)
head=re.sub(r'(<meta (?:name="description"|property="og:description"|name="twitter:description") content=")[^"]*(")',lambda m:m.group(1)+DESC+m.group(2),head)
head=re.sub(r'(<meta (?:property="og:title"|name="twitter:title") content=")[^"]*(")',lambda m:m.group(1)+TITLE+m.group(2),head)
head=re.sub(r'("headline": ")[^"]*(")',lambda m:m.group(1)+TITLE+m.group(2),head)
head=re.sub(r'("description": ")A licensed[^"]*(")',lambda m:m.group(1)+DESC+m.group(2),head)
head=re.sub(r'("date(?:Published|Modified)": ")[^"]*(")',lambda m:m.group(1)+'2026-11-04'+m.group(2),head)
head=re.sub(r'<meta name="keywords" content="[^"]*">','<meta name="keywords" content="Shuri Castle, Shurijo, Shuri Castle reopening, Shuri Castle main hall, Seiden, Shuri Castle tickets, Shuri Castle reservation, Shuri Castle fire, Ryukyu Kingdom, Naha, Okinawa castle, Shureimon">',head)
head=head.replace('guides/kochi-castle','guides/shuri-castle').replace('guide_kochi_','guide_shuri_').replace('og-guides-kochi-castle','og-guides-shuri-castle')
head=head.replace('高知城','首里城').replace('Kochi Castle','Shuri Castle')
head=re.sub(r"<h1>.*?</h1>","<h1><em>Shuri Castle</em>: Ryukyu's Red Palace, the Rebuilt Main Hall and Timed Tickets</h1>",head,count=1,flags=re.S)
head=head.replace("Shikoku's original keep, and the only castle where the lord's palace still stands beside it.",TAG)
faqs=[
("Is the main hall of Shuri Castle open?","The rebuilt main hall (Seiden) is scheduled to open to the public on 23 November 2026, after a completion ceremony on 22 November, according to Travel Watch and the park's ticket page. The park is closed on 22 November (Japan Ode). Plans can change near an opening, so please check the official Shuri Castle Park site before you go."),
("Do I need a reservation to go inside the main hall?","Yes. The park's ticket page says the interior is by timed advance reservation, in 30-minute slots, and that the reservation adds no extra charge. You book on the official ticket site, Webket, with up to nine tickets per purchase (Japan Ode). Unsold slots may be sold online until 15 minutes before the slot or at the Kofukumon ticket window. Without a reservation you can still see the rest of the paid area and the outside of the hall."),
("How much does Shuri Castle cost?","From 23 November 2026, the individual adult price for the paid area is 1,000 yen, up from 400 yen. High school students pay 760 yen, elementary and junior high students 370 yen, and children under 6 are free (Travel Watch, the park's ticket page). Groups of 20 or more pay 800 yen for adults. The areas outside the paid zone, such as Shureimon Gate, are free to enter (K005 Powerspot)."),
("How long should I plan for a visit?","The park's ticket page estimates 90 to 120 minutes from the Shurimori-kan visitor center, including the main hall, and says the main hall interior itself takes about 15 minutes. Japan Ode suggests allowing a half day from central Naha. Please add time for walking from the station."),
("How do I get to Shuri Castle from Naha?","Take the Yui Rail monorail to Shuri Station and walk about 15 minutes to Shureimon Gate (K005 Powerspot, Japan Ode). The park's ticket page recommends public transport because nearby roads are expected to be congested. Naha buses on routes 7 and 8 stop at Shurijo-mae, a short walk from the gate (K005 Powerspot)."),
("What survived the 2019 fire?","Wikipedia says the fire on 31 October 2019 destroyed the main hall, the North Hall, the South Hall and the Bandokoro. K005 Powerspot says the stone walls, the gates and the sacred sites, including Kyo-no-uchi and the Sonohyan-utaki Stone Gate, were largely untouched and can still be visited."),
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
assert not re.search('Kochi|Shikoku|kochi|Kanazawa',hh),re.findall('.{30}(?:Kochi|Shikoku|Kanazawa).{20}',hh)
main='''<main>

  <!-- TABLE OF CONTENTS -->
  <aside class="toc" aria-label="Table of contents">
    <div class="toc-label">TABLE OF CONTENTS ／ 目次</div>
    <div class="toc-title">In This Guide</div>
    <ol>
      <li><a href="#opening">A Palace, Not a Fortress</a></li>
      <li><a href="#history">The Kingdom's Seat, 1429 to 1879</a></li>
      <li><a href="#style">Red Lacquer and Dragons</a></li>
      <li><a href="#fire">The 2019 Fire and the Rebuild</a></li>
      <li><a href="#seiden">Booking the Main Hall</a></li>
      <li><a href="#see">What to See Around It</a></li>
      <li><a href="#visit">Visiting Shuri Castle</a></li>
      <li><a href="#stay">Making It a Trip</a></li>
      <li><a href="#faq">Frequently Asked Questions</a></li>
      <li><a href="#final">A Palace Rising Again</a></li>
    </ol>
  </aside>

  <article>

    <section id="opening">
      <p class="opening">As a licensed guide, I tell visitors that Shuri Castle is a palace before it is a castle. For about 450 years it was the royal court of the Ryukyu Kingdom, and it looks more like a Chinese palace in red lacquer than like a Japanese keep on a stone base. Its main hall burned in October 2019, and the rebuilt hall is scheduled to open to the public on 23 November 2026, by timed reservation.</p>
      <p>This guide covers the kingdom's history, what makes the architecture different, the fire and the rebuild, how the timed tickets work, and the practical details. Where my sources disagree or I could only find one, I say so. If you are reading this after 23 November 2026, please check the park's official site, since plans can change near an opening.</p>
    </section>

    <h2 id="history">The Kingdom's Seat, 1429 to 1879<span class="h2-jp">王国の王宮</span></h2>
    <p>Wikipedia says the date the castle was first built is uncertain, but that it was clearly in use during the Sanzan period (1322 to 1429) and was probably built in the earlier Gusuku period. From 1429, after the three principalities of Okinawa were unified, it served for about 450 years as the royal court and administrative center of the Ryukyu Kingdom. Wikipedia describes it as the political, economic and cultural heart of the islands.</p>
    <p>The kingdom did not stay fully independent. Wikipedia says samurai from the Satsuma domain seized Shuri on 6 May 1609, withdrew soon after, and left the kingdom as a Satsuma vassal for roughly 250 years. In 1879 Japan annexed the kingdom, the last king was moved to Tokyo, and the castle was later used as an army barracks. Travel sources say the main hall was designated a national treasure in 1925 (Sumimasen Guide).</p>
    <p>In the Battle of Okinawa in 1945 the castle was shelled and was almost completely destroyed (Wikipedia). It was rebuilt from 1992, after Shureimon Gate had been rebuilt in 1958. In 2000 the site was inscribed as a UNESCO World Heritage Site, as part of the Gusuku Sites and Related Properties of the Kingdom of Ryukyu. Wikipedia notes that only remnants such as stone walls and foundations that existed before 1950 are officially designated, not the rebuilt halls.</p>

    <h2 id="style">Red Lacquer and Dragons<span class="h2-jp">朱漆と龍</span></h2>
    <p>Wikipedia says the castle was greatly influenced by Chinese architecture, with features compared to the Forbidden City, and that gates and buildings were painted in red lacquer. It adds that the roof tiles were Goryeo tiles and later red Ryukyuan tiles, and that the stone walls were built of Ryukyuan limestone, with the outer walls added in the late 15th to early 16th centuries.</p>
    <p>Only two buildings used a Japanese style, according to Wikipedia: the Nanden and the Bandokoro, which hosted receptions for the Satsuma clan. The king's dragon motif decorates much of the castle, including the main hall's roof. Wikipedia also describes two 4.1-meter Great Dragon Pillars on the main hall's west facade, carved from Yonaguni sandstone, which is a detail I have not confirmed elsewhere.</p>

    <h2 id="fire">The 2019 Fire and the Rebuild<span class="h2-jp">火災と再建</span></h2>
    <p>On 31 October 2019 a fire destroyed the main hall (Seiden), the Hokuden, the Nanden and the Bandokoro, according to Wikipedia. It says an alarm sounded around 2:30 a.m., the fire was put out around 1:30 p.m., and roughly 4,200 square meters of six buildings were gutted. The source I used says the cause remains unresolved, so I will not give one.</p>
    <p>Rebuilding of the destroyed sections began in February 2020 (Wikipedia). Construction of the new main hall began in November 2022, its exterior was completed in July 2025, and the temporary roof was removed in October 2025 (K005 Powerspot, Sumimasen Guide). A completion ceremony is scheduled for 22 November 2026 (Sumimasen Guide, Japan Ode). Wikipedia says the new main hall uses wood from Taiwan and elsewhere, and that the Nanden and Hokuden were rebuilt as facades with steel and concrete interiors; I have not confirmed those details elsewhere. Sumimasen Guide says other lost buildings are part of the government's restoration plan, with detailed design of the North Hall underway.</p>

    <h2 id="seiden">Booking the Main Hall<span class="h2-jp">正殿の予約</span></h2>
    <p>The park's ticket page says entry to the main hall interior is by timed advance reservation, in 30-minute slots, with no extra charge for the time slot. You choose a date and slot on the official sales site, Webket, buy the ticket, show the QR code at the Hoshinmon gate, and join the main hall queue at your time. Japan Ode says each purchase can cover up to nine tickets.</p>
    <p>Travel Watch and the ticket page give the sales schedule. For visits from 23 November to 31 December 2026, tickets were sold in two batches, on 1 September and 1 October at 13:00. From 1 January 2027, sales open at 13:00 on the first day of the month two months before the visit. Unsold slots may still be sold online until 15 minutes before the slot, or at the Kofukumon ticket window. Tickets without the interior can be bought from one month ahead.</p>
    <p>A few rules matter. Visitors take their shoes off inside, so bring a bag for them (Sumimasen Guide, the ticket page). For tickets bought on Webket, the ticket page says the date can be changed until the day before and refunded until two days before. Group interior reservations are not accepted for 23 November to 6 December 2026, and groups use a lottery for now. If you have no reservation, you can still see the rest of the paid area and the outside of the hall (Travel Watch).</p>
    <p>The ticket page also suggests when to arrive. It recommends booking a slot 40 to 50 minutes after you expect to reach Shuri Station by monorail. It lists the last main hall slot as 17:00 to 17:29 from December to March and 18:00 to 18:29 from April to November, and it describes the mornings from 8:30 to 11:00 as very crowded and noon to 14:00 as relatively empty.</p>

    <h2 id="see">What to See Around It<span class="h2-jp">見どころ</span></h2>
    <p>K005 Powerspot says Shureimon Gate bears a plaque reading &ldquo;Shurei no kuni,&rdquo; the Land of Propriety, and that the gate appears on the 2,000-yen note. Wikipedia says it was built between 1527 and 1555. K005 Powerspot lists Shureimon, the Sonohyan-utaki Stone Gate, Kankaimon Gate, the Ryuhi spring, Zuisenmon Gate, Rokokumon Gate, the Hikagedai sundial and the Bankoku Shinryo Bell as free areas, and says the paid zone begins beyond Hoshinmon Gate.</p>
    <p>The Sonohyan-utaki Stone Gate was built in 1519 and is a gate for prayer rather than a passageway, where the king prayed for safe travel (K005 Powerspot). Kyo-no-uchi is the castle's largest sacred precinct, where, according to Wikipedia, the high priestess Kikoe-ogimi held prayers, and K005 Powerspot says priestesses prayed for the royal family's prosperity, safe voyages and good harvests. K005 Powerspot also says the stone walls, the gates and the sacred sites were largely untouched by the fire.</p>
    <p>Inside the paid zone, K005 Powerspot mentions the Reconstruction Exhibition Room in the Yohokoriden and the Agari-no-Azana lookout. Please check the park's notices before you go, because construction can change the route (Japan Ode).</p>

    <h2 id="visit">Visiting Shuri Castle<span class="h2-jp">アクセス</span></h2>
    <ul class="practical-list"><li><strong>Main hall opening:</strong> scheduled for 23 November 2026, after a completion ceremony on 22 November, when the whole park is closed. On 23 November the free area opens at 11:15 and the paid area and the main hall at noon (Japan Ode; Sumimasen Guide also gives noon).</li><li><strong>Paid-area admission from 23 November 2026:</strong> adults 1,000 yen, high school 760 yen, elementary and junior high 370 yen, under 6 free; groups of 20 or more 800, 610 and 300 yen. Until 21 November the adult price is 400 yen (Travel Watch, the park's ticket page, Sumimasen Guide).</li><li><strong>Free admission:</strong> under 6, Okinawa residents aged 70 or over and holders of a Japanese disability certificate, with proof (the park's ticket page).</li><li><strong>Hours:</strong> Japan Ode gives, from April to November, the free area 8:00 to 19:30 and the paid area 8:30 to 19:00 with last admission at 18:30; from December to March, 8:00 to 18:30 and 8:30 to 18:00 with last admission at 17:30. This is one source, so please confirm officially.</li><li><strong>Closed days:</strong> K005 Powerspot says the park customarily closes on the first Wednesday of July and the day after, though this varies, and it may close when a typhoon approaches.</li><li><strong>Monorail:</strong> Yui Rail to Shuri Station, then about 15 minutes on foot to Shureimon Gate (K005 Powerspot, Japan Ode). The ticket page gives about 20 minutes from the station to the Shurimori-kan visitor center, so please allow extra time.</li><li><strong>Bus:</strong> routes 7 and 8 to Shurijo-mae, about a 1-minute walk (K005 Powerspot).</li><li><strong>Car:</strong> the prefectural lot under Suimuikan charges 500 yen for the first 60 minutes, then 250 yen per 30 minutes, up to 1,000 yen (K005 Powerspot). The park recommends public transport because roads nearby are expected to be congested.</li><li><strong>Time needed:</strong> about 90 to 120 minutes from Shurimori-kan with the main hall; the interior takes about 15 minutes (the ticket page).</li><li><strong>Address and contact:</strong> 1-2 Shuri Kinjo-cho, Naha (Travel Watch). The park management center is 098-886-2020, 8:00 to 18:00 (the ticket page).</li></ul>

    <h2 id="stay">Making It a Trip<span class="h2-jp">滞在</span></h2>
    <p>Shuri Castle sits on a hill east of central Naha, and Japan Ode suggests planning a half day from the city center. If you like castles that were destroyed and rebuilt, our <a href="/guides/kumamoto-castle/" class="inline-link" onclick="trackEvent('click','internal','guide_shuri_to_kumamoto')">Kumamoto Castle guide</a> covers a castle damaged by earthquakes, and our <a href="/guides/nagoya-castle/" class="inline-link" onclick="trackEvent('click','internal','guide_shuri_to_nagoya')">Nagoya Castle guide</a> covers a rebuilt palace.</p>
    <div class="key-callout">
      <p>&#127890; <strong>Plan your trip:</strong> Browse guided tours, or plan a stay in Naha. <a href="https://www.viator.com/search/Naha?pid=P00298374&amp;mcid=42383&amp;medium=link&amp;campaign=sacred-japan" target="_blank" rel="noopener sponsored" onclick="trackEvent('click','affiliate','viator_shuri_local')">Browse Naha tours &rarr;</a></p>
    </div>

    <h2 id="faq">Frequently Asked Questions<span class="h2-jp">よくあるご質問</span></h2>
    <div class="faq-stack">
'''+''.join(f'''    <details class="faq-item">
        <summary>{q}</summary>
        <div class="faq-answer">{a}</div>
    </details>
''' for q,a in faqs)+'''    </div>

    <h2 id="final">A Palace Rising Again<span class="h2-jp">むすびに</span></h2>
    <p>Shuri Castle is worth a visit for the story it tells about the Ryukyu Kingdom. Walk through Shureimon, stand in the sacred precinct, and, if you have booked a slot, step into the rebuilt main hall.</p>

    <div class="closing-block">
      <span class="torii">&#9961;&#65039;</span>
      <p>The hall burned in a single night. The kingdom's red palace is being built again.</p>
    </div>

    <!-- RELATED GUIDES -->
    <section class="related-section">
      <h2>Related Guides</h2>
      <span class="h2-jp">関連ガイド</span>

      <div class="related-grid">

        <a class="related-card" href="/guides/kumamoto-castle/" onclick="trackEvent('click','internal','related_shuri_to_kumamoto')">
          <div class="related-card-label">SACRED JAPAN ／ GUIDES</div>
          <div class="related-card-title">&#127983; Kumamoto Castle Guide &rarr;</div>
          <div class="related-card-desc">Walls, earthquakes and a long rebuild.</div>
        </a>

        <a class="related-card" href="/guides/nagoya-castle/" onclick="trackEvent('click','internal','related_shuri_to_nagoya')">
          <div class="related-card-label">SACRED JAPAN ／ GUIDES</div>
          <div class="related-card-title">&#127983; Nagoya Castle Guide &rarr;</div>
          <div class="related-card-desc">Golden shachi and a rebuilt palace.</div>
        </a>

        <a class="related-card" href="/castles/" onclick="trackEvent('click','internal','related_shuri_to_castles')">
          <div class="related-card-label">SACRED JAPAN ／ CASTLES</div>
          <div class="related-card-title">&#127983; Japan's Castles &rarr;</div>
          <div class="related-card-desc">Every castle guide, with photos and official links.</div>
        </a>

      </div>
    </section>

  </article>

'''
tail=tail.replace('kochi-castle',SL).replace('_kochi_','_shuri_').replace('DKochi','DNaha').replace('search/Kochi','search/Naha')
def L(u,l,t): return f'<a href="{u}" target="_blank" rel="noopener" style="color:var(--beni);text-decoration:underline;" onclick="trackEvent(\'click\',\'external\',\'{l}\')">{t}</a>'
src='Sources verified at time of writing: '+', '.join([
 L('https://oki-park.jp/shurijo/ticket_guide/','src_shuri_official','Shuri Castle Park ticket page'),
 L('https://travel.watch.impress.co.jp/docs/news/2133105.html','src_shuri_watch','Travel Watch'),
 L('https://en.wikipedia.org/wiki/Shuri_Castle','src_shuri_wiki','Wikipedia'),
 L('https://k005.net/en/powerspot/shurijo-en/','src_shuri_k005','K005 Powerspot'),
 L('https://thejapanode.com/guides/shuri-castle-guide','src_shuri_ode','Japan Ode'),
 L('https://sumimasenguide.com/articles/shuri-castle-seiden-tickets','src_shuri_sumimasen','Sumimasen Guide'),
])+'. Hours, prices and availability change'
tail,n=re.subn(r'Sources verified at time of writing:.*?Hours, prices and availability change',lambda m:src,tail,flags=re.S); assert n==1
out=head+main+tail
assert not re.search('Kochi|Shikoku|kochi|Kanazawa|Uwajima',re.sub(r'"mainEntity": \[.*','',out,flags=re.S)),re.findall('.{30}(?:Kochi|Kanazawa).{20}',out)
os.makedirs(R+f'guides/{SL}',exist_ok=True); open(R+f'guides/{SL}/index.html','w',encoding='utf-8').write(out)
for tg in ['div','figure','picture','p','a','ul','li','details','section','h2']:
    assert len(re.findall(f'<{tg}[ >]',out))==len(re.findall(f'</{tg}>',out)),tg
for m in re.findall(r'<script type="application/ld\+json">(.*?)</script>',out,re.S): json.loads(m)
im=Image.open(R+'images/og/og-guides-matsue-castle.jpg').convert('RGB'); d=ImageDraw.Draw(im)
d.rectangle([40,150,1170,380],fill=(252,240,242))
f1=ImageFont.truetype(glob.glob('/usr/share/fonts/**/DejaVuSerif-Bold.ttf',recursive=True)[0],48)
f2=ImageFont.truetype(glob.glob('/usr/share/fonts/**/NotoSerifCJK-Bold.ttc',recursive=True)[0],28,index=0)
l1="Shuri Castle Guide:"; l2="Ryukyu's Red Palace"; print(d.textlength(l2,font=f1)); assert d.textlength(l2,font=f1)<1090
d.text((66,170),l1,font=f1,fill=(26,15,15)); d.text((66,238),l2,font=f1,fill=(26,15,15)); d.text((66,332),"首里城",font=f2,fill=(138,125,120))
im.save(R+f'images/og/og-guides-{SL}.jpg',quality=88); print('built',len(out))
