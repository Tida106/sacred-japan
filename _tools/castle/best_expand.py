import csv,re,os,html
R='/home/claude/sacred-japan/'
rows=list(csv.DictReader(open(R+'PHOTO-CREDITS.csv',encoding='utf-8-sig',newline='')))
def row(slug,name):
    c=[r for r in rows if r['page'].rstrip('/').endswith('/'+slug) and r['image'].split('/')[-1]==name]
    assert c,(slug,name); return c[-1]
from PIL import Image
def fig(slug,name,alt,note,first=False,lazy=True):
    r=row(slug,name); p=r['image']; fp=R+p.lstrip('/')
    assert os.path.exists(fp),fp
    wp=p.rsplit('.',1)[0]+'.webp'
    assert os.path.exists(R+wp.lstrip('/')),wp
    w,h=Image.open(fp).size
    mw=420 if h>w else 760
    cap=r['caption']; desc,rest=cap.split('Photo:',1); rest=rest.strip()
    if r['license'] and r['license_url']:
        rest=rest.replace(r['license'],f'<a href="{r["license_url"]}" target="_blank" rel="noopener" style="color:var(--enshu);">{r["license"]}</a>',1)
    rest=rest.replace(' (resized)','').replace(' (cropped and resized)','').replace('via Wikimedia Commons','via Wikimedia Commons (resized)') if 'resized' in cap else rest
    return (f'\n  <figure style="margin:36px auto;max-width:{mw}px;">\n'
      f'    <picture><source srcset="{wp}" type="image/webp"><img src="{p}" alt="{html.escape(alt)}" loading="lazy" style="width:100%;height:auto;border-radius:4px;display:block;"></picture>\n'
      f'    <figcaption style="font-size:13px;color:var(--enshu);margin-top:10px;text-align:center;line-height:1.6;">{desc.strip()}<br>Photo: {rest}</figcaption>\n  </figure>\n'
      f'  <p>{note}</p>\n')
t=open(R+'guides/best-castles-japan/index.html',encoding='utf-8').read()
def put(anchor,h,before=True):
    global t
    assert t.count(anchor)==1,(t.count(anchor),anchor[:60])
    t=t.replace(anchor,(h+anchor) if before else (anchor+h))
IL='class="inline-link" '
# link swaps: first-mention links to individual guides
for nm,sl in [('Himeji Castle','himeji-castle'),('Matsumoto Castle','matsumoto-castle'),('Kumamoto Castle','kumamoto-castle'),('Nijo Castle','nijo-castle')]:
    t=t.replace(f'<a href="/castles/" onclick="trackEvent(\'click\',\'internal\',\'guide_bestcastles_to_castleshub\')">{nm}</a>',
                f'<a {IL}href="/guides/{sl}/" onclick="trackEvent(\'click\',\'internal\',\'guide_bestcastles_to_{sl.replace("-","_")}\')">{nm}</a>')
# --- Himeji
put('  <blockquote>\n    <strong>The Legend of Okiku:</strong>',
 fig('himeji-castle','himeji-hyakken-corridor.jpg','A long wooden corridor inside Himeji Castle','This is the Hyakken Gallery, a long wooden corridor inside the castle. Seen from inside, the spiral plan stops being a diagram and becomes a long walk in which you cannot see far ahead.')+
 fig('himeji-castle','himeji-matchlocks.jpg','A rack of antique matchlock rifles','Matchlocks like these are what the loopholes were cut for. Every one of those 997 openings was placed so that a gunner could cover the path below.'))
put('  <h3>The Resilient White Phoenix</h3>',
 fig('himeji-castle','himeji-okiku-well.jpg',"Okiku's Well at Himeji Castle",'Okiku’s Well sits behind a stone fence. The story is easy to picture standing here: a maid, a missing plate, and a voice counting from the dark.'))
put('  <h2 id="matsumoto-castle-the-black-fortress-and">',
 fig('himeji-castle','himeji-keep-interior.jpg','Inside the main keep at Himeji','Inside the main keep the structure is the point. Thick posts and heavy beams carry the whole weight of the tower, and this is the timber frame that the Showa reconstruction had to rescue.'))
# --- Matsumoto
put('  <div class="key-callout">\n      <p><strong>The Paradox of Peace:</strong>',
 fig('matsumoto-castle','matsumoto-interior.jpg','An upper floor inside Matsumoto Castle keep','The upper floors are bare wood: thick pillars, plain boards and a very steep staircase. Nothing is decorated; the plainness fits a tower built around guns.'))
put('  <h3>The Grudge of Kasuke and Geotechnical Reality</h3>',
 fig('matsumoto-castle','matsumoto-tsukimi.jpg','Inside the Tsukimi-yagura at Matsumoto','The moon-viewing tower is the opposite of the keep. It has a railed veranda and wide openings, and it was built for looking at the autumn moon rather than defending anything.'))
put('  <h2 id="kumamoto-castle-the-impregnable-walls">',
 fig('matsumoto-castle','matsumoto-alps.jpg','Matsumoto Castle on a clear winter day with the Alps behind','On a clear winter day the keep stands in front of the Alps. The black walls stand out against the snow.'))
# --- Kumamoto
put('  <h3>Testing the 300-Year-Old Blueprint</h3>',
 fig('kumamoto-castle','kumamoto-turret-wall.jpg','A turret on a tall flared stone base at Kumamoto Castle','Look at where the wall meets the turret. The base flares outward and then curves up steeply, which is the shape that made it so hard to climb. This photograph was taken in 2009, before the earthquakes.'))
put('  <p><a class="inline-link" href="/guides/kumamoto-castle/" onclick="trackEvent(\'click\',\'internal\',\'guide_bestcastles_to_kumamoto_castle\')">Kumamoto Castle</a>\'s modern resilience',
 fig('kumamoto-castle','kumamoto-towers.jpg','The small keep, the Uto turret and the large keep at Kumamoto Castle','The small keep, the Uto turret and the large keep stand in a row. This is how the skyline looked in 2014, two years before the 2016 earthquakes.'))
put('  <h2 id="nijo-castle-the-sound-of-assassins-and">',
 fig('kumamoto-castle','kumamoto-collapse-2026.jpg','Collapsed stone wall at Kumamoto Castle after the July 2026 earthquake','This is the wall at the Nishi-demaru after the July 2026 earthquake, photographed on 29 August 2026. Kumamoto Castle is still being repaired, so check what is open before you go.'))
# --- Nijo
put('  <p>As visitors walked deeper into the palace toward the Grand Chamber',
 fig('nijo-castle','palace-room.jpg','A room in Nijo Castle Ninomaru Palace with pine paintings on gold','This is the effect the palace was designed to have: pine trees painted on gold leaf, and a coffered ceiling overhead. Photography inside is normally not allowed, so this picture was taken under special conditions.'))
put('  <h3>The Ultimate Regime Change Written in Metal</h3>',
 fig('nijo-castle','garden-pond-summer.jpg','The Ninomaru Garden pond at Nijo Castle in summer','Outside the palace the mood softens. The Ninomaru Garden is laid around a pond, and the palace roof is just beside it.'))
put('  <h2 id="conclusion-walking-the-shadows-of-the">',
 fig('nijo-castle','cherry-grove.jpg','Cherry trees in bloom on the grounds of Nijo Castle','In April cherry trees fill the grounds, and the stone walls and moat become a backdrop for the blossoms.')+
 fig('nijo-castle','autumn-maple.jpg','A maple in autumn color beside the walls and moat at Nijo Castle','Late in the year a single maple can turn red beside the same moat. This photograph is from December 2008.'))
exec(open(R+'_tools/castle/best_expand2.py',encoding='utf-8').read())
open(R+'guides/best-castles-japan/index.html','w',encoding='utf-8').write(t)
print('ok step1',len(t))
