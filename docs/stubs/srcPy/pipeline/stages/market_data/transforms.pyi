import polars as pl
from _typeshed import Incomplete
from polars import LazyFrame as LazyFrame
from pydantic import BaseModel
from srcPy.pipeline.core.pipeline_core_base import PipelineStep

logger: Incomplete

class ColumnRenameConfig(BaseModel):
    mapping: dict[str, str]

class ColumnRenameStep(PipelineStep):
    mapping: Incomplete
    def __init__(self, config: ColumnRenameConfig) -> None: ...
    def apply(self, lf: LazyFrame) -> LazyFrame: ...

class TypeCastConfig(BaseModel):
    model_config: Incomplete
    dtypes: dict[str, pl.DataType]

class TypeCastStep(PipelineStep):
    dtypes: Incomplete
    def __init__(self, config: TypeCastConfig) -> None: ...
    def apply(self, lf: LazyFrame) -> LazyFrame: ...

TRANSFORM_STEPS: dict[str, type[PipelineStep]]
TRANSFORM_CONFIGS: dict[str, type[BaseModel]]

def build_steps(configs: list[dict], step_registry: dict[str, type[PipelineStep]], config_registry: dict[str, type[BaseModel]]) -> list[PipelineStep]: ...
def build_transform_steps(configs: list[dict]) -> list[PipelineStep]: ...
