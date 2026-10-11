// Salle de jeux cachée : Duel des chantiers (jeu de cartes à la Hearthstone), Paires, Bibliothèque.
// Écrit en JavaScript « classique » (var, function) pour rester compatible partout.
(function () {
  'use strict';

  // ------------------------------------------------------------ outils communs
  var MARQUES = ['#d6001c', '#7f3fd4', '#9ccc0a', '#2d8ae0'];

  function $(id) { return document.getElementById(id); }
  function lire(cle, defaut) { try { var v = localStorage.getItem(cle); return v === null ? defaut : v; } catch (e) { return defaut; } }
  function ecrire(cle, v) { try { localStorage.setItem(cle, String(v)); } catch (e) { /* stockage indisponible */ } }
  function clamp(x, a, b) { return Math.max(a, Math.min(b, x)); }
  function vider(el) { while (el.firstChild) el.removeChild(el.firstChild); }
  function formatTemps(s) { return Math.floor(s / 60) + ':' + ('0' + (s % 60)).slice(-2); }
  function texte(tag, cls, t) {
    var e = document.createElement(tag);
    if (cls) e.className = cls;
    e.textContent = t;
    return e;
  }
  function melanger(a) {
    for (var i = a.length - 1; i > 0; i--) {
      var j = Math.floor(Math.random() * (i + 1));
      var t = a[i]; a[i] = a[j]; a[j] = t;
    }
    return a;
  }
  function hash(s) {
    var h = 0;
    for (var i = 0; i < s.length; i++) h = (h * 31 + s.charCodeAt(i)) % 100000;
    return h;
  }

  // ------------------------------------------------------------ données des cartes
  var MARQUES_BIB = {
    'cegelec': { nom: 'Cegelec', couleur: '#d6001c' },
    'building-solutions': { nom: 'Building Solutions', couleur: '#b3001a' },
    'maintenance-energies': { nom: 'Maintenance Énergies', couleur: '#e0384a' },
    'cegelec-nord': { nom: 'Cegelec Nord', couleur: '#8f0016' },
    'axians': { nom: 'Axians', couleur: '#7f3fd4' },
    'actemium': { nom: 'Actemium', couleur: '#8cb800', clair: true },
    'omexom-te': { nom: 'Omexom TE', couleur: '#2d8ae0' },
    'omexom-reseaux': { nom: 'Omexom Réseaux', couleur: '#1f6bb8' },
    'citeos': { nom: 'Citeos', couleur: '#901848' },
    'vinci': { nom: 'VINCI', couleur: '#b8892b' }
  };
  var RARETES = {
    'Commune': { nom: 'Commune', cls: 'r-commune', rang: 0 },
    'Rare': { nom: 'Rare', cls: 'r-rare', rang: 1 },
    'Épique': { nom: 'Épique', cls: 'r-epique', rang: 2 },
    'Légendaire': { nom: 'Légendaire', cls: 'r-legendaire', rang: 3 }
  };
  var TYPES = {
    objet: { nom: 'Objet', rarete: 'Commune', utilite: true },
    technicien: { nom: 'Technicien', rarete: 'Rare' },
    responsable: { nom: 'Responsable', rarete: 'Épique' },
    direction: { nom: 'Direction', rarete: 'Légendaire' }
  };
  // La rareté dépend du type de carte ; un champ « rarete » peut la forcer.
  function rareteDe(m) {
    if (m.rarete && RARETES[m.rarete]) return RARETES[m.rarete];
    var t = TYPES[m.type];
    if (t) return RARETES[t.rarete];
    return RARETES['Commune'];
  }
  function marqueDe(m) { return MARQUES_BIB[m.marque] || { nom: m.marque || '—', couleur: '#6b7785' }; }
  function initiales(nom) {
    return String(nom || '?').trim().split(/\s+/).map(function (p) { return p.charAt(0); }).join('').slice(0, 2).toUpperCase();
  }

  // ------------------------------------------------------------ onglets
  var onglets = document.querySelectorAll('.onglets button');
  Array.prototype.forEach.call(onglets, function (b) {
    b.addEventListener('click', function () {
      Array.prototype.forEach.call(onglets, function (x) {
        var actif = x === b;
        x.classList.toggle('actif', actif);
        x.setAttribute('aria-selected', actif ? 'true' : 'false');
      });
      Array.prototype.forEach.call(document.querySelectorAll('.jeu'), function (j) {
        j.classList.toggle('actif', j.id === 'jeu-' + b.getAttribute('data-jeu'));
      });
    });
  });

  // ============================================================ 1. DUEL DES CHANTIERS
  // Règles : 30 PV chacun, énergie +1 par tour (max 10), 7 cartes en main, 5 serviteurs sur le terrain.
  // Les stats viennent des cartes : coût = puissance et rareté ; capacité = marque.
  var D_PV = 30, D_MAIN_MAX = 7, D_PLATEAU_MAX = 5, D_ENERGIE_MAX = 10, D_DECK = 20;

  // Capacités : « pouvoir » (permanent) ou « cri de guerre » (effet immédiat à l'arrivée en jeu).
  // « n » est la valeur de base ; elle augmente avec la rareté (Épique +1, Légendaire +2), sauf si « fixe ».
  var CAPACITES = {
    'cegelec':              { kw: 'bouclier',    nom: 'Bouclier',    ico: '🛡', fixe: true, txt: function () { return 'Ignore le premier dégât subi.'; } },
    'building-solutions':   { kw: 'provocation', nom: 'Provocation', ico: '🧱', fixe: true, txt: function () { return 'Les ennemis doivent l\'attaquer en premier.'; } },
    'actemium':             { kw: 'ruee',        nom: 'Ruée',        ico: '🤖', fixe: true, txt: function () { return 'Peut attaquer dès son arrivée en jeu.'; } },
    'maintenance-energies': { cri: 'soin',   n: 3, nom: 'Soin',    ico: '🔧', txt: function (n) { return 'Rend ' + n + ' PV à ton héros.'; } },
    'cegelec-nord':         { cri: 'degats', n: 2, nom: 'Foudre',  ico: '⚡', txt: function (n) { return 'Inflige ' + n + ' dégâts à un ennemi au hasard.'; } },
    'axians':               { cri: 'pioche', n: 1, nom: 'Pioche',  ico: '📶', txt: function (n) { return 'Pioche ' + n + ' carte' + (n > 1 ? 's' : '') + '.'; } },
    'omexom-te':            { cri: 'energie', n: 1, nom: 'Énergie', ico: '☀️', txt: function (n) { return 'Donne +' + n + ' énergie ce tour.'; } },
    'omexom-reseaux':       { cri: 'buff',   n: 1, nom: 'Renfort', ico: '🔗', txt: function (n) { return 'Tes serviteurs gagnent +' + n + ' attaque.'; } },
    'citeos':               { cri: 'heros',  n: 2, nom: 'Éclair',  ico: '💡', txt: function (n) { return 'Inflige ' + n + ' dégâts au héros adverse.'; } },
    'vinci':                { cri: 'epargne', n: 2, nom: 'Épargne', ico: '🦫', fixe: true, txt: function (n) { return 'Gagne +' + n + ' cristaux d\'énergie maximum.'; } }
  };
  function capaciteInstance(marqueCle, rang) {
    var base = CAPACITES[marqueCle];
    if (!base) return null;
    var n = base.n || 0;
    if (n && !base.fixe && rang >= 2) n += rang - 1;
    return {
      kw: base.kw || null, cri: base.cri || null, n: n, nom: base.nom, ico: base.ico,
      type: base.cri ? 'Cri de guerre' : 'Pouvoir',
      txt: base.txt(n),
      court: base.ico + ' ' + base.nom + (n && base.cri ? ' ' + n : '')
    };
  }
  var FAMILLES = {
    cegelec:  { nom: 'Cegelec',  couleur: '#d6001c', icone: '🔴', marques: ['cegelec', 'building-solutions', 'maintenance-energies', 'cegelec-nord'],
                desc: 'Boucliers, provocation et soins : un jeu solide.' },
    axians:   { nom: 'Axians',   couleur: '#7f3fd4', icone: '🟣', marques: ['axians'],
                desc: 'Pioche des cartes et domine la partie par le nombre.' },
    actemium: { nom: 'Actemium', couleur: '#9ccc0a', icone: '🟢', marques: ['actemium'],
                desc: 'Ruée : attaque dès l\'arrivée en jeu.' },
    omexom:   { nom: 'Omexom',   couleur: '#2d8ae0', icone: '🔷', marques: ['omexom-te', 'omexom-reseaux', 'citeos'],
                desc: 'De l\'énergie, des buffs et des éclairs.' }
  };

  var duel = null;
  function modeSync() { return window.DUEL_SYNC === true; }

  // --- une carte → ses stats de jeu
  function baseCarte(m) {
    var puiss = clamp(Number(m.puissance) || 20, 1, 100);
    var r = rareteDe(m);
    var cout = clamp(Math.round(puiss / 16) + r.rang - 1, 1, 8);
    var cap = capaciteInstance(m.marque, r.rang);
    var total = cout * 2 + 1;
    if (cap && total >= 4) total -= 1;
    total = Math.max(total, 2);
    var ratio = m.type === 'objet' ? 0.4 : (m.type === 'technicien' ? 0.5 : 0.55);
    var jitter = (total >= 5) ? (hash(String(m.nom)) % 3) - 1 : 0;
    var att = clamp(Math.round(total * ratio) + jitter, 1, total - 1);
    var marque = marqueDe(m);
    return {
      nom: m.nom, fonction: m.fonction || '', icone: m.icone || '', photo: m.photo || '',
      marqueCle: m.marque, marqueNom: marque.nom, couleur: marque.couleur, puissance: puiss,
      rarete: r, cout: cout, att: att, pv: total - att, cap: cap,
      forts: m.forts || [], faibles: m.faibles || [], devise: m.devise || ''
    };
  }
  function capCle(c) { return c.cap ? (c.cap.kw || c.cap.cri) + ':' + c.cap.n : '-'; }
  // Évite les doublons « mêmes stats + même pouvoir » : la carte la plus puissante garde ses stats,
  // les suivantes sont décalées au plus près (attaque/vie échangées, ou +1/-1 de total).
  function dedoublonner(cartes) {
    var vues = {};
    function sig(c, a, p) { return c.cout + '|' + a + '|' + p + '|' + capCle(c); }
    cartes.slice().sort(function (a, b) {
      return (b.rarete.rang - a.rarete.rang) || (b.puissance - a.puissance) || String(a.nom).localeCompare(String(b.nom), 'fr');
    }).forEach(function (c) {
      if (vues[sig(c, c.att, c.pv)]) {
        var total = c.att + c.pv, essais = [], k;
        [1, -1, 2, -2, 3, -3, 4, -4].forEach(function (d) { essais.push([c.att + d, total - c.att - d]); });
        [[c.att + 1, c.pv], [c.att, c.pv + 1], [c.att + 1, c.pv + 1], [c.att - 1, c.pv], [c.att, c.pv - 1],
         [c.att + 2, c.pv], [c.att, c.pv + 2], [c.att + 2, c.pv + 1], [c.att + 1, c.pv + 2]].forEach(function (x) { essais.push(x); });
        for (k = 0; k < essais.length; k++) {
          var a = essais[k][0], p = essais[k][1];
          if (a >= 1 && p >= 1 && !vues[sig(c, a, p)]) { c.att = a; c.pv = p; break; }
        }
      }
      vues[sig(c, c.att, c.pv)] = true;
    });
    return cartes;
  }
  var catalogueMemo = null;
  function catalogue() {
    var liste = window.EQUIPE || [];
    if (catalogueMemo && catalogueMemo.n === liste.length) return catalogueMemo.map;
    var cartes = dedoublonner(liste.map(baseCarte));
    var map = {};
    cartes.forEach(function (c) { map[c.nom] = c; });
    catalogueMemo = { n: liste.length, map: map };
    return map;
  }
  function carteDe(m) { return catalogue()[m.nom] || baseCarte(m); }
  // --- construction des paquets
  function construireDeck(familleCle) {
    var pool = (window.EQUIPE || []).map(carteDe);
    var deck = [], compte = {};
    function ajouter(c) {
      var max = c.rarete.rang === 3 ? 1 : 2;
      if ((compte[c.nom] || 0) >= max || deck.length >= D_DECK) return false;
      compte[c.nom] = (compte[c.nom] || 0) + 1;
      deck.push(c);
      return true;
    }
    pool.filter(function (c) { return c.marqueCle === 'vinci'; }).forEach(ajouter);   // CASTOR : dans tous les decks
    var fam = FAMILLES[familleCle];
    var propres = fam ? pool.filter(function (c) { return fam.marques.indexOf(c.marqueCle) !== -1; }) : [];
    melanger(propres);
    propres.forEach(ajouter);
    propres.forEach(ajouter);                                                           // deuxième exemplaire si besoin
    melanger(pool).forEach(ajouter);                                                    // complète avec d'autres cartes
    melanger(pool).forEach(ajouter);
    return melanger(deck);
  }

  // --- état
  function nouveauCote(cle, nom, icone, deck) {
    return { cle: cle, nom: nom, icone: icone, pv: D_PV, energieMax: 0, energie: 0, deck: deck, main: [], plateau: [], fatigue: 0 };
  }
  var idCompteur = 0;
  function creerUnite(c) {
    var cap = c.cap || {};
    return {
      id: ++idCompteur, carte: c, nom: c.nom, icone: c.icone, photo: c.photo, couleur: c.couleur, rarete: c.rarete,
      cout: c.cout, att: c.att, pv: c.pv, pvMax: c.pv,
      bouclier: cap.kw === 'bouclier', provocation: cap.kw === 'provocation', ruee: cap.kw === 'ruee',
      endormi: cap.kw !== 'ruee', aAttaque: false
    };
  }
  function log(msg) {
    duel.log.push(msg);
    if (duel.log.length > 5) duel.log.shift();
  }
  // Événements visuels : accumulés pendant la logique, joués par rendre()
  function fx(type, data) {
    if (!duel) return;
    var e = data || {};
    e.type = type;
    duel.fx.push(e);
  }
  function adversaire(cote) { return cote === duel.joueur ? duel.ia : duel.joueur; }

  function piocher(cote, n) {
    for (var i = 0; i < n; i++) {
      if (!cote.deck.length) {
        cote.fatigue++;
        blesser(cote, cote.fatigue);
        log(cote.nom + ' n\'a plus de cartes : ' + cote.fatigue + ' dégât(s) d\'épuisement.');
      } else {
        var c = cote.deck.pop();
        if (cote.main.length >= D_MAIN_MAX) log(cote.nom + ' a la main pleine : ' + c.nom + ' est perdue.');
        else { cote.main.push(c); fx('pioche', { cote: cote.cle }); }
      }
    }
  }
  function blesser(cote, n) {
    if (n <= 0) return;
    cote.pv -= n;
    fx('degats', { heros: cote.cle, n: n });
  }
  function soigner(cote, n) {
    var avant = cote.pv;
    cote.pv = Math.min(D_PV, cote.pv + n);
    if (cote.pv > avant) fx('soin', { heros: cote.cle, n: cote.pv - avant });
  }
  function infliger(unite, n) {
    if (n <= 0) return;
    if (unite.bouclier) { unite.bouclier = false; fx('bouclier', { id: unite.id }); return; }
    unite.pv -= n;
    fx('degats', { id: unite.id, n: n });
  }
  function nettoyer() {
    [duel.joueur, duel.ia].forEach(function (cote) {
      var reste = [];
      cote.plateau.forEach(function (u, idx) {
        if (u.pv <= 0) {
          log(u.nom + ' est hors service.');
          fx('mort', { cote: cote.cle, unite: u, idx: idx });
        } else reste.push(u);
      });
      cote.plateau = reste;
    });
    if (duel.sel && !duel.joueur.plateau.some(function (u) { return u.id === duel.sel; })) duel.sel = null;
  }
  function verifierFin() {
    if (duel.fini) return true;
    var j = duel.joueur.pv <= 0, a = duel.ia.pv <= 0;
    if (!j && !a) return false;
    duel.fini = a && j ? 'nul' : (a ? 'gagne' : 'perdu');
    duel.sel = null;
    return true;
  }

  // --- jouer une carte
  function peutJouer(cote, index) {
    var c = cote.main[index];
    return !!c && c.cout <= cote.energie && cote.plateau.length < D_PLATEAU_MAX;
  }
  function jouerCarte(cote, index) {
    if (!peutJouer(cote, index)) return false;
    var c = cote.main.splice(index, 1)[0];
    cote.energie -= c.cout;
    var u = creerUnite(c);
    cote.plateau.push(u);
    fx('pose', { id: u.id, cote: cote.cle });
    log(cote.nom + ' joue ' + c.nom + '.');
    appliquerCri(cote, u);
    nettoyer();
    verifierFin();
    return true;
  }
  function appliquerCri(cote, u) {
    var cap = u.carte.cap;
    if (!cap || !cap.cri) return;
    var adv = adversaire(cote);
    if (cap.cri === 'soin') {
      soigner(cote, cap.n);
      log(u.nom + ' : ' + cote.nom + ' récupère ' + cap.n + ' PV.');
    } else if (cap.cri === 'pioche') {
      piocher(cote, cap.n);
      log(u.nom + ' : ' + cote.nom + ' pioche ' + cap.n + ' carte' + (cap.n > 1 ? 's' : '') + '.');
    } else if (cap.cri === 'energie') {
      cote.energie = Math.min(D_ENERGIE_MAX, cote.energie + cap.n);
      log(u.nom + ' : +' + cap.n + ' énergie.');
    } else if (cap.cri === 'buff') {
      cote.plateau.forEach(function (x) { x.att += cap.n; fx('buff', { id: x.id }); });
      log(u.nom + ' : les serviteurs de ' + cote.nom + ' gagnent +' + cap.n + ' attaque.');
    } else if (cap.cri === 'heros') {
      blesser(adv, cap.n);
      log(u.nom + ' : ' + cap.n + ' dégâts à ' + adv.nom + '.');
    } else if (cap.cri === 'epargne') {
      cote.energieMax = Math.min(D_ENERGIE_MAX, cote.energieMax + cap.n);
      cote.energie = Math.min(D_ENERGIE_MAX, cote.energie + cap.n);
      log(u.nom + ' : +' + cap.n + ' cristaux d\'énergie maximum.');
    } else if (cap.cri === 'degats') {
      var cibles = adv.plateau.slice();
      var idx = Math.floor(Math.random() * (cibles.length + 1));
      if (idx === cibles.length) { blesser(adv, cap.n); log(u.nom + ' : ' + cap.n + ' dégâts à ' + adv.nom + '.'); }
      else { infliger(cibles[idx], cap.n); log(u.nom + ' : ' + cap.n + ' dégâts à ' + cibles[idx].nom + '.'); }
    }
  }

  // --- attaquer
  function ciblesValides(cote) {
    var adv = adversaire(cote);
    var taunts = adv.plateau.filter(function (u) { return u.provocation; });
    if (taunts.length) return { unites: taunts, heros: false };
    return { unites: adv.plateau.slice(), heros: true };
  }
  function peutAttaquer(u) { return !u.endormi && !u.aAttaque && u.att > 0; }
  // cible : une unité adverse, ou la chaîne 'heros'
  function attaquer(cote, attaquant, cible) {
    var adv = adversaire(cote);
    var valides = ciblesValides(cote);
    if (!peutAttaquer(attaquant)) return false;
    fx('attaque', { id: attaquant.id, cote: cote.cle });
    if (cible === 'heros') {
      if (!valides.heros) { duel.fx.pop(); return false; }
      blesser(adv, attaquant.att);
      log(attaquant.nom + ' attaque ' + adv.nom + ' (' + attaquant.att + ' dégâts).');
    } else {
      if (valides.unites.indexOf(cible) === -1) { duel.fx.pop(); return false; }
      var degatsRendus = cible.att;
      infliger(cible, attaquant.att);
      infliger(attaquant, degatsRendus);
      log(attaquant.nom + ' attaque ' + cible.nom + '.');
    }
    attaquant.aAttaque = true;
    nettoyer();
    verifierFin();
    return true;
  }

  // --- tours
  function debutTour(cote) {
    cote.energieMax = Math.min(D_ENERGIE_MAX, cote.energieMax + 1);
    cote.energie = cote.energieMax;
    cote.plateau.forEach(function (u) { u.endormi = false; u.aAttaque = false; });
    piocher(cote, 1);
    duel.banniere = cote === duel.joueur ? 'À toi de jouer !' : 'Tour du client exigeant';
  }
  function finDeTourJoueur() {
    if (!duel || duel.fini || duel.phase || duel.tour !== 'joueur') return;
    duel.sel = null;
    duel.tour = 'ia';
    log('Tour du client exigeant…');
    debutTour(duel.ia);
    nettoyer();
    if (verifierFin()) { rendre(); return; }
    rendre();
    planifierIA();
  }
  function planifierIA() {
    var partie = duel;   // si le joueur abandonne puis relance, les anciens timers s'arrêtent
    function pas() {
      if (!duel || duel !== partie || duel.fini) return;
      var fait = iaEtape();
      nettoyer();
      var fin = verifierFin();
      rendre();
      if (fin) return;
      if (fait) {
        if (modeSync()) pas(); else setTimeout(pas, 900);
        return;
      }
      duel.tour = 'joueur';
      duel.numTour++;
      debutTour(duel.joueur);
      nettoyer();
      log('À toi de jouer !');
      verifierFin();
      rendre();
    }
    if (modeSync()) pas(); else setTimeout(pas, 1100);
  }

  // --- intelligence artificielle : une action à la fois
  function iaEtape() {
    var ia = duel.ia, jo = duel.joueur;
    // 1. jouer la carte la plus chère possible
    var meilleure = -1;
    for (var i = 0; i < ia.main.length; i++) {
      if (peutJouer(ia, i) && (meilleure === -1 || ia.main[i].cout > ia.main[meilleure].cout)) meilleure = i;
    }
    if (meilleure !== -1) { jouerCarte(ia, meilleure); return true; }
    // 2. attaquer avec un serviteur prêt
    for (var k = 0; k < ia.plateau.length; k++) {
      var u = ia.plateau[k];
      if (!peutAttaquer(u)) continue;
      var v = ciblesValides(ia);
      var cible = 'heros';
      if (!v.heros) {
        v.unites.sort(function (a, b) { return a.pv - b.pv; });
        cible = v.unites[0];
      } else if (u.att >= jo.pv) {
        cible = 'heros';
      } else {
        var score = 0, choisie = null;
        v.unites.forEach(function (t) {
          var tue = !t.bouclier && u.att >= t.pv;
          var survit = u.bouclier || t.att < u.pv;
          var s = -1;
          if (tue && survit) s = 10 + t.cout;
          else if (tue && t.cout >= u.cout) s = 4 + t.cout - u.cout;
          if (s > score) { score = s; choisie = t; }
        });
        if (choisie) cible = choisie;
      }
      attaquer(ia, u, cible);
      return true;
    }
    return false;
  }

  // --- démarrage et choix des cartes à changer (mulligan)
  function lancerDuel(familleCle) {
    var cles = Object.keys(FAMILLES);
    var familleIA = cles[Math.floor(Math.random() * cles.length)];
    duel = {
      joueur: nouveauCote('joueur', 'Toi', '🧑‍🔧', construireDeck(familleCle)),
      ia: nouveauCote('ia', 'Le client exigeant', '🧐', construireDeck(familleIA)),
      tour: 'joueur', numTour: 1, sel: null, fini: null, log: [], familleJoueur: familleCle,
      phase: 'mulligan', mull: {}, fx: [], banniere: null, confettis: false
    };
    piocher(duel.joueur, 3);
    piocher(duel.ia, 4);
    duel.fx = [];
    $('d-choix').hidden = true;
    $('d-table').hidden = false;
    rendre();
  }
  // Remplace les cartes marquées : on pioche d'abord, puis on remet les anciennes dans le paquet.
  function remplacerCartes(cote, indices) {
    var gardees = [], rendues = [];
    cote.main.forEach(function (c, i) { (indices[i] ? rendues : gardees).push(c); });
    var n = rendues.length;
    for (var k = 0; k < n; k++) { if (cote.deck.length) gardees.push(cote.deck.pop()); }
    rendues.forEach(function (c) { cote.deck.push(c); });
    melanger(cote.deck);
    cote.main = gardees;
    return n;
  }
  function validerMulligan() {
    if (!duel || duel.phase !== 'mulligan') return;
    var n = remplacerCartes(duel.joueur, duel.mull);
    // le client exigeant change ses cartes trop chères
    var aRemplacer = {};
    duel.ia.main.forEach(function (c, i) { if (c.cout >= 5) aRemplacer[i] = true; });
    remplacerCartes(duel.ia, aRemplacer);
    duel.phase = null;
    duel.mull = {};
    duel.fx = [];
    log(n ? 'Tu changes ' + n + ' carte' + (n > 1 ? 's' : '') + '.' : 'Tu gardes ta main.');
    debutTour(duel.joueur);
    log('La partie commence ! À toi de jouer.');
    rendre();
  }
  function retourChoix() {
    duel = null;
    $('d-table').hidden = true;
    $('d-choix').hidden = false;
    var cf = $('d-confettis'); if (cf) vider(cf);
  }

  // --- interactions du joueur
  function peutAgir() { return duel && !duel.fini && !duel.phase && duel.tour === 'joueur'; }
  function clicMain(index) {
    if (!peutAgir()) return;
    if (jouerCarte(duel.joueur, index)) { duel.sel = null; rendre(); }
  }
  function clicUniteJoueur(u) {
    if (!peutAgir()) return;
    if (!peutAttaquer(u)) return;
    duel.sel = duel.sel === u.id ? null : u.id;
    rendre();
  }
  function selectionnee() {
    if (!duel || !duel.sel) return null;
    for (var i = 0; i < duel.joueur.plateau.length; i++) if (duel.joueur.plateau[i].id === duel.sel) return duel.joueur.plateau[i];
    return null;
  }
  function clicCible(cible) {
    var s = selectionnee();
    if (!s || !peutAgir()) return;
    if (attaquer(duel.joueur, s, cible)) duel.sel = null;
    rendre();
  }

  // --- affichage
  function descriptionCarte(c) {
    var l = [c.nom + ' — ' + c.rarete.nom + ' · ' + c.marqueNom];
    if (c.fonction) l.push(c.fonction);
    l.push('Coût ' + c.cout + ' · Attaque ' + c.att + ' · Vie ' + c.pv);
    if (c.cap) l.push(c.cap.ico + ' ' + c.cap.type + ' — ' + c.cap.nom + (c.cap.n && c.cap.cri ? ' ' + c.cap.n : '') + ' : ' + c.cap.txt);
    if (c.forts.length) l.push('▲ ' + c.forts.join(' · '));
    if (c.faibles.length) l.push('▼ ' + c.faibles.join(' · '));
    return l.join('\n');
  }
  function carteEl(o, opts) {
    // o : carte (en main) ou unité (sur le terrain) ; opts : { classes, onclick, titre }
    var el = document.createElement('div');
    el.className = 'hs ' + o.rarete.cls + (opts.classes ? ' ' + opts.classes : '');
    el.style.setProperty('--m', o.couleur);
    if (o.id) el.setAttribute('data-id', o.id);
    if (opts.titre) el.title = opts.titre;
    el.appendChild(texte('span', 'cout', String(o.cout)));
    var art = document.createElement('div');
    art.className = 'art';
    var c = o.carte || o;
    if (c.photo) { var im = document.createElement('img'); im.src = c.photo; im.alt = ''; art.appendChild(im); }
    else art.textContent = c.icone || initiales(c.nom);
    el.appendChild(art);
    el.appendChild(texte('div', 'nom', o.nom));
    var cap = c.cap;
    // Cri de guerre : visible tant que la carte est en main. Pouvoir : visible aussi sur le terrain.
    if (cap && (cap.kw || !o.carte)) {
      var bandeau = document.createElement('div');
      bandeau.className = 'cap ' + (cap.cri ? 'cri' : 'pouvoir');
      bandeau.appendChild(texte('span', 'cap-type', cap.type));
      bandeau.appendChild(texte('span', 'cap-effet', cap.court));
      el.appendChild(bandeau);
      el.classList.add(cap.cri ? 'a-cri' : 'a-pouvoir');
    }
    el.appendChild(texte('span', 'att', String(o.att)));
    el.appendChild(texte('span', 'pv', String(o.pv)));
    if (opts.onclick) el.addEventListener('click', opts.onclick);
    return el;
  }
  function herosEl(cote, estIA, cible) {
    var el = document.createElement('div');
    el.className = 'heros' + (cible ? ' cible' : '');
    el.setAttribute('data-cote', cote.cle);
    el.appendChild(texte('span', 'heros-avatar', cote.icone));
    var info = document.createElement('div');
    info.appendChild(texte('div', 'heros-nom', cote.nom));
    var st = document.createElement('div');
    st.className = 'heros-stats';
    st.appendChild(texte('span', 'heros-pv', '❤ ' + Math.max(0, cote.pv)));
    st.appendChild(texte('span', 'heros-energie', '⚡ ' + cote.energie + '/' + cote.energieMax));
    var pile = texte('span', 'pile-dos', String(cote.deck.length));
    pile.title = 'Cartes restantes dans la pioche';
    st.appendChild(pile);
    info.appendChild(st);
    el.appendChild(info);
    if (estIA && cible) el.addEventListener('click', function () { clicCible('heros'); });
    return el;
  }

  // --- animations
  function flotter(el, valeur, cls) {
    var n = texte('span', 'fx-nombre ' + cls, valeur);
    el.appendChild(n);
    setTimeout(function () { if (n.parentNode) n.parentNode.removeChild(n); }, 1000);
  }
  function appliquerFx() {
    var evs = duel.fx;
    duel.fx = [];
    evs.forEach(function (e) {
      var el = null;
      if (e.id) el = document.querySelector('[data-id="' + e.id + '"]');
      if (e.heros) el = document.querySelector('.heros[data-cote="' + e.heros + '"]');
      if (e.type === 'pose' && el) el.classList.add('anim-pose');
      else if (e.type === 'attaque' && el) el.classList.add(e.cote === 'joueur' ? 'anim-attaque-haut' : 'anim-attaque-bas');
      else if (e.type === 'degats' && el) { el.classList.add('anim-touche'); flotter(el, '-' + e.n, 'degats'); }
      else if (e.type === 'soin' && el) flotter(el, '+' + e.n, 'soin');
      else if (e.type === 'bouclier' && el) el.classList.add('anim-bouclier');
      else if (e.type === 'buff' && el) el.classList.add('anim-buff');
      else if (e.type === 'pioche' && e.cote === 'joueur') {
        var main = $('d-joueur-main');
        if (main && main.lastChild && main.lastChild.classList) main.lastChild.classList.add('anim-pioche');
      } else if (e.type === 'mort') {
        var zone = $(e.cote === 'joueur' ? 'd-joueur-plateau' : 'd-ia-plateau');
        var fant = carteEl(e.unite, { classes: 'mort' });
        fant.removeAttribute('data-id');
        var ref = zone.children[e.idx] || null;
        zone.insertBefore(fant, ref);
      }
    });
  }
  function banniere(txt) {
    var b = $('d-banniere');
    if (!b) return;
    b.textContent = txt;
    b.classList.remove('banniere-go');
    void b.offsetWidth;
    b.classList.add('banniere-go');
  }
  function lancerConfettis() {
    var cf = $('d-confettis');
    if (!cf) return;
    vider(cf);
    var couleurs = ['#d6001c', '#7f3fd4', '#9ccc0a', '#2d8ae0', '#f0b429'];
    for (var i = 0; i < 48; i++) {
      var p = document.createElement('i');
      p.style.setProperty('--x', Math.round(Math.random() * 100) + '%');
      p.style.setProperty('--d', (Math.random() * 0.9).toFixed(2) + 's');
      p.style.setProperty('--k', couleurs[i % couleurs.length]);
      cf.appendChild(p);
    }
  }

  function rendreMulligan() {
    var zone = $('d-mull-main'); vider(zone);
    var n = 0;
    duel.joueur.main.forEach(function (c, idx) {
      var marque = !!duel.mull[idx];
      if (marque) n++;
      var el = carteEl(c, {
        classes: 'mull' + (marque ? ' a-remplacer' : ''), titre: descriptionCarte(c),
        onclick: function () { duel.mull[idx] = !duel.mull[idx]; rendre(); }
      });
      if (marque) el.appendChild(texte('span', 'mull-etiquette', 'Remplacer'));
      zone.appendChild(el);
    });
    $('d-mulligan-ok').textContent = n ? 'Remplacer ' + n + ' carte' + (n > 1 ? 's' : '') + ' et commencer' : 'Garder cette main et commencer';
  }

  function rendre() {
    if (!duel) return;
    var enMull = duel.phase === 'mulligan';
    $('d-mulligan').hidden = !enMull;
    $('d-jeu-zone').hidden = enMull;
    if (enMull) {
      rendreMulligan();
      $('d-tour').textContent = 'Choix des cartes de départ';
      $('d-fin-tour').disabled = true;
      return;
    }
    var s = selectionnee();
    var v = s ? ciblesValides(duel.joueur) : { unites: [], heros: false };
    var tourJoueur = peutAgir();

    var zIA = $('d-ia-heros'); vider(zIA);
    zIA.appendChild(herosEl(duel.ia, true, !!s && v.heros));
    var mIA = $('d-ia-main'); vider(mIA);
    for (var i = 0; i < duel.ia.main.length; i++) mIA.appendChild(texte('span', 'dos-mini', ''));

    var pIA = $('d-ia-plateau'); vider(pIA);
    duel.ia.plateau.forEach(function (u) {
      var cl = [];
      if (u.provocation) cl.push('provocation');
      if (u.bouclier) cl.push('bouclier');
      if (s && v.unites.indexOf(u) !== -1) cl.push('cible');
      pIA.appendChild(carteEl(u, {
        classes: cl.join(' '), titre: descriptionCarte(u.carte),
        onclick: (s && v.unites.indexOf(u) !== -1) ? function () { clicCible(u); } : null
      }));
    });

    var pJ = $('d-joueur-plateau'); vider(pJ);
    duel.joueur.plateau.forEach(function (u) {
      var cl = [];
      if (u.provocation) cl.push('provocation');
      if (u.bouclier) cl.push('bouclier');
      if (u.endormi) cl.push('endormi');
      if (tourJoueur && peutAttaquer(u)) cl.push('pret');
      if (duel.sel === u.id) cl.push('selection');
      pJ.appendChild(carteEl(u, { classes: cl.join(' '), titre: descriptionCarte(u.carte), onclick: function () { clicUniteJoueur(u); } }));
    });

    var zJ = $('d-joueur-heros'); vider(zJ);
    zJ.appendChild(herosEl(duel.joueur, false, false));

    var mJ = $('d-joueur-main'); vider(mJ);
    duel.joueur.main.forEach(function (c, idx) {
      var cl = (tourJoueur && peutJouer(duel.joueur, idx)) ? 'jouable' : '';
      mJ.appendChild(carteEl(c, { classes: cl, titre: descriptionCarte(c), onclick: function () { clicMain(idx); } }));
    });

    $('d-log').textContent = duel.log.join('  ·  ');
    $('d-tour').textContent = duel.fini ? 'Partie terminée' : (duel.tour === 'joueur' ? 'Tour ' + duel.numTour + ' : à toi !' : 'Tour du client exigeant…');
    $('d-fin-tour').disabled = !tourJoueur;

    appliquerFx();
    if (duel.banniere && !duel.fini) { banniere(duel.banniere); duel.banniere = null; }

    var fin = $('d-fin');
    if (duel.fini) {
      var msgs = { gagne: '🏆 Victoire ! Le client exigeant est satisfait… et vaincu.', perdu: '😅 Défaite ! Le client exigeant a eu le dernier mot.', nul: '🤝 Égalité parfaite !' };
      $('d-message').textContent = msgs[duel.fini];
      fin.hidden = false;
      if (duel.fini === 'gagne' && !duel.confettis) { duel.confettis = true; lancerConfettis(); }
    } else {
      fin.hidden = true;
    }
  }

  // --- liaison des boutons
  (function duelInit() {
    var boite = $('d-familles');
    Object.keys(FAMILLES).forEach(function (cle) {
      var f = FAMILLES[cle];
      var b = document.createElement('button');
      b.type = 'button'; b.className = 'duel-famille';
      b.style.setProperty('--f', f.couleur);
      b.appendChild(texte('span', 'ico', f.icone));
      b.appendChild(texte('strong', '', f.nom));
      b.appendChild(texte('small', '', f.desc));
      b.addEventListener('click', function () { lancerDuel(cle); });
      boite.appendChild(b);
    });
    var surprise = document.createElement('button');
    surprise.type = 'button'; surprise.className = 'duel-famille';
    surprise.style.setProperty('--f', '#d9b44a');
    surprise.appendChild(texte('span', 'ico', '🎲'));
    surprise.appendChild(texte('strong', '', 'Deck surprise'));
    surprise.appendChild(texte('small', '', 'Vingt cartes au hasard dans toute la collection.'));
    surprise.addEventListener('click', function () { lancerDuel(null); });
    boite.appendChild(surprise);

    $('d-fin-tour').addEventListener('click', finDeTourJoueur);
    $('d-abandon').addEventListener('click', retourChoix);
    $('d-mulligan-ok').addEventListener('click', validerMulligan);
    $('d-rejouer').addEventListener('click', function () { lancerDuel(duel ? duel.familleJoueur : null); });
    $('d-menu').addEventListener('click', retourChoix);
  })();
  // ============================================================ 2. PAIRES
  var pEtat;
  function pNouvelle() {
    var liste = (window.COLLEGUES || []).slice(0, 12);
    var grille = $('p-grille');
    if (pEtat && pEtat.timer) clearInterval(pEtat.timer);
    $('p-fin').hidden = true;
    vider(grille);
    if (liste.length < 2) { grille.textContent = 'Ajoute au moins 2 collègues dans collegues.js.'; return; }
    pEtat = { ouvertes: [], coups: 0, trouvees: 0, total: liste.length, debut: null, timer: null, verrou: false };
    var cartes = [];
    liste.forEach(function (c, i) { cartes.push({ c: c, m: MARQUES[i % 4] }); cartes.push({ c: c, m: MARQUES[i % 4] }); });
    melanger(cartes).forEach(function (x) {
      var b = document.createElement('button');
      b.type = 'button'; b.className = 'pcarte';
      b.dataset.nom = x.c.nom;
      b.setAttribute('aria-label', 'Carte retournée');
      b.style.setProperty('--m', x.m);
      var int = document.createElement('span'); int.className = 'int';
      var dos = document.createElement('span'); dos.className = 'dos';
      var logo = document.createElement('img'); logo.src = 'assets/logo_cegelec.jpg'; logo.alt = '';
      dos.appendChild(logo);
      var face = document.createElement('span'); face.className = 'face';
      var portrait = document.createElement('span'); portrait.className = 'portrait';
      if (x.c.photo) { var im = document.createElement('img'); im.src = x.c.photo; im.alt = x.c.nom; portrait.appendChild(im); }
      else { portrait.textContent = initiales(x.c.nom); }
      var nom = document.createElement('span'); nom.className = 'nom'; nom.textContent = x.c.nom;
      face.appendChild(portrait); face.appendChild(nom);
      int.appendChild(dos); int.appendChild(face); b.appendChild(int);
      b.addEventListener('click', function () { pRetourner(b); });
      grille.appendChild(b);
    });
    pInfos();
    var r = parseInt(lire('cegelec-paires-record', ''), 10);
    $('p-record').textContent = r ? r + ' coups' : '—';
  }
  function pInfos() {
    $('p-coups').textContent = pEtat.coups;
    $('p-temps').textContent = formatTemps(pEtat.debut ? Math.floor((Date.now() - pEtat.debut) / 1000) : 0);
  }
  function pRetourner(b) {
    if (pEtat.verrou || b.classList.contains('ouverte') || b.classList.contains('trouvee')) return;
    if (!pEtat.debut) { pEtat.debut = Date.now(); pEtat.timer = setInterval(pInfos, 500); }
    b.classList.add('ouverte');
    b.setAttribute('aria-label', b.dataset.nom);
    pEtat.ouvertes.push(b);
    if (pEtat.ouvertes.length < 2) return;
    pEtat.coups++; pEtat.verrou = true;
    var a = pEtat.ouvertes[0], c = pEtat.ouvertes[1];
    if (a.dataset.nom === c.dataset.nom) {
      a.classList.add('trouvee'); c.classList.add('trouvee');
      pEtat.trouvees++; pEtat.ouvertes = []; pEtat.verrou = false; pInfos();
      if (pEtat.trouvees === pEtat.total) pTerminer();
    } else {
      pInfos();
      setTimeout(function () {
        a.classList.remove('ouverte'); c.classList.remove('ouverte');
        a.setAttribute('aria-label', 'Carte retournée'); c.setAttribute('aria-label', 'Carte retournée');
        pEtat.ouvertes = []; pEtat.verrou = false;
      }, 900);
    }
  }
  function pTerminer() {
    clearInterval(pEtat.timer);
    var s = Math.floor((Date.now() - pEtat.debut) / 1000);
    var r = parseInt(lire('cegelec-paires-record', ''), 10);
    var msg = 'Bravo ! Toutes les paires trouvées en ' + pEtat.coups + ' coups et ' + formatTemps(s) + '.';
    if (!r || pEtat.coups < r) { ecrire('cegelec-paires-record', pEtat.coups); msg += ' Nouveau record !'; $('p-record').textContent = pEtat.coups + ' coups'; }
    $('p-fin').textContent = msg; $('p-fin').hidden = false;
  }
  $('p-nouvelle').addEventListener('click', pNouvelle);

  // ============================================================ 3. BIBLIOTHÈQUE DE CARTES
  function liste(cls, items) {
    var ul = document.createElement('ul'); ul.className = cls;
    (items || []).forEach(function (t) { ul.appendChild(texte('li', '', t)); });
    return ul;
  }
  function carteTcg(m, numero, total) {
    var marque = marqueDe(m);
    var r = rareteDe(m);
    var typeInfo = TYPES[m.type] || { nom: '', utilite: false };
    var p = clamp(Number(m.puissance) || 0, 1, 100);
    var art = document.createElement('article');
    art.className = 'tcg ' + r.cls;
    art.style.setProperty('--m', marque.couleur);

    var haut = document.createElement('div');
    haut.className = 'tcg-haut' + (marque.clair ? ' clair' : '');
    haut.appendChild(texte('span', '', marque.nom));
    haut.appendChild(texte('span', 'tcg-num', numero + ' / ' + total));
    art.appendChild(haut);

    var portrait = document.createElement('div');
    portrait.className = 'tcg-portrait';
    if (m.photo) {
      var img = document.createElement('img'); img.src = m.photo; img.alt = m.nom; img.loading = 'lazy';
      portrait.appendChild(img);
    } else if (m.icone) {
      portrait.textContent = m.icone;
      portrait.style.fontSize = '4.2rem';
    } else {
      portrait.textContent = initiales(m.nom);
    }
    portrait.appendChild(texte('span', 'tcg-rarete', r.nom));
    art.appendChild(portrait);

    var corps = document.createElement('div');
    corps.className = 'tcg-corps';
    corps.appendChild(texte('h3', '', m.nom || ''));
    corps.appendChild(texte('div', 'tcg-fonction', (typeInfo.nom ? typeInfo.nom + ' · ' : '') + (m.fonction || '')));

    var puiss = document.createElement('div');
    puiss.className = 'tcg-puissance';
    puiss.appendChild(texte('span', '', typeInfo.utilite ? 'Utilité' : 'Puissance'));
    var barre = document.createElement('span'); barre.className = 'tcg-barre';
    var i = document.createElement('i'); i.style.width = p + '%'; barre.appendChild(i);
    puiss.appendChild(barre);
    puiss.appendChild(texte('b', '', String(p)));
    corps.appendChild(puiss);

    // Statistiques et capacité telles qu'elles sont en jeu dans le Duel des chantiers
    var jc = carteDe(m);
    var stats = document.createElement('div');
    stats.className = 'tcg-stats';
    stats.title = 'Statistiques dans le Duel des chantiers';
    stats.appendChild(texte('span', 'st-cout', '⚡ ' + jc.cout));
    stats.appendChild(texte('span', 'st-att', '⚔ ' + jc.att));
    stats.appendChild(texte('span', 'st-pv', '❤ ' + jc.pv));
    corps.appendChild(stats);
    if (jc.cap) {
      var cp = document.createElement('div');
      cp.className = 'tcg-cap ' + (jc.cap.cri ? 'cri' : 'pouvoir');
      cp.appendChild(texte('span', 'tcg-cap-type', jc.cap.type));
      cp.appendChild(texte('strong', '', jc.cap.ico + ' ' + jc.cap.nom + (jc.cap.n && jc.cap.cri ? ' ' + jc.cap.n : '')));
      cp.appendChild(texte('span', 'tcg-cap-txt', jc.cap.txt));
      corps.appendChild(cp);
    }

    if (m.forts && m.forts.length) { corps.appendChild(texte('div', 'tcg-titre', 'Points forts')); corps.appendChild(liste('forts', m.forts)); }
    if (m.faibles && m.faibles.length) { corps.appendChild(texte('div', 'tcg-titre', 'Points faibles')); corps.appendChild(liste('faibles', m.faibles)); }
    if (m.devise) corps.appendChild(texte('div', 'tcg-devise', '« ' + m.devise + ' »'));
    art.appendChild(corps);
    return art;
  }

  var bibListe = $('bib-liste');
  function bibRendre() {
    var tout = (window.EQUIPE || []).slice();
    var fm = $('bib-marque').value, fr = $('bib-rarete').value, ft = $('bib-type').value, tri = $('bib-tri').value;
    var vues = tout.filter(function (m) {
      return (!fm || m.marque === fm) && (!fr || rareteDe(m).nom === fr) && (!ft || m.type === ft);
    });
    vues.sort(function (a, b) {
      if (tri === 'nom') return String(a.nom).localeCompare(String(b.nom), 'fr');
      if (tri === 'marque') return String(a.marque).localeCompare(String(b.marque)) || (b.puissance - a.puissance);
      return (b.puissance || 0) - (a.puissance || 0);
    });
    vider(bibListe);
    $('bib-nb').textContent = vues.length + ' / ' + tout.length;
    if (!vues.length) { bibListe.appendChild(texte('p', 'biblio-vide', 'Aucune carte ne correspond à ces filtres.')); return; }
    vues.forEach(function (m, idx) { bibListe.appendChild(carteTcg(m, idx + 1, vues.length)); });
    bibListe.scrollLeft = 0;
  }
  (function bibInit() {
    var sel = $('bib-marque');
    Object.keys(MARQUES_BIB).forEach(function (k) {
      var o = document.createElement('option'); o.value = k; o.textContent = MARQUES_BIB[k].nom; sel.appendChild(o);
    });
    ['bib-marque', 'bib-rarete', 'bib-type', 'bib-tri'].forEach(function (id) { $(id).addEventListener('change', bibRendre); });
    function defiler(sens) {
      if (bibListe.scrollBy) bibListe.scrollBy({ left: sens * 268, behavior: 'smooth' });
      else bibListe.scrollLeft += sens * 268;
    }
    $('bib-prec').addEventListener('click', function () { defiler(-1); });
    $('bib-suiv').addEventListener('click', function () { defiler(1); });
    bibListe.addEventListener('keydown', function (ev) {
      if (ev.key === 'ArrowRight') { defiler(1); ev.preventDefault(); }
      if (ev.key === 'ArrowLeft') { defiler(-1); ev.preventDefault(); }
    });
    bibRendre();
  })();

  // ============================================================ 4. DOS DE CARTES
  var DOS = [
    { cle: 'quatre', nom: 'Quatre marques' }, { cle: 'cegelec', nom: 'Rouge Cegelec' }, { cle: 'circuit', nom: 'Circuit' },
    { cle: 'chantier', nom: 'Chantier' }, { cle: 'lagon', nom: 'Lagon' }, { cle: 'foudre', nom: 'Foudre' },
    { cle: 'castor', nom: 'Castor doré' }
  ];
  (function dosInit() {
    var boite = $('dos-choix');
    if (!boite) return;
    function appliquer(cle) {
      document.body.setAttribute('data-dos', cle);
      Array.prototype.forEach.call(boite.querySelectorAll('.pastille'), function (b) {
        b.classList.toggle('actif', b.getAttribute('data-cle') === cle);
      });
      ecrire('cegelec-dos', cle);
    }
    DOS.forEach(function (d) {
      var b = document.createElement('button');
      b.type = 'button';
      b.className = 'pastille s-' + d.cle;
      b.setAttribute('data-cle', d.cle);
      b.title = 'Dos « ' + d.nom + ' »';
      b.setAttribute('aria-label', 'Dos de carte ' + d.nom);
      b.addEventListener('click', function () { appliquer(d.cle); });
      boite.appendChild(b);
    });
    var choisi = lire('cegelec-dos', 'quatre');
    var valide = DOS.some(function (d) { return d.cle === choisi; });
    appliquer(valide ? choisi : 'quatre');
  })();
  // ------------------------------------------------------------ démarrage
  pNouvelle();
})();
