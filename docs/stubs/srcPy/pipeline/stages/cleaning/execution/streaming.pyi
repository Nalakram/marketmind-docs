import polars as pl
from _typeshed import Incomplete
from srcPy.pipeline.stages.cleaning.core.base import CleaningStep as CleaningStep
from typing import AsyncGenerator

logger: Incomplete

class StreamingCleanerPipeline:
    steps: Incomplete
    mlflow_logger: Incomplete
    buffer: Incomplete
    buffer_size: Incomplete
    window: Incomplete
    config: Incomplete
    def __init__(self, steps: list[CleaningStep], buffer_size: int = 100, window: int = 252) -> None: ...
    def adjust_buffer_size(self, latency: float): ...
    async def process_stream(self, stream_gen: AsyncGenerator[pl.DataFrame, None]) -> AsyncGenerator[pl.DataFrame, None]: ...
    def close(self) -> None: ...
