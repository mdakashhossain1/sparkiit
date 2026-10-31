(function () {
  var icon = SITE.icon, img = SITE.img, dv = SITE.dv;
  var courses = SITE.courses;
  var apply = SITE.apply;

  document.getElementById('courseCount').textContent = courses.length;

  var tools = [['java', 'Java'], ['python', 'Python'], ['react', 'React'], ['nodejs', 'Node.js'], ['javascript', 'JavaScript'], ['html5', 'HTML5'], ['css3', 'CSS3'], ['mysql', 'MySQL'], ['postgresql', 'PostgreSQL'], ['docker', 'Docker'], ['kubernetes', 'Kubernetes'], ['git', 'Git'], ['tensorflow', 'TensorFlow'], ['figma', 'Figma'], ['android', 'Android'], ['spring', 'Spring']];
  var toolsRow = tools.map(function (t) {
    return '<div class="flex items-center gap-4 mx-8"><img src="' + dv(t[0]) + '" alt="" width="40" height="40" class="w-10 h-10"><span class="text-base font-medium text-slate-600 whitespace-nowrap">' + t[1] + '</span></div>';
  }).join('');
  document.getElementById('marquee').innerHTML = toolsRow + toolsRow;

  var msLogo = '<svg viewBox="0 0 23 23" class="w-9 h-9" aria-hidden="true"><path fill="#F25022" d="M1 1h10v10H1z"/><path fill="#7FBA00" d="M12 1h10v10H12z"/><path fill="#00A4EF" d="M1 12h10v10H1z"/><path fill="#FFB900" d="M12 12h10v10H12z"/></svg>';
  var simple = function (slug, name) { return '<img src="https://cdn.simpleicons.org/' + slug + '" alt="" width="36" height="36" class="w-9 h-9"><span>' + name + '</span>'; };
  var word = function (name, color) { return '<span class="w-9 h-9 rounded-lg grid place-items-center text-sm font-semibold text-white" style="background:' + color + '">' + name.charAt(0) + '</span><span>' + name + '</span>'; };
  var rowA = [msLogo + '<span>Microsoft</span>', simple('google', 'Google'), simple('sap', 'SAP'), simple('intel', 'Intel'), simple('nvidia', 'NVIDIA'), simple('cisco', 'Cisco'), simple('accenture', 'Accenture'), simple('infosys', 'Infosys'), word('Capgemini', '#0070AD'), simple('dell', 'Dell')];
  var rowB = [simple('siemens', 'Siemens'), simple('bosch', 'Bosch'), simple('toyota', 'Toyota'), simple('tesla', 'Tesla'), simple('tcs', 'TCS'), simple('wipro', 'Wipro'), word('Cognizant', '#1A4CA1'), simple('samsung', 'Samsung'), simple('qualcomm', 'Qualcomm'), word('Adobe', '#FA0F00')];
  var chip = function (inner) { return '<div class="flex items-center gap-4 mx-3 px-7 py-5 rounded-2xl border border-line bg-white text-lg font-medium text-slate-700 whitespace-nowrap">' + inner + '</div>'; };
  var rowHtml = function (a) { var s = a.map(chip).join(''); return s + s; };
  document.getElementById('partnersA').innerHTML = rowHtml(rowA);
  document.getElementById('partnersB').innerHTML = rowHtml(rowB);

  var roles = [
    { n: 'Java Developer', d: 'Build secure, scalable back-end systems for enterprises.', i: [['java'], ['spring'], ['mysql']], s: ['Java', 'Spring Boot', 'SQL'] },
    { n: 'Front-End Developer', d: 'Turn designs into fast, accessible interfaces.', i: [['html5'], ['css3'], ['javascript'], ['react']], s: ['HTML', 'CSS', 'React'] },
    { n: 'Back-End Developer', d: 'Design the APIs and databases behind every product.', i: [['nodejs'], ['express'], ['mongodb']], s: ['Node.js', 'APIs', 'MongoDB'] },
    { n: 'Data Analyst', d: 'Find the story in data and share it with dashboards.', i: [['python'], ['pandas'], ['mysql']], s: ['Python', 'Pandas', 'SQL'] },
    { n: 'ML Engineer', d: 'Train and ship models that solve real problems.', i: [['python'], ['tensorflow'], ['jupyter']], s: ['Python', 'TensorFlow', 'Modelling'] },
    { n: 'Cloud Engineer', d: 'Run reliable infrastructure across cloud platforms.', i: [['azure'], ['googlecloud'], ['docker'], ['kubernetes']], s: ['Cloud', 'Docker', 'CI/CD'] },
    { n: 'Security Analyst', d: 'Detect threats, test defences and respond fast.', i: [['linux'], ['bash'], ['python']], s: ['Linux', 'Scripting', 'Monitoring'] },
    { n: 'UI UX Designer', d: 'Research users and craft products people enjoy.', i: [['figma'], ['photoshop', 'plain'], ['illustrator', 'plain']], s: ['Figma', 'Prototyping', 'Research'] },
    { n: 'Android Developer', d: 'Create apps used by millions on Android devices.', i: [['android'], ['kotlin'], ['java']], s: ['Kotlin', 'Android', 'APIs'] }
  ];
  document.getElementById('roleWrap').innerHTML = roles.map(function (r) {
    var chips = r.i.map(function (x) { return '<span class="w-12 h-12 rounded-xl bg-white border border-line grid place-items-center shadow-soft"><img src="' + dv(x[0], x[1]) + '" alt="" width="28" height="28" class="w-7 h-7"></span>'; }).join('');
    var pills = r.s.map(function (x) { return '<span class="text-[11px] px-2.5 py-1 rounded-full bg-slate-100 text-slate-600">' + x + '</span>'; }).join('');
    return '<div class="swiper-slide !w-72 !h-auto"><div class="card h-full overflow-hidden"><div class="h-28 bg-gradient-to-br from-brand-50 to-white border-b border-line flex items-center justify-center gap-2.5">' + chips + '</div><div class="p-6"><h3 class="font-medium">' + r.n + '</h3><p class="mt-1.5 text-sm text-mute">' + r.d + '</p><div class="mt-4 flex flex-wrap gap-1.5">' + pills + '</div></div></div></div>';
  }).join('');

  var anim = typeof gsap !== 'undefined';
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  var courseSwiper = new Swiper('#courseSwiper', {
    slidesPerView: 1.12, spaceBetween: 16, grabCursor: true, rewind: true,
    autoplay: reduce ? false : { delay: 3200, disableOnInteraction: false, pauseOnMouseEnter: true },
    navigation: { prevEl: '#cPrev', nextEl: '#cNext' },
    pagination: { el: '.course-pag', clickable: true, dynamicBullets: true },
    breakpoints: { 640: { slidesPerView: 2.05 }, 1024: { slidesPerView: 3 } }
  });

  function cardHtml(c) {
    var chips = c.tools.length ? c.tools.slice(0, 4).map(function (t) { return '<span class="w-8 h-8 rounded-lg bg-white border border-line grid place-items-center shadow-soft"><img src="' + dv(t[0], t[1]) + '" alt="" width="18" height="18" class="w-[18px] h-[18px]"></span>'; }).join('') : '<span class="w-8 h-8 rounded-lg bg-white border border-line grid place-items-center shadow-soft">' + icon(c.icon, 'w-[18px] h-[18px] text-brand-600') + '</span>';
    var learn = c.mods.slice(0, 3).map(function (m) { return '<li class="flex gap-2.5 text-sm text-slate-600"><svg class="icon w-4 h-4 text-brand-600 mt-0.5"><use href="#i-check"/></svg><span class="line-clamp-1">' + m.t + '</span></li>'; }).join('');
    var more = c.mods.length > 3 ? '<li class="pl-[26px] text-xs text-mute">+ ' + (c.mods.length - 3) + ' more modules</li>' : '';
    return '<div class="swiper-slide !h-auto"><div class="card card-hover h-full overflow-hidden flex flex-col group">' +
      '<a href="program.html?p=' + c.slug + '" class="relative block overflow-hidden" tabindex="-1" aria-hidden="true">' +
      '<img src="' + img(c.img, 700) + '" alt="" width="700" height="400" class="w-full h-40 object-cover group-hover:scale-105 transition-transform duration-700" loading="lazy">' +
      '<span class="absolute left-3 top-3 text-[11px] uppercase tracking-wider rounded-full px-2.5 py-1 bg-white text-brand-700">' + c.cat + '</span>' +
      '<span class="absolute left-3 bottom-3 flex gap-1.5">' + chips + '</span></a>' +
      '<div class="p-6 flex flex-col flex-1">' +
      '<a href="program.html?p=' + c.slug + '" class="font-medium text-lg leading-snug hover:text-brand-600 transition-colors">' + c.name + '</a>' +
      '<div class="mt-3 flex flex-wrap gap-x-4 gap-y-1.5 text-xs text-mute">' +
      '<span class="inline-flex items-center gap-1.5">' + icon('video', 'w-3.5 h-3.5 text-brand-600') + 'Live online</span>' +
      '<span class="inline-flex items-center gap-1.5">' + icon('layers', 'w-3.5 h-3.5 text-brand-600') + c.mods.length + ' modules</span>' +
      '<span class="inline-flex items-center gap-1.5">' + icon('award', 'w-3.5 h-3.5 text-brand-600') + 'Certificate</span></div>' +
      '<p class="mt-5 text-xs font-medium text-mute">What you will learn</p>' +
      '<ul class="mt-2.5 space-y-2">' + learn + more + '</ul>' +
      '<div class="mt-auto pt-6 flex items-center gap-2">' +
      '<a href="program.html?p=' + c.slug + '" class="btn btn-outline btn-sm">Syllabus</a>' +
      '<a href="' + apply + '" target="_blank" rel="noopener noreferrer" class="btn btn-primary btn-sm ml-auto">Apply now ' + icon('external', 'w-4 h-4') + '</a></div>' +
      '</div></div></div>';
  }

  function showCat(cat) {
    document.querySelectorAll('#catTabs button').forEach(function (b) {
      var on = b.dataset.cat === cat;
      b.setAttribute('aria-selected', on);
      b.className = 'whitespace-nowrap px-4 py-2 rounded-full text-sm border transition-colors ' + (on ? 'tab-active border-brand-200' : 'border-line bg-white text-slate-600 hover:border-slate-300');
    });
    courseSwiper.removeAllSlides();
    courseSwiper.appendSlide(courses.filter(function (c) { return cat === 'All' || c.cat === cat; }).map(cardHtml));
    courseSwiper.slideTo(0, 0);
    courseSwiper.update();
    if (!reduce) courseSwiper.autoplay.start();
  }
  var tabs = document.getElementById('catTabs');
  ['All'].concat(SITE.cats).forEach(function (c) {
    var b = document.createElement('button');
    b.dataset.cat = c; b.textContent = c; b.setAttribute('role', 'tab');
    b.addEventListener('click', function () { showCat(c); });
    tabs.appendChild(b);
  });
  showCat('All');

  new Swiper('#heroSwiper', {
    effect: 'cards', grabCursor: true, rewind: true,
    cardsEffect: { slideShadows: false, perSlideOffset: 9, perSlideRotate: 3 },
    autoplay: reduce ? false : { delay: 3800, disableOnInteraction: false },
    pagination: { el: '.hero-pag', clickable: true }
  });

  new Swiper('#roleSwiper', {
    slidesPerView: 'auto', spaceBetween: 16, loop: true, speed: 6000, allowTouchMove: true, freeMode: true,
    autoplay: reduce ? false : { delay: 0, disableOnInteraction: false, pauseOnMouseEnter: true }
  });

  var tm = (SITE.config.testimonials || []);
  if (tm.length) {
    var sec = document.getElementById('stories');
    sec.hidden = false;
    document.getElementById('storyWrap').innerHTML = tm.map(function (t) {
      var photo = t.photo ? '<img src="' + t.photo + '" alt="" width="48" height="48" class="w-12 h-12 rounded-full object-cover ring-1 ring-brand-200">' : '<span class="w-12 h-12 rounded-full bg-brand-50 text-brand-700 grid place-items-center text-sm font-medium">' + t.name.charAt(0) + '</span>';
      return '<figure class="swiper-slide !h-auto"><div class="card p-8 h-full flex flex-col"><blockquote class="font-serif text-2xl leading-snug">' + t.quote + '</blockquote><figcaption class="mt-auto pt-8 flex items-center gap-3">' + photo + '<div><div class="text-sm font-medium">' + t.name + '</div><div class="text-xs text-mute">' + (t.program || '') + '</div></div></figcaption></div></figure>';
    }).join('');
    new Swiper('#storySwiper', {
      slidesPerView: 1, spaceBetween: 16, grabCursor: true,
      navigation: { prevEl: '#tPrev', nextEl: '#tNext' },
      pagination: { el: '.story-pag', clickable: true, dynamicBullets: true },
      breakpoints: { 768: { slidesPerView: 2 }, 1100: { slidesPerView: 2.4 } }
    });
  }

  if (!anim || reduce) { SITE.anim(); return; }
  gsap.from('#heroTitle [data-word]', { yPercent: 110, opacity: 0, duration: .9, ease: 'power4.out', stagger: .08, delay: .1 });
  gsap.to('#float1', { y: -10, duration: 3.2, ease: 'sine.inOut', yoyo: true, repeat: -1 });
  gsap.to('#float2', { y: 10, duration: 3.8, ease: 'sine.inOut', yoyo: true, repeat: -1 });
  SITE.anim();
})();
