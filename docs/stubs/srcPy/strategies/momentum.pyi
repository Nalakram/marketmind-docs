import pandas as pd
from .pipeline_strategy import FeaturePlan, PipelineStrategy
from _typeshed import Incomplete
from typing import Any

__all__ = ['MomentumStrategy']

class MomentumStrategy(PipelineStrategy):
    short: Incomplete
    long: Incomplete
    rsi_window: Incomplete
    rsi_hi: Incomplete
    rsi_lo: Incomplete
    adx_window: Incomplete
    adx_min: Incomplete
    clip: Incomplete
    def __init__(self, short: int = 20, long: int = 200, rsi_window: int = 14, rsi_hi: float = 70.0, rsi_lo: float = 30.0, adx_window: int = 14, adx_min: float = 15.0, clip: float = 1.0, **kwargs: Any) -> None: ...
    def features_plan(self) -> FeaturePlan: ...
    def generate_signal(self, features: pd.DataFrame) -> pd.Series: ...
