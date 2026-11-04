import re,json,os,glob
from PIL import Image,ImageDraw,ImageFont
R='/home/claude/sacred-japan/'; SL='aizuwakamatsu-castle'
s=open(R+'guides/kochi-castle/index.html',encoding='utf-8').read()
i=s.index('<main>'); j=s.index('</main>'); head,tail=s[:i],s[j:]
TITLE='Aizuwakamatsu Castle Guide: The Red-Roofed Keep, the 1868 Siege and the Byakkotai'
DESC="A licensed guide's guide to Aizuwakamatsu (Tsuruga) Castle in Fukushima: the 1868 siege, the red-tiled keep rebuilt in 1965, the Rinkaku tea house, cherry blossoms, fees and the bus from the station."
TAG='A rebuilt keep with its historic red roof tiles, besieged for a month in 1868, a short bus ride from Aizuwakamatsu Station.'
head=re.sub(r'<title>.*?</title>',f'<title>{TITLE} | Sacred Japan</title>',head,count=1)
head=re.sub(r'(<meta (?:name="description"|property="og:description"|name="twitter:description") content=")[^"]*(")',lambda m:m.group(1)+DESC+m.group(2),head)
head=re.sub(r'(<meta (?:property="og:title"|name="twitter:title") content=")[^"]*(")',lambda m:m.group(1)+TITLE+m.group(2),head)
head=re.sub(r'("headline": ")[^"]*(")',lambda m:m.group(1)+TITLE+m.group(2),head)
head=re.sub(r'("description": ")A licensed[^"]*(")',lambda m:m.group(1)+DESC+m.group(2),head)
head=re.sub(r'("date(?:Published|Modified)": ")[^"]*(")',lambda m:m.group(1)+'2026-11-04'+m.group(2),head)
head=re.sub(r'<meta name="keywords" content="[^"]*">','<meta name="keywords" content="Aizuwakamatsu Castle, Tsuruga Castle, Tsurugajo, Aizu Wakamatsu, Fukushima castle, Byakkotai, red roof castle, Aizu Boshin War, Tsuruga Castle hours, Aizuwakamatsu cherry blossoms">',head)
head=head.replace('guides/kochi-castle','guides/aizuwakamatsu-castle').replace('guide_kochi_','guide_aizuwakamatsu_').replace('og-guides-kochi-castle','og-guides-aizuwakamatsu-castle')
head=head.replace('高知城','会津若松城').replace('Kochi Castle','Aizuwakamatsu Castle')
head=re.sub(r"<h1>.*?</h1>","<h1><em>Aizuwakamatsu Castle</em>: The Red-Roofed Keep, the 1868 Siege and the Byakkotai</h1>",head,count=1,flags=re.S)
head=head.replace("Shikoku's original keep, and the only castle where the lord's palace still stands beside it.",TAG)
faqs=[
("How much does it cost to enter Tsuruga Castle?","The keep is 410 yen for adults and 150 yen for elementary and junior high students (GLTJP, Nippon.com, mytabi, Fun Japan). A combined ticket with the Rinkaku tea house is 520 yen (GLTJP, Nippon.com). Rinkaku alone is listed as 210 yen plus 600 yen for tea and a sweet at Nippon.com, and 200 yen plus 500 yen at Fun Japan, so please confirm at the gate. GLTJP says credit cards are not accepted."),
("What are the opening hours?","8:30 to 17:00, with last entry at 16:30, open every day of the year (GLTJP, Nippon.com, mytabi, Fun Japan). Please check the official site before a winter visit."),
("How do I get there from Aizuwakamatsu Station?","By bus it is about 10 to 20 minutes depending on the route, followed by a walk of 5 to 10 minutes. GLTJP names the Haikara-san bus and the Tsurugajo Iriguchi stop; Fun Japan names the Aizu Loop Bus and the Tsurugajo Kitaguchi stop; the Edo Legacy page names the Hongo Loop Line and Sanno-cho. Walking from the station takes about 30 minutes (Fun Japan). Please check the current timetable."),
("Why is the roof red?","Nippon.com says red iron-glazed tiles were adopted in 1648 because ordinary tiles cracked in the freezing winters, and the Edo Legacy page also says the glaze resists frost. The 1965 reconstruction used black tiles, and the roof was changed back to red in 2011 (GLTJP, Nippon.com, Edo Legacy, Fun Japan)."),
("Is the keep original?","No. The castle was demolished in 1874 after the 1868 siege, leaving only the stone walls. The current keep is a reinforced-concrete reconstruction completed in 1965 (GLTJP, Nippon.com, Fun Japan). Nippon.com says it was funded by citizen donations."),
("Who were the Byakkotai?","GLTJP describes them as teenage boys, sons of Aizu clan soldiers, who fought in the Boshin War. Nippon.com says about 20 young samurai fled to Mount Iimori during the siege, saw the town burning, believed the castle had fallen and chose to die. You can see Mount Iimori from the keep (GLTJP)."),
("When are the cherry blossoms?","The park has about 1,000 cherry trees (GLTJP, Edo Legacy) and Fun Japan calls April the best time. GLTJP says the trees are lit during the season. I did not find a peak-bloom date in these sources, so please check a current bloom report."),
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
assert not re.search('Kochi|Shikoku|kochi|Kanazawa|Shuri|Naha|Takeda|Asago|Machu|Odawara|Hojo',hh),re.findall('.{30}(?:Kochi|Shikoku|Kanazawa|Shuri|Naha|Takeda|Asago|Machu).{20}',hh)
main='''<main>

  <!-- TABLE OF CONTENTS -->
  <aside class="toc" aria-label="Table of contents">
    <div class="toc-label">TABLE OF CONTENTS ／ 目次</div>
    <div class="toc-title">In This Guide</div>
    <ol>
      <li><a href="#opening">The Castle That Held Out</a></li>
      <li><a href="#history">From Ashina to Matsudaira</a></li>
      <li><a href="#siege">The 1868 Siege</a></li>
      <li><a href="#keep">The Red-Roofed Keep</a></li>
      <li><a href="#grounds">Rinkaku, Cherry Trees and the View of Iimori</a></li>
      <li><a href="#visit">Visiting Tsuruga Castle</a></li>
      <li><a href="#stay">Making It a Trip</a></li>
      <li><a href="#faq">Frequently Asked Questions</a></li>
      <li><a href="#final">Before You Leave the Park</a></li>
    </ol>
  </aside>

  <article>

    <section id="opening">
      <p class="opening">As a licensed guide, I tell visitors that Tsuruga Castle in Aizuwakamatsu is the castle where the samurai era ended in practice. In the autumn of 1868 the lords of Aizu stayed loyal to the shogunate, and the imperial forces came for them. The castle was bombarded for about a month and then surrendered. Today it is the only keep in Japan I know of with a red roof, and a short walk from the keep you can look across to the hill where a group of teenage boys ended their lives.</p>
      <p>This guide covers the history, the siege, what is inside the keep and the tea house, the cherry blossoms, and the practical details. Where my sources disagree, I say so, and I mark claims I found in only one place.</p>
    </section>

    <h2 id="history">From Ashina to Matsudaira<span class="h2-jp">蘆名氏から松平氏へ</span></h2>
    <p>The sources give different starting points. Fun Japan and the Fukushima tourism page say the first fortification was built in 1384 by Ashina Naomori, and that the place was then called Kurokawa Castle. Date Masamune took it in 1589. Fun Japan says Gamo Ujisato received it in 1592 and renamed it Tsuruga; the Fukushima page says Date was summoned by Hideyoshi the following year, which would be 1590, and GLTJP says only &ldquo;late 16th century.&rdquo; So please read the date of Gamo&rsquo;s arrival as roughly 1590 to 1592.</p>
    <p>GLTJP says Gamo built a full-scale castle with stone walls and a keep and renamed the town Wakamatsu, and that the name Tsuruga may come from his childhood name, Tsuruchiyo, although it notes there are several theories. The Edo Legacy page gives 1593 for the building and says the keep was said to have had seven stories, and that after a major earthquake in 1611 it was replaced by a five-story keep. I found that in only one source, so I treat it as a claim to check.</p>
    <p>In 1643 the castle passed to Hoshina Masayuki, who took the Matsudaira name; Nippon.com calls him a son of the shogun Tokugawa Hidetada, and says his descendants ruled until 1868. That family tie explains a lot about what happened next.</p>
    <p>One detail I like is the roof. Nippon.com says the keep originally had black walls and black tiles, and that red iron-glazed tiles were adopted in 1648 because the harsh winters made ordinary tiles crack. The Edo Legacy page also says the glaze resists freezing. I found the year 1648 only at Nippon.com.</p>

    <h2 id="siege">The 1868 Siege<span class="h2-jp">会津戦争</span></h2>
    <p>The Boshin War began in January 1868, and GLTJP says the fighting reached Aizu in August. Nippon.com says the ninth lord, Matsudaira Katamori, was loyal to the shogunate, and that imperial forces invaded the domain. About 5,000 samurai and their families took refuge in the castle (Nippon.com). GLTJP says the siege began on 22 August and the castle held out under bombardment for more than a month, earning a reputation as an &ldquo;impregnable great castle.&rdquo;</p>
    <p>As allies surrendered one by one, Katamori surrendered unconditionally to spare the people of the domain (Nippon.com). The castle was badly damaged. In 1874 the new Meiji government had the buildings demolished, and only the stone walls and the grounds remained (GLTJP, Fun Japan, Nippon.com).</p>
    <p>The Byakkotai, the &ldquo;White Tiger Corps,&rdquo; are the part of the story most visitors know. GLTJP calls them teenage boys, sons of Aizu clan soldiers. Nippon.com says about 20 young samurai fled to Mount Iimori during the siege, saw the town burning, believed the castle had fallen, and chose to die rather than be captured. Numbers and details vary in other accounts, so I keep to what these two sources say. From the keep you can see Mount Iimori, which is why this view often goes quiet.</p>

    <h2 id="keep">The Red-Roofed Keep<span class="h2-jp">赤瓦の天守</span></h2>
    <p>The keep you see today was rebuilt in reinforced concrete in 1965, and Nippon.com says it was funded by citizen donations. It has five levels and six stories (Nippon.com). The roof, however, is worth a second look. The 1965 rebuild used black tiles, and in 2011 the roof was refurbished with red ones to match the historical appearance (GLTJP, Nippon.com, Edo Legacy, Fun Japan). The Edo Legacy page says this red roof is the only one of its kind among Japanese castle keeps, which is a claim I could not check elsewhere.</p>
    <p>Inside is the Wakamatsu Castle Keep Local History Museum. The mytabi Fukushima page says the interior was renovated in March 2004 as a &ldquo;castle museum.&rdquo; Nippon.com lists exhibits on the castle&rsquo;s lords and local figures, including the bacteriologist Noguchi Hideyo, replicas of samurai helmets and a stone-walled storage area under the keep where large amounts of salt were kept. The top floor is an observation deck with views of the city and the Aizu region (Nippon.com, Fun Japan). The Edo Legacy page also mentions AR experiences that bring the lost palace to life, which I have not seen myself.</p>
    <p>Several small buildings were rebuilt using Edo-period drawings. GLTJP names the Hishiki-yagura (a storage turret) and the Minami-hashirinagaya (weapons storage). Nippon.com names the Kurogane Gate, the Hoshii Turret and the south barracks, built with Edo-period drawings and photographs from the 1870s, and says a digital art installation in the Hoshii Turret was on hold until the end of September 2026. Since the two lists differ, please look at the signs on site.</p>

    <h2 id="grounds">Rinkaku, Cherry Trees and the View of Iimori<span class="h2-jp">麟閣と桜</span></h2>
    <p>Nippon.com says the park covers 22.8 hectares, and the Edo Legacy page says it is a designated National Historic Site. In the main citadel stands the <strong>Rinkaku</strong> tea house. GLTJP links it with Shoan, the son of the tea master Sen no Rikyu. Nippon.com says it was moved to save it from demolition and reassembled in the park, in a thatched building with a Japanese garden. Fun Japan says it is an Important Cultural Property of Fukushima Prefecture, and that tea ceremonies are held daily. Prices differ slightly between sources (see below).</p>
    <p>About 1,000 cherry trees surround the castle (GLTJP, Edo Legacy), and the park is on Japan&rsquo;s Top 100 cherry blossom list (Edo Legacy). GLTJP says the trees are lit up during the blossom season. Fun Japan calls April the best time for a visit.</p>

    <h2 id="visit">Visiting Tsuruga Castle<span class="h2-jp">アクセス</span></h2>
    <ul class="practical-list"><li><strong>Admission (adult):</strong> keep 410 yen, elementary and junior high students 150 yen (GLTJP, Nippon.com, mytabi, Fun Japan). A combined ticket for the keep and the Rinkaku tea house is 520 yen (GLTJP, Nippon.com). GLTJP says credit cards are not accepted.</li><li><strong>Rinkaku alone:</strong> 210 yen plus 600 yen for matcha and a sweet (Nippon.com), or 200 yen plus 500 yen (Fun Japan). The two sources differ, so please check at the gate.</li><li><strong>Hours:</strong> 8:30 to 17:00, last entry 16:30; open every day of the year (GLTJP, Nippon.com, mytabi, Fun Japan).</li><li><strong>By bus from Aizuwakamatsu Station:</strong> GLTJP says to take the Haikara-san bus to the Tsurugajo Iriguchi stop and walk about 5 minutes. Fun Japan says the Aizu Loop Bus takes about 20 minutes to the Tsurugajo Kitaguchi stop plus a 5-minute walk, and mytabi says about 10 minutes by bus. The Edo Legacy page says to take the Hongo Loop Line for about 7 minutes to Sanno-cho and walk about 10 minutes. Routes and stop names differ by source, so please check the current timetable.</li><li><strong>On foot:</strong> about 30 minutes from the station (Fun Japan).</li><li><strong>From Tokyo:</strong> Tohoku Shinkansen to Koriyama about 1 hour 30 minutes, then the Ban-etsu West Line to Aizuwakamatsu about 1 hour 11 minutes (Edo Legacy).</li><li><strong>By car:</strong> about 300 parking spaces, charged (mytabi, single source).</li><li><strong>Time needed:</strong> no source gives this. My own estimate is about 1 to 1.5 hours for the keep and the park, longer if you take tea.</li></ul>

    <h2 id="stay">Making It a Trip<span class="h2-jp">滞在</span></h2>
    <p>The mytabi page lists Oyakuen, the garden of the Aizu Matsudaira clan, among nearby sights, but does not say how far away it is, so check a map before planning a walk. If you like castles that survived a war and are still being repaired, our <a href="/guides/hirosaki-castle/" class="inline-link" onclick="trackEvent('click','internal','guide_aizuwakamatsu_to_hirosaki')">Hirosaki Castle guide</a> covers Tohoku&rsquo;s original keep, and our <a href="/guides/odawara-castle/" class="inline-link" onclick="trackEvent('click','internal','guide_aizuwakamatsu_to_odawara')">Odawara Castle guide</a> covers another rebuilt keep.</p>
    <div class="key-callout">
      <p>&#127890; <strong>Plan your trip:</strong> Browse guided tours or plan a stay around Aizuwakamatsu. <a href="https://www.viator.com/search/Aizuwakamatsu?pid=P00298374&amp;mcid=42383&amp;medium=link&amp;campaign=sacred-japan" target="_blank" rel="noopener sponsored" onclick="trackEvent('click','affiliate','viator_aizuwakamatsu_local')">Browse Aizuwakamatsu tours &rarr;</a></p>
    </div>

    <h2 id="faq">Frequently Asked Questions<span class="h2-jp">よくあるご質問</span></h2>
    <div class="faq-stack">
'''+''.join(f'''    <details class="faq-item">
        <summary>{q}</summary>
        <div class="faq-answer">{a}</div>
    </details>
''' for q,a in faqs)+'''    </div>

    <h2 id="final">Before You Leave the Park<span class="h2-jp">むすびに</span></h2>
    <p>Give Tsuruga Castle at least an hour. Look up at the red roof from the grounds, climb to the top to find Mount Iimori, and take tea at the Rinkaku if you have time. Please treat the Byakkotai story with the quiet it deserves.</p>

    <div class="closing-block">
      <span class="torii">&#9961;&#65039;</span>
      <p>The keep was rebuilt. The story it holds is the real one.</p>
    </div>

    <!-- RELATED GUIDES -->
    <section class="related-section">
      <h2>Related Guides</h2>
      <span class="h2-jp">関連ガイド</span>

      <div class="related-grid">

        <a class="related-card" href="/guides/hirosaki-castle/" onclick="trackEvent('click','internal','related_aizuwakamatsu_to_hirosaki')">
          <div class="related-card-label">SACRED JAPAN ／ GUIDES</div>
          <div class="related-card-title">&#127983; Hirosaki Castle Guide &rarr;</div>
          <div class="related-card-desc">Tohoku&rsquo;s original keep, being moved on its base.</div>
        </a>

        <a class="related-card" href="/guides/odawara-castle/" onclick="trackEvent('click','internal','related_aizuwakamatsu_to_odawara')">
          <div class="related-card-label">SACRED JAPAN ／ GUIDES</div>
          <div class="related-card-title">&#127983; Odawara Castle Guide &rarr;</div>
          <div class="related-card-desc">The Hojo stronghold and a rebuilt keep.</div>
        </a>

        <a class="related-card" href="/castles/" onclick="trackEvent('click','internal','related_aizuwakamatsu_to_castles')">
          <div class="related-card-label">SACRED JAPAN ／ CASTLES</div>
          <div class="related-card-title">&#127983; Japan's Castles &rarr;</div>
          <div class="related-card-desc">Every castle guide, with photos and official links.</div>
        </a>

      </div>
    </section>

  </article>

'''
tail=tail.replace('kochi-castle',SL).replace('_kochi_','_aizuwakamatsu_').replace('DKochi','DAizuwakamatsu').replace('search/Kochi','search/Aizuwakamatsu')
def L(u,l,t): return f'<a href="{u}" target="_blank" rel="noopener" style="color:var(--beni);text-decoration:underline;" onclick="trackEvent(\'click\',\'external\',\'{l}\')">{t}</a>'
src='Sources verified at time of writing: '+', '.join([
 L('https://www.gltjp.com/en/directory/item/12428/','src_aizu_gltjp','GLTJP'),
 L('https://www.nippon.com/en/guide-to-japan/gu900324/','src_aizu_nippon','Nippon.com'),
 L('https://edolegacytravel.metro.tokyo.lg.jp/spots/tsurugajo-castle-aizu-wakamatsu-castle/','src_aizu_edo','Edo Legacy Travel'),
 L('https://www.fun-japan.jp/jp/articles/9359','src_aizu_fun','Fun Japan'),
 L('https://fukushima-en.mytabi.net/tsurugajo.php','src_aizu_mytabi','mytabi Fukushima'),
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
l1="Aizuwakamatsu Castle Guide:"; l2="The Red-Roofed Keep"; print(d.textlength(l2,font=f1),d.textlength(l1,font=f1)); assert d.textlength(l2,font=f1)<1090 and d.textlength(l1,font=f1)<1090
d.text((66,170),l1,font=f1,fill=(26,15,15)); d.text((66,238),l2,font=f1,fill=(26,15,15)); d.text((66,332),"会津若松城",font=f2,fill=(138,125,120))
im.save(R+f'images/og/og-guides-{SL}.jpg',quality=88); print('built',len(out))
