import contextlib
import types
from _typeshed import Incomplete

logger: Incomplete
NVTX_ENABLED: Incomplete

@contextlib.contextmanager
def range_ctx(message: str, color: int | None = None): ...
def nvtx_range(message: str, color: int | None = None): ...

class nvtx_plan:
    name: Incomplete
    color: Incomplete
    def __init__(self, name: str, color: int | None = None) -> None: ...
    def __enter__(self): ...
    def __exit__(self, exc_type: type[BaseException] | None, exc: BaseException | None, tb: types.TracebackType | None) -> None: ...
