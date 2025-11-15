import polars as pl
from .contracts import MarketDataFrameSchema as MarketDataFrameSchema
from _typeshed import Incomplete
from srcPy.pipeline.core.pipeline_core_metrics import AsyncMLflowLogger as AsyncMLflowLogger
from srcPy.pipeline.stages.cleaning.core.base import CleaningStep

logger: Incomplete

class ValidationStep(CleaningStep):
    mlflow_logger: Incomplete
    required_columns: Incomplete
    ohlcv_mode: Incomplete
    schema: Incomplete
    strict: Incomplete
    def __init__(self, mlflow_logger: AsyncMLflowLogger, required_columns: list[str] | None = None, ohlcv_mode: bool = False, schema: MarketDataFrameSchema | None = None, strict: bool = True) -> None: ...
    def apply(self, df: pl.DataFrame) -> pl.DataFrame: ...
    def __del__(self) -> None: ...
