# -*- coding: utf-8 -*-
"""Génère les pages HTML de la maquette Cegelec Nouvelle-Calédonie.
Usage : python build.py   (écrit les .html à côté de ce fichier)
"""
import html
import os

ROOT = os.path.dirname(os.path.abspath(__file__))
O = "assets/officiel/"
P = "assets/photos/"
OFFICIEL = "https://www.cegelec.nc"

e = html.escape

# ---------------------------------------------------------------- données
ENTREPRISES = [
    dict(slug="ent-actemium.html", nom="Actemium Nouvelle-Calédonie", court="Actemium", badge="Industrie",
         img=O + "MicrosoftTeams-image-20-scaled.jpg", logo=O + "actemium_logo-e1611180030773-300x47-1.jpg",
         accroche="Actemium, marque de VINCI Energies spécialisée dans l'industrie, couvre l'ensemble du cycle de vie industriel.",
         intro="Actemium déploie son savoir-faire pour concevoir, réaliser et maintenir des systèmes sur l'ensemble des segments industriels. Notre offre : maîtriser le cycle de vie industriel de bout en bout.",
         blocs=[("Instrumentation", ["Conception et mise en œuvre", "Tuyauterie", "L'analyse industrielle"]),
                ("Contrôle commande et SIP", ["Contrôle commande et automatisme", "Supervision et MES", "Échange de données procès et ERP"]),
                ("Câblage process", ["Alimentation électrique et fluides des machines", "Câblage des équipements", "Réseaux", "Variation des vitesses"]),
                ("Courants faibles", ["Sécurité environnement", "Sécurité surveillance", "Réseaux", "Climatisation"]),
                ("Courants forts", ["Postes de transformation HTA", "Distribution BT", "Alimentation de secours", "Éclairage industriel", "Sécurité, fiabilité et qualité des installations"]),
                ("Ingénierie électrique", ["CAO/DAO", "Gestion de projets"])],
         titre_bloc="Nos expertises",
         bas=("Actemium : au cœur de la performance industrielle",
              "Afin de proposer des solutions efficaces et créatives à chacun de nos clients, nous combinons notre expertise professionnelle avec une approche segmentée et les synergies de notre réseau."),
         ext=("www.actemium.fr", "https://www.actemium.fr"), figs=[O + "actemium-removebg-preview.png"]),
    dict(slug="ent-axians.html", nom="Axians Nouvelle-Calédonie", court="Axians", badge="Numérique",
         img=O + "axians_1.jpg", logo=O + "axians_logo-e1611180087442.jpg",
         accroche="Axians est la marque de VINCI Energies dédiée aux solutions ICT.",
         intro="Nous accompagnons nos clients, entreprises privées et du secteur public, opérateurs et fournisseurs de services, tout au long du cycle de vie de leurs projets ICT, depuis les infrastructures de réseau jusqu'aux applications.",
         blocs=[("Infrastructure et réseau", ["Conception et management des réseaux et de leur environnement IT", "Intervention sur l'ensemble des métiers de l'IT"]),
                ("Téléphonie et communications unifiées", ["Déploiement de solutions full IP / TDM", "Applications au service des petites et moyennes entreprises"]),
                ("Câblage réseau et fibre optique", ["Installateur spécialisé et certifié en câblage informatique", "Câblage performant pour les débits des nouvelles solutions IT"]),
                ("Infogérance", ["Service d'externalisation intégrant plusieurs services associés", "Par exemple la maintenance informatique pour les professionnels"])],
         titre_bloc="Nos solutions et services",
         bas=("Axians, solutions ICT", "Axians propose une gamme unique de solutions et de services ICT couvrant l'ensemble du cycle de vie des projets, de la conception à l'exploitation."),
         ext=None, figs=[O + "axians_presnetation.png", O + "axians.png"]),
    dict(slug="ent-maintenance-energies.html", nom="Cegelec Nouvelle-Calédonie Maintenance Énergies", court="Maintenance Énergies", badge="Maintenance",
         img=O + "maintenance_energies.jpg", logo=O + "cegelec_logo-1-e1608011795431-300x99-1.jpg",
         accroche="Acteur du bien-être des occupants des bâtiments et des industries.",
         intro="Marque de VINCI Energies, Cegelec Nouvelle-Calédonie Maintenance Énergies crée, exploite et anime des espaces permettant à chacun de révéler tout son potentiel.",
         blocs=[("Courants forts", ["Poste HT", "TGBT, TD", "Onduleurs", "Distribution BT"]),
                ("Courants faibles", ["Système incendie", "Extinction incendie", "Contrôles d'accès", "Anti-intrusion", "Vidéosurveillance", "Câblage VDI", "Sonorisation", "Appel malade", "Porte automatique"]),
                ("Climatisation, ventilation", ["Désenfumage", "Climatisation individuelle (split)", "Climatisation à détente directe (VRV)", "Climatisation à eau (eau glacée)", "Armoire de précision", "Centrale de traitement d'air", "Chambres froides"])],
         titre_bloc="Nos solutions et services", bas=None, ext=None, figs=[]),
    dict(slug="ent-building-solutions.html", nom="Cegelec Nouvelle-Calédonie Building Solutions", court="Building Solutions", badge="Bâtiment",
         img=O + "bs_entreprise.jpg", logo=O + "cegelec_logo-1-e1608011795431-300x99-1.jpg",
         accroche="Apporter durablement du bien-être aux parties prenantes des bâtiments tertiaires.",
         intro="Marque de VINCI Energies spécialisée dans le domaine tertiaire, Building Solutions a pour but d'améliorer le service dans les bâtiments tertiaires. L'entreprise est positionnée sur le métier de la maintenance multitechnique des installations.",
         blocs=[("Courants forts", ["Poste HT et transformateurs", "TGBT (avec ou sans IS), TD", "Groupes électrogènes", "Distribution, protection foudre"]),
                ("Courants faibles", ["Détection incendie, extinction incendie", "Vidéosurveillance, sûreté, intrusion", "Sonorisation, télévision", "Câblage informatique", "Appel malade"]),
                ("Climatisation, ventilation", ["Énergie thermique", "Traitement de l'air et du confinement", "Froid", "Isolation"]),
                ("Nos points d'excellence", ["Eau glacée : réseau PVC pression", "Traitement de l'air", "Désenfumage", "VRV"])],
         titre_bloc="Nos solutions et services",
         bas=("Building Solutions : rendre les bâtiments plus durables et plus intelligents",
              "Building Solutions apporte des solutions globales permettant de disposer de bâtiments plus économes, confortables et sûrs, tout en répondant aux exigences réglementaires et aux dernières avancées technologiques liées au bâtiment connecté."),
         ext=None, figs=[O + "IMG_2506.jpg"]),
    dict(slug="ent-cegelec-nord.html", nom="Cegelec Nord Nouvelle-Calédonie", court="Cegelec Nord", badge="Province Nord",
         img=O + "carte_nouvelle-caledonie.png", logo=O + "cegelec_logo-1-e1608011795431-300x99-1.jpg",
         accroche="Une présence locale pour les clients de la Province Nord.",
         intro="Notre vision : concevoir, réaliser et maintenir les installations électriques (courant fort, courant faible) pour nos clients industriels, tertiaires et institutionnels en Province Nord, tout en accompagnant nos collaborateurs dans leur évolution professionnelle au sein de l'entreprise. Cegelec Nord intervient en travaux neufs ou en maintenance.",
         blocs=[("Courant fort", ["Travaux d'électricité industrielle et instrumentation", "Poste HTA / HTB", "Centrales photovoltaïques"]),
                ("Courant faible", ["Précâblage informatique et fibre optique", "Vidéosurveillance", "Radio GPS", "Contrôle d'accès", "Système de sécurité incendie"]),
                ("Maintenance tertiaire et industrielle", ["Thermographie", "Maintenance poste HTA", "Maintenance climatisation", "Maintenance SSI", "Maintenance contrôle d'accès / CCTV", "Travaux de rénovation CFo / CFa"])],
         titre_bloc="Cegelec Nord intervient dans les domaines suivants",
         bas=("Cegelec : des solutions technologiques pour les entreprises et les collectivités",
              "Cegelec apporte son expertise en automatisme, instrumentation et contrôle/commande, en génie climatique et électrique."),
         ext=("www.vinci-energies.com/cegelec", "https://www.vinci-energies.com/cegelec/"), figs=[]),
    dict(slug="ent-omexom-transition.html", nom="Omexom Transition Énergétique Nouvelle-Calédonie", court="Omexom Transition Énergétique", badge="Transition",
         img=O + "omexom.png", logo=O + "Omexom-800x472-new-e1611180519178-300x53-1.png",
         accroche="Production, transport, transformation et distribution d'énergie électrique.",
         intro="Omexom est la marque de VINCI Energies spécialisée dans les projets de production, de transport, de transformation et de distribution d'énergie électrique, jusqu'à son utilisation sur les territoires. Omexom s'appuie sur son expertise des grands réseaux électriques pour anticiper l'impact des énergies renouvelables, développer des solutions de stockage, rendre les infrastructures plus intelligentes et servir les nouveaux modes de consommation.",
         blocs=[("Citeos", ["Marque lumière et équipements urbains dynamiques de VINCI Energies", "Éclairage public, mise en valeur du patrimoine, illuminations festives", "Équipements urbains dynamiques, supervision et télégestion d'objets connectés", "Équipements d'infrastructures de transports"]),
                ("Omexom Institute", ["Des espaces ouverts pour renforcer ses compétences, s'inspirer et donner vie à ses idées"])],
         titre_bloc="Nos marques et expertises",
         bas=("Omexom et Citeos", "Omexom est spécialisée dans le domaine de l'infrastructure. Citeos déploie, maintient et exploite les équipements urbains et développe des solutions digitales dédiées aux citoyens, aux exploitants et aux gestionnaires."),
         ext=("www.omexom.fr", "https://www.omexom.fr"), figs=[O + "Omexom-site-corp@2x-1-e1686714666643.png"]),
    dict(slug="ent-omexom-reseaux.html", nom="Omexom Réseaux Nouvelle-Calédonie", court="Omexom Réseaux", badge="Réseaux",
         img=O + "pexels-saban-karabeli-10537250-scaled.jpg", logo=O + "Omexom-800x472-new-e1611180519178-300x53-1.png",
         accroche="Distribution d'énergie électrique et infrastructures de télécommunication.",
         intro="Omexom Réseaux, marque de VINCI Energies, est un partenaire de performance reconnu en Nouvelle-Calédonie dans les métiers de la distribution d'énergie électrique ainsi que du déploiement des infrastructures de réseaux de télécommunication. Elle propose une large gamme de services, de l'étude technique à la maintenance des infrastructures électriques et de télécommunication, et fournit des solutions sur mesure pour améliorer l'efficacité, la fiabilité et la durabilité des réseaux.",
         blocs=[("Réseaux électriques", ["Maintenance et fiabilisation des réseaux électriques", "Création, extension et renforcement des réseaux électriques HTA et BT (aérien et souterrains)", "Viabilisation de lotissements"]),
                ("Télécommunications", ["Déploiement de réseaux fibre optique"])],
         titre_bloc="Nos solutions et services", bas=None, ext=None,
         figs=[O + "power-2881462_1280-e1686631714444.jpg", O + "api_thumb_450-3.jpg"]),
]

REFS = [
    dict(slug="ref-ouaco.html", titre="Centrale solaire de Ouaco", theme=["Énergie solaire", "Photovoltaïque"],
         img=O + "serres-photovolatiques.jpg", lieu="Ouaco, Province Nord", ent="Omexom",
         resume="Omexom Nouvelle-Calédonie a réalisé des travaux pour la mise en place de panneaux solaires à Ouaco.",
         fiche=[("Localisation", "Ouaco, Province Nord, Nouvelle-Calédonie"),
                ("Tâches", "Conception, fourniture et installation (EPC) de l'intégralité de la centrale solaire"),
                ("Entreprise intervenante", "Omexom Nouvelle-Calédonie"),
                ("Durée du chantier", "10 mois, de janvier 2020 à octobre 2020"),
                ("Durée des études", "2 mois")],
         details=[("Étude", "étude des câbles, des structures au sol et serres, de la gestion des eaux, dimensionnement PDL et PTR et autres éléments de puissance"),
                  ("Terrassement du terrain", "création des pistes, nivellement, coulage des fondations"),
                  ("Structure", "battage des pieux et installation des structures au sol sur les serres"),
                  ("Électricité", "mise en place du réseau électrique, connexion des éléments")]),
    dict(slug="ref-hilton.html", titre="Rénovation de l'hôtel Hilton à l'Îlot Maître", theme=["Système électrique"],
         img=O + "4269834471.jpeg", lieu="Îlot Maître, Province Sud", ent="Building Solutions",
         resume="Cegelec Nouvelle-Calédonie Building Solutions a participé aux travaux de rénovation de l'hôtel Hilton à l'Îlot Maître.",
         fiche=[("Localisation", "Îlot Maître, Province Sud, Nouvelle-Calédonie"),
                ("Tâches", "Installation d'un système de détection incendie"),
                ("Entreprise intervenante", "Building Solutions Nouvelle-Calédonie"),
                ("Durée du chantier", "6 mois")],
         details=[], fig2=O + "bs_ilot_maitre-1024x576-1.png"),
    dict(slug="ref-kone.html", titre="Travaux au centre de détention de Koné", theme=["Énergie électrique", "Système électrique"],
         img=O + "3224788864.png", lieu="Koné, Province Nord", ent="Building Solutions",
         resume="Cegelec Nouvelle-Calédonie Building Solutions a participé aux travaux de construction du centre de détention de Koné.",
         fiche=[("Localisation", "Koné, Province Nord, Nouvelle-Calédonie"),
                ("Maître d'ouvrage", "Ministère de la Justice"),
                ("Maître d'ouvrage déléguée", "Direction Aviation Civile"),
                ("Architecte", "Architecte Studio & Artimon (mandataire)"),
                ("BET", "Soproner"),
                ("Tâches", "Installation du système de climatisation et d'électricité"),
                ("Entreprise intervenante", "Building Solutions Nouvelle-Calédonie"),
                ("Durée du chantier", "22 mois")],
         details=[], fig2=O + "centre-de-detention-1024x576-1.png"),
    dict(slug="ref-ftth.html", titre="Déploiement du réseau FTTH en Nouvelle-Calédonie", theme=["Fibre optique"],
         img=O + "reseau_ftth-1-1024x576-1.png", lieu="Grand Nouméa, Koné, Poindimié, La Foa, Bourail, Boulouparis", ent="Fibrelec, Omexom",
         resume="Fibrelec Nouvelle-Calédonie et Omexom Nouvelle-Calédonie ont réalisé le déploiement du réseau FTTH en Nouvelle-Calédonie.",
         fiche=[("Localisation", "Nouméa, Grand Nouméa, Koné, Poindimié, La Foa, Bourail et Boulouparis"),
                ("Tâches", "Déploiement de plus de 49 000 prises raccordables en Nouvelle-Calédonie"),
                ("Entreprises intervenantes", "Fibrelec / Omexom Nouvelle-Calédonie"),
                ("Durée du chantier", "Depuis 2015")],
         details=[]),
    dict(slug="ref-bel-air.html", titre="Éclairage public solaire du giratoire de Bel Air – Zone VKP", theme=["Énergie solaire", "Photovoltaïque"],
         img=O + "526345763.png", lieu="Koné, Province Nord", ent="Cegelec Nord",
         resume="Cegelec Nord Nouvelle-Calédonie a installé un éclairage public solaire sur le giratoire de Bel Air – Zone VKP.",
         fiche=[("Localisation", "Koné, Province Nord, Nouvelle-Calédonie"),
                ("Tâches", "Étude de dimensionnement avec notre fabricant FONROCHE ; plans d'implantation et choix du matériel ; installation de 12 mâts de 6 mètres"),
                ("Équipement de chaque mât", "Module photovoltaïque 140 Wc, lanterne LED 30 W, batterie NiMh 24 V 624 Wh, système intelligent de gestion et de programmation"),
                ("Entreprise intervenante", "Cegelec Nord"),
                ("Durée du chantier", "15 jours")],
         details=[]),
    dict(slug="ref-teari.html", titre="Éclairage public solaire du giratoire de Teari – Zone VKP", theme=["Photovoltaïque"],
         img=O + "2949785025.png", lieu="Koné, Province Nord", ent="Cegelec Nord",
         resume="Cegelec Nord Nouvelle-Calédonie a installé un éclairage public solaire sur le giratoire de Teari – Zone VKP.",
         fiche=[("Localisation", "Koné, Province Nord, Nouvelle-Calédonie"),
                ("Tâches", "Étude de dimensionnement avec notre fabricant FONROCHE ; plans d'implantation et choix du matériel ; installation de 15 mâts de 6 mètres"),
                ("Équipement de chaque mât", "Module photovoltaïque 140 Wc, lanterne LED 30 W, batterie NiMh 24 V 624 Wh, système intelligent de gestion et de programmation"),
                ("Entreprise intervenante", "Cegelec Nord"),
                ("Durée du chantier", "15 jours")],
         details=[]),
    dict(slug="ref-magnin.html", titre="Infrastructure réseau et téléphone de la Clinique Magnin", theme=["Système électrique"],
         img=O + "1307362408.png", lieu="Nouville, Province Sud", ent="Axians",
         resume="Axians Nouvelle-Calédonie a réalisé les travaux de l'infrastructure réseau et téléphonie de la Clinique Kuindo Magnin.",
         fiche=[("Localisation", "Nouville, Province Sud, Nouvelle-Calédonie"),
                ("Tâches", "270 terminaux multimédia pour les patients ; 170 bornes wifi ; 90 bornes DECT ; une vingtaine de télévisions connectées ; 40 switchs d'accès répartis sur 7 locaux techniques ; double couche de firewalling"),
                ("Entreprise intervenante", "Axians Nouvelle-Calédonie"),
                ("Durée du chantier", "3 mois")],
         details=[]),
    dict(slug="ref-enercal.html", titre="Renouvellement du système de dispatching pour Enercal", theme=["Énergie électrique"],
         img=O + "systeme_dispacthing-1024x566-1.png", lieu="Nouméa, Province Sud", ent="Actemium",
         resume="Actemium Nouvelle-Calédonie a réalisé les travaux pour le renouvellement du système de dispatching pour Enercal.",
         fiche=[("Localisation", "Nouméa, Province Sud, Nouvelle-Calédonie"),
                ("Tâches", "Prestation de déploiement terrain pour Siemens : survey des sites, réalisation du TGBT BCC, déploiement des PA sur les 22 sites, raccordement filerie entre CAD et PA, test des E/S en parallèle, électrification BCC – mur d'image, basculement des PA, adaptation des OMT, dépose des anciennes installations"),
                ("Entreprise intervenante", "Actemium Nouvelle-Calédonie"),
                ("Durée du chantier", "10 mois (2018)")],
         details=[]),
]
REF_ACCUEIL = ["ref-kone.html", "ref-hilton.html", "ref-ouaco.html"]
THEMES = ["Énergie électrique", "Énergie solaire", "Fibre optique", "Photovoltaïque", "Système électrique"]

SITES = [
    dict(nom="Cegelec Nouvelle-Calédonie", adr="Route de la Baie des Dames<br>98800 Nouméa<br>Nouvelle-Calédonie", tel="+687 27 56 46"),
    dict(nom="Cegelec Nord", adr="Dock DCGR Nord<br>Nouvelle-Calédonie", tel="+687 42 49 69"),
]

# ---------------------------------------------------------------- navigation
def menu_items():
    return [
        ("Nous connaître", "histoire.html", [
            ("Notre histoire", "histoire.html"), ("Notre organisation", "organisation.html"),
            ("Nos marques", "marques.html"), ("Nos valeurs", "valeurs.html"),
            ("VINCI Energies", "vinci-energies.html"), ("Travailler chez nous", "travailler-chez-nous.html")]),
        ("Nos entreprises", "entreprises.html", [(x["court"], x["slug"]) for x in ENTREPRISES]),
        ("Nos réalisations", "references.html", []),
        ("Notre engagement RSE", "rse.html", [("Nos certifications", "certifications.html"), ("Les évènements", "evenements.html")]),
        ("Contact", "contact.html", []),
    ]


def header(actif):
    lis = []
    for titre, href, subs in menu_items():
        cls = ' class="actif"' if actif == href or any(actif == s[1] for s in subs) else ""
        sub = ""
        if subs:
            sub = '<ul class="sous">' + "".join(f'<li><a href="{h}">{e(t)}</a></li>' for t, h in subs) + "</ul>"
        lis.append(f'<li><a href="{href}"{cls}>{e(titre)}</a>{sub}</li>')
    return f"""<header>
  <div class="wrap nav">
    <a class="logo" href="index.html" aria-label="Cegelec Nouvelle-Calédonie, accueil"><img src="assets/logo_cegelec.jpg" alt="Cegelec"></a>
    <button class="burger" aria-label="Menu" onclick="document.querySelector('.menu').classList.toggle('ouvert')">☰</button>
    <ul class="menu">{''.join(lis)}</ul>
    <a class="btn plein" href="contact.html">Nous contacter</a>
  </div>
</header>"""


def footer():
    ent = "".join(f'<li><a href="{x["slug"]}">{e(x["court"])}</a></li>' for x in ENTREPRISES)
    return f"""<footer>
  <div class="wrap">
    <div class="cols">
      <div><h4>Nous connaître</h4><ul>
        <li><a href="histoire.html">Notre histoire</a></li><li><a href="organisation.html">Notre organisation</a></li>
        <li><a href="marques.html">Nos marques</a></li><li><a href="valeurs.html">Nos valeurs</a></li>
        <li><a href="vinci-energies.html">VINCI Energies</a></li><li><a href="travailler-chez-nous.html">Travailler chez nous</a></li></ul></div>
      <div><h4>Nos entreprises</h4><ul>{ent}</ul></div>
      <div><h4>Aller plus loin</h4><ul>
        <li><a href="references.html">Nos réalisations</a></li><li><a href="rse.html">Notre engagement RSE</a></li>
        <li><a href="certifications.html">Nos certifications</a></li><li><a href="evenements.html">Les évènements</a></li>
        <li><a href="offres-emploi.html">Offres d'emploi</a></li><li><a href="contact.html">Contact</a></li></ul></div>
      <div><h4>Nous suivre</h4><ul>
        <li><a href="https://www.facebook.com/Cegelec.caledonie" target="_blank" rel="noopener">Facebook</a></li>
        <li><a href="https://www.linkedin.com/company/cegelec-nouvelle-cal%C3%A9donie/" target="_blank" rel="noopener">LinkedIn</a></li></ul></div>
    </div>
    <div class="bas">
      <nav>
        <a href="{OFFICIEL}/mentions-legales/" target="_blank" rel="noopener">Mentions légales</a> ·
        <a href="{OFFICIEL}/cookies/" target="_blank" rel="noopener">Cookies</a> ·
        <a href="plan-du-site.html">Plan du site</a> ·
        <a href="{OFFICIEL}/suppression-de-donnees/" target="_blank" rel="noopener">Suppression de données</a>
      </nav>
      <span id="signature">Maquette locale non officielle, d'après cegelec.nc. Ne pas publier en l'état.</span>
    </div>
  </div>
</footer>"""


def page(fichier, titre, corps, actif=None, hero_titre=None, hero_txt=None, hero_img=None, fil=None, accueil=False, head_extra=""):
    actif = actif or fichier
    if accueil:
        main = corps
    else:
        chemin = '<a href="index.html">Accueil</a>' + "".join(f' › <a href="{h}">{e(t)}</a>' if h else f" › {e(t)}" for t, h in (fil or []))
        style = f' style="--img: url(\'{hero_img}\')"' if hero_img else ""
        txt = f"<p>{e(hero_txt)}</p>" if hero_txt else ""
        main = f"""<div class="page-hero"{style}><div class="wrap">
  <div class="fil">{chemin}</div>
  <h1>{e(hero_titre or titre)}</h1>{txt}
</div></div>
<div class="contenu"><div class="wrap">
{corps}
</div></div>"""
    doc = f"""<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(titre)} – Cegelec Nouvelle-Calédonie (maquette)</title>
<link rel="stylesheet" href="style.css">
{head_extra}
</head>
<body>
{header(actif)}
<main>
{main}
</main>
{footer()}
<script src="site.js"></script>
</body>
</html>
"""
    with open(os.path.join(ROOT, fichier), "w", encoding="utf-8") as f:
        f.write(doc)


# ---------------------------------------------------------------- briques
def carte_ref(r, prefix_ent=True):
    return f"""<a class="carte" href="{r['slug']}" data-themes="{e('|'.join(r['theme']))}">
  <div class="visuel" style="background-image: linear-gradient(to top, rgba(0,0,0,.6), transparent 60%), url('{r['img']}')"><span class="badge">{e(' · '.join(r['theme']))}</span></div>
  <div class="corps"><h3>{e(r['titre'])}</h3><p>{e(r['resume'])}</p><span class="lieu">📍 {e(r['lieu'])}</span><span class="plus">Voir la référence →</span></div>
</a>"""


def carte_ent(x):
    return f"""<a class="carte" href="{x['slug']}">
  <div class="visuel" style="background-image: linear-gradient(to top, rgba(0,0,0,.6), transparent 60%), url('{x['img']}')"><span class="badge">{e(x['badge'])}</span></div>
  <div class="corps"><h3>{e(x['nom'])}</h3><p>{e(x['accroche'])}</p><span class="plus">Découvrir →</span></div>
</a>"""


def fig(src, legende=""):
    cap = f"<figcaption>{e(legende)}</figcaption>" if legende else ""
    return f'<figure><img src="{src}" alt="{e(legende)}" loading="lazy">{cap}</figure>'


def liste(items):
    return "<ul>" + "".join(f"<li>{e(i)}</li>" for i in items) + "</ul>"


def bloc_sites(clair=False):
    return '<div class="sites">' + "".join(
        f"""<div class="site"><h3>{e(s['nom'])}</h3><p>{s['adr']}</p><p><a class="tel" href="tel:{s['tel'].replace(' ', '')}">{s['tel']}</a></p></div>"""
        for s in SITES) + "</div>"


# ---------------------------------------------------------------- pages
def build_home():
    ref_cards = "".join(carte_ref(next(r for r in REFS if r["slug"] == s)) for s in REF_ACCUEIL)
    ent_cards = "".join(carte_ent(x) for x in ENTREPRISES)
    corps = f"""
<div class="hero" id="hero">
  <div class="slide actif" style="--img: url('{P}caroussel_numbo.jpg')"><div class="wrap">
    <span class="etiquette">Bienvenue</span>
    <h1>Cegelec Nouvelle-Calédonie vous souhaite la bienvenue</h1>
    <p>Énergie, traitement de l'air et technologies de l'information : six entreprises, une même exigence de qualité au service du territoire.</p>
    <div class="actions"><a class="btn plein" href="references.html">▶ Voir nos réalisations</a><a class="btn ligne" href="entreprises.html">Nos entreprises</a></div>
  </div></div>
  <div class="slide" style="--img: url('{P}focola_1_crop.jpg')"><div class="wrap">
    <span class="etiquette">Énergie solaire</span>
    <h1>Le photovoltaïque au service du territoire</h1>
    <p>Centrales solaires, serres photovoltaïques, éclairage public solaire : la transition énergétique en action.</p>
    <div class="actions"><a class="btn plein" href="ref-ouaco.html">▶ Centrale solaire de Ouaco</a></div>
  </div></div>
  <div class="slide" style="--img: url('{P}dumbea_mall.jpg')"><div class="wrap">
    <span class="etiquette">Réalisation</span>
    <h1>Dumbéa Mall</h1>
    <p>L'un de nos chantiers à Dumbéa, photographié de nuit.</p>
    <div class="actions"><a class="btn plein" href="references.html">▶ Toutes nos références</a></div>
  </div></div>
  <div class="points" id="points"></div>
</div>

<section class="sombre" id="realisations"><div class="wrap">
  <div class="titre-rang"><h2>Nos réalisations</h2><a href="references.html">Toutes nos références →</a></div>
  <div class="rang">{ref_cards}</div>
</div></section>

<section class="sombre" id="entreprises"><div class="wrap">
  <div class="titre-rang"><h2>Nos entreprises</h2><a href="entreprises.html">Toutes nos entreprises →</a></div>
  <div class="rang">{ent_cards}</div>
</div></section>

<section class="sombre" id="chiffres"><div class="wrap">
  <div class="titre-rang"><h2>Nos chiffres clés</h2><a href="histoire.html">Notre histoire →</a></div>
  <div class="chiffres">
    <div class="chiffre"><strong>6</strong><span>entreprises, chacune associée à une marque</span></div>
    <div class="chiffre"><strong>140+</strong><span>collaborateurs de VINCI Energies en Nouvelle-Calédonie (2021)</span></div>
    <div class="chiffre"><strong>×2</strong><span>chiffre d'affaires doublé en cinq ans</span></div>
    <div class="chiffre"><strong>50 ans</strong><span>de présence sur le territoire</span></div>
  </div>
</div></section>

<section class="sombre" id="contact"><div class="wrap">
  <div class="titre-rang"><h2>Où nous trouver ?</h2><a href="contact.html">Nous contacter →</a></div>
  {bloc_sites()}
</div></section>

<section class="sombre" id="social"><div class="wrap">
  <div class="titre-rang"><h2>Suivez-nous</h2></div>
  <div class="reseaux">
    <a href="https://www.facebook.com/Cegelec.caledonie" target="_blank" rel="noopener">Facebook</a>
    <a href="https://www.linkedin.com/company/cegelec-nouvelle-cal%C3%A9donie/" target="_blank" rel="noopener">LinkedIn</a>
  </div>
</div></section>
<div class="marge-haut"></div>"""
    page("index.html", "Accueil", corps, actif="index.html", accueil=True)


def build_nous_connaitre():
    fil = [("Nous connaître", None)]
    # Histoire
    corps = f"""
<h2>Petit historique de Cegelec Nouvelle-Calédonie</h2>
<p class="intro">La société Cegelec Nouvelle-Calédonie regroupe aujourd'hui six « entreprises » associées chacune à une marque, avec des services à forte valeur ajoutée dans les secteurs de l'énergie, du traitement de l'air et des technologies de l'information.</p>
<p>Elles couvrent les quatre domaines d'activité portés par VINCI Energies :</p>
{liste(["L'industrie", "Le tertiaire", "Les infrastructures", "Les télécommunications"])}
<p>Cegelec Nouvelle-Calédonie est fortement impliqué dans la vie sociétale du territoire et présent dans de nombreuses associations ou syndicats, comme le MEDEF, l'ONNC, la FCBTP et l'AFBTP.</p>
<div class="logos">
  <img src="{O}lamedef_logo-e1611182072639.jpg" alt="MEDEF NC">
  <img src="{O}logo_onnc-e1611182123751.jpg" alt="Observatoire Numérique Nouvelle-Calédonie">
  <img src="{O}fcbtp_logo-e1611181984995.png" alt="FCBTP">
  <img src="{O}logo_afbtp.jpg" alt="AFBTP">
</div>
<h2>Nos chiffres clés</h2>
<p>En 2021, VINCI Energies en Nouvelle-Calédonie, c'est :</p>
{liste(["Près de 3 milliards de chiffre d'affaires dans la zone", "Plus de 140 collaborateurs", "Un chiffre d'affaires qui a doublé en cinq ans"])}
<h2>Frise chronologique</h2>
{fig(O + 'frise_chronologique-e1611181339447.png', 'Les grandes étapes de Cegelec Nouvelle-Calédonie')}
"""
    page("histoire.html", "Notre histoire", corps, fil=fil + [("Notre histoire", None)], hero_img=P + "caroussel_numbo.jpg",
         hero_txt="Une implantation ancrée en Nouvelle-Calédonie, au sein du réseau VINCI Energies.")
    # Organisation
    corps = f"""
<p class="intro">L'organisation de Cegelec Nouvelle-Calédonie et de ses entreprises.</p>
{fig(O + 'organisation.jpg', "Organigramme de Cegelec Nouvelle-Calédonie")}
<p><a class="lien" href="entreprises.html">Découvrir nos entreprises →</a></p>"""
    page("organisation.html", "Notre organisation", corps, fil=fil + [("Notre organisation", None)])
    # Marques
    corps = f"""
<p class="intro">Cegelec Nouvelle-Calédonie porte les marques du groupe VINCI Energies : Actemium, Axians, Building Solutions, Citeos et Omexom.</p>
<p>VINCI Energies a développé des marques fédératrices d'expertises afin de mieux accompagner ses clients dans leurs projets.</p>
<div class="logos">
  <img src="{O}actemium_logo-e1611180030773-300x47-1.jpg" alt="Actemium">
  <img src="{O}axians_logo-e1611180087442.jpg" alt="Axians">
  <img src="{O}cegelec_logo-1-e1608011795431-300x99-1.jpg" alt="Cegelec">
  <img src="{O}logo_citeos-e1611178197790-300x73-1.jpg" alt="Citeos">
  <img src="{O}Omexom-800x472-new-e1611180519178-300x53-1.png" alt="Omexom">
</div>
<p><a class="lien" href="entreprises.html">Voir toutes nos entreprises →</a></p>"""
    page("marques.html", "Nos marques", corps, fil=fil + [("Nos marques", None)])
    # Valeurs
    lettres = [
        ("C", "Confiance", ["Partager nos besoins et attentes de nos parties intéressées", "Respecter nos engagements", "Consulter et améliorer la satisfaction de nos partenaires et clients"]),
        ("E", "Esprit d'entreprise", ["Promouvoir la culture d'entreprise", "S'appuyer sur un socle commun de règles et de méthodes", "Développer l'envie d'entreprendre"]),
        ("S", "Solidarité", ["Diffuser l'information", "Favoriser l'entraide", "Maintenir le dialogue social et le bien-être au travail"]),
        ("A", "Autonomie", ["Évaluer et renforcer les compétences de nos richesses humaines", "Laisser s'exprimer les talents", "Valoriser les initiatives individuelles ou collectives"]),
        ("R", "Responsabilité", ["Maîtriser les risques et créer des opportunités", "Proscrire les situations à risques pour éviter l'accident humain ou environnemental", "Analyser et reporter les performances financières"]),
    ]
    cartes = "".join(f'<div class="valeur"><div class="lettre">{l}</div><h3>{e(t)}</h3>{liste(i)}</div>' for l, t, i in lettres)
    corps = f"""
<p class="intro">Cegelec Nouvelle-Calédonie s'engage dans une démarche d'amélioration afin de pérenniser sa structure et d'assurer son adaptation permanente au contexte économique, écologique et sociétal.</p>
<p>Nos valeurs intrinsèques ont été déclinées en objectifs concrets. Nous nous engageons, au sein du comité de direction et avec l'appui de nos animateurs QHSE, à les mettre en œuvre de façon exemplaire, à en suivre les résultats et à assurer ainsi l'amélioration continue de notre organisation.</p>
<h2>Mission</h2>
<p>Accompagner nos clients, à travers nos entreprises Actemium, Axians, Cegelec Building Solutions et Maintenance Énergies, Cegelec Nord, Citeos et Omexom, en leur apportant des solutions et des services adaptés et répondant à nos critères de qualité, hygiène, santé, sécurité, environnement ainsi qu'aux réglementations.</p>
<h2>Vision</h2>
<p>Proposer des solutions personnalisées, innovantes et à forte valeur ajoutée qui permettront à nos clients d'être plus performants.</p>
<h2>Valeurs et objectifs</h2>
<div class="valeurs">{cartes}</div>
<p><a class="lien" href="{OFFICIEL}/app/uploads/sites/394/2022/11/REF-001-1-Charte-interne-CEGELEC-NC-signee.pdf" target="_blank" rel="noopener">Charte interne Cegelec NC signée (PDF) →</a></p>"""
    page("valeurs.html", "Nos valeurs", corps, fil=fil + [("Nos valeurs", None)])
    # VINCI Energies
    corps = f"""
<p class="intro">VINCI Energies contribue au monde qui change en connectant les infrastructures, les bâtiments et les sites industriels aux flux d'informations et d'énergies pour améliorer votre quotidien.</p>
<p>Cegelec Nouvelle-Calédonie appartient à VINCI, acteur mondial des métiers des concessions et de la construction, qui emploie plus de 200 000 collaborateurs dans une centaine de pays. Notre mission est de concevoir, financer, construire et gérer des infrastructures et des équipements qui contribuent à améliorer la vie quotidienne et la mobilité de chacun.</p>
<p>Parce que notre vision de la réussite est globale et ne se limite pas à nos résultats économiques, nous nous engageons sur la performance environnementale, sociale et sociétale de nos activités. Parce que nos réalisations sont d'utilité publique, nous considérons l'écoute et le dialogue avec les parties prenantes de nos projets comme une condition nécessaire à l'exercice de nos métiers.</p>
<p>L'ambition de VINCI est de créer de la valeur à long terme pour nos clients, nos salariés, nos actionnaires, nos partenaires et pour la société en général.</p>
<h2>Une organisation décentralisée, des valeurs partagées</h2>
{fig(O + 'Schema-VINCI.png', 'Organisation de VINCI et de VINCI Energies')}"""
    page("vinci-energies.html", "VINCI Energies", corps, fil=fil + [("VINCI Energies", None)])
    # Travailler chez nous
    corps = f"""
<p class="intro">Travailler chez Cegelec Nouvelle-Calédonie, c'est contribuer à des réalisations qui facilitent le quotidien, sécurisent la vie de tous les jours ou préparent demain. Rejoindre nos équipes, c'est partager nos succès.</p>
<h2>Pourquoi travailler chez Cegelec Nouvelle-Calédonie ?</h2>
<p>Parce que nos collaborateurs sont les acteurs de la réussite de notre société, qu'ils sont nos meilleurs ambassadeurs sur le terrain auprès de nos clients et portent véritablement les stratégies. Ce sont vos initiatives, vos projets, votre volonté de satisfaire chacun de nos clients et d'évoluer qui nous permettent de concrétiser de multiples réalisations.</p>
<h2>Débuter votre carrière professionnelle</h2>
<p>Cegelec Nouvelle-Calédonie multiplie les initiatives en direction des filières de formation et des jeunes diplômés. Ces actions vous permettent de mieux connaître nos méthodes de travail et de les mettre en pratique tout en vous familiarisant à notre culture. Ce sera pour vous l'occasion de confirmer votre potentiel, et à nous de vous proposer une éventuelle collaboration si l'expérience s'avère concluante.</p>
<h2>Booster vos compétences</h2>
<p>Une attention toute particulière est apportée au projet professionnel et au développement de vos compétences. Tous les collaborateurs ont l'opportunité d'échanger régulièrement avec leur responsable sur leurs objectifs et leur parcours, notamment lors d'un entretien individuel de management : évolutions de carrière possibles, besoins de formation et souhaits éventuels de mobilité.</p>
<h2>Postulez !</h2>
<p>Vous êtes à la recherche d'un stage, d'un contrat en alternance ou d'un emploi ? Nous diffusons régulièrement les descriptifs des postes disponibles dans nos offres d'emploi ainsi que sur l'espace recrutement de VINCI Energies. Pour toute candidature spontanée, envoyez votre CV et une lettre de motivation à <a class="lien" href="mailto:contact@cegelec.nc">contact@cegelec.nc</a>.</p>
<p><a class="btn plein" href="offres-emploi.html">Offres d'emploi</a></p>
{fig(O + 'cegelec-logo-2-1024x421-1.jpg')}"""
    page("travailler-chez-nous.html", "Travailler chez nous", corps, fil=fil + [("Travailler chez nous", None)],
         hero_txt="Rejoindre nos équipes, c'est partager nos succès.")
    # Offres d'emploi
    corps = f"""
<div class="grille">
  <div class="carte"><div class="corps">
    <span class="badge" style="background:#d6001c">CDI</span>
    <h3>OMEXOM : un(e) chef d'équipe CDI à temps complet</h3>
    <p>Recherche d'un(e) chef d'équipe CDI à temps complet.</p>
    <span class="lieu">Domaine : Matériel / Logistique · 📍 Nouméa, Province Sud</span>
  </div></div>
</div>
<p style="margin-top:22px">Candidature spontanée : <a class="lien" href="mailto:contact@cegelec.nc">contact@cegelec.nc</a></p>
<p><a class="lien" href="travailler-chez-nous.html">← Travailler chez nous</a></p>"""
    page("offres-emploi.html", "Offres d'emploi", corps, actif="travailler-chez-nous.html",
         fil=[("Nous connaître", None), ("Travailler chez nous", "travailler-chez-nous.html"), ("Offres d'emploi", None)])


def build_entreprises():
    cartes = "".join(carte_ent(x) for x in ENTREPRISES)
    corps = f"""
<p class="intro">Cegelec Nouvelle-Calédonie regroupe six entreprises associées chacune à une marque du groupe VINCI Energies.</p>
<div class="grille">{cartes}</div>
<h2>Où nous trouver</h2>
<div class="carte-nc">{fig(O + 'carte_nouvelle-caledonie.png', 'Siège social et Cegelec Nord en Nouvelle-Calédonie')}</div>
"""
    page("entreprises.html", "Nos entreprises", corps, fil=[("Nos entreprises", None)])
    for x in ENTREPRISES:
        blocs = "".join(f"<h3>{e(t)}</h3>{liste(i)}" for t, i in x["blocs"])
        bas = f"<h2>{e(x['bas'][0])}</h2><p>{e(x['bas'][1])}</p>" if x["bas"] else ""
        ext = f'<p><a class="lien" href="{x["ext"][1]}" target="_blank" rel="noopener">{x["ext"][0]} →</a></p>' if x["ext"] else ""
        figs = "".join(fig(f) for f in x["figs"])
        autres = "".join(f'<li><a href="{o["slug"]}">{e(o["court"])}</a></li>' for o in ENTREPRISES if o["slug"] != x["slug"])
        corps = f"""
<div class="logos"><img src="{x['logo']}" alt="{e(x['court'])}"></div>
<p class="intro">{e(x['intro'])}</p>
{fig(x['img']) if x['img'].endswith(('.jpg', '.jpeg')) else ''}
<h2>{e(x['titre_bloc'])}</h2>
{blocs}
{figs}
{bas}
{ext}
<h2>Les autres entreprises</h2>
<ul>{autres}</ul>"""
        page(x["slug"], x["court"], corps, actif="entreprises.html", hero_titre=x["nom"], hero_txt=x["accroche"],
             hero_img=x["img"] if x["img"].endswith((".jpg", ".jpeg")) else None,
             fil=[("Nos entreprises", "entreprises.html"), (x["court"], None)])


def build_refs():
    filtres = '<button class="actif" data-theme="">Tous</button>' + "".join(f'<button data-theme="{e(t)}">{e(t)}</button>' for t in THEMES)
    cartes = "".join(carte_ref(r) for r in REFS)
    corps = f"""
<p class="intro">Nos réalisations en Nouvelle-Calédonie : énergie, bâtiment, réseaux et industrie.</p>
<div class="filtres" id="filtres">{filtres}</div>
<div class="grille" id="liste-refs">{cartes}</div>"""
    page("references.html", "Nos réalisations", corps, fil=[("Nos réalisations", None)],
         hero_txt="Références", hero_img=P + "dumbea_mall.jpg")
    for r in REFS:
        fiche = "".join(f"<dt>{e(k)}</dt><dd>{e(v)}</dd>" for k, v in r["fiche"])
        details = ""
        if r["details"]:
            details = "<h2>Détail des travaux</h2>" + liste([f"{k} : {v}" for k, v in r["details"]])
        fig2 = fig(r["fig2"]) if r.get("fig2") else ""
        autres = [o for o in REFS if o["slug"] != r["slug"]][:3]
        voir = "".join(carte_ref(o) for o in autres)
        corps = f"""
<p class="intro">{e(r['resume'])}</p>
{fig(r['img'], r['titre'])}
<div class="fiche"><dl>{fiche}</dl></div>
{details}
{fig2}
<h2>D'autres références</h2>
<div class="grille">{voir}</div>
<p style="margin-top:22px"><a class="lien" href="references.html">← Toutes nos références</a></p>"""
        page(r["slug"], r["titre"], corps, actif="references.html", hero_titre=r["titre"], hero_txt=" · ".join(r["theme"]),
             fil=[("Nos réalisations", "references.html"), (r["titre"], None)])


def build_rse():
    def bloc(titre, txt, items=None, img=None, leg=""):
        return f"""<div class="evenement"><h3>{e(titre)}</h3>{''.join(f'<p>{e(t)}</p>' for t in txt)}{liste(items) if items else ''}{fig(img, leg) if img else ''}</div>"""
    corps = (
        '<p class="intro">En 2020, Cegelec Nouvelle-Calédonie se certifie ISO 14001, norme ISO qui concerne l\'environnement. Dans la continuité de son engagement, et poussée par le groupe VINCI Energies, la société a décidé d\'entamer une démarche RSE : un responsable RSE a été nommé en interne, un diagnostic des actions RSE déjà réalisées a été établi et un plan d\'action a été défini pour 2021.</p>'
        + '<h2>Quelques actions RSE à Cegelec Nouvelle-Calédonie</h2>'
        + bloc("« Mange mieux, bouge plus »", [], [
            "Un producteur de légumes locaux propose l'achat d'un panier de légumes deux fois par mois",
            "Mise à disposition d'un panier de fruits frais par le CE une fois par mois",
            "Mise à disposition gratuite d'une balance électronique professionnelle",
            "Intervention d'un kinésithérapeute sur les chantiers pour déceler les mauvais gestes et mauvaises postures par métier",
            "Création d'un club de va'a", "Ateliers de self-défense"], O + "106922831.jpg")
        + bloc("Réduction de la production de déchets",
               ["Cegelec Nouvelle-Calédonie, et plus particulièrement Omexom, a fait un don de centrales de PC à la Ressourcerie de Nouméa. Les équipements sont remis en état, revendus et réutilisés par d'autres personnes."],
               ["Rendre ces objets accessibles et à petit prix", "Créer de l'échange et du partage", "Sensibiliser les nouveaux salariés à un nouveau mode de consommation et à l'environnement"], O + "1737249268.jpg")
        + bloc("Réduction des impacts du changement climatique",
               ["La société s'est portée acquéreuse de cinq ruches dans la province des Îles, sur l'île de Lifou, et deux autres ruches ont été installées en Province Nord, près du site de Koné."],
               ["Former ses agents dans le domaine de l'apiculture", "Remplacer les cadeaux habituels des clients par des pots de miel issus de cette production, pour les sensibiliser à notre démarche environnementale"], O + "105408359.jpg")
        + bloc("Production d'énergie verte",
               ["Cegelec Nouvelle-Calédonie a installé des panneaux solaires sur son site de Numbo (installation en 2018, mise en production en 2019)."],
               ["Une économie financière par rapport à la facture d'électricité", "Le lancement de l'activité photovoltaïque en interne"], O + "1157999803.jpeg")
        + bloc("Préserver les milieux naturels",
               ["Le 22 septembre 2020, VINCI Energies a lancé sa démarche environnementale, autour de trois axes prioritaires : agir pour le climat, optimiser les ressources grâce à l'économie circulaire et préserver les milieux naturels. Sur le site de Numbo, Cegelec Nouvelle-Calédonie a planté 5 arbres fruitiers et disposé 5 jardinières de plantes grasses, médicinales et aromatiques, qui pourront être récoltées et utilisées par les équipes."], None, O + "2092819312.jpg")
        + bloc("Gestion des déchets sur le parc",
               ["Dans le cadre de sa certification ISO 14001, la société s'est engagée dans une démarche de tri des déchets : une première zone de tri à l'entrée du site (bennes à gravats, câbles, déchets industriels banals et métaux), une zone de gestion plus poussée créée en 2020 (DEEE, bacs à batterie, batteries, hydrocarbures, déchets souillés par des produits chimiques) et le recyclage du papier dans les bureaux depuis mai 2021."], None, O + "Tri-1024x173-1.jpg")
        + '<h2>Éducation et jeunesse</h2>'
        + bloc("Cours à l'UNC",
               ["Dans le cadre de l'objectif n°4 de l'ONU (éducation de qualité), le directeur et le responsable RSE ont présenté aux classes de DUT 1re année GEA et MMI le sujet de la croissance externe, en s'appuyant sur des cas concrets. Cegelec était aussi présent au Forum Projets tutorés des DUT à l'IUT."], None, O + "1634872398445-768x1024-1.jpg")
        + bloc("Parrainage IUT Cegelec – Axians",
               ["Le 11 février 2021, Cegelec et Axians ont signé une convention de parrainage pour les promotions 2021/2022 des DUT GEA et MMI de l'IUT de Nouvelle-Calédonie. Ce partenariat comporte :"],
               ["Un rapprochement entre une société présente depuis 50 ans sur le territoire et l'UNC/IUT", "Une présentation des métiers de gestion chez VINCI Energies et des métiers de l'informatique chez Axians", "Un soutien financier et matériel pour l'IUT de Nouvelle-Calédonie", "Des études de cas concrètes sur des données réelles, soutenues devant les dirigeants", "Un vivier pour une éventuelle embauche future de talents"], O + "dfgh-1024x768-1.jpg")
        + '<h2>Objectifs de développement durable</h2>'
        + fig(O + "4280860750.jpg", "Les 17 objectifs de développement durable de l'ONU")
        + '<p><a class="btn plein" href="certifications.html">Nos certifications</a> &nbsp; <a class="btn contour" href="evenements.html">Les évènements</a></p>'
    )
    page("rse.html", "Notre engagement RSE", corps, fil=[("Notre engagement RSE", None)],
         hero_txt="Une démarche responsable, pour les équipes et pour le territoire.")


def build_certifs():
    corps = f"""
<p class="intro">Cegelec Nouvelle-Calédonie conserve sa triple certification : ISO 9001 (système de management de la qualité), ISO 14001 (système de management de l'environnement) et ISO 45001 (système de management de la sécurité).</p>
<div class="certifs">
  <figure><img src="{O}3768182803.png" alt="Certification ISO 9001"><figcaption>ISO 9001 – Qualité</figcaption></figure>
  <figure><img src="{O}292626281.png" alt="Certification ISO 14001"><figcaption>ISO 14001 – Environnement</figcaption></figure>
  <figure><img src="{O}4137872684.png" alt="Certification ISO 45001"><figcaption>ISO 45001 – Sécurité</figcaption></figure>
</div>
<p>Cette triple certification, délivrée par DNV·GL, démontre la volonté d'améliorer en permanence l'efficacité de l'organisation ainsi que la qualité des prestations et des services.</p>
<p><a class="lien" href="evenements.html">Lire l'audit de renouvellement de juin 2021 →</a></p>"""
    page("certifications.html", "Nos certifications", corps, actif="certifications.html",
         fil=[("Notre engagement RSE", "rse.html"), ("Nos certifications", None)])


def build_events():
    def ev(date, titre, txt, img=None, items=None):
        return f"""<div class="evenement"><span class="date">{e(date)}</span><h3>{e(titre)}</h3>{''.join(f'<p>{e(t)}</p>' for t in txt)}{liste(items) if items else ''}{fig(img) if img else ''}</div>"""
    corps = (
        '<h2>Les évènements 2021</h2>'
        + ev("17 – 21 mai 2021", "Safety Day", ["Dans le cadre de la Safety Week de VINCI Energies et de sa démarche ISO 45001, Cegelec Nouvelle-Calédonie a organisé son Safety Day le jeudi 20 mai. La journée avait pour but de rappeler et de traiter les questions de sécurité et de santé au travail."],
             O + "2365190285.jpg", ["Réveil musculaire", "Compte rendu des visites sécurité du kiné", "Communication non violente", "Réalité virtuelle", "Risques psychosociaux, cannabis et alcool", "Manutention et rappel des fondamentaux sécurité"])
        + ev("Juin 2021", "Audit de renouvellement", ["Cegelec Nouvelle-Calédonie conserve sa triple certification ISO 9001, ISO 14001 et ISO 45001. L'audit s'est déroulé durant la période de confinement, dans le respect des gestes barrières. Merci à DNV·GL pour son efficacité et son professionnalisme."], O + "2930811143.jpg")
        + ev("2021", "COVID-19 : gestes barrières", ["La Nouvelle-Calédonie ayant perdu son statut de Covid free, Cegelec a activé sa cellule de crise interne :"], O + "2785689624.jpg",
             ["Plan de continuité d'activité (PCA) et plans de prévention spéciaux COVID-19", "Journal de bord quotidien et fiches de poste COVID-19", "Vidéos sur les gestes barrières, affiches, quarts d'heure sécurité, mails quotidiens", "Mise à disposition de masques, gels hydroalcooliques et thermomètres infrarouges"])
        + ev("Depuis octobre 2020", "Démarche de diminution des troubles musculosquelettiques", ["Un kinésithérapeute se déplace sur les chantiers et dans les bureaux pour dresser un état des lieux des gestes et postures, et proposer des pistes d'amélioration. Chaque visite fait l'objet d'un rapport sur les évolutions possibles du matériel ou des habitudes ; un bilan a été présenté lors de la Safety Week de mai 2021."], O + "Sans-titre.jpg")
        + ev("2021", "Cegelec Nouvelle-Calédonie intègre la Fondation universitaire de Nouvelle-Calédonie", ["Cegelec participe ainsi à l'objectif n°4 de l'ONU. Son financement soutient les travaux doctoraux d'une doctorante qui développe des techniques non invasives innovantes (laser et lidar) pour le suivi des mangroves urbaines."])
        + '<h2>Les évènements 2020</h2>'
        + ev("28 novembre 2020", "Journée sportive", ["Dernière journée sportive de l'année 2020, à l'Université de la Nouvelle-Calédonie : tournoi de pétanque, tournoi de volley, escalade, activités pour les enfants (maquillage, manège, château gonflable, trampoline) et distribution de cadeaux."], O + "4282327447.jpg")
        + ev("19 septembre 2020", "World Clean Up Day", ["En collaboration avec le service Environnement de la mairie du Mont-Dore, Cegelec a nettoyé le parcours pédestre de Robinson (mangrove). Une quinzaine d'enfants et une quinzaine d'adultes se sont réunis et ont ramassé environ 600 kg de déchets : bouteilles en plastique, pneus, moteurs, vélos, tôles…"], O + "word_clean_up.jpg")
        + ev("3 juillet 2020", "Safety Day", ["En raison du COVID-19, les activités prévues n'ont pas eu lieu. À la place, des quarts d'heure sécurité spécifiques à chaque service ont été organisés : attitudes et comportements, proactivité, signalement des situations dangereuses et incidents, port des EPI."])
    )
    page("evenements.html", "Les évènements", corps, actif="evenements.html",
         fil=[("Notre engagement RSE", "rse.html"), ("Les évènements", None)])


def build_contact_plan():
    corps = f"""
<div class="duo">
  <form class="contact" onsubmit="event.preventDefault(); document.getElementById('retour').hidden = false;">
    <div class="deux">
      <label>Civilité *<select required><option value="">—</option><option>Mme</option><option>M.</option></select></label>
      <label>Nom *<input required></label>
    </div>
    <div class="deux">
      <label>Prénom<input></label>
      <label>Nom de votre entreprise<input></label>
    </div>
    <div class="deux">
      <label>E-mail *<input type="email" required></label>
      <label>Localisation (code postal et ville) *<input required></label>
    </div>
    <label>Sujet du message *<input required></label>
    <label>Votre message *<textarea rows="6" required></textarea></label>
    <p style="font-size:.85rem;color:#5a606b">Les champs marqués d'un * sont obligatoires. Les données personnelles recueillies sont transmises uniquement à l'entreprise Cegelec Nouvelle-Calédonie et servent à répondre à votre demande.</p>
    <button class="btn plein" type="submit">Envoyer</button>
    <p class="note" id="retour" hidden>Maquette : l'envoi est désactivé, aucun message n'a été transmis.</p>
  </form>
  <div>
    {bloc_sites()}
    <p style="margin-top:18px">Candidature spontanée : <a class="lien" href="mailto:contact@cegelec.nc">contact@cegelec.nc</a></p>
    <div class="carte-nc" style="margin-top:14px">{fig(O + 'carte_nouvelle-caledonie.png')}</div>
  </div>
</div>"""
    page("contact.html", "Contact", corps, fil=[("Contact", None)])
    # Plan du site
    def ul(items):
        return "<ul>" + "".join(f'<li><a class="lien" href="{h}">{e(t)}</a></li>' for t, h in items) + "</ul>"
    corps = "<h2>Nous connaître</h2>" + ul([("Notre histoire", "histoire.html"), ("Notre organisation", "organisation.html"), ("Nos marques", "marques.html"), ("Nos valeurs", "valeurs.html"), ("VINCI Energies", "vinci-energies.html"), ("Travailler chez nous", "travailler-chez-nous.html"), ("Offres d'emploi", "offres-emploi.html")]) \
        + "<h2>Nos entreprises</h2>" + ul([("Toutes nos entreprises", "entreprises.html")] + [(x["nom"], x["slug"]) for x in ENTREPRISES]) \
        + "<h2>Nos réalisations</h2>" + ul([("Toutes nos références", "references.html")] + [(r["titre"], r["slug"]) for r in REFS]) \
        + "<h2>Notre engagement RSE</h2>" + ul([("Notre engagement RSE", "rse.html"), ("Nos certifications", "certifications.html"), ("Les évènements", "evenements.html")]) \
        + "<h2>Contact</h2>" + ul([("Contact", "contact.html")])
    page("plan-du-site.html", "Plan du site", corps, fil=[("Plan du site", None)])


def build_salle_de_jeu():
    """Page cachée (secret.html) : salle de jeux de cartes aux couleurs des marques.
    Onglets : Duel des chantiers (jeu à la Hearthstone), Paires, Bibliothèque.
    Absente du menu, du pied de page et du plan du site.
    Accès : taper « secret » au clavier, ou 5 clics sur la signature du pied de page."""
    doc = """<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<title>Salle de jeux – Cegelec Nouvelle-Calédonie (maquette)</title>
<link rel="stylesheet" href="cartes.css">
</head>
<body>
<div class="bandeau-marques" aria-hidden="true"><i class="m-cegelec"></i><i class="m-axians"></i><i class="m-actemium"></i><i class="m-omexom"></i></div>
<header class="salle-entete">
  <a class="logo" href="index.html" title="Retour au site"><img src="assets/logo_cegelec.jpg" alt="Cegelec"></a>
  <div class="titre"><h1>Salle de jeux</h1><p>Duel de cartes, paires et collection : aux couleurs des marques.</p></div>
  <a class="retour" href="index.html">← Retour au site</a>
</header>

<nav class="onglets" role="tablist" aria-label="Choix du jeu">
  <button role="tab" class="m-cegelec actif" data-jeu="duel" aria-selected="true"><span class="sym">⚔</span> Duel des chantiers <small>Le jeu</small></button>
  <button role="tab" class="m-axians" data-jeu="paires" aria-selected="false"><span class="sym">♦</span> Paires <small>Mémoire</small></button>
  <button role="tab" class="m-biblio" data-jeu="biblio" aria-selected="false"><span class="sym">★</span> Bibliothèque <small>Les cartes</small></button>
</nav>
<div class="dos-choix" id="dos-choix"><span>Dos de carte :</span></div>

<main class="table">

  <!-- ============ DUEL DES CHANTIERS ============ -->
  <section class="jeu actif" id="jeu-duel">

    <div id="d-choix" class="duel-choix">
      <h2>Duel des chantiers</h2>
      <p class="aide">Affronte « le client exigeant » avec un paquet de 20 cartes de l'équipe. Choisis ta marque :</p>
      <div id="d-familles" class="duel-familles"></div>
      <p class="legende-effets"><span><i class="puce cri"></i>Cri de guerre : effet immédiat quand la carte est posée</span><span><i class="puce pouvoir"></i>Pouvoir : effet permanent de la carte</span></p>
      <details class="regles">
        <summary>Comment jouer ?</summary>
        <ul>
          <li><b>Au départ :</b> tu reçois 3 cartes ; clique sur celles que tu veux remplacer avant de commencer.</li>
          <li><b>But :</b> faire tomber les PV du client exigeant à 0 avant qu'il ne fasse de même avec toi (30 PV chacun).</li>
          <li><b>Énergie ⚡ :</b> tu en gagnes 1 de plus à chaque tour (jusqu'à 10). Chaque carte a un coût, en haut à gauche.</li>
          <li><b>Jouer une carte :</b> clique sur une carte de ta main (bordure verte = jouable). Elle arrive sur ton terrain (5 cartes maximum).</li>
          <li><b>Attaquer :</b> clique sur une de tes cartes prêtes (bordure verte), puis sur une carte adverse ou sur le client. L'attaque est en bas à gauche, la vie en bas à droite.</li>
          <li><b>Une carte posée dort un tour</b> : elle ne peut attaquer qu'à ton tour suivant (sauf « Ruée »).</li>
          <li><b>Provocation 🧱 :</b> les cartes adverses avec Provocation doivent être attaquées en premier.</li>
          <li><b>Capacités des marques :</b> Cegelec 🛡 Bouclier · Building Solutions 🧱 Provocation · Maintenance Énergies 🔧 Soin · Cegelec Nord ⚡ Foudre · Axians 📶 Pioche · Actemium 🤖 Ruée · Omexom ☀️🔗 Énergie et renfort · Citeos 💡 Éclair · CASTOR 🦫 Épargne.</li>
          <li><b>Astuce :</b> survole une carte pour lire sa fiche complète.</li>
        </ul>
      </details>
    </div>

    <div id="d-table" class="duel-table" hidden>
      <div class="barre">
        <span id="d-tour">Tour 1</span>
        <button class="bouton" id="d-abandon" type="button">Abandonner</button>
      </div>
      <div id="d-mulligan" class="duel-mulligan" hidden>
        <h2>Ta main de départ</h2>
        <p class="aide">Clique sur les cartes que tu veux <b>remplacer</b>, puis valide. Les cartes marquées retournent dans le paquet et tu en piocheras de nouvelles.</p>
        <div id="d-mull-main" class="duel-main mull-main"></div>
        <button class="bouton" id="d-mulligan-ok" type="button">Garder cette main et commencer</button>
      </div>
      <div id="d-jeu-zone">
      <div id="d-ia-heros" class="zone-heros"></div>
      <div id="d-ia-main" class="main-ia" aria-label="Main de l'adversaire"></div>
      <div id="d-ia-plateau" class="duel-rangee" aria-label="Terrain de l'adversaire"></div>
      <div class="duel-ligne">— ligne de chantier —</div>
      <div id="d-joueur-plateau" class="duel-rangee" aria-label="Ton terrain"></div>
      <div class="duel-bas">
        <div id="d-joueur-heros" class="zone-heros"></div>
        <button class="bouton" id="d-fin-tour" type="button">Fin du tour ➜</button>
      </div>
      <div id="d-joueur-main" class="duel-main" aria-label="Ta main"></div>
      <p id="d-log" class="duel-log" aria-live="polite"></p>
      </div>
      <div id="d-banniere" class="banniere" aria-hidden="true"></div>
      <div id="d-confettis" class="confettis" aria-hidden="true"></div>
      <div id="d-fin" class="duel-fin" hidden>
        <p id="d-message"></p>
        <div class="actions-jeu">
          <button class="bouton" id="d-rejouer" type="button">Rejouer</button>
          <button class="bouton" id="d-menu" type="button">Changer de deck</button>
        </div>
      </div>
    </div>
  </section>

  <!-- ============ PAIRES ============ -->
  <section class="jeu" id="jeu-paires">
    <div class="barre">
      <span>Coups : <b id="p-coups">0</b></span><span>Temps : <b id="p-temps">0:00</b></span><span>Record : <b id="p-record">—</b></span>
      <button class="bouton" id="p-nouvelle" type="button">Nouvelle partie</button>
    </div>
    <p class="aide">Retrouve toutes les paires de collègues en un minimum de coups.</p>
    <div id="p-grille" class="grille-paires"></div>
    <p class="fin" id="p-fin" hidden></p>
  </section>

  <!-- ============ BIBLIOTHÈQUE ============ -->
  <section class="jeu" id="jeu-biblio">
    <div class="barre">
      <span>Cartes : <b id="bib-nb">0</b></span>
      <span class="biblio-nav">
        <button class="bouton" id="bib-prec" type="button" aria-label="Carte précédente">‹</button>
        <button class="bouton" id="bib-suiv" type="button" aria-label="Carte suivante">›</button>
      </span>
    </div>
    <p class="aide">La collection des cartes de l'équipe : fais défiler, filtre par marque, par type ou par rareté. Les cartes d'exemple se remplacent dans <code>equipe.js</code> et <code>objets.js</code>.</p>
    <div class="filtres-biblio">
      <label>Marque
        <select id="bib-marque"><option value="">Toutes</option></select>
      </label>
      <label>Type
        <select id="bib-type">
          <option value="">Tous</option><option value="direction">Direction</option><option value="responsable">Responsable</option>
          <option value="technicien">Technicien</option><option value="objet">Objet</option>
        </select>
      </label>
      <label>Rareté
        <select id="bib-rarete">
          <option value="">Toutes</option><option>Commune</option><option>Rare</option><option>Épique</option><option>Légendaire</option>
        </select>
      </label>
      <label>Tri
        <select id="bib-tri">
          <option value="puissance">Puissance (décroissante)</option>
          <option value="nom">Nom</option>
          <option value="marque">Marque</option>
        </select>
      </label>
    </div>
    <div class="biblio-liste" id="bib-liste" tabindex="0" aria-label="Liste des cartes"></div>
  </section>
</main>

<footer class="salle-pied">Maquette locale non officielle · couleurs inspirées des logos Cegelec, Actemium et Omexom ; Axians est en violet pour le distinguer d\'Omexom.</footer>
<script src="collegues.js"></script>
<script src="equipe.js"></script>
<script src="objets.js"></script>
<script src="cartes.js"></script>
</body>
</html>
"""
    with open(os.path.join(ROOT, "secret.html"), "w", encoding="utf-8") as f:
        f.write(doc)


if __name__ == "__main__":
    build_home()
    build_salle_de_jeu()
    build_nous_connaitre()
    build_entreprises()
    build_refs()
    build_rse()
    build_certifs()
    build_events()
    build_contact_plan()
    n = len([f for f in os.listdir(ROOT) if f.endswith(".html")])
    print(f"{n} pages générées dans {ROOT}")
