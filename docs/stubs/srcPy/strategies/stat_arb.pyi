import pandas as pd
from .pipeline_strategy import FeaturePlan, PipelineStrategy
from _typeshed import Incomplete
from typing import Any

__all__ = ['StatArbPairs']

class StatArbPairs(PipelineStrategy):
    z_win: Incomplete
    max_pairs: Incomplete
    def __init__(self, z_win: int = 60, max_pairs: int | None = None, **kwargs: Any) -> None: ...
    def features_plan(self) -> FeaturePlan: ...
    def generate_signal(self, features: pd.DataFrame) -> pd.DataFrame: ...
