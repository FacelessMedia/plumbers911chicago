document.addEventListener('DOMContentLoaded', function() {
  // === Phase 9: Mobile nav toggle ===
  var toggle = document.querySelector('.menu-toggle');
  var nav = document.querySelector('.main-nav');
  if (toggle && nav) {
    toggle.addEventListener('click', function() {
      nav.classList.toggle('open');
      var list = nav.querySelector('.nav-list');
      if (list) list.style.display = list.style.display === 'flex' ? 'none' : 'flex';
    });
  }

  // === Phase 142: Scroll-triggered fade-in animations ===
  if ('IntersectionObserver' in window && !window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    var animEls = document.querySelectorAll('.feature-card, .value-card, .step-card, .stat-card, .service-card, .location-card, .info-card, .faq-item');
    animEls.forEach(function(el) { el.style.opacity = '0'; el.style.transform = 'translateY(20px)'; el.style.transition = 'opacity .5s ease, transform .5s ease'; });
    var obs = new IntersectionObserver(function(entries) {
      entries.forEach(function(e) {
        if (e.isIntersecting) { e.target.style.opacity = '1'; e.target.style.transform = 'translateY(0)'; obs.unobserve(e.target); }
      });
    }, { threshold: 0.1, rootMargin: '0px 0px -40px 0px' });
    animEls.forEach(function(el) { obs.observe(el); });
  }

  // === Phase 143: Reading progress bar for blog posts ===
  var progressBar = document.getElementById('reading-progress');
  if (progressBar) {
    var article = document.querySelector('.blog-post') || document.querySelector('.content-body');
    if (article) {
      window.addEventListener('scroll', function() {
        var rect = article.getBoundingClientRect();
        var total = article.offsetHeight - window.innerHeight;
        var progress = Math.min(100, Math.max(0, (-rect.top / total) * 100));
        progressBar.style.width = progress + '%';
      });
    }
  }

  // === Phase 149: Back-to-top button ===
  var btt = document.getElementById('back-to-top');
  if (btt) {
    window.addEventListener('scroll', function() {
      btt.style.display = window.scrollY > 500 ? 'flex' : 'none';
    });
    btt.addEventListener('click', function(e) {
      e.preventDefault();
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });
  }

  // === Phase 150: Form validation ===
  var forms = document.querySelectorAll('#contact-form, .sidebar-form form, .sidebar-form-mini form');
  forms.forEach(function(form) {
    var phoneInputs = form.querySelectorAll('input[type="tel"]');
    phoneInputs.forEach(function(input) {
      input.addEventListener('input', function() {
        var v = this.value.replace(/\D/g, '');
        if (v.length >= 10) { this.value = '(' + v.slice(0,3) + ') ' + v.slice(3,6) + '-' + v.slice(6,10); }
        else if (v.length >= 6) { this.value = '(' + v.slice(0,3) + ') ' + v.slice(3,6) + '-' + v.slice(6); }
        else if (v.length >= 3) { this.value = '(' + v.slice(0,3) + ') ' + v.slice(3); }
      });
    });
    form.addEventListener('submit', function(e) {
      var valid = true;
      form.querySelectorAll('[required]').forEach(function(f) {
        f.style.borderColor = '';
        if (!f.value.trim()) { f.style.borderColor = '#e52521'; valid = false; }
      });
      if (!valid) { e.preventDefault(); }
    });
  });

  // === Phase 159: Cookie consent banner ===
  if (!localStorage.getItem('p911_consent')) {
    var banner = document.getElementById('cookie-consent');
    if (banner) {
      banner.style.display = 'block';
      var acceptBtn = document.getElementById('cookie-accept');
      if (acceptBtn) {
        acceptBtn.addEventListener('click', function() {
          localStorage.setItem('p911_consent', '1');
          banner.style.display = 'none';
        });
      }
    }
  }

  // === Phase 144: Auto-generate TOC from H2 headings ===
  var tocContainer = document.querySelector('.toc');
  if (!tocContainer) {
    var article = document.querySelector('.content-body');
    if (article && document.querySelector('.blog-post')) {
      var headings = article.querySelectorAll('h2[id]');
      if (headings.length >= 3) {
        var toc = document.createElement('nav');
        toc.className = 'auto-toc';
        toc.innerHTML = '<strong>In This Article:</strong>';
        var ol = document.createElement('ol');
        headings.forEach(function(h) {
          var li = document.createElement('li');
          var a = document.createElement('a');
          a.href = '#' + h.id;
          a.textContent = h.textContent;
          li.appendChild(a);
          ol.appendChild(li);
        });
        toc.appendChild(ol);
        article.insertBefore(toc, article.firstChild);
      }
    }
  }

  // === Phase 148: Social share buttons for blog posts ===
  var blogPost = document.querySelector('.blog-post');
  if (blogPost) {
    var shareDiv = document.createElement('div');
    shareDiv.className = 'share-buttons';
    shareDiv.innerHTML = '<strong>Share:</strong> ' +
      '<a href="https://www.facebook.com/sharer/sharer.php?u=' + encodeURIComponent(window.location.href) + '" target="_blank" rel="noopener" class="share-btn share-fb">Facebook</a> ' +
      '<a href="https://twitter.com/intent/tweet?url=' + encodeURIComponent(window.location.href) + '&text=' + encodeURIComponent(document.title) + '" target="_blank" rel="noopener" class="share-btn share-tw">X/Twitter</a> ' +
      '<a href="https://www.linkedin.com/sharing/share-offsite/?url=' + encodeURIComponent(window.location.href) + '" target="_blank" rel="noopener" class="share-btn share-li">LinkedIn</a> ' +
      '<button class="share-btn share-copy" onclick="navigator.clipboard.writeText(window.location.href);this.textContent=\'Copied!\'">Copy Link</button>';
    var postFooter = blogPost.querySelector('.post-footer .container');
    if (postFooter) postFooter.appendChild(shareDiv);
  }

  // === Phase 164: Phone click tracking ===
  document.querySelectorAll('a[href^="tel:"]').forEach(function(link) {
    link.addEventListener('click', function() {
      var loc = this.closest('.site-header') ? 'header' : this.closest('.mobile-call-bar') ? 'mobile-bar' : this.closest('.site-footer') ? 'footer' : this.closest('.sidebar-cta') ? 'sidebar' : this.closest('.hero') ? 'hero' : 'content';
      if (window.dataLayer) window.dataLayer.push({ event: 'phone_click', click_location: loc, phone_number: '833-758-6911' });
      if (window.gtag) window.gtag('event', 'phone_click', { event_category: 'engagement', event_label: loc });
    });
  });
});
