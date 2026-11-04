import re,csv,json,os
from PIL import Image
R='/home/claude/sacred-japan/'; A='/mnt/user-data/attachments/53e3d492-4bf8-5cd9-a0ec-63a7cbefb1d9/'
SL='odawara-castle'; D=R+f'guides/{SL}/images/'; os.makedirs(D,exist_ok=True)
L={'B2':('CC BY 2.0','https://creativecommons.org/licenses/by/2.0/'),
   'B3':('CC BY 3.0','https://creativecommons.org/licenses/by/3.0/'),
   'S2':('CC BY-SA 2.0','https://creativecommons.org/licenses/by-sa/2.0/'),
   'S3':('CC BY-SA 3.0','https://creativecommons.org/licenses/by-sa/3.0/'),
   'S4':('CC BY-SA 4.0','https://creativecommons.org/licenses/by-sa/4.0/'),
   'C0':('CC0 1.0','https://creativecommons.org/publicdomain/zero/1.0/'),
   'PD':('Public domain (released by the author)','https://commons.wikimedia.org/wiki/Template:PD-user')}
J='-image.jpg'
HERO=('keep-blue-sky','719a43b0','663highland','S3','The white three-tier keep of Odawara Castle on a tall stone base under a deep blue sky, with visitors walking in the courtyard below','The reconstructed keep on a clear day, 23 December 2016.')
KEEP=[
('keep-sunset','e886051a','Agustin Rafael Reyes','B2','The keep seen from below at sunset, with glowing yellow windows against a vivid blue, pink and orange sky and dark pine trees','The keep at sunset, 7 August 2010.',
 "The photographer writes on Commons that he kept his friends waiting just to shoot a sunset shot of the castle. The colors look strongly processed, with a more intense sky than you will usually see, so please treat it as a mood picture rather than a guide to the real light. What it does show clearly is the shape: a stone base, then a white keep with several layers of tiled roofs and triangular gables, and a small figure on top. The windows are lit because it is evening, but I have no source for evening opening, so check the hours above."),
('keep-southeast','f6e51621','Ymblanter','S4','The white keep with layered gabled roofs rising above a stone base, seen from low down under a cloudy sky, with trees at the right','The keep from the southeast, 14 April 2018.',
 "Commons has two files of the keep from 14 April 2018 by this photographer, one from the southeast and one from the east, and I believe this is the southeast view, though I cannot match the file to the time stamp with certainty. Standing this low you can see why the keep feels taller than its modest size. The stone base rises in a gentle curve, and each roof level has its own gable. A small viewing gallery runs around the upper floor, which fits the top-floor views described above."),
('tokiwagi-gate','49165250','KENPEI','S4','A white-walled gate building with a dark wooden lattice window and tiled eaves above a stone stairway, with visitors walking up and down','The Tokiwagi Gate, 7 June 2015.',
 "Commons titles this as the Tokiwagi Gate, taken on 7 June 2015. This is the building that japan-guide, which spells it Tokiwaki, says holds the Samurai Museum, so it is the gate you pass or use on the way to the keep. A dark lattice window sits above the passage, and visitors on the stairs give a sense of scale. I have not checked which entrance is used for the museum today, so please follow the signs on site.")]
GATES=[
('akagane-gate-close','109b7340','KENPEI','S4','A wide double wooden gate with lattice-patterned doors and metal studs under a white wall and tiled eaves, framed by large stone blocks','The Akagane Gate, 7 June 2015.',
 "This is the Akagane (copper) Gate, one of the main gates into the castle, photographed on 7 June 2015. The doors are made of tall wooden slats with rows of metal studs, set between thick stone walls. Through the passage you can see green trees beyond. It is a good place to look at how a castle gate is built to slow an attacker down."),
('akagane-gate-approach','f979faae','Kicho-66','S3','A tiled gate building with a white upper story and a wooden double gate, seen from a wide gravel slope under a blue sky','The Akagane Gate, 1 February 2008.',
 "The Japanese description on Commons calls this the Akagane Gate, the front gate of the Ninomaru enclosure, and says it was restored in 1997 (Heisei 9). That fits what japan-guide says about the main gates being restored in the years after the keep. The photo, taken on 1 February 2008, is a low-resolution file, so it is shown here at its original size."),
('akagane-gate-moat','8084009f','Ymblanter','S4','A white gate tower on a high stone wall above a moat, with a gravel area, a large rock and a wooden information sign in front, under a dark cloudy sky','The Akagane Gate across the moat, 14 April 2018.',
 "Commons gives this as the Akagane Gate seen from the southeast. The wooden sign at the right reads Akaganemon with opening hours that I read as 7:00 am to 9:00 pm and a lighting time from sunset until 10:00 pm. That sign is from 2018 and I have not seen a current one, so please check the hours on the day. The tall stone wall and the moat show how the gate was meant to be reached only along a narrow route."),
('umadashi-gate','306546c7','Ymblanter','S4','A small wooden gate with a tiled roof between white walls with triangular and square openings, in front of a gravel yard and pine trees','The Umadashi Gate, 14 April 2018.',
 "Commons titles this the Umadashi Gate seen from the east, taken on 14 April 2018. The white walls on both sides have small square and triangular openings, which are loopholes for defenders. The gate itself is plain, with a simple tiled roof, and the yard in front is open gravel. A wooden sign stands at the left. Compared with the big Akagane Gate, it is a much quieter corner of the grounds."),
('castle-entrance','bf7a3378','Alvinz','C0','A tiled wooden gate with decorated end tiles between white walls and a stone base, with a second gate roof and a wall behind it and a stone wall in the foreground','A gate at the castle entrance, 13 July 2018.',
 "The Chinese caption on Commons says this is the entrance of Odawara Castle in July 2018. It shows a small tiled gate between white walls, with another roof and wall visible beyond it. The decorated end tiles on the ridge are worth a closer look. I do not know which named gate this is, so I describe only what the caption says."),
('sumiyoshi-bridge','21d30c32','妖精書士','C0','A wooden bridge crossing a moat to a gate under a white tower on a stone wall, with pines and a mossy bank under a cloudy sky','The bridge at the Akagane Gate, 17 March 2020.',
 "The Japanese caption on Commons calls this the Sumiyoshi Bridge, which spans the moat at the Akagane Gate, photographed on 17 March 2020. The orange cones on the bridge suggest some kind of work or control when it was taken, and I do not know what for. The moat water and the stone walls give a good idea of the setting. The still water also reflects the white tower above.")]
SAKURA=[
('sakura-crowd','5bb27813','Σ64','B3','The keep rising above a stone wall with a large cherry tree in bloom beside it, with crowds of visitors and food stalls in the courtyard under a clear sky','Cherry blossom time at the keep, 1 April 2018.',
 "Commons gives this as the castle taken on 1 April 2018, and the crowd and the food stalls suggest a blossom weekend, with people on the viewing gallery at the top of the keep. The cherry tree is in full flower and its white-pink color looks lovely against the white walls. This is one day, so I would not read the date as a promise for any year. If you want a quiet visit, the park is probably better on a weekday morning, but that is my suggestion, not a fact from a source."),
('view-from-castle','036c12af','江戸村のとくぞう','S4','A high view over green trees and cherry blossoms to the town, the harbor and the sea, with mountains on the right under a hazy sky','Cherry trees and the sea, 4 April 2009.',
 "The caption on Commons is just Odawara Castle, taken on 4 April 2009. From the height it looks to have been taken from the keep, though that is my reading and not something the file says. Cherry trees in bloom fill the foreground, and beyond the town you can see the sea and the hills along the coast. It fits japan-guide&rsquo;s note that the top floor has views over the park and the city.")]
rows=[];sizes={}
def mk(k,f,au,lic,alt,cap,hero):
    im=Image.open(A+f+J).convert('RGB')
    if im.width>1200: im=im.resize((1200,round(im.height*1200/im.width)),Image.LANCZOS)
    im.save(D+k+'.jpg',quality=84,optimize=True); im.save(D+k+'.webp',quality=80)
    l=L[lic]; ld='eager' if hero else 'lazy'
    st=('width:100%;max-height:420px;object-fit:cover;object-position:center 30%;border-radius:4px;display:block;' if hero else 'width:100%;height:auto;border-radius:4px;display:block;')
    img=f'<picture><source srcset="/guides/{SL}/images/{k}.webp" type="image/webp"><img src="/guides/{SL}/images/{k}.jpg" alt="{alt}" width="{im.width}" height="{im.height}" loading="{ld}" style="{st}"></picture>'
    fc=f'<figcaption style="font-size:13px;color:var(--enshu);margin-top:10px;text-align:center;line-height:1.6;">{cap}<br>Photo: {au}, <a href="{l[1]}" target="_blank" rel="noopener" style="color:var(--enshu);">{l[0]}</a>, via Wikimedia Commons (resized)</figcaption>'
    sizes[k]=im.size
    rows.append([f'guides/{SL}',f'/guides/{SL}/images/{k}.jpg',l[0],l[1],l[1],cap+f' Photo: {au}, {l[0]}, via Wikimedia Commons (resized)'])
    return img,fc
def block(g):
    html=''
    for (k,f,au,lic,alt,cap,para) in g:
        img,fc=mk(k,f,au,lic,alt,cap,False)
        mw='420px' if sizes[k][1]>sizes[k][0] else '760px'
        html+=f'\n    <figure style="margin:28px auto;max-width:{mw};">{img}{fc}</figure>\n    <p>{para}</p>'
    return html
p=R+f'guides/{SL}/index.html'; s=open(p,encoding='utf-8').read()
def put(anc,html):
    global s
    assert s.count(anc)==1,anc; s=s.replace(anc,anc+html)
img,fc=mk(*HERO,True)
tocm='  <!-- TABLE OF CONTENTS -->'
assert s.count(tocm)==1
s=s.replace(tocm,f'  <figure style="margin:0 0 48px;">{img}{fc}</figure>\n\n'+tocm)
a=s.index('Jeepe also lists an armor-dressing experience'); b=s.index('</p>',a)+4
anc=s[a:b]
# keep photos: first two after the keep paragraph (before museum paragraph); tokiwagi after museum paragraph
k1="and the top floor has views over the park and the city.</p>"
put(k1,block(KEEP[:2]))
put(anc,block(KEEP[2:]))
put("is a ten-minute walk from the station.</p>",block(GATES))
put("The city page also names plum, cherry and hydrangea.</p>",block(SAKURA))
open(p,'w',encoding='utf-8').write(s)
import re
for tg in ['div','figure','picture','p','a','ul','li','details','section','h2']:
    assert len(re.findall(f'<{tg}[ >]',s))==len(re.findall(f'</{tg}>',s)),tg
for m in re.findall(r'<script type="application/ld\+json">(.*?)</script>',s,re.S): json.loads(m)
with open(R+'PHOTO-CREDITS.csv','a',newline='',encoding='utf-8') as f:
    w=csv.writer(f,lineterminator='\r\n'); [w.writerow(r) for r in rows]
print(len(rows),'photos',sizes)
