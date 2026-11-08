import re, csv, os
from PIL import Image
R='/home/claude/sacred-japan/'; A='/mnt/user-data/attachments/fd332c08-3f6b-545a-883b-83277e19ff52/'
SL='tsuyama-castle'
L={'S3':('CC BY-SA 3.0','https://creativecommons.org/licenses/by-sa/3.0/'),'B3':('CC BY 3.0','https://creativecommons.org/licenses/by/3.0/'),'B2':('CC BY 2.0','https://creativecommons.org/licenses/by/2.0/')}
rows=[]
def mk(k,f,au,lic,alt,cap,hero=False,maxw=760):
    im=Image.open(A+f+'-image.jpg').convert('RGB')
    if im.width>1200: im=im.resize((1200,round(im.height*1200/im.width)),Image.LANCZOS)
    D=R+f'guides/{SL}/images/'; os.makedirs(D,exist_ok=True)
    im.save(D+k+'.jpg',quality=84,optimize=True); im.save(D+k+'.webp',quality=80)
    l=L[lic]
    rows.append([f'guides/{SL}',f'/guides/{SL}/images/{k}.jpg',l[0],l[1],l[1],f'{cap} Photo: {au}, {l[0]}, via Wikimedia Commons (resized)'])
    fs='margin:0 0 48px;' if hero else f'margin:28px auto;max-width:{maxw}px;'
    ld='eager' if hero else 'lazy'
    return (f'<figure style="{fs}"><picture><source srcset="/guides/{SL}/images/{k}.webp" type="image/webp"><img src="/guides/{SL}/images/{k}.jpg" alt="{alt}" width="{im.width}" height="{im.height}" loading="{ld}" style="width:100%;height:auto;border-radius:4px;display:block;{"max-height:420px;object-fit:cover;" if hero else ""}"></picture>'
            f'<figcaption style="font-size:13px;color:var(--enshu);margin-top:10px;text-align:center;line-height:1.6;">{cap}<br>Photo: {au}, <a href="{l[1]}" target="_blank" rel="noopener" style="color:var(--enshu);">{l[0]}</a>, via Wikimedia Commons (resized)</figcaption></figure>')
def blk(*a,para): return '\n    '+mk(*a)+f'\n    <p>{para}</p>'
p=R+f'guides/{SL}/index.html'; s=open(p,encoding='utf-8').read()
def put(anchor,html,before=False):
    global s
    assert s.count(anchor)==1,anchor
    s=s.replace(anchor,(html+anchor) if before else (anchor+html))
LIB='津山市立図書館 (Tsuyama City Library)'
hero=mk('hero-blossom-turret','bd48f78f','denteru','B3','A white two-storey turret rising behind a frame of pale pink cherry blossom against a clear blue sky','The Bitchu Turret among cherry blossom, 8 April 2010 (Commons: Tsuyama Castle and Bitchu Turret surrounded by cherry blossoms).',hero=True)
put("  <!-- TABLE OF CONTENTS -->",hero+"\n\n",before=True)
put("please take it as a guide's note.</p>",
 blk('mori-statue','2ae2391c','663highland','S3','A seated bronze statue of a man in court dress in front of a rough stone wall, on a granite base','The statue at the castle, 28 January 2010.',
  para="A seated bronze figure sits in front of a rough stone wall, hands together, on a granite base. The green plate on the base reads, as I make it out, 森忠政公, which is &ldquo;Lord Mori Tadamasa,&rdquo; the man who built the castle. Commons labels the photo only as Tsuyama Castle, so I am reading the plate and not a caption. The wall behind him is a good first look at the stonework I describe below."))
put("so please wear comfortable shoes.</p>",
 blk('walls-tiers','dcc6ee66','663highland','S3','Tiered stone walls climbing a hill under bare cherry trees, with a white turret and a wooden trellis at the top','The tiered walls with the turret above, 21 March 2013 (Commons: Tsuyama Castle).',
  para="This is the view I would use to explain the castle. The walls rise in steps, one terrace on top of another, and the white turret sits on the highest edge beside a long wooden trellis. The cherry trees are bare, because this was taken on 21 March 2013, before the blossom. In winter light you can see the stonework clearly, which is why I like this season for a first visit.")+
 blk('stairs-reggaeman','582a0392','Reggaeman','S3','A wide stone staircase between two tall rough stone walls, with red paper lanterns on poles and bare trees above','The steps at the site of the Omote-chumon gate, 19 March 2005 (Commons: 表中門跡の石段).',
  para="Commons names this the stone steps at the site of the Omote-chumon gate (表中門跡). A wide flight of steps runs up between two high walls, and red lanterns on poles are already set out for the blossom festival, even though the trees are bare. The photo is from 19 March 2005, so details may have changed, but the layout of walls and steps is the part that lasts.")+
 blk('stairs-kohara','f7a40239','Yoshio Kohara','B3','A long stone staircase climbing between rough stone walls under green trees and blue sky, with fallen leaves on the steps','A stone staircase in early autumn, 9 September 2014 (Commons: Tsuyama Castle ruins).',
  para="Here is another flight of steps, photographed on 9 September 2014. The treads are worn and uneven, and a few fallen leaves lie on them. The cherry trees along the sides are green and thin out toward the top. I include it because it shows how steep the approach is and why my sources suggest good shoes."))
put("I would go inside for both reasons.</p>",
 blk('turret-below','6d4f6e29','Yoshio Kohara','B3','A white two-storey turret with grey roofs standing on a stone wall, seen from below against a deep blue sky','The Bitchu Turret from below, 9 September 2014 (Commons: Tsuyama Castle turret).',
  para="Seen from below, the turret looks much larger than it does in the blossom photographs. It has two storeys of white plaster walls with slatted windows, a gabled upper roof, and a long wooden trellis on the terrace to the right. It stands directly on the stone wall, so the whole thing reads as one piece, which I think is the best argument for rebuilding it.")+
 blk('turret-2005','a720f0a4','Reggaeman','S3','A white turret on a high stone wall behind bare trees, with a row of red lanterns below and a blue sky with large clouds','The turret on the day of its completion ceremony, 19 March 2005 (Commons: Bitchu Turret).',
  para="Commons says this photograph was taken on the day of the turret's completion ceremony. That fits the restoration dates I give above, which end in 2005. The trellis on the right has people standing on it. It is a smaller picture than the others, and I have kept it at its original size without enlarging it."))
put("Early morning is the easiest time for photographs.</p>",
 blk('festival-2011','d69e2a14','津山市立図書館 (Tsuyama City Library)','B2','Cherry trees in full bloom in front of a high stone wall, with a white turret on top under a clear blue sky','Cherry blossom below the walls, 12 April 2011 (Commons: Tsuyama Sakura Festival).',
  para="Commons files this under the Tsuyama Sakura Festival, and it was taken on 12 April 2011. Cherry trees fill the slope below the wall in full bloom, with the turret on top. You can also see a trellis and, I believe, some lanterns. It gives the best idea of the scale: the blossom is not along one path but covers the hill.")+
 blk('dusk-2018','8a7f9763','津山市立図書館 (Tsuyama City Library)','B2','Cherry trees in full white bloom around a stone staircase, with a white turret at the upper right and a bright pale sky behind it','Blossom at sunset by the staircase, 30 March 2018 (Commons title: sunset).',
  para="This was taken on 30 March 2018 at sunset, according to the Commons title. The sky is almost white, and the blossom is lit from behind, so the petals look pale and luminous. The turret at the upper right is the rebuilt Bitchu Turret, since no keep survives. A few visitors stand on the stone steps, and red lanterns are visible among the branches. March 30 is early, so in 2018 the trees were blooming well ahead of the usual early April.")+
 blk('dusk-2016','eeabbea7','津山市立図書館 (Tsuyama City Library)','B2','A floodlit white turret above a stone wall with glowing blossom trees and lanterns in the dusk, and city lights in the distance','Evening at the festival, 5 April 2016 (Commons: Sakura Festival, night).',
  para="From 5 April 2016, shortly after sunset. The turret and the great stone wall are lit, the blossom glows orange and pink, and the lanterns along the paths are on. In the distance are the lights of the town. A few people are walking at the foot of the wall, which gives a sense of its height. This is a smaller file, shown at its original size.")+
 blk('blue-2018','0063088a','津山市立図書館 (Tsuyama City Library)','B2','A turret lit pale blue above blossom trees lit by warm lanterns, with a stone staircase in front, at night','The turret lit in blue, 2 April 2018 (Commons: Sakura Festival, night).',
  para="This one is from 2 April 2018, at night. The turret is lit blue, and the blossom nearby takes on a violet tone, while the lanterns stay warm. I do not know how the colours of the lighting are chosen or whether they change from night to night, so please do not count on the same colour. I would check the festival information before going."))
put("<h2 id=\"visit\">",
 blk('river-2020','e9a18f66','津山市立図書館 (Tsuyama City Library)','B2','A row of cherry trees in full bloom along a riverside path, with a stone-walled hill rising in the background','Cherry trees by the river with the walls in the distance, 3 April 2020 (Commons: near Johoku Bridge).',
  para="Commons places this near Johoku Bridge (城北橋), on 3 April 2020. A row of blossoming trees follows a paved riverside path, and the castle hill with its stone walls rises behind them. It is a useful reminder that the walls are visible from the town below, not only from inside the park. I would add this view to your walk if the weather is good.")+"\n\n    ",before=True)
open(p,'w',encoding='utf-8').write(s)
with open(R+'PHOTO-CREDITS.csv','a',encoding='utf-8',newline='') as f: csv.writer(f,lineterminator='\r\n').writerows(rows)
print(len(rows))
for tg in ['div','figure','picture','p','a','ul','li','details','section','h2']:
    assert len(re.findall(f'<{tg}[ >]',s))==len(re.findall(f'</{tg}>',s)),tg
