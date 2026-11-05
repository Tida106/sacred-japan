import re,json,os
R='/home/claude/sacred-japan/'
H=json.load(open('/tmp/claude-0/-home-claude/fd332c08-3f6b-545a-883b-83277e19ff52/scratchpad/heroes.json'))
# (slug, EN, JP, type, hook)
L=[
('osaka-castle','Osaka Castle','大阪城','Rebuilt keep','Hideyoshi&rsquo;s castle, with a 1931 concrete keep, an observation deck and a moat you can walk around.'),
('nijo-castle','Nijo Castle','二条城','Palace','Ieyasu&rsquo;s Kyoto palace of 1603, with nightingale floors and gold-leaf rooms. There is no keep here, and that is the point.'),
('himeji-castle','Himeji Castle','姫路城','Original keep','The White Heron: the best known of Japan&rsquo;s twelve original keeps, and a maze of walls and gates.'),
('edo-castle','Edo Castle','江戸城','Ruins','The shogun&rsquo;s seat, now the free East Gardens of the Imperial Palace. The keep was lost in the great fire of 1657.'),
('kanazawa-castle','Kanazawa Castle','金沢城','Rebuilt turrets','Lead-tile turrets and an original gate of 1788, right beside Kenrokuen garden.'),
('nagoya-castle','Nagoya Castle','名古屋城','Rebuilt keep','Golden shachi on the roof and a rebuilt palace of gold-leaf rooms. The keep itself has been closed since May 2018.'),
('hiroshima-castle','Hiroshima Castle','広島城','Rebuilt keep','The Carp Castle: brought down by the 1945 blast and rebuilt in 1958.'),
('kumamoto-castle','Kumamoto Castle','熊本城','Rebuilt keep','Famous for its curving stone walls. Damaged in 2016 and again in July 2026, so check what is open.'),
('matsumoto-castle','Matsumoto Castle','松本城','Original keep','A black keep over a moat, with a red bridge and the Alps behind it.'),
('odawara-castle','Odawara Castle','小田原城','Rebuilt keep','The Hojo stronghold, with a 1960 keep, a ninja museum and cherry trees in spring.'),
('hirosaki-castle','Hirosaki Castle','弘前城','Original keep','The only original keep in Tohoku, famous for its cherry blossoms. The keep is currently being moved back onto its restored base.'),
('inuyama-castle','Inuyama Castle','犬山城','Original keep','One of the oldest keeps, on a cliff above the Kiso River, within easy reach of Nagoya.'),
('okayama-castle','Okayama Castle','岡山城','Rebuilt keep','The Black Crow Castle, rebuilt in the 1960s, with Korakuen garden on the other side of the river.'),
('matsuyama-castle','Matsuyama Castle','松山城','Original keep','An original keep on a hilltop in Shikoku, reached by ropeway or chairlift.'),
('hikone-castle','Hikone Castle','彦根城','Original keep','A graceful original keep, a lakeside garden and the mascot Hikonyan.'),
('matsue-castle','Matsue Castle','松江城','Original keep','A National Treasure and the only original keep in the San&rsquo;in region, with a moat cruise below.'),
('shuri-castle','Shuri Castle','首里城','Palace','The red palace of the Ryukyu kings. The rebuilt main hall is scheduled to reopen on 23 November 2026, with timed tickets.'),
('aizuwakamatsu-castle','Aizuwakamatsu Castle','会津若松城','Rebuilt keep','A red-roofed keep and the story of the 1868 siege and the Byakkotai.'),
('goryokaku','Goryokaku','五稜郭','Star fort','A star-shaped fort in Hakodate, the scene of the last battle of the Boshin War.'),
('sendai-castle','Sendai Castle','仙台城','Ruins','Date Masamune&rsquo;s hilltop fort. There is no keep, but there are huge walls and a view over the city.'),
('takeda-castle-ruins','Takeda Castle Ruins','竹田城跡','Ruins','Japan&rsquo;s Machu Picchu, above a sea of clouds on autumn mornings. Closed in January and February.'),
('gifu-castle','Gifu Castle','岐阜城','Rebuilt keep','Nobunaga&rsquo;s mountain castle, reached by ropeway. The keep is closed for reinforcement until late 2027.'),
('kochi-castle','Kochi Castle','高知城','Original keep','The keep and the main hall both survive, which is rare.'),
('uwajima-castle','Uwajima Castle','宇和島城','Original keep','A small, elegant original keep with ornate gables on a hill above the town.'),
('maruoka-castle','Maruoka Castle','丸岡城','Original keep','An original keep roofed with stone tiles, with a sad legend attached to its walls.'),
('marugame-castle','Marugame Castle','丸亀城','Original keep','A small original keep standing on some of Japan&rsquo;s tallest stone walls.'),
('bitchu-matsuyama-castle','Bitchu Matsuyama Castle','備中松山城','Original keep','The only original keep on a mountaintop, 430 metres up and famous for its sea of clouds.'),
('hagi-castle','Hagi Castle Ruins','萩城跡','Ruins','Moat and walls at the foot of Mt. Shizuki, in a World Heritage castle town.'),
('takato-castle-ruins','Takato Castle Ruins','高遠城址','Ruins','About 1,500 cherry trees on the site of a castle that is no longer there.'),
]
CAP={'kumamoto-castle':('guides/kumamoto-castle/images/keep-low-2026','Hyppolyte de Saint-Rambert','https://creativecommons.org/licenses/by/4.0/','CC BY 4.0','The black keep of Kumamoto Castle from the plaza below')}
def card(i,slug,en,jp,typ,hook):
    h=H[slug]; big=i<3
    if slug in CAP:
        base,au,lu,ln,alt=CAP[slug]; src='/'+base+'.jpg'; webp='/'+base+'.webp'
        cred=f'Photo: {au}, <a href="{lu}" target="_blank" rel="noopener">{ln}</a>, via Wikimedia Commons (resized)'
    else:
        src=h['src']; webp=re.sub(r'\.jpg$','.webp',src); alt=h['alt']
        cap=h['cap']; cred=cap.split('<br>')[-1] if '<br>' in cap else cap
        cred=cred.replace('style="color:var(--enshu);"','')
    assert os.path.exists(R+src.lstrip('/')),src
    if not os.path.exists(R+webp.lstrip('/')): webp=None
    pic=(f'<source srcset="{webp}" type="image/webp">' if webp else '')+f'<img src="{src}" alt="{alt}" loading="{"eager" if i<2 else "lazy"}">'
    cls='rk-card rk-big' if big else 'rk-card'
    return f'''    <article class="{cls}" id="{slug}">
      <a class="rk-img" href="/guides/{slug}/" onclick="trackEvent('click','internal','bestcastles_rank_{slug.replace('-','_')}_img')"><picture>{pic}</picture><span class="rk-badge">{i+1}</span></a>
      <div class="rk-body">
        <p class="rk-type">{typ}</p>
        <h3 class="rk-name">{en} <span>{jp}</span></h3>
        <p class="rk-hook">{hook}</p>
        <a class="rk-btn" href="/guides/{slug}/" onclick="trackEvent('click','internal','bestcastles_rank_{slug.replace('-','_')}')">Read the {en.replace(' Ruins','').replace(' Castle','')} guide</a>
        <p class="rk-credit">{cred}</p>
      </div>
    </article>
'''
def group(a,b,title=None):
    s=''
    if title: s+=f'  <h2 id="{title[0]}">{title[1]}</h2>\n'
    big=a==0
    s+='  <div class="rk-grid%s">\n'%(' rk-grid-big' if big else '')
    for i in range(a,b): s+=card(i,*L[i])
    return s+'  </div>\n'
body='''<style>
.rk-grid{display:grid;grid-template-columns:repeat(2,1fr);gap:28px 24px;margin:24px 0 40px;}
.rk-grid-big{grid-template-columns:1fr;gap:36px;}
.rk-card{background:#fff;border:1px solid #e8d8c4;border-radius:6px;overflow:hidden;display:flex;flex-direction:column;}
.rk-img{position:relative;display:block;}
.rk-img img{width:100%;aspect-ratio:3/2;object-fit:cover;display:block;}
.rk-big .rk-img img{aspect-ratio:16/10;max-height:520px;}
.rk-badge{position:absolute;top:12px;left:12px;width:44px;height:44px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-family:'Shippori Mincho',serif;font-size:22px;font-weight:700;color:#1a1a1a;background:linear-gradient(135deg,#f9e9a8 0%,#e6c45a 28%,#c9971c 52%,#f3d77c 78%,#d6a92b 100%);border:1px solid #b8860b;box-shadow:0 2px 6px rgba(0,0,0,.35);}
.rk-body{padding:16px 20px 18px;display:flex;flex-direction:column;flex:1;}
.rk-type{font-size:13px;letter-spacing:.14em;text-transform:uppercase;color:var(--kin);margin:0 0 4px;}
.rk-name{font-family:'Shippori Mincho',serif;font-size:24px;font-weight:400;margin:0 0 8px;line-height:1.3;color:var(--kon);}
.rk-name span{font-size:.62em;color:var(--enshu);margin-left:6px;}
.rk-hook{font-size:17px;line-height:1.65;margin:0 0 14px;color:var(--kon);}
.rk-btn{align-self:flex-start;display:inline-block;padding:8px 16px;background:linear-gradient(135deg,#f9e9a8 0%,#e6c45a 28%,#c9971c 52%,#f3d77c 78%,#d6a92b 100%);color:#1a1a1a;font-weight:700;font-size:15px;text-decoration:none;border-radius:3px;border:1px solid #b8860b;box-shadow:inset 0 1px 0 rgba(255,255,255,.7),0 1px 3px rgba(120,80,0,.35);margin-top:auto;}
.rk-btn:hover{filter:brightness(1.07);}
.rk-credit{font-size:12px;line-height:1.5;color:var(--enshu);margin:12px 0 0;}
.rk-credit a{color:var(--enshu);}
.rk-note{font-size:15px;color:var(--enshu);border-left:3px solid var(--kin);padding:4px 0 4px 14px;margin:0 0 28px;}
@media(max-width:700px){.rk-grid{grid-template-columns:1fr;}.rk-big .rk-img img{aspect-ratio:3/2;}}
</style>
  <article>

    <p>Which castle should you see first? This page puts the most visited castles in order, each with its best photo, and links to a full guide for every one. Photos mostly show the keep or the main gate, as it looks from the usual viewpoint.</p>
    <p class="rk-note">How the ranking works: places 1 to 10 follow NAVITIME&rsquo;s 2025 data on which castles visitors from the Americas, Europe and Oceania searched for most (<a class="inline-link" href="https://www.travelvoice.jp/20260417-159544" target="_blank" rel="noopener">Travel Voice, April 2026</a>). Places 11 onward are my own order, starting with the castles that rank highly among Asian visitors in the same data. Only twelve of these castles still have their original wooden keeps; the others are rebuilt, ruins or palaces, and each card says which.</p>

'''
body+=group(0,3,('top-3','The Top Three'))
body+=group(3,10,('top-10','Places 4 to 10'))
body+=group(10,20,('more-castles','Places 11 to 20'))
body+=group(20,len(L),('worth-the-trip','Places 21 to %d'%len(L)))
body+='''  <h2 id="also">Two More Guides, Without Photos Yet</h2>
  <p>We also have guides to <a class="inline-link" href="/guides/wakayama-castle/" onclick="trackEvent('click','internal','bestcastles_rank_wakayama')">Wakayama Castle</a>, the Kishu Tokugawa seat with a slanted covered bridge, and <a class="inline-link" href="/guides/tsuyama-castle/" onclick="trackEvent('click','internal','bestcastles_rank_tsuyama')">Tsuyama Castle</a>, known for its stone walls and about a thousand cherry trees.</p>

  <h2 id="which-castle-should-you-visit">Which Castle Should You Visit?</h2>
  <ul>
    <li><strong>One famous castle, with the least effort:</strong> <a class="inline-link" href="/guides/himeji-castle/">Himeji</a>.</li>
    <li><strong>A palace rather than a tower:</strong> <a class="inline-link" href="/guides/nijo-castle/">Nijo</a> in Kyoto, or <a class="inline-link" href="/guides/kochi-castle/">Kochi</a>, where the palace also survives.</li>
    <li><strong>A half day from a big city:</strong> <a class="inline-link" href="/guides/inuyama-castle/">Inuyama</a> from Nagoya, or <a class="inline-link" href="/guides/hikone-castle/">Hikone</a> from Kyoto.</li>
    <li><strong>A hike to a keep:</strong> <a class="inline-link" href="/guides/bitchu-matsuyama-castle/">Bitchu Matsuyama</a>, on a mountaintop.</li>
    <li><strong>Cherry blossoms:</strong> <a class="inline-link" href="/guides/hirosaki-castle/">Hirosaki</a> and <a class="inline-link" href="/guides/takato-castle-ruins/">Takato</a>.</li>
    <li><strong>Walls and history:</strong> <a class="inline-link" href="/guides/kumamoto-castle/">Kumamoto</a> (check what is open) and <a class="inline-link" href="/guides/marugame-castle/">Marugame</a>.</li>
  </ul>

'''
p=R+'guides/best-castles-japan/index.html'; s=open(p,encoding='utf-8').read()
a=s.index('  <!-- HERO IMAGE -->'); b=s.index('    <!-- RELATED GUIDES -->')
s=s[:a]+body+'\n'+s[b:]
# title, meta, h1, jsonld
T_old='The Best Castles in Japan: Beautiful Fortresses and Lethal Labyrinths'; T_new='The Best Castles in Japan, Ranked: 30 Castles in Photos'
s=s.replace(T_old,T_new)
D='Japan&#x27;s 30 most popular castles in order, each with its best photo and a link to a full guide: Osaka, Nijo, Himeji, Matsumoto, Kumamoto, Hirosaki and more.'
s=re.sub(r'<meta name="description" content="[^"]*">','<meta name="description" content="%s">'%D,s,1)
s=re.sub(r'(<meta (?:property="og:description"|name="twitter:description") content=")[^"]*(">)',r'\g<1>%s\2'%D,s)
s=s.replace("Discover the hidden lethal labyrinths, psychological warfare, and military engineering behind Japan's most beautiful fortresses like Himeji and Matsumoto.",D.replace('&#x27;',"'"))
s=s.replace('<h1>The Best Castles in Japan: Beautiful Fortresses and Lethal <em>Labyrinths</em></h1>','<h1>The Best Castles in Japan, <em>Ranked</em>: 30 Castles in Photos</h1>')
s=s.replace('"dateModified": "2026-11-05"','"dateModified": "2026-11-05"')
il={"@context":"https://schema.org","@type":"ItemList","name":T_new,"itemListOrder":"https://schema.org/ItemListOrderAscending","itemListElement":[{"@type":"ListItem","position":i+1,"name":x[1],"url":f"https://sacred-japan.net/guides/{x[0]}/"} for i,x in enumerate(L)]}
s=s.replace('</head>','<script type="application/ld+json">\n'+json.dumps(il,ensure_ascii=False)+'\n</script>\n</head>',1)
open(p,'w',encoding='utf-8').write(s)
for tag in ['div','figure','picture','p','a','ul','li','section','h2','h3','article','main']:
    o=len(re.findall(r'<%s[\s>]'%tag,s)); c=len(re.findall(r'</%s>'%tag,s)); print(tag,o,c)
for m in re.finditer(r'<script type="application/ld\+json">(.*?)</script>',s,re.S): json.loads(m.group(1))
print(len(L),'ok')
