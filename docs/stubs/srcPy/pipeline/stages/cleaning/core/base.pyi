import abc
import pandas as pd
from typing import Any as Incomplete
from abc import ABC, abstractmethod
from typing import Any

PolarsDataFrame: Incomplete

class PolarsDataFrame: ...

class CleaningStep(ABC, metaclass=abc.ABCMeta):
    """cleaning step class."""
    @abstractmethod
    def apply(self, df: pd.DataFrame) -> pd.DataFrame: ...

class StepRegistry:
    """step registry class."""
    @classmethod
    def register(cls, name: str, step_cls: type[CleaningStep]): ...
    @classmethod
    def get(cls, name: str) -> type[CleaningStep] | None: ...
    @classmethod
    def freeze(cls) -> None: ...
    @classmethod
    def thaw(cls) -> None: ...
    @classmethod
    def list_registered(cls) -> list[str]: ...

class DataValidationError(Exception):
    """Exception raised when data validation occurs."""
    message: Incomplete
    details: Incomplete
    def __init__(self, message: str, details: dict[str, Any] | None = None) -> None: ...