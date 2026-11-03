import re,json,os,glob
from PIL import Image,ImageDraw,ImageFont
R='/home/claude/sacred-japan/'; SL='osaka-castle'
s=open(R+'guides/kochi-castle/index.html',encoding='utf-8').read()
i=s.index('<main>'); j=s.index('</main>'); head,tail=s[:i],s[j:]
TITLE="Osaka Castle Guide: A Keep Built Three Times, and the Walls Beneath It"
DESC="A licensed guide's guide to Osaka Castle: Hideyoshi's keep, the Tokugawa rebuild, the 1931 concrete tower, the stone walls that survived, the 2025 Stone Wall Museum, and how to visit."
head=re.sub(r'<title>.*?</title>',f'<title>{TITLE} | Sacred Japan</title>',head,count=1)
head=re.sub(r'(<meta (?:name="description"|property="og:description"|name="twitter:description") content=")[^"]*(")',lambda m:m.group(1)+DESC+m.group(2),head)
head=re.sub(r'(<meta (?:property="og:title"|name="twitter:title") content=")[^"]*(")',lambda m:m.group(1)+TITLE+m.group(2),head)
head=re.sub(r'("headline": ")[^"]*(")',lambda m:m.group(1)+TITLE+m.group(2),head)
head=re.sub(r'("description": ")A licensed[^"]*(")',lambda m:m.group(1)+DESC+m.group(2),head)
head=re.sub(r'<meta name="keywords" content="[^"]*">','<meta name="keywords" content="Osaka Castle, Osaka Castle guide, Osaka Castle history, Osaka Castle hours, Osaka Castle tickets, Osaka Castle cherry blossoms, Nishinomaru Garden, Toyotomi Hideyoshi castle, Osaka Castle stone walls, Osaka Castle Stone Wall Museum, Osaka Castle how to visit">',head)
head=head.replace('guides/kochi-castle','guides/osaka-castle').replace('guide_kochi_','guide_osaka_').replace('og-guides-kochi-castle','og-guides-osaka-castle')
head=head.replace('高知城','大阪城').replace('Kochi Castle','Osaka Castle')
head=re.sub(r"<h1>.*?</h1>","<h1><em>Osaka Castle</em>: A Keep Built Three Times, and the Walls Beneath It</h1>",head,count=1,flags=re.S)
head=head.replace("Shikoku's original keep, and the only castle where the lord's palace still stands beside it.","Hideyoshi's castle, rebuilt by the Tokugawa and again in 1931, with the stone walls that outlasted both.")
faqs=[
("How much does Osaka Castle cost and when is it open?","The Osaka Convention and Visitors Bureau and GLTJP list the keep at 1,200 yen for adults and 600 yen for university and high school students, with junior high students and younger free. Hours are 9:00 to 18:00 with last entry at 17:30, and the keep is closed from December 28 to January 1. Japan-guide says the 1,200 yen ticket also covers the Toyotomi Stone Wall Museum, which opened in 2025. Hours are extended in cherry blossom season, Golden Week and summer, and prices change, so please confirm on the official site before you go."),
("Is the keep original?","No. GLTJP and Japan-guide say the keep you see was built in 1931 with donations from Osaka citizens, and Japan-guide describes it as a ferro-concrete tower. Hideyoshi's keep dates to 1585 according to Wikipedia, and the Tokugawa built a new one around 1628 to 1630 that lightning burned down in 1665. The stone walls and several gates and turrets do survive from the Tokugawa rebuild."),
("Are the stone walls original?","Many are. Wikipedia says the walls built in the 1620s still stand and are made of interlocked granite blocks without mortar, many with crests of the families that supplied them. Japan-guide adds that older Toyotomi-era walls were buried when the Tokugawa rebuilt the castle and were rediscovered in the 1950s."),
("How do I get to Osaka Castle?","Japan-guide recommends entering through the Otemon gate at the southwest corner of the park, reached from Tanimachi 4-chome station, and notes that Osakajokoen station on the JR Loop Line is about 10 minutes and 180 yen from JR Osaka Station. Walking times to the keep vary by source, from about 10 to 20 minutes, so allow extra time for the large grounds."),
("When are the cherry blossoms and is Nishinomaru Garden worth paying for?","Japan-guide says blossoms usually appear in late March and early April and that Nishinomaru Garden is especially popular then, staying open until 21:00 in the 2026 season. The garden charges a separate fee, given as 300 yen (350 in blossom season) by Japan-guide and 200 yen by another guide, and the tree count is given as about 600 and about 300, so treat those numbers as approximate and check locally."),
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
assert not re.search('Kochi|Shikoku|kochi',hh),re.search('.{50}(Kochi|Shikoku|kochi).{50}',hh,re.S).group(0)
main='''<main>

  <!-- TABLE OF CONTENTS -->
  <aside class="toc" aria-label="Table of contents">
    <div class="toc-label">TABLE OF CONTENTS ／ 目次</div>
    <div class="toc-title">In This Guide</div>
    <ol>
      <li><a href="#opening">The Castle That Was Built Three Times</a></li>
      <li><a href="#history">From Hideyoshi to the Tokugawa</a></li>
      <li><a href="#keep">The 1931 Keep and What Is Inside</a></li>
      <li><a href="#walls">The Walls: What Really Survived</a></li>
      <li><a href="#grounds">Moats, Gardens and the Park</a></li>
      <li><a href="#visit">Visiting Osaka Castle</a></li>
      <li><a href="#stay">Making It a Trip</a></li>
      <li><a href="#faq">Frequently Asked Questions</a></li>
      <li><a href="#final">Look Down, Not Just Up</a></li>
    </ol>
  </aside>

  <article>

    <section id="opening">
      <p class="opening">As a licensed guide, I tell guests at Osaka Castle to do something unusual: look at the ground before the tower. The keep that fills every postcard is a 1931 concrete reconstruction. The stone beneath it is the real thing, much of it laid in the 1620s. That is what makes this castle worth an hour of your time.</p>
      <p>This guide covers Hideyoshi's castle and its fall, the Tokugawa rebuild and the lightning strike, the 1931 keep and its museum, the walls and the new Stone Wall Museum, the park and Nishinomaru Garden, and the practical details of a visit.</p>
    </section>

    <h2 id="history">From Hideyoshi to the Tokugawa<span class="h2-jp">築城と再建</span></h2>
    <p>Japan-guide says Toyotomi Hideyoshi began Osaka Castle in 1583 on the site of the Ishiyama Hongan-ji temple, intending it as the centre of a unified Japan, and calls it the largest castle of its time. Wikipedia says the plan was modeled on Oda Nobunaga's Azuchi Castle, that the inner keep was finished in 1585 and that the whole castle was completed in 1597, a year before Hideyoshi died.</p>
    <p>The Toyotomi lasted only a little longer. Wikipedia says Tokugawa forces of about 200,000 laid siege in the winter of 1614 and had the outer moat filled in. When the Toyotomi tried to restore it in the summer of 1615, the Tokugawa broke through, Hideyori and his mother Yodo-dono died, and the castle burned. GLTJP and Japan-guide both date the destruction to 1615.</p>
    <p>The Tokugawa did not abandon the site. Wikipedia says Tokugawa Hidetada began rebuilding it in 1620, building over the Toyotomi castle, and that a new main tower went up between 1628 and 1630. GLTJP gives 1626 for that rebuild, so treat the exact year as uncertain. The new keep did not last: GLTJP and Wikipedia say lightning destroyed it in 1665, and Japan-guide says it was never rebuilt in the feudal era.</p>
    <p>After that the castle declined. Wikipedia says the bakufu paid for repairs in 1843, that several buildings burned during the fighting of 1868 and that the Honmaru Palace was lost in the Boshin War. The site then became an army arsenal. Wikipedia says American bombing on 14 August 1945 destroyed about 90 percent of the arsenal and killed 382 people, while Japan-guide says the castle survived the city's air raids.</p>

    <h2 id="keep">The 1931 Keep and What Is Inside<span class="h2-jp">天守</span></h2>
    <p>GLTJP says the present keep was reconstructed in 1931 with donations from Osaka citizens, and Japan-guide describes it as ferro-concrete. Wikipedia says it has five tiers outside and eight floors inside, on a tall stone base, with elevators. The Osaka tourism site gives its height as 55 meters. A renovation ran from 1995 to 1997, after which GLTJP says the tower was registered as a tangible cultural property.</p>
    <p>Inside, GLTJP says the keep is a history museum. It describes a miniature of the Summer Campaign screen, a full-scale model of Hideyoshi's golden tea room and full-scale replicas of the shachi roof ornaments, with a museum shop on the first floor. The observation deck is on the eighth floor and gives a 360-degree view over the city according to one guide. GLTJP adds that for about 500 yen you can try on a replica helmet or a kosode kimono, though another guide says that may be paid, so check on the day.</p>
    <p>Wikipedia says Hideyoshi's own plan was a five-story keep with three underground floors and gold leaf on its sides. I mention it because the golden tower of popular imagination belongs to Hideyoshi, not to what you climb today. The modern keep is white with green tiles and gold ornaments.</p>

    <h2 id="walls">The Walls: What Really Survived<span class="h2-jp">石垣</span></h2>
    <p>Wikipedia says the walls built in the 1620s still stand, made of interlocked granite boulders with no mortar. Many stones came from quarries near the Seto Inland Sea, and many carry carved crests of the families that supplied them. Wikipedia lists the Octopus Stone, Tako-ishi, among the castle's megaliths but gives no size, so I will not quote one.</p>
    <p>Japan-guide adds a detail I find moving. When the Tokugawa rebuilt, they buried the original Toyotomi walls, and those older stones were rediscovered in the 1950s. Japan-guide says the Toyotomi Stone Wall Museum opened next to the keep in 2025 and is included in the keep ticket. I have only that one source for the museum, so confirm what you can see at the official site.</p>
    <p>Wikipedia says the government has designated thirteen structures as important cultural properties, including the Otemon and Sakuramon gates, several turrets, the Kinmeisui well, the Kinzo storehouse and the Enshogura gunpowder magazine. Most of these are Tokugawa-era and stand outside the keep, so a walk around the walls shows you far more original fabric than the tower does.</p>

    <h2 id="grounds">Moats, Gardens and the Park<span class="h2-jp">堀と庭園</span></h2>
    <p>Wikipedia says the outer moat surrounds the whole castle in four water-filled sections, while the inner moat has a wet section on the northeast and a dry section on the southwest. Japan-guide says the park holds the citadels, gates, turrets, stone walls and moats, plus green space, sports facilities, a multi-purpose arena and a shrine dedicated to Hideyoshi.</p>
    <p>Nishinomaru Garden covers the former western citadel. Japan-guide describes a lawn garden with a tea house and the former Osaka Guest House, and says it gives good views up at the keep. It charges a separate fee and is closed on Mondays. The tree count is about 600 in Japan-guide and about 300 in another guide, so I would not quote a number to anyone. One guide also mentions a 20-minute boat cruise on the inner moat, called Gozabune, which I could not verify further.</p>

    <h2 id="visit">Visiting Osaka Castle<span class="h2-jp">アクセス</span></h2>
    <ul class="practical-list"><li><strong>Getting there:</strong> Japan-guide recommends the Otemon gate at the southwest corner, reached from Tanimachi 4-chome station, and says Osakajokoen station on the JR Loop Line is about 10 minutes and 180 yen from JR Osaka Station. GLTJP gives walking times of about 16 to 20 minutes from the nearest stations, and other guides say 10 to 20, so allow time.</li><li><strong>Tickets:</strong> 1,200 yen for adults, 600 yen for university and high school students with ID, and free for junior high students and younger with proof of age (Osaka tourism site). Japan-guide says the same ticket includes the Stone Wall Museum.</li><li><strong>Hours:</strong> 9:00 to 18:00, last entry 17:30, closed December 28 to January 1, with extended hours in cherry blossom season, Golden Week and summer (GLTJP).</li><li><strong>Queues:</strong> Japan-guide says lines can pass 30 minutes on busy days and suggests buying e-tickets in advance.</li><li><strong>Nishinomaru Garden:</strong> Japan-guide gives 9:00 to 17:00 (16:30 from November to February), closed Mondays and December 28 to January 4, with later hours in blossom season. Fees differ by source, so confirm on site.</li></ul>

    <h2 id="stay">Making It a Trip<span class="h2-jp">滞在</span></h2>
    <p>If Osaka Castle makes you curious about the keeps that did survive, our guides to <a href="/guides/himeji-castle/" class="inline-link" onclick="trackEvent('click','internal','guide_osaka_to_himeji')">Himeji Castle</a> and <a href="/guides/nijo-castle/" class="inline-link" onclick="trackEvent('click','internal','guide_osaka_to_nijo')">Nijo Castle</a> in Kyoto are the natural next steps, and both are an easy rail ride away.</p>
    <div class="key-callout">
      <p>&#127890; <strong>Plan your trip:</strong> Browse guided tours, or plan a stay in Osaka. <a href="https://www.viator.com/search/Osaka?pid=P00298374&amp;mcid=42383&amp;medium=link&amp;campaign=sacred-japan" target="_blank" rel="noopener sponsored" onclick="trackEvent('click','affiliate','viator_osaka_local')">Browse Osaka tours &rarr;</a></p>
    </div>

    <h2 id="faq">Frequently Asked Questions<span class="h2-jp">よくあるご質問</span></h2>
    <div class="faq-stack">
'''+''.join(f'''    <details class="faq-item">
        <summary>{q}</summary>
        <div class="faq-answer">{a}</div>
    </details>
''' for q,a in faqs)+'''    </div>

    <h2 id="final">Look Down, Not Just Up<span class="h2-jp">むすびに</span></h2>
    <p>Osaka Castle has lost its keep twice and gained a third, yet the foundations have held for about four centuries. Take the elevator up for the view, then spend longer walking the walls. That is where the castle's real age is.</p>

    <div class="closing-block">
      <span class="torii">&#9961;&#65039;</span>
      <p>The tower is new. The stone is not.</p>
    </div>

    <!-- RELATED GUIDES -->
    <section class="related-section">
      <h2>Related Guides</h2>
      <span class="h2-jp">関連ガイド</span>

      <div class="related-grid">

        <a class="related-card" href="/guides/himeji-castle/" onclick="trackEvent('click','internal','related_osaka_to_himeji')">
          <div class="related-card-label">SACRED JAPAN ／ GUIDES</div>
          <div class="related-card-title">&#127983; Himeji Castle Guide &rarr;</div>
          <div class="related-card-desc">Japan's best-known surviving keep.</div>
        </a>

        <a class="related-card" href="/guides/nijo-castle/" onclick="trackEvent('click','internal','related_osaka_to_nijo')">
          <div class="related-card-label">SACRED JAPAN ／ GUIDES</div>
          <div class="related-card-title">&#127983; Nijo Castle Guide &rarr;</div>
          <div class="related-card-desc">Kyoto's shogun palace and its singing floors.</div>
        </a>

        <a class="related-card" href="/castles/" onclick="trackEvent('click','internal','related_osaka_to_castles')">
          <div class="related-card-label">SACRED JAPAN ／ CASTLES</div>
          <div class="related-card-title">&#127983; Japan's Castles &rarr;</div>
          <div class="related-card-desc">Every castle guide, with photos and official links.</div>
        </a>

      </div>
    </section>

  </article>

'''
tail=tail.replace('kochi-castle',SL).replace('_kochi_','_osaka_')
def L(u,l,t): return f'<a href="{u}" target="_blank" rel="noopener" style="color:var(--beni);text-decoration:underline;" onclick="trackEvent(\'click\',\'external\',\'{l}\')">{t}</a>'
src='Sources verified at time of writing: '+', '.join([
 L('https://cdn.gltjp.com/en/directory/item/11618','src_osaka_gltjp','GLTJP'),
 L('https://www.japan-guide.com/e/e4000.html','src_osaka_japanguide','Japan-guide'),
 L('https://osaka-info.jp/en/spot/osaka-castle-main-keep/','src_osaka_osakainfo','Osaka tourism site'),
 L('https://en.wikipedia.org/wiki/Osaka_Castle','src_osaka_wikipedia','Wikipedia'),
])+'. Hours, prices and availability change'
tail,n=re.subn(r'Sources verified at time of writing:.*?Hours, prices and availability change',lambda m:src,tail,flags=re.S); assert n==1
tail=tail.replace('destination%3DKochi','destination%3DOsaka').replace('search/Kochi','search/Osaka')
out=head+main+tail
chk=re.sub(r'Kochi','',out); 
assert not re.search('Kochi|Shikoku|kochi|Uwajima',re.sub(r'"mainEntity": \[.*','',out,flags=re.S)),re.search('.{60}(Kochi|Shikoku|kochi|Uwajima).{60}',out,re.S).group(0)
os.makedirs(R+f'guides/{SL}',exist_ok=True); open(R+f'guides/{SL}/index.html','w',encoding='utf-8').write(out)
for tg in ['div','figure','picture','p','a','ul','li','details','section','h2']:
    assert len(re.findall(f'<{tg}[ >]',out))==len(re.findall(f'</{tg}>',out)),tg
for m in re.findall(r'<script type="application/ld\+json">(.*?)</script>',out,re.S): json.loads(m)
im=Image.open(R+'images/og/og-guides-matsue-castle.jpg').convert('RGB'); d=ImageDraw.Draw(im)
d.rectangle([40,150,1170,380],fill=(252,240,242))
f1=ImageFont.truetype(glob.glob('/usr/share/fonts/**/DejaVuSerif-Bold.ttf',recursive=True)[0],48)
f2=ImageFont.truetype(glob.glob('/usr/share/fonts/**/NotoSerifCJK-Bold.ttc',recursive=True)[0],28,index=0)
l2="A Keep Built Three Times"; assert d.textlength(l2,font=f1)<1090
d.text((66,170),"Osaka Castle Guide:",font=f1,fill=(26,15,15)); d.text((66,238),l2,font=f1,fill=(26,15,15)); d.text((66,332),"大阪城",font=f2,fill=(138,125,120))
im.save(R+f'images/og/og-guides-{SL}.jpg',quality=88); print('built',len(out))
