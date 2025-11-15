from _typeshed import Incomplete
from srcPy.data.base import AbstractAPIDataManager
from srcPy.pipeline.stages.market_data.sources.base import APIDataSource

class FundamentalDataManager(AbstractAPIDataManager): ...

class BloombergSource(APIDataSource):
    api_key: Incomplete
    def __init__(self, config) -> None: ...
