# CEGELEC_NC

Power BI reports (PBIP format) used to track technical interventions at Cegelec New Caledonia. Each project lives in its own folder and is documented there: purpose, report pages, data model and DAX measures.

## Power BI projects

| Project | Description |
|---|---|
| [`FANC_CVC/`](FANC_CVC/README.md) | HVAC maintenance tracking for the client FANC: corrective and preventive intervention orders, time spent, equipment fleet and criticality |
| [`Rapports_CPN/`](Rapports_CPN/README.md) | On-call intervention tracking (Anti-intrusion, 3PBL, Video): number of reports, total and average time per month/year |
| [`Devis/`](Devis/README.md) | Breakdown quote tracking: quote volumes and amounts, follow-up dates, clients, sites, jobs and managers (star schema, ready for report design) |

## Requirements

- Power BI Desktop with the *Power BI Project (.pbip)* feature enabled.
- Access credentials for the Teepee / SafePlace API. They are **not versioned**: they were replaced by placeholders (`<CLIENT_ID_A_RENSEIGNER>` / `<CLIENT_SECRET_A_RENSEIGNER>`, i.e. "to be filled in") and must be filled in locally before refreshing the data.
