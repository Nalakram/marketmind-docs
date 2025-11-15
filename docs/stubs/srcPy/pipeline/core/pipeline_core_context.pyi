from _typeshed import Incomplete
from srcPy.utils.optional_imports import pd as pd, pl
from typing import Literal

TimeFreq: Incomplete

class PipelineContext:
    frequency: TimeFreq
    asset_class: str
    latency: Literal['ultra', 'low', 'batch']
    streaming: bool
    time_col: str
    df: pl.DataFrame | pl.LazyFrame | pd.DataFrame | None
    assume_sorted: bool
    sample: int
    backend: str | None
    executor: str | None
    optimize: bool
    cache: bool
    def as_lazy(self) -> pl.LazyFrame | None: ...
    def infer_frequency(self) -> TimeFreq: ...
    def refine(self, **kwargs) -> PipelineContext: ...
