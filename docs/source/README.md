# MarketMind ![Version](https://img.shields.io/badge/version-1.13.1-blue) [![Python](https://img.shields.io/badge/Python-3.12.9-3776AB?style=flat-square&logo=python)](https://www.python.org/) [![C++20](https://img.shields.io/badge/C%2B%2B-20-00599C?style=flat-square&logo=cplusplus)](https://isocpp.org/) [![CUDA](https://img.shields.io/badge/CUDA-12.9-76B900?style=flat-square&logo=nvidia)](https://developer.nvidia.com/cuda-toolkit) ![License](https://img.shields.io/badge/license-Proprietary-red) [![Build Status](https://img.shields.io/github/actions/workflow/status/Nalakram/QuantAIvus/ci.yml?branch=main)](https://github.com/Nalakram/QuantAIvus/actions) [![codecov](https://codecov.io/gh/MindForgeLabs/MarketMind/graph/badge.svg?token=LIJZD4YCFB)](https://codecov.io/gh/MindForgeLabs/MarketMind) [![Java 21](https://img.shields.io/badge/Java-21-007396?style=flat-square&logo=openjdk)](https://www.oracle.com/java/technologies/downloads/#java21) [![Spring](https://img.shields.io/badge/Spring-3.5.0-6DB33F?style=flat-square&logo=spring&logoColor=white)](https://spring.io/) ![JavaFX 21](https://img.shields.io/badge/JavaFX-21-3873B3?style=flat-square)

 [![Windows Supported](https://custom-icon-badges.demolab.com/badge/Windows-Supported-0078D6?logo=windows11&logoColor=white)](https://www.microsoft.com/windows) [![Linux](https://img.shields.io/badge/Linux-Tested-FCC624?style=flat-square&logo=linux)](https://kernel.org/) [![Read the Docs](https://img.shields.io/badge/docs-Read_the_Docs-8CA1AF?logo=readthedocs)](https://marketmind-docs.readthedocs.io/en/latest/) ![Status](https://img.shields.io/badge/status-development-FFA500?style=flat-square)

![MarketMind Banner](https://raw.githubusercontent.com/Nalakram/marketmind-docs/main/docs/source/images/banner1.png)

MarketMind is an advanced algorithmic trading platform that provides automated, high-frequency trading capabilities with built-in analytics and risk 
controls. It ingests real-time market data and news (using NLP pipelines) and applies hybrid deep-learning models (e.g. multi-head Transformer layers 
combined with LSTM or Temporal Convolutional Networks) to generate continuous price and trend forecasts. 
Its trading engine can automatically execute buy/sell orders based on these model signals, applying configurable risk management (e.g. stop-loss, 
take-profit) to protect capital. The system is optimized for ultra-low-latency use cases and employs a multilingual architecture (performance-critical modules in C++, modeling and orchestration in Python, with Java 
components for UI and integration). 

MarketMind’s upcoming and planned features now include an Informer model for efficient long-sequence forecasting, graph neural networks (GNNs) to capture 
dynamic relationships among assets, hidden Markov models (HMMs) for identifying latent market regimes, and Granger causality tests to find predictive 
leading indicators in time series. The platform also emphasizes interpretability: it computes SHAP values to explain model predictions, assigning importance 
scores to each input feature.

---

## Table of Contents
- [Features](#features)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Versioning](#versioning)
- [Copyright](#copyright)

---

## Features

| **Category**     | **Feature**                  | **Summary**                                        |
|------------------|-----------------------------|----------------------------------------------------|
| 🟦 Functional    | Automated Trading            | Advanced models drive real-time, auto-executed trades with built-in risk controls. |
| 🟦 Functional    | High-Frequency & Multi-Asset | Low-latency trading for stocks, ETFs, and crypto.  |
| 🟦 Functional    | Analytics & Dashboard        | Interactive GUI with live forecasts, sentiment, and alerts. |
| 🟦 Functional    | Data Integration             | Unified market, news, and social data ingestion.   |
| 🟩 Technical     | Hybrid Deep Learning         | Ensemble of neural nets (e.g., Transformer, LSTM, GNN) for price and trend forecasts. |
| 🟩 Technical     | Explainable AI               | SHAP-based interpretability and feature importance.|
| 🟩 Technical     | Flexible Architecture        | Multi-language codebase (C++, Python, Java), supports TensorFlow & ONNX. |
| 🟩 Technical     | Advanced Modeling            | Informer, HMM, Granger causality for deeper insights and strategy. |

---

## Project Structure

<details>
<summary><strong>View Full Directory Tree</strong></summary>

```
MarketMind/
├── srcPy/           # Python: data pipeline, ML, trading logic
├── cpp/             # C++ backend: high-performance inference
├── src/
│   ├── main/
│   │   ├── java/        # JavaFX UI & business logic
│   │   └── resources/   # UI layouts (FXML), CSS, configs
│   └── test/            # Java tests & test resources
├── data/            # Datasets: raw, processed, config
├── models/          # Trained models, metadata, evaluation
├── tests/           # Python, C++, Java, and integration tests
├── deployment/      # Docker, InfluxDB, deployment configs
├── docs/            # Documentation, guides, images
├── scripts/         # Build & helper scripts
├── libs/            # Native libraries (e.g., JNI)
├── pom.xml          # Maven config
├── requirements.txt # Python dependencies
├── CMakeLists.txt   # C++ build config
├── README.md, LICENSE, .gitignore, etc.
```

</details>

### Key Folders

* **srcPy/** – Python package: data, ML, and trading logic
* **cpp/** – C++ backend for inference (gRPC/JNI)
* **src/main/java/** – JavaFX GUI, business logic
* **data/** – Datasets and config
* **models/** – Saved/trained models and metadata
* **tests/** – Comprehensive test suites (all languages)
* **deployment/** – Deployment configs (Docker, cloud, DB)
* **docs/** – Documentation and guides

### Top-level Files

* `pom.xml` – Maven (Java & C++ integration)
* `requirements.txt` – Python dependencies
* `CMakeLists.txt` – C++ build
* `.gitignore`, `LICENSE`, `README.md` – Standard repo files

---

## Prerequisites

| Requirement | Version | Notes |
|:---|:---:|:---|
| ![Python](https://img.shields.io/badge/Python-3.12.9-3776AB?logo=python) | 3.12.9 | ML pipelines & analytics |
| ![C++](https://img.shields.io/badge/C++-20-00599C?logo=cplusplus) | C++20 (CUDA 12.9) | High-performance inference |
| ![Java 21](https://img.shields.io/badge/Java-21-FFA500?style=flat-square&logo=openjdk) | Java 21 | User interface & integration |
| ![NVIDIA](https://img.shields.io/badge/NVIDIA-GPU-76B900?logo=nvidia) | CUDA 12.9+ | GPU recommended for speed |

---

## Documentation

Comprehensive documentation is provided in ReadTheDocs online docs site.
- Key documents include:
  - Getting Started Guide: Setup instructions, installation steps, and a quickstart walkthrough.
  - User Guide: Detailed walkthrough of the trading GUI and how to configure strategies.
  - Developer Guide: Information on project structure, coding standards, and how to extend modules.
  - API Reference: Auto-generated reference pages for all classes, methods, and configuration options (found under docs/api/).
  - Architecture & Design: Explanations of system architecture, data pipelines, and model designs.
  - Changelog: Version-by-version change log.
   
The hosted documentation site (ReadTheDocs) mirrors these files and provides search and navigation features. Users and developers are 
encouraged to consult the docs for configuration details and advanced topics.
See [Documentation](https://marketmind-docs.readthedocs.io/en/latest/index.html) for full documentation history.

---

## Versioning

MarketMind follows Semantic Versioning (MAJOR.MINOR.PATCH). New features that are backward-compatible increment the minor version, bug fixes increment the 
patch version, and any breaking changes would increment the major version. Each release has corresponding notes in the changelog.
See [Changelog](https://marketmind-docs.readthedocs.io/en/latest/CHANGELOG.html) for full changelog history.

---

## Copyright

MarketMind is proprietary software (© 2025 Mark Wuenschel. All rights reserved.). Its source code is not open-source. However, MarketMind relies on 
several third-party open-source libraries (e.g. NumPy, TensorFlow, ONNX Runtime, etc.) that are distributed under permissive licenses (such as MIT, BSD, or 
Apache 2.0). These permissive licenses explicitly allow incorporating the code into proprietary products without imposing copyleft restrictions prohibited 
without prior written permission from the copyright holder.
See full license details [here](https://marketmind-docs.readthedocs.io/en/latest/LICENSE.html).

See [Security Practices](https://marketmind-docs.readthedocs.io/en/latest/security_practices.html) for security policies.

