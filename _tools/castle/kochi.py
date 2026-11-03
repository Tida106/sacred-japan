import re,json,os,glob
from PIL import Image,ImageDraw,ImageFont
R='/home/claude/sacred-japan/'; SL='kochi-castle'
s=open(R+'guides/uwajima-castle/index.html',encoding='utf-8').read()
i=s.index('<main>'); j=s.index('</main>'); head,tail=s[:i],s[j:]
OT="Uwajima Castle Guide: A Keep Rebuilt to Look Peaceful, and the Climb to It"
OD="A licensed guide's guide to Uwajima Castle in Ehime: one of Japan's 12 original keeps, Todo Takatora's castle remade by the Date family, the ornate gables, and how to climb it."
TITLE="Kochi Castle Guide: The Keep and the Lord's Palace That Both Survived"
DESC="A licensed guide's guide to Kochi Castle in Shikoku: one of Japan's 12 original keeps, the only one that still has its lord's palace beside it, the 1727 fire, the gates, and how to visit."
def sub(t,a,b):
    assert a in t,a[:60]; return t.replace(a,b)
head=sub(head,OT,TITLE); head=sub(head,OD,DESC)
head=re.sub(r'<meta name="keywords" content="[^"]*">','<meta name="keywords" content="Kochi Castle, Kochi Castle guide, Kochi Castle Shikoku, Yamauchi Kazutoyo castle, Honmaru Palace Kochi, Kaitokukan, Japan original castles, Kochi Castle hours, Kochi Castle admission, Kochi Sunday market castle">',head)
head=sub(head,"<h1><em>Uwajima Castle</em>: A Keep Rebuilt to Look Peaceful</h1>","<h1><em>Kochi Castle</em>: The Keep and the Palace That Both Survived</h1>")
head=sub(head,"Ehime's small, ornate original keep, built by Todo Takatora and remade by the Date.","Shikoku's original keep, and the only castle where the lord's palace still stands beside it.")
head=head.replace('uwajima-castle',SL).replace('guide_uwajima_','guide_kochi_')
head=sub(head,'宇和島城','高知城'); head=head.replace('Uwajima Castle','Kochi Castle')
faqs=[
("How much does Kochi Castle cost and when is it open?","GLTJP lists 420 yen for visitors 18 and over, with under-18s free, for the keep, the Kaitokukan palace and the neighbouring gates. Japan Experience and Japan Visitor give 400 yen, so I would confirm at the gate. GLTJP gives 9:00 to 17:00 with last admission at 16:30, closed 26 December to 1 January, and says hours may be extended during events."),
("Why is Kochi Castle special?","GLTJP says it is the only castle in Japan where both the original keep and the Honmaru Palace survive, and that it is one of 12 castles with an original Edo-period keep. It also says 15 buildings on the grounds are Important Cultural Properties."),
("Is the keep original?","Yes. Japan Visitor says the castle burned down in 1727 and was rebuilt between 1729 and 1753, with the tower rebuilt in 1749 to its original design. So the keep you climb is the 18th-century rebuild, not the 1601 to 1611 original, but it is still an original wooden keep."),
("How do I get there from Kochi Station?","GLTJP gives about 15 minutes by Tosaden Kotsu bus to Kochijo-mae, or about 15 minutes by tram with a transfer at Harimayabashi, and about 30 minutes on foot from JR Kochi Station. Japan Experience says the main entrance is at the end of Otesuji, the street that holds the Sunday market."),
("When are the cherry blossoms?","GLTJP says about 225 cherry trees in the park reach full bloom in late March and are illuminated at night. Bloom timing varies by year, so check a local report before planning around it."),
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
assert not re.search('Uwajima|Ehime|uwajima',hh),re.search('.{40}(Uwajima|Ehime|uwajima).{40}',hh,re.S).group(0)
main='''<main>

  <!-- TABLE OF CONTENTS -->
  <aside class="toc" aria-label="Table of contents">
    <div class="toc-label">TABLE OF CONTENTS ／ 目次</div>
    <div class="toc-title">In This Guide</div>
    <ol>
      <li><a href="#opening">A Castle With Its Palace Still Beside It</a></li>
      <li><a href="#history">Kazutoyo, the Fire and the Rebuild</a></li>
      <li><a href="#keep">The Keep: The Hawk Castle</a></li>
      <li><a href="#palace">Kaitokukan: The Lord's Palace</a></li>
      <li><a href="#gates">Gates, Walls and Statues</a></li>
      <li><a href="#visit">Visiting Kochi Castle</a></li>
      <li><a href="#stay">Making It a Trip</a></li>
      <li><a href="#faq">Frequently Asked Questions</a></li>
      <li><a href="#final">One Castle, Both Halves</a></li>
    </ol>
  </aside>

  <article>

    <section id="opening">
      <p class="opening">As a licensed guide, I tell guests that most castles in Japan give you the tower and ask you to imagine the lord's home. Kochi Castle does not. GLTJP says it is the only castle in Japan where both the original keep and the Honmaru Palace survive, and the two stand within a short walk of each other on a hill in the middle of Kochi city, on Shikoku.</p>
      <p>This guide covers Yamauchi Kazutoyo and the castle's start, the 1727 fire and the rebuild, the keep, the Kaitokukan palace, the gates and statues, and the practical details of a visit.</p>
    </section>

    <h2 id="history">Kazutoyo, the Fire and the Rebuild<span class="h2-jp">築城と再建</span></h2>
    <p>Japan Visitor says Yamauchi Kazutoyo was moved to Tosa from Kakegawa after serving Tokugawa Ieyasu at Sekigahara in 1600. GLTJP says he was the first lord of the Tosa domain and that construction ran from 1601 to 1611. Wikipedia adds that he rebuilt the earlier Otakayama Castle on a larger scale and named it Kawanakayama Castle, later renamed Kochi Castle. I found that naming detail in one source.</p>
    <p>The castle did not survive intact in its first form. Wikipedia and Japan Visitor say a fire in 1727 destroyed much of the castle. Japan Visitor says it was rebuilt between 1729 and 1753, that the tower was rebuilt in 1749 to its original design, and that the Otemon gate survived the fire. Wikipedia says the Kaitokukan palace also burned and that its repair was finished in 1749.</p>
    <p>After that, Wikipedia says the domain ended in 1871 and the castle escaped the Meiji orders to destroy feudal fortifications, and that it came through the Pacific War intact. It became a National Historic Site in 1959 according to Wikipedia, with the protected area expanded in 2014.</p>

    <h2 id="keep">The Keep: The Hawk Castle<span class="h2-jp">天守</span></h2>
    <p>Japan Experience and Japan Visitor say the curving tiled eaves of the keep earned it the nickname Hawk Castle. Descriptions of its stories differ: GLTJP describes a four-tier exterior with six stories inside, Japan Experience gives six floors at about 18.5 meters, and Wikipedia calls it a five-story keep. I would rely on the six-story count inside, which most of these sources support, and treat the others as different ways of counting.</p>
    <p>GLTJP says the shachihoko roof ornaments were believed to help prevent fire, which fits a castle that had already burned once. Japan Experience mentions spikes set into the north-east wall of the tower, which it calls ninja repellents, and a hidden room for soldiers inside. GLTJP instead places the surviving shinobi-gaeshi in the Kaitokukan, so sources place these spikes differently and I would not repeat either claim more strongly than that.</p>
    <p>Japan Experience says the top of the keep gives views of Kochi town on a clear day.</p>

    <h2 id="palace">Kaitokukan: The Lord's Palace<span class="h2-jp">懐徳館</span></h2>
    <p>The Kaitokukan is the Honmaru Palace, and it is the reason Kochi is unusual. GLTJP says it was where the lord received guests, and Wikipedia describes it as a shoin-style palace with eight traditional rooms. GLTJP calls its shinobi-gaeshi, an intruder-prevention feature, the only one of its kind still standing in Japan. The same source says admission to the palace is included with the keep ticket.</p>

    <h2 id="gates">Gates, Walls and Statues<span class="h2-jp">城門と石垣</span></h2>
    <p>Sources give the Otemon different ages. GLTJP says it was built in 1801 and has an ishi-otoshi on its second floor for dropping stones or boiling water, Japan Visitor says it survived the 1727 fire, and Japan Experience calls it the oldest surviving part of the castle. I cannot reconcile those, so please treat the date as uncertain. Japan Visitor says a square enclosure in front of the gate, a masugata, lets defenders fire on intruders from three sides.</p>
    <p>GLTJP says the black Tsume Gate, also called the Karakuri Gate, connects the Honmaru Palace and the Ninomaru, and that its corridor served as offices for senior retainers. Japan Experience calls it a two-storey black-painted gate linking the inner and outer citadels.</p>
    <p>There are statues too. GLTJP says a bronze statue of Yamauchi Kazutoyo stands 4.32 meters tall on a 5.08-meter pedestal, unveiled on 20 September 1996, the anniversary of his death. Japan Visitor says a statue of his wife Chiyo stands in the grounds. Japan Experience says a statue of Itagaki Taisuke, a founder of the Meiji-era People's Rights Movement and a native of the area, stands just inside the main entrance.</p>

    <h2 id="visit">Visiting Kochi Castle<span class="h2-jp">アクセス</span></h2>
    <ul class="practical-list"><li><strong>Getting there:</strong> GLTJP says about 15 minutes by Tosaden Kotsu bus to Kochijo-mae, or about 15 minutes by tram with a transfer at Harimayabashi, and about 30 minutes on foot from JR Kochi Station.</li><li><strong>Tickets:</strong> 420 yen for visitors 18 and over, under-18s free (GLTJP). Japan Experience and Japan Visitor give 400 yen, so please confirm at the gate. The ticket covers the keep, the Kaitokukan, and neighbouring gates (GLTJP).</li><li><strong>Hours:</strong> 9:00 to 17:00, last admission 16:30, closed 26 December to 1 January, with possible extensions during events (GLTJP).</li><li><strong>Sunday market:</strong> Japan Experience says the main entrance is at the end of Otesuji, the street that holds the Sunday market.</li><li><strong>Cherry blossoms:</strong> about 225 trees reach full bloom in late March and are illuminated at night (GLTJP).</li></ul>

    <h2 id="stay">Making It a Trip<span class="h2-jp">滞在</span></h2>
    <p>Kochi pairs well with the other Shikoku castles. Our guides to <a href="/guides/uwajima-castle/" class="inline-link" onclick="trackEvent('click','internal','guide_kochi_to_uwajima')">Uwajima Castle</a> and <a href="/guides/marugame-castle/" class="inline-link" onclick="trackEvent('click','internal','guide_kochi_to_marugame')">Marugame Castle</a> cover two more of Shikoku's original keeps.</p>
    <div class="key-callout">
      <p>&#127890; <strong>Plan your trip:</strong> Browse guided tours, or plan a stay in Kochi. <a href="https://www.viator.com/search/Kochi?pid=P00298374&amp;mcid=42383&amp;medium=link&amp;campaign=sacred-japan" target="_blank" rel="noopener sponsored" onclick="trackEvent('click','affiliate','viator_kochi_local')">Browse Kochi tours on Viator</a> &middot; <a href="https://expedia.com/affiliate?siteid=1&amp;landingPage=https%3A%2F%2Fwww.expedia.co.jp%2FHotel-Search%3Fdestination%3DKochi&amp;camref=1101l5JmFa&amp;creativeref=1011l87782&amp;adref=PZf6lQ77e8" target="_blank" rel="noopener sponsored" onclick="trackEvent('click','affiliate','expedia_kochi_local')">Find stays in Kochi</a></p>
    </div>

    <h2 id="faq">Frequently Asked Questions<span class="h2-jp">よくあるご質問</span></h2>
    <div class="faq-stack">
'''+''.join(f'''    <details class="faq-item">
        <summary>{q}</summary>
        <div class="faq-answer">{a}</div>
    </details>
''' for q,a in faqs)+'''    </div>

    <h2 id="final">One Castle, Both Halves<span class="h2-jp">むすびに</span></h2>
    <p>Kochi is the castle I send people to when they ask what a lord's life looked like, because the answer is still standing a short walk from the tower. Climb the keep for the view, then spend the same time in the palace.</p>

    <div class="closing-block">
      <span class="torii">&#9961;&#65039;</span>
      <p>A keep on the hill, and the lord's palace still beside it.</p>
    </div>

    <!-- RELATED GUIDES -->
    <section class="related-section">
      <h2>Related Guides</h2>
      <span class="h2-jp">関連ガイド</span>

      <div class="related-grid">

        <a class="related-card" href="/guides/uwajima-castle/" onclick="trackEvent('click','internal','related_kochi_to_uwajima')">
          <div class="related-card-label">SACRED JAPAN ／ GUIDES</div>
          <div class="related-card-title">&#127983; Uwajima Castle Guide &rarr;</div>
          <div class="related-card-desc">A small, ornate original keep in Ehime.</div>
        </a>

        <a class="related-card" href="/guides/marugame-castle/" onclick="trackEvent('click','internal','related_kochi_to_marugame')">
          <div class="related-card-label">SACRED JAPAN ／ GUIDES</div>
          <div class="related-card-title">&#127983; Marugame Castle Guide &rarr;</div>
          <div class="related-card-desc">Shikoku's tall stone walls and a small keep.</div>
        </a>

        <a class="related-card" href="/castles/" onclick="trackEvent('click','internal','related_kochi_to_castles')">
          <div class="related-card-label">SACRED JAPAN ／ CASTLES</div>
          <div class="related-card-title">&#127983; Japan's 12 Original Castles &rarr;</div>
          <div class="related-card-desc">Every surviving keep, with photos and official links.</div>
        </a>

      </div>
    </section>

  </article>

'''
tail=tail.replace('uwajima-castle',SL).replace('_uwajima_','_kochi_')
def L(u,l,t): return f'<a href="{u}" target="_blank" rel="noopener" style="color:var(--beni);text-decoration:underline;" onclick="trackEvent(\'click\',\'external\',\'{l}\')">{t}</a>'
src='Sources verified at time of writing: '+', '.join([
 L('https://www.gltjp.com/en/article/item/20366/','src_kochi_gltjp','GLTJP'),
 L('https://www.japanvisitor.com/japan-city-guides/japanese-castles/kochi-castle','src_kochi_japanvisitor','Japan Visitor'),
 L('https://www.japan-experience.com/all-about-japan/kochi/attractions-excursions/kochi-castle','src_kochi_japanexperience','Japan Experience'),
 L('https://en.wikipedia.org/wiki/K%C5%8Dchi_Castle','src_kochi_wikipedia','Wikipedia'),
])+'. Hours, prices and availability change'
tail,n=re.subn(r'Sources verified at time of writing:.*?Hours, prices and availability change',lambda m:src,tail,flags=re.S); assert n==1
out=head+main+tail
out=out.replace('destination%3DUwajima','destination%3DKochi').replace('viator.com/search/Ehime','viator.com/search/Kochi')
chk=re.sub(r'related_kochi_to_uwajima|/guides/uwajima-castle/|Uwajima Castle|guide_kochi_to_uwajima|A small, ornate original keep in Ehime\.|Uwajima Castle Guide|two more of Shikoku|Ehime','',out)
assert not re.search('Uwajima|Ehime|uwajima',chk),re.search('.{50}(Uwajima|Ehime|uwajima).{50}',chk,re.S).group(0)
os.makedirs(R+f'guides/{SL}',exist_ok=True); open(R+f'guides/{SL}/index.html','w',encoding='utf-8').write(out)
for tg in ['div','figure','picture','p','a','ul','li','details','section','h2']:
    assert len(re.findall(f'<{tg}[ >]',out))==len(re.findall(f'</{tg}>',out)),tg
for m in re.findall(r'<script type="application/ld\+json">(.*?)</script>',out,re.S): json.loads(m)
im=Image.open(R+'images/og/og-guides-matsue-castle.jpg').convert('RGB'); d=ImageDraw.Draw(im)
d.rectangle([40,150,1170,380],fill=(252,240,242))
f1=ImageFont.truetype(glob.glob('/usr/share/fonts/**/DejaVuSerif-Bold.ttf',recursive=True)[0],48)
f2=ImageFont.truetype(glob.glob('/usr/share/fonts/**/NotoSerifCJK-Bold.ttc',recursive=True)[0],28,index=0)
l2="The Keep and Palace That Survived"; assert d.textlength(l2,font=f1)<1090,d.textlength(l2,font=f1)
d.text((66,170),"Kochi Castle Guide:",font=f1,fill=(26,15,15)); d.text((66,238),l2,font=f1,fill=(26,15,15)); d.text((66,332),"高知城",font=f2,fill=(138,125,120))
im.save(R+f'images/og/og-guides-{SL}.jpg',quality=88); print('built',len(out))
