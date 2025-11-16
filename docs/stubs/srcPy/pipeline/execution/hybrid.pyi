from typing import Any as Incomplete
from srcPy.ops.mm_logkit import get_logger as get_logger
from srcPy.pipeline.core.pipeline_core_base import StepRegistry as StepRegistry
from srcPy.pipeline.core.pipeline_core_context import PipelineContext as PipelineContext
from srcPy.pipeline.execution.batch import BatchPipeline as BatchPipeline
from srcPy.pipeline.execution.streaming import StreamingCleanerPipeline as StreamingCleanerPipeline
from srcPy.pipeline.stages.cleaning.core.base import CleaningStep as CleaningStep
from srcPy.pipeline.stages.cleaning.core.metrics import AsyncMLflowLogger as AsyncMLflowLogger
from srcPy.utils.exceptions import DataValidationError as DataValidationError
from srcPy.utils.optional_imports import pd as pd, pl as pl
from srcPy.utils.validators import validate_dataframe as validate_dataframe
from typing import AsyncGenerator

logger: Incomplete

class HybridCleanerPipeline(BatchPipeline):
    """hybrid cleaner pipeline class."""
    config: dict
    streaming: Incomplete
    mlflow_logger: Incomplete
    streaming_pipeline: Incomplete
    def __init__(self, steps: list[CleaningStep], streaming: bool = False, buffer_size: int = 100, window: int = 252, mlflow_logger: AsyncMLflowLogger | None = None) -> None: ...
    def run_batch(self, df: pl.DataFrame, distributed: bool = False) -> pl.DataFrame: ...
    async def run_stream(self, stream_gen: AsyncGenerator[pl.DataFrame, None]) -> AsyncGenerator[pl.DataFrame, None]: ...
    async def run(self, df: pl.DataFrame | None = None, stream_gen: AsyncGenerator[pl.DataFrame, None] | None = None, distributed: bool = False) -> pl.DataFrame | AsyncGenerator[pl.DataFrame, None]: ...