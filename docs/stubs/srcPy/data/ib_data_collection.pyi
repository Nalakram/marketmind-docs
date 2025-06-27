import pandas as pd
from _typeshed import Incomplete
from ib_insync import BarData, IB as IB
from srcPy.utils.config import get_config as get_config
from srcPy.utils.exceptions import DataFetchError as DataFetchError, IBConnectionError as IBConnectionError
from srcPy.utils.logger import configure_logger as configure_logger, get_logger as get_logger
from srcPy.utils.validators import validate_date as validate_date, validate_symbol as validate_symbol

logger: Incomplete

class NoDataError(DataFetchError):
    def __init__(self, symbol: str) -> None: ...

def create_mock_bars(n: int, start_date: str = '2025-01-01') -> list[BarData]: ...
def fetch_historical_data(symbol: str, end_date: str = '', duration: str = '1 Y', bar_size: str = '1 day', ib_client: IB | None = None, use_cache: bool = True, what_to_show: str = 'TRADES', use_rth: bool = True, format_date: int = 1) -> pd.DataFrame: ...
async def fetch_multiple_historical_data(symbols: list[str], end_date: str = '', duration: str = '1 Y', bar_size: str = '1 day', use_cache: bool = True, what_to_show: str = 'TRADES', use_rth: bool = True, format_date: int = 1) -> dict[str, pd.DataFrame]: ...
