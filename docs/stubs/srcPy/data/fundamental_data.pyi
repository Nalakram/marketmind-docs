from _typeshed import Incomplete
from srcPy.data.base import AbstractAPIDataManager as AbstractAPIDataManager
from srcPy.pipeline.stages.market_data.sources.base import APIDataSource as APIDataSource
from srcPy.utils.config import get_runtime_config as get_runtime_config

class FundamentalDataManager(AbstractAPIDataManager): ...

class BloombergSource(APIDataSource):
    api_key: Incomplete
    def __init__(self, config) -> None: ...
