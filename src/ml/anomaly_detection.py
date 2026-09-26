import pandas as pd
from sklearn.ensemble import IsolationForest

def detect_anomalies(df: pd.DataFrame, features=None):
    features = features or ["crude_capacity_bpd", "nci"]
    work = df[features].apply(pd.to_numeric, errors="coerce").dropna()
    model = IsolationForest(contamination="auto", random_state=42)
    labels = model.fit_predict(work)
    result = work.copy()
    result["anomaly"] = labels == -1
    result["anomaly_score"] = model.decision_function(work)
    return model, result
