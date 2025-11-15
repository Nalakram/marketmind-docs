import pandas as pd
import types
from _typeshed import Incomplete
from dataclasses import dataclass
from srcPy.data.data_cleaning import DataCleaner as DataCleaner
from srcPy.strategies.pipeline_strategy import PipelineStrategy as PipelineStrategy
from typing import Any, Iterable, Mapping, Protocol, TypeAlias

SERVICE_NAME: Incomplete
TENANT_ID: Incomplete
metrics: Incomplete
tracing: Incomplete
logger: Incomplete

class ObsTimer:
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
    ok: bool
    regime: str
    seed: int
    metrics_out: Mapping[str, Any] | None

DataSplit: TypeAlias

class SupportsClean(Protocol):
    def clean(self, df: pd.DataFrame) -> pd.DataFrame: ...

def load_data(start_date: str, end_date: str, cleaner: SupportsClean | None = None) -> DataSplit: ...
def run_backtests(strategy_key: str, params: Mapping[str, Any], regimes: Mapping[str, tuple[str, str]], *, leverage_cap: float = 1.0, commission: float = 0.0, slippage_perc: float = 0.0005, initial_nav: float = 1.0, num_seeds: int = 8, max_workers: int | None = None, cleaner: DataCleaner | None = None, timeout_s: float | None = None) -> dict[str, list[Mapping[str, Any] | None]]: ...
def statistical_tests(results: Mapping[str, list[Mapping[str, Any] | None]]) -> Mapping[str, Mapping[str, float]]: ...
def load_regimes(config_file: str | None = None, cli_args: Iterable[str] | None = None) -> Mapping[str, tuple[str, str]]: ...
def main(strategy: str = 'momentum', params: Mapping[str, Any] | None = None, regimes: Mapping[str, tuple[str, str]] | None = None, *, leverage_cap: float = 1.0, commission: float = 0.0, slippage_perc: float = 0.0005, initial_nav: float = 1.0, num_seeds: int = 8, max_workers: int | None = None, cleaner: DataCleaner | None = None, timeout_s: float | None = None) -> tuple[dict[str, list[Mapping[str, Any] | None]], Mapping[str, Mapping[str, float]]]: ...
