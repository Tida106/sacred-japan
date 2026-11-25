import re,json,os,glob
from urllib.parse import quote
from PIL import Image,ImageDraw,ImageFont
R='/home/claude/sacred-japan/'; SL='kurama-dera'; D=R+f'guides/{SL}/'
os.makedirs(D+'images',exist_ok=True); UP='/mnt/user-data/uploads/'
LIC={'by2':('CC BY 2.0','https://creativecommons.org/licenses/by/2.0/'),
     'by3':('CC BY 3.0','https://creativecommons.org/licenses/by/3.0/'),
     'by4':('CC BY 4.0','https://creativecommons.org/licenses/by/4.0/'),
     'bysa3':('CC BY-SA 3.0','https://creativecommons.org/licenses/by-sa/3.0/'),
     'cc0':('CC0 1.0','https://creativecommons.org/publicdomain/zero/1.0/'),
     'pd':('public domain','https://commons.wikimedia.org/wiki/Commons:Licensing')}
CF='https://commons.wikimedia.org/wiki/File:'
PN=lambda n:f'https://web.archive.org/web/2016/http://www.panoramio.com/photo/{n}'
P={ # slug:(upload,author,lic,link)
'gate-blue':('b17b99e2','ccfarmer','by3',CF+'Kurama-dera_temple_gate_-_panoramio.jpg'),
'tengu':('13054c8b','Maarten Heerlien','by2',CF+'Kyoto_20190906_(48885568086).jpg'),
'sando':('94b43f58','KENPEI','bysa3',CF+'Kurama-dera_sando.jpg'),
'gate-rain':('cecb65ba','Kurofune','by3',PN(17375714)),
'stairs':('cfa0c84a','Hyppolyte de Saint-Rambert','by4',CF+'Kurama-Dera_(Kyoto_Sakyo-ku)_Temple_hdsr_S5_25.jpg'),
'pagoda':('f34e0d30','Kurofune','by3',PN(17375743)),
'mainhall':('0710f885','Nankou Oronain','bysa3',PN(58151336)),
'hondenkondo':('9a55371f','KENPEI','bysa3',CF+'Kurama-dera_hondenkondo2.jpg'),
'tiger':('cbcb466b','Daderot','cc0',CF+'Tiger_by_honden_-_Kurama-dera_-_Kyoto_-_DSC06659.jpeg'),
'benzaiten':('730fce1e','KENPEI','bysa3',CF+'Kurama-dera_Tatsumino_benzaiten.jpg'),
'view':('edcba3ba','Maarten Heerlien','by2',CF+'View_from_Kurama-dera_grounds_(48885055523).jpg'),
'trees':('122ded3b','Daderot','cc0',CF+'Trees_-_Kurama-dera_-_Kyoto_-_DSC06694.jpeg'),
'yoshitoshi':('8acfff5e','Yoshitoshi Tsukioka','pd',CF+'Yoshitoshi_Sojobo_Instructs_Yoshitsune_in_the_Sword.jpg'),
}
if not os.path.exists(D+'images/gate-blue.jpg'):
    for k,v in P.items():
        im=Image.open(UP+v[0]+'-image.jpg').convert('RGB'); w,h=im.size
        if w>1200: im=im.resize((1200,round(h*1200/w)),Image.LANCZOS)
        im.save(D+f'images/{k}.jpg',quality=84); im.save(D+f'images/{k}.webp',quality=80)
SIZE={k:Image.open(D+f'images/{k}.jpg').size for k in P}
def fig(k,alt,cap,hero=False):
    u,a,l,cl=P[k]; ln,lu=LIC[l]; w,h=SIZE[k]
    if hero: st='margin:0 0 48px;'; ld='eager'; ims='style="width:100%;max-height:420px;object-fit:cover;border-radius:4px;display:block;"'
    else:
        st='margin:28px auto;max-width:%s;'%('420px' if h>w else '760px'); ld='lazy'; ims='style="width:100%;height:auto;border-radius:4px;display:block;"'
    if l=='pd': lic=f'public domain (a photographic reproduction of a print by {a})'; who=''
    else: lic=f'<a href="{lu}" target="_blank" rel="noopener">{ln}</a>'; who=f'Photo: {a}, '
    return f'''<figure style="{st}"><picture><source srcset="/guides/{SL}/images/{k}.webp" type="image/webp"><img src="/guides/{SL}/images/{k}.jpg" alt="{alt}" width="{w}" height="{h}" loading="{ld}" {ims}></picture><figcaption style="font-size:13px;color:var(--enshu);margin-top:10px;text-align:center;line-height:1.6;">{cap}.<br>{who}<a href="{cl}" target="_blank" rel="noopener">{a if l=='pd' else a}</a>{'' if False else ''}, {lic}, via Wikimedia Commons (resized)</figcaption></figure>
'''
# tidy credit line: author linked once
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
TITLE="Kurama-dera Guide: Tengu, Yoshitsune's Mountain, the Kongo-sho and the Hike to Kifune"
DESC="A licensed guide's guide to Kurama-dera in northern Kyoto: the Sonten trinity, the star-mandala stone floor, the tengu who trained young Yoshitsune, the cable car, fees, hours and the hike over the ridge to Kifune."
TAG="Kyoto's tengu mountain, 30 minutes up a zigzag path from Kurama Station."
head=re.sub(r'<title>.*?</title>',f'<title>{TITLE} | Sacred Japan</title>',head,count=1)
head=re.sub(r'(<meta (?:name="description"|property="og:description"|name="twitter:description") content=")[^"]*(")',lambda m:m.group(1)+DESC+m.group(2),head)
head=re.sub(r'(<meta (?:property="og:title"|name="twitter:title") content=")[^"]*(")',lambda m:m.group(1)+TITLE+m.group(2),head)
head=re.sub(r'("headline": ")[^"]*(")',lambda m:m.group(1)+TITLE+m.group(2),head)
head=re.sub(r'("description": ")A licensed[^"]*(")',lambda m:m.group(1)+DESC+m.group(2),head)
head=re.sub(r'("date(?:Published|Modified)": ")[^"]*(")',lambda m:m.group(1)+'2026-11-25'+m.group(2),head)
head=re.sub(r'<meta name="keywords" content="[^"]*">','<meta name="keywords" content="Kurama-dera, Kurama-dera temple, Kurama tengu, Kongo-sho, Mount Kurama, Kurama to Kibune hike, Yoshitsune Kurama, Kurama cable car, Kyoto power spot">',head)
head=head.replace('guides/gifu-castle',f'guides/{SL}').replace('guide_gifu_castle_','guide_kurama_dera_').replace('og-guides-gifu-castle',f'og-guides-{SL}')
head=head.replace('岐阜城','鞍馬寺').replace('Gifu Castle','Kurama-dera')
head=re.sub(r"<h1>.*?</h1>","<h1><em>Kurama-dera</em>: Tengu, Yoshitsune's Mountain, the Kongo-sho and the Hike to Kifune</h1>",head,count=1,flags=re.S)
head=head.replace("Nobunaga's mountain castle above Gifu, with the keep closed until late 2027.",TAG)
head=head.replace('SACRED JAPAN GUIDES ／ 城','SACRED JAPAN GUIDES ／ 寺')
IL='class="inline-link"'
def a(u,t,ev): return f'<a href="{u}" {IL} onclick="trackEvent(\'click\',\'internal\',\'guide_kurama_dera_to_{ev}\')">{t}</a>'
faqs=[
("Is there an entrance fee for Kurama-dera?","The temple asks for a mountain-upkeep contribution (<em>aizan-hi</em>) of &yen;500, paid at the gate beside the Niomon (GLTJP, Keihan, Kyoto Travel). Some older English pages still say &yen;300, so treat the current official figure as the one to trust. The Reihoden museum is an extra &yen;200, and the cable car is &yen;200 each way for adults (GLTJP). The temple does not take credit cards, so bring cash."),
("What are the opening hours?","The grounds and Main Hall are listed as 9:00 to 16:15 (GLTJP, Rurubu), though a few sites print 16:30, so go early and check the official site. The Reihoden museum closes at 16:00, and GLTJP lists it as closed on one weekday plus a winter closure from 12 December to the end of February. Sources disagree on the weekday (Monday on GLTJP, Tuesday on Rurubu), so check before you plan around the museum."),
("Should I take the cable car or walk?","Walking from the Niomon to the Main Hall takes about 30 minutes (GLTJP). The cable car runs about two minutes to Tahoto Station, followed by roughly 10 minutes on foot. One guide that read the temple&rsquo;s timings counts that as saving about 11 minutes, and says the last car up leaves at 16:20, after the Main Hall has shut at 16:15 (Hidden Japan Gems, single source). The same guide found fault and inspection suspensions in 2026, so check the temple&rsquo;s notice on the day. I like the walk on the way up: the zigzag path is half the point."),
("How long is the hike from Kurama-dera to Kifune?","On the temple&rsquo;s own leg timings, as read by Hidden Japan Gems, it is roughly 80 minutes from Kurama Station to Kifune Shrine without stops: 3 to the Niomon, 5 to Yuki Shrine, 20 to the Main Hall, 30 on to the Mao-den, then 20 down to Kifune. Our <a href=\"/shrines/kifune-shrine/\" class=\"inline-link\">Kifune Shrine guide</a> describes the Kifune end. The path crosses the famous tree roots and is slippery after rain."),
("Do I need to believe in Sonten to visit?","No. The temple welcomes visitors of any belief. As a guide, I describe the teachings as the temple&rsquo;s own and explain them in the terms the temple uses; you are free to take or leave the cosmic language. What I can promise is the mountain, the views and the history."),
("When is the best time to visit?","Mid-November is the usual maple peak (Kyoto Travel). Cherry blossoms on the mountain come later than in the city, around mid-April, during the temple&rsquo;s flower memorial. Two festivals are worth timing: the bamboo-cutting ceremony on 20 June, and the Kurama Fire Festival on 22 October at Yuki Shrine (Kyoto Travel), when the village is closed to cars and very crowded."),
]
faq_json=',\n'.join('''    {
      "@type": "Question",
      "name": %s,
      "acceptedAnswer": {
        "@type": "Answer",
        "text": %s
      }
    }'''%(json.dumps(re.sub('<[^>]+>','',re.sub('&rsquo;','’',q))),json.dumps(re.sub('&yen;','¥',re.sub('&rsquo;','’',re.sub('<[^>]+>','',a_))))) for q,a_ in faqs)
head=re.sub(r'("mainEntity": \[\n).*?(\n  \]\n\}\n</script>\n\n<!-- ── GOOGLE)',lambda m:m.group(1)+faq_json+m.group(2),head,flags=re.S)
hh=re.sub(r'"mainEntity": \[.*','',head,flags=re.S)
assert not re.search('Gifu|Nobunaga|castle|Castle',re.sub(r'<nav>.*?</nav>','',hh,flags=re.S).replace('Castles','')),re.findall('.{30}(?:Gifu|Nobunaga|astle).{20}',hh)
main='''<main>

  <aside class="toc" aria-label="Table of contents">
    <div class="toc-label">TABLE OF CONTENTS ／ 目次</div>
    <div class="toc-title">In This Guide</div>
    <ol>
      <li><a href="#opening">The Tengu Mountain</a></li>
      <li><a href="#history">How It Began</a></li>
      <li><a href="#sonten">Sonten and the Tigers</a></li>
      <li><a href="#climb">The Climb from Kurama Station</a></li>
      <li><a href="#hall">The Main Hall and the Kongo-sho</a></li>
      <li><a href="#grounds">Around the Grounds</a></li>
      <li><a href="#yoshitsune">Yoshitsune and the Tengu</a></li>
      <li><a href="#beyond">Beyond the Hall: Okunoin and Kifune</a></li>
      <li><a href="#seasons">Festivals and Seasons</a></li>
      <li><a href="#visit">Visiting Kurama-dera</a></li>
      <li><a href="#faq">Frequently Asked Questions</a></li>
      <li><a href="#final">Before You Go</a></li>
    </ol>
  </aside>

  <article>

'''+fig('gate-blue','The vermilion Niomon gate of Kurama-dera with a curved dark roof, white curtains and orange lanterns beneath maple leaves and a blue sky','The Niomon, the gate at the foot of the mountain path',hero=True)+'''
    <section id="opening">
      <p class="opening">As a licensed guide, I tell visitors that Kurama-dera is the one Kyoto temple where a child is said to have been taught swordsmanship by goblins. The child was the young Minamoto no Yoshitsune, the goblins were tengu, and the mountain is still full of them: a giant red tengu face greets you at the station. This is also a temple with a faith of its own, in a trinity called <em>Sonten</em>, and a stone floor in front of the Main Hall that people stand on to &ldquo;receive energy.&rdquo;</p>
      <p>This guide covers the history, the teachings in the temple&rsquo;s own terms, the climb and the Main Hall in photos, the Yoshitsune legend, the hike over the ridge to Kifune, the festivals, and the practical details.</p>
    </section>

    <h2 id="history">How It Began<span class="h2-jp">由緒</span></h2>
    <p>Tradition dates the temple to 770, when Gantei, a disciple of the Chinese monk Jianzhen (Ganjin) of Toshodai-ji in Nara, built a hermitage on the mountain and enshrined Bishamonten there (GLTJP, Kyoto Travel). In the Heian period it was revered as a guardian of the northern side of the capital (Kyoto Travel). Today it is the head temple of the Kurama Kokyo sect (GLTJP), which is a modern independent school, not one of the old ones.</p>
    <p>One famous line about the place is older than most of its buildings: the court lady Sei Shonagon wrote in <em>The Pillow Book</em> that the winding road to Kurama is a thing that is close and yet far (Rurubu, Tabi-mag). If you climb the path yourself, you will understand her.</p>

    <h2 id="sonten">Sonten and the Tigers<span class="h2-jp">尊天</span></h2>
    <p>Three deities are worshipped together as one, called <em>Sonten</em>: Bishamonten, the Thousand-Armed Kannon, and Goho Maoson (GLTJP). The first two are familiar Buddhist figures. Goho Maoson is not found elsewhere; the temple teaches that he descended to earth from Venus about six million years ago (Discover Kyoto), and some pages quote 6.5 million (Kansai Odyssey). Whatever you make of the cosmology, it explains the temple&rsquo;s unusual character: it talks about the universe more than most temples do. Discover Kyoto sums up the teaching as Kannon&rsquo;s mercy, Bishamonten&rsquo;s truth and Maoson&rsquo;s energy.</p>
    <p>The main image itself is a hidden Buddha, shown to the public only once every 60 years, in a Hinoe-Tora year; the next is 2046 (GLTJP). In the meantime, the temple&rsquo;s National Treasure triad of standing Bishamonten statues is kept in the Reihoden museum (GLTJP). The other signature detail is the guardians. Instead of the usual pair of lion-dogs, a pair of &ldquo;a-un&rdquo; tigers protects the principal image (GLTJP), and you will see them in front of the hall.</p>

    <h2 id="climb">The Climb from Kurama Station<span class="h2-jp">鞍馬駅から</span></h2>
    <p>The visit begins before you reach the temple. The Eizan Railway&rsquo;s terminal at Kurama is a village at the end of the line, and it announces itself.</p>
'''+fig('tengu','A giant red tengu face with a long round nose, black brows and a tall black cap, on a wooden stand in a forest with a sign reading welcome to the tengu town of Kurama','The giant tengu at Kurama, with a sign reading &ldquo;Welcome to Tengu Town, Kurama&rdquo; (the sign carries a railway brand)')+'''
    <p>A huge red tengu face, its round nose as big as a head, glares from a wooden stand in the greenery. The sign below it, as I read it, says <span lang="ja">ようこそ天狗の町 鞍馬へ</span>, &ldquo;Welcome to the tengu town of Kurama,&rdquo; and adds a line about taking care of nature. Keihan&rsquo;s guide says the tengu at the station is the second one to stand there. It is the most photographed object in the village, and a good way to meet the mountain&rsquo;s spirit in a lighter mood.</p>
'''+fig('sando','Wide stone steps lined with vermilion lanterns leading up to the Niomon gate, with a visitor climbing and a stone marker on the right','The steps up to the Niomon, with the temple name on the stone marker at right')+'''
    <p>From the station it is a few minutes&rsquo; walk to the foot of a wide flight of stone steps. Vermilion lanterns line both sides, a stone marker carved with the temple&rsquo;s name stands at the right, and the gate sits at the top. The nearest car park is down here too, which is why I always say: take the train.</p>
'''+fig('gate-rain','The Niomon on a rainy winter day, with visitors holding umbrellas on the stone steps, a Japanese flag and a multicolored banner at the gate','The Niomon on a wet winter day')+'''
    <p>The Niomon is the entrance gate, and the mountain-upkeep fee is paid beside it (see the practical list below). Keihan says the guardian statues inside are said to be by the Kamakura-period sculptor Tankei, a tradition rather than a documented fact. This photo, taken on a rainy day, shows a Japanese flag and a banner beside the gate, and a few people coming down with umbrellas. The mountain can be gloomy and lovely in such weather, but the stone is slippery.</p>
'''+fig('stairs','Steep stone steps lined on both sides with vermilion lanterns with green glass panes, climbing to a stone wall and a vermilion railing at the top','Stone steps and lanterns on the way up (the Commons title says only Kurama-dera)')+'''
    <p>Beyond the gate the path begins to climb, the road Sei Shonagon wrote about. Steps and lanterns appear again and again, with the vermilion railing of a terrace visible at the top in this photo. The Commons title says only Kurama-dera, so I cannot tell you which flight this is, but it gives a fair idea of what the upper path is like. On the way, you pass Yuki Shrine, the village shrine whose Fire Festival is described below.</p>
'''+fig('pagoda','A vermilion two-tier pagoda with a green copper roof and a tall finial among bare trees and cedars, with stone lanterns and vermilion lanterns in front','A vermilion pagoda among the trees (the Commons title gives no name)')+'''
    <p>This is a small vermilion pagoda of the two-tier type called a <em>tahoto</em>, with a green roof and a tall finial, set among trees with rows of lanterns in front. The cable car&rsquo;s upper terminus is called Tahoto Station, and NAVITIME describes the cable car as going up to the temple&rsquo;s two-tier pagoda. The Commons title does not name the building, so I cannot say for certain that this is that pagoda; it is, at any rate, the kind of sight that rewards the walk.</p>

    <h2 id="hall">The Main Hall and the Kongo-sho<span class="h2-jp">本殿金堂・金剛床</span></h2>
    <p>The goal of the climb is the Main Hall (<em>Honden Kondo</em>). In front of it lies the temple&rsquo;s best-known feature, a stone floor called the <em>Kongo-sho</em>. GLTJP, which has been checked by the temple, says it is modeled after a star mandala that represents the vibrations of cosmic energy, and calls it a popular power spot. Other sites describe the shape as a hexagram, and visitors often stand in the middle with their arms open (visitor reviews). It is a custom, not a requirement, and I would not go in expecting a dramatic sensation. I would go for the view, the quiet and the way the hall opens onto the mountainside.</p>
'''+fig('mainhall','The Main Hall of Kurama-dera with lanterns and a white curtain, steps with a visitor and a child climbing, and a circular pavement of pale and dark stone in front','The Main Hall and the circular Kongo-sho pavement in front of it')+'''
    <p>A circle of pale stone with a darker border, divided by straight lines into a geometric pattern, is laid in the gravel in front of the steps; a triangle sits at the center. A narrow white banner on the hall&rsquo;s right pillar appears to read, as I read it, <span lang="ja">義経祭 九月十五日</span>, the Yoshitsune Festival of 15 September that Kyoto Travel lists for the temple. Two visitors, a man and a child, are climbing the steps.</p>
'''+fig('hondenkondo','The Main Hall of Kurama-dera in spring with a gray tiled roof, red pillars and white walls behind blossoming cherry trees and a forested hill','The Main Hall in cherry season')+'''
    <p>In spring, cherry trees bloom in front of the hall. Kyoto Travel says the mountain&rsquo;s cherries open later than those in the city, around mid-April, and that the temple holds a flower memorial then. On the left, some trees are already in flower while the rest are still bare, which is typical of that moment. A stone pedestal with a dark statue stands at the foot of the steps; it appears to be one of the tigers.</p>
'''+fig('tiger','A bronze tiger statue seated on a stone pedestal under a tree, with its mouth open and a ridged coat','One of the pair of tigers in front of the Main Hall')+'''
    <p>Here is a close look at the guardian. This bronze tiger, with its mouth open and its coat ridged like armor, takes the place of the lion-dog you would expect at a shrine or temple. GLTJP says a pair of a-un tigers guards the principal image. Because the pair is traditionally one open mouth and one closed, look for the second tiger to complete the set.</p>

    <h2 id="grounds">Around the Grounds<span class="h2-jp">境内</span></h2>
    <p>Do not rush back down. The terrace and the paths around the hall reward a slow circuit, and a few small buildings sit along the way.</p>
'''+fig('benzaiten','A small vermilion open-fronted shrine with a white curtain bearing a black crest, a bell rope, hanging lanterns and a stone lantern in front, beside a stone wall','A small shrine on the grounds, which Commons calls Tatsumi no Benzaiten')+'''
    <p>This small, open-fronted vermilion shrine has a white curtain with a black crest, a thick bell rope, and gold-colored lanterns hanging inside. The Commons title calls it Tatsumi no Benzaiten, and the board on the left appears to mention Benzaiten. The crest is the temple&rsquo;s mark as I read it, but I would not hang much on that.</p>
'''+fig('view','A vermilion railing and a rock tied with a rope with zigzag white paper streamers, in front of forested mountains under a blue sky with large clouds','A roped-off rock beside a vermilion railing, with the mountains beyond')+'''
    <p>A vermilion railing runs along the edge of the terrace, with the forested mountains of northern Kyoto behind. In front is a rock fenced with a straw rope hung with zigzag paper streamers (<em>shide</em>), the signs Shinto uses to mark something sacred. The Commons title says only that it is the view from the grounds, so I do not know what this rock is called or why it is roped off.</p>
'''+fig('trees','A vermilion railing with several benches in front of a large green tree, a cedar and layers of forested mountains under a blue sky','Benches along the railing')+'''
    <p>Benches line the railing in this second view over the mountains, with a tall cedar, a leafy tree and layers of ridges receding into haze. It is a good place to sit before the descent, with the village far below.</p>

    <h2 id="yoshitsune">Yoshitsune and the Tengu<span class="h2-jp">牛若丸と天狗</span></h2>
    <p>The legend that made Kurama famous is the story of Yoshitsune. After his father was killed, the boy, then called Ushiwakamaru, was sent to the temple at the age of seven and stayed about ten years, according to Kyoto Travel. On the mountain he was known as Shanao. The story goes that at night he met the king of the tengu, Sojobo, who taught him swordsmanship (Wikipedia; Discover Kyoto). The same tale is the basis of the Noh play <em>Kurama Tengu</em>, which Kyoto Travel links to the temple&rsquo;s spring cherry blossoms; our '''+a('/culture/noh/','Noh guide','noh')+''' explains how to see Noh, and our '''+a('/culture/samurai/','samurai guide','samurai')+''' covers the warriors of his age.</p>
'''+fig('yoshitoshi','A woodblock print of a young man in a green jacket leaping with a sword under a full moon among falling cherry petals, with a white-bearded old man in a red robe crouching beside a cave and a waterfall','Yoshitoshi&rsquo;s print of the young Yoshitsune and the tengu Sojobo')+'''
    <p>The print, by the 19th-century artist Yoshitoshi, shows the scene. A young man with a sword leaps under a full moon in a flurry of cherry petals; beside a waterfall, a white-bearded figure in a red robe crouches, with a long nose. The caption at the lower left reads, as I read it, <span lang="ja">舍那王於鞍馬山學武術之圖</span>, &ldquo;Shanao learning martial arts on Mount Kurama.&rdquo; The Commons title calls the old man Sojobo, the Kurama tengu.</p>
    <p>The temple takes the story seriously. Kyoto Travel says Yoshitsune&rsquo;s spirit is believed to have returned to the mountain and is enshrined in the Yoshitsune Hall at the Okunoin, as an attendant of Maoson. The temple marks the Yoshitsune Festival on 15 September, with a service at 11:00 in the Main Hall (Kyoto Travel).</p>

    <h2 id="beyond">Beyond the Hall: Okunoin and Kifune<span class="h2-jp">奥の院と貴船</span></h2>
    <p>Most visitors turn back at the Main Hall, but the mountain continues. A path leads on to the Okunoin and its Mao-den, the hall of Goho Maoson. Along the way is the section of exposed cedar roots, the famous &ldquo;tree-root path,&rdquo; where shallow bedrock forces the roots to the surface (Hidden Japan Gems). Tabi-mag says the path passes Sojogadani, where there are halls to Fudo and Yoshitsune, and that this is where he is said to have trained; I have not walked every branch myself, so use the temple&rsquo;s map.</p>
    <p>From there, the trail goes over the ridge and down to Kifune Shrine. Using the temple&rsquo;s own leg timings, Hidden Japan Gems counts about 30 minutes from the Main Hall to the Mao-den, and 20 more down to Kifune. From Kifune Shrine it is still about 40 minutes down a narrow road to Kibuneguchi Station (same source). Our '''+a('/shrines/kifune-shrine/','Kifune Shrine guide','kifune')+''' covers the water shrine at the far end, and it is a classic half-day.</p>

    <h2 id="seasons">Festivals and Seasons<span class="h2-jp">年中行事</span></h2>
    <ul class="practical-list">
      <li><strong>Mid-April &mdash; flower memorial:</strong> an eight-day festival when the mountain cherries open; offerings of flowers, tea and performances are made to Sonten (Kyoto Travel).</li>
      <li><strong>20 June &mdash; bamboo-cutting ceremony (<em>Takekiri-e</em>):</strong> monks in warrior-monk costume cut green bamboo, which stands for a giant serpent, in a race between two teams, Tanba and Omi, which also predicts the harvest (Kyoto Travel; the 2026 ceremony ran from 14:00 to 15:00).</li>
      <li><strong>15 September &mdash; Yoshitsune Festival:</strong> a memorial for Yoshitsune at the Main Hall, at 11:00 (Kyoto Travel).</li>
      <li><strong>22 October &mdash; Kurama Fire Festival:</strong> held at Yuki Shrine on the approach, and counted among Kyoto&rsquo;s three great unusual festivals. It is a night festival; in 2026 the road between Kibuneguchi and Kurama Onsen was closed to cars from 15:00, car parks were shut and the area above the Niomon was restricted before the procession (Kyoto Travel). Please use the train.</li>
      <li><strong>Mid-to-late November &mdash; autumn leaves:</strong> the usual peak (Kyoto Travel).</li>
    </ul>

    <h2 id="visit">Visiting Kurama-dera<span class="h2-jp">アクセス</span></h2>
    <ul class="practical-list">
      <li><strong>Address:</strong> 1074 Kurama Honmachi, Sakyo-ku, Kyoto.</li>
      <li><strong>Getting there:</strong> take the Eizan Railway to Kurama, the terminal station, then 3 minutes on foot to the Niomon (GLTJP). From the Niomon it is about 30 minutes on foot to the Main Hall, or the cable car to Tahoto Station plus about 10 minutes on foot (GLTJP).</li>
      <li><strong>Fees:</strong> mountain-upkeep contribution &yen;500 (GLTJP); Reihoden museum &yen;200; cable car &yen;200 per adult each way, &yen;100 for younger children (GLTJP). Older pages may say &yen;300. No credit cards.</li>
      <li><strong>Hours:</strong> 9:00 to 16:15 (GLTJP, Rurubu; some sites say 16:30). Reihoden 9:00 to 16:00. Please check the official site, since the cable car has had suspensions.</li>
      <li><strong>Time needed:</strong> about two hours for the temple alone is my own estimate; allow more for the Kifune hike.</li>
      <li><strong>What to wear:</strong> shoes with grip; the path has stone steps and roots, and is slippery after rain.</li>
      <li><strong>Pair it with:</strong> <a href="/shrines/kifune-shrine/" class="inline-link" onclick="trackEvent('click','internal','guide_kurama_dera_to_kifune_pair')">Kifune Shrine</a> over the ridge, or the nearby <a href="/guides/best-shrines-kyoto/" class="inline-link" onclick="trackEvent('click','internal','guide_kurama_dera_to_best_shrines_kyoto')">best shrines in Kyoto</a>.</li>
    </ul>
    <div class="key-callout">
      <p>&#127890; <strong>Plan your trip:</strong> Browse guided tours or find a stay near northern Kyoto. <a href="https://www.viator.com/search/Kurama%20Kyoto?pid=P00298374&amp;mcid=42383&amp;medium=link&amp;campaign=sacred-japan" target="_blank" rel="noopener" onclick="trackEvent('click','affiliate','viator_kurama_dera_inline')">Find tours on Viator &rarr;</a></p>
    </div>

    <h2 id="faq">Frequently Asked Questions<span class="h2-jp">よくあるご質問</span></h2>
    <div class="faq-stack">
'''+''.join(f'''    <details class="faq-item">
        <summary>{q}</summary>
        <div class="faq-answer">{a_}</div>
    </details>
''' for q,a_ in faqs)+'''    </div>

    <h2 id="final">Before You Go<span class="h2-jp">むすびに</span></h2>
    <p>Climb on foot if you can, stop at the tengu, stand on the Kongo-sho for a minute without expecting anything, and look out over the mountain from the terrace. If you have the legs for it, carry on to Kifune.</p>

    <div class="closing-block">
      <span class="torii">&#9961;&#65039;</span>
      <p>Even if you meet no tengu, you will find the mountain they chose.</p>
    </div>

    <section class="related-section">
      <h2>Related Guides</h2>
      <span class="h2-jp">関連ガイド</span>
      <div class="related-grid">
        <a class="related-card" href="/shrines/kifune-shrine/" onclick="trackEvent('click','internal','related_kurama_dera_to_kifune')">
          <div class="related-card-label">SACRED JAPAN ／ SHRINES</div>
          <div class="related-card-title">&#128167; Kifune Shrine Guide &rarr;</div>
          <div class="related-card-desc">The water shrine at the other end of the ridge trail.</div>
        </a>
        <a class="related-card" href="/culture/noh/" onclick="trackEvent('click','internal','related_kurama_dera_to_noh')">
          <div class="related-card-label">SACRED JAPAN ／ CULTURE</div>
          <div class="related-card-title">&#127917; Noh Guide &rarr;</div>
          <div class="related-card-desc">The stage tradition behind <em>Kurama Tengu</em>.</div>
        </a>
        <a class="related-card" href="/culture/samurai/" onclick="trackEvent('click','internal','related_kurama_dera_to_samurai')">
          <div class="related-card-label">SACRED JAPAN ／ CULTURE</div>
          <div class="related-card-title">&#9876;&#65039; Samurai Guide &rarr;</div>
          <div class="related-card-desc">The warriors of Yoshitsune&rsquo;s world, in armor and swords.</div>
        </a>
      </div>
    </section>

  </article>

'''
tail=tail.replace('gifu-castle',SL).replace('gifu_castle','kurama_dera').replace('DGifu','DKurama%20Kyoto').replace('search/Gifu','search/Kurama%20Kyoto')
def L(u,l,t): return f'<a href="{u}" target="_blank" rel="noopener" style="color:var(--beni);text-decoration:underline;" onclick="trackEvent(\'click\',\'external\',\'{l}\')">{t}</a>'
src='Sources verified at time of writing: '+', '.join([
 L('https://www.kuramadera.or.jp/','src_kd_official','Kurama-dera official site'),
 L('https://www.gltjp.com/en/directory/item/12086/','src_kd_gltjp','GLTJP'),
 L('https://ja.kyoto.travel/event/single.php?event_id=4978','src_kd_kyototravel','Kyoto Travel (events)'),
 L('https://www.keihan.co.jp/recommend/kurama-kibune-ohara/kurama/','src_kd_keihan','Keihan'),
 L('https://www.discoverkyoto.com/places-go/kurama-dera/','src_kd_discoverkyoto','Discover Kyoto'),
 L('https://hiddenjapan-gems.com/kifune-kurama-guide/','src_kd_hjg','Hidden Japan Gems'),
 L('https://tabi-mag.jp/ky0244/','src_kd_tabimag','Tabi-mag'),
 L('https://rurubu.jp/andmore/spot/80026307','src_kd_rurubu','Rurubu'),
])+'. Hours, prices and availability change'
tail,n=re.subn(r'Sources verified at time of writing:.*?Hours, prices and availability change',lambda m:src,tail,flags=re.S); assert n==1
out=head+main+tail
assert not re.search('Gifu|Nobunaga|Kinka|Kumano',re.sub(r'"mainEntity": \[.*','',out,flags=re.S).replace('Kumano',''))
open(D+'index.html','w',encoding='utf-8').write(out)
for tg in ['div','figure','picture','p','a','ul','li','details','section','h2']:
    assert len(re.findall(f'<{tg}[ >]',out))==len(re.findall(f'</{tg}>',out)),tg
for m in re.findall(r'<script type="application/ld\+json">(.*?)</script>',out,re.S): json.loads(m)
im=Image.open(R+'images/og/og-guides-matsue-castle.jpg').convert('RGB'); d=ImageDraw.Draw(im)
d.rectangle([40,150,1170,380],fill=(252,240,242)); d.rectangle([1118,66,1160,96],fill=(252,240,242))
f1=ImageFont.truetype(glob.glob('/usr/share/fonts/**/DejaVuSerif-Bold.ttf',recursive=True)[0],48)
f2=ImageFont.truetype(glob.glob('/usr/share/fonts/**/NotoSerifCJK-Bold.ttc',recursive=True)[0],28,index=0)
l1="Kurama-dera Guide:"; l2="Tengu, Yoshitsune, Kifune"; assert d.textlength(l2,font=f1)<1090
d.text((66,170),l1,font=f1,fill=(26,15,15)); d.text((66,238),l2,font=f1,fill=(26,15,15)); d.text((66,332),"鞍馬寺",font=f2,fill=(138,125,120))
im.save(R+f'images/og/og-guides-{SL}.jpg',quality=88)
b=Image.open(D+'images/tengu.jpg'); w,h=b.size; ch=round(w*400/640); t=430
th=b.crop((0,t,w,t+ch)).resize((640,400),Image.LANCZOS); th.save(R+'images/hub/kurama-dera.jpg',quality=84); th.save(R+'images/hub/kurama-dera.webp',quality=80)
print('built',len(out))
