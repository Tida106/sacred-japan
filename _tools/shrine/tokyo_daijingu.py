import re,json,os,glob,csv,io
from PIL import Image,ImageDraw,ImageFont
R='/home/claude/sacred-japan/'; SL='tokyo-daijingu'; D=R+f'guides/{SL}/'
os.makedirs(D+'images',exist_ok=True); UP='/mnt/user-data/uploads/'
LIC={'bysa4':('CC BY-SA 4.0','https://creativecommons.org/licenses/by-sa/4.0/'),'cc0':('CC0 1.0','https://creativecommons.org/publicdomain/zero/1.0/')}
TOK='江戸村のとくぞう'
P={ # slug:(upload,author,lic,search term)
'torii':('4166d5d9',TOK,'bysa4',TOK+' 東京大神宮'),
'shinmon':('b248c845',TOK,'bysa4',TOK+' 東京大神宮'),
'temizuya':('13d4c08a','Daderot','cc0','Daderot 東京大神宮'),
'basin':('8c1a6d50','しんぎんぐきゃっと','bysa4','しんぎんぐきゃっと 東京大神宮'),
'gate-view':('655eca5c',TOK,'bysa4',TOK+' 東京大神宮'),
'front':('7fe2181f',TOK,'bysa4',TOK+' 東京大神宮'),
'approach':('b8fe3315','Miyuki Meinaka','bysa4','Miyuki Meinaka 東京大神宮'),
'praying':('cd85a52e','Higa4','cc0','Higa4 東京大神宮'),
'roof':('36576312','Daderot','cc0','Daderot 東京大神宮'),
'crowd':('7774b5b1','Miyuki Meinaka','bysa4','Miyuki Meinaka 東京大神宮'),
'inside':('8fbd49fa','Nesnad','bysa4','Nesnad 東京大神宮'),
'ema':('a13ec6d9','Higa4','cc0','Higa4 東京大神宮'),
}
if not os.path.exists(D+'images/torii.jpg'):
    for k,v in P.items():
        im=Image.open(UP+v[0]+'-image.jpg').convert('RGB'); w,h=im.size
        if w>1200: im=im.resize((1200,round(h*1200/w)),Image.LANCZOS)
        im.save(D+f'images/{k}.jpg',quality=84); im.save(D+f'images/{k}.webp',quality=80)
SIZE={k:Image.open(D+f'images/{k}.jpg').size for k in P}
def fig(k,alt,cap,hero=False):
    u,a,l,q=P[k]; ln,lu=LIC[l]; w,h=SIZE[k]
    from urllib.parse import quote
    cl=f'https://commons.wikimedia.org/w/index.php?search={quote(q)}&title=Special:MediaSearch&type=image'
    if hero: st='margin:0 0 48px;'; ld='eager'; ims='style="width:100%;max-height:420px;object-fit:cover;border-radius:4px;display:block;"'
    else:
        st='margin:28px auto;max-width:%s;'%('420px' if h>w else '760px'); ld='lazy'; ims='style="width:100%;height:auto;border-radius:4px;display:block;"'
    return f'''<figure style="{st}"><picture><source srcset="/guides/{SL}/images/{k}.webp" type="image/webp"><img src="/guides/{SL}/images/{k}.jpg" alt="{alt}" width="{w}" height="{h}" loading="{ld}" {ims}></picture><figcaption style="font-size:13px;color:var(--enshu);margin-top:10px;text-align:center;line-height:1.6;">{cap}.<br>Photo: {a}, <a href="{lu}" target="_blank" rel="noopener" style="color:var(--enshu);">{ln}</a>, via <a href="{cl}" target="_blank" rel="noopener" style="color:var(--enshu);">Wikimedia Commons</a> (resized)</figcaption></figure>
'''
s=open(R+'guides/gifu-castle/index.html',encoding='utf-8').read()
i=s.index('<main>'); j=s.index('</main>'); head,tail=s[:i],s[j:]
TITLE="Tokyo Daijingu Guide: Tokyo's Ise Shrine, Japan's First Shinto Wedding and Love Charms"
DESC="A licensed guide's guide to Tokyo Daijingu in Iidabashi: why it is called Tokyo's Ise Shrine, how it began Shinto weddings, the matchmaking deities, English love fortunes, hours and access."
TAG="Tokyo's Ise Shrine, five minutes from Iidabashi Station."
head=re.sub(r'<title>.*?</title>',f'<title>{TITLE} | Sacred Japan</title>',head,count=1)
head=re.sub(r'(<meta (?:name="description"|property="og:description"|name="twitter:description") content=")[^"]*(")',lambda m:m.group(1)+DESC+m.group(2),head)
head=re.sub(r'(<meta (?:property="og:title"|name="twitter:title") content=")[^"]*(")',lambda m:m.group(1)+TITLE+m.group(2),head)
head=re.sub(r'("headline": ")[^"]*(")',lambda m:m.group(1)+TITLE+m.group(2),head)
head=re.sub(r'("description": ")A licensed[^"]*(")',lambda m:m.group(1)+DESC+m.group(2),head)
head=re.sub(r'("date(?:Published|Modified)": ")[^"]*(")',lambda m:m.group(1)+'2026-11-25'+m.group(2),head)
head=re.sub(r'<meta name="keywords" content="[^"]*">','<meta name="keywords" content="Tokyo Daijingu, Tokyo Daijingu shrine, matchmaking shrine Tokyo, Iidabashi shrine, Shinto wedding, love fortune omikuji, Tokyo Ise shrine">',head)
head=head.replace('guides/gifu-castle',f'guides/{SL}').replace('guide_gifu_castle_','guide_tokyo_daijingu_').replace('og-guides-gifu-castle',f'og-guides-{SL}')
head=head.replace('岐阜城','東京大神宮').replace('Gifu Castle','Tokyo Daijingu')
head=re.sub(r"<h1>.*?</h1>","<h1><em>Tokyo Daijingu</em>: Tokyo's Ise Shrine, Japan's First Shinto Wedding and Love Charms</h1>",head,count=1,flags=re.S)
head=head.replace("Nobunaga's mountain castle above Gifu, with the keep closed until late 2027.",TAG)
head=head.replace('SACRED JAPAN GUIDES ／ 城','SACRED JAPAN GUIDES ／ 神社')
IL='class="inline-link"'
faqs=[
("What kind of shrine is Tokyo Daijingu?","It was founded in 1880 with the approval of Emperor Meiji so that people in Tokyo could worship the deities of the Grand Shrine of Ise from afar (official site). That is why it is affectionately called Tokyo's Ise Shrine. It is also known for matchmaking, and for being the shrine that began Shinto weddings for the public."),
("What are the opening hours?","The gate is open 6:00 to 21:00, charms and amulets are given out 8:00 to 19:00, and goshuin (shrine stamps) are received 9:00 to 17:00 (Visit Chiyoda, GO TOKYO). Hours can change, so check the shrine's official site before you go."),
("Is there an admission fee?","I know of no entrance fee for the grounds. Charms, fortunes and goshuin are paid for separately, and GO TOKYO lists payment as cash, so bring coins."),
("Are the love fortunes available in English?","Yes. GO TOKYO says omikuji fortunes are available in English, and Japan Travel and Tsunagu Japan report the same. One writer paid 200 yen for a fortune (Japaholic), but prices and designs change, so ask at the office."),
("How do I get there?","About five minutes on foot from Iidabashi Station: the JR West Exit, Tokyo Metro Yurakucho or Namboku Line exit B2a, or Tokyo Metro Tozai Line or Toei Oedo Line exit A4 (Visit Chiyoda, GO TOKYO). The address is 2-4-1 Fujimi, Chiyoda City."),
("When is the best time to visit?","Weekday mornings are my advice, because the shrine is popular with visitors seeking good relationships and the courtyard can fill up, as in the photos above. Expect crowds at New Year and on weekends."),
]
faq_json=',\n'.join('''    {
      "@type": "Question",
      "name": %s,
      "acceptedAnswer": {
        "@type": "Answer",
        "text": %s
      }
    }'''%(json.dumps(q),json.dumps(re.sub('<[^>]+>','',a))) for q,a in faqs)
head=re.sub(r'("mainEntity": \[\n).*?(\n  \]\n\}\n</script>\n\n<!-- ── GOOGLE)',lambda m:m.group(1)+faq_json+m.group(2),head,flags=re.S)
hh=re.sub(r'"mainEntity": \[.*','',head,flags=re.S)
assert not re.search('Gifu|Nobunaga|castle|Castle',re.sub(r'<nav>.*?</nav>','',hh,flags=re.S).replace('Castles','')),re.findall('.{30}(?:Gifu|Nobunaga|astle).{20}',hh)
main='''<main>

  <aside class="toc" aria-label="Table of contents">
    <div class="toc-label">TABLE OF CONTENTS ／ 目次</div>
    <div class="toc-title">In This Guide</div>
    <ol>
      <li><a href="#opening">Tokyo's Ise Shrine</a></li>
      <li><a href="#history">How It Began</a></li>
      <li><a href="#deities">The Deities and the Matchmaking</a></li>
      <li><a href="#wedding">Japan's First Shinto Wedding</a></li>
      <li><a href="#walk">A Walk Through the Precinct</a></li>
      <li><a href="#charms">Fortunes, Charms and Ema</a></li>
      <li><a href="#visit">Visiting Tokyo Daijingu</a></li>
      <li><a href="#faq">Frequently Asked Questions</a></li>
      <li><a href="#final">Before You Go</a></li>
    </ol>
  </aside>

  <article>

'''+fig('front','Front of the Tokyo Daijingu worship hall with a purple curtain, white chrysanthemum crests and visitors praying','The front of the worship hall, with its purple curtain and chrysanthemum crests',hero=True)+'''
    <section id="opening">
      <p class="opening">As a licensed guide, I often tell visitors that Tokyo has a small copy of Japan's holiest shrine, and that it is tucked behind office buildings five minutes from a train station. Tokyo Daijingu was founded so that people in the capital could pray to the deities of the Grand Shrine of Ise without making the long journey. It is still called <em>O-Ise-sama</em>, &ldquo;Tokyo's Ise Shrine,&rdquo; and today it is just as well known as a place to pray for good relationships.</p>
      <p>This guide covers the history, the deities, the shrine's claim to have begun Shinto weddings for the public, a walk through the precinct in photos, and the practical details.</p>
    </section>

    <h2 id="history">How It Began<span class="h2-jp">由緒</span></h2>
    <p>According to the shrine's own history, a new shrine was built in Tokyo in 1880 with the approval of Emperor Meiji, so that people in Tokyo could worship the deities enshrined at Ise from afar (official site). At first it was called <em>Hibiya Daijingu</em>, after the district where it stood. After the Great Kanto Earthquake of 1923 it moved to its present site in Iidabashi, in 1928, and was renamed <em>Iidabashi Daijingu</em>. It took the name Tokyo Daijingu after the war; GLTJP gives 1946 for the change, and I have not seen that year on the official English page, so I treat it as a single-source date.</p>
    <p>Tokyo Daijingu is counted among the Five Major Shrines of Tokyo (GLTJP, Tsunagu Japan), together with places such as Meiji Jingu. For the wider picture of Ise itself, see our <a href="/guides/ise-grand-shrine/" '''+IL+''' onclick="trackEvent('click','internal','guide_tokyo_daijingu_to_ise')">Ise Grand Shrine guide</a>.</p>

    <h2 id="deities">The Deities and the Matchmaking<span class="h2-jp">御祭神</span></h2>
    <p>The enshrined deities are those of Ise: Amaterasu-Sume-Okami and Toyouke-no-Okami, together with Yamatohime-no-Mikoto, whom the official site calls the founder of the Inner Shrine of Ise. The shrine also honors the three deities of creation and growth, Ame-no-Minakanushi, Takamimusubi and Kamimusubi.</p>
    <p>That last group explains the matchmaking reputation. Visit Chiyoda says these deities oversee <em>musubi</em>, the binding together of all things, so the shrine is known for blessings of good relationships, and people come from all over Japan to pray for them. In my own tours, I add that visitors pray here for many kinds of connection: partners, but also work and friends, as GLTJP notes.</p>

    <h2 id="wedding">Japan's First Shinto Wedding<span class="h2-jp">神前結婚式</span></h2>
    <p>The shrine is known as the first to hold Shinto wedding ceremonies in Japan. The story, as Walker Plus and GLTJP tell it, begins in 1900 (Meiji 33), when the wedding of the Crown Prince, later Emperor Taisho, was held before the deities in the Kashikodokoro sanctuary of the Imperial Palace. To commemorate it, Tokyo Daijingu began ceremonies of the same kind for the general public. Wikipedia and GO TOKYO date the first wedding at the shrine to 1901, so you will see both years.</p>
    <p>Weddings are still held here today. Walker Plus and a wedding venue listing mention a celebratory dance performed by shrine maidens, the <em>Toyohogi no Mai</em>, said to be unique to the shrine. That detail comes from those two sources only, so I mention it as something to look for if you see a ceremony, and not as a fixed feature. If you see a bridal party, please keep your distance.</p>

    <h2 id="walk">A Walk Through the Precinct<span class="h2-jp">境内</span></h2>
    <p>I will take you through in the order a visitor walks. It begins at the street.</p>
'''+fig('torii','A plain wooden torii and a stone marker reading Tokyo Daijingu above a short flight of stone steps, with trees on both sides','The torii and the stone marker reading Tokyo Daijingu, seen from the street')+'''
    <p>The precinct begins at a plain wooden torii and a tall stone marker carved with the shrine's name, at the top of a short flight of steps. Behind the torii, you can already see a gate and, through it, the purple curtain of the hall. A teal banner on the left appears to refer to Ise Jingu, as I read it.</p>
'''+fig('shinmon','A gate with vermilion pillars and white crest curtains at the top of stone steps, with red banners and a purple curtain visible beyond','The vermilion gate at the top of the steps')+'''
    <p>At the top of the steps stands a gate with vermilion pillars and white curtains, with red offering banners on its right. The banner on its left reads, as I read it, something like &ldquo;Let us visit Ise Jingu, the home of the heart.&rdquo; A small sign in front of the steps reminds visitors to purify themselves and then worship.</p>
'''+fig('temizuya','A wooden water pavilion with a bronze dragon, a banner about Ise Jingu talismans and a sign about the 62nd Ise Jingu rebuilding','The water pavilion, with a bronze dragon at the back')+'''
    <p>Purify your hands and mouth here before you go on. A bronze dragon sits at the back of the basin. The white banner on the right urges visitors to enshrine an Ise Jingu talisman, and the sign beside it appears to refer to the 62nd rebuilding of Ise Jingu in autumn 2013, so this photo seems to date from around that time. Traffic cones and blue sheets show the shrine was working on something nearby; I would not expect them now.</p>
'''+fig('basin','A granite basin with wooden channels from which water runs down, and a bronze dragon and a sign about how to purify behind','The basin, where water runs down wooden channels')+'''
    <p>Here is a detail I enjoy: there are no ladles. Water runs down a row of wooden channels, and a sign gives the steps. As I read it, you wash both hands under the running water, cup water in your hand to rinse your mouth, and wash both hands again. Compare this with the routine in our <a href="/culture/shrine-etiquette/" '''+IL+''' onclick="trackEvent('click','internal','guide_tokyo_daijingu_to_etiquette')">shrine etiquette guide</a>.</p>
'''+fig('gate-view','A view from inside a wooden gate across a pebble garden and a paved path to the hall with a purple curtain','Through the gate, along the paved path to the hall')+'''
    <p>From inside the gate the precinct opens out: a paved path runs across a garden of dark pebbles and stepping stones to the hall, with lanterns on either side. The courtyard is small, which is part of why it feels so intimate and why it fills up quickly.</p>
'''+fig('approach','The hall seen from a distance across a pebble garden, with visitors in front of a purple curtain and stone lanterns on both sides','The hall at the end of the stone path')+'''
    <p>This is the approach as you walk up the path: lanterns left and right, a purple curtain at the front of the hall, and crossed finials on the ridge. The chrysanthemum crests on the curtain are the shrine's most visible emblem.</p>
'''+fig('praying','Visitors praying in front of three offering boxes under a purple curtain with white chrysanthemum crests','Visitors praying at the offering boxes')+'''
    <p>At the hall, visitors pray in front of three offering boxes under the purple curtain. The usual routine is a coin, two bows, two claps, a silent prayer and one bow; the shrine usually has a leaflet in English describing how to pray (Wanderlog reviewer, single source), so ask at the office if you are unsure.</p>
'''+fig('roof','The roof of the hall seen from the side, with crossed finials and a row of logs with gold ends against a blue sky','The roof, with crossed finials and gold-capped logs')+'''
    <p>Look up at the roof. Crossed finials (<em>chigi</em>) rise at the ends of the ridge, and a row of logs capped in gold (<em>katsuogi</em>) runs along it. These are roof details that shrine buildings are often identified by; our <a href="/culture/shrine-architecture/" '''+IL+''' onclick="trackEvent('click','internal','guide_tokyo_daijingu_to_architecture')">shrine architecture guide</a> explains what they are.</p>
'''+fig('crowd','A crowd of visitors at the side of the hall in front of an amulet window with a red awning, with a green roof above','The busy side of the hall, near the amulet window')+'''
    <p>This is the busy side of the hall, where the amulet window is, under a red awning. On a good-weather day the area fills with visitors queuing for charms and fortunes. It is the reason I recommend a weekday morning.</p>
'''+fig('inside','The lit interior of the shrine hall seen through glass doors, with bamboo blinds with tassels, lanterns and rows of folding tables','The interior of the hall, seen through the glass doors')+'''
    <p>Through the glass doors you can see the interior: bamboo blinds with tassels, white curtains with crests, lanterns, and rows of low tables. Shinto weddings and rituals take place in a hall like this, though I cannot tell from the photo which ceremony it is set up for.</p>

    <h2 id="charms">Fortunes, Charms and Ema<span class="h2-jp">おみくじ・お守り・絵馬</span></h2>
    <p>The shrine is known for its fortune slips and charms. GO TOKYO says you can draw a love fortune in English, and Japan Travel reports that the staff had boxes of English omikuji ready. Tsunagu Japan notes that the shrine has many types of fortune slip, some even by blood type. Many charms are themed around love and relationships; one travel site counts over 40, including a lily-of-the-valley design (Magical Trip, single source), so I would browse the window and see what is on offer that day. Designs and prices change.</p>
'''+fig('ema','A wooden rack hung with colorful illustrated ema plaques beside the hall, with visitors reading them and a stall with white cloths on the right','Illustrated ema plaques on a rack beside the hall')+'''
    <p>Beside the hall, a wooden frame is hung with <em>ema</em>, the wooden wishing plaques. The ones here are printed with colorful illustrations, and GO TOKYO calls them colorful and quirky. Visitors stop to read what others have written. If you write one, keep your personal details off it; the plaques are on public display.</p>

    <h2 id="visit">Visiting Tokyo Daijingu<span class="h2-jp">アクセス</span></h2>
    <ul class="practical-list">
      <li><strong>Address:</strong> 2-4-1 Fujimi, Chiyoda City, Tokyo.</li>
      <li><strong>Hours:</strong> gate 6:00 to 21:00; charms 8:00 to 19:00; goshuin 9:00 to 17:00 (Visit Chiyoda, GO TOKYO). Please check the official site.</li>
      <li><strong>Access:</strong> about 5 minutes from Iidabashi Station: JR West Exit, Metro exit B2a (Yurakucho and Namboku Lines) or exit A4 (Tozai and Oedo Lines) (Visit Chiyoda).</li>
      <li><strong>Cost:</strong> I know of no entrance fee. Fortunes, charms and goshuin are extra, in cash.</li>
      <li><strong>Best time:</strong> a weekday morning; New Year and weekends are crowded.</li>
      <li><strong>Pair it with:</strong> <a href="/guides/meiji-jingu/" '''+IL+''' onclick="trackEvent('click','internal','guide_tokyo_daijingu_to_meiji')">Meiji Jingu</a> for a larger shrine, or the <a href="/anime/love-live/" '''+IL+''' onclick="trackEvent('click','internal','guide_tokyo_daijingu_to_love_live')">Love Live! pilgrimage</a> at Kanda Myojin, also in Chiyoda.</li>
    </ul>
    <div class="key-callout">
      <p>&#127890; <strong>Plan your trip:</strong> Browse tours or find a hotel near Iidabashi. <a href="https://www.viator.com/search/Tokyo%20shrine?pid=P00298374&amp;mcid=42383&amp;medium=link&amp;campaign=sacred-japan" target="_blank" rel="noopener" onclick="trackEvent('click','affiliate','viator_tokyo_daijingu_inline')">Find tours on Viator &rarr;</a></p>
    </div>

    <h2 id="faq">Frequently Asked Questions<span class="h2-jp">よくあるご質問</span></h2>
    <div class="faq-stack">
'''+''.join(f'''    <details class="faq-item">
        <summary>{q}</summary>
        <div class="faq-answer">{a}</div>
    </details>
''' for q,a in faqs)+'''    </div>

    <h2 id="final">Before You Go<span class="h2-jp">むすびに</span></h2>
    <p>Go in on a quiet morning, purify at the water pavilion, and look up at the roof before you leave. A small shrine in the middle of the city can still feel like a long journey made short.</p>

    <div class="closing-block">
      <span class="torii">&#9961;&#65039;</span>
      <p>Ise is far away, but Tokyo found a way to bring it home.</p>
    </div>

    <section class="related-section">
      <h2>Related Guides</h2>
      <span class="h2-jp">関連ガイド</span>
      <div class="related-grid">
        <a class="related-card" href="/guides/ise-grand-shrine/" onclick="trackEvent('click','internal','related_tokyo_daijingu_to_ise')">
          <div class="related-card-label">SACRED JAPAN ／ GUIDES</div>
          <div class="related-card-title">&#9961;&#65039; Ise Grand Shrine Guide &rarr;</div>
          <div class="related-card-desc">The shrine Tokyo Daijingu was founded to worship.</div>
        </a>
        <a class="related-card" href="/culture/shrine-etiquette/" onclick="trackEvent('click','internal','related_tokyo_daijingu_to_etiquette')">
          <div class="related-card-label">SACRED JAPAN ／ CULTURE</div>
          <div class="related-card-title">&#128591; Shrine Etiquette Guide &rarr;</div>
          <div class="related-card-desc">How to purify, bow and pray.</div>
        </a>
        <a class="related-card" href="/guides/meiji-jingu/" onclick="trackEvent('click','internal','related_tokyo_daijingu_to_meiji')">
          <div class="related-card-label">SACRED JAPAN ／ GUIDES</div>
          <div class="related-card-title">&#127795; Meiji Jingu Guide &rarr;</div>
          <div class="related-card-desc">Tokyo's most visited shrine.</div>
        </a>
      </div>
    </section>

  </article>

'''
tail=tail.replace('gifu-castle',SL).replace('gifu_castle','tokyo_daijingu').replace('DGifu','DTokyo%20Daijingu').replace('search/Gifu','search/Tokyo%20shrine')
def L(u,l,t): return f'<a href="{u}" target="_blank" rel="noopener" style="color:var(--beni);text-decoration:underline;" onclick="trackEvent(\'click\',\'external\',\'{l}\')">{t}</a>'
src='Sources verified at time of writing: '+', '.join([
 L('https://tokyodaijingu.or.jp/english/index_e.html','src_tdj_official','Tokyo Daijingu official site'),
 L('https://visit-chiyoda.tokyo/app/spot/detail/152','src_tdj_chiyoda','Visit Chiyoda'),
 L('https://www.gotokyo.org/en/spot/42/','src_tdj_gotokyo','GO TOKYO'),
 L('https://www.gltjp.com/en/article/item/21412/','src_tdj_gltjp','GLTJP'),
 L('https://en.wikipedia.org/wiki/Tokyo_Daijingu','src_tdj_wiki','Wikipedia'),
 L('https://www.walkerplus.com/article/1006230/','src_tdj_walker','Walker Plus'),
 L('https://www.tsunagujapan.com/wow_02483/','src_tdj_tsunagu','Tsunagu Japan'),
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
l1="Tokyo Daijingu Guide:"; l2="Tokyo's Ise Shrine"; assert d.textlength(l2,font=f1)<1090
d.text((66,170),l1,font=f1,fill=(26,15,15)); d.text((66,238),l2,font=f1,fill=(26,15,15)); d.text((66,332),"東京大神宮",font=f2,fill=(138,125,120))
im.save(R+f'images/og/og-guides-{SL}.jpg',quality=88)
b=Image.open(D+'images/front.jpg'); w,h=b.size; ch=round(w*400/640); t=max(0,(h-ch)//2)
th=b.crop((0,t,w,t+ch)).resize((640,400),Image.LANCZOS); th.save(R+'images/hub/tokyo-daijingu.jpg',quality=84); th.save(R+'images/hub/tokyo-daijingu.webp',quality=80)
print('built',len(out))
