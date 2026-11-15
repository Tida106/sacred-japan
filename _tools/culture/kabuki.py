import re, os, json
R='/home/claude/sacred-japan'
S='kabuki'
OUT=f'{R}/culture/{S}'
os.makedirs(OUT,exist_ok=True)

def link(href,txt,lab): return f'<a href="{href}" class="inline-link" onclick="trackEvent(\'click\',\'internal\',\'{lab}\')">{txt}</a>'
def ext(href,txt,lab): return f'<a href="{href}" target="_blank" rel="noopener" onclick="trackEvent(\'click\',\'external\',\'{lab}\')">{txt}</a>'
VI='https://www.viator.com/search/kabuki?pid=P00298374&amp;mcid=42383&amp;medium=link&amp;campaign=sacred-japan'
EX='https://expedia.com/affiliate?siteid=1&amp;landingPage=https%3A%2F%2Fwww.expedia.co.jp%2FHotel-Search%3Fdestination%3DTokyo&amp;camref=1101l5JmFa&amp;creativeref=1011l87782&amp;adref=PZf6lQ77e8'
WJ='https://www.az.emb-japan.go.jp/files/000180843.pdf'
GATE='https://thegate12.com/article/5'
GLT='https://www.gltjp.com/en/article/item/10015/'
GLT2='https://www.gltjp.com/en/article/item/20707/'
JAPN='https://japn-com.pages.dev/kabuki-theater-guide/'
KYO='https://kyoto.travel/en/travel-inspiration/kabuki-theater/'
GOGO='https://gogonihon.com/en/?p=110724'
MET='https://metropolisjapan.com/living-national-treasure/'
PIM='https://blog.pimsleur.com/?p=27934'
SAK='https://blog.sakura.co/blog/a-complete-guide-to-kabuki-theater'
NOM='https://www.getnomad.app/destination-guides/watching-kabuki-in-Japan'
JTR='https://www.japan.travel/en/guide/theater/'
KAN='https://www.kanpai-japan.com/japanese-arts-and-history/kabuki'
FAD='https://factsanddetails.com/japan/cat20/sub131/item715.html'
SHI='https://en.shinohara-engeki.jp/?p=1898'
KWEB='https://www.kabukiweb.net/'

faqs=[
("Do I need to understand Japanese to enjoy kabuki?","No, but you will want help. The Gate (a Tokyo tourism site) says kabuki's old-style Japanese is hard even for many native speakers, and that Kabukiza offers an English caption guide on a small screen, like an airplane seatback. GLTJP and the National Theatre also mention English guides. Please check the day's availability before you go."),
("Can I watch just one act?","At Kabukiza, yes. These single-act tickets are called <em>hitomakumi</em> or <em>makumi</em>. The Gate says the seats are on the fourth floor, about 90 seats plus standing room for about 60, and that an act runs from about 30 minutes to 1.5 hours. Prices are reported as roughly &yen;1,000 to &yen;3,000, depending on the source."),
("How much do full tickets cost?","Sources disagree a little. The Gate gives &yen;3,000 to &yen;20,000 per session; other guides give up to &yen;25,000 for the best seats. Prices depend on the seat and the program, so check the official ticket site for your date."),
("Can I take photos?","Not during the performance. Pimsleur's kabuki etiquette guide says to turn off your phone, refrain from any photography and stay in your seats. Kabukiza also has a gallery where, GLTJP says, you can touch props and take photographs, which is a better place for pictures."),
("Why are all the actors men?","Because of a shogunate ban. The Web Japan introduction says women's troupes were banned in 1629 because of links to prostitution, and young men's kabuki followed in 1652. The male actors who played women's roles, <em>onnagata</em>, then became a specialty. Kabuki was started by a woman, Izumo no Okuni, and that is one of its best-known ironies."),
("What should I shout from the audience?","I would not shout anything on your first visit. <em>Kakegoe</em> are shouted calls, usually an actor's house name, at a precise moment, and Sakura's guide says that traditionally only men took part, though women now do too. Learn the timing by listening to the regulars before you join in."),
("Is kabuki the same as noh?","No. Noh is the older, slower, mask-based art that kabuki borrowed from. The Web Japan introduction says the kabuki stage gradually evolved out of the noh stage, and that some kabuki plays are adapted from noh. Noh is a separate guide for later."),
]
faq_html=''.join(f"""      <details class="faq-item">
        <summary>{q}</summary>
        <div class="faq-answer">{a}</div>
      </details>

""" for q,a in faqs)
faq_ld=json.dumps({"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":re.sub('<[^>]+>','',a)}} for q,a in faqs]},ensure_ascii=False,indent=2)

TITLE="Kabuki Guide: Its History, Makeup, Famous Plays and How to Watch at Kabukiza"
DESC="A licensed guide's English introduction to kabuki: how a shrine maiden's dance became Japan's great theater, why only men perform it now, what the makeup and poses mean, and how to buy full or single-act tickets at Kabukiza."
URL=f"https://sacred-japan.net/culture/{S}/"
OG="https://sacred-japan.net/images/og/og-culture-kabuki.jpg"

CAPST='font-size:13px;color:var(--enshu);margin-top:10px;text-align:center;line-height:1.6;'
LA='style="color:var(--enshu);"'
CMB='https://commons.wikimedia.org/wiki/File:'
def lk(t,u): return f'<a href="{u}" target="_blank" rel="noopener" {LA}>{t}</a>'
def csearch(q): return 'https://commons.wikimedia.org/w/index.php?search='+q+'&title=Special:MediaSearch&type=image'
def pfig(src,alt,desc,cred,mw=760):
    return (f'<figure style="margin:36px auto;max-width:{mw}px;">\n      <picture><source srcset="/culture/kabuki/images/{src}.webp" type="image/webp"><img src="/culture/kabuki/images/{src}.jpg" alt="{alt}" loading="lazy" style="width:100%;height:auto;border-radius:4px;display:block;"></picture>\n      <figcaption style="{CAPST}">{desc}<br>{cred}</figcaption>\n    </figure>')
PDL=lk("public domain","https://commons.wikimedia.org/wiki/Commons:Public_domain")
def cm(q): return lk("Wikimedia Commons",csearch(q))
f_ebizo=pfig('ebizo-kumadori','Woodblock print of an actor shown from the chest up, facing the viewer with a white face painted with bold red lines, eyes turned sharply to one side, a tall black hat, wide black sleeves and a red collar, in front of a cream background with a fan-shaped title panel at top left','A kumadori portrait: Ichikawa Ebizo V as Usui Sadamitsu, from an unnamed series of actor portraits past and present, September 1863 (Commons description). Notice how the red lines run out from the eyes and mouth to turn the face into a mask.',f'Utagawa Kunisada I (Toyokuni III), {PDL}, via {cm("Kunisada+Ichikawa+Ebizo+V+Usui+Sadamitsu+1863")} (resized); uploaded by Horst Gr&auml;ber, 2012',420)
f_shib1=pfig('shibaraku-toyokuni','Woodblock print of an actor in an enormous red robe with huge white square-spiral patterns on the sleeves, a pale face, a tall black headdress with white points and a very long sword at his side','Ichikawa Danjuro in the play <em>Shibaraku</em>, 1812. The giant robe is part of the show: the hero bursts in and the stage fills with colour. LACMA, M.2003.168.1.',f'Utagawa Toyokuni I, {PDL} (LACMA public-domain release), via {cm("Utagawa+Toyokuni+Ichikawa+Danjuro+Kabuki+Play+Shibaraku")} (resized)',420)
f_shib2=pfig('shibaraku-kuniyoshi','Woodblock print on a blue background of a figure in a huge red robe with white square-spiral patterns crouched at the left, a woman in a pale gold robe in the middle and a man in a patterned robe seated at the right, with plum blossoms across the top','A print of a scene from <em>Shibaraku</em> or a play based on it, made between 1849 and 1851. Commons names Ichikawa Ebizo V as Kamakura Gongoro Kagemasa (left), Iwai Kumesaburo III as Princess Katsura no Mae and another actor as Prince Kamo Jiro Yoshitsuna (right); I have not matched the names to the figures.',f'Utagawa Kuniyoshi, {PDL}, via {cm("Kuniyoshi+Sadakiyo+Shinno+Yahazu+no+Okaji+Arajiro+Yoshizumi")} (resized); uploaded by Petrusbarbygere, 2005')
f_yura=pfig('yuranosuke','Woodblock print of an actor with a stern pale face, a thick black fur collar and cloak, a sword slung over the shoulder, against a deep blue night sky with a thin crescent moon','The actor Kataoka Nizaemon as Oboshi Yuranosuke, leader of the 47 ronin, second month of 1862 (LACMA title). This is the hero of <em>Kanadehon Chushingura</em>, the play based on the 1701-1703 incident mentioned below.',f'Utagawa Kunisada (Toyokuni III), {PDL} (LACMA public-domain release), via {cm("Kunisada+Kataoka+Nizaemon+Oboshi+Yuranosuke+LACMA")} (resized)',420)
f_koi=pfig('koi-zumo','Very wide woodblock print of five panels joined together, showing five actors in colourful robes standing and sitting in a row in front of a gold and green screen with pine trees','A five-sheet print of a scene from <em>Koi-zumo Yawaragi Soga</em>, January 1841. Commons lists the actors from the right as Iwai Shijaku I (Oiso no Tora), Sawamura Tossho I (Kudo Suketsune), Ichikawa Ebizo V (Goro Tokimune), Ichikawa Danjuro VIII (Juro Sukenari) and Iwai Tojaku I (Kewaizaka no Shosho). Museum of Fine Arts, Boston, 11.42167a-e.',f'Utagawa Kunisada, {PDL}, via {cm("Actors+Iwai+Shijaku+Oiso+no+Tora+Sawamura+Tossho+Kudo+Suketsune+Ichikawa+Ebizo")} (resized); uploaded by Tak1701d, 2019')
f_mitsu=pfig('mitsugoro','Woodblock print of an actor striding in a bold pose in a red robe with white fan patterns over a black kimono with wheel patterns, a sword held across his body, under pink cherry blossom branches on a cream background','Bando Mitsugoro III, about 1822 (Commons description: a colour woodblock print of the actor). I read the pose, with the whole body drawn into one shape, as the kind of thing the word <em>mie</em> describes.',f'Toyokawa Hikokuni, {PDL}, via {cm("Rising+Sun+Kabuki+Bando+Mitsugoro+III+c1822")} (resized); uploaded by Artanisen, 2021',420)
f_haka=pfig('hakamadare','Woodblock print of a half-length actor with a stern face looking to one side, a hairknot, a pale blue robe and a grey coat with white swirl crests, holding a long pipe-like object, against a blue background with vertical labels','A print titled simply <em>Kabuki Actor</em> in the Houston museum record, published in 1859, from the series <em>Toyokuni Manga Zue</em>. The Japanese description calls it a <em>mitate</em> print, one that likens the first Nakamura Fukusuke to Hakamadare Yasusuke. Museum of Fine Arts, Houston.',f'Utagawa Kunisada, {PDL}, via {cm("Utagawa+Kunisada+Kabuki+Actor+1859+Museum+of+Fine+Arts+Houston")} (resized)',420)
f_ichi=pfig('ichinotani','Three-sheet woodblock print of armoured warriors in dark lacquered armour with helmets, one beside a black horse at the water, one standing with a sword drawn, one leaping across a rocky slope','A triptych of a scene from Act 2 of <em>Ichinotani Futaba Gunki</em>, June 1851 (Commons). The actors named are Nakayama Bungoro II, Ichimura Takenojo V and Bando Shuka I. Museum of Fine Arts, Boston, 11.44012a-c.',f'Utagawa Kunisada, {PDL}, via {cm("Actors+Nakayama+Bungoro+II+Hirayama+Mushadokoro+Sueshige+Ichimura+Takenojo+V+Kumagai")} (resized); uploaded by Tak1701d, 2015')
f_futa=pfig('futatsu-chocho','Three-sheet woodblock print of three groups of figures against a green background with yellow flowers: a man grappling with another in black at the left, a woman in a pink and violet robe with a man in the middle, and two men fighting at the right','A triptych of a scene from Act 5 of <em>Futatsu Chocho Kuruwa Nikki</em>, February 1852 (Commons). The actors named include Ichikawa Danjuro VIII as Nuregami Chogoro and Iwai Kumesaburo III as Azuma of the Fujiya. Museum of Fine Arts, Boston, 11.43964a-c.',f'Utagawa Kunisada, {PDL}, via {cm("Actors+Ichikawa+Danjuro+VIII+Nuregami+Chogoro+Ichikawa+Saruzo+Yamasaki+Yogoro+Iwai+Kumesaburo")} (resized); uploaded by Tak1701d, 2015')
f_roof=pfig('satomi-roof','Woodblock print of two men fighting with swords across a steeply tiled grey roof with a golden fish ornament at the lower right, one in a red robe and one in dark armour','A fight on a tiled roof from the play <em>Satomi Hakkenden</em>, performed at the Ichimura theatre in January 1852. Commons names Seki Sanjuro III and Bando Shuka I as Inukai Genpachi and Inuzuka Shino. It is the upper part of a two-scene print; only the lower part is signed.',f'Utagawa Kunisada, {PDL}, via {cm("Kunisada+Seki+Sanjuro+III+Bando+Shuka+Inukai+Genpachi+Inuzuka+Shino+Satomi+hakkenden")} (resized); image from the U.S. Library of Congress (jpd.00053)')
f_neko1=pfig('nekomata-1','Three-sheet woodblock print of three actors in a row in front of a gold and black background, a man in a purple robe at the left with a sword, an old woman in a patterned robe seated in the middle with two white and spotted cats at her feet, and a man in grey at the right','One of two triptychs from the same July 1847 production of <em>Onoe Kikugoro uchidai banashi</em> at the Ichimura theatre. Commons lists the actors from the left as Ichimura Uzaemon XII, Onoe Baijiu (Onoe Kikugoro III) and Sawamura Sojuro V. The cats on the floor are what I notice first.',f'Utagawa Kunisada (signed Toyokuni), {PDL}, via {cm("Kunisada+triptych+Ichimura+Uzaemon+XII+Onoe+Baijiu+Sawamura+Sojuro+V+1847")} (resized); uploaded by Horst Gr&auml;ber, 2012')
f_neko2=pfig('nekomata-2','Three-sheet woodblock print with a figure in blue crouched at the left, a seated figure in a patterned robe in the middle with red flames rising behind, and another figure in a grey robe at the right, under a gold curtain','The second triptych of the same July 1847 production. This one is dated the same way but the order of the actors is reversed in Commons (from the left: Sawamura Sojuro V, Onoe Baijiu, Ichimura Uzaemon XII). The flames behind the middle figure suggest a ghost or spirit scene; that is my reading, not Commons.',f'Utagawa Kunisada (signed Toyokuni), {PDL}, via {cm("Kunisada+triptych+Sawamura+Sojuro+V+Onoe+Baijiu+Ichimura+Uzaemon+XII+1847")} (resized); uploaded by Horst Gr&auml;ber, 2012')

main=f"""<main>

  <!-- TABLE OF CONTENTS -->
  <aside class="toc" aria-label="Table of contents">
    <div class="toc-label">TABLE OF CONTENTS ／ 目次</div>
    <div class="toc-title">In This Guide</div>
    <ol>
      <li><a href="#opening">Opening: A Note from the Guide</a></li>
      <li><a href="#origin">A Shrine Maiden on a Dry Riverbed</a></li>
      <li><a href="#men">Why Only Men Perform</a></li>
      <li><a href="#stage">The Stage and What to Watch</a></li>
      <li><a href="#makeup">Makeup and the Colors</a></li>
      <li><a href="#plays">Three Kinds of Play</a></li>
      <li><a href="#where">Where to See Kabuki</a></li>
      <li><a href="#tickets">Tickets and Single Acts</a></li>
      <li><a href="#manners">Manners and Kakegoe</a></li>
      <li><a href="#faq">Frequently Asked Questions</a></li>
      <li><a href="#final">Final Thoughts</a></li>
    </ol>
  </aside>

  <article>

    <section id="opening">
      <p class="opening">A man in white paint and red lines across his face stops in the middle of a fight, glares at the audience and holds the pose, eyes crossed, for a long breath. Someone in the dark shouts a name. The whole theater exhales. That frozen moment, called a <em>mie</em>, is kabuki in a nutshell: it is not trying to look real, it is trying to look unforgettable.</p>
      <p>As a licensed guide, I find that kabuki is the easiest of Japan's classical theaters to enjoy as a visitor, because it is built to be spectacular. This guide explains where it came from, why only men perform it now, how to read the makeup, and how to buy a ticket without committing to five hours.</p>
    </section>

    <h2 id="origin">A Shrine Maiden on a Dry Riverbed<span class="h2-jp">出雲阿国と歌舞伎の始まり</span></h2>
    <p>The story starts in Kyoto in 1603. The {ext(WJ,'Web Japan introduction to kabuki','kabuki_webjapan_origin')} says kabuki is thought to have begun with dances and light theater performed there by Okuni, a female attendant at the Izumo shrine. Metropolis magazine adds that Izumo no Okuni danced with her troupe on the dry bed of the Kamo River, and that she dressed in costumes considered off-kilter for the time. Many sources call her a shrine maiden of Izumo, and I would say "said to be," since the details of her life are thin.</p>
    <p>The name explains the spirit. {ext(FAD,'Facts and Details','kabuki_factsdetails_name')} says <em>kabuki</em> is derived from a word meaning tilted, offbeat or outrageous, and the Gate says the performers copied the fashion of the <em>kabuki-mono</em>, the flamboyant rebels of the day. So the art form began as a show-off dance that borrowed its look from the street.</p>
    <p>If you have read our {link('/guides/izumo-taisha/','Izumo Taisha guide','kabuki_to_izumo')}, the link is a nice one: the shrine at the root of this story is the same Izumo, so the biggest popular theater in Japan has a shrine in its family tree.</p>

    {f_koi}

    <h2 id="men">Why Only Men Perform<span class="h2-jp">女形と禁止令</span></h2>
    <p>Kabuki started with women and ended up with men. The Web Japan introduction gives the sequence: the shogunate banned women's troupes in 1629 because of their links to prostitution; young men's (<em>wakashu</em>) kabuki became popular next but was banned in 1652; and adult men's kabuki (<em>yaro kabuki</em>) was then allowed to continue, under government rules to avoid sensual displays and to follow the conventions of kyogen.</p>
    <p>Out of that restriction came a specialty. Male actors who play women's roles are called <em>onnagata</em>, and the same source says their goal is to express the essence of the feminine, not to imitate women. The JAPN guide goes further and says that many consider their movement more feminine than that of actual women; that is an opinion, not a fact, but it shows how the art is valued.</p>
    <p>Two Edo-period actors also set the poles of acting. The Web Japan introduction says Ichikawa Danjuro I (1660-1704) pioneered the masculine, exaggerated <em>aragoto</em> style in Edo, while Sakata Tojuro I (1647-1709) developed the refined, realistic <em>wagoto</em> style in the Kyoto-Osaka area. You can still see the difference today: the Edo side is loud and heroic, the Kamigata side soft and human.</p>

    {f_mitsu}
    {f_haka}

    <h2 id="stage">The Stage and What to Watch<span class="h2-jp">舞台と見どころ</span></h2>
    <p>Kabuki has a vocabulary, and a few words make the show much easier.</p>
    <ul>
      <li><strong>Mie (<span class="jp">見得</span>):</strong> the climactic pose where the actor stops and holds a fixed stare, per the Web Japan introduction.</li>
      <li><strong>Hanamichi (<span class="jp">花道</span>):</strong> the "flower path," a runway that cuts through the audience for entrances and exits. Sit near it, and an actor will pass within arm's reach.</li>
      <li><strong>Revolving stage:</strong> the same source says it was first used in 1758, which lets a set change in front of your eyes.</li>
      <li><strong>Draw curtain:</strong> added to the stage that evolved from noh, it made complex multi-act plays possible.</li>
    </ul>
    <p>Music is live, with singers and shamisen players at the side, and a wooden clapper keeps time. I describe those from general knowledge of kabuki, not from the sources above, so treat them as a guide's impression.</p>
    <p>Edo's audience loved this too. The print by Utagawa Toyokuni III of the July 1858 production of <em>Shibaraku</em> that the JRailPass guide mentions is a good example, and our {link('/culture/ukiyo-e/','ukiyo-e guide','kabuki_to_ukiyoe')} explains how actors became the pop stars of those prints. The same Edo crowd is also behind our {link('/culture/sumo/','sumo guide','kabuki_to_sumo')}: the Japan Sumo Association itself says that, like kabuki, sumo became a mass attraction in the Edo period.</p>

    

    <h2 id="makeup">Makeup and the Colors<span class="h2-jp">隈取</span></h2>
    <p>The painted faces are called <em>kumadori</em>. {ext(KYO,'Kyoto Travel','kabuki_kyoto_makeup')} says the face is painted white, with thick red or blue lines on top, that the lines depend on the role, and that all the makeup is applied by the actors themselves. The Web Japan introduction says there are about a hundred styles.</p>
    <ul>
      <li><strong>Red:</strong> heroes, courage, justice and strength (Kyoto Travel, Web Japan, JAPN).</li>
      <li><strong>Blue or indigo:</strong> villains, jealousy, cold cunning or vengeful spirits. GLTJP specifically says blue is for powerful villains or vengeful spirits.</li>
      <li><strong>Brown:</strong> demons, ogres and supernatural beings (GLTJP, JAPN).</li>
    </ul>
    <p>Other sites give longer lists, with pink for youth or purple for nobility, but I found those in less careful sources, so I keep to the three that several agree on. The rule of thumb is simple: red is good, blue is bad, brown is not human.</p>

    {f_ebizo}
    {f_shib1}
    {f_shib2}
    {f_yura}

    <h2 id="plays">Three Kinds of Play<span class="h2-jp">時代物・世話物・所作事</span></h2>
    <p>The Web Japan introduction divides the repertoire into three main genres, each with an example it names:</p>
    <ul>
      <li><strong>Jidai-mono (historical plays):</strong> often set in an earlier era to avoid the censors. <em>Kanjincho</em> is adapted from the noh play <em>Ataka</em> and features Benkei's trick at a barrier checkpoint, and <em>Kanadehon Chushingura</em> is based on the 47 ronin incident of 1701-1703 (set in the Muromachi period on stage). If the warriors interest you, our {link('/culture/samurai/','samurai guide','kabuki_to_samurai')} gives the background.</li>
      <li><strong>Sewa-mono (domestic plays):</strong> more realistic, often based on recent scandals. <em>Benten Kozo</em> by Kawatake Mokuami (1816-1893) follows a thief and his gang.</li>
      <li><strong>Shosagoto (dance pieces):</strong> often used to show off the best onnagata. <em>Kyo-ganoko musume Dojoji</em> is the example given.</li>
    </ul>
    <p>For a first visit, I would pick a dance or a famous historical piece, since the plot matters less than the look. If the program is a dance, you will not need to follow the lines at all.</p>

    {f_ichi}
    {f_futa}
    {f_roof}
    {f_neko1}
    {f_neko2}

    <h2 id="where">Where to See Kabuki<span class="h2-jp">劇場ガイド</span></h2>
    <ul>
      <li><strong>Kabukiza, Ginza, Tokyo:</strong> the main venue. The Gate says the first Kabukiza opened in 1889 and the fifth, current one in 2013, with quakeproof construction and barrier-free access. Seating is reported at roughly 1,800 (JAPN) or 1,900 (Facts and Details), so I give no exact figure. Higashi-Ginza Station Exit 3 connects to the theater directly.</li>
      <li><strong>Minami-za, Kyoto:</strong> described as the oldest kabuki theater in Japan and the only one left in Kyoto, in the Gion area and near the Kamo River; Kanpai Japan says it was renovated in 2016. Both it and Kabukiza are run by Shochiku.</li>
      <li><strong>Shochikuza, Osaka:</strong> shows run less often, according to GetNomad.</li>
      <li><strong>National Theatre, Tokyo:</strong> GetNomad says it has "discovery" shows aimed at beginners, with English synopses, and Japan Travel says audio guides are provided for selected performances.</li>
      <li><strong>Others:</strong> Shinbashi Enbujo in Tokyo and Hakataza in Fukuoka also host kabuki runs, according to several guides.</li>
    </ul>
    <p>Kabukiza also has a gallery where, GLTJP says, you can try a carriage used in actual performances and touch the props. It is a good fallback if the schedule does not suit you.</p>

    <h2 id="tickets">Tickets and Single Acts<span class="h2-jp">チケットと一幕見</span></h2>
    <p>A normal Kabukiza program has a day and an evening session, each about 3 to 4 hours with intermissions of about 25 to 30 minutes, according to The Gate. That is a long time for a first visit, which is why the single act is so useful.</p>
    <h3>Full-session tickets</h3>
    <p>The Gate says standard tickets are sold online through Ticket Web Shochiku, or by phone, at about &yen;3,000 to &yen;20,000 per session. Other guides quote up to &yen;25,000, so check the official site. Monthly stories and casts are listed on {ext(KWEB,'Kabuki Web','kabuki_kabukiweb')}, which the Gate and the Shinohara guide both mention.</p>
    <h3>Single-act tickets (hitomakumi)</h3>
    <p>These are unique to Kabukiza. The Gate says the seats are on the fourth floor, about 90 seats plus a standing area for about 60, first-come, first-served, and sold at a box office to the left of the main entrance. The price is reported as about &yen;1,000 to &yen;3,000, and GLTJP and others say about &yen;2,000. The sources differ on the sale: the Gate and GLTJP say same day only, while GOGO Nihon says the seats were revived in June 2023 and can also be booked online from noon the day before. I would check the official page, and I would arrive early if a famous actor is in the cast, since the Gate says those acts sell out fast.</p>
    <h3>Captions</h3>
    <p>The Gate lists a caption guide with Japanese and English text for &yen;500 plus a &yen;1,000 deposit for a single act, and &yen;1,000 with an ID for a full show. GLTJP quotes an older price of &yen;700. Because the numbers differ, treat them as approximate.</p>
    <div class="key-callout" style="background:#fff8e6;border-left:4px solid var(--kin);padding:16px 20px;margin:28px 0;border-radius:2px;">
      <p style="margin:0;">&#127754; <strong>Plan your trip:</strong> Browse kabuki experiences in Japan, or find a stay in Tokyo. <a href="{VI}" target="_blank" rel="noopener sponsored" onclick="trackEvent('click','affiliate','viator_kabuki_local')">Browse kabuki experiences on Viator</a> &middot; <a href="{EX}" target="_blank" rel="noopener sponsored" onclick="trackEvent('click','affiliate','expedia_kabuki_local')">Find hotels in Tokyo</a></p>
    </div>

    <h2 id="manners">Manners and Kakegoe<span class="h2-jp">観劇のマナー</span></h2>
    <ul>
      <li><strong>Phones and cameras:</strong> Pimsleur's guide says to turn off your phone, refrain from photography and stay in your seat.</li>
      <li><strong>Food:</strong> The Gate says you may eat and drink at your seat during intermission, and a designated vendor sells bento boxes on the second basement floor.</li>
      <li><strong>Kakegoe:</strong> shouted calls from the audience, an old part of kabuki. Sakura's guide says only men traditionally took part, and women do now. As I said above, listen first.</li>
      <li><strong>Dress:</strong> the sources I read give no dress code, so I would say smart-casual is fine; that is my own view.</li>
    </ul>

    <h2 id="faq">Frequently Asked Questions<span class="h2-jp">よくあるご質問</span></h2>

    <div class="faq-stack">

{faq_html}    </div>

    <h2 id="final">Final Thoughts<span class="h2-jp">むすびに</span></h2>
    <p>If you remember one thing, remember the single act. One hour, a fourth-floor seat, a pair of English captions: that is enough to see a hero's pose, a villain's blue face and a revolving stage, and to understand why people have loved this for four centuries.</p>
    <p>If you enjoy this side of Japan, the Edo-period world around it is in our {link('/culture/ukiyo-e/','ukiyo-e guide','kabuki_to_ukiyoe2')} and {link('/culture/sumo/','sumo guide','kabuki_to_sumo2')}.</p>

    <div class="closing-block">
      <span class="torii">&#127754;</span>
      <p>A shrine maiden's dance, a painted face and a pose held a breath too long.</p>
    </div>

    <section class="related-section">
      <h2>Related Guides</h2>
      <span class="h2-jp">関連ガイド</span>
      <div class="related-grid">
        <a class="related-card" href="/culture/ukiyo-e/" onclick="trackEvent('click','internal','related_kabuki_to_ukiyoe')">
          <div class="related-card-label">SACRED JAPAN ／ GUIDE</div>
          <div class="related-card-title">&#127754; Ukiyo-e Guide →</div>
          <div class="related-card-desc">Edo woodblock prints, where kabuki actors were the stars.</div>
        </a>
        <a class="related-card" href="/culture/sumo/" onclick="trackEvent('click','internal','related_kabuki_to_sumo')">
          <div class="related-card-label">SACRED JAPAN ／ GUIDE</div>
          <div class="related-card-title">&#129474; Sumo Guide →</div>
          <div class="related-card-desc">The other Edo-era mass spectacle, with Shinto at its core.</div>
        </a>
        <a class="related-card" href="/culture/samurai/" onclick="trackEvent('click','internal','related_kabuki_to_samurai')">
          <div class="related-card-label">SACRED JAPAN ／ GUIDE</div>
          <div class="related-card-title">&#9876;&#65039; The Samurai Guide →</div>
          <div class="related-card-desc">The warriors behind Chushingura and Kanjincho.</div>
        </a>
        <a class="related-card" href="/guides/izumo-taisha/" onclick="trackEvent('click','internal','related_kabuki_to_izumo')">
          <div class="related-card-label">SACRED JAPAN ／ GUIDE</div>
          <div class="related-card-title">&#9961;&#65039; Izumo Taisha →</div>
          <div class="related-card-desc">The shrine at the root of Okuni's story.</div>
        </a>
      </div>
    </section>

    <p style="font-size:14px;color:var(--enshu);line-height:1.7;margin-top:32px;"><strong>Sources:</strong> {ext(WJ,'Web Japan: Kabuki','kabuki_src_webjapan')} (origins, bans, genres, plays, staging); {ext(GATE,'The Gate: Kabukiza','kabuki_src_gate')} (Kabukiza history, prices, single acts, captions; single-source figures are flagged); {ext(GLT,'GLTJP: single acts','kabuki_src_gltjp')} and {ext(GLT2,'GLTJP: guide to kabuki','kabuki_src_gltjp2')}; {ext(KYO,'Kyoto Travel','kabuki_src_kyoto')} and {ext(JAPN,'JAPN','kabuki_src_japn')} (makeup); {ext(MET,'Metropolis','kabuki_src_metropolis')} (Okuni on the Kamo riverbed); {ext(FAD,'Facts and Details','kabuki_src_fad')}; {ext(GOGO,'GOGO Nihon','kabuki_src_gogo')}; {ext(PIM,'Pimsleur','kabuki_src_pimsleur')} and {ext(SAK,'Sakura','kabuki_src_sakura')} (manners, kakegoe); {ext(NOM,'GetNomad','kabuki_src_getnomad')}, {ext(JTR,'Japan Travel','kabuki_src_jtravel')}, {ext(KAN,'Kanpai Japan','kabuki_src_kanpai')} and {ext(SHI,'Shinohara Engeki','kabuki_src_shinohara')} (theaters).</p>

  </article>

</main>"""

t=open(f'{R}/_tools/culture/tea.py',encoding='utf-8').read()
tail=t[t.index("s=open(f'{R}/culture/omamori-guide"):]
tail=tail.replace('<div class="hero-bg-kanji">茶道</div>','<div class="hero-bg-kanji">歌舞伎</div>')
tail=tail.replace('<h1>The Japanese <em>Tea Ceremony</em> Guide</h1>','<h1><em>Kabuki</em>: The Theater of Japan Guide</h1>')
tail=tail.replace('<div class="hero-jp">茶道ガイド</div>','<div class="hero-jp">歌舞伎ガイド</div>')
tail=tail.replace('What Happens, What to Do as a Guest, and Where to Try It','History, Makeup, Famous Plays and How to Watch at Kabukiza')
tail=tail.replace('Tea Ceremony Guide','Kabuki Guide')
tail=tail.replace('guide_tea','guide_kabuki').replace('viator_guide_tea_sticky','viator_guide_kabuki_sticky').replace('japanese+tea+ceremony','kabuki')
tail=re.sub(r'(<meta name="keywords" content=")[^"]*(")',r'\1kabuki, kabuki guide, Kabukiza, kabuki tickets, single act kabuki, onnagata, kumadori, Izumo no Okuni, kabuki makeup\2',tail)
tail=tail.replace('"datePublished":"2026-11-08","dateModified":"2026-11-08"','"datePublished":"2026-11-15","dateModified":"2026-11-15"')
exec(tail)
