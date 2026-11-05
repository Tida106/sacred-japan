import re,json,os,glob
from PIL import Image,ImageDraw,ImageFont
R='/home/claude/sacred-japan/'; SL='takato-castle-ruins'
s=open(R+'guides/kochi-castle/index.html',encoding='utf-8').read()
i=s.index('<main>'); j=s.index('</main>'); head,tail=s[:i],s[j:]
TITLE="Takato Castle Ruins Guide: 1,500 Kohigan Cherry Trees, a Lost Castle and the Peak-Season Fee"
DESC="A licensed guide's guide to Takato Castle Ruins Park in Ina, Nagano: the lost Takeda-era castle, about 1,500 Takato Kohigan cherry trees, the park&rsquo;s sights, the peak-season fee and how to get there."
TAG='A lost castle, 1,500 Kohigan cherry trees and a peak-season fee, in Ina, Nagano.'
head=re.sub(r'<title>.*?</title>',f'<title>{TITLE} | Sacred Japan</title>',head,count=1)
head=re.sub(r'(<meta (?:name="description"|property="og:description"|name="twitter:description") content=")[^"]*(")',lambda m:m.group(1)+DESC+m.group(2),head)
head=re.sub(r'(<meta (?:property="og:title"|name="twitter:title") content=")[^"]*(")',lambda m:m.group(1)+TITLE+m.group(2),head)
head=re.sub(r'("headline": ")[^"]*(")',lambda m:m.group(1)+TITLE+m.group(2),head)
head=re.sub(r'("description": ")A licensed[^"]*(")',lambda m:m.group(1)+DESC+m.group(2),head)
head=re.sub(r'("date(?:Published|Modified)": ")[^"]*(")',lambda m:m.group(1)+'2026-11-05'+m.group(2),head)
head=re.sub(r'<meta name="keywords" content="[^"]*">','<meta name="keywords" content="Takato Castle Ruins, Takato Castle Park, Takato Kohigan cherry, Takato cherry blossoms, Ina Nagano sakura, Japan three great cherry blossom spots, Takato castle, Japan castles">',head)
head=head.replace('guides/kochi-castle','guides/takato-castle-ruins').replace('guide_kochi_','guide_takato_castle_ruins_').replace('og-guides-kochi-castle','og-guides-takato-castle-ruins')
head=head.replace('高知城','高遠城址').replace('Kochi Castle','Takato Castle Ruins')
head=re.sub(r"<h1>.*?</h1>","<h1><em>Takato Castle Ruins</em>: 1,500 Kohigan Cherry Trees, a Lost Castle and the Peak-Season Fee</h1>",head,count=1,flags=re.S)
head=head.replace("Shikoku's original keep, and the only castle where the lord's palace still stands beside it.",TAG)
faqs=[
("Is there a castle at Takato Castle Ruins Park?","No. The castle buildings were all demolished in 1871 under the Meiji government&rsquo;s decree abolishing castles (Nippon.com, GLTJP). What remains is the layout: Nippon.com lists the Ote Gate, the Shintokukan, the moat and earthen ramparts as the main sights. The park is mainly known for its cherry trees."),
("What are the cherry trees?","About 1,500 Takato Kohigan cherry trees (GLTJP, japan-guide, Nippon.com). GLTJP and go-nagano describe a native variety that is slightly smaller than Somei Yoshino and has deeper pink to red flowers. Some trees are over 140 years old (GLTJP); Nippon.com says 30 of them are over 130 years old."),
("When is the best time to go?","Early to mid-April (japan-guide, go-nagano, GLTJP). It changes each year, so check the bloom forecast. japan-guide gives 4 to 13 April 2026 as the peak period for its bus route, as an example."),
("How much does it cost?","Admission is charged only during the cherry season. GLTJP, go-nagano and japan-guide say 600 yen for adults, and GLTJP and go-nagano say 300 yen for children. Nippon.com and The Gate say 500 yen, which looks older. japan-guide also mentions 1,000 yen on peak-season weekends, which I found in one source only. go-nagano says the park is free until the day after the official bloom announcement and again once the blossoms have fallen. Please check the festival site for the current rate."),
("How do I get there without a car?","japan-guide says to take the JR Iida Line to Inashi Station and then a JR bus to Takato Bus Station, about 20 minutes and 590 yen, then walk about 15 minutes to the park. GLTJP says 20 minutes on foot from the bus stop. During peak season a temporary JR bus also runs from Chino Station (50 minutes, 1,490 yen, japan-guide), and a 300-yen loop bus connects the town, the car parks and the park (japan-guide, go-nagano). Check each year&rsquo;s timetable, as the temporary bus runs only during the peak."),
("Should I drive?","go-nagano says driving is generally more convenient and lists about 3,000 parking spaces, but that paid lots near the park fill quickly on peak weekends and visitors are often directed to free lots in town. japan-guide warns that roads become very congested and advises avoiding weekends and arriving early."),
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
      <li><a href="#opening">A Lost Castle with Cherry Trees</a></li>
      <li><a href="#history">A Suwa Castle, Takeda&rsquo;s Renovation and 1871</a></li>
      <li><a href="#trees">How the Cherry Trees Came</a></li>
      <li><a href="#see">What You Can See Today</a></li>
      <li><a href="#visit">Visiting Takato Castle Ruins Park</a></li>
      <li><a href="#stay">Making It a Trip</a></li>
      <li><a href="#faq">Frequently Asked Questions</a></li>
      <li><a href="#final">Before You Go Under the Trees</a></li>
    </ol>
  </aside>

  <article>

    <section id="opening">
      <p class="opening">As a licensed guide, I send visitors to Takato in April for one reason: the cherry trees. The castle is gone, taken down in 1871, but the Takato Kohigan trees that were planted on its grounds a few years later made the site one of the most famous blossom spots in Japan. They are smaller and pinker than the usual Somei Yoshino, and under them the moat and ramparts of a Takeda-era castle make a very good setting.</p>
      <p>This guide covers the castle&rsquo;s history, the trees, what to see in the park, and how to deal with the crowds and the peak-season fee. Where my sources disagree I say so, and I mark claims I found in only one place.</p>
    </section>

    <h2 id="history">A Suwa Castle, Takeda&rsquo;s Renovation and 1871<span class="h2-jp">高遠城の歴史</span></h2>
    <p>According to Nippon.com, the Takato clan, a branch of the Suwa family, ruled the area from around the 14th century and is believed to have used this castle as its base. In 1547 Takeda Shingen took the castle and had his strategist Yamamoto Kansuke renovate and enlarge it; an area called the Kansuke-kuruwa still carries his name (Nippon.com, one source only).</p>
    <p>After the Tokugawa shogunate began, the lords included the Hoshina, Torii and Naito families (Nippon.com, no dates given). In 1871 the Meiji government&rsquo;s decree abolishing castles led to the demolition of every building inside it (Nippon.com, GLTJP). What survives is mostly earthwork: Nippon.com lists the Ote Gate, the Shintokukan, the moat and the earthen ramparts, and japan-guide says little of the original castle remains beyond some stone foundations.</p>

    <h2 id="trees">How the Cherry Trees Came<span class="h2-jp">桜の由来</span></h2>
    <p>GLTJP and Nippon.com say that former retainers of the Takato domain, saddened by the ruined castle, transplanted cherry trees here. go-nagano gives a date and a source: the trees were planted in 1875 by former samurai, who moved saplings from the cherry avenue at the old &ldquo;Sakura no Baba&rdquo; (now the site of Takato Elementary School), and 2025 marked 150 years since. japan-guide also dates the park&rsquo;s opening to 1875.</p>
    <p>The variety is the Takato Kohigan. GLTJP and go-nagano describe it as native to Takato, slightly smaller than Somei Yoshino and tinged with red. About 1,500 trees grow in the park (GLTJP, japan-guide, Nippon.com, go-nagano). GLTJP says some are over 140 years old, whereas Nippon.com says 30 of them are over 130 years old, so I would say simply &ldquo;well over a century.&rdquo; japan-guide and GLTJP call the park one of Japan&rsquo;s three great cherry blossom sites with Hirosaki and Yoshinoyama, but that ranking is a common label and not an official one.</p>
    <p>go-nagano says that about 150,000 visitors come in a season, so please be ready for crowds.</p>

    <h2 id="see">What You Can See in the Park<span class="h2-jp">見どころ</span></h2>
    <p>The <strong>Ounkyo bridge</strong> (go-nagano spells it Ouunbashi) is a gently curved bridge in the middle of the park and, according to japan-guide, one of the best blossom-viewing spots. The <strong>drum tower</strong> (taikoyagura) stands on the west side and, says japan-guide, has views of the town and the Central Alps; go-nagano says it was moved here in 1877.</p>
    <p><strong>Takatokaku</strong> is a two-storey building near the north gate, built in the 1930s in a mixed local and Western style (japan-guide). go-nagano gives 1936 and says it is a registered tangible cultural property. At the south end the <strong>Shinshu Takato Art Museum</strong> shows temporary exhibitions (japan-guide). go-nagano also lists the Toimon gate, a wholesale-store gate moved from the castle town, as one of the park&rsquo;s historic features, and mentions a small pond on the east moat that is popular for photos.</p>
    <p>In autumn, about 250 maple trees colour the park (GLTJP). The Gate says there is an evening light-up and projection mapping show for both the cherry blossoms and the maples, but I found that in one source only, so please check before you plan a trip around it.</p>

    <h2 id="visit">Visiting Takato Castle Ruins Park<span class="h2-jp">アクセス</span></h2>
    <ul class="practical-list"><li><strong>Admission:</strong> charged only in the cherry season. 600 yen for adults and 300 yen for children (GLTJP, go-nagano; japan-guide also gives 600 yen). Nippon.com and The Gate say 500 yen, which looks older. japan-guide mentions 1,000 yen on peak weekends (one source only). go-nagano says it becomes paid from the day after the official bloom announcement until the blossoms have fallen. Credit cards are not accepted (GLTJP).</li><li><strong>Hours:</strong> 8:00 to 17:00 in the cherry season; during the peak period the illumination runs until 21:00 (japan-guide) or 22:00, with last entry at 21:00 (go-nagano). Outside the season the park is open all day and free (GLTJP, japan-guide).</li><li><strong>By public transport:</strong> JR Iida Line to Inashi Station, then a JR bus to Takato Bus Station in about 20 minutes (590 yen), then a walk of 15 minutes (japan-guide) to 20 minutes (GLTJP). A temporary peak-season bus from Chino Station takes about 50 minutes (1,490 yen, japan-guide) and runs only in the peak days.</li><li><strong>Loop bus:</strong> 300 yen, about every 30 minutes, between the town, the car parks and the park (japan-guide, go-nagano).</li><li><strong>By car:</strong> about 3,000 spaces, but the roads become very congested at peak and paid lots fill early (japan-guide, go-nagano).</li><li><strong>Facilities:</strong> toilets and free Wi-Fi, but no coin lockers, and smoking is not allowed (GLTJP).</li><li><strong>Time needed:</strong> my own estimate is 1 to 2 hours on a quiet day, more at the peak.</li></ul>

    <h2 id="stay">Making It a Trip<span class="h2-jp">滞在</span></h2>
    <p>Takato is about 60 km south of Matsumoto (japan-guide), so it combines well with our <a href="/guides/matsumoto-castle/" '''+IL+''' onclick="trackEvent('click','internal','guide_takato_castle_ruins_to_matsumoto')">Matsumoto Castle guide</a>. For the other great cherry blossom castle, see our <a href="/guides/hirosaki-castle/" '''+IL+''' onclick="trackEvent('click','internal','guide_takato_castle_ruins_to_hirosaki')">Hirosaki Castle guide</a>.</p>
    <p><strong>Beating the crowds:</strong> japan-guide advises avoiding weekends and arriving early. go-nagano adds that picnic sheets and food are allowed again since 2023, and that food stalls operate in and around the park.</p>
    <div class="key-callout">
      <p>&#127890; <strong>Plan your trip:</strong> Browse guided tours or plan a stay around Nagano. <a href="https://www.viator.com/search/Nagano?pid=P00298374&amp;mcid=42383&amp;medium=link&amp;campaign=sacred-japan" target="_blank" rel="noopener sponsored" onclick="trackEvent('click','affiliate','viator_takato_castle_ruins_local')">Browse Nagano tours &rarr;</a></p>
    </div>

    <h2 id="faq">Frequently Asked Questions<span class="h2-jp">よくあるご質問</span></h2>
    <div class="faq-stack">
'''+''.join(f'''    <details class="faq-item">
        <summary>{q}</summary>
        <div class="faq-answer">{a}</div>
    </details>
''' for q,a in faqs)+'''    </div>

    <h2 id="final">Before You Go Under the Trees<span class="h2-jp">むすびに</span></h2>
    <p>Go for the blossom, early on a weekday if you can, and treat the ruins as the setting. Cross the Ounkyo bridge, look back at the moat, and remember that every tree here was planted by people who missed their castle.</p>

    <div class="closing-block">
      <span class="torii">&#9961;&#65039;</span>
      <p>A castle that vanished, and 1,500 trees planted in its place.</p>
    </div>

    <!-- RELATED GUIDES -->
    <section class="related-section">
      <h2>Related Guides</h2>
      <span class="h2-jp">関連ガイド</span>

      <div class="related-grid">

        <a class="related-card" href="/guides/matsumoto-castle/" onclick="trackEvent('click','internal','related_takato_castle_ruins_to_matsumoto')">
          <div class="related-card-label">SACRED JAPAN ／ GUIDES</div>
          <div class="related-card-title">&#127983; Matsumoto Castle Guide &rarr;</div>
          <div class="related-card-desc">The black keep and the Alps.</div>
        </a>

        <a class="related-card" href="/guides/hirosaki-castle/" onclick="trackEvent('click','internal','related_takato_castle_ruins_to_hirosaki')">
          <div class="related-card-label">SACRED JAPAN ／ GUIDES</div>
          <div class="related-card-title">&#127983; Hirosaki Castle Guide &rarr;</div>
          <div class="related-card-desc">Tohoku&rsquo;s original keep and its cherry trees.</div>
        </a>

        <a class="related-card" href="/castles/" onclick="trackEvent('click','internal','related_takato_castle_ruins_to_castles')">
          <div class="related-card-label">SACRED JAPAN ／ CASTLES</div>
          <div class="related-card-title">&#127983; Japan's Castles &rarr;</div>
          <div class="related-card-desc">Every castle guide, with photos and official links.</div>
        </a>

      </div>
    </section>

  </article>

'''
tail=tail.replace('kochi-castle',SL).replace('_kochi_','_sendai_castle_').replace('DKochi','DIna').replace('search/Kochi','search/Nagano')
def L(u,l,t): return f'<a href="{u}" target="_blank" rel="noopener" style="color:var(--beni);text-decoration:underline;" onclick="trackEvent(\'click\',\'external\',\'{l}\')">{t}</a>'
src='Sources verified at time of writing: '+', '.join([
 L('https://www.japan-guide.com/e/e6065.html','src_takato_jg','japan-guide'),
 L('https://www.gltjp.com/en/directory/item/15486','src_takato_gltjp','GLTJP'),
 L('https://www.nippon.com/ja/guide-to-japan/castle00116030/','src_takato_nippon','Nippon.com'),
 L('https://www.go-nagano.net/nature-and-outdoors/id22186','src_takato_gn','go-nagano'),
 L('https://thegate12.com/spot/366','src_takato_gate','The Gate'),
])+'. Hours, prices and availability change'
tail,n=re.subn(r'Sources verified at time of writing:.*?Hours, prices and availability change',lambda m:src,tail,flags=re.S); assert n==1
out=head+main+tail
assert not re.search('Kochi|Shikoku|kochi|Kanazawa|Shuri|Naha|Takeda Castle|Asago|Machu|Goryokaku Tower|Republic of Ezo|Sendai|Masamune|Wakayama|Kishu',re.sub(r'"mainEntity": \[.*','',out,flags=re.S)),re.findall('.{30}(?:Kochi|Kanazawa|Shuri|Naha|Asago|Machu).{20}',out)
os.makedirs(R+f'guides/{SL}',exist_ok=True); open(R+f'guides/{SL}/index.html','w',encoding='utf-8').write(out)
for tg in ['div','figure','picture','p','a','ul','li','details','section','h2']:
    assert len(re.findall(f'<{tg}[ >]',out))==len(re.findall(f'</{tg}>',out)),tg
for m in re.findall(r'<script type="application/ld\+json">(.*?)</script>',out,re.S): json.loads(m)
im=Image.open(R+'images/og/og-guides-matsue-castle.jpg').convert('RGB'); d=ImageDraw.Draw(im)
d.rectangle([40,150,1170,380],fill=(252,240,242)); d.rectangle([1118,66,1160,96],fill=(252,240,242))
f1=ImageFont.truetype(glob.glob('/usr/share/fonts/**/DejaVuSerif-Bold.ttf',recursive=True)[0],48)
f2=ImageFont.truetype(glob.glob('/usr/share/fonts/**/NotoSerifCJK-Bold.ttc',recursive=True)[0],28,index=0)
l1="Takato Castle Ruins Guide:"; l2="1,500 Cherry Trees, No Castle"; print(d.textlength(l2,font=f1),d.textlength(l1,font=f1)); assert d.textlength(l2,font=f1)<1090
d.text((66,170),l1,font=f1,fill=(26,15,15)); d.text((66,238),l2,font=f1,fill=(26,15,15)); d.text((66,332),"高遠城址",font=f2,fill=(138,125,120))
im.save(R+f'images/og/og-guides-{SL}.jpg',quality=88); print('built',len(out))
