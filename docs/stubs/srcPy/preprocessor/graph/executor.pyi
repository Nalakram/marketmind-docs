import abc
from typing import Any as Incomplete
from srcPy.ops.mm_logkit import get_logger as get_logger
from srcPy.preprocessor.graph.expr import get_polars_lowering as get_polars_lowering
from srcPy.preprocessor.utils.cuda_runtime import capabilities as capabilities
from srcPy.preprocessor.utils.errors import OOMRetry as OOMRetry
from srcPy.preprocessor.utils.nvtx import nvtx_range as nvtx_range
from srcPy.preprocessor.utils.plan_costs import HeuristicPlanner as HeuristicPlanner
from srcPy.utils.exceptions import PreprocessingError as PreprocessingError, UnsupportedPlan as UnsupportedPlan
from typing import Any

logger: Incomplete
Engine: Incomplete

class Executor(abc.ABC, metaclass=abc.ABCMeta):
    """executor class."""
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
    """polars executor class."""
    engine_pref: Incomplete
    def __init__(self, engine_pref: Engine = 'auto') -> None: ...
    def execute(self, plan: list[dict[str, Any]], data: Any, group_by: list[str]) -> Any: ...

class CuDFExecutor(Executor):
    """cu df executor class."""
    def __init__(self, pool_size: str = '4GB') -> None: ...
    def execute(self, plan: list[dict[str, Any]], data: Any, group_by: list[str]) -> Any: ...

class ExecutorFactory:
    """Factory for creating executor instances."""
    @classmethod
    def register(cls, backend: str, executor_cls: type[Executor]): ...
    @classmethod
    def create(cls, backend: str = 'auto', **kwargs) -> Executor: ...