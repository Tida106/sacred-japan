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
 ('wagashi','/culture/wagashi/','Wagashi',f'{R}/images/hub/wagashi.jpg'),
 ('japanese-sweets','/culture/japanese-sweets/','Sweets',f'{R}/culture/wagashi/images/dora1.jpg'),
 ('regional-food','/regional-food/','Regional',f'{R}/images/hub/culture-food.jpg'),
]
os.makedirs(f'{R}/images/food-nav',exist_ok=True)
for slug,_,_,src in ITEMS:
    im=Image.open(src).convert('RGB'); w,h=im.size; tw=int(h*4/3)
    im=im.crop(((w-tw)//2,0,(w-tw)//2+tw,h)) if tw<=w else im.crop((0,(h-int(w*3/4))//2,w,(h-int(w*3/4))//2+int(w*3/4)))
    im=im.resize((160,120),Image.LANCZOS); im.save(f'{R}/images/food-nav/{slug}.jpg',quality=82); im.save(f'{R}/images/food-nav/{slug}.webp',quality=78)
CSS='''<style>
.food-nav{margin:0 0 36px;padding:16px 18px 6px;background:var(--washi);border:1px solid var(--border-strong);border-left:3px solid var(--kin);border-radius:2px;}
.food-nav-h{font-family:'Noto Serif JP',serif;font-size:11px;letter-spacing:3px;color:var(--beni);margin:0 0 12px;}
.food-nav-list{display:flex;flex-wrap:wrap;gap:10px;margin:0;padding:0;list-style:none;}
.food-nav-list li{margin:0;padding:0;}
.food-nav-a{display:flex;align-items:center;gap:10px;padding:5px 14px 5px 5px;background:#fff;border:1px solid var(--border-strong);border-radius:3px;text-decoration:none;color:var(--sumi);font-family:'Shippori Mincho',serif;font-size:16px;line-height:1.2;transition:background .2s,transform .15s;}
a.food-nav-a:hover{background:var(--washi-dark);transform:translateY(-1px);}
.food-nav-a img{width:48px;height:36px;object-fit:cover;border-radius:2px;display:block;flex:none;}
.food-nav-a.is-here{background:linear-gradient(135deg,#f9e9a8 0%,#e6c45a 40%,#d6a92b 100%);border-color:#b8860b;font-weight:600;}
.food-nav-list{margin-bottom:10px;}
.related-card.has-thumb{display:flex;align-items:center;justify-content:space-between;gap:20px;}
.related-card.has-thumb .rc-text{flex:1;min-width:0;}
.related-card.has-thumb .rc-thumb{width:120px;height:90px;object-fit:cover;border-radius:3px;flex:none;display:block;}
@media(max-width:600px){.food-nav-list{flex-wrap:nowrap;overflow-x:auto;padding-bottom:6px;-webkit-overflow-scrolling:touch;}.food-nav-a{white-space:nowrap;}.related-card.has-thumb .rc-thumb{width:84px;height:63px;}.related-card.has-thumb{gap:14px;}}
</style>'''
def strip(cur):
    lis=[]
    for slug,url,label,_ in ITEMS:
        pic=f'<picture><source srcset="/images/food-nav/{slug}.webp" type="image/webp"><img src="/images/food-nav/{slug}.jpg" alt="" width="48" height="36" loading="lazy"></picture>'
        if slug==cur: lis.append(f'<li><span class="food-nav-a is-here" aria-current="page">{pic}{label}</span></li>')
        else: lis.append(f'<li><a class="food-nav-a" href="{url}" onclick="trackEvent(\'click\',\'internal\',\'food_nav_{cur}_to_{slug}\')">{pic}{label}</a></li>')
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
