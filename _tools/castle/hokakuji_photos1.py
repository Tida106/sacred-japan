import re, csv, os
from PIL import Image
R='/home/claude/sacred-japan/'; A='/mnt/user-data/attachments/fd332c08-3f6b-545a-883b-83277e19ff52/'
SL='hokakuji'
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


A1="<h2 id=\"the-pilgrim-s-guide\">"
intro='\n    <p>Photos of this temple are few. The four below come from Wikimedia Commons files labelled Hokakuji (鳳閣寺) in Kurotaki Village, Nara Prefecture. They show a hall that is standing and looks cared for, more intact than the ruin described above, so conditions may have changed over the years, or the two descriptions may be of different parts of the site. I could not settle this from the sources, so please read the photos as illustrations and check locally before you go.</p>'
h=blk('hall-spring','9585690f','Nankou Oronain','S3','A weathered wooden hall with a dark curved roof beside a gravel yard and a low stone fence, with woodpile under the porch and forest behind','The hall in spring, 26 April 2011 (Commons: Hokakuji, Kurotaki Village).',
  para="Commons dates this to 26 April 2011 and places it in Kurotaki Village. A hall with a dark, sweeping roof stands in a gravel yard, ringed by a low stone fence whose posts are inscribed with names. Firewood is stacked under the porch, and a tall stone marker stands at the right. It does not look abandoned, though the yard is quiet and nobody is in the frame.")+\
 blk('hall-summer','7545572a','8-hachiro','S3','The same kind of wooden hall seen from the front in summer, with green leaves in front, carved doors and a stone fence','The hall in summer, 30 June 2014 (Commons: Hokakuji, Kurotaki Village).',
  para="Commons lists this as the same temple, taken on 30 June 2014. The front shows four carved wooden doors, lattice windows to either side and a curved porch roof, with fresh green leaves crossing the view. I cannot say whether it is the same building as the one above, though the roof and the stone fence look alike. Summer here is dense green, which is a different mood from the November maples this guide describes.")+\
 blk('hall-facade','cddd7e8b','8-hachiro','S3','A close view of a carved wooden temple front with a curved eave, lion-like bracket carvings, a gold-lettered plaque and panelled doors','The carved front of the hall, 30 June 2014 (Commons: Hokakuji, Kurotaki Village).',
  para="A close, upward view of the front. Under the curved eave are carved brackets in the shape of lion-like beasts, a dragon-like carving over the lintel, and a plaque with gold lettering that I cannot read with confidence. The panelled doors carry round flower crests. This is the detail you see when you stand close, and it is a reminder that the carving is worth a slow look.",maxw=420)+\
 blk('rigen-tomb','e22dfe17','Nankou Oronain','S3','A small wooden roofed shelter with an iron fence around a stone pagoda, a wooden signpost in front and fallen leaves on the ground','The Mausoleum of Rigen-daishi, 26 April 2011 (Commons: 理源大師廟塔).',
  para="Commons names this the Mausoleum of Rigen-daishi (理源大師廟塔), dated 26 April 2011, and the signpost in the photo reads 石の廟塔 (重要文化財), a stone mausoleum tower that is an Important Cultural Property. A stone pagoda sits inside a wooden shelter behind an iron fence, with flowers left at the gate. I have not verified the history of the tomb for this guide, so I give only what the photo and Commons say.")
put(A1,intro+h+"\n\n",before=True)
open(p,'w',encoding='utf-8').write(s)
with open(R+'PHOTO-CREDITS.csv','a',encoding='utf-8',newline='') as f: csv.writer(f,lineterminator='\r\n').writerows(rows)
print(len(rows))
for tg in ['div','figure','picture','p','a','ul','li','details','section','h2']:
    assert len(re.findall(f'<{tg}[ >]',s))==len(re.findall(f'</{tg}>',s)),tg
