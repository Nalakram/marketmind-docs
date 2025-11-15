import polars as pl
from _typeshed import Incomplete
from datetime import datetime
from srcPy.pipeline.core.pipeline_core_base import CleaningStep
from srcPy.pipeline.core.pipeline_core_metrics import AsyncMLflowLogger as AsyncMLflowLogger

logger: Incomplete

def fetch_fred_data(indicator: str, start: datetime, end: datetime) -> pl.Series: ...

class EconomicIndicatorNormalizerStep(CleaningStep):
    mlflow_logger: Incomplete
    enabled: Incomplete
    indicators: Incomplete
    timestamp_col: Incomplete
    def __init__(self, mlflow_logger: AsyncMLflowLogger, enabled: bool, indicators: list[str], timestamp_col: str = 'timestamp') -> None: ...
    def apply(self, df: pl.DataFrame) -> pl.DataFrame: ...
    def __del__(self) -> None: ...
