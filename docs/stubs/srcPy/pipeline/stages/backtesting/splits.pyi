import pandas as pd
from typing import Any as Incomplete
from srcPy.pipeline.stages.cleaning.core.base import CleaningStep as CleaningStep

class BacktestingSplitNormalizerStep(CleaningStep):
    """backtesting split normalizer step class."""
    is_fast: bool
    enabled: Incomplete
    split_ratio: Incomplete
    def __init__(self, cfg) -> None: ...
    def apply(self, df: pd.DataFrame) -> pd.DataFrame: ...