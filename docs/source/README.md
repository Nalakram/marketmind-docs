# MarketMind ![Version](https://img.shields.io/badge/Version-3.3.0-8A2BE2) [![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=flat-square&logo=python)](https://www.python.org/) [![C++20](https://img.shields.io/badge/C%2B%2B-20-00599C?style=flat-square&logo=cplusplus)](https://isocpp.org/) [![CUDA](https://img.shields.io/badge/CUDA-12.9-76B900?style=flat-square&logo=nvidia)](https://developer.nvidia.com/cuda-toolkit) ![License](https://img.shields.io/badge/license-Proprietary-red) [![Build Status](https://img.shields.io/github/actions/workflow/status/Nalakram/QuantAIvus/ci.yml?branch=main)](https://github.com/Nalakram/QuantAIvus/actions) [![codecov](https://codecov.io/gh/MindForgeLabs/MarketMind/graph/badge.svg?token=LIJZD4YCFB)](https://codecov.io/gh/MindForgeLabs/MarketMind) [![Java 21](https://img.shields.io/badge/Java-21-007396?style=flat-square&logo=openjdk)](https://www.oracle.com/java/technologies/downloads/#java21) [![Spring](https://img.shields.io/badge/Spring-3.5.0-6DB33F?style=flat-square&logo=spring&logoColor=white)](https://spring.io/) ![JavaFX 21](https://img.shields.io/badge/JavaFX-21-3873B3?style=flat-square)
 [![Windows Supported](https://custom-icon-badges.demolab.com/badge/Windows-Supported-0078D6?logo=windows11&logoColor=white)](https://www.microsoft.com/windows) [![Linux](https://img.shields.io/badge/Linux-Tested-FCC624?style=flat-square&logo=linux)](https://kernel.org/) [![Read the Docs](https://img.shields.io/badge/docs-Read_the_Docs-8CA1AF?logo=readthedocs)](https://marketmind-docs.readthedocs.io/en/latest/) ![Status](https://img.shields.io/badge/status-development-FFA500?style=flat-square)

![MarketMind Banner](https://raw.githubusercontent.com/Nalakram/marketmind-docs/main/docs/source/images/banner1.png)


MarketMind is an algorithmic trading platform designed for automated, high-frequency trading with built-in analytics and risk controls. It employs a multilingual architecture — performance-critical modules in C++, modeling and orchestration in Python, and a JavaFX desktop UI with Spring Boot services — optimized for ultra-low-latency use cases.

**What's working today (Phase 0):** A complete vertical slice from JavaFX UI → Python subprocess → preprocessing (OHLCV ingestion, technical indicators) → backtesting engine (SMA crossover, Sharpe/drawdown/win rate) → validation gates → JSON results displayed in the desktop UI. The system produces auditable run bundles with deterministic artifact hashing, leakage-protected time-series splits (purge/embargo), and a fail-closed gate framework — all backed by 150+ passing tests.

**What's planned:** The platform is designed to ingest real-time market data and news (NLP pipelines) and apply hybrid deep-learning models (Transformer + LSTM/TCN) for price and trend forecasting, with C++ inference for sub-millisecond latency. Future features include Informer models for long-sequence forecasting, graph neural networks for cross-asset relationships, hidden Markov models for regime detection, Granger causality for leading indicators, and SHAP-based interpretability. See [Current Status & Roadmap](#current-status--roadmap) for phase timelines.

> **Proprietary — internal contributions or by arrangement.** See the _Contributing_ section below and the `Programming Guidelines` for review/coverage/security requirements.

---

## Table of Contents
- [Current Status & Roadmap](#current-status--roadmap)
- [What's New in 3.3.0](#whats-new-in-330)
- [Architecture Overview](#architecture-overview)
- [Backtesting Infrastructure](#backtesting-infrastructure)
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

## Current Status & Roadmap

**Version:** 3.3.0 (February 2026) &nbsp;|&nbsp; **Phase:** 0 (Nearing Completion)

### Phase 0 Definition of Done

| Criteria | Status | Evidence |
|----------|--------|----------|
| Run Bundle v1 emitted by pipeline | ✅ Done | `run_pipeline.py` produces `run_bundle_v1/{timestamp}_{hash}/` per Appendix C |
| Gate CLI invoked automatically | ✅ Done | `srcPy/cli/gate.py` — Appendix C/D v5.1 compliant, 42 tests |
| Java↔Python bridge stable | ✅ Done | stdout JSON + exit codes match Appendix E (0/1/2/3) |
| End-to-end UI demo | ✅ Done | JavaFX button → Python subprocess → backtest → gates → results card |
| Integration canary (vertical slice) | ✅ Done | 10 tests in `test_vertical_slice.py` |
| Splits with purge/embargo | ✅ Done | `splits.py` — 40 tests (33 unit + 7 property), `splits_manifest.json` v1.0.0 |
| ≥5 leakage property tests | ✅ Done | 20 Hypothesis tests covering 5 invariants (temporal ordering, sample disjointness, purge gap, fit-on-train-only, no look-ahead) |
| Preprocessor ≥85% line / ≥70% branch | 🚧 79.9% / 92% | ~125 lines remaining for 85% target; branch target exceeded |
| Baseline locked (CI == local ≤0.5% drift) | ❌ Not started | Infrastructure task |

### Preprocessor Coverage (`srcPy/preprocessor/*`)

**Line coverage:** 79.9% → 85% target (~125 lines remaining) &nbsp;|&nbsp; **Branch coverage:** 92% ✅ (target: 70%)

<details>
<summary>Per-file breakdown</summary>

| File | Coverage | Notes |
|------|----------|-------|
| `ops_custom.py` | 96% | ✅ Bug-fixed (method overrides) |
| `graph.py` | 94% | ✅ |
| `core.py` | 93% | ✅ |
| `expr.py` | 93% | ✅ Bug-fixed (frozen dataclass) |
| `ops.py` | 90% | ✅ Bug-fixed (cached_property) |
| `transforms.py` | 88% | ✅ |
| `columns.py` | 86% | ✅ |
| `api.py` | 83% | ✅ Bug-fixed (dead code removed) |
| `errors.py` | 83% | ✅ |
| `splits.py` | 81% | ✅ New (purge/embargo) |
| `dsl.py` | 80% | ✅ |
| `specs.py` | 59% | 🚧 ~36 uncovered lines |
| `executor.py` | 55% | 🚧 ~60 uncovered lines, bug-fixed (lru_cache) |
| `backends/polars.py` | 42% | 🚧 ~67 uncovered lines |
| `expr_builders.py` | 31% | 🚧 ~34 uncovered lines |

</details>

### Roadmap

| Phase | Focus | Timeline | Status |
|-------|-------|----------|--------|
| **Phase 0** | Validation infrastructure — gates, splits, leakage tests, run bundles, UI vertical slice | Jan–Feb 2026 | 🚧 7/9 criteria met |
| **Phase I** | Live data integration — streaming ingestion, replay, data quality gates | 4–6 weeks after Phase 0 | Not started |
| **Phase II** | ML model integration — feature engineering, XGBoost/LSTM baselines, walk-forward validation, meta-learning | 6–8 weeks after Phase I | Not started |
| **Phase III** | Low-latency execution — C++ inference (<1ms), order execution, risk controls, kill switch | 8–12 weeks after Phase II | Not started |
| **Phase IV** | Production & scale — distributed backtesting, monitoring, multi-asset, multi-strategy | Ongoing after Phase III | Not started |

### Pipeline Architecture (Working)

```
Java UI → python -m srcPy.bridge.run_pipeline input.csv
              ↓
         1. Create run_bundle_v1/{timestamp}_{hash}/
         2. Write plan.json (IN_PROGRESS)
         3. Write env_fingerprint.json
         4. Preprocess (load OHLCV, compute returns/SMA/RSI)
         5. Backtest (SMA crossover signals → Sharpe, drawdown, win rate)
         6. Write dataset_manifest.json, preprocessing_report.json, splits_manifest.json
         7. Invoke Gate CLI → gate_result.json
         8. Update plan.json (COMPLETE)
              ↓
         stdout: JSON with status + backtest metrics + gate result
         Exit codes: 0=SUCCESS, 1=FAILED_GATES, 2=INVALID_INPUT, 3=ERROR
```

---

## What's New in 3.3.0

**3.3.0** completes the Phase 0 vertical slice — an end-to-end pipeline from JavaFX UI through backtesting to validation gates — and pushes preprocessor coverage from 56% to 80%.

### End-to-End Pipeline & Java Integration
- **Working vertical slice**: Button click in JavaFX UI → Python subprocess → preprocessing → backtesting → gate validation → JSON results displayed in UI results card (validation status, total return, Sharpe ratio, max drawdown, win rate, trade count)
- **Run bundle pipeline** (`srcPy/bridge/run_pipeline.py`): Single command produces versioned `run_bundle_v1/{timestamp}_{hash}/` directories with all Appendix C artifacts
- **Java↔Python bridge** with stdout JSON + exit codes per Appendix E; BacktestService with JSON extraction from mixed Python output
- **AtlantaFX theming** for the desktop UI

### Gate CLI (Appendix C/D v5.1 Compliant)
- **Full bundle validation** (`srcPy/cli/gate.py`): Validates all 5 required files per Appendix C.2 with schema version checks
- **Plan identity gate** with expected/actual evidence pattern per Appendix D.2
- **Leakage invariant enforcement** with purge gap verification and timestamp parsing
- **Exit codes** per Appendix D.1: `0`=PASS, `1`=FAIL, `2`=invalid input, `3`=internal error
- **42 tests** covering gate logic, schema validation, and edge cases

### Time-Series Splits with Purge/Embargo
- **`splits.py`**: `TimeSeriesSplitter` and `PurgedKFold` implementations with configurable purge and embargo windows
- **`splits_manifest.json`** v1.0.0 schema with fold metadata (purge count, embargo count, contiguity flags)
- **40 tests** (33 unit + 7 property-based via Hypothesis)

### Property-Based Leakage Tests
- **20 Hypothesis tests** covering 5 leakage invariants: temporal ordering, sample disjointness, purge gap enforcement, fit-on-train-only, no look-ahead bias
- Located in `tests/python/property/test_leakage_invariants.py`

### Preprocessor Coverage Push (56% → 80%)
- **7 critical bug fixes**: `factory.py` (missing import + silent exceptions), `planner.py` (undefined attributes), `api.py` (dead code), `executor.py` (broken lru_cache), `ops.py` (cached_property incompatibility), `ops_custom.py` (method override mismatch), `expr.py` (frozen dataclass with mutable parent)
- **Deleted dead code**: `expr_opt.py` (28 lines, 0% coverage, duplicated logic)
- **~1,500 lines of new tests** across 4 test files targeting specific uncovered modules

### Previous Release (3.2.0)
<details>
<summary>Gate Runner CLI, Artifact Registry, CAS Storage (December 2025)</summary>

- **Fail-closed validation service** (`mm-gate`) for Spec Bundle v1 inputs with deterministic decision artifacts
- **RFC8785 JCS canonicalization** + SHA-256 for reproducible artifact hashing
- **Content-addressable storage (CAS)** with idempotent artifact registration and deduplication
- **Run state machine**: REGISTERING → COMPLETE → FAILED with visibility controls
- **47 tests** covering happy path, hash tampering, threshold violations, schema violations, and determinism

</details>

<p>See <a href="https://marketmind-docs.readthedocs.io/en/latest/CHANGELOG.html">Changelog</a> for full changelog history.</p> 

---

## Architecture Overview

```
         ┌──────────────────────────┐         ┌──────────────────────────┐
         │   Backtesting Engine     │         │      Python Orchestrator │
         │  (Lane A/B simulation)   │◄───────►│  (pipelines/engines)     │
         │  • Artifact provenance   │  gRPC   └───────────┬──────────────┘
         │  • Transfer gap analysis │                     │
         └────────────┬─────────────┘                     │
                      │                              Registries/Plugins
         ┌────────────▼─────────────┐                     │
         │   Gate Runner CLI        │                     ▼
         │  (mm-gate validate)      │         ┌──────────────────────────┐
         └──────────────────────────┘         │  Artifact Registry (CAS) │
                                              │  • Run state machine     │
         ┌──────────────────────────┐         │  • Deduplication         │
         │        JavaFX UI         │         └──────────────────────────┘
         │  (desktop client)        │◄────────►  GPU/CPU Backends
         └────────────┬─────────────┘   gRPC   (cuDF/CuPy/Polars/Torch)
                      │ JNI/gRPC
                      ▼
         ┌──────────────────────────┐
         │      C++ Inference       │
         │ (ultra‑low latency)      │
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
  Python -->|register| ArtifactReg[Artifact Registry]
  ArtifactReg -->|validate| GateRunner[Gate Runner CLI]
  GateRunner -->|promote| Production[Production Deployment]
```

</details>

**Key ideas**
- **Registry‑driven pipelines:** All cleaning/preprocessing steps are plug‑ins (e.g., `rename`, `cast`, `resample`, technical features, embeddings, topic modeling, explainability). Registries enable runtime composition and safe fallbacks.
- **Self‑evolving engine:** Adaptive strategies learn when to parallelize, reorder, or switch backends based on risk/telemetry.
- **GPU acceleration end‑to‑end:** cuDF → CuPy sliding windows → Torch tensors → model → TensorRT/ORT → C++ inference.
- **Explainable modeling:** SHAP/feature importance and statistical tools for transparent decisions.
- **Artifact provenance:** RFC8785-canonicalized hashing ensures reproducible artifact identity across backtesting lanes.

---

## Backtesting Infrastructure

MarketMind includes a production-grade backtesting system designed for multi-fidelity strategy validation:

### Multi-Fidelity Simulation (Lane A/B)
- **Lane A (Low-fidelity)**: Rapid prototyping with simplified market dynamics for fast iteration cycles
- **Lane B (High-fidelity)**: Production-grade simulation with full order book dynamics, slippage, and transaction costs
- **Transfer gap measurement**: Quantitative metrics (Spearman ρ, top-k overlap) validate strategy robustness across lanes

### Run Bundle Pipeline (Working)
The pipeline produces a complete, auditable `run_bundle_v1/` directory from a single command:

```bash
# Full pipeline: preprocess → backtest → gate validation → JSON output
python -m srcPy.bridge.run_pipeline tests/fixtures/sample_spy.csv --fast-sma 5 --slow-sma 10

# Individual CLI tools
python -m srcPy.cli.preprocess input.csv output.csv --sma 5 10 --rsi 14
python -m srcPy.cli.backtest data.csv --output-dir bundles/run1
```

**Bundle output** (per Appendix C):
```
run_bundle_v1/{timestamp}_{hash}/
├── plan.json                    # Identity + point-in-time anchor
├── env_fingerprint.json         # Python version, git SHA, dependencies
├── dataset_manifest.json        # Symbols, row count, time range
├── preprocessing_report.json    # Transform trace with fit/transform boundaries
├── splits_manifest.json         # Fold metadata, purge/embargo windows
└── gate_result.json             # PASS/FAIL per gate with evidence
```

### Time-Series Splits (Purge/Embargo)
Leakage-protected train/test splitting using Marcos López de Prado's methodology:

- **`TimeSeriesSplitter`**: Walk-forward splits with configurable purge and embargo windows
- **`PurgedKFold`**: K-fold cross-validation that purges observations within the purge window of test boundaries and embargoes observations after test periods
- **`splits_manifest.json`**: Machine-readable fold metadata (purge count, embargo count, contiguity flags) with schema version validation

### Gate Runner CLI
The `mm-gate` CLI provides fail-closed artifact validation before strategy promotion:

```bash
# Validate backtesting artifacts against policy thresholds
mm-gate validate <bundle_dir> [--policy policies/gating_policy.v1.yaml]

# Promote strategy (emits promotion_event.json on PASS)
mm-gate promote <bundle_dir> [--policy <path>] [--allow-run-ids]
```

**Exit codes:**
- `0` = PASS (all gates satisfied)
- `2` = Validation failure (threshold violation, hash mismatch, schema error)
- `3` = Configuration error (missing policy, invalid bundle)

**Validation gates:**
- **Schema compliance**: JSON Schema Draft-07/2020-12 with deep closed-world validation
- **Integrity verification**: SHA-256 hash matching for all artifacts in `artifact_index.json`
- **Comparability locks**: Enforces matching `fidelity_id`, `cost_model_id`, `scenario_id`, `data_slice_id` between baseline and candidate
- **Threshold gating**: Spearman ρ ≥ 0.70, top-k overlap ≥ 0.60 (k ∈ [5, 10, 20])
- **Binding validation**: Requires content hashes (not just run IDs) for promotion to production
- **Leakage invariant enforcement**: Purge gap verification with timestamp parsing

### Gate CLI (`srcPy/cli/gate.py`)
Bundle-level validation aligned to Appendix C/D v5.1:

```bash
# Validate a run bundle
marketmind-gate check --bundle /path/to/run_bundle_v1 --output /path/to/gate_result.json
```

**Exit codes** (Appendix D.1): `0`=all gates PASS, `1`=one or more FAIL, `2`=invalid input, `3`=internal error

**Gates implemented:** file presence (5 required files per C.2), schema version validation, plan identity with expected/actual evidence, leakage invariant checks

### Artifact Registry (CAS)
Content-addressable storage with deterministic deduplication:

```python
from srcPy.artifact_registry import ArtifactRegistry, BlobStore

# Register backtest result (automatic deduplication)
artifact_id = await registry.register_artifact(
    run_id="run_abc123",
    plan_hash="sha256:...",
    artifact_type="backtest_result",
    content_hash="sha256:...",  # Computed via RFC8785 JCS
    content={"sharpe_ratio": 1.42, "pnl": 0.18},
    lane="A"  # or "B"
)
```

**Key features:**
- **Idempotency**: Re-registering `(plan_hash, artifact_type, content_hash)` returns existing artifact ID
- **Run state machine**: `REGISTERING` → `COMPLETE` → `FAILED` with visibility controls
- **Immutable identity**: Artifact provenance preserved across deduplication
- **NaN/Infinity rejection**: Hashing contract enforcement prevents non-finite floats

See the [Backtesting Guide](https://marketmind-docs.readthedocs.io/en/latest/backtesting.html) for detailed usage.

---

## Desktop UI & Services (JavaFX + Spring Boot)
MarketMind ships a first‑class Java desktop and local service layer with a working end-to-end backtesting integration:
- The JavaFX desktop is bundled with Spring Boot services for local APIs and controller wiring, themed with **AtlantaFX**.
- Spring uses a controller factory wired to FXML controllers (FXML → Spring controller factory → beans), enabling Spring-managed services inside the UI controller lifecycle.
- **BacktestService** invokes the Python pipeline via `PythonRunner` subprocess, extracts JSON from mixed stdout output, and displays results in a dashboard card showing: validation status (PASS/FAIL), total return, Sharpe ratio, max drawdown, win rate, and trade count.

Run the service + UI in development:
```bash
# start Spring Boot services (local dev)
export DISPLAY=host.docker.internal:0
mvn compile -DskipTests -Dprotoc.skip=true -Dcheckstyle.skip=true -q
mvn javafx:run -DskipTests -Dprotoc.skip=true -Dcheckstyle.skip=true

# build the desktop artifact (CI / release)
mvn -q -DskipTests package
```

Generated gRPC stubs and the Java service layer are produced during `mvn compile` / build — see `cpp/` and `src/main/java` for wiring.

---

## Tech Stack
**Languages:** Python 3.12 · C++20 · Java 21/JavaFX 21 · Maven/Spring Boot

**ML & Infra:** PyTorch, TensorFlow/Keras, ONNX, TensorRT, ORT, Triton (optional), cuDF/CuPy, Polars

**Data & I/O:** pandas, Polars, PyArrow, yfinance, FRED, InfluxDB, Redis

**Orchestration & QA:** structlog, pytest + coverage (branch), mypy --strict, CodeQL/Dependabot (internal)

**Backtesting & Validation:** RFC8785 JCS canonicalization, jsonschema (Draft-07/2020-12), ruamel.yaml

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

### Option A: Run the backtesting pipeline (working today)
```bash
# 1. Install Python dependencies
poetry install

# 2. Run the full pipeline (preprocess → backtest → validate → JSON output)
python -m srcPy.bridge.run_pipeline tests/fixtures/sample_spy.csv --fast-sma 5 --slow-sma 10

# 3. Run the JavaFX UI with backtesting integration
export DISPLAY=host.docker.internal:0
mvn compile -DskipTests -Dprotoc.skip=true -Dcheckstyle.skip=true -q
mvn javafx:run -DskipTests -Dprotoc.skip=true -Dcheckstyle.skip=true
```

### Option B: Build the C++ runtime + minimal inference (Phase III — not yet implemented)
This path will produce a tiny ONNX model, build the C++ runtime, and run inference.

1. **Export a tiny model to ONNX**
```bash
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

---

## Project Structure
<details>
<summary><strong>View Directory Tree</strong></summary>

Legend: ✅ Production-ready &nbsp;|&nbsp; 🚧 In progress &nbsp;|&nbsp; 🔮 Planned

```
MarketMind/
├── srcPy/                 # Python: pipelines, ML, trading logic
│   ├── preprocessor/      # ✅ Feature engineering + data transforms
│   │   ├── core.py        #    ✅ load_ohlcv, add_returns, add_sma, add_rsi (93% coverage)
│   │   ├── splits.py      #    ✅ TimeSeriesSplitter, PurgedKFold (81% coverage, 40 tests)
│   │   └── graph/         #    ✅ Registry-driven pipeline graph
│   │       ├── factory.py     # ✅ Bug-fixed (SentimentLexicon import, alias registration)
│   │       ├── planner.py     # ✅ Bug-fixed (metrics/weights init)
│   │       ├── api.py         # ✅ Bug-fixed (dead code removed), 83% coverage
│   │       ├── executor.py    # 🚧 Bug-fixed (lru_cache), 55% coverage
│   │       ├── ops.py         # ✅ Bug-fixed (cached_property), 90% coverage
│   │       ├── ops_custom.py  # ✅ Bug-fixed (method overrides), 96% coverage
│   │       └── expr.py        # ✅ Bug-fixed (frozen dataclass), 93% coverage
│   ├── backtest/          # ✅ Backtesting engine
│   │   └── engine.py      #    ✅ BacktestResult, add_signals, compute_metrics
│   ├── bridge/            # ✅ Java↔Python integration
│   │   └── run_pipeline.py #   ✅ Bundle assembly + gate invocation (Appendix C/E)
│   ├── cli/               # ✅ Command-line tools
│   │   ├── gate.py        #    ✅ Appendix C/D v5.1 bundle validation (42 tests)
│   │   ├── preprocess.py  #    ✅ Preprocessing CLI
│   │   └── backtest.py    #    ✅ Backtesting CLI
│   ├── backtesting/       # ✅ Multi-fidelity backtesting engine (Lane A/B)
│   ├── artifact_registry/ # ✅ CAS storage with run state machine
│   ├── pipeline/
│   │   └── examples/      # ✅ Vertical slice smoke tests
│   └── ...
├── marketmind_gate/       # ✅ Gate Runner CLI for artifact validation
│   ├── cli.py             # Entry point (mm-gate validate/promote)
│   ├── hashing/
│   │   └── canonical.py   # RFC8785 JCS + SHA-256
│   ├── gates/
│   │   ├── core.py        # ✅ Gate validation framework (19 tests)
│   │   ├── schema.py      # JSON Schema validation
│   │   ├── integrity.py   # Hash verification
│   │   ├── invariants.py  # Transfer report checks
│   │   ├── policy.py      # Threshold gating
│   │   └── decision.py    # Decision artifact emission
│   ├── io/
│   │   └── resolvers.py   # URI resolution
│   └── policy/
│       └── loader.py      # YAML policy loading
├── src/                   # ✅ Java: JavaFX + Spring Boot services
│   └── main/java/**/
│       ├── MainApp.java         # ✅ AtlantaFX theme initialization
│       ├── utils/PythonRunner.java        # ✅ Python subprocess management
│       ├── services/BacktestService.java  # ✅ Pipeline invocation + JSON extraction
│       └── features/dashboard/
│           ├── DashboardController.java   # ✅ Backtest integration + results display
│           └── Dashboard.fxml             # ✅ Backtest controls + results card
├── cpp/                   # 🔮 C++ backend (JNI/gRPC) — Phase III
├── data/                  # Datasets & configs
├── models/                # 🔮 Saved/trained models — Phase II
├── schemas/               # ✅ JSON Schema definitions
│   ├── identity.schema.json
│   ├── artifacts.schema.json
│   ├── transfer_report.schema.json
│   ├── gate_decision.schema.json
│   └── promotion_event.schema.json
├── policies/              # ✅ Gating policies (YAML)
│   └── gating_policy.v1.yaml
├── tests/                 # Python/C++/Java + integration
│   ├── fixtures/
│   │   ├── sample_spy.csv               # ✅ Test data (20 rows)
│   │   ├── valid_bundle/                # ✅ Gate runner test fixtures
│   │   ├── hash_mismatch/
│   │   ├── threshold_violation/
│   │   └── ...                          # 7 fixture bundles total
│   ├── python/
│   │   ├── unit/
│   │   │   ├── preprocessor/
│   │   │   │   ├── test_core.py                     # ✅ 7 tests
│   │   │   │   ├── test_dsl_and_api.py              # ✅ Coverage push
│   │   │   │   ├── test_transforms_and_columns.py   # ✅ Coverage push
│   │   │   │   ├── test_expr_ops_executor.py        # ✅ Coverage push
│   │   │   │   └── test_executor_polars_coverage.py # ✅ Coverage push
│   │   │   ├── backtest/test_engine.py  # ✅ 10 tests
│   │   │   ├── gate/test_core.py        # ✅ 19 tests
│   │   │   ├── cli/test_gate.py         # ✅ 42 tests (Gate CLI)
│   │   │   └── test_hashing.py          # ✅ 27 tests (canonicalization)
│   │   ├── property/
│   │   │   ├── test_leakage_invariants.py  # ✅ 20 Hypothesis tests (5 invariants)
│   │   │   └── test_splits_properties.py   # ✅ 7 property-based tests
│   │   └── integration/
│   │       ├── test_vertical_slice.py          # ✅ 10 end-to-end tests
│   │       ├── test_gate_runner.py             # ✅ 20 tests
│   │       ├── test_registry_smoke.py          # ✅ 14 tests
│   │       └── test_vertical_slice_smoke.py    # ✅ 26 tests
│   └── unit/
│       └── test_hashing.py   # ✅ 27 tests
├── deployment/            # Docker, InfluxDB, etc.
├── docs/                  # canonical docs (point to ./docs)
├── scripts/               # build & helper scripts
├── .github/
│   └── workflows/
│       └── gate-runner.yml # CI: mypy, pytest, schema validation
├── pyproject.toml         # Poetry config & plugin registries
├── CMakeLists.txt         # C++ build config
├── pom.xml                # Maven config (Java 24, AtlantaFX)
└── README.md, LICENSE, .gitignore
```
</details>

---

## Configuration
- Store local secrets and settings in `data/config.yaml` or environment variables.
- Pipelines are assembled from **plugin steps** registered via entry points; you can add custom steps in your own package and expose them via the registry.
- Gate Runner policies are defined in `policies/gating_policy.v1.yaml` and can be customized per deployment.

---

## Testing & Gates
```bash
# Run all tests
poetry run pytest -q

# Full pipeline tests
poetry run pytest tests/python/ -v

# Gate CLI tests (42 tests)
poetry run pytest tests/python/unit/cli/test_gate.py -v

# Gate Runner tests (47 tests)
poetry run pytest tests/unit/test_hashing.py tests/integration/test_gate_runner.py

# Artifact Registry tests (40 tests)
poetry run pytest tests/integration/test_registry_smoke.py tests/integration/test_vertical_slice_smoke.py

# Preprocessor tests (~1,500 lines)
poetry run pytest tests/python/unit/preprocessor/ -v

# Property-based leakage tests (27 Hypothesis tests)
poetry run pytest tests/python/property/ -v

# Splits tests (40 tests)
poetry run pytest tests/python/unit/preprocessor/test_splits.py tests/python/property/test_splits_properties.py -v

# Type checking
poetry run mypy marketmind_gate --strict
```

**Coverage & Quality:**
- **Preprocessor line coverage**: 79.9% (target: 85%) | **Branch coverage**: 92% ✅ (target: 70%)
- **mypy --strict**: Success across 15 source files (0 issues)
- **CI/CD**: GitHub Actions workflow validates mypy, pytest, and schema integrity on every push

**Test markers:**
- `gpu`, `integration`, `perf`, `contract`, `executor`, `streaming`, `benchmark`, `smoke`, `regression`
- `backtesting`, `provenance`, `lane_a`, `lane_b`, `leakage`, `property`

**Test inventory (150+ tests):**

| Suite | Tests | Focus |
|-------|------:|-------|
| Gate CLI (`test_gate.py`) | 42 | Bundle validation, schema checks, exit codes per Appendix D |
| Splits unit (`test_splits.py`) | 33 | TimeSeriesSplitter, PurgedKFold, manifest emission |
| Hashing (`test_hashing.py`) | 27 | RFC8785 canonicalization, SHA-256 invariance |
| Vertical slice smoke (`test_vertical_slice_smoke.py`) | 26 | End-to-end pipeline (CAS registry path) |
| Leakage invariants (`test_leakage_invariants.py`) | 20 | Hypothesis: temporal ordering, purge, embargo, fit-on-train, look-ahead |
| Gate runner (`test_gate_runner.py`) | 20 | Gate logic, determinism |
| Gate core (`test_core.py`) | 19 | Gate validation framework |
| CAS registry (`test_registry_smoke.py`) | 14 | CAS invariants, state machine |
| Backtest engine (`test_engine.py`) | 10 | BacktestResult, metrics computation |
| Vertical slice integration (`test_vertical_slice.py`) | 10 | UI pipeline end-to-end |
| Splits property (`test_splits_properties.py`) | 7 | Hypothesis: split invariants |
| Preprocessor core (`test_core.py`) | 7 | load_ohlcv, indicators |
| Preprocessor coverage push | ~1,500 lines | 4 files targeting dsl, api, transforms, columns, expr, ops, executor |

---

## Performance (SLOs)
Measured latencies vary by hardware and configuration. Replace the example numbers below with your telemetry snapshots from `telemetry/` or monitoring.

| Component | p50 | p95 | p99 |
|---|---:|---:|---:|
| GPU inference (single request) | 2 ms | 6 ms | 12 ms |
| Feature materialization (in-memory, polars/cuDF) | 5 ms | 25 ms | 80 ms |
| Cache hit (local redis) | 0.5 ms | 2 ms | 8 ms |
| Artifact hash computation (RFC8785 JCS) | 1 ms | 5 ms | 15 ms |
| Gate validation (single bundle) | 50 ms | 200 ms | 500 ms |

> These are illustrative — please update with measured values from your perf runs or telemetry.

---

## Security & Privacy (summary)
**Draft — <p>See <a href="https://marketmind-docs.readthedocs.io/en/latest/security_practices.html">Security Practices</a> for security policies</p> and <p> <a href="https://marketmind-docs.readthedocs.io/en/latest/security_practices.html">Privacy Policy</a> for full (draft) details.**
- gRPC‑TLS by default for all inter‑process communication.
- Local‑first processing: models and PII (not collected by default) are processed locally unless explicitly configured.
- No PII/telemetry shipped by default; opt‑in telemetry is gated and auditable.
- **Artifact integrity**: SHA-256 hash verification prevents tampering with backtesting results.

**Important:** Security and privacy docs are marked **Draft**. This README intentionally avoids language implying public open‑source auditability because the project is proprietary.

---

## Public Interfaces (at a glance)

### Working (Phase 0) ✅

**Run Bundle Pipeline**
- `python -m srcPy.bridge.run_pipeline <input_csv>` — full pipeline producing `run_bundle_v1/` with JSON stdout
- `python -m srcPy.cli.preprocess <input> <output>` — standalone preprocessing
- `python -m srcPy.cli.backtest <input> --output-dir <dir>` — standalone backtesting

**Gate CLI** (`srcPy/cli/gate.py`)
- `marketmind-gate check --bundle <dir> --output <path>` — validate run bundle per Appendix C/D

**Gate Runner CLI** (`mm-gate`)
- `mm-gate validate <bundle_dir>` — validate backtesting artifacts against policy
- `mm-gate promote <bundle_dir>` — promote strategy (emits promotion_event.json on PASS)

**Artifact Registry API**
- `register_artifact()` — CAS registration with automatic deduplication
- `get_latest()` — query latest COMPLETE artifacts for a plan
- `mark_run_complete()` / `mark_run_failed()` — state machine transitions

### Planned (Phase I–III) 🔮

**gRPC endpoints** (generated from `.proto` during `mvn compile`)
- `PredictService.Predict` — single request inference
- `IngestService.Stream` — streaming ingestion for market ticks
- `ModelAdmin.Export` — export/prepare models (ONNX/TensorRT bundles)

**C++ / ORT inference contract**
- `input`: float32 tensor, shape `[B, T, F]` (batch, timesteps, features)
- `output`: float32 tensor, shape `[B, O]` (batch, outputs/probabilities)

> Copy the exact contract fields from your generated stubs or `docs/protos` when locking APIs for integration.

---

## Contributing
This project is **proprietary**. Contributions are accepted from internal contributors or by arrangement only. For contribution workflows, code style, and coverage gates, see `Programming Guidelines` in the repo. Pull requests are subject to mandatory review, security review, and must meet coverage & contract tests.

**Development workflow:**
1. Create feature branch from `main`
2. Implement changes with ≥90% branch coverage
3. Run `mypy --strict` and `pytest` locally
4. Submit PR (CI validates mypy, pytest, schema integrity)
5. Require 1+ review from CODEOWNERS

---

## Versioning & Changelog
MarketMind follows Semantic Versioning (MAJOR.MINOR.PATCH). New features that are backward-compatible increment the minor version, bug fixes increment the 
patch version, and any breaking changes would increment the major version. Each release has corresponding notes in the changelog.
<p>See <a href="https://marketmind-docs.readthedocs.io/en/latest/CHANGELOG.html">Changelog</a> for full changelog history.</p> 


Current release: **3.3.0**.

**Recent releases:**
- **3.3.0** (Feb 2026): End-to-end pipeline (UI → Python → backtest → gates → results), Gate CLI (Appendix C/D), splits with purge/embargo, 20 leakage property tests, preprocessor coverage 56% → 80%, 7 critical bug fixes
- **3.2.0** (Dec 2025): Gate Runner CLI, Artifact Registry (CAS), vertical slice smoke tests, CI/CD improvements
- **3.1.1** (Nov 2025): Unified adaptive executor, surgical execute/skip policy, coverage gates tightened

**Upcoming:**
- **3.4.0** (Target: March 2026): Phase 0 completion (85% coverage, CI baseline lock), begin Phase I (live data)
- **4.0.0** (Target: Q2–Q3 2026): ML training pipeline, C++ inference, meta-learning platform

---

## License
MarketMind is proprietary software (© 2025–2026 Mark Wuenschel. All rights reserved.). Its source code is not open-source. However, MarketMind relies on 
several third-party open-source libraries (e.g. NumPy, TensorFlow, ONNX Runtime, etc.) that are distributed under permissive licenses (such as MIT, BSD, or 
Apache 2.0). These permissive licenses explicitly allow incorporating the code into proprietary products without imposing copyleft restrictions prohibited 
without prior written permission from the copyright holder.
See the [LICENSE](LICENSE) file for full terms.

---

_Last updated: 3.3.0 (February 2026)._
