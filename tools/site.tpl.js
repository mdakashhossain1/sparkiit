(function () {
  var DV = 'https://cdn.jsdelivr.net/gh/devicons/devicon@v2.16.0/icons/';
  var SITE = window.SITE = {};

  SITE.dv = function (n, v) { return DV + n + '/' + n + '-' + (v || 'original') + '.svg'; };
  SITE.img = function (id, w, h) { return 'https://images.unsplash.com/photo-' + id + '?auto=format&fit=crop&w=' + (w || 800) + (h ? '&h=' + h : '') + '&q=70'; };
  SITE.icon = function (n, c) { return '<svg class="icon ' + (c || '') + '"><use href="#i-' + n + '"/></svg>'; };
  SITE.slug = function (n) { return n.toLowerCase().replace(/&/g, 'and').replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, ''); };

  SITE.toolName = function (k) { var m = { amazonwebservices: 'AWS', googlecloud: 'Google Cloud', nodejs: 'Node.js', html5: 'HTML5', css3: 'CSS3', mysql: 'MySQL', javascript: 'JavaScript', postgresql: 'PostgreSQL', tensorflow: 'TensorFlow', scikitlearn: 'scikit-learn', numpy: 'NumPy', raspberrypi: 'Raspberry Pi', cplusplus: 'C++', matlab: 'MATLAB', php: 'PHP', raspberry: 'Raspberry Pi' }; return m[k] || k.charAt(0).toUpperCase() + k.slice(1); };
  SITE.cats = window.PROGRAM_CATS || [];
  SITE.catLabel = {};
  SITE.courses = (window.PROGRAMS || []).map(function (p) { p.tools = p.tools || []; return p; });

  SITE.card = function (c) {
    var chips = c.tools.length ? c.tools.map(function (t) { return '<img src="' + SITE.dv(t[0], t[1]) + '" alt="" class="w-5 h-5">'; }).join('') : SITE.icon(c.icon, 'w-5 h-5 text-brand-600');
    return '<a href="program.html?p=' + c.slug + '" class="card card-hover h-full flex flex-col overflow-hidden group">' +
      '<div class="relative overflow-hidden"><img src="' + SITE.img(c.img, 700) + '" alt="" class="w-full h-44 object-cover group-hover:scale-105 transition-transform duration-700" loading="lazy">' +
      '<span class="absolute left-3 top-3 text-[11px] uppercase tracking-wider rounded-full px-2.5 py-1 bg-brand-50 text-brand-700">' + c.mods.length + ' modules</span></div>' +
      '<div class="p-6 flex flex-col flex-1"><div class="flex items-center gap-2 h-8 -mt-10 relative"><span class="inline-flex items-center gap-2 bg-white border border-line rounded-lg px-2.5 py-1.5 shadow-[0_2px_8px_rgba(15,23,42,.05)]">' + chips + '</span></div>' +
      '<h3 class="mt-4 font-medium flex items-start justify-between gap-3">' + c.name + '<span class="text-slate-300 group-hover:text-brand-600 transition-colors mt-0.5">' + SITE.icon('arrow', 'w-4 h-4') + '</span></h3>' +
      '<p class="mt-2 text-sm text-mute">' + c.d + '</p></div></a>';
  };

  var sprite = '%%SPRITE%%';
  var cfg = SITE.config = window.SITE_CONFIG || {};
  var apply = cfg.applyUrl || 'https://evolvix.tech';
  var social = cfg.social || {};
  var page = (location.pathname.split('/').pop() || 'index.html').toLowerCase();

  var nav = [['programs.html', 'Programs'], ['career-pass.html', 'Career Pass'], ['about.html', 'About'], ['contact.html', 'Contact']];
  var active = function (h) { return page === h || (h === 'programs.html' && page === 'program.html'); };
  var navDesk = nav.map(function (n) {
    return '<a href="' + n[0] + '" class="relative py-1 transition-colors ' + (active(n[0]) ? 'text-brand-600 font-medium' : 'hover:text-ink') + '">' + n[1] + (active(n[0]) ? '<span class="absolute -bottom-1 left-0 right-0 h-0.5 rounded-full bg-brand-600"></span>' : '') + '</a>';
  }).join('');
  var navMob = nav.map(function (n) { return '<a href="' + n[0] + '" class="py-3 border-b border-line ' + (active(n[0]) ? 'text-brand-600 font-medium' : '') + '">' + n[1] + '</a>'; }).join('');

  var applyBtn = function (cls) { return '<a href="' + apply + '" target="_blank" rel="noopener noreferrer" class="btn btn-primary ' + cls + '">Apply now ' + SITE.icon('external', 'w-4 h-4') + '</a>'; };

  var header = '<a href="#main" class="skip-link">Skip to content</a>' +
    '<header id="siteHeader" x-data="{ menu: false }" class="sticky top-0 z-40 bg-white/90 backdrop-blur-md border-b border-line transition-shadow duration-300"><nav class="container-x h-[72px] flex items-center justify-between" aria-label="Main">' +
    '<a href="index.html" class="flex items-center gap-2.5 font-semibold text-xl tracking-tight" aria-label="SparkIIT home"><img src="logo-mark.svg" alt="" class="w-9 h-9"><span>Spark<span class="text-brand-600">IIT</span></span></a>' +
    '<div class="hidden lg:flex items-center gap-9 text-sm text-slate-600">' + navDesk + '</div>' +
    '<div class="hidden lg:block">' + applyBtn('btn-sm') + '</div>' +
    '<button class="lg:hidden -mr-2 p-2" aria-label="Toggle menu" :aria-expanded="menu" @click="menu = !menu"><svg class="icon w-6 h-6" x-show="!menu"><use href="#i-menu"/></svg><svg class="icon w-6 h-6" x-show="menu" x-cloak><use href="#i-x"/></svg></button></nav>' +
    '<div x-show="menu" x-cloak x-transition.opacity class="lg:hidden border-t border-line bg-white"><div class="container-x py-3 flex flex-col text-slate-700" @click="menu = false">' + navMob +
    '<div class="pt-5 pb-3">' + applyBtn('w-full') + '</div></div></div></header>';

  var li = function (h, t) { return '<li><a href="' + h + '" class="hover:text-ink transition-colors">' + t + '</a></li>'; };
  var soc = function (key, icon, label) {
    return social[key] ? '<a href="' + social[key] + '" target="_blank" rel="noopener noreferrer" class="w-10 h-10 rounded-lg border border-line bg-white grid place-items-center text-slate-500 hover:text-brand-600 hover:border-brand-200 transition" aria-label="' + label + '">' + SITE.icon(icon, 'w-[18px] h-[18px]') + '</a>' : '';
  };
  var socials = soc('instagram', 'instagram', 'Instagram') + soc('linkedin', 'linkedin', 'LinkedIn') + soc('facebook', 'facebook', 'Facebook');
  var contactRows = '';
  if (cfg.address) contactRows += '<li class="flex gap-3">' + SITE.icon('pin', 'w-4 h-4 mt-1 text-brand-600') + '<span>' + cfg.address + '</span></li>';
  if (cfg.phone) contactRows += '<li class="flex gap-3">' + SITE.icon('phone', 'w-4 h-4 mt-1 text-brand-600') + '<a href="tel:' + cfg.phone.replace(/\s+/g, '') + '" class="hover:text-ink">' + cfg.phone + '</a></li>';
  if (cfg.email) contactRows += '<li class="flex gap-3">' + SITE.icon('mail', 'w-4 h-4 mt-1 text-brand-600') + '<a href="mailto:' + cfg.email + '" class="hover:text-ink">' + cfg.email + '</a></li>';

  var footer = '<footer class="border-t border-line bg-slate-50/70"><div class="container-x py-16 grid md:grid-cols-12 gap-12">' +
    '<div class="md:col-span-5"><a href="index.html" class="flex items-center gap-2.5 font-semibold text-xl tracking-tight"><img src="logo-mark.svg" alt="" class="w-9 h-9"><span>Spark<span class="text-brand-600">IIT</span></span></a>' +
    '<p class="mt-4 text-sm text-mute max-w-sm">Mentor-led programs and certifications for learners building a career in technology, engineering and business.</p>' +
    '<div class="mt-6">' + applyBtn('btn-sm') + '</div>' + (socials ? '<div class="mt-6 flex gap-2">' + socials + '</div>' : '') + '</div>' +
    '<div class="md:col-span-3"><h4 class="text-sm font-medium">Explore</h4><ul class="mt-4 space-y-3 text-sm text-slate-600">' + li('index.html', 'Home') + li('programs.html', 'Programs') + li('career-pass.html', 'Career Pass') + li('about.html', 'About') + '</ul></div>' +
    '<div class="md:col-span-4"><h4 class="text-sm font-medium">Support</h4><ul class="mt-4 space-y-3 text-sm text-slate-600">' + li('contact.html', 'Contact us') + li('verify-certificate.html', 'Verify a certificate') + li('affiliate.html', 'Affiliate program') + '</ul>' +
    (contactRows ? '<ul class="mt-6 space-y-3 text-sm text-slate-600">' + contactRows + '</ul>' : '') + '</div></div>' +
    '<div class="border-t border-line"><div class="container-x py-6 text-xs text-mute">&copy; ' + new Date().getFullYear() + ' SparkIIT. All rights reserved.</div></div></footer>' +
    (cfg.whatsapp ? '<a href="' + cfg.whatsapp + '" target="_blank" rel="noopener noreferrer" class="fixed bottom-5 right-5 z-30 btn btn-primary rounded-full" aria-label="Chat on WhatsApp">' + SITE.icon('chat', 'w-[18px] h-[18px]') + '<span class="hidden sm:inline">Chat with us</span></a>' : '');

  document.body.insertAdjacentHTML('afterbegin', sprite);
  var h = document.getElementById('site-header'); if (h) h.outerHTML = header;
  var f = document.getElementById('site-footer'); if (f) f.outerHTML = footer;

  var hd = document.getElementById('siteHeader');
  if (hd) {
    var onScroll = function () { hd.classList.toggle('shadow-soft', window.scrollY > 8); };
    onScroll();
    window.addEventListener('scroll', onScroll, { passive: true });
  }

  SITE.apply = apply;

  SITE.sendMail = function (form) {
    var to = cfg.formEmail || cfg.email;
    if (!to) return;
    var lines = [];
    form.querySelectorAll('[name]').forEach(function (el) {
      var label = el.closest('label'), span = label && label.querySelector('span');
      if (el.value) lines.push((span ? span.textContent.trim() : el.name) + ': ' + el.value);
    });
    lines.push('', 'Sent from ' + location.href);
    var url = 'https://mail.google.com/mail/?view=cm&fs=1&to=' + encodeURIComponent(to) + '&su=' + encodeURIComponent(form.dataset.subject || 'Website enquiry') + '&body=' + encodeURIComponent(lines.join('\n'));
    window.open(url, '_blank', 'noopener');
  };
  SITE.applyBtn = applyBtn;

  SITE.anim = function () {
    if (typeof gsap === 'undefined') { document.documentElement.classList.add('anim-fallback'); return; }
    gsap.registerPlugin(ScrollTrigger);
    ScrollTrigger.batch('[data-anim]', {
      start: 'top 92%', once: true,
      onEnter: function (els) { gsap.to(els, { opacity: 1, y: 0, duration: .8, ease: 'power3.out', stagger: .08, overwrite: true }); }
    });
  };
})();
