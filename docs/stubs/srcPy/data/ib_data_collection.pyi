from _typeshed import Incomplete
from collections.abc import Generator
from contextlib import contextmanager
from dataclasses import dataclass
from datetime import datetime
from srcPy.utils.optional_imports import pd as pd

@dataclass
class _Bar:
    date: datetime
    open: float
    high: float
    low: float
    close: float
    volume: int

def create_mock_bars(n: int, start_date: str = '2025-01-01'): ...

class NoDataError(RuntimeError): ...

@contextmanager
def ib_connection(*args, **kwargs) -> Generator[Incomplete, None, Incomplete]: ...
def fetch_historical_data(symbol: str, end_datetime: str, *, duration: str = '1 D', bar_size: str = '1 min', what_to_show: str = 'TRADES', use_cache: bool = True, ib_client: object | None = None): ...
