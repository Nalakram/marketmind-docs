import pandas as pd
from _typeshed import Incomplete
from collections import deque
from dataclasses import dataclass, dataclass as _dataclass, field
from pathlib import Path
from srcPy.strategies.pipeline_strategy import BacktestConfig, ChampionChallenger, PipelineStrategy, StrategyContext, TradeIntent
from typing import Any, Protocol

@_dataclass
class DriftState:
    ref_mean: float = ...
    ref_std: float = ...

LOG: Incomplete

@dataclass
class EvolutionEvent:
    timestamp: pd.Timestamp
    event_type: str
    strategy_name: str
    old_params: dict[str, Any]
    new_params: dict[str, Any]
    performance_delta: float
    metadata: dict[str, Any] = field(default_factory=dict)

class EvolutionCallback(Protocol):
    def on_evolution_event(self, event: EvolutionEvent) -> None: ...

class AdaptiveParameterSpace:
    base_space: Incomplete
    adaptation_rate: Incomplete
    memory_length: Incomplete
    performance_history: dict[str, deque]
    current_space: Incomplete
    def __init__(self, base_space: dict[str, tuple[float, float]], adaptation_rate: float = 0.1, memory_length: int = 100) -> None: ...
    def update(self, params: dict[str, Any], score: float) -> None: ...
    def evolve_space(self) -> dict[str, tuple[float, float]]: ...

@dataclass
class MultiFrameDriftState:
    short_term: DriftState | None = ...
    medium_term: DriftState | None = ...
    long_term: DriftState | None = ...

class MultiTimeframeDriftMonitor:
    short_window: Incomplete
    medium_window: Incomplete
    long_window: Incomplete
    sensitivity: Incomplete
    state: Incomplete
    def __init__(self, short_window: int = 20, medium_window: int = 60, long_window: int = 200, sensitivity: float = 2.5) -> None: ...
    def check_drift(self, returns: pd.Series) -> tuple[bool, dict[str, bool]]: ...

class StrategyEnsemble:
    strategy_specs: Incomplete
    rebalance_frequency: Incomplete
    blend_weights: dict[str, float]
    performance_history: dict[str, list[float]]
    steps_since_rebalance: int
    def __init__(self, strategies: list[tuple[str, dict[str, Any]]], rebalance_frequency: int = 50) -> None: ...
    def update_performance(self, strategy_name: str, score: float) -> None: ...
    def should_rebalance(self) -> bool: ...
    def rebalance_weights(self) -> dict[str, float]: ...

class SelfEvolvingAdapter:
    strategies: Incomplete
    ctx: Incomplete
    prices: Incomplete
    evolution_frequency: Incomplete
    optimization_trials: Incomplete
    min_history: Incomplete
    backtest_cfg: Incomplete
    callbacks: Incomplete
    step_count: int
    evolution_history: list[EvolutionEvent]
    strategy_instances: dict[str, PipelineStrategy]
    champion_challengers: dict[str, ChampionChallenger]
    adaptive_spaces: dict[str, AdaptiveParameterSpace]
    drift_monitors: dict[str, MultiTimeframeDriftMonitor]
    ensemble: Incomplete
    performance_buffer: dict[str, pd.Series]
    last_weights: pd.DataFrame | None
    def __init__(self, strategies: list[tuple[str, str, dict[str, tuple[float, float]]]], ctx: StrategyContext, prices: pd.DataFrame, evolution_frequency: int = 100, optimization_trials: int = 30, min_history_for_evolution: int = 50, backtest_cfg: BacktestConfig | None = None, callbacks: list[EvolutionCallback] | None = None) -> None: ...
    def generate_trade_intent(self) -> TradeIntent: ...
    def get_evolution_summary(self) -> dict[str, Any]: ...
    def force_evolution(self, strategy_name: str | None = None) -> None: ...

class LoggingEvolutionCallback:
    def on_evolution_event(self, event: EvolutionEvent) -> None: ...

class FileEvolutionCallback:
    filepath: Incomplete
    def __init__(self, filepath: str | Path) -> None: ...
    def on_evolution_event(self, event: EvolutionEvent) -> None: ...

def create_evolving_system(price_data: pd.DataFrame) -> SelfEvolvingAdapter: ...
