import pandas as pd
from _typeshed import Incomplete

logger: Incomplete

def detect_drift(ref_data: pd.DataFrame, new_data: pd.DataFrame, columns: list[str], threshold: float = 0.05) -> dict: ...
