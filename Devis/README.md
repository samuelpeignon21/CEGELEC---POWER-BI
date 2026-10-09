# Devis – Breakdown quote tracking

Power BI project (**PBIP** format, editable in Power BI Desktop) that tracks the **breakdown repair quotes** (*devis de dépannage*) of Cegelec New Caledonia: quote volumes and amounts, follow-up dates, clients, sites, jobs (*affaires*) and managers.

It is a cleaned-up rebuild of the original `DEVIS.pbit` template: same Teepee / SafePlace source, but with a proper star schema, one date table, typed and trimmed columns, readable names and a ready-to-use set of DAX measures. The report itself (`Devis.Report`) only contains an empty page: the visuals are left to be designed.

## Before the first refresh

1. Open `Devis.pbip` in Power BI Desktop (*Power BI Project* feature enabled).
2. **Transform data** → query `SRC_Classeur` → replace `<CLIENT_ID_A_RENSEIGNER>` and `<CLIENT_SECRET_A_RENSEIGNER>` with the Teepee API credentials (they are **not versioned**). This is the only query that holds them; every table reads its data through it.
3. If asked, set the `safeplace.teepee.fr` data source to *Anonymous* access, then **Refresh**.
4. Check the points listed under [Assumptions to verify](#assumptions-to-verify).

> The original `.pbit` stored the API secret in clear text. Since it has been shared, it is worth regenerating the `Client_Secret` on the Teepee side.

## Data model (`Devis.SemanticModel`)

Import mode, 6 tables + 1 measure table, one workbook downloaded through `Web.Contents` (`client_id` / `client_secret` headers).

| Table | Role |
|---|---|
| `FACT_Devis` | One row per quote: number, title, state, type, creation and follow-up dates, total excl. tax (`Total HT`), TGC, validated / purchase-order flags, free-text fields. Carries the keys to all dimensions. |
| `DIM_Clients` | Clients, **current + archived** (`Origine` = Actif / Archive), de-duplicated on `Client_ID`. |
| `DIM_Sites` | Client sites / agencies, **current + archived**, with address, postal code, city and GPS coordinates when known. |
| `DIM_Affaires` | Codex jobs linked to the quote (project number, descriptions, WBS, dates, service, quote price). Technical columns are kept but hidden. |
| `DIM_Utilisateurs` | Users, used for the quote's two managers (RA and RT). |
| `DIM_Calendrier` | Single DAX date table (from the first creation year to the end of the latest year in the data, at least the current year). Replaces the 11 hidden *LocalDateTable* of the original; auto date/time is disabled. |
| `Mesures` | Empty table that groups the DAX measures. |

### Relationships

| From (many) | To (one) | State |
|---|---|---|
| `FACT_Devis[Client_ID]` | `DIM_Clients[Client_ID]` | active |
| `FACT_Devis[Site_ID]` | `DIM_Sites[Site_ID]` | active |
| `FACT_Devis[Affaire_ID]` | `DIM_Affaires[Affaire_ID]` | active |
| `FACT_Devis[Responsable_RA_ID]` | `DIM_Utilisateurs[Utilisateur_ID]` | active |
| `FACT_Devis[Responsable_RT_ID]` | `DIM_Utilisateurs[Utilisateur_ID]` | inactive (`USERELATIONSHIP`) |
| `FACT_Devis[Date de création]` | `DIM_Calendrier[Date]` | active |
| `FACT_Devis[Date de relance]` | `DIM_Calendrier[Date]` | inactive (`USERELATIONSHIP`) |

The original model had no link from the quotes to the clients, the jobs or the managers; those were missing and are now added.

### Power Query

- `SRC_Classeur`: the workbook (single place for the URL and credentials). `fnFeuille(name)`: reads a sheet and promotes its headers.
- Helpers: `fnNet` (trim, empty text → null), `fnNombre` (number or French-formatted text → number), `fnCoord` (GPS), `fnBool` (0/1/oui/non → true/false), `fnCodePostal` (text, padded to 5 digits so leading zeros are not lost), `fnAjouterCle` (left join of a quote-to-X relation sheet).
- Each table: select the useful columns, rename them (readable French names), clean text, convert values, set explicit types (`fr-FR` culture), de-duplicate on the key and drop rows without key.
- Clients and sites: current and archived records are appended and de-duplicated (current record wins).
- Relation sheets are reduced to one row per quote before joining, so the fact table can never grow (if a quote has several jobs / managers, the first one is kept).

### DAX measures (`Mesures`)

| Folder | Measures |
|---|---|
| Volumes | `Nombre de devis`, `Nombre de clients`, `Nombre de sites` |
| Montants | `Montant HT`, `Montant HT moyen`, `Montant HT cumul annuel` |
| Comparaison N-1 | `Montant HT N-1`, `Variation Montant HT vs N-1`, `Nombre de devis N-1` |
| Suivi | `Devis validés`, `Taux de validation`, `Devis à relancer`, `Délai moyen avant relance (jours)` |

Implicit measures are discouraged: columns are summarised through these measures only.

## Assumptions to verify

These could not be checked because the `.pbit` holds the model but no data:

- **`Valide`** is read as "quote validated" (`Validé`, drives `Devis validés` and `Taux de validation`); `EnregistrementBC` as "purchase order recorded" (`BC enregistré`).
- **Managers**: sheet `Rel_Utilisateurs (Re` → `Responsable_RA_ID`, sheet `Rel_Utilisateurs (El` → `Responsable_RT_ID` (as the original query names `Rel_Responsable(RA)` / `(RT)` suggest).
- **`TotalMainDOeuvre_1…8` and `TauxHoraireTechniciens_1`**: meaning unknown, kept **hidden** under their original names. Rename and unhide the ones you need.
- **`Total HT`** keeps its decimals (the original forced it to a whole number) but is displayed without them; amounts are probably in XPF.
- **`État du devis`**: its values are not known, so no measure depends on them. Once the list of states is known, add measures such as "accepted quotes" and "conversion rate".
- **`Devis à relancer`** counts quotes whose follow-up date is today or earlier, whatever their state.
- In `DIM_Affaires`, columns `AnneE`, `AnneE_1`, `AnneE_2`, `ConcateNation`, `TECH_1`, `TECH_2`, `OSMOSE_CD`, … come from the source as-is and are hidden.
