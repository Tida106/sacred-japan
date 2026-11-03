import re,csv,json
from PIL import Image
R='/home/claude/sacred-japan/'; A='/mnt/user-data/attachments/53e3d492-4bf8-5cd9-a0ec-63a7cbefb1d9/'
SL='hiroshima-castle'; D=R+f'guides/{SL}/images/'
import os; os.makedirs(D,exist_ok=True)
L={'BY4':('CC BY 4.0','https://creativecommons.org/licenses/by/4.0/'),
   'S4':('CC BY-SA 4.0','https://creativecommons.org/licenses/by-sa/4.0/'),
   'S3':('CC BY-SA 3.0','https://creativecommons.org/licenses/by-sa/3.0/'),
   'B3':('CC BY 3.0','https://creativecommons.org/licenses/by/3.0/'),
   'C0':('CC0','https://creativecommons.org/publicdomain/zero/1.0/')}
# key, file, author, lic, alt, caption, paragraph, anchor
P=[
('hero','02fb33e3','Marion &amp; Christoph Aistleitner','C0',
 'A five-story castle keep with dark wooden walls above green trees, behind a calm moat and a long stone wall, under a partly cloudy sky',
 'The keep above the moat and its stone wall, 4 February 2014.',
 None,'HERO'),
('autumn-front','294b2bf6','Yoshio Kohara','B3',
 'The front of a five-story keep with dark wooden walls and white gables, with red and green autumn trees and three visitors walking toward the entrance',
 'The keep from the front in autumn, 28 November 2014.',
 "This is the view most visitors get: the keep seen straight on from the Honmaru, with its stacked gables and dark wooden boards, and the entrance low at the center where the ticket line forms. The red leaves on the right give the date away as late autumn. The three people walking toward the door also help show the scale, since the keep looks large but is only five stories.",
 'including the base and the shachihoko.</p>'),
('entrance-wide','70358222','DXR','S4',
 'A wide view of the keep with a covered walkway leading to the entrance, a signboard on the right, and blue sky above',
 'The keep and its entrance walkway, uploaded 5 May 2019.',
 "From a wider angle you can see the covered walkway that leads into the keep, with its red-brown posts, and the signboard beside it. I would not read much into the walkway as history, because it is a visitor facility added in front of a replica. Its main use is to show you where the museum begins.",
 'check what is on when you go.</p>'),
('entrance-tall','afe73409','DXR','S4',
 'A tall view of the five-story keep from the entrance square, with a stone bench in the foreground and blue sky above',
 'The keep seen from below at the entrance square, photographed 17 April 2019.',
 "This tall frame, taken from the square in front, shows how the roofs and gables step upward. Look at the large gable over the entrance and the smaller ones above it, which give the keep its layered look. The stone bench in the foreground is a good reminder that the square is a place to sit and take it in before you go up.",
 None),
('city-view','c0682036','Jakubhal (uploader)','BY4',
 'A view over green treetops and a moat to the city, with a white broadcasting tower and several tall buildings under a blue sky',
 'A view over the trees and moat toward the city, uploaded 20 October 2025.',
 "I could not confirm the exact spot from the Commons page, but the height suggests an upper level of the keep or a nearby high point. It gives a sense of where the castle sits now: a green island of trees and water in the middle of a modern city, with the broadcasting tower and apartment blocks pressing close. Please treat this as an illustration of the setting rather than a marked viewpoint.",
 None),
('moat-blue','316a5d50','ノボホショコロトソ','BY4',
 'A keep standing above green trees and a stone-faced moat bank, seen across calm water under a clear blue sky',
 'The keep across the moat, 30 August 2025.',
 "Across the moat, the keep rises above a thick screen of trees, and the stone facing of the bank runs along the waterline. This is the best kind of day for the walk around the moat, when the water is calm and the sky is clear. The only unattractive detail is a pair of cranes at the right edge, which is a reminder that the city around the castle is always changing.",
 'which Wikipedia says was moved there after 1945.</p>'),
('moat-cloudy','0a6edcfa','melveny','S4',
 'A keep at the right behind green trees and a stone bank, with a broadcasting tower and apartment blocks reflected in a moat covered with duckweed',
 'The moat on a cloudy day, 24 August 2013.',
 "On an overcast day the castle looks quieter and darker, and the moat is carpeted with floating green plants. The broadcasting tower and apartment block on the left are reflected in the water beside the trees. I like this picture because it shows the castle as part of the working city, not as a postcard, which is how many residents see it.",
 'which is a single-source figure.</p>'),
('night-moat','3c631a7a','Hiroaki Kaneko','S3',
 'The lit keep glowing against a black sky above trees and a stone wall, with two bright streaks reflected in the dark moat',
 'The keep lit at night, reflected in the moat, 25 November 2015.',
 "The keep is lit from below, so the white plaster and the roof edges glow against the sky and the gold streaks in the water double the effect. Commons notes the picture came from Panoramio, and the photographer's watermark is on the image. If you are staying in the city, a walk here after dinner gives you a very different castle from the daytime one. Lighting hours can change, so please check locally.",
 'Itsukushima Shrine guide</a>.</p>'),
('night-branches','0812cd1c','ADS-Slayer','S3',
 'The lit keep seen through bare tree branches at night, with a deep blue sky and a small tower with a red light at the right',
 'The keep at night through bare branches, taken around 9 p.m. in January 2009 per the photographer.',
 "Seen through leafless branches, the lit keep looks like a glowing lantern in the dark. The photographer's comment on Commons gives a date of 20 January 2009 and a time of around 9 p.m. The bare trees are a reminder that winter lighting is quite different from the cherry blossom season, when the trees around the castle are in flower.",
 None),
]
def mk(k,f,au,lic,alt,cap,hero=False):
    im=Image.open(A+f+'-image.jpg').convert('RGB')
    if im.width>1200: im=im.resize((1200,round(im.height*1200/im.width)),Image.LANCZOS)
    im.save(D+k+'.jpg',quality=84,optimize=True); im.save(D+k+'.webp',quality=80)
    l=L[lic]
    ld='eager' if hero else 'lazy'
    st='width:100%;max-height:420px;object-fit:cover;object-position:center 30%;border-radius:4px;display:block;' if hero else 'width:100%;height:auto;border-radius:4px;display:block;'
    img=f'<picture><source srcset="/guides/{SL}/images/{k}.webp" type="image/webp"><img src="/guides/{SL}/images/{k}.jpg" alt="{alt}" width="{im.width}" height="{im.height}" loading="{ld}" style="{st}"></picture>'
    fc=f'<figcaption style="font-size:13px;color:var(--enshu);margin-top:10px;text-align:center;line-height:1.6;">{cap}<br>Photo: {au}, <a href="{l[1]}" target="_blank" rel="noopener" style="color:var(--enshu);">{l[0]}</a>, via Wikimedia Commons (resized)</figcaption>'
    return im,l,img,fc
p=R+f'guides/{SL}/index.html'; s=open(p,encoding='utf-8').read()
# group by anchor; photos with None anchor attach to previous anchor
groups=[];
for t in P:
    if t[7] is None: groups[-1].append(t)
    else: groups.append([t])
rows=[]
for g in groups:
    html=''
    for (k,f,au,lic,alt,cap,para,anc) in [(x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7]) for x in g]:
        hero=(k=='hero')
        im,l,img,fc=mk(k,f,au,lic,alt,cap,hero)
        if hero:
            html=f'  <figure style="margin:0 0 48px;">{img}{fc}</figure>\n\n'
        else:
            mw='420px' if im.height>im.width else '760px'
            html+=f'\n    <figure style="margin:28px auto;max-width:{mw};">{img}{fc}</figure>\n    <p>{para}</p>'
        rows.append([f'guides/{SL}',f'/guides/{SL}/images/{k}.jpg',l[0],l[1],l[1],cap+f' Photo: {au.replace("&amp;","&")}, {l[0]}, via Wikimedia Commons (resized)'])
    anc=g[0][7]
    if anc=='HERO':
        a='  <!-- TABLE OF CONTENTS -->'; assert s.count(a)==1
        s=s.replace(a,html+a)
    else:
        assert s.count(anc)==1,anc
        s=s.replace(anc,anc+html)
open(p,'w',encoding='utf-8').write(s)
with open(R+'PHOTO-CREDITS.csv','a',encoding='utf-8',newline='') as fh:
    w=csv.writer(fh,lineterminator='\r\n')
    for r in rows: w.writerow(r)
for tg in ['div','figure','picture','p','a','ul','li','details','section','h2']:
    assert len(re.findall(f'<{tg}[ >]',s))==len(re.findall(f'</{tg}>',s)),tg
for m in re.findall(r'<script type="application/ld\+json">(.*?)</script>',s,re.S): json.loads(m)
print('ok',s.count('<figure'))
