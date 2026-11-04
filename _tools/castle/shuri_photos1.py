import re,csv,json,os
from PIL import Image
R='/home/claude/sacred-japan/'; A='/mnt/user-data/attachments/53e3d492-4bf8-5cd9-a0ec-63a7cbefb1d9/'
SL='shuri-castle'; D=R+f'guides/{SL}/images/'; os.makedirs(D,exist_ok=True)
L={'S4':('CC BY-SA 4.0','https://creativecommons.org/licenses/by-sa/4.0/'),
   'S3':('CC BY-SA 3.0','https://creativecommons.org/licenses/by-sa/3.0/'),
   'B3':('CC BY 3.0','https://creativecommons.org/licenses/by/3.0/'),
   'B4':('CC BY 4.0','https://creativecommons.org/licenses/by/4.0/')}
HERO=('shureimon','d5a42ded','Suicasmo','S4','Shureimon Gate, a two-tier red gate with orange tiled roofs and a gold-lettered plaque, seen from the front with a few visitors walking beyond it','Shureimon Gate, 11 February 2015.')
SEE1="and says the paid zone begins beyond Hoshinmon Gate.</p>"
SEE2="were largely untouched by the fire.</p>"
SEE3="construction can change the route (Japan Ode).</p>"
FIRE="so I will not give one.</p>"
SEID="Japan Ode says each purchase can cover up to nine tickets.</p>"
P=[
(SEE1,[('plaque','596e00d3','Hiroki Ogawa','B3','Close-up of the gold-lettered plaque above Shureimon, reading right to left, with round decorated roof tile ends below it','The plaque of Shureimon Gate.',
 "Commons describes this as the plaque of Shureimon Gate in Naha, and it was originally posted to Panoramio in April 2016. Read right to left, the four large gold characters are the &ldquo;Shurei no kuni&rdquo; plaque described above, the Land of Propriety. Below it you can see the round ends of the roof tiles, each stamped with a flower design. The gold leaf is worn in places, which is part of the charm of a plaque that has been hanging in the weather for a long time.")]),
 (SEE1,[('shureimon-sunset','9dbab144','Kennagata','S4','People in summer kimono raising their arms under Shureimon Gate while the setting sun glows through the gate','Shureimon at sunset, 27 April 2019.',
 "Commons says this was taken on 27 April 2019, before the fire destroyed the castle, and notes that the gate escaped the fire. Its caption describes a folk dance in traditional Ryukyu and Japanese costume, and the photo shows a group of people in kimono raising their arms under the gate as the sun sets behind it. I include it because it shows the gate as a place where people actually gather, not only as a monument.")]),
(SEE2,[('kankaimon','e06f06e6','Suicasmo','S4','Kankaimon Gate, a stone arch with a weathered wooden gatehouse, a framed signboard and two stone guardian lions at its base','A stone gate with a signboard and two guardian lions.',
 "Commons titles this only &ldquo;Gates of Shuri Castle,&rdquo; but the signboard above the arch appears to read &ldquo;Kankaimon,&rdquo; the Welcome Gate, so I am treating it as that gate. It is a good example of the other side of Shuri's architecture: pale limestone, a rounded arch, and a plain gatehouse of weathered wood. Two stone guardian lions sit at the foot of the walls, and beyond the arch you can see the path climbing toward the next gate."),
 ('zuisenmon','273afa8e','Zairon','B4','Zuisenmon Gate, a red gatehouse resting on a limestone gate base between curved stone walls, in front of cycad plants','Zuisen Gate, 26 October 2023.',
 "Commons labels this Zuisen Gate, the gate named in K005 Powerspot's list of free areas. It is a different picture from Kankaimon: the gatehouse is lacquered red, with gold brackets and a small signboard, and it sits above a limestone gate base between two curved stone walls. The cycad plants in the foreground are a typical sight around the castle. I took the red gatehouse as a sign that this part was rebuilt, but I have not confirmed its date, so please check on site.")]),
(SEE3,[('kobikimon','2bd18485','663highland','S3','A curved grey limestone wall with a plain arched passage and an empty paved square in front of it, under a deep blue sky','Kobiki Gate, 27 July 2011.',
 "Commons titles this Kobiki Gate of Shuri Castle. It is nothing like the red gates: there is no gatehouse, only a rounded arch cut into a curving wall of grey limestone, with an empty paved square in front of it. I include it because walls like this are the real subject of the castle's World Heritage listing mentioned above. The photo is from 2011, so the surroundings may have changed."),
 ('kyukeimon','e045d1a3','Zairon','B4','Kyukeimon Gate, a weathered wooden gatehouse with a red signboard above a stone arch, with a small stairway leading up to it','Kyukei Gate, 26 October 2023.',
 "Commons labels this Kyukei Gate. The signboard has red and gold characters that appear to read &ldquo;Kyukeimon,&rdquo; and the gatehouse is grey, aged wood, quite unlike the red structures nearby. A short stair rises to a limestone arch, and through the arch you can see cycads in a small garden. I did not find this gate in the sources I used for the visiting details, so please check the park map on the day."),
 ('courtyard-hoshinmon','28d45b41','そらみみ (Soramimi)','S4','A large paved courtyard with red and grey stripes in front of a long red building with tiled roofs, under a cloudy sky','The courtyard and the red gate building, 15 March 2015.',
 "The Japanese caption on Commons reads &ldquo;Shuri Castle, the Unaa courtyard and Hoshinmon Gate.&rdquo; The courtyard is paved in red and grey stripes, and visitors in the photo give a sense of its size. This picture is from 2015, before the fire; Wikipedia says the main hall was destroyed in 2019, and it stood on the far side of the courtyard from this gate. The paved courtyard is part of what you walk across before you reach the main hall.")]),
(FIRE,[('throne','8679c967','CEphoto, Uwe Aranas','S3','The gold dragon-flanked throne of the Ryukyu kings in the main hall, with a gold-lettered plaque on a red and black lacquer background above it','The throne in the main hall, before the 2019 fire.',
 "This is the throne room as it looked on 10 January 2016, before the 2019 fire. Commons describes a throne in the Seiden, and says that the plaque above it carries the calligraphy of the Kangxi Emperor and reads &ldquo;Chuzan seido.&rdquo; Gold dragons stand either side of a red lacquer chair, and the dragon motif repeats on the beams and columns. I cannot say how the rebuilt hall will compare in detail, so please treat this as a picture of the earlier building.")]),
(SEID,[('hoshinmon','4555b6f7','CEphoto, Uwe Aranas','S3','The front of Hoshinmon Gate, a wide red building with a central doorway, stone steps and a gold-lettered plaque above the opening','Hoshinmon Gate, January 2016.',
 "Commons describes this as the entrance gate to the inner yard of Shuri Castle, and the plaque over the doorway appears to read &ldquo;Hoshin,&rdquo; so I am treating it as Hoshinmon. It is the gate where the ticket page says visitors with an interior reservation show their QR code. Stone steps lead up to a doorway, with guardian lions on the posts beside them, and through the opening you can see the red and gold facade of the building beyond. The photo is from 2016, so queue markers and signs will look different today.")]),
]
rows=[];sizes={}
def mk(k,f,au,lic,alt,cap,hero):
    im=Image.open(A+f+'-image.jpg').convert('RGB')
    if im.width>1200: im=im.resize((1200,round(im.height*1200/im.width)),Image.LANCZOS)
    im.save(D+k+'.jpg',quality=84,optimize=True); im.save(D+k+'.webp',quality=80)
    l=L[lic]; ld='eager' if hero else 'lazy'
    st=('width:100%;max-height:420px;object-fit:cover;object-position:center 30%;border-radius:4px;display:block;' if hero else 'width:100%;height:auto;border-radius:4px;display:block;')
    img=f'<picture><source srcset="/guides/{SL}/images/{k}.webp" type="image/webp"><img src="/guides/{SL}/images/{k}.jpg" alt="{alt}" width="{im.width}" height="{im.height}" loading="{ld}" style="{st}"></picture>'
    fc=f'<figcaption style="font-size:13px;color:var(--enshu);margin-top:10px;text-align:center;line-height:1.6;">{cap}<br>Photo: {au}, <a href="{l[1]}" target="_blank" rel="noopener" style="color:var(--enshu);">{l[0]}</a>, via Wikimedia Commons (resized)</figcaption>'
    sizes[k]=im.size
    rows.append([f'guides/{SL}',f'/guides/{SL}/images/{k}.jpg',l[0],l[1],l[1],cap+f' Photo: {au}, {l[0]}, via Wikimedia Commons (resized)'])
    return img,fc
p=R+f'guides/{SL}/index.html'; s=open(p,encoding='utf-8').read()
k,f,au,lic,alt,cap=HERO
img,fc=mk(k,f,au,lic,alt,cap,True)
a='  <!-- TABLE OF CONTENTS -->'; assert s.count(a)==1
s=s.replace(a,f'  <figure style="margin:0 0 48px;">{img}{fc}</figure>\n\n'+a)
merged={}
for anc,g in P: merged.setdefault(anc,[]).extend(g)
for anc,g in merged.items():
    html=''
    for (k,f,au,lic,alt,cap,para) in g:
        img,fc=mk(k,f,au,lic,alt,cap,False)
        mw='420px' if sizes[k][1]>sizes[k][0] else '760px'
        html+=f'\n    <figure style="margin:28px auto;max-width:{mw};">{img}{fc}</figure>\n    <p>{para}</p>'
    assert s.count(anc)==1,anc; s=s.replace(anc,anc+html)
open(p,'w',encoding='utf-8').write(s)
with open(R+'PHOTO-CREDITS.csv','a',encoding='utf-8',newline='') as fh:
    w=csv.writer(fh,lineterminator='\r\n')
    for r in rows: w.writerow(r)
for tg in ['div','figure','picture','p','a','ul','li','details','section','h2']:
    assert len(re.findall(f'<{tg}[ >]',s))==len(re.findall(f'</{tg}>',s)),tg
for m in re.findall(r'<script type="application/ld\+json">(.*?)</script>',s,re.S): json.loads(m)
print('ok',s.count('<figure'),sizes)
