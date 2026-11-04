import re,csv,json,os
from PIL import Image
R='/home/claude/sacred-japan/'; A='/mnt/user-data/attachments/53e3d492-4bf8-5cd9-a0ec-63a7cbefb1d9/'
SL='takeda-castle-ruins'; D=R+f'guides/{SL}/images/'; os.makedirs(D,exist_ok=True)
L={'S2':('CC BY-SA 2.0','https://creativecommons.org/licenses/by-sa/2.0/'),
   'S3':('CC BY-SA 3.0','https://creativecommons.org/licenses/by-sa/3.0/'),
   'S4':('CC BY-SA 4.0','https://creativecommons.org/licenses/by-sa/4.0/'),
   'C0':('CC0 1.0','https://creativecommons.org/publicdomain/zero/1.0/'),
   'PD':('Public domain (released by the author)','https://commons.wikimedia.org/wiki/Template:PD-user')}
J='-image.jpg'
HERO=('sunrise-cloud-sea','d7c2c9c1','bullets95','S2','Stone wall terraces and pine trees on a ridge at sunrise, with a sea of clouds filling the valley and mountains beyond','A sea of clouds around the ruins at sunrise, 5 December 2010.')
STONE=[('survey-marker','21a55795','Baku13','S3','A tall granite marker carved with the characters for Takeda Castle Ruins and Hyogo Prefecture, standing in green undergrowth below a stone wall','The marker at the foot of the ruins, 7 May 2013.',
 "Commons titles this only as Takeda Castle, taken on 7 May 2013. The carved characters read &ldquo;Takeda-jo-seki&rdquo; (Takeda Castle Ruins) with the word for historic site above and &ldquo;Hyogo Prefecture&rdquo; below, which is how a designated historic site is usually labelled. Behind it you can see the edge of a stone wall above the slope. It is a small thing, but it is a good reminder that the stone here is protected, so please stay on the paths.")]
WALLS=[
('aerial-south-ninomaru','8e19f88c','ブレイズマン (Blazeman)','PD','Looking down from the highest platform onto stepped stone terraces and a gate passage, with a river valley and a road far below','The south terraces seen from the keep platform, 15 April 2009.',
 "This view looks down from the keep platform onto the southern enclosures. The Japanese description on Commons, which I translate here, says that each gate passage has a turret base on both sides, with the gate between them under a long turret, and that the routes bend several times. You can see that zigzag in the stone: no passage runs straight. The tree with the reddish tint at the center is, I believe, a cherry not yet in bloom, which fits the April date."),
('aerial-south-may','5c96a160','Baku13','S3','A similar view of the stepped stone terraces from above in spring green, with a pine on the far platform and a long valley beyond','The same area in May, 7 May 2013.',
 "Commons labels this view as the south enclosures, taken on 7 May 2013. Compare it with the April photo: the mountains are fully green and the stone is the same. The pines on the far platform and the road in the valley give a sense of how high this ridge stands above the town."),
('path-between-walls','0c7d6baf','Brakeet','C0','A visitor walks up a dirt path between two high stone walls toward a stepped terrace with trees','A path between the walls, 5 May 2011.',
 "A visitor climbs a dirt path between rough stone walls toward a higher terrace. The photo was taken on 5 May 2011 at 15:47, and Commons gives only the general description of Takeda Castle. The walls are built of irregular stones fitted together rather than cut blocks, which is why they look so rugged. Because of the ridge&rsquo;s shape, paths like this one run between walls rather than across open ground."),
('keep-platform-from-south','98524c2d','ブレイズマン (Blazeman)','PD','Stepped stone walls rising to a keep platform under a blue sky, with a visitor standing on a wall at the left','The keep platform seen from the south enclosure, 15 April 2009.',
 "Commons says this was taken from the south enclosure and shows the keep platform; the Japanese caption calls it the tenshudai. A visitor stands on the wall edge at the left, and two more are on the top terrace, which helps with scale. The nearer walls are layered, with each terrace set back from the one below."),
('keep-platform-from-sannomaru','e7e45d5b','ブレイズマン (Blazeman)','PD','The terraced stone walls of the keep platform with bare cherry trees, seen from below under a blue sky','The keep platform from the third enclosure, 15 April 2009.',
 "The description says this was taken from the third enclosure (the sannomaru). From here the keep platform looks like a stepped pyramid of stone, with leafless cherry trees on the terraces in mid-April. It gives a good idea of how the castle rises in layers up the ridge."),
('ruins-from-opposite-slope','ab5246df','Brakeet','C0','A tall stone-walled ruin on a ridge above green forest, with a few tiny visitors on top and hills behind','The ruins from across the valley, 5 May 2011.',
 "Taken on 5 May 2011 at 16:10, this shows the walls from a distance, with several tiny visitors on the top that show how large the stone work is. In spring the ridge is green, so the walls stand out against the trees. I do not know exactly where it was taken from, so please treat it as an example of the view from outside.")]
CLOUDS=[
('autumn-mist','c20f14c1','Norio NAKAYAMA','S2','Mist drifting across a ridge of stone walls above a hillside of orange and green autumn trees','Mist and autumn color below the ruins, 16 November 2011.',
 "The source title on Commons says this was taken at Ritsuun-kyo, the viewpoint opposite the castle, on 16 November 2011 at 08:08. The cloud here is thin and moving, not a flat sea. The hillside below is turning yellow and orange, and the sun lights the walls. If you hope for the classic cloud-sea photo, remember that you may also get a morning like this one, which has its own beauty."),
('snow-cloud-sea','2e256c0a','Hiroaki Kaneko','S3','Snow-covered stone wall terraces and bare trees above a thin sea of clouds, with mountains and a deep blue sky behind','The ruins under snow with a sea of clouds, 24 December 2011.',
 "Commons gives this as the Takeda Castle site in winter with a sea of clouds, taken on 24 December 2011, and lists a camera position on the ruins. The walls and terraces have a thin cover of fresh snow and a few visitors are on the walls. This is the short winter-hours season in my sources (about 10:00 to 15:00 from early December, and closed from 4 January), so check the dates first if snow is what you are after.")]
SPRING=[
('sakura-aerial','4684fac8','Totti','S4','Cherry trees in full bloom around a curved path on the ruins, with a town, river and mountains below','Cherry trees in bloom, 13 April 2019.',
 "On Commons the file is titled as the castle in full cherry bloom, taken on 13 April 2019. Cherry trees grow around the terraces and the paved path winds between them, with visitors strolling in the sun. The town and river are far below. This is one example of how things looked on one day, because the bloom varies from year to year."),
('sakura-wall','cacf962b','Totti','S4','Cherry trees in bloom around a rope-fenced stone wall, with visitors sitting on benches in the shade','Blossom beside a stone wall, 13 April 2019.',
 "Taken the same day, this shows the trees close up beside a rope-fenced stone wall, with visitors resting on benches in the shade. Small solar panels on stands are visible along the ropes. I do not know what they power, so I will not guess. The photo shows how the blossoms and the old stone share the same space."),
('sakura-valley','c520e68e','Totti','S4','A single early cherry tree in bloom beside a stone wall, with a long valley, a road and mountains in the distance','A single cherry tree and the valley, 13 April 2019.',
 "The same photographer on the same day, now looking down the valley, with one pink tree in front and the grass still dry and golden. It is an easy view to picture when you read the walking times above: the road far below is the way you came."),
('sakura-april-2022','00818f82','Drivephotographer','C0','Cherry trees with reddish young leaves and a few blossoms on a grassy terrace with orange cones, under a blue sky','Cherry trees before the bloom, 17 April 2022.',
 "Photographed on 17 April 2022, this shows cherry trees with a reddish tint and few open flowers. It is not full bloom, and orange cones mark off an area on the grass. Together with the 2019 photos it shows how much the timing can differ, so I would not plan a trip around one fixed date.")]
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
# hero
img,fc=mk(*HERO,True)
tocm='  <!-- TABLE OF CONTENTS -->'
assert s.count(tocm)==1
s=s.replace(tocm,f'  <figure style="margin:0 0 48px;">{img}{fc}</figure>\n\n'+tocm)
put("Lovers&rsquo; Sanctuary&rdquo; in 2012.</p>",block(STONE))
put("nothing blocks the view down to the town.</p>",block(WALLS))
put("are what people hope for.</p>","\n    <p>The photo at the top of this page shows the kind of morning people come for: a sea of clouds filling the valley at sunrise, with the stone terraces and pines standing above it. Commons gives only the date, 5 December 2010 at 07:11, and does not say where it was taken. Conditions like these are the exception, not a promise.</p>")
put("another inside the ruins, if you can spare both.</p>",block(CLOUDS))
vis='    <h2 id="visit">'
assert s.count(vis)==1
sp='    <h2 id="spring">Spring on the Walls<span class="h2-jp">春の桜</span></h2>\n    <p>The ruins are not only a cloud-season destination. The photos below, all from Commons, show cherry trees growing on the terraces among the stone. I do not have a source for the number of trees or the usual peak dates, so I will only describe what the pictures show and say that the bloom changes each year.</p>'+block(SPRING)+'\n\n'
s=s.replace(vis,sp+vis)
t='<li><a href="#clouds">The Sea of Clouds</a></li>'
assert s.count(t)==1
s=s.replace(t,t+'\n      <li><a href="#spring">Spring on the Walls</a></li>')
open(p,'w',encoding='utf-8').write(s)
with open(R+'PHOTO-CREDITS.csv','a',encoding='utf-8',newline='') as fh:
    w=csv.writer(fh,lineterminator='\r\n')
    for r in rows: w.writerow(r)
for tg in ['div','figure','picture','p','a','ul','li','details','section','h2']:
    assert len(re.findall(f'<{tg}[ >]',s))==len(re.findall(f'</{tg}>',s)),tg
for m in re.findall(r'<script type="application/ld\+json">(.*?)</script>',s,re.S): json.loads(m)
print('ok',s.count('<figure'),sizes)
