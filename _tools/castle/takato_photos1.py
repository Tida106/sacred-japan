import re
import csv
from PIL import Image
R='/home/claude/sacred-japan/'; A='/mnt/user-data/attachments/53e3d492-4bf8-5cd9-a0ec-63a7cbefb1d9/'
SL='takato-castle-ruins'
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
hero=mk('aerial','0e8b8233-image.jpg','Maeda','S4','A red-roofed building among pine trees on a hillside covered in pink cherry blossom','Cherry trees in full bloom around a red-roofed building, 10 April 2021.',hero=True)
put("  <!-- TABLE OF CONTENTS -->",hero+"\n\n",before=True)
put("so please be ready for crowds.</p>",
 blk('bridge-white','7d58612a-image.jpg','FlyMeToFullmoon','PD','A red-brown arched wooden bridge crowded with visitors, framed by white cherry blossom on every side','The arched wooden bridge among the blossom, crowded with visitors. The Commons date, 30 October 2006, is the upload date.',
  para="Commons shows an arched wooden bridge full of people under a canopy of pale blossom. I take it to be the cherry bridge I describe above, though the Commons text does not name it. It shows the crowds well: people stand shoulder to shoulder on the span, and the branches are so thick that the sky is almost hidden. The 30 October 2006 date is the upload date and not the day of the photo. The photographer has released the work into the public domain.")+
 blk('bridge-pink','0100d91c-image.jpg','江戸村のとくぞう (Edomura no Tokuzo)','S4','A wooden arched bridge with a few visitors, seen from below through pink cherry branches and a stone wall','The same kind of bridge from below, 13 April 2010.',
  para="This one is from 13 April 2010, taken from the path below the bridge. The blossom is pink here, where the other picture looks white, which I put down to light and exposure and not to a different kind of tree. The stone wall under the bridge is a useful reminder that the whole park sits on old castle terraces. Please remember that these are spring photographs: outside bloom time the bridge looks very different."))
put("go-nagano says it was moved here in 1877.</p>","")
put("popular for photos.</p>",
 blk('ote-gate','a402b680-image.jpg','Qurren','S4','A small tiled gate with an open lawn behind it, under fresh green trees and a blue sky','The gate labelled on Commons as the Ote Gate of Takato Castle, 30 April 2022.',
  para="Commons labels this the traditional Ote Gate of Takato Castle (伝・高遠城大手門). The word 伝 means &ldquo;said to be,&rdquo; so I repeat it as a tradition and not as a fact. It is a modest gate with a tiled roof, and behind it is an open lawn with fresh green leaves. This is how the park looks at the end of April, after the blossom, which is useful if you arrive late.")+
 blk('tonya-gate','20ca5814-image.jpg','Qurren','S4','A tiled gate with a signboard beside it, seen from the front along a brick path through green maple trees','The Ton\'ya Gate (問屋門), 30 April 2022.',
  para="This is the Ton\'ya Gate (問屋門), as Commons names it, photographed on the same day. A signboard stands to the left of the gate. A brick path runs through it under fresh green leaves, and a wooden rail is just visible in the foreground. I mention it because it is one of the few older-looking structures in the park.")+
 blk('hakuto-bridge','7ba267fc-image.jpg','Qurren','S4','A paved path crossing a stone-railed bridge under bright green maple trees','The Hakuto Bridge (白兎橋), 30 April 2022.',
  para="Commons calls this the Hakuto Bridge (白兎橋). It has stone posts and a stone railing and crosses a dry section of the park under green maple leaves. It is a quiet spot compared with the cherry bridge, and it shows how the park feels when the crowds have gone."))
s=s  # Takatokaku photo inserted below
import re as _re
m=_re.search(r"(Takatokaku</strong> is a two-storey.*?)(</p>)",s,_re.S)
assert m, 'takatokaku'
blkh=blk('takatokaku','f9cdac8f-image.jpg','江戸村のとくぞう (Edomura no Tokuzo)','S4','A two-storey wooden building with curved red-brown roofs and a queue of visitors in front, with cherry blossom above','A wooden building with curved roofs and a queue of visitors, 13 April 2010.',
  para="Commons does not name the building, but the curved roofs and the position match my description of Takatokaku, so I take it to be that building, and I am not certain. In the photo, a line of visitors in spring clothes walks past it under the blossom, which gives a good idea of how busy the path is in bloom season.")
s=s[:m.end()]+blkh+s[m.end():]
open(p,'w',encoding='utf-8').write(s)
import csv
with open(R+'PHOTO-CREDITS.csv','a',encoding='utf-8',newline='') as f: csv.writer(f,lineterminator='\r\n').writerows(rows)
print(len(rows))
for tg in ['div','figure','picture','p','a','ul','li','details','section','h2']:
    assert len(re.findall(f'<{tg}[ >]',s))==len(re.findall(f'</{tg}>',s)),tg
