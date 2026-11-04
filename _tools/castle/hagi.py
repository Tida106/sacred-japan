import re,json,os,glob
from PIL import Image,ImageDraw,ImageFont
R='/home/claude/sacred-japan/'; SL='hagi-castle'
s=open(R+'guides/kochi-castle/index.html',encoding='utf-8').read()
i=s.index('<main>'); j=s.index('</main>'); head,tail=s[:i],s[j:]
TITLE="Hagi Castle Ruins Guide: The Castle Its Own Lords Tore Down, Now a Park and World Heritage Site"
DESC="A licensed guide's guide to Hagi Castle ruins in Yamaguchi: why the Mori moved here from Hiroshima, why the keep was torn down in 1874, what survives in Shizuki Park, the cherry blossoms and how to visit."
head=re.sub(r'<title>.*?</title>',f'<title>{TITLE} | Sacred Japan</title>',head,count=1)
head=re.sub(r'(<meta (?:name="description"|property="og:description"|name="twitter:description") content=")[^"]*(")',lambda m:m.group(1)+DESC+m.group(2),head)
head=re.sub(r'(<meta (?:property="og:title"|name="twitter:title") content=")[^"]*(")',lambda m:m.group(1)+TITLE+m.group(2),head)
head=re.sub(r'("headline": ")[^"]*(")',lambda m:m.group(1)+TITLE+m.group(2),head)
head=re.sub(r'("description": ")A licensed[^"]*(")',lambda m:m.group(1)+DESC+m.group(2),head)
head=re.sub(r'<meta name="keywords" content="[^"]*">','<meta name="keywords" content="Hagi Castle, Hagi Castle ruins, Shizuki Park, Hagi Castle admission, Hagi Castle hours, Hagi Castle cherry blossoms, Hagi Castle history, Hagi castle town, Mori clan Hagi">',head)
head=head.replace('guides/kochi-castle','guides/hagi-castle').replace('guide_kochi_','guide_hagi_').replace('og-guides-kochi-castle','og-guides-hagi-castle')
head=head.replace('高知城','萩城跡').replace('Kochi Castle','Hagi Castle')
head=re.sub(r"<h1>.*?</h1>","<h1><em>Hagi Castle Ruins</em>: The Castle Its Own Lords Tore Down, Now a Park and World Heritage Site</h1>",head,count=1,flags=re.S)
head=head.replace("Shikoku's original keep, and the only castle where the lord's palace still stands beside it.","A castle with no keep: the Mori lords' seat after Hiroshima, torn down in 1874 and now a park of walls, moat and cherry trees.")
faqs=[
("Is there a keep at Hagi Castle?","No. The Hagi city site and the Ministry of Land, Infrastructure, Transport and Tourism (MLIT) multilingual sign database both say the main keep was torn down in 1874, and that the grounds became Shizuki Park. Wikipedia describes it as a five-story keep, which is the only source I found that gives the number of floors. What you see now is the stone walls, the moat, the keep foundation, a shrine and a teahouse."),
("Why were the Mori lords in Hagi?","Wikipedia says the Mori backed the losing side in 1600 and did not fight at Sekigahara, after which Tokugawa Ieyasu took about two-thirds of their lands. They had built Hiroshima Castle, and Hagi was the remote place they were moved to. The city site and MLIT say they relocated to Hagi in 1603 and built the castle in 1604. For the earlier castle, see our Hiroshima Castle guide."),
("What does it cost, and when is it open?","GLTJP, Japan-guide and the Hagi city site give 220 yen for adults and 100 yen for elementary and junior high school students, while Fun Japan gives 210 yen. GLTJP says the ticket includes a combined ticket for the Former Asa Mori Residence Nagaya. Hours are 8:00 to 18:30 from April to October, 8:30 to 18:00 in March and 8:30 to 16:30 from November to February, and the city site and Japan-guide say it is open every day. Please confirm on the official site."),
("Is Hagi Castle a World Heritage site?","Yes, as part of a larger listing. The Hagi city site, Wikipedia and Fun Japan say the castle site was registered in 2015 as part of Hagi Castle Town, within Sites of Japan's Meiji Industrial Revolution: Iron and Steel, Shipbuilding and Coal Mining. The city site and MLIT also say it is a National Historic Site, designated in 1951, although Wikipedia gives two different years."),
("How do I get there, and how long should I allow?","The city site, Japan-guide and Fun Japan say to take the Hagi Junkan Ma-ru bus to the Hagi Castle Ruins and Shizuki Park Entrance stop and walk about 5 minutes. The sources disagree on whether that is the east or west route, so please check the bus map. Japan-guide gives about 2.5 km from Higashi-Hagi Station, which is 30 to 45 minutes on foot or 10 to 20 minutes by bicycle. I would allow about two hours for the park, and more if you climb Mount Shizuki, which is my own estimate."),
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
      <li><a href="#opening">A Castle You Visit for What Is Missing</a></li>
      <li><a href="#history">From Hiroshima to Hagi</a></li>
      <li><a href="#end">1863 to 1874: Taking It Down</a></li>
      <li><a href="#see">What You Can See Now</a></li>
      <li><a href="#shizuki">Mount Shizuki and the Castle Town</a></li>
      <li><a href="#blossoms">Cherry Blossoms</a></li>
      <li><a href="#visit">Visiting Hagi Castle Ruins</a></li>
      <li><a href="#stay">Making It a Trip</a></li>
      <li><a href="#faq">Frequently Asked Questions</a></li>
      <li><a href="#final">A Castle Worth Its Silence</a></li>
    </ol>
  </aside>

  <article>

    <section id="opening">
      <p class="opening">As a licensed guide, I send visitors to Hagi Castle with one warning: there is no castle. The keep is gone, and the buildings around it are gone, and what remains is a set of stone walls, a moat and a park by the sea. I still think it is one of the more interesting castle sites in western Japan, because the people who built it were the people who tore it down, and the reason says a lot about how Japan changed in the 1860s and 1870s.</p>
      <p>This guide covers why the Mori lords came to Hagi, why they gave up their own castle, what is left to see in Shizuki Park, the cherry blossoms and the practical details. Where my sources disagree, I say so.</p>
    </section>

    <h2 id="history">From Hiroshima to Hagi<span class="h2-jp">広島から萩へ</span></h2>
    <p>The Mori family ruled the Choshu domain, in what is now Yamaguchi, during the Edo period. Wikipedia says they had built Hiroshima Castle as their main stronghold under Toyotomi rule, that they backed the losing side in 1600 and did not actually fight at Sekigahara, and that Tokugawa Ieyasu afterward took about two-thirds of their holdings. The Hagi city site and MLIT say the family relocated to Hagi in 1603 and built the castle in 1604, and the city site describes Hagi as a sparsely populated area far from central Japan. If you have read our <a href="/guides/hiroshima-castle/" class="inline-link" onclick="trackEvent('click','internal','guide_hagi_to_hiroshima')">Hiroshima Castle guide</a>, this is the same family, a generation later and a long way from the delta.</p>
    <p>The city site says the castle stood at the foot of Mount Shizuki and was built to be hard to take. An attacker had to pass three moats, an upper-class samurai district, large stone walls and several gates, and a small fortress at the top of Mount Shizuki was the last place to hold out. Fun Japan describes the layout as a flatland castle with Honmaru, Ninomaru and Sannomaru walls and a mountain castle on the summit. Wikipedia gives 1604 to 1608 for the construction, which is a single-source figure, and says the keep had five stories, with many turrets set along the stone walls. GLTJP says the Mori ruled from here for over 250 years.</p>

    <h2 id="end">1863 to 1874: Taking It Down<span class="h2-jp">解体</span></h2>
    <p>The end came in two stages. Wikipedia says that in 1863 the Mori moved their seat to Yamaguchi Castle because they feared a foreign naval attack after the Shimonoseki campaign, which is a single-source detail I have not confirmed elsewhere. After samurai rule ended in 1868, the city site and MLIT say the Hagi lords gave up their domain and castle and helped remove the symbols of the old order, and MLIT adds that the end of samurai rule was partly caused by the Mori.</p>
    <p>The main keep was torn down in 1874. The sources describe the order differently. Wikipedia and Fun Japan say the Meiji government ordered the destruction, one page of the city site says the government dismantled many castles to show that samurai rule had ended, and another city page and MLIT say the former lords gave up the castle and helped remove it. I would read it as a decision both sides were part of. The city site says the grounds were sold off in the following years, and they later became a city park.</p>

    <h2 id="see">What You Can See Now<span class="h2-jp">見どころ</span></h2>
    <p>Do not expect a building. Japan-guide lists the walls, the moats, the foundation of the former keep, and a shrine and a teahouse in the park. GLTJP adds that free VR displays show the castle as it once stood, and the city site says a VR reconstruction of the keep can be viewed on a smartphone or tablet, which I think is the best way to see what the walls once held up.</p>
    <p>Shizukiyama Shrine stands in the Honmaru ruins. The city site says it is the Mori family shrine, built in 1878, and GLTJP says it honors the successive lords. For the teahouse, GLTJP calls it Hanae Chatei and says feudal lords once held tea gatherings there. The city site says it was moved to the park in 1889, and Fun Japan says it came from the Sannomaru, along with the Banseibashi bridge, which it says came from the Meirinkan clan school. Those two details are from one source each, so please treat them as a guide's note.</p>
    <p>The Ninomaru held shrines, temples and twelve turrets, according to Fun Japan, which says only the stone walls of its gates remain. Wikipedia says the stone walls of the central and hilltop areas remain largely intact and that an outer gate and a corner turret were later restored, which I could not reconcile with the Fun Japan account, so please check on site. GLTJP says the stone walls and other features are lit from sunset until 10 p.m., and Fun Japan says the keep ruins are lit and reflected in the moat.</p>

    <h2 id="shizuki">Mount Shizuki and the Castle Town<span class="h2-jp">指月山と城下町</span></h2>
    <p>Japan-guide says Mount Shizuki can be reached by a hike of roughly 20 minutes to the summit, and the city site says the final fortress stood at the top. It does not say what is left up there, so I would go for the view and the walk, not for a second set of ruins.</p>
    <p>The ruins are part of a larger listing. The city site, Wikipedia and Fun Japan say the castle site was registered in 2015 as part of Hagi Castle Town in the Meiji Industrial Revolution World Heritage listing, and Wikipedia gives 5 July 2015. The city site and MLIT say it is a National Historic Site, designated in 1951, while Wikipedia gives two different years. If you have time, Fun Japan names the Former Asa Mori Residence in the Sannomaru as the largest samurai residence in Hagi, with a tenement house that is an Important Cultural Property, and GLTJP says your admission includes a combined ticket for its nagaya. Please check the ticket details at the gate.</p>

    <h2 id="blossoms">Cherry Blossoms<span class="h2-jp">桜</span></h2>
    <p>The park is best known for its cherry trees. GLTJP and Fun Japan give about 600 Somei Yoshino trees, while the city site says over 500, so I would say several hundred. GLTJP and Fun Japan also mention the Midori Yoshino, a rare cherry with white blossoms that they say is found only in this region and that is a natural monument of Yamaguchi Prefecture. None of my sources give a bloom date, so please check the local forecast before you plan around it.</p>

    <h2 id="visit">Visiting Hagi Castle Ruins<span class="h2-jp">アクセス</span></h2>
    <ul class="practical-list"><li><strong>Admission:</strong> 220 yen for adults, and 100 yen for elementary and junior high school students (GLTJP, Japan-guide and the Hagi city site). Fun Japan gives 210 yen. GLTJP says the ticket includes a combined ticket for the Former Asa Mori Residence Nagaya. Please confirm on the official site.</li><li><strong>Hours:</strong> 8:00 to 18:30 from April to October, 8:30 to 18:00 in March, and 8:30 to 16:30 from November to February (Japan-guide and the city site). GLTJP lists November and December but not January and February.</li><li><strong>Closed:</strong> No closing days are given (Japan-guide and the city site).</li><li><strong>Bus:</strong> Take the Hagi Junkan Ma-ru bus to the Hagi Castle Ruins and Shizuki Park Entrance stop, then walk about 5 minutes. The sources disagree on whether this is the east or the west route, so please check the bus map.</li><li><strong>On foot or by bike:</strong> About 2.5 km from Higashi-Hagi Station, 30 to 45 minutes on foot or 10 to 20 minutes by bicycle, and bicycles are permitted inside the park (Japan-guide).</li><li><strong>By car or train:</strong> About 5 minutes by car from Tamae Station (GLTJP). The city site lists free parking at Shizuki Daiichi.</li><li><strong>From Tokyo:</strong> Fun Japan says to take the Shinkansen to Shin-Yamaguchi (about 4.5 hours), then the Super Hagi-go bus (about 60 minutes), then the Ma-ru bus (about 15 minutes) and walk 5 minutes.</li><li><strong>Facilities:</strong> Restrooms and free Wi-Fi, with no coin lockers (GLTJP).</li></ul>

    <h2 id="stay">Making It a Trip<span class="h2-jp">滞在</span></h2>
    <p>Hagi is a day trip from Yamaguchi or an overnight stop in its own right, and the castle works best as the start of a walk through the old castle town. If you want another castle where the keep is gone but the walls remain, see our <a href="/guides/hiroshima-castle/" class="inline-link" onclick="trackEvent('click','internal','guide_hagi_to_hiroshima_2')">Hiroshima Castle guide</a> for the Mori family's earlier seat, or our <a href="/guides/matsue-castle/" class="inline-link" onclick="trackEvent('click','internal','guide_hagi_to_matsue')">Matsue Castle guide</a> for one that survived on the San'in coast.</p>
    <div class="key-callout">
      <p>&#127890; <strong>Plan your trip:</strong> Browse guided tours, or plan a stay in Hagi. <a href="https://www.viator.com/search/Hagi?pid=P00298374&amp;mcid=42383&amp;medium=link&amp;campaign=sacred-japan" target="_blank" rel="noopener sponsored" onclick="trackEvent('click','affiliate','viator_hagi_local')">Browse Hagi tours &rarr;</a></p>
    </div>

    <h2 id="faq">Frequently Asked Questions<span class="h2-jp">よくあるご質問</span></h2>
    <div class="faq-stack">
'''+''.join(f'''    <details class="faq-item">
        <summary>{q}</summary>
        <div class="faq-answer">{a}</div>
    </details>
''' for q,a in faqs)+'''    </div>

    <h2 id="final">A Castle Worth Its Silence<span class="h2-jp">むすびに</span></h2>
    <p>Hagi Castle is worth a visit if you like walls, water and the story behind a missing building. Go in spring if you can, take the 20-minute climb up Mount Shizuki if the weather is clear, and keep in mind that the lords who built the castle are the ones who took it down.</p>

    <div class="closing-block">
      <span class="torii">&#9961;&#65039;</span>
      <p>The walls remain. The castle was taken down by the people who built it.</p>
    </div>

    <!-- RELATED GUIDES -->
    <section class="related-section">
      <h2>Related Guides</h2>
      <span class="h2-jp">関連ガイド</span>

      <div class="related-grid">

        <a class="related-card" href="/guides/hiroshima-castle/" onclick="trackEvent('click','internal','related_hagi_to_hiroshima')">
          <div class="related-card-label">SACRED JAPAN ／ GUIDES</div>
          <div class="related-card-title">&#127983; Hiroshima Castle Guide &rarr;</div>
          <div class="related-card-desc">The Mori family's earlier castle, rebuilt after 1945.</div>
        </a>

        <a class="related-card" href="/guides/matsue-castle/" onclick="trackEvent('click','internal','related_hagi_to_matsue')">
          <div class="related-card-label">SACRED JAPAN ／ GUIDES</div>
          <div class="related-card-title">&#127983; Matsue Castle Guide &rarr;</div>
          <div class="related-card-desc">A surviving original keep on the San'in coast.</div>
        </a>

        <a class="related-card" href="/castles/" onclick="trackEvent('click','internal','related_hagi_to_castles')">
          <div class="related-card-label">SACRED JAPAN ／ CASTLES</div>
          <div class="related-card-title">&#127983; Japan's Castles &rarr;</div>
          <div class="related-card-desc">Every castle guide, with photos and official links.</div>
        </a>

      </div>
    </section>

  </article>

'''
tail=tail.replace('kochi-castle',SL).replace('_kochi_','_hagi_').replace('DKochi','DHagi').replace('search/Kochi','search/Hagi')
def L(u,l,t): return f'<a href="{u}" target="_blank" rel="noopener" style="color:var(--beni);text-decoration:underline;" onclick="trackEvent(\'click\',\'external\',\'{l}\')">{t}</a>'
src='Sources verified at time of writing: '+', '.join([
 L('https://www.gltjp.com/en/directory/item/16147/','src_hagi_gltjp','GLTJP'),
 L('https://www.japan-guide.com/e/e6152.html','src_hagi_jguide','Japan-guide'),
 L('https://en.wikipedia.org/wiki/Hagi_Castle','src_hagi_wikipedia','Wikipedia'),
 L('https://www.hagishi.com/en/search/detail.php?d=190010','src_hagi_city','Hagi city site'),
 L('https://www.mlit.go.jp/tagengo-db/en/H30-01054.html','src_hagi_mlit','MLIT multilingual sign database'),
 L('https://fun-japan.jp/en/articles/10581','src_hagi_funjapan','Fun Japan'),
])+'. Hours, prices and availability change'
tail,n=re.subn(r'Sources verified at time of writing:.*?Hours, prices and availability change',lambda m:src,tail,flags=re.S); assert n==1
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
l2="The Castle Its Lords Tore Down"; print(d.textlength(l2,font=f1)); assert d.textlength(l2,font=f1)<1090
d.text((66,170),"Hagi Castle Ruins Guide:",font=f1,fill=(26,15,15)); d.text((66,238),l2,font=f1,fill=(26,15,15)); d.text((66,332),"萩城跡",font=f2,fill=(138,125,120))
im.save(R+f'images/og/og-guides-{SL}.jpg',quality=88); print('built',len(out))
