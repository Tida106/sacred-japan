import csv
from PIL import Image
R='/home/claude/sacred-japan/'; A='/mnt/user-data/attachments/53e3d492-4bf8-5cd9-a0ec-63a7cbefb1d9/'
SL='goryokaku'
L={'B4':('CC BY 4.0','https://creativecommons.org/licenses/by/4.0/'),'S3':('CC BY-SA 3.0','https://creativecommons.org/licenses/by-sa/3.0/')}
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
GT='Goryokaku-Tower'
hero=mk('hero-sakura','4829ce99-image.jpg',GT,'B4','The star-shaped fort from above in cherry blossom, with pale pink trees along the moat and the town and mountains beyond','Goryokaku in cherry blossom, 4 May 2017.',hero=True)
t='  <!-- TABLE OF CONTENTS -->'; assert s.count(t)==1
s=s.replace(t,'  '+hero+'\n\n'+t)
put("shows the star from within.</p>",
 blk('stone-marker','3af60dbc-image.jpg','くろふね (Kurofune)','B4','A granite marker inscribed with the name Goryokaku beside a wooden bridge and a moat with trees and a stone wall behind','The stone marker at the edge of the moat, 23 July 2021.',maxw=760,
  para="Commons labels this 五稜郭公園 (Goryokaku Park), and the time is 5:02 in the morning on 23 July 2021. The granite marker at the right reads 特別史跡 五稜郭跡, &ldquo;Special Historic Site, Goryokaku ruins,&rdquo; which matches the designation in the sources above. Behind it a wooden bridge crosses the moat toward a grassy earthwork with a stone retaining wall. Commons does not name the bridge, so I only describe it.")+
 blk('cannons','4c431243-image.jpg','くろふね (Kurofune)','B4','Two old iron cannon on stone and concrete bases in a gravel yard, with trees and a low building behind','Cannon on display in the park, 23 July 2021.',
  para="This is from the same early morning, at 5:30, and Commons again says only 五稜郭公園. Two cannon rest on stone blocks over concrete bases: a thick, short barrel in the foreground and a longer, slimmer one behind. GLTJP says two cannons are displayed in the park, which fits what is shown, but Commons does not say which guns these are, so please treat the match as likely rather than certain."))
put("dioramas.</p>",
 blk('panorama-2011','7ff7a0f4-image.jpg','京浜にけ (Keihin nike)','S3','A summer view of the star-shaped fort from above, with green trees on the earthworks, a bridge over the moat and the town and mountains beyond','Goryokaku in summer, seen from the tower, 11 July 2011.',
  para="Commons describes this as the special historic site Goryokaku seen from the second floor of Goryokaku Tower, taken on 11 July 2011. It is a good picture for understanding the plan. The five points of the star run out in a green mass of trees, the moat curves around them, and a bridge crosses to the middle. The dark-roofed building near the centre appears to be the Magistrate&rsquo;s Office, though Commons does not label it. The tower was rebuilt in 2006, so this is the current tower&rsquo;s view."))
put("a claim I found in one source only.</p>",
 blk('summer-2017','df77a493-image.jpg',GT,'B4','The star-shaped fort in summer from a high viewpoint, with bright green trees, the moat and a red-roofed building in the lower right','Goryokaku in early summer, 14 June 2017.',
  para="The Commons description for this one is &ldquo;Hokkaido, summer Goryokaku,&rdquo; from the FIND/47 project, dated 14 June 2017, and the author is listed as Goryokaku-Tower. Commons does not give the viewpoint, but the glass-roofed building at the bottom edge and the angle suggest it was taken from the tower. In June the earthworks are covered in fresh green and the moat is dark blue, which is the opposite of the pink in the picture at the top of this page.")+
 blk('autumn-2017','9a15b976-image.jpg',GT,'B4','The star-shaped fort in autumn, with orange and red trees along the moat and on the earthworks under a cloudy sky','Goryokaku in autumn, 4 November 2017.',
  para="Commons calls this &ldquo;Hokkaido, autumn Goryokaku,&rdquo; and gives the date as 4 November 2017. The trees along the moat and across the earthworks have turned orange and red, and a few dark pines stay green near the centre. If you are in Hakodate in late autumn, it shows that the park is worth a visit outside blossom season. The date is a guide only, because the timing of colour changes varies from year to year."))
put("Please check the current schedule before you plan around it.</p>",
 blk('winter-2017','e54c007c-image.jpg',GT,'B4','The star-shaped fort covered in snow, with a snowy moat and bare trees, the town and snowy mountains beyond','Goryokaku in winter, 19 February 2017.',
  para="Commons labels this &ldquo;Hokkaido, winter Goryokaku,&rdquo; dated 19 February 2017. Snow covers the moat and the earthworks so thickly that the star becomes almost a white outline, with rows of bare trees casting shadows across the ground. The season also overlaps with the December-to-February illumination described above, which is lit after dark, so please do not read this daytime picture as a view of the lights."))
open(p,'w',encoding='utf-8').write(s)
with open(R+'PHOTO-CREDITS.csv','a',encoding='utf-8',newline='') as f: csv.writer(f,lineterminator='\r\n').writerows(rows)
print(len(rows))
