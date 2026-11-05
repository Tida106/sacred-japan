import re, csv, os
from PIL import Image
R='/home/claude/sacred-japan/'; A='/mnt/user-data/attachments/fd332c08-3f6b-545a-883b-83277e19ff52/'
SL='matsumoto-castle'
L={'S2':('CC BY-SA 2.0','https://creativecommons.org/licenses/by-sa/2.0/'),'S4':('CC BY-SA 4.0','https://creativecommons.org/licenses/by-sa/4.0/'),'B3':('CC BY 3.0','https://creativecommons.org/licenses/by/3.0/'),'B4':('CC BY 4.0','https://creativecommons.org/licenses/by/4.0/'),'S3':('CC BY-SA 3.0','https://creativecommons.org/licenses/by-sa/3.0/'),'B2':('CC BY 2.0','https://creativecommons.org/licenses/by/2.0/'),'C0':('CC0 1.0','https://creativecommons.org/publicdomain/zero/1.0/')}
rows=[]
def blk(k,f,au,lic,alt,cap,para,maxw=760):
    im=Image.open(A+f+'-image.jpg').convert('RGB')
    if im.width>1200: im=im.resize((1200,round(im.height*1200/im.width)),Image.LANCZOS)
    D=R+f'guides/{SL}/images/'; os.makedirs(D,exist_ok=True)
    im.save(D+k+'.jpg',quality=84,optimize=True); im.save(D+k+'.webp',quality=80)
    l=L[lic]
    rows.append([f'guides/{SL}',f'/guides/{SL}/images/{k}.jpg',l[0],l[1],l[1],f'{cap} Photo: {au}, {l[0]}, via Wikimedia Commons (resized)'])
    return (f'\n    <figure style="margin:28px auto;max-width:{maxw}px;"><picture><source srcset="/guides/{SL}/images/{k}.webp" type="image/webp"><img src="/guides/{SL}/images/{k}.jpg" alt="{alt}" width="{im.width}" height="{im.height}" loading="lazy" style="width:100%;height:auto;border-radius:4px;display:block;"></picture>'
            f'<figcaption style="font-size:13px;color:var(--enshu);margin-top:10px;text-align:center;line-height:1.6;">{cap}<br>Photo: {au}, <a href="{l[1]}" target="_blank" rel="noopener" style="color:var(--enshu);">{l[0]}</a>, via Wikimedia Commons (resized)</figcaption></figure>\n    <p>{para}</p>')
p=R+f'guides/{SL}/index.html'; s=open(p,encoding='utf-8').read()
def put(anchor,html):
    global s
    assert s.count(anchor)==1,anchor
    s=s.replace(anchor,anchor+html)


def before(anchor,html):
    global s
    assert s.count(anchor)==1,anchor
    s=s.replace(anchor,html+'\n\n    '+anchor)

keep=blk('bridge-aerial','27ad2ec0','Zairon','S4','A high view of a red zigzag bridge over a green moat beside a stone wall, with cherry trees and a park beyond','The red bridge and the moat seen from above, 7 April 2019 (Commons: View from Matsumoto Castle to the Bridge).',
 "This is the view that makes the steep stairs worth it. The Commons title says it looks from the castle toward the bridge, and from up here the red bridge zigzags across the green moat while the park spreads out behind it, with pale cherry trees in early April. The roof ornament in the lower right corner shows how high the vantage point is. On a grey day the moat will not look this bright.")
keep+=blk('bridge-ledgard','638aa292','Bryan Ledgard','B2','A red lacquered bridge with a round post in the foreground leading toward the black keep across the moat under a blue sky','Approaching the keep over the red bridge, 19 October 2011.',
 "The red bridge is the classic approach, and it is a good place to read how the keep is arranged: the large main keep at the back, a smaller keep beside it, and the stone base rising from the water. This photo is from October 2011, so small details around the castle may have changed since.")
keep+=blk('bridge-pundit','85c86550','Dariusz Jemielniak (&ldquo;Pundit&rdquo;)','S3','The black keep with white gables seen over a red bridge under a bright blue sky with a few clouds','The keep from the red bridge on a clear day, July 2014.',
 "A clear summer day gives the strongest contrast. The black siding looks almost wet against the sky, the white gables stand out and the red railing frames it all. Look at the roofline: the gables are layered, which makes the keep look bigger than it is. Commons gives 18 July 2014 as the date taken, so I mention only the month and year.")
keep+=blk('bridge-moat','783aa548','Raki_Man','B3','A long red bridge across a green moat with the dark keep behind it under a cloudy sky','The red bridge across the moat on an overcast day, 26 June 2016.',
 "Even on an overcast day in June, the castle still works. The red of the bridge is reflected in the dark moat and the keep looks heavier and moodier than in sunshine. If the forecast is grey, I would still go: the interior stays the same, and the crowds are often thinner.")
before('<h2 id="moon">',keep)

# --- new night/blossom section
night=('<h2 id="night">Cherry Blossoms, Blue Hour and the Night Light-Up<span class="h2-jp">夜桜・夜景</span></h2>\n    <p>The castle changes a lot after the sun goes down, and these photos are why I tell guests to plan an evening here if they can. Opening hours and any special lighting change from year to year, so check the official site before you go.</p>')
night+=blk('spring-cloud','eaf708e1','Oren Rozen','S4','The black keep behind a red bridge on a cloudy day with pale cherry blossoms along the moat','Cherry blossoms beside the moat on a cloudy day, 13 April 2016.',
 "Early to mid April is when the blossoms come out around the moat. On a cloudy day like this the petals look soft and the black walls of the keep show up well behind them. The photo is from 2016, and the timing shifts each year with the weather.")
night+=blk('blue-hour','cf7f6121','Oren Rozen','S4','The keep and a red bridge in blue evening light, with pink cherry blossoms beside the moat','Blue hour at the castle, 12 April 2016 (Commons: Blue hour at Matsumoto Castle).',
 "The same week, in the blue light just after sunset. The sky and the moat turn the same cool colour, the red bridge glows, and the cherry blossoms start to pick up the lighting. If you only have one evening, this is the moment I would aim for, about half an hour after sunset.")
night+=blk('night-suicasmo','19932171','Suicasmo','S4','The white-lit keep and its small keep against a black night sky, with pale cherry trees on the left and a still moat below','The keep floodlit at night, 3 February 2017 (Commons: Matsumoto Castle Keep Tower).',
 "In winter the keep is lit against a black sky, and the bare trees on the left look like frost. The strong white light picks out each tier of the roof, so you can count the layers. This is a long exposure, and in person your eyes will not see quite so much detail.")
night+=blk('night-zairon','8c5a459e','Zairon','S4','The floodlit keep at night reflected in a dark moat, with a green glow in the water at the bottom','The keep at night with its reflection in the moat, 6 April 2019.',
 "From the same spring as the daytime photo above, this is the reflection shot visitors line up for. The water is calm enough to mirror the whole keep. A green tint in the lower part of the water appears to be light reflected in the moat, though the Commons description does not say where it comes from.",maxw=480)
night+=blk('night-chan-left','fde342cf','Andrew Chan','B2','The keep at night under a violet sky, with its green stone base lit and reflected in the water','The keep at night, 24 November 2010 (Commons: Matsumoto Castle at night &ndash; left).',
 "A November night, in a very different mood. The violet sky and the green stone base are partly a result of long exposure and the camera's colour treatment, so treat the colours as artistic, not literal. It does show the broad shape of the keep and the Inui keep next to it.")
night+=blk('night-chan-tall','038d00a0','Andrew Chan','B2','A tall view of the keep at night under a purple sky with a bright moon above, and its reflection below','The same evening in a tall frame, 24 November 2010 (Commons: Matsumoto Castle at night &ndash; tall).',
 "A second frame from the same evening, this time with the moon above the roof. It is a useful reminder of how the castle has been used for moon viewing, though the moon here is probably exaggerated by the long exposure.",maxw=420)
night+=blk('night-kikuchi-blue','acdbe628','Hiroaki Kikuchi','B4','The keep at night under a deep blue starry sky with a perfect reflection in the black moat','The keep in deep blue light with its reflection, 25 January 2026.',
 "This is the more recent version of the reflection shot, taken in January 2026 on a clear night. The Commons record notes that the image was selected as a picture of the month on the Japanese Wikipedia. The photographer took it during the winter projection-mapping period, which I describe below.",maxw=420)
night+=blk('taiko-gate','3c20f1d6','Zairon','S4','A lit wooden gate with a white upper wall and tiled roof at night, with trees on both sides','The Taiko Gate at night, 6 April 2019 (Commons: Taiko Gate of Matsumoto Castle at Night).',
 "The Taiko Gate is the entrance to the main part of the castle, where the ticket line forms. At night the white wall and the glow from the opening make it look like a theatre set. The ticket office and entry rules change, so treat this as scenery, not as a guide to the current route.")
night+=blk('projection-kikuchi','c280eb9f','Hiroaki Kikuchi','C0','The keep at night lit in blue, orange and green projected colour, with its reflection in the moat','Projection mapping on the keep, 25 January 2026.',
 "Recently the castle has been used for projection mapping. The Commons description says this was the 2025&ndash;2026 projection-mapping event on the National Treasure keep, held from 13 December 2025 to 15 February 2026, and that this photo was taken at the start of the show on 25 January 2026. I mention the dates so you can see that it was a limited event, and I would not assume it runs every winter.",maxw=420)
night+=blk('projection-futo','ff5c59ec','Raita Futo','B2','The keep and the stone base lit in bands of colour at night, with the colours reflected in the moat','A colourful light-up of the keep, 4 February 2024 (Commons: Matsumoto Castle Light-up).',
 "An earlier light-up, from February 2024, shows that this kind of show is not new. The colour covers both the keep and its stone base, and the moat doubles it. The Commons record gives a source titled &ldquo;Matsumoto Castle Light-up&rdquo;. Dates and times for any such event are announced by the city, so check the latest information before you plan around it.")
before('<h2 id="visit">',night)

# TOC + dateModified
a='<li><a href="#visit">Visiting Matsumoto Castle</a></li>'
assert s.count(a)==1
s=s.replace(a,'<li><a href="#night">Cherry Blossoms, Blue Hour and the Night Light-Up</a></li>\n      '+a)
assert s.count('"dateModified": "2026-11-01"')==1
s=s.replace('"dateModified": "2026-11-01"','"dateModified": "2026-11-05"')
open(p,'w',encoding='utf-8').write(s)
with open(R+'PHOTO-CREDITS.csv','a',encoding='utf-8',newline='') as fh: csv.writer(fh,lineterminator='\r\n').writerows(rows)
print(len(rows))
for tg in ['div','figure','picture','p','a','ul','li','details','section','h2']:
    assert len(re.findall(f'<{tg}[ >]',s))==len(re.findall(f'</{tg}>',s)),tg
import json
for m in re.finditer(r'<script type="application/ld\+json">(.*?)</script>',s,re.S): json.loads(m.group(1))
print('ok')
