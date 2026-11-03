import re,csv,json
from PIL import Image
R='/home/claude/sacred-japan/'; A='/mnt/user-data/attachments/53e3d492-4bf8-5cd9-a0ec-63a7cbefb1d9/'
SL='hiroshima-castle'; D=R+f'guides/{SL}/images/'
L={'BY4':('CC BY 4.0','https://creativecommons.org/licenses/by/4.0/'),'S4':('CC BY-SA 4.0','https://creativecommons.org/licenses/by-sa/4.0/')}
def fig(k,f,au,lic,alt,cap,para):
    im=Image.open(A+f+'-image.jpg').convert('RGB')
    if im.width>1200: im=im.resize((1200,round(im.height*1200/im.width)),Image.LANCZOS)
    im.save(D+k+'.jpg',quality=84,optimize=True); im.save(D+k+'.webp',quality=80)
    l=L[lic]; mw='420px' if im.height>im.width else '760px'
    img=f'<picture><source srcset="/guides/{SL}/images/{k}.webp" type="image/webp"><img src="/guides/{SL}/images/{k}.jpg" alt="{alt}" width="{im.width}" height="{im.height}" loading="lazy" style="width:100%;height:auto;border-radius:4px;display:block;"></picture>'
    fc=f'<figcaption style="font-size:13px;color:var(--enshu);margin-top:10px;text-align:center;line-height:1.6;">{cap}<br>Photo: {au}, <a href="{l[1]}" target="_blank" rel="noopener" style="color:var(--enshu);">{l[0]}</a>, via Wikimedia Commons (resized)</figcaption>'
    rows.append([f'guides/{SL}',f'/guides/{SL}/images/{k}.jpg',l[0],l[1],l[1],cap+f' Photo: {au}, {l[0]}, via Wikimedia Commons (resized)'])
    return f'\n    <figure style="margin:28px auto;max-width:{mw};">{img}{fc}</figure>\n    <p>{para}</p>'
rows=[]
gate=fig('main-gate','e3d4a3e3','Jakub Hałun','BY4','A gatehouse with a tiled roof and white walls beside a corner of stone wall, with a wooden bridge at the left, a moat in front and tall buildings behind under a blue sky',
 'The Main Gate and its bridge across the moat, 17 August 2024.',
 "Commons titles this the Main Gate of Hiroshima Castle, and it shows the reconstructed gate with its wooden bridge, the tower-like corner structure on the stone base and the long walls running away to the left. This is the entrance side of the Ninomaru that I described above. The stone corner is worth a look, because it is the part that is original, and the timber above it was rebuilt in the 1990s. Commons marks the photo as a Quality image.")
shrine='\n\n    <h3>Hiroshima Gokoku Shrine<span class="h2-jp"> 広島護国神社</span></h3>\n    <p>The shrine inside the inner moat is a working shrine, and it is worth a short stop if you are already at the castle. Gokoku shrines honor those who died in service of the country, so I would keep voices low and photos respectful. The pictures below show the approach, the main hall and some of the details that visitors notice.</p>'
shrine+=fig('gokoku-torii','1b1f5dd1','そらみみ','S4','A large white granite torii with a nameplate, with the shrine main hall visible beyond it under a deep blue sky',
 'The stone torii and the main hall behind it, 11 March 2017.',
 "Commons describes this simply as the torii of Hiroshima Gokoku Shrine. It is a large granite torii, with the shrine's name on the plaque at the top, and the main hall sits straight ahead at the end of the paved approach. The signboards and the guardian lion-dog statues on either side are the usual small details of a shrine front.")
shrine+=fig('gokoku-torii-inside','efbc2eab','Hyppolyte de Saint-Rambert','BY4','A large granite torii seen from the shrine side, with stalls selling fortune slips at the left, a delivery truck and a tall apartment tower beyond',
 'The torii with New Year stalls and the city behind it, 11 January 2024.',
 "This shows how close the shrine sits to the modern city: through the torii you can see a delivery truck and a tall tower block. The stall at the left sells omikuji fortune slips, which suggests a New Year period. The vertical inscription on the right pillar appears to read as a commemoration of an enthronement ceremony in the second year of Heisei, but I could not read it with full confidence. It may be the same torii as in the previous picture, seen from the other side, but I cannot confirm that.")
shrine+=fig('gokoku-chozuya','a53c2164','Hyppolyte de Saint-Rambert','BY4','A purification fountain under a green copper roof supported by two pale pillars, with tents and a red-and-white curtain behind it',
 'The purification fountain, 11 January 2024.',
 "The water pavilion has a green copper roof and two thick pillars, and the basin is where visitors rinse their hands before approaching the hall. Behind it you can see tents being set up with red-and-white curtains and banners that read as the first shrine visit of the year. A sign on the pavilion appears to say that the night-time water supply is stopped, so please take it as a picture from a particular day.")
shrine+=fig('gokoku-haiden-people','f41c4372','Hyppolyte de Saint-Rambert','BY4','The front of a shrine hall with a green roof, a large plaque reading the year of the dragon, people praying at the front and two workers raking gravel in the foreground',
 'The front of the main hall with worshippers and workers, 11 January 2024.',
 "Worshippers stand in front of the hall, while in the foreground two workers rake the gravel, which gives a sense of how much daily care a shrine needs. The large plaque at the front reads 甲辰, the sexagenary cycle name for 2024, the year of the dragon, and a dragon image hangs above the offering area. A bronze carp stands at each end of the platform.")
shrine+=fig('gokoku-haiden','3e827712','Madhav Sharma','S4','A wide view of the shrine hall with colorful hanging streamers, two shrine maidens in white and red and a priest sweeping in front, behind a paved path and dark gravel',
 'The main hall in summer, 23 June 2016.',
 "This wide view down the paved path shows the hall in a calmer season. Two shrine maidens in red and white and a priest are sweeping in front of it, with colored streamers hanging from the eaves. Commons describes it as Hiroshima Gokoku-jinja. The two pictures of the hall show how different the same place can look in winter and in summer.")
shrine+=fig('gokoku-carp','8b316a5d','Hyppolyte de Saint-Rambert','BY4','A bronze statue of a carp leaping up out of stylized waves, with votive plaques and signboards behind it',
 'The bronze carp statue, 11 January 2024.',
 "The carp that leaps up out of the waves is one of the shrine's best-known sights. The Japanese sign behind it appears to explain the old legend of a carp that climbs a waterfall at the Dragon Gate and becomes a dragon, and that fits the dragon year plaque in the earlier picture. The English notice at the bottom warns that the bronze can be hot when it is sunny, which is a practical tip.")
p=R+f'guides/{SL}/index.html'; s=open(p,encoding='utf-8').read()
a='which is how many residents see it.</p>'; assert s.count(a)==1; s=s.replace(a,a+gate)
b='I would read the numbers as approximate and the trees as real.</p>'; assert s.count(b)==1; s=s.replace(b,b+shrine)
open(p,'w',encoding='utf-8').write(s)
with open(R+'PHOTO-CREDITS.csv','a',encoding='utf-8',newline='') as fh:
    w=csv.writer(fh,lineterminator='\r\n')
    for r in rows: w.writerow(r)
for tg in ['div','figure','picture','p','a','ul','li','details','section','h2','h3']:
    assert len(re.findall(f'<{tg}[ >]',s))==len(re.findall(f'</{tg}>',s)),tg
for m in re.findall(r'<script type="application/ld\+json">(.*?)</script>',s,re.S): json.loads(m)
print('ok',s.count('<figure'))
