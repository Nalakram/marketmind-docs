import abc
import polars as pl
from _typeshed import Incomplete
from srcPy.pipeline.core.pipeline_core_base import CleaningStep
from srcPy.pipeline.core.pipeline_core_metrics import AsyncMLflowLogger as AsyncMLflowLogger

logger: Incomplete

class BaseSentimentExtractor(CleaningStep, metaclass=abc.ABCMeta):
    mlflow_logger: Incomplete
    enabled: Incomplete
    text_col: Incomplete
    analyzer: Incomplete
    def __init__(self, mlflow_logger: AsyncMLflowLogger, enabled: bool, text_col: str = 'text', analyzer: str = 'vader') -> None: ...
    def apply(self, df: pl.DataFrame) -> pl.DataFrame: ...
    def __del__(self) -> None: ...

class SentimentExtractor(BaseSentimentExtractor):
    model: Incomplete
    def __init__(self, mlflow_logger: AsyncMLflowLogger, enabled: bool, text_col: str = 'text') -> None: ...

class AdvancedSentimentExtractor(BaseSentimentExtractor):
    model: Incomplete
    def __init__(self, mlflow_logger: AsyncMLflowLogger, enabled: bool, text_col: str = 'text', analyzer: str = 'finbert') -> None: ...
