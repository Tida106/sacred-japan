import re,json,os,glob
from PIL import Image,ImageDraw,ImageFont
R='/home/claude/sacred-japan/'; SL='tsuyama-castle'
s=open(R+'guides/kochi-castle/index.html',encoding='utf-8').read()
i=s.index('<main>'); j=s.index('</main>'); head,tail=s[:i],s[j:]
TITLE="Tsuyama Castle Guide: Stone Walls, a Rebuilt Turret and 1,000 Cherry Trees"
DESC="A licensed guide's guide to Tsuyama Castle (Kakuzan Park) in Okayama: Mori Tadamasa's hill castle, why the keep was torn down in 1874, the stone walls, the rebuilt Bitchu Turret, the cherry blossoms and how to visit."
head=re.sub(r'<title>.*?</title>',f'<title>{TITLE} | Sacred Japan</title>',head,count=1)
head=re.sub(r'(<meta (?:name="description"|property="og:description"|name="twitter:description") content=")[^"]*(")',lambda m:m.group(1)+DESC+m.group(2),head)
head=re.sub(r'(<meta (?:property="og:title"|name="twitter:title") content=")[^"]*(")',lambda m:m.group(1)+TITLE+m.group(2),head)
head=re.sub(r'("headline": ")[^"]*(")',lambda m:m.group(1)+TITLE+m.group(2),head)
head=re.sub(r'("description": ")A licensed[^"]*(")',lambda m:m.group(1)+DESC+m.group(2),head)
head=re.sub(r'<meta name="keywords" content="[^"]*">','<meta name="keywords" content="Tsuyama Castle, Kakuzan Park, Tsuyama Castle cherry blossoms, Tsuyama Castle admission, Tsuyama Castle hours, Bitchu Turret, Tsuyama Okayama, Mori Tadamasa, Tsuyama sakura festival">',head)
head=head.replace('guides/kochi-castle','guides/tsuyama-castle').replace('guide_kochi_','guide_tsuyama_').replace('og-guides-kochi-castle','og-guides-tsuyama-castle')
head=head.replace('高知城','津山城').replace('Kochi Castle','Tsuyama Castle')
head=re.sub(r"<h1>.*?</h1>","<h1><em>Tsuyama Castle</em>: Stone Walls, a Rebuilt Turret and 1,000 Cherry Trees</h1>",head,count=1,flags=re.S)
head=head.replace("Shikoku's original keep, and the only castle where the lord's palace still stands beside it.","A hill castle in Okayama whose keep was torn down in 1874: great stone walls, a turret rebuilt in 2005 and about 1,000 cherry trees.")
faqs=[
("Is there a keep at Tsuyama Castle?","No. Wikipedia says the keep and all the turrets were destroyed in 1874 to 1875, after the castle passed to the Ministry of Finance in 1873 and was sold. GLTJP says most buildings were demolished after the Meiji-era abandonment order. What remains is the stone walls, and the one restored building is the Bitchu Turret."),
("Who built Tsuyama Castle?","GLTJP says Mori Tadamasa, a younger brother of Mori Ranmaru, an aide of Oda Nobunaga, renamed the hill Tsuyama and began building. Wikipedia says he moved here from Shinano in 1603 with 186,000 koku and started that year. The two sources disagree on the finish: Wikipedia gives 1616, while GLTJP says 1604 after 13 years of work, which does not add up from a 1603 start, so I would say the early 1600s to 1616. Wikipedia also says a smaller castle was built on the hill in the 1440s by the Yamana, and that it was abandoned."),
("What does it cost, and when is it open?","GLTJP and Jeepe's highlights give 310 yen for adults, while Nippon.com and Jeepe's FAQ give 300 yen, and junior high school students and younger are free. Normal hours are 8:40 to 19:00 in summer and 8:40 to 17:00 in winter, but the month where each season begins differs by source (GLTJP: April to September; Jeepe: May to September). During the cherry blossom festival the park opens at 7:30 and closes at 22:00. GLTJP gives December 29 to 31 as closed. Please confirm officially."),
("How do I get there?","GLTJP and Jeepe say it is about a 10-minute walk from JR Tsuyama Station. Jeepe says the JR Tsuyama Line takes about 1 hour 10 minutes from Okayama Station. Jeepe also says parking near the park costs about 600 yen and fills early in the blossom season."),
("When are the cherry blossoms?","Nippon.com and Jeepe give early April as the usual peak, about 1,000 Somei Yoshino trees, and Jeepe says the festival normally runs about two weeks from late March to mid-April. The dates vary by year, so please check the forecast and the festival dates before you go. The trees are lit at night, roughly 18:00 to 22:00 according to Jeepe."),
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
      <li><a href="#opening">A Castle Known by Its Walls</a></li>
      <li><a href="#history">Mori Tadamasa Builds on the Hill</a></li>
      <li><a href="#end">1873 to 1875: Sold and Taken Down</a></li>
      <li><a href="#walls">The Stone Walls</a></li>
      <li><a href="#bitchu">The Bitchu Turret</a></li>
      <li><a href="#blossoms">Cherry Blossoms</a></li>
      <li><a href="#visit">Visiting Tsuyama Castle</a></li>
      <li><a href="#stay">Making It a Trip</a></li>
      <li><a href="#faq">Frequently Asked Questions</a></li>
      <li><a href="#final">A Castle You Read in Stone</a></li>
    </ol>
  </aside>

  <article>

    <section id="opening">
      <p class="opening">As a licensed guide, I describe Tsuyama Castle to visitors as a castle you read in stone. The keep is gone, and so are almost all of the buildings, but the great walls on the hill are still there, and in early April about a thousand cherry trees grow along them. It is one of the better places in Okayama Prefecture to see how large a castle on a hill could be, and it is easy to reach from the station.</p>
      <p>This guide covers who built it and why it came down, what you can still see, the Bitchu Turret, the cherry blossoms and the practical details. Where my sources disagree, I say so.</p>
    </section>

    <h2 id="history">Mori Tadamasa Builds on the Hill<span class="h2-jp">森忠政の築城</span></h2>
    <p>The hill had an earlier castle. Wikipedia says the Yamana family built a fortress in the Tsuru mountains in the 1440s, and that it was abandoned after the Onin War weakened the clan. GLTJP gives the name Tsuruyama for that first castle and 1441 for the date.</p>
    <p>The castle you see traces came later. GLTJP says Mori Tadamasa, a younger brother of Mori Ranmaru, a close aide of Oda Nobunaga, renamed the hill Tsuyama and began construction. Wikipedia says he came from Shinano in 1603 with 186,000 koku and says the work finished in 1616 with 77 turrets and a five-story keep. GLTJP says more than 80 palaces, turrets and gates were built and describes the castle as one of three great hirayama castles, along with Himeji and Matsuyama. I would treat the exact counts as approximate, and GLTJP's completion date of 1604 does not fit its own 13 years of work, so I would trust Wikipedia's 1616.</p>
    <p>Wikipedia adds an odd detail: five-story towers were banned in the early Edo period, so Tadamasa removed the roof of the fourth floor to keep the keep from counting as five stories. This is a single-source detail that I have not confirmed elsewhere, so please take it as a guide's note.</p>

    <h2 id="end">1873 to 1875: Sold and Taken Down<span class="h2-jp">廃城</span></h2>
    <p>The end came with the Meiji government. GLTJP says most buildings were demolished after the abandonment order, and Nippon.com gives 1873 for the government ordinance that ordered feudal castles torn down and says only the stone walls survived. Wikipedia says the castle came under Ministry of Finance management in 1873 and was sold, and that the keep and all the turrets were destroyed in 1874 to 1875. It also says the stone walls of the Koshimaki Turret collapsed and that conservation followed in 1890.</p>

    <h2 id="walls">The Stone Walls<span class="h2-jp">石垣</span></h2>
    <p>The walls are the reason to come. GLTJP says the stone walls stand about 10 meters high and are still as they were when built. Nippon.com says the three-tiered wall is 45 meters high. These figures are very far apart, and I could not reconcile them, so I would not quote either one as a measurement. What I can say is that the walls are stacked in tiers up the hill, and that they are the backdrop of nearly every photograph of the castle.</p>
    <p>Jeepe notes that the grounds have many stone steps and slopes, and that surfaces can be slippery after rain, so please wear comfortable shoes.</p>

    <h2 id="bitchu">The Bitchu Turret<span class="h2-jp">備中櫓</span></h2>
    <p>The one rebuilt building is the Bitchu Turret. GLTJP says it was the largest turret and was once second in presence only to the keep, and that it was restored as part of the castle's 400th anniversary project. Wikipedia and Nippon.com say the restoration took place in 2004 to 2005 (Nippon.com says 2004). GLTJP says it has a tatami room, which is unusual for a turret, and that it was joined to the main hall by a corridor, so it may have been part of the main hall.</p>
    <p>Jeepe says visitors can go inside and see tatami-floored rooms in a palace style, with displays on the castle's history. Nippon.com says it is open to the public and gives a view of the cherry blossoms. I would go inside for both reasons.</p>

    <h2 id="blossoms">Cherry Blossoms<span class="h2-jp">桜</span></h2>
    <p>Kakuzan Park, as the site is now called, is best known for its cherry trees. GLTJP, Nippon.com and Jeepe all give about 1,000 trees, mostly Somei Yoshino, and Nippon.com says they bloom in early April in light pink. Nippon.com counts the park among Japan's top 100 cherry blossom spots. Jeepe says lanterns are lit along the paths, and that the lit blossoms reflect off the stone walls. GLTJP says the blossoms can be seen from the top of the walls.</p>
    <p>Jeepe says weekends and holidays are crowded, and recommends weekday mornings or late afternoons. Early morning is the easiest time for photographs.</p>

    <h2 id="visit">Visiting Tsuyama Castle<span class="h2-jp">アクセス</span></h2>
    <ul class="practical-list"><li><strong>Admission:</strong> 310 yen for adults (GLTJP, Jeepe highlights) or 300 yen (Nippon.com, Jeepe FAQ), free for junior high school students and younger. Please confirm on the official site.</li><li><strong>Hours:</strong> 8:40 to 19:00 in the warm season and 8:40 to 17:00 in the cold season, with the season split differing by source (GLTJP: April to September; Jeepe: May to September). Festival hours are 7:30 to 22:00.</li><li><strong>Closed:</strong> December 29 to 31 (GLTJP).</li><li><strong>Walk:</strong> about 10 minutes from JR Tsuyama Station (GLTJP, Jeepe).</li><li><strong>Train:</strong> about 1 hour 10 minutes from Okayama Station on the JR Tsuyama Line (Jeepe).</li><li><strong>Car:</strong> about 15 minutes from Tsuyama IC or Innosho IC on the Chugoku Expressway; nearby temporary parking is about 600 yen and fills early in the blossom season (Jeepe).</li><li><strong>Address:</strong> 135 Sange, Tsuyama, Okayama (GLTJP).</li></ul>

    <h2 id="stay">Making It a Trip<span class="h2-jp">滞在</span></h2>
    <p>Tsuyama sits inland from the coast, so most visitors come on a day trip from Okayama or stay in the town overnight. If you are in Okayama, our <a href="/guides/okayama-castle/" class="inline-link" onclick="trackEvent('click','internal','guide_tsuyama_to_okayama')">Okayama Castle guide</a> covers the rebuilt Crow Castle and Korakuen, and our <a href="/guides/bitchu-matsuyama-castle/" class="inline-link" onclick="trackEvent('click','internal','guide_tsuyama_to_bitchu')">Bitchu Matsuyama Castle guide</a> covers the surviving keep on a mountaintop in the same prefecture.</p>
    <div class="key-callout">
      <p>&#127890; <strong>Plan your trip:</strong> Browse guided tours, or plan a stay near Okayama. <a href="https://www.viator.com/search/Okayama?pid=P00298374&amp;mcid=42383&amp;medium=link&amp;campaign=sacred-japan" target="_blank" rel="noopener sponsored" onclick="trackEvent('click','affiliate','viator_tsuyama_local')">Browse Okayama tours &rarr;</a></p>
    </div>

    <h2 id="faq">Frequently Asked Questions<span class="h2-jp">よくあるご質問</span></h2>
    <div class="faq-stack">
'''+''.join(f'''    <details class="faq-item">
        <summary>{q}</summary>
        <div class="faq-answer">{a}</div>
    </details>
''' for q,a in faqs)+'''    </div>

    <h2 id="final">A Castle You Read in Stone<span class="h2-jp">むすびに</span></h2>
    <p>Tsuyama Castle is worth a visit if you like stonework and spring blossoms. Walk up from the station, go inside the Bitchu Turret, and look at the walls in tiers; the keep is gone, but the hill still shows how big the castle was.</p>

    <div class="closing-block">
      <span class="torii">&#9961;&#65039;</span>
      <p>The keep is gone. The walls still hold the hill.</p>
    </div>

    <!-- RELATED GUIDES -->
    <section class="related-section">
      <h2>Related Guides</h2>
      <span class="h2-jp">関連ガイド</span>

      <div class="related-grid">

        <a class="related-card" href="/guides/okayama-castle/" onclick="trackEvent('click','internal','related_tsuyama_to_okayama')">
          <div class="related-card-label">SACRED JAPAN ／ GUIDES</div>
          <div class="related-card-title">&#127983; Okayama Castle Guide &rarr;</div>
          <div class="related-card-desc">The black Crow Castle and Korakuen garden.</div>
        </a>

        <a class="related-card" href="/guides/bitchu-matsuyama-castle/" onclick="trackEvent('click','internal','related_tsuyama_to_bitchu')">
          <div class="related-card-label">SACRED JAPAN ／ GUIDES</div>
          <div class="related-card-title">&#127983; Bitchu Matsuyama Castle Guide &rarr;</div>
          <div class="related-card-desc">A surviving keep on a mountaintop in Okayama.</div>
        </a>

        <a class="related-card" href="/castles/" onclick="trackEvent('click','internal','related_tsuyama_to_castles')">
          <div class="related-card-label">SACRED JAPAN ／ CASTLES</div>
          <div class="related-card-title">&#127983; Japan's Castles &rarr;</div>
          <div class="related-card-desc">Every castle guide, with photos and official links.</div>
        </a>

      </div>
    </section>

  </article>

'''
tail=tail.replace('kochi-castle',SL).replace('_kochi_','_tsuyama_').replace('DKochi','DOkayama').replace('search/Kochi','search/Okayama')
def L(u,l,t): return f'<a href="{u}" target="_blank" rel="noopener" style="color:var(--beni);text-decoration:underline;" onclick="trackEvent(\'click\',\'external\',\'{l}\')">{t}</a>'
src='Sources verified at time of writing: '+', '.join([
 L('https://www.gltjp.com/en/directory/item/12541','src_tsuyama_gltjp','GLTJP'),
 L('https://nippon.com/en/guide-to-japan/sakura00133020','src_tsuyama_nippon','Nippon.com'),
 L('https://www.jeepe.jp/en/articles/tsuyama-sakura-festival-guide-1259','src_tsuyama_jeepe','Jeepe'),
 L('https://en.wikipedia.org/wiki/Tsuyama_Castle','src_tsuyama_wikipedia','Wikipedia'),
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
l1="Tsuyama Castle Guide:"; l2="Stone Walls and 1,000 Cherry Trees"; print(d.textlength(l2,font=f1)); assert d.textlength(l2,font=f1)<1090
d.text((66,170),l1,font=f1,fill=(26,15,15)); d.text((66,238),l2,font=f1,fill=(26,15,15)); d.text((66,332),"津山城",font=f2,fill=(138,125,120))
im.save(R+f'images/og/og-guides-{SL}.jpg',quality=88); print('built',len(out))
