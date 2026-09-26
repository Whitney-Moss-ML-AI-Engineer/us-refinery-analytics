# U.S. Refinery Analytics Platform

End-to-end petroleum refinery analytics platform combining EIA data engineering, PADD analysis, refinery complexity, exploratory data analysis, machine learning, deep learning, geospatial analytics, and an HTML/CSS/JavaScript dashboard.

## Objectives
- Build reproducible ETL pipelines for U.S. refinery data.
- Organize facilities by PADD, state, operator, capacity, status, and complexity.
- Preserve source lineage and data-quality metadata.
- Perform statistical EDA with pandas and SciPy.
- Apply ML for clustering, anomaly detection, forecasting, classification, and risk modeling.
- Apply deep learning to multivariate time series and refinery operational signals when sufficient historical data are available.
- Serve curated data through an API and interactive web dashboard.
- Export analytical datasets to CSV, Excel, Power BI, and Tableau.

## Architecture
```
Sources -> Raw -> Staging -> Curated -> Warehouse -> Analytics -> API -> Web Dashboard
                         |                    |
                         +-> EDA ------------+-> ML / Deep Learning
```

## Technology
Python, pandas, NumPy, SciPy, scikit-learn, PyTorch, SQL/PostgreSQL, FastAPI/Flask, HTML5, CSS3, JavaScript, Plotly, Matplotlib, GitHub Actions.

## Important methodology
Nelson Complexity Index (NCI) is retained as a sourced field. Do not fabricate missing NCI values. Complexity tiers must record their threshold methodology and source/version. PADD assignment is deterministic from state using the project configuration.

## Repository layout
- `src/extract`: source/API ingestion
- `src/transform`: cleaning, PADD mapping, enrichment
- `src/eda`: statistical analysis
- `src/ml`: classical ML
- `src/deep_learning`: PyTorch models
- `api`: REST service
- `dashboard`: HTML/CSS/JavaScript UI
- `warehouse`: dimensional model and SQL
- `notebooks`: reproducible research
- `tests`: data and model tests
- `exports`: BI-ready outputs

## Model families
### Classical ML
- K-Means / hierarchical clustering
- DBSCAN anomaly detection
- Random Forest / Gradient Boosting
- Logistic Regression
- PCA
- Isolation Forest
- time-series regression and forecasting

### Deep Learning
- MLP
- 1-D CNN
- LSTM
- GRU
- Transformer encoder
- Autoencoder for anomaly detection

Deep-learning models should only be trained where the target and historical observations support them. Avoid leakage by splitting data chronologically for forecasting.

## Sample workflow
```bash
pip install -r requirements.txt
python -m src.pipeline.run_etl
python -m src.eda.run_eda
python -m src.ml.train_models
python -m api.app
```

## Data sources
Primary sources should include the U.S. Energy Information Administration (EIA), EIA Energy Atlas/GIS, EPA datasets where appropriate, and first-party operator disclosures. See `docs/api/eia_api.md`.

## Disclaimer
This repository is an analytical and engineering project. It is not investment advice.
