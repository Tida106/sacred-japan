import re,os,csv,json
from PIL import Image
R='/home/claude/sacred-japan/'; A='/mnt/user-data/attachments/53e3d492-4bf8-5cd9-a0ec-63a7cbefb1d9/'
SL='nagoya-castle'; D=R+f'guides/{SL}/images/'
S4=('CC BY-SA 4.0','https://creativecommons.org/licenses/by-sa/4.0/')
PD=('Public domain','https://commons.wikimedia.org/wiki/Template:PD-self')
def fig(k,au,lic,alt,cap,w,h):
    img=f'<picture><source srcset="/guides/{SL}/images/{k}.webp" type="image/webp"><img src="/guides/{SL}/images/{k}.jpg" alt="{alt}" width="{w}" height="{h}" loading="lazy" style="width:100%;height:auto;border-radius:4px;display:block;"></picture>'
    fc=f'<figcaption style="font-size:13px;color:var(--enshu);margin-top:10px;text-align:center;line-height:1.6;">{cap}<br>Photo: {au}, <a href="{lic[1]}" target="_blank" rel="noopener" style="color:var(--enshu);">{lic[0]}</a>, via Wikimedia Commons (resized)</figcaption>'
    mw='max-width:760px;' if w>=h else 'max-width:420px;'
    return f'<figure style="margin:28px auto;{mw}">{img}{fc}</figure>\n'
P=[
('palace-room','f8420b28','Mauricio V. Genta',S4,
 'A tatami room seen through a doorway, with a black coffered ceiling fitted with gold ornaments and wall panels painted with crowds, riders and pine groves on a gold ground, framed in black lacquer and gold fittings',
 'Inside the palace, 27 August 2023 (Commons: Interior of Nagoya Castle, in Spanish).',
 "Commons titles this only as an interior of Nagoya Castle, and the colours point to the Honmaru Palace. The view is taken from the threshold, which is how most visitors see the rooms. Black lacquer frames hold gold-ground paintings of crowds, riders and groves of pine, with gold fittings at each joint, and the black ceiling carries more gold ornaments overhead. A second room opens at the right with a blue shoreline painted on its sliding doors. The wall paintings in the reconstructed palace are reproductions, and I am describing only what the photo shows."),
('palace-gold','e0b15374','Kiyotaka Katsuragi',S4,
 'An empty tatami room with walls of plain gold leaf, pale coffered wood ceiling, bamboo-screen transoms, and painted doors with a snowy rock on the left and red maple and pine on the right',
 'A room of the reconstructed Honmaru Palace, 2015 (Commons: Honmaru Palace, reconstructed).',
 "This is the plainest and most dramatic room in the set. Three wall panels of gold leaf face you with nothing painted on them, and the light turns the whole room amber. The painted doors do the talking: a snow-covered rock on the left, red maple leaves and slender pines on the right, so two seasons meet in one room. Above, the pale wooden ceiling is divided into square coffers and the bamboo transoms let in a little light."),
('palace-sea','97bd1088','Kiyotaka Katsuragi',S4,
 'A tatami room whose wall panels show a blue bay with boats and a small red torii on a sandy shore, with a doorway opening to another room of black lacquer and gold-framed paintings',
 'Another room of the reconstructed Honmaru Palace, 2015 (Commons: Honmaru Palace, reconstructed).',
 "Here the walls are a seascape. Blue water fills the panels on the right, boats float on it, and a small red torii stands on the pale shore at the far right. To the left, an open sliding door shows the next room, with black lacquer, gold fittings and more painted panels. It gives a good idea of how the rooms connect, and why I tell people to look through each doorway before they step through it. Commons gives the room title only in Japanese; as far as I can tell, the two Katsuragi photos come from different rooms."),
('exhibit-taimenjo','e84c2bc7','Gryffindor',PD,
 'A display of a reception room with tatami, a bird-cage charcoal brazier, two candle stands, a green-covered bench, lattice screens and painted wall panels',
 'A museum display of a reception room, 15 February 2011 (Commons: Nagoya Castle).',
 "This one is different, and I include it because it shows what the palace looked like in the display cases before the reconstruction. It is a model room: tatami, a brazier under a bird-cage cover, two tall candle stands, a bench covered in green silk, and lattice sliding screens with small painted panels below. The photo was taken in 2011, years before the rebuilt palace opened in full."),
('exhibit-sign','c22a4b84','Gryffindor',PD,
 'The same reception room display from the front, with a floor plan sign on the left and a bilingual information sign on the right, labelled Taimenjo',
 'The same display with its signs, 15 February 2011 (Commons: Nagoya Castle).',
 "The signs identify the room as the Taimenjo, with a floor plan on one side and an English text on the other. As I read it, the English sign explains that in the original Honmaru Palace this room lay innermost among the public rooms and served as a reception room for daily and political affairs and informal meetings, and that the panels show seasonal scenes of ordinary people's lives in Kyoto and elsewhere. Please treat it as an exhibit label from 2011, not as the current wording in the palace."),
('kettle','18e69245','Gryffindor',S4,
 'A gold tea kettle with a hammered body, a round crest, small fish-head handles and a gold lid with a round knob, displayed in a glass case on a dark red cloth',
 'The gold tea kettle at the Ninomaru Teahouse, 23 November 2017 (Commons: Ninomaru Teahouse).',
 "The Commons description says this is a gold-plated tea kettle (pure silver body with 24-karat gold plating) shown at the Ninomaru Teahouse, and that in 2017 tea was served with it on Fridays from 10:00 to 16:00. That is a six-year-old note, so ask at the castle whether it still runs. The hammered body catches the light in small facets, and the fish-head handles echo the shachi on the keep."),
]
H={};rows=[]
for k,f,au,lic,alt,cap,ps in P:
    im=Image.open(A+f+'-image.jpg').convert('RGB'); print(k,im.size)
    if im.width>1200: im=im.resize((1200,round(im.height*1200/im.width)),Image.LANCZOS)
    im.save(D+k+'.jpg',quality=84,optimize=True); im.save(D+k+'.webp',quality=80)
    H[k]=fig(k,au,lic,alt,cap,im.width,im.height)+f'    <p>{ps}</p>\n'
    rows.append([f'guides/{SL}',f'/guides/{SL}/images/{k}.jpg',lic[0],lic[1],lic[1],f'{cap}Photo: {au}, {lic[0]}, via Wikimedia Commons (resized)'])
p=R+f'guides/{SL}/index.html'; s=open(p,encoding='utf-8').read()
def aft(s,a,t):
    assert s.count(a)==1,a; return s.replace(a,a+'\n'+t)
s=aft(s,'which in fact it has.</p>',H['palace-room']+H['palace-gold']+H['palace-sea']+H['exhibit-taimenjo']+H['exhibit-sign'])
s=aft(s,'to frame a shot like this.</p>',H['kettle'])
open(p,'w',encoding='utf-8').write(s)
with open(R+'PHOTO-CREDITS.csv','a',encoding='utf-8',newline='') as f:
    w=csv.writer(f,lineterminator='\r\n'); [w.writerow(r) for r in rows]
for tg in ['div','figure','picture','p','a','ul','li','details','section','h2']:
    assert len(re.findall(f'<{tg}[ >]',s))==len(re.findall(f'</{tg}>',s)),tg
for m in re.findall(r'<script type="application/ld\+json">(.*?)</script>',s,re.S): json.loads(m)
print('ok',s.count('<figure'))
