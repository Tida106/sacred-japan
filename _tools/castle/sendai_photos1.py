import re
import csv
from PIL import Image
R='/home/claude/sacred-japan/'; A='/mnt/user-data/attachments/53e3d492-4bf8-5cd9-a0ec-63a7cbefb1d9/'
SL='sendai-castle'
L={'S2':('CC BY-SA 2.0','https://creativecommons.org/licenses/by-sa/2.0/'),'S4':('CC BY-SA 4.0','https://creativecommons.org/licenses/by-sa/4.0/'),'B3':('CC BY 3.0','https://creativecommons.org/licenses/by/3.0/'),'B4':('CC BY 4.0','https://creativecommons.org/licenses/by/4.0/'),'S3':('CC BY-SA 3.0','https://creativecommons.org/licenses/by-sa/3.0/'),'B2':('CC BY 2.0','https://creativecommons.org/licenses/by/2.0/'),'PD':('Public Domain','https://commons.wikimedia.org/wiki/Template:PD-self')}
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
hero=mk('turret','05f080c5-image.jpg','663highland','S3','A white two-storey turret with two fish-shaped roof ornaments beside a tall dark stone wall, with stone steps and a grassy bank in the foreground','The reconstructed turret beside a stone wall, from the Commons upload of 2007.',hero=True)
put("  <!-- TABLE OF CONTENTS -->",hero+"\n\n",before=True)
put("marked on the ground.</p>",
 "\n    <p>The picture at the top of this page shows what I take to be that turret, though Commons labels it only &ldquo;Sendai Castle in Sendai, Miyagi prefecture, Japan,&rdquo; so I cannot confirm which turret it is. It is a two-storey white building with grilles in the walls and a fish-shaped ornament at each end of the ridge. On the right is a steeply battered wall of dark stone, which gives a good sense of the scale I describe above. The Commons history lists uploads in 2007 and 2013, so I do not give a date.</p>")
put("I found those two dates in one source only.</p>",
 blk('marker','c38ce85c-image.jpg','Sendai Blog','B2','A tall grey stone marker with the characters for Historic Site, Sendai Castle ruins, beside a map board and a wide paved stairway under green trees','The stone marker for the Sendai Castle ruins, 3 July 2009.',
  para="Commons describes this as the stone sign of Sendai Castle and dates it 3 July 2009. The marker reads 史跡 仙台城跡 (Historic Site, Sendai Castle ruins) and, along its edge, a date that I read as 平成十五年八月二十七日, which is 27 August 2003 and fits the designation year above. A map board stands beside it and a wide stairway leads up under the trees. Note that the sign is from 2009, so the board may have changed."))
put("(one source only).</p>",
 blk('statue','2a19b2f4-image.jpg','九翼天使 (Kyuyoku Tenshi)','S3','The bronze equestrian statue of Date Masamune in a crescent-crested helmet, seen from below against a blue sky and a pine tree','The Date Masamune statue seen from below, uploaded 29 October 2011.',
  maxw=640,para="This is the equestrian statue as you meet it on the hill: Masamune in armour and a helmet with a large crescent crest, one hand on his sword and the horse lifting a front hoof. The 29 October 2011 date on my screenshot is the upload date, so it is not necessarily the day of the photo. Photographed from low down, the statue stands out clearly against the blue sky; the pine on the right and the bare branch on the left suggest an autumn or winter day, but I have no way to confirm that.")+
 blk('panorama','18f4bad4-image.jpg','Enirac Sum','PD','A wide panorama of Sendai city with high-rise buildings behind green treetops under a pale blue sky','The city of Sendai from the castle site, 31 May 2010.',
  maxw=900,para="Commons describes this as a panoramic view of Sendai City, stitched from 13 photographs, taken on 31 May 2010 from what it calls the site of the Sendai Castle keep tower base. Because this guide says that no keep was built, I would simply read that as the high ground of the castle site, which is the view I describe here. The high-rises of the centre fill the middle, with the Hirose River just visible on the right, a detail that I judge from the landscape and not from Commons. The photographer has released this work into the public domain."))
put("Be aware that the film is in Japanese (japan-guide).</p>",
 blk('honmaru-hall','4dd10c8a-image.jpg','掬茶 (Kikucha)','S4','A two-storey building with a dark tiled roof, large windows and an outdoor staircase, with a food court sign and people at tables under a blue sky','The Aoba Castle honmaru hall, 21 December 2025.',
  para="Commons labels this the Aoba Castle honmaru hall (青葉城本丸会館) and dates it 21 December 2025. A sign on the ground floor reads &ldquo;AOBAJO FOOD COURT,&rdquo; and people sit at tables in the sun in front of it. It is a modern visitor building and not part of the old castle, so I include it as a practical landmark for a break on the hill. I have not checked its opening hours, so please do not plan a meal around it."))
open(p,'w',encoding='utf-8').write(s)
import csv
with open(R+'PHOTO-CREDITS.csv','a',encoding='utf-8',newline='') as f: csv.writer(f,lineterminator='\r\n').writerows(rows)
print(len(rows))
for tg in ['div','figure','picture','p','a','ul','li','details','section','h2']:
    assert len(re.findall(f'<{tg}[ >]',s))==len(re.findall(f'</{tg}>',s)),tg
