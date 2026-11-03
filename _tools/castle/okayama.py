import re,json,os,glob
from PIL import Image,ImageDraw,ImageFont
R='/home/claude/sacred-japan/'; SL='okayama-castle'
s=open(R+'guides/kochi-castle/index.html',encoding='utf-8').read()
i=s.index('<main>'); j=s.index('</main>'); head,tail=s[:i],s[j:]
TITLE="Okayama Castle Guide: The Black Crow Castle, a 1966 Rebuild and Korakuen Next Door"
DESC="A licensed guide's guide to Okayama Castle: why the keep is black, what the 1945 fire destroyed, the two original turrets, the 1966 rebuild and how to combine it with Korakuen."
head=re.sub(r'<title>.*?</title>',f'<title>{TITLE} | Sacred Japan</title>',head,count=1)
head=re.sub(r'(<meta (?:name="description"|property="og:description"|name="twitter:description") content=")[^"]*(")',lambda m:m.group(1)+DESC+m.group(2),head)
head=re.sub(r'(<meta (?:property="og:title"|name="twitter:title") content=")[^"]*(")',lambda m:m.group(1)+TITLE+m.group(2),head)
head=re.sub(r'("headline": ")[^"]*(")',lambda m:m.group(1)+TITLE+m.group(2),head)
head=re.sub(r'("description": ")A licensed[^"]*(")',lambda m:m.group(1)+DESC+m.group(2),head)
head=re.sub(r'<meta name="keywords" content="[^"]*">','<meta name="keywords" content="Okayama Castle, Okayama Castle guide, Crow Castle, Ujo, Okayama Castle admission, Okayama Castle hours, Korakuen and Okayama Castle, black castle Japan, Okayama Castle history">',head)
head=head.replace('guides/kochi-castle','guides/okayama-castle').replace('guide_kochi_','guide_okayama_').replace('og-guides-kochi-castle','og-guides-okayama-castle')
head=head.replace('高知城','岡山城').replace('Kochi Castle','Okayama Castle')
head=re.sub(r"<h1>.*?</h1>","<h1><em>Okayama Castle</em>: The Black Crow Castle, a 1966 Rebuild and Korakuen Next Door</h1>",head,count=1,flags=re.S)
head=head.replace("Shikoku's original keep, and the only castle where the lord's palace still stands beside it.","Japan's black castle, a 1966 rebuild of the keep, two original turrets and Korakuen next door.")
faqs=[
("Is Okayama Castle original?","No. GLTJP and Wikipedia agree that the main keep burned in the air raids of 1945, and Wikipedia gives the date as 29 June 1945. The keep you see now is a concrete replica, rebuilt between 1964 and 1966. Two turrets survived and are Important Cultural Properties, so the original is not entirely gone."),
("Why is Okayama Castle black?","GLTJP describes a jet-black exterior with black lacquered siding boards, which earned it the nickname Crow Castle, or Ujo. Wikipedia contrasts it with the white Himeji Castle. The same sources mention gold on the roof, and they differ a little on how much, so I would call the gilding a detail to look for rather than a promise."),
("How much does it cost, and when is it open?","GLTJP gives 500 yen for adults, free for under 14, from 9:00 to 17:30 with last entry at 17:00, and closed from 29 to 31 December. Jeepe says elementary and junior high students enter free, so the age line differs by source. Jeepe also lists a combined ticket with Korakuen for 800 yen. Confirm all of it on the official site, because hours can be extended for events."),
("Can I visit Korakuen on the same day?","Yes. Jeepe describes Korakuen and the castle as neighbors joined by the Tsukimi Bridge. It gives Korakuen as 500 yen for adults and 200 yen for ages 65 and over, with hours of about 7:30 to 18:00 from 20 March to 30 September and 8:00 to 17:00 from 1 October to 19 March, and entry closing 15 minutes earlier. Check the official page for current hours."),
("How do I get there from Okayama Station?","GLTJP says to take the Higashiyama Line of the Okayama Electric Tramway to Shiroshita Station, then walk about 10 minutes, for about 15 minutes in all. Jeepe gives about 4 minutes on the tram, and also mentions a bus from the east exit that takes 10 to 12 minutes. Walking the whole way is possible but takes longer."),
("How long should I allow?","None of my sources gives a figure. My own estimate is about an hour for the keep museum and the two turrets, and a half day if you add Korakuen. The keep is a museum rather than a climb through original rooms, so it is a short visit."),
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
      <li><a href="#opening">The Black Castle Beside the Garden</a></li>
      <li><a href="#history">From the Nawa Clan to the Ikeda</a></li>
      <li><a href="#black">Why It Is Called the Crow</a></li>
      <li><a href="#fire">The 1945 Fire and the 1966 Rebuild</a></li>
      <li><a href="#survives">What Is Original</a></li>
      <li><a href="#visit">Visiting Okayama Castle</a></li>
      <li><a href="#stay">Making It a Trip</a></li>
      <li><a href="#faq">Frequently Asked Questions</a></li>
      <li><a href="#final">A Rebuilt Keep, an Honest Visit</a></li>
    </ol>
  </aside>

  <article>

    <section id="opening">
      <p class="opening">As a licensed guide, I send people to Okayama Castle for one reason: it is black. Most castles in Japan are white, and Himeji, the one everyone knows, is the whitest of all. Okayama's keep is dark, with black boards and gold on the roof, and the locals call it the Crow Castle. It is also a rebuild, which I say first, because that changes what you should expect inside.</p>
      <p>This guide covers who built it, why it is black, what the 1945 fire took, what is still original, and the practical details, including Korakuen next door. Where my sources disagree, I say so.</p>
    </section>

    <h2 id="history">From the Nawa Clan to the Ikeda<span class="h2-jp">築城</span></h2>
    <p>Wikipedia says the Nawa clan built the first castle here between 1346 and 1369. In 1570, it says, Ukita Naoie killed the castle lord Kanemitsu Munetaka and began remodeling. Naoie's son, Ukita Hideie, completed the main keep in 1597. GLTJP says the work took about eight years and was guided by Toyotomi Hideyoshi.</p>
    <p>Hideie sided with the Toyotomi at Sekigahara in 1600, was captured by the Tokugawa and was exiled to Hachijo. Wikipedia says the castle then went to Kobayakawa Hideaki, who died two years later without an heir, and then to the Ikeda clan, who held it from 1602 to 1869. GLTJP adds that the lords after Hideie expanded the castle town, which grew into today's Okayama City, and Wikipedia says the Ikeda added Korakuen as a private garden.</p>
    <p>After the shogunate fell, the castle passed in 1869 to the Ministry of War. Wikipedia says the outer moats were filled in between 1873 and 1882 and most buildings were dismantled, so the castle's walls gradually disappeared under the city.</p>

    <h2 id="black">Why It Is Called the Crow<span class="h2-jp">烏城</span></h2>
    <p>GLTJP describes a jet-black exterior with black lacquered siding boards, and says that is why the castle is called Ujo, the Crow Castle. Wikipedia sets it against the white Himeji Castle. The two sources then differ on the gold. GLTJP mentions gold-leaf roof tiles and a second nickname, Kin-ujo, or Golden Crow Castle. Wikipedia says the keep had gilded roof tiles before Sekigahara and that today only parts of the roof, including the shachihoko, are gilded, and that the rooftop ornaments were gilded in 1996 for the 400th anniversary.</p>
    <p>I would not promise a golden roof, then. What you can count on is the contrast: a dark keep with bright ornaments at the roof line, which looks sharpest against a clear sky.</p>

    <h2 id="fire">The 1945 Fire and the 1966 Rebuild<span class="h2-jp">再建</span></h2>
    <p>GLTJP says the keep was designated a National Treasure before the air raids of 1945 burned it down. Wikipedia gives the date as 29 June 1945 and says the raid also destroyed an adjacent gate, leaving two turrets and some stone walls. Reconstruction of the keep and gate began in 1964 and finished in 1966, and Wikipedia calls the keep a concrete replica.</p>
    <p>GLTJP says the rebuilt keep now serves as a museum of Okayama's history from the Sengoku through the Edo period. Both GLTJP and Jeepe mention extras inside, such as projection mapping, a kimono dressing experience and the Ujo Cafe, though they add that exhibits and events change by season.</p>

    <h2 id="survives">What Is Original<span class="h2-jp">現存する遺構</span></h2>
    <p>Two turrets survived the war. Wikipedia says the Agency for Cultural Affairs lists both as Important Cultural Properties. GLTJP names them as Tsukimi Yagura and Nishite Yagura. It dates Tsukimi Yagura to the Edo period, says it is the only turret still standing on the Honmaru site, and says it looks like two stories from outside but has three. It puts Nishite Yagura at around 1603 to 1615.</p>
    <p>If you want the original wood and stone rather than a museum, these two and the surviving walls are where to spend your time.</p>

    <h2 id="visit">Visiting Okayama Castle<span class="h2-jp">アクセス</span></h2>
    <ul class="practical-list"><li><strong>Admission:</strong> About 500 yen for adults. GLTJP says under 14 is free, and Jeepe says elementary and junior high students are free. A combined ticket with Korakuen is listed at 800 yen (Jeepe). Please confirm on the official site.</li><li><strong>Hours:</strong> 9:00 to 17:30, last entry 17:00. Hours may be extended during events (GLTJP).</li><li><strong>Closed:</strong> 29 to 31 December (GLTJP).</li><li><strong>Getting there:</strong> Okayama Electric Tramway, Higashiyama Line, to Shiroshita Station, then about 10 minutes on foot, or about 15 minutes in all (GLTJP). Jeepe also mentions a bus from the east exit, about 10 to 12 minutes.</li><li><strong>Stamp:</strong> A stamp for the 100 Famous Castles is available in the paid area, according to GLTJP, which says this comes from a visitor review, so confirm it.</li><li><strong>Korakuen:</strong> Joined to the castle by the Tsukimi Bridge (Jeepe). Adults are about 500 yen, and hours change in October and March (Jeepe).</li></ul>

    <h2 id="stay">Making It a Trip<span class="h2-jp">滞在</span></h2>
    <p>GLTJP says illuminations called Ujo Togenkyo run in spring, summer and autumn, and that Korakuen holds its own illumination, Genso Teien, in the same seasons. Themes change by year, so check the dates before you plan an evening. For a white castle to compare, see our <a href="/guides/himeji-castle/" class="inline-link" onclick="trackEvent('click','internal','guide_okayama_to_himeji')">Himeji Castle guide</a>, and for a mountain castle in the same prefecture, our <a href="/guides/bitchu-matsuyama-castle/" class="inline-link" onclick="trackEvent('click','internal','guide_okayama_to_bitchu')">Bitchu Matsuyama Castle guide</a>.</p>
    <div class="key-callout">
      <p>&#127890; <strong>Plan your trip:</strong> Browse guided tours, or plan a stay in Okayama. <a href="https://www.viator.com/search/Okayama?pid=P00298374&amp;mcid=42383&amp;medium=link&amp;campaign=sacred-japan" target="_blank" rel="noopener sponsored" onclick="trackEvent('click','affiliate','viator_okayama_local')">Browse Okayama tours &rarr;</a></p>
    </div>

    <h2 id="faq">Frequently Asked Questions<span class="h2-jp">よくあるご質問</span></h2>
    <div class="faq-stack">
'''+''.join(f'''    <details class="faq-item">
        <summary>{q}</summary>
        <div class="faq-answer">{a}</div>
    </details>
''' for q,a in faqs)+'''    </div>

    <h2 id="final">A Rebuilt Keep, an Honest Visit<span class="h2-jp">むすびに</span></h2>
    <p>Okayama Castle is worth it for its color, its two surviving turrets and the garden next door, not for original rooms. Go knowing the keep is a 1966 replica, see the turrets for the real thing, and finish in Korakuen.</p>

    <div class="closing-block">
      <span class="torii">&#9961;&#65039;</span>
      <p>The crow was rebuilt. The color is still its own.</p>
    </div>

    <!-- RELATED GUIDES -->
    <section class="related-section">
      <h2>Related Guides</h2>
      <span class="h2-jp">関連ガイド</span>

      <div class="related-grid">

        <a class="related-card" href="/guides/himeji-castle/" onclick="trackEvent('click','internal','related_okayama_to_himeji')">
          <div class="related-card-label">SACRED JAPAN ／ GUIDES</div>
          <div class="related-card-title">&#127983; Himeji Castle Guide &rarr;</div>
          <div class="related-card-desc">The white castle, for comparison with the black one.</div>
        </a>

        <a class="related-card" href="/guides/bitchu-matsuyama-castle/" onclick="trackEvent('click','internal','related_okayama_to_bitchu')">
          <div class="related-card-label">SACRED JAPAN ／ GUIDES</div>
          <div class="related-card-title">&#127983; Bitchu Matsuyama Castle Guide &rarr;</div>
          <div class="related-card-desc">Japan's only surviving mountain-top keep, in the same prefecture.</div>
        </a>

        <a class="related-card" href="/castles/" onclick="trackEvent('click','internal','related_okayama_to_castles')">
          <div class="related-card-label">SACRED JAPAN ／ CASTLES</div>
          <div class="related-card-title">&#127983; Japan's Castles &rarr;</div>
          <div class="related-card-desc">Every castle guide, with photos and official links.</div>
        </a>

      </div>
    </section>

  </article>

'''
tail=tail.replace('kochi-castle',SL).replace('_kochi_','_okayama_')
def L(u,l,t): return f'<a href="{u}" target="_blank" rel="noopener" style="color:var(--beni);text-decoration:underline;" onclick="trackEvent(\'click\',\'external\',\'{l}\')">{t}</a>'
src='Sources verified at time of writing: '+', '.join([
 L('https://www.gltjp.com/en/article/item/20347/','src_okayama_gltjp','GLTJP'),
 L('https://en.wikipedia.org/wiki/Okayama_Castle','src_okayama_wikipedia','Wikipedia'),
 L('https://www.jeepe.jp/en/articles/okayama-day-trip-course-2261','src_okayama_jeepe','Jeepe'),
])+'. Hours, prices and availability change'
tail,n=re.subn(r'Sources verified at time of writing:.*?Hours, prices and availability change',lambda m:src,tail,flags=re.S); assert n==1
tail=tail.replace('destination%3DKochi','destination%3DOkayama').replace('search/Kochi','search/Okayama')
out=head+main+tail
assert not re.search('Kochi|Shikoku|kochi|Uwajima',re.sub(r'"mainEntity": \[.*','',out,flags=re.S))
os.makedirs(R+f'guides/{SL}',exist_ok=True); open(R+f'guides/{SL}/index.html','w',encoding='utf-8').write(out)
for tg in ['div','figure','picture','p','a','ul','li','details','section','h2']:
    assert len(re.findall(f'<{tg}[ >]',out))==len(re.findall(f'</{tg}>',out)),tg
for m in re.findall(r'<script type="application/ld\+json">(.*?)</script>',out,re.S): json.loads(m)
im=Image.open(R+'images/og/og-guides-matsue-castle.jpg').convert('RGB'); d=ImageDraw.Draw(im)
d.rectangle([40,150,1170,380],fill=(252,240,242))
f1=ImageFont.truetype(glob.glob('/usr/share/fonts/**/DejaVuSerif-Bold.ttf',recursive=True)[0],48)
f2=ImageFont.truetype(glob.glob('/usr/share/fonts/**/NotoSerifCJK-Bold.ttc',recursive=True)[0],28,index=0)
l2="The Black Crow Castle"; assert d.textlength(l2,font=f1)<1090
d.text((66,170),"Okayama Castle Guide:",font=f1,fill=(26,15,15)); d.text((66,238),l2,font=f1,fill=(26,15,15)); d.text((66,332),"岡山城",font=f2,fill=(138,125,120))
im.save(R+f'images/og/og-guides-{SL}.jpg',quality=88); print('built',len(out))
