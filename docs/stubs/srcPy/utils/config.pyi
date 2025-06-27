from _typeshed import Incomplete
from datetime import datetime
from pathlib import Path
from pydantic import BaseModel
from srcPy.utils.exceptions import ConfigValidationError as ConfigValidationError
from srcPy.utils.logger import configure_logger as configure_logger, get_logger as get_logger
from typing import Any

logger: Incomplete
BASE: Path
CONFIG_PATH: Path
SCHEMA_PATH: Path

class RSIConfig(BaseModel):
    enabled: bool
    window: int
    fillna_method: str

class MACDConfig(BaseModel):
    enabled: bool
    fast_period: int
    slow_period: int
    signal_period: int
    fillna_method: str

class ATRConfig(BaseModel):
    enabled: bool
    window: int
    fillna_method: str

class BollingerBandsConfig(BaseModel):
    enabled: bool
    window: int
    std_dev: float
    fillna_method: str

class VWAPConfig(BaseModel):
    enabled: bool
    reset_period: str
    fillna_method: str

class TechnicalIndicators(BaseModel):
    rsi: RSIConfig | None
    macd: MACDConfig | None
    atr: ATRConfig | None
    vwap: VWAPConfig | None
    bollinger_bands: BollingerBandsConfig | None

class ClipExtremes(BaseModel):
    min: float
    max: float

class NormalizationConfig(BaseModel):
    method: str
    rolling_window: int
    clip_extremes: ClipExtremes

class SentimentConfig(BaseModel):
    enabled: bool
    source: str
    sentiment_model: str

class ESGNormalizedConfig(BaseModel):
    enabled: bool
    method: str

class CalendarConfig(BaseModel):
    enabled: bool
    day_of_week: bool
    holidays: list[str] | None
    timezones: list[str] | None
    def is_holiday(self, date: datetime) -> bool: ...

class CustomFeatures(BaseModel):
    sentiment: SentimentConfig | None
    esg_normalized: ESGNormalizedConfig | None

class AnomalyDetectionConfig(BaseModel):
    enabled: bool
    method: str | None
    params: dict | None

class Preprocessing(BaseModel):
    technical_indicators: TechnicalIndicators
    normalization: NormalizationConfig
    custom_features: CustomFeatures
    calendar_features: CalendarConfig

class Streaming(BaseModel):
    batch_size: int
    update_interval_seconds: int
    buffer_size: int
    max_latency_ms: int
    buffer_retention_seconds: int
    event_triggers: dict[str, str]
    priority_queue: str
    failure_recovery: dict[str, Any]
    sync_interval_seconds: int

class RetryPolicy(BaseModel):
    max_attempts: int
    initial_backoff_seconds: int
    max_backoff_seconds: int
    retry_strategy: str

class ValidationThresholds(BaseModel):
    max_missing_ratio: float
    max_outlier_ratio: float

class Fallback(BaseModel):
    twitter: str
    esg: str
    data_source: str

class Alerting(BaseModel):
    enabled: bool
    channel: str
    critical_failures: list[str]
    alert_severity: list[str]

class ErrorHandling(BaseModel):
    retry_policy: RetryPolicy
    validation_thresholds: ValidationThresholds
    fallback: Fallback
    alerting: Alerting
    fallback_timeout_seconds: int

class RateLimitConfig(BaseModel):
    per_minute: int | None
    max_calls_per_window: int | None
    window_seconds: int | None

class CSVConfig(BaseModel):
    path: str
    chunksize: int
    use_dask: bool
    compression: str
    data_format: str

class InfluxDBConfig(BaseModel):
    host: str
    port: int
    token: str
    org: str
    bucket: str
    query: str

class DataSource(BaseModel):
    type: str
    csv: CSVConfig | None
    influxdb: InfluxDBConfig | None

class TwitterConfig(BaseModel):
    base_url: str
    bearer_token: str
    authentication_type: str
    endpoints: dict[str, str]
    default_params: dict[str, Any]
    rate_limit: RateLimitConfig
    retry_after_header: str
    timeout_seconds: int
    cache_duration_hours: int
    data_resolution: str
    api_key: str | None

class AlpacaConfig(BaseModel):
    api_key: str | None
    secret_key: str
    endpoint: str

class ESGConfig(BaseModel):
    base_url: str
    api_key: str
    authentication_type: str
    endpoints: dict[str, str]
    default_params: dict[str, str]
    timeout_seconds: int
    cache_duration_hours: int
    data_resolution: str

class BloombergConfig(BaseModel):
    base_url: str
    api_key: str | None
    authentication_type: str | None
    endpoints: dict[str, str]
    default_params: dict[str, str]
    rate_limit: RateLimitConfig | None
    timeout_seconds: int
    cache_duration_hours: int
    data_resolution: str | None

class WeatherConfig(BaseModel):
    base_url: str
    api_key: str | None
    authentication_type: str | None
    endpoints: dict[str, str]
    default_params: dict[str, str]
    rate_limit: RateLimitConfig | None
    timeout_seconds: int
    cache_duration_hours: int
    data_resolution: str | None

class FREDConfig(BaseModel):
    base_url: str
    api_key: str | None
    authentication_type: str | None
    endpoints: dict[str, str]
    default_params: dict[str, str]
    rate_limit: RateLimitConfig | None
    timeout_seconds: int
    cache_duration_hours: int
    data_resolution: str | None

class AlternativeData(BaseModel):
    twitter: TwitterConfig | None
    alpaca: AlpacaConfig | None
    esg: ESGConfig | None
    fred: FREDConfig | None
    bloomberg: BloombergConfig | None
    weather: WeatherConfig | None

class InteractiveBrokersConfig(BaseModel):
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

class RealTimeMarketDataConfig(BaseModel):
    interactive_brokers: InteractiveBrokersConfig | None
    alpaca: AlpacaConfig | None

class ModelArchitecture(BaseModel):
    num_layers: int
    hidden_size: int
    dropout: float

class Model(BaseModel):
    model_type: str
    architecture: ModelArchitecture
    sequence_length: int
    prediction_horizon: int
    feature_list: list[str]
    training_device: str
    model_checkpoint: dict[str, int]
    feature_importance: dict[str, str]
    onnx_export: dict[str, Any]

class Cleaning(BaseModel):
    missing_values: dict[str, Any]
    outliers: dict[str, Any]
    denoising: dict[str, Any]

class FileOutputConfig(BaseModel):
    enabled: bool
    path: str
    rotation: str

class InfluxDBOutputConfig(BaseModel):
    enabled: bool
    host: str
    port: int
    token: str
    org: str
    bucket: str

class OutputsConfig(BaseModel):
    console: bool
    file: FileOutputConfig
    influxdb: InfluxDBOutputConfig

class MetricAggregationConfig(BaseModel):
    aggregation_window_seconds: int

class DashboardConfig(BaseModel):
    grafana_url: str

class Logging(BaseModel):
    level: str
    outputs: OutputsConfig
    metrics_report_interval_seconds: int
    custom_metrics: list[str]
    model_metrics: list[str]
    metric_aggregation: MetricAggregationConfig
    log_sampling_rate: float
    dashboard_config: DashboardConfig

class EncryptionConfig(BaseModel):
    at_rest: bool
    in_transit: bool
    encryption_algorithm: str

class CredentialsConfig(BaseModel):
    twitter_api_key: str | None
    esg_api_key: str | None
    fred_api_key: str | None
    bloomberg_api_key: str | None
    weather_api_key: str | None
    alpha_vantage_api_key: str | None

class DataAnonymizationConfig(BaseModel):
    anonymize_pii: bool

class ComplianceConfig(BaseModel):
    audit_log: bool
    retention_days: int
    audit_frequency_days: int
    data_anonymization: DataAnonymizationConfig

class Security(BaseModel):
    encryption: EncryptionConfig
    key_management: str
    credentials: CredentialsConfig
    compliance: ComplianceConfig

class RiskManagementConfig(BaseModel):
    stop_loss: float
    max_drawdown: float

class DateRangeConfig(BaseModel):
    start: str
    end: str

class PositionSizingConfig(BaseModel):
    method: str

class Backtesting(BaseModel):
    initial_capital: float
    transaction_cost_rate: float
    slippage_rate: float
    strategy_list: list[str]
    risk_management: RiskManagementConfig
    date_range: DateRangeConfig
    performance_metrics: list[str]
    position_sizing: PositionSizingConfig
    benchmark_index: str
    backtest_frequency: str

class DistributedProcessing(BaseModel):
    framework: str
    num_workers: int
    memory_per_worker: str
    cluster_type: str
    min_rows_for_distributed: int

class Config(BaseModel):
    version: str
    schema_uri: str
    data_source: DataSource
    alternative_data: AlternativeData | None
    market_data_sources: list[dict[str, Any]]
    cleaning: Cleaning
    preprocessing: Preprocessing
    streaming: Streaming
    error_handling: ErrorHandling
    model: Model
    logging: Logging
    security: Security
    backtesting: Backtesting
    distributed_processing: DistributedProcessing
    real_time_market_data: RealTimeMarketDataConfig | None
    anomaly_detection: AnomalyDetectionConfig

def resolve_env_vars(data: Any) -> Any: ...
def load_config(path: Path | None = None) -> Config: ...

config: Config | None

def get_config() -> Config: ...
