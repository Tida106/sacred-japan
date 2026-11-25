import re,json,os,glob,shutil
from PIL import Image,ImageDraw,ImageFont
R='/home/claude/sacred-japan/'; SL='omiwa-jinja'; D=R+f'guides/{SL}/'
os.makedirs(D+'images',exist_ok=True); SRC=R+'culture/japanese-mythology/images/'
LIC={'by3':('CC BY 3.0','https://creativecommons.org/licenses/by/3.0/'),
     'by4':('CC BY 4.0','https://creativecommons.org/licenses/by/4.0/'),
     'by21jp':('CC BY 2.1 JP','https://creativecommons.org/licenses/by/2.1/jp/'),
     'cc0':('CC0 1.0','https://creativecommons.org/publicdomain/zero/1.0/'),
     'pd':('public domain','https://commons.wikimedia.org/wiki/Commons:Public_domain')}
def CS(t): return 'https://commons.wikimedia.org/w/index.php?search='+t.replace(' ','+')+'&title=Special:MediaSearch&type=image'
UP='/mnt/user-data/uploads/'
LIC['bysa4']=('CC BY-SA 4.0','https://creativecommons.org/licenses/by-sa/4.0/')
P={
'haiden':('de3f63a2','KishujiRapid','bysa4','https://commons.wikimedia.org/wiki/User:KishujiRapid'),
'nitorii':('5f0f770a','Ocdp','cc0','https://commons.wikimedia.org/wiki/User:Ocdp'),
'torii':('4ea19461','z tanuki','by3','https://web.archive.org/web/20161023171648/http://www.panoramio.com/photo/61889699'),
'pano3':('d5ffb643','z tanuki','by3','https://web.archive.org/web/20161023171648/http://www.panoramio.com/photo/61889699'),
}
for k,v in P.items():
    im=Image.open(UP+v[0]+'-image.webp').convert('RGB')
    im.save(D+f'images/{k}.jpg',quality=84); im.save(D+f'images/{k}.webp',quality=80)
SIZE={k:Image.open(D+f'images/{k}.jpg').size for k in P}
def fig2(k,alt,cap,date,hero=False):
    u,a,l,cl=P[k]; ln,lu=LIC[l]; w,h=SIZE[k]
    if hero: st='margin:0 0 48px;'; ld='eager'; ims='style="width:100%;max-height:420px;object-fit:cover;border-radius:4px;display:block;"'
    else:
        mw=min(420 if h>w else 760,w)
        st='margin:28px auto;max-width:%dpx;'%mw; ld='lazy'; ims='style="width:100%;height:auto;border-radius:4px;display:block;"'
    lic=f'<a href="{lu}" target="_blank" rel="noopener">{ln}</a>'
    return f'''<figure style="{st}"><picture><source srcset="/guides/{SL}/images/{k}.webp" type="image/webp"><img src="/guides/{SL}/images/{k}.jpg" alt="{alt}" width="{w}" height="{h}" loading="{ld}" {ims}></picture><figcaption style="font-size:13px;color:var(--enshu);margin-top:10px;text-align:center;line-height:1.6;">{cap}.<br>Photo: <a href="{cl}" target="_blank" rel="noopener">{a}</a>{(', '+date) if date else ''}, {lic}, via Wikimedia Commons (resized)</figcaption></figure>
'''
fig=fig2
s=open(R+'guides/gifu-castle/index.html',encoding='utf-8').read()
i=s.index('<main>'); j=s.index('</main>'); head,tail=s[:i],s[j:]
TITLE="Omiwa Shrine Guide: Nara's Mountain Shrine with No Main Hall, the Triple Torii and the Climb"
DESC="A licensed guide's guide to Omiwa Shrine in Nara: Mount Miwa as the sacred body, why there is no honden, the 1664 worship hall, the cedar ball of sake brewers, Sai Shrine's healing well, the mountain climb and how to get there from Miwa Station."
TAG="Nara's oldest mountain shrine, with no main hall: the worship hall, the torii, the cedar ball and the way up Mount Miwa."
head=re.sub(r'<title>.*?</title>',f'<title>{TITLE} | Sacred Japan</title>',head,count=1)
head=re.sub(r'(<meta (?:name="description"|property="og:description"|name="twitter:description") content=")[^"]*(")',lambda m:m.group(1)+DESC+m.group(2),head)
head=re.sub(r'(<meta (?:property="og:title"|name="twitter:title") content=")[^"]*(")',lambda m:m.group(1)+TITLE+m.group(2),head)
head=re.sub(r'("headline": ")[^"]*(")',lambda m:m.group(1)+TITLE+m.group(2),head)
head=re.sub(r'("description": ")A licensed[^"]*(")',lambda m:m.group(1)+DESC+m.group(2),head)
head=re.sub(r'("date(?:Published|Modified)": ")[^"]*(")',lambda m:m.group(1)+'2026-11-25'+m.group(2),head)
head=re.sub(r'<meta name="keywords" content="[^"]*">','<meta name="keywords" content="Omiwa Shrine, Omiwa Jinja, Miwa Shrine, Mount Miwa, Nara shrine, Sakurai, Omononushi, no honden shrine, sugidama, Miwa Myojin, Yamanobe no Michi, Mount Miwa climb">',head)
head=head.replace('guides/gifu-castle',f'guides/{SL}').replace('guide_gifu_castle_','guide_omiwa_').replace('og-guides-gifu-castle',f'og-guides-{SL}')
head=head.replace('岐阜城','大神神社').replace('Gifu Castle','Omiwa Shrine')
head=re.sub(r"<h1>.*?</h1>","<h1><em>Omiwa Shrine</em>: Nara\'s Mountain Shrine with No Main Hall, the Triple Torii and the Climb</h1>",head,count=1,flags=re.S)
head=head.replace("Nobunaga's mountain castle above Gifu, with the keep closed until late 2027.",TAG)
head=head.replace('SACRED JAPAN GUIDES ／ 城','SACRED JAPAN GUIDES ／ 神社')
IL='class="inline-link"'
def a(u,t,ev): return f'<a href="{u}" {IL} onclick="trackEvent(\'click\',\'internal\',\'guide_omiwa_to_{ev}\')">{t}</a>'
faqs=[
("Does Omiwa Shrine really have no main hall?","Yes. Nippon.com explains that because the shrine is dedicated to the whole mountain, it has no <em>honden</em> and rites take place in the <em>haiden</em>, the worship hall. Lonely Planet adds that the kami is considered inseparable from the mountain, and that this is thought to be an older style of worship."),
("Who is enshrined at Omiwa Shrine?","The main deity is Omononushi. Nippon.com says the Kojiki and Nihon Shoki record that he appeared before Okuninushi, offered his help in building the land, and asked to be worshipped on Mount Miwa. He is seen as a protector against evil and misfortune and as the patron of sake."),
("Can I climb Mount Miwa?","Yes, as an act of worship, not as ordinary hiking. Nippon.com says climbers must apply for permission, wear a white sash, and that eating, drinking, smoking and photography are prohibited on the mountain. Matcha (2017) and Live Japan give registration at Sai Shrine as 9:00 to 14:00, a fee of 300 yen and a return by 16:00, with a round trip of about 2 to 3 hours. Matcha also lists closing days and says foreign visitors need basic Japanese or a Japanese companion. Those details date from 2017 to 2020, so confirm with the shrine."),
("What is the big ball of cedar leaves?","It is a <em>sugidama</em>. Nippon.com says such balls hang at sake breweries and shops to signal a new brew, many sake makers get theirs from this shrine, and the one in the worship hall is about 1.7 metres across and about 250 kilograms, replaced with a fresh green one every autumn. See our "+a('/guides/sake-shrines/','guide to sake and shrines','sake')+" for more."),
("How do I get to Omiwa Shrine?","Take the JR Sakurai Line (the Man&rsquo;yo Mahoroba Line) to Miwa Station. Nippon.com, GLTJP and Lonely Planet say about 5 minutes on foot; japan-guide says 10. From JR Nara Station the ride is about 25 minutes and 330 yen (japan-guide) or about 30 minutes (Live Japan). The grounds are always open and free."),
("Can I see the triple torii behind the hall?","Only with the shrine&rsquo;s permission. Japan-guide says visitors must ask at the shrine office and be guided by a priest, and Tsunagu Japan describes it as a special worship that has to be applied for. A similar triple torii stands at Hibara Shrine, which is open to walk up to (japan-guide)."),
]
faq_json=',\n'.join("""    {
      "@type": "Question",
      "name": %s,
      "acceptedAnswer": {
        "@type": "Answer",
        "text": %s
      }
    }"""%(json.dumps(re.sub('<[^>]+>','',q)),json.dumps(re.sub('&ldquo;|&rdquo;','"',re.sub('&rsquo;','’',re.sub('<[^>]+>','',a_))))) for q,a_ in faqs)
head=re.sub(r'("mainEntity": \[\n).*?(\n  \]\n\}\n</script>\n\n<!-- ── GOOGLE)',lambda m:m.group(1)+faq_json+m.group(2),head,flags=re.S)
hh=re.sub(r'"mainEntity": \[.*','',head,flags=re.S)
assert not re.search('Gifu|Nobunaga|castle|Castle',re.sub(r'<nav>.*?</nav>','',hh,flags=re.S).replace('Castles','')),re.findall('.{30}(?:Gifu|Nobunaga|astle).{20}',hh)
main="""<main>

  <aside class="toc" aria-label="Table of contents">
    <div class="toc-label">TABLE OF CONTENTS ／ 目次</div>
    <div class="toc-title">In This Guide</div>
    <ol>
      <li><a href="#opening">A Shrine for a Mountain</a></li>
      <li><a href="#mountain">Mount Miwa and Omononushi</a></li>
      <li><a href="#approach">Walking In: Torii and Approach</a></li>
      <li><a href="#hall">The Worship Hall and the Triple Torii</a></li>
      <li><a href="#sugidama">Sake, Cedar Balls and the Snake</a></li>
      <li><a href="#sai">Sai Shrine and the Climb</a></li>
      <li><a href="#visit">Visiting Omiwa Shrine</a></li>
      <li><a href="#faq">Frequently Asked Questions</a></li>
      <li><a href="#final">Before You Go</a></li>
    </ol>
  </aside>

  <article>

"""+fig('haiden','Front of the unpainted wooden worship hall of Omiwa Shrine with a curved gable over the steps, visitors standing before it and tall trees behind','The worship hall of Omiwa Shrine, with visitors at the front steps',None,hero=True)+"""
    <p class="opening" id="opening">As a licensed guide, I would point anyone curious about the roots of Shinto to this place. Omiwa Shrine in Nara has a worship hall, a row of gates and a lot of cedar, but no main hall at all. The god is the mountain behind it, and everything you do here points that way.</p>
    <p>That makes it quiet and a little austere. Visitors walk in from Miwa Station, bow at an unusual gate, pray at a hall that faces a wooded hill, and leave. This guide covers what you are looking at, what the cedar ball and the snake are about, and what to know if you want to climb the mountain itself.</p>

    <h2 id="mountain">Mount Miwa and Omononushi<span class="h2-jp">三輪山と大物主</span></h2>
    <p>Nippon.com describes Mount Miwa as a 467-metre peak in the southeast corner of the Nara basin, honoured as the shrine&rsquo;s tutelary deity. The shrine is one of Japan&rsquo;s oldest, and its founding is recorded in the Kojiki and Nihon Shoki. Because the shrine is dedicated to the whole mountain, it has no honden; rites take place in the haiden. Japan-guide is careful on age: it says the exact date is unknown and that this is thought to be one of the oldest shrines, if not the oldest.</p>
    <p>The god is Omononushi. In the story Nippon.com summarises, he appeared before Okuninushi, offered his help in finishing the land and asked to be enshrined on Mount Miwa. If you know the Izumo side of that story, see our """+a('/guides/izumo-taisha/','Izumo Taisha guide','izumo')+""" and the """+a('/culture/japanese-mythology/','mythology guide','mythology')+""". Nippon.com adds that for centuries no one could climb the mountain or touch its trees, which is why old pine, cedar and cypress still cover the summit.</p>
    <p>The lack of a main hall is not a gap. It is one of the clearest examples of the idea in our """+a('/culture/shrine-architecture/','shrine architecture guide','architecture')+""": some kami are a mountain, and the building only needs to give you somewhere to stand.</p>

    <h2 id="approach">Walking In: Torii and Approach<span class="h2-jp">鳥居と参道</span></h2>
"""+fig('nitorii','Stone pillar inscribed with the shrine name beside a wooden torii with a green plaque, a small signboard nearby and trees behind','The stone marker and the second torii at the entrance',None)+"""
    <p>From Miwa Station, Live Japan says it takes about 5 minutes to reach the Ni no Torii, the second torii, and that going through it brings you onto the sacred grounds. In the photo, a stone pillar carries the shrine name beside the wooden torii, and a small signboard stands nearby. The signboard&rsquo;s characters read 玄山 as I read them, but I could not tell what it marks.</p>
"""+fig('torii','Large dark wooden torii with a horizontal plaque reading the name Miwa Myojin, seen from the front with trees behind','The second torii, with its plaque reading Miwa Myojin',None)+"""
    <p>Tabiiro reports that the plaque on this torii reads 三輪明神 (<em>Miwa Myojin</em>), an older name for the shrine&rsquo;s god. The same source says the first torii is a large one of over 30 metres, from which the mountain can be seen.</p>

    <h2 id="hall">The Worship Hall and the Triple Torii<span class="h2-jp">拝殿と三ツ鳥居</span></h2>
    <p>Matcha says the haiden is said to have been first built in the Kamakura period, but the present building dates from 1664, rebuilt by the shogun Tokugawa Ietsuna. It has a gabled roof of cypress bark with a curved <em>karahafu</em> gable on the front. GLTJP says the hall and the three torii behind it are designated Important Cultural Properties.</p>
"""+fig('pano3','Wide view of the lawn and gravel in front of the worship hall, with the hall and cedar trees along the right and a few visitors','The grounds in front of the worship hall, in a wide view',None)+"""
    <p>The wide view shows how open the front of the hall is. The photo is a panorama, so the proportions are stretched sideways, and the date is unknown.</p>
    <p>Behind the hall stands the <em>mitsu-torii</em>, three torii joined together, through which the mountain is worshipped (Matcha, japan-guide). Japan-guide calls the style ancient and extremely rare. To see it, you need to ask at the shrine office and be guided by a priest (japan-guide); Tsunagu Japan describes it as a special worship that needs an application. A similar triple torii stands at Hibara Shrine, about a 20-minute walk north along the Yamanobe-no-michi trail (japan-guide).</p>
    <p>Nippon.com also notes that the torii in front of the hall is only two posts joined by a sacred rope, with no crossbeam. It is worth a pause before you walk on.</p>

    <h2 id="sugidama">Sake, Cedar Balls and the Snake<span class="h2-jp">杉玉と巳さん</span></h2>
    <p>Omononushi is also the patron of sake. Nippon.com says the cedar balls (<em>sugidama</em>) that hang at breweries and shops to signal a new brew are often supplied from this shrine. The big one in the haiden is about 1.7 metres across and about 250 kilograms, and a fresh green ball replaces it every autumn. Our """+a('/guides/sake-shrines/','sake and shrines guide','sake')+""" covers the wider tradition.</p>
    <p>The snake is the other signature. Matcha says a white snake, regarded as a form of Omononushi, is believed to live in a cedar of about 500 years old in front of the haiden, and that visitors leave eggs because snakes are thought to like them. Tabi-mag calls the snake a familiar &ldquo;Mi-san&rdquo; and says the white snake is a manifestation of the god. Matcha also mentions a bronze rabbit in the vestibule of the sanshuden, said to cure aches when stroked; its polished look shows how often it is touched.</p>

    <h2 id="sai">Sai Shrine and the Climb<span class="h2-jp">狭井神社と三輪山登拝</span></h2>
    <p>Walking from the haiden to Sai Shrine takes about four minutes along the &ldquo;medicine path&rdquo;, lined with medicinal plants given by people in the pharmaceutical industry (Tabiiro, GLTJP). Tabiiro says Sai Shrine enshrines the rough spirit of the mountain&rsquo;s god and is worshipped for recovery from illness, and that water from the well beside it is believed to cure disease. Matcha adds that many visitors take the water home.</p>
    <p>Sai Shrine is also where you register to climb Mount Miwa. Nippon.com says pilgrims have been allowed to climb only since the Meiji period, must apply for permission, wear a white sash and carry a gohei staff, and may not eat, drink, smoke or photograph. Matcha (2017) and Live Japan give registration as 9:00 to 14:00 for 300 yen, with a return to Sai Shrine by 16:00 and a round trip of about 2 to 3 hours on a steep path. Matcha also lists closing days and says foreign visitors need basic Japanese or a Japanese companion. These details are several years old, so confirm them with the shrine before you go.</p>

    <h2 id="visit">Visiting Omiwa Shrine<span class="h2-jp">参拝案内</span></h2>
    <ul class="practical-list">
      <li><strong>Address:</strong> 1422 Miwa, Sakurai City, Nara 633-8538 (GLTJP). Phone 0744-42-6633.</li>
      <li><strong>By train:</strong> JR Sakurai Line (Man&rsquo;yo Mahoroba Line) to Miwa Station. About 5 minutes on foot (Nippon.com, GLTJP, Lonely Planet) or 10 (japan-guide). From JR Nara, about 25 minutes and 330 yen (japan-guide), twice an hour.</li>
      <li><strong>Hours and fees:</strong> the grounds are always open and free. Japan-guide gives 9:00 to 17:00 for the shrine office; GLTJP gives 8:00 to 17:00 for the goshuin office. Confirm on the shrine&rsquo;s site (oomiwa.or.jp).</li>
      <li><strong>Walking trail:</strong> the shrine is at the south end of the Yamanobe-no-michi; the most popular section from Isonokami Shrine takes three to four hours (JNTO).</li>
      <li><strong>Time needed:</strong> one to two hours for the main grounds (Kupi, a general guide); plan 2 to 3 hours extra for the climb.</li>
    </ul>
    <div class="key-callout">
      <p>&#127890; <strong>Plan your trip:</strong> Browse guided tours or find a stay in Nara. <a href="https://www.viator.com/search/Nara?pid=P00298374&amp;mcid=42383&amp;medium=link&amp;campaign=sacred-japan" target="_blank" rel="noopener" onclick="trackEvent('click','affiliate','viator_omiwa')">Book a Tour</a></p>
    </div>

    <h2 id="faq">Frequently Asked Questions<span class="h2-jp">よくあるご質問</span></h2>
    <div class="faq-stack">
"""+''.join(f"""    <details class="faq-item">
        <summary>{q}</summary>
        <div class="faq-answer">{a_}</div>
    </details>
""" for q,a_ in faqs)+"""    </div>

    <h2 id="final">Before You Go<span class="h2-jp">むすびに</span></h2>
    <p>Come on a quiet weekday if you can, bow at the torii, and spend a moment at the haiden facing the trees. There is no building to look at, and that is the point.</p>

    <div class="closing-block">
      <span class="torii">&#9961;&#65039;</span>
      <p>A mountain for a god, and a hall built only to face it.</p>
    </div>

    <section class="related-section">
      <h2>Related Guides</h2>
      <span class="h2-jp">関連ガイド</span>
      <div class="related-grid">
        <a class="related-card" href="/guides/sake-shrines/" onclick="trackEvent('click','internal','related_omiwa_to_sake')">
          <div class="related-card-label">SACRED JAPAN ／ GUIDES</div>
          <div class="related-card-title">&#127862; Sake and Shrines &rarr;</div>
          <div class="related-card-desc">Why sake is offered to the gods, and the cedar ball of Omiwa.</div>
        </a>
        <a class="related-card" href="/culture/shrine-architecture/" onclick="trackEvent('click','internal','related_omiwa_to_architecture')">
          <div class="related-card-label">SACRED JAPAN ／ CULTURE</div>
          <div class="related-card-title">&#9961;&#65039; Shrine Architecture &rarr;</div>
          <div class="related-card-desc">Styles, roofs and the shrines that need no main hall.</div>
        </a>
        <a class="related-card" href="/guides/izumo-taisha/" onclick="trackEvent('click','internal','related_omiwa_to_izumo')">
          <div class="related-card-label">SACRED JAPAN ／ GUIDES</div>
          <div class="related-card-title">&#9961;&#65039; Izumo Taisha &rarr;</div>
          <div class="related-card-desc">The shrine of Okuninushi, whom Omononushi came to help.</div>
        </a>
      </div>
    </section>

  </article>

"""
tail=tail.replace('gifu-castle',SL).replace('gifu_castle','omiwa').replace('DGifu','DNara').replace('search/Gifu','search/Nara')
def L(u,l,t): return f'<a href="{u}" target="_blank" rel="noopener" style="color:var(--beni);text-decoration:underline;" onclick="trackEvent(\'click\',\'external\',\'{l}\')">{t}</a>'
src='Sources verified at time of writing: '+', '.join([
 L('https://nippon.com/en/guide-to-japan/gu009007','src_om_nippon','Nippon.com'),
 L('https://www.japan-guide.com/e/e4190.html','src_om_jg','japan-guide'),
 L('https://www.gltjp.com/en/directory/item/12208/','src_om_gltjp','GLTJP'),
 L('https://matcha-jp.com/en/5057?page=2','src_om_matcha','Matcha (2017)'),
 L('https://livejapan.com/en/in-kansai/in-pref-nara/in-nara-suburbs/article-a2000237','src_om_live','Live Japan'),
 L('https://tabiiro.jp/likes/articles/view/2131/','src_om_tabiiro','Tabiiro'),
 L('https://tabi-mag.jp/oomiwa/','src_om_tabimag','Tabi-mag'),
 L('https://tsunagujapan.com/oomiwajinja','src_om_tsunagu','Tsunagu Japan'),
 L('https://www.lonelyplanet.com/points-of-interest/omiwa-jinja/1612633','src_om_lp','Lonely Planet'),
 L('https://www.japan.travel/japans-local-treasures/yamanobe-no-michi-trail-2022/','src_om_jnto','JNTO'),
])+'. Hours, prices and availability change'
tail,n=re.subn(r'Sources verified at time of writing:.*?Hours, prices and availability change',lambda m:src,tail,flags=re.S); assert n==1
out=head+main+tail
assert not re.search('Gifu|Nobunaga|Kinka',re.sub(r'"mainEntity": \[.*','',out,flags=re.S))
open(D+'index.html','w',encoding='utf-8').write(out)
for tg in ['div','figure','picture','p','a','ul','li','details','section','h2']:
    assert len(re.findall(f'<{tg}[ >]',out))==len(re.findall(f'</{tg}>',out)),tg
for m in re.findall(r'<script type="application/ld\+json">(.*?)</script>',out,re.S): json.loads(m)
im=Image.open(R+'images/og/og-guides-matsue-castle.jpg').convert('RGB'); d=ImageDraw.Draw(im)
d.rectangle([40,150,1170,380],fill=(252,240,242)); d.rectangle([1118,66,1160,96],fill=(252,240,242))
f1=ImageFont.truetype(glob.glob('/usr/share/fonts/**/DejaVuSerif-Bold.ttf',recursive=True)[0],48)
f2=ImageFont.truetype(glob.glob('/usr/share/fonts/**/NotoSerifCJK-Bold.ttc',recursive=True)[0],28,index=0)
l1="Omiwa Shrine Guide:"; l2="No Main Hall, Only a Mountain"; assert d.textlength(l2,font=f1)<1090
d.text((66,170),l1,font=f1,fill=(26,15,15)); d.text((66,238),l2,font=f1,fill=(26,15,15)); d.text((66,332),"大神神社",font=f2,fill=(138,125,120))
im.save(R+f'images/og/og-guides-{SL}.jpg',quality=88)
b=Image.open(D+'images/haiden.jpg'); w,h=b.size; ch=round(w*400/640); t=max(0,(h-ch)//2)
th=b.crop((0,t,w,t+ch)).resize((640,400),Image.LANCZOS); th.save(R+f'images/hub/{SL}.jpg',quality=84); th.save(R+f'images/hub/{SL}.webp',quality=80)
print('built',len(out))
