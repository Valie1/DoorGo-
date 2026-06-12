from pathlib import Path
import re, shutil, zipfile, os
site=Path('/mnt/data/doorgo_work/site')
js=site/'script.js'
s=js.read_text()
# Remove hover bubble whole IIFE
s=re.sub(r"\n// DoorGO v16: universal smooth hover popups \+ magnetic movement\n\(function\(\)\{.*?\n\}\)\(\);\s*$", "\n", s, flags=re.S)
# Remove small pointer tilt block
s=re.sub(r"\n  // Small pointer tilt on desktop only\n  const cards = \[\.\.\.document\.querySelectorAll\('\.service-card,\.contact-card,\.video-card'\)\];.*?\n  \}\);\n", "\n", s, flags=re.S)
# Remove v14 hover target pointermove transform block
s=re.sub(r"\n  // smooth parallax / spotlight on cards and images\n  const hoverTargets=document\.querySelectorAll\('.*?'\);.*?\n  \}\);\n", "\n", s, flags=re.S)
js.write_text(s)
# Patch MainHome hero with banner + service strip preserved but better structure (remove hero-inner trust stuffing maybe keep)
main=site/'MainHome.html'
h=main.read_text()
old=re.search(r'<section class="hero">.*?</section>\n<section class="section">', h, flags=re.S)
if old:
    new='''<section class="hero home-hero-v17"><div class="hero-inner"><span class="eyebrow">DoorGO 24/7</span><h1>ჩაკეტილი კარის და მანქანის გაღება <span>თბილისში</span></h1><p class="hero-sub">სწრაფი გამოძახება, სუფთა მუშაობა და წინასწარ შეთანხმებული ფასი.</p><div class="hero-actions"><a class="btn" href="tel:597606000">დარეკე: 597 60 60 00</a><a class="btn white" href="OurServices.html">ნახე სერვისები</a></div></div><div class="home-service-showcase"><div class="hero-grid"><div class="hero-tile"><div class="tile-icon"><img alt="" src="house-key.png"/></div><img alt="ჩაკეტილი სახლის კარის გაღება" src="house lock.jpg"/><span>ჩაკეტილი სახლის კარის გაღება</span></div><div class="hero-tile"><div class="tile-icon"><img alt="" src="car-open.png"/></div><img alt="ჩაკეტილი მანქანის კარის გაღება" src="car lock.jpg"/><span>ჩაკეტილი მანქანის კარის გაღება</span></div><div class="hero-tile"><div class="tile-icon"><img alt="" src="door-handle.png"/></div><img alt="საკეტის შეცვლა/შეკეთება" src="change lock.jpg"/><span>საკეტის შეცვლა/შეკეთება</span></div></div><div class="trust-row"><div class="trust">24/7 გამოძახება</div><div class="trust">დაუზიანებლად</div><div class="trust">თბილისის მასშტაბით</div><div class="trust">ფასი 50₾-დან</div></div></div></section>\n<section class="section">'''
    h=h[:old.start()]+new+h[old.end()-len('<section class="section">'):]
main.write_text(h)
(site/'index.html').write_text(h.replace('<title>მთავარი  DoorGO</title>','<title>მთავარი  DoorGO</title>'))
# ensure body class v17 for pages
for p in site.glob('*.html'):
    t=p.read_text()
    t=t.replace('body class="dg-v13"','body class="dg-v13 dg-v17"')
    # remove aria-label on social/floating? keep accessibility, bubble gone so ok
    p.write_text(t)
# append CSS override
css=site/'style.css'
css.write_text(css.read_text()+r'''

/* =====================================================
   DoorGO v17 LOCK-IN PATCH
   Fixes: real banners back, no hover text bubbles, pure pop hover,
   cleaner desktop/mobile layout, better service photo positions.
   ===================================================== */
body.dg-v17{
  background:
    radial-gradient(circle at 10% 8%,rgba(33,214,255,.13),transparent 28%),
    radial-gradient(circle at 92% 16%,rgba(8,121,242,.08),transparent 32%),
    linear-gradient(180deg,#f8fdff,#ffffff 45%,#effbff)!important;
  color:#061826!important;
}
.dg-hover-bubble{display:none!important;opacity:0!important;visibility:hidden!important;content:none!important;}

/* no browser-looking/AI tooltip labels, only real animation */
[title]{cursor:pointer;}
.dg-hoverable:before,.dg-hoverable:after{pointer-events:none;}

/* header more solid, no awkward crop */
body.dg-v17 .site-header{
  background:rgba(255,255,255,.94)!important;
  border-bottom:1px solid rgba(31,202,245,.30)!important;
  box-shadow:0 10px 32px rgba(4,29,46,.07)!important;
}
body.dg-v17 .header-inner{min-height:74px!important;}
body.dg-v17 .brand img{height:58px!important;max-width:150px!important;object-fit:contain!important;}
body.dg-v17 .nav a,body.dg-v17 .dropdown-trigger{transition:transform .18s cubic-bezier(.2,1.4,.2,1), color .18s ease!important;}
body.dg-v17 .nav a:hover,body.dg-v17 .dropdown-trigger:hover{transform:translateY(-3px) scale(1.05)!important;color:#0879f2!important;}

/* universal POP hover: immediate, visible, no text bubble */
body.dg-v17 a,body.dg-v17 button,body.dg-v17 .service-card,body.dg-v17 .hero-tile,body.dg-v17 .real-gallery-card,body.dg-v17 .video-card,body.dg-v17 .video-placeholder,body.dg-v17 .contact-card,body.dg-v17 .info-box,body.dg-v17 .feature,body.dg-v17 .trust,body.dg-v17 .lead-card,body.dg-v17 .operator-box,body.dg-v17 .map-panel,body.dg-v17 .service-photo,body.dg-v17 .map-box{
  transition:transform .16s cubic-bezier(.16,1.45,.32,1), box-shadow .20s ease, filter .20s ease, background .20s ease, border-color .20s ease!important;
  will-change:transform;
}
body.dg-v17 a:hover,body.dg-v17 button:hover,body.dg-v17 .service-card:hover,body.dg-v17 .hero-tile:hover,body.dg-v17 .real-gallery-card:hover,body.dg-v17 .video-card:hover,body.dg-v17 .video-placeholder:hover,body.dg-v17 .contact-card:hover,body.dg-v17 .info-box:hover,body.dg-v17 .feature:hover,body.dg-v17 .trust:hover,body.dg-v17 .lead-card:hover,body.dg-v17 .operator-box:hover,body.dg-v17 .map-panel:hover,body.dg-v17 .service-photo:hover,body.dg-v17 .map-box:hover{
  transform:translateY(-8px) scale(1.035)!important;
  filter:saturate(1.04);
}
body.dg-v17 .btn:hover{transform:translateY(-6px) scale(1.06)!important;}
body.dg-v17 .socials a:hover,body.dg-v17 .footer-socials a:hover{
  transform:translateY(-7px) scale(1.14)!important;
  background:#fff!important;
  box-shadow:0 0 0 8px rgba(33,214,255,.13),0 18px 42px rgba(8,121,242,.22)!important;
}
body.dg-v17 .socials a:hover img,body.dg-v17 .footer-socials a:hover img{filter:none!important;opacity:1!important;transform:scale(1.18)!important;}

/* one clean banner design everywhere */
body.dg-v17 .dg-clean-banner,
body.dg-v17 .home-hero-v17 .hero-inner{
  position:relative!important;
  min-height:360px!important;
  width:100%!important;
  max-width:none!important;
  margin:0!important;
  padding:70px 22px 74px!important;
  display:grid!important;
  place-items:center!important;
  text-align:center!important;
  color:#fff!important;
  overflow:hidden!important;
  background-color:#09283a!important;
  background-image:
    linear-gradient(90deg,rgba(5,20,30,.62),rgba(10,50,67,.38),rgba(5,20,30,.62)),
    radial-gradient(circle at 50% 50%,rgba(37,219,255,.25),transparent 38%),
    url("doorgo banner.png")!important;
  background-size:cover,cover,cover!important;
  background-repeat:no-repeat!important;
  background-position:center!important;
  border-bottom:1px solid rgba(37,219,255,.25)!important;
  box-shadow:inset 0 -45px 100px rgba(3,20,30,.22)!important;
}
body.dg-v17 .dg-clean-banner:before,
body.dg-v17 .home-hero-v17 .hero-inner:before{
  content:""!important;
  position:absolute!important;
  inset:0!important;
  background:
    linear-gradient(115deg,transparent 0%,rgba(255,255,255,.12) 46%,transparent 54%),
    radial-gradient(circle at 50% 46%,rgba(255,255,255,.10),transparent 38%)!important;
  transform:translateX(-115%);
  animation:v17BannerSweep 5.8s ease-in-out infinite!important;
}
body.dg-v17 .dg-clean-banner:after,
body.dg-v17 .home-hero-v17 .hero-inner:after{
  content:""!important;position:absolute!important;left:-7%;right:-7%;bottom:-44px;height:92px!important;
  background:#f7fdff!important;border-radius:50% 50% 0 0/100% 100% 0 0!important;
  box-shadow:0 -22px 65px rgba(37,219,255,.14)!important;
}
@keyframes v17BannerSweep{0%,32%{transform:translateX(-115%)}70%,100%{transform:translateX(115%)}}
body.dg-v17 .dg-clean-banner-inner,body.dg-v17 .home-hero-v17 .hero-inner > *{position:relative;z-index:2;}
body.dg-v17 .dg-clean-banner h1,
body.dg-v17 .home-hero-v17 h1{
  color:#fff!important;
  font-size:clamp(44px,6.4vw,86px)!important;
  line-height:.98!important;
  letter-spacing:-.065em!important;
  text-shadow:0 20px 55px rgba(0,0,0,.36),0 0 24px rgba(37,219,255,.18)!important;
  max-width:1120px!important;
  margin:14px auto 12px!important;
}
body.dg-v17 .home-hero-v17 h1 span{color:#e8fbff!important;}
body.dg-v17 .hero-sub{color:rgba(255,255,255,.90)!important;font-weight:800!important;}
body.dg-v17 .eyebrow{background:rgba(255,255,255,.18)!important;color:#0879f2!important;backdrop-filter:blur(10px);}
body.dg-v17 .dg-clean-banner .eyebrow, body.dg-v17 .home-hero-v17 .eyebrow{color:#fff!important;border-color:rgba(255,255,255,.22)!important;}

/* home service showcase: no broken/cropped banner feeling */
body.dg-v17 .home-service-showcase{
  background:
    radial-gradient(circle at 50% 0%,rgba(37,219,255,.16),transparent 38%),
    linear-gradient(180deg,#061826,#082c42)!important;
  padding:72px 22px 72px!important;
}
body.dg-v17 .home-service-showcase .hero-grid{
  max-width:1080px!important;margin:0 auto!important;padding:0!important;background:none!important;
  display:grid!important;grid-template-columns:repeat(3,minmax(0,1fr))!important;gap:28px!important;
  box-shadow:none!important;
}
body.dg-v17 .hero-tile{
  min-height:330px!important;border-radius:34px!important;box-shadow:0 28px 80px rgba(0,0,0,.28)!important;
  border:1px solid rgba(37,219,255,.25)!important;
}
body.dg-v17 .hero-tile img{height:100%!important;width:100%!important;object-fit:cover!important;}
body.dg-v17 .hero-tile:after{background:linear-gradient(180deg,rgba(0,0,0,.02),rgba(3,20,30,.78))!important;}
body.dg-v17 .home-service-showcase .trust-row{max-width:1080px;margin:34px auto 0!important;}

/* service cards stronger and same quality */
body.dg-v17 .service-grid{gap:30px!important;align-items:stretch!important;}
body.dg-v17 .service-card{
  border-radius:32px!important;overflow:hidden!important;background:linear-gradient(180deg,#fff,#f6fdff)!important;
  box-shadow:0 24px 70px rgba(4,37,58,.12)!important;
}
body.dg-v17 .service-card:hover{box-shadow:0 34px 95px rgba(4,37,58,.22),0 0 0 1px rgba(37,219,255,.26) inset!important;}
body.dg-v17 .card-img{height:260px!important;}
body.dg-v17 .card-body{min-height:245px!important;display:flex;flex-direction:column;justify-content:space-between;}

/* service detail photos: better crop, centered, editorial */
body.dg-v17 .service-top{
  padding:68px 22px 72px!important;
  background:linear-gradient(180deg,#f4fcff,#ffffff 60%,#eefbff)!important;
}
body.dg-v17 .service-photo{
  width:min(1040px,88vw)!important;
  aspect-ratio:16/7.6!important;
  border-radius:36px!important;
  overflow:hidden!important;
  margin:0 auto!important;
  background:#eaf7fb!important;
  box-shadow:0 28px 82px rgba(4,37,58,.16),0 0 0 1px rgba(37,219,255,.26)!important;
}
body.dg-v17 .service-photo img{
  width:100%!important;height:100%!important;object-fit:cover!important;display:block!important;
}
body.dg-v17 .service-photo img[src="house lock.jpg"]{object-position:center 48%!important;}
body.dg-v17 .service-photo img[src="car lock.jpg"]{object-position:center 52%!important;}
body.dg-v17 .service-photo img[src="change lock.jpg"]{object-position:center 48%!important;}

/* contact icons readable */
body.dg-v17 .contact-cards{align-items:stretch!important;}
body.dg-v17 .contact-card{min-height:265px!important;display:flex!important;flex-direction:column!important;justify-content:center!important;align-items:center!important;text-align:center!important;}
body.dg-v17 .contact-icon{
  width:88px!important;height:88px!important;border-radius:28px!important;margin:0 auto 22px!important;
  display:grid!important;place-items:center!important;background:#fff!important;box-shadow:0 16px 45px rgba(8,121,242,.14)!important;
}
body.dg-v17 .contact-icon img{width:46px!important;height:46px!important;object-fit:contain!important;opacity:1!important;filter:none!important;}
body.dg-v17 .contact-card:hover .contact-icon{background:linear-gradient(135deg,#eaffff,#ffffff)!important;}
body.dg-v17 .contact-card:hover .contact-icon img{filter:none!important;transform:scale(1.16)!important;}

/* gallery: equal, cleaner, no repeated awkward layout */
body.dg-v17 .portfolio-masonry,
body.dg-v17 .real-gallery-grid{
  display:grid!important;
  grid-template-columns:repeat(3,minmax(0,1fr))!important;
  gap:26px!important;
  max-width:1180px!important;
  margin:0 auto!important;
  align-items:stretch!important;
}
body.dg-v17 .portfolio-masonry .real-gallery-card,
body.dg-v17 .real-gallery-card,
body.dg-v17 .real-gallery-card:nth-child(n){
  grid-column:auto!important;grid-row:auto!important;
  height:360px!important;min-height:360px!important;border-radius:30px!important;
  box-shadow:0 24px 72px rgba(4,37,58,.14)!important;
}
body.dg-v17 .real-gallery-card img{height:100%!important;width:100%!important;object-fit:cover!important;}
body.dg-v17 .real-gallery-card:hover{transform:translateY(-10px) scale(1.04)!important;z-index:10;}
body.dg-v17 .gallery-lightbox.open{animation:v17LightIn .32s cubic-bezier(.16,1.2,.25,1) both!important;}
body.dg-v17 .gallery-lightbox.closing{animation:v17LightOut .28s ease both!important;}
body.dg-v17 .gallery-lightbox img{animation:v17PhotoIn .34s cubic-bezier(.16,1.2,.25,1) both!important;border-radius:30px!important;}
@keyframes v17LightIn{from{opacity:0;backdrop-filter:blur(0)}to{opacity:1;backdrop-filter:blur(18px)}}
@keyframes v17LightOut{from{opacity:1;backdrop-filter:blur(18px)}to{opacity:0;backdrop-filter:blur(0)}}
@keyframes v17PhotoIn{from{opacity:0;transform:scale(.86) translateY(24px)}to{opacity:1;transform:none}}

/* footer and call button */
body.dg-v17 .footer{padding-top:80px!important;}
body.dg-v17 .phone-float{position:fixed!important;z-index:9999!important;left:28px!important;bottom:28px!important;}
body.dg-v17 .phone-float:hover{transform:translateY(-9px) scale(1.13)!important;}

/* stop random sticky lower hero buttons from covering design */
body.dg-v17 .hero-actions{position:relative!important;bottom:auto!important;z-index:2!important;}
body.dg-v17 .quick-bar,body.dg-v17 .mobile-quick,body.dg-v17 .bottom-cta,body.dg-v17 .sticky-bottom,body.dg-v17 .quick-contact{display:none!important;}

@media(max-width:900px){
  body.dg-v17 .site-header{position:sticky!important;top:0!important;}
  body.dg-v17 .header-inner{min-height:64px!important;padding:8px 14px!important;}
  body.dg-v17 .brand span{font-size:17px!important;}
  body.dg-v17 .brand img{height:42px!important;max-width:105px!important;}
  body.dg-v17 .menu-toggle{display:block!important;}
  body.dg-v17 .nav{display:none!important;position:absolute!important;left:12px!important;right:12px!important;top:64px!important;background:rgba(255,255,255,.96)!important;backdrop-filter:blur(18px)!important;border:1px solid rgba(37,219,255,.25)!important;border-radius:22px!important;padding:12px!important;box-shadow:0 24px 70px rgba(4,37,58,.18)!important;}
  body.dg-v17 .nav.open{display:grid!important;gap:4px!important;}
  body.dg-v17 .nav a,body.dg-v17 .dropdown-trigger{padding:12px 14px!important;border-radius:14px!important;}
  body.dg-v17 .dropdown-menu{position:static!important;width:auto!important;visibility:visible!important;opacity:1!important;transform:none!important;box-shadow:none!important;background:#f2fcff!important;margin:6px 0!important;}
  body.dg-v17 .socials a{width:36px!important;height:36px!important;}
  body.dg-v17 .socials img{width:18px!important;height:18px!important;}
  body.dg-v17 .dg-clean-banner,body.dg-v17 .home-hero-v17 .hero-inner{min-height:300px!important;padding:52px 16px 62px!important;background-size:cover!important;}
  body.dg-v17 .dg-clean-banner h1,body.dg-v17 .home-hero-v17 h1{font-size:clamp(38px,12vw,58px)!important;line-height:1.02!important;}
  body.dg-v17 .hero-sub{font-size:15px!important;}
  body.dg-v17 .home-service-showcase{padding:46px 16px!important;}
  body.dg-v17 .home-service-showcase .hero-grid{grid-template-columns:1fr!important;gap:18px!important;}
  body.dg-v17 .hero-tile{min-height:300px!important;}
  body.dg-v17 .trust-row{grid-template-columns:1fr 1fr!important;gap:10px!important;}
  body.dg-v17 .service-grid,body.dg-v17 .feature-grid,body.dg-v17 .info-grid,body.dg-v17 .contact-cards,body.dg-v17 .video-row{grid-template-columns:1fr!important;}
  body.dg-v17 .service-card{border-radius:28px!important;}
  body.dg-v17 .card-img{height:230px!important;}
  body.dg-v17 .card-body{min-height:auto!important;padding:24px!important;}
  body.dg-v17 .service-photo{width:94vw!important;aspect-ratio:4/3!important;border-radius:28px!important;}
  body.dg-v17 .portfolio-masonry,body.dg-v17 .real-gallery-grid{grid-template-columns:1fr!important;gap:18px!important;max-width:94vw!important;}
  body.dg-v17 .portfolio-masonry .real-gallery-card,body.dg-v17 .real-gallery-card,body.dg-v17 .real-gallery-card:nth-child(n){height:340px!important;min-height:340px!important;}
  body.dg-v17 .footer-inner{grid-template-columns:1fr!important;text-align:left!important;gap:28px!important;}
  body.dg-v17 .phone-float{width:64px!important;height:64px!important;left:16px!important;bottom:16px!important;}
}
@media(max-width:520px){
  body.dg-v17 .top-line{height:3px!important;}
  body.dg-v17 .header-inner{gap:8px!important;}
  body.dg-v17 .socials{gap:5px!important;}
  body.dg-v17 .socials a{width:33px!important;height:33px!important;}
  body.dg-v17 .dg-clean-banner,body.dg-v17 .home-hero-v17 .hero-inner{min-height:270px!important;}
  body.dg-v17 .dg-clean-banner h1,body.dg-v17 .home-hero-v17 h1{font-size:38px!important;}
  body.dg-v17 .hero-actions{display:grid!important;grid-template-columns:1fr!important;gap:10px!important;width:100%!important;max-width:330px!important;margin:18px auto 0!important;}
  body.dg-v17 .btn{width:100%!important;min-height:48px!important;}
  body.dg-v17 .trust-row{grid-template-columns:1fr!important;}
  body.dg-v17 .hero-tile{min-height:260px!important;}
  body.dg-v17 .section{padding:58px 16px!important;}
  body.dg-v17 .content{padding:54px 16px!important;}
  body.dg-v17 .service-photo{aspect-ratio:1.2/1!important;}
  body.dg-v17 .portfolio-masonry .real-gallery-card,body.dg-v17 .real-gallery-card,body.dg-v17 .real-gallery-card:nth-child(n){height:315px!important;min-height:315px!important;}
}
''')
