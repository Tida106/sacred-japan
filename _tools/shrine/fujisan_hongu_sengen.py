import re,json,os,glob
from PIL import Image,ImageDraw,ImageFont
R='/home/claude/sacred-japan/'; SL='fujisan-hongu-sengen-taisha'; D=R+f'guides/{SL}/'
os.makedirs(D+'images',exist_ok=True); UP='/mnt/user-data/uploads/'
LIC={'by3':('CC BY 3.0','https://creativecommons.org/licenses/by/3.0/'),
     'bysa3':('CC BY-SA 3.0','https://creativecommons.org/licenses/by-sa/3.0/'),
     'bysa4':('CC BY-SA 4.0','https://creativecommons.org/licenses/by-sa/4.0/'),
     'cc0':('CC0 1.0','https://creativecommons.org/publicdomain/zero/1.0/')}
def CS(t): return 'https://commons.wikimedia.org/w/index.php?search='+t+'&title=Special:MediaSearch&type=image'
U=lambda n:'https://commons.wikimedia.org/wiki/User:'+n
ENNUI=U('Ennui'); MOC=U('Mocchy'); ZAI=U('Zairon'); EDO=U('%E6%B1%9F%E6%88%B8%E6%9D%91%E3%81%AE%E3%81%A8%E3%81%8F%E3%81%9E%E3%81%86')
P={ # slug:(upload,author,lic,link)
'daitorii':('1a2d6ae5','Ennui','cc0',ENNUI),
'tyouzuya':('2cf8987d','Ennui','cc0',ENNUI),
'romon':('9e908eae','Zairon','bysa4',ZAI),
'ema-ichiyo':('bd5cd2f1','江戸村のとくぞう','bysa4',EDO),
'ema-banpo':('6e052117','江戸村のとくぞう','bysa4',EDO),
'through-romon':('5a8833c2','江戸村のとくぞう','bysa4',EDO),
'haiden':('670e203b','Zairon','bysa4',ZAI),
'honden':('3f3998f0','Zairon','bysa4',ZAI),
'uketsukesho':('14875e3b','Ennui','bysa3',ENNUI),
'omamori':('22017cf5','jetalone','by3','https://www.flickr.com/photos/jetalone/2705949166/'),
'shingen':('b1dc6755','Mocchy','cc0',MOC),
'fujiview':('bc5477eb','Zairon','bysa4',ZAI),
'wakutama':('679dfa20','Mocchy','cc0',MOC),
'shiraito-green':('79f0397c','SHIZUOKACITYperson','bysa4',U('SHIZUOKACITYperson')),
'shiraito-autumn':('e56d4538','松岡明芳','bysa4',U('%E6%9D%BE%E5%B2%A1%E6%98%8E%E8%8A%B3')),
'yakisoba':('79fbc6d2','しんかわな','by3',U('%E3%81%97%E3%82%93%E3%81%8B%E3%82%8F%E3%81%AA')),
}
if not os.path.exists(D+'images/daitorii.jpg'):
    for k,v in P.items():
        f=UP+v[0]+('-image.png' if v[0]=='79f0397c' else '-image.jpg')
        im=Image.open(f).convert('RGB'); w,h=im.size
        if w>1200: im=im.resize((1200,round(h*1200/w)),Image.LANCZOS)
        im.save(D+f'images/{k}.jpg',quality=84); im.save(D+f'images/{k}.webp',quality=80)
SIZE={k:Image.open(D+f'images/{k}.jpg').size for k in P}
def fig2(k,alt,cap,hero=False):
    u,a,l,cl=P[k]; ln,lu=LIC[l]; w,h=SIZE[k]
    if hero: st='margin:0 0 48px;'; ld='eager'; ims='style="width:100%;max-height:420px;object-fit:cover;border-radius:4px;display:block;"'
    else:
        st='margin:28px auto;max-width:%s;'%('420px' if h>w else '760px'); ld='lazy'; ims='style="width:100%;height:auto;border-radius:4px;display:block;"'
    lic=f'<a href="{lu}" target="_blank" rel="noopener">{ln}</a>'
    return f'''<figure style="{st}"><picture><source srcset="/guides/{SL}/images/{k}.webp" type="image/webp"><img src="/guides/{SL}/images/{k}.jpg" alt="{alt}" width="{w}" height="{h}" loading="{ld}" {ims}></picture><figcaption style="font-size:13px;color:var(--enshu);margin-top:10px;text-align:center;line-height:1.6;">{cap}.<br>Photo: <a href="{cl}" target="_blank" rel="noopener">{a}</a>, {lic}, via Wikimedia Commons (resized)</figcaption></figure>
'''
fig=fig2
s=open(R+'guides/gifu-castle/index.html',encoding='utf-8').read()
i=s.index('<main>'); j=s.index('</main>'); head,tail=s[:i],s[j:]
TITLE="Fujisan Hongu Sengen Taisha Guide: Mt. Fuji's Head Shrine, Wakutama Pond and Sakura"
DESC="A licensed guide's guide to Fujisan Hongu Sengen Taisha in Fujinomiya: the head shrine of some 1,300 Sengen shrines, the two-storey 1604 hall, Wakutama Pond, cherry blossoms, ema, omamori, Shiraito Falls and how to get there."
TAG="The head shrine of Mt. Fuji, in Fujinomiya, shown here from the great torii to Wakutama Pond in photos."
head=re.sub(r'<title>.*?</title>',f'<title>{TITLE} | Sacred Japan</title>',head,count=1)
head=re.sub(r'(<meta (?:name="description"|property="og:description"|name="twitter:description") content=")[^"]*(")',lambda m:m.group(1)+DESC+m.group(2),head)
head=re.sub(r'(<meta (?:property="og:title"|name="twitter:title") content=")[^"]*(")',lambda m:m.group(1)+TITLE+m.group(2),head)
head=re.sub(r'("headline": ")[^"]*(")',lambda m:m.group(1)+TITLE+m.group(2),head)
head=re.sub(r'("description": ")A licensed[^"]*(")',lambda m:m.group(1)+DESC+m.group(2),head)
head=re.sub(r'("date(?:Published|Modified)": ")[^"]*(")',lambda m:m.group(1)+'2026-11-25'+m.group(2),head)
head=re.sub(r'<meta name="keywords" content="[^"]*">','<meta name="keywords" content="Fujisan Hongu Sengen Taisha, Fuji Sengen Shrine, Fujinomiya shrine, Wakutama Pond, Konohanasakuyahime, Mt Fuji shrine, Sengen shrine, Fujinomiya cherry blossoms, Shiraito Falls">',head)
head=head.replace('guides/gifu-castle',f'guides/{SL}').replace('guide_gifu_castle_','guide_fujisan_hongu_').replace('og-guides-gifu-castle',f'og-guides-{SL}')
head=head.replace('岐阜城','富士山本宮浅間大社').replace('Gifu Castle','Fujisan Hongu Sengen Taisha')
head=re.sub(r"<h1>.*?</h1>","<h1><em>Fujisan Hongu Sengen Taisha</em>: Mt. Fuji\'s Head Shrine, Wakutama Pond and Sakura</h1>",head,count=1,flags=re.S)
head=head.replace("Nobunaga's mountain castle above Gifu, with the keep closed until late 2027.",TAG)
head=head.replace('SACRED JAPAN GUIDES ／ 城','SACRED JAPAN GUIDES ／ 神社')
IL='class="inline-link"'
def a(u,t,ev): return f'<a href="{u}" {IL} onclick="trackEvent(\'click\',\'internal\',\'guide_fujisan_hongu_to_{ev}\')">{t}</a>'
faqs=[
("Who is enshrined at Fujisan Hongu Sengen Taisha?","The main deity is Konohanasakuya-hime, the goddess of Mt. Fuji. Her husband Ninigi and her father Oyamatsumi are enshrined with her (Wikipedia, All About Japan). The city of Fujinomiya describes her as a deity with the power of both fire and water, used to calm the mountain&rsquo;s eruptions."),
("Why is this called the head shrine of Sengen shrines?","It is regarded as the head of more than 1,300 Sengen (Asama) shrines across Japan, which honour Mt. Fuji and its deity (GLTJP, Fujinomiya city). All About Japan adds that it was recorded as the chief shrine (ichinomiya) of the old Suruga Province as early as the 10th century."),
("When was the shrine built, and who built the present halls?","Fujinomiya city says the shrine was established at its present site in 806, though the worship of Mt. Fuji itself pre-dates historical records. The present buildings date to 1604, when Tokugawa Ieyasu rebuilt them (Edo Legacy Travel, All About Japan). The main hall was repaired several times, notably after the 1854 earthquake (Wikipedia)."),
("Do I need to climb Mt. Fuji to see the shrine?","No. The shrine stands in the middle of Fujinomiya, not on the mountain. Everything above the 8th station is considered shrine land and has an inner shrine, but you do not need to climb for a normal visit. A shogunate decision of 1779 is cited for the 8th-station boundary (Openers; the shrine&rsquo;s own materials)."),
("How do I get there?","Walk 10 to 15 minutes from Fujinomiya Station on the JR Minobu Line, depending on the source (Yamanashi tourism says 10, JNTO says 15). Buses run once every one to two hours, take 5 to 10 minutes and cost 180 yen (japan-guide). SoraNews24 gives about 30 minutes by taxi or bus from Shin-Fuji Station on the Tokaido Shinkansen. Some guides name Nishi-Fujinomiya Station instead; check a map for your route."),
("When are the cherry blossoms and which events matter?","The grounds hold about 500 cherry trees, usually in bloom from late March to early April (GLTJP, japan-guide). GLTJP lists a yabusame (horseback archery) display on 5 May and the Fujinomiya Autumn Festival in November. Check the official calendar for exact dates."),
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
      <li><a href="#opening">The Front Door to Mt. Fuji</a></li>
      <li><a href="#history">History: Calming a Volcano</a></li>
      <li><a href="#approach">Torii, Water and the Romon</a></li>
      <li><a href="#ema">Ema and the Haiden</a></li>
      <li><a href="#honden">The Two-Storey Honden</a></li>
      <li><a href="#office">Reception Office and Omamori</a></li>
      <li><a href="#sakura">Sakura and Mt. Fuji</a></li>
      <li><a href="#wakutama">Wakutama Pond</a></li>
      <li><a href="#nearby">Shiraito Falls and Yakisoba</a></li>
      <li><a href="#visit">Visiting Fujisan Hongu Sengen Taisha</a></li>
      <li><a href="#faq">Frequently Asked Questions</a></li>
      <li><a href="#final">Before You Go</a></li>
    </ol>
  </aside>

  <article>

"""+fig('daitorii','A large vermilion torii with the plaque Fujisan Hongu and a snow-capped Mt. Fuji rising behind it on a clear day','The great vermilion torii, with the plaque <span lang="ja">冨士山本宮</span> as I read it and a snowy Mt. Fuji behind',hero=True)+"""
    <p class="opening" id="opening">As a licensed guide, I like to say that Mt. Fuji has many doors, but this is the oldest and the most traditional one. Fujisan Hongu Sengen Taisha stands in the middle of Fujinomiya, on the south-west side of the mountain, and it was long treated as the front door for pilgrims who climbed from here (All About Japan).</p>
    <p>The photograph above shows why people remember it: a vermilion torii with Fuji itself standing in the frame. This guide walks the shrine in sixteen photos, from the torii to the pond and out to the waterfall and noodles nearby.</p>

    <h2 id="history">History: Calming a Volcano<span class="h2-jp">由緒</span></h2>
    <p>The shrine exists because Mt. Fuji was once feared. Fujinomiya city says it was built to enshrine the mountain&rsquo;s deity and calm repeated eruptions, and that the spring water of Wakutama Pond on the grounds was believed to help. The deity is Konohanasakuya-hime, whom the city describes as having the power of both fire and water. Her husband Ninigi and father Oyamatsumi are enshrined with her. If you know the Kojiki story of the goddess who gave birth in fire, this is the place where it is told; our """+a('/culture/japanese-mythology/','Japanese mythology guide','mythology')+""" covers it, and """+a('/guides/kirishima-jingu/','Kirishima Jingu','kirishima')+""" is Ninigi&rsquo;s own shrine.</p>
    <p>The city gives 806 as the year the shrine was set up at its present site, though the roots of worship are older than the written record. The halls you see now were rebuilt in 1604 by Tokugawa Ieyasu, in gratitude for Sekigahara according to Edo Legacy Travel and All About Japan. It is regarded as the head of more than 1,300 Sengen shrines (GLTJP). In 1779 the shogunate is said to have confirmed that everything above Mt. Fuji&rsquo;s 8th station belongs to the shrine (Openers; I found it in one place, so treat the date as a good lead rather than a settled fact). The shrine is also one of the component sites of the 2013 World Heritage listing (Fujinomiya city).</p>

    <h2 id="approach">Torii, Water and the Romon<span class="h2-jp">鳥居・手水舎・楼門</span></h2>
    <p>The great torii in the opening photo is the entrance for many visitors, and on a clear winter day it frames Fuji like a picture. It is a good reminder to bow before you walk through.</p>
"""+fig('tyouzuya','The temizuya with vermilion pillars and a blue-green roof, a signboard explaining the purification steps beside it','The temizuya, with vermilion pillars, a blue-green roof and a sign explaining the steps')+"""
    <p>The temizuya is the first stop. The vermilion pillars and blue-green roof stand out against the trees, and a sign beside it explains the purification steps. If you are new to this, our """+a('/culture/shrine-etiquette/','shrine etiquette guide','etiquette')+""" has the sequence.</p>
"""+fig('romon','The two-storey Romon gate in cherry blossom season with large ema on both sides, flags and stone steps leading up','The two-storey Romon in cherry blossom season, with ema on both sides and flags above')+"""
    <p>The Romon is the gate into the inner shrine. It has two storeys, and in spring cherry branches arch over the stone steps. Large ema stand to either side and small flags hang in front, so the whole entrance feels bright and busy rather than hushed. Photographs like this one are why April is the most crowded time.</p>

    <h2 id="ema">Ema and the Haiden<span class="h2-jp">絵馬と拝殿</span></h2>
"""+fig('ema-ichiyo','A large ema board painted with a tiger and the characters Ichiyo Raifuku','A large ema with a tiger and the four characters <span lang="ja">一陽来復</span> as I read them, photographed in 2022')+"""
    <p>Two giant ema stand beside the approach. This one has a tiger and the four characters I read as <em>ichiyo raifuku</em>, a phrase about winter ending and the light returning, which people use for hoping that bad luck turns. It was photographed in 2022, a Year of the Tiger; the shrine changes the design each year, so what you see will be different. A poem is written beside it; I have not confirmed whose it is.</p>
"""+fig('ema-banpo','A large ema board showing a figure in an eboshi hat and the four characters Banpo Kyowa','A second large ema, with an eboshi-hatted figure and four characters I read as <span lang="ja">萬邦共和</span>')+"""
    <p>The second ema shows a figure in a court hat (<em>eboshi</em>) beside four characters that I read as <em>banpo kyowa</em>, a wish for all nations to live in harmony. A waka is written on it too, and again I do not know the author, so I will not guess.</p>
"""+fig('through-romon','The haiden seen from inside the Romon, with a chrysanthemum-patterned curtain hanging in the gate and a straight path beyond','Looking through the Romon to the haiden, with a chrysanthemum-patterned curtain hanging in the gate')+"""
    <p>Pass through the gate and look back along the axis: a curtain with a chrysanthemum pattern hangs in the opening, and a straight path leads on toward the haiden. The strong central line is typical of a large shrine.</p>
"""+fig('haiden','The front of the haiden with a thatched roof, a heavy shimenawa, sake barrels, a priest and visitors','The haiden from the front, with a heavy shimenawa, stacked sake barrels, a priest and visitors')+"""
    <p>This is the haiden, the worship hall. A thick shimenawa rope hangs across the front, sake barrels are stacked at the side, and a priest and several visitors stand on the terrace. A sign for the pond is visible as I read it. The curved roof and the barrels give it a lively look even before you step up to pray.</p>

    <h2 id="honden">The Two-Storey Honden<span class="h2-jp">本殿</span></h2>
"""+fig('honden','The two-storey main hall roof with crossed chigi and rows of katsuogi on the ridge','The two-storey honden, with chigi and katsuogi on the upper roof')+"""
    <p>Walk round and the main hall rises behind the haiden. It has two storeys, one roof stacked above another, which is the shape architects call <em>sengen-zukuri</em> and which you see at Sengen shrines. Crossed chigi and rows of katsuogi decorate the ridge. The main hall is nationally designated; GLTJP calls it an Important Cultural Property, and SoraNews24 notes the two-storey form as a trait of Sengen shrines. If you want to read roofs like this, our """+a('/culture/shrine-architecture/','guide to shrine architecture','architecture')+""" explains chigi and katsuogi.</p>

    <h2 id="office">Reception Office and Omamori<span class="h2-jp">授与所とお守り</span></h2>
"""+fig('uketsukesho','The reception office with a purple curtain bearing a white crest and signboards at the windows','The reception office, with a purple curtain bearing the shrine crest in white')+"""
    <p>The reception office is where you ask for amulets and the goshuin. A purple curtain with a white crest hangs over the counter, and signboards at the windows tell you what is offered. Hours are not posted in the photo, so check the official site.</p>
"""+fig('omamori','Two omamori, one with cherry blossoms and Fuji summit characters, the other red with Mt. Fuji','Two omamori: one with cherry blossoms, one in red with Mt. Fuji (photographed in 2008, so current designs may differ)')+"""
    <p>Two amulets show how the shrine uses its mountain. One carries a cherry-blossom pattern, and the other is red with Fuji on it. They were photographed in 2008, so the current designs may be different. See our """+a('/culture/omamori-guide/','omamori guide','omamori')+""" for what each type is for.</p>

    <h2 id="sakura">Sakura and Mt. Fuji<span class="h2-jp">桜</span></h2>
"""+fig('shingen','A weeping cherry in full bloom before a vermilion hall, a miko, an ema rack and a sign for the pond','The weeping cherry known as Shingen-zakura in full bloom, with a miko and an ema rack beside it')+"""
    <p>GLTJP says the grounds have more than 500 cherry trees in the Sakura no Baba, and singles out the Shingen-zakura, a weeping cherry connected with the warlord Takeda Shingen. In the photo it blooms in front of a vermilion building, with a miko walking past and ema hanging nearby. The usual bloom is late March to early April (GLTJP, japan-guide).</p>
"""+fig('fujiview','Mt. Fuji rising over a park with cherry blossoms in bloom and a children&rsquo;s pond','Mt. Fuji from Fujinomiya, over cherry blossoms in a park')+"""
    <p>Step out of the shrine in the same season and Fuji is there, over blossoms and a park. This view is from Fujinomiya, not strictly from the shrine grounds, but it is the picture visitors come for. The mountain is often hidden by cloud in the afternoon, so go early.</p>

    <h2 id="wakutama">Wakutama Pond<span class="h2-jp">湧玉池</span></h2>
"""+fig('wakutama','Wakutama Pond with clear water, vermilion bridges, a torii and autumn trees','Wakutama Pond in autumn, with vermilion bridges and a torii')+"""
    <p>Wakutama Pond is the heart of the place. Spring water from Mt. Fuji wells up here, and pilgrims once purified themselves in it before climbing (Yamanashi tourism). The water is so clear that the bottom shows, and red bridges and a torii sit on the bank against autumn trees. It is protected as a Special Natural Monument. The city says the water was believed to calm the mountain, which links the whole shrine back to its origin.</p>

    <h2 id="nearby">Shiraito Falls and Yakisoba<span class="h2-jp">白糸の滝と富士宮やきそば</span></h2>
    <p>Fujinomiya is more than the shrine. Shiraito Falls is another water feature of Mt. Fuji, and it is on a different outing from the shrine; plan it as a separate stop by bus or car. It is also part of the World Heritage listing.</p>
"""+fig('shiraito-green','Shiraito Falls in summer, many thin streams falling into a turquoise pool','Shiraito Falls in summer, with many thin streams and a turquoise pool')+"""
    <p>In summer the falls are many thin white threads rather than a single drop, falling into a turquoise pool among green trees. It is cooler and calmer than the shrine on a hot day.</p>
"""+fig('shiraito-autumn','Shiraito Falls with red maples in autumn, white streams visible beyond the trees','Shiraito Falls in autumn, with red maples (photographed in December 2013)')+"""
    <p>The same falls in autumn have red maples around the white water. This one was taken in December 2013, so colour times vary from year to year.</p>
"""+fig('yakisoba','A plate of Fujinomiya yakisoba with thick noodles, cabbage and fish powder, with red pickled ginger','Fujinomiya yakisoba, with thick noodles, cabbage, fish powder and red pickled ginger (photographed in 2008)')+"""
    <p>For lunch, try Fujinomiya yakisoba. Its fame comes from the noodles, which are chewy and thick, and the plate in the photo is topped with fish powder and served with red pickled ginger. Ameblo describes it as a local speciality known for its chewy noodles. If you like noodles, our """+a('/culture/noodles/','noodles guide','noodles')+""" covers yakisoba as well.</p>

    <h2 id="visit">Visiting Fujisan Hongu Sengen Taisha<span class="h2-jp">参拝案内</span></h2>
    <ul class="practical-list">
      <li><strong>Address:</strong> 1-1 Miyamachi, Fujinomiya, Shizuoka.</li>
      <li><strong>Getting there:</strong> Fujinomiya Station on the JR Minobu Line, then a 10 to 15 minute walk (sources differ); or about 30 minutes by taxi or bus from Shin-Fuji Station.</li>
      <li><strong>Hours and fees:</strong> admission is free as far as I know. Hours vary by season, so check the official site before you go.</li>
      <li><strong>Best times:</strong> late March to early April for blossoms; 5 May for yabusame; November for the autumn festival (GLTJP).</li>
      <li><strong>Pair it with:</strong> Shiraito Falls and Fujinomiya yakisoba, and our """+a('/culture/shrine-etiquette/','shrine etiquette guide','etiquette_pair')+""".</li>
    </ul>
    <div class="key-callout">
      <p>&#127890; <strong>Plan your trip:</strong> Browse guided tours or find a stay near Mt. Fuji. <a href="https://www.viator.com/search/Fujinomiya%20Shizuoka?pid=P00298374&amp;mcid=42383&amp;medium=link&amp;campaign=sacred-japan" target="_blank" rel="noopener" onclick="trackEvent('click','affiliate','viator_fujisan_hongu')">Book a Tour</a></p>
    </div>

    <h2 id="faq">Frequently Asked Questions<span class="h2-jp">よくあるご質問</span></h2>
    <div class="faq-stack">
"""+''.join(f"""    <details class="faq-item">
        <summary>{q}</summary>
        <div class="faq-answer">{a_}</div>
    </details>
""" for q,a_ in faqs)+"""    </div>

    <h2 id="final">Before You Go<span class="h2-jp">むすびに</span></h2>
    <p>Come in the morning, bow at the torii, and finish at the pond. Wakutama is where the shrine&rsquo;s reason for existing is easiest to see: clear water coming up from the mountain that people once feared.</p>

    <div class="closing-block">
      <span class="torii">&#9961;&#65039;</span>
      <p>The front door to Mt. Fuji, and the water that calms it.</p>
    </div>

    <section class="related-section">
      <h2>Related Guides</h2>
      <span class="h2-jp">関連ガイド</span>
      <div class="related-grid">
        <a class="related-card" href="/culture/japanese-mythology/" onclick="trackEvent('click','internal','related_fujisan_hongu_to_mythology')">
          <div class="related-card-label">SACRED JAPAN ／ CULTURE</div>
          <div class="related-card-title">&#128302; Japanese Mythology &rarr;</div>
          <div class="related-card-desc">Konohanasakuya-hime, Ninigi and the Kojiki.</div>
        </a>
        <a class="related-card" href="/culture/shrine-architecture/" onclick="trackEvent('click','internal','related_fujisan_hongu_to_architecture')">
          <div class="related-card-label">SACRED JAPAN ／ CULTURE</div>
          <div class="related-card-title">&#127983;&#65039; Shrine Architecture &rarr;</div>
          <div class="related-card-desc">Read the roofs and halls you have just seen.</div>
        </a>
        <a class="related-card" href="/guides/kirishima-jingu/" onclick="trackEvent('click','internal','related_fujisan_hongu_to_kirishima')">
          <div class="related-card-label">SACRED JAPAN ／ GUIDES</div>
          <div class="related-card-title">&#9961;&#65039; Kirishima Jingu &rarr;</div>
          <div class="related-card-desc">Ninigi&rsquo;s shrine in Kyushu.</div>
        </a>
      </div>
    </section>

  </article>

"""
tail=tail.replace('gifu-castle',SL).replace('gifu_castle','fujisan_hongu').replace('DGifu','DFujinomiya%20Shizuoka').replace('search/Gifu','search/Fujinomiya%20Shizuoka')
def L(u,l,t): return f'<a href="{u}" target="_blank" rel="noopener" style="color:var(--beni);text-decoration:underline;" onclick="trackEvent(\'click\',\'external\',\'{l}\')">{t}</a>'
src='Sources verified at time of writing: '+', '.join([
 L('http://fuji-hongu.or.jp/sengen/english/index.html','src_fh_official','Fujisan Hongu Sengen Taisha official site'),
 L('https://www.gltjp.com/en/directory/item/14561/','src_fh_gltjp','GLTJP'),
 L('https://www.japan.travel/spot/1306','src_fh_jnto','JNTO'),
 L('https://www.japan-guide.com/e/e6367.html','src_fh_jg','japan-guide'),
 L('https://edolegacytravel.metro.tokyo.lg.jp/spots/mt-fuji-hongu-sengen-taisha-shrine/','src_fh_edo','Edo Legacy Travel'),
 L('https://allabout-japan.com/en/article/6056','src_fh_aaj','All About Japan'),
 L('https://soranews24.com/2024/12/05/staying-one-step-ahead-of-the-tourist-crowds-with-a-visit-to-japans-main-mt-fuji-shrine%e3%80%90photos%e3%80%91/','src_fh_sn','SoraNews24'),
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
l1="Fujisan Hongu Sengen Taisha Guide:"; l2="Mt. Fuji's Head Shrine"; assert d.textlength(l2,font=f1)<1090
d.text((66,170),l1,font=f1,fill=(26,15,15)); d.text((66,238),l2,font=f1,fill=(26,15,15)); d.text((66,332),"富士山本宮浅間大社",font=f2,fill=(138,125,120))
im.save(R+f'images/og/og-guides-{SL}.jpg',quality=88)
b=Image.open(D+'images/daitorii.jpg'); w,h=b.size; ch=round(w*400/640); t=max(0,(h-ch)//2)
th=b.crop((0,t,w,t+ch)).resize((640,400),Image.LANCZOS); th.save(R+'images/hub/fujisan-hongu-sengen-taisha.jpg',quality=84); th.save(R+'images/hub/fujisan-hongu-sengen-taisha.webp',quality=80)
print('built',len(out))
