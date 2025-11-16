from ._base_plan_step import PlanStep as PlanStep
from ._normalize import canonical_op as canonical_op, normalize_clip as normalize_clip, normalize_common_keys as normalize_common_keys
from ._provenance import build_meta as build_meta
from _typeshed import Incomplete
from srcPy.ops.mm_logkit import get_logger as get_logger
from srcPy.preprocessor.api import PlanSpec as PlanSpec

logger: Incomplete

class ScalingStep(PlanStep):
    STEP_NAME: str
    STEP_VERSION: str
    @staticmethod
    def forbid_backend_imports() -> bool: ...
