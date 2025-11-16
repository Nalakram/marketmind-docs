from typing import Any as Incomplete
from srcPy.ops.mm_logkit import get_logger as get_logger
from srcPy.pipeline.core.pipeline_core_base import PipelineConfigError as PipelineConfigError, PipelineStep as PipelineStep
from srcPy.pipeline.core.pipeline_core_context import PipelineContext as PipelineContext
from srcPy.utils.exceptions import DataValidationError as DataValidationError
from srcPy.utils.optional_imports import dd as dd, pd as pd, pl as pl
from srcPy.utils.validators import validate_dataframe as validate_dataframe

logger: Incomplete

class BatchPipeline:
    """batch pipeline class."""
    steps: Incomplete
    def __init__(self, steps: list[PipelineStep], *, default_cfg: dict | None = None) -> None: ...
    def run(self, data, *, ctx: PipelineContext | None = None, distributed: str | None = None, collect: bool = True): ...