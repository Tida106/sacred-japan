import re,csv,os
from PIL import Image
R='/home/claude/sacred-japan/'; A='/mnt/user-data/attachments/53e3d492-4bf8-5cd9-a0ec-63a7cbefb1d9/'
SL='himeji-castle'
L={'S3':('CC BY-SA 3.0','https://creativecommons.org/licenses/by-sa/3.0/'),'S4':('CC BY-SA 4.0','https://creativecommons.org/licenses/by-sa/4.0/'),'B2':('CC BY 2.0','https://creativecommons.org/licenses/by/2.0/'),'B4':('CC BY 4.0','https://creativecommons.org/licenses/by/4.0/'),'C0':('CC0 1.0','https://creativecommons.org/publicdomain/zero/1.0/')}
rows=[]
def mk(k,f,au,lic,alt,cap,maxw=760):
    im=Image.open(A+f).convert('RGB')
    if im.width>1200: im=im.resize((1200,round(im.height*1200/im.width)),Image.LANCZOS)
    D=R+f'guides/{SL}/images/'; os.makedirs(D,exist_ok=True)
    im.save(D+k+'.jpg',quality=84,optimize=True); im.save(D+k+'.webp',quality=80)
    if lic=='MLIT':
        credit='Photo: Naokijp, made based on <a href="https://service.gsi.go.jp/map-photos/" target="_blank" rel="noopener" style="color:var(--enshu);">National Land Image Information (Color Aerial Photographs)</a>, Ministry of Land, Infrastructure, Transport and Tourism, via Wikimedia Commons (resized)'
        rows.append([f'guides/{SL}',f'/guides/{SL}/images/{k}.jpg','MLIT attribution terms','','',f'{cap} Photo: Naokijp, made based on National Land Image Information (Color Aerial Photographs), Ministry of Land, Infrastructure, Transport and Tourism, via Wikimedia Commons (resized)'])
    else:
        l=L[lic]
        credit=f'Photo: {au}, <a href="{l[1]}" target="_blank" rel="noopener" style="color:var(--enshu);">{l[0]}</a>, via Wikimedia Commons (resized)'
        rows.append([f'guides/{SL}',f'/guides/{SL}/images/{k}.jpg',l[0],l[1],l[1],f'{cap} Photo: {au}, {l[0]}, via Wikimedia Commons (resized)'])
    return (f'<figure style="margin:32px auto;max-width:{maxw}px;"><picture><source srcset="/guides/{SL}/images/{k}.webp" type="image/webp"><img src="/guides/{SL}/images/{k}.jpg" alt="{alt}" width="{im.width}" height="{im.height}" loading="lazy" style="width:100%;height:auto;border-radius:4px;display:block;"></picture>'
            f'<figcaption style="font-size:13px;color:var(--enshu);margin-top:10px;text-align:center;line-height:1.6;">{cap}<br>{credit}</figcaption></figure>')
def blk(*a,para,maxw=760): return '\n    '+mk(*a,maxw=maxw)+f'\n    <p>{para}</p>\n'
p=R+f'guides/{SL}/index.html'; s=open(p,encoding='utf-8').read()
def put(anchor,html,before=False):
    global s
    assert s.count(anchor)==1,anchor
    s=s.replace(anchor,(html+anchor) if before else (anchor+html))
# opening: Suicasmo
put('    <h2 id="history">',
 blk('keep-below','889a2c74-image.jpg','Suicasmo','S4','The white main keep and smaller keeps of Himeji Castle above a long white wall and stone base, with green trees in front and a clear blue sky','The keep seen from below, 30 July 2016 (Commons: &ldquo;Himeji Castle Keep Tower&rdquo;).',
  para='This is the view that stops guests mid-sentence. The tall main keep stands behind, with the smaller keeps to its left, and the long white wall in front runs along the top of the stone base. Look closely at that wall: it is pierced by small square and triangular openings, the loopholes the section below explains. The picture was taken on a clear summer day in 2016, and trees fill the lower half, which is how the castle often appears as you approach it.')+'\n',before=True)
# maze: aerial
put('<div style="display:flex;flex-wrap:wrap;gap:20px;justify-content:center;align-items:flex-start;margin:32px 0;">',
 blk('aerial','5b44db6e-image.jpg','Naokijp','MLIT','An aerial view of Himeji Castle seen straight down, with a green wooded castle hill in the middle ringed by water and dense city streets around it','The castle from directly above, 17 May 2010. Commons notes it was made from a Geospatial Information Authority of Japan aerial photograph.',maxw=620,
  para='From above you can see why the route to the keep cannot be a straight line. The keep and the main baileys sit in the middle of a dense belt of trees, and the moats curve around them in broad bands, with the modern city packed against the outside. The picture was made from a government aerial survey photograph in 2010, before the restoration work that ended in 2015, so small details have changed, but the shape of the moats and baileys is the same.')+'\n',before=True)
# survived: Kitsakis
put('the brightness is the first thing you notice.</p>',
 blk('after-renovation','7570d9aa-image.jpg','Nikos Kitsakis','S4','The renovated white keep of Himeji Castle rising above stone walls and green trees under a blue sky, with a building at the left still covered in scaffolding and grey sheeting','The keep in May 2015 after the five-year renovation of the roofs and walls (Commons description).',
  para='Commons dates this to May 2015, soon after the reopening described above. The plaster is bright white and the roof tiles are crisp. At the left of the picture a smaller building is still wrapped in scaffolding and grey sheeting, a reminder that work on the grounds continued even after the keep itself was finished.'))
# seasons section (before visit)
seasons='\n    <h2 id="seasons">Himeji Through the Seasons<span class="h2-jp">四季</span></h2>\n    <p>Himeji looks different in each season, and the guests I take in early April see a different castle from the ones who come in autumn. These are photographs from several photographers and years, so use them as a guide to the mood and not as a calendar.</p>\n'
seasons+=blk('cherry-bridge','dda72221-image.jpg','Seattleite7','S4','Himeji Castle keep framed by pink cherry blossom branches, with a red bridge over the moat and a few people standing on it','Cherry blossoms around the moat, 2 April 2015.',
  para='The most famous way to see Himeji. Commons gives the Russian description roughly as &ldquo;Himeji Castle through the cherry blossoms, from Himeji Zoo&rdquo;; the red bridge crosses the moat in front, and a few people stand on it to take pictures. This was taken in early April 2015, which fits the usual blossom season. As the FAQ below says, this is also the most crowded time to visit.')
seasons+=blk('crowd-april','080a1073-image.jpg','DimiTalen','C0','A large crowd of visitors walking toward Himeji Castle under a blue sky, with cherry blossoms and the distant white keep','Crowds walking toward the castle in cherry blossom season, 6 April 2016.',
  para='This is what that same season looks like from the ground. Dozens of people hold up phones and cameras as they walk toward the keep, and pink cherry trees stand along both sides of the way. Commons dates it to 6 April 2016. A building at the left of the keep still has scaffolding on it. If you want the blossoms without a crowd like this, go early on a weekday.')
seasons+=blk('view-sakura','43b5bef6-image.jpg','Oren Rozen','S4','A view over the castle grounds from a high point, with tiled roofs in the foreground, pink cherry trees, white walls and gates, and a city and mountains in the distance','The grounds and the city from a high point, 4 April 2016.',
  para='Commons labels this only &ldquo;Himeji Castle, Himeji, Japan&rdquo;, but the camera position on the file is right at the castle and the view looks down over the baileys, so I take it to be from the keep or near it. Cherry trees fill the grounds between the white walls and gates, with the city beyond and low mountains on the horizon. A fish-shaped roof ornament sits at the bottom right. It is a good picture of how many gates and walls the castle packs into a small area.')
seasons+=blk('autumn-moat','6c313920-image.jpg','Martin Falbisoner','S4','Himeji Castle seen across a still moat with a long stone wall and a white earthen wall in front, red and orange autumn leaves, and a blue sky with clouds','The keep above a moat, with autumn leaves (uploaded December 2016).',
  para='In autumn the castle sits among red and orange leaves, and the still water of the moat reflects the stone wall in front of it. The photographer uploaded this in late 2016. A long white wall with small square openings runs across the middle of the picture, a good place to see the loopholes from the outside. Autumn is quieter than April, and the light is soft.')
seasons+=blk('pink-night','000f777c-image.jpg','Lifes Legacy','B4','Himeji Castle keep and smaller keeps lit bright pink against a black night sky','The keep lit in pink, 1 October 2015.',
  para='Commons describes this as the castle lit in pink for Breast Cancer Awareness Month in October, photographed at about seven in the evening on 1 October 2015. It is a special lighting, not the castle&rsquo;s normal appearance, and I do not know whether it was repeated in other years. It does show how the white plaster takes on any color of light.')
seasons+=blk('night-panorama','7edb1896-image.jpg','Purity Standard','B2','A wide night panorama of Himeji Castle keep in the distance above trees lit green, with a wooden bridge at the left and stone walls and still water reflecting the lights','A night panorama of the castle across the moat, 28 October 2015.',
  para='A wide night view taken in late October 2015, with the keep lit white in the distance. The trees and stone wall in the foreground are lit green, and a wooden bridge crosses the moat at the left. Everything reflects in the water. Commons gives only &ldquo;Japan&rdquo; as the description, so I do not name the bridge or the gate. It is a reminder that the castle is worth seeing from the outside after dark if your trip allows.')
put('    <h2 id="visit">',seasons,before=True)
# visit: bridge
put('<ul class="practical-list">',
 blk('sakuramon-bridge','19448ad9-image.jpg','Nando.sm','S3','A wooden bridge with new pale timber rails over a moat, with a few visitors crossing and the white keep of Himeji Castle on the hill behind it under a blue sky','The wooden bridge at the entrance with the keep behind it, 8 August 2009 (Commons: Sakura Gate Bridge).',
  para='Commons titles this &ldquo;Himeji Castle and Sakura Gate Bridge view from the entrance&rdquo;. The bridge crosses the moat at the entrance, and the keep stands on its hill behind it. A visitor shelters from the summer sun under an umbrella. The timber looks new in this 2009 photograph, so it will have weathered since.'),before=True)
# koko-en
put('    <h2 id="stay">',' ',before=True) if False else None
put('rather than rush back.</p>',
 blk('koko-en','befa860f-image.jpg','Drivephotographer','C0','A Japanese garden pond with an arched stone bridge, orange koi, pruned pine trees and blue sky','Koko-en garden, 2 January 2021.',
  para='Koko-en is the garden beside the castle that I suggest for the second half of the morning. Commons dates this to 2 January 2021. An arched stone bridge crosses a pond, orange koi swim near the bank, and pruned pines frame the view. The combined ticket with the castle, listed in the FAQ below, covers it.'))
# TOC + date
put('      <li><a href="#visit">Visiting Himeji Castle</a></li>','      <li><a href="#seasons">Himeji Through the Seasons</a></li>\n',before=True)
s=s.replace('"dateModified": "2026-11-01"','"dateModified": "2026-11-05"')
open(p,'w',encoding='utf-8').write(s)
with open(R+'PHOTO-CREDITS.csv','a',encoding='utf-8',newline='') as f: csv.writer(f,lineterminator='\r\n').writerows(rows)
print(len(rows))
for tg in ['div','figure','picture','p','a','ul','li','details','section','h2']:
    assert len(re.findall(f'<{tg}[ >]',s))==len(re.findall(f'</{tg}>',s)),tg
