import abc
from .cuda_runtime import capabilities as capabilities
from .errors import SchemaMismatch as SchemaMismatch
from _typeshed import Incomplete
from abc import ABC, abstractmethod
from srcPy.ops.mm_logkit import get_logger as get_logger
from typing import Any, Mapping, Sequence

logger: Incomplete

class Validator(ABC, metaclass=abc.ABCMeta):
    @abstractmethod
    def validate(self, obj: Any) -> None: ...

class SchemaValidator(Validator):
    expected: Incomplete
    strict: Incomplete
    def __init__(self, expected: Mapping[str, str], strict: bool = False) -> None: ...
    def validate(self, df: Any) -> None: ...

class PlanValidator(Validator):
    def validate(self, graph: dict[Any, Sequence[Any]]) -> None: ...

class ValidatorFactory:
    @staticmethod
    def schema(expected: Mapping[str, str], strict: bool = False) -> Validator: ...
    @staticmethod
    def plan() -> Validator: ...

def schema_checks(df, expected: Mapping[str, str], strict: bool = False) -> None: ...
def plan_checks(graph: dict[Any, Sequence[Any]]) -> None: ...
