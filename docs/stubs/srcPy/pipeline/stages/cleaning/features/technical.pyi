import abc
import polars as pl
from _typeshed import Incomplete
from srcPy.pipeline.core.pipeline_core_base import CleaningStep
from srcPy.pipeline.core.pipeline_core_metrics import AsyncMLflowLogger as AsyncMLflowLogger

logger: Incomplete

class BaseTechnicalIndicatorStep(CleaningStep, metaclass=abc.ABCMeta):
    mlflow_logger: Incomplete
    enabled: Incomplete
    window: Incomplete
    fillna_method: Incomplete
    indicator_name: Incomplete
    def __init__(self, mlflow_logger: AsyncMLflowLogger, enabled: bool, window: int, fillna_method: str = 'ffill', indicator_name: str = 'indicator') -> None: ...
    def apply(self, df: pl.DataFrame) -> pl.DataFrame: ...
    def __del__(self) -> None: ...

class RSINormalizerStep(BaseTechnicalIndicatorStep):
    def __init__(self, mlflow_logger: AsyncMLflowLogger, enabled: bool, window: int, fillna_method: str = 'ffill') -> None: ...

class MACDNormalizerStep(BaseTechnicalIndicatorStep):
    fast: Incomplete
    slow: Incomplete
    signal: Incomplete
    def __init__(self, mlflow_logger: AsyncMLflowLogger, enabled: bool, fast: int = 12, slow: int = 26, signal: int = 9, fillna_method: str = 'ffill') -> None: ...
    def apply(self, df: pl.DataFrame) -> pl.DataFrame: ...

class ATRNormalizerStep(BaseTechnicalIndicatorStep):
    def __init__(self, mlflow_logger: AsyncMLflowLogger, enabled: bool, window: int, fillna_method: str = 'ffill') -> None: ...

class VWAPNormalizerStep(BaseTechnicalIndicatorStep):
    def __init__(self, mlflow_logger: AsyncMLflowLogger, enabled: bool, window: int, fillna_method: str = 'ffill') -> None: ...

class IncrementalRSI:
    window: Incomplete
    gains: Incomplete
    losses: Incomplete
    prev_price: float | None
    def __init__(self, window: int) -> None: ...
    def update(self, price: float) -> float: ...

class IncrementalRSIStep(CleaningStep):
    mlflow_logger: Incomplete
    rsi: Incomplete
    def __init__(self, mlflow_logger: AsyncMLflowLogger, window: int) -> None: ...
    def apply(self, df: pl.DataFrame) -> pl.DataFrame: ...
    def __del__(self) -> None: ...

class IncrementalMACD:
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
    mlflow_logger: Incomplete
    macd: Incomplete
    def __init__(self, mlflow_logger: AsyncMLflowLogger, fast: int = 12, slow: int = 26, signal: int = 9) -> None: ...
    def apply(self, df: pl.DataFrame) -> pl.DataFrame: ...
    def __del__(self) -> None: ...
