import contextlib
from typing import Any as Incomplete
from collections.abc import Generator
from dataclasses import dataclass
from srcPy.ops.mm_logkit import get_logger as get_logger

logger: Incomplete

@dataclass(frozen=True)
class GpuCapabilities:
    """gpu capabilities class."""
    has_cuda: bool
    has_rmm: bool
    has_cudf: bool
    has_polars_gpu: bool
    has_nvtabular: bool
    has_kvikio: bool
    device_count: int = ...
    compute_capability: str | None = ...

def capabilities() -> GpuCapabilities: ...
def init_rmm_pool(pool_size: int | None = None, managed_memory: bool = False, async_alloc: bool = True, logging: bool = False, release_threshold: int | None = None) -> None: ...

class StreamFactory:
    """Factory for creating stream instances."""
    @staticmethod
    def create(non_blocking: bool = True): ...

class StreamPool:
    """stream pool class."""
    def __init__(self, size: int = 4, non_blocking: bool = True) -> None: ...
    @contextlib.contextmanager
    def lease(self) -> Generator[Incomplete]: ...

def pinned_array(shape, dtype: str = 'float32'): ...
def device_synchronize() -> None: ...
@contextlib.contextmanager
def maybe_stream(stream) -> Generator[None]: ...