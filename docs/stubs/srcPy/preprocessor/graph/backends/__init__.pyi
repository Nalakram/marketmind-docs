# from . import cudf as cudf, polars as polars  # stripped for AutoAPI
# from .cudf import CuDFExecutor as CuDFExecutor  # stripped for AutoAPI
# from .polars import PolarsExecutor as PolarsExecutor  # stripped for AutoAPI
# from .registry import get as get, list_ops as list_ops, register as register  # stripped for AutoAPI
from typing import Any as Incomplete
from srcPy.ops.mm_logkit import get_logger as get_logger
from typing import Literal

logger: Incomplete = ...

def get_executor(backend: Literal['auto', 'polars', 'cudf', 'cpu', 'gpu'] = 'auto'): ...