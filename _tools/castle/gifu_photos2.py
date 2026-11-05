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

put("the ride gives a view over Gifu and the Nagara River.</p>",
 blk('ropeway','f3a0487d-image.jpg','Hyppolyte de Saint-Rambert','B4','A ropeway cabin hanging from cables above a steep hillside of fresh green forest, with a pale sky behind','A Mt. Kinka Ropeway cabin over the forested slope, 15 May 2025.',
  para="Commons labels this only &ldquo;au parc de Gifu&rdquo; (&ldquo;at Gifu Park&rdquo;), and I take the cabin to be on the Mt. Kinka Ropeway, which starts there. The sign on its front appears to read as a 70th-anniversary message, and a small butterfly decoration with the kanji for Kicho sits on the pole above it; both are my reading of the picture and not something Commons states. What the photo does show well is the slope itself: steep, wooded and in fresh spring green, so the four-minute ride is a climb through forest before it is a view."))
put("a day with no view.</p>",
 blk('residence-gate','a80d5932-image.jpg','\u305d\u3089\u307f\u307f (Soramimi)','S3','A wooden gate with two square posts and one open door leaf, with a stone staircase climbing into bare winter trees, and a tall stone marker at the right','The gate at the ruins of Nobunaga\u2019s residence in Gifu Park, 5 February 2014.',
  para="Commons titles this Gifu Park, the site of the Oda Nobunaga residence, and the tall stone marker on the right reads as exactly that in Japanese. A plain timber gate frame stands at the foot of a stone staircase that climbs the slope. It is a modern marker of the place and not an original gate, and I do not know what stands at the top of the steps, so I do not describe it. The photo was taken on a winter afternoon in 2014, when the trees were bare, and the layout of the park may have changed since.")+
 blk('nobunaga-garden','3fe153a5-image.jpg','\u305d\u3089\u307f\u307f (Soramimi)','S3','A still pond in a Japanese garden with stone lanterns, an arched bridge, mossy rocks and a stepping-stone path, among bare winter trees','The garden in Gifu Park labelled &ldquo;Nobunaga\u2019s garden&rdquo;, 5 February 2014.',
  para="Commons labels this &ldquo;Gifu Park, Nobunaga&rsquo;s garden&rdquo; and dates it to the same afternoon as the gate, a few minutes earlier. A dark pond holds two small islets, one with what looks like a stone frog and another with a turtle, and an arched bridge and two stone lanterns sit among moss and bare trees. I cannot say how much of this is original to Nobunaga&rsquo;s time and how much is a later garden; I only know that the park is the place where his residence is thought to have stood. Treat it as a quiet, free corner for a rainy day, as the section above suggests."))
put("separately if you want to go.</p>",
 blk('ukai-boat','46a537cb-image.jpg','Ludger Heide','S4','A wooden boat at night with a blazing fire basket hanging from its bow, sparks streaming through the dark air, two men in dark clothing and cormorants swimming in the water','Cormorant fishing on the Nagara River, 7 July 2025.',
  para="Commons titles this &ldquo;Nagara River cormorant fishing&rdquo; and dates it 7 July 2025, shortly after eight in the evening. The blaze at the bow is the fire basket that lights the water so the fish can be seen; sparks stream back from it. One man poles the boat from the stern and the other, crouched near the fire, appears to be handling the cords that run out toward the birds, which is my reading of the picture. Two cormorants float in the foreground. The photo shows why people book a boat: the whole scene is lit by that one fire.")+
 blk('cormorant','9d7b23e8-image.jpg','yellow_bird_woodstock','S2','A close side view of a cormorant\u2019s head with a hooked black beak, a teal eye ringed with blue, yellow skin at the beak base, a white throat and white spiky feathers on the neck','A cormorant used in ukai, 1 May 2010.',
  para="Commons describes this as a cormorant of the ukai fishing, photographed in Gifu City, with the Latin name Phalacrocorax capillatus, dated 1 May 2010 in the afternoon. It is a daytime portrait and not taken on the river. The hooked tip of the beak is what catches the fish, the eye is a striking teal with a blue rim, and the bright yellow skin at the base of the bill and the white throat and neck feathers make the bird easy to recognise. It gives a face to the fishing described above."))
open(p,'w',encoding='utf-8').write(s)
with open(R+'PHOTO-CREDITS.csv','a',encoding='utf-8',newline='') as f: csv.writer(f,lineterminator='\r\n').writerows(rows)
print(len(rows))
for tg in ['div','figure','picture','p','a','ul','li','details','section','h2']:
    assert len(re.findall(f'<{tg}[ >]',s))==len(re.findall(f'</{tg}>',s)),tg
