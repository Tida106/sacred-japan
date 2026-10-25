(function(){
  if(window.__secnav)return;window.__secnav=1;
  var mq=window.matchMedia('(max-width:768px)');
  function init(){
    var hs=[].slice.call(document.querySelectorAll('h2')).filter(function(h){
      return !h.closest('footer,nav,aside,.mobile-menu,[class*="related"],[class*="newsletter"],[class*="share"],[class*="amazon"],[class*="cookie"]')&&h.offsetParent!==null;
    });
    if(hs.length<3)return;
    var used={};
    var S=hs.map(function(h,i){
      var c=h.cloneNode(true);[].forEach.call(c.querySelectorAll('span,small,em.jp'),function(n){if(/h2-jp|jp|ja/i.test(n.className))n.remove();});
      var t=(c.textContent||'').replace(/\s+/g,' ').trim().split(/\s[—–-]\s|:|\(/)[0].trim();
      if(!t)t='Section '+(i+1);
      if(!h.id){var b='sn-'+(i+1);h.id=b;}
      return [h.id,t,h];
    });
    var css='.secnav-pill{position:fixed;left:12px;bottom:14px;z-index:900;max-width:calc(100vw - 84px);display:flex;align-items:center;gap:8px;padding:10px 14px;border:1px solid rgba(0,0,0,.12);border-radius:999px;background:rgba(253,240,243,.96);color:#2a2a2a;font:600 13px/1.2 system-ui,-apple-system,sans-serif;box-shadow:0 2px 10px rgba(0,0,0,.15);cursor:pointer;-webkit-backdrop-filter:blur(6px);backdrop-filter:blur(6px)}'+
    '.secnav-pill span{overflow:hidden;text-overflow:ellipsis;white-space:nowrap}.secnav-count{opacity:.55;font-weight:500}'+
    '.secnav-sheet{position:fixed;inset:0;z-index:1000;display:none;background:rgba(0,0,0,.35)}.secnav-sheet.open{display:block}'+
    '.secnav-panel{position:absolute;left:0;right:0;bottom:0;max-height:75vh;overflow-y:auto;background:#fdf0f3;border-radius:16px 16px 0 0;padding:8px 0 20px;font-family:system-ui,-apple-system,sans-serif}'+
    '.secnav-panel h3{margin:0;padding:14px 20px 8px;font-size:12px;letter-spacing:.08em;text-transform:uppercase;opacity:.6;color:#2a2a2a}'+
    '.secnav-panel a{display:flex;gap:12px;align-items:center;padding:13px 20px;color:#2a2a2a;text-decoration:none;font-size:15px;border-top:1px solid rgba(0,0,0,.06)}'+
    '.secnav-panel a b{width:22px;opacity:.45;font-weight:500;font-size:12px}.secnav-panel a.on{background:rgba(180,40,60,.09);font-weight:700}';
    var st=document.createElement('style');st.textContent=css;document.head.appendChild(st);
    var root=document.createElement('div');
    root.innerHTML='<button class="secnav-pill" type="button" aria-haspopup="dialog" aria-label="Jump to section"><span class="sl">Top</span><span class="secnav-count"></span><span aria-hidden="true">▴</span></button><div class="secnav-sheet" role="dialog" aria-label="Page sections"><div class="secnav-panel"></div></div>';
    document.body.appendChild(root);
    var pill=root.querySelector('.secnav-pill'),label=root.querySelector('.sl'),count=root.querySelector('.secnav-count'),sheet=root.querySelector('.secnav-sheet'),panel=root.querySelector('.secnav-panel');
    var cur=-2;
    function esc(s){return s.replace(/[&<>"]/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c];});}
    function render(){var h='<h3>Jump to section</h3>';S.forEach(function(s,i){h+='<a href="#'+s[0]+'"'+(i===cur?' class="on"':'')+'><b>'+(i+1)+'</b>'+esc(s[1])+'</a>';});panel.innerHTML=h;}
    function update(){var y=window.innerHeight*0.35,idx=-1;for(var i=0;i<S.length;i++){if(S[i][2].getBoundingClientRect().top<=y)idx=i;}
      if(idx!==cur){cur=idx;label.textContent=idx<0?'Top':S[idx][1];count.textContent=idx<0?'':(idx+1)+'/'+S.length;render();}}
    function close(){sheet.classList.remove('open');}
    pill.addEventListener('click',function(){render();sheet.classList.add('open');var on=panel.querySelector('.on');if(on)on.scrollIntoView({block:'center'});});
    sheet.addEventListener('click',function(e){if(e.target===sheet)close();});
    panel.addEventListener('click',function(e){var a=e.target.closest('a');if(!a)return;e.preventDefault();close();var el=document.getElementById(a.getAttribute('href').slice(1));if(el)window.scrollTo({top:el.getBoundingClientRect().top+window.pageYOffset-70,behavior:'smooth'});});
    var t;window.addEventListener('scroll',function(){if(t)return;t=setTimeout(function(){t=null;update();},100);},{passive:true});
    function vis(){root.style.display=mq.matches?'':'none';}
    vis();(mq.addEventListener?mq.addEventListener('change',vis):mq.addListener(vis));
    update();
  }
  if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',init);else init();
})();
