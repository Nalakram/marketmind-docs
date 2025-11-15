import pandas as pd
from _typeshed import Incomplete
from srcPy.pipeline.stages.cleaning.core.base import CleaningStep

class BacktestingSplitNormalizerStep(CleaningStep):
    is_fast: bool
    enabled: Incomplete
    split_ratio: Incomplete
    def __init__(self, cfg) -> None: ...
    def apply(self, df: pd.DataFrame) -> pd.DataFrame: ...
