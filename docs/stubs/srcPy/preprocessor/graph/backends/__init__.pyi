from . import cudf as cudf, polars as polars
from .cudf import CuDFExecutor as CuDFExecutor
from .polars import PolarsExecutor as PolarsExecutor
from .registry import get as get, list_ops as list_ops, register as register
from _typeshed import Incomplete
from typing import Literal

logger: Incomplete

def get_executor(backend: Literal['auto', 'polars', 'cudf', 'cpu', 'gpu'] = 'auto'): ...
