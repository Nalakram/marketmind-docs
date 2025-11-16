import abc
import polars as pl
from typing import Any as Incomplete
from srcPy.ops.mm_logkit import get_logger as get_logger
from srcPy.pipeline.core.pipeline_core_base import CleaningStep as CleaningStep
from srcPy.pipeline.core.pipeline_core_metrics import AsyncMLflowLogger as AsyncMLflowLogger
from srcPy.utils.exceptions import DataValidationError as DataValidationError
from srcPy.utils.validators import validate_dataframe as validate_dataframe

logger: Incomplete

class BaseTechnicalIndicatorStep(CleaningStep, metaclass=abc.ABCMeta):
    """base technical indicator step class."""
    mlflow_logger: Incomplete
    enabled: Incomplete
    window: Incomplete
    fillna_method: Incomplete
    indicator_name: Incomplete
    def __init__(self, mlflow_logger: AsyncMLflowLogger, enabled: bool, window: int, fillna_method: str = 'ffill', indicator_name: str = 'indicator') -> None: ...
    def apply(self, df: pl.DataFrame) -> pl.DataFrame: ...
    def __del__(self) -> None: ...

class RSINormalizerStep(BaseTechnicalIndicatorStep):
    """rsi normalizer step class."""
    def __init__(self, mlflow_logger: AsyncMLflowLogger, enabled: bool, window: int, fillna_method: str = 'ffill') -> None: ...

class MACDNormalizerStep(BaseTechnicalIndicatorStep):
    """macd normalizer step class."""
    fast: Incomplete
    slow: Incomplete
    signal: Incomplete
    def __init__(self, mlflow_logger: AsyncMLflowLogger, enabled: bool, fast: int = 12, slow: int = 26, signal: int = 9, fillna_method: str = 'ffill') -> None: ...
    def apply(self, df: pl.DataFrame) -> pl.DataFrame: ...

class ATRNormalizerStep(BaseTechnicalIndicatorStep):
    """atr normalizer step class."""
    def __init__(self, mlflow_logger: AsyncMLflowLogger, enabled: bool, window: int, fillna_method: str = 'ffill') -> None: ...

class VWAPNormalizerStep(BaseTechnicalIndicatorStep):
    """vwap normalizer step class."""
    def __init__(self, mlflow_logger: AsyncMLflowLogger, enabled: bool, window: int, fillna_method: str = 'ffill') -> None: ...

class IncrementalRSI:
    """incremental rsi class."""
    window: Incomplete
    gains: Incomplete
    losses: Incomplete
    prev_price: float | None
    def __init__(self, window: int) -> None: ...
    def update(self, price: float) -> float: ...

class IncrementalRSIStep(CleaningStep):
    """incremental rsi step class."""
    mlflow_logger: Incomplete
    rsi: Incomplete
    def __init__(self, mlflow_logger: AsyncMLflowLogger, window: int) -> None: ...
    def apply(self, df: pl.DataFrame) -> pl.DataFrame: ...
    def __del__(self) -> None: ...

class IncrementalMACD:
    """incremental macd class."""
    fast: Incomplete
    slow: Incomplete
    signal: Incomplete
    ema_fast: float | None
    ema_slow: float | None
    macd: float | None
    macd_signal: float | None
    def __init__(self, fast: int, slow: int, signal: int) -> None: ...
    def update(self, price: float) -> tuple[float, float]: ...

class IncrementalMACDStep(CleaningStep):
    """incremental macd step class."""
    mlflow_logger: Incomplete
    macd: Incomplete
    def __init__(self, mlflow_logger: AsyncMLflowLogger, fast: int = 12, slow: int = 26, signal: int = 9) -> None: ...
    def apply(self, df: pl.DataFrame) -> pl.DataFrame: ...
    def __del__(self) -> None: ...