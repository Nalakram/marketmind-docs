import dataclasses
import pandas as pd
import polars as pl
from typing import Any as Incomplete
from dataclasses import dataclass, field
from pathlib import Path
from srcPy.ops.mm_logkit import get_logger as get_logger
from typing import Any, Callable, Mapping, Protocol, Sequence

LOG: Incomplete

class PipelineError(Exception): ...
class ValidationError(PipelineError): ...
class MaterializationError(PipelineError): ...

@dataclass
class TradeIntent:
    """trade intent class."""
    weights: pd.Series | pd.DataFrame
    raw: Mapping[str, Any] = field(default_factory=dict)
    diagnostics: Mapping[str, Any] = field(default_factory=dict)

@dataclass
class StrategyContext:
    """strategy context class."""
    prices: pd.Series | pd.DataFrame
    features: pd.DataFrame | pl.DataFrame | None = ...
    timestamps: pd.Index | None = ...
    asset_names: list[str] | None = ...
    backend: str = ...
    cache_dir: str | Path = ...
    random_state: int = ...
    def validate(self) -> StrategyContext: ...

class RegimeDetector(Protocol):
    """regime detector class."""
    def gate(self, features: pd.DataFrame | pl.DataFrame) -> pd.Series | pl.Series | float | int: ...

class RiskManager(Protocol):
    """Manages risk resources and operations."""
    def clamp(self, weights: pd.Series | pd.DataFrame, prices: pd.Series | pd.DataFrame, **kwargs: Any) -> pd.Series | pd.DataFrame: ...

class PositionSizer(Protocol):
    """position sizer class."""
    def size(self, signal: pd.Series | pd.DataFrame, **kwargs: Any) -> pd.Series | pd.DataFrame: ...

@dataclass(frozen=True)
class FeatureStep:
    """feature step class."""
    op: str
    inputs: tuple[str, ...]
    args: tuple[Any, ...] = ...
    kwargs: Mapping[str, Any] = dataclasses.field(default_factory=dict)
    out: str = ...

@dataclass
class FeaturePlan:
    """feature plan class."""
    steps: list[FeatureStep]
    def signature(self) -> str: ...

def feature_op(name: str) -> Callable[[Callable[..., Any]], Callable[..., Any]]: ...
def op_pct_change(df: pd.DataFrame | pl.DataFrame, col: str, periods: int = 1, out: str | None = None): ...
def op_roll_mean(df: pd.DataFrame | pl.DataFrame, col: str, window: int, minp: int | None = None, out: str | None = None): ...
def op_roll_std(df: pd.DataFrame | pl.DataFrame, col: str, window: int, minp: int | None = None, out: str | None = None): ...
def op_ema(df: pd.DataFrame | pl.DataFrame, col: str, span: int, adjust: bool = False, out: str | None = None): ...
def op_zscore(df: pd.DataFrame | pl.DataFrame, col: str, window: int, minp: int | None = None, out: str | None = None): ...

class _Cache:
    """cache class."""
    root: Incomplete
    def __init__(self, cache_dir: str | Path) -> None: ...
    def get(self, key: str) -> Any | None: ...
    def set(self, key: str, value: Any) -> None: ...

def materialize_features(ctx: StrategyContext, plan: FeaturePlan, price_col: str | None = None) -> pd.DataFrame | pl.DataFrame: ...

@dataclass
class StrategySpec:
    """strategy spec class."""
    name: str
    params: Mapping[str, Any] = field(default_factory=dict)

class StrategyRegistry:
    """strategy registry class."""
    @classmethod
    def register(cls, name: str, strat_cls: type[PipelineStrategy]) -> None: ...
    @classmethod
    def get(cls, name: str) -> type[PipelineStrategy]: ...
    @classmethod
    def clear_for_test(cls) -> None: ...

class PipelineStrategy:
    """Strategy for pipeline behavior."""
    regime: RegimeDetector | None
    risk: RiskManager | None
    sizer: PositionSizer | None
    params: Incomplete
    random_state: Incomplete
    def __init__(self, **params: Any) -> None: ...
    def features_plan(self) -> FeaturePlan: ...
    def generate_signal(self, features: pd.DataFrame | pl.DataFrame) -> pd.Series | pd.DataFrame: ...
    def generate_trade_intent(self, ctx: StrategyContext) -> TradeIntent: ...

@dataclass
class BacktestConfig:
    """Configuration for backtest."""
    cost_per_unit_turnover: float = ...
    leverage_cap: float = ...
    initial_nav: float = ...

def backtest_portfolio(prices: pd.DataFrame, weights: pd.DataFrame, cfg: BacktestConfig) -> pd.DataFrame: ...

@dataclass
class SweepResult:
    """sweep result class."""
    params: Mapping[str, Any]
    score: float
    details: Mapping[str, Any] = field(default_factory=dict)

def parameter_sweep(strategy_cls: type['PipelineStrategy'], param_grid: Mapping[str, Sequence[Any]], ctx: StrategyContext, *, prices: pd.DataFrame | None = None, backtest_cfg: BacktestConfig | None = None, n_jobs: int = 1) -> list['SweepResult']: ...
def optuna_tune(strategy_cls: type['PipelineStrategy'], sampler_spec: Mapping[str, tuple[float, float]], ctx: StrategyContext, *, prices: pd.DataFrame | None = None, backtest_cfg: BacktestConfig | None = None, n_trials: int = 50) -> list['SweepResult']: ...

@dataclass
class DriftState:
    """drift state class."""
    ref_mean: float
    ref_std: float

def detect_drift(series: pd.Series, st: DriftState | None, threshold: float = 3.0, sensitivity: float = 1.0) -> tuple[DriftState, bool]: ...

@dataclass
class ChampionChallenger:
    """champion challenger class."""
    strategy_cls: type[PipelineStrategy]
    ctx: StrategyContext
    prices: pd.DataFrame
    backtest_cfg: BacktestConfig = field(default_factory=BacktestConfig)
    champion_params: dict[str, Any] = field(default_factory=dict)
    history: list[tuple[str, dict[str, Any], float]] = field(default_factory=list)
    def evaluate(self, params: Mapping[str, Any]) -> float: ...
    def step(self, challenger_params: Mapping[str, Any], improvement: float = 0.01) -> dict[str, Any]: ...

class NullRegime:
    """null regime class."""
    def gate(self, features: pd.DataFrame | pl.DataFrame) -> int: ...

class LinearSizer:
    """linear sizer class."""
    scale: Incomplete
    clip: Incomplete
    def __init__(self, scale: float = 1.0, clip: float = 1.0) -> None: ...
    def size(self, signal: pd.Series | pd.DataFrame, **_: Any) -> pd.Series | pd.DataFrame: ...

class TurnoverLimiterRisk:
    """turnover limiter risk class."""
    max_turnover: Incomplete
    def __init__(self, max_turnover: float = 0.5) -> None: ...
    def clamp(self, weights: pd.Series | pd.DataFrame, prices: pd.Series | pd.DataFrame, **_: Any) -> pd.Series | pd.DataFrame: ...

@dataclass
class BlendSpec:
    """blend spec class."""
    parts: list[tuple[float, PipelineStrategy]]
    def normalize(self) -> None: ...

def blend(ctx: StrategyContext, spec: BlendSpec) -> TradeIntent: ...

class LegacyBaseStrategy(PipelineStrategy):
    """Strategy for legacy base behavior."""
    legacy: Incomplete
    def __init__(self, legacy_impl: Any, **params: Any) -> None: ...
    def features_plan(self) -> FeaturePlan: ...
    def generate_signal(self, features: pd.DataFrame | pl.DataFrame) -> pd.Series | pd.DataFrame: ...