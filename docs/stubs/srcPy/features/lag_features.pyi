import pandas as pd
from _typeshed import Incomplete

logger: Incomplete

def generate_lag_features(df: pd.DataFrame, columns: list[str], lags: list[int]) -> pd.DataFrame: ...
