import abc
import polars as pl
from typing import Any as Incomplete
from abc import abstractmethod
from srcPy.ops.mm_logkit import get_logger as get_logger
from srcPy.pipeline.core.pipeline_core_metrics import AsyncMLflowLogger as AsyncMLflowLogger
from srcPy.pipeline.stages.cleaning.core.base import CleaningStep as CleaningStep
from srcPy.utils.exceptions import FileFormatError as FileFormatError
from srcPy.utils.validators import validate_dataframe as validate_dataframe, validate_file_data as validate_file_data

logger: Incomplete

class FSInterface(metaclass=abc.ABCMeta):
    """fs interface class."""
    @abstractmethod
    def get_size(self, path: str) -> int: ...

class LocalFS(FSInterface):
    """local fs class."""
    def get_size(self, path: str) -> int: ...

class IOValidationStep(CleaningStep):
    """io validation step class."""
    mlflow_logger: Incomplete
    file_path: Incomplete
    format: Incomplete
    max_size_bytes: Incomplete
    fs: Incomplete
    supported_formats: Incomplete
    def __init__(self, mlflow_logger: AsyncMLflowLogger, file_path: str, format: str | None = None, max_size_bytes: int = ..., fs: FSInterface | None = None) -> None: ...
    def apply(self, df: pl.DataFrame) -> pl.DataFrame: ...
    def __del__(self) -> None: ...