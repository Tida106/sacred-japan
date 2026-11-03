import re,csv,json
from PIL import Image
R='/home/claude/sacred-japan/'; A='/mnt/user-data/attachments/53e3d492-4bf8-5cd9-a0ec-63a7cbefb1d9/'
SL='okayama-castle'; D=R+f'guides/{SL}/images/'
S4=('CC BY-SA 4.0','https://creativecommons.org/licenses/by-sa/4.0/')
S3=('CC BY-SA 3.0','https://creativecommons.org/licenses/by-sa/3.0/')
B3=('CC BY 3.0','https://creativecommons.org/licenses/by/3.0/')
B2=('CC BY 2.0','https://creativecommons.org/licenses/by/2.0/')
B4=('CC BY 4.0','https://creativecommons.org/licenses/by/4.0/')
P=[
('turret','6e22afb6','663highland',S3,'A two-story white turret with gray tile roofs and a wooden upper level, on a stone base with a low white wall, under a deep blue sky','A surviving turret (Commons file uploaded 14 February 2008).',
 "This is one of the two turrets that came through the war. The lower walls are white plaster, the upper level is bare wood, and the roofs are gray tile with a curved gable, all on a low stone base with a white wall running off on both sides. Commons does not tell me which of the two turrets this is in the part of the description I could read, so I will not name it. Compare it with the descriptions above and the signs on site.",'survives','a'),
('night','ce2bf132','恭パパ',S4,'A castle keep lit in green at night above a field of hundreds of glowing paper lanterns, with a crowd of people and a stage below it','The keep lit up above a field of paper lanterns (Commons description: Okayama Castle Togokyo lighting, 14 August 2015).',
 "This is the castle after dark during a lantern event. The Commons description calls it the Okayama Castle Togokyo light-up, which I read as a seasonal event. The keep is washed in green, and thousands of paper lanterns glow on the lawn in front of it, with a crowd and a small stage under the walls. Events like this change from year to year, so check the dates before you plan around one.",'evening','b'),
('korakuen-spring','ffeb393d','Fjkelfeimvvn',B3,'A still pond reflecting a green grassy hill with pink and white azaleas and a small stone bridge, with a black castle keep above the trees','Korakuen and the keep from the pond, 9 May 2010.',
 "Korakuen is the garden next door, and this is why I pair the two. Commons says it was built in 1700 by Ikeda Tsunamasa, lord of the Okayama clan, and calls the black building the keep of Okayama Castle. The Japanese description says the view is from the shore of Sawa no Ike pond, looking at Yuishinzan hill and the keep. In early May the azaleas on the hill are pink and white, and the whole scene is doubled in the water.",'visit','c'),
('korakuen-autumn','1e57f708','Zairon',B4,'A black castle keep rising above green and orange trees behind a grassy hill, a small bridge and a pond, framed by pine branches at the right','Korakuen with the keep above the trees, 20 October 2023.',
 "The same garden in late October looks very different. The keep is a small dark shape between the trees, a few leaves have turned orange, and pine branches frame the right side. Commons gives only the date and says it is Koraku-en Garden, so it is a good guide to what to expect at that time of year, with the caveat that peak color comes later.",'visit','c'),
('tsukimi-bridge','0fdab0be','George N',B2,'A pale steel truss bridge crossing a green river toward a wooded bank, with a small cafe and rowing boats at the right under a blue sky with clouds','Tsukimi Bridge, 18 August 2016.',
 "Commons titles this Tsukimi Bridge, and Jeepe lists it as the link between the castle and Korakuen. It is a steel truss bridge, pale gray, crossing the river with a wooded bank behind it, and a small cafe and a row of boats sit at the right. The photo was taken in August, and the green water and strong sun are what summer looks like here.",'visit','c'),
]
def fig(k,au,lic,alt,cap,im):
    img=f'<picture><source srcset="/guides/{SL}/images/{k}.webp" type="image/webp"><img src="/guides/{SL}/images/{k}.jpg" alt="{alt}" width="{im.width}" height="{im.height}" loading="lazy" style="width:100%;height:auto;border-radius:4px;display:block;"></picture>'
    fc=f'<figcaption style="font-size:13px;color:var(--enshu);margin-top:10px;text-align:center;line-height:1.6;">{cap}<br>Photo: {au}, <a href="{lic[1]}" target="_blank" rel="noopener" style="color:var(--enshu);">{lic[0]}</a>, via Wikimedia Commons (resized)</figcaption>'
    return img,fc
p=R+f'guides/{SL}/index.html'; s=open(p,encoding='utf-8').read()
blocks={'a':'','b':'','c':''}; rows=[]
for k,f,au,lic,alt,cap,ps,g,_ in P:
    im=Image.open(A+f+'-image.jpg').convert('RGB')
    if im.width>1200: im=im.resize((1200,round(im.height*1200/im.width)),Image.LANCZOS)
    im.save(D+k+'.jpg',quality=84,optimize=True); im.save(D+k+'.webp',quality=80)
    img,fc=fig(k,au,lic,alt,cap,im)
    blocks[_]+=f'\n    <figure style="margin:28px auto;max-width:760px;">{img}{fc}</figure>\n    <p>{ps}</p>'
    rows.append([f'guides/{SL}',f'/guides/{SL}/images/{k}.jpg',lic[0],lic[1],lic[1],cap+f' Photo: {au}, {lic[0]}, via Wikimedia Commons (resized)'])
a='so I will not put a name on it.</p>'; assert s.count(a)==1; s=s.replace(a,a+blocks['a'])
a='though I cannot tell you what they are.</p>'; assert s.count(a)==1; s=s.replace(a,a+blocks['b'])
i=s.index('</ul>',s.index('id="visit"'))+5; s=s[:i]+blocks['c']+s[i:]
open(p,'w',encoding='utf-8').write(s)
with open(R+'PHOTO-CREDITS.csv','a',encoding='utf-8',newline='') as f: csv.writer(f,lineterminator='\r\n').writerows(rows)
for tg in ['div','figure','picture','p','a','ul','li','details','section','h2']:
    assert len(re.findall(f'<{tg}[ >]',s))==len(re.findall(f'</{tg}>',s)),tg
for m in re.findall(r'<script type="application/ld\+json">(.*?)</script>',s,re.S): json.loads(m)
print('ok',s.count('<figure'))
