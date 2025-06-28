(glossary)=
# Glossary

This glossary defines key terms, acronyms, and domain‑specific concepts used in the **MarketMind** project, covering market prediction, analytics, system design, and development workflows.  If you encounter an unfamiliar term in the docs, look here first.

---

## A

**Access Controls** *(Placeholder)*  
Mechanisms to restrict access to MarketMind resources based on user roles or permissions.  
*See `security_practices.md` for details.*

**API Endpoint** *(Placeholder)*  
A specific route or URL in the MarketMind API for interacting with the platform (e.g., submitting predictions).  
*See `api_reference.md` for specifics.*

**Audit Trail** *(Placeholder)*  
A record of actions or changes in MarketMind for compliance and auditing purposes.  
*See `regulatory_compliance.md` for details.*

**Augmented Dickey‑Fuller (ADF) Test**  
A statistical test for stationarity in a time series, used to determine if a series has a unit root (non‑stationary). A low *p*-value (<0.05) suggests stationarity.  
*See `stat_tests.py` and `architecture.md` for usage in data preprocessing.*

**ATR – Average True Range**  
A volatility indicator based on recent high–low trading ranges that quantifies market volatility.  
*Tagged in `ATRConfig`.*

**Autoencoder**  
An unsupervised neural network that learns to reconstruct its input; useful for anomaly detection when reconstruction error signals outliers.  
*Tagged in `AnomalyDetectionConfig`.*

---

## B

**Bidirectional LSTM**  
A Long Short‑Term Memory (LSTM) model that processes sequences in both forward and backward directions, improving context capture for predictions.  
*See `lstm_classifier.py` for implementation.*

**Bollinger Bands**  
A volatility indicator consisting of an upper and lower band plotted at *k* standard deviations above and below a simple moving average (SMA).  
*Tagged in `BollingerBandsConfig`.*

---

## C

**CI/CD Pipeline** *(Placeholder)*  
The automated process for building, testing, and deploying MarketMind code or documentation, often using GitHub Actions.  
*See GitHub Actions workflow files.*

**Coding Standard** *(Placeholder)*  
Guidelines for writing consistent, readable code in MarketMind, including naming conventions and docstring formats.  
*See `contributors/coding_standards.md`.*

**Cointegration**  
A statistical property where multiple non‑stationary time series share a stable long‑term relationship, tested using Johansen’s cointegration test.  
*See `stat_tests.py` for implementation.*

---

## D

**Data Pipeline** *(Placeholder)*  
The sequence of processes for ingesting, transforming, and feeding data into MarketMind’s prediction models.  
*See `architecture.md` for details.*

---

## E

**Environment Setup** *(Placeholder)*  
The process of configuring a development or runtime environment for MarketMind, including Python, dependencies, and API keys.  
*See `getting_started.md` and `contributors/onboarding.md`.*

**ESG – Environmental, Social, Governance**  
A set of non‑financial metrics (environmental impact, social responsibility, and corporate governance) used to evaluate a company’s sustainability and ethical impact.  
*Tagged in `ESGConfig` and `ESGNormalizedConfig`.*

**Exponential Back‑off**  
A retry strategy where the delay between consecutive attempts grows geometrically (e.g., 1 s, 2 s, 4 s…).  
*Tagged in `RetryPolicy.retry_strategy`.*

---

## F

**FinBERT**  
A BERT language model fine‑tuned on financial corpora for domain‑specific sentiment analysis.  
*Tagged in `SentimentConfig.sentiment_model`.*

**Furo**  
A modern, clean Sphinx theme used for MarketMind’s documentation, enhancing readability and navigation.  
*See `conf.py` for configuration.*

---

## G

**Git Workflow** *(Placeholder)*  
The process for contributing code to MarketMind, including branching, commits, and pull requests.  
*See `contributors/contribution_workflow.md`.*

**Granger Causality Test**  
A statistical test to determine if one time series can predict another, used in MarketMind for feature selection. A low *p*-value suggests causality.  
*See `stat_tests.py` for implementation.*

---

## I

**InfluxDB**  
A high‑performance time‑series database used for storing and querying high‑frequency market data.  
*Tagged in `InfluxDBConfig`.*

**InvalidInputError**  
A custom exception in MarketMind raised when input data fails validation (e.g., mismatched indices in statistical tests).  
*See `stat_tests.py` and `srcPy/utils/exceptions.py`.*

**Isolation Forest**  
A tree‑based algorithm that isolates anomalies by recursively partitioning data; points that require fewer splits are considered outliers.  
*Tagged in `AnomalyDetectionConfig.method`.*

---

## K

**Kelly Criterion**  
A position‑sizing formula that allocates capital proportionally to the edge and odds of a trade, maximising long‑run growth rate.  
*Tagged in `PositionSizingConfig.method`.*

**KPSS Test**  
A statistical test for level stationarity in a time series, complementing the ADF test. A low *p*-value suggests non‑stationarity.  
*See `stat_tests.py`.*

---

## L

**Linear Back‑off**  
A retry strategy where the delay between consecutive attempts increases by a fixed increment (e.g., 1 s, 2 s, 3 s…).  
*Tagged in `RetryPolicy.retry_strategy`.*

**LSTM (Long Short‑Term Memory)**  
A recurrent neural network architecture used in MarketMind for sequence modeling, capturing temporal dependencies in market data.  
*See `lstm_classifier.py` for the `LSTMClassifier` implementation.*

**Ljung‑Box Test**  
A statistical test for autocorrelation in time series residuals, used to evaluate model fit in MarketMind. A low *p*-value indicates autocorrelation.  
*See `stat_tests.py`.*

---

## M

**MACD – Moving Average Convergence Divergence**  
A trend‑following momentum indicator derived from the difference between a fast and a slow exponential moving average (EMA).  
*Tagged in `MACDConfig`.*

**MARKETMIND_API_KEY** *(Placeholder)*  
An environment variable for authenticating with MarketMind’s API or services.  
*See `getting_started.md` for setup.*

**MyST Parser**  
A Sphinx extension enabling Markdown support in MarketMind’s documentation, used for files like `index.md`.  
*See `conf.py` and [MyST‑Parser documentation](https://myst-parser.readthedocs.io/).*  

---

## O

**OHLC**  
A bar or candlestick representation of price containing the {**O**pen, **H**igh, **L**ow, **C**lose} values for a given interval.  
*Tagged in `CSVConfig.data_format`.*

---

## P

**Prediction Engine** *(Placeholder)*  
The core component of MarketMind responsible for generating market predictions using models like `LSTMClassifier`.  
*See `architecture.md` and `tutorials/basic_prediction.ipynb`.*

**Pull Request** *(Placeholder)*  
A proposed change to MarketMind’s codebase, submitted via GitHub for review and merging.  
*See `contributors/contribution_workflow.md`.*

---

## R

**Regulatory Standard** *(Placeholder)*  
A compliance requirement (e.g., SEC, GDPR) that MarketMind adheres to for financial operations.  
*See `regulatory_compliance.md`.*

**RSI – Relative Strength Index**  
A momentum oscillator that measures recent price‑change magnitude to identify overbought or oversold conditions.  
*Tagged in `RSIConfig`.*

---

## S

**Sphinx**  
The documentation generator used for MarketMind’s documentation, rendering Markdown and reStructuredText into HTML.  
*See `conf.py` and [Sphinx documentation](https://www.sphinx-doc.org/).*  

**Structured Logging**  
A logging approach in MarketMind that attaches key‑value pairs to log entries, enabling machine‑readable, queryable logs.  
*See `logger.py` for implementation.*

**Sentiment (financial)**  
The aggregated mood or attitude inferred from news, social‑media, or other text sources toward a financial asset or market.  
*Tagged in `SentimentConfig`.*

---

## T

**Threat Model** *(Placeholder)*  
A structured analysis of potential security threats to MarketMind and their mitigations.  
*See `internal/threat_model.md`.*

**Tick Data**  
Granular data capturing every individual trade or quote update for an instrument.  
*Tagged in `CSVConfig.data_format`.*

---

## V

**Validation**  
The process of checking input data for correctness, used in MarketMind’s statistical tests and utilities.  
*See `stat_tests.py` and `srcPy/utils/validators.py`.*

**VADER**  
*Valence Aware Dictionary and sEntiment Reasoner* – a rule‑based model for general‑purpose sentiment analysis, particularly well‑suited to social‑media text.  
*Tagged in `SentimentConfig.sentiment_model`.*

**Value‑at‑Risk (VaR)**  
A risk metric that estimates the maximum expected loss over a specified horizon at a given confidence level.  
*Tagged in `RiskManagementConfig`.*

**VWAP – Volume‑Weighted Average Price**  
The average price of a security weighted by traded volume, calculated cumulatively throughout the trading session.  
*Tagged in `VWAPConfig`.*

---

## Z

**Z‑score**  
A standardised measure indicating how many standard deviations an observation is from the mean; used for anomaly detection and normalisation.  
*Tagged in `AnomalyDetectionConfig.method`.*

---

*Last updated: {{ autogenerated on build }}*

