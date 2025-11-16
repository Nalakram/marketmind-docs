from typing import Any as Incomplete
from srcPy.preprocessor.graph.executor import Executor
from typing import Any

__all__ = ['get', 'register', 'list_ops', 'get_lowering', 'get', 'register', 'OPS', 'get', 'register', 'OPS']

get_lowering: Incomplete

def get(*args): ...
def register(*args, **kwargs): ...
def list_ops(*args): ...

class PolarsExecutor(Executor):
    """polars executor class."""
    engine_pref: Incomplete
    to_torch: Incomplete
    def __init__(self, engine_pref: Engine = 'auto', to_torch: bool = False) -> None: ...
    def execute(self, compiled_plan, df: Any): ...

OPS: Incomplete