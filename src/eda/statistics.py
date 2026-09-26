import pandas as pd
from scipy import stats

def descriptive_summary(df: pd.DataFrame) -> pd.DataFrame:
    return df.describe(include="all").T

def iqr_outliers(df: pd.DataFrame, column: str) -> pd.DataFrame:
    x = pd.to_numeric(df[column], errors="coerce").dropna()
    q1, q3 = x.quantile([0.25, 0.75])
    iqr = q3 - q1
    mask = (df[column] < q1 - 1.5 * iqr) | (df[column] > q3 + 1.5 * iqr)
    return df.loc[mask]

def correlation_matrix(df: pd.DataFrame) -> pd.DataFrame:
    return df.select_dtypes("number").corr()

def compare_padds(df: pd.DataFrame, value: str, padd_a: str, padd_b: str):
    a = df.loc[df["padd"] == padd_a, value].dropna()
    b = df.loc[df["padd"] == padd_b, value].dropna()
    return stats.mannwhitneyu(a, b, alternative="two-sided")
