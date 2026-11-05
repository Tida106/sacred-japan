import re,json,os,glob
from PIL import Image,ImageDraw,ImageFont
R='/home/claude/sacred-japan/'; SL='gifu-castle'
s=open(R+'guides/kochi-castle/index.html',encoding='utf-8').read()
i=s.index('<main>'); j=s.index('</main>'); head,tail=s[:i],s[j:]
TITLE="Gifu Castle Guide: Nobunaga's Mountain Castle, Its Closed Keep and What You Can Still See"
DESC="A licensed guide's guide to Gifu Castle on Mount Kinka: Saito Dosan, Oda Nobunaga, the 1956 keep that is closed for seismic work until late 2027, the ropeway, the ruins you can still walk and how to get there."
TAG="Nobunaga's mountain castle above Gifu, with the keep closed until late 2027."
head=re.sub(r'<title>.*?</title>',f'<title>{TITLE} | Sacred Japan</title>',head,count=1)
head=re.sub(r'(<meta (?:name="description"|property="og:description"|name="twitter:description") content=")[^"]*(")',lambda m:m.group(1)+DESC+m.group(2),head)
head=re.sub(r'(<meta (?:property="og:title"|name="twitter:title") content=")[^"]*(")',lambda m:m.group(1)+TITLE+m.group(2),head)
head=re.sub(r'("headline": ")[^"]*(")',lambda m:m.group(1)+TITLE+m.group(2),head)
head=re.sub(r'("description": ")A licensed[^"]*(")',lambda m:m.group(1)+DESC+m.group(2),head)
head=re.sub(r'("date(?:Published|Modified)": ")[^"]*(")',lambda m:m.group(1)+'2026-11-05'+m.group(2),head)
head=re.sub(r'<meta name="keywords" content="[^"]*">','<meta name="keywords" content="Gifu Castle, Gifu Castle closed, Mount Kinka ropeway, Oda Nobunaga castle, Saito Dosan, Inabayama Castle, Gifu Park, Japan castles">',head)
head=head.replace('guides/kochi-castle','guides/gifu-castle').replace('guide_kochi_','guide_gifu_castle_').replace('og-guides-kochi-castle','og-guides-gifu-castle')
head=head.replace('高知城','岐阜城').replace('Kochi Castle','Gifu Castle')
head=re.sub(r"<h1>.*?</h1>","<h1><em>Gifu Castle</em>: Nobunaga's Mountain Castle, Its Closed Keep and What You Can Still See</h1>",head,count=1,flags=re.S)
head=head.replace("Shikoku's original keep, and the only castle where the lord's palace still stands beside it.",TAG)
faqs=[
("Can I go inside Gifu Castle right now?","No. GLTJP says the keep is closed for seismic reinforcement from 19 May 2026 to late October 2027, and followingtheshogun gives the same dates and says reopening is planned for November 2027. followingtheshogun adds that the museum has been closed since 1 April 2026. Dates can change, so please check the City of Gifu or the ropeway&rsquo;s own pages before you go."),
("Is it still worth visiting while the keep is closed?","It depends on what you want. The stone walls, the well and the area around the keep are free to walk, the ropeway is running, and the ruins of Nobunaga&rsquo;s residence at the foot of the mountain are open (followingtheshogun). What you cannot do is climb the keep for the 360-degree view or see the museum. If the view and the exhibits are the point, waiting until the reopening planned for November 2027 is reasonable."),
("How do I get to the top?","Take the Mt. Kinka Ropeway from Gifu Park. The ride takes about 4 minutes (GLTJP, Nippon.com), and the walk from the top station to the castle is about 8 minutes (GLTJP, go-centraljapan), though Nippon.com says 10 and another source says 15. You can also hike one of four routes of 1.1 to 2.3 km, which GLTJP puts at 40 to 60 minutes each. followingtheshogun says that sections of the trails near the summit are closed until the end of September 2027, so check which routes are open."),
("How much does it cost?","The keep and museum ticket is 200 yen for adults and 100 yen for children (GLTJP, Nippon.com, go-centraljapan), but both are closed. The ropeway is 1,300 yen round trip for adults and 650 yen for children, or 800 and 400 yen one way (followingtheshogun). Nippon.com gives 1,100 yen round trip, which may be an older price. The ruins and Gifu Park are free (followingtheshogun)."),
("Does the ropeway run all year?","followingtheshogun says it runs normally but lists maintenance suspensions on 1 to 28 December 2026 and 7 January to 16 February 2027. I found that in one source only, so please check the ropeway&rsquo;s own site before planning around those dates."),
("How do I get to Gifu from Nagoya?","followingtheshogun says the JR Tokaido Main Line rapid takes about 20 minutes and costs about 480 yen. From JR Gifu or Meitetsu Gifu Station, GLTJP says a Gifu Bus (the N80 or the City Loop Line) takes about 15 minutes to Gifu Park, followed by a 3-minute walk to the ropeway&rsquo;s Sanroku Station. Bus stop names differ between sources, so check the sign on the bus."),
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
assert not re.search('Kochi|Shikoku|kochi|Kanazawa|Shuri|Naha|Takeda Castle|Asago|Machu|Odawara|Hojo|Aizu|Tsuruga|Goryokaku|Hakodate|Ezo|Sendai|Aoba|Masamune|Wakayama|Kishu',hh),re.findall('.{30}(?:Kochi|Shikoku|Kanazawa|Shuri|Naha|Aizu|Tsuruga|Goryokaku|Hakodate).{20}',hh)
IL='class="inline-link"'
main='''<main>

  <!-- TABLE OF CONTENTS -->
  <aside class="toc" aria-label="Table of contents">
    <div class="toc-label">TABLE OF CONTENTS ／ 目次</div>
    <div class="toc-title">In This Guide</div>
    <ol>
      <li><a href="#opening">A Castle on a Mountain, Closed Until 2027</a></li>
      <li><a href="#history">Inabayama, Dosan and Nobunaga</a></li>
      <li><a href="#keep">The Keep: Three Builds in a Century</a></li>
      <li><a href="#closed">What Is Closed, What Is Open</a></li>
      <li><a href="#see">What to See Today</a></li>
      <li><a href="#visit">Visiting Gifu Castle</a></li>
      <li><a href="#stay">Making It a Trip</a></li>
      <li><a href="#faq">Frequently Asked Questions</a></li>
      <li><a href="#final">Before You Go Up</a></li>
    </ol>
  </aside>

  <article>

    <section id="opening">
      <p class="opening">As a licensed guide, I describe Gifu Castle as a place where the mountain matters more than the building. The keep you see from town is a 1956 reconstruction, but the hill under it, Mount Kinka, is where Saito Dosan made his stronghold and where Oda Nobunaga chose the name Gifu in 1567 for the castle and the town below.</p>
      <p>One thing to know before you plan anything: the keep and museum are currently closed for seismic reinforcement. GLTJP gives the closure as 19 May 2026 to late October 2027, and followingtheshogun says reopening is planned for November 2027. The ropeway still runs and the ruins are still open, so this guide tells you what you can do now and what to save for later. Where my sources disagree I say so, and I mark claims I found in only one.</p>
    </section>

    <h2 id="history">Inabayama, Dosan and Nobunaga<span class="h2-jp">岐阜城の歴史</span></h2>
    <p>The castle was first called Inabayama Castle. GLTJP says a Kamakura shogunate official set up a fortress on the mountain in 1201. go-centraljapan names him as Nikaido Yukimasa, and the Japanese government&rsquo;s multilingual database (MLIT) says the first fortification is believed to date from 1201 to 1204 and was built by the Nikaido clan. In the 15th century, GLTJP says, Saito Dosan developed the castle. MLIT is more specific: Dosan took the mountain in 1539 and his family held it for three generations.</p>
    <p>In 1567 Oda Nobunaga defeated Saito Tatsuoki, took the castle and its town, and renamed the castle Gifu (MLIT, Nippon.com). Nippon.com says he used a seal reading <em>tenka fubu</em>, &ldquo;unify the realm with military might.&rdquo; He moved his base to Azuchi Castle in 1576 and left Gifu to his son Nobutada (Nippon.com). Both men died in the Honnoji Incident of 1582.</p>
    <p>The end came after Nobunaga. MLIT says that in 1600, under Oda Hidenobu, the castle was attacked by Tokugawa Ieyasu&rsquo;s forces and destroyed. GLTJP says Ieyasu ordered the castle abandoned in 1601, and Nippon.com says he had it torn down after Sekigahara. The year differs between sources, so I give 1600 to 1601. MLIT adds that some stone walls and wooden structures were reused to build Kano Castle a few kilometers to the south. GLTJP&rsquo;s FAQ counts 22 lords before the abandonment.</p>
    <p>MLIT says the ruins cover more than 2 square kilometers and are a National Historic Site. It also quotes a contemporary account: a Portuguese missionary called the palace and gardens at the foot of the mountain a &ldquo;paradise on earth.&rdquo; Nippon.com says excavations of Nobunaga&rsquo;s residence began in 1984 and found gold-leafed chrysanthemum and peony tiles, with a 2012 analysis confirming the gold leaf.</p>

    <h2 id="keep">The Keep: Three Builds in a Century<span class="h2-jp">天守</span></h2>
    <p>GLTJP and Nippon.com agree on the modern keep&rsquo;s history. A wooden replica was built in 1910 (GLTJP calls it Japan&rsquo;s first replica keep, and Nippon.com says it was a tourist attraction). Fire destroyed it in 1943. The present reinforced-concrete keep was completed in 1956, funded by local donations (GLTJP). It has three tiers and four floors, and Nippon.com says the lower three floors hold a museum and the top floor is an observation area. Nippon.com also says the modern keep follows historic records for its dimensions and appearance, and that the stone walls are original, dating from the Warring States period.</p>
    <p>I tell visitors plainly: this is not an original keep, and nobody knows exactly what Nobunaga&rsquo;s tower looked like. What you come for is the position, high above the Nagara River, and the walls that are original.</p>

    <h2 id="closed">What Is Closed, What Is Open<span class="h2-jp">現在の見学状況</span></h2>
    <ul class="practical-list">
      <li><strong>Keep:</strong> closed since 19 May 2026 for seismic reinforcement; late October 2027 end, reopening planned November 2027 (GLTJP, followingtheshogun).</li>
      <li><strong>Museum:</strong> followingtheshogun says it has been closed since 1 April 2026 on the same schedule. I found that date in one source only.</li>
      <li><strong>Summit ruins and the area around the keep:</strong> free and open, including the presumed first gate ruins, the stone walls and the well remains (followingtheshogun).</li>
      <li><strong>Gifu Park at the foot of the mountain:</strong> free and open, with the ruins of Nobunaga&rsquo;s residence, the garden ruins, Mitarashi Pond and an excavation information center that, according to followingtheshogun, is open 9:00 to 16:00 and closed on Tuesdays.</li>
      <li><strong>Ropeway:</strong> running, with maintenance suspensions listed for 1 to 28 December 2026 and 7 January to 16 February 2027 (followingtheshogun, one source).</li>
      <li><strong>Trails and toilets:</strong> followingtheshogun says some trail sections near the summit are closed until the end of September 2027 and the summit toilets are out of service until then. One source only.</li>
    </ul>
    <p>Everything above can change, so please check the City of Gifu before you travel.</p>

    <h2 id="see">What to See Today<span class="h2-jp">見どころ</span></h2>
    <p><strong>The ropeway and the view of the plain.</strong> The Mt. Kinka Ropeway leaves from Sanroku Station in Gifu Park and reaches the summit in about 4 minutes (GLTJP, Nippon.com). GLTJP&rsquo;s ropeway page says it runs every 15 minutes, or every 10 minutes at peak times. Even with the keep closed, the ride gives a view over Gifu and the Nagara River.</p>
    <p><strong>The walls and the area around the keep.</strong> The stone walls near the summit are the oldest thing here. Walk the grounds slowly and imagine the keep as a lookout and not as the centerpiece. On rainy days, followingtheshogun suggests the lower slopes instead, because the summit steps get slippery.</p>
    <p><strong>Gifu Park and Nobunaga&rsquo;s residence.</strong> At the foot of the mountain, GLTJP says the park was the site of the residences of Dosan and Nobunaga, with excavation still going on as of 2021. This is where the gold-leaf tiles were found. It is free and flat, which makes it a good alternative on a day with no view.</p>
    <p><strong>The Squirrel Village.</strong> GLTJP&rsquo;s ropeway page says a squirrel village just outside the summit station was created in 1965 as Japan&rsquo;s first, using the wild squirrels on the mountain. I could not confirm whether it is open during the keep closure, so please check.</p>
    <p><strong>The Nagara River and cormorant fishing.</strong> The river runs below the castle and is known for <em>ukai</em>, fishing with trained cormorants from small boats. GLTJP says Nobunaga invited guests to watch it as hospitality and the Edo shogunate protected it. I did not verify the current season dates or ticket prices, so please check those separately if you want to go.</p>
    <p><strong>Autumn color.</strong> GLTJP says the foliage usually peaks from early to late November, and lists Japanese maple, ginkgo and lacquer trees. It also says the castle is on a &ldquo;Hida-Mino 33 Selections&rdquo; list of autumn spots. Given the December ropeway suspension listed above, late November is the time to go if you want both.</p>
    <p><strong>A goshuin stamp.</strong> GLTJP says a goshuin with the Oda clan crest is sold at the shop by the ropeway station, with a premium version at some events.</p>

    <h2 id="visit">Visiting Gifu Castle<span class="h2-jp">アクセス</span></h2>
    <ul class="practical-list">
      <li><strong>From Nagoya:</strong> JR Tokaido Main Line rapid to JR Gifu Station, about 20 minutes and about 480 yen (followingtheshogun).</li>
      <li><strong>To Gifu Park:</strong> Gifu Bus from JR Gifu or Meitetsu Gifu Station, about 15 minutes on the N80 or the City Loop Line, then about 3 minutes on foot to Sanroku Station (GLTJP). Stop names differ between sources, so check the sign.</li>
      <li><strong>Ropeway:</strong> about 4 minutes, then about 8 minutes on foot to the castle (GLTJP, go-centraljapan); Nippon.com says 10 minutes. Fare 1,300 yen round trip for adults and 650 yen for children, or 800 and 400 yen one way (followingtheshogun). Nippon.com gives 1,100 yen, which may be older.</li>
      <li><strong>Hiking:</strong> four routes of 1.1 to 2.3 km, 40 to 60 minutes each (GLTJP). Some sections near the summit are closed (see above).</li>
      <li><strong>Normal keep hours (when it reopens):</strong> GLTJP gives 9:30 to 17:30 from 16 March to 16 October and 9:30 to 16:30 from 17 October to 15 March, with 6:30 to 16:30 on 1 January. go-centraljapan adds an 8:30 opening from 12 May to 16 October. Please check the official pages at that time.</li>
      <li><strong>Normal keep and museum ticket:</strong> 200 yen for adults and 100 yen for children, for ages 4 to under 16 (GLTJP).</li>
    </ul>

    <h2 id="stay">Making It a Trip<span class="h2-jp">滞在</span></h2>
    <p>Gifu is an easy day trip from Nagoya, and it pairs well with our <a href="/guides/inuyama-castle/" '''+IL+''' onclick="trackEvent('click','internal','guide_gifu_castle_to_inuyama')">Inuyama Castle guide</a>, which is one of Japan&rsquo;s oldest original keeps and was built by Nobunaga&rsquo;s uncle (per GLTJP). The keep at <a href="/guides/nagoya-castle/" '''+IL+''' onclick="trackEvent('click','internal','guide_gifu_castle_to_nagoya')">Nagoya Castle</a> is also closed at the moment, so Inuyama is the better choice for going inside a castle in this part of Japan.</p>
    <div class="key-callout">
      <p>&#127890; <strong>Plan your trip:</strong> Browse guided tours or plan a stay around Gifu. <a href="https://www.viator.com/search/Gifu?pid=P00298374&amp;mcid=42383&amp;medium=link&amp;campaign=sacred-japan" target="_blank" rel="noopener" onclick="trackEvent('click','affiliate','viator_gifu_castle_inline')">Find tours on Viator &rarr;</a></p>
    </div>

    <h2 id="faq">Frequently Asked Questions<span class="h2-jp">よくあるご質問</span></h2>
    <div class="faq-stack">
'''+''.join(f'''    <details class="faq-item">
        <summary>{q}</summary>
        <div class="faq-answer">{a}</div>
    </details>
''' for q,a in faqs)+'''    </div>

    <h2 id="final">Before You Go Up<span class="h2-jp">むすびに</span></h2>
    <p>Go for the ropeway, the walls and the view of the Nagara River, and treat the closed keep as a reason to return in late 2027. If you need an open keep today, Inuyama is the safer choice, and if you want Nobunaga, the walls above the plain are still the place to stand.</p>

    <div class="closing-block">
      <span class="torii">&#9961;&#65039;</span>
      <p>The man who named Gifu left it in 1576, but the mountain kept his name.</p>
    </div>

    <!-- RELATED GUIDES -->
    <section class="related-section">
      <h2>Related Guides</h2>
      <span class="h2-jp">関連ガイド</span>

      <div class="related-grid">

        <a class="related-card" href="/guides/inuyama-castle/" onclick="trackEvent('click','internal','related_gifu_castle_to_inuyama')">
          <div class="related-card-label">SACRED JAPAN ／ GUIDES</div>
          <div class="related-card-title">&#127983; Inuyama Castle Guide &rarr;</div>
          <div class="related-card-desc">A keep on a cliff over the Kiso River.</div>
        </a>

        <a class="related-card" href="/guides/nagoya-castle/" onclick="trackEvent('click','internal','related_gifu_castle_to_nagoya')">
          <div class="related-card-label">SACRED JAPAN ／ GUIDES</div>
          <div class="related-card-title">&#127983; Nagoya Castle Guide &rarr;</div>
          <div class="related-card-desc">The golden shachi and a rebuilt palace.</div>
        </a>

        <a class="related-card" href="/castles/" onclick="trackEvent('click','internal','related_gifu_castle_to_castles')">
          <div class="related-card-label">SACRED JAPAN ／ CASTLES</div>
          <div class="related-card-title">&#127983; Japan's Castles &rarr;</div>
          <div class="related-card-desc">Every castle guide, with photos and official links.</div>
        </a>

      </div>
    </section>

  </article>

'''
tail=tail.replace('kochi-castle',SL).replace('_kochi_','_gifu_castle_').replace('DKochi','DGifu').replace('search/Kochi','search/Gifu')
def L(u,l,t): return f'<a href="{u}" target="_blank" rel="noopener" style="color:var(--beni);text-decoration:underline;" onclick="trackEvent(\'click\',\'external\',\'{l}\')">{t}</a>'
src='Sources verified at time of writing: '+', '.join([
 L('https://www.gltjp.com/en/article/item/20350/','src_gifu_gltjp','GLTJP'),
 L('https://www.nippon.com/en/guide-to-japan/gu900238/','src_gifu_nippon','Nippon.com'),
 L('https://www.mlit.go.jp/tagengo-db/en/H30-00670.html','src_gifu_mlit','MLIT multilingual database'),
 L('https://go-centraljapan.jp/route/dragon/en/14.html','src_gifu_gcj','Go Central Japan'),
 L('https://followingtheshogun.com/gifu_park_eng/','src_gifu_fts','Following the Shogun'),
])+'. Hours, prices and availability change'
tail,n=re.subn(r'Sources verified at time of writing:.*?Hours, prices and availability change',lambda m:src,tail,flags=re.S); assert n==1
out=head+main+tail
assert not re.search('Kochi|Shikoku|kochi|Takato|Nagano',re.sub(r'"mainEntity": \[.*','',out,flags=re.S)),re.findall('.{30}(?:Kochi|Takato|Nagano).{20}',out)
os.makedirs(R+f'guides/{SL}',exist_ok=True); open(R+f'guides/{SL}/index.html','w',encoding='utf-8').write(out)
for tg in ['div','figure','picture','p','a','ul','li','details','section','h2']:
    assert len(re.findall(f'<{tg}[ >]',out))==len(re.findall(f'</{tg}>',out)),tg
for m in re.findall(r'<script type="application/ld\+json">(.*?)</script>',out,re.S): json.loads(m)
im=Image.open(R+'images/og/og-guides-matsue-castle.jpg').convert('RGB'); d=ImageDraw.Draw(im)
d.rectangle([40,150,1170,380],fill=(252,240,242)); d.rectangle([1118,66,1160,96],fill=(252,240,242))
f1=ImageFont.truetype(glob.glob('/usr/share/fonts/**/DejaVuSerif-Bold.ttf',recursive=True)[0],48)
f2=ImageFont.truetype(glob.glob('/usr/share/fonts/**/NotoSerifCJK-Bold.ttc',recursive=True)[0],28,index=0)
l1="Gifu Castle Guide:"; l2="Nobunaga's Hill, Keep Closed"; print(d.textlength(l2,font=f1)); assert d.textlength(l2,font=f1)<1090
d.text((66,170),l1,font=f1,fill=(26,15,15)); d.text((66,238),l2,font=f1,fill=(26,15,15)); d.text((66,332),"岐阜城",font=f2,fill=(138,125,120))
im.save(R+f'images/og/og-guides-{SL}.jpg',quality=88); print('built',len(out))
