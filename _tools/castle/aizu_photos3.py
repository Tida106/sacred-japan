import csv
from PIL import Image
R='/home/claude/sacred-japan/'; A='/mnt/user-data/attachments/53e3d492-4bf8-5cd9-a0ec-63a7cbefb1d9/'
SL='aizuwakamatsu-castle'; k='rinkaku-gate-bamboo'
im=Image.open(A+'6181ca3f-image.jpg').convert('RGB'); im=im.resize((1200,round(im.height*1200/im.width)),Image.LANCZOS) if im.width>1200 else im
D=R+f'guides/{SL}/images/'; im.save(D+k+'.jpg',quality=84,optimize=True); im.save(D+k+'.webp',quality=80)
lic,u='CC BY 3.0','https://creativecommons.org/licenses/by/3.0/'
cap='The Rinkaku tea house garden, 22 August 2011.'
fig=(f'<figure style="margin:28px auto;max-width:760px;"><picture><source srcset="/guides/{SL}/images/{k}.webp" type="image/webp"><img src="/guides/{SL}/images/{k}.jpg" alt="A small gate with a moss-covered bamboo-trimmed roof beside a bamboo fence, with a yellow-walled tea house behind green trees" width="{im.width}" height="{im.height}" loading="lazy" style="width:100%;height:auto;border-radius:4px;display:block;"></picture>'
 f'<figcaption style="font-size:13px;color:var(--enshu);margin-top:10px;text-align:center;line-height:1.6;">{cap}<br>Photo: jeienne, <a href="{u}" target="_blank" rel="noopener" style="color:var(--enshu);">{lic}</a>, via Wikimedia Commons (resized)</figcaption></figure>')
para="Commons describes this as the tea room Rinkaku inside Tsuruga Castle Park, taken on 22 August 2011. A small gate with a moss-covered roof, edged with split bamboo, stands at the left, and a bamboo fence with black rope lashings runs along the garden. Behind a rounded shrub, a low building with ochre walls and paper-screen windows is partly hidden by the trees. A small sign stands at the right, but I cannot read it well enough to say what it says. It is a good picture of how much of Rinkaku is in the garden, not only in the tea house itself."
p=R+f'guides/{SL}/index.html'; s=open(p,encoding='utf-8').read()
a="though I cannot say which gate this is.</p>"; assert s.count(a)==1
s=s.replace(a,a+'\n    '+fig+f'\n    <p>{para}</p>'); open(p,'w',encoding='utf-8').write(s)
with open(R+'PHOTO-CREDITS.csv','a',encoding='utf-8',newline='') as f: csv.writer(f,lineterminator='\r\n').writerow([f'guides/{SL}',f'/guides/{SL}/images/{k}.jpg',lic,u,u,f'{cap} Photo: jeienne, {lic}, via Wikimedia Commons (resized)'])
