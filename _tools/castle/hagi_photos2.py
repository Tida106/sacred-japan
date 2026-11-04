import re,csv,json
from PIL import Image
R='/home/claude/sacred-japan/'; A='/mnt/user-data/attachments/53e3d492-4bf8-5cd9-a0ec-63a7cbefb1d9/'
SL='hagi-castle'; D=R+f'guides/{SL}/images/'
L={'S4':('CC BY-SA 4.0','https://creativecommons.org/licenses/by-sa/4.0/'),
   'S3':('CC BY-SA 3.0','https://creativecommons.org/licenses/by-sa/3.0/'),
   'B2':('CC BY 2.0','https://creativecommons.org/licenses/by/2.0/')}
# key,file,author,lic,alt,caption,para,anchor,small
P=[
('hero-shizuki','eb7fa9ae','Kuru man (retouched by トトト)','B2',
 'Wooded Mount Shizuki behind a green moat and a stone wall, with a tall stone marker post reading Historic Site, Hagi Castle ruins, in the foreground right',
 'Mount Shizuki behind the moat and the stone walls, 22 September 2010.',None,'HERO',False),
('keep-base','d558e3f7','Reggaeman','S3',
 'A stone base with sloping walls rising from a calm moat, with reeds along the bank and a wooded hill behind it',
 'The stone base of the former keep, 19 October 2006.',
 "Commons titles this view as the keep base, the foundation that Japan-guide lists among what remains. It is a small, low-resolution photo from 2006, and I have not enlarged it. What it shows well is the shape: the sloped stone wall rising straight out of the water, with reeds along the bank and the wooded hill behind. Please remember there was once a five-story keep on top of this, according to Wikipedia, and today there is only the stone.",
 'which I think is the best way to see what the walls once held up.</p>',True),
('shizukiyama-torii','ec256f2a','そらみみ','S4',
 'A grey stone torii with a green plaque, standing on a wide gravel approach lined with trees, with a stone marker post at the left',
 'The torii on the approach to Shizukiyama Shrine, 4 May 2017.',
 "Commons describes this as the approach to Shizukiyama Shrine. The torii has a green plaque that appears to read the shrine's name, and the right pillar is inscribed with what reads as a date in the 23rd year of Meiji, in June. The stone post on the left reads &ldquo;縣社&rdquo;, an old shrine rank. Please treat my reading of the inscriptions as a guide's note, since I am reading them from the photo. The wide gravel path under the trees is the kind of walk that makes the ruins feel like a shrine ground.",
 "so please treat them as a guide's note.</p>",False),
('shrine-hall','458a8076','そらみみ','S4',
 'A wooden shrine hall with a curved green-copper roof, a white banner with a black crest across the front, and red-and-white curtains along the base',
 'A shrine hall hung with a crest banner and red-and-white curtains. Uploaded 29 July 2017.',
 "I could not confirm from the Commons page which building this is, so please read it as an illustration. The setting and the banner fit the Mori family shrine that the city site places in the Honmaru ruins. The black crest on the banner looks like a line above three dots, which I believe is a Mori family mark, though I have not confirmed it. The red-and-white curtains suggest a festival or a ceremony, and the date is not given.",
 None,False),
('stone-bridge','eeebd790','そらみみ','S4',
 'A small arched stone bridge with carved posts over a pond of tall green irises, with stone lanterns and a stepped stone monument beyond it',
 'An arched stone bridge among irises and lanterns. Uploaded 28 July 2017.',
 "The Commons page I saw did not give a description or a date, so I will not name the place. It is a small arched stone bridge with carved posts, set over a pond full of tall irises, with stone lanterns and a stepped stone monument behind it. Two visitors walk past on the path at the right. The informational signboards nearby suggest a place meant for visitors, which is why I include it as an illustration of a park path here.",
 None,False),
('moat-gokuraku','7be3297f','そらみみ','S4',
 'A calm moat reflecting clouds, with a long stone wall on the right, a low stone bridge at the back, and wooded Mount Shizuki beyond',
 'The inner moat and the Gokuraku Bridge, 4 May 2017.',
 "This is the view that explains the layout. The inner moat runs along a high stone wall, and at the far end you can see the low stone bridge that Commons calls the Gokuraku Bridge. Mount Shizuki rises behind it, which the city site says carried the last fortress. It is a quiet, still photo, and it shows how much of the castle is water, stone and trees now.",
 'so signs and fittings may have changed.</p>',False),
]
def mk(k,f,au,lic,alt,cap,hero,small):
    im=Image.open(A+f+'-image.jpg').convert('RGB')
    if im.width>1200: im=im.resize((1200,round(im.height*1200/im.width)),Image.LANCZOS)
    im.save(D+k+'.jpg',quality=84,optimize=True); im.save(D+k+'.webp',quality=80)
    l=L[lic]; ld='eager' if hero else 'lazy'
    st=('width:100%;max-height:420px;object-fit:cover;object-position:center 40%;border-radius:4px;display:block;' if hero else 'width:100%;height:auto;border-radius:4px;display:block;')
    img=f'<picture><source srcset="/guides/{SL}/images/{k}.webp" type="image/webp"><img src="/guides/{SL}/images/{k}.jpg" alt="{alt}" width="{im.width}" height="{im.height}" loading="{ld}" style="{st}"></picture>'
    fc=f'<figcaption style="font-size:13px;color:var(--enshu);margin-top:10px;text-align:center;line-height:1.6;">{cap}<br>Photo: {au}, <a href="{l[1]}" target="_blank" rel="noopener" style="color:var(--enshu);">{l[0]}</a>, via Wikimedia Commons (resized)</figcaption>'
    return im,l,img,fc
p=R+f'guides/{SL}/index.html'; s=open(p,encoding='utf-8').read()
groups=[]
for t in P:
    if t[7] is None: groups[-1].append(t)
    else: groups.append([t])
rows=[]
sizes={}
for g in groups:
    html=''
    for (k,f,au,lic,alt,cap,para,anc,small) in g:
        hero=(k=='hero-shizuki')
        im,l,img,fc=mk(k,f,au,lic,alt,cap,hero,small); sizes[k]=im.size
        if hero: html=f'  <figure style="margin:0 0 48px;">{img}{fc}</figure>\n\n'
        else:
            mw='610px' if small else ('420px' if im.height>im.width else '760px')
            html+=f'\n    <figure style="margin:28px auto;max-width:{mw};">{img}{fc}</figure>\n    <p>{para}</p>'
        rows.append([f'guides/{SL}',f'/guides/{SL}/images/{k}.jpg',l[0],l[1],l[1],cap+f' Photo: {au}, {l[0]}, via Wikimedia Commons (resized)'])
    anc=g[0][7]
    if anc=='HERO':
        a='  <!-- TABLE OF CONTENTS -->'; assert s.count(a)==1; s=s.replace(a,html+a)
    else:
        assert s.count(anc)==1,anc; s=s.replace(anc,anc+html)
# shrine photos group: place after p2 anchor
a2="so please treat them as a guide's note.</p>"
open(p,'w',encoding='utf-8').write(s)
with open(R+'PHOTO-CREDITS.csv','a',encoding='utf-8',newline='') as fh:
    w=csv.writer(fh,lineterminator='\r\n')
    for r in rows: w.writerow(r)
for tg in ['div','figure','picture','p','a','ul','li','details','section','h2']:
    assert len(re.findall(f'<{tg}[ >]',s))==len(re.findall(f'</{tg}>',s)),tg
for m in re.findall(r'<script type="application/ld\+json">(.*?)</script>',s,re.S): json.loads(m)
print('ok',s.count('<figure'),sizes)
