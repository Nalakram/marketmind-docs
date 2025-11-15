import polars as pl
from _typeshed import Incomplete
from srcPy.pipeline.core.pipeline_core_metrics import AsyncMLflowLogger
from srcPy.pipeline.stages.cleaning.core.base import CleaningStep as CleaningStep

logger: Incomplete

class CleanerPipeline:
    steps: Incomplete
    mlflow_logger: Incomplete
    config: Incomplete
    def __init__(self, steps: list[CleaningStep], mlflow_logger: AsyncMLflowLogger = None) -> None: ...
    def run(self, df: pl.DataFrame, distributed: bool = False) -> pl.DataFrame: ...
    def close(self) -> None: ...
