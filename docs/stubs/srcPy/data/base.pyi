from _typeshed import Incomplete
from collections import OrderedDict as OrderedDict
from functools import singledispatch
from srcPy.ops.mm_logkit import get_logger as get_logger
from srcPy.pipeline.stages.market_data.sources.base import APIDataSource as APIDataSource
from srcPy.utils.exceptions import DataFetchError as DataFetchError, NoDataError as NoDataError
from srcPy.utils.optional_imports import pl as pl
from srcPy.utils.validators import lazy_validate_ohlcv as lazy_validate_ohlcv

logger: Incomplete

class AbstractAPIDataManager:
    registry: dict[str, type[APIDataSource]]
    def __init_subclass__(cls, **kwargs) -> None: ...
    @classmethod
    def register(cls, source_type: str): ...
    config: Incomplete
    sources: dict[str, APIDataSource]
    def __init__(self, config) -> None: ...
    def add_source(self, source_type: str, source: APIDataSource): ...
    @singledispatch
    async def load_data(self, query: str | list[str], source_name: str | None = None) -> pl.LazyFrame | dict[str, pl.LazyFrame | Exception]: ...
    @load_data.register
    async def _(self, query: str, source_name: str | None = None) -> pl.LazyFrame: ...
    @load_data.register
    async def _(self, queries: list, source_name: str | None = None) -> dict[str, pl.LazyFrame | Exception]: ...
