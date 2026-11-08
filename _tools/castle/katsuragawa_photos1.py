import re, csv, os
from PIL import Image
R='/home/claude/sacred-japan/'; A='/mnt/user-data/attachments/fd332c08-3f6b-545a-883b-83277e19ff52/'
SL='katsuragawa'
L={'B3':('CC BY 3.0','https://creativecommons.org/licenses/by/3.0/'),'S3':('CC BY-SA 3.0','https://creativecommons.org/licenses/by-sa/3.0/'),'S25':('CC BY-SA 2.5','https://creativecommons.org/licenses/by-sa/2.5/'),'S4':('CC BY-SA 4.0','https://creativecommons.org/licenses/by-sa/4.0/'),'B4':('CC BY 4.0','https://creativecommons.org/licenses/by/4.0/'),'B2':('CC BY 2.0','https://creativecommons.org/licenses/by/2.0/'),'CC0':('CC0 1.0','https://creativecommons.org/publicdomain/zero/1.0/'),'PD':('Public Domain','https://commons.wikimedia.org/wiki/Template:PD-self')}
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


put("gives Katsuragawa its sense of having stood here far longer than three centuries.</p>",
 blk('hall-festival','6e3eccea','tanohei','B3','A large wooden temple hall with a layered thatch-like roof, hung with a row of coloured cloth banners and a red-and-white striped curtain, with a few people standing in front on gravel','The hall dressed for an occasion, 18 May 2011 (Commons: Katsuragawa Myoo-in).',
  para="Commons titles this simply as Katsuragawa Myoo-in (葛川明王院) and dates it to 18 May 2011. The hall is hung with a row of multicoloured banners and a long red-and-white curtain, and a large black crest on a white cloth marks the entrance. A few people stand quietly on the gravel. I do not know which ceremony this was, so I will not name one, but it shows that the hall is used, and that on certain days it looks very different from the plain weathered hall you may find. The file offers a choice of licences (GFDL or CC BY 3.0), and I credit it under CC BY 3.0."))
open(p,'w',encoding='utf-8').write(s)
with open(R+'PHOTO-CREDITS.csv','a',encoding='utf-8',newline='') as f: csv.writer(f,lineterminator='\r\n').writerows(rows)
print(len(rows))
for tg in ['div','figure','picture','p','a','ul','li','details','section','h2']:
    assert len(re.findall(f'<{tg}[ >]',s))==len(re.findall(f'</{tg}>',s)),tg
