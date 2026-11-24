from pathlib import Path
from html import escape as e
import json
root=Path(__file__).resolve().parent; sections=[]
for l in (root/'content.txt').read_text().splitlines():
 if not l.strip():continue
 if l.startswith('# '):
  key,fa,en,subfa,suben=l[2:].split('|'); sections.append(dict(id=key,title=[fa,en],subtitle=[subfa,suben],items=[],notes=[]))
 else:
  note=l.startswith('! '); a,b,c,d=l[2:].split('|') if note else l.split('|'); sections[-1]['notes' if note else 'items'].append(dict(title=[a.strip(),b.strip()],body=[c,d]))
(root/'content.json').write_text(json.dumps(sections,ensure_ascii=False,indent=2))
# Native inline SVG icon library, no third-party resources.
icons={
 'target':'<circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5"/><circle cx="12" cy="12" r="1"/>',
 'eye':'<path d="M2 12s3.6-7 10-7 10 7 10 7-3.6 7-10 7S2 12 2 12Z"/><circle cx="12" cy="12" r="3"/>',
 'layers':'<path d="m12 3 10 5-10 5L2 8l10-5Zm-10 9 10 5 10-5M2 16l10 5 10-5"/>',
 'people':'<circle cx="9" cy="8" r="3"/><path d="M2 20v-3a5 5 0 0 1 5-5h4a5 5 0 0 1 5 5v3M16 5a3 3 0 0 1 0 6m2 2a5 5 0 0 1 4 5v2"/>',
 'shield':'<path d="m12 2 8 3v7c0 5-5 9-8 10-3-1-8-5-8-10V5l8-3Z"/><path d="m8 12 3 3 5-6"/>',
 'search':'<circle cx="10.5" cy="10.5" r="6.5"/><path d="m16 16 5 5"/>',
 'filter':'<path d="M3 4h18l-7 8v7l-4 2v-9L3 4Z"/>',
 'file':'<path d="M6 2h8l4 4v16H6zM14 2v5h5M9 12h6m-6 4h6"/>',
 'chart':'<path d="M3 3v18h18M7 16l5-5 4 3 5-8"/><path d="M17 6h4v4"/>',
 'megaphone':'<path d="m3 10 13-5v14L3 14v-4Zm4 5 2 6h4l-2-5M20 9l2-2m-2 6h2m-2 4 2 2"/>',
 'handshake':'<path d="m2 11 5-6 5 2 5-2 5 6-5 6-4 3-5-3-6-6Zm5-6 4 6 3-2 5 5M5 14l3-3m1 6 3-3m1 6 3-3"/>',
 'scale':'<path d="M12 3v18M5 21h14M3 7h18M6 7 2 14h8L6 7Zm12 0-4 7h8l-4-7Z"/>',
 'check':'<circle cx="12" cy="12" r="9"/><path d="m8 12 3 3 5-6"/>',
 'calculator':'<rect x="5" y="2" width="14" height="20" rx="2"/><path d="M8 6h8M8 10h2m4 0h2m-8 4h2m4 0h2m-8 4h2m4 0h2"/>',
 'wallet':'<rect x="3" y="5" width="18" height="15" rx="3"/><path d="M3 8V5l13-3v3m5 6h-6v4h6"/>',
 'lock':'<rect x="4" y="10" width="16" height="11" rx="2"/><path d="M8 10V6a4 4 0 0 1 8 0v4m-4 4v3"/>',
 'route':'<circle cx="5" cy="5" r="2"/><circle cx="19" cy="19" r="2"/><path d="M7 5h9a4 4 0 0 1 0 8H8a3 3 0 0 0 0 6h9"/>',
 'building':'<path d="M3 22h18M5 22V7l8-4v19m0-12h6v12M8 9h2m-2 4h2m-2 4h2m6-3h1m-1 4h1"/>',
 'globe':'<circle cx="12" cy="12" r="9"/><ellipse cx="12" cy="12" rx="4" ry="9"/><path d="M3 12h18M5 7h14M5 17h14"/>',
 'link':'<path d="m10 13 4-4m-6 7-2 2a4 4 0 0 1-6-6l5-5a4 4 0 0 1 6 0m2 10a4 4 0 0 0 6 0l4-4a4 4 0 0 0-6-6l-2 2" transform="translate(1 0) scale(.9)"/>',
 'database':'<ellipse cx="12" cy="5" rx="8" ry="3"/><path d="M4 5v14c0 4 16 4 16 0V5M4 12c0 4 16 4 16 0"/>',
 'leaf':'<path d="M20 3c-9 0-16 5-16 12a5 5 0 0 0 5 5c7 0 11-7 11-17ZM3 21l10-10"/>',
 'drop':'<path d="M12 2C8 8 4 12 4 16a8 8 0 0 0 16 0c0-4-4-8-8-14Z"/>',
 'factory':'<path d="M3 21V10l6-4v6l6-4v4h6v9H3ZM16 12V3h4v9M6 17h2m3 0h2m3 0h2"/>',
 'cpu':'<rect x="5" y="5" width="14" height="14" rx="2"/><rect x="9" y="9" width="6" height="6"/><path d="M9 2v3m6-3v3M9 19v3m6-3v3M2 9h3m-3 6h3m14-6h3m-3 6h3"/>',
 'bulb':'<path d="M9 18h6m-6 3h6M8 15c-1-2-3-3-3-6a7 7 0 0 1 14 0c0 3-2 4-3 6l-1 3H9l-1-3Z"/>',
 'truck':'<path d="M2 5h12v12H2zm12 5h5l3 4v3h-8"/><circle cx="6" cy="19" r="2"/><circle cx="18" cy="19" r="2"/>',
 'wheat':'<path d="M12 22V3m0 6c-5 0-7-3-7-6 5 0 7 3 7 6Zm0 5c5 0 7-3 7-6-5 0-7 3-7 6Zm0 5c-5 0-7-3-7-6 5 0 7 3 7 6Z"/>',
 'heart':'<path d="M12 21 3 12a5 5 0 0 1 9-5 5 5 0 0 1 9 5l-9 9Z"/><path d="M6 12h4l2-3 2 6 2-3h3"/>',
 'compass':'<circle cx="12" cy="12" r="9"/><path d="m16 8-3 5-5 3 3-5 5-3Z"/>',
 'book':'<path d="M12 5C8 2 4 3 2 4v16c3-2 7-2 10 0 3-2 7-2 10 0V4c-2-1-6-2-10 1Zm0 0v15"/>',
 'box':'<path d="m3 7 9-5 9 5v10l-9 5-9-5V7Zm0 0 9 5 9-5m-9 5v10M7 5l10 5"/>',
 'calendar':'<rect x="3" y="5" width="18" height="16" rx="2"/><path d="M7 2v6m10-6v6M3 10h18m-14 5h3m4 0h3"/>',
 'message':'<path d="M3 4h18v13H9l-6 4V4Z"/><path d="M7 9h10m-10 4h6"/>',
 'phone':'<path d="m4 3 4 0 2 5-3 2c2 4 3 5 7 7l2-3 5 2v4C11 24 0 13 4 3Z"/>',
 'pin':'<path d="M12 22S4 14 4 9a8 8 0 0 1 16 0c0 5-8 13-8 13Z"/><circle cx="12" cy="9" r="3"/>',
 'arrow':'<path d="M4 12h16m-6-6 6 6-6 6"/>',
 'menu':'<path d="M4 6h16M4 12h16M4 18h16"/>',
 'info':'<circle cx="12" cy="12" r="9"/><path d="M12 11v6m0-10v1"/>',
 'briefcase':'<rect x="3" y="7" width="18" height="14" rx="2"/><path d="M8 7V3h8v4M3 12l9 3 9-3M12 13v4"/>',
}
def svg(name):return '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.65" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'+icons.get(name,icons['check'])+'</svg>'
iconsets={'overview':'target eye layers people shield','cycle':'search filter file layers megaphone handshake scale check','readiness':'search calculator wallet file lock route','promotion':'target people file megaphone calendar message handshake check shield','facilitation':'scale file building wallet check globe','aftercare':'chart route people link building database','sectors':'leaf drop factory cpu wallet bulb truck wheat heart compass book box','partnership':'handshake file target people wallet database calendar chart','risk':'scale people search shield lock wallet chart info briefcase','engagement':'message file search handshake megaphone check','documents':'file file file wallet chart check'}
shortnav=[('overview','درباره راهبرد','About'),('cycle','خدمات','Services'),('sectors','حوزه‌های فعالیت','Sectors'),('partnership','مدل همکاری','Partnership'),('risk','کنترل ریسک','Governance'),('engagement','آغاز همکاری','Engagement')]
serviceids=['readiness','promotion','facilitation','aftercare']
heroitems=[('شناسایی و آماده‌سازی پروژه','Project identification and preparation','search','readiness'),('ساختاردهی مالی','Financial structuring','chart','cycle'),('تسهیل مجوزها','Permit facilitation','scale','facilitation'),('معرفی سرمایه‌گذار خارجی','Foreign investor introduction','globe','promotion'),('پشتیبانی پس از سرمایه‌گذاری','Post-investment support','handshake','aftercare')]
for lang in (0,1):
 fa=lang==0; tr=lambda a,b:a if fa else b
 title=tr('آژانس تامین مالی و سرمایه‌گذاری راهبرد','RAHBORD INVESTMENT AND FINANCE AGENCY')
 other=tr('en.html','index.html'); current=tr('index.html','en.html'); direction=tr('rtl','ltr'); langcode=tr('fa','en')
 nav=''.join(f'<a href="#{s}">{e(tr(a,b))}</a>' for s,a,b in shortnav)
 hero_links=''.join(f'<a href="#{sid}" class="hero-chip"><span class="tiny-icon">{svg(icon)}</span><span>{e(tr(a,b))}</span></a>' for a,b,icon,sid in heroitems)
 service_nav=''.join(f'<a href="#{s["id"]}"><span class="tiny-icon">{svg(iconsets[s["id"]].split()[0])}</span>{e(s["title"][lang])}<span class="link-arrow">{svg("arrow")}</span></a>' for s in sections if s['id'] in serviceids)
 chunks=[]
 for j,s in enumerate(sections):
  sid=s['id']; items=s['items']; note=s['notes']; iconseq=iconsets[sid].split(); image=f'assets/images/{sid}.webp';
  h=e(s['title'][lang]); sub=e(s['subtitle'][lang]);
  cards=''.join(f'<article class="item {"bullet" if not it["title"][lang] else ""}"><span class="item-icon">{svg(iconseq[k%len(iconseq)])}</span><div>{f"<h3>{e(it["title"][lang])}</h3>" if it["title"][lang] else ""}<p>{e(it["body"][lang])}</p></div></article>' for k,it in enumerate(items))
  notes=''.join(f'<aside class="note">{svg("info")}<div>{f"<h3>{e(n["title"][lang])}</h3>" if n["title"][lang] else ""}<p>{e(n["body"][lang])}</p></div></aside>' for n in note)
  if sid=='documents':
   chunks.append(f'<section class="section documents" id="{sid}"><div class="container"><div class="section-heading"><span class="section-mark"></span><h2>{h}</h2></div><div class="items cols-3">{cards}</div></div></section>');continue
  # Intro band with actual catalog image, followed by full card grid.
  img2=f'<img class="office-small" src="assets/images/office.webp" alt="{tr("فضای اداری آژانس راهبرد","Rahbord agency office")}" loading="lazy">' if sid=='overview' else ''
  if sid=='overview':
   intro=f'<div class="intro-copy"><span class="section-mark"></span><h2>{h}</h2><p class="subtitle">{sub}</p></div><div class="intro-img"><img src="{image}" alt="{h}" loading="lazy">{img2}</div>'
  else:
   intro=f'<div class="intro-copy"><span class="section-mark"></span><h2>{h}</h2>{f"<p class=\"subtitle\">{sub}</p>" if sub else ""}{f"<p class=\"english-label\" lang=\"en\" dir=\"ltr\">{e(s["title"][1])}</p>" if fa and not sub else ""}</div><div class="intro-img"><img src="{image}" alt="{h}" loading="lazy"></div>'
  chunks.append(f'<section class="section section-{sid} {"tint" if j%2 else ""}" id="{sid}"><div class="container"><div class="section-intro {"reverse" if j%2 else ""}">{intro}</div><div class="items {"cols-4" if sid in ("cycle","sectors","partnership") else "cols-3"}">{cards}</div>{notes}</div></section>')
  if sid=='cycle':chunks.append(f'<div class="service-jumps"><div class="container"><div class="service-grid">{service_nav}</div></div></div>')
 address=tr('خیابان ملاصدرا، خیابان شیرازی جنوبی، بلوار برزیل غربی، پلاک ۱۳۴ طبقه ۲ واحد ۴','Mollasadra Street, South Shirazi Street, West Brazil Boulevard, No. 134, 2nd floor, Unit 4')
 contactfields=''.join(f'<div class="contact-field"><span>{tr(a,b)}</span><span class="empty-field">—</span></div>' for a,b in [('همراه','Mobile'),('پست الکترونیکی','Email'),('وب‌سایت','Website'),('شماره مجوز فعالیت','Activity License Number'),('تاریخ اعتبار','Validity Date')])
 html=f'''<!doctype html>
<html lang="{langcode}" dir="{direction}">
<head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="description" content="{e(tr('کاتالوگ معرفی خدمات آژانس تامین مالی و سرمایه‌گذاری راهبرد','Services catalogue of Rahbord Investment and Finance Agency'))}"><title>{e(title)}</title><link rel="stylesheet" href="assets/style.css"><link rel="icon" href="assets/images/logo.webp"><link rel="alternate" hreflang="{tr('en','fa')}" href="{other}"></head>
<body><a class="skip" href="#main">{tr('رفتن به محتوا','Skip to content')}</a>
<header class="header"><div class="container header-inner"><a class="brand" href="{current}" aria-label="{e(title)}"><img src="assets/images/logo.webp" alt=""><span><strong>{tr('آژانس تامین مالی و سرمایه‌گذاری راهبرد','RAHBORD')}</strong><small>{tr('RAHBORD INVESTMENT AND FINANCE AGENCY','INVESTMENT AND FINANCE AGENCY')}</small></span></a><nav id="main-nav" aria-label="{tr('منوی اصلی','Main navigation')}">{nav}</nav><div class="header-actions"><a class="language" href="{other}" lang="{tr('en','fa')}">{svg('globe')} {tr('EN','فارسی')}</a><button class="menu-toggle" aria-controls="main-nav" aria-expanded="false" aria-label="{tr('باز کردن منو','Open menu')}">{svg('menu')}</button></div></div></header>
<main id="main"><section class="hero"><div class="container hero-grid"><div class="hero-content"><div class="eyebrow"><span></span> RAIFA</div><h1>{tr('از فرصت تا سرمایه‌گذاری','From Opportunity to Investment')}</h1><p class="hero-brand">{title}</p><p class="hero-description">{tr('ویژه شرکت‌ها، مؤسسات، هلدینگ‌ها، سازمان‌های عمومی و صاحبان پروژه','For companies, institutions, holding groups, public organizations and project owners')}</p><div class="hero-actions"><a class="btn primary" href="#engagement">{tr('برای آغاز همکاری','Begin cooperation')} {svg('arrow')}</a><a class="btn outline" href="assets/catalog.pdf">{svg('file')}{tr('کاتالوگ معرفی خدمات','Services catalogue')}</a></div></div><div class="hero-visual"><img src="assets/images/hero.webp" alt="{tr('مهره آبی در مسیر هزارتو','Blue chess piece in a maze')}"><div class="hero-image-label"><span class="tiny-icon">{svg('target')}</span>{tr('از فرصت تا سرمایه‌گذاری','From Opportunity to Investment')}</div></div></div><div class="container hero-chips">{hero_links}</div></section>
{''.join(chunks)}
<section class="contact" id="contact"><div class="container"><div class="contact-grid"><div class="contact-copy"><img class="contact-image" src="assets/images/closing.webp" alt="{tr('مهره در هزارتو','Chess piece in maze')}" loading="lazy"><span class="eyebrow">RAIFA</span><h2>{tr('آژانس جذب و توسعه سرمایه‌گذاری راهبرد','Rahbord Investment Attraction and Development Agency')}</h2><p class="tagline">{tr('از فرصت تا سرمایه‌گذاری','From Opportunity to Investment')}</p><h3>{tr('برای آغاز همکاری','To Begin Cooperation')}</h3><p>{tr('یک جلسه تشخیصی، فهرست پروژه‌های اولیه و اسناد پایه کافی است تا مسیر پیشنهادی جذب سرمایه برای سازمان شما طراحی شود.','A diagnostic meeting, an initial project list and basic documents are sufficient to design a proposed investment attraction pathway for your organization.')}</p></div><div class="contact-card"><h2>{tr('اطلاعات تماس','Contact Information')}</h2><div class="address"><span class="item-icon">{svg('pin')}</span><div><strong>{tr('نشانی','Address')}</strong><p>{address}</p></div></div><div class="address"><span class="item-icon">{svg('phone')}</span><div><strong>{tr('تلفن','Telephone')}</strong><p><a href="tel:+982188068694" dir="ltr">{tr('(۰۲۱) ۸۸۰۶۸۶۹۴','(021) 88068694')}</a></p></div></div><div class="contact-fields">{contactfields}</div></div></div></div></section>
</main><footer><div class="container footer-inner"><img src="assets/images/footer-logo.webp" alt="RAIFA"><span>RAHBORD INVESTMENT AGENCY<br><small>RAHBORD INVESTMENT AND FINANCE AGENCY</small></span><a href="#main">{tr('بازگشت به بالا','Back to top')} ↑</a></div></footer><script src="assets/site.js" defer></script></body></html>'''
 (root/current).write_text(html,encoding='utf-8')
print('Sections:',len(sections),'Items:',sum(len(s['items']) for s in sections),'Notes:',sum(len(s['notes']) for s in sections))
