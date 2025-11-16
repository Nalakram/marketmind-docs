from typing import Any as Incomplete
from collections.abc import Generator
from functools import singledispatch
from srcPy.utils.optional_imports import pl
from typing import Any

__all__ = ['build_loader', 'fetch_raw', 'APIDataLoader', 'AlpacaStreamLoader', 'BloombergLoader', 'CSVLoader', 'ESGLoader', 'FREDLoader', 'InfluxDBLoader', 'TwitterLoader', 'WeatherLoader']

class PipelineConfig: ...

@singledispatch
async def fetch_raw(cfg: Any, *, symbols: str | list[str], start: str, end: str, concurrency_limit: int = 50) -> pl.LazyFrame | dict[str, pl.LazyFrame | Exception]: ...
def build_loader(cfg: Any) -> Any: ...

class _LoaderBase:
    """loader base class."""
    config: Incomplete
    max_attempts: Incomplete
    retry_strategy: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...
    def load_data(self): ...
    async def stream_data(self) -> Generator[Incomplete]: ...

# Names in __all__ with no definition:
#   APIDataLoader
#   AlpacaStreamLoader
#   BloombergLoader
#   CSVLoader
#   ESGLoader
#   FREDLoader
#   InfluxDBLoader
#   TwitterLoader
#   WeatherLoader