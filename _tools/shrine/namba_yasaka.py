import sys; sys.path.insert(0,'/home/claude/sacred-japan/_tools/shrine')
from shrine_common import *
HY='https://commons.wikimedia.org/wiki/User:Hyppolyte_de_Saint-Rambert'
P={
'lion-front':('b74cc376','Hyppolyte de Saint-Rambert','by4',HY),
'torii-view':('0b339111','Hyppolyte de Saint-Rambert','by4',HY),
'lion-closeup':('c7fe0060','Hyppolyte de Saint-Rambert','by4',HY),
'lion-angle':('d9aa1e1b','Hyppolyte de Saint-Rambert','by4',HY),
'lion-side':('/tmp/immanuelle.jpg','Immanuelle','by4','https://commons.wikimedia.org/wiki/User:Immanuelle'),
'haiden':('8557f811','KENPEI','bysa3','https://commons.wikimedia.org/wiki/User:KENPEI'),
'ema':('0524e38a','Ethan Doyle White','bysa4','https://commons.wikimedia.org/wiki/User:Doyle_of_London'),
}
faqs=[
("What is the lion head at Namba Yasaka Shrine?","It is the Shishiden, a hall and stage shaped like a giant lion's head, built in 1974 together with the rebuilt main hall (GLTJP). It is about 12 m high, 11 m wide and 10 m deep, and is said to swallow evil spirits and bring luck in competition."),
("Who is enshrined at Namba Yasaka Shrine?","GLTJP names Susanoo-no-Mikoto. Magical Trip adds his wife Kushinada-hime and their eight children, the Yahashira-miko (single source for the full list). Older sources describe the shrine as a Gozu Tenno shrine from the Shinto-Buddhist era."),
("How old is the shrine?","Tradition dates it to the reign of Emperor Nintoku (313-399), per GLTJP, and the founding records were lost to fire. It is documented as a well-known Gozu Tenno shrine by the late 11th century (tabi-mag, Magical Trip). The present buildings are postwar, rebuilt in 1974."),
("What are the opening hours and is entry free?","GLTJP (shrine-verified) lists daily 6:00 to 17:00, with the amulet and goshuin office open 9:00 to 16:50. Entry is free, cards are not accepted and there is no parking. Check the official site before you go."),
("How do I get there?","About 7 minutes on foot from JR Namba Station or 8 minutes from Nankai Namba Station (GLTJP). Magical Trip gives about 6 minutes from Namba Station on the Osaka Metro Midosuji and Yotsubashi lines."),
("When are the festivals?","The Tsunahiki Shinji, a tug-of-war with a rope shaped like the eight-headed serpent, is held on the third Sunday of January (shrine's own page). The summer festival with the boat procession is on July 13 and 14 (Magical Trip, Fun! JAPAN); the shrine's own page confirms the January date. Confirm dates with the shrine."),
]
def body(fig,a): return """<main>

"""+fig('lion-front','A giant grey-green lion head with copper-coloured eyes and fangs forms the front of a shrine hall, with visitors standing in front of it and an office building behind','The Shishiden seen from the grounds, February 2024',hero=True)+"""

  <aside class="toc" aria-label="Table of contents">
    <div class="toc-label">TABLE OF CONTENTS ／ 目次</div>
    <div class="toc-title">In This Guide</div>
    <ol>
      <li><a href="#opening">A Lion You Can Walk Into</a></li>
      <li><a href="#lion">The Shishiden</a></li>
      <li><a href="#history">History and Deities</a></li>
      <li><a href="#festivals">Two Festivals</a></li>
      <li><a href="#visit">Visiting Namba Yasaka</a></li>
      <li><a href="#faq">Frequently Asked Questions</a></li>
      <li><a href="#final">Before You Go</a></li>
    </ol>
  </aside>

  <article>

    <p class="opening" id="opening">As a licensed guide, I send people to Namba Yasaka Shrine when they want one stop in Osaka that nobody expects: a shrine hall built as an open-mouthed lion's head, a few minutes' walk from the neon of Namba.</p>
    <p>The lion is the draw, but the shrine behind it is old, and it keeps two festivals worth planning a trip around. This guide covers the hall, the gods, the festivals and the practical details.</p>

    <h2 id="lion">The Shishiden<span class="h2-jp">獅子殿</span></h2>
"""+fig('torii-view','A stone torii with a twisted rope across it frames the giant lion head at the back of the grounds, with a stone marker reading Namba Yasaka Shrine at the right and people with suitcases on the pavement','The lion head seen through the stone torii from the street')+"""
    <p>The first view is from the street. Through the stone torii, past a marker that reads 難波八阪神社 (as I read it), the lion looks out from the far end of the grounds. This matches GLTJP, which says it can be seen from outside the east torii. The photo is from February 2024, and plum blossom is out on the left.</p>
    <p>The Shishiden stands west of the main hall and is shaped like a lion's head. GLTJP, whose entry was confirmed by the shrine, gives its size as 12 m high, 11 m wide and 10 m deep, and says it can be seen from outside the east torii. It was built in 1974 with the rebuilt main hall, as a symbol to surprise Osaka people, drawing on the local lion dance meant to drive off evil.</p>
"""+fig('lion-closeup','Close-up of the lion head with wide copper-coloured eyes that have dark round centres, a flat nose with dark nostrils, large copper fangs and a hall with hanging lanterns inside the mouth','Close-up of the eyes, nose and fangs')+"""
    <p>Up close, the eyes are large copper-coloured domes with a dark round centre, and the fangs and a row of front teeth have the same metallic colour. The surface looks like speckled grey-green stone, though it is a built surface and not carved rock. Below the teeth you can see a ceiling of square panels and rows of hanging lanterns.</p>
"""+fig('lion-angle','The lion head seen from a three-quarter angle with pigeons on its brow, a straw rope and a green lantern in front of the open mouth, and visitors standing below','The lion from the side, with the sanctuary in its mouth')+"""
    <p>From the side you see how the whole building is the head: the mouth is the hall. In the opening there are straw ropes and a gold ornament on the altar (as I read the photo). The pigeons on the brow are a common sight here. A tall stone lantern stands at the front on the right.</p>
    <p>Inside the mouth are a sanctuary and a stage where dances are sometimes performed at festivals (Magical Trip, Fun! JAPAN). GLTJP says the ceiling has hand-carved phoenixes, each with a different pattern, and that the eyes light up during the summer festival and New Year. Magical Trip describes the structure as mostly steel-reinforced concrete with some wood, and the eyes and teeth as brass; another site says resin sprayed with copper powder, so I would not state the material as settled.</p>
"""+fig('lion-side','The lion head seen from the right side in bright sunlight, its open mouth forming a stage with copper-coloured teeth along the floor, and two visitors walking past','The open mouth seen from the side in summer')+"""
    <p>This summer photo, from August 2024, shows the opening from the side: the lower jaw forms a platform and the teeth run along its edge, so the mouth really is a stage. It also shows the scale, with visitors beside the head as small as they look at the base of a building.</p>
    <p>People pray here to ward off bad luck and for success in exams, business and competition (GLTJP, Walkerplus).</p>

    <h2 id="history">History and Deities<span class="h2-jp">由緒と御祭神</span></h2>
    <p>Tradition places the founding in the reign of Emperor Nintoku (313-399) (GLTJP). Walkerplus and Magical Trip tell it as a response to an epidemic, when the god Gozu Tenno appeared and was enshrined. The founding records were lost to fire, so this is legend rather than documented history.</p>
"""+fig('haiden','A wide shrine hall with a green copper roof curving upward, gold ornaments, lanterns hanging along the eaves, a thick straw rope, stone steps and two stone guardian lions, with visitors on the steps and a banner for Shichi-go-san','The main hall (haiden), November 2007')+"""
    <p>Behind the lion is the main hall. In this 2007 photo, taken before the more recent visits, it has a curved green roof with gold fittings, lanterns hung along the eaves and a banner that reads 七五三詣 (as I read it), for the children's festival in November. The building has been rebuilt since the war (GLTJP says the main hall was rebuilt in 1974), but I cannot tell from this photo whether it has changed since 2007.</p>
    <p>By the Enryaku era of 1069 to 1073 it was already known as a Gozu Tenno shrine, with a temple beside it, and local people called it Naniwa Shimo-no-miya (tabi-mag, Fun! JAPAN). Shinto and Buddhism were combined until the separation orders; the temple ended and the shrine became a village shrine in 1872 (Walkerplus). Air raids destroyed the buildings, and the main hall was rebuilt in 1974 (GLTJP).</p>
    <p>GLTJP names Susanoo-no-Mikoto. Magical Trip lists him with his wife Kushinada-hime and their eight children. Susanoo is the god who defeated the Yamata no Orochi serpent; our """+a('/culture/japanese-mythology/','Japanese mythology guide','mythology')+""" tells that story. Magical Trip also notes five smaller shrines in the grounds, the best known being Sasayama Shrine.</p>

    <h2 id="festivals">Two Festivals<span class="h2-jp">祭り</span></h2>
    <p><strong>Tsunahiki Shinji</strong>, the rope-pulling ritual, is held in the morning of the third Sunday of January, according to the shrine's own page (nambayasaka.jp). It is designated an intangible folk cultural property of Osaka City. The shrine says its origin is not clear, but that it appears in Edo-period printed books, so it is old; it is known as the &ldquo;Namba tug-of-war&rdquo; (難波の綱引), and used to be held on January 14.</p>
    <p>The story behind it is Susanoo's defeat of the eight-headed serpent at the Hi River in Izumo, and the rope is made up as a serpent with eight heads and eight tails (八頭八尾). The shrine's page gives these steps: the rope is begun (綱打始め), brought out (綱引出し), then pulled in the direction of that year's lucky direction (恵方), and finally offered before the shrine. It lists prayers for the shrine's divine virtue, for freedom from plague and disaster, for the harvest of sea, river and mountain, for steady livelihoods, for family safety and for business. The page says nothing on who may join or watch, so ask the shrine if you want to take part. Our <a href="/culture/japanese-mythology/" class="inline-link">Japanese mythology guide</a> tells the serpent story.</p>
    <p><strong>The summer festival</strong> runs on July 13 and 14, with a boat procession. Magical Trip says about twenty lantern-decorated boats go along the river and that the procession was revived in 2001 after 230 years. Lion dances are offered on the Shishiden stage (Fun! JAPAN). Dates and details can change, so check with the shrine.</p>

    <h2 id="visit">Visiting Namba Yasaka<span class="h2-jp">参拝案内</span></h2>
    <ul class="practical-list">
      <li><strong>Address:</strong> 2-9-19 Motomachi, Naniwa-ku, Osaka (tel. 06-6641-1149; GLTJP).</li>
      <li><strong>Hours:</strong> daily 6:00 to 17:00; amulets and goshuin 9:00 to 16:50 (GLTJP). Entry is free.</li>
      <li><strong>Access:</strong> about 7 minutes on foot from JR Namba, 8 minutes from Nankai Namba (GLTJP); about 6 minutes from Namba on the Osaka Metro (Magical Trip).</li>
      <li><strong>Payment:</strong> cards are not accepted and there is no parking (GLTJP). Bring cash.</li>
      <li><strong>Ema:</strong> the shrine's wooden plaques show a pair of lions, one on green and one on red.</li>
      <li><strong>Busy times:</strong> January 1 to 3 is crowded (Walkerplus).</li>
      <li><strong>Time to allow:</strong> 20 to 30 minutes by itself (my estimate), longer if you combine it with Namba sightseeing.</li>
    </ul>
"""+fig('ema','A wooden ema plaque with a printed pair of lion faces, one on a green ground and one on a red ground, and the shrine name written down the left side','An ema plaque with the two lions')+"""
    <p>The plaque in the photo carries two lion faces, the name 難波八阪神社 in vertical writing, and a space for the name at the bottom. It is a 2019 photo, so the design may have changed.</p>
    <div class="key-callout">
      <p>&#127890; <strong>Plan your trip:</strong> Browse guided tours in Osaka. <a href="https://www.viator.com/search/Osaka?pid=P00298374&amp;mcid=42383&amp;medium=link&amp;campaign=sacred-japan" target="_blank" rel="noopener" onclick="trackEvent('click','affiliate','viator_namba_yasaka')">Find Osaka tours &rarr;</a></p>
    </div>

    <h2 id="faq">Frequently Asked Questions<span class="h2-jp">よくあるご質問</span></h2>
    <div class="faq-stack">
@@FAQ@@    </div>

    <h2 id="final">Before You Go<span class="h2-jp">むすびに</span></h2>
    <p>Come for the lion, and stay a moment at the main hall behind it. If you want an older Osaka shrine on the same trip, see our """+a('/guides/sumiyoshi-taisha/','Sumiyoshi Taisha guide','sumiyoshi')+""".</p>

    <div class="closing-block">
      <span class="torii">&#9961;&#65039;</span>
      <p>A lion with its mouth open, and an old god of Namba waiting behind it.</p>
    </div>

    <section class="related-section">
      <h2>Related Guides</h2>
      <span class="h2-jp">関連ガイド</span>
      <div class="related-grid">
        <a class="related-card" href="/guides/sumiyoshi-taisha/" onclick="trackEvent('click','internal','related_namba_yasaka_to_sumiyoshi')">
          <div class="related-card-label">SACRED JAPAN ／ GUIDES</div>
          <div class="related-card-title">&#9961;&#65039; Sumiyoshi Taisha &rarr;</div>
          <div class="related-card-desc">Osaka&rsquo;s ancient seaside shrine.</div>
        </a>
        <a class="related-card" href="/culture/japanese-mythology/" onclick="trackEvent('click','internal','related_namba_yasaka_to_mythology')">
          <div class="related-card-label">SACRED JAPAN ／ CULTURE</div>
          <div class="related-card-title">&#128214; Japanese Mythology &rarr;</div>
          <div class="related-card-desc">Susanoo and the eight-headed serpent.</div>
        </a>
        <a class="related-card" href="/guides/kitano-tenmangu/" onclick="trackEvent('click','internal','related_namba_yasaka_to_kitano')">
          <div class="related-card-label">SACRED JAPAN ／ GUIDES</div>
          <div class="related-card-title">&#9961;&#65039; Kitano Tenmangu &rarr;</div>
          <div class="related-card-desc">Another shrine people visit for exam luck.</div>
        </a>
      </div>
    </section>

  </article>

"""
build(dict(slug='namba-yasaka-shrine',ev='namba_yasaka',dest='Osaka',jp='難波八阪神社',en='Namba Yasaka Shrine',
 title="Namba Yasaka Shrine Guide: The Giant Lion Head Hall, Festivals and How to Visit",
 desc="A licensed guide's guide to Namba Yasaka Shrine in Osaka: the 12 m lion-head Shishiden built in 1974, the deities, the January tug-of-war and summer boat festival, hours and access.",
 kw="Namba Yasaka Shrine, Namba Yasaka Jinja, lion head shrine Osaka, Shishiden, Osaka shrine, Namba shrine, Tsunahiki Shinji",
 h1="<h1><em>Namba Yasaka Shrine</em>: The Giant Lion Head Hall, Festivals and How to Visit</h1>",
 tag="Osaka's shrine with a lion-head hall, a few minutes from Namba.",
 og=("Namba Yasaka Shrine Guide:","The Giant Lion Head Hall"),thumb='lion-front',photos=P,faqs=faqs,body=body,
 sources=[('https://nambayasaka.jp/?page_id=145','official','Namba Yasaka Shrine (Tsunahiki page)'),('https://www.gltjp.com/en/directory/item/14268/','gltjp','GLTJP'),('https://www.magical-trip.com/media/osakas-namba-yasaka-shrine-home-of-the-majestic-lion-head-and-rich-traditions/','magical','Magical Trip'),('https://www.fun-japan.jp/tw/articles/11636','funjapan','Fun! JAPAN'),('https://tabi-mag.jp/os0336/','tabimag','tabi-mag'),('https://www.walkerplus.com/spot/ar0727s30771/','walker','Walkerplus')]))
