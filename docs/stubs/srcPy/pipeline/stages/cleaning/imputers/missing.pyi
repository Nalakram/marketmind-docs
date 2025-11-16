import abc
from typing import Any as Incomplete
from srcPy.ops.mm_logkit import get_logger as get_logger
from srcPy.pipeline.core.pipeline_core_base import CleaningStep as CleaningStep
from srcPy.pipeline.core.pipeline_core_metrics import AsyncMLflowLogger as AsyncMLflowLogger
from srcPy.utils.exceptions import DataValidationError as DataValidationError

KalmanFilter: Incomplete
logger: Incomplete

class _NullLogger:
    """null logger class."""
    def log_metric(self, key, value) -> None: ...
    def close(self) -> None: ...

class BaseMissingImputer(CleaningStep, metaclass=abc.ABCMeta):
    """base missing imputer class."""
    mlflow_logger: Incomplete
    method: Incomplete
    params: Incomplete
    supported_methods: Incomplete
    def __init__(self, method: str = 'forward_fill', params: dict | None = None, mlflow_logger: AsyncMLflowLogger | None = None, **_) -> None: ...
    def apply(self, df): ...
    def __del__(self) -> None: ...

class MissingValueNormalizerStep(BaseMissingImputer): ...
class MissingImputer(MissingValueNormalizerStep): ...