import pandas as pd
from _typeshed import Incomplete
from srcPy.data.data_cleaning import DataCleaner as DataCleaner
from srcPy.data.data_loader import build_loader as build_loader
from srcPy.data.ib_data_collection import fetch_historical_data as fetch_historical_data, fetch_multiple_historical_data as fetch_multiple_historical_data
from srcPy.data.market_data import AlphaVantageSource as AlphaVantageSource, CoinGeckoSource as CoinGeckoSource, FileSource as FileSource, MarketDataManager as MarketDataManager
from srcPy.data.preprocessor import Preprocessor as Preprocessor
from srcPy.utils.config import get_config as get_config
from srcPy.utils.logger import get_logger as get_logger

logger: Incomplete

class DataPipelineOrchestrator:
    config: Incomplete
    market_manager: Incomplete
    cleaner: Incomplete
    preprocessor: Incomplete
    def __init__(self, config: Incomplete | None = None) -> None: ...
    def fetch_data(self, source: str, **kwargs) -> pd.DataFrame: ...
    def fetch_multiple_data(self, symbols: list[str], source: str, cache_dir: str | None = None, **kwargs) -> dict[str, pd.DataFrame]: ...
    def run_pipeline(self, df: pd.DataFrame, cache_dir: str | None = None) -> tuple | dict[str, tuple]: ...
    def process(self, source: str, **kwargs) -> tuple | dict[str, tuple]: ...
    def process_multiple(self, symbols: list[str], source: str, cache_dir: str | None = None, **kwargs) -> dict[str, tuple | dict[str, tuple]]: ...
