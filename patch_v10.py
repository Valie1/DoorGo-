from bs4 import BeautifulSoup, NavigableString
from pathlib import Path

root=Path('/mnt/data/doorgo_v10')
htmls=list(root.glob('*.html'))
# remove visible dash characters from text nodes only; keep href/src/filenames/classes intact
for p in htmls:
    soup=BeautifulSoup(p.read_text(encoding='utf-8'), 'html.parser')
    for node in soup.find_all(string=True):
        if isinstance(node, NavigableString):
            parent=node.parent.name if node.parent else ''
            if parent in ['script','style']:
                continue
            text=str(node)
            new=text.replace('—',' ').replace('–',' ').replace(' - ',' ').replace(' — ',' ').replace(' – ',' ')
            # Remove standalone hyphen used as separator but not inside code-like identifiers in visible text.
            new=new.replace(' | ', '  ')
            if new!=text:
                node.replace_with(new)
    # better titles for gallery and names without separators
    if p.name=='Gallery.html' or p.name=='VideoGallery.html':
        if soup.title: soup.title.string='გალერია DoorGO'
    p.write_text(str(soup), encoding='utf-8')

# Make Gallery HTML more polished: rewrite header section and gallery captions (keeps images)
p= root/'Gallery.html'
soup=BeautifulSoup(p.read_text(encoding='utf-8'), 'html.parser')
# Remove videos section entirely? User wants gallery and 2 video placeholders earlier; keep but nicer and no explanatory text.
# Add class on body
if soup.body:
    soup.body['class'] = (soup.body.get('class', []) + ['gallery-polished-page'])
# replace gallery section heading for cleaner copy
head=soup.select_one('.gallery-layout-head')
if head:
    head.clear()
    div=soup.new_tag('div')
    sp=soup.new_tag('span', **{'class':'eyebrow'}); sp.string='DoorGO Portfolio'
    h=soup.new_tag('h2'); h.string='რეალური ნამუშევრები'
    div.append(sp); div.append(h)
    ptag=soup.new_tag('p'); ptag.string='სუფთა, თანამედროვე და სწრაფი მომსახურების ვიზუალური მაგალითები.'
    div.append(ptag)
    head.append(div)
    a=soup.new_tag('a', href='tel:597606000', **{'class':'mini-cta'}); a.string='დარეკვა'
    head.append(a)
# change captions to not duplicate too much
captions=['დაცვის ცილინდრი','კარის მექანიზმი','სახელურის დეტალი','ჩაკეტილი კარი','შიდა კარის საკეტი','მეტალის საკეტი','ცილინდრის ახლო ხედი','დაზიანებული მექანიზმი','ძველი საკეტი']
for fig,cap in zip(soup.select('.real-gallery-card'),captions):
    fc=fig.find('figcaption') or soup.new_tag('figcaption')
    fc.clear()
    b=soup.new_tag('b'); b.string=cap
    fc.append(b)
    if not fig.find('figcaption'): fig.append(fc)
# replace hero copy
hero=soup.select_one('.gallery-modern-hero .gallery-hero-inner')
if hero:
    hero.clear()
    sp=soup.new_tag('span', **{'class':'eyebrow'}); sp.string='DoorGO Gallery'
    h=soup.new_tag('h1'); h.string='გალერია'
    par=soup.new_tag('p'); par.string='კარის გაღების, საკეტის შეცვლის და კარის მექანიზმების რეალური ფოტოები.'
    actions=soup.new_tag('div', **{'class':'gallery-hero-actions'})
    a1=soup.new_tag('a', href='tel:597606000', **{'class':'btn'}); a1.string='დარეკვა'
    a2=soup.new_tag('a', href='OurServices.html', **{'class':'btn white'}); a2.string='სერვისები'
    actions.append(a1); actions.append(a2)
    hero.append(sp); hero.append(h); hero.append(par); hero.append(actions)
# Remove remaining text dash again
for node in soup.find_all(string=True):
    if node.parent and node.parent.name not in ['script','style']:
        node.replace_with(str(node).replace('—',' ').replace('–',' ').replace(' - ',' '))
p.write_text(str(soup), encoding='utf-8')
# VideoGallery duplicate same as Gallery
(root/'VideoGallery.html').write_text((root/'Gallery.html').read_text(encoding='utf-8'), encoding='utf-8')
