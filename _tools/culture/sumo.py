import re, os, json
R='/home/claude/sacred-japan'
S='sumo'
OUT=f'{R}/culture/{S}'
os.makedirs(OUT,exist_ok=True)

def link(href,txt,lab): return f'<a href="{href}" class="inline-link" onclick="trackEvent(\'click\',\'internal\',\'{lab}\')">{txt}</a>'
def ext(href,txt,lab): return f'<a href="{href}" target="_blank" rel="noopener" onclick="trackEvent(\'click\',\'external\',\'{lab}\')">{txt}</a>'
VI='https://www.viator.com/search/sumo?pid=P00298374&amp;mcid=42383&amp;medium=link&amp;campaign=sacred-japan'
EX='https://expedia.com/affiliate?siteid=1&amp;landingPage=https%3A%2F%2Fwww.expedia.co.jp%2FHotel-Search%3Fdestination%3DTokyo&amp;camref=1101l5JmFa&amp;creativeref=1011l87782&amp;adref=PZf6lQ77e8'
JSA='https://www.sumo.or.jp/pdf/en/sumo_introduction.pdf'
WAT='https://watabi.org/en/articles/japan-sumo-guide'
GLT='https://www.gltjp.com/en/article/item/10024/'
WSH='https://en.wikipedia.org/wiki/Shinto_origins_of_sumo'
WDO='https://en.wikipedia.org/wiki/Dohy%C5%8D'
WNO='https://en.wikipedia.org/wiki/Nomi_no_Sukune'
TOM='https://gltjp.com/en/directory/item/10061'
PHJ='https://photojpn.org/matsuri/fukagawa/taka1.html'
SFM='https://sumofanmag.com/content/Issue_4/EdoTokyo2.htm'
SFG='https://sumofanmag.com/content/Issue_2/Sumo1011.htm'
JEX='https://www.japan-experience.com/all-about-japan/nara/temples-shrines/sumo-shrine'
FLIP='https://flipjapanguide.com/sumo-morning-practice/'
TAN='https://www.tanaka-tokyotours.com/tours/sumo-practice'
SEX='https://sumoexperience.com/business/watch-sumo-practice/'
ALL='https://allabout-japan.com/en/article/11460/'
JOD='https://thejapanode.com/guides/how-to-watch-sumo-japan'
NDL='https://jpsearch.go.jp/en/gallery/ndl-MEk8o2l88B3'
TIX='https://sumo.pia.jp/en/'

faqs=[
("How many sumo tournaments are there each year?","Six. They are called <em>honbasho</em> and are held in odd-numbered months: January, May and September in Tokyo, March in Osaka, July in Nagoya and November in Fukuoka. Each lasts 15 days, according to the Japan Sumo Association's own introduction."),
("Can I buy sumo tickets on the day?","Sometimes, but do not plan around it. WaTabi says same-day tickets are simply unsold reserved seats, sold through the web, convenience stores and the box office, and that if a date sold out in advance there are none. Treat it as a fallback."),
("Is it safe to buy tickets from resale sites?","I would stay with the official channels. WaTabi reports that the association prohibits resale for profit without its permission, names several third-party platforms, and says it takes no responsibility for tickets bought that way. The official face-value resale on the ticket site is the safer way to get a sold-out date."),
("What time should I arrive?","WaTabi suggests about 2 p.m. for a Tokyo tournament, because the top-division bouts come late in the day. For its September example it gives the top-division ring-entering ceremony at about 15:40 and the first top-division bout at about 16:05. Times shift a little by tournament, so check the day's schedule."),
("Can I watch morning practice during a tournament?","Usually not in Tokyo. One tour-company guide says that during the Tokyo tournament periods morning-practice viewing is off the table, and that the best window is the run-up to a Tokyo tournament. If your trip falls in a tournament month, look for dates just before it."),
("Why does sumo have so many rituals?","Because many of them come from Shinto. The Japan Sumo Association explains the salt as a way to expel evil from the sacred ring, and the roof over the ring resembles a shrine roof. Wikipedia's article on the Shinto origins of sumo adds that the referee dresses much like a priest and that a ring-blessing ceremony is held the day before each tournament."),
("Is sumo a religion?","No. It is a professional sport with a ranking system, salaries and a calendar. But it keeps a lot of Shinto form: the purifying salt, the stamping, the clapping and the shrine-like roof. I find it easiest to say that the sport grew out of ritual and still remembers it."),
]
faq_html=''.join(f"""      <details class="faq-item">
        <summary>{q}</summary>
        <div class="faq-answer">{a}</div>
      </details>

""" for q,a in faqs)
faq_ld=json.dumps({"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":re.sub('<[^>]+>','',a)}} for q,a in faqs]},ensure_ascii=False,indent=2)

TITLE="Sumo Guide: Shinto Rituals, the Six Tournaments, Tickets and Morning Practice"
DESC="A licensed guide's English introduction to sumo: why the ring is treated like a shrine, what the salt and stamping mean, how the ranks and six tournaments work, how to buy tickets, and where to follow sumo to its shrines in Tokyo."
URL=f"https://sacred-japan.net/culture/{S}/"
OG="https://sacred-japan.net/images/og/og-culture-sumo.jpg"

main=f"""<main>

  <!-- TABLE OF CONTENTS -->
  <aside class="toc" aria-label="Table of contents">
    <div class="toc-label">TABLE OF CONTENTS ／ 目次</div>
    <div class="toc-title">In This Guide</div>
    <ol>
      <li><a href="#opening">Opening: A Note from the Guide</a></li>
      <li><a href="#shrine">A Shrine in the Middle of an Arena</a></li>
      <li><a href="#rituals">What to Watch Before Each Bout</a></li>
      <li><a href="#origins">Where Sumo Comes From</a></li>
      <li><a href="#rules">How a Bout and a Career Work</a></li>
      <li><a href="#calendar">The Six Tournaments</a></li>
      <li><a href="#tickets">Tickets</a></li>
      <li><a href="#day">A Day at the Tournament</a></li>
      <li><a href="#stable">Morning Practice at a Stable</a></li>
      <li><a href="#shrines">Sumo Shrines to Visit</a></li>
      <li><a href="#faq">Frequently Asked Questions</a></li>
      <li><a href="#final">Final Thoughts</a></li>
    </ol>
  </aside>

  <article>

    <section id="opening">
      <p class="opening">Two very large men crouch at opposite ends of a clay ring. Each throws a handful of salt, stamps one foot into the ground, claps, and stares. Then, after minutes of this, they charge, and the bout is often over in seconds. Most of the drama of sumo is in what happens before the clash, and almost all of that is ritual.</p>
      <p>As a licensed guide, I think sumo is the easiest way to see Shinto practice in action without visiting a shrine. This guide explains the rituals, the rules, the six yearly tournaments, how to buy tickets, and how to follow sumo back to the shrines where it grew up.</p>
    </section>

    <h2 id="shrine">A Shrine in the Middle of an Arena<span class="h2-jp">土俵という聖域</span></h2>
    <p>The ring is called the <em>dohyo</em> (<span class="jp">土俵</span>). The {ext(JSA,'Japan Sumo Association','sumo_jsa_dohyo')} describes it as 6.7 m square and 60 cm high, made of a special clay with a thin layer of sand on top. The fights take place inside a circle a little over 4.55 m across, marked by straw bales, and part of the ring is rebuilt for every tournament: 20 cm of soil is removed and new soil is added.</p>
    <p>Above the ring hangs a roof, suspended from the ceiling by cables, and it looks like the roof of a shrine. Wikipedia's article on the {ext(WSH,'Shinto origins of sumo','sumo_wiki_shinto')} says the canopy is reminiscent of a Shinto shrine, and that the referee dresses much like a priest. World History Encyclopedia goes further and says the whole arrangement still enjoys the status of a sacred Shinto shrine. I would put it more carefully: it is not a shrine you can pray at, but it is a space that is treated as sacred.</p>
    <p>The day before a tournament opens there is a ring-blessing ceremony, the <em>dohyo matsuri</em>. According to {ext(WDO,'Wikipedia','sumo_wiki_dohyo')}, it is led by one of the head referees with two other referees standing in for Shinto priests, and it purifies the ring and invites the <em>kami</em> to watch. Wikipedia's Shinto-origins article adds that salt, kelp, dried squid and chestnuts are buried in the center of the ring. I read both as describing the usual form of the ceremony, not a rule written in stone.</p>
    <p>The referee, the <em>gyoji</em>, is part of the same picture. {ext(SFG,'Sumo Fan Magazine','sumo_sfm_gyoji')} says he wears a kimono-style costume that resembles the court dress of the Kamakura-period samurai, and a lacquered gauze hat that is quite like a Shinto priest's hat. If you have read our {link('/culture/what-is-shinto/','guide to Shinto','sumo_to_shinto')}, the look will feel familiar.</p>

    <h2 id="rituals">What to Watch Before Each Bout<span class="h2-jp">取組前の所作</span></h2>
    <p>These are the things that make first-time viewers ask "what is he doing?" The Japan Sumo Association's introduction and Wikipedia agree on the main points.</p>
    <ul>
      <li><strong>Salt:</strong> "Purifying salt is used to expel evil from the sacred area of the ring," the association says. The wrestlers scatter it before the bout.</li>
      <li><strong>Chikara-mizu:</strong> the "power water." The association says it symbolizes water that purifies the body, and the wrestlers rinse their mouths with it.</li>
      <li><strong>Stamping (<em>shiko</em>):</strong> raising a leg high and bringing it down hard. {ext(GLT,'GLTJP','sumo_gltjp_shiko')} describes it as stamping on the ring to stamp out evil spirits, and the association describes the champion's version in the same way.</li>
      <li><strong>Clapping:</strong> Wikipedia notes that this recalls the clapping at a shrine that attracts the attention of the gods.</li>
    </ul>
    <p>The most formal version is the champion's ring-entering ceremony, the <em>dohyo-iri</em>. The association says the highest-ranked wrestlers, the <em>yokozuna</em>, perform it with the most ceremony, wearing a heavy braided rope. Wikipedia says the ceremony is regarded as a purification ritual in its own right and is occasionally performed at shrines. The rope reminds me of the twisted <em>shimenawa</em> ropes that mark sacred places at shrines. That comparison is mine, not the association's, and our {link('/culture/what-is-shinto/','guide to Shinto','sumo_to_shinto2')} explains the shrine rope.</p>

    <h2 id="origins">Where Sumo Comes From<span class="h2-jp">相撲の起源</span></h2>
    <p>The oldest story is a legend. The Japan Sumo Association's introduction points to the tale of the contest between Nomi no Sukune and Taima no Kehaya in the <em>Nihon Shoki</em>, the chronicle completed in 720. {ext(WNO,'Wikipedia','sumo_wiki_nomi')} dates it, allegedly, to 23 BC: the emperor sent Nomi no Sukune against Taima no Kehaya, who had boasted that he was the strongest man under heaven. Nomi no Sukune won with kicks that killed him. Wikipedia is careful to say that this was not modern sumo, though Nomi no Sukune is regarded as its founder.</p>
    <p>The association also mentions a divine version: according to legend, the origin of the Japanese people depended on the outcome of a sumo match. I believe this refers to the contest between the gods Takemikazuchi and Takeminakata, though the association's text does not name them. Takeminakata's defeat is the story behind the main deity of Suwa Taisha, which you can read in our {link('/guides/suwa-taisha/','Suwa Taisha guide','sumo_to_suwa')}.</p>
    <p>A later layer is court ritual. The National Diet Library's entry, shown on the {ext(NDL,'Japan Search portal','sumo_ndl')}, says that during the Nara period an agricultural divination ritual known as <em>sumai no sechi-e</em> started. Sumo as a ritual for the harvest is also how several tourism writers explain its origin, so I treat the harvest link as common wisdom rather than a documented fact.</p>
    <p>The form we know belongs to the Edo period. The association says that, like kabuki, sumo became a mass attraction then. Sources agree that in 1684 fund-raising sumo (<em>kanjin-zumo</em>) was authorized, to raise money for building and repairing shrines and temples, and that it grew into the professional sport. They differ on details: GLTJP says the main tournament was held on the grounds of Tomioka Hachimangu for about a hundred years from 1684, while Sumo Fan Magazine says the first tournament after the revival was held at Eitaiji, a temple affiliated with the shrine. One source says the tournaments later moved to Ekoin temple in Ryogoku, in 1791, and I found that in only one place. You can see the Edo audience in our guide to {link('/culture/ukiyo-e/','ukiyo-e','sumo_to_ukiyoe')}, where wrestlers were popular print subjects.</p>

    <h2 id="rules">How a Bout and a Career Work<span class="h2-jp">ルールと番付</span></h2>
    <p>The rules are short. According to the association, a wrestler loses if he is forced or thrown out of the inner circle, or if any part of his body other than the soles of his feet touches the ground, including a knee, a fingertip or the topknot. It also lists forbidden acts such as striking with a fist, hair pulling, eye gouging and choking. The association counts 82 winning techniques, called <em>kimarite</em>.</p>
    <p>The wrestler wears a <em>mawashi</em>, a silk belt that the association says is about 9 m long and 80 cm wide, wound around the waist four to seven times. The association says there are about 700 wrestlers in professional sumo.</p>
    <h3>Ranks</h3>
    <p>Rank is called <em>banzuke</em>, and it is set by results in the six tournaments. From the top, the divisions are:</p>
    <ol>
      <li><strong>Makuuchi</strong> (the top division, up to 42 wrestlers), which contains the top ranks: <em>yokozuna</em>, <em>ozeki</em>, <em>sekiwake</em>, <em>komusubi</em>, then <em>maegashira</em></li>
      <li><strong>Juryo</strong></li>
      <li><strong>Makushita</strong></li>
      <li><strong>Sandanme</strong></li>
      <li><strong>Jonidan</strong></li>
      <li><strong>Jonokuchi</strong></li>
    </ol>
    <p>In each 15-day tournament the two top divisions fight once a day for 15 days, and the lower divisions fight seven times, the association says. Only the top two divisions wear the elaborate topknot called <em>oichomage</em>. A wrestler can move up or down, with one exception: the association says that a yokozuna can never be demoted, but is expected to retire after persistently poor results, and that promotion to yokozuna requires winning two consecutive tournaments or equivalent results, together with a judgment of character.</p>

    <h2 id="calendar">The Six Tournaments<span class="h2-jp">年6回の本場所</span></h2>
    <p>Three tournaments are in Tokyo, at the Ryogoku Kokugikan. The dates below for 2027 are from {ext(JOD,'The Japan Ode','sumo_japanode_dates')} and {ext(WAT,'WaTabi','sumo_watabi_dates')}, which agree with each other. Please check the association's own site before you book flights.</p>
    <ul>
      <li><strong>January:</strong> Tokyo, Ryogoku Kokugikan, 10-24 January 2027 (general sale 5 December 2026)</li>
      <li><strong>March:</strong> Osaka, EDION Arena Osaka, 14-28 March 2027 (general sale 6 February)</li>
      <li><strong>May:</strong> Tokyo, Ryogoku Kokugikan, 9-23 May 2027 (general sale 10 April)</li>
      <li><strong>July:</strong> Nagoya, IG Arena, 11-25 July 2027 (general sale 15 May)</li>
      <li><strong>September:</strong> Tokyo, Ryogoku Kokugikan, 12-26 September 2027 (general sale 7 August)</li>
      <li><strong>November:</strong> Fukuoka, Fukuoka Kokusai Center, 14-28 November 2027 (general sale 18 September)</li>
    </ul>
    <p>The November 2026 Fukuoka tournament runs 8-22 November, so it is on as I write this. Venue names for Nagoya have changed over the years, and older guides use the old names.</p>

    <h2 id="tickets">Tickets<span class="h2-jp">チケット</span></h2>
    <p>This is the hard part, especially for Tokyo. For overseas visitors, WaTabi says the official English service is {ext(TIX,'TICKET OOSUMO ENGLISH','sumo_ticket_official')}. Its description of the January 2027 sale is a "ladder": fan-club pre-lotteries in mid- and late November, a ticket-site pre-lottery in late November, then the general sale on 5 December 2026 at 10:00. If you are traveling in a Tokyo tournament month, the date to remember is the general sale date, or an earlier lottery if you can use one.</p>
    <h3>Prices (Tokyo, from January 2027, as reported by WaTabi)</h3>
    <p>WaTabi reports a price rise for 2027 and says older official price PDFs still show the earlier prices, so please confirm on the official ticket site. I give the weekday-to-final-day range per person.</p>
    <ul>
      <li><strong>Chair D</strong> (back row, online only): &yen;3,000 for adults; children aged 4-15 are &yen;500 on weekdays and &yen;1,000 on weekends and holidays, which WaTabi calls the cheapest admission in the building.</li>
      <li><strong>Chair C / B:</strong> &yen;5,000-7,000 / &yen;6,000-8,000</li>
      <li><strong>Chair A / S:</strong> &yen;10,000-12,000 / &yen;11,000-13,000</li>
      <li><strong>Box seats (<em>masu</em>), sold by the box:</strong> from &yen;9,500 (C) up to &yen;22,500-25,000 (SS, new for 2027)</li>
      <li><strong>Ringside (<em>tamari</em>):</strong> &yen;25,000-30,000, age 16 and over</li>
    </ul>
    <p>Osaka and Fukuoka cost less according to the same article (for example, Fukuoka's Chair C is &yen;2,000 on weekdays), and for Osaka it recommends buying before you fly.</p>
    <h3>If it is sold out</h3>
    <p>WaTabi describes an official face-value resale service on the ticket site, with a 10% fee for the seller. It also reports that the association prohibits resale for profit without permission, names several outside platforms, and says it took 138 enforcement actions across the six tournaments of 2025. I found those figures in that one article, so I cite them as WaTabi's report, but the advice is easy to follow: if you are buying, use the official channels.</p>

    <h2 id="day">A Day at the Tournament<span class="h2-jp">一日の流れ</span></h2>
    <p>The sport starts in the morning and builds to an evening climax. WaTabi's approximate timetable for a Tokyo September tournament shows the shape of the day:</p>
    <ul>
      <li><strong>8:45</strong> doors open; the lowest divisions begin from about 9:20</li>
      <li><strong>About 14:15</strong> the juryo ring-entering ceremony, with juryo bouts from about 14:35</li>
      <li><strong>About 15:40</strong> the top-division ring-entering ceremony, then the yokozuna's ceremony at about 15:55</li>
      <li><strong>About 16:05</strong> top-division bouts begin, with the top ranks after 17:00</li>
      <li><strong>About 17:55</strong> the bow-twirling ceremony, and the finish at about 18:00</li>
    </ul>
    <p>The article's advice is to arrive around 2 p.m., which fits my own feeling that the first half of the day is for sumo fans and the second half is for everyone. Times vary by tournament and day, so check the day's schedule before you go.</p>
    <p>For food, GLTJP describes <em>chanko-nabe</em>, the wrestlers' stew, as a broth made from chicken bones flavored with soy sauce or miso, with ingredients such as meatballs and napa cabbage. It says recipes vary by stable, that many retired wrestlers run restaurants serving it, and that the Kokugikan has restaurants serving chanko-nabe supervised by stables. Our {link('/culture/popular-dishes/','guide to popular Japanese dishes','sumo_to_dishes')} covers other everyday favorites.</p>

    <h2 id="stable">Morning Practice at a Stable<span class="h2-jp">朝稽古の見学</span></h2>
    <p>If tickets fail, there is a second way to see sumo: morning practice (<em>asa-geiko</em>) at a stable, the <em>heya</em> where wrestlers live and train. Several tour companies run it. One guide describes meeting at Ryogoku Station and spending roughly 1.5 to 2 hours watching from the tatami, with a briefing on etiquette beforehand.</p>
    <p>Etiquette is strict. {ext(TAN,'One Tokyo tour company','sumo_tanaka_rules')} says there is no talking, eating or drinking during practice, and {ext(SEX,'another','sumo_sumoexp_rules')} says you may not leave until the practice has finished and asks guests to show respect to the stable master and the wrestlers, since a stable is not a tourist attraction. Timing matters too: {ext(FLIP,'a tour guide','sumo_flip_timing')} says viewing is off the table during Tokyo tournament periods and that the best time is the run-up to a Tokyo tournament.</p>
    <p>One more point. {ext(ALL,'An All About Japan writer','sumo_allabout_arashio')} says you can visit Arashio Stable without a tour, free and with no reservation, if you check its calendar. That article is a few years old, and rules for visitors change, so please check the stable's current policy before relying on it.</p>
    <div class="key-callout" style="background:#fff8e6;border-left:4px solid var(--kin);padding:16px 20px;margin:28px 0;border-radius:2px;">
      <p style="margin:0;">&#127754; <strong>Plan your trip:</strong> Browse sumo experiences in Japan, or find a stay in Tokyo. <a href="{VI}" target="_blank" rel="noopener sponsored" onclick="trackEvent('click','affiliate','viator_sumo_local')">Browse sumo experiences on Viator</a> &middot; <a href="{EX}" target="_blank" rel="noopener sponsored" onclick="trackEvent('click','affiliate','expedia_sumo_local')">Find hotels in Tokyo</a></p>
    </div>

    <h2 id="shrines">Sumo Shrines to Visit<span class="h2-jp">相撲ゆかりの神社</span></h2>
    <p>This is where sumo and a shrine guide meet.</p>
    <h3>Tomioka Hachimangu, Fukagawa, Tokyo</h3>
    <p>{ext(TOM,'GLTJP','sumo_gltjp_tomioka')} calls it the largest Hachiman shrine of the Edo period and the birthplace of <em>kanjin-zumo</em>, the origin of today's sumo, with many sumo-related stone monuments, including one for yokozuna, one for ozeki and a stone with wrestlers' hand and foot prints. {ext(PHJ,'PhotoGuide Japan','sumo_photojpn_tomioka')} says the centerpiece is a 3.5 m, 20-ton monument made in 1900 by the 12th yokozuna, Jinmaku Kyugoro, after collecting donations. After the original stone filled up, two new slabs were added alongside it in 1983. {ext(SFM,'Sumo Fan Magazine','sumo_sfm_tomioka')} says a new yokozuna has his name inscribed on the monument, so the shrine and the champions stay linked. The shrine's big Fukagawa Hachiman Festival is held in mid-August.</p>
    <h3>Sumo Shrine, Sakurai, Nara</h3>
    <p>{ext(JEX,'Japan Experience','sumo_japanexp_sakurai')} describes the Sumo Shrine (<em>Sumo-jinja</em>), near Anashinimasu Hyozu Shrine in Sakurai, as an ancient shrine claimed to be the birthplace of sumo, where the bout between Nomi no Sukune and Taima no Kehaya is said to have taken place. The grounds have cherry trees and hand prints left by wrestlers who made the journey. It is a claim, not a proven site, so I recommend going for the atmosphere.</p>
    <p>I have only given you the shrines I could confirm in more than one source. For shrine manners at any of them, see our {link('/culture/shrine-etiquette/','shrine etiquette guide','sumo_to_etiquette2')}.</p>

    <h2 id="faq">Frequently Asked Questions<span class="h2-jp">よくあるご質問</span></h2>

    <div class="faq-stack">

{faq_html}    </div>

    <h2 id="final">Final Thoughts<span class="h2-jp">むすびに</span></h2>
    <p>If you only remember one thing, remember the salt. A handful of white crystals thrown onto clay tells you that this is a sport that still thinks of its ring as a place to be purified before it is used. Everything else, from the stamping to the shrine roof, follows from that.</p>
    <p>If you enjoy that side of Japan, look next at the warriors in our {link('/culture/samurai/','samurai guide','sumo_to_samurai')} and the Edo prints in our {link('/culture/ukiyo-e/','ukiyo-e guide','sumo_to_ukiyoe2')}.</p>

    <div class="closing-block">
      <span class="torii">&#127754;</span>
      <p>A handful of salt, a stamp of the foot, and a ring that is also a shrine.</p>
    </div>

    <section class="related-section">
      <h2>Related Guides</h2>
      <span class="h2-jp">関連ガイド</span>
      <div class="related-grid">
        <a class="related-card" href="/culture/what-is-shinto/" onclick="trackEvent('click','internal','related_sumo_to_shinto')">
          <div class="related-card-label">SACRED JAPAN ／ GUIDE</div>
          <div class="related-card-title">&#9961;&#65039; What Is Shinto? →</div>
          <div class="related-card-desc">The kami, purification and the shrine forms that sumo still borrows.</div>
        </a>
        <a class="related-card" href="/culture/samurai/" onclick="trackEvent('click','internal','related_sumo_to_samurai')">
          <div class="related-card-label">SACRED JAPAN ／ GUIDE</div>
          <div class="related-card-title">&#9876;&#65039; The Samurai Guide →</div>
          <div class="related-card-desc">Armor, swords and the warrior culture of Japan.</div>
        </a>
        <a class="related-card" href="/culture/ukiyo-e/" onclick="trackEvent('click','internal','related_sumo_to_ukiyoe')">
          <div class="related-card-label">SACRED JAPAN ／ GUIDE</div>
          <div class="related-card-title">&#127754; Ukiyo-e Guide →</div>
          <div class="related-card-desc">Edo woodblock prints, where wrestlers were popular subjects.</div>
        </a>
        <a class="related-card" href="/culture/shrine-etiquette/" onclick="trackEvent('click','internal','related_sumo_to_etiquette')">
          <div class="related-card-label">SACRED JAPAN ／ GUIDE</div>
          <div class="related-card-title">&#128591; Shrine Etiquette →</div>
          <div class="related-card-desc">How to behave at a shrine, including the sumo shrines above.</div>
        </a>
      </div>
    </section>

    <p style="font-size:14px;color:var(--enshu);line-height:1.7;margin-top:32px;"><strong>Sources:</strong> {ext(JSA,'Japan Sumo Association introduction','sumo_src_jsa')} (ring, rituals, ranks, rules); {ext(WAT,'WaTabi','sumo_src_watabi')} (tickets, prices, daily schedule, resale; single-source figures are flagged); {ext(JOD,'The Japan Ode','sumo_src_japanode')} (2027 dates); {ext(GLT,'GLTJP','sumo_src_gltjp')} (shiko, chanko-nabe); {ext(WSH,'Wikipedia: Shinto origins of sumo','sumo_src_wsh')}, {ext(WDO,'Dohyo','sumo_src_wdo')} and {ext(WNO,'Nomi no Sukune','sumo_src_wno')}; {ext(TOM,'GLTJP: Tomioka Hachimangu','sumo_src_tomioka')}, {ext(PHJ,'PhotoGuide Japan','sumo_src_photojpn')} and {ext(SFM,'Sumo Fan Magazine','sumo_src_sfm')} (Tomioka Hachimangu); {ext(JEX,'Japan Experience','sumo_src_jex')} (Sumo Shrine); {ext(TAN,'Tanaka Tokyo Tours','sumo_src_tanaka')}, {ext(SEX,'Sumo Experience','sumo_src_sumoexp')}, {ext(FLIP,'Flip Japan Guide','sumo_src_flip')} and {ext(ALL,'All About Japan','sumo_src_allabout')} (stable visits).</p>

  </article>

</main>"""

t=open(f'{R}/_tools/culture/tea.py',encoding='utf-8').read()
tail=t[t.index("s=open(f'{R}/culture/omamori-guide"):]
tail=tail.replace('<div class="hero-bg-kanji">茶道</div>','<div class="hero-bg-kanji">相撲</div>')
tail=tail.replace('<h1>The Japanese <em>Tea Ceremony</em> Guide</h1>','<h1><em>Sumo</em>: The Sacred Sport Guide</h1>')
tail=tail.replace('<div class="hero-jp">茶道ガイド</div>','<div class="hero-jp">相撲ガイド</div>')
tail=tail.replace('What Happens, What to Do as a Guest, and Where to Try It','Shinto Rituals, the Six Tournaments, Tickets and Morning Practice')
tail=tail.replace('Tea Ceremony Guide','Sumo Guide')
tail=tail.replace('guide_tea','guide_sumo').replace('viator_guide_tea_sticky','viator_guide_sumo_sticky').replace('japanese+tea+ceremony','sumo')
tail=re.sub(r'(<meta name="keywords" content=")[^"]*(")',r'\1sumo, sumo tickets, Grand Sumo tournament, Ryogoku Kokugikan, sumo rituals, dohyo, yokozuna, sumo morning practice, Tomioka Hachimangu\2',tail)
tail=tail.replace('"datePublished":"2026-11-08","dateModified":"2026-11-08"','"datePublished":"2026-11-15","dateModified":"2026-11-15"')
exec(tail)
