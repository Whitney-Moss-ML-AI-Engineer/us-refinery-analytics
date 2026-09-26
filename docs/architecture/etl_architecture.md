# ETL Architecture

## Extract
1. Pull EIA API datasets.
2. Download official EIA refinery capacity files when required.
3. Load EIA GIS refinery location data.
4. Add first-party operator enrichment.
5. Store immutable raw snapshots with extraction timestamp and source URL.

## Transform
- Normalize facility names and operators.
- Normalize state and coordinates.
- Derive PADD from state.
- Convert capacity to numeric barrels/day.
- Standardize operational status.
- Preserve NCI as source value.
- Add `nci_source`, `nci_date`, and `nci_method`.
- Create data-quality flags.
- Deduplicate facilities using stable facility identifiers where available.

## Load
Bronze/raw -> staging -> curated Parquet -> PostgreSQL warehouse.

## Orchestration
Development: Python CLI.
Production options: Prefect or Apache Airflow.
Scheduling should be configurable; EIA refresh frequency determines the appropriate cadence.

## Data quality gates
- Required identifier not null.
- State is a valid U.S. state/territory code where applicable.
- PADD mapping must resolve.
- Capacity >= 0.
- Latitude between -90 and 90.
- Longitude between -180 and 180.
- Duplicate facility checks.
- Source timestamp required.
