import polars as pl
from . import register_source as register_source
from ..exceptions import DataFetchError as DataFetchError
from .base import DataSource as DataSource
from _typeshed import Incomplete
from typing import AsyncIterator

class IBKRSource(DataSource):
    host: Incomplete
    port: Incomplete
    client_id: Incomplete
    default_bar_size: Incomplete
    what_to_show: Incomplete
    use_rth: Incomplete
    ib: Incomplete
    queue_maxsize: Incomplete
    def __init__(self, config: dict) -> None: ...
    async def __aenter__(self): ...
    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None: ...
    async def get_historical(self, symbol: str, start: str, end: str, *, eager: bool = False) -> pl.LazyFrame | pl.DataFrame: ...
    async def get_realtime(self, symbol: str, *, interval: float = 5.0) -> AsyncIterator[pl.DataFrame]: ...
