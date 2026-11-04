import re,csv
from PIL import Image
R='/home/claude/sacred-japan/'; A='/mnt/user-data/attachments/53e3d492-4bf8-5cd9-a0ec-63a7cbefb1d9/'
SL='aizuwakamatsu-castle'
L={'B3':('CC BY 3.0','https://creativecommons.org/licenses/by/3.0/'),'B4':('CC BY 4.0','https://creativecommons.org/licenses/by/4.0/'),
   'S3':('CC BY-SA 3.0','https://creativecommons.org/licenses/by-sa/3.0/'),'S4':('CC BY-SA 4.0','https://creativecommons.org/licenses/by-sa/4.0/'),
   'PD':('Public domain','https://commons.wikimedia.org/wiki/Template:PD-user')}
rows=[]
def mk(k,f,au,lic,alt,cap,hero=False,maxw=None):
    im=Image.open(A+f+'-image.jpg').convert('RGB')
    if im.width>1200: im=im.resize((1200,round(im.height*1200/im.width)),Image.LANCZOS)
    D=R+f'guides/{SL}/images/'
    import os; os.makedirs(D,exist_ok=True)
    im.save(D+k+'.jpg',quality=84,optimize=True); im.save(D+k+'.webp',quality=80)
    l=L[lic]
    rows.append([f'guides/{SL}',f'/guides/{SL}/images/{k}.jpg',l[0],l[1],l[1],f'{cap} Photo: {au}, {l[0]}, via Wikimedia Commons (resized)'])
    st=('width:100%;max-height:420px;object-fit:cover;object-position:center 25%;border-radius:4px;display:block;' if hero else 'width:100%;height:auto;border-radius:4px;display:block;')
    ld='eager' if hero else 'lazy'
    fs='margin:0 0 48px;' if hero else f'margin:28px auto;max-width:{maxw or 760}px;'
    return (f'<figure style="{fs}"><picture><source srcset="/guides/{SL}/images/{k}.webp" type="image/webp"><img src="/guides/{SL}/images/{k}.jpg" alt="{alt}" width="{im.width}" height="{im.height}" loading="{ld}" style="{st}"></picture>'
            f'<figcaption style="font-size:13px;color:var(--enshu);margin-top:10px;text-align:center;line-height:1.6;">{cap}<br>Photo: {au}, <a href="{l[1]}" target="_blank" rel="noopener" style="color:var(--enshu);">{l[0]}</a>, via Wikimedia Commons (resized)</figcaption></figure>')
def blk(*a,para,maxw=None): return '\n    '+mk(*a,maxw=maxw)+f'\n    <p>{para}</p>'
p=R+f'guides/{SL}/index.html'; s=open(p,encoding='utf-8').read()
def put(anchor,html):
    global s
    assert s.count(anchor)==1,anchor
    s=s.replace(anchor,anchor+html)
# hero
h=mk('hero-keep-stone','ede281ec','Asturio Cantabrio','S4','The white five-level keep rising above a rough stone wall and a pine tree under a blue sky','The keep and its stone base, July 2022.',hero=True)
t='  <!-- TABLE OF CONTENTS -->'; assert s.count(t)==1
s=s.replace(t,'  '+h+'\n\n'+t)
put("which is a claim I could not check elsewhere.</p>",
 blk('keep-2007','4f35b2b0','Umako','PD','The white keep with a red railing on the top floor and dark grey roof tiles, seen across a lawn','The keep with its older dark roof, 3 September 2007.',
  para="This is the keep as it looked before the roof was changed back. Commons titles it &ldquo;Tenshukaku of Aizuwakamatsu castle,&rdquo; and the photographer has released it into the public domain. The roof tiles are dark grey, which matches the sources that say the 1965 rebuild used black tiles and that red ones returned in 2011. The red railing around the top-floor observation deck is already there. Compare this with the 2022 photo at the top of the page to see the difference the roof makes.")+
 blk('keep-dusk-hdr','a6bc7563','studio IRONY','B3','The keep at dusk with bare cherry trees, a glowing orange and purple sky and banners hanging on the stone wall','The keep at dusk, uploaded 21 April 2010.',maxw=720,
  para="Commons gives only an upload date of 21 April 2010 for this one, and the colours are heavily processed, so please read the sky as an effect rather than a typical evening. What I can take from it is the setting: bare cherry trees in front, a mossy stone wall, a few banners, and the keep with its older dark roof above. At 720 pixels wide it is a small file, so I show it small.")
)
put("please look at the signs on site.</p>",
 blk('iron-gate','768866ee','lienyuan lee','B3','A gate with a tiled roof and a white wall above a sloping stone base, under a blue sky','The Iron Gate, 25 October 2007.',
  para="Commons titles this &ldquo;Iron Gate of Tsuruga-jo Castle,&rdquo; with the Chinese label 鶴之城鐵門. It is a gate with a covered passage and small shuttered windows above it, set between a white wall and a sloping stone base. The stonework is worth a close look, because the large blocks were cut to fit tightly. Commons also says it was taken in October 2007, so the gate has had several years of repair work since then.")+
 blk('gate-and-keep','6cc5dec2','Σ64','S3','A tiled gate with a stone staircase beside it, with the white keep rising behind the roofs','A gate with the keep behind, 21 August 2007.',
  para="Commons calls this simply &ldquo;Aizuwakamatsu Castle&rdquo; and does not name the gate, so I describe only what I can see. A covered gate with shuttered windows frames the view, a steep stone stair runs up at the left, and the keep stands out above the tiled roofs behind it. The red railing on the top floor is a useful guide for finding the keep from anywhere in the grounds. The photographer lists both a GNU licence and CC BY-SA 3.0; I use the Creative Commons one.")+
 blk('view-from-keep','c4e31b88','Asturio Cantabrio','S4','A view looking down from the keep at long tiled roofs, a white turret, a lawn and visitors, with the town beyond','The view down from the keep, July 2022.',
  para="Taken from above in July 2022, this shows what the top floor gives you. Long tiled roofs run below, and a white two-storey turret stands at the end of one of them. At the left is the open lawn of the main citadel, with visitors on the paths. Beyond the trees the town stretches to the hills. Commons does not name the buildings, so I do not label them. Notice that the new roof tiles look reddish-brown from here.")
)
put("Prices differ slightly between sources (see below).</p>",
 blk('rinkaku-moss','59b593b2','Bernie Ongewe','S4','A small covered bench in a garden with mossy ground, stepping stones, a stone lantern and a pine tree','The garden near the Rinkaku tea house, 25 September 2022.',
  para="Commons titles this &ldquo;Rinkaku Japanese Tea Room at Tsuruga-j&#333;,&rdquo; so it was taken in the tea-house area. It shows a small open shelter with a bench, a path of stepping stones across bright green moss, a stone lantern at the left and a pine at the right. This is the kind of small, quiet garden detail that is easy to miss from the main path. It is a garden view, not the inside of the tea room.")+
 blk('rinkaku-gate','66f5e2df','Bernie Ongewe','S4','A small wooden garden gate with a mossy bark roof and bamboo fences, with a path of stepping stones beyond','A small garden gate with a roof, 25 September 2022.',
  para="Another picture from the same visit and the same Commons title. A little wooden gate with a moss-covered roof and bamboo fencing stands over a stepping-stone path, and a low building can be seen behind it. Gates like this mark the move from one part of a tea garden to the next, though I cannot say which gate this is.")
)
put("Fun Japan calls April the best time for a visit.</p>",
 blk('sakura-aerial','22c6029f','SQZ','B4','The keep and long white walls among cherry trees in bloom, seen from above with mountains and the town behind','The castle in cherry blossom from above, 24 April 2017.',
  para="Commons describes this as the cherry blossom at Tsuruga Castle in Aizuwakamatsu, taken at 6:09 in the morning on 24 April 2017. From above you can see how the white walls and the red-brown roof of the keep sit inside a ring of trees, with the town and the hills behind. Several white tents are set up on the lawn. The date shows that in 2017 the trees were in bloom in late April, though the timing changes each year.")+
 blk('sakura-night-keep','deec1fd9','Fumihiko Ueno','B3','The lit white keep seen through the branches of cherry trees in bloom at night','The keep through cherry blossoms at night, 30 April 2010.',
  para="Commons gives the date as 30 April 2010. The keep glows white in the dark, framed on both sides by heavily lit cherry branches. This matches GLTJP&rsquo;s statement that the trees are illuminated during the blossom season. The roof here is the older dark one, since the red tiles came in 2011.")+
 blk('sakura-night-wall','0351f84b','Fumihiko Ueno','B3','A mossy stone wall in the foreground, cherry blossoms lit at night and the keep with its red railing above','Cherry blossoms, a stone wall and the keep at night, 30 April 2010.',
  para="The same photographer and date as the picture above, from a lower angle. A mossy stone wall fills the lower left, lit warm, while blossoms hang over the top and the keep rises behind with its red railing. A sign at the lower right appears to be an exhibition notice, but I cannot read it well enough to say more.")+
 blk('snow-lanterns','61397a1d','Fumihiko Ueno','B3','The keep at night in heavy snow, with pine trees wrapped in rope supports and rows of glowing snow lanterns and candles in the foreground','The keep in snow with lanterns at night, 12 February 2011.',
  para="This one is from 12 February 2011. Snow lies on the roofs, the pines have rope supports to hold up their branches under the weight, and rows of snow lanterns and small candles glow in the foreground. People are standing along the rope. The sources I used do not describe a winter event at the castle, so I cannot tell you which one this was, but it shows that the castle is also worth a look in deep winter.")
)
for tg in ['div','figure','picture','p','a','ul','li','details','section','h2']:
    assert len(re.findall(f'<{tg}[ >]',s))==len(re.findall(f'</{tg}>',s)),tg
open(p,'w',encoding='utf-8').write(s)
with open(R+'PHOTO-CREDITS.csv','a',encoding='utf-8',newline='') as f:
    w=csv.writer(f,lineterminator='\r\n');[w.writerow(r) for r in rows]
print(len(rows))
