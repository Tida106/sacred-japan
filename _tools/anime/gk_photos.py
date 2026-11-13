import os
from PIL import Image
R='/home/claude/sacred-japan'
U='/mnt/user-data/uploads/'
OUT=R+'/anime/golden-kamuy/images/'
L={'bysa3':('CC BY-SA 3.0','https://creativecommons.org/licenses/by-sa/3.0/'),
   'bysa4':('CC BY-SA 4.0','https://creativecommons.org/licenses/by-sa/4.0/'),
   'by2':('CC BY 2.0','https://creativecommons.org/licenses/by/2.0/'),
   'by4':('CC BY 4.0','https://creativecommons.org/licenses/by/4.0/'),
   'cc0':('CC0','https://creativecommons.org/publicdomain/zero/1.0/')}
# key: (upload, commons filename, slug, author, lic, date, alt, caption-place, description)
P={}
def add(k,up,fn,auth,lic,date,alt,cap,desc,maxw=760): P[k]=dict(up=up,fn=fn,auth=auth,lic=lic,date=date,alt=alt,cap=cap,desc=desc,maxw=maxw)
a='663highland'
add('otaru-hero','c8e4ee26-image.jpg','Otaru_Canal_HDR2.jpg','Tan Wei Liang Byorn','bysa4','2019-08-10','Otaru Canal at night with lit brick warehouses reflected in the water','Otaru Canal at night','')
add('otaru-dusk','75b15a46-image.jpg','Otaru_Hokkaido_Japan.jpg','Chi King','by2','','Otaru Canal at dusk with warehouses reflected in still water and gas lamps along the bank','Otaru Canal at dusk',
 "The canal at blue hour, with the gas-style lamps along the bank already lit and the warehouses reflected in still water. The stone warehouses on the right are the reason Otaru looks the way it does: this was a trading port, and the canal is where goods were moved between ships and storehouses. Snow is still piled along the left bank, so this was taken in the cold season.")
add('otaru-night','1279e656-image.jpg','Otaru_Canal_HDR1.jpg','Tan Wei Liang Byorn','bysa4','2019-08-10','Otaru Canal on a summer night, a brick warehouse covered in ivy glowing in the lamplight','Otaru Canal, summer night',
 "A summer night on the canal. The brick warehouse on the right, partly covered in ivy, is lit from below, and the lamps along the left bank are doubled in the water. The photo has been processed to bring out the colors, so the real scene is a little calmer, but the mood of a warm evening walk along the water is accurate.")
add('otaru-snow','4325d2c0-image.jpg','Otaru_canal.jpg','欅 (Keyaki)','bysa3','2009-02-07','Otaru Canal in winter with snow on the banks and people walking along the left side','Otaru Canal in winter',
 "The same canal in February, gray and quiet, with people strolling the snowy bank on the left. If you are following a story set in the Hokkaido cold, winter is when Otaru feels closest to it. Dress for it: the wind off the water is sharp.")
add('otaru-lights','495d6a26-image.jpg','Otaru_Canal_Night.jpg','Haha169','bysa4','2016-02-16','Otaru Canal on a winter night with blue lights along the snowy bank and warm streetlights reflected in the water','Otaru Canal, winter night',
 "A winter night with strings of blue lights along the snow-covered bank, which looks like a seasonal lighting display. Icicles hang from the eaves of the warehouse on the right. Lighting events change from year to year, so check the Otaru tourism site before you plan around one.")
add('hv-entrance','f4a62146-image.jpg','220722_Historical_Village_of_Hokkaido_Sapporo_Hokkaido_Japan03s5.jpg',a,'bysa4','2022-07-22','The cream and red main building of the Historical Village of Hokkaido under a blue sky','Historical Village of Hokkaido, main building',
 "The large cream building with a red roof that you meet first, as far as I can tell the village's main building near the entrance. Its decorative half-timbering and iron rooftop railing give a first hint of the Western-influenced style of Hokkaido's Meiji era, when the island was being developed quickly. Everything beyond this point is a relocated or restored building from that period.")
add('hv-studio','815f39e1-image.jpg','220722_Historical_Village_of_Hokkaido_Sapporo_Hokkaido_Japan84s5.jpg',a,'bysa4','2022-07-22','A dark wooden photo studio building with a red roof and a tall glass skylight in the Historical Village of Hokkaido','Historical Village of Hokkaido, photo studio',
 "A photo studio with a tall glass skylight in the roof, where daylight lit the sitter. The white sign on the right advertises photography services, including on-location and night shooting, and reads as a photographer's name, which I read as Hirose (廣瀬). It is a small reminder that the village is not only farms and shops but the whole fabric of a pioneer-era town.")
add('hv-barn','a112ecb4-image.jpg','220722_Historical_Village_of_Hokkaido_Sapporo_Hokkaido_Japan28s5.jpg',a,'bysa4','2022-07-22','A large wooden barn with a bright blue roof and a stone silo at the Historical Village of Hokkaido','Historical Village of Hokkaido, barn and silo',
 "A dairy-style barn with a blue roof and a stone silo, showing the farming side of the village. Hokkaido was opened to settlement partly to farm it, and the American-style barns that appeared here are one of the island's visual signatures. I cannot tell you whether this exact barn appears in the manga, so treat it as an example of the setting, not a confirmed scene.")
add('hv-tram','eda6a97c-image.jpg','_______Historical_Village_of_Hokkaido_-_panoramio_4.jpg','t-konno','bysa3','2015-04-18','A white horse pulling a tram along rails past a small brick building and bare trees at the Historical Village of Hokkaido','Historical Village of Hokkaido, horse-drawn tram',
 "A white horse pulling a tram along the rails on the village's main street, with a small brick building on the left and bare trees in early spring. This is what I mean by walking into a page of the story. Operating days and seasons change, so check the village's official page before you count on a ride.")
add('hv-entrance2','17bf29ed-image.jpg','Historical_Village_of_Hokkaido__Moerenuma_Park_-_HistoricalVillageHokkaido7168.jpg','lumoplank','cc0','','The same cream and red main building of the Historical Village of Hokkaido seen from the side on a cloudy day','Historical Village of Hokkaido, main building from the side',
 "The same cream-and-red building from the side on an overcast day. Weather in Hokkaido can turn quickly even in summer, so bring a layer.")
add('ab-bridge','82fac727-image.jpg','130713_Abashiri_Prison_Museum_Abashiri_Hokkaido_Japan01n.jpg',a,'bysa3','2013-07-13','A wooden truss bridge leading toward the entrance of Abashiri Prison Museum on a sunny day','Abashiri Prison Museum, approach bridge',
 "The wooden bridge on the approach, with the museum's entrance buildings ahead. Walking across it on a clear summer morning feels cheerful, which is a strange contrast with what the museum is about.")
add('ab-bridge-snow','6a955456-image.jpg','Mirror_bridge_at_Abashiri_Prison_Museum_-_panoramio.jpg','mayatomo','bysa3','2010-02-06','The wooden truss bridge at Abashiri Prison Museum covered in snow with a person clearing it','Abashiri Prison Museum, approach bridge in winter',
 "The same bridge in February, with a worker shoveling a path through the snow. Abashiri is in northeastern Hokkaido and winters are long and cold, which is the weather the story's early chapters imagine.")
add('ab-gate','5e66f7e8-image.jpg','130713_Abashiri_Prison_Museum_Abashiri_Hokkaido_Japan04n.jpg',a,'bysa3','2013-07-13','The gate pillars and signboards of Abashiri Prison Museum with the red-brick entrance building behind','Abashiri Prison Museum, gate',
 "The gate pillars with two wooden signboards: one for the preservation foundation that runs the site and one reading Museum Abashiri Prison (博物館 網走監獄). The red-brick building with two domed towers is visible through the bars.")
add('ab-front','0dd8824c-image.jpg','130713_Abashiri_Prison_Museum_Abashiri_Hokkaido_Japan08n.jpg',a,'bysa3','2013-07-13','Red-brick front building of Abashiri Prison Museum with a central arch and two dome towers, a brick path leading to it','Abashiri Prison Museum, entrance building',
 "The red-brick entrance building with its central arch and two gray domes, with the brick path leading straight to it. The signs beside the arch read Museum Abashiri Prison (博物館 網走監獄) on the left and Abashiri Prison (網走刑務所) on the right. Figures dressed as a guard and a worker stand by the entrance, which are display figures, not real people.")
add('ab-statue','65ba424b-image.jpg','130713_Abashiri_Prison_Museum_Abashiri_Hokkaido_Japan10n.jpg',a,'bysa3','2013-07-13','A statue of a bent working figure in a straw hat in front of the red-brick entrance of Abashiri Prison Museum','Abashiri Prison Museum, statue at the entrance',
 "A statue of a bent figure in a straw hat in the courtyard in front of the entrance. It stands for the labor that this place is known for: prisoners cleared land and built roads. The story is fiction, but this is the labor it points to.")
add('ab-snow-front','00d5b78f-image.jpg','Abashiri_Prison.jpg','Kotaro','bysa4','2010-03-05','The red-brick entrance of Abashiri Prison Museum with snow on the domes and roof','Abashiri Prison Museum, entrance in snow',
 "The entrance in winter, with snow on the domes. This is a small, low-resolution photo, so I show it at its natural size.",maxw=427)
add('ab-corridor1','45936a4d-image.jpg','130713_Abashiri_Prison_Museum_Abashiri_Hokkaido_Japan56n.jpg',a,'bysa3','2013-07-13','A long wooden cell corridor with skylights at Abashiri Prison Museum','Abashiri Prison Museum, cell block',
 "A long wooden cell block lit from skylights above, with cell doors down both sides. A plate on the right appears to give a cell number. This is the museum's best-known interior, and it is a quiet, slightly heavy place to walk through.")
add('ab-corridor2','f5b6c0cc-image.jpg','Abashiri_Prison_52356207412.jpg','Raita Futo','by2','2022-07-27','A long cell block with brick floor and skylight beams, warm light falling on wooden cell doors','Abashiri Prison Museum, cell block corridor',
 "Another view of a cell block, with a brick floor and warm light from the skylights. The color is warmer than most photos of this corridor, so editing may have enhanced it, but the layout is the same.")
add('ab-watch','59ff6a9d-image.jpg','Abashiri_Prison_Museum_-_2022_Aug_9_various_13_59_29_068000.jpeg','Nesnad','by4','2022-08-09','The octagonal central watch post inside the cell block building at Abashiri Prison Museum','Abashiri Prison Museum, central watch post',
 "The octagonal central watch post (中央見張). The cell blocks radiate from this point, so a guard standing here could look down several wings at once. Signs on the walls mark the wings by number.")
add('ab-meal','ea40745e-image.jpg','130713_Abashiri_Prison_Museum_Abashiri_Hokkaido_Japan43s3.jpg',a,'bysa3','2013-07-13','Wax-figure prisoners in orange robes eating a meal while an officer in white looks on, at Abashiri Prison Museum','Abashiri Prison Museum, meal display',
 "A museum display with figures of prisoners in orange robes eating a meal while an officer in a white uniform watches. They are mannequins, and the scene gives you a sense of daily life more than any sign could.")

h='Higa4'
add('up-exterior','699d1764-image.jpg','Shiraoi-upopoy_38.jpg',h,'cc0','2020-11-15','The dark angular roof and stone base of the National Ainu Museum at Upopoy at dusk, with visitors walking on the path','Upopoy, National Ainu Museum exterior',
 "The National Ainu Museum seen from the approach path at dusk, with its long, angular gray roof over a stone base. The pattern of lighter tiles on the end wall looks like an Ainu-style design, but I could not confirm that from the file. The photo is from 2020, the year Upopoy opened, and the surroundings may look different now.")
add('up-chise','17f5d938-image.jpg','Shiraoi-upopoy_14.jpg',h,'cc0','2020-11-15','A large reed-thatched Ainu house with a layered roof, an information board in front, and a raised storehouse behind','Upopoy, reconstructed chise',
 "A reconstructed <em>chise</em>, the traditional Ainu house, with walls and roof thatched in reeds and tied down with horizontal bands. The board in front is titled \u300c\u30c1\u30bb\u306e\u5efa\u7bc9\u300d (Building a Cise), and a raised storehouse stands behind it on the right. Photographed in late autumn, which is why the grass is dry and the trees are bare.")
add('up-room','9a2e0673-image.jpg','Shiraoi-upopoy_10.jpg',h,'cc0','2020-11-15','A reed-walled room with a woven patterned panel, a white patterned garment on the wall and a bamboo frame, on a wooden floor','Upopoy, exhibition room with Ainu garment',
 "A reed-walled room with a woven panel in a bold diamond-and-zigzag pattern, a white garment with curling embroidered lines hung on the wall, and a bent-wood frame on the floor. The photo is slightly blurred, so I am using it for the atmosphere rather than the detail. The labels were not legible, so I will not name the objects.")
add('up-hearth-wide','6bd0bd75-image.jpg','Shiraoi-upopoy_09.jpg',h,'cc0','2020-11-15','A sunken square hearth in a large reed-walled hall with hanging wooden fixtures and benches along the wall','Upopoy, hall with a hearth',
 "A square hearth sunk into the floor of a large reed-walled hall, with hanging wooden fixtures above and benches along the far wall. Commons describes the hearth in this series as an irori, the Japanese word for it. In an Ainu house the hearth is the center of the room, and I would treat it with that respect. This photo is also slightly blurred.")
add('up-hearth','e54caf89-image.jpg','Shiraoi-upopoy_06.jpg',h,'cc0','2020-11-15','A sunken hearth with glowing charcoal, an iron kettle hanging above it and white shaved-wood decorations on the rim','Upopoy, hearth with kettle',
 "The same kind of hearth with live charcoal glowing in the ash and an iron kettle hanging above it. The white curled shavings standing by the rim look like <em>inau</em>, the ritual wood shavings, but that is my reading and the file does not say so. Visitors stand in the background in socks, so shoes come off in this room.")
add('up-chise-inside','42f1ec1a-image.jpg','Interior_of_traditional_Ainu-style_house_cise_in_UPOPOY.jpg','\u63ac\u8336','bysa4','2026-08-22','Inside a traditional Ainu house, woven patterned reed mats on the walls, hanging bundles and a central hearth under dark roof beams','Upopoy, inside a chise',
 "The inside of a chise, as Commons titles the file. The walls are lined with woven mats in black, red and natural reed, and bundles hang from the roof beams; the Commons description calls them inau. Imagine this lit by the fire and you have the room the manga's Ainu characters sit in. The light is dim, so expect something like this rather than a bright exhibition hall.")
add('up-sword','c12b6b65-image.jpg','Ainu_ritual_sword_National_Ainu_Museum_and_Park.jpg','Hiart','cc0','2025','A dark curved sword in an ornate scabbard on a clear stand, with a label reading Emushi, Ritual Sword','National Ainu Museum, ritual sword',
 "A ritual sword in the museum, with the label reading \u30a8\u30e0\u30b7 (<em>emushi</em>) and Ritual Sword in four languages. Its scabbard is dark and finely worked with pierced metal panels. The label calls it a ritual sword, not a weapon, so I would not read it as one.")
add('up-basin','717e8268-image.jpg','Ainu_four-handled_basin_National_Ainu_Museum_and_Park.jpg','Hiart','cc0','2025','A dark wide bowl with four long handles tipped with metal caps, on a white display surface','National Ainu Museum, four-handled basin',
 "A wide dark basin with four long handles tipped with metal, as Commons titles it. It is carved with fine patterns on the sides. I cannot tell you its use or age from the photo, so check the label in the museum.")
add('up-bark','16585125-image.jpg','Bark_fiber_garment_National_Ainu_Museum_and_Park.jpg','Hiart','cc0','2025','A brown woven garment with dark blue appliqu\u00e9 bands and fine white stitched lines in a glass case','National Ainu Museum, bark fiber garment',
 "A bark fiber garment, as Commons titles it, in a warm brown woven cloth with dark blue bands and blue-green patches stitched with fine white lines. The cloth looks rough and strong, which is the point: this is clothing for daily work. Photographed through glass, so there are some reflections.")
add('up-grass','0f0b979a-image.jpg','Grass_fiber_garment_National_Ainu_Museum_and_Park.jpg','Hiart','cc0','2025','A pale woven garment with black bands and colored embroidery in stepped spiral patterns, seen through a glass case','National Ainu Museum, grass fiber garment',
 "A grass fiber garment, as Commons titles it, in a pale woven cloth with black bands and thread in green, yellow and pink in stepped, curling patterns. Compare it with the brown bark one above: the patterns differ from garment to garment. A visitor is reflected in the glass.",maxw=640)
add('up-meal','7129329f-image.jpg','Seasonal_Ohaw_set_meal_Umizora-no-Haru.jpg','\u63ac\u8336','bysa4','2026-08-22','A wooden tray with a bowl of rice, a carved wooden bowl of soup with leek, thin slices of roast meat, and a cup of tea','Upopoy, seasonal ohaw set at Umizora no Haru',
 "A seasonal <em>ohaw</em> set at the Upopoy restaurant Umizora no Haru (\u6d77\u7a7a\u306e\u30cf\u30eb), according to Commons. <em>Ohaw</em> is the Ainu word for a soup. Here it comes in a carved wooden bowl with leek and root vegetables, next to rice and a few slices of roast meat. The menu changes by season and I have not checked what is served now.")

def build(k):
    p=P[k]
    os.makedirs(OUT,exist_ok=True)
    im=Image.open(U+p['up']).convert('RGB')
    w=min(1200,im.width)
    if im.width>w: im=im.resize((w,round(im.height*w/im.width)),Image.LANCZOS)
    im.save(OUT+k+'.jpg',quality=84,optimize=True); im.save(OUT+k+'.webp',quality=80)
    p['w'],p['h']=im.size
def esc(s): return s.replace('&','&amp;').replace('"','&quot;').replace('<','&lt;')
def fig(k,hero=False):
    p=P[k]; lic,url=L[p['lic']]
    d=(' '+p['date']) if p['date'] else ''
    cap=f"{p['cap']} — <a href=\"{url}\" target=\"_blank\" rel=\"noopener\">{lic}</a> {p['auth']}{d}, via <a href=\"https://commons.wikimedia.org/wiki/File:{p['fn']}\" target=\"_blank\" rel=\"noopener\">Wikimedia Commons</a> (resized)"
    if p['lic']=='cc0': cap=f"{p['cap']} — {p['auth']}, <a href=\"{url}\" target=\"_blank\" rel=\"noopener\">CC0</a>{d}, via <a href=\"https://commons.wikimedia.org/wiki/File:{p['fn']}\" target=\"_blank\" rel=\"noopener\">Wikimedia Commons</a> (resized)"
    if hero:
        sty='margin:0 0 40px;'; img='width:100%;max-height:420px;object-fit:cover;display:block;'; ld='eager'
    else:
        sty=f"margin:28px auto 12px;max-width:{p['maxw']}px;"; img='width:100%;height:auto;display:block;border-radius:4px;'; ld='lazy'
    s=f'''<figure style="{sty}">
      <picture>
        <source srcset="/anime/golden-kamuy/images/{k}.webp" type="image/webp">
        <img src="/anime/golden-kamuy/images/{k}.jpg" alt="{esc(p['alt'])}" width="{p['w']}" height="{p['h']}" style="{img}" loading="{ld}">
      </picture>
      <figcaption style="font-size:12px;color:#888;margin-top:6px;">{cap}</figcaption>
    </figure>
'''
    if not hero and p['desc']: s+=f"    <p>{p['desc']}</p>\n"
    return s
for k in P: build(k)
