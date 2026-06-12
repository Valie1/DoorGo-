from bs4 import BeautifulSoup
from pathlib import Path

root = Path('.')

def banner(soup, title, eyebrow='DoorGO', buttons=True):
    sec = soup.new_tag('section')
    sec['class'] = ['dg-clean-banner','reveal']
    inner = soup.new_tag('div'); inner['class']=['dg-clean-banner-inner']
    if eyebrow:
        sp = soup.new_tag('span'); sp['class']=['eyebrow']; sp.string = eyebrow; inner.append(sp)
    h = soup.new_tag('h1'); h.string = title; inner.append(h)
    if buttons:
        actions = soup.new_tag('div'); actions['class']=['dg-banner-actions']
        a1=soup.new_tag('a', href='tel:597606000'); a1['class']=['btn']; a1.string='დარეკვა'
        a2=soup.new_tag('a', href='OurServices.html'); a2['class']=['btn','white']; a2.string='სერვისები'
        actions.append(a1); actions.append(a2); inner.append(actions)
    sec.append(inner)
    return sec

page_titles = {
    'AboutUs.html': ('ჩვენს შესახებ', 'DoorGO'),
    'Contact.html': ('კონტაქტი', 'DoorGO'),
    'Gallery.html': ('გალერია', 'DoorGO'),
    'VideoGallery.html': ('გალერია', 'DoorGO'),
    'OurServices.html': ('სერვისები', 'DoorGO'),
    'chaketili-saxlis-karis-gageba.html': ('ჩაკეტილი კარის გაღება', 'DoorGO 24/7'),
    'off-track-door-fix.html': ('ჩაკეტილი მანქანის კარის გაღება', 'DoorGO 24/7'),
    'saketis-shecvla-sheketeba.html': ('საკეტის შეცვლა', 'DoorGO 24/7'),
}

for file, (title, eyebrow) in page_titles.items():
    p = root/file
    soup = BeautifulSoup(p.read_text(encoding='utf-8'), 'html.parser')
    main = soup.find('main')
    # Some pages (OurServices) accidentally start content outside main. Make a main if needed.
    if not main:
        main = soup.new_tag('main')
        hdr = soup.find('header')
        # move siblings after header until phone-float/footer into main
        for sib in list(hdr.next_siblings):
            if getattr(sib,'name',None) in ['a','footer','script']:
                break
            main.append(sib.extract())
        hdr.insert_after(main)
    # remove old title/banner/gallery hero at top
    for sec in list(soup.find_all('section')):
        cls = sec.get('class', [])
        if 'page-title' in cls or 'banner-hero' in cls or 'gallery-modern-hero' in cls or 'gallery-hero' in cls:
            # remove only if before first content-ish section or title areas
            sec.decompose()
    # service pages: keep service-top photo but insert clean banner before it
    main.insert(0, banner(soup, title, eyebrow, buttons=(file not in ['AboutUs.html','Contact.html'])))
    # remove text hero cards from Contact/About that were duplicating above banner
    if file == 'Contact.html':
        ch = soup.select_one('.contact-hero-card')
        if ch: ch.decompose()
    if file == 'AboutUs.html':
        # keep actual about content but no extra top page-title already removed
        pass
    # remove title attrs / accidental browser tooltip hints
    for tag in soup.find_all(True):
        if tag.has_attr('title'):
            del tag['title']
    p.write_text(str(soup), encoding='utf-8')

# Fix Gallery layout text and make all captions cleaner / no redundant text
for file in ['Gallery.html','VideoGallery.html']:
    p=root/file
    soup=BeautifulSoup(p.read_text(encoding='utf-8'), 'html.parser')
    head=soup.select_one('.gallery-layout-head')
    if head:
        h2=head.find('h2')
        if h2: h2.string='კარისა და საკეტის ფოტოები'
        # remove mini cta if too cramped? keep but shorter
        a=head.find('a', class_='mini-cta')
        if a: a.string='კონტაქტი'
    for fig in soup.select('figure.real-gallery-card'):
        # keep short labels only
        cap=fig.find('figcaption')
        if cap and cap.find('b'):
            b=cap.find('b')
            # avoid repetitive long descriptors
            txt=b.get_text(strip=True).replace(' და ', ' / ')
            b.string=txt
            for span in cap.find_all('span'): span.decompose()
    p.write_text(str(soup),encoding='utf-8')

# Add body class to all pages for v13 polish
for p in root.glob('*.html'):
    soup=BeautifulSoup(p.read_text(encoding='utf-8'), 'html.parser')
    body=soup.find('body')
    if body:
        cls=body.get('class', [])
        if 'dg-v13' not in cls: cls.append('dg-v13')
        body['class']=cls
    p.write_text(str(soup),encoding='utf-8')
