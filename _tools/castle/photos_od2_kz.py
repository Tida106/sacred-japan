import re,os
from PIL import Image
R='/home/claude/sacred-japan/'; A='/mnt/user-data/attachments/53e3d492-4bf8-5cd9-a0ec-63a7cbefb1d9/'
L={'B4':('CC BY 4.0','https://creativecommons.org/licenses/by/4.0/'),'S4':('CC BY-SA 4.0','https://creativecommons.org/licenses/by-sa/4.0/')}
rows=[]
def mk(SL,k,f,au,lic,alt,cap):
    im=Image.open(A+f+'-image.jpg').convert('RGB')
    if im.width>1200: im=im.resize((1200,round(im.height*1200/im.width)),Image.LANCZOS)
    D=R+f'guides/{SL}/images/'
    im.save(D+k+'.jpg',quality=84,optimize=True); im.save(D+k+'.webp',quality=80)
    l=L[lic]
    rows.append([f'guides/{SL}',f'/guides/{SL}/images/{k}.jpg',l[0],l[1],l[1],f'{cap} Photo: {au}, {l[0]}, via Wikimedia Commons (resized)'])
    return (f'\n    <figure style="margin:28px auto;max-width:760px;"><picture><source srcset="/guides/{SL}/images/{k}.webp" type="image/webp"><img src="/guides/{SL}/images/{k}.jpg" alt="{alt}" width="{im.width}" height="{im.height}" loading="lazy" style="width:100%;height:auto;border-radius:4px;display:block;"></picture>'
            f'<figcaption style="font-size:13px;color:var(--enshu);margin-top:10px;text-align:center;line-height:1.6;">{cap}<br>Photo: {au}, <a href="{l[1]}" target="_blank" rel="noopener" style="color:var(--enshu);">{l[0]}</a>, via Wikimedia Commons (resized)</figcaption></figure>')
def edit(SL,jobs):
    p=R+f'guides/{SL}/index.html'; s=open(p,encoding='utf-8').read()
    for anchor,items in jobs:
        assert s.count(anchor)==1,anchor
        h=''.join(mk(SL,*i[:6])+f'\n    <p>{i[6]}</p>' for i in items)
        s=s.replace(anchor,anchor+h)
    for tg in ['div','figure','picture','p','a','ul','li','details','section','h2']:
        assert len(re.findall(f'<{tg}[ >]',s))==len(re.findall(f'</{tg}>',s)),tg
    open(p,'w',encoding='utf-8').write(s)
edit('odawara-castle',[
("which fits the top-floor views described above.</p>",[
 ('keep-east','9e726809','Ymblanter','S4','The keep seen from low down beside the stone wall under a grey sky, with a gabled roof over the entrance level and a railing in front','The keep from the east, 14 April 2018.',
  'This is the other file from the same day, which I take to be the east view. The camera is close to the stone base and looks up, so the roofs stack above the gable at the entrance level. Under the grey sky the white walls and dark tiles stand out clearly. A few people are standing at the opening in the base, which gives a rough sense of scale. Compared with the sunny view from the southeast, this is the moodier way to see it.'),
 ('keep-pine-2024','6d69c51e','Akonnchiroll','B4','The white keep on its stone base on a clear winter day, with a large leaning pine on the left and bare trees on the right','The keep on a clear winter day, 14 February 2024.',
  'Commons titles this &ldquo;Odawara Castle in 2024.&rdquo; A big pine leans in from the left, bare branches frame the right side, and the keep sits on its stone base against a blue sky streaked with cloud. A few visitors are crossing the open ground below. It is a good reminder that this is a place for a winter walk as well as the cherry season. I cannot tell which species the trees on the right are, so please treat them as scenery.')]),
("it is a much quieter corner of the grounds.</p>",[
 ('gate-moat-2021','10507362','Suicasmo','S4','A white-walled gate with a tiled roof on a high stone base beside a moat, with a wooden bridge at the left and a tall pine behind','A gate beside the moat, 1 December 2021.',
  'Commons titles this only &ldquo;Odawara Castle Gate,&rdquo; so I do not name which gate it is. Low early light warms the white wall, a wooden bridge crosses the water at the left, and a tall pine rises behind the tiled roof. The stone base is tall, with the moat at its foot. It is a good example of how the castle is built from gate, wall and water working together.')]),
])
edit('kanazawa-castle',[
("Evening lighting varies by date, so please check the schedule above.</p>",[
 ('night-wall-pink','9a27c249','くろふね (Kurofune)','B4','A long stone wall lit in pink and orange at night, with a white turret and green-tiled roofs above it','The lit wall and turrets at night, 5 November 2022.',
  'The same evening, from a different spot. The stone wall at the bottom is washed with pink and orange light, and the white walls and green-tiled roofs above it glow in a cooler tone. The dark patterned lower walls under the windows show up well. Commons does not name the buildings, so I treat this as the turrets of the main group of buildings; please do not take that as a firm label.'),
 ('night-gate-side','c07fc2d7','くろふね (Kurofune)','B4','A two-storey gate with lit windows seen from the side, with a lit wooden bridge in the left foreground','The gate and its bridge seen from the side, 5 November 2022.',
  'This is the same gate as the front view above, seen from the side. The lit bridge runs along the left edge, with warm lights under its deck, and the gate stands behind with its windows glowing. Seen from here, the thickness of the stone base is easier to judge. As before, the name is my reading rather than Commons&rsquo;s.'),
 ('night-moon-turret','3ce2aa6b','くろふね (Kurofune)','B4','A lit white turret with a dark patterned lower wall at the right and a small tiled roof at the lower left, with a bright moon in a black sky','A turret under the moon, 5 November 2022.',
  'The moon sits high in a black sky at the upper left, and a lit turret fills the right side, with its dark square-patterned lower wall and layered roofs. The small tiled roof at the lower left is probably part of another structure, but Commons does not say which. Photos like this are only possible if you stay until dark, which is a good reason to plan the visit around the lighting.')]),
])
import csv
with open(R+'PHOTO-CREDITS.csv','a',encoding='utf-8',newline='') as f:
    w=csv.writer(f,lineterminator='\r\n'); [w.writerow(r) for r in rows]
print(len(rows))
