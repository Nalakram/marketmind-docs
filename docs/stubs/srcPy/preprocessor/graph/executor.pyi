import abc
from _typeshed import Incomplete
from typing import Any

logger: Incomplete
Engine: Incomplete

class Executor(abc.ABC, metaclass=abc.ABCMeta):
    backend: Incomplete
    cache: dict[str, Any]
    lru_cache: Incomplete
    execution_history: list[dict[str, Any]]
    planner: Incomplete
    def __init__(self, backend: str, cache_size: int = 128) -> None: ...
    @abc.abstractmethod
    def execute(self, plan: list[dict[str, Any]], data: Any, group_by: list[str]) -> Any: ...
    def evolve(self, threshold: float = 1.0) -> str | None: ...

class PolarsExecutor(Executor):
    engine_pref: Incomplete
    def __init__(self, engine_pref: Engine = 'auto') -> None: ...
    def execute(self, plan: list[dict[str, Any]], data: Any, group_by: list[str]) -> Any: ...

class CuDFExecutor(Executor):
    def __init__(self, pool_size: str = '4GB') -> None: ...
    def execute(self, plan: list[dict[str, Any]], data: Any, group_by: list[str]) -> Any: ...

class ExecutorFactory:
    @classmethod
    def register(cls, backend: str, executor_cls: type[Executor]): ...
    @classmethod
    def create(cls, backend: str = 'auto', **kwargs) -> Executor: ...
