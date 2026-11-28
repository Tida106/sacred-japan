import re,json,os,glob
from PIL import Image,ImageDraw,ImageFont
R='/home/claude/sacred-japan/'; UP='/mnt/user-data/uploads/'
LIC={'by2':('CC BY 2.0','https://creativecommons.org/licenses/by/2.0/'),
 'by3':('CC BY 3.0','https://creativecommons.org/licenses/by/3.0/'),
 'cc0':('CC0 1.0','https://creativecommons.org/publicdomain/zero/1.0/'),
 'bysa2':('CC BY-SA 2.0','https://creativecommons.org/licenses/by-sa/2.0/'),
 'bysa3':('CC BY-SA 3.0','https://creativecommons.org/licenses/by-sa/3.0/'),
 'bysa4':('CC BY-SA 4.0','https://creativecommons.org/licenses/by-sa/4.0/')}
def esc_json(t):
    t=re.sub('<[^>]+>','',t)
    for a,b in [('&rsquo;','’'),('&ldquo;','"'),('&rdquo;','"'),('&ndash;','-'),('&#333;','ō'),('&amp;','&')]: t=t.replace(a,b)
    return t
def build(c):
    SL=c['slug']; D=R+f'guides/{SL}/'; os.makedirs(D+'images',exist_ok=True)
    P=c['photos']; SIZE={}
    for k,v in P.items():
        im=Image.open(v[0] if v[0].startswith('/') else glob.glob(UP+v[0]+'-image.*')[0]).convert('RGB')
        if im.width>1200: im=im.resize((1200,round(im.height*1200/im.width)),Image.LANCZOS)
        im.save(D+f'images/{k}.jpg',quality=84); im.save(D+f'images/{k}.webp',quality=80); SIZE[k]=im.size
    def fig(k,alt,cap,hero=False):
        u,a,l,cl=P[k]; ln,lu=LIC[l]; w,h=SIZE[k]
        if hero: st='margin:0 0 48px;'; ld='eager'; ims='style="width:100%;max-height:420px;object-fit:cover;border-radius:4px;display:block;"'
        else:
            mw=min(420 if h>w else 760,w); st='margin:28px auto;max-width:%dpx;'%mw; ld='lazy'; ims='style="width:100%;height:auto;border-radius:4px;display:block;"'
        return f'<figure style="{st}"><picture><source srcset="/guides/{SL}/images/{k}.webp" type="image/webp"><img src="/guides/{SL}/images/{k}.jpg" alt="{alt}" width="{w}" height="{h}" loading="{ld}" {ims}></picture><figcaption style="font-size:13px;color:var(--enshu);margin-top:10px;text-align:center;line-height:1.6;">{cap}.<br>Photo: <a href="{cl}" target="_blank" rel="noopener">{a}</a>, <a href="{lu}" target="_blank" rel="noopener">{ln}</a>, via Wikimedia Commons (resized)</figcaption></figure>\n'
    s=open(R+'guides/gifu-castle/index.html',encoding='utf-8').read()
    i=s.index('<main>'); j=s.index('</main>'); head,tail=s[:i],s[j:]
    T,DESC=c['title'],c['desc']
    head=re.sub(r'<title>.*?</title>',f'<title>{T} | Sacred Japan</title>',head,count=1)
    head=re.sub(r'(<meta (?:name="description"|property="og:description"|name="twitter:description") content=")[^"]*(")',lambda m:m.group(1)+DESC+m.group(2),head)
    head=re.sub(r'(<meta (?:property="og:title"|name="twitter:title") content=")[^"]*(")',lambda m:m.group(1)+T+m.group(2),head)
    head=re.sub(r'("headline": ")[^"]*(")',lambda m:m.group(1)+T+m.group(2),head)
    head=re.sub(r'("description": ")A licensed[^"]*(")',lambda m:m.group(1)+DESC+m.group(2),head)
    head=re.sub(r'("date(?:Published|Modified)": ")[^"]*(")',lambda m:m.group(1)+'2026-11-25'+m.group(2),head)
    head=re.sub(r'<meta name="keywords" content="[^"]*">','<meta name="keywords" content="%s">'%c['kw'],head)
    head=head.replace('guides/gifu-castle',f'guides/{SL}').replace('guide_gifu_castle_',f'guide_{c["ev"]}_').replace('og-guides-gifu-castle',f'og-guides-{SL}')
    head=head.replace('岐阜城',c['jp']).replace('Gifu Castle',c['en'])
    head=re.sub(r"<h1>.*?</h1>",c['h1'].replace('\\','\\\\'),head,count=1,flags=re.S)
    head=head.replace("Nobunaga's mountain castle above Gifu, with the keep closed until late 2027.",c['tag'])
    head=head.replace('SACRED JAPAN GUIDES ／ 城','SACRED JAPAN GUIDES ／ 神社')
    faqs=c['faqs']
    fj=',\n'.join('    {\n      "@type": "Question",\n      "name": %s,\n      "acceptedAnswer": {\n        "@type": "Answer",\n        "text": %s\n      }\n    }'%(json.dumps(esc_json(q)),json.dumps(esc_json(a_))) for q,a_ in faqs)
    head=re.sub(r'("mainEntity": \[\n).*?(\n  \]\n\}\n</script>\n\n<!-- ── GOOGLE)',lambda m:m.group(1)+fj+m.group(2),head,flags=re.S)
    hh=re.sub(r'"mainEntity": \[.*','',head,flags=re.S)
    assert not re.search('Gifu|Nobunaga|castle|Castle',re.sub(r'<nav>.*?</nav>','',hh,flags=re.S).replace('Castles','')),re.findall('.{30}(?:Gifu|Nobunaga|astle).{20}',hh)
    IL='class="inline-link"'
    def a(u,t,ev): return f'<a href="{u}" {IL} onclick="trackEvent(\'click\',\'internal\',\'guide_{c["ev"]}_to_{ev}\')">{t}</a>'
    body=c['body'](fig,a)
    faqh=''.join(f'    <details class="faq-item">\n        <summary>{q}</summary>\n        <div class="faq-answer">{a_}</div>\n    </details>\n' for q,a_ in faqs)
    main=body.replace('@@FAQ@@',faqh)
    tail=tail.replace('gifu-castle',SL).replace('gifu_castle',c['ev']).replace('DGifu','D'+c['dest']).replace('search/Gifu','search/'+c['dest'])
    def L(u,l,t): return f'<a href="{u}" target="_blank" rel="noopener" style="color:var(--beni);text-decoration:underline;" onclick="trackEvent(\'click\',\'external\',\'src_{c["ev"]}_{l}\')">{t}</a>'
    src='Sources verified at time of writing: '+', '.join(L(u,l,t) for u,l,t in c['sources'])+'. Hours, prices and availability change'
    tail,n=re.subn(r'Sources verified at time of writing:.*?Hours, prices and availability change',lambda m:src,tail,flags=re.S); assert n==1
    out=head+main+tail
    assert not re.search('Gifu|Nobunaga|Kinka',re.sub(r'"mainEntity": \[.*','',head+tail,flags=re.S))
    open(D+'index.html','w',encoding='utf-8').write(out)
    for tg in ['div','figure','picture','p','a','ul','li','details','section','h2']:
        assert len(re.findall(f'<{tg}[ >]',out))==len(re.findall(f'</{tg}>',out)),tg
    for m_ in re.findall(r'<script type="application/ld\+json">(.*?)</script>',out,re.S): json.loads(m_)
    im=Image.open(R+'images/og/og-guides-matsue-castle.jpg').convert('RGB'); d=ImageDraw.Draw(im)
    d.rectangle([40,150,1170,380],fill=(252,240,242)); d.rectangle([1118,66,1160,96],fill=(252,240,242))
    f1=ImageFont.truetype(glob.glob('/usr/share/fonts/**/DejaVuSerif-Bold.ttf',recursive=True)[0],48)
    f2=ImageFont.truetype(glob.glob('/usr/share/fonts/**/NotoSerifCJK-Bold.ttc',recursive=True)[0],28,index=0)
    l1,l2=c['og']; assert d.textlength(l2,font=f1)<1090 and d.textlength(l1,font=f1)<1090
    d.text((66,170),l1,font=f1,fill=(26,15,15)); d.text((66,238),l2,font=f1,fill=(26,15,15)); d.text((66,332),c['jp'],font=f2,fill=(138,125,120))
    im.save(R+f'images/og/og-guides-{SL}.jpg',quality=88)
    if c.get('thumb'):
     b=Image.open(D+f'images/{c["thumb"]}.jpg'); w,h=b.size; ch=round(w*400/640); t=max(0,(h-ch)//2)
     th=b.crop((0,t,w,t+ch)).resize((640,400),Image.LANCZOS)
     th.save(R+f'images/hub/{SL}.jpg',quality=84); th.save(R+f'images/hub/{SL}.webp',quality=80)
    # PHOTO-CREDITS
    rows=''
    for k,v in P.items():
        ln,lu=LIC[v[2]]
        rows+=f'guides/{SL},/guides/{SL}/images/{k}.jpg,{ln},{lu},{v[3]},"{k}: Photo: {v[1]}, {ln}, via Wikimedia Commons (resized)"\r\n'
    old=open(R+'PHOTO-CREDITS.csv',encoding='utf-8',newline='').read()
    keep=''.join(l for l in old.splitlines(True) if not l.startswith(f'guides/{SL},'))
    open(R+'PHOTO-CREDITS.csv','w',encoding='utf-8',newline='').write(keep+rows)
    print('built',SL,len(out))
