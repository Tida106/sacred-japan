import re,csv,os
from PIL import Image
R='/home/claude/sacred-japan/'; A='/mnt/user-data/attachments/53e3d492-4bf8-5cd9-a0ec-63a7cbefb1d9/'
SL='aizuwakamatsu-castle'
L={'B3':('CC BY 3.0','https://creativecommons.org/licenses/by/3.0/'),'B4':('CC BY 4.0','https://creativecommons.org/licenses/by/4.0/'),'S4':('CC BY-SA 4.0','https://creativecommons.org/licenses/by-sa/4.0/')}
rows=[]
def mk(k,f,au,lic,alt,cap):
    im=Image.open(A+f+'-image.jpg').convert('RGB')
    if im.width>1200: im=im.resize((1200,round(im.height*1200/im.width)),Image.LANCZOS)
    D=R+f'guides/{SL}/images/'
    im.save(D+k+'.jpg',quality=84,optimize=True); im.save(D+k+'.webp',quality=80)
    l=L[lic]
    rows.append([f'guides/{SL}',f'/guides/{SL}/images/{k}.jpg',l[0],l[1],l[1],f'{cap} Photo: {au}, {l[0]}, via Wikimedia Commons (resized)'])
    return (f'<figure style="margin:28px auto;max-width:760px;"><picture><source srcset="/guides/{SL}/images/{k}.webp" type="image/webp"><img src="/guides/{SL}/images/{k}.jpg" alt="{alt}" width="{im.width}" height="{im.height}" loading="lazy" style="width:100%;height:auto;border-radius:4px;display:block;"></picture>'
            f'<figcaption style="font-size:13px;color:var(--enshu);margin-top:10px;text-align:center;line-height:1.6;">{cap}<br>Photo: {au}, <a href="{l[1]}" target="_blank" rel="noopener" style="color:var(--enshu);">{l[0]}</a>, via Wikimedia Commons (resized)</figcaption></figure>')
def blk(*a,para): return '\n    '+mk(*a)+f'\n    <p>{para}</p>'
p=R+f'guides/{SL}/index.html'; s=open(p,encoding='utf-8').read()
def put(anchor,html):
    global s
    assert s.count(anchor)==1,anchor
    s=s.replace(anchor,anchor+html)
put("but I cannot read it well enough to say more.</p>",
 blk('bridge-day','4c8a442c','Bernie Ongewe','S4','A red wooden bridge with gold finials crossing between two tall moss-covered stone walls under a blue sky','A red bridge between high stone walls, 25 September 2022.',
  para="Commons titles this &ldquo;Ttsuruga-j&#333; / Aizuwakamatsu Castle&rdquo; and does not name the bridge, so I only describe what I can see. A red-lacquered bridge with gold-topped posts runs straight into a gap between two very tall stone walls. The walls are dark with moss and built of large blocks, and the pines above them are the only thing breaking the line. It is a good example of how the castle uses stone and a single colour to control the way you approach. This was taken in late September, so the greens are summer greens.")+
 blk('bridge-night','d37b5719','Fumihiko Ueno','B3','A red bridge lit from below at night, with floodlit cherry trees in bloom and a large bare tree beside a stone wall','A red bridge and cherry blossoms at night, 30 April 2010.',
  para="Commons gives the date as 30 April 2010 and the place only as Otemachi in Aizuwakamatsu, so I cannot tell you which bridge this is. Lights along the rail make the red lacquer glow orange, and floodlights turn the cherry trees beyond into pale clouds against the black sky. The large bare tree at the left shows that not every tree was in bloom at once. A rough stone wall rises at the right edge, much like the walls in the photograph above, though I do not claim it is the same place.")
)
put("it shows that the castle is also worth a look in deep winter.</p>",
 blk('snow-wall-trees','f494c05b','くろふね (Kurofune)','B4','The white keep above a snow-covered stone base, with bare trees and a low wooden fence in front under a cloudy sky','The keep over a snowy stone base, 8 February 2020.',
  para="Commons labels this 若松城（鶴ヶ城）, with a time of 9:43 in the morning on 8 February 2020. Fresh snow sits on every ledge of the rough stone base, so the stones look like a heap of white boulders. Bare trees stand at the left and right, and a low wooden fence keeps visitors back from the slope. The keep above shows its red-brown tiles dusted white. It is a reminder that the stone base, not the keep, is the oldest-looking part of the view.")+
 blk('snow-pine-keep','8386e2a6','くろふね (Kurofune)','B4','The white keep seen between two snowy pine trees held up by rope supports, with a stone base below','The keep between snowy pines with rope supports, 8 February 2020.',
  para="Four minutes later, at 9:47, the same photographer looked up from a lower spot. Pines at the left and centre are wrapped in a fan of ropes running up to a central pole, which holds up the branches under the weight of the snow. This kind of rope support is a familiar winter sight in snowy parts of Japan. Behind the trees the keep climbs through its levels, and a long white wall runs off to the left.")+
 blk('snow-wall-keep','7fc7e8a7','くろふね (Kurofune)','B4','A long white wall on a stone base with the keep behind it, over a snowy open ground with rope-supported pines','A white wall and the keep over snowy ground, 8 February 2020.',
  para="This is the same morning, at 9:49. A long white wall with a tiled roof stands on a base of large cut stones at the left, and the keep rises behind the pines at the right. There is a signpost and an information board on the path, and the open ground in the foreground is covered with snow. I cannot name the wall or the building at the left from Commons, so I treat it as general scenery. Snow like this is typical of the region in deep winter, but I cannot say how often it falls on any given day.")
)
open(p,'w',encoding='utf-8').write(s)
with open(R+'PHOTO-CREDITS.csv','a',encoding='utf-8',newline='') as f: csv.writer(f,lineterminator='\r\n').writerows(rows)
