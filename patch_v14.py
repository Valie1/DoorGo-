from pathlib import Path
root=Path(__file__).resolve().parent
css=root/'style.css'
js=root/'script.js'
css_add=r'''

/* =========================================================
   DoorGO v14 EXTRA MOTION + PREMIUM POLISH PASS
   More motion everywhere, cleaner banner, better mobile feel.
   ========================================================= */
:root{
  --ease-out: cubic-bezier(.16,1,.3,1);
  --ease-bounce: cubic-bezier(.2,1.35,.3,1);
  --deep-shadow: 0 36px 110px rgba(3,24,43,.18);
  --cyan-glow: 0 0 0 1px rgba(25,214,255,.24), 0 28px 90px rgba(25,214,255,.18);
}

html{scroll-behavior:smooth;}
body.dg-v13{
  background:
    radial-gradient(circle at 8% 8%,rgba(25,214,255,.13),transparent 26%),
    radial-gradient(circle at 92% 5%,rgba(8,121,242,.10),transparent 30%),
    linear-gradient(180deg,#f7fdff 0%,#fff 42%,#effbff 100%)!important;
}
body.dg-v13:before{
  content:"";
  position:fixed;
  inset:0;
  z-index:-2;
  pointer-events:none;
  background:
    linear-gradient(rgba(8,121,242,.025) 1px, transparent 1px),
    linear-gradient(90deg, rgba(8,121,242,.025) 1px, transparent 1px);
  background-size:42px 42px;
  mask-image:linear-gradient(to bottom,transparent 0%,#000 14%,#000 86%,transparent 100%);
}

/* Scroll progress line */
.scroll-progress{
  position:fixed;top:0;left:0;height:4px;width:0%;z-index:12000;
  background:linear-gradient(90deg,var(--cyan),var(--blue),#72efff);
  box-shadow:0 0 20px rgba(25,214,255,.7);
  transform-origin:left;
  transition:width .08s linear;
}

/* Loading entrance */
body.dg-v13:not(.page-ready) .site-header,
body.dg-v13:not(.page-ready) main,
body.dg-v13:not(.page-ready) .footer,
body.dg-v13:not(.page-ready) .phone-float{opacity:0;transform:translateY(10px)}
body.dg-v13.page-ready .site-header,
body.dg-v13.page-ready main,
body.dg-v13.page-ready .footer,
body.dg-v13.page-ready .phone-float{opacity:1;transform:none;transition:opacity .55s var(--ease-out),transform .55s var(--ease-out)}

/* Header feels alive */
body.dg-v13 .site-header{
  border-bottom:1px solid rgba(25,214,255,.28)!important;
  box-shadow:0 18px 60px rgba(4,42,65,.08)!important;
}
body.dg-v13 .brand img{transition:transform .55s var(--ease-bounce), filter .55s var(--ease-out)}
body.dg-v13 .brand:hover img{transform:translateY(-3px) rotate(-2deg) scale(1.05);filter:drop-shadow(0 18px 24px rgba(25,214,255,.24))}
body.dg-v13 .nav>a,
body.dg-v13 .dropdown-trigger{transition:transform .35s var(--ease-bounce), color .25s ease!important;}
body.dg-v13 .nav>a:hover,
body.dg-v13 .dropdown-trigger:hover{transform:translateY(-4px) scale(1.035)!important;color:var(--blue)!important;}
body.dg-v13 .nav>a:before,
body.dg-v13 .dropdown-trigger:before{
  content:"";position:absolute;left:50%;bottom:2px;width:7px;height:7px;border-radius:50%;
  background:var(--cyan);transform:translateX(-50%) scale(0);opacity:0;transition:.3s var(--ease-bounce);
  box-shadow:0 0 16px rgba(25,214,255,.8);
}
body.dg-v13 .nav>a:hover:before,
body.dg-v13 .dropdown:hover .dropdown-trigger:before{opacity:1;transform:translateX(-50%) scale(1)}
body.dg-v13 .socials a,
body.dg-v13 .footer-socials a{
  position:relative!important;isolation:isolate;
  box-shadow:0 12px 30px rgba(5,52,78,.10),0 0 0 8px rgba(25,214,255,.09)!important;
}
body.dg-v13 .socials a:before,
body.dg-v13 .footer-socials a:before{
  content:"";position:absolute;inset:-7px;border-radius:50%;border:1px solid rgba(25,214,255,.45);
  animation:dgSocialRing 2.8s ease-in-out infinite;z-index:-1;
}
body.dg-v13 .socials a:hover,
body.dg-v13 .footer-socials a:hover{transform:translateY(-8px) rotate(-6deg) scale(1.08)!important;background:linear-gradient(145deg,#fff,#e8fbff)!important;}
body.dg-v13 .socials a:hover img,
body.dg-v13 .footer-socials a:hover img{animation:dgWiggle .55s var(--ease-bounce)}

/* Universal animated surfaces */
body.dg-v13 .service-card,
body.dg-v13 .contact-card,
body.dg-v13 .info-box,
body.dg-v13 .feature,
body.dg-v13 .video-card,
body.dg-v13 .video-placeholder,
body.dg-v13 .lead-card,
body.dg-v13 .operator-box,
body.dg-v13 .map-panel,
body.dg-v13 .trust,
body.dg-v13 .price-box,
body.dg-v13 .faq details,
body.dg-v13 .real-gallery-card{
  position:relative!important;overflow:hidden!important;transform-style:preserve-3d;will-change:transform,box-shadow;
}
body.dg-v13 .service-card:before,
body.dg-v13 .contact-card:before,
body.dg-v13 .info-box:before,
body.dg-v13 .feature:before,
body.dg-v13 .video-card:before,
body.dg-v13 .video-placeholder:before,
body.dg-v13 .lead-card:before,
body.dg-v13 .operator-box:before,
body.dg-v13 .map-panel:before,
body.dg-v13 .trust:before,
body.dg-v13 .price-box:before,
body.dg-v13 .faq details:before,
body.dg-v13 .real-gallery-card:before{
  content:"";position:absolute;inset:-80px auto auto -90px;width:90px;height:220%;
  background:linear-gradient(90deg,transparent,rgba(255,255,255,.62),transparent);
  transform:rotate(22deg) translateX(-120%);opacity:0;pointer-events:none;z-index:4;
}
body.dg-v13 .service-card:hover:before,
body.dg-v13 .contact-card:hover:before,
body.dg-v13 .info-box:hover:before,
body.dg-v13 .feature:hover:before,
body.dg-v13 .video-card:hover:before,
body.dg-v13 .video-placeholder:hover:before,
body.dg-v13 .lead-card:hover:before,
body.dg-v13 .operator-box:hover:before,
body.dg-v13 .map-panel:hover:before,
body.dg-v13 .trust:hover:before,
body.dg-v13 .price-box:hover:before,
body.dg-v13 .faq details:hover:before,
body.dg-v13 .real-gallery-card:hover:before{animation:dgSurfaceSweep .9s var(--ease-out)}
body.dg-v13 .service-card:hover,
body.dg-v13 .contact-card:hover,
body.dg-v13 .info-box:hover,
body.dg-v13 .feature:hover,
body.dg-v13 .video-card:hover,
body.dg-v13 .video-placeholder:hover,
body.dg-v13 .lead-card:hover,
body.dg-v13 .operator-box:hover,
body.dg-v13 .map-panel:hover,
body.dg-v13 .trust:hover,
body.dg-v13 .price-box:hover,
body.dg-v13 .faq details:hover{
  transform:translateY(-12px) scale(1.012)!important;
  box-shadow:var(--deep-shadow),var(--cyan-glow)!important;
  border-color:rgba(25,214,255,.52)!important;
}

/* Buttons: richer movement */
body.dg-v13 .btn,
body.dg-v13 .card-link,
body.dg-v13 .mini-cta{
  isolation:isolate;transform:translateZ(0);transition:transform .38s var(--ease-bounce),box-shadow .38s var(--ease-out),filter .38s ease!important;
}
body.dg-v13 .btn:hover,
body.dg-v13 .mini-cta:hover{transform:translateY(-6px) scale(1.045)!important;filter:saturate(1.12);}
body.dg-v13 .btn:after{
  content:"";position:absolute;inset:0;border-radius:inherit;z-index:-1;background:inherit;filter:blur(16px);opacity:.35;transition:.35s;
}
body.dg-v13 .btn:hover:after{opacity:.68;filter:blur(22px)}
body.dg-v13 .btn:active{transform:translateY(-2px) scale(.98)!important;}
.ripple-dot{position:absolute;border-radius:50%;pointer-events:none;background:rgba(255,255,255,.7);transform:translate(-50%,-50%) scale(0);animation:dgRipple .65s ease-out forwards;z-index:10;}

/* Clean banner: same beautiful type everywhere and more motion */
body.dg-v13 .dg-clean-banner{
  min-height:330px!important;
  background:
    linear-gradient(90deg,rgba(4,28,42,.62),rgba(6,70,95,.36),rgba(4,28,42,.62)),
    url("doorgo banner.png") center/520px auto repeat!important;
  border-bottom:1px solid rgba(25,214,255,.30)!important;
}
body.dg-v13 .dg-clean-banner:before{
  background:
    radial-gradient(circle at 50% 52%,rgba(255,255,255,.18),transparent 30%),
    linear-gradient(180deg,rgba(255,255,255,.08),rgba(0,0,0,.18))!important;
}
body.dg-v13 .dg-clean-banner .dg-clean-banner-inner:before,
body.dg-v13 .dg-clean-banner .dg-clean-banner-inner:after{
  content:"";position:absolute;left:50%;transform:translateX(-50%);height:3px;border-radius:999px;
  background:linear-gradient(90deg,transparent,var(--cyan),var(--blue),transparent);
  width:min(420px,70vw);opacity:.8;animation:dgLineBreathe 2.4s ease-in-out infinite;
}
body.dg-v13 .dg-clean-banner .dg-clean-banner-inner:before{top:50%;margin-top:42px;}
body.dg-v13 .dg-clean-banner .dg-clean-banner-inner:after{display:none;}
body.dg-v13 .dg-clean-banner h1{
  animation:dgTitlePop .9s var(--ease-bounce) both, dgTitleGlow 3.8s ease-in-out infinite!important;
}
.dg-banner-particle{
  position:absolute;width:8px;height:8px;border-radius:50%;background:rgba(25,214,255,.75);
  box-shadow:0 0 22px rgba(25,214,255,.9);pointer-events:none;z-index:1;animation:dgParticle 6s linear infinite;
}
.dg-banner-particle:nth-child(2n){width:5px;height:5px;background:rgba(255,255,255,.75)}

/* Service card media feels more premium */
body.dg-v13 .card-img:before,
body.dg-v13 .service-photo:before{
  content:"";position:absolute;inset:0;z-index:2;pointer-events:none;
  background:radial-gradient(circle at var(--mx,50%) var(--my,50%),rgba(255,255,255,.28),transparent 28%);
  opacity:0;transition:opacity .32s ease;
}
body.dg-v13 .service-card:hover .card-img:before,
body.dg-v13 .service-photo:hover:before{opacity:1;}
body.dg-v13 .card-img img,
body.dg-v13 .service-photo img,
body.dg-v13 .real-gallery-card img{transition:transform .75s var(--ease-out),filter .75s var(--ease-out)!important;}
body.dg-v13 .service-card:hover .card-img img,
body.dg-v13 .service-photo:hover img{transform:scale(1.095)!important;filter:saturate(1.12) contrast(1.06)}

/* Gallery layout: stronger consistent alignment */
body.dg-v13 .portfolio-masonry,
body.dg-v13 .real-gallery-grid.portfolio-masonry{
  align-items:stretch!important;
  grid-template-columns:repeat(3,minmax(230px,1fr))!important;
}
body.dg-v13 .real-gallery-card{cursor:zoom-in!important;}
body.dg-v13 .real-gallery-card figcaption{
  background:linear-gradient(180deg,transparent,rgba(2,18,30,.86))!important;
}
body.dg-v13 .real-gallery-card:hover img{transform:scale(1.08)!important;filter:saturate(1.12) contrast(1.06);}
body.dg-v13 .gallery-lightbox{backdrop-filter:blur(18px);background:rgba(3,16,26,.72)!important;}
body.dg-v13 .gallery-lightbox img{
  max-width:min(88vw,980px);max-height:84vh;border-radius:30px;box-shadow:0 45px 140px rgba(0,0,0,.42),0 0 0 1px rgba(255,255,255,.18);
}

/* Contact icons always visible, with a stronger premium hover */
body.dg-v13 .contact-card .contact-icon img{opacity:1!important;visibility:visible!important;mix-blend-mode:normal!important;}
body.dg-v13 .contact-card:hover .contact-icon{transform:translateY(-8px) rotate(3deg) scale(1.05)!important;}
body.dg-v13 .contact-card:hover h3{color:var(--blue)!important;}

/* Floating phone as real sticky action */
body.dg-v13 .phone-float{
  width:74px!important;height:74px!important;border-radius:50%!important;
  background:linear-gradient(135deg,#19e66b,#08b83b)!important;
  display:grid!important;place-items:center!important;
  box-shadow:0 0 0 12px rgba(16,200,63,.13),0 24px 58px rgba(16,200,63,.32)!important;
  animation:dgPhoneBounce 2.4s ease-in-out infinite!important;
}
body.dg-v13 .phone-float:before,
body.dg-v13 .phone-float:after{content:"";position:absolute;inset:-10px;border-radius:50%;border:1px solid rgba(16,200,63,.35);animation:dgPhoneWave 2s ease-out infinite;}
body.dg-v13 .phone-float:after{animation-delay:.72s;}
body.dg-v13 .phone-float img{width:34px!important;height:34px!important;filter:brightness(0) invert(1)!important;animation:dgWiggle 2.4s ease-in-out infinite;}
body.dg-v13 .phone-float:hover{animation:none!important;transform:translateY(-12px) scale(1.12) rotate(-7deg)!important;}

/* Footer polish */
body.dg-v13 .footer{position:relative;overflow:hidden;}
body.dg-v13 .footer:before{content:"";position:absolute;inset:0;background:radial-gradient(circle at 20% 0%,rgba(25,214,255,.14),transparent 34%),radial-gradient(circle at 85% 20%,rgba(8,121,242,.12),transparent 30%);pointer-events:none;}
body.dg-v13 .footer a{transition:color .25s ease,transform .35s var(--ease-bounce)!important;}
body.dg-v13 .footer a:hover{color:var(--cyan)!important;transform:translateX(6px);}

/* FAQ open animation */
body.dg-v13 details[open]{animation:dgOpen .32s var(--ease-out);}
body.dg-v13 summary{cursor:pointer;transition:color .25s ease,transform .25s ease;}
body.dg-v13 summary:hover{color:var(--blue);transform:translateX(4px);}

/* Mobile: much stronger custom app-like look */
@media(max-width:760px){
  body.dg-v13{background:linear-gradient(180deg,#effbff,#fff 34%,#f4fcff)!important;}
  body.dg-v13 .site-header{width:calc(100% - 18px)!important;margin:9px auto 0!important;border-radius:24px!important;}
  body.dg-v13 .nav.open{
    position:fixed!important;left:12px!important;right:12px!important;top:92px!important;
    display:flex!important;flex-direction:column!important;gap:8px!important;
    padding:18px!important;border-radius:28px!important;background:rgba(255,255,255,.94)!important;
    border:1px solid rgba(25,214,255,.28)!important;box-shadow:0 34px 100px rgba(3,24,43,.22)!important;
    animation:dgMobileMenu .42s var(--ease-bounce) both!important;z-index:9999!important;
  }
  body.dg-v13 .nav.open a,body.dg-v13 .nav.open .dropdown-trigger{width:100%;padding:13px 14px!important;border-radius:18px;background:linear-gradient(135deg,#fff,#effcff);}
  body.dg-v13 .dropdown-menu{position:static!important;width:100%!important;opacity:1!important;visibility:visible!important;transform:none!important;display:none;margin-top:6px;box-shadow:none!important;}
  body.dg-v13 .dropdown:hover .dropdown-menu,body.dg-v13 .dropdown:focus-within .dropdown-menu{display:block!important;}

  body.dg-v13 .dg-clean-banner{
    min-height:252px!important;padding:44px 14px 58px!important;margin-top:0!important;
    background-size:310px auto!important;border-radius:0 0 34px 34px!important;
  }
  body.dg-v13 .dg-clean-banner h1{font-size:clamp(34px,13vw,54px)!important;text-shadow:0 14px 34px rgba(0,0,0,.38)!important;}
  body.dg-v13 .dg-banner-actions .btn{min-width:132px!important;border-radius:18px!important;}

  body.dg-v13 .hero-inner{padding:28px 16px 0!important;}
  body.dg-v13 .hero h1{font-size:clamp(32px,11vw,46px)!important;line-height:1.06!important;}
  body.dg-v13 .hero-actions{position:sticky;bottom:12px;z-index:40;margin-top:18px;}
  body.dg-v13 .hero-grid{grid-template-columns:1fr!important;gap:18px!important;padding:26px 16px!important;border-radius:34px 34px 0 0!important;}
  body.dg-v13 .hero-tile{min-height:240px!important;border-radius:28px!important;}

  body.dg-v13 .service-grid,
  body.dg-v13 .feature-grid,
  body.dg-v13 .info-grid,
  body.dg-v13 .video-row,
  body.dg-v13 .contact-cards-polished,
  body.dg-v13 .trust-row{grid-template-columns:1fr!important;gap:18px!important;}
  body.dg-v13 .service-card,body.dg-v13 .feature,body.dg-v13 .info-box,body.dg-v13 .lead-card,body.dg-v13 .price-box,body.dg-v13 .cta-band{border-radius:30px!important;}
  body.dg-v13 .card-img{height:220px!important;}
  body.dg-v13 .card-body{padding:22px!important;}
  body.dg-v13 .card-body h3,body.dg-v13 .feature h3,body.dg-v13 .info-box h3{font-size:22px!important;}
  body.dg-v13 .icon-badge{width:78px!important;height:78px!important;margin:-39px 0 0 22px!important;}
  body.dg-v13 .icon-badge img{width:38px!important;height:38px!important;}

  body.dg-v13 .portfolio-masonry,
  body.dg-v13 .real-gallery-grid.portfolio-masonry{grid-template-columns:1fr 1fr!important;gap:12px!important;}
  body.dg-v13 .portfolio-masonry .real-gallery-card,
  body.dg-v13 .real-gallery-grid.portfolio-masonry .real-gallery-card{aspect-ratio:1/1.32!important;border-radius:22px!important;}
  body.dg-v13 .real-gallery-card figcaption{padding:30px 12px 12px!important;}
  body.dg-v13 .real-gallery-card figcaption b{font-size:13px!important;line-height:1.25!important;}

  body.dg-v13 .contact-hero-card{border-radius:30px!important;text-align:left!important;}
  body.dg-v13 .contact-hero-card h2{font-size:28px!important;}
  body.dg-v13 .contact-card{display:grid!important;grid-template-columns:78px 1fr!important;text-align:left!important;align-items:center!important;gap:14px!important;min-height:150px!important;}
  body.dg-v13 .contact-card .contact-icon{margin:0!important;width:72px!important;height:72px!important;border-radius:24px!important;}
  body.dg-v13 .contact-card h3{font-size:20px!important;}
  body.dg-v13 .contact-card p{font-size:14px!important;}
  body.dg-v13 .map-panel{min-height:220px!important;}

  body.dg-v13 .phone-float{width:64px!important;height:64px!important;left:16px!important;bottom:16px!important;}
  body.dg-v13 .phone-float img{width:30px!important;height:30px!important;}

  body.dg-v13 .footer-inner{gap:26px!important;text-align:left!important;}
  body.dg-v13 .footer-logo{max-width:116px!important;}
}

@media(max-width:420px){
  body.dg-v13 .portfolio-masonry,
  body.dg-v13 .real-gallery-grid.portfolio-masonry{grid-template-columns:1fr!important;}
  body.dg-v13 .portfolio-masonry .real-gallery-card,
  body.dg-v13 .real-gallery-grid.portfolio-masonry .real-gallery-card{aspect-ratio:4/5!important;}
  body.dg-v13 .contact-card{grid-template-columns:1fr!important;text-align:center!important;}
  body.dg-v13 .contact-card .contact-icon{margin:0 auto 10px!important;}
}

@media(prefers-reduced-motion:reduce){
  *,*::before,*::after{animation-duration:.01ms!important;animation-iteration-count:1!important;transition-duration:.01ms!important;scroll-behavior:auto!important;}
}

@keyframes dgSurfaceSweep{0%{opacity:0;transform:rotate(22deg) translateX(-130%)}25%{opacity:.9}100%{opacity:0;transform:rotate(22deg) translateX(420%)}}
@keyframes dgSocialRing{0%,100%{transform:scale(.92);opacity:.45}50%{transform:scale(1.12);opacity:.9}}
@keyframes dgWiggle{0%,100%{transform:rotate(0)}20%{transform:rotate(-9deg)}40%{transform:rotate(8deg)}60%{transform:rotate(-5deg)}80%{transform:rotate(3deg)}}
@keyframes dgRipple{to{transform:translate(-50%,-50%) scale(7);opacity:0}}
@keyframes dgTitlePop{0%{opacity:0;transform:translateY(22px) scale(.94);filter:blur(6px)}100%{opacity:1;transform:none;filter:blur(0)}}
@keyframes dgTitleGlow{0%,100%{text-shadow:0 18px 50px rgba(0,0,0,.38),0 0 0 rgba(25,214,255,0)}50%{text-shadow:0 18px 50px rgba(0,0,0,.38),0 0 30px rgba(25,214,255,.35)}}
@keyframes dgLineBreathe{0%,100%{transform:translateX(-50%) scaleX(.72);opacity:.45}50%{transform:translateX(-50%) scaleX(1);opacity:1}}
@keyframes dgParticle{0%{transform:translateY(110px) translateX(0) scale(.7);opacity:0}14%{opacity:1}100%{transform:translateY(-170px) translateX(55px) scale(1.1);opacity:0}}
@keyframes dgPhoneBounce{0%,100%{transform:translateY(0) rotate(0)}50%{transform:translateY(-8px) rotate(-4deg)}}
@keyframes dgPhoneWave{0%{opacity:.75;transform:scale(.8)}100%{opacity:0;transform:scale(1.55)}}
@keyframes dgOpen{from{opacity:.7;transform:translateY(-4px)}to{opacity:1;transform:none}}
@keyframes dgMobileMenu{0%{opacity:0;transform:translateY(-10px) scale(.94)}100%{opacity:1;transform:none}}
'''
css.write_text(css.read_text(encoding='utf-8')+css_add,encoding='utf-8')

js_add=r'''

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

  // smooth parallax / spotlight on cards and images
  const hoverTargets=document.querySelectorAll('.service-card,.contact-card,.info-box,.feature,.video-card,.video-placeholder,.lead-card,.operator-box,.map-panel,.real-gallery-card,.service-photo');
  hoverTargets.forEach(el=>{
    el.addEventListener('pointermove',e=>{
      if(window.innerWidth<761) return;
      const r=el.getBoundingClientRect();
      const x=(e.clientX-r.left)/r.width;
      const y=(e.clientY-r.top)/r.height;
      el.style.setProperty('--mx',(x*100).toFixed(1)+'%');
      el.style.setProperty('--my',(y*100).toFixed(1)+'%');
      const rx=(.5-y)*5;
      const ry=(x-.5)*5;
      if(!el.classList.contains('service-photo')) el.style.transform=`translateY(-10px) rotateX(${rx.toFixed(2)}deg) rotateY(${ry.toFixed(2)}deg)`;
    });
    el.addEventListener('pointerleave',()=>{
      el.style.removeProperty('--mx');
      el.style.removeProperty('--my');
      el.style.transform='';
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
'''
js.write_text(js.read_text(encoding='utf-8')+js_add,encoding='utf-8')
