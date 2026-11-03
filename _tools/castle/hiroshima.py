import re,json,os,glob
from PIL import Image,ImageDraw,ImageFont
R='/home/claude/sacred-japan/'; SL='hiroshima-castle'
s=open(R+'guides/kochi-castle/index.html',encoding='utf-8').read()
i=s.index('<main>'); j=s.index('</main>'); head,tail=s[:i],s[j:]
TITLE="Hiroshima Castle Guide: The Carp Castle, the 1945 Blast and a 1958 Keep"
DESC="A licensed guide's guide to Hiroshima Castle: the Mori founding, the Asano era, what happened on 6 August 1945, the 1958 rebuilt keep, the Ninomaru turrets, the surviving trees and how to visit."
head=re.sub(r'<title>.*?</title>',f'<title>{TITLE} | Sacred Japan</title>',head,count=1)
head=re.sub(r'(<meta (?:name="description"|property="og:description"|name="twitter:description") content=")[^"]*(")',lambda m:m.group(1)+DESC+m.group(2),head)
head=re.sub(r'(<meta (?:property="og:title"|name="twitter:title") content=")[^"]*(")',lambda m:m.group(1)+TITLE+m.group(2),head)
head=re.sub(r'("headline": ")[^"]*(")',lambda m:m.group(1)+TITLE+m.group(2),head)
head=re.sub(r'("description": ")A licensed[^"]*(")',lambda m:m.group(1)+DESC+m.group(2),head)
head=re.sub(r'<meta name="keywords" content="[^"]*">','<meta name="keywords" content="Hiroshima Castle, Hiroshima Castle guide, Carp Castle, Rijo, Hiroshima Castle admission, Hiroshima Castle hours, Hiroshima Castle atomic bomb, Hiroshima Castle history, Hiroshima Ninomaru">',head)
head=head.replace('guides/kochi-castle','guides/hiroshima-castle').replace('guide_kochi_','guide_hiroshima_').replace('og-guides-kochi-castle','og-guides-hiroshima-castle')
head=head.replace('高知城','広島城').replace('Kochi Castle','Hiroshima Castle')
head=re.sub(r"<h1>.*?</h1>","<h1><em>Hiroshima Castle</em>: The Carp Castle, the 1945 Blast and a 1958 Keep</h1>",head,count=1,flags=re.S)
head=head.replace("Shikoku's original keep, and the only castle where the lord's palace still stands beside it.","A castle founded on a river delta, destroyed in 1945, rebuilt in 1958, with survivors in the grounds.")
faqs=[
("Is Hiroshima Castle original?","No. Wikipedia and a Ministry of Land, Infrastructure, Transport and Tourism (MLIT) multilingual sign database both say the original keep was destroyed in the atomic bombing of 6 August 1945, and that the present keep was completed in 1958. Wikipedia and MLIT call it a concrete replica, while GLTJP says the top floor is wood and the lower floors are reinforced concrete. The stone walls, moat and a few trees are what remain from before the bomb."),
("What happened to the castle on 6 August 1945?","Troops were stationed at the castle at the end of the war, and MLIT says the atomic bomb leveled it, probably because the blast destroyed the lower pillars and the rest collapsed. Wikipedia says it was long believed the whole tower was blown away, and that evidence from 2010 points to the same collapse. Please treat the exact mechanism as something historians still discuss."),
("How much does it cost, and when is it open?","GLTJP gives 370 yen for adults, 180 yen for ages 65 and over and high school students, and free for junior high students and younger. Japan Experience gives 360 yen. GLTJP lists 9:00 to 18:00 from March to November (last entry 17:30) and 9:00 to 17:00 from December to February (last entry 16:30), closed 29 to 31 December. Please confirm on the official site, https://www.rijo-castle.jp/."),
("Is the Ninomaru free?","GLTJP says the Ninomaru, the outer enclosure with the rebuilt gate and turrets, is free. It lists 9:00 to 17:30 from April to September (last entry 17:00) and 9:00 to 16:30 from October to March (last entry 16:00), closed 29 December to 2 January. Confirm the hours on site or on the official page."),
("How do I get there from Hiroshima Station?","GLTJP says to take Hiroshima Electric Railway line 1, 2 or 6 to Kamiyacho-higashi or Kamiyacho-nishi and walk about 15 minutes, or to take a bus from the south exit and walk about 8 minutes. It gives about 25 minutes on foot from the station. Japan Experience gives Kamiyacho as the nearest tram stop."),
("Can I combine it with the Peace Memorial Park?","Yes. Japan Experience places the castle west of Hiroshima Station, with Shukkeien Garden about 10 minutes on foot to the east, and the Peace Museum and Atomic Bomb Dome to the south in Peace Park. I would treat the park as a visit of its own, and the castle as the older layer of the city\'s story."),
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
      <li><a href="#opening">A Castle Before the City</a></li>
      <li><a href="#history">Mori, Fukushima and Asano</a></li>
      <li><a href="#bomb">6 August 1945</a></li>
      <li><a href="#keep">The 1958 Keep</a></li>
      <li><a href="#grounds">Ninomaru, Moat and Survivors</a></li>
      <li><a href="#visit">Visiting Hiroshima Castle</a></li>
      <li><a href="#stay">Making It a Trip</a></li>
      <li><a href="#faq">Frequently Asked Questions</a></li>
      <li><a href="#final">The Older Layer of the City</a></li>
    </ol>
  </aside>

  <article>

    <section id="opening">
      <p class="opening">As a licensed guide, I tell visitors that Hiroshima Castle is where the city started. Before there was a Hiroshima, there was a lord, a river delta and a castle on flat ground, and the town grew around it. Most people come to this city for the Peace Memorial Park, which is right, and the castle is the quieter part of the same story, with a keep that was rebuilt in 1958 after the bomb.</p>
      <p>This guide covers who built the castle, who held it, what is known about 6 August 1945, what you can actually see now, and the practical details. Where my sources disagree, I say so.</p>
    </section>

    <h2 id="history">Mori, Fukushima and Asano<span class="h2-jp">築城と城主</span></h2>
    <p>Mori Terumoto built the castle on flat land in the delta of the Ota River. The sources give different dates for the start, from 1588 (GLTJP) to 1589 (MLIT and Wikipedia) and 1590 (Japan Experience), and they agree it was finished in 1599. GLTJP says Terumoto moved here from a mountain stronghold. Wikipedia and MLIT give the castle the nickname Rijo, the Carp Castle, and MLIT says it became the base for the growth of Hiroshima.</p>
    <p>After Sekigahara in 1600, Terumoto lost the castle. Wikipedia says Fukushima Masanori held it from 1600 to 1619, and Japan Experience says he lost it after failing to report repairs made following a flood in 1619. The Asano family then governed from here, starting with Asano Nagaakira, until the end of Tokugawa rule, which MLIT counts as twelve generations. Japan Experience adds that the Mori moved to Hagi.</p>
    <p>In the Meiji period the castle became a military facility. Wikipedia says the Imperial General Headquarters was based here during the First Sino-Japanese War of 1894 to 1895. Wikipedia and MLIT both say the original keep was designated a National Treasure in 1931.</p>
    <p>One figure is worth a caution. GLTJP says the castle had 88 turrets, which it describes as the highest number in Japan. I found that in one source only, so treat it as a claim to check.</p>

    <h2 id="bomb">6 August 1945<span class="h2-jp">原爆</span></h2>
    <p>MLIT says troops were stationed at the castle near the end of the war, and that the atomic bomb leveled it on 6 August 1945, probably because the blast destroyed the lower pillars and the rest of the structure collapsed. Wikipedia says it was long believed that the whole tower was blown away, and that evidence from 2010 points to the collapse instead. I would present the cause as the best current reading, not as settled.</p>
    <p>Hiroshima is a city where visitors come for this history, and I think the castle works best when you see it as one layer of it. The Peace Memorial Park is the place for the bombing itself, and I would not try to make the castle carry that weight.</p>

    <h2 id="keep">The 1958 Keep<span class="h2-jp">再建天守</span></h2>
    <p>The present keep was completed in 1958. Wikipedia and MLIT call it a concrete replica of the original wooden keep, while GLTJP says it has a wooden top floor and reinforced concrete lower floors. Wikipedia says it is five stories, 26.6 meters above a 12.4 meter stone base, and GLTJP gives about 40 meters including the base and the shachihoko.</p>
    <p>Inside it is a history museum. GLTJP describes the layout floor by floor: the first floor has exhibits on the castle structure, a hands-on area and a shop, the second floor covers daily life and culture with restored folding screens, the third has armor and swords, the fourth has main keep exhibits and special exhibitions, and the fifth is an observation room with views of the city. Exhibits change, so check what is on when you go.</p>

    <h2 id="grounds">Ninomaru, Moat and Survivors<span class="h2-jp">二の丸と被爆樹木</span></h2>
    <p>Wikipedia says the castle had three concentric moats, and that the two outer ones were filled in during the late 19th and early 20th centuries. Japan Experience says only the inner moat survives. Inside it stands the Hiroshima Gokoku Shrine, which Wikipedia says was moved there after 1945.</p>
    <p>GLTJP describes the Ninomaru as an outpost guarding the Naka Gomon gate, with military buildings rather than a palace: the Omote Gomon gate, a Hira Yagura, a long Tamon Yagura of 68 meters, a Taiko Yagura, a guardhouse, a stable and a well. It says everything but the stone walls was lost in 1945 and that restoration ran from 1989 to 1994, with the gate rebuilt in 1991. Wikipedia says a gate and three turrets were rebuilt in wood in 1994. The same source puts the stone walls of the Honmaru and Ninomaru at 31,781 stones, with 214 carved marks confirmed on the north side, which is a single-source figure.</p>
    <p>Some things are older than the keep you see. Wikipedia says a concrete bunker in the Honmaru was used for the first radio broadcast after the bombing, and it lists a eucalyptus and a willow about 740 meters from the hypocenter and a holly about 935 meters away that survived. GLTJP counts four such trees at the castle and gives slightly different distances, 740 meters for the eucalyptus, 770 for the willow and 910 for two hollies, while MLIT says three trees survived. I would read the numbers as approximate and the trees as real.</p>

    <h2 id="visit">Visiting Hiroshima Castle<span class="h2-jp">アクセス</span></h2>
    <ul class="practical-list"><li><strong>Admission:</strong> About 370 yen for adults (GLTJP), or 360 yen (Japan Experience). GLTJP gives 180 yen for ages 65 and over and high school students, and free for junior high students and younger. Please confirm on the official site.</li><li><strong>Hours (keep):</strong> 9:00 to 18:00 from March to November, last entry 17:30, and 9:00 to 17:00 from December to February, last entry 16:30 (GLTJP). Hours may change by season and for events.</li><li><strong>Closed:</strong> 29 to 31 December (GLTJP).</li><li><strong>Ninomaru:</strong> Free (GLTJP). 9:00 to 17:30 from April to September and 9:00 to 16:30 from October to March, closed 29 December to 2 January.</li><li><strong>Getting there:</strong> Tram line 1, 2 or 6 to Kamiyacho-higashi or Kamiyacho-nishi, then about 15 minutes on foot, or a bus from the south exit of Hiroshima Station and about 8 minutes on foot. About 25 minutes on foot from the station (GLTJP).</li><li><strong>Nearby:</strong> Shukkeien Garden is about 10 minutes on foot to the east. The Peace Museum and Atomic Bomb Dome are to the south in Peace Park (Japan Experience).</li></ul>

    <h2 id="stay">Making It a Trip<span class="h2-jp">滞在</span></h2>
    <p>GLTJP says the best time for cherry blossoms is late March to early April, with evening lighting on the blossoms and the castle during the season. For another castle that burned in the war and was rebuilt in concrete, see our <a href="/guides/okayama-castle/" class="inline-link" onclick="trackEvent('click','internal','guide_hiroshima_to_okayama')">Okayama Castle guide</a>, and for a white castle that came through intact, our <a href="/guides/himeji-castle/" class="inline-link" onclick="trackEvent('click','internal','guide_hiroshima_to_himeji')">Himeji Castle guide</a>. If you are going on to Miyajima, see our <a href="/guides/itsukushima-shrine/" class="inline-link" onclick="trackEvent('click','internal','guide_hiroshima_to_itsukushima')">Itsukushima Shrine guide</a>.</p>
    <div class="key-callout">
      <p>&#127890; <strong>Plan your trip:</strong> Browse guided tours, or plan a stay in Hiroshima. <a href="https://www.viator.com/search/Hiroshima?pid=P00298374&amp;mcid=42383&amp;medium=link&amp;campaign=sacred-japan" target="_blank" rel="noopener sponsored" onclick="trackEvent('click','affiliate','viator_hiroshima_local')">Browse Hiroshima tours &rarr;</a></p>
    </div>

    <h2 id="faq">Frequently Asked Questions<span class="h2-jp">よくあるご質問</span></h2>
    <div class="faq-stack">
'''+''.join(f'''    <details class="faq-item">
        <summary>{q}</summary>
        <div class="faq-answer">{a}</div>
    </details>
''' for q,a in faqs)+'''    </div>

    <h2 id="final">The Older Layer of the City<span class="h2-jp">むすびに</span></h2>
    <p>Hiroshima Castle is worth an hour or two for the story of how the city began, the Ninomaru turrets, the moat and the few trees that were there in 1945, and not for original rooms. Go knowing the keep is a 1958 rebuild, and spend the rest of the day at the Peace Memorial Park.</p>

    <div class="closing-block">
      <span class="torii">&#9961;&#65039;</span>
      <p>The keep was rebuilt. The city around it remembers.</p>
    </div>

    <!-- RELATED GUIDES -->
    <section class="related-section">
      <h2>Related Guides</h2>
      <span class="h2-jp">関連ガイド</span>

      <div class="related-grid">

        <a class="related-card" href="/guides/okayama-castle/" onclick="trackEvent('click','internal','related_hiroshima_to_okayama')">
          <div class="related-card-label">SACRED JAPAN ／ GUIDES</div>
          <div class="related-card-title">&#127983; Okayama Castle Guide &rarr;</div>
          <div class="related-card-desc">The black castle, also rebuilt after 1945.</div>
        </a>

        <a class="related-card" href="/guides/itsukushima-shrine/" onclick="trackEvent('click','internal','related_hiroshima_to_itsukushima')">
          <div class="related-card-label">SACRED JAPAN ／ GUIDES</div>
          <div class="related-card-title">&#9961;&#65039; Itsukushima Shrine Guide &rarr;</div>
          <div class="related-card-desc">The floating torii on Miyajima, a short trip from the city.</div>
        </a>

        <a class="related-card" href="/castles/" onclick="trackEvent('click','internal','related_hiroshima_to_castles')">
          <div class="related-card-label">SACRED JAPAN ／ CASTLES</div>
          <div class="related-card-title">&#127983; Japan's Castles &rarr;</div>
          <div class="related-card-desc">Every castle guide, with photos and official links.</div>
        </a>

      </div>
    </section>

  </article>

'''
tail=tail.replace('kochi-castle',SL).replace('_kochi_','_hiroshima_')
def L(u,l,t): return f'<a href="{u}" target="_blank" rel="noopener" style="color:var(--beni);text-decoration:underline;" onclick="trackEvent(\'click\',\'external\',\'{l}\')">{t}</a>'
src='Sources verified at time of writing: '+', '.join([
 L('https://www.gltjp.com/en/article/item/20344/','src_hiroshima_gltjp','GLTJP'),
 L('https://en.wikipedia.org/wiki/Hiroshima_Castle','src_hiroshima_wikipedia','Wikipedia'),
 L('https://www.mlit.go.jp/tagengo-db/common/001560954.pdf','src_hiroshima_mlit','MLIT multilingual sign database'),
 L('https://www.japan-experience.com/all-about-japan/hiroshima/attractions-excursions/hiroshima-castle','src_hiroshima_jexp','Japan Experience'),
])+'. Hours, prices and availability change'
tail,n=re.subn(r'Sources verified at time of writing:.*?Hours, prices and availability change',lambda m:src,tail,flags=re.S); assert n==1
tail=tail.replace('destination%3DHiroshima','destination%3DHiroshima').replace('search/Hiroshima','search/Hiroshima')
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
l2="x"; assert d.textlength(l2,font=f1)<1090
d.text((66,170),"Hiroshima Castle Guide:",font=f1,fill=(26,15,15)); d.text((66,238),l2,font=f1,fill=(26,15,15)); d.text((66,332),"広島城",font=f2,fill=(138,125,120))
im.save(R+f'images/og/og-guides-{SL}.jpg',quality=88); print('built',len(out))
