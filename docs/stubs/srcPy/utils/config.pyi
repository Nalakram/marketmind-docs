"""config.py — one-stop, type-safe access to every MarketMind knob.

config.py is the central nervous system of the platform’s configuration layer. It transforms a single
`config.yaml` file into a deeply-nested tree of Pydantic models, validates that tree against a
JSON Schema, and gives the rest of the codebase an IDE-friendly, auto-completed object to query.

| Feature                       | How it works                                                                                                                                                                                                                 |
|-------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Rich model catalogue**       | 90-plus `BaseModel` subclasses cover everything from **technical indicators** (`RSIConfig`, `MACDConfig`, `VWAPConfig`) to **security & compliance** (`EncryptionConfig`, `ComplianceConfig`) and **backtesting knobs** (`RiskManagementConfig`, `PositionSizingConfig`). These models are grouped logically—e.g., `TechnicalIndicators`, `Streaming`, `Logging`—and ultimately roll up into the root `Config` model that mirrors the full YAML hierarchy. |
| **Environment-variable expansion** | The function `resolve_env_vars()` walks any nested dict, list, or string structure and replaces `${VAR}` placeholders with values from `os.environ`, keeping sensitive data like API keys out of source control. |
| **Four-stage loader**          | The `load_config()` function runs a four-step pipeline: 1️⃣ Load YAML, 2️⃣ Expand environment variables, 3️⃣ Validate against JSON Schema, 4️⃣ Parse into the root `Config` Pydantic model. Any failure halts startup. |
| **Singleton accessor**         | Calling `get_config()` anywhere in the codebase returns the same cached instance, avoiding redundant parses and ensuring config consistency across modules. |
| **Handy constants & logging**  | Constants like `BASE`, `CONFIG_PATH`, and `SCHEMA_PATH` help locate project directories and key files. A preconfigured `logger` is also available, ensuring logging works even before app startup completes. |


**Why it matters**
------------------

- **Zero magic strings:** Every section is a strongly-typed attribute
  (``config.preprocess.normalization.method``) instead of brittle ``dict["method"]`` lookups.

- **Fail-fast:** Schema + Pydantic validation catches typos or missing keys before a single trade executes.

- **Docs-ready:** Each model ships NumPy-style docstrings, cross-linked to the glossary and stubbed
  in ``config.pyi``, so Sphinx auto-generates polished API pages out of the box.

- **Extensible:** Dropping a new section in YAML only requires a matching ``BaseModel``; the loader
  picks it up automatically.
"""

from _typeshed import Incomplete
from datetime import datetime
from pathlib import Path
from pydantic import BaseModel, Field
from srcPy.utils.exceptions import ConfigValidationError as ConfigValidationError
from srcPy.utils.logger import configure_logger as configure_logger, get_logger as get_logger
from typing import Any, Dict, List, Optional
from typing_extensions import Literal

logger: Incomplete
"""The configured logger instance for the MarketMind platform."""

BASE: Path
"""The project root directory, typically two levels above this file."""

CONFIG_PATH: Path
"""The default path to the configuration YAML file (e.g., 'data/config.yaml')."""

SCHEMA_PATH: Path
"""The default path to the JSON schema file used for validation (e.g.,
'data/config_schema.json')."""

class RSIConfig(BaseModel):
    """Configuration for the Relative Strength Index (:term:`RSI`) technical indicator.

    The :term:`RSI` is a momentum oscillator that measures the speed and change of
    price movements, commonly used to identify overbought or oversold conditions
    in the :term:`RSI`.

    Attributes
    ----------
    enabled : bool, default ``False``
        Whether to enable :term:`RSI` calculation.
    window : int, default ``14``
        The number of periods to use for calculating the :term:`RSI`.
    fillna_method : str, default ``'ffill'``
        The method to fill NaN values in the :term:`RSI` series.
    """

    enabled: bool = False
    window: int = 14
    fillna_method: str = 'ffill'

class MACDConfig(BaseModel):
    """Configuration for the :term:`MACD` indicator.

    The :term:`MACD` is a trend-following momentum indicator that shows the
    relationship between two moving averages.

    Attributes
    ----------
    enabled : bool, default ``False``
        Whether to enable :term:`MACD` calculation.
    fast_period : int, default ``12``
        The period for the fast moving average.
    slow_period : int, default ``26``
        The period for the slow moving average.
    signal_period : int, default ``9``
        The period for the signal line.
    fillna_method : str, default ``'ffill'``
        The method to fill NaN values.
    """

    enabled: bool = False
    fast_period: int = 12
    slow_period: int = 26
    signal_period: int = 9
    fillna_method: str = 'ffill'

class ATRConfig(BaseModel):
    """Configuration for the :term:`ATR` indicator.

    The :term:`ATR` measures market volatility by calculating the average range
    between high and low prices.

    Attributes
    ----------
    enabled : bool, default ``False``
        Whether to enable :term:`ATR` calculation.
    window : int, default ``14``
        The number of periods to use for calculating the :term:`ATR`.
    fillna_method : str, default ``'ffill'``
        The method to fill NaN values.
    """

    enabled: bool = False
    window: int = 14
    fillna_method: str = 'ffill'

class BollingerBandsConfig(BaseModel):
    """Configuration for :term:`Bollinger Bands`.

    :term:`Bollinger Bands` are volatility bands placed above and below a moving
    average.

    Attributes
    ----------
    enabled : bool, default ``False``
        Whether to enable :term:`Bollinger Bands` calculation.
    window : int, default ``20``
        The period for the moving average.
    std_dev : float, default ``2.0``
        The number of standard deviations for the bands.
    fillna_method : str, default ``'ffill'``
        The method to fill NaN values.
    """

    enabled: bool = False
    window: int = 20
    std_dev: float = 2.0
    fillna_method: str = 'ffill'

class VWAPConfig(BaseModel):
    """Configuration for the :term:`VWAP`.

    The :term:`VWAP` is a trading benchmark that gives the average price a security
    has traded at throughout the day, based on both volume and price.

    Attributes
    ----------
    enabled : bool, default ``False``
        Whether to enable :term:`VWAP` calculation.
    reset_period : Literal['daily', 'hourly', 'weekly'], default ``'daily'``
        The period at which :term:`VWAP` resets.
    fillna_method : str, default ``'ffill'``
        The method to fill NaN values.
    """

    enabled: bool = False
    reset_period: Literal['daily', 'hourly', 'weekly'] = 'daily'
    fillna_method: str = 'ffill'

class TechnicalIndicators(BaseModel):
    """Configuration grouping all technical indicators.

    This model aggregates settings for various technical indicators used in
    preprocessing.

    Attributes
    ----------
    rsi : :class:`~marketmind.config.RSIConfig` | None, default None
        Configuration for the :term:`RSI` indicator.
    macd : :class:`~marketmind.config.MACDConfig` | None, default None
        Configuration for the :term:`MACD` indicator.
    atr : :class:`~marketmind.config.ATRConfig` | None, default None
        Configuration for the :term:`ATR` indicator.
    vwap : :class:`~marketmind.config.VWAPConfig` | None, default None
        Configuration for the :term:`VWAP` indicator.
    bollinger_bands : :class:`~marketmind.config.BollingerBandsConfig` | None, default None
        Configuration for :term:`Bollinger Bands`.
    """

    rsi: Optional[RSIConfig] = None
    macd: Optional[MACDConfig] = None
    atr: Optional[ATRConfig] = None
    vwap: Optional[VWAPConfig] = None
    bollinger_bands: Optional[BollingerBandsConfig] = None

class ClipExtremes(BaseModel):
    """Configuration for clipping extreme values during normalization.

    Attributes
    ----------
    min : float
        The minimum value for clipping.
    max : float
        The maximum value for clipping.
    """

    min: float
    max: float

class NormalizationConfig(BaseModel):
    """Configuration for feature normalization routines.

    Attributes
    ----------
    method : Literal['minmax', 'standard', 'robust']
        The normalization method.
    rolling_window : int
        The size of the rolling window for normalization.
    clip_extremes : :class:`~marketmind.config.ClipExtremes`
        Settings for clipping extreme values.
    """

    method: Literal['minmax', 'standard', 'robust']
    rolling_window: int
    clip_extremes: ClipExtremes

class SentimentConfig(BaseModel):
    """Configuration for :term:`Sentiment (financial)` score generation.

    Attributes
    ----------
    enabled : bool
        Whether to enable :term:`Sentiment (financial)` analysis.
    source : str
        The data source for :term:`Sentiment (financial)`.
    sentiment_model : Literal['vader', 'bert', 'finbert']
        The model used for :term:`Sentiment (financial)` analysis. Options include
        :term:`VADER`, :term:`FinBERT`, or BERT.
    """

    enabled: bool
    source: str
    sentiment_model: Literal['vader', 'bert', 'finbert']

class ESGNormalizedConfig(BaseModel):
    """Configuration for :term:`ESG` feature normalization.

    Attributes
    ----------
    enabled : bool
        Whether to enable :term:`ESG` normalization.
    method : Literal['minmax', 'standard', 'robust']
        The normalization method for :term:`ESG` data.
    """

    enabled: bool
    method: Literal['minmax', 'standard', 'robust']

class CalendarConfig(BaseModel):
    """Configuration for calendar-based feature engineering.

    Attributes
    ----------
    enabled : bool, default ``False``
        Whether to enable calendar features.
    day_of_week : bool, default ``True``
        Whether to include day-of-week features.
    holidays : list[str] | None, default ``[]``
        List of holiday dates in 'YYYY-MM-DD' format.
    timezones : list[str] | None, default ``[]``
        List of timezones to consider.
    """

    enabled: bool = False
    day_of_week: bool = True
    holidays: Optional[List[str]] = []
    timezones: Optional[List[str]] = []

    def is_holiday(self, date: datetime) -> bool:
        """Check if the given date is a holiday.

        Parameters
        ----------
        date : datetime
            The date to check.

        Returns
        -------
        bool
            True if the date is a holiday, False otherwise.
        """

class CustomFeatures(BaseModel):
    """Configuration for custom-engineered features.

    Attributes
    ----------
    sentiment : :class:`~marketmind.config.SentimentConfig` | None, default None
        Settings for :term:`Sentiment (financial)` analysis features.
    esg_normalized : :class:`~marketmind.config.ESGNormalizedConfig` | None, default None
        Settings for normalized :term:`ESG` features.
    """

    sentiment: Optional[SentimentConfig] = None
    esg_normalized: Optional[ESGNormalizedConfig] = None

class AnomalyDetectionConfig(BaseModel):
    """Configuration for runtime anomaly detection.

    Attributes
    ----------
    enabled : bool, default ``False``
        Whether to enable anomaly detection.
    method : Literal['zscore', 'isolation_forest', 'autoencoder'] | None, default None
        The anomaly detection method. Options include :term:`Z-score`,
        :term:`Isolation Forest`, or :term:`Autoencoder`.
    params : dict | None, default ``{}``
        Parameters for the anomaly detection method.
    """

    enabled: bool = False
    method: Optional[Literal['zscore', 'isolation_forest', 'autoencoder']] = None
    params: Optional[dict] = {}

class Preprocessing(BaseModel):
    """Top-level configuration for data preprocessing.

    Attributes
    ----------
    technical_indicators : :class:`~marketmind.config.TechnicalIndicators`
        Settings for technical indicators.
    normalization : :class:`~marketmind.config.NormalizationConfig`
        Settings for feature normalization.
    custom_features : :class:`~marketmind.config.CustomFeatures`
        Settings for custom features.
    calendar_features : :class:`~marketmind.config.CalendarConfig`, default a default instance of :class:`~marketmind.config.CalendarConfig`
        Settings for calendar-based features.
    """

    technical_indicators: TechnicalIndicators
    normalization: NormalizationConfig
    custom_features: CustomFeatures
    calendar_features: CalendarConfig = Field(default_factory=CalendarConfig)

class Streaming(BaseModel):
    """Configuration for in-memory streaming and mini-batch processing.

    Attributes
    ----------
    batch_size : int
        The size of each batch.
    update_interval_seconds : int
        Frequency of updates in seconds.
    buffer_size : int
        Size of the data buffer.
    max_latency_ms : int
        Maximum allowed latency in milliseconds.
    buffer_retention_seconds : int
        Duration to retain data in the buffer.
    event_triggers : dict[str, str]
        Event triggers for streaming actions.
    priority_queue : str
        Type of priority queue to use.
    failure_recovery : dict[str, Any]
        Settings for failure recovery.
    sync_interval_seconds : int
        Interval for synchronization in seconds.
    """

    batch_size: int
    update_interval_seconds: int
    buffer_size: int
    max_latency_ms: int
    buffer_retention_seconds: int
    event_triggers: Dict[str, str]
    priority_queue: str
    failure_recovery: Dict[str, Any]
    sync_interval_seconds: int

class RetryPolicy(BaseModel):
    """Configuration for retry policies on external data refreshes.

    Attributes
    ----------
    max_attempts : int
        Maximum number of retry attempts.
    initial_backoff_seconds : int
        Initial backoff duration in seconds.
    max_backoff_seconds : int
        Maximum backoff duration in seconds.
    retry_strategy : Literal['exponential', 'linear']
        Strategy for retries. Options include :term:`Exponential Back-off` or
        :term:`Linear Back-off`.
    """

    max_attempts: int
    initial_backoff_seconds: int
    max_backoff_seconds: int
    retry_strategy: Literal['exponential', 'linear']

class ValidationThresholds(BaseModel):
    """Configuration for data validation thresholds.

    Attributes
    ----------
    max_missing_ratio : float
        Maximum allowed ratio of missing data.
    max_outlier_ratio : float
        Maximum allowed ratio of outliers.
    """

    max_missing_ratio: float
    max_outlier_ratio: float

class Fallback(BaseModel):
    """Configuration for fallback data sources.

    Attributes
    ----------
    twitter : str
        Fallback source for Twitter data.
    esg : str
        Fallback source for :term:`ESG` data.
    data_source : str
        Fallback main data source.
    """

    twitter: str
    esg: str
    data_source: str

class Alerting(BaseModel):
    """Configuration for real-time alerting.

    Attributes
    ----------
    enabled : bool
        Whether alerting is enabled.
    channel : str
        The alerting channel.
    critical_failures : list[str]
        List of critical failure conditions.
    alert_severity : list[str]
        List of severity levels for alerts.
    """

    enabled: bool
    channel: str
    critical_failures: List[str]
    alert_severity: List[str]

class ErrorHandling(BaseModel):
    """Configuration for error handling policies.

    Attributes
    ----------
    retry_policy : :class:`~marketmind.config.RetryPolicy`
        Settings for retrying failed operations.
    validation_thresholds : :class:`~marketmind.config.ValidationThresholds`
        Thresholds for data validation.
    fallback : :class:`~marketmind.config.Fallback`
        Fallback data sources.
    alerting : :class:`~marketmind.config.Alerting`
        Alerting settings.
    fallback_timeout_seconds : int
        Timeout for fallback operations in seconds.
    """

    retry_policy: RetryPolicy
    validation_thresholds: ValidationThresholds
    fallback: Fallback
    alerting: Alerting
    fallback_timeout_seconds: int

class RateLimitConfig(BaseModel):
    """Configuration for API rate limits.

    Attributes
    ----------
    per_minute : int | None, default None
        Maximum calls per minute.
    max_calls_per_window : int | None, default None
        Maximum calls per custom window.
    window_seconds : int | None, default None
        Window size in seconds for rate limiting.
    """

    per_minute: Optional[int] = None
    max_calls_per_window: Optional[int] = None
    window_seconds: Optional[int] = None

class CSVConfig(BaseModel):
    """Configuration for CSV data ingestion.

    Attributes
    ----------
    path : str
        Path to the CSV file.
    chunksize : int
        Size of chunks for processing.
    use_dask : bool
        Whether to use Dask for parallel processing.
    compression : str
        Compression type.
    data_format : Literal['ohlc', 'tick']
        Format of the data. Options include 'ohlc' for :term:`OHLC` bars or 'tick'
        for :term:`Tick data`.
    """

    path: str
    chunksize: int
    use_dask: bool
    compression: str
    data_format: Literal['ohlc', 'tick']

class InfluxDBConfig(BaseModel):
    """Configuration for :term:`InfluxDB` data source.

    Attributes
    ----------
    host : str
        Host address of the :term:`InfluxDB` server.
    port : int
        Port number for connection.
    token : str
        Authentication token.
    org : str
        Organization name.
    bucket : str
        Bucket name for data storage.
    query : str
        Query to fetch data.
    """

    host: str
    port: int
    token: str
    org: str
    bucket: str
    query: str

class DataSource(BaseModel):
    """Configuration for the main market data source.

    Attributes
    ----------
    type : Literal['csv', 'influxdb']
        Type of data source.
    csv : :class:`~marketmind.config.CSVConfig` | None, default None
        CSV-specific settings.
    influxdb : :class:`~marketmind.config.InfluxDBConfig` | None, default None
        :term:`InfluxDB`-specific settings.
    """

    type: Literal['csv', 'influxdb']
    csv: Optional[CSVConfig] = None
    influxdb: Optional[InfluxDBConfig] = None

class TwitterConfig(BaseModel):
    """Configuration for Twitter/X API integration.

    Attributes
    ----------
    base_url : str
        Base URL for the API.
    bearer_token : str
        Bearer token for authentication.
    authentication_type : Literal['bearer', 'oauth']
        Type of authentication.
    endpoints : dict[str, str]
        API endpoints.
    default_params : dict[str, Any]
        Default parameters for requests.
    rate_limit : :class:`~marketmind.config.RateLimitConfig`
        Rate limit settings.
    retry_after_header : str
        Header for retry timing.
    timeout_seconds : int
        Request timeout in seconds.
    cache_duration_hours : int
        Cache duration in hours.
    data_resolution : str
        Resolution of data.
    api_key : str | None, default None
        API key, if required.
    """

    base_url: str
    bearer_token: str
    authentication_type: Literal['bearer', 'oauth']
    endpoints: Dict[str, str]
    default_params: Dict[str, Any]
    rate_limit: RateLimitConfig
    retry_after_header: str
    timeout_seconds: int
    cache_duration_hours: int
    data_resolution: str
    api_key: Optional[str] = None

class AlpacaConfig(BaseModel):
    """Configuration for Alpaca market data or brokerage API.

    Attributes
    ----------
    api_key : str | None, default None
        API key.
    secret_key : str
        Secret key for authentication.
    endpoint : str
        API endpoint URL.
    """

    api_key: Optional[str] = None
    secret_key: str
    endpoint: str

class ESGConfig(BaseModel):
    """Configuration for :term:`ESG` data provider (e.g., Sustainalytics).

    Attributes
    ----------
    base_url : str
        Base URL for the API.
    api_key : str
        API key for authentication.
    authentication_type : Literal['bearer', 'api_key']
        Type of authentication.
    endpoints : dict[str, str]
        API endpoints.
    default_params : dict[str, str]
        Default request parameters.
    timeout_seconds : int
        Request timeout in seconds.
    cache_duration_hours : int
        Cache duration in hours.
    data_resolution : str
        Data resolution.
    """

    base_url: str
    api_key: str
    authentication_type: Literal['bearer', 'api_key']
    endpoints: Dict[str, str]
    default_params: Dict[str, str]
    timeout_seconds: int
    cache_duration_hours: int
    data_resolution: str

class BloombergConfig(BaseModel):
    """Configuration for Bloomberg data services.

    Attributes
    ----------
    base_url : str
        Base URL for the API.
    api_key : str | None, default None
        API key.
    authentication_type : str | None, default None
        Authentication type.
    endpoints : dict[str, str]
        API endpoints.
    default_params : dict[str, str], default ``{}``
        Default request parameters.
    rate_limit : :class:`~marketmind.config.RateLimitConfig` | None, default None
        Rate limit settings.
    timeout_seconds : int, default ``10``
        Request timeout in seconds.
    cache_duration_hours : int, default ``24``
        Cache duration in hours.
    data_resolution : str | None, default None
        Data resolution.
    """

    base_url: str
    api_key: Optional[str] = None
    authentication_type: Optional[str] = None
    endpoints: Dict[str, str]
    default_params: Dict[str, str] = {}
    rate_limit: Optional[RateLimitConfig] = None
    timeout_seconds: int = 10
    cache_duration_hours: int = 24
    data_resolution: Optional[str] = None

class WeatherConfig(BaseModel):
    """Configuration for weather data provider.

    Attributes
    ----------
    base_url : str
        Base URL for the API.
    api_key : str | None, default None
        API key.
    authentication_type : str | None, default None
        Authentication type.
    endpoints : dict[str, str]
        API endpoints.
    default_params : dict[str, str], default ``{}``
        Default request parameters.
    rate_limit : :class:`~marketmind.config.RateLimitConfig` | None, default None
        Rate limit settings.
    timeout_seconds : int, default ``10``
        Request timeout in seconds.
    cache_duration_hours : int, default ``24``
        Cache duration in hours.
    data_resolution : str | None, default None
        Data resolution.
    """

    base_url: str
    api_key: Optional[str] = None
    authentication_type: Optional[str] = None
    endpoints: Dict[str, str]
    default_params: Dict[str, str] = {}
    rate_limit: Optional[RateLimitConfig] = None
    timeout_seconds: int = 10
    cache_duration_hours: int = 24
    data_resolution: Optional[str] = None

class FREDConfig(BaseModel):
    """Configuration for Federal Reserve Economic Data (FRED) API.

    Attributes
    ----------
    base_url : str
        Base URL for the API.
    api_key : str | None, default None
        API key.
    authentication_type : str | None, default None
        Authentication type.
    endpoints : dict[str, str]
        API endpoints.
    default_params : dict[str, str], default ``{}``
        Default request parameters.
    rate_limit : :class:`~marketmind.config.RateLimitConfig` | None, default None
        Rate limit settings.
    timeout_seconds : int, default ``10``
        Request timeout in seconds.
    cache_duration_hours : int, default ``24``
        Cache duration in hours.
    data_resolution : str | None, default None
        Data resolution.
    """

    base_url: str
    api_key: Optional[str] = None
    authentication_type: Optional[str] = None
    endpoints: Dict[str, str]
    default_params: Dict[str, str] = {}
    rate_limit: Optional[RateLimitConfig] = None
    timeout_seconds: int = 10
    cache_duration_hours: int = 24
    data_resolution: Optional[str] = None

class AlternativeData(BaseModel):
    """Configuration for non-traditional data providers.

    Attributes
    ----------
    twitter : :class:`~marketmind.config.TwitterConfig` | None, default None
        Twitter API settings.
    alpaca : :class:`~marketmind.config.AlpacaConfig` | None, default None
        Alpaca API settings.
    esg : :class:`~marketmind.config.ESGConfig` | None, default None
        :term:`ESG` provider settings.
    fred : :class:`~marketmind.config.FREDConfig` | None, default None
        FRED API settings.
    bloomberg : :class:`~marketmind.config.BloombergConfig` | None, default None
        Bloomberg API settings.
    weather : :class:`~marketmind.config.WeatherConfig` | None, default None
        Weather API settings.
    """

    twitter: Optional[TwitterConfig] = None
    alpaca: Optional[AlpacaConfig] = None
    esg: Optional[ESGConfig] = None
    fred: Optional[FREDConfig] = None
    bloomberg: Optional[BloombergConfig] = None
    weather: Optional[WeatherConfig] = None

class InteractiveBrokersConfig(BaseModel):
    """Configuration for Interactive Brokers real-time data stream.

    Attributes
    ----------
    host : str
        Host address for the IB Gateway/TWS.
    port : int
        Port number for connection.
    client_id : int
        Client ID for the connection.
    subscription_topics : list[str]
        Topics to subscribe to.
    api_key : str
        API key for authentication.
    endpoint : str
        API endpoint URL.
    connection_timeout_seconds : int
        Timeout for establishing connection.
    priority : int
        Priority level for data requests.
    what_to_show : str, default ``'TRADES'``
        Data type to retrieve.
    use_rth : bool, default ``True``
        Whether to use regular trading hours only.
    format_date : int, default ``1``
        Date format code (1 for string, 2 for epoch).
    """

    host: str
    port: int
    client_id: int
    subscription_topics: List[str]
    api_key: str
    endpoint: str
    connection_timeout_seconds: int
    priority: int
    what_to_show: str = 'TRADES'
    use_rth: bool = True
    format_date: int = 1

class RealTimeMarketDataConfig(BaseModel):
    """Configuration for real-time market data sources.

    Attributes
    ----------
    interactive_brokers : :class:`~marketmind.config.InteractiveBrokersConfig` | None, default None
        Settings for Interactive Brokers.
    alpaca : :class:`~marketmind.config.AlpacaConfig` | None, default None
        Settings for Alpaca real-time data.
    """

    interactive_brokers: Optional[InteractiveBrokersConfig] = None
    alpaca: Optional[AlpacaConfig] = None

class ModelArchitecture(BaseModel):
    """Configuration for neural network architecture.

    Attributes
    ----------
    num_layers : int
        Number of layers in the model.
    hidden_size : int
        Size of hidden layers.
    dropout : float
        Dropout rate for regularization.
    """

    num_layers: int
    hidden_size: int
    dropout: float

class Model(BaseModel):
    """Configuration for model training and inference.

    Attributes
    ----------
    model_type : str
        Type of model.
    architecture : :class:`~marketmind.config.ModelArchitecture`
        Neural network architecture settings.
    sequence_length : int
        Length of input sequences.
    prediction_horizon : int
        Horizon for predictions.
    feature_list : list[str]
        List of features to use.
    training_device : str
        Device for training.
    model_checkpoint : dict[str, int]
        Checkpoint settings.
    feature_importance : dict[str, str]
        Feature importance metrics.
    onnx_export : dict[str, Any]
        Settings for ONNX export.
    """

    model_type: str
    architecture: ModelArchitecture
    sequence_length: int
    prediction_horizon: int
    feature_list: List[str]
    training_device: str
    model_checkpoint: Dict[str, int]
    feature_importance: Dict[str, str]
    onnx_export: Dict[str, Any]

class Cleaning(BaseModel):
    """Configuration for data cleaning rules.

    Attributes
    ----------
    missing_values : dict[str, Any]
        Rules for handling missing values.
    outliers : dict[str, Any]
        Rules for handling outliers.
    denoising : dict[str, Any]
        Rules for denoising data.
    """

    missing_values: Dict[str, Any]
    outliers: Dict[str, Any]
    denoising: Dict[str, Any]

class FileOutputConfig(BaseModel):
    """Configuration for file-based logging output.

    Attributes
    ----------
    enabled : bool
        Whether file logging is enabled.
    path : str
        Path to the log file.
    rotation : str
        Log rotation policy.
    """

    enabled: bool
    path: str
    rotation: str

class InfluxDBOutputConfig(BaseModel):
    """Configuration for :term:`InfluxDB` logging output.

    Attributes
    ----------
    enabled : bool
        Whether :term:`InfluxDB` logging is enabled.
    host : str
        Host address of the :term:`InfluxDB` server.
    port : int
        Port number for connection.
    token : str
        Authentication token.
    org : str
        Organization name.
    bucket : str
        Bucket name for logs.
    """

    enabled: bool
    host: str
    port: int
    token: str
    org: str
    bucket: str

class OutputsConfig(BaseModel):
    """Configuration for all logging outputs.

    Attributes
    ----------
    console : bool
        Whether console logging is enabled.
    file : :class:`~marketmind.config.FileOutputConfig`
        File logging settings.
    influxdb : :class:`~marketmind.config.InfluxDBOutputConfig`
        :term:`InfluxDB` logging settings.
    """

    console: bool
    file: FileOutputConfig
    influxdb: InfluxDBOutputConfig

class MetricAggregationConfig(BaseModel):
    """Configuration for metric aggregation.

    Attributes
    ----------
    aggregation_window_seconds : int
        Window size for aggregating metrics in seconds.
    """

    aggregation_window_seconds: int

class DashboardConfig(BaseModel):
    """Configuration for dashboard integration.

    Attributes
    ----------
    grafana_url : str
        URL for the Grafana dashboard.
    """

    grafana_url: str

class Logging(BaseModel):
    """Configuration for global logging and metrics.

    Attributes
    ----------
    level : str
        Logging level.
    outputs : :class:`~marketmind.config.OutputsConfig`
        Settings for log outputs.
    metrics_report_interval_seconds : int
        Interval for reporting metrics.
    custom_metrics : list[str]
        List of custom metrics to log.
    model_metrics : list[str]
        List of model-specific metrics.
    metric_aggregation : :class:`~marketmind.config.MetricAggregationConfig`
        Metric aggregation settings.
    log_sampling_rate : float
        Sampling rate for logs.
    dashboard_config : :class:`~marketmind.config.DashboardConfig`
        Dashboard integration settings.
    """

    level: str
    outputs: OutputsConfig
    metrics_report_interval_seconds: int
    custom_metrics: List[str]
    model_metrics: List[str]
    metric_aggregation: MetricAggregationConfig
    log_sampling_rate: float
    dashboard_config: DashboardConfig

class EncryptionConfig(BaseModel):
    """Configuration for data encryption.

    Attributes
    ----------
    at_rest : bool
        Whether to encrypt data at rest.
    in_transit : bool
        Whether to encrypt data in transit.
    encryption_algorithm : str
        Encryption algorithm to use.
    """

    at_rest: bool
    in_transit: bool
    encryption_algorithm: str

class CredentialsConfig(BaseModel):
    """Configuration for storing API credentials.

    Attributes
    ----------
    twitter_api_key : str | None, default None
        Twitter API key.
    esg_api_key : str | None, default None
        :term:`ESG` API key.
    fred_api_key : str | None, default None
        FRED API key.
    bloomberg_api_key : str | None, default None
        Bloomberg API key.
    weather_api_key : str | None, default None
        Weather API key.
    alpha_vantage_api_key : str | None, default None
        Alpha Vantage API key.
    """

    twitter_api_key: Optional[str] = None
    esg_api_key: Optional[str] = None
    fred_api_key: Optional[str] = None
    bloomberg_api_key: Optional[str] = None
    weather_api_key: Optional[str] = None
    alpha_vantage_api_key: Optional[str] = None

class DataAnonymizationConfig(BaseModel):
    """Configuration for data anonymization.

    Attributes
    ----------
    anonymize_pii : bool
        Whether to anonymize personally identifiable information.
    """

    anonymize_pii: bool

class ComplianceConfig(BaseModel):
    """Configuration for regulatory compliance.

    Attributes
    ----------
    audit_log : bool
        Whether to enable audit logging.
    retention_days : int
        Number of days to retain logs.
    audit_frequency_days : int
        Frequency of audits in days.
    data_anonymization : :class:`~marketmind.config.DataAnonymizationConfig`
        Anonymization settings.
    """

    audit_log: bool
    retention_days: int
    audit_frequency_days: int
    data_anonymization: DataAnonymizationConfig

class Security(BaseModel):
    """Configuration for security settings.

    Attributes
    ----------
    encryption : :class:`~marketmind.config.EncryptionConfig`
        Encryption settings.
    key_management : str
        Key management strategy.
    credentials : :class:`~marketmind.config.CredentialsConfig`
        API credentials.
    compliance : :class:`~marketmind.config.ComplianceConfig`
        Compliance settings.
    """

    encryption: EncryptionConfig
    key_management: str
    credentials: CredentialsConfig
    compliance: ComplianceConfig

class RiskManagementConfig(BaseModel):
    """Configuration for risk management in backtesting.

    Attributes
    ----------
    stop_loss : float
        Stop-loss threshold.
    max_drawdown : float
        Maximum allowed drawdown.
    """

    stop_loss: float
    max_drawdown: float

class DateRangeConfig(BaseModel):
    """Configuration for backtesting date range.

    Attributes
    ----------
    start : str
        Start date in 'YYYY-MM-DD' format.
    end : str
        End date in 'YYYY-MM-DD' format.
    """

    start: str
    end: str

class PositionSizingConfig(BaseModel):
    """Configuration for position sizing in backtesting.

    Attributes
    ----------
    method : Literal['fixed', 'kelly', 'volatility']
        Position sizing method. Options include :term:`Kelly Criterion`, fixed, or
        volatility-based.
    """

    method: Literal['fixed', 'kelly', 'volatility']

class Backtesting(BaseModel):
    """Configuration for the backtesting engine.

    Attributes
    ----------
    initial_capital : float
        Starting capital for backtesting.
    transaction_cost_rate : float
        Rate of transaction costs.
    slippage_rate : float
        Rate of slippage.
    strategy_list : list[str]
        List of strategies to test.
    risk_management : :class:`~marketmind.config.RiskManagementConfig`
        Risk management settings.
    date_range : :class:`~marketmind.config.DateRangeConfig`
        Date range for backtesting.
    performance_metrics : list[str]
        Metrics to evaluate performance.
    position_sizing : :class:`~marketmind.config.PositionSizingConfig`
        Position sizing settings.
    benchmark_index : str
        Benchmark index.
    backtest_frequency : str
        Frequency of backtesting.
    """

    initial_capital: float
    transaction_cost_rate: float
    slippage_rate: float
    strategy_list: List[str]
    risk_management: RiskManagementConfig
    date_range: DateRangeConfig
    performance_metrics: List[str]
    position_sizing: PositionSizingConfig
    benchmark_index: str
    backtest_frequency: str

class DistributedProcessing(BaseModel):
    """Configuration for distributed processing.

    Attributes
    ----------
    framework : str
        Framework to use.
    num_workers : int
        Number of workers.
    memory_per_worker : str
        Memory allocation per worker.
    cluster_type : str
        Type of cluster.
    min_rows_for_distributed : int, default ``1000``
        Minimum rows to trigger distributed processing.
    """

    framework: str
    num_workers: int
    memory_per_worker: str
    cluster_type: str
    min_rows_for_distributed: int = 1000

class Config(BaseModel):
    """Root configuration for the MarketMind platform.

    This model defines the entire configuration structure loaded from
    'config.yaml'.

    Attributes
    ----------
    version : str
        Configuration version.
    schema_uri : str
        URI of the JSON schema for validation.
    data_source : :class:`~marketmind.config.DataSource`
        Main data source settings.
    alternative_data : :class:`~marketmind.config.AlternativeData` | None, default None
        Non-traditional data sources.
    market_data_sources : list[dict[str, Any]], default ``[]``
        List of additional market data sources.
    cleaning : :class:`~marketmind.config.Cleaning`
        Data cleaning settings.
    preprocessing : :class:`~marketmind.config.Preprocessing`
        Preprocessing settings.
    streaming : :class:`~marketmind.config.Streaming`
        Streaming pipeline settings.
    error_handling : :class:`~marketmind.config.ErrorHandling`
        Error handling policies.
    model : :class:`~marketmind.config.Model`
        Model training and inference settings.
    logging : :class:`~marketmind.config.Logging`
        Logging and metrics settings.
    security : :class:`~marketmind.config.Security`
        Security settings.
    backtesting : :class:`~marketmind.config.Backtesting`
        Backtesting engine settings.
    distributed_processing : :class:`~marketmind.config.DistributedProcessing`
        Distributed processing settings.
    real_time_market_data : :class:`~marketmind.config.RealTimeMarketDataConfig` | None, default None
        Real-time market data settings.
    anomaly_detection : :class:`~marketmind.config.AnomalyDetectionConfig`, default a default instance of :class:`~marketmind.config.AnomalyDetectionConfig`
        Anomaly detection settings.

    Examples
    --------
    >>> if TYPE_CHECKING:
    ...     import erdantic as erd
    ...     erd.draw(Config)
    """

    version: str
    schema_uri: str
    data_source: DataSource
    alternative_data: Optional[AlternativeData] = Field(default_factory=AlternativeData)
    market_data_sources: List[Dict[str, Any]] = Field(default_factory=list)
    cleaning: Cleaning
    preprocessing: Preprocessing
    streaming: Streaming
    error_handling: ErrorHandling
    model: Model
    logging: Logging
    security: Security
    backtesting: Backtesting
    distributed_processing: DistributedProcessing
    real_time_market_data: Optional[RealTimeMarketDataConfig] = Field(default_factory=RealTimeMarketDataConfig)
    anomaly_detection: AnomalyDetectionConfig = Field(default_factory=AnomalyDetectionConfig)

def resolve_env_vars(data: Any) -> Any:
    """Recursively replace '${VAR}' placeholders with environment variable values.
    :noindex:

    Parameters
    ----------
    data : Any
        Nested structure (dict, list, scalar) to process.

    Returns
    -------
    Any
        Data with environment variables expanded.
    """

def load_config(path: Optional[Path] = None) -> Config:
    """Load and validate the configuration from a YAML file.

    Parameters
    ----------
    path : Path | None, default None
        Path to the YAML file. If None, uses CONFIG_PATH.

    Returns
    -------
    Config
        Validated configuration object.

    Raises
    ------
    FileNotFoundError
        If the YAML or schema file is not found.
    ConfigValidationError
        If validation fails.
    """

config: Optional[Config]
"""Module-level singleton holding the loaded configuration."""

def get_config() -> Config:
    """Retrieve the cached configuration, loading it if necessary.

    Returns
    -------
    Config
        The current configuration object.
    """

__all__ = [
    'logger',
    'BASE',
    'CONFIG_PATH',
    'SCHEMA_PATH',
    'RSIConfig',
    'MACDConfig',
    'ATRConfig',
    'BollingerBandsConfig',
    'VWAPConfig',
    'TechnicalIndicators',
    'ClipExtremes',
    'NormalizationConfig',
    'SentimentConfig',
    'ESGNormalizedConfig',
    'CalendarConfig',
    'CustomFeatures',
    'AnomalyDetectionConfig',
    'Preprocessing',
    'Streaming',
    'RetryPolicy',
    'ValidationThresholds',
    'Fallback',
    'Alerting',
    'ErrorHandling',
    'RateLimitConfig',
    'CSVConfig',
    'InfluxDBConfig',
    'DataSource',
    'TwitterConfig',
    'AlpacaConfig',
    'ESGConfig',
    'BloombergConfig',
    'WeatherConfig',
    'FREDConfig',
    'AlternativeData',
    'InteractiveBrokersConfig',
    'RealTimeMarketDataConfig',
    'ModelArchitecture',
    'Model',
    'Cleaning',
    'FileOutputConfig',
    'InfluxDBOutputConfig',
    'OutputsConfig',
    'MetricAggregationConfig',
    'DashboardConfig',
    'Logging',
    'EncryptionConfig',
    'CredentialsConfig',
    'DataAnonymizationConfig',
    'ComplianceConfig',
    'Security',
    'RiskManagementConfig',
    'DateRangeConfig',
    'PositionSizingConfig',
    'Backtesting',
    'DistributedProcessing',
    'Config',
    'resolve_env_vars',
    'load_config',
    'get_config',
    'config',
]