import polars as pl
from typing import Any as Incomplete
from datetime import datetime
from srcPy.ops.mm_logkit import get_logger as get_logger
from srcPy.pipeline.core.pipeline_core_base import CleaningStep as CleaningStep
from srcPy.pipeline.core.pipeline_core_metrics import AsyncMLflowLogger as AsyncMLflowLogger
from srcPy.utils.exceptions import DataFetchError as DataFetchError
from srcPy.utils.validators import validate_series as validate_series

logger: Incomplete

def fetch_fred_data(indicator: str, start: datetime, end: datetime) -> pl.Series: ...

class EconomicIndicatorNormalizerStep(CleaningStep):
    """economic indicator normalizer step class."""
    mlflow_logger: Incomplete
    enabled: Incomplete
    indicators: Incomplete
    timestamp_col: Incomplete
    def __init__(self, mlflow_logger: AsyncMLflowLogger, enabled: bool, indicators: list[str], timestamp_col: str = 'timestamp') -> None: ...
    def apply(self, df: pl.DataFrame) -> pl.DataFrame: ...
    def __del__(self) -> None: ...