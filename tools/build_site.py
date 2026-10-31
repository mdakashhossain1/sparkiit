import json, os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCR = os.path.dirname(os.path.abspath(__file__))

sprite = open(os.path.join(ROOT, 'assets', 'sprite.txt'), encoding='utf-8').read()
tpl = open(os.path.join(SCR, 'site.tpl.js'), encoding='utf-8').read()
open(os.path.join(ROOT, 'assets', 'site.js'), 'w', encoding='utf-8').write(tpl.replace("'%%SPRITE%%'", json.dumps(sprite)))

APPLY = 'https://evolvix.tech'
ARROW = '<svg class="icon w-4 h-4"><use href="#i-arrow"/></svg>'
EXT = '<svg class="icon w-4 h-4"><use href="#i-external"/></svg>'
CHECK = '<svg class="icon w-4 h-4 text-brand-600 mt-1"><use href="#i-check"/></svg>'
INPUT = 'mt-1.5 w-full h-11 rounded-lg border border-line bg-white px-3.5 text-sm text-ink placeholder:text-slate-400 outline-none focus:border-brand-500 focus:ring-4 focus:ring-brand-100 transition'
TEXTAREA = 'mt-1.5 w-full rounded-lg border border-line bg-white px-3.5 py-3 text-sm text-ink placeholder:text-slate-400 outline-none focus:border-brand-500 focus:ring-4 focus:ring-brand-100 transition'

def T(s):
    return (s.replace('__APPLY__', APPLY).replace('__ARROW__', ARROW).replace('__EXT__', EXT)
             .replace('__CHECK__', CHECK).replace('__INPUT__', INPUT).replace('__TEXTAREA__', TEXTAREA))

HEAD = '''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>%(title)s | SparkIIT</title>
<meta name="description" content="%(desc)s">
<meta name="theme-color" content="#1F57F0">
<meta property="og:type" content="website">
<meta property="og:site_name" content="SparkIIT">
<meta property="og:title" content="%(title)s | SparkIIT">
<meta property="og:description" content="%(desc)s">
<meta name="twitter:card" content="summary">
<script>document.documentElement.classList.add('js')</script>
<link rel="icon" type="image/svg+xml" href="logo-mark.svg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,300;0,400;0,500;0,600;0,700;1,500&display=swap" rel="stylesheet">
%(swcss)s<link rel="stylesheet" href="assets/styles.css">
</head>
<body>
<div id="site-header"></div>
<main id="main">
'''
TAIL = '''
</main>
<div id="site-footer"></div>
%(swjs)s<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js"></script>
<script defer src="https://cdn.jsdelivr.net/npm/@alpinejs/collapse@3.14.1/dist/cdn.min.js"></script>
<script defer src="https://cdn.jsdelivr.net/npm/alpinejs@3.14.1/dist/cdn.min.js"></script>
<script src="assets/config.js"></script>
<script src="assets/programs-data.js"></script>
<script src="assets/site.js"></script>
%(script)s
<script>SITE.anim();</script>
</body>
</html>
'''
SWCSS = '<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swiper@11.1.14/swiper-bundle.min.css">\n'
SWJS = '<script src="https://cdn.jsdelivr.net/npm/swiper@11.1.14/swiper-bundle.min.js"></script>\n'


def page(name, title, desc, body, script='', swiper=False):
    html = HEAD % {'title': title, 'desc': desc, 'swcss': SWCSS if swiper else ''} + T(body) + TAIL % {'script': script, 'swjs': SWJS if swiper else ''}
    open(os.path.join(ROOT, name), 'w', encoding='utf-8').write(html)


def hero(crumb, title, desc, extra=''):
    return '''<section class="relative overflow-hidden border-b border-line">
  <div class="grid-bg absolute inset-0 pointer-events-none"></div>
  <div class="orb w-96 h-96 bg-brand-200/50 -top-32 -left-24"></div>
  <div class="relative container-x pt-14 pb-14 md:pt-20 md:pb-20">
    <nav class="text-xs text-mute flex items-center gap-2" aria-label="Breadcrumb"><a href="index.html" class="hover:text-ink">Home</a><span aria-hidden="true">/</span><span class="text-ink" aria-current="page">''' + crumb + '''</span></nav>
    <h1 data-anim class="h1 mt-6 max-w-3xl">''' + title + '''</h1>
    <p data-anim class="lead mt-5">''' + desc + '''</p>
    ''' + extra + '''
  </div>
</section>'''


def cta(title='Ready to start learning?', desc='Choose a program, apply in minutes and begin with live mentors and real projects.'):
    return '''<section class="section pt-0 md:pt-0">
  <div class="container-x">
    <div data-anim class="relative overflow-hidden rounded-3xl bg-brand-900 text-white px-6 py-14 md:px-16 md:py-20 text-center">
      <svg class="absolute -right-24 -top-24 w-[28rem] h-[28rem] text-white/10 pointer-events-none" viewBox="0 0 400 400" fill="none" stroke="currentColor" aria-hidden="true"><circle cx="200" cy="200" r="60"/><circle cx="200" cy="200" r="110"/><circle cx="200" cy="200" r="160"/><circle cx="200" cy="200" r="195"/></svg>
      <div class="relative"><h2 class="h2 max-w-2xl mx-auto">''' + title + '''</h2>
      <p class="mt-4 text-white/75 max-w-lg mx-auto">''' + desc + '''</p>
      <div class="mt-9 flex flex-wrap justify-center gap-3"><a href="__APPLY__" target="_blank" rel="noopener noreferrer" class="btn btn-light">Apply now __EXT__</a><a href="programs.html" class="btn btn-ghost-light">Browse programs</a></div></div>
    </div>
  </div>
</section>'''


def icon_row(icon, title, text):
    return '<div data-anim class="flex gap-4"><div class="icon-tile flex-none"><svg class="icon"><use href="#i-' + icon + '"/></svg></div><div><h3 class="font-medium">' + title + '</h3><p class="mt-1.5 text-sm text-mute">' + text + '</p></div></div>'


def field(kind, label, name, ph='', options=None, required=True):
    if kind == 'select':
        opts = ''.join('<option>' + o + '</option>' for o in options)
        return '<label class="text-sm"><span class="font-medium">' + label + '</span><select name="' + name + '" class="__INPUT__">' + opts + '</select></label>'
    if kind == 'textarea':
        return '<label class="text-sm"><span class="font-medium">' + label + '</span><textarea name="' + name + '" rows="4" class="__TEXTAREA__" placeholder="' + ph + '"></textarea></label>'
    ac = {'email': 'email', 'tel': 'tel', 'text': 'name'}.get(kind, 'off')
    return '<label class="text-sm"><span class="font-medium">' + label + '</span><input ' + ('required ' if required else '') + 'name="' + name + '" type="' + kind + '" autocomplete="' + ac + '" class="__INPUT__" placeholder="' + ph + '"></label>'


def form(rows, button, subject='Website enquiry'):
    inner = ''
    for r in rows:
        if isinstance(r, list):
            inner += '<div class="grid sm:grid-cols-2 gap-4">' + ''.join(r) + '</div>'
        else:
            inner += r
    return '''<div x-data="{ sent: false }">
  <form x-show="!sent" data-subject="''' + subject + '''" @submit.prevent="SITE.sendMail($event.target); sent = true" class="card p-6 md:p-8 grid gap-5 shadow-soft">''' + inner + '''
    <button type="submit" class="btn btn-primary">''' + button + ''' __ARROW__</button>
  </form>
  <div x-show="sent" x-cloak class="card p-10 text-center shadow-soft"><div class="w-12 h-12 rounded-full bg-brand-50 text-brand-600 grid place-items-center mx-auto"><svg class="icon w-6 h-6"><use href="#i-check"/></svg></div><h2 class="mt-5 font-serif text-3xl">Thank you.</h2><p class="mt-2 text-sm text-mute">We have noted your details and will reach out shortly.</p></div>
</div>'''


PROGRAM_OPTS = ['Software Development', 'Data and AI', 'Cloud and DevOps', 'Cyber Security', 'Design', 'Engineering', 'Business and Management', 'Healthcare and Life Sciences', 'Not sure yet']

# ------------------------------------------------------------------ contact
contact = hero('Contact', 'Let us help you choose the right program.', 'Tell us where you are today and where you want to be. Our team will get back to you with a clear plan.') + '''
<section class="section">
  <div class="container-x grid lg:grid-cols-12 gap-10 lg:gap-14">
    <div class="lg:col-span-7" data-anim>
      ''' + form([[field('text', 'Full name', 'name', 'Your name'), field('tel', 'Phone', 'phone', '+91')], field('email', 'Email', 'email', 'you@example.com'), field('select', 'Interested in', 'interest', options=PROGRAM_OPTS), field('select', 'Current status', 'status', options=['Student', 'Recent graduate', 'Working professional', 'Career switcher']), field('textarea', 'Message', 'message', 'Anything we should know?')], 'Send message', 'Website enquiry') + '''
    </div>
    <div class="lg:col-span-5 space-y-5">
      <div data-anim class="card overflow-hidden shadow-soft">
        <img src="https://images.unsplash.com/photo-1553877522-43269d4ea984?auto=format&fit=crop&w=900&q=70" alt="Learners at work in a bright room" class="w-full h-48 object-cover" loading="lazy">
        <div class="p-7"><h2 class="text-xl font-medium">Ready to apply?</h2><p class="mt-2 text-sm text-mute">Skip the wait and submit your application directly.</p><a href="__APPLY__" target="_blank" rel="noopener noreferrer" class="btn btn-primary mt-6">Apply now __EXT__</a></div>
      </div>
      <ul id="contactInfo" class="space-y-4 text-sm text-slate-600"></ul>
    </div>
  </div>
</section>''' + cta()
contact_js = '''<script>
(function () {
  var c = SITE.config, rows = '';
  if (c.address) rows += '<li class="flex gap-3">' + SITE.icon('pin', 'w-4 h-4 mt-1 text-brand-600') + '<span>' + c.address + '</span></li>';
  if (c.phone) rows += '<li class="flex gap-3">' + SITE.icon('phone', 'w-4 h-4 mt-1 text-brand-600') + '<a href="tel:' + c.phone.replace(/\\s+/g, '') + '" class="hover:text-ink">' + c.phone + '</a></li>';
  if (c.email) rows += '<li class="flex gap-3">' + SITE.icon('mail', 'w-4 h-4 mt-1 text-brand-600') + '<a href="mailto:' + c.email + '" class="hover:text-ink">' + c.email + '</a></li>';
  var el = document.getElementById('contactInfo');
  if (rows) el.innerHTML = rows; else el.remove();
})();
</script>'''
page('contact.html', 'Contact', 'Talk to the SparkIIT team about programs, batches and how to apply.', contact, contact_js)

# ------------------------------------------------------------------ about
slide = lambda img, t, d: ('<div class="swiper-slide !h-auto"><div class="card card-hover p-5 h-full"><img src="https://images.unsplash.com/photo-' + img +
                           '?auto=format&fit=crop&w=800&q=70" alt="" class="w-full h-44 object-cover rounded-xl" loading="lazy"><h3 class="mt-5 font-medium">' + t + '</h3><p class="mt-2 text-sm text-mute">' + d + '</p></div></div>')
teach = ''.join([
    slide('1531482615713-2afd69097998', 'Live sessions', 'Ask questions in the moment and learn from classmates.'),
    slide('1517694712202-14dd9538aa97', 'Hands-on practice', 'Apply every topic through guided exercises and projects.'),
    slide('1521737711867-e3b97375f902', 'Career support', 'Resume reviews, mock interviews and guidance on applying.'),
    slide('1519389950473-47ba0277781c', 'Peer learning', 'Study with a cohort that keeps you moving.'),
    slide('1498050108023-c5249f4df085', 'Mentor feedback', 'Get feedback on your work from practitioners.'),
])
arrows = ('<div class="flex gap-2"><button id="aPrev" class="w-11 h-11 rounded-full border border-line bg-white grid place-items-center hover:border-brand-300 hover:text-brand-600 active:scale-95 transition" aria-label="Previous"><svg class="icon w-4 h-4 rotate-180"><use href="#i-chevron"/></svg></button>'
          '<button id="aNext" class="w-11 h-11 rounded-full border border-line bg-white grid place-items-center hover:border-brand-300 hover:text-brand-600 active:scale-95 transition" aria-label="Next"><svg class="icon w-4 h-4"><use href="#i-chevron"/></svg></button></div>')
about = hero('About', 'We help learners become job-ready.', 'SparkIIT pairs live mentors with practical projects and certification, so what you learn is what employers ask for.') + '''
<section class="section">
  <div class="container-x grid lg:grid-cols-12 gap-12 lg:gap-16 items-center">
    <div class="lg:col-span-6" data-anim>
      <div class="grid grid-cols-5 grid-rows-2 gap-3 h-[26rem]">
        <img src="https://images.unsplash.com/photo-1522202176988-66273c2fd55f?auto=format&fit=crop&w=800&q=70" alt="Students collaborating" class="col-span-3 row-span-2 w-full h-full object-cover rounded-2xl" loading="lazy">
        <img src="https://images.unsplash.com/photo-1531482615713-2afd69097998?auto=format&fit=crop&w=600&q=70" alt="Mentor and learner" class="col-span-2 w-full h-full object-cover rounded-2xl" loading="lazy">
        <img src="https://images.unsplash.com/photo-1498050108023-c5249f4df085?auto=format&fit=crop&w=600&q=70" alt="Laptop showing code" class="col-span-2 w-full h-full object-cover rounded-2xl" loading="lazy">
      </div>
    </div>
    <div class="lg:col-span-6">
      <h2 data-anim class="h2">Learning should lead somewhere.</h2>
      <p data-anim class="mt-6 text-slate-600">Too many courses end with a certificate and no clear next step. We built SparkIIT around that next step: live sessions with practitioners, structured syllabi across technology, engineering and business, and support as you apply what you learn.</p>
      <p data-anim class="mt-4 text-slate-600">Every program has a published syllabus and a downloadable brochure, so you know what you will cover before you begin.</p>
      <div data-anim class="mt-8 flex flex-wrap gap-3"><a href="programs.html" class="btn btn-primary">Browse programs __ARROW__</a><a href="__APPLY__" target="_blank" rel="noopener noreferrer" class="btn btn-outline">Apply now __EXT__</a></div>
    </div>
  </div>
</section>
<section class="section bg-slate-50/70 border-y border-line">
  <div class="container-x">
    <h2 data-anim class="h2 max-w-2xl">Four principles behind every program.</h2>
    <div class="mt-14 grid sm:grid-cols-2 gap-x-14 gap-y-10 max-w-4xl">
      ''' + icon_row('target', 'Outcome first', 'Every module exists to move you closer to a job or a better role.') + icon_row('users', 'Mentors who practise', 'Learn from people who work with these tools every day.') + icon_row('layers', 'Build early, build often', 'Projects and exercises come early, not as an afterthought.') + icon_row('shield', 'Honest guidance', 'We tell you what a role really needs, and what it takes to get there.') + '''
    </div>
  </div>
</section>
<section class="section overflow-hidden">
  <div class="container-x">
    <div class="flex items-end justify-between gap-6"><h2 data-anim class="h2">How we teach</h2>''' + arrows + '''</div>
    <div class="swiper mt-12 !overflow-hidden" id="teachSwiper"><div class="swiper-wrapper">''' + teach + '''</div></div>
    <div class="swiper-pagination !relative !mt-8 teach-pag"></div>
  </div>
</section>''' + cta()
about_js = "<script>new Swiper('#teachSwiper', { slidesPerView: 1.1, spaceBetween: 16, grabCursor: true, navigation: { prevEl: '#aPrev', nextEl: '#aNext' }, pagination: { el: '.teach-pag', clickable: true, dynamicBullets: true }, breakpoints: { 640: { slidesPerView: 2.1 }, 1024: { slidesPerView: 3 } } });</script>"
page('about.html', 'About', 'About SparkIIT: mentor-led programs and certification that make you job-ready.', about, about_js, True)

# ------------------------------------------------------------------ programs
programs = hero('Programs', 'Explore our programs.', 'Browse every program, compare syllabi and download the brochure. Apply when you are ready.') + '''
<section class="section pt-12 md:pt-16">
  <div class="container-x">
    <div class="flex flex-col lg:flex-row lg:items-center gap-5 justify-between">
      <label class="relative lg:w-80 block"><span class="sr-only">Search programs</span><svg class="icon w-4 h-4 absolute left-4 top-1/2 -translate-y-1/2 text-slate-400"><use href="#i-search"/></svg><input id="q" type="search" placeholder="Search programs" class="w-full h-11 rounded-full border border-line bg-white pl-11 pr-4 text-sm placeholder:text-slate-400 outline-none focus:border-brand-500 focus:ring-4 focus:ring-brand-100 transition"></label>
      <div id="cats" class="flex gap-2 overflow-x-auto no-scrollbar -mx-5 px-5 lg:mx-0 lg:px-0" role="tablist" aria-label="Program categories"></div>
    </div>
    <p id="count" class="mt-10 text-sm text-mute" aria-live="polite"></p>
    <div id="grid" class="mt-4 grid sm:grid-cols-2 lg:grid-cols-3 gap-6"></div>
    <div id="empty" class="hidden card p-14 text-center text-mute">No programs match your search. Try a different keyword.</div>
  </div>
</section>''' + cta('Cannot find what you need?', 'Tell us your goal and we will suggest the right program.')
programs_js = '''<script>
(function () {
  var cat = 'All', q = '';
  var cats = ['All'].concat(SITE.cats);
  var box = document.getElementById('cats');
  cats.forEach(function (c) {
    var b = document.createElement('button');
    b.dataset.c = c; b.textContent = c; b.setAttribute('role', 'tab');
    b.addEventListener('click', function () { cat = c; render(); });
    box.appendChild(b);
  });
  function render() {
    box.querySelectorAll('button').forEach(function (b) {
      var on = b.dataset.c === cat;
      b.setAttribute('aria-selected', on);
      b.className = 'whitespace-nowrap px-4 py-2 rounded-full text-sm border transition-colors ' + (on ? 'tab-active border-brand-200' : 'border-line bg-white text-slate-600 hover:border-slate-300');
    });
    var list = SITE.courses.filter(function (c) { return (cat === 'All' || c.cat === cat) && (c.name + ' ' + c.d).toLowerCase().indexOf(q) > -1; });
    document.getElementById('grid').innerHTML = list.map(function (c) { return '<div>' + SITE.card(c) + '</div>'; }).join('');
    document.getElementById('count').textContent = list.length + (list.length === 1 ? ' program' : ' programs');
    document.getElementById('empty').classList.toggle('hidden', list.length > 0);
  }
  document.getElementById('q').addEventListener('input', function (e) { q = e.target.value.trim().toLowerCase(); render(); });
  render();
})();
</script>'''
page('programs.html', 'Programs', 'Browse SparkIIT programs in software, data, cloud, security, design, engineering and business.', programs, programs_js)

# ------------------------------------------------------------------ program detail
program = '<div id="prog"></div>'
program_js = r'''<script>
(function () {
  var esc = function (s) { return String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;'); };
  var p = new URLSearchParams(location.search).get('p');
  var c = SITE.courses.filter(function (x) { return x.slug === p; })[0] || SITE.courses[0];
  document.title = c.name + ' | SparkIIT';
  var meta = document.querySelector('meta[name="description"]');
  if (meta) meta.setAttribute('content', c.name + ' at SparkIIT: syllabus, tools and brochure. ' + c.d);
  var pdf = 'pdf/' + encodeURIComponent(c.pdf);
  var related = SITE.courses.filter(function (x) { return x.cat === c.cat && x.slug !== c.slug; });
  if (related.length < 3) related = related.concat(SITE.courses.filter(function (x) { return x.cat !== c.cat && x.slug !== c.slug; }).slice(0, 3 - related.length));
  related = related.slice(0, 6);

  var tools = c.tools.length ? c.tools.map(function (t) { return '<span class="inline-flex items-center gap-2.5 bg-white border border-line rounded-xl px-4 py-2.5 text-sm"><img src="' + SITE.dv(t[0], t[1]) + '" alt="" class="w-6 h-6">' + esc(SITE.toolName(t[0])) + '</span>'; }).join('') : '';
  var highlights = [['target', 'Industry-focused skills', 'Learn the tools and methods employers ask for, taught step by step.'], ['award', 'Certification', 'Finish the program and earn a certificate you can share with employers.'], ['layers', 'Hands-on practice', 'Practise each topic through guided exercises and projects.']];

  var modTabs = c.mods.map(function (m, i) {
    return '<button type="button" @click="m = ' + i + '" :aria-current="m === ' + i + '" :class="m === ' + i + ' ? \'bg-brand-50 text-brand-700 border-brand-200 font-medium\' : \'bg-white text-slate-600 border-line hover:border-slate-300\'" class="w-64 shrink-0 lg:w-full text-left flex items-start gap-3 px-4 py-3 rounded-xl border text-sm transition-colors"><span class="text-xs w-6 flex-none pt-0.5" :class="m === ' + i + ' ? \'text-brand-600\' : \'text-slate-400\'">' + (i < 9 ? '0' : '') + (i + 1) + '</span><span>' + esc(m.t) + '</span></button>';
  }).join('');
  var modPanels = c.mods.map(function (m, i) {
    var items = m.items.length ? '<ul class="grid sm:grid-cols-2 gap-x-8 gap-y-3.5">' + m.items.map(function (t) { return '<li class="flex gap-3 text-sm text-slate-600"><svg class="icon w-4 h-4 text-brand-600 mt-0.5"><use href="#i-check"/></svg><span>' + esc(t) + '</span></li>'; }).join('') + '</ul>' : '<p class="text-sm text-mute">Topics for this module are listed in the brochure.</p>';
    return '<div x-show="m === ' + i + '" x-cloak x-transition.opacity.duration.200ms><p class="text-xs text-brand-600 font-medium">Module ' + (i + 1) + ' of ' + c.mods.length + '</p><h3 class="mt-2 text-xl md:text-2xl font-medium leading-snug">' + esc(m.t) + '</h3><div class="mt-7">' + items + '</div></div>';
  }).join('');

  var dl = function (cls) { return '<a href="' + pdf + '" download class="btn btn-outline ' + cls + '">' + SITE.icon('download', 'w-4 h-4') + 'Download brochure</a>'; };

  var html = '' +
  '<section class="relative overflow-hidden border-b border-line"><div class="grid-bg absolute inset-0 pointer-events-none"></div><div class="orb w-96 h-96 bg-brand-200/50 -top-32 -left-24"></div>' +
  '<div class="relative container-x pt-12 pb-14 md:pt-16 md:pb-20 grid lg:grid-cols-12 gap-12 items-center"><div class="lg:col-span-7">' +
  '<nav class="text-xs text-mute flex flex-wrap items-center gap-2" aria-label="Breadcrumb"><a href="index.html" class="hover:text-ink">Home</a><span aria-hidden="true">/</span><a href="programs.html" class="hover:text-ink">Programs</a><span aria-hidden="true">/</span><span class="text-ink" aria-current="page">' + esc(c.name) + '</span></nav>' +
  '<h1 data-anim class="h1 mt-6">' + esc(c.name) + '</h1>' +
  '<p data-anim class="lead mt-5">' + esc(c.d) + '</p>' +
  '<ul data-anim class="mt-7 flex flex-wrap gap-2.5"><li class="pill">' + SITE.icon('layers', 'w-3.5 h-3.5 text-brand-600') + esc(c.cat) + '</li><li class="pill">' + SITE.icon('video', 'w-3.5 h-3.5 text-brand-600') + 'Live online sessions</li><li class="pill">' + SITE.icon('file', 'w-3.5 h-3.5 text-brand-600') + c.mods.length + ' modules</li><li class="pill">' + SITE.icon('award', 'w-3.5 h-3.5 text-brand-600') + 'Certificate</li></ul>' +
  '<div data-anim class="mt-9 flex flex-wrap gap-3">' + SITE.applyBtn('') + dl('') + '</div></div>' +
  '<div class="lg:col-span-5" data-anim><div class="relative"><div class="absolute -inset-3 rounded-3xl bg-brand-50 rotate-2"></div><img src="' + SITE.img(c.img, 1000) + '" alt="" class="relative w-full aspect-[4/3] object-cover rounded-2xl shadow-lift"></div></div></div></section>' +

  '<section class="section"><div class="container-x"><h2 class="h2 max-w-2xl">Built to make you job-ready.</h2><p class="lead mt-5">Designed for students, professionals and career switchers who want practical skills and proof of what they can do.</p><div class="mt-14 grid md:grid-cols-3 gap-10">' + highlights.map(function (h) { return '<div data-anim class="flex gap-4"><div class="icon-tile flex-none">' + SITE.icon(h[0]) + '</div><div><h3 class="font-medium">' + h[1] + '</h3><p class="mt-1.5 text-sm text-mute">' + h[2] + '</p></div></div>'; }).join('') + '</div></div></section>' +

  '<section id="syllabus" class="section bg-slate-50/70 border-y border-line"><div class="container-x"><div class="flex flex-wrap items-end justify-between gap-6"><h2 class="h2">What you will learn</h2>' + dl('btn-sm') + '</div>' +
  '<div class="mt-12 grid grid-cols-1 lg:grid-cols-12 gap-6" x-data="{ m: 0 }"><div class="lg:col-span-4 min-w-0"><div class="flex lg:grid gap-2 overflow-x-auto lg:overflow-x-visible lg:sticky lg:top-24 lg:max-h-[34rem] lg:overflow-y-auto no-scrollbar -mx-5 px-5 lg:mx-0 lg:px-0 pb-1">' + modTabs + '</div></div><div class="lg:col-span-8 min-w-0"><div class="card p-7 md:p-10 min-h-[22rem] shadow-soft">' + modPanels + '</div></div></div>' +
  (tools ? '<h3 class="mt-14 font-medium">Tools you will use</h3><div class="mt-5 flex flex-wrap gap-3">' + tools + '</div>' : '') + '</div></section>' +

  '<section id="enquire" class="section scroll-mt-24"><div class="container-x grid lg:grid-cols-12 gap-12 items-center"><div class="lg:col-span-5"><h2 class="h2">Enroll in ' + esc(c.name) + '.</h2><p class="lead mt-5">Share your details and we will send the batch dates, fees and joining steps. Or apply directly.</p><div class="mt-8 flex flex-wrap gap-3">' + SITE.applyBtn('') + dl('') + '</div></div>' +
  '<div class="lg:col-span-7" x-data="{ sent: false }"><form x-show="!sent" data-subject="Enquiry: ' + esc(c.name) + '" @submit.prevent="SITE.sendMail($event.target); sent = true" class="card p-7 md:p-9 grid gap-5 shadow-soft"><div class="grid sm:grid-cols-2 gap-4"><label class="text-sm"><span class="font-medium">Full name</span><input required name="name" type="text" autocomplete="name" class="__INPUT__" placeholder="Your name"></label><label class="text-sm"><span class="font-medium">Phone</span><input required name="phone" type="tel" autocomplete="tel" class="__INPUT__" placeholder="+91"></label></div><label class="text-sm"><span class="font-medium">Email</span><input required name="email" type="email" autocomplete="email" class="__INPUT__" placeholder="you@example.com"></label><button type="submit" class="btn btn-primary">Request details ' + SITE.icon('arrow', 'w-4 h-4') + '</button></form>' +
  '<div x-show="sent" x-cloak class="card p-10 text-center shadow-soft"><div class="w-12 h-12 rounded-full bg-brand-50 text-brand-600 grid place-items-center mx-auto">' + SITE.icon('check', 'w-6 h-6') + '</div><h3 class="mt-5 font-serif text-3xl">Thank you.</h3><p class="mt-2 text-sm text-mute">We will reach out shortly.</p></div></div></div></section>' +

  (related.length ? '<section class="section bg-slate-50/70 border-t border-line overflow-hidden"><div class="container-x"><h2 class="h2">Related programs</h2><div class="swiper mt-12 !overflow-hidden" id="relSwiper"><div class="swiper-wrapper">' + related.map(function (r) { return '<div class="swiper-slide !h-auto">' + SITE.card(r) + '</div>'; }).join('') + '</div></div><div class="swiper-pagination !relative !mt-8 rel-pag"></div></div></section>' : '') +

  '<div class="lg:hidden fixed bottom-0 inset-x-0 z-30 border-t border-line bg-white/95 backdrop-blur px-5 py-3 flex items-center gap-3"><div class="min-w-0 flex-1"><div class="text-sm font-medium truncate">' + esc(c.name) + '</div><div class="text-xs text-mute">' + c.mods.length + ' modules</div></div>' + SITE.applyBtn('btn-sm') + '</div>';

  document.getElementById('prog').innerHTML = html;
  document.body.style.paddingBottom = window.innerWidth < 1024 ? '4.5rem' : '';
  if (related.length) new Swiper('#relSwiper', { slidesPerView: 1.1, spaceBetween: 16, grabCursor: true, pagination: { el: '.rel-pag', clickable: true, dynamicBullets: true }, breakpoints: { 640: { slidesPerView: 2.1 }, 1024: { slidesPerView: 3 } } });
})();
</script>'''
page('program.html', 'Program', 'SparkIIT program details: syllabus, tools and brochure.', program, program_js.replace('__INPUT__', INPUT), True)

# ------------------------------------------------------------------ career pass
step = lambda i, t, d: ('<li data-anim class="flex gap-5"><span class="w-9 h-9 rounded-full bg-brand-600 text-white grid place-items-center text-sm font-medium flex-none">' + str(i) + '</span><div><h3 class="font-medium">' + t + '</h3><p class="mt-1.5 text-sm text-mute">' + d + '</p></div></li>')
tracks = [('code', 'Software Development'), ('chart', 'Data and AI'), ('cloud', 'Cloud and DevOps'), ('shield', 'Cyber Security'), ('palette', 'Design'), ('layers', 'Engineering'), ('briefcase', 'Business and Management'), ('users', 'Healthcare and Life Sciences')]
track_slides = ''.join('<div class="swiper-slide !w-64"><a href="programs.html" class="card card-hover p-6 block h-full"><div class="icon-tile"><svg class="icon"><use href="#i-' + ic + '"/></svg></div><h3 class="mt-8 font-medium">' + t + '</h3><span class="mt-3 inline-flex items-center gap-1.5 text-sm text-brand-600">View programs ' + ARROW + '</span></a></div>' for ic, t in tracks)
career = '''<section class="relative overflow-hidden bg-brand-900 text-white">
  <svg class="absolute -right-24 -top-24 w-[34rem] h-[34rem] text-white/10 pointer-events-none" viewBox="0 0 400 400" fill="none" stroke="currentColor" aria-hidden="true"><circle cx="200" cy="200" r="60"/><circle cx="200" cy="200" r="110"/><circle cx="200" cy="200" r="160"/><circle cx="200" cy="200" r="195"/></svg>
  <div class="relative container-x pt-16 pb-16 md:pt-24 md:pb-24 grid lg:grid-cols-12 gap-12 items-center">
    <div class="lg:col-span-7">
      <nav class="text-xs text-white/60 flex items-center gap-2" aria-label="Breadcrumb"><a href="index.html" class="hover:text-white">Home</a><span aria-hidden="true">/</span><span class="text-white" aria-current="page">Career Pass</span></nav>
      <h1 data-anim class="h1 mt-6">One pass to become a leader in the tech industry.</h1>
      <p data-anim class="mt-6 text-lg text-white/75 max-w-xl">Learn across multiple domains, add business fundamentals and get dedicated support as you move into your next role.</p>
      <div data-anim class="mt-9 flex flex-wrap gap-3"><a href="__APPLY__" target="_blank" rel="noopener noreferrer" class="btn btn-light">Get the Career Pass __EXT__</a><a href="programs.html" class="btn btn-ghost-light">Browse programs</a></div>
    </div>
    <div class="lg:col-span-5" data-anim><img src="https://images.unsplash.com/photo-1519389950473-47ba0277781c?auto=format&fit=crop&w=1000&q=70" alt="Colleagues collaborating at laptops" class="w-full h-80 object-cover rounded-2xl border border-white/15"></div>
  </div>
</section>
<section class="section">
  <div class="container-x">
    <h2 data-anim class="h2 max-w-2xl">Everything you need in one place.</h2>
    <div class="mt-14 grid md:grid-cols-3 gap-10">''' + icon_row('code', 'Multiple domains', 'Learn more than one domain and keep your options open.') + icon_row('briefcase', 'Business skills', 'Management fundamentals for people moving into leadership.') + icon_row('users', 'Dedicated support', 'Guidance on your resume, interviews and next steps.') + '''</div>
  </div>
</section>
<section class="section bg-slate-50/70 border-y border-line">
  <div class="container-x grid lg:grid-cols-12 gap-14">
    <div class="lg:col-span-4"><h2 data-anim class="h2">How it works</h2><p data-anim class="lead mt-5">Four simple stages from enrolment to your next role.</p></div>
    <ol class="lg:col-span-8 grid sm:grid-cols-2 gap-x-12 gap-y-10">''' + step(1, 'Pick your domains', 'Choose from several tracks that match your goals.') + step(2, 'Learn and practise', 'Join live sessions and work through hands-on exercises.') + step(3, 'Add business skills', 'Build the management fundamentals leaders rely on.') + step(4, 'Move forward', 'Get guidance as you apply for your next opportunity.') + '''</ol>
  </div>
</section>
<section class="section overflow-hidden">
  <div class="container-x"><h2 data-anim class="h2">Tracks you can choose from</h2></div>
  <div class="edge-fade mt-12 overflow-hidden"><div class="swiper !overflow-visible container-x" id="trackSwiper"><div class="swiper-wrapper">''' + track_slides + '''</div></div></div>
</section>''' + cta('Ready for the Career Pass?', 'Apply today and talk to our team about dates and which domains suit you.')
career_js = "<script>new Swiper('#trackSwiper', { slidesPerView: 'auto', spaceBetween: 16, grabCursor: true, freeMode: true });</script>"
page('career-pass.html', 'Career Pass', 'The SparkIIT Career Pass: multiple domains, business skills and dedicated support.', career, career_js, True)

# ------------------------------------------------------------------ verify certificate
verify = hero('Verify certificate', 'Verify a SparkIIT certificate.', 'Employers and institutions can confirm that a certificate is genuine using its certificate ID.') + '''
<section class="section">
  <div class="max-w-xl mx-auto px-5" x-data="{ done: false }">
    <form data-subject="Certificate verification request" @submit.prevent="SITE.sendMail($event.target); done = true" data-anim class="card p-8 md:p-10 grid gap-5 shadow-soft">
      <div class="icon-tile"><svg class="icon"><use href="#i-shield"/></svg></div>
      <h2 class="font-serif text-2xl">Enter certificate details</h2>
      ''' + field('text', 'Certificate ID', 'certificate_id', 'e.g. SPK-0000-0000') + field('text', 'Learner name (optional)', 'learner', 'As printed on the certificate', required=False) + '''
      <button type="submit" class="btn btn-primary">Verify __ARROW__</button>
      <p x-show="done" x-cloak role="status" class="text-sm text-brand-700 bg-brand-50 rounded-lg px-4 py-3">Online verification is not available yet. Please contact SparkIIT with the certificate ID and we will confirm it for you.</p>
    </form>
  </div>
</section>''' + cta()
page('verify-certificate.html', 'Verify certificate', 'Verify a SparkIIT certificate with its certificate ID.', verify)

# ------------------------------------------------------------------ affiliate
aff = ''.join(step(i + 1, t, d) for i, (t, d) in enumerate([('Join', 'Fill in the form and our team will share your referral details.'), ('Share', 'Recommend SparkIIT to friends, classmates and your audience.'), ('Earn', 'Get rewarded when someone you referred enrols.')]))
affiliate = hero('Affiliate', 'Share SparkIIT and earn.', 'Know someone who wants a career in tech? Join the affiliate program and get rewarded for every learner you bring.') + '''
<section class="section">
  <div class="container-x grid lg:grid-cols-12 gap-14">
    <div class="lg:col-span-5">
      <h2 data-anim class="h2">How it works</h2>
      <ol class="mt-10 space-y-8">''' + aff + '''</ol>
      <ul class="mt-12 space-y-4 text-slate-600">
        <li data-anim class="flex gap-3">__CHECK__<span>Rewards for every successful referral</span></li>
        <li data-anim class="flex gap-3">__CHECK__<span>Ready-to-share material from our team</span></li>
        <li data-anim class="flex gap-3">__CHECK__<span>No fee to join</span></li>
      </ul>
    </div>
    <div class="lg:col-span-7" data-anim>
      ''' + form([[field('text', 'Full name', 'name', 'Your name'), field('tel', 'Phone', 'phone', '+91')], field('email', 'Email', 'email', 'you@example.com'), field('select', 'How will you share?', 'channel', options=['Social media', 'College or community', 'Blog or YouTube', 'Friends and family', 'Other']), field('textarea', 'Tell us about your audience', 'audience', 'Optional')], 'Join the affiliate program', 'Affiliate application') + '''
    </div>
  </div>
</section>'''
page('affiliate.html', 'Affiliate', 'Join the SparkIIT affiliate program and earn by referring learners.', affiliate)

print('built pages')
