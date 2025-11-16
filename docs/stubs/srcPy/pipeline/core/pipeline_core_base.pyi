import abc
from typing import Any as Incomplete
from abc import ABC, abstractmethod
from enum import Enum
from srcPy.pipeline.core.pipeline_core_context import PipelineContext as PipelineContext
from srcPy.utils.optional_imports import pd as pd, pl as pl
from typing import Any, AsyncIterable, AsyncIterator, Generic, TypeVar

StepRegistry: Incomplete

class StepRegistry(dict):
    """step registry class."""
    def register(self, name, cls): ...
InT = TypeVar('InT')
OutT = TypeVar('OutT')
Engine: Incomplete

class PipelineError(Exception):
    """Exception raised when pipeline occurs."""
    code: str
    def to_dict(self) -> dict: ...

class PipelineGraphError(PipelineError):
    """Exception raised when pipeline graph occurs."""
    code: str

class PipelineConfigError(PipelineError):
    """Exception raised when pipeline config occurs."""
    code: str

class ErrorCode(Enum):
    """error code class."""
    MISSING_DATA = 'MISSING_DATA'
    INVALID_SCHEMA = 'INVALID_SCHEMA'
    OUTLIER_DETECTED = 'OUTLIER_DETECTED'
    DRIFT_DETECTED = 'DRIFT_DETECTED'
    PROCESSING_FAILURE = 'PROCESSING_FAILURE'
    RESOURCE_EXHAUSTED = 'RESOURCE_EXHAUSTED'

class DataError(Exception):
    """Exception raised when data occurs."""
    message: Incomplete
    code: Incomplete
    details: Incomplete
    def __init__(self, message: str, code: ErrorCode, details: dict[str, Any] | None = None) -> None: ...
    def to_dict(self) -> dict[str, Any]: ...

class MissingDataError(DataError): ...
class InvalidSchemaError(DataError): ...

class DataSource(ABC, metaclass=abc.ABCMeta):
    """data source class."""
    config: Incomplete
    def __init__(self, config: Any) -> None: ...
    @abstractmethod
    async def load_data(self, *args, **kwargs) -> pl.DataFrame: ...
    async def stream_data(self) -> AsyncIterable[pl.DataFrame]: ...

class PipelineStep(ABC, Generic[InT, OutT]):
    """pipeline step class."""
    STEP_NAME: Incomplete
    STEP_VERSION: str
    requires: set[str]
    produces: set[str]
    preferred_engine: Engine | None
    name: Incomplete
    def __init__(self, name: str | None = None, **_) -> None: ...
    async def execute(self, data: Any, context: PipelineContext) -> Any: ...
    def apply_batch(self, lf: pl.LazyFrame, ctx: PipelineContext) -> pl.LazyFrame: ...
    def apply_batch_pandas(self, df: pd.DataFrame, ctx: PipelineContext) -> pd.DataFrame: ...
    async def apply_stream(self, aiter: AsyncIterator[dict], ctx: PipelineContext) -> AsyncIterator[dict]: ...
    @classmethod
    def compose(cls, *steps: PipelineStep) -> CompositeStep: ...
    def __rshift__(self, other: PipelineStep) -> CompositeStep: ...

class CompositeStep(PipelineStep):
    """composite step class."""
    steps: Incomplete
    def __init__(self, steps: list[PipelineStep], **kwargs) -> None: ...
    def apply_batch(self, lf: pl.LazyFrame, ctx: PipelineContext) -> pl.LazyFrame: ...

class CleaningStep(PipelineStep, metaclass=abc.ABCMeta):
    """cleaning step class."""
    @abstractmethod
    def apply(self, df: pl.DataFrame) -> pl.DataFrame: ...
    def apply_batch(self, lf: pl.LazyFrame, ctx: PipelineContext) -> pl.LazyFrame: ...