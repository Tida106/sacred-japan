import re,json,os,glob
from PIL import Image,ImageDraw,ImageFont
R='/home/claude/sacred-japan/'; SL='goryokaku'
s=open(R+'guides/kochi-castle/index.html',encoding='utf-8').read()
i=s.index('<main>'); j=s.index('</main>'); head,tail=s[:i],s[j:]
TITLE="Goryokaku Guide: Hakodate's Star Fort, the Republic of Ezo and the Last Battle of the Boshin War"
DESC="A licensed guide's guide to Goryokaku in Hakodate: why the fort is a star, the Republic of Ezo and the 1869 battle, the rebuilt Magistrate's Office, the tower, cherry blossoms, winter lights, fees and the tram from the station."
TAG='A star-shaped fort, a short-lived republic and the last battle of the Boshin War, a tram ride from Hakodate Station.'
head=re.sub(r'<title>.*?</title>',f'<title>{TITLE} | Sacred Japan</title>',head,count=1)
head=re.sub(r'(<meta (?:name="description"|property="og:description"|name="twitter:description") content=")[^"]*(")',lambda m:m.group(1)+DESC+m.group(2),head)
head=re.sub(r'(<meta (?:property="og:title"|name="twitter:title") content=")[^"]*(")',lambda m:m.group(1)+TITLE+m.group(2),head)
head=re.sub(r'("headline": ")[^"]*(")',lambda m:m.group(1)+TITLE+m.group(2),head)
head=re.sub(r'("description": ")A licensed[^"]*(")',lambda m:m.group(1)+DESC+m.group(2),head)
head=re.sub(r'("date(?:Published|Modified)": ")[^"]*(")',lambda m:m.group(1)+'2026-11-04'+m.group(2),head)
head=re.sub(r'<meta name="keywords" content="[^"]*">','<meta name="keywords" content="Goryokaku, Goryokaku Park, Goryokaku Tower, Hakodate, star fort Japan, Republic of Ezo, Hijikata Toshizo, Boshin War, Hakodate Magistrate Office, Goryokaku cherry blossoms, Goryokaku illumination">',head)
head=head.replace('guides/kochi-castle','guides/goryokaku').replace('guide_kochi_','guide_goryokaku_').replace('og-guides-kochi-castle','og-guides-goryokaku')
head=head.replace('高知城','五稜郭').replace('Kochi Castle','Goryokaku')
head=re.sub(r"<h1>.*?</h1>","<h1><em>Goryokaku</em>: Hakodate&rsquo;s Star Fort, the Republic of Ezo and the Last Battle of the Boshin War</h1>",head,count=1,flags=re.S)
head=head.replace("Shikoku's original keep, and the only castle where the lord's palace still stands beside it.",TAG)
faqs=[
("How much does it cost to visit Goryokaku?","The park is free (GLTJP, Jeepe). Paid parts are separate: the Goryokaku Tower observation deck is 1,200 yen for adults (japan-guide, GLTJP; the Jeepe FAQ says 1,000 yen), and the rebuilt Hakodate Magistrate&rsquo;s Office is 500 yen (japan-guide, Jeepe). Prices change, so please check on the day."),
("What are the opening hours?","GLTJP says the area outside the fort is open at all times, and the inner grounds are open 5:00 to 19:00 from April to October and 5:00 to 18:00 from November to March (GLTJP, Jeepe). The tower is open 9:00 to 18:00 with ticket sales until 17:50 (GLTJP, Jeepe). The Magistrate&rsquo;s Office is open 9:00 to 18:00, or to 17:00 from November to March, and japan-guide says it is closed from 31 December to 3 January."),
("How do I get there from Hakodate Station?","The tram to Goryokaku Koen-mae takes about 15 to 17 minutes and costs 230 yen, followed by a walk of about 10 minutes (japan-guide, GLTJP). A bus to Goryokaku Koen Iriguchi takes about 17 minutes plus a 5-minute walk, and the Goryokaku Tower shuttle bus takes about 15 minutes (GLTJP). Please do not confuse the park with JR Goryokaku Station, which GLTJP says is about a 40-minute walk away."),
("Why is Goryokaku shaped like a star?","Wikipedia says the five points let the fort put more guns on its walls than a traditional Japanese castle and reduce blind spots where cannons could not fire. Nippon.com says it was modelled on the walled fortress cities of Europe, and Wikipedia says it was designed by the Rangaku scholar Takeda Ayasaburo."),
("What happened to Hijikata Toshizo?","Hijikata Toshizo, the vice-commander of the Shinsengumi, fought for the former shogunate in the Battle of Hakodate. The Tabi-Samurai Japan page says he was shot by a government soldier at the Ippongi barrier in Hakodate, fell from his horse and died at the age of 34, during the all-out attack that began on 11 May by the old calendar. That is in the town, not inside the fort, but the tower&rsquo;s history corridor features him (Wikipedia, GLTJP)."),
("When are the cherry blossoms and the winter lights?","The blossoms usually fall from late April to early May (GLTJP, Nippon.com, Jeepe); Nippon.com says they opened on 25 April and peaked about the end of the month in 2018. GLTJP says about 2,000 lights outline the star from December to the end of February. Please check the current dates before you travel."),
("Is it worth going up the tower?","The star shape is easiest to understand from above, and the tower&rsquo;s deck is at about 90 metres (GLTJP). Nippon.com gives the decks as 86 and 90 metres. For a short visit, Jeepe suggests the tower followed by half a loop along the moat, and says a stroll in the park takes 30 to 60 minutes with about 30 more for the tower."),
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
assert not re.search('Kochi|Shikoku|kochi|Kanazawa|Shuri|Naha|Takeda|Asago|Machu|Odawara|Hojo|Aizu|Tsuruga',hh),re.findall('.{30}(?:Kochi|Shikoku|Kanazawa|Shuri|Naha|Aizu|Tsuruga).{20}',hh)
IL='class="inline-link"'
main='''<main>

  <!-- TABLE OF CONTENTS -->
  <aside class="toc" aria-label="Table of contents">
    <div class="toc-label">TABLE OF CONTENTS ／ 目次</div>
    <div class="toc-title">In This Guide</div>
    <ol>
      <li><a href="#opening">A Fort Drawn With a Ruler</a></li>
      <li><a href="#history">Why a Star?</a></li>
      <li><a href="#war">The Republic of Ezo and the Last Battle</a></li>
      <li><a href="#see">The Moat, the Magistrate&rsquo;s Office and the Tower</a></li>
      <li><a href="#cherry">Cherry Blossoms and Winter Lights</a></li>
      <li><a href="#visit">Visiting Goryokaku</a></li>
      <li><a href="#stay">Making It a Trip</a></li>
      <li><a href="#faq">Frequently Asked Questions</a></li>
      <li><a href="#final">Before You Leave the Park</a></li>
    </ol>
  </aside>

  <article>

    <section id="opening">
      <p class="opening">As a licensed guide, I like to tell visitors that Goryokaku looks different depending on whether you stand on top of it or beside it. From the tower it is a neat five-pointed star drawn around a green park. From the ground it is a quiet moat, a bank of earth and a lot of cherry trees. Behind both views is a short, odd chapter of history: a fort built to guard Hakodate from foreign ships ended up as the capital of a republic that lasted only a few months.</p>
      <p>This guide covers why the fort is a star, what happened here in 1868 and 1869, what to see, the cherry blossoms and winter lights, and the practical details. Where my sources disagree I say so, and I mark claims I found in only one place.</p>
    </section>

    <h2 id="history">Why a Star?<span class="h2-jp">なぜ星形なのか</span></h2>
    <p>Nippon.com sets the scene. Commodore Perry&rsquo;s mission reached Japan in 1853, and the Kanagawa Treaty of 1854 opened the port of Hakodate. GLTJP says the fort was built in the late Edo period as a government office for the Tokugawa shogunate, to run Hokkaido and to defend it from foreign powers. It calls Goryokaku Japan&rsquo;s first Western-style fortress, and says the name means a fort with five corners.</p>
    <p>Wikipedia says it was designed in 1855 by Takeda Ayasaburo, a scholar of Western learning who had studied European fortified cities. The dates of construction are not consistent. Jeepe says work began in 1857 and was completed in 1864, and Nippon.com also gives 1864. Wikipedia says the fortress was completed in 1866 after seven years of construction, and the Jeepe FAQ also says 1866. I would say simply that it was built in the 1850s and 1860s and was in use by the end of that decade.</p>
    <p>The star has a practical reason. Wikipedia says the five points allowed the fort to mount more guns on its walls than a traditional Japanese castle could, and reduced the number of blind spots where cannons could not fire. The moat served another purpose in winter: Wikipedia says it was used to harvest ice, which supported a considerable commercial ice industry.</p>

    <h2 id="war">The Republic of Ezo and the Last Battle<span class="h2-jp">蝦夷共和国と箱館戦争</span></h2>
    <p>The shogunate fell in 1868, but not everyone accepted it. Wikipedia says Enomoto Takeaki, the vice-commander of the shogunate navy, refused to hand over his fleet and sailed from Shinagawa on 20 August 1868. The same source says Goryokaku was occupied on 26 October 1868 and became the rebel army&rsquo;s command centre, and that the rebels founded the Ezo Republic in December with Enomoto as its president. Wikipedia gives the date as 25 December, while the Tabi-Samurai Japan page gives 15 December, which may be a different calendar, so I leave it at &ldquo;December 1868.&rdquo; Wikipedia says the republic existed only in 1869.</p>
    <p>The end came in the spring. The Tabi-Samurai Japan page says the government launched an all-out attack on Hakodate by land and sea on 11 May by the old calendar, and that its fleet began bombarding Goryokaku the next day. It says Enomoto agreed to surrender and that &ldquo;Goryokaku was surrendered at noon on the 18th,&rdquo; which ended both the Hakodate War and the Boshin War. Wikipedia gives 27 June 1869 for the surrender; I read these as the same day in two calendars, but I have not confirmed the conversion.</p>
    <p>Hijikata Toshizo, the Shinsengumi vice-commander, is the other name visitors ask about. GLTJP calls Goryokaku the last place associated with him. The Tabi-Samurai Japan page says he was shot by a government soldier at the Ippongi barrier in Hakodate after crossing a bridge, fell from his horse and died aged 34. That was in the town rather than in the fort, so please do not expect a memorial at the star itself. Wikipedia says the tower&rsquo;s exhibition features him, with several statues.</p>
    <p>Enomoto survived. Wikipedia says that after a few years in prison he was rehabilitated and held various ministry posts in the Meiji period. The Tabi-Samurai Japan page, a single source, says he was released in 1872 and later served as Minister to Russia and in several cabinet posts.</p>

    <h2 id="see">The Moat, the Magistrate&rsquo;s Office and the Tower<span class="h2-jp">見どころ</span></h2>
    <p>GLTJP says the grounds cover about 120,000 square metres and are designated a Special Historic Site; Wikipedia gives the designation year as 1952. Most of the buildings were torn down after the war because of their Tokugawa associations (Wikipedia), and the fort became a public park in 1914 at the request of Hakodate&rsquo;s citizens (Nippon.com). The moat and earth walls are what remain, and that is the real attraction: a walk along them shows the star from within.</p>
    <p>At the centre stands the <strong>Hakodate Magistrate&rsquo;s Office</strong>. GLTJP says the original was dismantled in 1871 and that one-third of the building was reconstructed on the same site with the same design, methods and dimensions. Nippon.com and japan-guide say it reopened in 2010. GLTJP says the interior has exhibits and videos. It is a useful stop because it shows the fort as an office, not only as a battlefield.</p>
    <p><strong>Goryokaku Tower</strong> stands beside the park. Nippon.com says the first tower was built in 1964 for the fort&rsquo;s 100th anniversary and replaced in 2006 by a 107-metre tower (japan-guide agrees on the height). Viewing decks are at 86 and 90 metres (Nippon.com), or at about 90 metres (GLTJP). GLTJP also describes a &ldquo;Goryokaku History Corridor&rdquo; on the second floor with scale models, bronze statues and dioramas.</p>

    <h2 id="cherry">Cherry Blossoms and Winter Lights<span class="h2-jp">桜とイルミネーション</span></h2>
    <p>Nippon.com says more than 10,000 Somei Yoshino trees were planted between 1914 and 1924 and about 1,600 remain. GLTJP says about 1,500, and japan-guide says &ldquo;over one thousand,&rdquo; so I would call it around 1,500. The season usually runs from late April to early May, which is later than in many parts of Japan (GLTJP, Nippon.com, Jeepe). GLTJP says visitors can tour the moat by rowboat in blossom season, a claim I found in one source only.</p>
    <p>In winter, GLTJP says the &ldquo;Goryo-boshi no Yume&rdquo; illumination runs from December to the end of February, with about 2,000 lights outlining the star shape around the moat. Please check the current schedule before you plan around it.</p>

    <h2 id="visit">Visiting Goryokaku<span class="h2-jp">アクセス</span></h2>
    <ul class="practical-list"><li><strong>Park admission:</strong> free; some facilities inside charge a fee (GLTJP, Jeepe).</li><li><strong>Park hours:</strong> the area outside the fort is open at all times; the inner grounds are open 5:00 to 19:00 from April to October and 5:00 to 18:00 from November to March (GLTJP, Jeepe).</li><li><strong>Goryokaku Tower:</strong> adults 1,200 yen, middle and high school students 900 yen, elementary students 600 yen, preschoolers free (GLTJP). The Jeepe FAQ gives 1,000, 750 and 500 yen instead, so please check on the day. Open 9:00 to 18:00, tickets until 17:50 (GLTJP, Jeepe); japan-guide says there are no closing days.</li><li><strong>Hakodate Magistrate&rsquo;s Office:</strong> adults 500 yen (japan-guide, Jeepe), students and children 250 yen (Jeepe). Open 9:00 to 18:00, or to 17:00 from November to March; last admission is 15 minutes before closing (japan-guide) or 30 minutes (Jeepe). japan-guide says it is closed from 31 December to 3 January.</li><li><strong>Tram:</strong> from Hakodate Station to Goryokaku Koen-mae, about 15 to 17 minutes and 230 yen, then about 10 minutes on foot (japan-guide, GLTJP).</li><li><strong>Bus:</strong> Hakodate Bus to Goryokaku Koen Iriguchi, about 17 minutes, then about 5 minutes on foot; or the Goryokaku Tower&ndash;Trappistine shuttle, about 15 minutes to Goryokaku Tower-mae (GLTJP).</li><li><strong>JR Goryokaku Station:</strong> GLTJP warns that this is about a 40-minute walk from the park.</li><li><strong>From Hakodate Airport:</strong> the airport shuttle to Goryokaku Tower-mae takes about 40 minutes (GLTJP), and Jeepe says the loop bus takes 30 to 40 minutes.</li><li><strong>Time needed:</strong> Jeepe suggests 30 to 60 minutes for the park and about 30 more for the tower, with extra time for the Magistrate&rsquo;s Office.</li></ul>

    <h2 id="stay">Making It a Trip<span class="h2-jp">滞在</span></h2>
    <p>Goryokaku fits easily into a day in Hakodate. If you like fortifications that tell a story of the Boshin War, our <a href="/guides/aizuwakamatsu-castle/" '''+IL+''' onclick="trackEvent('click','internal','guide_goryokaku_to_aizuwakamatsu')">Aizuwakamatsu Castle guide</a> covers the siege that came before this one, and our <a href="/guides/hirosaki-castle/" '''+IL+''' onclick="trackEvent('click','internal','guide_goryokaku_to_hirosaki')">Hirosaki Castle guide</a> covers another northern castle.</p>
    <div class="key-callout">
      <p>&#127890; <strong>Plan your trip:</strong> Browse guided tours or plan a stay around Hakodate. <a href="https://www.viator.com/search/Hakodate?pid=P00298374&amp;mcid=42383&amp;medium=link&amp;campaign=sacred-japan" target="_blank" rel="noopener sponsored" onclick="trackEvent('click','affiliate','viator_goryokaku_local')">Browse Hakodate tours &rarr;</a></p>
    </div>

    <h2 id="faq">Frequently Asked Questions<span class="h2-jp">よくあるご質問</span></h2>
    <div class="faq-stack">
'''+''.join(f'''    <details class="faq-item">
        <summary>{q}</summary>
        <div class="faq-answer">{a}</div>
    </details>
''' for q,a in faqs)+'''    </div>

    <h2 id="final">Before You Leave the Park<span class="h2-jp">むすびに</span></h2>
    <p>Give Goryokaku about two hours if you want the tower, the Magistrate&rsquo;s Office and a walk along the moat. Look at the star from above first, then walk down and trace one of its points on foot, and you will understand why it was built the way it was.</p>

    <div class="closing-block">
      <span class="torii">&#9961;&#65039;</span>
      <p>The republic lasted months. The star it was fought over is still there.</p>
    </div>

    <!-- RELATED GUIDES -->
    <section class="related-section">
      <h2>Related Guides</h2>
      <span class="h2-jp">関連ガイド</span>

      <div class="related-grid">

        <a class="related-card" href="/guides/aizuwakamatsu-castle/" onclick="trackEvent('click','internal','related_goryokaku_to_aizuwakamatsu')">
          <div class="related-card-label">SACRED JAPAN ／ GUIDES</div>
          <div class="related-card-title">&#127983; Aizuwakamatsu Castle Guide &rarr;</div>
          <div class="related-card-desc">The red-roofed keep and the 1868 siege.</div>
        </a>

        <a class="related-card" href="/guides/hirosaki-castle/" onclick="trackEvent('click','internal','related_goryokaku_to_hirosaki')">
          <div class="related-card-label">SACRED JAPAN ／ GUIDES</div>
          <div class="related-card-title">&#127983; Hirosaki Castle Guide &rarr;</div>
          <div class="related-card-desc">Tohoku&rsquo;s original keep, being moved on its base.</div>
        </a>

        <a class="related-card" href="/castles/" onclick="trackEvent('click','internal','related_goryokaku_to_castles')">
          <div class="related-card-label">SACRED JAPAN ／ CASTLES</div>
          <div class="related-card-title">&#127983; Japan's Castles &rarr;</div>
          <div class="related-card-desc">Every castle guide, with photos and official links.</div>
        </a>

      </div>
    </section>

  </article>

'''
tail=tail.replace('kochi-castle',SL).replace('_kochi_','_goryokaku_').replace('DKochi','DHakodate').replace('search/Kochi','search/Hakodate')
def L(u,l,t): return f'<a href="{u}" target="_blank" rel="noopener" style="color:var(--beni);text-decoration:underline;" onclick="trackEvent(\'click\',\'external\',\'{l}\')">{t}</a>'
src='Sources verified at time of writing: '+', '.join([
 L('https://www.gltjp.com/en/article/item/20331/','src_goryo_gltjp','GLTJP (park)'),
 L('https://www.gltjp.com/en/article/item/20360/','src_goryo_gltjp_tower','GLTJP (tower)'),
 L('https://www.japan-guide.com/e/e5352.html','src_goryo_jg','japan-guide'),
 L('https://www.nippon.com/articles/-/16559','src_goryo_nippon','Nippon.com'),
 L('https://en.wikipedia.org/wiki/Gory%C5%8Dkaku','src_goryo_wiki','Wikipedia (Goryokaku)'),
 L('https://en.wikipedia.org/wiki/Battle_of_Hakodate','src_goryo_wiki_battle','Wikipedia (Battle of Hakodate)'),
 L('https://www.jeepe.jp/en/articles/goryokaku-hokkaido-guide-1333','src_goryo_jeepe','Jeepe'),
 L('https://en.tabi-samurai-japan.com/story/event/427/2/','src_goryo_tabisamurai','Tabi-Samurai Japan'),
])+'. Hours, prices and availability change'
tail,n=re.subn(r'Sources verified at time of writing:.*?Hours, prices and availability change',lambda m:src,tail,flags=re.S); assert n==1
out=head+main+tail
assert not re.search('Kochi|Shikoku|kochi|Kanazawa|Shuri|Naha|Takeda Castle|Asago|Machu',re.sub(r'"mainEntity": \[.*','',out,flags=re.S)),re.findall('.{30}(?:Kochi|Kanazawa|Shuri|Naha|Asago|Machu).{20}',out)
os.makedirs(R+f'guides/{SL}',exist_ok=True); open(R+f'guides/{SL}/index.html','w',encoding='utf-8').write(out)
for tg in ['div','figure','picture','p','a','ul','li','details','section','h2']:
    assert len(re.findall(f'<{tg}[ >]',out))==len(re.findall(f'</{tg}>',out)),tg
for m in re.findall(r'<script type="application/ld\+json">(.*?)</script>',out,re.S): json.loads(m)
im=Image.open(R+'images/og/og-guides-matsue-castle.jpg').convert('RGB'); d=ImageDraw.Draw(im)
d.rectangle([40,150,1170,380],fill=(252,240,242)); d.rectangle([1118,66,1160,96],fill=(252,240,242))
f1=ImageFont.truetype(glob.glob('/usr/share/fonts/**/DejaVuSerif-Bold.ttf',recursive=True)[0],48)
f2=ImageFont.truetype(glob.glob('/usr/share/fonts/**/NotoSerifCJK-Bold.ttc',recursive=True)[0],28,index=0)
l1="Goryokaku Guide:"; l2="Star Fort, Ezo Republic, 1869"; print(d.textlength(l2,font=f1),d.textlength(l1,font=f1)); assert d.textlength(l2,font=f1)<1090
d.text((66,170),l1,font=f1,fill=(26,15,15)); d.text((66,238),l2,font=f1,fill=(26,15,15)); d.text((66,332),"五稜郭",font=f2,fill=(138,125,120))
im.save(R+f'images/og/og-guides-{SL}.jpg',quality=88); print('built',len(out))
