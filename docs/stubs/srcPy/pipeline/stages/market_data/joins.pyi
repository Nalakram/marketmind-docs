from .transforms import build_steps as build_steps
from _typeshed import Incomplete
from polars import LazyFrame as LazyFrame
from pydantic import BaseModel
from srcPy.ops.caching import ttl_cache as ttl_cache
from srcPy.ops.mm_logkit import get_logger as get_logger
from srcPy.pipeline.core.pipeline_core_base import PipelineStep as PipelineStep
from srcPy.utils.exceptions import DataValidationError as DataValidationError
from typing import Callable

logger: Incomplete
SOURCE_REGISTRY: dict[str, LazyFrame]

class JoinSpec(BaseModel):
    source_name: str
    on: list[str]
    how: str
    suffix: str | None

class MultiSourceJoinConfig(BaseModel):
    joins: list[JoinSpec]

class MultiSourceJoinStep(PipelineStep):
    config: Incomplete
    def __init__(self, config: MultiSourceJoinConfig) -> None: ...
    def apply(self, lf: LazyFrame) -> LazyFrame: ...

AGG_MAP: dict[str, Callable]

class ResampleConfig(BaseModel):
    freq: str
    group_by: list[str]
    agg: dict[str, str]
    timestamp_col: str

class ResampleStep(PipelineStep):
    freq: Incomplete
    group_by: Incomplete
    agg: Incomplete
    timestamp_col: Incomplete
    def __init__(self, config: ResampleConfig) -> None: ...
    def apply(self, lf: LazyFrame) -> LazyFrame: ...

JOIN_STEPS: dict[str, type[PipelineStep]]
JOIN_CONFIGS: dict[str, type[BaseModel]]

def build_join_steps(configs: list[dict]) -> list[PipelineStep]: ...
