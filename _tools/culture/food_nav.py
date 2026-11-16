"""Post-process the food guides: add a 'Japanese food guides' strip at the top of <main>
and small right-hand thumbnails on the bottom related cards. Idempotent.
Run AFTER rebuilding any food builder (dishes/ramen/noodles/yakitori/bread/wagashi/sweets):
    python3 _tools/culture/food_nav.py
"""
import re, os
from PIL import Image
R='/home/claude/sacred-japan'
# slug -> (page dir, url, label, thumb source)
ITEMS=[
 ('popular-dishes','/culture/popular-dishes/','Dishes',f'{R}/images/hub/popular-dishes.jpg'),
 ('ramen','/culture/ramen/','Ramen',f'{R}/images/hub/ramen.jpg'),
 ('noodles','/culture/noodles/','Noodles',f'{R}/images/hub/noodles.jpg'),
 ('yakitori','/culture/yakitori/','Yakitori',f'{R}/images/hub/yakitori.jpg'),
 ('bread','/culture/bread/','Bread',f'{R}/images/hub/bread.jpg'),
 ('wagashi','/culture/wagashi/','Japanese Sweets',f'{R}/images/hub/wagashi.jpg'),
 ('japanese-sweets','/culture/japanese-sweets/','Snacks &amp; Souvenirs',None),
 ('regional-food','/regional-food/','Regional',f'{R}/images/hub/culture-food.jpg'),
]
os.makedirs(f'{R}/images/food-nav',exist_ok=True)
for slug,_,_,src in ITEMS:
    if src is None:
        from PIL import ImageDraw, ImageFont
        im=Image.new('RGB',(320,240),(252,240,242)); d=ImageDraw.Draw(im)
        d.rectangle([8,8,311,231],outline=(201,151,28),width=3); d.rectangle([14,14,305,225],outline=(201,151,28),width=1)
        f1=ImageFont.truetype('/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc',84); f2=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf',26)
        d.text((160,98),'お土産',font=f1,fill=(139,32,48),anchor='mm'); d.text((160,178),'SOUVENIRS',font=f2,fill=(160,110,0),anchor='mm')
    else:
        im=Image.open(src).convert('RGB')
    w,h=im.size; tw=int(h*4/3)
    im=im.crop(((w-tw)//2,0,(w-tw)//2+tw,h)) if tw<=w else im.crop((0,(h-int(w*3/4))//2,w,(h-int(w*3/4))//2+int(w*3/4)))
    im=im.resize((160,120),Image.LANCZOS); im.save(f'{R}/images/food-nav/{slug}.jpg',quality=82); im.save(f'{R}/images/food-nav/{slug}.webp',quality=78)
CSS='''<style>
.food-nav{margin:0 0 40px;padding:20px 20px 8px;background:var(--washi);border:1px solid var(--border-strong);border-left:3px solid var(--kin);border-radius:2px;}
.food-nav-h{font-family:'Noto Serif JP',serif;font-size:12px;letter-spacing:3px;color:var(--beni);margin:0 0 14px;}
.food-nav-list{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin:0 0 12px;padding:0;list-style:none;}
.food-nav-list li{margin:0;padding:0;}
.food-nav-a{display:block;background:#fff;border:1px solid var(--border-strong);border-radius:3px;overflow:hidden;text-decoration:none;color:var(--sumi);font-family:'Shippori Mincho',serif;font-size:18px;text-align:center;transition:transform .15s,box-shadow .2s;}
a.food-nav-a:hover{transform:translateY(-2px);box-shadow:0 3px 8px rgba(80,40,40,.15);}
.food-nav-a picture,.food-nav-a img{display:block;width:100%;}
.food-nav-a img{aspect-ratio:4/3;object-fit:cover;height:auto;}
.food-nav-a .fn-l{display:block;padding:9px 6px 11px;line-height:1.2;}
.food-nav-a.is-here{border-color:#b8860b;box-shadow:0 0 0 2px #e6c45a;}
.food-nav-a.is-here .fn-l{background:linear-gradient(135deg,#f9e9a8 0%,#e6c45a 40%,#d6a92b 100%);font-weight:600;}
.related-card.has-thumb{display:flex;align-items:center;justify-content:space-between;gap:20px;}
.related-card.has-thumb .rc-text{flex:1;min-width:0;}
.related-card.has-thumb .rc-thumb{width:120px;height:90px;object-fit:cover;border-radius:3px;flex:none;display:block;}
@media(max-width:600px){.food-nav-list{grid-template-columns:repeat(2,1fr);}.related-card.has-thumb .rc-thumb{width:84px;height:63px;}.related-card.has-thumb{gap:14px;}}
</style>'''
def strip(cur):
    lis=[]
    for slug,url,label,_ in ITEMS:
        pic=f'<picture><source srcset="/images/food-nav/{slug}.webp" type="image/webp"><img src="/images/food-nav/{slug}.jpg" alt="" width="160" height="120" loading="lazy"></picture>'
        if slug==cur: lis.append(f'<li><span class="food-nav-a is-here" aria-current="page">{pic}<span class="fn-l">{label}</span></span></li>')
        else: lis.append(f'<li><a class="food-nav-a" href="{url}" onclick="trackEvent(\'click\',\'internal\',\'food_nav_{cur}_to_{slug}\')">{pic}<span class="fn-l">{label}</span></a></li>')
    return ('<!--FOODNAV-->'+CSS+f'<div class="food-nav" role="group" aria-label="Japanese food guides"><p class="food-nav-h">JAPANESE FOOD GUIDES ／ 日本の食ガイド</p><ul class="food-nav-list">'+''.join(lis)+'</ul></div><!--/FOODNAV-->')
URLS={u:s for s,u,_,_ in ITEMS}
for slug,_,_,_ in ITEMS[:-1]:
    p=f'{R}/culture/{slug}/index.html'; s=open(p,encoding='utf-8').read()
    s=re.sub(r'<!--FOODNAV-->.*?<!--/FOODNAV-->','',s,flags=re.S)
    assert s.count('<main>')==1,slug
    s=s.replace('<main>','<main>\n'+strip(slug),1)
    # related cards -> thumbs
    def fix(m):
        full=m.group(0); href=m.group(1)
        if 'has-thumb' in full or href not in URLS or URLS[href]==slug: return full
        sl=URLS[href]
        inner=m.group(3)
        pic=f'<picture><source srcset="/images/food-nav/{sl}.webp" type="image/webp"><img class="rc-thumb" src="/images/food-nav/{sl}.jpg" alt="" width="120" height="90" loading="lazy"></picture>'
        return f'<a class="related-card has-thumb" href="{href}"{m.group(2)}><div class="rc-text">{inner}</div>{pic}</a>'
    s,n=re.subn(r'<a class="related-card" href="([^"]+)"([^>]*)>(.*?)</a>',fix,s,flags=re.S)
    open(p,'w',encoding='utf-8').write(s)
    print(slug,'cards',s.count('has-thumb'))
