import abc
import pandas as pd
from _typeshed import Incomplete
from abc import ABC, abstractmethod
from collections.abc import Generator
from srcPy.utils.config import get_config as get_config
from srcPy.utils.exceptions import DataValidationError as DataValidationError
from srcPy.utils.logger import configure_logger as configure_logger, get_logger as get_logger

def get_runtime_config(): ...

logger: Incomplete
streaming_latency: Incomplete
buffer_length: Incomplete

class CleaningStep(ABC, metaclass=abc.ABCMeta):
    @abstractmethod
    def apply(self, df: pd.DataFrame) -> pd.DataFrame: ...

class MissingImputer:
    method: Incomplete
    params: Incomplete
    def __init__(self, method: str, params: dict) -> None: ...
    def apply(self, df: pd.DataFrame) -> pd.DataFrame: ...

class OutlierHandler(CleaningStep):
    method: Incomplete
    params: Incomplete
    def __init__(self, method, params) -> None: ...
    def apply(self, df): ...

class Denoiser(CleaningStep):
    method: Incomplete
    params: Incomplete
    def __init__(self, method, params) -> None: ...
    def apply(self, df): ...

class IncrementalRSI:
    window: Incomplete
    gains: Incomplete
    losses: Incomplete
    prev_price: Incomplete
    def __init__(self, window) -> None: ...
    def update(self, price): ...

class IncrementalRSIStep(CleaningStep):
    rsi: Incomplete
    def __init__(self, window) -> None: ...
    def apply(self, df): ...

class IncrementalMACD:
    fast: Incomplete
    slow: Incomplete
    signal: Incomplete
    ema_fast: Incomplete
    ema_slow: Incomplete
    macd: Incomplete
    macd_signal: Incomplete
    def __init__(self, fast, slow, signal) -> None: ...
    def update(self, price): ...

class IncrementalMACDStep(CleaningStep):
    macd: Incomplete
    def __init__(self, fast, slow, signal) -> None: ...
    def apply(self, df): ...

class SentimentExtractor(CleaningStep):
    enabled: Incomplete
    model: Incomplete
    def __init__(self, cfg) -> None: ...
    def apply(self, df): ...

class CalendarFeatures(CleaningStep):
    day: Incomplete
    holiday: Incomplete
    calendar: Incomplete
    def __init__(self, cfg) -> None: ...
    def apply(self, df): ...

class AnomalyDetector(CleaningStep):
    enabled: Incomplete
    contamination: Incomplete
    refit_interval: Incomplete
    method: Incomplete
    model: Incomplete
    counter: int
    def __init__(self, cfg) -> None: ...
    def apply(self, df): ...

class StreamingIsolationForest:
    contamination: Incomplete
    refit_every: Incomplete
    window_size: Incomplete
    buffer: Incomplete
    model: Incomplete
    counter: int
    def __init__(self, contamination, refit_every, window_size: int = 1000) -> None: ...
    def fit(self, data) -> None: ...
    def predict(self, df): ...

class StreamingAnomalyStep:
    contamination: Incomplete
    refit_every: Incomplete
    random_state: Incomplete
    model: Incomplete
    def __init__(self, contamination: float = 0.1, refit_every: int = 100, random_state: int = 42) -> None: ...
    def apply(self, df): ...

class CleanerPipeline:
    steps: Incomplete
    def __init__(self, steps) -> None: ...
    def run(self, df, distributed: bool = False): ...

class StreamingCleanerPipeline(CleanerPipeline):
    buffer: Incomplete
    buffer_size: Incomplete
    rsi: Incomplete
    macd: Incomplete
    def __init__(self, steps, buffer_size: int = 100, window: int = 252) -> None: ...
    async def process_stream(self, stream_gen) -> Generator[Incomplete]: ...

class ValidationStep(CleaningStep):
    required_columns: Incomplete
    def __init__(self, required_columns: Incomplete | None = None) -> None: ...
    def apply(self, df): ...

class RSICalculator(CleaningStep):
    enabled: Incomplete
    window: Incomplete
    fillna_method: Incomplete
    def __init__(self, cfg) -> None: ...
    def apply(self, df): ...

class DataCleaner:
    cfg: Incomplete
    pipeline: Incomplete
    def __init__(self, cfg: Incomplete | None = None, streaming: bool = False) -> None: ...
    def clean(self, df: pd.DataFrame) -> pd.DataFrame: ...
    def clean_chunk(self, df: pd.DataFrame) -> pd.DataFrame: ...
