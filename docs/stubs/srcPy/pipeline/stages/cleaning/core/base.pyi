import abc
import pandas as pd
from _typeshed import Incomplete
from abc import ABC, abstractmethod
from typing import Any

PolarsDataFrame: Incomplete

class PolarsDataFrame: ...

class CleaningStep(ABC, metaclass=abc.ABCMeta):
    @abstractmethod
    def apply(self, df: pd.DataFrame) -> pd.DataFrame: ...

class StepRegistry:
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
    message: Incomplete
    details: Incomplete
    def __init__(self, message: str, details: dict[str, Any] | None = None) -> None: ...
