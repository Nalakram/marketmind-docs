from _typeshed import Incomplete
from srcPy.pipeline.core.pipeline_core_base import PipelineStep as PipelineStep
from srcPy.pipeline.core.pipeline_core_context import PipelineContext

logger: Incomplete

class BatchPipeline:
    steps: Incomplete
    def __init__(self, steps: list[PipelineStep], *, default_cfg: dict | None = None) -> None: ...
    def run(self, data, *, ctx: PipelineContext | None = None, distributed: str | None = None, collect: bool = True): ...
