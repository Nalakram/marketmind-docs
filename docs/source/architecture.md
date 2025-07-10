# Architecture

## Data Pipeline Architecture Overview

![Data Pipeline Architecture](https://raw.githubusercontent.com/Nalakram/marketmind-docs/main/docs/source/images/DataPipelineV1.png)

This figure illustrates the end-to-end data flow for the **MarketMind AI** data pipeline, designed for robust, scalable ingestion, processing, and machine learning with heterogeneous market and alternative data sources.

---

### Key Components

#### Market Data
Ingests structured and unstructured data from diverse sources, including:
- **APIs:** AlphaVantage, CoinGecko
- **Files:** CSV, Parquet
- **Vendors:** Bloomberg, FRED, IBKR
- **Alt Data:** Twitter, Weather services  
This broad connectivity enables unified access to financial, economic, and sentiment signals.

#### Data Loader(s)
Modular, extensible loaders supporting both batch and real-time streaming workflows. Asynchronous and synchronous operation ensures resilience and high throughput.

#### Data Cleaning
Comprehensive, step-wise pipeline for:
- Missing value imputation
- Outlier handling
- Denoising
- Validation
- Anomaly detection
- Feature extraction (e.g., sentiment, calendar features)

#### Preprocessor
**_Highlighted in teal in the diagram to emphasize GPU acceleration._**  
Performs feature engineering, technical indicator calculation, and normalization using GPU-based libraries (`cuDF`, `cuML`), enabling scalable computation for large, complex datasets.

#### ML Dataset & DataLoader(s)
Outputs ML-ready, PyTorch-compatible datasets and loaders. Supports regression, classification, and multi-horizon forecasting.

#### Model Training/Serving
Trains and serves models (e.g., LSTM) on preprocessed data—enabling inference, forecasting, and analytics.

---

### Design Highlights

- **Modular, extensible architecture:** Clear boundaries between ingestion, cleaning, feature engineering, and model components.
- **GPU-accelerated preprocessing:** Scales efficiently with data size and complexity.
- **ML framework compatibility:** Native support for PyTorch and industry standards.
- **Production and research ready:** Suitable for both prototyping and deployment.

> **Note:**  
> The Preprocessor stage is visually highlighted to showcase the use of GPU acceleration—a key differentiator for efficient, large-scale time series processing.

