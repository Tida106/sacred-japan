import re,csv,json
from PIL import Image
R='/home/claude/sacred-japan/'; A='/mnt/user-data/attachments/53e3d492-4bf8-5cd9-a0ec-63a7cbefb1d9/'
SL='okayama-castle'; D=R+f'guides/{SL}/images/'
lic=('CC BY-SA 2.0','https://creativecommons.org/licenses/by-sa/2.0/'); au='Mikel Lizarralde'; k='shachi-view'
alt='A gold shachihoko seen from behind and above, with a green moat with boats at the left, a wooded garden with lawns beyond, and a city with low mountains in the distance'
cap='Looking north from the keep, past the shachihoko to the moat and Korakuen, 4 August 2008.'
ps="Commons describes this as a view north from the keep, with Korakuen beyond the moat, and it adds that the tall building to the left of the shachihoko is the Okayama Plaza Hotel. The gold fish ornament fills the center of the frame, with its red eyes and fins catching the sun, and below it you can see rental boats on the moat and the lawns of the garden spreading out under the trees. It shows in one picture why the two sites work as a pair, and the summer haze gives a sense of how far the view runs to the hills beyond the city."
im=Image.open(A+'2053ce9e-image.jpg').convert('RGB')
if im.width>1200: im=im.resize((1200,round(im.height*1200/im.width)),Image.LANCZOS)
im.save(D+k+'.jpg',quality=84,optimize=True); im.save(D+k+'.webp',quality=80)
img=f'<picture><source srcset="/guides/{SL}/images/{k}.webp" type="image/webp"><img src="/guides/{SL}/images/{k}.jpg" alt="{alt}" width="{im.width}" height="{im.height}" loading="lazy" style="width:100%;height:auto;border-radius:4px;display:block;"></picture>'
fc=f'<figcaption style="font-size:13px;color:var(--enshu);margin-top:10px;text-align:center;line-height:1.6;">{cap}<br>Photo: {au}, <a href="{lic[1]}" target="_blank" rel="noopener" style="color:var(--enshu);">{lic[0]}</a>, via Wikimedia Commons (resized)</figcaption>'
p=R+f'guides/{SL}/index.html'; s=open(p,encoding='utf-8').read()
a='how the castle town grew into the modern city.</p>'; assert s.count(a)==1
s=s.replace(a,a+f'\n    <figure style="margin:28px auto;max-width:760px;">{img}{fc}</figure>\n    <p>{ps}</p>')
open(p,'w',encoding='utf-8').write(s)
with open(R+'PHOTO-CREDITS.csv','a',encoding='utf-8',newline='') as f: csv.writer(f,lineterminator='\r\n').writerow([f'guides/{SL}',f'/guides/{SL}/images/{k}.jpg',lic[0],lic[1],lic[1],cap+f' Photo: {au}, {lic[0]}, via Wikimedia Commons (resized)'])
for tg in ['div','figure','picture','p','a','ul','li','details','section','h2']:
    assert len(re.findall(f'<{tg}[ >]',s))==len(re.findall(f'</{tg}>',s)),tg
for m in re.findall(r'<script type="application/ld\+json">(.*?)</script>',s,re.S): json.loads(m)
print('ok',s.count('<figure'))
