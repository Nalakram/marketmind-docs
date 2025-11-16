from typing import Any as Incomplete
from srcPy.data.base import AbstractAPIDataManager as AbstractAPIDataManager
from srcPy.pipeline.stages.market_data.sources.base import APIDataSource as APIDataSource
from srcPy.utils.config import get_runtime_config as get_runtime_config

class AlternativeDataManager(AbstractAPIDataManager): ...

class TwitterSource(APIDataSource):
    """twitter source class."""
    bearer_token: Incomplete
    def __init__(self, config) -> None: ...

class ESGSource(APIDataSource):
    """esg source class."""
    def __init__(self, config) -> None: ...

class WeatherSource(APIDataSource):
    """weather source class."""
    api_key: Incomplete
    def __init__(self, config) -> None: ...