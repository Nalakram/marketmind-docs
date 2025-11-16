from typing import Any as Incomplete
from srcPy.ops.mm_logkit import get_logger as get_logger
from srcPy.preprocessor.graph.backends.registry import register as register
from srcPy.preprocessor.graph.executor import Executor as Executor
from srcPy.preprocessor.utils.columns import op_chain as op_chain
from srcPy.preprocessor.utils.cuda_runtime import capabilities as capabilities, init_rmm_pool as init_rmm_pool
from srcPy.preprocessor.utils.errors import OOMRetry as OOMRetry
from srcPy.preprocessor.utils.io_gpu import read_parquet_gpu as read_parquet_gpu
from srcPy.preprocessor.utils.nvtx import nvtx_range as nvtx_range
from srcPy.preprocessor.utils.plan_costs import HeuristicPlanner as HeuristicPlanner, PlanSegment as PlanSegment
from srcPy.preprocessor.utils.specs import SpecFactory as SpecFactory
from srcPy.preprocessor.utils.torch_bridge import to_torch_batch as to_torch_batch
from srcPy.utils.exceptions import PreprocessingError as PreprocessingError
from srcPy.utils.validators import validate_dataframe as validate_dataframe

logger: Incomplete = ...

def robust_scaler_cudf(ir, gdf, group_by=None, **_): ...

class CuDFExecutor(Executor):
    """cu df executor class."""
    to_torch: Incomplete = ...
    def __init__(self, *, pool_size: str = '4GB', to_torch: bool = False) -> None: ...
    def read_parquet(self, path, columns=None, byte_range=None): ...
    def execute(self, compiled_plan, df): ...