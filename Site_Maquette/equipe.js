// Bibliothèque de cartes : une carte par membre de l'équipe… ou par objet.
//
// Les cartes ci-dessous sont des EXEMPLES FICTIFS (des métiers et des objets, pas des personnes).
// Pour créer la carte d'un vrai collègue (avec son accord !), copie une ligne et remplace les champs.
//
// ─── type : détermine la RARETÉ de la carte ──────────────────────────────────
//   "objet"        → Commune par défaut ; la rareté de chaque objet est évaluée dans objets.js
//                                   (camion, voiture, câble RJ45, salle réseau, téléphone ToIP, infogérance…)
//   "technicien"   → Rare         (tous les techniciens, monteurs, électriciens, apprentis…)
//   "responsable"  → Épique       (responsables d'affaires, chefs de projet, responsables de service)
//   "direction"    → Légendaire   (chefs d'entreprise, directeurs, responsable administratif et financier)
//   Facultatif : rarete: "Commune" | "Rare" | "Épique" | "Légendaire" force une rareté précise
//                (par exemple un technicien exceptionnel en "Épique").
//
// ─── autres champs ───────────────────────────────────────────────────────────
//   nom        : prénom, surnom ou nom de l'objet
//   fonction   : poste, ou description courte de l'objet
//   marque     : "cegelec" "building-solutions" "maintenance-energies" "cegelec-nord"
//                "axians" "actemium" "omexom-te" "omexom-reseaux" "citeos"
//   puissance  : de 1 à 100. Pour une personne : puissance hiérarchique. Pour un objet : utilité.
//   forts      : 1 à 3 points forts
//   faibles    : 1 à 2 points faibles (reste bienveillant : humour doux, rien de blessant)
//   devise     : petite phrase en bas de carte (facultatif)
//   photo      : "assets/equipe/prenom.jpg" (facultatif, sinon initiales)
//   icone      : un emoji pour les objets (facultatif, remplace les initiales)
window.EQUIPE = [
  // ----- Direction : Légendaire
  { type: "direction", nom: "Exemple · Directeur", fonction: "Directeur d'entreprise", marque: "cegelec", puissance: 95,
    forts: ["Vision d'ensemble", "Décision rapide"], faibles: ["Agenda toujours plein"], devise: "Le cap, c'est moi." },
  { type: "direction", nom: "Exemple · RAF", fonction: "Responsable administratif et financier", marque: "cegelec", puissance: 88,
    forts: ["Chiffres au centime", "Garde le budget"], faibles: ["Allergique aux notes de frais oubliées"], devise: "Ça rentre dans le budget." },

  // ----- Responsables : Épique
  { type: "responsable", nom: "Exemple · Resp. d'affaires", fonction: "Responsable d'affaires", marque: "building-solutions", puissance: 74,
    forts: ["Négocie sans trembler", "Garde le client content"], faibles: ["Téléphone toujours collé à l'oreille"], devise: "Le chantier d'abord, le planning ensuite." },
  { type: "responsable", nom: "Exemple · Chef de projet", fonction: "Chef de projet solaire", marque: "omexom-te", puissance: 78,
    forts: ["Gère 10 mois de chantier", "Aime le soleil"], faibles: ["Jamais à l'ombre"], devise: "Plus de watts, moins de bruit." },
  { type: "responsable", nom: "Exemple · QHSE", fonction: "Responsable QHSE", marque: "cegelec", puissance: 68,
    forts: ["Veille sur tout le monde", "Mémoire des normes"], faibles: ["Voit un risque partout"], devise: "Zéro accident." },

  // ----- Techniciens : Rare
  { type: "technicien", nom: "Exemple · Chef de chantier", fonction: "Chef de chantier", marque: "building-solutions", puissance: 58,
    forts: ["Planning maîtrisé", "Sang-froid"], faibles: ["Café obligatoire à 7 h"], devise: "Sur le chantier à l'heure." },
  { type: "technicien", nom: "Exemple · Technicien fibre", fonction: "Technicien fibre optique", marque: "axians", puissance: 48,
    forts: ["Précision chirurgicale", "Patience"], faibles: ["Allergique aux câbles emmêlés"], devise: "Un brin à la fois." },
  { type: "technicien", nom: "Exemple · Automaticien", fonction: "Automaticien", marque: "actemium", puissance: 52,
    forts: ["Logique implacable", "Dépanne à distance"], faibles: ["Parle en schémas"], devise: "Ça marche. Ou presque." },
  { type: "technicien", nom: "Exemple · Monteur réseaux", fonction: "Monteur réseaux", marque: "omexom-reseaux", puissance: 35,
    forts: ["Zéro vertige", "Équipe soudée"], faibles: ["Sieste à la pause"], devise: "Toujours en hauteur." },
  { type: "technicien", nom: "Exemple · Maintenance", fonction: "Technicien de maintenance", marque: "maintenance-energies", puissance: 42,
    forts: ["Dépannage express", "Connaît chaque tableau"], faibles: ["Téléphone qui sonne tout le temps"], devise: "Rien ne lui résiste." },
  { type: "technicien", nom: "Exemple · Électricien Nord", fonction: "Électricien Province Nord", marque: "cegelec-nord", puissance: 45,
    forts: ["Autonome", "Connaît chaque piste"], faibles: ["Radio toujours trop forte"], devise: "Le Nord, c'est chez lui." },
  { type: "technicien", nom: "Exemple · Apprenti", fonction: "Apprenti", marque: "cegelec", puissance: 12,
    forts: ["Curiosité", "Énergie"], faibles: ["Perd souvent ses clés"], devise: "Demain, patron." },

  // ----- Objets : Commune
  { type: "objet", icone: "🚚", nom: "Camion Omexom", fonction: "Véhicule de chantier", marque: "omexom-reseaux", puissance: 60,
    forts: ["Transporte tout le matériel", "Passe partout"], faibles: ["Consomme beaucoup"], devise: "Chargé jusqu'au toit." },
  { type: "objet", icone: "🚗", nom: "Voiture de service", fonction: "Véhicule de service", marque: "cegelec", puissance: 40,
    forts: ["Toujours disponible", "Clim qui marche"], faibles: ["Jamais le plein"], devise: "Une pour tous." },
  { type: "objet", icone: "🚙", nom: "Voiture de fonction", fonction: "Véhicule de fonction", marque: "cegelec", puissance: 45,
    forts: ["Confortable", "Belle allure"], faibles: ["Tout le monde la regarde"], devise: "Le grade se voit." },
  { type: "objet", icone: "🔌", nom: "Câble RJ45", fonction: "Câblage réseau", marque: "axians", puissance: 30,
    forts: ["Relie tout", "Pas cher"], faibles: ["Se noue tout seul"], devise: "Branché, connecté." },
  { type: "objet", icone: "🖧", nom: "Salle réseau", fonction: "Local technique", marque: "axians", puissance: 65,
    forts: ["Cœur du réseau", "Au frais"], faibles: ["Bruit de ventilateurs"], devise: "Ici, tout passe." },
  { type: "objet", icone: "☎️", nom: "Téléphone ToIP", fonction: "Téléphonie sur IP", marque: "axians", puissance: 35,
    forts: ["Fonctionne partout", "Transfert d'appels"], faibles: ["Sonnerie envahissante"], devise: "Allô, ici Axians." },
  { type: "objet", icone: "🛠️", nom: "Infogérance", fonction: "Technique d'externalisation IT", marque: "axians", puissance: 70,
    forts: ["Supervise à distance", "Prévient les pannes"], faibles: ["Invisible quand tout va bien"], devise: "On s'occupe de tout." }
];
