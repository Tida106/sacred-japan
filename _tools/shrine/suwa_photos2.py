import re,csv,io
from PIL import Image
R='/home/claude/sacred-japan/'; SL='suwa-taisha'
ZT='https://commons.wikimedia.org/w/index.php?search=%s&title=Special:MediaSearch&type=image'
LIC={'cc0':('CC0','https://creativecommons.org/publicdomain/zero/1.0/'),
 'by3':('CC BY 3.0','https://creativecommons.org/licenses/by/3.0/'),
 'by4':('CC BY 4.0','https://creativecommons.org/licenses/by/4.0/')}
F='https://commons.wikimedia.org/wiki/File:'
HON=ZT%'Suwa+taisha+Kamisha+Honmiya+panoramio'
P={
'honmiya-otorii':('ec5da7fe','Saigen Jiro',F+'Suwa-taisha_Kamisha_Honmiya_otorii.jpg','cc0'),
'honmiya-big-torii':('dd67d384','Immanuelle',F+'Suwa_Taisha_Kamisha_Honmiya_Big_Torii.jpg','by4'),
'honmiya-dragon-temizu':('fc230fe9','z tanuki',HON,'by3'),
'honmiya-myojinyu':('6cc452f5','z tanuki',HON,'by3'),
'honmiya-nunobashi':('113b04ea','Saigen Jiro',F+'Suwa-taisha_Kamisha_Honmiya_nunobashi.jpg','cc0'),
'honmiya-shikyakumon':('62ef3202','Saigen Jiro',F+'Suwa-taisha_Kamisha_Honmiya_shikyakumon.jpg','cc0'),
'honmiya-shikyakumon-2':('f8b14f57','Saigen Jiro',F+'Suwa-taisha_Kamisha_Honmiya_shikyakumon-2.jpg','cc0'),
'honmiya-haisho':('0311301f','Saigen Jiro',F+'Suwa-taisha_Kamisha_Honmiya_haisho.jpg','cc0'),
'honmiya-haiden-front':('72a94720','Saigen Jiro',F+'Suwa-taisha_Kamisha_Honmiya_haiden-1.jpg','cc0'),
'honmiya-haiden-angle':('d9b9331c','Saigen Jiro',F+'Suwa-taisha_Kamisha_Honmiya_haiden-3.jpg','cc0'),
'honmiya-chokushiden':('bccc7c12','Saigen Jiro',F+'Suwa-taisha_Kamisha_Honmiya_chokushiden_and_gokenrou.jpg','cc0'),
'honmiya-shinmesha':('6590bbaa','Saigen Jiro',F+'Suwa-taisha_Kamisha_Honmiya_shinmesha.jpg','cc0'),
'honmiya-okutsuishi':('1ca95d53','Saigen Jiro',F+'Suwa-taisha_Kamisha_Honmiya_okutsuishi.jpg','cc0'),
'maemiya-haisho':('144acedf','Saigen Jiro',F+'Suwa-taisha_Kamisha_Maemiya_haisho.jpg','cc0'),
'onb-maemiya-4':('e7c9e2e1','z tanuki',ZT%'Suwa+taisha+Kamisha+Maemiya+panoramio','by3'),
'akimiya-subshrines-2':('566f4251','z tanuki',ZT%'Suwa+taisha+Shimosha+Akimiya+panoramio','by3'),
'akimiya-subshrines-3':('ff544520','z tanuki',ZT%'Suwa+taisha+Shimosha+Akimiya+panoramio','by3'),
'harumiya-kaguraden':('17adc311','Saigen Jiro','https://commons.wikimedia.org/wiki/User:Saigen_Jiro','cc0'),
'harumiya-approach':('b698b5bc','z tanuki',ZT%'Suwa+taisha+Shimosha+Harumiya+panoramio','by3'),
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
# (anchor key to insert after, new blocks)
INS={
'__h3_honmiya':[
 blk('honmiya-otorii','The large stone torii at the entrance to Kamisha Honmiya with a shrine stone marker and steps beyond','The stone torii at the entrance to Kamisha Honmiya',"The walk begins at this large stone torii, with the shrine’s name stone at the left and a flight of steps beyond. It is a plain, solid gate, and a good place to bow before you go in."),
 blk('honmiya-big-torii','A large bronze-green torii with a thick shimenawa rope and a gate beyond, with sunlight flaring through the trees','A large torii hung with a thick shimenawa',"A second, much more imposing torii, its pillars the green-grey of weathered bronze and a heavy shimenawa slung across the upper beam. Sunlight flares through the cedars at the left, and a roofed gate waits at the far end of the paved approach. The wooden board at the right is a notice of rules for visitors; I can read only the heading, so check it on the day."),
 blk('honmiya-dragon-temizu','A bronze dragon pouring water into a purification basin edged with moss, with the Honmiya buildings behind','The dragon temizu at Kamisha Honmiya',"The dragon-shaped water basin, a bronze dragon curled over a mossy rock and pouring water from its mouth, with bamboo ladles laid ready. A bamboo fence hung with paper strips runs behind it, and visitors are walking toward the worship halls in the background. The bare ground and light suggest an early-spring visit."),
 blk('honmiya-myojinyu','A stone lion head pouring water into a rock basin with a signboard reading Myojin-yu, with ladles laid across it','The Myojin-yu water basin',"Next to the dragon basin is a second one, fed from the mouth of a carved stone lion. The signpost reads <em>Myojin-yu</em> and, as I read it, says the water is traditionally linked to Suwa Myojin and to the source of Suwa’s hot springs. Rows of sake barrels stand in the background at right."),
],
'honmiya-gate':[
 blk('honmiya-nunobashi','The long raised Nunobashi covered corridor above a mossy stone wall, seen between tall cedar trunks, with an information board in front','The Nunobashi covered corridor',"Seen from the gravel below, the Nunobashi is a long, low-roofed corridor raised on a stone-walled bank, with an information board in front and tall cedar trunks standing like pillars in the foreground. Its dark wooden frame lets you look through to the greenery behind."),
 blk('honmiya-shikyakumon','The Shikyakumon, a four-legged gate with a gently curved shingle roof and latticed doors, between two thatch-roofed buildings','The Shikyakumon gate, from the front',"The Shikyakumon, the four-legged gate, seen straight on. It has a curved shingle roof, a row of white-tipped rafter ends under the eaves, and latticed doors through which you can see the halls beyond. Thatch-roofed buildings with fresh pale timber stand on either side."),
 blk('honmiya-shikyakumon-2','The Shikyakumon seen past a leafy branch, with the courtyard and a lantern at the right','The Shikyakumon through the leaves',"The same gate from the side, with a branch of fresh leaves crossing in front of it. Here you can see the paved courtyard on the right and, at the far end, what looks like a large drum under the eaves. The warm, new-looking wood beside the older timber shows how often these buildings are repaired."),
],
'honmiya-haisho-grounds':[
 blk('honmiya-haisho','The Honmiya Haisho worship hall with white curtains bearing the shrine crest, two visitors standing inside, and a sign at the right','The Haisho worship hall',"The Haisho is the open worship hall where visitors stand to pray. White curtains bearing the shrine’s leaf crest hang across the front, and two visitors stand inside. A sign at the right, as I read it, asks that only people receiving a formal prayer use this entrance and others go to the offering place."),
],
'honmiya-carving':[
 blk('honmiya-haiden-front','The Honmiya Haiden seen from the front, with a curved gable, gold fittings and stone-paved courtyard, flanked by two lanterns','The Haiden, seen from the front',"The Haiden from the front. A curved central gable carries gold fittings and fine carving, with long, low-roofed wings stretching to either side and a stone lantern at each edge. The deep green forest behind makes the gold stand out."),
 blk('honmiya-haiden-angle','The Honmiya Haiden seen from an angle, showing carved eaves, gold fittings and the stone courtyard','The Haiden, from an angle',"From an angle you can see how deep the building is: carved beams and brackets under the curved gable, gold-edged stairs and rails, and a tall tree growing up beside it. A wooden stand holding a folded white offering sits in the courtyard at the right."),
],
'honmiya-chokuganden':[
 blk('honmiya-chokushiden','Wooden shrine buildings with a long low corridor and a raised hall among tall cedar trees, with information signs in front','The Chokushiden and the Gokenro',"Calm wooden buildings in a quiet corner of the grounds: a raised hall on the left, a long low corridor to its right and tall cedars all around. The Commons title calls them the Chokushiden and the Gokenro, which I take to be a hall for imperial envoys and a related corridor, but I cannot tell the exact roles from the photo."),
],
'honmiya-okuninushi':[
 blk('honmiya-shinmesha','A small shrine hall beside a huge old tree with a stone lantern at the right','The Shinmesha',"The Shinmesha stands in a clearing beside a great old tree, with a large moss-covered stone lantern at the right. The name suggests a stable for the shrine’s sacred horse, and a clear paved path leads up to it."),
 blk('honmiya-okutsuishi','A moss and fern covered rock enclosed by a shimenawa with paper streamers, with a stone lantern behind','The Okutsu-ishi rock',"A large rock wrapped in moss and small ferns, roped off with a shimenawa hung with paper streamers and lit by a patch of sun. A stone lantern with a mossy cap stands behind it. I read it as an object of worship in its own right, though the photo does not explain its role."),
],
'maemiya-jikkenro':[
 blk('maemiya-haisho','The Maemiya worship hall with a thick shimenawa, a lantern on each side and a flight of stone steps in front','The worship area at Maemiya',"The worship area at the top of the stone steps, with a thick shimenawa across the front, a white curtain bearing the shrine crest and a stone lantern at each side. Cedars lean in overhead, and the whole place feels tucked into the hillside."),
],
'onb-maemiya':[
 blk('onb-maemiya-4','The fourth Onbashira of Kamisha Maemiya, a bare pale pillar inside a small wooden fence on a leaf-strewn slope','The fourth pillar at Kamisha Maemiya',"The fourth pillar at Maemiya stands on a slope of fallen leaves with bare trees around it, inside a small fence hung with paper streamers. The sign on the trunk reads <em>Maemiya Yonnoonbashira</em>, the fourth pillar of Maemiya."),
],
'akimiya-subshrines':[
 blk('akimiya-subshrines-2','Two auxiliary shrines in the Akimiya precincts with name boards and a metal fire-extinguishing box in front','More auxiliary shrines at Akimiya',"Two roofed auxiliary shrines beside a paved path, with wooden name boards that, as I read them, include Kashima-sha, Kamo Kamishimo-sha and Yasaka-sha. A metal box in front is marked for fire-fighting water."),
 blk('akimiya-subshrines-3','A central small shrine with a smaller shrine on each side atop stone steps in the Akimiya precincts','A trio of small shrines at Akimiya',"A group of three miniature shrines on a stone platform, with a larger one in the middle. The boards beside them read Kotaijingu-sha (for the deities of Ise) and Inari-sha, as I read them, so Ise and Inari are both represented here among the smaller shrines."),
],
'__h3_harumiya':[
 blk('harumiya-approach','A cobbled approach leading to the Harumiya Kaguraden with its great shimenawa between tall cedar trees and a festival information board','The approach to the Harumiya Kaguraden',"The approach at Harumiya is a stone path with a band of cobbles down the middle, running straight toward the Kaguraden under tall cedars. The board at the right announces the Onbashira festival, as I read it."),
 blk('harumiya-kaguraden','The Harumiya Kaguraden with a thick shimenawa across its front, a stone-paved path and an ema rack at the right','The Harumiya Kaguraden',"The Kaguraden up close, its great straw rope slung across the front and an ema rack with plaques and paper cranes at the right. The cobbled path leads straight to the steps."),
],
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
    s=s[:j]+'  '+add+s[j:] if False else s[:j]+add+s[j:]
open(p,'w',encoding='utf-8').write(s)
rows=[]
for k,(u,a,l,li) in P.items():
    ln,lu=LIC[li]; rows.append(['guides/suwa-taisha',f'/guides/{SL}/images/{k}.jpg',ln,lu,l,f'{k}: Photo: {a}, {ln}, via Wikimedia Commons (resized)'])
b=io.StringIO(); csv.writer(b,lineterminator='\r\n').writerows(rows)
open(R+'PHOTO-CREDITS.csv','a',encoding='utf-8',newline='').write(b.getvalue())
print(len(P))
