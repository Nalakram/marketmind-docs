import pandas as pd
import types
from typing import Any as Incomplete
from dataclasses import dataclass
from srcPy.data.data_cleaning import DataCleaner as DataCleaner
from srcPy.data.data_loader import build_loader as build_loader
from srcPy.ops.caching import versioned_key as versioned_key
from srcPy.ops.multi_tier_cache import MultiTierClient as MultiTierClient, version_to_int as version_to_int
from srcPy.ops.observability import LoggingManager as LoggingManager, MetricConfig as MetricConfig, MetricsManager as MetricsManager, TracingConfig as TracingConfig, TracingManager as TracingManager, set_strategy as set_strategy, set_tenant as set_tenant
from srcPy.strategies.pipeline_strategy import BacktestConfig as BacktestConfig, PipelineStrategy as PipelineStrategy, StrategyContext as StrategyContext, StrategyRegistry as StrategyRegistry, backtest_portfolio as backtest_portfolio
from srcPy.utils.exceptions import DataValidationError as DataValidationError, InvalidInputError as InvalidInputError, StatisticalTestError as StatisticalTestError
from srcPy.utils.validators import validate_data_for_training as validate_data_for_training
from typing import Any, Iterable, Mapping, Protocol, TypeAlias

SERVICE_NAME: Incomplete
TENANT_ID: Incomplete
metrics: Incomplete
tracing: Incomplete
logger: Incomplete

class ObsTimer:
    """obs timer class."""
    name: Incomplete
    labels: Incomplete
    t0: float
    def __init__(self, name: str, labels: dict[str, str] | None = None) -> None: ...
    def __enter__(self): ...
    def __exit__(self, exc_type: type[BaseException] | None, exc: BaseException | None, tb: types.TracebackType | None): ...

CACHE_TTL: Incomplete
L2_TYPE: Incomplete
CACHE: Incomplete

@dataclass(frozen=True)
class RunSpec:
    """run spec class."""
    strategy_key: str
    params: Mapping[str, Any]
    regime: str
    start: str
    end: str
    seed: int
    leverage_cap: float
    turn_cost: float
    initial_nav: float

@dataclass(frozen=True)
class RunResult:
    """run result class."""
    ok: bool
    regime: str
    seed: int
    metrics_out: Mapping[str, Any] | None

DataSplit: TypeAlias

class SupportsClean(Protocol):
    """supports clean class."""
    def clean(self, df: pd.DataFrame) -> pd.DataFrame: ...

def load_data(start_date: str, end_date: str, cleaner: SupportsClean | None = None) -> DataSplit: ...
def run_backtests(strategy_key: str, params: Mapping[str, Any], regimes: Mapping[str, tuple[str, str]], *, leverage_cap: float = 1.0, commission: float = 0.0, slippage_perc: float = 0.0005, initial_nav: float = 1.0, num_seeds: int = 8, max_workers: int | None = None, cleaner: DataCleaner | None = None, timeout_s: float | None = None) -> dict[str, list[Mapping[str, Any] | None]]: ...
def statistical_tests(results: Mapping[str, list[Mapping[str, Any] | None]]) -> Mapping[str, Mapping[str, float]]: ...
def load_regimes(config_file: str | None = None, cli_args: Iterable[str] | None = None) -> Mapping[str, tuple[str, str]]: ...
def main(strategy: str = 'momentum', params: Mapping[str, Any] | None = None, regimes: Mapping[str, tuple[str, str]] | None = None, *, leverage_cap: float = 1.0, commission: float = 0.0, slippage_perc: float = 0.0005, initial_nav: float = 1.0, num_seeds: int = 8, max_workers: int | None = None, cleaner: DataCleaner | None = None, timeout_s: float | None = None) -> tuple[dict[str, list[Mapping[str, Any] | None]], Mapping[str, Mapping[str, float]]]: ...