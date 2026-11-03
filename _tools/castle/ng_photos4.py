import re,csv,json
from PIL import Image
R='/home/claude/sacred-japan/'; A='/mnt/user-data/attachments/53e3d492-4bf8-5cd9-a0ec-63a7cbefb1d9/'
SL='nagoya-castle'; D=R+f'guides/{SL}/images/'
S4=('CC BY-SA 4.0','https://creativecommons.org/licenses/by-sa/4.0/')
k='moat-sakura'; au='Alpsdake'; lic=S4
alt='A stone castle wall rising from a still moat, with cherry trees in full bloom and pines along its top and the water reflecting the wall and blossoms'
cap='The outer moat and cherry blossoms, 31 March 2015 (Commons: Moats of Nagoya Castle and Sakura).'
ps="This is the moat view I mean when I say to look at the walls from the water side. The stone wall climbs straight out of the still moat, and cherry trees in full bloom spill over its top between dark pines, with the whole scene doubled in the water. The corner of the wall at the center shows pale, squared stones, and a white building is just visible at the far left, though Commons does not say what it is. Late March is the usual peak, which matches the cherry blossom festival dates above."
im=Image.open(A+'b49348a6-image.jpg').convert('RGB'); print(im.size)
if im.width>1200: im=im.resize((1200,round(im.height*1200/im.width)),Image.LANCZOS)
im.save(D+k+'.jpg',quality=84,optimize=True); im.save(D+k+'.webp',quality=80)
img=f'<picture><source srcset="/guides/{SL}/images/{k}.webp" type="image/webp"><img src="/guides/{SL}/images/{k}.jpg" alt="{alt}" width="{im.width}" height="{im.height}" loading="lazy" style="width:100%;height:auto;border-radius:4px;display:block;"></picture>'
fc=f'<figcaption style="font-size:13px;color:var(--enshu);margin-top:10px;text-align:center;line-height:1.6;">{cap}<br>Photo: {au}, <a href="{lic[1]}" target="_blank" rel="noopener" style="color:var(--enshu);">{lic[0]}</a>, via Wikimedia Commons (resized)</figcaption>'
h=f'<figure style="margin:28px auto;max-width:760px;">{img}{fc}</figure>\n    <p>{ps}</p>\n'
p=R+f'guides/{SL}/index.html'; s=open(p,encoding='utf-8').read()
a='to frame a shot like this.</p>'; assert s.count(a)==1
s=s.replace(a,a+'\n'+h); open(p,'w',encoding='utf-8').write(s)
with open(R+'PHOTO-CREDITS.csv','a',encoding='utf-8',newline='') as f:
    csv.writer(f,lineterminator='\r\n').writerow([f'guides/{SL}',f'/guides/{SL}/images/{k}.jpg',lic[0],lic[1],lic[1],cap+f'Photo: {au}, {lic[0]}, via Wikimedia Commons (resized)'])
for tg in ['div','figure','picture','p','a','ul','li','details','section','h2']:
    assert len(re.findall(f'<{tg}[ >]',s))==len(re.findall(f'</{tg}>',s)),tg
for m in re.findall(r'<script type="application/ld\+json">(.*?)</script>',s,re.S): json.loads(m)
print('ok',s.count('<figure'))
