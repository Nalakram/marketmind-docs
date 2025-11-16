from .cuda_runtime import capabilities as capabilities
from .errors import OOMRetry as OOMRetry
from .specs import Spec as Spec
from _typeshed import Incomplete
from dataclasses import dataclass
from srcPy.ops.mm_logkit import get_logger as get_logger
from typing import Any, Callable

logger: Incomplete

@dataclass
class PlanSegment:
    ops: list[Callable]
    spec: Spec | None = ...
    estimated_cost: float = ...
    def __hash__(self) -> int: ...

def estimate_compute_cost(op: Callable, backend: str) -> float: ...
def score_segment(segment: PlanSegment, sample_data: Any, backend: str | None = None) -> float: ...

class HeuristicPlanner:
    metrics: dict[str, float]
    def select_plan(self, segments: list[PlanSegment], sample_data: Any) -> list[PlanSegment]: ...
    def optimize(self, segments: list[PlanSegment], sample_data: Any) -> list[PlanSegment]: ...
