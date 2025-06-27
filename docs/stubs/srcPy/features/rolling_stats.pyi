import pandas as pd
from _typeshed import Incomplete

logger: Incomplete

def add_rolling_stats(df: pd.DataFrame, columns: list[str], window_sizes: list[int], stats: list[str]) -> pd.DataFrame: ...
