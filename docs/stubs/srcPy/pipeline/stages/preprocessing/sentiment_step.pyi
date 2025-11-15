from ._base_plan_step import PlanStep as PlanStep
from ._normalize import assign_device_hint as assign_device_hint, canonical_op as canonical_op, normalize_clip as normalize_clip, normalize_common_keys as normalize_common_keys
from ._provenance import build_meta as build_meta
from _typeshed import Incomplete

logger: Incomplete

class SentimentESGStep(PlanStep):
    STEP_NAME: str
    STEP_VERSION: str
    @staticmethod
    def forbid_backend_imports() -> bool: ...
