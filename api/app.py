from fastapi import FastAPI
import pandas as pd

app = FastAPI(title="U.S. Refinery Analytics API")
DATA = "data/processed/refineries.parquet"

@app.get("/api/refineries")
def refineries():
    df = pd.read_parquet(DATA)
    return df.to_dict(orient="records")
