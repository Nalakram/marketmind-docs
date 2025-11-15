import abc
import polars as pl
from .batch import AnomalyNormalizerStep as AnomalyNormalizerStep
from .streaming import StreamingAnomalyNormalizerStep as StreamingAnomalyNormalizerStep
from _typeshed import Incomplete
from srcPy.pipeline.core.pipeline_core_base import CleaningStep
from srcPy.pipeline.core.pipeline_core_metrics import AsyncMLflowLogger

__all__ = ['AnomalyNormalizerStep', 'StreamingAnomalyNormalizerStep']

class BaseAnomalyNormalizerStep(CleaningStep, metaclass=abc.ABCMeta):
    mlflow_logger: Incomplete
    enabled: Incomplete
    params: Incomplete
    def __init__(self, mlflow_logger: AsyncMLflowLogger, enabled: bool, params: dict) -> None: ...
    def apply(self, df: pl.DataFrame) -> pl.DataFrame: ...
    def freeze(self) -> dict: ...
    def thaw(self, state: dict): ...
