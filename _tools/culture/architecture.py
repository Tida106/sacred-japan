import re, os, json
R='/home/claude/sacred-japan'
S='shrine-architecture'
OUT=f'{R}/culture/{S}'
os.makedirs(OUT,exist_ok=True)

def link(href,txt,lab): return f'<a href="{href}" class="inline-link" onclick="trackEvent(\'click\',\'internal\',\'{lab}\')">{txt}</a>'
def ext(href,txt,lab): return f'<a href="{href}" target="_blank" rel="noopener" onclick="trackEvent(\'click\',\'external\',\'{lab}\')">{txt}</a>'
VI='https://www.viator.com/search/japan+shrine+tour?pid=P00298374&amp;mcid=42383&amp;medium=link&amp;campaign=sacred-japan'
EX='https://expedia.com/affiliate?siteid=1&amp;landingPage=https%3A%2F%2Fwww.expedia.co.jp%2FHotel-Search%3Fdestination%3DKyoto&amp;camref=1101l5JmFa&amp;creativeref=1011l87782&amp;adref=PZf6lQ77e8'

KOK='https://d-museum.kokugakuin.ac.jp/eos/detail/?id=9696'
KOKS='https://d-museum.kokugakuin.ac.jp/eos/detail/?id=9063'
NIP='https://nippon.com/en/views/b05209'
NIPS='https://www.nippon.com/en/views/b05201/your-virtual-guide-to-the-shinto-shrine.html'
WHE='https://www.worldhistory.org/Shinto_Architecture/'
WIKI='https://en.wikipedia.org/wiki/Shinto_architecture'
WIKIH='https://en.wikipedia.org/wiki/Honden'
MLIT='https://www.mlit.go.jp/tagengo-db/R3-00180.html'
JGIZ='https://www.japan-guide.com/e/e5804.html'
WJA='https://web-japan.org/atlas/architecture/arc20.html'
ISEK='https://en.ise-kanko.jp/shikinen-sengu-63/'
TW='https://www.tokyoweekender.com/?p=294342'
NG='https://www.nationalgeographic.com/travel/article/this-japanese-shrine-is-torn-down-every-20-years'
WTOP='https://wtop.com/world/2025/09/photos-show-historic-japanese-shrine-that-is-torn-down-and-rebuilt-every-20-years'
WEF='https://www.weforum.org/stories/arts-and-culture/japans-holiest-shrine-is-pulled-down-and-rebuilt-every-20-years-on-purpose/'
JFS='https://www.japanfs.org/en/news/archives/news_id027786.html'
NIPONICA='https://web-japan.org/niponica/niponica32/en/feature/feature02.html'
EMB='https://www.sg.emb-japan.go.jp/JCC/E-Magazine-Sep-2024-Miyadaiku.html'
LJ='https://livejapan.com/en/in-kansai/in-pref-osaka/in-osaka-suburbs/article-a2000907/'
BUNKA='https://www.bunka.go.jp/tokei_hakusho_shuppan/shuppanbutsu/bunkazai_pamphlet/pdf/94442601_02.pdf'
SMITH='https://www.smithsonianmag.com/smart-news/this-japanese-shrine-has-been-torn-down-and-rebuilt-every-20-years-for-the-past-millennium-575558/'

# photo slots: filled in by later photo scripts (key -> ready-made <figure> html)
PH={}
def ph(k): return PH.get(k,'')

CAPST='font-size:13px;color:var(--enshu);margin-top:10px;text-align:center;line-height:1.6;'
LA='style="color:var(--enshu);"'
def lk(t,u): return f'<a href="{u}" target="_blank" rel="noopener" {LA}>{t}</a>'
def cfile(n): return lk("Wikimedia Commons","https://commons.wikimedia.org/wiki/File:"+n)
def csearch(q): return lk("Wikimedia Commons",'https://commons.wikimedia.org/w/index.php?search='+q+'&title=Special:MediaSearch&type=image')
def pfig(src,alt,desc,cred,mw=760):
    return (f'<figure style="margin:36px auto;max-width:{mw}px;">\n      <picture><source srcset="/culture/shrine-architecture/images/{src}.webp" type="image/webp"><img src="/culture/shrine-architecture/images/{src}.jpg" alt="{alt}" loading="lazy" style="width:100%;height:auto;border-radius:4px;display:block;"></picture>\n      <figcaption style="{CAPST}">{desc}<br>{cred}</figcaption>\n    </figure>')
L_BYSA3=lk("CC BY-SA 3.0","https://creativecommons.org/licenses/by-sa/3.0/")
L_BYSA4=lk("CC BY-SA 4.0","https://creativecommons.org/licenses/by-sa/4.0/")
L_BY2=lk("CC BY 2.0","https://creativecommons.org/licenses/by/2.0/")

PH['roof']=pfig('ise-naiku-roof','Roof of a main sanctuary seen over a plank fence in a forest: a thick thatched roof with forked chigi at both ends and a row of round katsuogi logs laid across the ridge, with gold-colored metal fittings, and part of a second roof at the left',
 'The roof of the main sanctuary of the Inner Shrine at Ise, as Commons labels it, seen over its plank fence. You can see all three features from this section: thick thatch, the forked chigi at each end of the ridge, and a row of katsuogi laid across it, with gold-colored metal fittings. World History Encyclopedia gives 10 katsuogi for the Inner Shrine, and the row here looks like about ten to me, though I would not swear to my count from a photo. Notice that the fence hides everything below the roof, which is how most visitors see this building.',
 f'Photo: N yotarou, August 2006, {L_BYSA3} (the file is also offered under GFDL and CC BY 2.5), via {cfile("Naiku_01.jpeg")} (resized)',mw=760)
PH['roof']+='\n\n    '+pfig('ise-tsukiyomi-miya','Two small separate shrine buildings with thatched roofs, forked chigi and a row of katsuogi on each ridge, standing in a court of white gravel behind a plain wooden fence, with a stone lantern in the foreground and tall trees behind',
 'Two small buildings at Tsukiyomi-no-miya, a subsidiary shrine of the Inner Shrine, with the same thatch, chigi and katsuogi as the main sanctuary. The Japanese description on Commons says the shrines of Izanagi and Izanami here follow the Inner Shrine\'s pattern whatever the sex of the deity, with inward-cut chigi and six katsuogi. That is worth knowing: it suggests the rule of thumb above is a tendency and not a law, since a male deity appears with the pattern the rule would link to a female one. That is my reading of the description, not a statement from the shrine.',
 f'Photo: N yotarou, September 2006, {L_BYSA3} (also offered under GFDL), via {cfile("Tsukiyomi-no-miyaNaiku_05.jpeg")} (resized)',mw=760)
PH['roof']+='\n\n    '+pfig('roof-closeup-copper','Close view from below of the corner of a shrine roof: dark weathered copper sheathing, a forked chigi with gold-colored rectangular openings, a round katsuogi end with a small crest, and a row of short round rafter ends under the eave, against green leaves',
 'A close look at a roof corner at a smaller shrine. Commons gives no location, and I cannot tell which shrine it is. The chigi and the roof edge are sheathed in dark, weathered copper, the chigi have gold-colored framed openings, and the end of a katsuogi carries a round crest that looks like a swirling design to me. It is a useful picture of how much metal sits on a roof that people describe as pure wood, and of how the forked chigi cross at the ridge. Commons titles the file only with the word 鞭掛.',
 f'Photo: 粟山 (name as shown on Commons), 16 October 2022, {L_BYSA4}, via {csearch("%E9%9E%AD%E6%8E%9B+shrine+chigi+katsuogi")} (resized)',mw=760)
PH['origins']=pfig('ise-mishine-mikura','A small raised-floor building in a forest: pale wood walls, a thatched roof with forked chigi and a row of katsuogi, stout posts holding the floor off the ground, a rope fence in front and a stone lantern at the right',
 'A raised-floor building at the Inner Shrine, titled on Commons as Mishine-no-mikura at the Ise grand sanctuary. As I read the name, it is a storehouse for the sacred rice, which would fit the granary model: stout posts lift the floor off the ground, the walls are plain wood and the roof is thatch. The part of the Commons page I could see does not say what the building holds, so take the storehouse reading as mine.',
 f'Photo: Jean-Pierre Dalbéra, 13 May 2018, {L_BY2} (reviewed on Commons as licensed on Flickr), via {cfile("Le_sanctuaire_shinto_Mishine-no-mikura_grand_sanctuaire_dIse_Japon_42387575474.jpg")} (resized)',mw=760)
PH['styles']=pfig('shinmei-drawing','Line drawing of a shinmei-zukuri shrine building: a heavy gabled roof with forked chigi and a row of katsuogi logs, a veranda with a railing on posts all around, and a flight of steps up to the entrance on the long side',
 'A line drawing of shinmei-zukuri (Commons: \"Japanese shrine type Shimmei\"). It shows the points from the list above in one picture: the gabled roof with chigi and katsuogi, a raised floor on posts with a railed veranda, and the stair up to an entrance on the long side of the building.',
 f'Drawing: Fraxinus2, 14 May 2014, {L_BYSA3}, via {cfile("Shimmei_Stil.jpg")} (resized)',mw=520)
L_PD=lk("public domain","https://commons.wikimedia.org/wiki/Template:PD-user-w")
PH['styles']+='\n\n    '+pfig('nagare-drawing','Line drawing of a nagare-zukuri shrine building: one long gabled roof whose front slope sweeps down in a smooth curve over a covered porch, a railed veranda on posts at the side, and wooden steps leading up at the front',
 'A line drawing of nagare-zukuri (Commons: \"Japanese shrine type Nagare\"). The front slope of the roof is much longer than the rear slope and runs down in one curve over the steps and porch. That sweep is the \"flow\" in the name, and it is the quickest way to spot the style.',
 f'Drawing: Fraxinus2, 14 May 2014, {L_BYSA3}, via {cfile("Nagare_Stil.jpg")} (resized)',mw=520)
PH['styles']+='\n\n    '+pfig('fushimi-honden','A shrine hall at dusk with a dark, deeply curved roof topped by a gold crest at the front gable, red pillars and white panels under the eaves, gold ornaments on the beams, a red railing in front and a gravel court',
 'The main hall of Fushimi Inari Taisha in Kyoto, described on Commons as the main shrine (honden). The long roof sweeps forward in a deep curve over the front, which matches the Commons title of the next photo, nagare-zukuri. It is a good building to compare with the drawing above. The photo is from 2004, so details may have changed since.',
 f'Photo: Stanislaus, 27 March 2004, released into the {L_PD} on Japanese Wikipedia, via {cfile("Hushimi-inari-taisha_honden.jpg")} (533 x 400, not enlarged)',mw=533)
PH['styles']+='\n\n    '+pfig('fushimi-nagare-roof','Corner of a shrine roof seen from below against a blue sky: a thick, curved dark roof that looks like layered bark, a gold crest on the ridge end, red rafters and beams, white panels, and gold flower-shaped metal fittings along the eaves',
 'A close look at the same shrine, titled on Commons \"Fushimi Inari Taisha Nagare Zukuri.\" The roof curves down in one long arc, the rafters under the eave are painted vermilion, and gold fittings mark the beam ends. The roof surface looks like layered bark, though the Commons page does not say what it is made of, so I will not name the material. The white sheet at the bottom is a cover over something at the shrine, probably for an event.',
 f'Photo: Immanuelle, 20 August 2023, {L_BYSA4}, via {cfile("Fushimi_Inari_Taisha_Nagare_Zukuri.jpg")} (resized)',mw=760)
PH['ise']=pfig('ise-izawa-miya','Two new-looking buildings made of pale unpainted wood in a forest clearing: a thatched hall with forked chigi and katsuogi behind a tall plank fence, and a smaller gabled hall with a ribbed roof and a simple gate frame in front, standing on a bed of white stones',
 'Izawa-no-miya, which the Japanese description on Commons gives as a subsidiary shrine of the Inner Shrine in Shima, Mie Prefecture. The wood is pale and unweathered and the thatch looks fresh, which is what a shinmei building looks like when it is new. The photo is from May 2015, but the Commons page does not say when this building was put up, so I do not tie it to the 2013 rebuilding. The bed of white stones around the buildings is a common sight at the Ise shrines.',
 f'Photo: N yotarou, May 2015, {L_BYSA4}, via {cfile("Izawa-no-miya_07.jpg")} (resized)',mw=760)

faqs=[
("What is the difference between a honden and a haiden?","The honden is the main hall where the kami is enshrined; it sits at the back and is normally closed to the public. The haiden is the worship hall in front of it, and it is the building most visitors actually stand before. The {WIKIH_L} and the {WIKI_L} both describe this order, with a heiden (offering hall) sometimes joining the two."),
("Why do some shrines have no main hall?","Some kami are a mountain, a tree or a rock, so the shrine needs a place to pray toward but not a building to house the god. {NIP_L} gives Omiwa Shrine (Mount Miwa) as an example and also names Suwa Taisha. At such shrines the haiden is the most important building. Our {SUWA_L} explains how Suwa works."),
("What are the crossed beams on the roof?","They are called <em>chigi</em>, and the short logs lying across the ridge are <em>katsuogi</em>. They once held the thatch in place and are now mostly decoration, but they are the clearest sign of an old, orthodox shrine roof. Nippon.com adds a rule of thumb about what their cut and count say about the deity; see the section on reading the roof above."),
("Is Ise Shrine really rebuilt every 20 years, and can I see it?","Yes. The Kokugakuin Encyclopedia of Shinto dates the practice to 690 for the Inner Shrine and 692 for the Outer Shrine, and the 62nd rebuilding was in 2013. The current cycle began in 2025 and ends in 2033. The new building is put up beside the old one, and the inner sanctuary is closed to ordinary visitors. What you can do is walk the grounds and see the outer fences and the subsidiary shrines. Our {ISE_L} has the visiting details."),
("Are shrines really built without nails?","The main structure is, yes. Traditional carpenters join the timbers with <em>kigumi</em>, which the Web Japan feature describes as joining wood without nails or metal fittings. But I would not say there is no metal anywhere. The Encyclopedia of Shinto lists gold and copper hardware among the materials at Ise, and the Izumo roof ridge carries copper-wrapped katsuogi. So \"no nails in the framing\" is accurate; \"no metal at all\" is not."),
("Which shrine style is the most common?","Nagare-zukuri. The Kokugakuin Encyclopedia of Shinto calls it the most common shrine style nationwide, with kasuga-zukuri second, and says most small and medium shrines use one of the two. If you have visited a handful of local shrines, you have probably seen both."),
("What is the tallest shrine building in Japan?","The main hall of Izumo Taisha. Japan Guide and the Ministry of Land, Infrastructure, Transport and Tourism database both give 24 meters for the building rebuilt in 1744. Earlier versions are said to have been far taller, but the Encyclopedia of Shinto calls the 48-meter reconstruction drawings somewhat unrealistic. See our {IZUMO_L}."),
]
LINKS={
 'WIKIH_L':'<a href="https://en.wikipedia.org/wiki/Honden" target="_blank" rel="noopener">Wikipedia entry on the honden</a>',
 'WIKI_L':'<a href="https://en.wikipedia.org/wiki/Shinto_architecture" target="_blank" rel="noopener">overview of Shinto architecture</a>',
 'NIP_L':'<a href="https://nippon.com/en/views/b05209" target="_blank" rel="noopener">Nippon.com</a>',
 'SUWA_L':'<a href="/guides/suwa-taisha/" class="inline-link">Suwa Taisha guide</a>',
 'ISE_L':'<a href="/guides/ise-grand-shrine/" class="inline-link">Ise Grand Shrine guide</a>',
 'IZUMO_L':'<a href="/guides/izumo-taisha/" class="inline-link">Izumo Taisha guide</a>',
}
def fill(a):
    for k,v in LINKS.items(): a=a.replace('{'+k+'}',v)
    return a
faq_html=''.join(f"""      <details class="faq-item">
        <summary>{q}</summary>
        <div class="faq-answer">{fill(a)}</div>
      </details>

""" for q,a in faqs)
faq_ld=json.dumps({"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":re.sub('<[^>]+>','',fill(a))}} for q,a in faqs]},ensure_ascii=False,indent=2)

TITLE="Shinto Shrine Architecture Guide: Styles, Roofs, Parts and How Shrines Are Built"
DESC="A licensed guide's English introduction to Shinto shrine architecture: the honden, haiden and torii, how to read chigi and katsuogi on the roof, the main styles from Ise to Izumo to Nikko, and how shrines are built."
URL=f"https://sacred-japan.net/culture/{S}/"
OG="https://sacred-japan.net/images/og/og-culture-shrine-architecture.jpg"

L_CC0=lk("CC0","https://creativecommons.org/publicdomain/zero/1.0/")
L_BYSA4b=L_BYSA4
L_BY4=lk("CC BY 4.0","https://creativecommons.org/licenses/by/4.0/")
L_BY3=lk("CC BY 3.0","https://creativecommons.org/licenses/by/3.0/")
PH['styles']+='\n\n    '+pfig('sumiyoshi-keidai','Wide view across a gravel court at Sumiyoshi Taisha: several dark thatched sanctuary roofs side by side, each with a pair of crossed chigi on the ridge, red-painted fences along the front, a few visitors walking, and tall pines at the right under a pale sky',
 'Sumiyoshi Taisha in Osaka, the model for sumiyoshi-zukuri. Commons labels this view \"precinct\" (境内). The main sanctuaries stand in a row, and every roof has the same crossed chigi on the ridge. Behind the red fence, the buildings are painted vermilion and white, which is the look the encyclopedia gives for this style.',
 f'Photo: Saigen Jiro, 14 May 2016, {L_CC0} (public domain dedication, credited anyway), via {cfile("Sumiyoshi-taisha,_keidai.jpg")} (resized)',mw=760)
PH['styles']+='\n\n    '+pfig('sumiyoshi-second-honden','Corner view of a sanctuary at Sumiyoshi Taisha: a steep thatched roof with crossed chigi and a row of short round katsuogi ends with gold crests on the ridge, the gable end painted vermilion with white walls below, and a red fence around it, with a second curved roof beside it',
 'The second main sanctuary, labeled on Commons as the honden of the second main shrine (第二本宮本殿). The gable end faces the camera, with vermilion beams and white wall panels under a steep roof, which matches the gable-end entrance in the list above. I cannot see the interior, so I will not repeat the claim about two rooms from this photo. The ridge carries crossed chigi at the near end and gold-crested katsuogi along the top.',
 f'Photo: Saigen Jiro, 14 May 2016, {L_CC0} (public domain dedication, credited anyway), via {cfile("Sumiyoshi-taisha,_hongu-2_honden.jpg")} (resized)',mw=760)
PH['styles']+='\n\n    '+pfig('sumiyoshi-second-shaden','Side view of a sanctuary at Sumiyoshi Taisha: a long thatched roof with crossed chigi at the left end and four round katsuogi ends along the ridge, a row of gold-and-red brackets under the eave, vermilion pillars with white walls, a red fence with black-capped posts in front, and a second building with a curved roof at the right',
 'The same group from the long side, labeled on Commons as the shrine building of the second main shrine (第二本宮社殿). From here you can see the pattern of the style in one frame: a straight roofline, vermilion pillars with white walls, and a fence around the building. The curved roof at the right belongs to a different, attached structure, and I do not know its name.',
 f'Photo: Saigen Jiro, 14 May 2016, {L_CC0} (public domain dedication, credited anyway), via {cfile("Sumiyoshi-taisha,_hongu-2_shaden.jpg")} (resized)',mw=760)
PH['styles']+='\n\n    '+pfig('sumiyoshi-first-hongu','Front of a hall at Sumiyoshi Taisha under a blue sky with pine trees: a wide dark thatched roof with a curved gabled porch over the center, crossed chigi above the ridge, a green net over the gable ornament, red fences and lanterns, and a few people standing on the gravel and on the hall steps',
 'The first main shrine (第一本宮), as the sign on the post reads. The hall faces a gravel court, and a curved gabled porch roof projects from the center of the thatched roof, with crossed chigi above the ridge. It looks like a ceremony is under way inside, with a priest in white and a person in a white head covering on the steps. The green netting over the gable ornament is something I can see but not explain.',
 f'Photo: Nankou Oronain (as36…), 13 October 2012, {L_BYSA3}, originally posted to Panoramio, via {csearch("Sumiyoshi-taisha+hongu+Nankou+Oronain")} (resized)',mw=760)
PH['styles']+='\n\n    '+pfig('sumiyoshi-hongu-chigi','Front of a main sanctuary hall at Sumiyoshi Taisha on a clear day: a deep thatched roof with large crossed chigi on top, a curved gable over the entrance with a green net over its ornament, two hanging lanterns, red fences left and right, and a woman walking across the gravel in front',
 'The main sanctuary group again, in a close view from the front. The chigi are very large here, crossed in an X above a flat metal base. The curved gable over the entrance is a later-looking addition to the straight roofline, so the building has two roof shapes at once. Commons titles this view \"Hongu\" (the main shrines) without saying which of the four.',
 f'Photo: Hyppolyte de Saint-Rambert, 9 February 2024, {L_BY4}, via {csearch("Sumiyoshi-taisha+Osaka+Sumiyoshi-ku+Hongu+Hyppolyte")} (resized)',mw=760)
PH['izumo']=pfig('izumo-honden-wide','The main sanctuary of Izumo Taisha seen from the side under a blue-grey sky: a tall steeply swept roof with crossed chigi and a row of round katsuogi on the ridge, two smaller buildings with their own crossed chigi on the left, and a long fence in the foreground with a mossy roof of its own',
 'The main sanctuary at Izumo, which Commons titles as the main hall of Izumo Taisha, seen from outside the fence. Compare it with the Ise roofs above: the roof is a deep, steeply swept mass of bark, the chigi cross at the ridge and the katsuogi are round logs laid along it, but the whole building is a tall, almost square block, not a long low hall. The two smaller roofs at the left carry the same crossed chigi. The long fence in front has a mossy roof of its own, which is why you only ever see the top of the hall.',
 f'Photo: Naokijp, 4 January 2022, {L_BYSA4}, via {cfile("Izumo_Taisha_Main_Sanctuary_001.jpg")} (resized)',mw=760)
PH['izumo']+='\n\n    '+pfig('izumo-honden-hills','Izumo Taisha seen across a gravel court under low cloud: a tall dark roof with large crossed chigi and round katsuogi rises behind lower bark-roofed halls and gates with gold crests, with wooded hills behind and a stone stair and a few signboards in front',
 'Commons titles this one simply as the main hall of Izumo Taisha. What I can see is the tall gable of the main hall with its crossed chigi rising behind lower bark-roofed halls and gates, with gold crests on the gable ends and the wooded hill behind. I cannot tell which of the lower structures in front is which, so I will not name them. It is a good picture of how the hall sits deep in the compound, with several layers of roofs between you and it.',
 f'Photo: Saigen Jiro, 8 March 2016, {L_CC0} (public domain dedication, credited anyway), via {cfile("Honden_of_Izumo-taisha-1.jpeg")} (resized)',mw=760)
PH['izumo']+='\n\n    '+pfig('izumo-roofs-fence','Several dark thatched roofs of the Izumo Taisha sanctuary rising over a long fence with a mossy roof: crossed chigi and round katsuogi on each ridge, steep curved eaves, and a stone-edged path in the foreground under a clear sky',
 'A 2006 view of the same group of roofs from the path outside the fence. The chigi cross at the ridge of each building, and the katsuogi sit along it, a little more spread out than on a thatched Ise roof. With a clear sky behind them, the swept lines of the eaves are easy to read. The Commons description just says it is the Izumo-taisha.',
 f'Photo: Blue Lotus (Amy, Flickr user), 20 March 2006, {L_BY2} (reviewed on Commons as licensed on Flickr), via {cfile("Izumo-taisha_121538651_f69f257ed0_o.jpg")} (resized)',mw=760)
PH['izumo']+='\n\n    '+pfig('izumo-roofs-flag','Dark roofs of the Izumo Taisha sanctuary against a clear blue sky: a large steep roof with crossed chigi and round katsuogi, a smaller roof beside it, and a Japanese flag on a pole between them, with a dark fence in the foreground',
 'The same group from a lower angle, in silhouette. The crossed chigi and the round katsuogi stand out clearly against the sky, and the Japanese flag between the roofs gives a sense of scale. The Commons description is again only the Izumo-taisha, so I cannot say which building is in front.',
 f'Photo: Blue Lotus (Amy, Flickr user), 20 March 2006, {L_BY2} (reviewed on Commons as licensed on Flickr), via {cfile("Izumo-taisha_121539276_b25e49382d_o.jpg")} (resized)',mw=760)
PH['izumo']+='\n\n    '+pfig('izumo-karidono','Wide view of a large hall at Izumo Taisha under a cloudy sky: a broad dark gabled roof with a smaller roof over the entrance, a thick rope hanging across the front, visitors standing on the stone court, a signboard reading Karidono, and grey hoarding at the right',
 'A reminder that Izumo was being worked on in the years of the last big renovation. The Commons description says the building shown is the temporary hall (the sign reads 御仮殿, Karidono, as I read it) and that the main sanctuary was under reconstruction in May 2012, due for completion in May 2013. That fits the schedule above. The rope across the front and the grey screen at the right are part of what a visitor saw at the time, and the scene will look different now.',
 f'Photo: z tanuki, 2 May 2012, {L_BY3} (originally posted to Panoramio, reviewed on Commons), via {csearch("Izumo+Grand+Shrine+panoramio+z+tanuki")} (resized)',mw=760)

main=f"""<main>

  <!-- TABLE OF CONTENTS -->
  <aside class="toc" aria-label="Table of contents">
    <div class="toc-label">TABLE OF CONTENTS ／ 目次</div>
    <div class="toc-title">In This Guide</div>
    <ol>
      <li><a href="#opening">Opening: A Note from the Guide</a></li>
      <li><a href="#layout">The Layout: From Torii to Honden</a></li>
      <li><a href="#origins">Two Ancient Models: The Granary and the House</a></li>
      <li><a href="#roof">Reading the Roof: Chigi and Katsuogi</a></li>
      <li><a href="#styles">The Main Styles at a Glance</a></li>
      <li><a href="#ise">Ise: The Shrine That Is Rebuilt</a></li>
      <li><a href="#izumo">Izumo: The Tallest Hall</a></li>
      <li><a href="#craft">How Shrines Are Built</a></li>
      <li><a href="#visit">How to Read a Shrine When You Visit</a></li>
      <li><a href="#faq">Frequently Asked Questions</a></li>
      <li><a href="#final">Final Thoughts</a></li>
    </ol>
  </aside>

  <article>

    <section id="opening">
      <p class="opening">Stand in front of almost any shrine hall in Japan and look up. At the very top of the roof you will often see two timbers crossing like a pair of horns, and lying along the ridge a row of short, fat logs. They look like decoration, and they are, but they are also a code. According to Nippon.com, the way the horns are cut and how many logs there are can tell you whether the kami inside is male or female.</p>
      <p>As a licensed guide, I find that visitors who learn four or five terms start to see shrines instead of just walking through them. This guide gives you those terms: how a shrine compound is laid out, the two ancient models that every style grows from, the main styles you will meet, and two famous buildings that show the extremes, Ise, which is rebuilt every twenty years, and Izumo, which is the tallest. Then it explains how the buildings are made, and how to put it all to use on your next visit.</p>
    </section>

    <h2 id="layout">The Layout: From Torii to Honden<span class="h2-jp">社殿の配置</span></h2>
    <p>A shrine is a sequence, and the buildings are arranged along a path that moves you from the ordinary world toward the kami. The {ext(WIKI,'Wikipedia overview of Shinto architecture','arch_wikipedia_layout')} and the {ext(WHE,'World History Encyclopedia article','arch_whe_layout')} give the same basic order.</p>
    <ul>
      <li><strong>Torii:</strong> the gate that marks the entrance to a sacred area. Wikipedia notes that a torii can be made of wood, stone, metal or concrete, and that Fushimi Inari has thousands.</li>
      <li><strong>Sando:</strong> the approach path that joins the torii to the worship hall.</li>
      <li><strong>Haiden:</strong> the hall of worship, where you stand to pray. World History Encyclopedia calls it usually the most impressive building at the shrine.</li>
      <li><strong>Heiden:</strong> the offering hall between the haiden and the honden. It is sometimes a separate building and sometimes just a covered link, and some shrines do not have one.</li>
      <li><strong>Honden:</strong> the main sanctuary, where the kami is enshrined. It is normally at the rear, smaller and plainer than the haiden, and closed to the public.</li>
      <li><strong>Tamagaki and kairo:</strong> the fence that surrounds the honden, and the covered, colonnaded walkway that can run around the inner sacred area.</li>
    </ul>
    <p>The honden itself is usually divided into two parts, an inner sanctuary (<em>naijin</em>) and an outer one (<em>gejin</em>), according to World History Encyclopedia. The object that holds the spirit, the <em>goshintai</em>, is kept inside, which is one reason you will almost never see it.</p>
    <p>There is one important exception. Nippon.com points out that some shrines have only a haiden, because the kami is a natural feature such as a sacred mountain or tree. It names Omiwa Shrine at Mount Miwa and Suwa Taisha. If you want to see how that works on the ground, our {link('/guides/suwa-taisha/','Suwa Taisha guide','arch_to_suwa')} walks through it.</p>
    {ph('layout')}

    <h2 id="origins">Two Ancient Models: The Granary and the House<span class="h2-jp">神明造と大社造</span></h2>
    <p>Nippon.com says that all honden styles trace back to one of two models: <em>shinmei-zukuri</em>, which is modeled on the ancient Japanese granary and best known at Ise, and <em>taisha-zukuri</em>, which is thought to reflect ancient residential architecture and takes its name from Izumo Taisha. The Wikipedia overview adds a third ancient form, <em>sumiyoshi-zukuri</em>, represented by Sumiyoshi Taisha.</p>
    <p>That is a useful picture to hold on to. The oldest shrines did not copy a temple. They copied a storehouse for rice, which was the wealth of the country, and a house for a chief. Wikipedia also notes that before Buddhism arrived, most shrines were temporary structures built for a particular purpose, and that from around the mid-6th century Buddhism brought new elements. Later shrine halls borrowed features from temple architecture such as stone column bases, brackets, painted surfaces and metal ornaments. The {ext(KOK,'Encyclopedia of Shinto','arch_kokugakuin_history')} adds that shrine architecture did not evolve in a straight line the way temples and houses did, and that there were periodic movements to return to ancient forms.</p>
    <p>So when a shrine is plain, unpainted wood, you are probably looking at the oldest tradition. When it is red, gilded and carved, you are looking at a later layer that borrowed from the temple world. If you want to compare the two worlds on the ground, our {link('/culture/shrine-vs-temple/','shrine vs temple guide','arch_to_shrinetemple')} sets them side by side.</p>
    {ph('origins')}

    <h2 id="roof">Reading the Roof: Chigi and Katsuogi<span class="h2-jp">千木と鰹木</span></h2>
    <p>Back to the code on the roof. Nippon.com describes <em>chigi</em> as paired slender timbers at the roof ends that fork upward and outward from the ridge, and <em>katsuogi</em> as short logs laid across the ridge. It calls them probably the most distinctive features of Shinto architecture, found on the most orthodox honden. World History Encyclopedia says they once did real work, holding down the roof in early wooden buildings, and are now mostly decorative.</p>
    <p>The rule of thumb, as Nippon.com gives it:</p>
    <ul>
      <li><strong>Chigi cut horizontally</strong> (<em>uchi-sogi</em>) suggests a female deity, and <strong>chigi cut vertically</strong> (<em>soto-sogi</em>) a male one.</li>
      <li><strong>An even number of katsuogi</strong> suggests a female deity, and <strong>an odd number</strong> a male one.</li>
      <li>Horizontal chigi almost always go with an even number of katsuogi, and vertical chigi with an odd number.</li>
    </ul>
    <p>Treat it as a guide, not a law; Nippon.com itself says &quot;almost always.&quot; But two famous buildings fit it. World History Encyclopedia counts 10 katsuogi on the Inner Shrine at Ise, which enshrines the goddess Amaterasu, and the Ministry of Land, Infrastructure, Transport and Tourism database says the Izumo main hall carries three, wrapped in copper sheeting, for the god Okuninushi. I only checked the counts, not the chigi cuts, so I am noting a pattern, not proving the rule.</p>
    {ph('roof')}

    <h2 id="styles">The Main Styles at a Glance<span class="h2-jp">本殿の様式</span></h2>
    <p>Japanese shrine styles are named with the suffix <em>-zukuri</em>, meaning &quot;built in the manner of.&quot; The list below follows the {ext(KOK,'Kokugakuin Encyclopedia of Shinto','arch_kokugakuin_styles')}, which is the most careful source I found. I have kept to the features it gives and added links to our own guides where we cover the shrine.</p>
    <ul>
      <li><strong>Shinmei-zukuri (神明造):</strong> a gabled roof with the entrance on the long side, a straight roofline without upturned eaves, unfinished planed wood, and chigi and katsuogi. Found at the Ise shrines and their branches, and used for many shrines built since the Meiji period. See our {link('/guides/ise-grand-shrine/','Ise Grand Shrine guide','arch_to_ise')}.</li>
      <li><strong>Taisha-zukuri (大社造):</strong> entrance at the gable end, with a central &quot;heart pillar,&quot; <em>shin no mihashira</em>. The model is Izumo Taisha. See our {link('/guides/izumo-taisha/','Izumo Taisha guide','arch_to_izumo')}.</li>
      <li><strong>Sumiyoshi-zukuri (住吉造):</strong> entrance at the gable end, an interior divided into front and rear rooms, vermilion pillars and white walls. See our {link('/guides/sumiyoshi-taisha/','Sumiyoshi Taisha guide','arch_to_sumiyoshi')}.</li>
      <li><strong>Nagare-zukuri (流造):</strong> a gabled roof with the entrance on the long side and a portico roof that sweeps forward over the full width. The encyclopedia calls it the most common style in the country, and gives the Upper and Lower Kamo shrines in Kyoto as examples. Our {link('/guides/best-shrines-kyoto/','best shrines in Kyoto guide','arch_to_kyoto')} includes the Kamo area.</li>
      <li><strong>Kasuga-zukuri (春日造):</strong> entrance at the gable end, a small roof covering the entry stairway, and usually just one bay wide. It is the second most common style, concentrated in the Kinki region. See our {link('/guides/kasuga-taisha/','Kasuga Taisha guide','arch_to_kasuga')}.</li>
      <li><strong>Hachiman-zukuri (八幡造):</strong> two gabled buildings joined front and rear, each entered from the side that is not the gable. The examples given are Usa Jingu and Iwashimizu Hachimangu.</li>
      <li><strong>Ryonagare-zukuri (両流造):</strong> a nagare-style building with the full-width portico roof at the front and the rear. Itsukushima Shrine is one example. See our {link('/guides/itsukushima-shrine/','Itsukushima Shrine guide','arch_to_itsukushima')}.</li>
      <li><strong>Gongen-zukuri (権現造), also called ishinoma-zukuri:</strong> a haiden in front of the honden, joined by a low roofed passage called the <em>ishi no ma</em>. Kitano Tenmangu and Nikko Toshogu are the examples. The name &quot;gongen&quot; comes from Tokugawa Ieyasu's posthumous title, Tosho Daigongen, and the encyclopedia warns that the term is sometimes applied loosely to any lavishly ornamented style. See our {link('/guides/nikko-toshogu/','Nikko Toshogu guide','arch_to_nikko')}.</li>
    </ul>
    <p>The encyclopedia lists more regional forms, such as hiyoshi-zukuri and owari-zukuri, and a simplified <em>misedana-zukuri</em> that is usually used for small auxiliary shrines. For a first visit, the first five on the list will take you a long way.</p>
    {ph('styles')}

    <h2 id="ise">Ise: The Shrine That Is Rebuilt<span class="h2-jp">伊勢と式年遷宮</span></h2>
    <p>The Ise shrines use a pure form called <em>yuitsu shinmei-zukuri</em>. The Encyclopedia of Shinto describes it as a linear, storehouse-shaped building with a thatched gabled roof on pillars sunk directly into the ground, with the entrance on the side that is not the gable. The materials are limited to cypress, miscanthus reeds (<em>kaya</em>) and gold and copper hardware, and a sacred central post, <em>shin no mihashira</em>, is ritually set beneath the main sanctuary's floor.</p>
    <p>Then comes the part that surprises most visitors. The same encyclopedia says the transfer to a newly built shrine, <em>shikinen sengu</em>, was first performed in 690 for the Inner Shrine and in 692 for the Outer Shrine, in the reign of Empress Jito. The Wikipedia entry on Ise says the old buildings are dismantled and new ones built on an adjacent site to exactly the same design, and the World Economic Forum notes it had been rebuilt 62 times by 2013. The current cycle, the 63rd, began in 2025 and concludes in 2033, according to {ext(NG,'National Geographic','arch_natgeo_sengu')}.</p>
    <p>It is not a quick job. Tokyo Weekender describes it as roughly an eight-year journey of about 30 rituals; the Ise city tourism site says about nine years. The difference is probably in where you start counting. An Associated Press report carried by WTOP says workers collect and process more than 10,000 cypress trees for it.</p>
    <p>Why every twenty years? No single answer is certain. A practical one, from an English translation of the Japanese encyclopedia entry, is that plain wood pillars set in the ground and thatched roofs simply do not last long. The Japan for Sustainability newsletter adds that in the granary design the heavy thatched roof pressed the wall boards together and helped keep the stored rice dry. Smithsonian magazine adds that the cycle keeps artisan skills alive by passing them between generations. I find the second reason the more convincing one. A building that is rebuilt every generation is a building whose builders never forget how.</p>
    <p>For visitors, the practical point is that the sanctuary itself is closed to ordinary worshippers. World History Encyclopedia says only senior priests and the emperor may enter the inner part. What you can see are the outer fences, the paths and the shinmei-style buildings of the subsidiary shrines.</p>
    {ph('ise')}

    <h2 id="izumo">Izumo: The Tallest Hall<span class="h2-jp">出雲大社の本殿</span></h2>
    <p>If Ise is about renewal, Izumo is about scale. The Ministry of Land, Infrastructure, Transport and Tourism database says the main hall was last rebuilt in 1744, stands 24 meters high and is the tallest shrine building in Japan. It was designated a National Treasure in 1952. The building has nine pillars in a three-by-three grid, with the thickest, the <em>shin no mihashira</em>, at the center, and its hinoki-bark roof carries chigi measuring over 7 meters. Web Japan gives the floor as roughly 11 meters on each side.</p>
    <p>The ancient version was said to be taller. The Encyclopedia of Shinto notes that Heian-period records give a height of 16 <em>jo</em>, about 48 meters, but it calls reconstruction drawings of that scale somewhat unrealistic. I would treat 48 meters as a legend with some archaeology behind it, not a measurement.</p>
    <p>Japan Guide says that until 1744 Izumo was periodically rebuilt like Ise, and that since then the tradition has been only partly kept, with major renovations about every 60 years instead. The most recent began in 2008 and was mostly complete in spring 2013, when the roof was replaced and the deity returned. For the story behind the building, see our {link('/guides/izumo-taisha/','Izumo Taisha guide','arch_to_izumo2')} and our {link('/culture/japanese-mythology/','Japanese mythology guide','arch_to_mythology')}.</p>
    {ph('izumo')}

    <h2 id="craft">How Shrines Are Built<span class="h2-jp">宮大工と木組み</span></h2>
    <p>Shrines are built of wood, and World History Encyclopedia says the preferred wood is hinoki, Japanese cypress, left plain or painted. Roofs vary. At Ise the roof is thatch; at Izumo it is thick layers of hinoki bark. The Agency for Cultural Affairs lists thatching and roofing with cypress bark and wooden shingles among the traditional skills needed to conserve heritage buildings, which is a good reminder that these roofs are crafts, not just materials.</p>
    <p>The people who build and repair them are <em>miyadaiku</em>, shrine and temple carpenters. The Web Japan feature on them says that one of their most important techniques is <em>kigumi</em>, joining wood without nails or metal fittings, and that it takes over ten years to become a full-fledged miyadaiku. The Embassy of Japan in Singapore notes that UNESCO designated Japan's traditional skills and knowledge for wooden architecture, including wooden joinery, as Intangible Cultural Heritage in 2020.</p>
    <p>One explanation of why they avoid metal in the framing, from a Live Japan feature, is that nails and fasteners rust in Japan's rain and humidity and make the wood rot, so a joint that holds by shape is easier to repair for a thousand years. I give that as one account, not a rule. As I said in the Ise section, metal is not absent from shrines. It appears as hardware and as copper wrapping, so the accurate version is that the frame is joined without nails, not that nothing metal is used.</p>
    {ph('craft')}

    <div class="key-callout" style="background:#fff8e6;border-left:4px solid var(--kin);padding:16px 20px;margin:28px 0;border-radius:2px;">
      <p style="margin:0;">&#127754; <strong>Plan your trip:</strong> Browse guided shrine tours in Japan, or find a stay near the shrines in this guide. <a href="{VI}" target="_blank" rel="noopener sponsored" onclick="trackEvent('click','affiliate','viator_shrine_architecture')">Book a Tour →</a> &nbsp;|&nbsp; <a href="{EX}" target="_blank" rel="noopener sponsored" onclick="trackEvent('click','affiliate','expedia_shrine_architecture')">Find Hotels →</a></p>
    </div>

    <h2 id="visit">How to Read a Shrine When You Visit<span class="h2-jp">鑑賞のコツ</span></h2>
    <p>Here is the five-step routine I use with groups. You can do it in a minute at any shrine.</p>
    <ol>
      <li><strong>Look up at the roof first.</strong> Do you see chigi and katsuogi? If so, you are at an orthodox, older-style hall. Count the logs, and notice how the chigi tips are cut.</li>
      <li><strong>Find the entrance.</strong> Is it on the long side or the gable end? That one question separates the shinmei and nagare family from the taisha, sumiyoshi and kasuga family.</li>
      <li><strong>Check for a front porch roof.</strong> A roof that sweeps forward over the whole width is the mark of nagare-zukuri, the most common style.</li>
      <li><strong>Walk around the side.</strong> The haiden hides the honden. From the side you can often see the second, smaller building behind it, and whether a heiden joins the two.</li>
      <li><strong>Ask what is made of plain wood and what is painted.</strong> Plain, planed wood points to the oldest tradition. Red paint, gilding and carving point to the later layers that borrowed from temples.</li>
    </ol>
    <p>Before you do any of this, remember the manners that come first: bow at the torii and rinse your hands. Our {link('/culture/shrine-etiquette/','shrine etiquette guide','arch_to_etiquette')} covers them, and our {link('/culture/what-is-shinto/','what is Shinto guide','arch_to_shinto')} explains the ideas behind the buildings.</p>

    <h2 id="faq">Frequently Asked Questions<span class="h2-jp">よくあるご質問</span></h2>

    <div class="faq-stack">

{faq_html}    </div>

    <h2 id="final">Final Thoughts<span class="h2-jp">むすびに</span></h2>
    <p>If you remember one thing, remember the roof. The crossed horns and the row of logs are the oldest signature of a Shinto building, and once you notice them you will find them everywhere, from the great halls to the smallest roadside shrine. From there the rest follows: where the door is, whether the roof sweeps forward, and whether the building is plain or painted.</p>
    <p>If you would like to see the extremes for yourself, start with the {link('/guides/ise-grand-shrine/','Ise Grand Shrine','arch_final_ise')} and the {link('/guides/izumo-taisha/','Izumo Taisha','arch_final_izumo')}. And if you are curious about the old theater stage that borrows a shrine's roof, our {link('/culture/noh/','noh guide','arch_final_noh')} shows how far that idea travelled.</p>

    <div class="closing-block">
      <span class="torii">&#127754;</span>
      <p>Two crossed beams, a row of logs and a door on the right side.</p>
    </div>

    <section class="related-section">
      <h2>Related Guides</h2>
      <span class="h2-jp">関連ガイド</span>
      <div class="related-grid">
        <a class="related-card" href="/guides/ise-grand-shrine/" onclick="trackEvent('click','internal','related_arch_to_ise')">
          <div class="related-card-label">SACRED JAPAN ／ GUIDE</div>
          <div class="related-card-title">&#9961;&#65039; Ise Grand Shrine →</div>
          <div class="related-card-desc">The shrine that is rebuilt every twenty years.</div>
        </a>
        <a class="related-card" href="/guides/izumo-taisha/" onclick="trackEvent('click','internal','related_arch_to_izumo')">
          <div class="related-card-label">SACRED JAPAN ／ GUIDE</div>
          <div class="related-card-title">&#9961;&#65039; Izumo Taisha →</div>
          <div class="related-card-desc">The tallest shrine hall in Japan.</div>
        </a>
        <a class="related-card" href="/culture/shrine-etiquette/" onclick="trackEvent('click','internal','related_arch_to_etiquette')">
          <div class="related-card-label">SACRED JAPAN ／ GUIDE</div>
          <div class="related-card-title">&#128591; Shrine Etiquette →</div>
          <div class="related-card-desc">How to bow, rinse and pray before you look up.</div>
        </a>
        <a class="related-card" href="/culture/shrine-vs-temple/" onclick="trackEvent('click','internal','related_arch_to_shrinetemple')">
          <div class="related-card-label">SACRED JAPAN ／ GUIDE</div>
          <div class="related-card-title">&#9961;&#65039; Shrine vs Temple →</div>
          <div class="related-card-desc">How to tell the two apart at the gate.</div>
        </a>
      </div>
    </section>

    <p style="font-size:14px;color:var(--enshu);line-height:1.7;margin-top:32px;"><strong>Sources:</strong> {ext(KOK,'Encyclopedia of Shinto: History and Typology of Shrine Architecture','arch_src_kok')} (styles, examples); {ext(KOKS,'Encyclopedia of Shinto: Shikinen Sengu','arch_src_koks')} (Ise dates and materials); {ext(NIP,'Nippon.com: Honden','arch_src_nippon')} (granary and house models, chigi and katsuogi rule, shrines without a honden); {ext(NIPS,'Nippon.com: Virtual Guide to the Shinto Shrine','arch_src_nippon2')}; {ext(WHE,'World History Encyclopedia: Shinto Architecture','arch_src_whe')} (layout, hinoki); {ext(WIKI,'Wikipedia: Shinto architecture','arch_src_wiki')} and {ext(WIKIH,'Honden','arch_src_wikih')}; {ext(MLIT,'MLIT multilingual database: Izumo honden','arch_src_mlit')}; {ext(JGIZ,'Japan Guide: Izumo Taisha','arch_src_jgiz')}; {ext(WJA,'Web Japan: Izumo Taisha','arch_src_wja')}; {ext(NG,'National Geographic','arch_src_ng')}, {ext(WTOP,'AP via WTOP','arch_src_wtop')}, {ext(WEF,'World Economic Forum','arch_src_wef')}, {ext(TW,'Tokyo Weekender','arch_src_tw')}, {ext(ISEK,'Ise City tourism','arch_src_isek')}, {ext(JFS,'Japan for Sustainability','arch_src_jfs')} and {ext(SMITH,'Smithsonian','arch_src_smith')} (Ise rebuilding); {ext(NIPONICA,'Web Japan: Miyadaiku','arch_src_niponica')}, {ext(EMB,'Embassy of Japan in Singapore','arch_src_emb')}, {ext(LJ,'Live Japan','arch_src_lj')} and {ext(BUNKA,'Agency for Cultural Affairs','arch_src_bunka')} (carpentry and roofing); {ext('https://japanese-wiki-corpus.github.io/building/Jingu%20Shikinen%20Sengu.html','Jingu Shikinen Sengu (English translation of the Japanese entry)','arch_src_jwc')} (why the buildings need renewing).</p>

  </article>

</main>"""

t=open(f'{R}/_tools/culture/tea.py',encoding='utf-8').read()
tail=t[t.index("s=open(f'{R}/culture/omamori-guide"):]
tail=tail.replace('<div class="hero-bg-kanji">茶道</div>','<div class="hero-bg-kanji">社殿</div>')
tail=tail.replace('<h1>The Japanese <em>Tea Ceremony</em> Guide</h1>','<h1>Shinto Shrine <em>Architecture</em> Guide</h1>')
tail=tail.replace('<div class="hero-jp">茶道ガイド</div>','<div class="hero-jp">神社建築ガイド</div>')
tail=tail.replace('What Happens, What to Do as a Guest, and Where to Try It','Styles, Roofs, Parts and How Shrines Are Built')
tail=tail.replace('Tea Ceremony Guide','Shrine Architecture Guide')
tail=tail.replace('guide_tea','guide_arch').replace('viator_guide_tea_sticky','viator_guide_arch_sticky').replace('japanese+tea+ceremony','japan+shrine+tour')
tail=re.sub(r'(<meta name="keywords" content=")[^"]*(")',r'\1Shinto shrine architecture, shrine styles, shinmei-zukuri, taisha-zukuri, nagare-zukuri, chigi katsuogi, honden haiden, torii, Ise shikinen sengu, Izumo Taisha honden\2',tail)
tail=tail.replace('"datePublished":"2026-11-08","dateModified":"2026-11-08"','"datePublished":"2026-11-23","dateModified":"2026-11-23"')
exec(tail)
