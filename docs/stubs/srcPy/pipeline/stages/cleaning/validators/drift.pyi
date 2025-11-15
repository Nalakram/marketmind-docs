import abc
import numpy as np
import polars as pl
from _typeshed import Incomplete
from abc import abstractmethod
from srcPy.pipeline.core.pipeline_core_metrics import AsyncMLflowLogger as AsyncMLflowLogger
from srcPy.pipeline.stages.cleaning.core.base import CleaningStep

logger: Incomplete

class BaseDriftTest(metaclass=abc.ABCMeta):
    @abstractmethod
    def compute(self, curr: np.ndarray, ref: np.ndarray) -> tuple[float, float]: ...

class KSTest(BaseDriftTest):
    def compute(self, curr: np.ndarray, ref: np.ndarray) -> tuple[float, float]: ...

class DriftDetectionStep(CleaningStep):
    mlflow_logger: Incomplete
    enabled: Incomplete
    reference_data: Incomplete
    threshold: Incomplete
    columns: Incomplete
    test: Incomplete
    strict: Incomplete
    def __init__(self, mlflow_logger: AsyncMLflowLogger, enabled: bool = True, reference_data: pl.DataFrame | None = None, threshold: float = 0.05, columns: list[str] | None = None, test: BaseDriftTest | None = None, strict: bool = True) -> None: ...
    def apply(self, df: pl.DataFrame) -> pl.DataFrame: ...
    def __del__(self) -> None: ...
