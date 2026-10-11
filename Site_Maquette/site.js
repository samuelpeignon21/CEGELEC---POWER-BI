// Carrousel de la page d'accueil
(function () {
  var hero = document.getElementById('hero');
  if (hero) {
    var slides = Array.prototype.slice.call(hero.querySelectorAll('.slide'));
    var pts = document.getElementById('points');
    var i = 0, timer;
    function aller(n) {
      i = n;
      slides.forEach(function (s, k) { s.classList.toggle('actif', k === n); });
      Array.prototype.forEach.call(pts.children, function (b, k) { b.classList.toggle('actif', k === n); });
    }
    function reset() { clearInterval(timer); timer = setInterval(function () { aller((i + 1) % slides.length); }, 6000); }
    slides.forEach(function (_, n) {
      var b = document.createElement('button');
      b.setAttribute('aria-label', 'Diapositive ' + (n + 1));
      b.onclick = function () { aller(n); reset(); };
      pts.appendChild(b);
    });
    aller(0); reset();
  }

  // Accès à la page secrète : code Konami, ou 5 clics sur la signature du pied de page
  var konami = ['ArrowUp', 'ArrowUp', 'ArrowDown', 'ArrowDown', 'ArrowLeft', 'ArrowRight', 'ArrowLeft', 'ArrowRight', 'b', 'a'];
  var pos = 0;
  var mot = 'secret', lettres = '';
  document.addEventListener('keydown', function (ev) {
    var k = ev.key.length === 1 ? ev.key.toLowerCase() : ev.key;
    if (ev.key.length === 1) {
      lettres = (lettres + k).slice(-mot.length);
      if (lettres === mot) { window.location.href = 'secret.html'; }
    }
    pos = (k === konami[pos]) ? pos + 1 : (k === konami[0] ? 1 : 0);
    if (pos === konami.length) { window.location.href = 'secret.html'; }
  });
  var sig = document.getElementById('signature');
  if (sig) {
    var clics = 0, t0;
    sig.addEventListener('click', function () {
      var now = Date.now();
      clics = (now - t0 < 2000) ? clics + 1 : 1;
      t0 = now;
      if (clics >= 5) { window.location.href = 'secret.html'; }
    });
  }

  // Filtre par thème sur la page des références
  var filtres = document.getElementById('filtres');
  if (filtres) {
    filtres.addEventListener('click', function (ev) {
      var b = ev.target.closest('button');
      if (!b) return;
      var theme = b.getAttribute('data-theme');
      Array.prototype.forEach.call(filtres.children, function (x) { x.classList.toggle('actif', x === b); });
      Array.prototype.forEach.call(document.querySelectorAll('#liste-refs .carte'), function (c) {
        var themes = (c.getAttribute('data-themes') || '').split('|');
        c.style.display = (!theme || themes.indexOf(theme) !== -1) ? '' : 'none';
      });
    });
  }
})();
