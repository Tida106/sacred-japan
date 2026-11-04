import re,csv,json
from PIL import Image
R='/home/claude/sacred-japan/'; A='/mnt/user-data/attachments/53e3d492-4bf8-5cd9-a0ec-63a7cbefb1d9/'
SL='hagi-castle'; D=R+f'guides/{SL}/images/'
import os; os.makedirs(D,exist_ok=True)
lic=('CC BY-SA 4.0','https://creativecommons.org/licenses/by-sa/4.0/')
k='gokuraku-bridge'
alt='A wide gravel bridge between two stone walls leading to a gate site, with stone marker posts on each side, visitors walking, and a forested hill under a cloudy sky'
cap='The bridge to the Honmaru gate site, 4 May 2017.'
para=("This is the approach most visitors take into the inner part of the ruins: a broad gravel bridge across the moat, with stone walls on both sides and the gate site ahead. The tall post on the left reads &ldquo;史跡 萩城趾&rdquo; (Historic Site, Hagi Castle ruins), and the one on the right appears to name Shizukiyama Shrine, which stands inside. Commons titles the view as the Gokuraku Bridge and the Honmaru gate site. The small board near the gate seems to celebrate the World Heritage listing, and the brown sign at the right says bicycles may be ridden in. The photo is from 2017, so signs and fittings may have changed.")
im=Image.open(A+'a478105b-image.jpg').convert('RGB')
if im.width>1200: im=im.resize((1200,round(im.height*1200/im.width)),Image.LANCZOS)
im.save(D+k+'.jpg',quality=84,optimize=True); im.save(D+k+'.webp',quality=80)
img=f'<picture><source srcset="/guides/{SL}/images/{k}.webp" type="image/webp"><img src="/guides/{SL}/images/{k}.jpg" alt="{alt}" width="{im.width}" height="{im.height}" loading="lazy" style="width:100%;height:auto;border-radius:4px;display:block;"></picture>'
fc=f'<figcaption style="font-size:13px;color:var(--enshu);margin-top:10px;text-align:center;line-height:1.6;">{cap}<br>Photo: そらみみ, <a href="{lic[1]}" target="_blank" rel="noopener" style="color:var(--enshu);">{lic[0]}</a>, via Wikimedia Commons (resized)</figcaption>'
html=f'\n    <figure style="margin:28px auto;max-width:760px;">{img}{fc}</figure>\n    <p>{para}</p>'
p=R+f'guides/{SL}/index.html'; s=open(p,encoding='utf-8').read()
a='Fun Japan says the keep ruins are lit and reflected in the moat.</p>'
assert s.count(a)==1
s=s.replace(a,a+html)
open(p,'w',encoding='utf-8').write(s)
with open(R+'PHOTO-CREDITS.csv','a',encoding='utf-8',newline='') as fh:
    csv.writer(fh,lineterminator='\r\n').writerow([f'guides/{SL}',f'/guides/{SL}/images/{k}.jpg',lic[0],lic[1],lic[1],cap+' Photo: そらみみ, CC BY-SA 4.0, via Wikimedia Commons (resized)'])
for tg in ['div','figure','picture','p','a','ul','li','details','section','h2']:
    assert len(re.findall(f'<{tg}[ >]',s))==len(re.findall(f'</{tg}>',s)),tg
for m in re.findall(r'<script type="application/ld\+json">(.*?)</script>',s,re.S): json.loads(m)
print('ok',s.count('<figure'))
