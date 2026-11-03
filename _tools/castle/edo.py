import re,json,os,glob
from PIL import Image,ImageDraw,ImageFont
R='/home/claude/sacred-japan/'; SL='edo-castle'
s=open(R+'guides/kochi-castle/index.html',encoding='utf-8').read()
i=s.index('<main>'); j=s.index('</main>'); head,tail=s[:i],s[j:]
TITLE="Edo Castle Guide: A Missing Keep, Free Ruins and the East Gardens Today"
DESC="A licensed guide's guide to Edo Castle in Tokyo: the keep that burned in 1657 and was never rebuilt, the Pine Corridor, what survives in the Imperial Palace East Gardens, and how to visit for free."
head=re.sub(r'<title>.*?</title>',f'<title>{TITLE} | Sacred Japan</title>',head,count=1)
head=re.sub(r'(<meta (?:name="description"|property="og:description"|name="twitter:description") content=")[^"]*(")',lambda m:m.group(1)+DESC+m.group(2),head)
head=re.sub(r'(<meta (?:property="og:title"|name="twitter:title") content=")[^"]*(")',lambda m:m.group(1)+TITLE+m.group(2),head)
head=re.sub(r'("headline": ")[^"]*(")',lambda m:m.group(1)+TITLE+m.group(2),head)
head=re.sub(r'("description": ")A licensed[^"]*(")',lambda m:m.group(1)+DESC+m.group(2),head)
head=re.sub(r'<meta name="keywords" content="[^"]*">','<meta name="keywords" content="Edo Castle, Edo Castle guide, Edo Castle ruins, Edo Castle keep, Imperial Palace East Gardens, Imperial Palace East Garden hours, Tokyo castle, Edo Castle tenshudai, Matsu no Oroka, Edo Castle history, Tokyo free attraction">',head)
head=head.replace('guides/kochi-castle','guides/edo-castle').replace('guide_kochi_','guide_edo_').replace('og-guides-kochi-castle','og-guides-edo-castle')
head=head.replace('高知城','江戸城').replace('Kochi Castle','Edo Castle')
head=re.sub(r"<h1>.*?</h1>","<h1><em>Edo Castle</em>: A Missing Keep, Free Ruins and the East Gardens Today</h1>",head,count=1,flags=re.S)
head=head.replace("Shikoku's original keep, and the only castle where the lord's palace still stands beside it.","The shoguns' castle in the middle of Tokyo, with no keep left, but its foundations, gates and walls free to walk.")
faqs=[
("Is Edo Castle still standing?","Not as a whole. Japan-guide says no main buildings remain in the innermost circles, only the moats, walls, entrance gates and several guardhouses. Wikipedia lists a few surviving structures, including Fujimi-yagura, a three-story turret. The Imperial Palace East Gardens now occupy the former Honmaru, Ninomaru and Sannomaru, according to GLTJP."),
("Can I visit Edo Castle, and does it cost anything?","Yes. The Imperial Palace East Gardens, which cover the old Honmaru, Ninomaru and Sannomaru, are free, according to GLTJP and Japan-guide. Visitors take an admission slip at the gate and return it on the way out. The gates are Otemon, Hirakawamon and Kitahanebashimon."),
("When is it open and when is it closed?","GLTJP and Japan-guide agree on hours that change by season: 9:00 to 18:00 from mid-April to August, 9:00 to 17:00 in March to mid-April and September, 9:00 to 16:30 in October and 9:00 to 16:00 from November to February, with last entry 30 minutes earlier. Both say it is closed on Mondays and Fridays and from 28 December to 3 January. One Japanese guide I read gave slightly different hours, so check the Imperial Household Agency's calendar before you go."),
("Where is the keep?","There is none. Japan-guide says the keep, finished in 1638, was destroyed by fire in 1657 and has not been rebuilt. What remains is the stone base, the tenshudai, with a lawn where the tower stood. The Japanese government's multilingual sign database says work on a new keep stopped after the shogun's uncle argued that a peaceful Japan no longer needed such a giant structure."),
("How long should I allow?","One Japanese guide, Jeepe, suggests about 60 minutes for the entrance gates, guardhouses and keep base, and about 90 minutes if you add the Ninomaru Garden. I would allow two hours if you like stonework."),
("How do I get there?","GLTJP says it is about a five-minute walk from Otemachi Station, and Japan-guide gives a 10 to 15 minute walk from Tokyo Station to the Otemon entrance. Jeepe lists the Otemachi C13a exit. The exact time depends on the gate and your pace."),
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
      <li><a href="#opening">A Castle With Nothing to Climb</a></li>
      <li><a href="#history">From Ota Dokan to the Shogun</a></li>
      <li><a href="#keep">The Keep That Was Never Rebuilt</a></li>
      <li><a href="#corridor">The Pine Corridor</a></li>
      <li><a href="#survives">What Survives Today</a></li>
      <li><a href="#visit">Visiting the East Gardens</a></li>
      <li><a href="#stay">Making It a Trip</a></li>
      <li><a href="#faq">Frequently Asked Questions</a></li>
      <li><a href="#final">A Castle You Read, Not Climb</a></li>
    </ol>
  </aside>

  <article>

    <section id="opening">
      <p class="opening">As a licensed guide, I tell people that Edo Castle is the biggest castle in Japan that most visitors never realize they have seen. The stone moats around Tokyo Station, the bridge in front of the palace and the lawns inside the gates all belong to it. There is no keep to climb, because it burned in 1657 and was never rebuilt. What you get instead is free, quiet and full of foundations you can stand on.</p>
      <p>This guide covers how the castle grew, why its keep never came back, the corridor where a famous attack took place, what survives, and the practical details, including hours that change by season. Where my sources disagree, I say so.</p>
    </section>

    <h2 id="history">From Ota Dokan to the Shogun<span class="h2-jp">築城</span></h2>
    <p>Wikipedia says Ota Dokan first built a castle here in 1457. In 1590, after the siege of Odawara, the site passed to Tokugawa Ieyasu, who later made it his base. Ieyasu received the title of shogun in 1603, and Wikipedia says most of the construction ran from 1593 to 1636, finishing under Tokugawa Iemitsu. Japan-guide says the Tokugawa shoguns ruled from the castle from 1603 to 1867.</p>
    <p>The scale was huge. Wikipedia gives a perimeter of about 16 kilometers, ramparts nearly 20 meters high, and a Honmaru ringed by 11 turrets, 15 defense houses and more than 20 gates, though it also notes that estimates of the circumference vary. Few castles in Japan were designed so clearly as a government.</p>
    <p>The end came with the shogunate. Wikipedia says the compound was renamed Tokyo Castle in 1868 and the Imperial Castle in 1869, and that a fire in 1873 consumed most of what was left of the old castle. Japan-guide says Emperor Meiji lived here from 1868 to 1888, and Wikipedia says a new palace was built in 1888.</p>

    <h2 id="keep">The Keep That Was Never Rebuilt<span class="h2-jp">天守台</span></h2>
    <p>Japan-guide says the keep was completed in 1638 and was the tallest castle tower in Japan's history. Wikipedia describes it as five stories, about 51 meters. The Meireki fire of 1657 destroyed it. The base was rebuilt by the shogun Tokugawa Ietsuna, according to the Japanese government's multilingual sign database, but the tower on top was not. That source says construction stopped after Ietsuna's uncle argued that a peaceful Japan no longer needed such an enormous symbol of power.</p>
    <p>The base still stands, and it is the most interesting place in the gardens. It is a large stone platform with a lawn on top, and you can walk up onto it. The two sources give slightly different sizes: Wikipedia says about 41 by 45 meters and 11 meters high, while the sign database says 42 by 46 meters and 10 meters high. Either way, standing on it you can feel how large the tower must have been, even with nothing on it.</p>

    <h2 id="corridor">The Pine Corridor<span class="h2-jp">松の大廊下</span></h2>
    <p>The Honmaru Palace once stood where the East Gardens lawns are now, and one corridor in it became famous. The sign database says the Matsu no Oroka, about 55 meters long and 4 meters wide, led to the shogun's reception room and was named for the pines painted on its sliding doors. In 1701, it says, Asano, lord of Ako, attacked and wounded Kira, a court master of ceremonies, there, and Asano was ordered to commit suicide.</p>
    <p>In 1702 Asano's 47 masterless retainers took revenge by killing Kira, and the shogunate, divided on how to treat them, ordered them to commit seppuku rather than be executed. The story became Chushingura, the basis of countless kabuki plays and films. If you know the 47 Ronin, this is where it begins.</p>

    <h2 id="survives">What Survives Today<span class="h2-jp">現存する遺構</span></h2>
    <p>GLTJP says the East Gardens sit on parts of the old Honmaru, Ninomaru and Sannomaru and keep the tenshudai, three guardhouses and Fujimi-yagura. Wikipedia lists the surviving structures as Fujimi-yagura, a three-story turret, Fushimi-yagura, Tatsumi-yagura and Fujimi-tamon, along with Hanzo-mon and Nijubashi. Some of these may lie outside the gardens, so I would not promise to see them all on one visit.</p>
    <p>Japan-guide adds that a Japanese-style garden has been made in the former Ninomaru, at the foot of the hill. It is a good place to sit after the stone, and Jeepe describes it with ponds and mixed woodland.</p>

    <h2 id="visit">Visiting the East Gardens<span class="h2-jp">アクセス</span></h2>
    <ul class="practical-list"><li><strong>Admission:</strong> Free (GLTJP, Japan-guide). Take an admission slip at the gate and hand it back on your way out. The gates are Otemon, Hirakawamon and Kitahanebashimon.</li><li><strong>Hours:</strong> 9:00 to 18:00 from mid-April to August, 9:00 to 17:00 in March to mid-April and September, 9:00 to 16:30 in October, 9:00 to 16:00 from November to February. Last entry is 30 minutes before closing (GLTJP, Japan-guide). One Japanese guide gives slightly different hours, so confirm with the Imperial Household Agency.</li><li><strong>Closed:</strong> Mondays and Fridays, and 28 December to 3 January. The holiday rules are described a little differently by each source, so check the official calendar, as events also cause closures.</li><li><strong>Getting there:</strong> About five minutes on foot from Otemachi Station (GLTJP), or 10 to 15 minutes from Tokyo Station (Japan-guide).</li><li><strong>Time to allow:</strong> About 60 to 90 minutes for the gates, keep base and garden (Jeepe), and two hours if you linger.</li></ul>

    <h2 id="stay">Making It a Trip<span class="h2-jp">滞在</span></h2>
    <p>If you want a castle with a keep you can climb, our <a href="/guides/osaka-castle/" class="inline-link" onclick="trackEvent('click','internal','guide_edo_to_osaka')">Osaka Castle guide</a> and <a href="/guides/nagoya-castle/" class="inline-link" onclick="trackEvent('click','internal','guide_edo_to_nagoya')">Nagoya Castle guide</a> are the natural next steps, and the Shinkansen from Tokyo Station reaches both.</p>
    <div class="key-callout">
      <p>&#127890; <strong>Plan your trip:</strong> Browse guided tours, or plan a stay in Tokyo. <a href="https://www.viator.com/search/Tokyo?pid=P00298374&amp;mcid=42383&amp;medium=link&amp;campaign=sacred-japan" target="_blank" rel="noopener sponsored" onclick="trackEvent('click','affiliate','viator_edo_local')">Browse Tokyo tours &rarr;</a></p>
    </div>

    <h2 id="faq">Frequently Asked Questions<span class="h2-jp">よくあるご質問</span></h2>
    <div class="faq-stack">
'''+''.join(f'''    <details class="faq-item">
        <summary>{q}</summary>
        <div class="faq-answer">{a}</div>
    </details>
''' for q,a in faqs)+'''    </div>

    <h2 id="final">A Castle You Read, Not Climb<span class="h2-jp">むすびに</span></h2>
    <p>Edo Castle asks you to bring a little imagination. The tower is gone, the palace is gone, but the stone base, the gates and the corridor's site are still there, and they cost nothing. Go on a clear day, climb the keep base, and look at the lawn the way the shoguns saw it.</p>

    <div class="closing-block">
      <span class="torii">&#9961;&#65039;</span>
      <p>The tower is gone. The stones remember.</p>
    </div>

    <!-- RELATED GUIDES -->
    <section class="related-section">
      <h2>Related Guides</h2>
      <span class="h2-jp">関連ガイド</span>

      <div class="related-grid">

        <a class="related-card" href="/guides/osaka-castle/" onclick="trackEvent('click','internal','related_edo_to_osaka')">
          <div class="related-card-label">SACRED JAPAN ／ GUIDES</div>
          <div class="related-card-title">&#127983; Osaka Castle Guide &rarr;</div>
          <div class="related-card-desc">A keep built three times, and the walls beneath it.</div>
        </a>

        <a class="related-card" href="/guides/nagoya-castle/" onclick="trackEvent('click','internal','related_edo_to_nagoya')">
          <div class="related-card-label">SACRED JAPAN ／ GUIDES</div>
          <div class="related-card-title">&#127983; Nagoya Castle Guide &rarr;</div>
          <div class="related-card-desc">Golden shachi, a rebuilt palace and a keep that is closed.</div>
        </a>

        <a class="related-card" href="/castles/" onclick="trackEvent('click','internal','related_edo_to_castles')">
          <div class="related-card-label">SACRED JAPAN ／ CASTLES</div>
          <div class="related-card-title">&#127983; Japan's Castles &rarr;</div>
          <div class="related-card-desc">Every castle guide, with photos and official links.</div>
        </a>

      </div>
    </section>

  </article>

'''
tail=tail.replace('kochi-castle',SL).replace('_kochi_','_edo_')
def L(u,l,t): return f'<a href="{u}" target="_blank" rel="noopener" style="color:var(--beni);text-decoration:underline;" onclick="trackEvent(\'click\',\'external\',\'{l}\')">{t}</a>'
src='Sources verified at time of writing: '+', '.join([
 L('https://www.gltjp.com/en/directory/item/18846/','src_edo_gltjp','GLTJP'),
 L('https://japan-guide.com/e/e3018.html','src_edo_japanguide','Japan-guide'),
 L('https://en.wikipedia.org/wiki/Edo_Castle','src_edo_wikipedia','Wikipedia'),
 L('https://www.mlit.go.jp/tagengo-db/en/H30-00468.html','src_edo_mlit_keep','MLIT sign database (keep base)'),
 L('https://www.mlit.go.jp/tagengo-db/en/H30-00472.html','src_edo_mlit_corridor','MLIT sign database (Pine Corridor)'),
 L('https://www.jeepe.jp/ja/articles/tokyo-imperial-palace-1048','src_edo_jeepe','Jeepe'),
])+'. Hours, prices and availability change'
tail,n=re.subn(r'Sources verified at time of writing:.*?Hours, prices and availability change',lambda m:src,tail,flags=re.S); assert n==1
tail=tail.replace('destination%3DKochi','destination%3DTokyo').replace('search/Kochi','search/Tokyo')
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
l2="A Missing Keep, Free Ruins"; assert d.textlength(l2,font=f1)<1090
d.text((66,170),"Edo Castle Guide:",font=f1,fill=(26,15,15)); d.text((66,238),l2,font=f1,fill=(26,15,15)); d.text((66,332),"江戸城",font=f2,fill=(138,125,120))
im.save(R+f'images/og/og-guides-{SL}.jpg',quality=88); print('built',len(out))
