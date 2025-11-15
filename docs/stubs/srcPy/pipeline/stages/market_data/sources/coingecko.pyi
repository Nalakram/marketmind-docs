import polars as pl
from . import register_source as register_source
from ..exceptions import DataFetchError as DataFetchError
from .base import APIDataSource as APIDataSource
from _typeshed import Incomplete
from typing import AsyncIterator

class CoinGeckoSource(APIDataSource):
    base_url: str
    vs_currency: Incomplete
    coin_map: Incomplete
    rate_limit: Incomplete
    def __init__(self, config: dict) -> None: ...
    async def get_historical(self, symbol: str, start: str, end: str, *, eager: bool = False) -> pl.LazyFrame | pl.DataFrame: ...
    async def get_realtime(self, symbol: str, *, interval: float = None) -> AsyncIterator[pl.DataFrame]: ...
