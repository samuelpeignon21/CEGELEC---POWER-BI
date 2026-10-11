// Cartes OBJETS : équipements et techniques des métiers de chaque entité.
// Elles s'ajoutent à la liste de equipe.js (même format). La rareté de chaque objet est évaluée en bas de ce fichier.
// « puissance » représente ici l'utilité de l'objet (1 à 100).
function objet(marque, icone, nom, fonction, puissance, forts, faibles, devise) {
  return { type: "objet", marque: marque, icone: icone, nom: nom, fonction: fonction, puissance: puissance, forts: forts, faibles: faibles, devise: devise };
}

window.EQUIPE = (window.EQUIPE || []).concat([

  // ───────── Cegelec : matériel de tous les jours ─────────
  objet("cegelec", "🔌", "Câble électrique", "Distribution d'énergie", 55, ["Amène le courant partout", "Se déroule sans fin"], ["Jamais assez long"], "Le courant passe."),
  objet("cegelec", "⛑️", "Casque de chantier", "Équipement de protection", 50, ["Protège la tête", "Obligatoire partout"], ["Laisse une marque sur le front"], "Sécurité d'abord."),
  objet("cegelec", "🦺", "Gilet haute visibilité", "Équipement de protection", 38, ["Se voit de loin", "Toujours à portée"], ["Jamais à la bonne taille"], "On me voit, donc on m'évite."),
  objet("cegelec", "📟", "Multimètre", "Instrument de mesure", 58, ["Ne ment jamais", "Mesure tout"], ["Pile toujours à plat"], "Tension ? Je vérifie."),
  objet("cegelec", "🗄️", "Tableau électrique", "Distribution BT", 62, ["Cœur du bâtiment", "Protège les circuits"], ["Étiquettes introuvables"], "Un disjoncteur, une histoire."),
  objet("cegelec", "🪜", "Échelle", "Matériel d'accès", 30, ["Monte partout", "Légère"], ["Toujours dans l'autre camion"], "Un pas après l'autre."),
  objet("cegelec", "📱", "Tablette de chantier", "Suivi et rapports", 44, ["Plans dans la poche", "Photos immédiates"], ["Batterie capricieuse au soleil"], "Tout le dossier dans la main."),
  objet("cegelec", "🪫", "Rallonge de chantier", "Alimentation provisoire", 28, ["Dépanne tout le monde"], ["S'enroule en nœud"], "Un mètre de plus."),

  // ───────── Actemium : industrie et process ─────────
  objet("actemium", "🤖", "Automate programmable", "Contrôle commande", 80, ["Pilote toute la ligne", "Jamais fatigué"], ["Ne pardonne pas une virgule"], "Je fais tourner l'usine."),
  objet("actemium", "⚙️", "Variateur de vitesse", "Câblage process", 66, ["Économise l'énergie", "Démarrage en douceur"], ["Chauffe en été"], "Ni trop vite, ni trop lent."),
  objet("actemium", "🌡️", "Capteur d'instrumentation", "Instrumentation", 52, ["Mesure en continu", "Précis"], ["Se dérègle au pire moment"], "Je sens tout."),
  objet("actemium", "🔧", "Tuyauterie industrielle", "Fluides de process", 48, ["Transporte les fluides", "Solide"], ["Impossible à déplacer"], "Ça coule de source."),
  objet("actemium", "🗃️", "Armoire de commande", "Contrôle commande", 64, ["Tout est câblé", "Accès centralisé"], ["Porte qui grince"], "Le cerveau de la machine."),
  objet("actemium", "🖥️", "Écran de supervision", "Supervision et MES", 60, ["Vue d'ensemble de l'usine", "Alarmes claires"], ["Trop de voyants rouges"], "Je vois tout."),
  objet("actemium", "⚡", "Poste de transformation HTA", "Courants forts", 78, ["Abaisse la tension", "Fiable"], ["Ronronne"], "Du haut vers le bas."),
  objet("actemium", "📐", "Plan CAO/DAO", "Ingénierie électrique", 40, ["Précis au millimètre", "Base de tout projet"], ["Mise à jour tardive"], "Dessine, puis construis."),
  objet("actemium", "💡", "Éclairage industriel", "Courants forts", 42, ["Éclaire les ateliers", "Robuste"], ["Ampoule jamais de rechange"], "Que la lumière soit."),

  // ───────── Axians : ICT, réseaux, téléphonie ─────────
  objet("axians", "📶", "Borne wifi", "Réseau sans fil", 56, ["Couvre tout l'établissement", "Discrète au plafond"], ["Capricieuse près du béton"], "Connecté partout."),
  objet("axians", "🔀", "Switch d'accès", "Infrastructure réseau", 60, ["Aiguille les données", "Beaucoup de ports"], ["Un seul câble débranché, et c'est la panique"], "Chaque port compte."),
  objet("axians", "🛡️", "Firewall", "Cybersécurité", 82, ["Bloque les intrus", "Surveille jour et nuit"], ["Bloque aussi les gentils"], "Tu ne passeras pas."),
  objet("axians", "🗄️", "Baie de brassage", "Local technique", 54, ["Tout est rangé", "Étiquetée"], ["Un seul câble déplacé suffit à tout casser"], "Ordre et câbles."),
  objet("axians", "🧵", "Fibre optique", "Câblage fibre", 74, ["Débit énorme", "Fine comme un cheveu"], ["Ne supporte pas d'être pliée"], "À la vitesse de la lumière."),
  objet("axians", "🔬", "Soudeuse de fibre", "Outillage fibre", 62, ["Raccords invisibles", "Précision extrême"], ["Cale qui demande du calme"], "Je soude le futur."),
  objet("axians", "📡", "Borne DECT", "Téléphonie mobile", 36, ["Couvre le bâtiment", "Autonome"], ["Zones d'ombre"], "Je capte, donc je suis."),
  objet("axians", "🖥️", "Serveur", "Infrastructure IT", 72, ["Héberge les applications", "Redondant"], ["Ventilateur bruyant"], "Toujours en ligne."),
  objet("axians", "☁️", "Data center", "Stockage et cloud", 85, ["Stocke tout", "Refroidi en permanence"], ["Facture d'électricité record"], "Les données dorment ici."),
  objet("axians", "📺", "Terminal multimédia", "Divertissement patient", 25, ["Divertit les patients", "Simple d'usage"], ["Télécommande disparue"], "Un écran, une pause."),

  // ───────── Cegelec Maintenance Énergies ─────────
  objet("maintenance-energies", "❄️", "Climatisation split", "Climatisation individuelle", 55, ["Rafraîchit en minutes", "Silencieuse"], ["Filtre à nettoyer"], "Garde ton calme."),
  objet("maintenance-energies", "🌬️", "Centrale de traitement d'air", "Climatisation, ventilation", 70, ["Renouvelle l'air", "Gère l'humidité"], ["Énorme"], "Respire."),
  objet("maintenance-energies", "🧊", "Chambre froide", "Froid", 48, ["Conserve tout", "Isolée"], ["Porte qui reste ouverte"], "Cool, tout simplement."),
  objet("maintenance-energies", "🔋", "Onduleur", "Alimentation de secours", 76, ["Prend le relais en une seconde", "Sauve les données"], ["Batterie qui vieillit"], "Même quand ça coupe."),
  objet("maintenance-energies", "🔲", "TGBT", "Courants forts", 74, ["Distribue l'énergie du bâtiment", "Protège l'installation"], ["Ne pas toucher"], "Tableau général, rôle général."),
  objet("maintenance-energies", "🔥", "Détecteur incendie", "Système incendie", 66, ["Alerte tôt", "Toujours à l'affût"], ["Se déclenche avec un grille-pain"], "Je sens la fumée."),
  objet("maintenance-energies", "🔐", "Contrôle d'accès", "Courants faibles", 50, ["Filtre les entrées", "Garde une trace"], ["Badge oublié"], "Badge, s'il vous plaît."),
  objet("maintenance-energies", "📹", "Caméra de vidéosurveillance", "Courants faibles", 46, ["Voit tout", "Veille 24 h/24"], ["Angle mort à gauche"], "Je regarde."),
  objet("maintenance-energies", "🔔", "Appel malade", "Courants faibles", 34, ["Prévient immédiatement", "Rassure"], ["Sonne souvent pour rien"], "Un bouton, une présence."),

  // ───────── Cegelec Building Solutions ─────────
  objet("building-solutions", "🌀", "Système VRV", "Climatisation à détente directe", 68, ["Climatise plusieurs zones", "Économe"], ["Complexe à régler"], "Un groupe, plusieurs pièces."),
  objet("building-solutions", "💧", "Groupe d'eau glacée", "Climatisation à eau", 72, ["Refroidit de grands bâtiments", "Puissant"], ["Gros et lourd"], "L'eau qui rafraîchit."),
  objet("building-solutions", "⛽", "Groupe électrogène", "Alimentation de secours", 70, ["Démarre en cas de coupure", "Autonome"], ["Bruyant", "Aime le gasoil"], "Je prends le relais."),
  objet("building-solutions", "💨", "Désenfumage", "Sécurité incendie", 58, ["Évacue les fumées", "Protège les couloirs"], ["On l'oublie jusqu'au jour J"], "Sortie dégagée."),
  objet("building-solutions", "🔊", "Sonorisation", "Courants faibles", 32, ["Annonce partout", "Clair"], ["Larsen !"], "Un, deux, un, deux."),
  objet("building-solutions", "🚪", "Porte automatique", "Courants faibles", 28, ["S'ouvre toute seule", "Accessible"], ["Se referme sur le sac"], "Sésame, ouvre-toi."),
  objet("building-solutions", "⛈️", "Parafoudre", "Protection foudre", 56, ["Absorbe la foudre", "Protège les équipements"], ["Travaille rarement… mais ce jour-là !"], "Que l'orage vienne."),

  // ───────── Cegelec Nord ─────────
  objet("cegelec-nord", "☀️", "Centrale photovoltaïque", "Courants forts", 78, ["Produit sans bruit", "Peu de maintenance"], ["Dépend de la météo"], "Le soleil du Nord."),
  objet("cegelec-nord", "📷", "Caméra thermique", "Maintenance, thermographie", 60, ["Voit la chaleur", "Détecte les faiblesses"], ["Révèle ce qu'on voulait cacher"], "Je repère le point chaud."),
  objet("cegelec-nord", "📻", "Radio GPS", "Courants faibles", 36, ["Localise les équipes", "Communique partout"], ["Pas de réseau en brousse"], "Où êtes-vous ?"),
  objet("cegelec-nord", "🛻", "Pick-up 4x4", "Véhicule de chantier", 58, ["Passe partout", "Charge le matériel"], ["Boue jusqu'au toit"], "Les pistes ne lui font pas peur."),
  objet("cegelec-nord", "🏭", "Poste HTA/HTB", "Courants forts", 80, ["Reçoit la haute tension", "Solide"], ["Ne pas s'approcher"], "Je tiens la haute tension."),

  // ───────── Omexom Transition Énergétique ─────────
  objet("omexom-te", "🔆", "Panneau solaire", "Production photovoltaïque", 66, ["Transforme le soleil en électricité", "Silencieux"], ["Poussière sur la vitre"], "Du soleil en volts."),
  objet("omexom-te", "🔋", "Batterie de stockage", "Solutions de stockage", 74, ["Garde le surplus", "Lisse la production"], ["Coûte cher"], "Pour les jours sans soleil."),
  objet("omexom-te", "🔁", "Onduleur photovoltaïque", "Conversion d'énergie", 70, ["Convertit le courant", "Surveille la centrale"], ["Chauffe sous le soleil"], "Du continu à l'alternatif."),
  objet("omexom-te", "🌱", "Serre photovoltaïque", "Énergie et agriculture", 64, ["Abrite les cultures", "Produit de l'électricité"], ["Structure à entretenir"], "Cultiver et produire."),
  objet("omexom-te", "🌿", "Mât d'éclairage solaire", "Éclairage public solaire", 38, ["Autonome", "Éclaire sans réseau"], ["Batterie à surveiller"], "Mon soleil, ma lumière."),

  // ───────── Omexom Réseaux ─────────
  objet("omexom-reseaux", "🗼", "Pylône", "Réseau électrique", 62, ["Porte les lignes", "Visible de loin"], ["Impossible à cacher"], "Haut et fier."),
  objet("omexom-reseaux", "⚡", "Ligne électrique HTA", "Réseau aérien", 68, ["Distribue l'énergie", "Traverse les vallées"], ["Vent et orages"], "Du courant d'un bout à l'autre."),
  objet("omexom-reseaux", "🕳️", "Câble souterrain", "Réseau souterrain", 58, ["Discret", "Protégé des intempéries"], ["Difficile à localiser"], "Sous nos pieds."),
  objet("omexom-reseaux", "🔌", "Transformateur", "Distribution", 72, ["Adapte la tension", "Robuste"], ["Lourd", "Ronronne"], "Je change la tension."),
  objet("omexom-reseaux", "🏗️", "Nacelle élévatrice", "Matériel de levage", 46, ["Atteint les hauteurs", "Évite les échelles"], ["Besoin de place"], "Toujours plus haut."),
  objet("omexom-reseaux", "⏱️", "Compteur électrique", "Distribution", 30, ["Compte chaque kWh", "Fiable"], ["Personne ne le regarde"], "Je note tout."),

  // ───────── Citeos : éclairage public et équipements urbains ─────────
  objet("citeos", "💡", "Lampadaire LED", "Éclairage public", 48, ["Économe", "Longue durée de vie"], ["Attire les insectes"], "La ville s'allume."),
  objet("citeos", "🏛️", "Mise en lumière du patrimoine", "Éclairage architectural", 34, ["Sublime les monuments", "Ambiance de soirée"], ["Facture quand tout s'allume"], "Le monument, de nuit."),
  objet("citeos", "🎄", "Illumination festive", "Éclairage événementiel", 26, ["Ambiance garantie", "Rassemble tout le monde"], ["Se déroule une fois par an"], "Joyeuses fêtes."),
  objet("citeos", "🚦", "Équipement urbain connecté", "Supervision et télégestion", 52, ["Se pilote à distance", "Remonte ses pannes"], ["Dépend du réseau"], "La ville intelligente."),

  // ───────── VINCI : la carte légendaire ─────────
  // Un objet, mais d'une rareté exceptionnelle : le plan d'épargne Groupe VINCI.
  // Infos relevées sur castor.vinci.com (les règles d'abondement sont fixées chaque année).
  {
    type: "objet", rarete: "Légendaire", marque: "vinci", icone: "🦫",
    nom: "CASTOR", fonction: "Plan d'épargne Groupe VINCI", puissance: 90,
    forts: [
      "Jusqu'à 80 actions VINCI gratuites (offre 2023)",
      "Bâtit ton épargne, branche après branche",
      "Fait de toi un actionnaire du Groupe"
    ],
    faibles: [
      "Épargne indisponible pendant 3 ans",
      "Investi en actions : la Bourse monte… et descend"
    ],
    devise: "Avec CASTOR, investissez-vous dans VINCI !"
  }
]);


// ─────────────────────────────────────────────────────────────────────────────
// RARETÉ DES OBJETS : évaluée objet par objet (la CASTOR est déjà Légendaire plus haut).
//   Commune    : on en trouve partout, peu coûteux, facile à remplacer
//   Rare       : équipement technique ou spécialisé, qu'on ne trouve pas dans tous les ateliers
//   Épique     : équipement lourd, coûteux ou critique, dont la panne arrête une installation
//   Légendaire : infrastructure stratégique, exceptionnelle ou unique
// Pour changer la rareté d'un objet, modifie simplement sa ligne ci-dessous.
(function () {
  var RARETE_OBJETS = {
    // Cegelec
    "Câble électrique": "Commune", "Casque de chantier": "Commune", "Gilet haute visibilité": "Commune",
    "Multimètre": "Rare", "Tableau électrique": "Rare", "Échelle": "Commune",
    "Tablette de chantier": "Rare", "Rallonge de chantier": "Commune",
    "Voiture de service": "Commune", "Voiture de fonction": "Rare",
    // Actemium
    "Automate programmable": "Épique", "Variateur de vitesse": "Rare", "Capteur d'instrumentation": "Commune",
    "Tuyauterie industrielle": "Rare", "Armoire de commande": "Rare", "Écran de supervision": "Rare",
    "Poste de transformation HTA": "Épique", "Plan CAO/DAO": "Commune", "Éclairage industriel": "Commune",
    // Axians
    "Câble RJ45": "Commune", "Borne wifi": "Commune", "Switch d'accès": "Rare", "Firewall": "Épique",
    "Baie de brassage": "Rare", "Fibre optique": "Rare", "Soudeuse de fibre": "Épique", "Borne DECT": "Commune",
    "Serveur": "Rare", "Data center": "Légendaire", "Terminal multimédia": "Commune",
    "Salle réseau": "Épique", "Téléphone ToIP": "Commune", "Infogérance": "Épique",
    // Cegelec Maintenance Énergies
    "Climatisation split": "Commune", "Centrale de traitement d'air": "Épique", "Chambre froide": "Rare",
    "Onduleur": "Épique", "TGBT": "Épique", "Détecteur incendie": "Commune", "Contrôle d'accès": "Rare",
    "Caméra de vidéosurveillance": "Commune", "Appel malade": "Commune",
    // Cegelec Building Solutions
    "Système VRV": "Rare", "Groupe d'eau glacée": "Épique", "Groupe électrogène": "Épique",
    "Désenfumage": "Rare", "Sonorisation": "Commune", "Porte automatique": "Commune", "Parafoudre": "Rare",
    // Cegelec Nord
    "Centrale photovoltaïque": "Légendaire", "Caméra thermique": "Rare", "Radio GPS": "Commune",
    "Pick-up 4x4": "Rare", "Poste HTA/HTB": "Légendaire",
    // Omexom Transition Énergétique
    "Panneau solaire": "Commune", "Batterie de stockage": "Épique", "Onduleur photovoltaïque": "Rare",
    "Serre photovoltaïque": "Épique", "Mât d'éclairage solaire": "Rare",
    // Omexom Réseaux
    "Camion Omexom": "Rare", "Pylône": "Épique", "Ligne électrique HTA": "Épique", "Câble souterrain": "Rare",
    "Transformateur": "Épique", "Nacelle élévatrice": "Rare", "Compteur électrique": "Commune",
    // Citeos
    "Lampadaire LED": "Commune", "Mise en lumière du patrimoine": "Rare", "Illumination festive": "Commune",
    "Équipement urbain connecté": "Rare"
  };
  (window.EQUIPE || []).forEach(function (m) {
    if (m.type === "objet" && !m.rarete && RARETE_OBJETS[m.nom]) { m.rarete = RARETE_OBJETS[m.nom]; }
  });
})();
