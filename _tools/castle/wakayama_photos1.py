import re, csv, os
from PIL import Image
R='/home/claude/sacred-japan/'; A='/mnt/user-data/attachments/fd332c08-3f6b-545a-883b-83277e19ff52/'
SL='wakayama-castle'
L={'S3':('CC BY-SA 3.0','https://creativecommons.org/licenses/by-sa/3.0/'),'S25':('CC BY-SA 2.5','https://creativecommons.org/licenses/by-sa/2.5/'),'S4':('CC BY-SA 4.0','https://creativecommons.org/licenses/by-sa/4.0/'),'B4':('CC BY 4.0','https://creativecommons.org/licenses/by/4.0/'),'B2':('CC BY 2.0','https://creativecommons.org/licenses/by/2.0/'),'CC0':('CC0 1.0','https://creativecommons.org/publicdomain/zero/1.0/'),'PD':('Public Domain','https://commons.wikimedia.org/wiki/Template:PD-self')}
rows=[]
def mk(k,f,au,lic,alt,cap,hero=False,maxw=760):
    im=Image.open(A+f+'-image.jpg').convert('RGB')
    if im.width>1200: im=im.resize((1200,round(im.height*1200/im.width)),Image.LANCZOS)
    D=R+f'guides/{SL}/images/'; os.makedirs(D,exist_ok=True)
    im.save(D+k+'.jpg',quality=84,optimize=True); im.save(D+k+'.webp',quality=80)
    l=L[lic]
    rows.append([f'guides/{SL}',f'/guides/{SL}/images/{k}.jpg',l[0],l[1],l[1],f'{cap} Photo: {au}, {l[0]}, via Wikimedia Commons (resized)'])
    fs='margin:0 0 48px;' if hero else f'margin:28px auto;max-width:{maxw}px;'
    ld='eager' if hero else 'lazy'
    ex='max-height:420px;object-fit:cover;' if hero else ''
    return (f'<figure style="{fs}"><picture><source srcset="/guides/{SL}/images/{k}.webp" type="image/webp"><img src="/guides/{SL}/images/{k}.jpg" alt="{alt}" width="{im.width}" height="{im.height}" loading="{ld}" style="width:100%;height:auto;border-radius:4px;display:block;{ex}"></picture>'
            f'<figcaption style="font-size:13px;color:var(--enshu);margin-top:10px;text-align:center;line-height:1.6;">{cap}<br>Photo: {au}, <a href="{l[1]}" target="_blank" rel="noopener" style="color:var(--enshu);">{l[0]}</a>, via Wikimedia Commons (resized)</figcaption></figure>')
def blk(*a,para,maxw=760): return '\n    '+mk(*a,maxw=maxw)+f'\n    <p>{para}</p>'
p=R+f'guides/{SL}/index.html'; s=open(p,encoding='utf-8').read()
def put(anchor,html,before=False):
    global s
    assert s.count(anchor)==1,anchor
    s=s.replace(anchor,(html+anchor) if before else (anchor+html))

LIB=''
hero=mk('hero-keep-bridge','985d6493','Saigen Jiro','CC0','A white keep on a wooded hill above a moat, with a long wooden roofed bridge sloping across the water in front','The keep above the slanted roofed bridge, 14 November 2018 (Commons: keep and roofed bridge corridor).',hero=True)
put("  <!-- TABLE OF CONTENTS -->",hero+"\n\n",before=True)
put("so I would just say it was begun in 1585 under Hideyoshi&rsquo;s orders.</p>",
 blk('keep-below-fg2','d50283ea','Fg2','PD','A white keep with green copper roof ornaments seen from below against a deep blue sky, with red autumn leaves at the lower right','The keep seen from below, 26 November 2005.',
  para="This is the keep as you meet it when you climb: white plaster walls under stacked roofs, each with a small gable, and dull green ornaments on the ridges. The outline is that of a castle built to be seen from the town. The photo is from 26 November 2005, and the photographer has placed it in the public domain."))
put("I found that height in one source only.</p>",
 blk('aerial-city','fd8583cb','Saigen Jiro','CC0','A wide view over a park with a moat, a long roofed wooden bridge and a hill crowned by a white keep, with mountains behind','The castle hill from a high building, 14 November 2018 (Commons: view from Wakayama City Hall).',
  para="Commons says this view was taken from Wakayama City Hall. It shows the point of the hill well: the keep and its long white walls sit on a small rise, with the moat and the roofed bridge in front and mountains on the horizon. The hill is modest, but it dominates the flat ground around it. Some autumn colour is starting in the trees."))
put("only the Okaguchi Gate and the stone walls survive from the original castle (one source only).</p>",
 blk('keep-summer','c1ad84fa','Suicasmo','S4','A white keep with green roof ornaments rising above bright green trees against a pale blue sky','The keep in summer, 24 July 2021 (Commons: Wakayama Castle Keep Tower).',
  para="Here the keep is set in summer foliage, photographed on 24 July 2021. A smaller tower stands to its right. The thick trees hide the stone base, so the keep seems to float above the green. It is a good reminder that this is a postwar replica on an old hill, in a park.")+
 blk('entrance','91cdab27'.replace('91cdab27','79533d09'),'Motokoka','S4','The entrance side of a white castle keep complex with curved green-trimmed gables, a gravel path and clipped pines in front','The entrance side of the keep complex, 13 June 2009.',
  para="Commons titles this only as Wakayama Castle, so I am reading what I see: the front of the keep complex, with a smaller tower to the left joined to the main keep, a curved gable over the doorway and a gravel path lined with clipped shrubs. It shows the linked layout that GLTJP describes, where the main keep and a smaller tower are connected. Photographed on 13 June 2009."))
put("japan-guide says the top floor has an observation deck over the city.</p>",
 blk('keep-lookup','7f1abf62','Hyppolyte de Saint-Rambert','S4','A white keep with layered tiled roofs seen steeply from below against a clear blue sky, with bare branches at the edge','The keep from directly below, 23 February 2020 (Commons: low-angle view of the keep).',
  para="Commons describes this as a low-angle view of the keep from 23 February 2020. The camera looks almost straight up the white wall, past a drum-shaped bulge at one corner, to the stacked gables and the green ornaments. In February the trees are bare, so nothing hides the structure.")+
 blk('keep-honmaru','9ae3f0e3','Saigen Jiro','CC0','A white keep with green roof ornaments rising behind a stone wall and trees against a blue sky','The keep seen from the site of the Honmaru Palace, 23 November 2018.',
  para="Commons says the photographer stood at the site of the Honmaru Palace (本丸御殿跡) on 23 November 2018. The palace is gone, and what remains is open ground with a view up to the keep and its neighbouring tower. The leaves nearby are starting to turn.")+
 blk('roofs-inui','8ffe29a3','KENPEI','S25','A tiled gabled turret roof seen from above, with white plaster walls, red autumn leaves below and the city behind','The Inui Turret (乾櫓), 23 November 2008.',
  para="Commons names this the Inui Turret (乾櫓), photographed on 23 November 2008 from a high point. You see the layered grey roofs, the white plaster beneath and a bright patch of autumn leaves in the foreground, with the modern city behind. The old roof tiles and the town together give a sense of how close the castle sits to the streets.")+
 blk('roofs-ninomon','47192071','KENPEI','S25','Tiered tiled roofs and gables of a castle building seen from above, with autumn trees and city buildings beyond','The Ninomon Gate turret (二の門櫓門), 23 November 2008.',
  para="Commons labels this the turret over the Ninomon Gate (二の門櫓門), photographed on the same day. It is an upright picture of stepped tile roofs with small gables, looking down on the town. It is a useful picture for the detail in the roof tiles, with their rounded ends, which are hard to see from the ground.",maxw=420))
put("you can cross it freely.</p>",
 blk('bridge-portrait','22cc1e46','663highland','S3','A long wooden roofed bridge sloping across a moat with a white keep high on the hill behind, among yellow-green autumn trees','The slanted bridge below the keep, 4 December 2008 (Commons: Wakayama Castle).',
  para="Commons titles this only as Wakayama Castle. It shows the sloping roofed bridge crossing the moat, with the keep high above. The bridge climbs from left to right, which is what you cross on foot; it is built on a slope, so it does not run level. The yellow of the trees suggests early December. The bridge was restored in 2006, and this photo was taken two years later.",maxw=420))
put("you will start to spot them.</p>",
 blk('wall-road','91cdab27','Motokoka','S4','A wide paved stone road running beside a high rough stone wall under pine trees','A paved approach beside a high stone wall, 13 June 2009.',
  para="This is a wide, paved path beside a high rough stone wall, photographed on 13 June 2009. Commons gives only the castle name, so I do not know which part of the grounds it is. It is a good example of the walls that line the approach, built from uneven stones in rough courses.")+
 blk('steps-663','df76f8ab','663highland','S3','A stone path and steps climbing past moss-covered stone walls, with two visitors at the top and a labelled tree','A stone path and steps under the walls, 4 December 2008 (Commons: Wakayama Castle).',
  para="A rough stone path climbs beside mossy walls, with two visitors at the top. A small label on a tree reads ヒノキ (hinoki, cypress). The stones are of different sizes and shapes, which is the look of the walls I mention above. Commons does not say where in the grounds this is.")+
 blk('okaguchi-gate','a02c55c1','Suikotei','B4','A dark wooden gate with a white upper storey, in front of a rough stone wall and pine trees, with an information board at the right','The Okaguchi Gate (岡口門), 16 August 2025.',
  para="Commons names this the Okaguchi Gate (岡口門), photographed on 16 August 2025. This is the gate that Japan Experience says survives from the original castle, and I found that in one source only. The white upper storey with slatted windows sits on a heavy dark wooden gate, and a large rough stone wall stands beside it. The information board at the right gives the castle map.")+
 blk('oimawari-gate','a9c0234f','kouko0515','PD','A red-painted wooden gate between two stone walls, seen from the front on a gravel path','The Oimawari Gate (追廻門), 5 October 2007.',
  para="Commons names this the Oimawari Gate (追廻門), photographed on 5 October 2007. It is a red-painted gate set between stone walls. I have not confirmed its history, so I treat it as a gate you may pass, not as an original. This is a small picture (640 by 480 pixels), and I have kept it at its original size."))
put("Entry is free (GLTJP, japan-guide).</p>",
 blk('garden-pavilion-663','c43754ec','663highland','S3','A small hexagonal-roofed pavilion over a still pond, with red maple leaves and green trees reflected in the water','The pavilion over the pond, autumn colour, 4 December 2008.',
  para="I read this as the pond in the Nishinomaru Garden, since Commons labels several of this photographer's files that day with the garden's name. A small pavilion stands over still water, and the maples on the left have turned deep red, doubled in the reflection. The date is 4 December 2008, which is within the late-November to early-December window GLTJP suggests.")+
 blk('garden-pavilion-saigen','c3b07622','Saigen Jiro','CC0','A pavilion beside a pond with bright red and orange maple trees, pines and visitors on the far bank','The pond and pavilion in full colour, 23 November 2018 (Commons: distant view of the garden).',
  para="Commons calls this a distant view of the autumn-leaf garden (紅葉渓庭園 遠景), from 23 November 2018. The same pavilion appears, but now the maples are red, orange and pink, with pines in between and a few visitors on the far path. The colour is more advanced than in the earlier photo, even though it was taken earlier in the month, so it is worth knowing that timing varies by year.")+
 blk('garden-bridge-kenpei','9c43cff5','KENPEI','S3','A small arched wooden bridge above a pond of still water with rocks, with maple and pine trees around it','The pond and arched bridge in the garden, 23 November 2008 (Commons: Momijidani garden).',
  para="Commons labels this the garden's Momijidani (紅葉渓庭園), 23 November 2008. A small arched wooden bridge crosses above a pond full of rocks, and a few walkers cross it. The leaves are only starting to change, which gives a calmer, greener view than the other pictures. A small signpost stands in the pond.")+
 blk('garden-gate-663','239e72f1','663highland','S3','A thatched, moss-covered garden gate framing a stone-stepped path and bright autumn maples beyond, with a stone marker and notice boards','The thatched gate to the garden, 4 December 2008.',
  para="This is the entrance gate to the garden, as I read the stone marker beside it: 名勝 和歌山城西の丸庭園 (紅葉渓庭園), a Place of Scenic Beauty. The moss-covered thatched roof frames a path of stepping stones that leads to bright maples. The notice boards at the left are in Japanese, and Commons gives the date as 4 December 2008."))
put("It recommends late November to early December for the autumn leaves.</p>",
 blk('cherry-view','5c88da58','jmurawski','B2','Cherry trees in full bloom between castle roofs, with a keep tower and the city and river beyond in haze','Cherry trees below the keep, with the city beyond (Commons: skyline viewed from the castle; uploaded to Flickr on 8 April 2007).',
  para="Commons says this is the skyline of Wakayama viewed from the castle, uploaded to Flickr on 8 April 2007 (the date is the upload date and not necessarily the photo date). Cherry trees in full bloom fill the court between the tiled roofs of the buildings, and a tower of the castle rises behind them, with the city and the river in the haze. It gives a good idea of how the blossom sits within the castle, not just around it."))
open(p,'w',encoding='utf-8').write(s)
with open(R+'PHOTO-CREDITS.csv','a',encoding='utf-8',newline='') as f: csv.writer(f,lineterminator='\r\n').writerows(rows)
print(len(rows))
for tg in ['div','figure','picture','p','a','ul','li','details','section','h2']:
    assert len(re.findall(f'<{tg}[ >]',s))==len(re.findall(f'</{tg}>',s)),tg
