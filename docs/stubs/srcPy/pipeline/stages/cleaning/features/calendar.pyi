import polars as pl
from _typeshed import Incomplete
from srcPy.pipeline.core.pipeline_core_base import CleaningStep
from srcPy.pipeline.core.pipeline_core_metrics import AsyncMLflowLogger as AsyncMLflowLogger

logger: Incomplete

class TimeZoneNormalizerStep(CleaningStep):
    mlflow_logger: Incomplete
    target_tz: Incomplete
    timestamp_col: Incomplete
    def __init__(self, mlflow_logger: AsyncMLflowLogger, target_tz: str = 'UTC', timestamp_col: str = 'timestamp') -> None: ...
    def apply(self, df: pl.DataFrame) -> pl.DataFrame: ...
    def __del__(self) -> None: ...

class GlobalCalendarNormalizerStep(CleaningStep):
    mlflow_logger: Incomplete
    countries: Incomplete
    day_of_week: Incomplete
    is_holiday: Incomplete
    timestamp_col: Incomplete
    def __init__(self, mlflow_logger: AsyncMLflowLogger, countries: list[str], day_of_week: bool = True, is_holiday: bool = True, timestamp_col: str = 'timestamp') -> None: ...
    def apply(self, df: pl.DataFrame) -> pl.DataFrame: ...
    def __del__(self) -> None: ...
