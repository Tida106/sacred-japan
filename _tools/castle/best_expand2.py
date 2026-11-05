def card(slug,name,jp,paras,photos):
    out='\n  <h3 id="%s">%s <span style="font-size:.7em;color:var(--enshu);font-weight:400;">%s</span></h3>\n'%(slug,name,jp)
    for ps in paras: out+='  <p>%s</p>\n'%ps
    for (sl,nm,a,note) in photos: out+=fig(sl,nm,a,note)
    out+='  <p><a %shref="/guides/%s/" onclick="trackEvent(\'click\',\'internal\',\'best_castles_to_%s\')">Read the full %s guide →</a></p>\n'%(IL,slug,slug.replace("-","_"),name)
    return out
sec="""
  <h2 id="ten-more-original-keeps">Ten More Original Keeps</h2>
  <p>Himeji and Matsumoto are two of the twelve castles in Japan whose keeps survive from before the modern era. Kumamoto and Nijo are not on that list; they are here for their walls and their palace. The other ten original keeps are Inuyama, Hikone, Matsue, Maruoka, Matsuyama in Ehime, Bitchu Matsuyama, Uwajima, Kochi, Hirosaki and Marugame. Each is a different kind of place, and each has its own full guide on this site.</p>
"""
sec+=card('inuyama-castle','Inuyama Castle','犬山城',
 ['A small wooden keep on a low cliff above the Kiso River. There is no maze and no vast stone base. You climb a steep staircase to a balcony with a view across two prefectures. It is a good half day from Nagoya. GLTJP and japan-guide give 1537 as the year it was first built, but the date of the present keep is debated, so it is safest to call it one of the oldest.'],
 [('inuyama-castle','inuyama-hero.jpg','Inuyama Castle keep among cherry blossoms','The keep in cherry blossom season, March 2023. It is small, and the blossoms make it look smaller.'),
  ('inuyama-castle','inuyama-lords-room.jpg','The raised Jodan-no-ma room inside Inuyama Castle','Inside, the second floor has a raised room used by the Naruse lords. The Naruse family owned the castle until 2004.')])
sec+=card('hikone-castle','Hikone Castle','彦根城',
 ['On the shore of Lake Biwa in Shiga, about 50 minutes from Kyoto by train. The three-story keep is a National Treasure, and according to Wikipedia the keep was moved here from another castle. Ii Naomasa, a general of Tokugawa Ieyasu, started the castle; Wikipedia says his son Ii Naokatsu finished it in 1622.'],
 [('hikone-castle','hikone-hero.jpg','Hikone Castle keep among autumn leaves','The keep among autumn leaves, November 2016.'),
  ('hikone-castle','hikone-tenbin.jpg','The Tenbin Yagura gate at Hikone Castle','The Tenbin Yagura, a gate with a watchtower on each side, is on the way up to the keep.')])
sec+=card('matsue-castle','Matsue Castle','松江城',
 ['The quiet one among the great keeps. Visit Matsue says it was completed in 1611 after a five-year build by Horio Yoshiharu, and Nippon.com adds that it is the only one of the twelve in the San’in region. For decades nobody could prove when it was built. The proof turned up in 2012 in a shrine, as two wooden talismans, and the keep was designated a National Treasure in 2015.'],
 [('matsue-castle','keep-summer.jpg','Matsue Castle black keep in summer','The black keep in summer, July 2008.'),
  ('matsue-castle','keep-snow.jpg','Matsue Castle keep with snow','The same keep in January 2017, with snow on the ground.')])
sec+=card('maruoka-castle','Maruoka Castle','丸岡城',
 ['Maruoka is known for its roof. It is covered in stone tiles, about 6,000 of them, and Nippon.com puts the total at about 120 tons. Under the roof is a small three-story keep in Fukui that fell down in 1948 and was put back together.'],
 [('maruoka-castle','hero.jpg','Maruoka Castle keep among pines','The keep on its stone base among pines, May 2010.'),
  ('maruoka-castle','stairs.jpg','The steep stairs with a rope inside Maruoka Castle','The stairs inside are steep enough that a rope is provided to help you climb.')])
sec+=card('matsuyama-castle','Matsuyama Castle','松山城',
 ['The one you can see from the street and still have to earn. It sits on a hill in the middle of Matsuyama in Ehime, and you can go up by ropeway or by single-seat lift. Nippon.com says Kato Yoshiaki founded it in 1602. Lightning destroyed the first keep, and the present keep dates to the 1850s.'],
 [('matsuyama-castle','keep-top.jpg','The upper floors of Matsuyama Castle keep','The keep’s upper floors and the veranda around the top story, October 2023.'),
  ('matsuyama-castle','view-roof.jpg','The city and the sea seen from Matsuyama Castle hill','From the castle hill you can see the city and, beyond it, the sea.')])
sec+=card('bitchu-matsuyama-castle','Bitchu Matsuyama Castle','備中松山城',
 ['This one comes with a mountain. It stands in Takahashi, Okayama, on a peak of about 430 meters, and Nippon.com says it is the only one of the twelve on a mountaintop. You walk up from a car park, or all the way from the town. It is not the same as Matsuyama Castle in Ehime, which shares the name. In autumn and early winter, clouds can fill the valley below it.'],
 [('bitchu-matsuyama-castle','clouds.jpg','Bitchu Matsuyama Castle above a sea of clouds','The castle above a sea of clouds, November 2021.'),
  ('bitchu-matsuyama-castle','keep-front.jpg','The keep of Bitchu Matsuyama Castle','The small keep seen from the front, April 2006.')])
sec+=card('hirosaki-castle','Hirosaki Castle','弘前城',
 ['The keep is not where it is supposed to be. It was lifted off its stone base in 2015 and moved sideways so the wall beneath could be rebuilt, and it is only now being brought back. According to the city, the keep interior is closed until fiscal 2032, and the exterior will be visible only until about autumn 2028, so earlier is better. The park is also one of Japan’s best-known cherry blossom spots. Check the current status before you go.'],
 [('hirosaki-castle','otemon-sakura.jpg','Otemon Gate at Hirosaki Castle through cherry blossoms','The Otemon Gate seen through cherry blossoms, April 2025.'),
  ('hirosaki-castle','keep-temporary.jpg','The Hirosaki Castle keep on its temporary base','The keep waiting on its temporary base in the Honmaru, May 2022.')])
sec+=card('uwajima-castle','Uwajima Castle','宇和島城',
 ['The keep that was remodeled to look peaceful. Nippon.com says it has decorative gables and hanging fish-shaped ornaments on every floor, which are read as symbols of a peaceful age. It is small, about 15.8 meters by Zooming Japan’s figure, on a wooded hill in Ehime. Todo Takatora built the castle, and the Date family later held it.'],
 [('uwajima-castle','hero.jpg','Uwajima Castle keep','The keep, June 2017.'),
  ('uwajima-castle','blossom.jpg','Uwajima Castle keep and cherry blossom','The keep and cherry blossom seen from the main enclosure, March 2008.')])
sec+=card('kochi-castle','Kochi Castle','高知城',
 ['Most castles give you the tower and ask you to imagine the lord’s home. Kochi does not. GLTJP says it is the only castle in Japan where both the original keep and the Honmaru Palace survive, a short walk apart on a hill in the middle of Kochi city. Yamauchi Kazutoyo built it between 1601 and 1611. After a fire in 1727 it was rebuilt.'],
 [('kochi-castle','hero.jpg','Kochi Castle keep above stone walls','The keep above the stone walls, February 2008.'),
  ('kochi-castle','palace-keep.jpg','The keep and the tiled building in front of it at Kochi Castle','The keep and the tiled building in front of it, May 2007.')])
sec+=card('marugame-castle','Marugame Castle','丸亀城',
 ['Look at it from below first. The keep itself is small, about 15 meters by Nippon.com’s figure, but it sits on a stepped stone slope that GLTJP calls Japan’s tallest at 60 meters. Nippon.com and Wikipedia put the single tallest wall at over 20 meters, so read the 60-meter figure as the whole slope. Part of the walls collapsed in the heavy rain of July 2018, and repairs are continuing.'],
 [('marugame-castle','hero.jpg','Marugame Castle keep above its stone wall','The three-story keep above its stone wall.'),
  ('marugame-castle','view.jpg','The view from Marugame Castle','The view from the castle, January 2017.')])
sec+="""
  <p>Four of the twelve are on Shikoku: Matsuyama, Uwajima, Marugame and Kochi. If you are planning a Shikoku trip, you can see them all.</p>

  <h2 id="rebuilt-castles-worth-the-trip">Rebuilt Castles Worth the Trip</h2>
  <p>Several of Japan’s most famous castles are rebuilds. That does not make them less worth visiting, but it changes what to expect inside.</p>
"""
sec+=card('osaka-castle','Osaka Castle','大阪城',
 ['Look at the ground before the tower. The keep on every postcard is a 1931 concrete reconstruction. The stone beneath it is the real thing, much of it laid in the 1620s.'],
 [('osaka-castle','hero.jpg','Osaka Castle keep above its stone walls and moat','The keep above the stone walls, May 2018.')])
sec+=card('nagoya-castle','Nagoya Castle','名古屋城',
 ['You cannot go up the main keep; it has been closed since May 2018, and the golden shachi on its roof are for looking at from the ground. The reason to go is the Honmaru Palace, rebuilt over ten years, whose rooms are at ground level.'],
 [('nagoya-castle','keep-close.jpg','The keep and its two golden shachi at Nagoya Castle','The keep and its two golden shachi up close.')])
sec+=card('hiroshima-castle','Hiroshima Castle','広島城',
 ['Hiroshima Castle is where the city started. Mori Terumoto built it on flat land in the delta of the Ota River, and the town grew around it. The keep was rebuilt in 1958. Most people come to the city for the Peace Memorial Park, and the castle is the quieter part of the same story.'],
 [('hiroshima-castle','autumn-front.jpg','Hiroshima Castle keep from the front in autumn','The keep from the front in autumn, November 2014.')])
sec+=card('okayama-castle','Okayama Castle','岡山城',
 ['Most castles in Japan are white. Okayama’s keep is black, with gold on the roof, and the locals call it the Crow Castle. It is a rebuild, which is worth knowing before you go. Korakuen garden is next door.'],
 [('okayama-castle','hero.jpg','Okayama Castle black keep from the front','The black keep from the front, January 2008.'),
  ('okayama-castle','night.jpg','Okayama Castle keep lit above paper lanterns','The keep lit up above a field of paper lanterns during a summer lighting event.')])
sec+="""
  <h2 id="which-castle-should-you-visit">Which Castle Should You Visit?</h2>
  <ul>
    <li><strong>One famous castle, with the least effort:</strong> Himeji.</li>
    <li><strong>A half day from a big city:</strong> Inuyama from Nagoya, or Hikone from Kyoto (about 50 minutes by train).</li>
    <li><strong>A hike to a keep:</strong> Bitchu Matsuyama, on a mountaintop.</li>
    <li><strong>Walls and history:</strong> Kumamoto (check what is open) and Marugame.</li>
    <li><strong>Cherry blossoms:</strong> Hirosaki, though the keep is in the middle of a long restoration.</li>
    <li><strong>A palace rather than a tower:</strong> Nijo in Kyoto, or Kochi, where the palace also survives.</li>
  </ul>
"""
put('  <h2 id="conclusion-walking-the-shadows-of-the">',sec)
put('      <li><a href="#conclusion-walking-the-shadows-of-the">',
 '      <li><a href="#ten-more-original-keeps">Ten More Original Keeps</a></li>\n      <li><a href="#rebuilt-castles-worth-the-trip">Rebuilt Castles Worth the Trip</a></li>\n      <li><a href="#which-castle-should-you-visit">Which Castle Should You Visit?</a></li>\n')
t=t.replace('"dateModified": "2026-11-03"','"dateModified": "2026-11-05"')
