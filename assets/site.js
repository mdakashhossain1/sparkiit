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

  var sprite = "<svg xmlns=\"http://www.w3.org/2000/svg\" class=\"hidden\" aria-hidden=\"true\">\n  <symbol id=\"i-arrow\" viewBox=\"0 0 24 24\"><path d=\"M5 12h14M13 6l6 6-6 6\"/></symbol>\n  <symbol id=\"i-code\" viewBox=\"0 0 24 24\"><path d=\"M8 8l-5 4 5 4M16 8l5 4-5 4M14 5l-4 14\"/></symbol>\n  <symbol id=\"i-chart\" viewBox=\"0 0 24 24\"><path d=\"M4 20v-6M10 20V4M16 20v-9M2 20h20\"/></symbol>\n  <symbol id=\"i-briefcase\" viewBox=\"0 0 24 24\"><rect x=\"3\" y=\"7\" width=\"18\" height=\"13\" rx=\"2\"/><path d=\"M9 7V5a1 1 0 011-1h4a1 1 0 011 1v2M3 13h18\"/></symbol>\n  <symbol id=\"i-cloud\" viewBox=\"0 0 24 24\"><path d=\"M7 18a4 4 0 01-.5-7.97A6 6 0 0118 9.5 4.25 4.25 0 0117.5 18H7z\"/></symbol>\n  <symbol id=\"i-shield\" viewBox=\"0 0 24 24\"><path d=\"M12 3l8 3v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6l8-3zM9 12l2 2 4-4\"/></symbol>\n  <symbol id=\"i-users\" viewBox=\"0 0 24 24\"><circle cx=\"9\" cy=\"8\" r=\"3\"/><path d=\"M3 19c0-3 2.7-5 6-5s6 2 6 5\"/><circle cx=\"17\" cy=\"9\" r=\"2.5\"/><path d=\"M16 14c3 0 5 1.8 5 4.5\"/></symbol>\n  <symbol id=\"i-award\" viewBox=\"0 0 24 24\"><circle cx=\"12\" cy=\"9\" r=\"5\"/><path d=\"M8.5 13.5L7 21l5-3 5 3-1.5-7.5\"/></symbol>\n  <symbol id=\"i-file\" viewBox=\"0 0 24 24\"><path d=\"M6 3h8l5 5v13H6z\"/><path d=\"M14 3v5h5M9 13h6M9 17h6\"/></symbol>\n  <symbol id=\"i-chat\" viewBox=\"0 0 24 24\"><path d=\"M4 5h16v11H9l-5 4z\"/></symbol>\n  <symbol id=\"i-rocket\" viewBox=\"0 0 24 24\"><path d=\"M12 3c4 2 6 6 5 11l-5 4-5-4c-1-5 1-9 5-11z\"/><circle cx=\"12\" cy=\"10\" r=\"1.5\"/><path d=\"M7 16l-3 4 4-1M17 16l3 4-4-1\"/></symbol>\n  <symbol id=\"i-check\" viewBox=\"0 0 24 24\"><path d=\"M5 12l5 5 9-10\"/></symbol>\n  <symbol id=\"i-menu\" viewBox=\"0 0 24 24\"><path d=\"M4 7h16M4 12h16M4 17h16\"/></symbol>\n  <symbol id=\"i-plus\" viewBox=\"0 0 24 24\"><path d=\"M12 5v14M5 12h14\"/></symbol>\n  <symbol id=\"i-x\" viewBox=\"0 0 24 24\"><path d=\"M6 6l12 12M18 6L6 18\"/></symbol>\n  <symbol id=\"i-star\" viewBox=\"0 0 24 24\"><path d=\"M12 3l2.7 5.6 6.1.9-4.4 4.3 1 6.1L12 17l-5.4 2.9 1-6.1L3.2 9.5l6.1-.9z\"/></symbol>\n  <symbol id=\"i-quote\" viewBox=\"0 0 24 24\"><path d=\"M7 17c-2 0-3-1.5-3-3.5C4 10 6 7 9 6M17 17c-2 0-3-1.5-3-3.5 0-3.5 2-6.5 5-7.5\"/></symbol>\n  <symbol id=\"i-linkedin\" viewBox=\"0 0 24 24\"><rect x=\"3\" y=\"3\" width=\"18\" height=\"18\" rx=\"3\"/><path d=\"M8 10v7M8 7v.01M12 17v-7M12 13c0-2 1-3 3-3s2.5 1.5 2.5 3v4\"/></symbol>\n  <symbol id=\"i-instagram\" viewBox=\"0 0 24 24\"><rect x=\"3\" y=\"3\" width=\"18\" height=\"18\" rx=\"5\"/><circle cx=\"12\" cy=\"12\" r=\"4\"/><path d=\"M17.5 6.5v.01\"/></symbol>\n  <symbol id=\"i-facebook\" viewBox=\"0 0 24 24\"><path d=\"M14 8h3V4h-3a4 4 0 00-4 4v3H7v4h3v6h4v-6h3l1-4h-4V8.5c0-.3.2-.5.5-.5z\"/></symbol>\n  <symbol id=\"i-phone\" viewBox=\"0 0 24 24\"><path d=\"M5 4h4l2 5-2.5 1.5a11 11 0 005 5L15 13l5 2v4a2 2 0 01-2 2A16 16 0 013 6a2 2 0 012-2z\"/></symbol>\n  <symbol id=\"i-mail\" viewBox=\"0 0 24 24\"><rect x=\"3\" y=\"5\" width=\"18\" height=\"14\" rx=\"2\"/><path d=\"M3 7l9 6 9-6\"/></symbol>\n  <symbol id=\"i-pin\" viewBox=\"0 0 24 24\"><path d=\"M12 21s7-6 7-11a7 7 0 10-14 0c0 5 7 11 7 11z\"/><circle cx=\"12\" cy=\"10\" r=\"2.5\"/></symbol>\n  <symbol id=\"i-layers\" viewBox=\"0 0 24 24\"><path d=\"M12 3l9 5-9 5-9-5zM3 13l9 5 9-5\"/></symbol>\n  <symbol id=\"i-target\" viewBox=\"0 0 24 24\"><circle cx=\"12\" cy=\"12\" r=\"9\"/><circle cx=\"12\" cy=\"12\" r=\"5\"/><circle cx=\"12\" cy=\"12\" r=\"1\"/></symbol>\n  <symbol id=\"i-dashboard\" viewBox=\"0 0 24 24\"><rect x=\"3\" y=\"3\" width=\"8\" height=\"10\" rx=\"1.5\"/><rect x=\"13\" y=\"3\" width=\"8\" height=\"6\" rx=\"1.5\"/><rect x=\"13\" y=\"11\" width=\"8\" height=\"10\" rx=\"1.5\"/><rect x=\"3\" y=\"15\" width=\"8\" height=\"6\" rx=\"1.5\"/></symbol>\n  <symbol id=\"i-video\" viewBox=\"0 0 24 24\"><rect x=\"3\" y=\"6\" width=\"13\" height=\"12\" rx=\"2\"/><path d=\"M16 10l5-3v10l-5-3\"/></symbol>\n  <symbol id=\"i-download\" viewBox=\"0 0 24 24\"><path d=\"M12 4v11M7 11l5 5 5-5M5 20h14\"/></symbol>\n  <symbol id=\"i-trend\" viewBox=\"0 0 24 24\"><path d=\"M3 17l6-6 4 4 8-9M15 6h6v6\"/></symbol>\n  <symbol id=\"i-external\" viewBox=\"0 0 24 24\"><path d=\"M8 16L16 8M9 8h7v7\"/></symbol>\n  <symbol id=\"i-clock\" viewBox=\"0 0 24 24\"><circle cx=\"12\" cy=\"12\" r=\"9\"/><path d=\"M12 7v5l3 2\"/></symbol>\n  <symbol id=\"i-chevron\" viewBox=\"0 0 24 24\"><path d=\"M9 6l6 6-6 6\"/></symbol>\n  <symbol id=\"i-palette\" viewBox=\"0 0 24 24\"><path d=\"M12 3a9 9 0 100 18c1.5 0 2-1 1.5-2s-.5-2 1-2H17a4 4 0 004-4c0-5-4-10-9-10z\"/><circle cx=\"8\" cy=\"11\" r=\"1\"/><circle cx=\"12\" cy=\"7.5\" r=\"1\"/><circle cx=\"16\" cy=\"11\" r=\"1\"/></symbol>\n  <symbol id=\"i-phone-dev\" viewBox=\"0 0 24 24\"><rect x=\"7\" y=\"2.5\" width=\"10\" height=\"19\" rx=\"2.5\"/><path d=\"M11 18.5h2\"/></symbol>\n  <symbol id=\"i-server\" viewBox=\"0 0 24 24\"><rect x=\"3\" y=\"4\" width=\"18\" height=\"6\" rx=\"1.5\"/><rect x=\"3\" y=\"14\" width=\"18\" height=\"6\" rx=\"1.5\"/><path d=\"M7 7h.01M7 17h.01\"/></symbol>\n  <symbol id=\"i-coffee\" viewBox=\"0 0 24 24\"><path d=\"M4 9h12v5a5 5 0 01-5 5H9a5 5 0 01-5-5V9zM16 10h2a2 2 0 010 4h-2M7 3v2M11 3v2\"/></symbol>\n  <symbol id=\"i-layout\" viewBox=\"0 0 24 24\"><rect x=\"3\" y=\"4\" width=\"18\" height=\"16\" rx=\"2\"/><path d=\"M3 9h18M9 9v11\"/></symbol>\n\n  <symbol id=\"i-lock\" viewBox=\"0 0 24 24\"><rect x=\"5\" y=\"11\" width=\"14\" height=\"9\" rx=\"2\"/><path d=\"M8 11V8a4 4 0 018 0v3\"/></symbol>\n  <symbol id=\"i-search\" viewBox=\"0 0 24 24\"><circle cx=\"11\" cy=\"11\" r=\"6\"/><path d=\"M20 20l-4-4\"/></symbol>\n  <symbol id=\"i-calendar\" viewBox=\"0 0 24 24\"><rect x=\"3\" y=\"5\" width=\"18\" height=\"16\" rx=\"2\"/><path d=\"M3 10h18M8 3v4M16 3v4\"/></symbol>\n  <symbol id=\"i-book\" viewBox=\"0 0 24 24\"><path d=\"M4 5a2 2 0 012-2h13v16H6a2 2 0 00-2 2zM4 19V5\"/></symbol>\n  <symbol id=\"i-gift\" viewBox=\"0 0 24 24\"><rect x=\"3\" y=\"8\" width=\"18\" height=\"5\" rx=\"1\"/><path d=\"M12 8v13M5 13v8h14v-8M12 8c-2-4-6-3-5 0M12 8c2-4 6-3 5 0\"/></symbol>\n</svg>";
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
