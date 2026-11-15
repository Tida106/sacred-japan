import re, os, json
R='/home/claude/sacred-japan'
S='noh'
OUT=f'{R}/culture/{S}'
os.makedirs(OUT,exist_ok=True)

def link(href,txt,lab): return f'<a href="{href}" class="inline-link" onclick="trackEvent(\'click\',\'internal\',\'{lab}\')">{txt}</a>'
def ext(href,txt,lab): return f'<a href="{href}" target="_blank" rel="noopener" onclick="trackEvent(\'click\',\'external\',\'{lab}\')">{txt}</a>'
VI='https://www.viator.com/search/noh?pid=P00298374&amp;mcid=42383&amp;medium=link&amp;campaign=sacred-japan'
EX='https://expedia.com/affiliate?siteid=1&amp;landingPage=https%3A%2F%2Fwww.expedia.co.jp%2FHotel-Search%3Fdestination%3DTokyo&amp;camref=1101l5JmFa&amp;creativeref=1011l87782&amp;adref=PZf6lQ77e8'
WJ='https://www.az.emb-japan.go.jp/files/000180853.pdf'
JG='https://japan-guide.com/e/e2091.html'
JAPN='https://japn-com.pages.dev/noh-theater-guide/'
JT='https://en.japantravel.com/tokyo/watching-noh-in-tokyo/71704'
JT2='https://en.japantravel.com/tokyo/introducing-noh-kyogen/68903'
TO='https://timeout.com/tokyo/theatre/noh-performance-at-the-national-noh-theatre'
KAN='https://www.kanpai-japan.com/japanese-arts-and-history/noh-theater'
JOBJ='https://japanobjects.com/features/noh'
MAG='https://magcul.net/topics/311475?lang=en'
WIL='https://bushisgo.rezio.shop/product/fe445ebc-4bbe-47a5-981b-ae5e06bde54f?lang=en-US'
FUN='https://www.fun-japan.jp/en/articles/14262'

faqs=[
("Is noh boring?","It is slow on purpose, and I would not pretend otherwise. Japan Guide describes it as built on song and dance with slow movement, poetic language and a monotone delivery. The way in is to treat it as a ritual you watch, not a plot you follow. JAPN suggests that first-timers pick a program with a demon or warrior play, since those have more visible action than the subtler woman plays."),
("Do I need Japanese?","Not at the National Noh Theatre. Japan Travel and Time Out both say it has English subtitles on small screens at the seats, though Japan Travel also says that at some performances an English booklet is what is offered. Kyogen is usually performed without subtitles, according to a report about one other theatre, so check the program."),
("How long is a performance?","Less than you fear. Japan Guide says a typical program today lasts a couple of hours, with two or three noh plays and short kyogen pieces in between, and JAPN says individual plays run 30 to 90 minutes. Web Japan says a traditional program had five noh plays, so a full day is the old format."),
("How much do tickets cost?","Japan Travel and JAPN give about &yen;3,000 to &yen;6,000, Time Out quoted &yen;3,400 to &yen;5,200 for one program, and Japan Guide gives a wider &yen;3,000 to &yen;12,500. Japan Travel adds that students under 26 may get half price. Please check the theatre's own page for your date."),
("Why are the actors all men?","Japan Guide states that all performers are male, and the shogunate made noh its official ceremonial art in the Tokugawa period. Women performers have appeared in recent times, but the sources I read do not cover that, so I leave it at the tradition."),
("What is the difference between noh and kabuki?","Noh is the older, quieter, mask-based art of suggestion; kabuki is the flamboyant, popular theater of the Edo period. The Web Japan introduction to kabuki says its stage gradually evolved out of the noh stage and that some plays are adapted from noh. Our kabuki guide explains the other side."),
("Can I see noh at a shrine?","Sometimes. Japan Guide lists Itsukushima Shrine, Chusonji Temple, Fushimi Inari Shrine and Yasukuni Shrine as places with historic outdoor stages and occasional performances, and warns that tickets can be hard to get. Web Japan adds that outdoor night performances by firelight, <em>takiginoh</em>, have grown popular in recent years."),
]
faq_html=''.join(f"""      <details class="faq-item">
        <summary>{q}</summary>
        <div class="faq-answer">{a}</div>
      </details>

""" for q,a in faqs)
faq_ld=json.dumps({"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":re.sub('<[^>]+>','',a)}} for q,a in faqs]},ensure_ascii=False,indent=2)

TITLE="Noh Guide: Masks, Ghost Stories, the Stage and How to Watch Your First Performance"
DESC="A licensed guide's English introduction to noh theater: how Kan'ami and Zeami shaped it, why a ghost is so often the main character, how to read the masks and the five kinds of play, and where to watch with English subtitles."
URL=f"https://sacred-japan.net/culture/{S}/"
OG="https://sacred-japan.net/images/og/og-culture-noh.jpg"


CAPST='font-size:13px;color:var(--enshu);margin-top:10px;text-align:center;line-height:1.6;'
LA='style="color:var(--enshu);"'
def lk(t,u): return f'<a href="{u}" target="_blank" rel="noopener" {LA}>{t}</a>'
def csearch(q): return 'https://commons.wikimedia.org/w/index.php?search='+q+'&title=Special:MediaSearch&type=image'
def cm(q): return lk("Wikimedia Commons",csearch(q))
def pfig(src,alt,desc,cred,mw=760):
    return (f'<figure style="margin:36px auto;max-width:{mw}px;">\n      <picture><source srcset="/culture/noh/images/{src}.webp" type="image/webp"><img src="/culture/noh/images/{src}.jpg" alt="{alt}" loading="lazy" style="width:100%;height:auto;border-radius:4px;display:block;"></picture>\n      <figcaption style="{CAPST}">{desc}<br>{cred}</figcaption>\n    </figure>')
L_CC0=lk("CC0","https://creativecommons.org/publicdomain/zero/1.0/")
L_BYSA3=lk("CC BY-SA 3.0","https://creativecommons.org/licenses/by-sa/3.0/")
L_BY3=lk("CC BY 3.0","https://creativecommons.org/licenses/by/3.0/")
f_nat=pfig('noh-national','Inside the National Noh Theatre in Tokyo: a square wooden stage under its own Shinto-style gabled roof, with a large green pine painted on the back wall, a covered bridge-like passage to the left, small pine trees beside it and rows of empty audience seats in front','The stage of the National Noh Theatre in Tokyo, seen from the audience. It shows the elements described above in one frame: the roofed, square cypress stage, the painted pine on the back wall, the angled passage on the left that leads to it, and the small pines set beside that passage. The roof stands inside the building, which is how most noh stages are housed today.',f'Photo: Bokken (2005 original; the higher-quality version uploaded by Artanisen, 2019), public domain, via {cm("Noh+stage+front+Noh+National+Theatre+Tokyo")} (small original, shown at its native size)',760)
f_hashi=pfig('noh-hashigakari','Close view of a wooden noh stage: in the foreground the polished floor and the step at its edge, at left a roofed passage with a railing and a straw rope hung with white paper streamers along its top, and at right the back wall with part of a painted pine in faded green and orange-brown','The <em>hashigakari</em>, the bridge from the dressing room to the stage, at a noh stage that Commons describes as the one at Himure Hachimangu in Omi-Hachiman. The straw rope with white paper streamers is the kind of rope used at shrines, and it is a reminder that these stages belong to shrines. The step at the lower edge is the stage front, and part of the painted pine shows at the right.',f'Photo: fitm, {lk("CC BY-SA 3.0","https://creativecommons.org/licenses/by-sa/3.0/")} (also offered under GFDL), 9 August 2008, via {cm("Hashigakari+Noh+butai+Himure+Hachimangu")} (resized)',760)
f_itsu=pfig('itsukushima-noh','Wide panorama at low tide at Itsukushima Shrine: a noh stage with a dark thatched-looking roof at left, standing over wet sand with the sea and part of the great torii behind it, red covered corridors running to the right, a five-story pagoda in the distance and a hanging lantern in the foreground','The noh stage at Itsukushima Shrine on Miyajima, photographed at low tide on 30 April 2013 (Commons). With the water out, you can see how the stage and the red corridors stand on pillars over the sand, and at high tide the same space is sea. The sea behind the stage is the backdrop here instead of a wall. In the distance is a five-story pagoda. The Commons title is only &ldquo;Noh stage&rdquo; and the tags give Hatsukaichi, where Miyajima lies.',f'Photo: z tanuki, {L_BY3}, via {cm("Noh+stage+Itsukushima+panoramio+z+tanuki")} (resized)',760)
f_chext=pfig('chuson-exterior','Wide view of an old wooden noh stage with a deep thatched roof in a cedar forest, a roofed passage joined to its left, a white sheet and an orange traffic cone at the far left, and a few visitors sitting on the stage edge under the roof',f'The noh stage at Hakusan Shrine in the grounds of Chusonji, {link('/guides/hiraizumi/','Hiraizumi','noh_photo_hiraizumi')}, seen from the open ground in front, with the stage open on three sides under a thick thatched roof. The white sheet at the left and the cone suggest maintenance work on that day, so the scene may look different when you go.',f'Photo: Daderot, {L_CC0}, 10 August 2017, via {cm("Noh+stage+Hakusan-jinja+Chusonji+Hiraizumi+Iwate")} (resized)',760)
f_chint=pfig('chuson-interior','Inside the same stage, looking at its back wall: weathered gray wooden boards with a faded pine painted in blue-green and orange-brown, carved cloud-shaped brackets under the beams, and a railing and the long passage at left','The back wall of the same stage, with a painted pine that has weathered to faded blue-green and orange-brown. Compare it with the bright green pine of the Tokyo stage: the subject is the same, but time has changed the paint. The carved beam brackets show that even a plain-looking stage is carefully made.',f'Photo: Daderot, {L_CC0}, 10 August 2017, via {cm("Noh+stage+Hakusan-jinja+Chusonji+Hiraizumi+Iwate")} (resized)',760)
f_chfr=pfig('chuson-front','Front view of the old noh stage at Chusonji under a steep thatched roof with a small roof ornament on the ridge, tall cedar trees behind, a low fence in front, and a roofed passage and a second thatched building at left','The same stage from the front, in June 2011 (Commons). The steep thatched roof and the cedars behind it give a very different feeling from the cypress stage in Tokyo. The notice boards at the front are in Japanese, and I have not tried to read them.',f'Photo: Tak1701d, {L_BYSA3} (also offered under GFDL), 21 June 2011, via {cm("Noh+stage+Hakusan+shrine+Chusonji+Tak1701d")} (resized)',760)
f_sado=pfig('sado-takigi','Night performance on an outdoor noh stage: a masked performer in a tall black hat, a long black wig and a gold-and-blue patterned robe stands at left, three seated musicians with drums and a flute sit at the back before a green pine painted on a gold-brown wall, a chorus kneels at right, paper lanterns at both sides read takigi noh, and fire baskets burn in the foreground above a dark audience','A noh performance on a stage in Sado, the island where Japan Guide says Zeami was exiled; the title says only &ldquo;Sado&rdquo; and I cannot say which stage it is. I read the lanterns as <em>takigi</em> noh (&ldquo;firewood noh&rdquo;), noh played by firelight, and baskets of fire burn on both sides. You can see the roles described above: the masked lead, three musicians (a flute and two hand drums, as I read them) at the back, and a kneeling chorus at the right.',f'Photo: Yoshiyuki Ito, {L_BYSA3}, Commons date 7 October 2017, via {cm("Noh+Performance+Sado+Yoshiyuki+Ito")} (resized)',760)

main=f"""<main>

  <!-- TABLE OF CONTENTS -->
  <aside class="toc" aria-label="Table of contents">
    <div class="toc-label">TABLE OF CONTENTS ／ 目次</div>
    <div class="toc-title">In This Guide</div>
    <ol>
      <li><a href="#opening">Opening: A Note from the Guide</a></li>
      <li><a href="#history">Kan'ami, Zeami and the Shogun</a></li>
      <li><a href="#stage">A Stage Built Like a Shrine</a></li>
      <li><a href="#cast">Who Is Who on Stage</a></li>
      <li><a href="#masks">The Masks</a></li>
      <li><a href="#plays">Five Kinds of Play</a></li>
      <li><a href="#kyogen">Kyogen: The Comedy in Between</a></li>
      <li><a href="#where">Where to Watch</a></li>
      <li><a href="#tips">Tickets and First-Timer Tips</a></li>
      <li><a href="#faq">Frequently Asked Questions</a></li>
      <li><a href="#final">Final Thoughts</a></li>
    </ol>
  </aside>

  <article>

    <section id="opening">
      <p class="opening">A traveling monk arrives at a quiet place and meets a stranger who tells him a local story. As the evening goes on, the stranger turns out to be the ghost of someone who has been dead for centuries, and after an interval the ghost comes back in his true form to dance the story out. That is the plot of a surprising number of noh plays, and it explains why noh feels less like a drama and more like a ceremony for the dead.</p>
      <p>As a licensed guide, I recommend noh to visitors who like Japan's quieter side. This guide explains where it came from, how the stage and the masks work, the five kinds of play, and how to watch a first performance with English subtitles without falling asleep.</p>
    </section>

    <h2 id="history">Kan'ami, Zeami and the Shogun<span class="h2-jp">観阿弥と世阿弥</span></h2>
    <p>The {ext(WJ,'Web Japan introduction to noh','noh_webjapan_origin')} says noh emerged as a distinct theatrical form in the 14th century and describes it as the oldest extant professional theater in the world. It grew out of a popular genre called <em>sarugaku</em>, which Kan'ami (1333-1384) and his son Zeami (1363-1443) transformed into noh. Kan'ami added music and dance from the popular entertainment <em>kuse-mai</em> and won the patronage of the shogun Ashikaga Yoshimitsu (1358-1408).</p>
    <p>After Kan'ami died, Zeami led the Kanze troupe, refined the aesthetics and wrote essays that set the standards of performance for later centuries. Two of his ideas are worth knowing. <em>Yugen</em> is a Zen-influenced ideal that stresses the suggestion of mystery and depth, and <em>monomane</em> means the imitation of things. If you remember only one, remember <em>yugen</em>: noh tries to hint, not to show.</p>
    <p>Later history is a story of institutions. Japan Guide says that Zeami fell out of favor and was banished to Sado Island, which is a single-source detail I give only as reported. The Web Japan introduction says that in the 17th century noh became an official property of the Tokugawa shogunate and grew slower and more solemn; Japan Guide adds that the shogunate made it its official ceremonial art and issued regulations, and that five main troupes perform to this day. After the Meiji Restoration of 1868, performers such as Umewaka Minoru I (1828-1909) and noble patronage kept it alive, and since the end of World War II it has depended on public support. If you have read our {link('/culture/samurai/','samurai guide','noh_to_samurai')}, the warrior-class patronage will make sense.</p>

    <h2 id="stage">A Stage Built Like a Shrine<span class="h2-jp">能舞台</span></h2>
    <p>The noh stage looks almost empty, and that is the point. Web Japan says the main stage measures 6 by 6 meters, is built of polished <em>hinoki</em> cypress and has a Shinto-style roof. Japan Guide adds that the roof is supported by four corner pillars and that the stage is open on three sides. A painted pine tree on the back wall is the only backdrop for every play, and an angled bridge, the <em>hashigakari</em>, serves as the entrance passage. The stage was originally outdoors and is now usually housed in a larger building.</p>
    <p>I would compare it with the ring in our {link('/culture/sumo/','sumo guide','noh_to_sumo')}: both are spaces with a shrine roof, and both are treated as set apart. Keep your eyes on the bridge. Many entrances happen there, slowly, and the audience watches a ghost walk toward them for a full minute.</p>
    {f_nat}

    {f_hashi}

    <div class="key-callout" style="background:#fff8e6;border-left:4px solid var(--kin);padding:16px 20px;margin:28px 0;border-radius:2px;">
      <p style="margin:0;">&#127754; <strong>Plan your trip:</strong> Browse noh and other traditional performance experiences, or find a stay in Tokyo. <a href="{VI}" target="_blank" rel="noopener sponsored" onclick="trackEvent('click','affiliate','viator_noh_local')">Browse noh experiences on Viator</a> &middot; <a href="{EX}" target="_blank" rel="noopener sponsored" onclick="trackEvent('click','affiliate','expedia_noh_local')">Find hotels in Tokyo</a></p>
    </div>

    <h2 id="cast">Who Is Who on Stage<span class="h2-jp">役柄</span></h2>
    <p>Roles are fixed, and learning them makes the stage readable. These come from the Web Japan introduction and Japan Guide, which agree except where I flag it.</p>
    <ul>
      <li><strong>Shite:</strong> the leading character, usually masked. Depending on the play, Japan Guide says the shite may be a holy old man, a deity, a demon, a spirit or a living man.</li>
      <li><strong>Waki:</strong> the supporting role, unmasked, and always a living person such as a priest, monk or samurai. The waki is the one who meets the ghost.</li>
      <li><strong>Tsure, wakitsure, kokata:</strong> accompanying characters, and the child role.</li>
      <li><strong>Jiutai:</strong> the chorus, which voices the lead's words and thoughts. The two sources disagree on which side of the stage it sits on (stage right in one, left in the other), so I give no side.</li>
      <li><strong>Hayashikata:</strong> the musicians, with a flute, a small hand drum (<em>kotsuzumi</em>), a large hand drum (<em>otsuzumi</em>) and, when needed, a floor drum (<em>taiko</em>).</li>
      <li><strong>Koken:</strong> stage attendants in black who help the performers; Japan Guide says they are not part of the play.</li>
    </ul>
    <p>The other great tool is the folding fan. Web Japan calls it a key hand prop that stands in for objects or actions, and Japan Guide says it can stand for a dagger or a lantern.</p>

    <h2 id="masks">The Masks<span class="h2-jp">能面</span></h2>
    <p>Masks are worn by the shite to signal the character type, according to Japan Guide, and are carved from Japanese cypress. The types include young woman, old man and demon, and the Web Japan introduction says each has a level of dignity, <em>kurai</em>, that shapes the performance. Kanpai Japan says the woman's mask follows the idealized beauty of the Heian period, and that demon masks have golden or red hues, big eyes and a grin showing the teeth.</p>
    <p>The most famous is the <em>hannya</em>, a female demon mask. In <em>Aoi no Ue</em> (Lady Aoi), a play Zeami revised from <em>The Tale of Genji</em>, Web Japan says the shite switches from a woman's mask, <em>deigan</em>, to the hannya, which is the turn from grief to jealousy in a single costume change. Japan Guide says a skilled actor can change the expression of a fixed mask by tilting the head. The next time someone calls a noh mask blank, watch the tilt of the head.</p>

    <h2 id="plays">Five Kinds of Play<span class="h2-jp">五番立て</span></h2>
    <p>Web Japan says about 240 plays survive today, in five groups. Guides name some of the groups differently, so I give the Web Japan list first:</p>
    <ol>
      <li><strong>God plays (waki noh):</strong> a deity blesses the land. Kanpai Japan says the god appears as an old man and the piece mixes song, dance and Shinto ritual.</li>
      <li><strong>Warrior plays (shuramono):</strong> usually a monk meets the soul of a past warrior who is stuck in the cycle of rebirth.</li>
      <li><strong>Wig plays (kazura-mono):</strong> woman plays, centered on female characters, often caught between love and sorrow.</li>
      <li><strong>Miscellaneous plays (zatsu noh):</strong> other guides call this group "madness" plays, with characters driven to madness by tragedy.</li>
      <li><strong>Demon plays (kiri-noh):</strong> short, fast pieces with supernatural beings.</li>
    </ol>
    <p>Web Japan says plays follow the <em>jo-ha-kyu</em> pattern: introduction, exposition and a rapid finale. A traditional program had five noh plays and three or four kyogen; Japan Guide says today's programs usually have two or three noh plays. If you are choosing, JAPN's advice is to pick a demon or warrior play for more visible action. The plot of a woman play can be a single memory, and I find those the most moving, but I would not start there.</p>

    <h2 id="kyogen">Kyogen: The Comedy in Between<span class="h2-jp">狂言</span></h2>
    <p>Noh is not performed alone. Web Japan says independent kyogen are comic plays performed between noh plays, with roots in entertainment brought from China in the 8th century or earlier. Japan Guide says they last about 15 to 20 minutes, use two or three actors and rely on satire, wit, rhythmic language and exaggerated action, with plots from everyday life. Web Japan also says that within a noh play a kyogen actor often bridges the two acts, retelling the story in colloquial language while the lead changes costume. That is the interval I mentioned in the opening.</p>
    <p>Web Japan names about 260 independent kyogen plays, of which about 50 use masks, usually for non-human characters. The kyogen in a noh program is the part everybody understands, and it is the part you are allowed to laugh at.</p>

    <h2 id="where">Where to Watch<span class="h2-jp">能楽堂</span></h2>
    <ul>
      <li><strong>National Noh Theatre, Sendagaya, Tokyo:</strong> opened in 1983 according to Japan Travel, with seating for 627 and English subtitles on the seats. Japan Travel also lists it as 5 minutes from the Sendagaya Ekimae bus stop, and an operator listing puts it near Kita-Sando and Sendagaya stations; check a map for your route.</li>
      <li><strong>Other Tokyo venues:</strong> Japan Guide lists the Kanze Noh Theater in Ginza and the Cerulean Tower Noh Theatre in Shibuya. Matcha adds the Hosho Noh Theater in Suidobashi, with the caution that outside the National Noh Theatre it is hard to find programs and explanations in English.</li>
      <li><strong>Elsewhere:</strong> Otsuki Noh Theatre in Osaka and the Nagoya Noh Theatre next to Nagoya Castle (Japan Guide).</li>
      <li><strong>Shrines and temples:</strong> Japan Guide lists historic outdoor stages at {link('/guides/itsukushima-shrine/','Itsukushima Shrine','noh_to_itsukushima')} on Miyajima, where the stage stands on pillars in the sea, Chusonji Temple in {link('/guides/hiraizumi/','Hiraizumi','noh_to_hiraizumi')} and {link('/guides/fushimi-inari-taisha/','Fushimi Inari Shrine','noh_to_inari')}, as well as Yasukuni Shrine in Tokyo. Performances there are occasional and tickets can be hard to get.</li>
    </ul>

    <p>A few of these stages in pictures. Itsukushima first, then the old stage at Chusonji, then a firelit performance on Sado.</p>

    {f_itsu}

    {f_chext}

    {f_chint}

    {f_chfr}

    {f_sado}

    <h2 id="tips">Tickets and First-Timer Tips<span class="h2-jp">鑑賞のコツ</span></h2>
    <p>Prices vary by source and program. Japan Travel and JAPN say &yen;3,000 to &yen;6,000, Time Out quoted &yen;3,400 to &yen;5,200 for one program, and Japan Guide gives &yen;3,000 to &yen;12,500. Japan Travel says some performances are split into two parts with tickets sold separately, and that buying both can qualify for a discount. Japan Guide says tickets are sold at the venue counter or online and that online purchases often require Japanese; some venues sell discounted single-act tickets, which suits a first visit.</p>
    <p>For a ready-made option, one listing on a Japan tour-booking site describes a 2025 Noh Experience Tour at the National Noh Theatre with a 40-minute lecture, a mask experience and a two-hour performance with English subtitles, for &yen;15,000. I only saw that listing, so treat the details as unconfirmed and check the operator.</p>
    <p>My own advice, as a guide, is to read the synopsis before the lights go down, since the subtitles give you the words and the program gives you the story, and to let the slowness happen. If a scene feels empty, look at the shite's hands and at the fan.</p>

    <h2 id="faq">Frequently Asked Questions<span class="h2-jp">よくあるご質問</span></h2>

    <div class="faq-stack">

{faq_html}    </div>

    <h2 id="final">Final Thoughts<span class="h2-jp">むすびに</span></h2>
    <p>If you remember one thing, remember the ghost. In noh the dead return to tell their stories, the living listen, and a pine tree painted on a wall is all the scenery you need. Give it one program and let it be slow.</p>
    <p>If you enjoy this side of Japan, the livelier theater of the same country is in our {link('/culture/kabuki/','kabuki guide','noh_to_kabuki')}, and the tea room next door to it in our {link('/culture/tea-ceremony/','tea ceremony guide','noh_to_tea')}.</p>

    <div class="closing-block">
      <span class="torii">&#127754;</span>
      <p>A painted pine, a ghost on a bridge and a mask that learns to feel.</p>
    </div>

    <section class="related-section">
      <h2>Related Guides</h2>
      <span class="h2-jp">関連ガイド</span>
      <div class="related-grid">
        <a class="related-card" href="/culture/kabuki/" onclick="trackEvent('click','internal','related_noh_to_kabuki')">
          <div class="related-card-label">SACRED JAPAN ／ GUIDE</div>
          <div class="related-card-title">&#127917; Kabuki Guide →</div>
          <div class="related-card-desc">The flamboyant theater that grew up beside noh.</div>
        </a>
        <a class="related-card" href="/culture/samurai/" onclick="trackEvent('click','internal','related_noh_to_samurai')">
          <div class="related-card-label">SACRED JAPAN ／ GUIDE</div>
          <div class="related-card-title">&#9876;&#65039; The Samurai Guide →</div>
          <div class="related-card-desc">The warrior class that kept noh alive.</div>
        </a>
        <a class="related-card" href="/culture/tea-ceremony/" onclick="trackEvent('click','internal','related_noh_to_tea')">
          <div class="related-card-label">SACRED JAPAN ／ GUIDE</div>
          <div class="related-card-title">&#127861; Tea Ceremony Guide →</div>
          <div class="related-card-desc">Another art of stillness and suggestion.</div>
        </a>
        <a class="related-card" href="/guides/itsukushima-shrine/" onclick="trackEvent('click','internal','related_noh_to_itsukushima')">
          <div class="related-card-label">SACRED JAPAN ／ GUIDE</div>
          <div class="related-card-title">&#9961;&#65039; Itsukushima Shrine →</div>
          <div class="related-card-desc">A noh stage standing on pillars in the sea.</div>
        </a>
      </div>
    </section>

    <p style="font-size:14px;color:var(--enshu);line-height:1.7;margin-top:32px;"><strong>Sources:</strong> {ext(WJ,'Web Japan: Noh and Kyogen','noh_src_webjapan')} (history, roles, stage, repertoire, kyogen); {ext(JG,'Japan Guide: Noh Theater','noh_src_japanguide')} (troupes, roles, program, venues, tickets); {ext(JAPN,'JAPN','noh_src_japn')}, {ext(JT,'Japan Travel: Watching Noh in Tokyo','noh_src_jt')}, {ext(JT2,'Japan Travel: National Noh Theatre','noh_src_jt2')} and {ext(TO,'Time Out Tokyo','noh_src_timeout')} (tickets, subtitles); {ext(KAN,'Kanpai Japan','noh_src_kanpai')} (masks, play types); {ext(MAG,'Magcul','noh_src_magcul')} (kyogen without subtitles at one theatre); {ext(WIL,'WILLER tour listing','noh_src_willer')} (single listing, unconfirmed).</p>

  </article>

</main>"""

t=open(f'{R}/_tools/culture/tea.py',encoding='utf-8').read()
tail=t[t.index("s=open(f'{R}/culture/omamori-guide"):]
tail=tail.replace('<div class="hero-bg-kanji">茶道</div>','<div class="hero-bg-kanji">能</div>')
tail=tail.replace('<h1>The Japanese <em>Tea Ceremony</em> Guide</h1>','<h1><em>Noh</em>: The Oldest Theater Guide</h1>')
tail=tail.replace('<div class="hero-jp">茶道ガイド</div>','<div class="hero-jp">能楽ガイド</div>')
tail=tail.replace('What Happens, What to Do as a Guest, and Where to Try It','Masks, Ghost Stories, the Stage and How to Watch Your First Performance')
tail=tail.replace('Tea Ceremony Guide','Noh Guide')
tail=tail.replace('guide_tea','guide_noh').replace('viator_guide_tea_sticky','viator_guide_noh_sticky').replace('japanese+tea+ceremony','noh')
tail=re.sub(r'(<meta name="keywords" content=")[^"]*(")',r'\1noh, noh theater, noh guide, noh masks, hannya, National Noh Theatre, kyogen, Zeami, Kan\'ami, watch noh in Tokyo\2',tail)
tail=tail.replace('"datePublished":"2026-11-08","dateModified":"2026-11-08"','"datePublished":"2026-11-15","dateModified":"2026-11-15"')
exec(tail)
