/* The Plastering and Rendering Group: demo site behaviour */
(function () {
  'use strict';
  var d = document;
  var canHover = !!(window.matchMedia && window.matchMedia('(hover: hover) and (pointer: fine)').matches);
  var each = function (list, fn) { Array.prototype.forEach.call(list, fn); };

  /* ---------- Services dropdown (desktop) ---------- */
  var megaBtn = d.querySelector('[data-mega-btn]');
  var mega = d.getElementById('mega');
  var megaWrap = d.querySelector('[data-mega-wrap]');
  if (megaBtn && mega) {
    var closeTimer = null;
    var setMega = function (open) {
      mega.hidden = !open;
      megaBtn.setAttribute('aria-expanded', open ? 'true' : 'false');
    };
    megaBtn.addEventListener('click', function (e) {
      // A mouse click on a hover device opens (hover may already have);
      // keyboard and touch toggle.
      if (canHover && e.detail > 0) { setMega(true); return; }
      setMega(mega.hidden);
    });
    if (canHover && megaWrap) {
      megaWrap.addEventListener('mouseenter', function () { clearTimeout(closeTimer); setMega(true); });
      megaWrap.addEventListener('mouseleave', function () {
        closeTimer = setTimeout(function () { setMega(false); }, 220);
      });
    }
    d.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && !mega.hidden) { setMega(false); megaBtn.focus(); }
    });
    d.addEventListener('click', function (e) {
      if (!mega.hidden && !mega.contains(e.target) && !megaBtn.contains(e.target)) setMega(false);
    });
    mega.addEventListener('focusout', function (e) {
      var to = e.relatedTarget;
      if (to && !mega.contains(to) && to !== megaBtn) setMega(false);
    });
    mega.addEventListener('click', function (e) {
      if (e.target.closest && e.target.closest('a')) setMega(false);
    });
  }

  /* ---------- Mobile menu ---------- */
  var menuBtn = d.querySelector('[data-menu-btn]');
  var mnav = d.getElementById('mnav');
  if (menuBtn && mnav) {
    var label = menuBtn.querySelector('.menu-label');
    var setMenu = function (open) {
      mnav.hidden = !open;
      menuBtn.setAttribute('aria-expanded', open ? 'true' : 'false');
      if (label) label.textContent = open ? 'Close' : 'Menu';
    };
    menuBtn.addEventListener('click', function () { setMenu(mnav.hidden); });
    mnav.addEventListener('click', function (e) {
      if (e.target.closest && e.target.closest('a')) setMenu(false);
    });
  }
  each(d.querySelectorAll('[data-acc]'), function (btn) {
    var panel = d.getElementById(btn.getAttribute('aria-controls'));
    btn.addEventListener('click', function () {
      var open = btn.getAttribute('aria-expanded') !== 'true';
      btn.setAttribute('aria-expanded', open ? 'true' : 'false');
      if (panel) panel.hidden = !open;
    });
  });

  /* ---------- Carousels (swipe rows with dots; arrows where present) ---------- */
  var cars = [];
  var visibleItems = function (el) {
    return Array.prototype.filter.call(el.children, function (c) { return !c.hidden; });
  };
  var metrics = function (el) {
    var items = visibleItems(el);
    if (!items.length) return null;
    var w = items[0].getBoundingClientRect().width;
    var gap = parseFloat(getComputedStyle(el).columnGap) || 0;
    var per = Math.max(1, Math.floor((el.clientWidth + gap + 2) / (w + gap)));
    return { step: w + gap, pages: Math.max(1, items.length - per + 1) };
  };
  var mark = function (c, m) {
    m = m || metrics(c.el);
    if (!m) return;
    var x = c.el.scrollLeft;
    var atEnd = x + c.el.clientWidth >= c.el.scrollWidth - 4;
    var idx = atEnd ? m.pages - 1 : Math.round(x / m.step);
    idx = Math.max(0, Math.min(m.pages - 1, idx));
    each(c.dots.children, function (dot, i) { dot.classList.toggle('on', i === idx); });
    if (c.prev) c.prev.disabled = x <= 2;
    if (c.next) c.next.disabled = atEnd;
  };
  var refresh = function (c) {
    var m = metrics(c.el);
    var scrollable = c.el.scrollWidth > c.el.clientWidth + 2;
    if (!m || !scrollable) {
      c.dots.style.display = 'none';
      if (c.prev) c.prev.disabled = true;
      if (c.next) c.next.disabled = true;
      return;
    }
    c.dots.style.display = '';
    if (c.dots.children.length !== m.pages) {
      c.dots.innerHTML = '';
      for (var i = 0; i < m.pages; i++) c.dots.appendChild(d.createElement('span'));
    }
    mark(c, m);
  };
  each(d.querySelectorAll('.carousel'), function (el) {
    var dots = d.createElement('div');
    dots.className = 'dots';
    dots.setAttribute('aria-hidden', 'true');
    var slot = el.parentNode.querySelector('.dots-slot');
    if (slot) slot.appendChild(dots); else el.insertAdjacentElement('afterend', dots);
    var id = el.id;
    var c = {
      el: el, dots: dots,
      prev: id ? d.querySelector('[data-car-prev="' + id + '"]') : null,
      next: id ? d.querySelector('[data-car-next="' + id + '"]') : null
    };
    cars.push(c);
    var go = function (dir) {
      var m = metrics(el);
      if (m) el.scrollBy({ left: dir * m.step, behavior: 'smooth' });
    };
    if (c.prev) c.prev.addEventListener('click', function () { go(-1); });
    if (c.next) c.next.addEventListener('click', function () { go(1); });
    var raf = 0;
    el.addEventListener('scroll', function () {
      if (raf) return;
      raf = requestAnimationFrame(function () { raf = 0; mark(c); });
    }, { passive: true });
    refresh(c);
  });
  var resizeRaf = 0;
  window.addEventListener('resize', function () {
    if (resizeRaf) return;
    resizeRaf = requestAnimationFrame(function () { resizeRaf = 0; cars.forEach(refresh); });
  });
  window.addEventListener('load', function () { cars.forEach(refresh); });

  /* ---------- Filters (Jobs we're proud of) ---------- */
  var fbtns = d.querySelectorAll('[data-filter]');
  each(fbtns, function (b) {
    b.addEventListener('click', function () {
      var f = b.getAttribute('data-filter');
      each(fbtns, function (o) { o.setAttribute('aria-pressed', o === b ? 'true' : 'false'); });
      each(d.querySelectorAll('[data-cat]'), function (item) {
        item.hidden = !(f === 'all' || item.getAttribute('data-cat') === f);
      });
      cars.forEach(refresh);
    });
  });

  /* ---------- Before / after sliders ---------- */
  each(d.querySelectorAll('[data-ba]'), function (ba) {
    var range = ba.querySelector('.ba-range');
    var active = false;
    var pid = null;
    var set = function (p) {
      p = Math.max(0, Math.min(100, p));
      ba.style.setProperty('--pos', p + '%');
      if (range) range.value = String(Math.round(p));
    };
    var at = function (e) {
      var r = ba.getBoundingClientRect();
      set((e.clientX - r.left) / r.width * 100);
    };
    ba.addEventListener('pointerdown', function (e) {
      if (e.pointerType === 'mouse' && e.button !== 0) return;
      active = true;
      pid = e.pointerId;
      try { ba.setPointerCapture(pid); } catch (err) { /* older browsers */ }
      // Touch waits for a horizontal move, so a vertical scroll doesn't jump the handle.
      if (e.pointerType === 'mouse') { at(e); e.preventDefault(); }
    });
    ba.addEventListener('pointermove', function (e) {
      if (active && e.pointerId === pid) at(e);
    });
    ['pointerup', 'pointercancel', 'lostpointercapture'].forEach(function (t) {
      ba.addEventListener(t, function () { active = false; });
    });
    if (range) {
      range.addEventListener('input', function () { set(+range.value); });
      range.addEventListener('keydown', function (e) {
        var v = +range.value;
        var k = e.key;
        if (k === 'ArrowLeft' || k === 'ArrowDown') { set(v - 5); e.preventDefault(); }
        else if (k === 'ArrowRight' || k === 'ArrowUp') { set(v + 5); e.preventDefault(); }
        else if (k === 'Home') { set(0); e.preventDefault(); }
        else if (k === 'End') { set(100); e.preventDefault(); }
      });
    }
  });

  /* ---------- Quote form (preview only) ---------- */
  each(d.querySelectorAll('[data-quote-form]'), function (f) {
    f.addEventListener('submit', function (e) {
      e.preventDefault();
      var s = f.querySelector('.form-status');
      if (s) s.hidden = false;
    });
  });
})();
