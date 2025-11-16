from .batch import BatchPipeline as BatchPipeline
from .hybrid import HybridCleanerPipeline as HybridCleanerPipeline
from .streaming import StreamingCleanerPipeline as StreamingCleanerPipeline
from typing import Callable, TypeVar

__all__ = ['run_blocking', 'run_cpu', 'BatchPipeline', 'StreamingCleanerPipeline', 'HybridCleanerPipeline']

T = TypeVar('T')

def run_blocking(func: Callable[..., T], *args, timeout: float | None = None, **kwargs) -> T: ...
def run_cpu(func: Callable[..., T], *args, timeout: float | None = None, **kwargs) -> T: ...