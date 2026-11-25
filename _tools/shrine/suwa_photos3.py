import re,csv,io
from PIL import Image
R='/home/claude/sacred-japan/'; SL='suwa-taisha'
ZT='https://commons.wikimedia.org/w/index.php?search=%s&title=Special:MediaSearch&type=image'
LIC={'cc0':('CC0','https://creativecommons.org/publicdomain/zero/1.0/'),
 'by3':('CC BY 3.0','https://creativecommons.org/licenses/by/3.0/'),
 'bysa3':('CC BY-SA 3.0','https://creativecommons.org/licenses/by-sa/3.0/'),
 'by4':('CC BY 4.0','https://creativecommons.org/licenses/by/4.0/')}
F='https://commons.wikimedia.org/wiki/File:'
HON=ZT%'Suwa+taisha+Kamisha+Honmiya+panoramio'
P={
'akimiya-heihaiden-angle':('a72a56e3','Saigen Jiro',F+'Suwa-taisha_Shimosha_Akimiya_heihaiden.jpg','cc0'),
'akimiya-heihaiden-front':('1edba42f','663highland',F+'Suwa_taisha_akimiya05n4592.jpg','bysa3'),
'honmiya-nunobashi-inside':('f2d95d1b','Immanuelle',F+'Nunobashi_Suwa_Taisha_Kamisha_Honmiya_corridor.jpg','by4'),
'honmiya-ema-horse':('71960655','z tanuki',ZT%'Suwa+taisha+Kamisha+Honmiya+panoramio','by3'),
'harumiya-heihaiden-prayer':('8e0fd759','Saigen Jiro','https://commons.wikimedia.org/wiki/User:Saigen_Jiro','cc0'),
}
SIZE={}
for k,(u,a,l,li) in P.items():
    im=Image.open(f'/mnt/user-data/uploads/{u}-image.jpg').convert('RGB')
    w,h=im.size; tw=min(900 if h>w else 1200,w); th=round(h*tw/w)
    im=im.resize((tw,th),Image.LANCZOS)
    d=R+f'guides/{SL}/images/{k}'
    im.save(d+'.jpg',quality=84,optimize=True); im.save(d+'.webp',quality=80); SIZE[k]=(tw,th)
def blk(k,alt,cap,text):
    u,a,l,li=P[k]; ln,lu=LIC[li]; w,h=SIZE[k]; mw=min(420 if h>w else 760,w)
    return f'''<figure style="margin:28px auto;max-width:{mw}px;"><picture><source srcset="/guides/{SL}/images/{k}.webp" type="image/webp"><img src="/guides/{SL}/images/{k}.jpg" alt="{alt}" width="{w}" height="{h}" loading="lazy" style="width:100%;height:auto;border-radius:4px;display:block;"></picture><figcaption style="font-size:13px;color:var(--enshu);margin-top:10px;text-align:center;line-height:1.6;">{cap}<br>Photo: <a href="{l}" target="_blank" rel="noopener">{a}</a>, <a href="{lu}" target="_blank" rel="noopener">{ln}</a>, via Wikimedia Commons (resized)</figcaption></figure>
  <p>{text}</p>
'''
INS={
'honmiya-nunobashi':[blk('honmiya-nunobashi-inside','Inside the Nunobashi corridor, a long wooden walkway with paper streamers and hanging lanterns leading to a bright far end','Inside the Nunobashi',"Stepping inside, the Nunobashi becomes a long wooden tunnel: plank floor, rounded brackets carved with a small crest, white paper streamers and metal lanterns hanging along both sides, and a bright opening far ahead with a couple of walkers. Mossy ground and old cedar trunks show through the open sides.")],
'honmiya-haisho':[blk('honmiya-ema-horse','A large ema plaque with a gilded horse in relief and the characters for dedication hanging under the eaves','A large horse ema under the eaves',"Under the eaves hangs a large plaque with a horse carved in relief, still showing flecks of gold. The characters at the top read <em>hono</em>, \u201cdedication\u201d. A dedication in this shape is the origin of the small ema you can buy and write on.")],
'akimiya-torii':[
 blk('akimiya-heihaiden-front','The Akimiya Heihaiden from the front with two visitors praying, long galleries on both sides and a prayer-entrance sign at the right','The Heihaiden at Akimiya, from the front',"The Heihaiden at Akimiya from the front: a two-tier central gate-like hall with a curved roof and heavy carving, and long open galleries running to both sides. Three visitors stand at the steps to pray, and the white sign at the right reads <em>Kitosha iriguchi</em>, the entrance for those receiving a prayer, as I read it."),
 blk('akimiya-heihaiden-angle','The Akimiya Heihaiden from an angle, with layered curved roofs, gold fittings and carving, and visitors standing in front','The Heihaiden at Akimiya, from an angle',"From the side the layering is clearer: a sweeping curved roof over the central hall, gold-tipped rafters and fittings, dense carving below, and galleries stepping away on each side. A wooden stand at the right holds ema and paper cranes. This is the same hall as the photo above, taken on a cooler, overcast day."),
],
'harumiya-heihaiden':[blk('harumiya-heihaiden-prayer','Visitors praying in front of the Harumiya Heihaiden, with an ema rack and paper cranes at the right','Visitors praying at the Harumiya Heihaiden',"Two visitors stand to pray in front of the Heihaiden. An ema rack and strings of colourful paper cranes hang at the right, so even this quiet site has a steady stream of worshippers.")],
}
p=R+f'guides/{SL}/index.html'
s=open(p,encoding='utf-8').read()
def after_para(s,imgkey):
    i=s.index(f'images/{imgkey}.jpg"'); j=s.index('</p>\n',i)+len('</p>\n'); return j
for key,blocks in INS.items():
    add=''.join(blocks)
    if key=='__h3_honmiya':
        i=s.index('<h3 id="honmiya"'); j=s.index('</p>\n',i)+5
    elif key=='__h3_harumiya':
        i=s.index('<h3 id="harumiya"'); j=s.index('</p>\n',i)+5
    else: j=after_para(s,key)
    s=s[:j]+add+s[j:]
open(p,'w',encoding='utf-8').write(s)
rows=[]
for k,(u,a,l,li) in P.items():
    ln,lu=LIC[li]; rows.append(['guides/suwa-taisha',f'/guides/{SL}/images/{k}.jpg',ln,lu,l,f'{k}: Photo: {a}, {ln}, via Wikimedia Commons (resized)'])
b=io.StringIO(); csv.writer(b,lineterminator='\r\n').writerows(rows)
open(R+'PHOTO-CREDITS.csv','a',encoding='utf-8',newline='').write(b.getvalue())
print(len(P))
