import polars as pl
from _typeshed import Incomplete
from srcPy.ops.mm_logkit import get_logger as get_logger
from srcPy.pipeline.core.pipeline_core_base import CleaningStep as CleaningStep
from srcPy.pipeline.core.pipeline_core_metrics import AsyncMLflowLogger as AsyncMLflowLogger

logger: Incomplete

class AlternativeDataNormalizerStep(CleaningStep):
    mlflow_logger: Incomplete
    enabled: Incomplete
    esg_enabled: Incomplete
    supply_chain_enabled: Incomplete
    custom_sources: Incomplete
    executor: Incomplete
    def __init__(self, mlflow_logger: AsyncMLflowLogger, enabled: bool, esg_enabled: bool = False, supply_chain_enabled: bool = False, custom_sources: dict[str, callable] | None = None) -> None: ...
    def apply(self, df: pl.DataFrame) -> pl.DataFrame: ...
    def __del__(self) -> None: ...
