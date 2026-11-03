import re,json,os,glob
from PIL import Image,ImageDraw,ImageFont
R='/home/claude/sacred-japan/'; SL='nagoya-castle'
s=open(R+'guides/kochi-castle/index.html',encoding='utf-8').read()
i=s.index('<main>'); j=s.index('</main>'); head,tail=s[:i],s[j:]
TITLE="Nagoya Castle Guide: Golden Shachi, a Rebuilt Palace and a Keep That Is Closed"
DESC="A licensed guide's guide to Nagoya Castle: Ieyasu's showpiece, the golden shachi, the rebuilt Honmaru Palace, why the keep has been closed since 2018, and how to visit today."
head=re.sub(r'<title>.*?</title>',f'<title>{TITLE} | Sacred Japan</title>',head,count=1)
head=re.sub(r'(<meta (?:name="description"|property="og:description"|name="twitter:description") content=")[^"]*(")',lambda m:m.group(1)+DESC+m.group(2),head)
head=re.sub(r'(<meta (?:property="og:title"|name="twitter:title") content=")[^"]*(")',lambda m:m.group(1)+TITLE+m.group(2),head)
head=re.sub(r'("headline": ")[^"]*(")',lambda m:m.group(1)+TITLE+m.group(2),head)
head=re.sub(r'("description": ")A licensed[^"]*(")',lambda m:m.group(1)+DESC+m.group(2),head)
head=re.sub(r'<meta name="keywords" content="[^"]*">','<meta name="keywords" content="Nagoya Castle, Nagoya Castle guide, Nagoya Castle history, Nagoya Castle hours, Nagoya Castle tickets, Nagoya Castle keep closed, Nagoya Castle Honmaru Palace, Nagoya Castle golden shachi, Nagoya Castle cherry blossoms, Tokugawa Ieyasu castle, Nagoya Castle how to visit">',head)
head=head.replace('guides/kochi-castle','guides/nagoya-castle').replace('guide_kochi_','guide_nagoya_').replace('og-guides-kochi-castle','og-guides-nagoya-castle')
head=head.replace('高知城','名古屋城').replace('Kochi Castle','Nagoya Castle')
head=re.sub(r"<h1>.*?</h1>","<h1><em>Nagoya Castle</em>: Golden Shachi, a Rebuilt Palace and a Keep That Is Closed</h1>",head,count=1,flags=re.S)
head=head.replace("Shikoku's original keep, and the only castle where the lord's palace still stands beside it.","Ieyasu's showpiece castle, with its golden shachi, a rebuilt palace and a keep that has been closed since 2018.")
faqs=[
("Can I go inside Nagoya Castle's main keep?","No, not at the moment. GLTJP and Japan-guide say the keep has been closed since May 2018 because of earthquake-resistance and ageing concerns. The plan is to rebuild it in wood. GLTJP gives fiscal 2032 as the target for completion, while Japan-guide says only that it will not be before 2032 and that no firm schedule exists, so treat any date as uncertain and check the official site before you travel. You can still walk the grounds and enter the Honmaru Palace."),
("How much does Nagoya Castle cost and when is it open?","GLTJP, Japan-guide and Watabi agree that admission rose to 1,000 yen for adults from 1 October 2026, up from 500 yen, with junior high students and younger free. GLTJP gives 9:00 to 16:30, with the Honmaru Palace closing a little earlier at 16:00, and closure from 29 December to 1 January. I could not confirm the fee on the official fee page, so check it before you go."),
("What is there to see if the keep is closed?","The main draw is the Honmaru Palace, reconstructed between 2009 and 2018 in shoin style with more than thirty rooms, and open in full since June 2018. The walls, the moats, the surviving corner turrets seen from outside and the Ninomaru Garden are all on the grounds. Watabi's advice is blunt: if climbing a keep is the point of your trip, Osaka Castle is the better choice for now."),
("How do I get to Nagoya Castle?","GLTJP says to take the Meijo subway line to Nagoya-jo station and leave by exit 7, about a five-minute walk. The station was renamed in January 2023; older maps may still say Shiyakusho (City Hall). The Meguru tourist loop bus also stops here, costs 210 yen per ride or 500 yen for a day pass, and does not run on Mondays."),
("When is the best time to visit?","GLTJP counts about 1,000 cherry trees of ten varieties on the grounds and gives late March to late April for the cherry blossom festival, which is when I would go. The palace interior is a good rainy-day plan, since much of it is indoors."),
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
      <li><a href="#opening">A Castle You Can Visit, Without Its Keep</a></li>
      <li><a href="#history">Ieyasu's Showpiece</a></li>
      <li><a href="#shachi">The Golden Shachi</a></li>
      <li><a href="#war">1945 and the Concrete Keep</a></li>
      <li><a href="#palace">The Honmaru Palace</a></li>
      <li><a href="#grounds">Walls, Turrets and the Ninomaru Garden</a></li>
      <li><a href="#visit">Visiting Nagoya Castle</a></li>
      <li><a href="#stay">Making It a Trip</a></li>
      <li><a href="#faq">Frequently Asked Questions</a></li>
      <li><a href="#final">The Keep Is Closed. The Castle Is Not.</a></li>
    </ol>
  </aside>

  <article>

    <section id="opening">
      <p class="opening">As a licensed guide, I have to start a Nagoya Castle visit with a warning: you cannot go up the main keep. It has been shut since May 2018, and the golden shachi on its roof are for looking at from the ground. That sounds like a reason to skip it. I think it is the opposite, because the castle's best rooms are now at ground level, in a palace that was rebuilt over ten years and opened in full in 2018.</p>
      <p>This guide covers how the castle began, the golden shachi, what the 1945 air raid took and what came back, the Honmaru Palace, the walls and gardens, and the practical details, including the new ticket price. Where my sources disagree, I say so.</p>
    </section>

    <h2 id="history">Ieyasu's Showpiece<span class="h2-jp">築城</span></h2>
    <p>Wikipedia says Tokugawa Ieyasu decided to build the castle in 1609 and 1610, and that work began in January 1610. It was a national project: about twenty daimyo were ordered to supply labour and stone, including Kato Kiyomasa, Fukushima Masanori and Maeda Toshimitsu. Wikipedia names Nakai Masakiyo as the works commissioner. Many of the stones still carry the marks of the families that supplied them, and the largest block is known as the Kiyomasa Stone.</p>
    <p>The keep was finished in December 1612 and the Honmaru Palace in February 1615, with the Ninomaru Palace following in 1617, according to Wikipedia's account of the construction. The castle later belonged to the Owari branch of the Tokugawa family, the line that ruled this region.</p>
    <p>After the Meiji Restoration the castle changed hands. Wikipedia says the Imperial Household Ministry took it over in 1893 and renamed it the Nagoya Detached Palace, and that it was given to the city in December 1930. Wikipedia adds that twenty-four structures were designated national treasures that same year, which matters for what happened next.</p>

    <h2 id="shachi">The Golden Shachi<span class="h2-jp">金の鯱</span></h2>
    <p>The pair of golden shachi, mythical fish with a tiger's head, is what the whole city associates with the castle. The official site and Wikipedia give the male, on the north end of the roof, as 2.621 meters tall and 1,272 kilograms, using 44.69 kilograms of gold. The female, on the south end, is 2.579 meters and 1,215 kilograms, with 43.39 kilograms of gold.</p>
    <p>The earlier pairs did not all survive. Wikipedia says the government took the shachi in 1871, and the pair that stood on the roof was lost when the keep burned in 1945. The current pair went up on the rebuilt keep in 1959. Wikipedia says they were shown at the 2005 Expo and then returned to the roof. For years I have told guests that they can read the castle's whole history in those two animals, since they have been melted down, taken by the state, burned and replaced.</p>

    <h2 id="war">1945 and the Concrete Keep<span class="h2-jp">戦災と再建</span></h2>
    <p>Wikipedia says the air raid of 14 May 1945 burned the keep, the Honmaru Palace and other buildings that had been designated national treasures only fifteen years earlier. The site was made a Special Historic Site in 1952. The keep you see now is a steel-reinforced concrete reconstruction that reopened on 3 October 1959, and it is the building that has been closed since 2018.</p>
    <p>GLTJP and Japan-guide say the closure is for seismic safety and age, and that the city plans a wooden reconstruction. GLTJP gives fiscal 2032 as the target, while Japan-guide says it will come after 2032 with no fixed schedule. The official site, as far as I could see, only says that the keep is closed. I would not plan a trip around a reopening date.</p>

    <h2 id="palace">The Honmaru Palace<span class="h2-jp">本丸御殿</span></h2>
    <p>This is the reason to come now. According to GLTJP and Wikipedia, the Honmaru Palace was reconstructed from 2009 to 2018, over about ten years and roughly 15 billion yen, and opened to visitors in full in June 2018. It has more than thirty rooms in the shoin style, the formal residential style of the warrior class. Photography is allowed inside, with no flash or tripod.</p>
    <p>I tell visitors to go slowly through the rooms and look at the thresholds between them, because the rank of the people a room was built for shows in how much gold and detail is on its walls. It is not a museum in the usual sense. It feels closer to walking through a building that has just been finished, which in fact it has.</p>

    <h2 id="grounds">Walls, Turrets and the Ninomaru Garden<span class="h2-jp">石垣と庭園</span></h2>
    <p>Wikipedia says three of the original corner turrets survive, in the southwest, southeast and northwest, while the northeast turret was lost in the war. The guides I checked describe the surviving ones as normally closed to visitors, so plan to see them from outside, from the moat side.</p>
    <p>The Ninomaru Garden, which Wikipedia says was designated a place of scenic beauty in 1953 and enlarged in 2018, is a quiet counterweight to the palace. GLTJP counts about 1,000 cherry trees of ten varieties across the grounds, and the cherry blossom festival runs from late March to late April.</p>

    <h2 id="visit">Visiting Nagoya Castle<span class="h2-jp">アクセス</span></h2>
    <ul class="practical-list"><li><strong>Getting there:</strong> Take the Meijo subway line to Nagoya-jo station and use exit 7, about five minutes on foot (GLTJP). The station was renamed in January 2023 and older maps may still show Shiyakusho. The Meguru tourist loop bus stops here, costs 210 yen per ride or 500 yen for a day, and does not run on Mondays.</li><li><strong>Tickets:</strong> 1,000 yen for adults from 1 October 2026, previously 500 yen, with junior high students and younger free (GLTJP, Japan-guide and Watabi agree). I could not confirm this on the official fee page, so check before you go.</li><li><strong>Hours:</strong> 9:00 to 16:30, with the Honmaru Palace closing at 16:00, and closed from 29 December to 1 January (GLTJP).</li><li><strong>The keep:</strong> Closed to visitors since May 2018. Check the official Nagoya Castle site for the latest.</li><li><strong>Time to allow:</strong> Most of a morning if you take the palace slowly and walk the garden.</li></ul>

    <h2 id="stay">Making It a Trip<span class="h2-jp">滞在</span></h2>
    <p>If you want to climb a keep on the same trip, our guides to <a href="/guides/inuyama-castle/" class="inline-link" onclick="trackEvent('click','internal','guide_nagoya_to_inuyama')">Inuyama Castle</a>, a short ride north in Aichi, and <a href="/guides/osaka-castle/" class="inline-link" onclick="trackEvent('click','internal','guide_nagoya_to_osaka')">Osaka Castle</a> are the natural next steps.</p>
    <div class="key-callout">
      <p>&#127890; <strong>Plan your trip:</strong> Browse guided tours, or plan a stay in Nagoya. <a href="https://www.viator.com/search/Nagoya?pid=P00298374&amp;mcid=42383&amp;medium=link&amp;campaign=sacred-japan" target="_blank" rel="noopener sponsored" onclick="trackEvent('click','affiliate','viator_nagoya_local')">Browse Nagoya tours &rarr;</a></p>
    </div>

    <h2 id="faq">Frequently Asked Questions<span class="h2-jp">よくあるご質問</span></h2>
    <div class="faq-stack">
'''+''.join(f'''    <details class="faq-item">
        <summary>{q}</summary>
        <div class="faq-answer">{a}</div>
    </details>
''' for q,a in faqs)+'''    </div>

    <h2 id="final">The Keep Is Closed. The Castle Is Not.<span class="h2-jp">むすびに</span></h2>
    <p>Nagoya Castle is in an in-between moment: the keep waits for its wooden rebuild, while the palace beside it is as complete as it has been in eighty years. Go for the palace, look up at the gold, and come back when the tower reopens.</p>

    <div class="closing-block">
      <span class="torii">&#9961;&#65039;</span>
      <p>The tower is waiting. The palace is ready.</p>
    </div>

    <!-- RELATED GUIDES -->
    <section class="related-section">
      <h2>Related Guides</h2>
      <span class="h2-jp">関連ガイド</span>

      <div class="related-grid">

        <a class="related-card" href="/guides/inuyama-castle/" onclick="trackEvent('click','internal','related_nagoya_to_inuyama')">
          <div class="related-card-label">SACRED JAPAN ／ GUIDES</div>
          <div class="related-card-title">&#127983; Inuyama Castle Guide &rarr;</div>
          <div class="related-card-desc">A keep you can climb, an hour from Nagoya.</div>
        </a>

        <a class="related-card" href="/guides/osaka-castle/" onclick="trackEvent('click','internal','related_nagoya_to_osaka')">
          <div class="related-card-label">SACRED JAPAN ／ GUIDES</div>
          <div class="related-card-title">&#127983; Osaka Castle Guide &rarr;</div>
          <div class="related-card-desc">A keep built three times, and the walls beneath it.</div>
        </a>

        <a class="related-card" href="/castles/" onclick="trackEvent('click','internal','related_nagoya_to_castles')">
          <div class="related-card-label">SACRED JAPAN ／ CASTLES</div>
          <div class="related-card-title">&#127983; Japan's Castles &rarr;</div>
          <div class="related-card-desc">Every castle guide, with photos and official links.</div>
        </a>

      </div>
    </section>

  </article>

'''
tail=tail.replace('kochi-castle',SL).replace('_kochi_','_nagoya_')
def L(u,l,t): return f'<a href="{u}" target="_blank" rel="noopener" style="color:var(--beni);text-decoration:underline;" onclick="trackEvent(\'click\',\'external\',\'{l}\')">{t}</a>'
src='Sources verified at time of writing: '+', '.join([
 L('https://www.gltjp.com/en/article/item/20335/','src_nagoya_gltjp','GLTJP'),
 L('https://www.japan-guide.com/e/e3300.html','src_nagoya_japanguide','Japan-guide'),
 L('https://watabi.org/en/articles/nagoya-castle-guide','src_nagoya_watabi','Watabi'),
 L('https://en.wikipedia.org/wiki/Nagoya_Castle','src_nagoya_wikipedia','Wikipedia'),
])+'. Hours, prices and availability change'
tail,n=re.subn(r'Sources verified at time of writing:.*?Hours, prices and availability change',lambda m:src,tail,flags=re.S); assert n==1
tail=tail.replace('destination%3DKochi','destination%3DNagoya').replace('search/Kochi','search/Nagoya')
out=head+main+tail
assert not re.search('Kochi|Shikoku|kochi|Uwajima|Osaka Castle Guide',re.sub(r'"mainEntity": \[.*','',out,flags=re.S).replace('Osaka Castle','').replace('osaka',''))
os.makedirs(R+f'guides/{SL}',exist_ok=True); open(R+f'guides/{SL}/index.html','w',encoding='utf-8').write(out)
for tg in ['div','figure','picture','p','a','ul','li','details','section','h2']:
    assert len(re.findall(f'<{tg}[ >]',out))==len(re.findall(f'</{tg}>',out)),tg
for m in re.findall(r'<script type="application/ld\+json">(.*?)</script>',out,re.S): json.loads(m)
im=Image.open(R+'images/og/og-guides-matsue-castle.jpg').convert('RGB'); d=ImageDraw.Draw(im)
d.rectangle([40,150,1170,380],fill=(252,240,242))
f1=ImageFont.truetype(glob.glob('/usr/share/fonts/**/DejaVuSerif-Bold.ttf',recursive=True)[0],48)
f2=ImageFont.truetype(glob.glob('/usr/share/fonts/**/NotoSerifCJK-Bold.ttc',recursive=True)[0],28,index=0)
l2="Golden Shachi, Closed Keep"; assert d.textlength(l2,font=f1)<1090
d.text((66,170),"Nagoya Castle Guide:",font=f1,fill=(26,15,15)); d.text((66,238),l2,font=f1,fill=(26,15,15)); d.text((66,332),"名古屋城",font=f2,fill=(138,125,120))
im.save(R+f'images/og/og-guides-{SL}.jpg',quality=88); print('built',len(out))
