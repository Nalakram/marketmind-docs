import polars as pl
from .registry import register_source as register_source
from _typeshed import Incomplete
from srcPy.pipeline.stages.market_data.sources.base import DataSource
from typing import AsyncIterator

class FREDSource(DataSource):
    fred: Incomplete
    def __init__(self, config: dict) -> None: ...
    async def get_historical(self, symbol: str, start: str, end: str, *, eager: bool = False) -> pl.LazyFrame | pl.DataFrame: ...
    async def get_realtime(self, symbol: str, *, interval: float = 3600.0) -> AsyncIterator[pl.DataFrame]: ...
