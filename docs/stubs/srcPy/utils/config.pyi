from typing import Any as Incomplete
from pathlib import Path
from srcPy.ops.mm_logkit import get_logger as get_logger
from srcPy.utils.dependency_manager import ensure_influxdb_client as ensure_influxdb_client, ensure_polars as ensure_polars, ensure_pydantic as ensure_pydantic
from srcPy.utils.exceptions import ConfigValidationError as ConfigValidationError
from typing import Any, Literal, Mapping

BaseModel: Incomplete
Field: Incomplete
ValidationError: Incomplete
ConfigDict: Incomplete
model_validator: Incomplete
logger: Incomplete
BASE: Path
DEFAULT_CONFIG_PATH: Path
DEFAULT_SCHEMA_PATH: Path
CONFIG_PATH: Path | None
SCHEMA_PATH: Path | None

class Section(BaseModel):
    """section class."""
    model_config: Incomplete
    def validate_section(self) -> None: ...

class _CSVSourceModel(Section):
    """csv source model class."""
    type: Literal['csv']
    path: str
    chunksize: int
    use_dask: bool
    compression: str | None
    data_format: str

class _InfluxSourceModel(Section):
    """influx source model class."""
    type: Literal['influxdb']
    host: str
    port: int
    token: str
    org: str
    bucket: str
    query: str

class _PolarsMixin:
    """polars mixin class."""
    def to_polars(self, **read_kwargs) -> Any: ...

class CSVSource(_PolarsMixin, _CSVSourceModel):
    """csv source class."""
    def to_polars(self, **read_kwargs) -> Any: ...

class InfluxSource(_PolarsMixin, _InfluxSourceModel):
    """influx source class."""
    def to_polars(self, **read_kwargs) -> Any: ...

DataSource: Incomplete

class RSI(Section):
    """rsi class."""
    enabled: bool
    window: int
    fillna_method: str
    def validate_section(self) -> None: ...

class MACD(Section):
    """macd class."""
    enabled: bool
    fast_period: int
    slow_period: int
    signal_period: int
    fillna_method: str
    def validate_section(self) -> None: ...

class ATR(Section):
    """atr class."""
    enabled: bool
    window: int
    fillna_method: str

class Bollinger(Section):
    """bollinger class."""
    enabled: bool
    window: int
    std_dev: float
    fillna_method: str

class VWAP(Section):
    """vwap class."""
    enabled: bool
    reset_period: str
    fillna_method: str

class TechnicalIndicators(Section):
    """technical indicators class."""
    rsi: RSI | None
    macd: MACD | None
    atr: ATR | None
    vwap: VWAP | None
    bollinger_bands: Bollinger | None
    extra_indicators: dict[str, dict[str, Any]]
    def validate_section(self) -> None: ...

class Clip(Section):
    """clip class."""
    min: float
    max: float

class Normalization(Section):
    """normalization class."""
    method: str
    rolling_window: int
    clip_extremes: Clip
    def validate_section(self) -> None: ...

class Calendar(Section):
    """calendar class."""
    enabled: bool
    day_of_week: bool
    holidays: list[str]
    timezones: list[str]
    def is_holiday(self, dt) -> bool: ...

class Sentiment(Section):
    """sentiment class."""
    enabled: bool
    source: str
    sentiment_model: str

class ESGNormalized(Section):
    """esg normalized class."""
    enabled: bool
    method: str

class CustomFeatures(Section):
    """custom features class."""
    sentiment: Sentiment | None
    esg_normalized: ESGNormalized | None

class Preprocessing(Section):
    """preprocessing class."""
    technical_indicators: TechnicalIndicators
    normalization: Normalization
    custom_features: CustomFeatures
    calendar_features: Calendar
    steps: list[dict[str, Any]]
    step_macros: dict[str, dict[str, Any]]
    def validate_section(self) -> None: ...
    def expand_macros(self) -> None: ...

class CleaningCombo(Section):
    """cleaning combo class."""
    name: str
    when: dict[str, Any] | None

class Cleaning(Section):
    """cleaning class."""
    combos: list[CleaningCombo]
    missing_values: dict[str, Any]
    outliers: dict[str, Any]
    denoising: dict[str, Any]

class Streaming(Section):
    """streaming class."""
    batch_size: int
    update_interval_seconds: int
    buffer_size: int
    max_latency_ms: int
    buffer_retention_seconds: int
    event_triggers: dict[str, str]
    priority_queue: str
    failure_recovery: dict[str, Any]
    sync_interval_seconds: int

class RetryPolicy(Section):
    """retry policy class."""
    max_attempts: int
    initial_backoff_seconds: int
    max_backoff_seconds: int
    retry_strategy: str

class ValidationThresholds(Section):
    """validation thresholds class."""
    max_missing_ratio: float
    max_outlier_ratio: float

class Fallback(Section):
    """fallback class."""
    twitter: str
    esg: str
    data_source: str

class Alerting(Section):
    """alerting class."""
    enabled: bool
    channel: str
    critical_failures: list[str]
    alert_severity: list[str]

class ErrorHandling(Section):
    """error handling class."""
    retry_policy: RetryPolicy
    validation_thresholds: ValidationThresholds
    fallback: Fallback
    alerting: Alerting
    fallback_timeout_seconds: int

class ModelArchitecture(Section):
    """model architecture class."""
    num_layers: int
    hidden_size: int
    dropout: float

class Model(Section):
    """model class."""
    model_type: str
    architecture: ModelArchitecture
    sequence_length: int
    prediction_horizon: int
    feature_list: list[str]
    training_device: str
    model_checkpoint: dict[str, int]
    feature_importance: dict[str, str]
    onnx_export: dict[str, Any]

class FileOutput(Section):
    """file output class."""
    enabled: bool
    path: str
    rotation: str

class InfluxDBOutput(Section):
    """influx db output class."""
    enabled: bool
    host: str
    port: int
    token: str
    org: str
    bucket: str

class Outputs(Section):
    """outputs class."""
    console: bool
    file: FileOutput
    influxdb: InfluxDBOutput

class MetricAggregation(Section):
    """metric aggregation class."""
    aggregation_window_seconds: int

class DashboardConfig(Section):
    """Configuration for dashboard."""
    grafana_url: str

class Logging(Section):
    """logging class."""
    level: str
    outputs: Outputs
    metrics_report_interval_seconds: int
    custom_metrics: list[str]
    model_metrics: list[str]
    metric_aggregation: MetricAggregation
    log_sampling_rate: float
    dashboard_config: DashboardConfig

class Encryption(Section):
    """encryption class."""
    at_rest: bool
    in_transit: bool
    encryption_algorithm: str

class Credentials(Section):
    """credentials class."""
    twitter_api_key: str | None
    esg_api_key: str | None
    fred_api_key: str | None
    bloomberg_api_key: str | None
    weather_api_key: str | None
    alpha_vantage_api_key: str | None
    def validate_secrets(self) -> Credentials: ...

class DataAnonymization(Section):
    """data anonymization class."""
    anonymize_pii: bool

class Compliance(Section):
    """compliance class."""
    audit_log: bool
    retention_days: int
    audit_frequency_days: int
    data_anonymization: DataAnonymization

class Security(Section):
    """security class."""
    encryption: Encryption
    key_management: str
    credentials: Credentials
    compliance: Compliance

class RiskManagement(Section):
    """risk management class."""
    stop_loss: float
    max_drawdown: float

class DateRange(Section):
    """date range class."""
    start: str
    end: str

class PositionSizing(Section):
    """position sizing class."""
    method: str

class Backtesting(Section):
    """backtesting class."""
    initial_capital: float
    transaction_cost_rate: float
    slippage_rate: float
    strategy_list: list[str]
    risk_management: RiskManagement
    date_range: DateRange
    performance_metrics: list[str]
    position_sizing: PositionSizing
    benchmark_index: str
    backtest_frequency: str

class DistributedProcessing(Section):
    """distributed processing class."""
    framework: str
    num_workers: int
    memory_per_worker: str
    cluster_type: str
    min_rows_for_distributed: int

class InteractiveBrokers(Section):
    """interactive brokers class."""
    host: str
    port: int
    client_id: int
    subscription_topics: list[str]
    api_key: str
    endpoint: str
    connection_timeout_seconds: int
    priority: int
    what_to_show: str
    use_rth: bool
    format_date: int

class Alpaca(Section):
    """alpaca class."""
    api_key: str | None
    secret_key: str
    endpoint: str

class RealTimeMarketData(Section):
    """real time market data class."""
    interactive_brokers: InteractiveBrokers | None
    alpaca: Alpaca | None

class RateLimit(Section):
    """rate limit class."""
    per_minute: int | None
    max_calls_per_window: int | None
    window_seconds: int | None

class ExternalAPISource(Section):
    """external api source class."""
    base_url: str
    api_key: str | None
    authentication_type: str | None
    endpoints: dict[str, str]
    default_params: dict[str, str]
    rate_limit: RateLimit | None
    timeout_seconds: int
    cache_duration_hours: int
    data_resolution: str | None
    def validate_section(self) -> None: ...

class Twitter(Section):
    """twitter class."""
    base_url: str
    bearer_token: str
    authentication_type: str
    endpoints: dict[str, str]
    default_params: dict[str, Any]
    rate_limit: RateLimit
    retry_after_header: str
    timeout_seconds: int
    cache_duration_hours: int
    data_resolution: str
    api_key: str | None

class ESG(Section):
    """esg class."""
    base_url: str
    api_key: str
    authentication_type: str
    endpoints: dict[str, str]
    default_params: dict[str, str]
    timeout_seconds: int
    cache_duration_hours: int
    data_resolution: str

class FRED(ExternalAPISource): ...
class Bloomberg(ExternalAPISource): ...
class Weather(ExternalAPISource): ...

class AlternativeData(Section):
    """alternative data class."""
    twitter: Twitter | None
    alpaca: Alpaca | None
    esg: ESG | None
    fred: FRED | None
    bloomberg: Bloomberg | None
    weather: Weather | None

class AnomalyDetection(Section):
    """anomaly detection class."""
    enabled: bool
    method: str | None
    params: dict[str, Any] | None

class PipelineConfig(BaseModel):
    """Configuration for pipeline."""
    model_config: Incomplete
    version: str
    schema_uri: str
    data_source: DataSource
    preprocessing: Preprocessing
    cleaning: Cleaning
    streaming: Streaming
    error_handling: ErrorHandling
    model: Model
    logging: Logging
    security: Security
    backtesting: Backtesting
    distributed_processing: DistributedProcessing
    alternative_data: AlternativeData
    market_data_sources: list[dict[str, Any]]
    real_time_market_data: RealTimeMarketData
    anomaly_detection: AnomalyDetection
    includes: list[str]
    profiles: dict[str, dict[str, Any]]
    active_profiles: list[str]
    list_merge_strategy: str
    def merged(self, *overlays: Mapping[str, Any], list_strategy: str | None = None) -> PipelineConfig: ...
    def with_profile(self, *profile_names: str) -> PipelineConfig: ...

def load_config(path: Path | None = None, schema_path: Path | None = None, *, apply_env: bool = True, env_prefix: str = 'MARKETMIND__', list_strategy: str = 'replace') -> PipelineConfig: ...
def get_config(path: Path | None = None) -> PipelineConfig: ...
def reload_config(path: Path | None = None) -> PipelineConfig: ...
def reset_config_cache() -> None: ...
def get_runtime_config() -> PipelineConfig: ...
def get_dataset(**kwargs) -> Any: ...
def validate_runtime_requirements(conf: PipelineConfig | None = None) -> list[str]: ...