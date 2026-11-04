import re,json,os,glob
from PIL import Image,ImageDraw,ImageFont
R='/home/claude/sacred-japan/'; SL='takeda-castle-ruins'
s=open(R+'guides/kochi-castle/index.html',encoding='utf-8').read()
i=s.index('<main>'); j=s.index('</main>'); head,tail=s[:i],s[j:]
TITLE="Takeda Castle Ruins Guide: Japan's Machu Picchu, the Cloud Sea and the Winter Closure"
DESC="A licensed guide's guide to the Takeda Castle Ruins in Asago, Hyogo: the stone walls on Mt. Kojo, when the sea of clouds appears, the Ritsuun-kyo viewpoint, the winter closure and how to get up there."
TAG="Stone walls on a 353-meter mountain in Asago, Hyogo: the 'castle in the sky' above the autumn cloud sea, closed from January to February."
head=re.sub(r'<title>.*?</title>',f'<title>{TITLE} | Sacred Japan</title>',head,count=1)
head=re.sub(r'(<meta (?:name="description"|property="og:description"|name="twitter:description") content=")[^"]*(")',lambda m:m.group(1)+DESC+m.group(2),head)
head=re.sub(r'(<meta (?:property="og:title"|name="twitter:title") content=")[^"]*(")',lambda m:m.group(1)+TITLE+m.group(2),head)
head=re.sub(r'("headline": ")[^"]*(")',lambda m:m.group(1)+TITLE+m.group(2),head)
head=re.sub(r'("description": ")A licensed[^"]*(")',lambda m:m.group(1)+DESC+m.group(2),head)
head=re.sub(r'("date(?:Published|Modified)": ")[^"]*(")',lambda m:m.group(1)+'2026-11-04'+m.group(2),head)
head=re.sub(r'<meta name="keywords" content="[^"]*">','<meta name="keywords" content="Takeda Castle Ruins, Takeda Castle, Takeda Jo, Japan Machu Picchu, Castle in the Sky, Tenku no Shiro, Asago, Hyogo castle, Ritsuun-kyo, sea of clouds, cloud sea Japan, Mt Kojo">',head)
head=head.replace('guides/kochi-castle','guides/takeda-castle-ruins').replace('guide_kochi_','guide_takeda_').replace('og-guides-kochi-castle','og-guides-takeda-castle-ruins')
head=head.replace('高知城','竹田城跡').replace('Kochi Castle','Takeda Castle Ruins')
head=re.sub(r"<h1>.*?</h1>","<h1><em>Takeda Castle Ruins</em>: Japan's Machu Picchu, the Cloud Sea and the Winter Closure</h1>",head,count=1,flags=re.S)
head=head.replace("Shikoku's original keep, and the only castle where the lord's palace still stands beside it.",TAG)
faqs=[
("When is the best time to see the sea of clouds at Takeda Castle?","japan-guide gives October and November, around sunrise (roughly 6:00 to 6:30), and says a sea of clouds appears on about one morning in three on average. thegate12 gives September to November, and GLTJP says autumn through early winter. Nothing is guaranteed, so I suggest staying more than one night if the view is the point."),
("Is Takeda Castle open in winter?","Only partly. All three sources I used say the ruins are closed from 4 January through the end of February. Early December to 3 January is a short-hours season (10:00 to 15:00 in japan-guide and GLTJP; thegate12 gives slightly different times). Please check the official Asago site for the exact reopening date."),
("How much does it cost to enter Takeda Castle?","Adults pay 500 yen; junior high students and younger are free (japan-guide, GLTJP, thegate12). Credit cards are not accepted at the entrance (GLTJP, thegate12), so bring cash. japan-guide adds a 300-yen environmental cooperation fee for the Ritsuun-kyo viewpoint."),
("How do I get to Takeda Castle Ruins?","From JR Takeda Station you can walk up in about 40 minutes (japan-guide, GLTJP; thegate12 says 30). The Tenku Bus runs from the station to the Takedajo-seki stop in about 20 minutes (300 yen one way, roughly hourly, not in winter), followed by a walk of about 20 minutes to the entrance. A taxi takes about 15 minutes to the trailhead for around 2,000 yen (japan-guide)."),
("Is the view from inside the ruins or from across the valley?","Both are worth it, but they are different. The famous cloud-sea photo is taken from Ritsuun-kyo, a viewpoint on the opposite slope, because from there you see the whole ridge and the walls. Inside the ruins you walk on the walls themselves and look out over the town."),
("Is anything of the castle still standing?","No buildings remain. What survives is the stone: GLTJP says the walls are almost entirely intact, following the contours of the mountain, and that the keep foundation and entrances are still visible."),
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
assert not re.search('Kochi|Shikoku|kochi|Kanazawa|Shuri|Naha',hh),re.findall('.{30}(?:Kochi|Shikoku|Kanazawa|Shuri|Naha).{20}',hh)
main='''<main>

  <!-- TABLE OF CONTENTS -->
  <aside class="toc" aria-label="Table of contents">
    <div class="toc-label">TABLE OF CONTENTS ／ 目次</div>
    <div class="toc-title">In This Guide</div>
    <ol>
      <li><a href="#opening">A Castle Made of Stone Only</a></li>
      <li><a href="#history">From 1400s Fortress to 1600 Abandonment</a></li>
      <li><a href="#walls">The Walls on Mt. Kojo</a></li>
      <li><a href="#clouds">The Sea of Clouds</a></li>
      <li><a href="#visit">Visiting Takeda Castle Ruins</a></li>
      <li><a href="#stay">Making It a Trip</a></li>
      <li><a href="#faq">Frequently Asked Questions</a></li>
      <li><a href="#final">A Castle in the Sky</a></li>
    </ol>
  </aside>

  <article>

    <section id="opening">
      <p class="opening">As a licensed guide, I tell visitors that Takeda Castle is the one place where you go to see a castle that is not there. No tower, no hall, no gate survives. What remains is a long ridge of stone walls on a mountain in Asago, Hyogo, and on a cold autumn morning, with cloud filling the valley below, they look as if they are floating. That is why people call it &ldquo;Japan&rsquo;s Machu Picchu&rdquo; and the &ldquo;castle in the sky.&rdquo;</p>
      <p>This guide covers the history, the walls, when the clouds actually come, and the practical details, including a long winter closure. Where my sources disagree, I say so, and I mark claims I found in only one place.</p>
    </section>

    <h2 id="history">From 1400s Fortress to 1600 Abandonment<span class="h2-jp">築城と廃城</span></h2>
    <p>The sources do not agree on the start. japan-guide says the castle was originally built in 1411. thegate12 says construction began in 1443 under Yamana Sozen and took 13 years. I would treat the founding as &ldquo;the 15th century&rdquo; and leave it there.</p>
    <p>japan-guide says Toyotomi Hideyoshi conquered the castle during one of his western campaigns, and thegate12 says Akamatsu Hirohide finished the stone walls in 1590. That second detail is from one source only. Both sources say the castle was abandoned after the Battle of Sekigahara in 1600, and thegate12 ties this to Akamatsu&rsquo;s defeat.</p>
    <p>After that it simply decayed for centuries. japan-guide says the ruins were restored in the 1970s and 1980s and opened to visitors. GLTJP says it is listed among Japan&rsquo;s Top 100 Castles and was designated a &ldquo;Lovers&rsquo; Sanctuary&rdquo; in 2012.</p>

    <h2 id="walls">The Walls on Mt. Kojo<span class="h2-jp">石垣</span></h2>
    <p>GLTJP puts the castle on Mt. Kojo (also called Mt. Torafusu) at 353.7 meters, and says the stone walls are almost entirely intact, following the natural terrain in a curved layout, with the keep foundation and entrances still visible. thegate12 gives the site as about 100 meters wide and 400 meters long. japan-guide describes a central fortress with three wings, on foundations that are largely intact.</p>
    <p>What this means on the ground: you walk along the tops of the walls and between the foundations, so the shape of the castle is something you feel with your feet. Because no buildings stand, nothing blocks the view down to the town.</p>

    <h2 id="clouds">The Sea of Clouds<span class="h2-jp">雲海</span></h2>
    <p>japan-guide says the best season is October and November, around sunrise (roughly 6:00 to 6:30), and that a sea of clouds appears on about one morning in three on average. thegate12 says September to November; GLTJP says autumn through early winter. These are not guarantees, and cold, calm, clear mornings after a humid day are what people hope for.</p>
    <p>The classic view is from <strong>Ritsuun-kyo</strong>, on the slope opposite the castle. japan-guide says the lower decks are a few steps from the parking lot, while viewpoints 1 and 2, which have the best view, are 10 to 40 minutes up a steep dirt trail. It lists a 300-yen environmental cooperation fee, and says there is no public transport there; by car it is about 10 minutes from the town center. Please wear shoes you trust on dirt in the dark.</p>
    <p>One practical point: the ruins open early in the cloud season (5:00 in japan-guide and GLTJP, 4:00 in thegate12), so you can be on the walls near dawn. I would still choose one morning at Ritsuun-kyo for the famous photo and another inside the ruins, if you can spare both.</p>

    <h2 id="visit">Visiting Takeda Castle Ruins<span class="h2-jp">アクセス</span></h2>
    <ul class="practical-list"><li><strong>Admission:</strong> 500 yen for adults; junior high and younger free (japan-guide, GLTJP, thegate12). Cash only (GLTJP, thegate12).</li><li><strong>Hours (sources differ, please confirm officially):</strong> japan-guide gives March to May 8:00 to 18:00, June to mid-September 6:00 to 18:00, mid-September to early December 5:00 to 17:00, and early December to 3 January 10:00 to 15:00. GLTJP gives 8:00 to 17:00 in March to May, 5:00 to 17:00 from June to 6 December, and 10:00 to 15:00 from 7 December to 3 January. thegate12 gives different closing times and says 4:00 opening from September. Last entry is 30 minutes before closing.</li><li><strong>Closed:</strong> 4 January through the end of February (all three sources). thegate12 writes &ldquo;lat February,&rdquo; which looks like a typo, so please confirm the reopening date.</li><li><strong>On foot from JR Takeda Station:</strong> about 40 minutes up a steep trail (japan-guide, GLTJP), 30 minutes in thegate12. It can be slippery after rain.</li><li><strong>Tenku Bus:</strong> from Takeda Station to the Takedajo-seki stop in about 20 minutes, 300 yen one way or 500 yen for a day pass, roughly one per hour, not in winter; then about 20 minutes on foot to the entrance (japan-guide).</li><li><strong>Taxi:</strong> about 15 minutes and 2,000 yen to the trailhead, then about 20 minutes on foot (japan-guide).</li><li><strong>Ritsuun-kyo:</strong> no public transport; about 10 minutes by car or 45 minutes on foot from the town center. The free Yamajiro no Sato parking lot is halfway up, and the bus from there to the trailhead is 200 yen one way (japan-guide).</li><li><strong>Facilities:</strong> restrooms only at the admission booth; no smoking on the trails or in the ruins (GLTJP).</li><li><strong>Address and phone:</strong> 169 Wadayama-cho Takeda, Asago-shi, Hyogo; 079-672-4003 (thegate12). Volunteer guides in Japanese are listed at 2,000 to 3,000 yen (thegate12, single source).</li></ul>

    <h2 id="stay">Making It a Trip<span class="h2-jp">滞在</span></h2>
    <p>The cloud season rewards staying in or near Asago the night before, because the best light is before 7 a.m. If you like the idea of ruins that are mostly stone, our <a href="/guides/bitchu-matsuyama-castle/" class="inline-link" onclick="trackEvent('click','internal','guide_takeda_to_bitchu')">Bitchu Matsuyama Castle guide</a> covers the other famous castle that floats above clouds, and our <a href="/guides/hagi-castle/" class="inline-link" onclick="trackEvent('click','internal','guide_takeda_to_hagi')">Hagi Castle ruins guide</a> covers a castle site that its own lords tore down.</p>
    <div class="key-callout">
      <p>&#127890; <strong>Plan your trip:</strong> Browse guided tours, or plan a stay near Asago. <a href="https://www.viator.com/search/Asago?pid=P00298374&amp;mcid=42383&amp;medium=link&amp;campaign=sacred-japan" target="_blank" rel="noopener sponsored" onclick="trackEvent('click','affiliate','viator_takeda_local')">Browse Asago tours &rarr;</a></p>
    </div>

    <h2 id="faq">Frequently Asked Questions<span class="h2-jp">よくあるご質問</span></h2>
    <div class="faq-stack">
'''+''.join(f'''    <details class="faq-item">
        <summary>{q}</summary>
        <div class="faq-answer">{a}</div>
    </details>
''' for q,a in faqs)+'''    </div>

    <h2 id="final">A Castle in the Sky<span class="h2-jp">むすびに</span></h2>
    <p>Takeda Castle is worth the early alarm. Plan for a morning rather than an afternoon, check the dates before you commit to winter, and let the stone do the talking.</p>

    <div class="closing-block">
      <span class="torii">&#9961;&#65039;</span>
      <p>The buildings are gone. The walls are still holding up the sky.</p>
    </div>

    <!-- RELATED GUIDES -->
    <section class="related-section">
      <h2>Related Guides</h2>
      <span class="h2-jp">関連ガイド</span>

      <div class="related-grid">

        <a class="related-card" href="/guides/bitchu-matsuyama-castle/" onclick="trackEvent('click','internal','related_takeda_to_bitchu')">
          <div class="related-card-label">SACRED JAPAN ／ GUIDES</div>
          <div class="related-card-title">&#127983; Bitchu Matsuyama Castle Guide &rarr;</div>
          <div class="related-card-desc">The mountain castle above the clouds.</div>
        </a>

        <a class="related-card" href="/guides/hagi-castle/" onclick="trackEvent('click','internal','related_takeda_to_hagi')">
          <div class="related-card-label">SACRED JAPAN ／ GUIDES</div>
          <div class="related-card-title">&#127983; Hagi Castle Ruins Guide &rarr;</div>
          <div class="related-card-desc">A castle its own lords tore down.</div>
        </a>

        <a class="related-card" href="/castles/" onclick="trackEvent('click','internal','related_takeda_to_castles')">
          <div class="related-card-label">SACRED JAPAN ／ CASTLES</div>
          <div class="related-card-title">&#127983; Japan's Castles &rarr;</div>
          <div class="related-card-desc">Every castle guide, with photos and official links.</div>
        </a>

      </div>
    </section>

  </article>

'''
tail=tail.replace('kochi-castle',SL).replace('_kochi_','_takeda_').replace('DKochi','DAsago').replace('search/Kochi','search/Asago')
def L(u,l,t): return f'<a href="{u}" target="_blank" rel="noopener" style="color:var(--beni);text-decoration:underline;" onclick="trackEvent(\'click\',\'external\',\'{l}\')">{t}</a>'
src='Sources verified at time of writing: '+', '.join([
 L('https://japan-guide.com/e/e3592.html','src_takeda_jg','japan-guide'),
 L('https://www.gltjp.com/en/directory/item/19012/','src_takeda_gltjp','GLTJP'),
 L('https://thegate12.com/spot/572','src_takeda_gate12','thegate12'),
])+'. Hours, prices and availability change'
tail,n=re.subn(r'Sources verified at time of writing:.*?Hours, prices and availability change',lambda m:src,tail,flags=re.S); assert n==1
out=head+main+tail
assert not re.search('Kochi|Shikoku|kochi|Kanazawa|Shuri|Naha',re.sub(r'"mainEntity": \[.*','',out,flags=re.S)),re.findall('.{30}(?:Kochi|Kanazawa|Shuri|Naha).{20}',out)
os.makedirs(R+f'guides/{SL}',exist_ok=True); open(R+f'guides/{SL}/index.html','w',encoding='utf-8').write(out)
for tg in ['div','figure','picture','p','a','ul','li','details','section','h2']:
    assert len(re.findall(f'<{tg}[ >]',out))==len(re.findall(f'</{tg}>',out)),tg
for m in re.findall(r'<script type="application/ld\+json">(.*?)</script>',out,re.S): json.loads(m)
im=Image.open(R+'images/og/og-guides-matsue-castle.jpg').convert('RGB'); d=ImageDraw.Draw(im)
d.rectangle([40,150,1170,380],fill=(252,240,242))
f1=ImageFont.truetype(glob.glob('/usr/share/fonts/**/DejaVuSerif-Bold.ttf',recursive=True)[0],48)
f2=ImageFont.truetype(glob.glob('/usr/share/fonts/**/NotoSerifCJK-Bold.ttc',recursive=True)[0],28,index=0)
l1="Takeda Castle Ruins Guide:"; l2="Japan's Machu Picchu"; print(d.textlength(l2,font=f1),d.textlength(l1,font=f1)); assert d.textlength(l2,font=f1)<1090 and d.textlength(l1,font=f1)<1090
d.text((66,170),l1,font=f1,fill=(26,15,15)); d.text((66,238),l2,font=f1,fill=(26,15,15)); d.text((66,332),"竹田城跡",font=f2,fill=(138,125,120))
im.save(R+f'images/og/og-guides-{SL}.jpg',quality=88); print('built',len(out))
