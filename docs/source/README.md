**MarketMind**  
────────────────────────

Algorithmic Trading Platform

README & Technical Overview

Version 3.3.1  ·  February 2026  ·  Proprietary

Python 3.12  ·  C++20  ·  Java 21 / JavaFX  ·  Spring Boot

*Companion documents: Implementation Plan v5.3  ·  Technical Roadmap v1.1  ·  VERSION.md*

# **Contents**

1\.  Overview

2\.  Current Status & Roadmap

3\.  Architecture Overview

4\.  Design Foundations

5\.  Backtesting Infrastructure

6\.  Desktop UI & Services

7\.  Tech Stack

8\.  Installation & Quickstart

9\.  Project Structure

10\. Testing & Quality

11\. Performance SLOs

12\. Security & Privacy

13\. Document Map

14\. Versioning & Changelog

15\. License

# **1\. Overview**

MarketMind is an algorithmic trading platform designed for automated, high-frequency trading with built-in analytics, validation gates, and risk controls. It ingests market data and applies hybrid deep-learning models to generate continuous price and trend forecasts. Its trading engine executes buy/sell orders based on model signals with configurable risk management.

**What works today (Phase 0):** A complete vertical slice from JavaFX desktop UI through Python subprocess to preprocessing, backtesting, gate validation, and results display — backed by 150+ passing tests, 20 Hypothesis property-based leakage tests, and an artifact registry with content-addressable storage.

**What’s planned:** Real-time data feeds, ML training pipelines (Transformer \+ LSTM/TCN), ONNX/TensorRT optimization, C++ sub-millisecond inference, a Medallion-inspired signal factory with meta-learning, and SHAP-based interpretability. The architectural vision encompasses a 6-lane fidelity simulation system, an Autonomous Alpha Factory loop, and hierarchical meta-learning.

The system employs a multilingual architecture: performance-critical modules in C++, modeling and orchestration in Python (Polars/PyTorch), and a JavaFX desktop UI with Spring Boot services. All backtesting artifacts are hashed with RFC8785 JCS canonicalization for reproducibility.

*Proprietary — internal contributions or by arrangement. See Contributing and Programming Guidelines for requirements.*

# **2\. Current Status & Roadmap**

**Version:** 3.3.0  |  Phase 0: Validation Infrastructure  |  7 of 9 milestones complete

| What Works ✅ | What Doesn’t Yet ❌ |
| :---- | :---- |
| End-to-end vertical slice: UI → Python → backtest → gates → results | Live data feeds — no streaming, no replay, no WebSocket |
| Run bundle pipeline producing auditable artifact directories | ML models — no training, no ONNX export, no inference |
| Gate CLI with Appendix C/D v5.1 compliance (42 tests) | C++ inference engine — JNI interface exists, no native lib |
| Purge/embargo time-series splits (40 tests, 100% coverage) | NLP / sentiment pipeline — deps installed, nothing wired |
| 20 Hypothesis leakage property tests covering 5 invariants | Statistical validity report — spec’d (Appendix H), not built |
| Artifact Registry with CAS, dedup, state machine (14 tests) | Strategy ecosystem — stat\_arb/momentum sketched, not pipelined |
| Preprocessor at 80% line / 92% branch coverage | Risk framework — Kelly/position sizing not integrated |
| 150+ tests passing across unit, integration, property suites | Execution cost modeling — backtests assume zero costs |

**Phase 0 remaining:** Preprocessor coverage 80% → 85% (\~125 test lines across 4 files) and CI baseline lock (pytest.ini/.coveragerc diff check).

## **Roadmap**

| Phase | Focus | Timeline | Status |
| :---- | :---- | :---- | :---- |
| 0 | Validation infrastructure: gates, bundles, splits, leakage tests | Jan – Feb 2026 | 🚧 7/9 complete |
| I | Live data: feeds, replay engine, quality gates, PIT enforcement | \+4–6 weeks | Not started |
| II | ML models: features, XGBoost/LSTM, signal registry, meta-learning | \+6–8 weeks | Not started |
| III | Low-latency execution: C++ inference, order engine, risk controls | \+8–12 weeks | Not started |
| IV | Production & scale: distributed backtesting, monitoring, multi-asset | Ongoing | Not started |

## **Working Pipeline**

\# Single command produces auditable run bundle:

python \-m srcPy.bridge.run\_pipeline tests/fixtures/sample\_spy.csv \--fast-sma 5 \--slow-sma 10

\# Output: run\_bundle\_v1/{timestamp}\_{hash}/

\#   ├── plan.json                    \# Run configuration \+ plan\_hash

\#   ├── env\_fingerprint.json          \# Python, git, system, deps, GPU

\#   ├── dataset\_manifest.json         \# Data provenance \+ hashes

\#   ├── preprocessing\_report.json     \# Feature computation report

\#   ├── splits\_manifest.json          \# Train/test split details

\#   └── gate\_result.json              \# PASS/FAIL \+ reason codes

\# stdout: JSON result  |  exit codes: 0=PASS, 1=FAIL, 2=invalid input, 3=internal error

# **3\. Architecture Overview**

    ┌─────────────────────────┐     ┌─────────────────────────┐

    │  Backtesting Engine        │     │  Python Orchestrator      │

    │  (Lane A/B simulation)     │◄──►│  (pipelines / engines)    │

    │  • Artifact provenance     │gRPC └──────────┬──────────────┘

    │  • Transfer gap analysis   │            │

    └───────────┬─────────────┘    Registries / Plugins

               │                         │

    ┌───────────▼─────────────┐         ▼

    │  Gate Runner CLI          │  ┌─────────────────────────┐

    │  (mm-gate validate)       │  │  Artifact Registry (CAS)  │

    └─────────────────────────┘  │  • Run state machine       │

                                  │  • Deduplication           │

    ┌─────────────────────────┐  └─────────────────────────┘

    │  JavaFX Desktop UI       │

    │  (Spring Boot \+ AtlantaFX)│◄──► GPU/CPU Backends

    └───────────┬─────────────┘  (Polars/cuDF/CuPy/Torch)

               │ JNI/gRPC

               ▼

    ┌─────────────────────────┐

    │  C++ Inference  🔮       │

    │  (ultra-low latency)      │

    └─────────────────────────┘

### **Key Architectural Ideas**

* **Registry-driven plugin pipelines:** All cleaning, preprocessing, and strategy steps are typed plugins composed at runtime. Seven canonical plugin types (SignalFn through Validator) enforce strict separation of concerns.

* **Functional Core / Imperative Shell (FCIS):** Strategy logic is pure, stateless computation over immutable DataFrames. All side effects (I/O, clocks, exchange calls) live in the shell.

* **Canonical IR Pipeline:** Strategies emit typed Intermediate Representations — not side effects. The 7-stage pipeline (MarketData → Features → Alpha → Targets → Orders → Fills → Ledger) separates pure computation from stateful execution.

* **Artifact provenance:** RFC8785 JCS-canonicalized hashing ensures reproducible artifact identity across backtesting lanes and environments.

* **Multi-fidelity simulation:** Strategies are validated across a fidelity ladder (Lanes 0–5), from fast analytical screening to real-time shadow deployment.

# **4\. Design Foundations**

MarketMind’s architecture is grounded in 11 research documents produced December 2025 through February 2026, covering every layer from data integrity to meta-learning. This section summarizes the key architectural commitments that shape all implementation decisions.

## **4.1 Canonical IR Pipeline**

The system processes data through a 7-stage pipeline with a hard boundary between pure computation and stateful execution. Stages 1–3 are pure functions: deterministic, cacheable, and safe for JAX/GPU acceleration. Stages 4–7 are stateful: event-driven with explicit state machines.

MarketData → Features → Alpha → Targets → Orders → Fills → Ledger

\[──── Pure (Functional Core) ────\]   \[─── Stateful (Imperative Shell) ───\]

*Source: Research Pack · Strategy I/O Contract v2 (December 2025\)*

## **4.2 Plugin Architecture**

All strategy logic composes from seven canonical plugin types with explicit Protocol signatures and forbidden boundaries. Each type has a single responsibility; cross-boundary access (e.g., a SignalFn reading cost data) is a hard violation.

| Plugin Type | Primary I/O | Responsibilities | Forbidden |
| :---- | :---- | :---- | :---- |
| SignalFn | MarketData → Alpha \[-1,1\] | Normalized signals, indicators, param schema | Sizing, costs, execution, I/O |
| SizingFn | Alpha \+ Data → Positions | Vol targeting, Kelly/fixed-fraction sizing | Signal generation, risk, costs |
| RiskFn | Targets \+ Current → Clipped | Position caps, drawdown throttle, kill switch | Signals, sizing, costs, execution |
| CostModel | Trades \+ Data → Cost | Spread/fee/impact estimation, lane-specific | Signal/sizing/risk decisions |
| ExecutionModel | Orders \+ Data → Fills | Fill simulation, slippage, latency, queues | Signal/sizing/risk logic |
| PortfolioAllocator | Strategy Pos → Portfolio | Multi-strategy combination, exposure limits | Individual signals, execution |
| Validator | Any \+ Schema → Result | Config/output validation, combinatoric checks | Data transformation, side effects |

*Source: Plugin Architecture — Best of All Worlds (December 2025\)*

## **4.3 Multi-Fidelity Simulation (Lanes 0–5)**

Strategies are validated across a fidelity ladder. Lower lanes are fast, cheap filters for hypothesis testing. Higher lanes are expensive, realistic validators. Promotion from Lane A to Lane B requires transfer metric thresholds (Kendall τ-b, NDCG@k).

| Lane | Fidelity Level | Primary Use | Status |
| :---- | :---- | :---- | :---- |
| 0: Analytical | Monthly/daily returns | Factor analysis, portfolio theory | ✅ Current |
| 1: Signal | OHLCV bars | Hypothesis testing, feature selection | ✅ Current |
| 2: Backtest | Tick/quote \+ static costs | Parameter optimization, walk-forward | 🚧 Needs Appendix G |
| 3: Microstructure | L2 / limit order book | Execution logic, fill probability | 🔮 Phase III |
| 4: Agent-Based | Synthetic / generative | Resilience, liquidity crises | 🔮 Phase IV+ |
| 5: Shadow | Real-time feed | Deployment validation, canary testing | 🔮 Phase III–IV |

**Comparability locks:** When comparing across lanes, data\_slice\_id, feature\_plan\_hash, strategy\_config\_hash, and random\_seed must match. Only cost\_model and execution\_model may differ.

*Source: Unified Fidelity & MetaLearning Report · Plugin Architecture Section 5 (December 2025\)*

## **4.4 Point-in-Time Data Integrity**

All data access flows through a single front door: DataView.as\_of(T), which enforces both valid\_time ≤ T and knowledge\_time ≤ T. This makes look-ahead bias mechanically impossible at the API level.

* **Bitemporal facts:** Every mutable datum carries valid\_time (when it’s true in the world) and knowledge\_time (when it becomes knowable). Storage is append-only.

* **Safe joins only:** All temporal joins are backward ASOF with explicit staleness bounds (TTL). Forward and nearest joins are forbidden.

* **Restatements are rows:** Corrections are new versioned rows, not edits. Default PIT returns originally-known values.

* **Universe is auditable:** Daily membership table with reason codes. Delisted assets included until delist date.

* **Automated defense:** CI battery includes poison-pill, backward-time invariance, restatement replay, survivorship, and corporate action timing tests.

*Source: Priority 0a Super Report — Point-in-Time & No Future Leakage (December 2025\)*

## **4.5 Distributed Determinism**

Reproducibility is a tiered contract, not an all-or-nothing property. Different artifact classes require different levels of determinism:

| Tier | Guarantee | Applies To |
| :---- | :---- | :---- |
| D3: Bitwise | Byte-identical outputs | Orders, fills, positions, ledger, promotion decisions |
| D2: Semantic | Within explicit (rtol, atol) | NAV, returns, risk metrics, ML training artifacts |
| D1: Topological | Logically equivalent | Non-audit intermediate caches only |
| D0: None | Debug only | Never for promotion or audit |

**Three pillars:** Hierarchical seed derivation (master → run/fold/worker/strategy/asset via HMAC-SHA256), deterministic ordering (stable asset\_id \+ session index), and numeric policy (Decimal for cash/ledger, float64 for signals, Kahan summation for sensitive totals).

*Source: Priority 0b Super Report — Distributed Determinism & Parallel Semantics (December 2025\)*

## **4.6 Statistical Rigor**

Every backtest claim requires statistical validation before it can be considered credible:

* **Deflated Sharpe Ratio (DSR):** Adjusts for the number of trials and non-normality. Gate: FAIL if DSR \< 0 (strategy is likely a false discovery).

* **Bootstrap confidence intervals:** Block bootstrap preserving autocorrelation. Gate: WARN if 95% CI includes zero.

* **Minimum Track Record Length:** Estimates years needed for significance. SR \= 1.0 requires \~3.8 years at 95% confidence.

* **Multiple testing correction:** Benjamini-Hochberg FDR control when testing multiple strategy variants.

*Source: Research Agenda Priority 8 · Implementation Plan Appendix H (January 2026\)*

# **5\. Backtesting Infrastructure**

## **5.1 Run Bundle Pipeline**

A single command produces an auditable run\_bundle\_v1/ directory containing all manifests and gate results. The pipeline assembles plan.json (configuration \+ plan\_hash), env\_fingerprint.json (Python, git, deps, system, GPU), dataset\_manifest.json (data provenance \+ hashes), preprocessing\_report.json, splits\_manifest.json, and gate\_result.json.

python \-m srcPy.bridge.run\_pipeline tests/fixtures/sample\_spy.csv \--fast-sma 5 \--slow-sma 10

## **5.2 Time-Series Splits**

TimeSeriesSplitter implements walk-forward validation. PurgedKFold implements Marcos López de Prado’s purge and embargo methodology for financial cross-validation. Configurable purge and embargo windows prevent temporal contamination. 40 tests at 100% coverage.

## **5.3 Gate Runner CLI (mm-gate)**

Fail-closed artifact validation service for Spec Bundle v1 inputs. RFC8785 JCS canonicalization \+ SHA-256 for reproducible hashing. Multi-dialect JSON Schema validation (Draft-07/2020-12). Transfer report gating with Spearman ρ ≥ 0.70 and top-k overlap ≥ 0.60. 47 tests covering happy path, hash tampering, threshold violations, and determinism.

## **5.4 Gate CLI (srcPy/cli/gate.py)**

Bundle-level Appendix C/D v5.1 validation. Validates all 5 required bundle files per Appendix C.2. Implements plan\_identity gate with expected/actual evidence pattern. Enforces leakage invariants with purge gap verification. Exit codes: 0 \= PASS, 1 \= FAIL, 2 \= invalid input, 3 \= internal error. 42 tests.

## **5.5 Artifact Registry (CAS)**

Content-addressable storage with idempotent artifact registration and deduplication. Run state machine: REGISTERING → COMPLETE → FAILED with visibility controls (only COMPLETE runs queryable). Immutable artifact identity preserves provenance across deduplication. NaN/Infinity rejection with structured exception handling. 14 integration tests.

## **5.6 Lane A/B Multi-Fidelity**

Lane A provides rapid prototyping with zero or simplified costs. Lane B provides full order book simulation with realistic slippage and transaction costs. Comparability locks (data\_slice\_id, feature\_plan\_hash, strategy\_config\_hash, random\_seed) ensure valid cross-lane comparison. Only cost\_model and execution\_model differ between lanes.

# **6\. Desktop UI & Services**

JavaFX desktop application with Spring Boot services and AtlantaFX theming. The UI provides dashboard navigation, backtest controls, and a results card displaying validation status (PASS/FAIL), total return, Sharpe ratio, max drawdown, win rate, and trade count.

export DISPLAY=host.docker.internal:0

mvn compile \-DskipTests \-Dprotoc.skip=true \-Dcheckstyle.skip=true \-q

mvn javafx:run \-DskipTests \-Dprotoc.skip=true \-Dcheckstyle.skip=true

The Java service layer (BacktestService, PythonRunner) manages Python subprocess lifecycle, extracts JSON from mixed stdout/logging output, and maps exit codes to UI states.

# **7\. Tech Stack**

| Layer | Technologies |
| :---- | :---- |
| Languages | Python 3.12, C++20, Java 21 / JavaFX 21, Maven / Spring Boot 3.5 |
| ML & Compute | PyTorch, TensorFlow/Keras, ONNX, TensorRT, ORT, cuDF, CuPy, Polars |
| Data & I/O | pandas, Polars, PyArrow, yfinance, FRED API, InfluxDB, Redis |
| Validation | RFC8785 JCS, jsonschema (Draft-07/2020-12), Pandera, Pydantic, ruamel.yaml |
| QA & CI | pytest \+ Hypothesis, mypy \--strict, structlog, CodeQL, Dependabot, GitHub Actions |
| UI | JavaFX 21, AtlantaFX theming, FXML layouts, Scene Builder-compatible |
| Infrastructure | Poetry (Python), Maven (Java), Docker, protobuf/gRPC (planned) |

# **8\. Installation & Quickstart**

### **Prerequisites**

* Python 3.12+ with Poetry

* Java 21+ with Maven

* Git

### **Install**

git clone \<repo-url\> && cd MarketMind

poetry install                    \# Python dependencies

mvn compile \-DskipTests \-q        \# Java compilation

### **Run Pipeline**

python \-m srcPy.bridge.run\_pipeline tests/fixtures/sample\_spy.csv \--fast-sma 5 \--slow-sma 10

### **Run Desktop UI**

mvn javafx:run \-DskipTests \-Dprotoc.skip=true \-Dcheckstyle.skip=true

### **Run Tests**

poetry run pytest tests/python/ \-v                     \# All Python tests (150+)

poetry run pytest tests/python/property/ \-v            \# Hypothesis leakage tests

poetry run mypy marketmind\_gate \--strict               \# Type checking

# **9\. Project Structure**

Legend:  ✅ working & tested  ·  🚧 code exists, not fully pipelined  ·  🔮 spec or planned only

| Directory | Status | Description |
| :---- | :---- | :---- |
| srcPy/preprocessor/ | ✅ | Feature engineering: core.py, splits.py, graph/ engine. 80% coverage. |
| srcPy/backtest/ | ✅ | SMA crossover engine, BacktestResult, metrics computation. |
| srcPy/bridge/ | ✅ | run\_pipeline.py (\~450 lines) — bundle assembly \+ exit codes. |
| srcPy/cli/ | ✅ | gate.py (42 tests), preprocess.py, backtest.py CLI tools. |
| srcPy/strategies/ | 🚧 | stat\_arb.py (cointegration sketched), momentum.py. Not pipelined. |
| srcPy/artifact\_registry/ | ✅ | CAS storage, run state machine, dedup. 14 integration tests. |
| srcPy/pipeline/ | 🚧 | BatchPipeline, StepRegistry. Graph engine has bugs fixed. |
| srcPy/data/ | 🚧 | Async IBKR fetch with tests. No live streaming. |
| srcPy/ops/ | ✅ | Caching, logging, @instrument decorator, observability utilities. |
| marketmind\_gate/ | ✅ | mm-gate CLI: RFC8785, schema validation, promotion. 47 tests. |
| src/main/java/ | ✅ | JavaFX app, Spring Boot services, AtlantaFX theming. |
| cpp/ | 🔮 | InferenceJNI interface exists in Java. No native C++ library. |
| tests/ | ✅ | 150+ tests: unit, integration, property-based (Hypothesis). |
| policies/ | ✅ | gating\_policy.v1.yaml — gate runner policy definitions. |

# **10\. Testing & Quality**

### **Commands**

poetry run pytest tests/python/ \-v                     \# All Python tests

poetry run pytest tests/python/unit/gate/ \-v           \# Gate tests (42 \+ 19\)

poetry run pytest tests/python/unit/preprocessor/ \-v   \# Preprocessor tests

poetry run pytest tests/python/unit/backtest/ \-v       \# Backtest tests (10)

poetry run pytest tests/python/property/ \-v            \# Hypothesis leakage (20)

poetry run mypy marketmind\_gate \--strict               \# Type checking

### **Coverage & Quality**

* Preprocessor: 80% line / 92% branch coverage (target: 85% / 70%)

* mypy \--strict: 0 issues across 15 source files

* CI/CD: GitHub Actions validates mypy, pytest, and schema integrity on every push

### **Test Markers**

gpu, integration, perf, contract, executor, streaming, benchmark, smoke, regression, backtesting, provenance, lane\_a, lane\_b

# **11\. Performance SLOs**

Measured latencies vary by hardware and configuration. Replace with your telemetry snapshots.

| Component | p50 | p95 | p99 |
| :---- | :---- | :---- | :---- |
| GPU inference (single request) | 2 ms | 6 ms | 12 ms |
| Feature materialization (Polars/cuDF) | 5 ms | 25 ms | 80 ms |
| Cache hit (local Redis) | 0.5 ms | 2 ms | 8 ms |
| Artifact hash computation (RFC8785) | 1 ms | 5 ms | 15 ms |
| Gate validation (single bundle) | 50 ms | 200 ms | 500 ms |

*Illustrative targets — update with measured values from perf runs or telemetry.*

# **12\. Security & Privacy**

Draft — see Security Practices and Privacy Policy documentation for full details.

* gRPC-TLS by default for all inter-process communication

* Local-first processing: models and PII processed locally unless explicitly configured

* No PII/telemetry shipped by default; opt-in telemetry is gated and auditable

* Artifact integrity: SHA-256 hash verification prevents tampering with backtesting results

*Security and privacy documentation is marked Draft. This README avoids implying public open-source auditability; the project is proprietary.*

# **13\. Document Map**

MarketMind’s design is documented across 11 research and operational documents. This table serves as the canonical index for finding the right document for any question.

## **Operational Documents (Current State)**

| Document | Purpose | Version | Date |
| :---- | :---- | :---- | :---- |
| README (this document) | What works today, quickstart, project structure | v3.3.1 | Feb 2026 |
| VERSION.md | Release-by-release changelog | v3.3.0 | Feb 2026 |
| Implementation Plan | Phase definitions, priority stack, appendices C–M | v5.3 | Feb 2026 |
| Technical Roadmap | Feature inventory, research agenda, execution plan | v1.1 | Feb 2026 |

## **Architecture & Contract Documents (Dec 5–9, 2025\)**

| Document | Key Concepts |
| :---- | :---- |
| Research Agenda (Implementation Pack Ed.) | Priorities 0a–12 with dependency graph, done-when criteria, implementation packs |
| Priority 0a: PIT & Leakage | Bitemporal data, DataView.as\_of(T), safe joins, leakage CI battery |
| Priority 0b: Determinism | Tiers D0–D3, seed hierarchy, numeric policy, GPU knobs, env fingerprint |
| Plugin Architecture | 7 plugin types, Protocol signatures, manifests, Lane A/B locks, cache keys |
| Strategy I/O Contract v2 | Canonical IRs (Alpha/Target/Order/Fill), IGR lanes, Pandera/Pydantic |

## **Research Vision Documents (Dec 19, 2025\)**

| Document | Key Concepts |
| :---- | :---- |
| Unified Fidelity & MetaLearning Report | Lane 0–5 matrix, Autonomous Alpha Factory, meta-learning hierarchy, anti-Goodhart |
| Research Pack (3 unified reports) | Canonical IR (7-stage pipeline), data contracts, artifact governance, CAS scaling |

## **Quick Lookup**

| I need to… | Open this document |
| :---- | :---- |
| Add a new strategy plugin | Plugin Architecture → Strategy I/O Contract v2 |
| Add a new data source | Priority 0a (PIT contract \+ DataView API) |
| Understand lane fidelity | Fidelity Report (Lanes 0–5) \+ Plugin Arch (A/B locks) |
| Add a validation gate | Implementation Plan Appendices C–M |
| Fix a determinism issue | Priority 0b (tiers \+ seeds \+ numeric policy) |
| Plan Phase II work | Technical Roadmap \+ Research Agenda (priorities 0a–12) |
| Understand signal architecture | Research Pack (Canonical IR) \+ Strategy I/O v2 (Alpha IR) |
| Add statistical tests | Implementation Plan Appendix H \+ Research Agenda Priority 8 |
| Design position management | Strategy I/O v2 (IGR lanes: α/β/π/Ω) |
| Check acceptance criteria | Research Agenda (per-priority ‘Done When’) |

# **14\. Versioning & Changelog**

MarketMind follows Semantic Versioning (MAJOR.MINOR.PATCH). See VERSION.md for detailed release notes.

| Version | Date | Highlights |
| :---- | :---- | :---- |
| 3.3.0 | Feb 2026 | End-to-end pipeline, Gate CLI (42 tests), splits, 20 leakage property tests, preprocessor 56→80% |
| 3.2.0 | Dec 2025 | Gate Runner CLI (mm-gate), Artifact Registry (CAS), vertical slice smoke tests, CI/CD |
| 3.1.1 | Nov 2025 | Unified adaptive executor, surgical execute/skip policy, coverage gates tightened |

**Next:** 3.4.0 (Phase 0 complete: stat validity, CI baseline) → 4.0.0 (ML pipeline, C++ inference)

# **15\. License**

MarketMind is proprietary software (© 2025–2026 Mark Wuenschel. All rights reserved). Its source code is not open-source. MarketMind relies on third-party open-source libraries (NumPy, TensorFlow, ONNX Runtime, etc.) distributed under permissive licenses (MIT, BSD, Apache 2.0) which allow incorporation into proprietary products without copyleft restrictions. See the LICENSE file for full terms.

────────────────────────  
*Last updated: v3.3.1 · February 2026*