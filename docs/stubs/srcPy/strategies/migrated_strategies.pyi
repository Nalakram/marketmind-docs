import pandas as pd
from _typeshed import Incomplete
from dataclasses import dataclass
from srcPy.strategies.pipeline_strategy import FeaturePlan, PipelineStrategy
from typing import Any, Final, Literal, Protocol

__all__ = ['RSIStrategy', 'MACDStrategy', 'BollingerBandsStrategy', 'MeanReversionStrategy', 'MovingAverageCrossoverStrategy', 'EnsemblePipelineStrategy', 'clear_strategy_cache']

class _SupportsToPandas(Protocol):
    def to_pandas(self) -> pd.DataFrame: ...

def clear_strategy_cache() -> None: ...

class RSIStrategy(PipelineStrategy):
    rsi_window: Incomplete
    upper: Incomplete
    lower: Incomplete
    neutral_zone: Incomplete
    clip: Incomplete
    zero_on_any_nan: Incomplete
    def __init__(self, rsi_window: int = 14, upper: float = 70.0, lower: float = 30.0, neutral_zone: bool = True, clip: float = 1.0, zero_on_any_nan: bool = True, **kwargs: Any) -> None: ...
    def features_plan(self) -> FeaturePlan: ...
    def generate_signal(self, features: pd.DataFrame) -> pd.Series: ...

class MACDStrategy(PipelineStrategy):
    fast: Incomplete
    slow: Incomplete
    signal: Incomplete
    use_histogram: Incomplete
    clip: Incomplete
    def __init__(self, fast: int = 12, slow: int = 26, signal: int = 9, use_histogram: bool = True, clip: float = 1.0, **kwargs: Any) -> None: ...
    def features_plan(self) -> FeaturePlan: ...
    def generate_signal(self, features: pd.DataFrame) -> pd.Series: ...

class BollingerBandsStrategy(PipelineStrategy):
    period: Incomplete
    num_std: Incomplete
    mode: Literal['reversion', 'breakout']
    clip: Incomplete
    def __init__(self, period: int = 20, num_std: float = 2.0, mode: Literal['reversion', 'breakout'] = 'reversion', clip: float = 1.0, **kwargs: Any) -> None: ...
    def features_plan(self) -> FeaturePlan: ...
    def generate_signal(self, features: pd.DataFrame) -> pd.Series: ...

class MeanReversionStrategy(PipelineStrategy):
    period: Incomplete
    entry_threshold: Incomplete
    exit_threshold: Incomplete
    clip: Incomplete
    def __init__(self, period: int = 20, entry_threshold: float = 2.0, exit_threshold: float = 0.5, clip: float = 1.0, **kwargs: Any) -> None: ...
    def features_plan(self) -> FeaturePlan: ...
    def generate_signal(self, features: pd.DataFrame) -> pd.Series: ...

class MovingAverageCrossoverStrategy(PipelineStrategy):
    short: Incomplete
    long: Incomplete
    ma_type: Literal['sma', 'ema']
    use_momentum: Incomplete
    clip: Incomplete
    price_col: Incomplete
    def __init__(self, short: int = 50, long: int = 200, ma_type: Literal['sma', 'ema'] = 'sma', use_momentum: bool = False, clip: float = 1.0, price_col: str | None = None, **kwargs: Any) -> None: ...
    def features_plan(self) -> FeaturePlan: ...
    def generate_signal(self, features: pd.DataFrame) -> pd.Series: ...

@dataclass
class _SubStrategyState:
    strategy: PipelineStrategy
    params: dict[str, Any]
    failure_count: int = ...
    last_signal: pd.Series | None = ...
    open: bool = ...

class EnsemblePipelineStrategy(PipelineStrategy):
    ADAPTIVE_UPDATE_INTERVAL: Final[int]
    MAX_FAILURES: Final[int]
    MIN_WEIGHT_FLOOR: Final[float]
    strategy_specs: Incomplete
    combination_method: Incomplete
    adaptive_weights: Incomplete
    performance_window: Incomplete
    weights: Incomplete
    def __init__(self, strategy_specs: list[tuple[str, dict]], weights: list[float] | None = None, combination_method: Literal['weighted', 'majority'] = 'weighted', adaptive_weights: bool = False, performance_window: int = 50, **kwargs: Any) -> None: ...
    def features_plan(self) -> FeaturePlan: ...
    def generate_signal(self, features: pd.DataFrame) -> pd.Series: ...
