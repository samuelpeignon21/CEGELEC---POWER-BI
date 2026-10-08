# Rapports_CPN – On-call intervention tracking

Power BI project (**PBIP** format, editable in Power BI Desktop) that tracks and analyses Cegelec's **CPN on-call interventions** across three technical domains.

## Purpose

After each on-call intervention, technicians fill in a report (Teepee / SafePlace application). This Power BI report centralises those reports in order to:

- **Count** the number of interventions per month and per year;
- **Measure** the time spent (total and average) per domain;
- **Browse** the details of each report (date, number, time, report content).

## Report content (3 pages, 1280×720)

| Page | Domain | Content |
|---|---|---|
| `Astreinte_Anti-Intrusion` | Anti-intrusion | Interventions on anti-intrusion systems |
| `Astreinte_3PBL` | 3PBL | 3PBL interventions |
| `Astreinte_VIDEO` | Video | Interventions on video systems |

(*Astreinte* = on call.) Every page has the same structure:

1. **Year slicer**, based on the date table;
2. **Cards**: total and average intervention time (`X h XX` format);
3. **Column chart**: number of reports per month;
4. **Table**: arrival date, report number, time and report text.

## Data model (`Rapports_CPN.SemanticModel`)

Data is imported (*Import* mode) from Excel files exposed by the Power BI API of **safeplace.teepee.fr** (`Web.Contents` with `Client_Id` / `Client_Secret` headers).

| Table | Role |
|---|---|
| `RapportCPNAntiIntrus` | Anti-intrusion on-call reports |
| `RapportCPN3PBL` | 3PBL on-call reports |
| `RapportCPNVideO` | Video on-call reports |
| `USER` | User reference table (last name, first name, e-mail, position, department…) |
| `TAB_Date` | Calendar table computed in DAX (from 2025-01-06 to the end of the current month): year, month, quarter, ISO week, working day, current week… |

Intermediate queries (`expressions.tmdl`), organised in groups (`VIDEO\RELATION`, `VIDEO\TRSF`, `Anti-intusion`, `3PBL`): report ↔ user relation tables, Teepee roles, attached photos.

**Power Query transformations**: header promotion, typing, join with `USER` to build a `Nom Prenom` column ("Last name, First name"), and splitting of date and time to produce `Temps` (intervention duration) and the arrival date.

**Relationships**: each report table is linked to `TAB_Date` through its arrival date (`DateArriver`, `Datearrivee`, `Date arriver`). Secondary dates use Power BI automatic date tables (`LocalDateTable_*`).

**DAX measures** (one series per domain):

- `Temps total (min) …`: sum of durations in minutes (`HOUR*60 + MINUTE` on `Temps`);
- `Temps moyen (min) …`: average duration in minutes;
- `Temps total …` / `Temps moyen …`: `X h XX` formatting for display.

## Folder structure

```
Rapports_CPN/
├── Rapports_CPN.pbip            # Project file to open in Power BI Desktop
├── Rapports_CPN.Report/         # Report definition (pages, visuals, theme)
└── Rapports_CPN.SemanticModel/  # Semantic model (tables, measures, relationships, M queries)
```

## Opening the project

1. Open `Rapports_CPN.pbip` with Power BI Desktop (*Power BI Projects* feature enabled).
2. **Fill in the access credentials**: in the queries, the values `<CLIENT_ID_A_RENSEIGNER>` and `<CLIENT_SECRET_A_RENSEIGNER>` ("to be filled in") are intentional placeholders (see below).
3. Refresh the data.

## Security

The original files contained the Teepee API `Client_Id` / `Client_Secret` in clear text. They were **removed before versioning** (they do not appear in this repository, but were present in the shared source file). It is recommended to **regenerate them in Teepee** and, in the long run, to store them in Power BI parameters or in the data gateway rather than in the M code.

Local files (`.pbi/cache.abf`, `localSettings.json`) are excluded by `.gitignore`.
