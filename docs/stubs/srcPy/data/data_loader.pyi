from abc import ABC, abstractmethod
from typing import Any, Dict, List, Literal, TypeVar, Generic, Union, AsyncIterator, TYPE_CHECKING, Protocol
from dataclasses import dataclass

if TYPE_CHECKING:
    import aiohttp
    import pandas as pd
    from srcPy.utils.config import CSVConfig, TwitterConfig, ESGConfig, FREDConfig, BloombergConfig, WeatherConfig, AlpacaConfig, InfluxDBConfig
    from srcPy.utils.exceptions import NoDataError, IBConnectionError

__all__ = [
    'BaseDataLoader', 'APIDataLoader', 'CSVLoader', 'TwitterLoader', 'ESGLoader',
    'FREDLoader', 'BloombergLoader', 'WeatherLoader', 'AlpacaStreamLoader',
    'InfluxDBLoader', 'get_runtime_config', 'build_loader', 'RetryPolicy', 'Streamable'
]

ConfigT = TypeVar("ConfigT")

@dataclass
class RetryPolicy:
    """
    Configuration for retry policy in API data loaders.

    Attributes:
        max_attempts (int): Maximum number of retry attempts.
        initial_backoff_seconds (float): Initial backoff time in seconds.
        max_backoff_seconds (float): Maximum backoff time in seconds.
        retry_strategy (str): Retry style such as :term:`Exponential Back-off`.
        fallback (bool): Whether to use a fallback mechanism.
        fallback_timeout_seconds (float): Timeout for fallback in seconds.
    """
    max_attempts: int
    initial_backoff_seconds: float
    max_backoff_seconds: float
    retry_strategy: str
    fallback: bool
    fallback_timeout_seconds: float

class Streamable(Protocol):
    """
    Protocol for data loaders that support streaming.

    Any class with an asynchronous `stream_data` method satisfies this protocol.
    """
    async def stream_data(self) -> AsyncIterator[Any]:
        """
        Stream data asynchronously.

        :yields: Data from the stream.
        :rtype: AsyncIterator[Any]
        """
        pass

def get_runtime_config() -> Any:
    """
    Retrieve the runtime configuration.

    :returns: Runtime configuration object.
    :rtype: Any
    """

class BaseDataLoader(Generic[ConfigT], ABC):
    """
    Abstract base class for data loaders.

    This class defines the interface for all data loaders. Subclasses must implement the `load_data` method.

    :param config: Configuration object for the data loader.
    :type config: ConfigT
    """
    def __init__(self, config: ConfigT):
        """
        Initialize the data loader.
        """
        pass

    @abstractmethod
    async def load_data(self, *args, **kwargs) -> 'pd.DataFrame':
        """
        Load data asynchronously.

        This method must be implemented by subclasses.

        :returns: Loaded data.
        :rtype: pandas.DataFrame
        :raises NotImplementedError: If not implemented by subclass.
        """
        pass

class APIDataLoader(BaseDataLoader[ConfigT]):
    """
    Base class for API data loaders.

    Provides implementation for loading data from APIs with retry logic.

    :param config: Configuration object.
    :type config: ConfigT

    Attributes:
        retry_policy (RetryPolicy): Configuration for retry attempts and backoff.
    """
    def __init__(self, config: ConfigT):
        """
        Initialize the API data loader.
        """
        pass

    async def _request(self, url: str, headers: Dict[str, str], timeout: int) -> List[Dict[str, Any]]:
        """
        Make an asynchronous HTTP GET request.

        :param url: The URL to request.
        :type url: str
        :param headers: HTTP headers.
        :type headers: Dict[str, str]
        :param timeout: Timeout in seconds.
        :type timeout: int
        :returns: JSON response as a list of dictionaries.
        :rtype: List[Dict[str, Any]]
        :raises aiohttp.ClientError: If the request fails.
        """
        pass

class CSVLoader(BaseDataLoader['CSVConfig']):
    """
    Loader for CSV data.

    Loads data from a CSV file specified in the configuration.

    :param config: Configuration object for CSV loading.
    :type config: :class:`~srcPy.utils.config.CSVConfig`
    """
    def __init__(self, config: 'CSVConfig'):
        """
        Initialize the CSV loader.
        """
        pass

    def load_data(self) -> List['pd.DataFrame']:
        """
        Load data from the CSV file.

        Reads the CSV file in chunks and returns a list of DataFrames.

        :returns: List of DataFrames, each representing a chunk of the CSV file.
        :rtype: List[pandas.DataFrame]
        :raises ValueError: If no data is loaded from the CSV file.
        """
        pass

    async def stream_data(self) -> AsyncIterator[Union[str, bytes]]:
        """
        Stream data from a WebSocket connection.

        Yields messages received from the WebSocket.

        :yields: Message received from the WebSocket.
        :type: Union[str, bytes]
        :raises: :exc:`~srcPy.utils.exceptions.IBConnectionError`: If the WebSocket connection fails.
        """
        pass

class TwitterLoader(APIDataLoader['TwitterConfig']):
    """
    Loader for Twitter data.

    Loads data from the Twitter :term:`REST API` using the provided configuration.

    :param config: Configuration object for Twitter API.
    :type config: :class:`~srcPy.utils.config.TwitterConfig`

    Attributes:
        base_url (str): Base URL for the Twitter API.
        endpoints (Dict[str, str]): :term:`API Endpoint` for various Twitter queries.
        bearer_token (str): Bearer token for authentication.
        retry_after_header (str): Header for rate-limit retry information.
        timeout (int): Request timeout in seconds.
        api_key (str): API key for Twitter authentication.
    """
    def __init__(self, config: 'TwitterConfig'):
        """
        Initialize the Twitter loader.
        """
        pass

    async def load_data(self, query: str) -> 'pd.DataFrame':
        """
        Load data from the Twitter :term:`REST API` for a given query.

        :param query: The query to search for.
        :type query: str
        :returns: DataFrame containing the loaded data.
        :rtype: pandas.DataFrame
        :raises: :exc:`~srcPy.utils.exceptions.NoDataError`: If no data is returned from the API.
        :raises aiohttp.ClientError: If the HTTP request fails.
        :raises RuntimeError: If the API returns a 4xx/5xx error.
        """
        pass

    async def stream_data(self) -> AsyncIterator[bytes]:
        """
        Stream data from the Twitter :term:`Streaming API` filtered stream endpoint.

        Yields lines of data received from the stream.

        :yields: Line of data from the stream.
        :type: bytes
        :raises aiohttp.ClientError: If the stream request fails.
        """
        pass

class ESGLoader(APIDataLoader['ESGConfig']):
    """
    Loader for :term:`ESG` data.

    Loads :term:`ESG` data from an :term:`REST API`.

    :param config: Configuration object for ESG API.
    :type config: :class:`~srcPy.utils.config.ESGConfig`
    """
    def __init__(self, config: 'ESGConfig'):
        """
        Initialize the ESG loader.
        """
        pass

    async def load_data(self, identifiers: List[str]) -> 'pd.DataFrame':
        """
        Load :term:`ESG` data for the given identifiers.

        :param identifiers: List of identifiers to load data for.
        :type identifiers: List[str]
        :returns: DataFrame containing the loaded data.
        :rtype: pandas.DataFrame
        :raises aiohttp.ClientError: If the HTTP request fails.
        :raises RuntimeError: If the API returns a 4xx/5xx error.
        """
        pass

class FREDLoader(APIDataLoader['FREDConfig']):
    """
    Loader for FRED data.

    Loads economic data from the FRED :term:`REST API`.

    :param config: Configuration object for FRED API.
    :type config: :class:`~srcPy.utils.config.FREDConfig`

    Attributes:
        api_key (str): API key for FRED authentication.
    """
    def __init__(self, config: 'FREDConfig'):
        """
        Initialize the FRED loader.
        """
        pass

    async def load_data(self, series_ids: List[str]) -> 'pd.DataFrame':
        """
        Load economic data from the FRED :term:`REST API` for the given series IDs.

        :param series_ids: List of series IDs to load data for.
        :type series_ids: List[str]
        :returns: DataFrame containing the loaded data.
        :rtype: pandas.DataFrame
        :raises aiohttp.ClientError: If the HTTP request fails.
        :raises RuntimeError: If the API returns a 4xx/5xx error.
        """
        pass

class BloombergLoader(APIDataLoader['BloombergConfig']):
    """
    Loader for Bloomberg data.

    Loads financial data from the Bloomberg :term:`REST API`.

    :param config: Configuration object for Bloomberg API.
    :type config: :class:`~srcPy.utils.config.BloombergConfig`

    Attributes:
        api_key (str): API key for Bloomberg authentication.
    """
    def __init__(self, config: 'BloombergConfig'):
        """
        Initialize the Bloomberg loader.
        """
        pass

    async def load_data(self, topics: List[str]) -> 'pd.DataFrame':
        """
        Load financial data from the Bloomberg :term:`REST API` for the given topics.

        :param topics: List of topics to load data for.
        :type topics: List[str]
        :returns: DataFrame containing the loaded data.
        :rtype: pandas.DataFrame
        :raises aiohttp.ClientError: If the HTTP request fails.
        :raises RuntimeError: If the API returns a 4xx/5xx error.
        """
        pass

class WeatherLoader(APIDataLoader['WeatherConfig']):
    """
    Loader for weather data.

    Loads weather data from an :term:`REST API`.

    :param config: Configuration object for Weather API.
    :type config: :class:`~srcPy.utils.config.WeatherConfig`

    Attributes:
        api_key (str): API key for Weather API authentication.
    """
    def __init__(self, config: 'WeatherConfig'):
        """
        Initialize the Weather loader.
        """
        pass

    async def load_data(self, locations: List[str]) -> 'pd.DataFrame':
        """
        Load weather data from an :term:`REST API` for the given locations.

        :param locations: List of locations to load data for.
        :type locations: List[str]
        :returns: DataFrame containing the loaded data.
        :rtype: pandas.DataFrame
        :raises aiohttp.ClientError: If the HTTP request fails.
        :raises RuntimeError: If the API returns a 4xx/5xx error.
        """
        pass

class AlpacaStreamLoader(BaseDataLoader['AlpacaConfig']):
    """
    Loader for streaming data from Alpaca.

    Streams real-time market data from a :term:`Streaming API` over WebSockets.

    :param config: Configuration object for Alpaca streaming.
    :type config: :class:`~srcPy.utils.config.AlpacaConfig`

    Attributes:
        api_key (str): API key for Alpaca authentication.
        secret_key (str): Secret key for Alpaca authentication.
        endpoint (str): :term:`API Endpoint` for streaming.
    """
    def __init__(self, config: 'AlpacaConfig'):
        """
        Initialize the Alpaca stream loader.
        """
        pass

    async def stream_data(self) -> AsyncIterator['aiohttp.WSMessage']:
        """
        Stream data from the Alpaca :term:`Streaming API` WebSocket.

        Yields messages received from the WebSocket.

        :yields: Message received from the WebSocket.
        :type: aiohttp.WSMessage
        :raises: :exc:`~srcPy.utils.exceptions.IBConnectionError`: If the WebSocket connection fails.
        """
        pass

    async def load_data(self, *args, **kwargs) -> 'pd.DataFrame':
        """
        Not implemented for stream loader.

        :returns: None
        :rtype: pandas.DataFrame
        :raises NotImplementedError: Always raised.
        """
        pass

class InfluxDBLoader(BaseDataLoader['InfluxDBConfig']):
    """
    Loader for :term:`InfluxDB` data.

    Loads data from :term:`InfluxDB` using the provided configuration.

    :param config: Configuration object for InfluxDB.
    :type config: :class:`~srcPy.utils.config.InfluxDBConfig`
    """
    def __init__(self, config: 'InfluxDBConfig'):
        """
        Initialize the InfluxDB loader.
        """
        pass

    async def load_data(self, query: str) -> 'pd.DataFrame':
        """
        Load data from :term:`InfluxDB` using the given query.

        :param query: The query to execute.
        :type query: str
        :returns: DataFrame containing the loaded data.
        :rtype: pandas.DataFrame
        :raises ValueError: If the query is invalid or fails.
        """
        pass

_LoaderKey = Literal[
    "csv", "influxdb", "twitter", "alpaca_stream",
    "esg", "fred", "bloomberg", "weather"
]

def build_loader(config_section: _LoaderKey) -> BaseDataLoader:
    """
    Build and return a data loader based on the configuration section.

    :param config_section: The section of the configuration to use (e.g., 'csv', 'twitter', etc.).
    :type config_section: Literal['csv', 'influxdb', 'twitter', 'alpaca_stream', 'esg', 'fred', 'bloomberg', 'weather']
    :returns: An instance of a data loader subclass.
    :rtype: BaseDataLoader
    :raises ValueError: If the config_section is unknown.
    """
    pass