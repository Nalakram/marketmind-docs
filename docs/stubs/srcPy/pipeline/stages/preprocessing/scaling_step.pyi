# from ._base_plan_step import PlanStep as PlanStep  # stripped for AutoAPI
# from ._normalize import canonical_op as canonical_op, normalize_clip as normalize_clip, normalize_common_keys as normalize_common_keys  # stripped for AutoAPI
# from ._provenance import build_meta as build_meta  # stripped for AutoAPI
from typing import Any as Incomplete
from srcPy.ops.mm_logkit import get_logger as get_logger
from srcPy.preprocessor.api import PlanSpec as PlanSpec

logger: Incomplete = ...

class ScalingStep(PlanStep):
    """scaling step class."""
    STEP_NAME: str = ...
    STEP_VERSION: str = ...
    @staticmethod
    def forbid_backend_imports() -> bool: ...