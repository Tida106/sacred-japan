import re,json,os,glob
from PIL import Image,ImageDraw,ImageFont
R='/home/claude/sacred-japan/'; SL='wakayama-castle'
s=open(R+'guides/kochi-castle/index.html',encoding='utf-8').read()
i=s.index('<main>'); j=s.index('</main>'); head,tail=s[:i],s[j:]
TITLE="Wakayama Castle Guide: The Kishu Tokugawa Seat, a Linked Keep and the Slanted Bridge"
DESC="A licensed guide's guide to Wakayama Castle: the Kishu Tokugawa seat, the rebuilt linked keep, the slanted bridge corridor, the marked stone walls, Nishinomaru Garden, fees and access from the stations."
TAG='The Kishu Tokugawa seat, a rebuilt linked keep and a slanted bridge corridor, a short bus ride from the station.'
head=re.sub(r'<title>.*?</title>',f'<title>{TITLE} | Sacred Japan</title>',head,count=1)
head=re.sub(r'(<meta (?:name="description"|property="og:description"|name="twitter:description") content=")[^"]*(")',lambda m:m.group(1)+DESC+m.group(2),head)
head=re.sub(r'(<meta (?:property="og:title"|name="twitter:title") content=")[^"]*(")',lambda m:m.group(1)+TITLE+m.group(2),head)
head=re.sub(r'("headline": ")[^"]*(")',lambda m:m.group(1)+TITLE+m.group(2),head)
head=re.sub(r'("description": ")A licensed[^"]*(")',lambda m:m.group(1)+DESC+m.group(2),head)
head=re.sub(r'("date(?:Published|Modified)": ")[^"]*(")',lambda m:m.group(1)+'2026-11-05'+m.group(2),head)
head=re.sub(r'<meta name="keywords" content="[^"]*">','<meta name="keywords" content="Wakayama Castle, Kishu Tokugawa, Tokugawa Yorinobu, Wakayama Castle keep, Nishinomaru Garden, slanted bridge corridor, Wakayama sightseeing, Japan castles">',head)
head=head.replace('guides/kochi-castle','guides/wakayama-castle').replace('guide_kochi_','guide_wakayama_castle_').replace('og-guides-kochi-castle','og-guides-wakayama-castle')
head=head.replace('高知城','和歌山城').replace('Kochi Castle','Wakayama Castle')
head=re.sub(r"<h1>.*?</h1>","<h1><em>Wakayama Castle</em>: The Kishu Tokugawa Seat, a Linked Keep and the Slanted Bridge</h1>",head,count=1,flags=re.S)
head=head.replace("Shikoku's original keep, and the only castle where the lord's palace still stands beside it.",TAG)
faqs=[
("Is the keep at Wakayama Castle original?","No. The keep was destroyed in the 1945 air raid and the present one is a ferroconcrete replica. GLTJP gives the rebuild as 1958 with the same exterior; japan-guide says 1957. Fun Japan adds that an earlier keep was destroyed by lightning in 1846 and rebuilt in 1850 (one source only). Only the stone walls and a few gates survive from the original castle."),
("How much does it cost to visit?","The keep is 410 yen for adults and 200 yen for elementary and junior high students (GLTJP, japan-guide, Fun Japan), open 9:00 to 17:30 with last entry at 17:00 and closed 29 to 31 December. An older listing on Japan Experience says 350 yen, and japan-guide also mentions a much higher figure from April 2025 that I could not confirm, so please check the day&rsquo;s price. The grounds and Nishinomaru Garden are free (GLTJP, japan-guide)."),
("What is the slanted bridge corridor?","It is a roofed corridor bridge that links the Nishinomaru area with the Ninomaru Ooku (GLTJP). GLTJP says that in the Edo period only a limited number of people, such as the lord, could use it, that it slopes at about 11 degrees and has steps to stop people slipping, and that it was restored in 2006 from Edo-period drawings. You can walk across it for free."),
("When are the cherry blossoms and autumn leaves?","GLTJP says about 600 trees, mainly Somei Yoshino, bloom on the grounds, with a festival from late March to early April and evening illumination from sunset to 23:00. The same page says the autumn colours in Nishinomaru Garden are best from late November to early December. Both dates move with the weather."),
("How do I get there?","From JR Wakayama Station, GLTJP says to take Wakayama Bus route 0 or 25 to the Wakayama-jo-mae stop, about 5 to 6 minutes; japan-guide gives 5 minutes and 230 yen. From Nankai Wakayamashi Station, japan-guide says a bus takes 5 minutes (220 yen) and Fun Japan and Japan Experience say about a 10-minute walk. Walking from JR Wakayama Station is 20 to 30 minutes depending on the source."),
("How long should I allow?","That is my own estimate: about an hour for the keep and the corridor bridge, and another hour if you add Nishinomaru Garden and the museums beside the park. GLTJP and Japan Experience both mention the Museum of Modern Art, and GLTJP also mentions the Wakayama Prefectural Museum."),
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
assert not re.search('Kochi|Shikoku|kochi|Kanazawa|Shuri|Naha|Takeda|Asago|Machu|Odawara|Hojo|Aizu|Tsuruga|Goryokaku|Hakodate|Ezo|Sendai|Aoba|Masamune',hh),re.findall('.{30}(?:Kochi|Shikoku|Kanazawa|Shuri|Naha|Aizu|Tsuruga|Goryokaku|Hakodate).{20}',hh)
IL='class="inline-link"'
main='''<main>

  <!-- TABLE OF CONTENTS -->
  <aside class="toc" aria-label="Table of contents">
    <div class="toc-label">TABLE OF CONTENTS ／ 目次</div>
    <div class="toc-title">In This Guide</div>
    <ol>
      <li><a href="#opening">A Castle of the Kishu Tokugawa</a></li>
      <li><a href="#history">From Hidenaga to the Kishu Tokugawa</a></li>
      <li><a href="#fall">Lightning, Abandonment and 1945</a></li>
      <li><a href="#see">What You Can See Today</a></li>
      <li><a href="#visit">Visiting Wakayama Castle</a></li>
      <li><a href="#stay">Making It a Trip</a></li>
      <li><a href="#faq">Frequently Asked Questions</a></li>
      <li><a href="#final">Before You Cross the Bridge</a></li>
    </ol>
  </aside>

  <article>

    <section id="opening">
      <p class="opening">As a licensed guide, I describe Wakayama Castle to visitors as the castle of a family that nearly ruled Japan. Ieyasu&rsquo;s tenth son was sent here in 1619 to found the Kishu Tokugawa, one of the three branches of the shogun&rsquo;s own clan, and the white keep on its small hill still looks the part. It is a postwar replica, but it comes with a stone-wall puzzle, a roofed bridge that slopes down a hillside and a garden built by that first lord.</p>
      <p>This guide covers the castle&rsquo;s history, what you can see today, and the practical details. Where my sources disagree I say so, and I mark claims I found in only one place.</p>
    </section>

    <h2 id="history">From Hidenaga to the Kishu Tokugawa<span class="h2-jp">紀州徳川家の城</span></h2>
    <p>The castle began with Hideyoshi. Fun Japan and Japan Experience say Toyotomi Hideyoshi had the castle built in 1585, with his younger brother Hidenaga in charge, and japan-guide says Hideyoshi gave Kii Province to Hidenaga, who built an early version on this site. GLTJP credits the first build to Todo Takatora in its introduction and to Hidenaga in its history section, so I would just say it was begun in 1585 under Hideyoshi&rsquo;s orders.</p>
    <p>GLTJP says that after Sekigahara in 1600 Asano Yoshinaga became lord, and that work on the linked keep and the Honmaru progressed in his time. In 1619 Tokugawa Yorinobu, Ieyasu&rsquo;s tenth son, entered the castle and founded the Kishu Tokugawa family, which held it for about 250 years (GLTJP). Japan-guide describes the Kishu branch as one of three cadet branches of the Tokugawa clan, the others being based in Nagoya and in present-day Ibaraki.</p>
    <p>Japan Experience says the castle sits on a small hill called Torafusu, about 49 metres high, and that its curved corners follow the contours of the hill. I found that height in one source only.</p>

    <h2 id="fall">Lightning, Abandonment and 1945<span class="h2-jp">焼失と再建</span></h2>
    <p>Fun Japan says lightning destroyed the keep in 1846 and that it was rebuilt in 1850; I found that in one source only. Japan-guide says the castle was abandoned after the Meiji Restoration and many buildings were demolished, and that the grounds opened to the public in 1901 (one source only). In the Second World War, a large bombing raid destroyed eleven important buildings including the keep (japan-guide); GLTJP dates this to the 1945 Wakayama air raid.</p>
    <p>The present keep is a reconstruction. GLTJP says it was rebuilt in 1958 with the same exterior; japan-guide gives 1957. Japan Experience adds that the Otemon Gate was rebuilt in 1989 and that only the Okaguchi Gate and the stone walls survive from the original castle (one source only).</p>

    <h2 id="see">What You Can See Today<span class="h2-jp">見どころ</span></h2>
    <p>The <strong>keep</strong> is a white three-storey building connected to a smaller tower by a connecting turret (tamon yagura), according to GLTJP, which calls it one of Japan&rsquo;s three great linked-tower keeps. Fun Japan names Himeji and Matsumoto as the other two, whereas other lists I know name Himeji and Matsuyama, so I would not rely on any one list. Inside, GLTJP says there are arms, armour and Kishu Tokugawa documents, and japan-guide says the top floor has an observation deck over the city.</p>
    <p>The <strong>slanted bridge corridor</strong> is my favourite part. GLTJP says it is a roofed corridor linking Nishinomaru with the Ninomaru Ooku, that in the Edo period only a limited number of people such as the lord could use it, and that it slopes at about 11 degrees with non-slip steps. It was restored in 2006 from Edo-period drawings and you can cross it freely.</p>
    <p>The <strong>stone walls</strong> carry a puzzle. GLTJP says about 170 types and more than 2,100 mason&rsquo;s marks have been identified, on tops, bottoms and sides, with circles, triangles, family crests and names, and that their meaning is unclear. If you look closely as you climb, you will start to spot them.</p>
    <p><strong>Nishinomaru Garden</strong> is a national Place of Scenic Beauty and, according to GLTJP, was created in the early Edo period by Yorinobu for tea ceremonies and Noh. It is a strolling pond garden with a two-tiered pond and a spring-fed waterfall, and it is known for autumn colour, which is why GLTJP also calls it Momijidani. Entry is free (GLTJP, japan-guide).</p>
    <p>Beside the garden, GLTJP lists the Koshoan tea house (470 yen per serving, 9:00 to 16:30) and a free small zoo on the grounds. The zoo&rsquo;s closing days (Tuesdays in June to September and December to February) are from GLTJP alone, so please check before you plan around it.</p>
    <p>On the south side of the park, GLTJP and Japan Experience both mention the Museum of Modern Art, and GLTJP adds the Wakayama Prefectural Museum, which it says opened in 1994 and was designed by Kisho Kurokawa.</p>

    <h2 id="visit">Visiting Wakayama Castle<span class="h2-jp">アクセス</span></h2>
    <ul class="practical-list"><li><strong>Keep:</strong> 410 yen for adults and 200 yen for elementary and junior high students (GLTJP, japan-guide, Fun Japan); Japan Experience lists an older 350 yen, and japan-guide mentions a higher figure from April 2025 that I could not confirm. Please check the day&rsquo;s price.</li><li><strong>Hours:</strong> 9:00 to 17:30, last entry 17:00; closed 29 to 31 December (GLTJP, japan-guide). Japan Experience lists 9:00 to 16:30, which looks out of date.</li><li><strong>Nishinomaru Garden:</strong> free, 9:00 to 17:00 (GLTJP); japan-guide gives last entry 16:45.</li><li><strong>From JR Wakayama Station:</strong> bus route 0 or 25 to Wakayama-jo-mae in about 5 to 6 minutes (GLTJP), 230 yen (japan-guide). Walking takes 20 to 30 minutes depending on the source.</li><li><strong>From Nankai Wakayamashi Station:</strong> bus in 5 minutes for 220 yen (japan-guide), or a walk of 10 minutes (Fun Japan, Japan Experience) to 15 to 20 minutes (japan-guide).</li><li><strong>Taxi:</strong> about 10 minutes and about 1,000 yen from either station (japan-guide).</li><li><strong>Time needed:</strong> my own estimate is an hour for the keep and the corridor bridge, and another hour for the garden and a museum.</li></ul>

    <h2 id="stay">Making It a Trip<span class="h2-jp">滞在</span></h2>
    <p>Wakayama is an easy day trip from Osaka. Our <a href="/guides/osaka-castle/" '''+IL+''' onclick="trackEvent('click','internal','guide_wakayama_castle_to_osaka')">Osaka Castle guide</a> covers Hideyoshi&rsquo;s own castle, and our <a href="/guides/himeji-castle/" '''+IL+''' onclick="trackEvent('click','internal','guide_wakayama_castle_to_himeji')">Himeji Castle guide</a> covers the original linked-keep castle that Wakayama is often compared with.</p>
    <p><strong>Cherry blossoms and colour:</strong> GLTJP says about 600 trees, mainly Somei Yoshino, bloom on the grounds, with a festival from late March to early April and evening illumination from sunset to 23:00. It recommends late November to early December for the autumn leaves.</p>
    <div class="key-callout">
      <p>&#127890; <strong>Plan your trip:</strong> Browse guided tours or plan a stay around Wakayama. <a href="https://www.viator.com/search/Wakayama?pid=P00298374&amp;mcid=42383&amp;medium=link&amp;campaign=sacred-japan" target="_blank" rel="noopener sponsored" onclick="trackEvent('click','affiliate','viator_wakayama_castle_local')">Browse Wakayama tours &rarr;</a></p>
    </div>

    <h2 id="faq">Frequently Asked Questions<span class="h2-jp">よくあるご質問</span></h2>
    <div class="faq-stack">
'''+''.join(f'''    <details class="faq-item">
        <summary>{q}</summary>
        <div class="faq-answer">{a}</div>
    </details>
''' for q,a in faqs)+'''    </div>

    <h2 id="final">Before You Cross the Bridge<span class="h2-jp">むすびに</span></h2>
    <p>Go for the corridor bridge, the marked stones and the garden, and treat the keep as a handsome postwar copy of a Tokugawa original. Walk the slope the way the lord did, then come back down through the autumn trees.</p>

    <div class="closing-block">
      <span class="torii">&#9961;&#65039;</span>
      <p>A Tokugawa hill, a sloping bridge and 2,100 stone marks nobody has read.</p>
    </div>

    <!-- RELATED GUIDES -->
    <section class="related-section">
      <h2>Related Guides</h2>
      <span class="h2-jp">関連ガイド</span>

      <div class="related-grid">

        <a class="related-card" href="/guides/osaka-castle/" onclick="trackEvent('click','internal','related_wakayama_castle_to_osaka')">
          <div class="related-card-label">SACRED JAPAN ／ GUIDES</div>
          <div class="related-card-title">&#127983; Osaka Castle Guide &rarr;</div>
          <div class="related-card-desc">Hideyoshi&rsquo;s castle, rebuilt in concrete.</div>
        </a>

        <a class="related-card" href="/guides/himeji-castle/" onclick="trackEvent('click','internal','related_wakayama_castle_to_himeji')">
          <div class="related-card-label">SACRED JAPAN ／ GUIDES</div>
          <div class="related-card-title">&#127983; Himeji Castle Guide &rarr;</div>
          <div class="related-card-desc">The original linked-keep castle.</div>
        </a>

        <a class="related-card" href="/castles/" onclick="trackEvent('click','internal','related_wakayama_castle_to_castles')">
          <div class="related-card-label">SACRED JAPAN ／ CASTLES</div>
          <div class="related-card-title">&#127983; Japan's Castles &rarr;</div>
          <div class="related-card-desc">Every castle guide, with photos and official links.</div>
        </a>

      </div>
    </section>

  </article>

'''
tail=tail.replace('kochi-castle',SL).replace('_kochi_','_sendai_castle_').replace('DKochi','DWakayama').replace('search/Kochi','search/Wakayama')
def L(u,l,t): return f'<a href="{u}" target="_blank" rel="noopener" style="color:var(--beni);text-decoration:underline;" onclick="trackEvent(\'click\',\'external\',\'{l}\')">{t}</a>'
src='Sources verified at time of writing: '+', '.join([
 L('https://www.japan-guide.com/e/e4927.html','src_wakayama_jg','japan-guide'),
 L('https://www.gltjp.com/en/article/item/20419/','src_wakayama_gltjp','GLTJP'),
 L('https://www.fun-japan.jp/en/articles/12721','src_wakayama_fj','Fun Japan'),
 L('https://www.japan-experience.com/all-about-japan/wakayama/attractions-excursions/wakayama-castle','src_wakayama_je','Japan Experience'),
])+'. Hours, prices and availability change'
tail,n=re.subn(r'Sources verified at time of writing:.*?Hours, prices and availability change',lambda m:src,tail,flags=re.S); assert n==1
out=head+main+tail
assert not re.search('Kochi|Shikoku|kochi|Kanazawa|Shuri|Naha|Takeda Castle|Asago|Machu|Goryokaku Tower|Republic of Ezo|Sendai|Masamune',re.sub(r'"mainEntity": \[.*','',out,flags=re.S)),re.findall('.{30}(?:Kochi|Kanazawa|Shuri|Naha|Asago|Machu).{20}',out)
os.makedirs(R+f'guides/{SL}',exist_ok=True); open(R+f'guides/{SL}/index.html','w',encoding='utf-8').write(out)
for tg in ['div','figure','picture','p','a','ul','li','details','section','h2']:
    assert len(re.findall(f'<{tg}[ >]',out))==len(re.findall(f'</{tg}>',out)),tg
for m in re.findall(r'<script type="application/ld\+json">(.*?)</script>',out,re.S): json.loads(m)
im=Image.open(R+'images/og/og-guides-matsue-castle.jpg').convert('RGB'); d=ImageDraw.Draw(im)
d.rectangle([40,150,1170,380],fill=(252,240,242)); d.rectangle([1118,66,1160,96],fill=(252,240,242))
f1=ImageFont.truetype(glob.glob('/usr/share/fonts/**/DejaVuSerif-Bold.ttf',recursive=True)[0],48)
f2=ImageFont.truetype(glob.glob('/usr/share/fonts/**/NotoSerifCJK-Bold.ttc',recursive=True)[0],28,index=0)
l1="Wakayama Castle Guide:"; l2="Kishu Tokugawa's Linked Keep"; print(d.textlength(l2,font=f1),d.textlength(l1,font=f1)); assert d.textlength(l2,font=f1)<1090
d.text((66,170),l1,font=f1,fill=(26,15,15)); d.text((66,238),l2,font=f1,fill=(26,15,15)); d.text((66,332),"和歌山城",font=f2,fill=(138,125,120))
im.save(R+f'images/og/og-guides-{SL}.jpg',quality=88); print('built',len(out))
