import csv
from PIL import Image
R='/home/claude/sacred-japan/'; A='/mnt/user-data/attachments/53e3d492-4bf8-5cd9-a0ec-63a7cbefb1d9/'
SL='goryokaku'
L={'S2':('CC BY-SA 2.0','https://creativecommons.org/licenses/by-sa/2.0/'),'S4':('CC BY-SA 4.0','https://creativecommons.org/licenses/by-sa/4.0/'),'B3':('CC BY 3.0','https://creativecommons.org/licenses/by/3.0/'),'B4':('CC BY 4.0','https://creativecommons.org/licenses/by/4.0/'),'S3':('CC BY-SA 3.0','https://creativecommons.org/licenses/by-sa/3.0/')}
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
def put(anchor,html):
    global s
    assert s.count(anchor)==1,anchor
    s=s.replace(anchor,anchor+html)
GT='Goryokaku-Tower'; KY='掬茶 (Kikucha)'; H='663highland'
put("not only as a battlefield.</p>",
 blk('bugyosho','e580271d-image.jpg','ぽん吉 (Ponkichi)','B3','The reconstructed Magistrate\'s Office, a large wooden building with a brown tiled roof, a small turret on top and pine trees behind','The reconstructed Magistrate\'s Office, 10 August 2010.',
  para="Commons labels this the restored Hakodate Magistrate&rsquo;s Office and dates it 10 August 2010, the summer it reopened according to the sources above. It is a long, low wooden hall with a brown tiled roof, a decorated gable at the front and a small lookout turret on the ridge, with pines behind it. Visitors are sitting along the veranda and queuing at the entrance. Please remember that GLTJP describes it as a one-third reconstruction, so what you see is a partial rebuild of a much larger office."))
put("so this is the current tower&rsquo;s view.</p>",
 blk('tower-sakura','3b2c8726-image.jpg',GT,'B4','Goryokaku Tower rising behind a mass of pale pink cherry blossom, with people walking on the grass beneath the trees','Goryokaku Tower behind the blossom, 29 April 2018.',
  para="This is the tower as most visitors will first see it: a white shaft with a wide glass viewing deck, standing above the cherry trees. It is dated 29 April 2018, which fits the late-April start of the season mentioned below. Carp streamers hang from the tower, and walkers pass under the trees. It also shows how close the tower is to the park, so you can combine both in one visit.")+
 blk('tower-night','a12421df-image.jpg',KY,'S4','Goryokaku Tower lit white at night, rising above the dark roofs and lights of the town','Goryokaku Tower at night, 24 November 2024.',
  para="Commons describes this simply as the night view of Goryokaku Tower, and the time is 17:37 on 24 November 2024. The shaft is lit in pale green-white, and the glass deck glows at the top. It appears to be taken from a distance across the town with a long lens, so the tower looks closer than it is. If you would like to see it lit, late autumn already gives you an evening after about 17:00.")+
 blk('tower-window','3c97a283-image.jpg',H,'S3','A long row of slanted windows on the tower\'s observation floor, with a visitor at the railing and green parkland and the moat below','Looking down from the observation floor, 2012.',
  para="Commons lists this as a view of Goryokaku Tower from 2012 and gives the author as 663highland, but the date shown on my screenshot is the upload date, so I give only the year. The windows lean outward, and through them you can see the green park, a curve of the moat and the town stretching to hazy hills. A glass panel in the floor is visible at the bottom of the picture. The tower&rsquo;s decks are the easiest way to see the star shape as a whole, as described above.")+
 blk('tower-mural','82b4555b-image.jpg',H,'S3','A large circular display printed with a colourful woodblock-style scene of men in mixed Western and Japanese dress, with red name labels, in a bright lobby','A colourful circular wall display inside the tower, 2012.',
  para="This is a circular display covered in a colour print in the style of a woodblock scene, with red and white labels naming the figures, standing in a bright lobby while visitors queue to one side. I do not have the Commons description for it, so I cannot say what exactly it shows or which floor it is on, only that it is in the tower. It may well belong to the history exhibits that GLTJP mentions, but please treat that link as a guess."))
put("a claim I found in one source only.</p>",
 blk('moat-sakura','b5cbae83-image.jpg','Iso10970','S4','A wide moat with cherry trees in full bloom on both banks, a stone wall on the right and snow-streaked mountains in the distance','Cherry trees along the moat, 5 May 2017.',
  para="Commons describes this as the cherry blossoms at Goryokaku in Hakodate, dated 5 May 2017. Blossom lines both banks, the water is still, and a stone-faced bank juts into the moat on the right. Snow still lies on the mountains in the distance. The date shows that the trees can still be in bloom in early May, which is later than in much of Japan; the hero picture at the top is dated one day earlier."))
put("varies from year to year.</p>",
 blk('autumn-2019','077973e9-image.jpg','くろふね (Kurofune)','B4','The star-shaped fort seen from high above in autumn, with orange trees, a dark blue moat, the town and mountains under a deep blue sky','Goryokaku from above in autumn, 2 November 2019.',
  para="This one is dated 2 November 2019, at 15:14, and Commons gives the title simply as Goryokaku Park. The sky is a deep blue, the trees are orange and red, and the long shadow of the tower falls across the middle of the fort. I believe the shadow is the tower&rsquo;s, though Commons does not say so. The colours look strongly processed to me, so please treat them as brighter than what you will see."))
put("Please check the current schedule before you plan around it.</p>",
 blk('lights-color','0a4d9ba6-image.jpg','bryan…','S2','The star-shaped moat outlined in rows of warm white lights at night, with the town glowing in the distance','The star outlined in lights at dusk, 26 February 2015.',
  para="Commons tags this as Goryokaku Tower and Goryokaku, dated 26 February 2015 at 17:49, and the location is that of the tower, so I take it to be a view from the deck. Rows of warm white lights run along the edges of the star and some of the moat, while patches of snow remain on the earthworks and a lit roof glows green at the bottom left. It is a good picture of what the winter illumination looks like from above, but the light layout may well have changed since 2015.")+
 blk('lights-bw','9cdfbbee-image.jpg','bryan…','S2','A black-and-white view of the star-shaped moat outlined in rows of lights at night, with the town lights beyond','The same view in black and white.',
  para="The same photographer uploaded this black-and-white version of what appears to be the same scene, with the same date and time. Without the colour, the star is reduced to a clean white outline against the dark ground, which is the clearest way I have found to show the shape of the fort."))
put("which is lit after dark, so please do not read this daytime picture as a view of the lights.</p>",
 blk('winter-city','9c63a8c5-image.jpg',KY,'S4','A snowy town seen from a high floor, with the sea on the left and a mountain on the skyline under broken cloud','The town after snow, 24 December 2023.',
  para="Commons dates this to 24 December 2023 and says it is a winter view from Goryokaku Tower. Snow lies on the roofs and streets, the sea glitters on the left, and a mountain with antennas on its summit rises on the skyline. I believe that is Mount Hakodate, but Commons does not name it. It is a useful reminder that the tower&rsquo;s view takes in the town and the sea, not only the fort."))
open(p,'w',encoding='utf-8').write(s)
with open(R+'PHOTO-CREDITS.csv','a',encoding='utf-8',newline='') as f: csv.writer(f,lineterminator='\r\n').writerows(rows)
print(len(rows))
