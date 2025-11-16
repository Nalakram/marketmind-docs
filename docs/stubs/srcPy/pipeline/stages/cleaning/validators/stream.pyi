import polars as pl
from .contracts import MarketDataFrameSchema as MarketDataFrameSchema
from _typeshed import Incomplete
from srcPy.ops.mm_logkit import get_logger as get_logger
from srcPy.pipeline.core.pipeline_core_metrics import AsyncMLflowLogger as AsyncMLflowLogger
from srcPy.pipeline.stages.cleaning.core.base import CleaningStep as CleaningStep
from srcPy.utils.exceptions import DataValidationError as DataValidationError
from srcPy.utils.validators import validate_stream_chunk as validate_stream_chunk

logger: Incomplete

class StreamValidationStep(CleaningStep):
    mlflow_logger: Incomplete
    schema: Incomplete
    strict: Incomplete
    sampling_rate: Incomplete
    def __init__(self, mlflow_logger: AsyncMLflowLogger, schema: MarketDataFrameSchema | None = None, strict: bool = True, sampling_rate: float = 1.0) -> None: ...
    def apply(self, df: pl.DataFrame) -> pl.DataFrame: ...
    def __del__(self) -> None: ...
