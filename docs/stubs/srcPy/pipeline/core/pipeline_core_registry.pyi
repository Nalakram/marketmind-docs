from _typeshed import Incomplete
from srcPy.ops.mm_logkit import get_logger as get_logger
from srcPy.pipeline.core.pipeline_core_base import PipelineStep as PipelineStep

logger: Incomplete

class StepRegistry:
    @classmethod
    def register(cls, *args, override: bool = False) -> None: ...
    @classmethod
    def get(cls, stage: str, name: str) -> type[PipelineStep]: ...
    @classmethod
    def load_plugins(cls, entry_point_group: str, stage: str) -> None: ...
