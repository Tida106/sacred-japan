import re
import csv
from PIL import Image
R='/home/claude/sacred-japan/'; A='/mnt/user-data/attachments/53e3d492-4bf8-5cd9-a0ec-63a7cbefb1d9/'
SL='gifu-castle'
L={'S2':('CC BY-SA 2.0','https://creativecommons.org/licenses/by-sa/2.0/'),'S4':('CC BY-SA 4.0','https://creativecommons.org/licenses/by-sa/4.0/'),'B3':('CC BY 3.0','https://creativecommons.org/licenses/by/3.0/'),'B4':('CC BY 4.0','https://creativecommons.org/licenses/by/4.0/'),'S3':('CC BY-SA 3.0','https://creativecommons.org/licenses/by-sa/3.0/'),'B2':('CC BY 2.0','https://creativecommons.org/licenses/by/2.0/'),'C0':('CC0 1.0','https://creativecommons.org/publicdomain/zero/1.0/'),'PD':('Public Domain','https://commons.wikimedia.org/wiki/Template:PD-self')}
rows=[]
def mk(k,f,au,lic,alt,cap,hero=False,maxw=760):
    im=Image.open(A+f).convert('RGB')
    if im.width>1200: im=im.resize((1200,round(im.height*1200/im.width)),Image.LANCZOS)
    D=R+f'guides/{SL}/images/'
    import os; os.makedirs(D,exist_ok=True)
    im.save(D+k+'.jpg',quality=84,optimize=True); im.save(D+k+'.webp',quality=80)
    l=L[lic]
    rows.append([f'guides/{SL}',f'/guides/{SL}/images/{k}.jpg',l[0],l[1],l[1],f'{cap} Photo: {au}, {l[0]}, via Wikimedia Commons (resized)'])
    fs='margin:0 0 48px;' if hero else f'margin:28px auto;max-width:{maxw}px;'
    ld='eager' if hero else 'lazy'
    return (f'<figure style="{fs}"><picture><source srcset="/guides/{SL}/images/{k}.webp" type="image/webp"><img src="/guides/{SL}/images/{k}.jpg" alt="{alt}" width="{im.width}" height="{im.height}" loading="{ld}" style="width:100%;height:auto;border-radius:4px;display:block;"></picture>'
            f'<figcaption style="font-size:13px;color:var(--enshu);margin-top:10px;text-align:center;line-height:1.6;">{cap}<br>Photo: {au}, <a href="{l[1]}" target="_blank" rel="noopener" style="color:var(--enshu);">{l[0]}</a>, via Wikimedia Commons (resized)</figcaption></figure>')
def blk(*a,para,maxw=760,hero=False): return '\n    '+mk(*a,maxw=maxw)+f'\n    <p>{para}</p>'

p=R+f'guides/{SL}/index.html'; s=open(p,encoding='utf-8').read()
def put(anchor,html,before=False):
    global s
    assert s.count(anchor)==1,anchor
    s=s.replace(anchor,(html+anchor) if before else (anchor+html))
hero=mk('keep-winter','be1e1c3c-image.jpg','Drivephotographer','C0','A white three-tier keep with a black lower floor and gold ornaments on a stone base, with yellow banners along the stairs under a blue winter sky','The keep from the stairs below, 21 February 2021.',hero=True)
put("  <!-- TABLE OF CONTENTS -->",hero+"\n\n",before=True)
put("dating from the Warring States period.</p>",
 blk('keep-green','d7f3201c-image.jpg','Hyppolyte de Saint-Rambert','B4','The keep seen up a path between railings, with a tall yellow banner showing a black crest in the foreground and fresh green maple leaves above','The keep from the path below, 15 May 2025.',maxw=420,
  para="Commons labels this only &ldquo;au ch\u00e2teau de Gifu&rdquo; and dates it 15 May 2025. It shows the approach as I describe it: a stone-edged path with wooden railings climbs toward the keep, and tall yellow banners carrying a black crest line the way. I take the crest to be the Oda one, because the same crest is on the goshuin I mention below, but the Commons text does not say so. The fresh maple leaves explain the date, and in November the same trees are why the autumn color is worth the climb. This was taken when the keep was open, which it is not at the moment.")+
 blk('keep-closeup','aba0a1be-image.jpg','Hyppolyte de Saint-Rambert','B4','A close view of the upper floors of the keep, with white walls, grey tiled roofs, gold ornaments on the gable and an observation deck with a few visitors','The upper floors, 15 May 2025.',
  para="This is the same keep from closer in, taken on the same day. You can see the three roof levels, the gilded decoration on the central gable, the black-painted lower walls and, at the top, the observation deck with a few people looking out. That deck is the 360-degree viewpoint that is currently closed. Some of the gold looks worn in this picture, so treat the colors here as a snapshot of that day."))
put("the walls that are original.</p>",
 blk('keep-museum','01b2b7f5-image.jpg','Alpsdake','S3','The white keep on a wooded summit with a smaller white two-storey building with a tiled roof to its right, under a clear blue sky','The keep and the Gifu Castle Museum on the summit, 18 February 2012.',
  para="Commons describes this as Gifu Castle and the Gifu Castle Museum on top of Mount Kinka (the original description is in Japanese), taken on 18 February 2012. The smaller building to the right is therefore the museum, which GLTJP says sits on the east side of the grounds and was restored in 1975 in the style of a corner turret. The picture is from a distance in winter, when the bare trees show how small the buildings are on top of the mountain. Both buildings are closed at the moment according to my sources (see below)."))
put("view over Gifu and the Nagara River.</p>",
 blk('view','be12c029-image.jpg','Hyppolyte de Saint-Rambert','B4','A view from the keep along a grey tiled roof ridge to a wide river with a bridge, a sports ground and the city of Gifu, with hazy mountains behind','The view from the keep, 15 May 2025.',
  para="This was taken from the keep on 15 May 2025, and Commons labels it only as Gifu Castle. A roof ridge with its end tile points the way, and the wide river with a long bridge below is, by the geography, the Nagara, though the Commons text does not say so. Behind it lie the flat city, a sports complex and a line of hazy hills. It is the view you cannot have at present, because the keep is closed, so I include it to show what the reopening in November 2027 will bring back."))
put("as a lookout and not as the centerpiece. On rainy days, followingtheshogun suggests the lower slopes instead, because the summit steps get slippery.</p>" if False else "slippery.</p>",
 blk('tenka-gate','70b552ea-image.jpg','\u30d6\u30ec\u30a4\u30ba\u30de\u30f3 (Braizman)','PD','A wide wooden gate frame with two tall square posts and an open door leaf, with stone steps climbing between banners into green trees','The Tenka Daiichi-no-mon gate, 29 July 2008.',maxw=620,
  para="Commons names this the Tenka Daiichi-no-mon (&ldquo;First Gate Under Heaven&rdquo;) and labels it a restoration gate; the sign on the right carries the same name in English. GLTJP says a kabuki-style gate of this name, 4 m high and 5.5 m wide, was put up on Mount Kinka in 1990 and renovated in 2020. I take it to be the same gate, but this photo is from 2008, before that renovation, so it may look different now. Beyond it, stone steps climb between banners that carry the castle&rsquo;s name. A stone marker at the left appears to read as a commemorative gift from a local club, which is my reading and not something Commons states."))
put("a good alternative on a day with no view.</p>" if False else "a day with no view.</p>",
 blk('statue-pagoda','38038315-image.jpg','baggio4ever','B3','A bronze statue of a rider on a leaping horse raising a bow, beside a tiled roof corner, with a wooded mountain behind and a small castle on the summit and a red pagoda on the slope','A bronze rider with a bow, with the keep on the summit behind, 3 May 2013.',
  para="Commons titles this &ldquo;Gifu Castle, three-storey pagoda and statue&rdquo; and dates it 3 May 2013. In the foreground is a bronze rider on a leaping horse, one arm raised with a bow. Behind him the wooded slope of Mount Kinka rises, with a small red pagoda on the hillside and, on the summit at the top, the tiny white keep. I do not know who the statue depicts, because Commons does not say, so I leave it unnamed. The picture shows how high the keep sits above the town, which is the point of the whole climb."))
open(p,'w',encoding='utf-8').write(s)
with open(R+'PHOTO-CREDITS.csv','a',encoding='utf-8',newline='') as f: csv.writer(f,lineterminator='\r\n').writerows(rows)
print(len(rows))
for tg in ['div','figure','picture','p','a','ul','li','details','section','h2']:
    assert len(re.findall(f'<{tg}[ >]',s))==len(re.findall(f'</{tg}>',s)),tg
