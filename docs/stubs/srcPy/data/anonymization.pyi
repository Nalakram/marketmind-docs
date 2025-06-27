import pandas as pd
from _typeshed import Incomplete

logger: Incomplete

def k_anonymize(df: pd.DataFrame, quasi_identifiers: list[str], k: int = 5) -> pd.DataFrame: ...
