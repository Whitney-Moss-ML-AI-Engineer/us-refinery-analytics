import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

def refinery_clusters(df: pd.DataFrame, features=None, n_clusters=4):
    features = features or ["crude_capacity_bpd", "nci"]
    work = df[features].apply(pd.to_numeric, errors="coerce").dropna()
    X = StandardScaler().fit_transform(work)
    model = KMeans(n_clusters=n_clusters, random_state=42, n_init="auto")
    labels = model.fit_predict(X)
    result = work.copy()
    result["cluster"] = labels
    return model, result
