from . import cudf as cudf, polars as polars
from .cudf import CuDFExecutor as CuDFExecutor
from .polars import PolarsExecutor as PolarsExecutor
from .registry import get as get, list_ops as list_ops, register as register
from typing import Any as Incomplete
from srcPy.ops.mm_logkit import get_logger as get_logger
from typing import Literal

logger: Incomplete

def get_executor(backend: Literal['auto', 'polars', 'cudf', 'cpu', 'gpu'] = 'auto'): ...