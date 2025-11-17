# from .batch import BatchPipeline as BatchPipeline  # stripped for AutoAPI
# from .hybrid import HybridCleanerPipeline as HybridCleanerPipeline  # stripped for AutoAPI
# from .streaming import StreamingCleanerPipeline as StreamingCleanerPipeline  # stripped for AutoAPI
from typing import Callable, TypeVar

__all__ = ['run_blocking', 'run_cpu', 'BatchPipeline', 'StreamingCleanerPipeline', 'HybridCleanerPipeline']

T = TypeVar('T')

def run_blocking(func: Callable[..., T], *args, timeout: float | None = None, **kwargs) -> T: ...
def run_cpu(func: Callable[..., T], *args, timeout: float | None = None, **kwargs) -> T: ...