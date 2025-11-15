from _typeshed import Incomplete
from srcPy.data.base import AbstractAPIDataManager
from srcPy.pipeline.stages.market_data.sources.base import APIDataSource

class AlternativeDataManager(AbstractAPIDataManager): ...

class TwitterSource(APIDataSource):
    bearer_token: Incomplete
    def __init__(self, config) -> None: ...

class ESGSource(APIDataSource):
    def __init__(self, config) -> None: ...

class WeatherSource(APIDataSource):
    api_key: Incomplete
    def __init__(self, config) -> None: ...
