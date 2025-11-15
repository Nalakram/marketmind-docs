from _typeshed import Incomplete
from srcPy.pipeline.core.pipeline_core_base import PipelineStep
from srcPy.preprocessor.api import PlanSpec as PlanSpec

class PlanStep(PipelineStep):
    STEP_VERSION: str
    cfg: Incomplete
    def __init__(self, *, backend: str | None = 'auto', device: int = 0, nvtx: bool = False, **cfg) -> None: ...
    def fit_transform(self, df, ctx): ...
