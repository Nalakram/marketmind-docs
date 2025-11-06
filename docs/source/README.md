# MarketMind ![Version](https://img.shields.io/badge/Version-2.0.0-8A2BE2) [![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=flat-square&logo=python)](https://www.python.org/) [![C++20](https://img.shields.io/badge/C%2B%2B-20-00599C?style=flat-square&logo=cplusplus)](https://isocpp.org/) [![CUDA](https://img.shields.io/badge/CUDA-12.9-76B900?style=flat-square&logo=nvidia)](https://developer.nvidia.com/cuda-toolkit) ![License](https://img.shields.io/badge/license-Proprietary-red) [![Build Status](https://img.shields.io/github/actions/workflow/status/Nalakram/QuantAIvus/ci.yml?branch=main)](https://github.com/Nalakram/QuantAIvus/actions) [![codecov](https://codecov.io/gh/MindForgeLabs/MarketMind/graph/badge.svg?token=LIJZD4YCFB)](https://codecov.io/gh/MindForgeLabs/MarketMind) [![Java 21](https://img.shields.io/badge/Java-21-007396?style=flat-square&logo=openjdk)](https://www.oracle.com/java/technologies/downloads/#java21) [![Spring](https://img.shields.io/badge/Spring-3.5.0-6DB33F?style=flat-square&logo=spring&logoColor=white)](https://spring.io/) ![JavaFX 21](https://img.shields.io/badge/JavaFX-21-3873B3?style=flat-square)
 [![Windows Supported](https://custom-icon-badges.demolab.com/badge/Windows-Supported-0078D6?logo=windows11&logoColor=white)](https://www.microsoft.com/windows) [![Linux](https://img.shields.io/badge/Linux-Tested-FCC624?style=flat-square&logo=linux)](https://kernel.org/) [![Read the Docs](https://img.shields.io/badge/docs-Read_the_Docs-8CA1AF?logo=readthedocs)](https://marketmind-docs.readthedocs.io/en/latest/) ![Status](https://img.shields.io/badge/status-development-FFA500?style=flat-square)

![MarketMind Banner](https://raw.githubusercontent.com/Nalakram/marketmind-docs/main/docs/source/images/banner1.png)

MarketMind is an advanced algorithmic trading platform that provides automated, high-frequency trading capabilities with built-in analytics and risk 
controls. It ingests real-time market data and news (using NLP pipelines) and applies hybrid deep-learning models (e.g. multi-head Transformer layers 
combined with LSTM or Temporal Convolutional Networks) to generate continuous price and trend forecasts. 
Its trading engine can automatically execute buy/sell orders based on these model signals, applying configurable risk management (e.g. stop-loss, 
take-profit) to protect capital. The system is optimized for ultra-low-latency use cases (MarketMind was originally conceived as “the first AI high 
frequency trading application”) and employs a multilingual architecture (performance-critical modules in C++, modeling and orchestration in Python, with Java 
components for UI and integration). 

MarketMind’s upcoming and planned features now include an Informer model for efficient long-sequence forecasting, graph neural networks (GNNs) to capture 
dynamic relationships among assets, hidden Markov models (HMMs) for identifying latent market regimes, and Granger causality tests to find predictive 
leading indicators in time series. The platform also emphasizes interpretability: it computes SHAP values to explain model predictions, assigning importance 
scores to each input feature.

---

## Table of Contents
- [What’s New in 3.1.1](#whats-new-in-311)
- [Architecture Overview](#architecture-overview)
- [Desktop UI & Services (JavaFX + Spring Boot)](#desktop-ui--services-javafx--spring-boot)
- [Tech Stack](#tech-stack)
- [Installation & Support Matrix](#installation--support-matrix)
- [3-step End-to-end Quickstart](#3-step-end-to-end-quickstart)
- [Project Structure](#project-structure)
- [Configuration](#configuration)
- [Testing & Gates](#testing--gates)
- [Performance (SLOs)](#performance-slos)
- [Security & Privacy (summary)](#security--privacy-summary)
- [Public Interfaces (at a glance)](#public-interfaces-at-a-glance)
- [Contributing](#contributing)
- [Versioning & Changelog](#versioning--changelog)
- [License](#license)

---

## What’s New in 3.1.1
**3.1.1** hardens the adaptive executor and test infra:
- Unified executor routing via `adaptive_executor.run(...)` (registry → classifier → dispatch).
- Surgical execute/skip policy with ENV passthrough and meta‑registry contract tests.
- Coverage/quality gates tightened and noise control for CI jobs.

<p>See <a href="https://marketmind-docs.readthedocs.io/en/latest/CHANGELOG.html">Changelog</a> for full changelog history.</p> 

---

## Architecture Overview

```
         ┌──────────────────────────┐         ┌──────────────────────────┐
         │        JavaFX UI         │◄──────► │      Python Orchestrator │
         │  (desktop client)        │   gRPC  │  (pipelines/engines)     │
         └────────────┬─────────────┘         └───────────┬──────────────┘
                      │ JNI/gRPC                         Registries/Plugins
                      ▼                                         │
         ┌──────────────────────────┐                           ▼
         │      C++ Inference       │◄────────────►  GPU/CPU Backends
         │ (ultra‑low latency)      │              (cuDF/CuPy/Polars/Torch)
         └──────────────────────────┘
```

<details>
<summary><strong>Mermaid: detailed pipeline (click to expand)</strong></summary>

```mermaid
flowchart LR
  Training[Training (PyTorch/TensorFlow)] -->|export| ONNX[Export ONNX]
  ONNX -->|optimize| TensorRT[TensorRT / TRT]
  TensorRT -->|bundle| ORT[ORT / TensorRT EP]
  ORT -->|serve| CppInf[C++ Inference (Triton/gRPC/ORT)]
  CppInf -->|gRPC/JNI| Python[Python Orchestrator]
  Python -->|gRPC| JavaFX[JavaFX UI & Spring Services]
```

</details>

**Key ideas**
- **Registry‑driven pipelines:** All cleaning/preprocessing steps are plug‑ins (e.g., `rename`, `cast`, `resample`, technical features, embeddings, topic modeling, explainability). Registries enable runtime composition and safe fallbacks.
- **Self‑evolving engine:** Adaptive strategies learn when to parallelize, reorder, or switch backends based on risk/telemetry.
- **GPU acceleration end‑to‑end:** cuDF → CuPy sliding windows → Torch tensors → model → TensorRT/ORT → C++ inference.
- **Explainable modeling:** SHAP/feature importance and statistical tools for transparent decisions.

---

## Desktop UI & Services (JavaFX + Spring Boot)
MarketMind ships a first‑class Java desktop and local service layer:
- The JavaFX desktop is bundled with Spring Boot services for local APIs and controller wiring.
- Spring uses a controller factory wired to FXML controllers (FXML → Spring controller factory → beans), enabling Spring-managed services inside the UI controller lifecycle.

Run the service + UI in development:
```bash
# start Spring Boot services (local dev)
mvn spring-boot:run

# build the desktop artifact (CI / release)
mvn -q -DskipTests package
```

Generated gRPC stubs and the Java service layer are produced during `mvn compile` / build — see `cpp/` and `src/main/java` for wiring.

---

## Tech Stack
**Languages:** Python 3.12 · C++20 · Java 21/JavaFX 21 · Maven/Spring Boot

**ML & Infra:** PyTorch, TensorFlow/Keras, ONNX, TensorRT, ORT, Triton (optional), cuDF/CuPy, Polars

**Data & I/O:** pandas, Polars, PyArrow, yfinance, FRED, InfluxDB, Redis

**Orchestration & QA:** structlog, pytest + coverage (branch), CodeQL/Dependabot (internal)

---

## Installation & Support Matrix
### Quick prerequisites
- Python 3.12, Poetry, CMake, Ninja, Maven 3.8+, JDK 21
- For GPU: NVIDIA drivers + CUDA 12.9, Conda (recommended for RAPIDS/cuDF)

| Mode | OS | Install path |
|---|---:|---|
| CPU-only | Linux / Windows | `poetry install` (recommended) |
| GPU (CUDA + RAPIDS) | Linux (native Conda) | Create Conda env → use Poetry venv inside conda → `poetry install -E gpu` |

**Notes:** RAPIDS/cuDF are best installed in a Conda environment and paired with Poetry by pointing Poetry at the Conda venv. Windows GPU/RAPIDS support is limited — prefer Linux for GPU workloads.

---

## 3-step End-to-end Quickstart (lands the plane)
This minimal path produces a tiny ONNX model, builds the C++ runtime, and runs a minimal Python pipeline that exercises inference.

1. **Export a tiny model to ONNX**
```bash
# example stub; this script exports a small model to models/tiny.onnx
poetry run python -m srcPy.models.export_tiny_onnx --out models/tiny.onnx
```

2. **Build the C++ runtime**
```bash
cmake -S cpp -B build -DCMAKE_BUILD_TYPE=Release
cmake --build build -j
```

3. **Run the minimal Python pipeline (hello-pipeline → hello-inference)**
```bash
poetry run python -m srcPy.pipeline.examples.minimal --model models/tiny.onnx
```

If you want to run the full Java UI against the local services, start Step 2 (runtime) then run `mvn spring-boot:run` and start the packaged JavaFX client.

---

## Project Structure
<details>
<summary><strong>View Directory Tree</strong></summary>

```
MarketMind/
├── srcPy/                 # Python: pipelines, ML, trading logic
├── cpp/                   # C++ backend (JNI/gRPC)
├── src/                   # Java: JavaFX + Spring Boot services
├── data/                  # Datasets & configs
├── models/                # Saved/trained models (include ONNX)
├── tests/                 # Python/C++/Java + integration
├── deployment/            # Docker, InfluxDB, etc.
├── docs/                  # canonical docs (point to ./docs)
├── scripts/               # build & helper scripts
├── pyproject.toml         # Poetry config & plugin registries
├── CMakeLists.txt         # C++ build config
├── pom.xml                # Maven config
└── README.md, LICENSE, .gitignore
```
</details>

---

## Configuration
- Store local secrets and settings in `data/config.yaml` or environment variables.
- Pipelines are assembled from **plugin steps** registered via entry points; you can add custom steps in your own package and expose them via the registry.

---

## Testing & Gates
```bash
poetry run pytest -q
```
- Coverage threshold: **90%** (branch coverage enabled) with targeted `omit` patterns.
- Markers: `gpu`, `integration`, `perf`, `contract`, `executor`, `streaming`, `benchmark`, `smoke`, `regression`.
- CI jobs avoid noisy tests via `executor` contract/registry tests introduced in 3.1.1.

---

## Performance (SLOs)
Measured latencies vary by hardware and configuration. Replace the example numbers below with your telemetry snapshots from `telemetry/` or monitoring.

| Component | p50 | p95 | p99 |
|---|---:|---:|---:|
| GPU inference (single request) | 2 ms | 6 ms | 12 ms |
| Feature materialization (in-memory, polars/cuDF) | 5 ms | 25 ms | 80 ms |
| Cache hit (local redis) | 0.5 ms | 2 ms | 8 ms |

> These are illustrative — please update with measured values from your perf runs or telemetry.

---

## Security & Privacy (summary)
**Draft — <p>See <a href="https://marketmind-docs.readthedocs.io/en/latest/security_practices.html">Security Practices</a> for security policies</p> and <p> <a href="https://marketmind-docs.readthedocs.io/en/latest/privaccy_practices.html">Privacy Policy</a> for full (draft) details.**
- gRPC‑TLS by default for all inter‑process communication.
- Local‑first processing: models and PII (not collected by default) are processed locally unless explicitly configured.
- No PII/telemetry shipped by default; opt‑in telemetry is gated and auditable.

**Important:** Security and privacy docs are marked **Draft**. This README intentionally avoids language implying public open‑source auditability because the project is proprietary.


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
<p>See <a href=https://marketmind-docs.readthedocs.io/en/latest/infographics_gallery.html)>Infographics Gallery</a> for interactive research documentation</p>
 
<p>See <a href="https://marketmind-docs.readthedocs.io/en/latest/CHANGELOG.html">Changelog</a> for full changelog history.</p> 


## Public Interfaces (at a glance)
**gRPC** endpoints (generated from `.proto` during `mvn compile`)
- `PredictService.Predict` — single request inference
- `IngestService.Stream` — streaming ingestion for market ticks
- `ModelAdmin.Export` — export/prepare models (ONNX/TensorRT bundles)

**C++ / ORT inference contract (essential fields)**
- `input`: float32 tensor, shape `[B, T, F]` (batch, timesteps, features)
- `output`: float32 tensor, shape `[B, O]` (batch, outputs/probabilities)
- `dtype`: float32; model expects normalized inputs (zscore per feature)
- `warmup`: recommended warmup runs (N=5) before steady SLOs; keep EPs (TensorRT/ORT) warmed for latency stability

> Copy the exact contract fields from your generated stubs or `docs/protos` when locking APIs for integration.

---

## Contributing
This project is **proprietary**. Contributions are accepted from internal contributors or by arrangement only. For contribution workflows, code style, and coverage gates, see `Programming Guidelines` in the repo. Pull requests are subject to mandatory review, security review, and must meet coverage & contract tests.

---

## Versioning & Changelog
MarketMind follows Semantic Versioning (MAJOR.MINOR.PATCH). New features that are backward-compatible increment the minor version, bug fixes increment the 
patch version, and any breaking changes would increment the major version. Each release has corresponding notes in the changelog.
<p>See <a href="https://marketmind-docs.readthedocs.io/en/latest/CHANGELOG.html">Changelog</a> for full changelog history.</p> 


Current release: **3.1.1**.

---

## Copyright

MarketMind is proprietary software (© 2025 Mark Wuenschel. All rights reserved.). Its source code is not open-source. However, MarketMind relies on 
several third-party open-source libraries (e.g. NumPy, TensorFlow, ONNX Runtime, etc.) that are distributed under permissive licenses (such as MIT, BSD, or 
Apache 2.0). These permissive licenses explicitly allow incorporating the code into proprietary products without imposing copyleft restrictions prohibited 
without prior written permission from the copyright holder.
See the [LICENSE](LICENSE) file for full terms.

---

_Last updated: 3.1.1._ 11/05/2025