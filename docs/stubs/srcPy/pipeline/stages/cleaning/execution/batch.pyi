import polars as pl
from typing import Any as Incomplete
from srcPy.ops.mm_logkit import get_logger as get_logger
from srcPy.pipeline.core.pipeline_core_metrics import AsyncMLflowLogger as AsyncMLflowLogger
from srcPy.pipeline.stages.cleaning.core.base import CleaningStep as CleaningStep
from srcPy.utils.config import get_config as get_config
from srcPy.utils.exceptions import DataValidationError as DataValidationError
from srcPy.utils.validators import validate_dataframe as validate_dataframe

logger: Incomplete

class CleanerPipeline:
    """cleaner pipeline class."""
    steps: Incomplete
    mlflow_logger: Incomplete
    config: Incomplete
    def __init__(self, steps: list[CleaningStep], mlflow_logger: AsyncMLflowLogger = None) -> None: ...
    def run(self, df: pl.DataFrame, distributed: bool = False) -> pl.DataFrame: ...
    def close(self) -> None: ...