import re,json,os,glob
from PIL import Image,ImageDraw,ImageFont
R='/home/claude/sacred-japan/'; SL='hokkaido-jingu'; D=R+f'guides/{SL}/'
os.makedirs(D+'images',exist_ok=True); UP='/mnt/user-data/uploads/'
LIC={'by3':('CC BY 3.0','https://creativecommons.org/licenses/by/3.0/'),
     'bysa2':('CC BY-SA 2.0','https://creativecommons.org/licenses/by-sa/2.0/'),
     'bysa3':('CC BY-SA 3.0','https://creativecommons.org/licenses/by-sa/3.0/'),
     'bysa4':('CC BY-SA 4.0','https://creativecommons.org/licenses/by-sa/4.0/')}
def CS(t): return 'https://commons.wikimedia.org/w/index.php?search='+t+'&title=Special:MediaSearch&type=image'
LEE=CS('lienyuan%20lee%20Hokkaido%20Shrine')
TSU=CS('Hideshi%20Tsunematsu%20Hokkaido%20Shrine')
P={ # slug:(upload,author,lic,link)
'torii-snow':('138eed1d','t-konno','bysa3',CS('Hokkaido%20Shrine%20Torii%20in%20the%20snow')),
'torii':('0cb44c8b','lienyuan lee','by3',LEE),
'approach':('b1feae05','danobrienmuzyka','bysa2','https://www.flickr.com/photos/60098295@N00/3475176280'),
'shinmon-inside':('864aed36','Hideshi Tsunematsu','by3',TSU),
'shinmon-rain':('62505a8e','lienyuan lee','by3',LEE),
'shinmon-snow':('f088901a','bryan&hellip; (Flickr)','bysa2','https://www.flickr.com/photos/91049143@N00/16696341536'),
'temizuya':('55c87ec0','Hideshi Tsunematsu','by3',TSU),
'haiden-summer':('b12feed6','Daigaku2051','bysa3',CS('Daigaku2051%20Hokkaido%20Jingu')),
'haiden-front':('cade2646','lienyuan lee','by3',LEE),
'haiden-side':('f30060c2','lienyuan lee','by3',LEE),
'tongu':('6d5f0578','Pundit','bysa4',CS('Pundit%20Hokkaido%20Jingu%20Tongu')),
}
if not os.path.exists(D+'images/torii-snow.jpg'):
    for k,v in P.items():
        im=Image.open(UP+v[0]+'-image.jpg').convert('RGB'); w,h=im.size
        if w>1200: im=im.resize((1200,round(h*1200/w)),Image.LANCZOS)
        im.save(D+f'images/{k}.jpg',quality=84); im.save(D+f'images/{k}.webp',quality=80)
SIZE={k:Image.open(D+f'images/{k}.jpg').size for k in P}
def fig2(k,alt,cap,hero=False):
    u,a,l,cl=P[k]; ln,lu=LIC[l]; w,h=SIZE[k]
    if hero: st='margin:0 0 48px;'; ld='eager'; ims='style="width:100%;max-height:420px;object-fit:cover;border-radius:4px;display:block;"'
    else:
        st='margin:28px auto;max-width:%s;'%('420px' if h>w else '760px'); ld='lazy'; ims='style="width:100%;height:auto;border-radius:4px;display:block;"'
    lic=f'public domain (photographic reproduction of a print)' if l=='pd' else f'<a href="{lu}" target="_blank" rel="noopener">{ln}</a>'
    return f'''<figure style="{st}"><picture><source srcset="/guides/{SL}/images/{k}.webp" type="image/webp"><img src="/guides/{SL}/images/{k}.jpg" alt="{alt}" width="{w}" height="{h}" loading="{ld}" {ims}></picture><figcaption style="font-size:13px;color:var(--enshu);margin-top:10px;text-align:center;line-height:1.6;">{cap}.<br>{'Artist' if l=='pd' else 'Photo'}: <a href="{cl}" target="_blank" rel="noopener">{a}</a>, {lic}, via Wikimedia Commons (resized)</figcaption></figure>
'''
fig=fig2
s=open(R+'guides/gifu-castle/index.html',encoding='utf-8').read()
i=s.index('<main>'); j=s.index('</main>'); head,tail=s[:i],s[j:]
TITLE="Hokkaido Jingu Guide: Sapporo's Pioneer Shrine, Snowy Torii and the Hangan-sama Mochi"
DESC="A licensed guide's guide to Hokkaido Jingu in Sapporo: the three pioneer gods, the 1974 fire and 1978 rebuild, the torii and Shinmon gate through the seasons, the Tongu branch shrine, hatsumode, cherry blossoms and how to get there."
TAG="Sapporo's forest shrine, built for the gods of Hokkaido's settlement and shown here from torii to haiden in photos."
head=re.sub(r'<title>.*?</title>',f'<title>{TITLE} | Sacred Japan</title>',head,count=1)
head=re.sub(r'(<meta (?:name="description"|property="og:description"|name="twitter:description") content=")[^"]*(")',lambda m:m.group(1)+DESC+m.group(2),head)
head=re.sub(r'(<meta (?:property="og:title"|name="twitter:title") content=")[^"]*(")',lambda m:m.group(1)+TITLE+m.group(2),head)
head=re.sub(r'("headline": ")[^"]*(")',lambda m:m.group(1)+TITLE+m.group(2),head)
head=re.sub(r'("description": ")A licensed[^"]*(")',lambda m:m.group(1)+DESC+m.group(2),head)
head=re.sub(r'("date(?:Published|Modified)": ")[^"]*(")',lambda m:m.group(1)+'2026-11-25'+m.group(2),head)
head=re.sub(r'<meta name="keywords" content="[^"]*">','<meta name="keywords" content="Hokkaido Jingu, Hokkaido Shrine, Sapporo shrine, Maruyama Park, Hokkaido Jingu hatsumode, Hangan-sama, Sapporo Festival, Hokkaido Jingu access, Sapporo cherry blossoms">',head)
head=head.replace('guides/gifu-castle',f'guides/{SL}').replace('guide_gifu_castle_','guide_hokkaido_jingu_').replace('og-guides-gifu-castle',f'og-guides-{SL}')
head=head.replace('岐阜城','北海道神宮').replace('Gifu Castle','Hokkaido Jingu')
head=re.sub(r"<h1>.*?</h1>","<h1><em>Hokkaido Jingu</em>: Sapporo's Pioneer Shrine, Snowy Torii and the Hangan-sama Mochi</h1>",head,count=1,flags=re.S)
head=head.replace("Nobunaga's mountain castle above Gifu, with the keep closed until late 2027.",TAG)
head=head.replace('SACRED JAPAN GUIDES ／ 城','SACRED JAPAN GUIDES ／ 神社')
IL='class="inline-link"'
def a(u,t,ev): return f'<a href="{u}" {IL} onclick="trackEvent(\'click\',\'internal\',\'guide_hokkaido_jingu_to_{ev}\')">{t}</a>'
faqs=[
("Who is enshrined at Hokkaido Jingu?","Four kami: Okunitama, Onamuchi (Okuninushi) and Sukunahikona, the three &ldquo;pioneer gods&rdquo; who were enshrined by imperial order in 1869, and Emperor Meiji, added in 1964 (JNTO, GLTJP, LIVE JAPAN)."),
("Why is the shrine only about 60 years old in its present form?","The shrine was founded in the Meiji era, so it is young by Japanese standards. The main hall burned down in 1974 and was rebuilt in 1978 (JNTO, Wikipedia). The name changed from Sapporo Shrine to Hokkaido Jingu in 1964 (GLTJP)."),
("Is there an admission fee, and what are the hours?","Admission is free. GLTJP lists seasonal hours: 6:00 to 17:00 from April to October, 7:00 to 17:00 in March, and 7:00 to 16:00 in February and from November to December. New Year hours are different (open from midnight on 1 January). Hours can change, so check the official site."),
("How do I get to Hokkaido Jingu?","Take the Tozai subway line to Maruyama-Koen Station, then walk about 15 minutes through the park (JNTO, Visit Hokkaido). From Sapporo Station it is a 2-minute ride to Odori and then about 7 minutes on the Tozai line (JNTO). JR buses from the station stop about 4 minutes on foot from the shrine (LIVE JAPAN)."),
("What is Hangan-sama?","It is a grilled rice-cake sweet with red-bean paste sold at the shrine&rsquo;s tea shops. LIVE JAPAN and GLTJP link the name to Shima Yoshitake, the official who laid out Sapporo&rsquo;s streets, and a statue of him stands in front of the main hall. You may also read that it refers to Minamoto no Yoshitsune; I found the Shima Yoshitake explanation in the more careful sources. It is not sold from 1 to 11 January (LIVE JAPAN)."),
("When is the Sapporo Festival and when is hatsumode busiest?","The Hokkaido Shrine Festival (Sapporo Festival) runs 14 to 16 June, with the main procession of mikoshi and floats on the 16th (Sapporo Tourism). The first three days of January are the most crowded for hatsumode, and LIVE JAPAN suggests going from 4 January to avoid the crush."),
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
      <li><a href="#opening">A Shrine for People Starting Over</a></li>
      <li><a href="#history">History: Four Kami, One Fire</a></li>
      <li><a href="#torii">The Torii and the Approach</a></li>
      <li><a href="#shinmon">The Shinmon Gate in Three Weathers</a></li>
      <li><a href="#halls">Water, Haiden and Roof</a></li>
      <li><a href="#tongu">The Tongu in the City</a></li>
      <li><a href="#seasons">Hatsumode, Blossoms and the June Festival</a></li>
      <li><a href="#getting-there">Getting There</a></li>
      <li><a href="#visit">Visiting Hokkaido Jingu</a></li>
      <li><a href="#faq">Frequently Asked Questions</a></li>
      <li><a href="#final">Before You Go</a></li>
    </ol>
  </aside>

  <article>

"""+fig('torii-snow','The large torii of Hokkaido Jingu under snow at New Year, with a crowd of visitors, a snow-covered stone lantern and a route map board','The large torii under snow at hatsumode, the first shrine visit of the year',hero=True)+"""
    <p class="opening" id="opening">As a licensed guide, I describe Hokkaido Jingu to visitors as a shrine for people who are starting something. Most of the great shrines of Honshu stand on a thousand years of history. This one has a date you can say out loud: 1869, when the Meiji government ordered the gods of Hokkaido&rsquo;s settlement to be enshrined, in the same year the island received its present name.</p>
    <p>It sits in a forest of about 180,000 square metres beside Maruyama Park in Sapporo. This guide walks the precinct in photos, from the torii to the haiden, with the history, the festival and the practical details.</p>

    <h2 id="history">History: Four Kami, One Fire<span class="h2-jp">由緒</span></h2>
    <p>In 1869, by order of Emperor Meiji, a ceremony was held to enshrine three kami to watch over the development of Hokkaido: Okunitama, Onamuchi (Okuninushi) and Sukunahikona (Wikipedia, JNTO). The shrine was then called Sapporo Jinja. LIVE JAPAN says the gods were enshrined at the present site in 1871. In 1964 Emperor Meiji was added as the fourth deity and the name became Hokkaido Jingu (GLTJP).</p>
    <p>The main hall burned down in 1974 and was restored in 1978 (JNTO). GLTJP says the rebuilding took four years. The halls you see today are therefore postwar buildings in a Meiji-era shrine, which is part of why the place feels clean and open rather than old and mossy.</p>

    <h2 id="torii">The Torii and the Approach<span class="h2-jp">鳥居と参道</span></h2>
    <p>The photograph at the top shows the torii at hatsumode. The crowd is bundled up, a stone lantern wears a cap of snow, and a board with a route map stands beside the path, which hints at how many people the shrine has to move through at New Year.</p>
"""+fig('torii','A large dark metal torii beside a stone pillar reading Hokkaido Jingu and a notice board, with visitors under umbrellas and granite steps','A great torii beside the stone pillar reading <span lang="ja">北海道神宮</span>, photographed in 2003')+"""
    <p>Here the large torii stands beside a stone pillar engraved with the shrine&rsquo;s name, with a notice board and a few visitors under umbrellas. GLTJP describes several torii on the way in: a first torii about 19 m tall and outside the grounds, a second at the entrance of the approach, a third near the parking area, and a stainless-steel &ldquo;Reiwa torii&rdquo; built for the 150th anniversary of the enshrinement. I cannot tell you which of these this photograph shows, so treat the labels as a guide to the sequence rather than a caption.</p>
"""+fig('approach','A long straight gravel approach lined with trees and stone lanterns leading toward the inner shrine','The gravel approach, lined with trees and stone lanterns, photographed in 2009')+"""
    <p>Beyond the gate the approach is a long, straight gravel road between trees and stone lanterns. This is where the city drops away. The image is small and low in resolution, but it shows the main point: the shrine is arranged as a walk through a forest, not a short climb to a hall.</p>

    <h2 id="shinmon">The Shinmon Gate in Three Weathers<span class="h2-jp">神門</span></h2>
"""+fig('shinmon-inside','The Shinmon gate seen from the courtyard under a snow-covered roof, with a large drum beside the opening and the approach visible beyond','The Shinmon seen from the courtyard, the snowy approach framed in its opening')+"""
    <p>This view is from the courtyard side, looking back out through the gate. The roof is covered in fresh snow, five gold-capped logs sit along the ridge, and a large drum stands beside the opening, with the approach visible beyond like a framed picture. The wet pavement in front shows that this was a thawing day. The drum is a reminder that the gate marks the point where the ordinary precinct ends.</p>
"""+fig('shinmon-rain','The Shinmon gate in rain with a thick shimenawa rope and white shide hanging in the opening, visitors under umbrellas on the steps','The Shinmon in rain, with a heavy shimenawa across the opening (photographed in 2003)')+"""
    <p>In rain the same gate looks different. A thick shimenawa rope hangs across the opening with white paper shide, and visitors with umbrellas climb the steps. The wet roof darkens the whole building, so the gold fittings stand out more.</p>
"""+fig('shinmon-snow','The Shinmon gate in light snowfall, with snow on the roof and a shimenawa above the stone steps, visitors in winter coats','The Shinmon in light snow, February 2015')+"""
    <p>Hokkaido gives you the third version. Light snow falls, the steps are dusted white, and the visitors wear winter coats. If you can choose, a snowy weekday morning gives the most atmosphere, though you should allow time for cold hands and slippery steps.</p>

    <h2 id="halls">Water, Haiden and Roof<span class="h2-jp">手水舎と拝殿</span></h2>
"""+fig('temizuya','A purification pavilion with water flowing from wooden spouts, with the roof of a hall blurred in the background','The water pavilion, with the roof of a hall softly out of focus behind it')+"""
    <p>Before the hall comes the chozuya, where water runs from wooden spouts. The roof of a shrine building appears out of focus in the background. If the steps are new to you, our """+a('/culture/shrine-etiquette/','shrine etiquette guide','etiquette')+""" covers them.</p>
"""+fig('haiden-summer','The haiden in summer light with visitors in front, crossed chigi on the roof and a stepped paved terrace','The haiden in summer, with the green trees behind (photographed in 2007)')+"""
    <p>In summer the worship hall stands under a broad roof against green trees, with visitors on the paved terrace in front. The crossed chigi and the logs along the ridge are the most obvious features. If you want to know what those are and why shrine roofs carry them, see our """+a('/culture/shrine-architecture/','guide to shrine architecture','architecture')+""".</p>
"""+fig('haiden-front','The front of the haiden with crossed chigi, a white curtain bearing a chrysanthemum crest, and offering boxes with gold crests, with traffic cones and a worker','The haiden from the front, with a white curtain, offering boxes and a worker (photographed in 2003)')+"""
    <p>From the front you see the white curtain with its chrysanthemum crest and the offering boxes with gold crests. Traffic cones and a worker show that repairs were under way, which is a reminder that a visit can include scaffolding or work areas; check what is closed before you go.</p>
"""+fig('haiden-side','The front-left corner of the haiden with its gold fittings, crossed chigi, a white curtain with chrysanthemum crests, and construction cones','The corner of the haiden, with gold fittings and crossed chigi')+"""
    <p>This angle shows the front-left corner of the roof, with gold fittings, crossed chigi and the white curtain again. The timber framing under the eaves is the part I would look at slowly, because it is what the 1978 reconstruction was built from.</p>

    <h2 id="tongu">The Tongu in the City<span class="h2-jp">頓宮</span></h2>
"""+fig('tongu','A stone torii with pink banners and white lanterns marked as a tongu, with a small haiden and a chrysanthemum curtain beyond','The torii of the Tongu, Hokkaido Jingu&rsquo;s branch shrine in Sapporo (photographed in 2017)')+"""
    <p>If you do not have time to go out to Maruyama, there is a smaller branch shrine in central Sapporo, called a <em>tongu</em>. The sign reads <span lang="ja">頓宮</span> as I read it. A stone torii stands at the gate, pink banners with wishes line the path, white lanterns hang, and a small haiden with a chrysanthemum curtain waits beyond. It is not a substitute for the main shrine, but it is a quick stop in the city.</p>

    <h2 id="seasons">Hatsumode, Blossoms and the June Festival<span class="h2-jp">季節</span></h2>
    <p><strong>New Year.</strong> Hatsumode is the busiest time. The gates open from midnight on 1 January, and the first three days are the most crowded (GLTJP, LIVE JAPAN). LIVE JAPAN suggests going from 4 January. Guides give attendance figures in the hundreds of thousands; I have not found an official count, so treat those as estimates. A parking management fee of &yen;500 applies over this period.</p>
    <p><strong>Blossoms.</strong> The grounds hold roughly 1,100 cherry trees (Ezo-yamazakura, Somei Yoshino and yaezakura) and over 200 plum trees; the best viewing is late April to early May (GLTJP). The plum grove lies between the second torii and the park entrance torii.</p>
    <p><strong>June festival.</strong> The Hokkaido Shrine Festival, also called the Sapporo Festival, runs 14 to 16 June. On the 16th, more than a thousand people in Heian-style costume parade with four mikoshi and several floats from the shrine to central Sapporo (Sapporo Tourism; the number of floats is given as eight or nine depending on the year).</p>
    <p><strong>Sweets and sub-shrines.</strong> Jingu Chaya and a neighbouring tea shop sell Hangan-sama, a grilled rice-cake sweet; hours are about 9:00 to 16:00 (LIVE JAPAN). Three sub-shrines stand in the grounds: Kaitaku Jinja, built in 1938 for those who contributed to Hokkaido&rsquo;s settlement; Korei Jinja, for miners; and Hotaki Jinja, linked to money luck (GLTJP, LIVE JAPAN). A goshuin is &yen;300 at the prayer reception (Sapporo Tourism).</p>

    <h2 id="getting-there">Getting There<span class="h2-jp">アクセス</span></h2>
    <p>The usual route is the Tozai subway line to Maruyama-Koen Station, then about 15 minutes on foot through Maruyama Park (JNTO, Visit Hokkaido). From Sapporo Station, ride 2 minutes to Odori and change for 7 minutes to Maruyama-Koen (JNTO). JR buses (En15, En16, Circular West 20 and 21) run from the station area to a stop about 4 minutes from the shrine (LIVE JAPAN). Parking is free, with about 230 spaces (Visit Hokkaido).</p>

    <h2 id="visit">Visiting Hokkaido Jingu<span class="h2-jp">参拝案内</span></h2>
    <ul class="practical-list">
      <li><strong>Address:</strong> 474 Miyagaoka, Chuo-ku, Sapporo.</li>
      <li><strong>Getting there:</strong> Maruyama-Koen Station (Tozai line), then a 15-minute walk through Maruyama Park.</li>
      <li><strong>Fees and hours:</strong> free; about 6:00 to 17:00 from April to October and 7:00 to 16:00 from November to February (GLTJP lists seasonal variations and New Year hours). Check the official site before you go.</li>
      <li><strong>Goshuin:</strong> &yen;300 at the prayer reception (Sapporo Tourism).</li>
      <li><strong>Best times:</strong> late April to early May for blossoms; 14 to 16 June for the festival; 4 January or later to avoid the worst New Year crowds.</li>
      <li><strong>Pair it with:</strong> a walk through Maruyama Park, and our """+a('/culture/shrine-etiquette/','shrine etiquette guide','etiquette_pair')+""" if you are new to shrines.</li>
    </ul>
    <div class="key-callout">
      <p>&#127890; <strong>Plan your trip:</strong> Browse guided tours or find a stay in Sapporo. <a href="https://www.viator.com/search/Sapporo%20Hokkaido?pid=P00298374&amp;mcid=42383&amp;medium=link&amp;campaign=sacred-japan" target="_blank" rel="noopener" onclick="trackEvent('click','affiliate','viator_hokkaido_jingu')">Book a Tour</a></p>
    </div>

    <h2 id="faq">Frequently Asked Questions<span class="h2-jp">よくあるご質問</span></h2>
    <div class="faq-stack">
"""+''.join(f"""    <details class="faq-item">
        <summary>{q}</summary>
        <div class="faq-answer">{a_}</div>
    </details>
""" for q,a_ in faqs)+"""    </div>

    <h2 id="final">Before You Go<span class="h2-jp">むすびに</span></h2>
    <p>Go in the morning, walk the approach slowly, and look at the Shinmon before you look at the hall. In snow, in rain or in summer, it is the gate that gives the shrine its character.</p>

    <div class="closing-block">
      <span class="torii">&#9961;&#65039;</span>
      <p>A shrine for the people who arrived with nothing, and for anyone starting again.</p>
    </div>

    <section class="related-section">
      <h2>Related Guides</h2>
      <span class="h2-jp">関連ガイド</span>
      <div class="related-grid">
        <a class="related-card" href="/culture/shrine-etiquette/" onclick="trackEvent('click','internal','related_hokkaido_jingu_to_etiquette')">
          <div class="related-card-label">SACRED JAPAN ／ CULTURE</div>
          <div class="related-card-title">&#9961;&#65039; Shrine Etiquette &rarr;</div>
          <div class="related-card-desc">How to bow, purify and pray at a shrine.</div>
        </a>
        <a class="related-card" href="/culture/shrine-architecture/" onclick="trackEvent('click','internal','related_hokkaido_jingu_to_architecture')">
          <div class="related-card-label">SACRED JAPAN ／ CULTURE</div>
          <div class="related-card-title">&#127983;&#65039; Shrine Architecture &rarr;</div>
          <div class="related-card-desc">Read the roofs and halls you have just seen.</div>
        </a>
        <a class="related-card" href="/culture/goshuin-guide/" onclick="trackEvent('click','internal','related_hokkaido_jingu_to_goshuin')">
          <div class="related-card-label">SACRED JAPAN ／ CULTURE</div>
          <div class="related-card-title">&#128215; Goshuin Guide &rarr;</div>
          <div class="related-card-desc">Collecting the shrine stamps.</div>
        </a>
      </div>
    </section>

  </article>

"""
tail=tail.replace('gifu-castle',SL).replace('gifu_castle','hokkaido_jingu').replace('DGifu','DSapporo%20Hokkaido').replace('search/Gifu','search/Sapporo%20Hokkaido')
def L(u,l,t): return f'<a href="{u}" target="_blank" rel="noopener" style="color:var(--beni);text-decoration:underline;" onclick="trackEvent(\'click\',\'external\',\'{l}\')">{t}</a>'
src='Sources verified at time of writing: '+', '.join([
 L('https://www.hokkaidojingu.or.jp','src_hj_official','Hokkaido Jingu official site'),
 L('https://www.gltjp.com/en/article/item/20333/','src_hj_gltjp','GLTJP'),
 L('https://livejapan.com/ms/in-hokkaido/in-pref-hokkaido/in-sapporo_chitose/article-a1000375/','src_hj_livejapan','LIVE JAPAN'),
 L('https://www.japan.travel/en/spot/1935/','src_hj_jnto','JNTO'),
 L('https://www.visit-hokkaido.jp/en/spot/detail_10001.html','src_hj_vh','Visit Hokkaido'),
 L('https://www.sapporo.travel/en/spot/facility/hokkaido_shrine/','src_hj_sapporo','Sapporo Tourism'),
 L('https://www.sapporo.travel/en/event/event-list/hokkaido_shrine_festival/','src_hj_festival','Sapporo Tourism (festival)'),
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
l1="Hokkaido Jingu Guide:"; l2="Sapporo's Pioneer Shrine"; assert d.textlength(l2,font=f1)<1090
d.text((66,170),l1,font=f1,fill=(26,15,15)); d.text((66,238),l2,font=f1,fill=(26,15,15)); d.text((66,332),"北海道神宮",font=f2,fill=(138,125,120))
im.save(R+f'images/og/og-guides-{SL}.jpg',quality=88)
b=Image.open(D+'images/torii-snow.jpg'); w,h=b.size; ch=round(w*400/640); t=max(0,(h-ch)//2)
th=b.crop((0,t,w,t+ch)).resize((640,400),Image.LANCZOS); th.save(R+'images/hub/hokkaido-jingu.jpg',quality=84); th.save(R+'images/hub/hokkaido-jingu.webp',quality=80)
print('built',len(out))
