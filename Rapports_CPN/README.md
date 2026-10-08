# Rapports CPN – Suivi des interventions d'astreinte

Projet Power BI (format **PBIP**, éditable sous Power BI Desktop) qui suit et analyse les **interventions d'astreinte CPN** de Cegelec, réalisées sur trois domaines techniques.

## Objectif

Les techniciens saisissent un rapport après chaque intervention d'astreinte (application Teepee / SafePlace). Ce rapport Power BI les centralise afin de :

- **Compter** le nombre d'interventions par mois et par année ;
- **Mesurer** le temps passé (total et moyen) par domaine ;
- **Consulter** le détail de chaque rapport (date, numéro, temps, contenu du rapport).

## Contenu du rapport (3 pages, 1280×720)

| Page | Domaine | Contenu |
|---|---|---|
| `Astreinte_Anti-Intrusion` | Anti-intrusion | Interventions sur les systèmes anti-intrusion |
| `Astreinte_3PBL` | 3PBL | Interventions 3PBL |
| `Astreinte_VIDEO` | Vidéo | Interventions sur les systèmes vidéo |

Chaque page a la même structure :

1. **Segment (filtre) Année**, issu de la table de dates ;
2. **Cartes** : temps total et temps moyen d'intervention (format `X h XX`) ;
3. **Histogramme** : nombre de rapports par mois ;
4. **Tableau** : date d'arrivée, numéro de rapport, temps et rapport.

## Modèle de données (`Rapports_CPN.SemanticModel`)

Les données sont importées (mode *Import*) depuis des fichiers Excel exposés par l'API Power BI de **safeplace.teepee.fr** (`Web.Contents` avec en-têtes `Client_Id` / `Client_Secret`).

| Table | Rôle |
|---|---|
| `RapportCPNAntiIntrus` | Rapports d'astreinte Anti-intrusion |
| `RapportCPN3PBL` | Rapports d'astreinte 3PBL |
| `RapportCPNVideO` | Rapports d'astreinte Vidéo |
| `USER` | Référentiel des utilisateurs (nom, prénom, e-mail, poste, service…) |
| `TAB_Date` | Table calendrier calculée en DAX (du 06/01/2025 à la fin du mois courant) : année, mois, trimestre, semaine ISO, jour ouvré, semaine courante… |

Requêtes intermédiaires (`expressions.tmdl`), classées par groupes (`VIDEO\RELATION`, `VIDEO\TRSF`, `Anti-intusion`, `3PBL`) : tables de relation rapport ↔ utilisateur, rôles Teepee, photos jointes.

**Transformations Power Query** : promotion des en-têtes, typage, jointure avec `USER` pour obtenir une colonne `Nom Prenom` (« Nom, Prénom »), séparation de la date et de l'heure pour produire `Temps` (durée d'intervention) et la date d'arrivée.

**Relations** : chaque table de rapports est reliée à `TAB_Date` par sa date d'arrivée (`DateArriver`, `Datearrivee`, `Date arriver`). Les dates secondaires ont des tables de dates automatiques Power BI (`LocalDateTable_*`).

**Mesures DAX** (une série par domaine) :

- `Temps total (min) …` : somme des durées en minutes (`HOUR*60 + MINUTE` sur `Temps`) ;
- `Temps moyen (min) …` : moyenne des durées en minutes ;
- `Temps total …` / `Temps moyen …` : mise en forme `X h XX` pour l'affichage.

## Structure du dossier

```
Rapports_CPN/
├── Rapports_CPN.pbip            # Fichier projet à ouvrir dans Power BI Desktop
├── Rapports_CPN.Report/         # Définition du rapport (pages, visuels, thème)
└── Rapports_CPN.SemanticModel/  # Modèle sémantique (tables, mesures, relations, requêtes M)
```

## Ouvrir le projet

1. Ouvrir `Rapports_CPN.pbip` avec Power BI Desktop (fonction *Projets Power BI* activée).
2. **Renseigner les identifiants d'accès** : dans les requêtes, les valeurs `<CLIENT_ID_A_RENSEIGNER>` et `<CLIENT_SECRET_A_RENSEIGNER>` ont volontairement été remplacées par des placeholders (voir ci-dessous).
3. Actualiser les données.

## Sécurité

Les fichiers d'origine contenaient en clair les `Client_Id` / `Client_Secret` de l'API Teepee. Ils ont été **retirés avant versionnement** (ils n'apparaissent pas dans ce dépôt, mais figuraient dans le fichier source partagé). Il est recommandé de **les régénérer côté Teepee** et, à terme, de les stocker dans des paramètres Power BI ou la passerelle de données plutôt que dans le code M.

Les fichiers locaux (`.pbi/cache.abf`, `localSettings.json`) sont exclus par le `.gitignore`.
