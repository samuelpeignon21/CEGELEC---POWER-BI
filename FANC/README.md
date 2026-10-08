# FANC – Suivi de la maintenance CVC

Projet Power BI (format **PBIP**, éditable sous Power BI Desktop) qui suit l'activité de maintenance **CVC** (chauffage, ventilation, climatisation) réalisée pour le client **FANC** : interventions correctives, interventions préventives et parc d'équipements.

## Objectif

Les techniciens saisissent leurs bons d'intervention (BI) et les clients leurs demandes (tickets) dans la plateforme Teepee / SafePlace. Ce rapport rassemble ces données pour :

- **Mesurer l'activité** : nombre de bons d'intervention, temps total, moyen et médian passé ;
- **Suivre les correctifs et les préventifs** par année, trimestre, mois et site ;
- **Consulter le détail** de chaque intervention (compte rendu, constat d'arrivée, pièces à remplacer…) ;
- **Surveiller le parc d'équipements** : criticité, équipements à l'arrêt ou en marche dégradée.

## Contenu du rapport (3 pages, 1280×720, thème *Storm*)

| Page | Contenu |
|---|---|
| **Rapport d'activités correctives CVC** | Segments (année, trimestre, numéro de BI, numéro client, « intervention réalisée en »), cartes (nombre de BI, temps moyen, temps médian), histogramme du nombre de BI par mois, barres par site, tableau détaillé (compte rendu, constat d'arrivée, pièces à remplacer, informations de la demande client…) |
| **Rapport d'activités préventives CVC** | Segments (année, site), cartes (nombre de BI, temps total passé, temps moyen), histogramme par site, tableau (compte rendu préventif, dates de création et de fin, description, numéro de BI) |
| **Parc Équipements** | Segments site / sous-site, cartes de synthèse (équipements critiques, à l'arrêt, en marche dégradée, % de criticité), tableau du parc (local, désignation, marque, puissance, n° de série, statut, criticité, mesures, commentaire) |

## Modèle de données (`FANC.SemanticModel`)

Les données sont importées (mode *Import*) depuis des fichiers Excel exposés par l'API Power BI de **safeplace.teepee.fr** (`Web.Contents` avec en-têtes `client_id` / `client_secret`, 23 requêtes).

### Tables principales (`Tab_*`)

| Table | Rôle |
|---|---|
| `Tab_Tickets` | Demandes d'intervention (motif, statut, priorité, dates de création/résolution, demandeur…) |
| `Tab_Bons d'Intervention_Tickets` | **Table de faits centrale** : bons d'intervention correctifs et préventifs (type, compte rendu, signature client, temps en heures…) |
| `Tab_Bons d'Intervention_Maintenance` | BI issus du module maintenance, ajoutés à la table précédente |
| `Tab_Horraires` | Horaires saisis par BI (début, fin, temps en heures) |
| `Tab_Equipements` | Parc d'équipements (désignation, marque, statut, criticité, puissance…) enrichi de l'entreprise, du site et du sous-site |
| `Tab_Entreprise`, `Tab_Sites`, `Tab_SousSites` | Référentiels clients, sites et sous-sites |
| `Tab_Validation ticket` | Validation des tickets par le client |
| `Tab_date` | Calendrier calculé en DAX (de 2024-01-01 à fin du mois courant) : année, mois, trimestre, semaine ISO, jour ouvré, semaine courante |
| `Mesures` | Table vide qui regroupe les mesures DAX |

### Tables de liaison et d'historique

- `Rel_Ticket->Entreprise`, `Rel_Ticket->Sites`, `Rel_Ticket->BI`, `Rel_Ticekt->Validation` : relations ticket ↔ entreprise / site / BI / validation ;
- `Rel_BI->Entreprise`, `Rel_BI->Sites` : relations BI ↔ entreprise / site ;
- `Rel_Equipements->Entreprise|Sites|SousSites` : relations équipement ↔ entreprise / site / sous-site ;
- `Tab_Entreprise_Historique`, `Tab_Site_Historique`, `Rel_Horraires_BI_Historique`, `Rel_BI->…_Historique` : **données de l'ancien système**, ajoutées (`Table.Combine`) aux tables actuelles pour conserver l'historique. L'historique entreprise est filtré sur le client « FANC ».

### Transformations Power Query

- Renommage et typage des colonnes, suppression des colonnes inutiles ;
- Fusion des BI « tickets » et « maintenance » (`Table.Combine`) ;
- **Filtres métier** : on ne garde que les BI dont le statut n'est ni vide ni « À faire », **et** dont la signature client est « OUI » (colonne calculée à partir du champ de signature) ;
- Colonne conditionnelle pour distinguer les BI préventifs ;
- Horaires : suppression des valeurs aberrantes de `TempsEnHeure` (négatives, nulles ou démesurées) ;
- Équipements : jointures successives avec entreprise, site et sous-site ;
- Requête `Erreurs dans Tab_Entreprise` : requête de diagnostic générée par Power BI (lignes en erreur).

### Relations

Schéma en étoile autour de `Tab_Bons d'Intervention_Tickets` : tickets ↔ BI via `Rel_Ticket->BI`, BI ↔ sites/entreprises via les tables `Rel_BI->…`, `Tab_date` reliée à la date de création des BI, équipements reliés à leur entreprise/site/sous-site. Certaines relations sont en filtrage bidirectionnel, d'autres inactives (`Rel_Ticket->Entreprise`, `Rel_Ticket->Sites`).

### Mesures DAX (table `Mesures`)

| Mesure | Définition |
|---|---|
| `Nb Tickets` / `Nb Tickets Résolus` | Nombre de tickets / tickets au statut « Resolu » |
| `KPI Couleur Résolution` | Vert si tous les tickets sont résolus, rouge sinon (mise en forme conditionnelle) |
| `Temps Total passé` / `Temps Moyen Intervention` / `Temps Médian Intervention` | Somme, moyenne, médiane de `Temps en heures` |
| `Nbr_Equipements_Critiques` | Équipements de criticité « Critique » |
| `Nbr_Equipements_Arrêt` / `Nbr_Equipements_Marche_dégradée` | Équipements à l'arrêt / en marche dégradée |
| `%_Criticité` | Part d'équipements critiques dans le parc |

## Structure du dossier

```
FANC/
├── FANC.pbip              # Fichier projet à ouvrir dans Power BI Desktop
├── FANC.Report/           # Définition du rapport (pages, visuels, thème Storm, logo)
└── FANC.SemanticModel/    # Modèle sémantique (tables, mesures, relations, requêtes M)
```

## Ouvrir le projet

1. Ouvrir `FANC.pbip` avec Power BI Desktop (fonction *Projets Power BI* activée).
2. Renseigner les identifiants d'accès : les valeurs `<CLIENT_ID_A_RENSEIGNER>` et `<CLIENT_SECRET_A_RENSEIGNER>` des requêtes sont des placeholders (voir ci-dessous).
3. Actualiser les données.

## Sécurité

Les requêtes contenaient en clair des `client_id` / `client_secret` de l'API Teepee (plusieurs jeux de clés selon les sources). Ils ont été **remplacés par des placeholders** dans la version actuelle du dépôt. Attention : ils restent visibles dans l'**historique Git** des commits précédents. Il est donc recommandé de **les régénérer côté Teepee**, puis de les stocker dans des paramètres Power BI ou la passerelle de données plutôt que dans le code M.
