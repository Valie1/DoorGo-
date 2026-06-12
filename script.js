
(function(){
  const btn = document.querySelector('.menu-toggle');
  const nav = document.querySelector('.nav');

  function setMenu(open){
    if(!nav || !btn) return;
    nav.classList.toggle('open', open);
    document.body.classList.toggle('menu-open', open);
    btn.setAttribute('aria-expanded', open ? 'true' : 'false');
  }

  if(btn && nav){
    btn.addEventListener('click', (e)=>{
      e.stopPropagation();
      setMenu(!nav.classList.contains('open'));
    });

    nav.querySelectorAll('a').forEach(a=>{
      a.addEventListener('click', ()=>setMenu(false));
    });

    document.addEventListener('click', (e)=>{
      if(document.body.classList.contains('menu-open') && !nav.contains(e.target) && !btn.contains(e.target)){
        setMenu(false);
      }
    });

    window.addEventListener('resize', ()=>{
      if(window.innerWidth > 760) setMenu(false);
    });
  }

  const revealEls=[...document.querySelectorAll('.reveal,.service-card,.info-box,.feature,.contact-card,.video-card,.lead-card,.operator-box,.map-panel,.contact-hero-card,.faq,.price-box')];
  revealEls.forEach((el,i)=>{
    el.classList.add('reveal');
    el.style.setProperty('--reveal-delay', `${Math.min(i*35, 240)}ms`);
  });

  const io=new IntersectionObserver((entries)=>{
    entries.forEach(e=>{
      if(e.isIntersecting){
        e.target.classList.add('in-view');
        io.unobserve(e.target);
      }
    });
  },{threshold:.10, rootMargin:'0px 0px -40px 0px'});
  revealEls.forEach(el=>io.observe(el));

  document.querySelectorAll('.nav a').forEach(a=>{
    if(a.getAttribute('href')===location.pathname.split('/').pop()) a.classList.add('active');
  });

  // Mobile quick action bar removed in v11.

})();



// DoorGO v13 gallery lightbox with enter + leave animation
(function(){
  const cards=[...document.querySelectorAll('.real-gallery-card')];
  if(!cards.length) return;
  const box=document.createElement('div');
  box.className='gallery-lightbox';
  box.innerHTML='<button type="button" aria-label="close">×</button><img alt="DoorGO gallery preview">';
  document.body.appendChild(box);
  const img=box.querySelector('img');
  let closingTimer=null;
  const open=(src)=>{
    clearTimeout(closingTimer);
    img.src=src;
    box.classList.remove('closing');
    requestAnimationFrame(()=>box.classList.add('open'));
  };
  const close=()=>{
    if(!box.classList.contains('open')) return;
    box.classList.add('closing');
    box.classList.remove('open');
    closingTimer=setTimeout(()=>{ box.classList.remove('closing'); img.removeAttribute('src'); }, 360);
  };
  box.querySelector('button').addEventListener('click',close);
  box.addEventListener('click',e=>{ if(e.target===box) close(); });
  document.addEventListener('keydown',e=>{ if(e.key==='Escape') close(); });
  cards.forEach(card=>{
    card.setAttribute('tabindex','0');
    const go=()=>open(card.dataset.full || card.querySelector('img').src);
    card.addEventListener('click',go);
    card.addEventListener('keydown',e=>{ if(e.key==='Enter' || e.key===' '){ e.preventDefault(); go(); }});
  });
})();

// DoorGO v10 wider motion pass
(function(){
  const animated = [
    ...document.querySelectorAll('main section, main h1, main h2, main h3, main p, main img, .footer a, .footer p, .footer h3, .footer-logo, .nav a, .brand')
  ];
  animated.forEach((el,i)=>{
    if(!el.classList.contains('reveal')) el.classList.add('reveal');
    if(!el.style.getPropertyValue('--reveal-delay')) el.style.setProperty('--reveal-delay', `${Math.min((i%10)*45, 360)}ms`);
  });
  const io2 = new IntersectionObserver((entries)=>{
    entries.forEach(e=>{ if(e.isIntersecting){ e.target.classList.add('in-view'); io2.unobserve(e.target); }});
  },{threshold:.08,rootMargin:'0px 0px -24px 0px'});
  animated.forEach(el=>{ if(!el.classList.contains('in-view')) io2.observe(el); });
})();


// DoorGO v14: extra motion, particles, ripple, parallax and better interactive feel
(function(){
  document.body.classList.add('dg-v14');
  requestAnimationFrame(()=>document.body.classList.add('page-ready'));

  // scroll progress
  const progress=document.createElement('div');
  progress.className='scroll-progress';
  document.body.appendChild(progress);
  const updateProgress=()=>{
    const max=document.documentElement.scrollHeight-window.innerHeight;
    progress.style.width=(max>0?Math.min(100,(window.scrollY/max)*100):0)+'%';
  };
  updateProgress();
  window.addEventListener('scroll',updateProgress,{passive:true});

  // banner floating particles
  document.querySelectorAll('.dg-clean-banner').forEach((banner)=>{
    for(let i=0;i<18;i++){
      const p=document.createElement('span');
      p.className='dg-banner-particle';
      p.style.left=(5+Math.random()*90)+'%';
      p.style.top=(30+Math.random()*60)+'%';
      p.style.animationDelay=(-Math.random()*6).toFixed(2)+'s';
      p.style.animationDuration=(4.5+Math.random()*4).toFixed(2)+'s';
      banner.appendChild(p);
    }
  });

  // ripple for all important click targets
  document.querySelectorAll('.btn,.menu-toggle,.socials a,.footer-socials a,.phone-float,.card-link,.mini-cta').forEach(el=>{
    el.addEventListener('pointerdown',e=>{
      const r=el.getBoundingClientRect();
      const dot=document.createElement('span');
      dot.className='ripple-dot';
      dot.style.left=(e.clientX-r.left)+'px';
      dot.style.top=(e.clientY-r.top)+'px';
      dot.style.width=dot.style.height=Math.max(r.width,r.height)/5+'px';
      el.appendChild(dot);
      setTimeout(()=>dot.remove(),700);
    });
  });


  // stagger children inside sections after reveal
  const sectionObserver=new IntersectionObserver(entries=>{
    entries.forEach(entry=>{
      if(!entry.isIntersecting) return;
      const children=[...entry.target.querySelectorAll('.service-card,.feature,.info-box,.contact-card,.real-gallery-card,.trust,.video-card,.video-placeholder')];
      children.forEach((child,i)=>{
        child.style.animationDelay=`${Math.min(i*70,420)}ms`;
        child.classList.add('dg-staggered');
      });
      sectionObserver.unobserve(entry.target);
    });
  },{threshold:.12});
  document.querySelectorAll('section,.content,.footer').forEach(s=>sectionObserver.observe(s));
})();


// DoorGO v18 alive micro interactions: no text tooltips, just smooth pop/ripple motion
(function(){
  document.querySelectorAll('[title]').forEach(el=>el.removeAttribute('title'));
  const popTargets = document.querySelectorAll('a,button,.service-card,.hero-tile,.contact-card,.info-box,.feature,.trust,.real-gallery-card,.video-placeholder,.video-card,.lead-card,.operator-box,.map-box,.map-panel,details,summary');
  popTargets.forEach(el=>{
    el.classList.add('ripple-pop');
    el.addEventListener('pointerenter',()=>el.classList.add('is-hovered'),{passive:true});
    el.addEventListener('pointerleave',()=>el.classList.remove('is-hovered'),{passive:true});
    el.addEventListener('pointerdown',(e)=>{
      const r=document.createElement('span');
      r.className='dg-ripple';
      const rect=el.getBoundingClientRect();
      r.style.left=(e.clientX-rect.left)+'px';
      r.style.top=(e.clientY-rect.top)+'px';
      el.appendChild(r);
      setTimeout(()=>r.remove(),700);
    },{passive:true});
  });
})();


/* DoorGO v20 — mouse glow only, no zoom pop */
(function(){
  const cards = document.querySelectorAll('.service-card,.contact-card,.feature,.info-box,.lead-card,.price-box,.faq,.video-card,.real-gallery-card,.gallery-card,.portfolio-card,.hero-tile,.operator-box,.map-panel');
  cards.forEach((el)=>{
    el.addEventListener('pointermove', (e)=>{
      const r = el.getBoundingClientRect();
      el.style.setProperty('--mx', (((e.clientX-r.left)/r.width)*100).toFixed(2)+'%');
      el.style.setProperty('--my', (((e.clientY-r.top)/r.height)*100).toFixed(2)+'%');
    }, {passive:true});
  });
})();


/* DoorGO v21 — electric video + clean glow position */
(function(){
  const glowTargets = document.querySelectorAll('.electric-video-card,.electric-lock-info');
  glowTargets.forEach((el)=>{
    el.addEventListener('pointermove', (e)=>{
      const r = el.getBoundingClientRect();
      el.style.setProperty('--mx', (((e.clientX-r.left)/r.width)*100).toFixed(2)+'%');
      el.style.setProperty('--my', (((e.clientY-r.top)/r.height)*100).toFixed(2)+'%');
    }, {passive:true});
  });
})();


/* DoorGO v23 mobile cleanup */
(function(){
  const btn = document.querySelector('.menu-toggle');
  const nav = document.querySelector('.nav');
  if(btn && nav){
    btn.addEventListener('click', function(){
      setTimeout(()=>btn.classList.toggle('active', nav.classList.contains('open')), 0);
    });
    document.addEventListener('click', function(e){
      if(!nav.contains(e.target) && !btn.contains(e.target)){
        btn.classList.remove('active');
      }
    });
  }

  document.querySelectorAll('.faq').forEach((faq)=>{
    const h = faq.querySelector('h3');
    const p = faq.querySelector('p');
    const ht = h ? h.textContent.replace('+','').trim() : '';
    const pt = p ? p.textContent.trim() : '';
    if(ht === 'არის?' || (!pt && ht.length < 10)){
      faq.classList.add('dg-empty-faq');
    }
  });
})();


/* DoorGO v24 — reliable mobile menu state */
(function(){
  const btn = document.querySelector('.menu-toggle');
  const nav = document.querySelector('.nav');
  if(!btn || !nav) return;

  const sync = () => btn.classList.toggle('active', nav.classList.contains('open'));

  btn.addEventListener('click', () => setTimeout(sync, 10));

  nav.querySelectorAll('a').forEach(a => {
    a.addEventListener('click', () => {
      nav.classList.remove('open');
      sync();
    });
  });

  document.addEventListener('click', (e) => {
    if(!nav.contains(e.target) && !btn.contains(e.target)){
      nav.classList.remove('open');
      sync();
    }
  });

  window.addEventListener('resize', () => {
    if(window.innerWidth > 820){
      nav.classList.remove('open');
      sync();
    }
  });
})();


/* DoorGO v25 — iOS mobile app shell */
(function(){
  const btn = document.querySelector('.menu-toggle');
  const nav = document.querySelector('.nav');
  if(btn && nav){
    const sync = () => btn.classList.toggle('active', nav.classList.contains('open'));
    btn.addEventListener('click', () => setTimeout(sync, 10));
    nav.querySelectorAll('a').forEach(a => a.addEventListener('click', () => {
      nav.classList.remove('open');
      sync();
    }));
    document.addEventListener('click', (e)=>{
      if(!nav.contains(e.target) && !btn.contains(e.target)){
        nav.classList.remove('open');
        sync();
      }
    });
  }
})();


/* DoorGO v26 — smoother mobile open/close state */
(function(){
  const btn = document.querySelector('.menu-toggle');
  const nav = document.querySelector('.nav');
  if(!btn || !nav) return;
  const sync = () => {
    btn.classList.toggle('active', nav.classList.contains('open'));
    document.body.classList.toggle('mobile-menu-open', nav.classList.contains('open'));
  };
  btn.addEventListener('click', () => setTimeout(sync, 10));
  nav.querySelectorAll('a').forEach(a => a.addEventListener('click', () => {
    nav.classList.remove('open');
    sync();
  }));
  document.addEventListener('click', (e)=>{
    if(!nav.contains(e.target) && !btn.contains(e.target)){
      nav.classList.remove('open');
      sync();
    }
  });
})();


/* DoorGO v27 — keep socials visible and sync clean menu button */
(function(){
  const btn = document.querySelector('.menu-toggle');
  const nav = document.querySelector('.nav');
  if(!btn || !nav) return;

  const sync = () => {
    const isOpen = nav.classList.contains('open');
    btn.classList.toggle('active', isOpen);
    document.body.classList.toggle('mobile-menu-open', isOpen);
  };

  btn.addEventListener('click', () => setTimeout(sync, 10));

  nav.querySelectorAll('a').forEach(a => a.addEventListener('click', () => {
    nav.classList.remove('open');
    sync();
  }));

  document.addEventListener('click', (e)=>{
    if(!nav.contains(e.target) && !btn.contains(e.target)){
      nav.classList.remove('open');
      sync();
    }
  });

  sync();
})();


/* DoorGO v29 — compact mobile header state */
(function(){
  const btn = document.querySelector('.menu-toggle');
  const nav = document.querySelector('.nav');
  if(!btn || !nav) return;

  const sync = () => {
    const open = nav.classList.contains('open');
    btn.classList.toggle('active', open);
    document.body.classList.toggle('mobile-menu-open', open);
  };

  btn.addEventListener('click', () => setTimeout(sync, 10));

  nav.querySelectorAll('a').forEach(a => a.addEventListener('click', () => {
    nav.classList.remove('open');
    sync();
  }));

  document.addEventListener('click', (e) => {
    if(!nav.contains(e.target) && !btn.contains(e.target)){
      nav.classList.remove('open');
      sync();
    }
  });

  window.addEventListener('resize', sync);
  sync();
})();


/* DoorGO v33 — Fabri/Cut&Hire inspired custom video player */
(function(){
  if(window.__doorGoV33VideoPlayer) return;
  window.__doorGoV33VideoPlayer = true;

  const cardPlayers = [...document.querySelectorAll('.dg-video-card .custom-player')];
  if(!cardPlayers.length) return;

  const fineHover = window.matchMedia && window.matchMedia('(hover:hover) and (pointer:fine)').matches;

  function formatTime(seconds){
    if(!Number.isFinite(seconds) || seconds < 0) return '0:00';
    const m = Math.floor(seconds / 60);
    const s = Math.floor(seconds % 60).toString().padStart(2,'0');
    return `${m}:${s}`;
  }

  function setRangeValue(input, value){
    if(!input) return;
    input.style.setProperty('--value', `${value}%`);
  }

  function updateInline(pl){
    const v = pl.querySelector('video:not(.card-hover-preview)');
    const progress = pl.querySelector('.progress');
    const time = pl.querySelector('.player-time');
    const play = pl.querySelector('.play-toggle');
    const mute = pl.querySelector('.mute-toggle');
    const vol = pl.querySelector('.volume');
    if(!v) return;
    const pct = v.duration ? (v.currentTime / v.duration) * 100 : 0;
    if(progress){ progress.value = pct; setRangeValue(progress, pct); }
    if(time) time.textContent = `${formatTime(v.currentTime)} / ${formatTime(v.duration)}`;
    if(play) play.textContent = v.paused ? '▶' : '❚❚';
    if(mute) mute.textContent = v.muted || v.volume === 0 ? '🔇' : '🔊';
    if(vol){ vol.value = v.muted ? 0 : v.volume; setRangeValue(vol, (v.muted ? 0 : v.volume) * 100); }
    pl.classList.toggle('playing', !v.paused);
    pl.classList.toggle('paused', v.paused && v.currentTime > 0);
  }

  function showPoster(pl){
    const poster = pl.querySelector('.forced-video-poster');
    if(poster){
      poster.style.display = 'block';
      poster.style.opacity = '1';
      poster.style.visibility = 'visible';
    }
    pl.classList.remove('playing','paused','previewing','video-warming');
  }

  function hidePoster(pl){
    const poster = pl.querySelector('.forced-video-poster');
    if(poster){
      poster.style.opacity = '0';
      poster.style.visibility = 'hidden';
    }
  }

  function warmVideo(v, pl){
    if(!v || v.dataset.warmed) return;
    pl?.classList.add('video-warming');
    v.preload = 'auto';
    v.load?.();
    v.dataset.warmed = '1';
    setTimeout(()=>pl?.classList.remove('video-warming'), 900);
  }

  function stopPreview(pl, reset=true){
    const v = pl.querySelector('video:not(.card-hover-preview)');
    if(!v) return;
    v.pause();
    if(reset) {
      try{ v.currentTime = 0; }catch(_){}
    }
    v.muted = true;
    showPoster(pl);
    updateInline(pl);
  }

  function startPreview(pl){
    const v = pl.querySelector('video:not(.card-hover-preview)');
    if(!v) return;
    warmVideo(v, pl);
    v.muted = true;
    v.volume = 0;
    try{
      if(!v.currentTime || v.currentTime < .05) v.currentTime = Math.min(.15, v.duration || .15);
    }catch(_){}
    const promise = v.play();
    if(promise && promise.catch) promise.catch(()=>{});
    pl.classList.add('previewing');
    hidePoster(pl);
    updateInline(pl);
  }

  function ensureModal(){
    let modal = document.querySelector('.dg-player-modal');
    if(modal) return modal;

    modal = document.createElement('div');
    modal.className = 'dg-player-modal';
    modal.innerHTML = `
      <button class="dg-player-close" type="button" aria-label="ვიდეოს დახურვა">×</button>
      <div class="dg-player-shell portrait">
        <div class="custom-player dg-modal-player">
          <video playsinline webkit-playsinline preload="metadata"></video>
          <div class="dg-player-titlebar"><b></b><span></span></div>
          <div class="player-overlay">
            <div class="progress-wrap"><input class="progress" type="range" min="0" max="100" value="0"></div>
            <div class="player-controls">
              <div class="player-left"><button class="player-btn play-toggle" type="button">▶</button><button class="player-btn mute-toggle" type="button">🔊</button><span class="player-time">0:00 / 0:00</span></div>
              <div class="player-right"><input class="volume" type="range" min="0" max="1" step="0.05" value="1"><button class="player-btn fullscreen-toggle" type="button">⛶</button></div>
            </div>
          </div>
        </div>
      </div>`;
    document.body.appendChild(modal);

    const closeBtn = modal.querySelector('.dg-player-close');
    const shell = modal.querySelector('.dg-player-shell');
    const player = modal.querySelector('.dg-modal-player');
    const video = player.querySelector('video');
    const progress = player.querySelector('.progress');
    const playBtn = player.querySelector('.play-toggle');
    const muteBtn = player.querySelector('.mute-toggle');
    const vol = player.querySelector('.volume');
    const fsBtn = player.querySelector('.fullscreen-toggle');
    let uiTimer = null;

    function update(){
      const pct = video.duration ? (video.currentTime / video.duration) * 100 : 0;
      progress.value = pct;
      setRangeValue(progress, pct);
      player.querySelector('.player-time').textContent = `${formatTime(video.currentTime)} / ${formatTime(video.duration)}`;
      playBtn.textContent = video.paused ? '▶' : '❚❚';
      muteBtn.textContent = video.muted || video.volume === 0 ? '🔇' : '🔊';
      vol.value = video.muted ? 0 : video.volume;
      setRangeValue(vol, (video.muted ? 0 : video.volume) * 100);
      player.classList.toggle('playing', !video.paused);
      player.classList.toggle('paused', video.paused);
    }

    function showUI(){
      player.classList.add('show-ui');
      clearTimeout(uiTimer);
      if(!video.paused){
        uiTimer = setTimeout(()=>player.classList.remove('show-ui'), 1600);
      }
    }

    function close(){
      modal.classList.remove('open');
      document.body.classList.remove('locked-player-open');
      video.pause();
      setTimeout(()=>{
        if(!modal.classList.contains('open')){
          video.removeAttribute('src');
          video.load();
          player.classList.remove('playing','paused','show-ui');
        }
      }, 220);
    }

    closeBtn.addEventListener('click', (e)=>{ e.preventDefault(); close(); });
    modal.addEventListener('click', (e)=>{ if(e.target === modal) close(); });
    shell.addEventListener('click', (e)=>e.stopPropagation());
    video.addEventListener('click', ()=>{ video.paused ? video.play().catch(()=>{}) : video.pause(); showUI(); update(); });
    playBtn.addEventListener('click', (e)=>{ e.stopPropagation(); video.paused ? video.play().catch(()=>{}) : video.pause(); showUI(); update(); });
    muteBtn.addEventListener('click', (e)=>{ e.stopPropagation(); video.muted = !video.muted; showUI(); update(); });
    vol.addEventListener('input', ()=>{ video.volume = +vol.value; video.muted = video.volume === 0; showUI(); update(); });
    progress.addEventListener('input', ()=>{ if(video.duration) video.currentTime = (+progress.value / 100) * video.duration; showUI(); update(); });
    fsBtn.addEventListener('click', (e)=>{
      e.stopPropagation();
      showUI();
      if(document.fullscreenElement) document.exitFullscreen().catch(()=>{});
      else player.requestFullscreen?.().catch(()=>{});
    });

    ['loadedmetadata','loadeddata','canplay','timeupdate','volumechange','play','pause'].forEach(ev=>video.addEventListener(ev, ()=>{ update(); showUI(); }));
    player.addEventListener('mousemove', showUI);
    player.addEventListener('mouseenter', showUI);
    window.addEventListener('keydown', (e)=>{ if(e.key === 'Escape' && modal.classList.contains('open')) close(); });

    modal.openFromCard = function(card){
      const source = card.querySelector('video:not(.card-hover-preview)');
      if(!source) return;
      cardPlayers.forEach(stopPreview);
      const src = source.getAttribute('src') || source.currentSrc;
      const poster = source.dataset.forcePoster || source.getAttribute('poster') || '';
      const title = card.dataset.videoTitle || card.querySelector('.dg-video-meta b')?.textContent || 'DoorGO ვიდეო';
      const subtitle = card.dataset.videoSubtitle || card.querySelector('.dg-video-meta span')?.textContent || '';
      player.querySelector('.dg-player-titlebar b').textContent = title;
      player.querySelector('.dg-player-titlebar span').textContent = subtitle;
      video.setAttribute('src', src);
      if(poster) video.setAttribute('poster', poster);
      video.muted = false;
      video.volume = 1;
      vol.value = 1;
      shell.classList.add('portrait');
      shell.classList.remove('landscape');
      modal.classList.add('open');
      document.body.classList.add('locked-player-open');
      showUI();
      video.load();
      const start = ()=>{
        try{ video.currentTime = 0; }catch(_){}
        const playPromise = video.play();
        if(playPromise && playPromise.catch) playPromise.catch(()=>{ player.classList.add('paused'); showUI(); });
        update();
        showUI();
      };
      if(video.readyState >= 2) start();
      else video.addEventListener('canplay', start, {once:true});
    };

    return modal;
  }

  const modal = ensureModal();

  cardPlayers.forEach((pl)=>{
    const card = pl.closest('.dg-video-card');
    const v = pl.querySelector('video:not(.card-hover-preview)');
    if(!card || !v) return;

    v.muted = true;
    v.playsInline = true;

    ['loadedmetadata','timeupdate','volumechange','play','pause'].forEach(ev=>v.addEventListener(ev, ()=>updateInline(pl)));

    pl.querySelectorAll('.player-btn, .progress, .volume').forEach(control=>{
      control.addEventListener('click', (e)=>{ e.preventDefault(); e.stopPropagation(); modal.openFromCard(card); }, true);
      control.addEventListener('pointerup', (e)=>{ e.preventDefault(); e.stopPropagation(); modal.openFromCard(card); }, true);
    });

    if(fineHover){
      pl.addEventListener('pointerenter', ()=>startPreview(pl), {passive:true});
      pl.addEventListener('pointerleave', ()=>stopPreview(pl, true), {passive:true});
      card.addEventListener('pointerenter', ()=>warmVideo(v, pl), {passive:true});
    } else {
      pl.addEventListener('touchstart', ()=>warmVideo(v, pl), {passive:true});
    }

    card.addEventListener('click', (e)=>{
      e.preventDefault();
      e.stopPropagation();
      modal.openFromCard(card);
    }, true);

    updateInline(pl);
  });

  if('IntersectionObserver' in window){
    const io = new IntersectionObserver(entries=>{
      entries.forEach(entry=>{
        if(entry.isIntersecting){
          const pl = entry.target;
          const v = pl.querySelector('video:not(.card-hover-preview)');
          warmVideo(v, pl);
          io.unobserve(pl);
        }
      });
    }, {rootMargin:'550px 0px', threshold:.01});
    cardPlayers.forEach(pl=>io.observe(pl));
  }

  window.addEventListener('load', ()=>{
    document.querySelectorAll('.dg-video-card .forced-video-poster').forEach(img=>{
      if(img.decode) img.decode().catch(()=>{});
    });
  }, {once:true});
})();


/* DoorGO v35 — fullscreen animation helper */
(function(){
  if(window.__doorGoV35FullscreenPolish) return;
  window.__doorGoV35FullscreenPolish = true;

  document.addEventListener('click', (e)=>{
    const btn = e.target.closest('.dg-player-modal .fullscreen-toggle');
    if(!btn) return;
    const player = btn.closest('.dg-modal-player');
    if(!player) return;
    player.classList.remove('fullscreen-start');
    void player.offsetWidth;
    player.classList.add('fullscreen-start');
    setTimeout(()=>player.classList.remove('fullscreen-start'), 520);
  }, true);

  document.addEventListener('fullscreenchange', ()=>{
    const player = document.querySelector('.dg-modal-player');
    if(player && document.fullscreenElement === player){
      player.classList.add('fullscreen-start');
      setTimeout(()=>player.classList.remove('fullscreen-start'), 520);
    }
  });
})();




/* DoorGO v37 — REAL native fullscreen button */
(function(){
  if(window.__doorGoV37RealFullscreen) return;
  window.__doorGoV37RealFullscreen = true;

  const isFs = () => document.fullscreenElement || document.webkitFullscreenElement;

  function getPlayer(btn){
    return btn.closest('.dg-modal-player') || btn.closest('.custom-player');
  }

  function setFsButton(player){
    const btn = player?.querySelector('.fullscreen-toggle');
    if(!btn) return;
    const fullscreenNow = isFs() === player;
    btn.textContent = fullscreenNow ? '⤢' : '⛶';
    player.classList.toggle('real-fullscreen-active', fullscreenNow);
  }

  document.addEventListener('click', function(e){
    const btn = e.target.closest('.dg-player-modal .fullscreen-toggle');
    if(!btn) return;

    e.preventDefault();
    e.stopPropagation();
    e.stopImmediatePropagation();

    const player = getPlayer(btn);
    if(!player) return;

    player.classList.remove('fullscreen-start');
    void player.offsetWidth;
    player.classList.add('fullscreen-start');

    const current = isFs();
    if(current){
      (document.exitFullscreen?.() || document.webkitExitFullscreen?.call(document) || Promise.resolve())
        .catch(()=>{})
        .finally(()=>setTimeout(()=>setFsButton(player), 80));
    } else {
      const request = player.requestFullscreen || player.webkitRequestFullscreen || player.msRequestFullscreen;
      if(request){
        request.call(player).then?.(()=>{}).catch?.(()=>{});
      }
      setTimeout(()=>setFsButton(player), 120);
    }

    setTimeout(()=>player.classList.remove('fullscreen-start'), 520);
  }, true);

  document.addEventListener('fullscreenchange', function(){
    document.querySelectorAll('.dg-modal-player').forEach(setFsButton);
  });

  document.addEventListener('webkitfullscreenchange', function(){
    document.querySelectorAll('.dg-modal-player').forEach(setFsButton);
  });

  document.addEventListener('keydown', function(e){
    if(e.key === 'f' || e.key === 'F'){
      const modal = document.querySelector('.dg-player-modal.open');
      const btn = modal?.querySelector('.fullscreen-toggle');
      if(btn){
        e.preventDefault();
        btn.click();
      }
    }
  });
})();


/* DoorGO v44 — Cut & Hire style service windows loop */
(function(){
  if(window.__doorGoV44ServiceLoop) return;
  window.__doorGoV44ServiceLoop = true;

  function prepareLoop(track){
    if(!track || track.dataset.dgLoopReady === '1') return;

    const originalCards = Array.from(track.children).filter(el => el.classList && el.classList.contains('service-card') && !el.classList.contains('dg-loop-clone'));
    if(originalCards.length < 2) return;

    track.classList.add('dg-service-loop');

    // Clone enough cards so 3 original cards can loop like a 4-window Cut & Hire marquee.
    for(let round = 0; round < 2; round++){
      originalCards.forEach(card => {
        const clone = card.cloneNode(true);
        clone.classList.add('dg-loop-clone');
        clone.setAttribute('aria-hidden', 'true');
        track.appendChild(clone);
      });
    }

    track.dataset.dgLoopReady = '1';

    const setDistance = () => {
      const cards = Array.from(track.children).filter(el => el.classList && el.classList.contains('service-card'));
      const firstClone = cards.find(el => el.classList.contains('dg-loop-clone'));
      if(!firstClone || !cards[0]) return;

      const distance = Math.max(1, firstClone.offsetLeft - cards[0].offsetLeft);
      track.style.setProperty('--dg-loop-distance', distance + 'px');

      // Duration adjusts to distance, so desktop/mobile feel smooth instead of too fast.
      const duration = Math.max(24, Math.min(44, distance / 34));
      track.style.animationDuration = duration + 's';
    };

    requestAnimationFrame(setDistance);
    window.addEventListener('load', setDistance, {once:true});
    window.addEventListener('resize', setDistance);
  }

  function init(){
    document.querySelectorAll('.related-track, .services-strip .service-grid').forEach(prepareLoop);
  }

  if(document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
  else init();
})();


/* DoorGO v45 — fix moving service card images + hover pause zone */
(function(){
  if(window.__doorGoV45ServiceWindowFix) return;
  window.__doorGoV45ServiceWindowFix = true;

  function normalizeCardImages(track){
    if(!track) return;

    const imgs = track.querySelectorAll('.card-img img');
    imgs.forEach(img => {
      const src = img.getAttribute('src');
      const wrap = img.closest('.card-img');

      // Lazy images inside transformed marquee clones can stay blank in Chrome.
      img.loading = 'eager';
      img.decoding = 'async';
      img.fetchPriority = 'high';
      img.removeAttribute('loading');

      if(wrap && src){
        wrap.classList.add('has-bg');
        wrap.style.setProperty('--dg-card-bg', 'url("' + src.replace(/"/g, '\\"') + '")');
      }

      // Force decode/load for clones too.
      if(src && !img.complete){
        const preload = new Image();
        preload.src = src;
      }
    });
  }

  function fixLoop(track){
    if(!track) return;
    normalizeCardImages(track);

    // Recalculate loop distance after images/card layout are ready.
    const cards = Array.from(track.children).filter(el => el.classList && el.classList.contains('service-card'));
    const firstClone = cards.find(el => el.classList.contains('dg-loop-clone'));
    if(firstClone && cards[0]){
      const distance = Math.max(1, firstClone.offsetLeft - cards[0].offsetLeft);
      track.style.setProperty('--dg-loop-distance', distance + 'px');
      const duration = Math.max(26, Math.min(46, distance / 32));
      track.style.animationDuration = duration + 's';
    }
  }

  function init(){
    document.querySelectorAll('.related-track, .services-strip .service-grid.dg-service-loop, .services-strip .service-grid').forEach(track => {
      fixLoop(track);
      setTimeout(() => fixLoop(track), 250);
      setTimeout(() => fixLoop(track), 900);
    });
  }

  if(document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
  else init();

  window.addEventListener('load', init);
  window.addEventListener('resize', () => {
    clearTimeout(window.__dgV45ResizeTimer);
    window.__dgV45ResizeTimer = setTimeout(init, 120);
  });
})();


/* DoorGO v46 — remove reveal blur from service-loop clones + reliable pause only on card */
(function(){
  if(window.__doorGoV46ServiceLoopClarity) return;
  window.__doorGoV46ServiceLoopClarity = true;

  function cleanTrack(track){
    if(!track) return;

    track.querySelectorAll('.service-card').forEach(card => {
      card.classList.add('in-view');
      card.style.opacity = '1';
      card.style.filter = 'none';
      card.style.visibility = 'visible';

      card.querySelectorAll('img').forEach(img => {
        img.loading = 'eager';
        img.removeAttribute('loading');
        img.style.opacity = '1';
        img.style.visibility = 'visible';
        img.style.filter = 'none';
        if(img.src){
          const wrap = img.closest('.card-img');
          if(wrap){
            wrap.classList.add('has-bg');
            wrap.style.setProperty('--dg-card-bg', 'url("' + img.getAttribute('src') + '")');
          }
        }
      });
    });
  }

  function setupPause(section, track){
    if(!section || !track || section.dataset.dgV46PauseReady === '1') return;
    section.dataset.dgV46PauseReady = '1';

    section.querySelectorAll('.service-card').forEach(card => {
      card.addEventListener('mouseenter', () => section.classList.add('paused-on-card'));
      card.addEventListener('mouseleave', () => section.classList.remove('paused-on-card'));
      card.addEventListener('focusin', () => section.classList.add('paused-on-card'));
      card.addEventListener('focusout', () => section.classList.remove('paused-on-card'));
      card.addEventListener('touchstart', () => {
        section.classList.add('paused-on-card');
        clearTimeout(section.__dgPauseTimer);
        section.__dgPauseTimer = setTimeout(() => section.classList.remove('paused-on-card'), 1700);
      }, {passive:true});
    });

    // Important: leaving the cards/section resumes the loop.
    section.addEventListener('mouseleave', () => section.classList.remove('paused-on-card'));
  }

  function init(){
    document.querySelectorAll('.related-track, .services-strip .service-grid.dg-service-loop, .services-strip .service-grid').forEach(track => {
      cleanTrack(track);
      const section = track.closest('.related, .services-strip');
      setupPause(section, track);
    });
  }

  if(document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
  else init();

  window.addEventListener('load', () => {
    init();
    setTimeout(init, 300);
    setTimeout(init, 1000);
  });
})();


/* DoorGO v53 — mobile service showcase tab switcher */
(function(){
  if(window.__doorGoV53MobileSwitcher) return;
  window.__doorGoV53MobileSwitcher = true;
  function init(){
    document.querySelectorAll('.mobile-service-switcher').forEach(function(box){
      if(box.dataset.dgV53Ready === '1') return;
      box.dataset.dgV53Ready = '1';
      var tabs = Array.from(box.querySelectorAll('[data-service-tab]'));
      var panels = Array.from(box.querySelectorAll('[data-service-panel]'));
      function activate(name){
        tabs.forEach(function(btn){
          var on = btn.getAttribute('data-service-tab') === name;
          btn.classList.toggle('is-active', on);
          btn.setAttribute('aria-selected', on ? 'true' : 'false');
        });
        panels.forEach(function(panel){
          panel.classList.toggle('is-active', panel.getAttribute('data-service-panel') === name);
        });
      }
      tabs.forEach(function(btn){
        btn.addEventListener('click', function(){ activate(btn.getAttribute('data-service-tab')); });
      });
      var activeBtn = box.querySelector('[data-service-tab].is-active') || tabs[0];
      if(activeBtn) activate(activeBtn.getAttribute('data-service-tab'));
    });
  }
  if(document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
  else init();
  window.addEventListener('load', init);
})();
