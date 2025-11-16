import polars as pl
from . import register_source as register_source
from ..exceptions import DataFetchError as DataFetchError
from .base import DataSource as DataSource
from typing import Any as Incomplete
from influxdb_client.client.query_api import QueryApi as QueryApi
from typing import AsyncIterator

class InfluxDBSource(DataSource):
    """influx db source class."""
    client: Incomplete
    query_api: QueryApi
    bucket: Incomplete
    measurement: Incomplete
    def __init__(self, config: dict) -> None: ...
    async def get_historical(self, symbol: str, start: str, end: str, *, eager: bool = False) -> pl.LazyFrame | pl.DataFrame: ...
    async def get_realtime(self, symbol: str, *, interval: float = 60.0) -> AsyncIterator[pl.DataFrame]: ...
    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None: ...