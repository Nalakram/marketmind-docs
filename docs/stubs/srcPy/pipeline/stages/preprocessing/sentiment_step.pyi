from ._base_plan_step import PlanStep as PlanStep
from ._normalize import assign_device_hint as assign_device_hint, canonical_op as canonical_op, normalize_clip as normalize_clip, normalize_common_keys as normalize_common_keys
from ._provenance import build_meta as build_meta
from typing import Any as Incomplete
from srcPy.ops.mm_logkit import get_logger as get_logger
from srcPy.preprocessor.api import PlanSpec as PlanSpec

logger: Incomplete

class SentimentESGStep(PlanStep):
    """sentiment esg step class."""
    STEP_NAME: str
    STEP_VERSION: str
    @staticmethod
    def forbid_backend_imports() -> bool: ...