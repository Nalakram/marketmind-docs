# MarketMind 

![Status](https://img.shields.io/badge/status-early_development-orange)
![Version](https://img.shields.io/badge/version-3.1.1-blue)
[![Java 21](https://img.shields.io/badge/Java-21-007396?style=flat-square&logo=openjdk)](https://www.oracle.com/java/technologies/downloads/#java21)
[![Python 3.12](https://img.shields.io/badge/Python-3.12-3776AB?style=flat-square&logo=python)](https://www.python.org/)
[![Spring](https://img.shields.io/badge/Spring-3.5.0-6DB33F?style=flat-square&logo=spring&logoColor=white)](https://spring.io/)
![JavaFX 21](https://img.shields.io/badge/JavaFX-21-3873B3?style=flat-square)
![License](https://img.shields.io/badge/license-Proprietary-red)

**Algorithmic trading platform — under active development**

> ⚠️ **Early Development**: MarketMind is building toward a production trading platform.
> Many capabilities described in the [Vision](#vision) section are planned but not yet implemented.
> See [Current Status](#current-status) for what works today.

---

## Table of Contents
- [Current Status](#current-status)
- [What Works Today](#what-works-today)
- [Vision](#vision)
- [Architecture](#architecture)
- [Tech Stack](#tech-stack)
- [Roadmap](#roadmap)
- [Project Structure](#project-structure)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

---

## Current Status

**Version 3.1.1** — December 2025

| Component | Status | Notes |
|-----------|:------:|-------|
| JavaFX Desktop UI | ✅ | Spring Boot services integrated |
| Python Pipeline Framework | 🚧 | ~50% test coverage, preprocessing in progress |
| Gate Runner (Validation) | 🚧 | Framework implemented, test coverage in progress |
| Backtesting Engine | 🚧 | Design complete, Lane A/B architecture defined |
| C++ Inference Runtime | ❌ | Planned for Phase 3 |
| ML Model Training | ❌ | Planned for Phase 3 |
| Live Data Feeds | ❌ | Planned for Phase 3 |
| Automated Trading | ❌ | Planned for Phase 3 |

**Legend:** ✅ Working | 🚧 In Progress | ❌ Not Started

---

## What Works Today

### Prerequisites
- Python 3.12 with Poetry
- Java 21 (JDK) with Maven 3.8+
- (Optional) NVIDIA drivers + CUDA 12.x for GPU features

### Quick Start

```bash
# Clone the repository
git clone https://github.com/MindForgeLabs/MarketMind.git
cd MarketMind

# Install Python dependencies
poetry install

# Run tests
poetry run pytest -q

# Start Java UI (separate terminal)
mvn spring-boot:run
```

### What You Can Do
- **Run the test suite** to verify the codebase
- **Launch the JavaFX UI** for the desktop interface
- **Explore the pipeline framework** in `srcPy/pipeline/`
- **Review artifact validation** in `marketmind_gate/`

### What Doesn't Work Yet
- Model training and inference (no trained models exist)
- C++ runtime (not implemented)
- Live data feeds (not connected)
- Automated trade execution (not implemented)

---

## Vision

MarketMind aims to be a production-grade algorithmic trading platform combining:

- **Multi-fidelity backtesting** — Lane A (fast prototyping) and Lane B (production-realistic validation) with transfer gap analysis
- **Artifact governance** — Deterministic hashing, content-addressable storage, and fail-closed promotion gates
- **GPU-accelerated inference** — ONNX/TensorRT optimization with C++ serving for ultra-low latency
- **NLP pipelines** — News sentiment analysis using spaCy and BERTopic
- **Hybrid deep learning** — Multi-head Transformers combined with LSTM/TCN for time-series forecasting
- **Explainable AI** — SHAP values and feature importance for transparent decisions

*These capabilities are on the roadmap. See [Roadmap](#roadmap) for timeline.*

---

## Architecture

### Current State (v3.1.1)

```
┌──────────────────────────────┐
│      JavaFX Desktop UI       │  ✅ Implemented
│   (Spring Boot services)     │
└──────────────┬───────────────┘
               │ Local calls
               ▼
┌──────────────────────────────┐
│    Python Infrastructure     │  🚧 In Progress
│  • Pipeline framework        │
│  • Preprocessing steps       │
│  • Gate runner (validation)  │
└──────────────────────────────┘
```

### Target State (Phase 3+)

```
┌─────────────────┐        gRPC         ┌─────────────────────┐
│   JavaFX UI     │◄──────────────────►│  Python Orchestrator │
│ (Spring Boot)   │                     │  (pipelines/ML)      │
└─────────────────┘                     └──────────┬──────────┘
                                                   │
                                                   ▼
                                        ┌─────────────────────┐
                                        │   C++ Inference     │
                                        │  (ONNX/TensorRT)    │◄──► GPU
                                        └─────────────────────┘
```

---

## Tech Stack

### Currently Used

| Category | Technologies |
|----------|-------------|
| **Languages** | Python 3.12, Java 21 |
| **Frameworks** | Spring Boot 3.5.0, JavaFX 21, Poetry |
| **Data** | Polars, pandas |
| **Testing** | pytest, mypy --strict |
| **Build** | Maven, Poetry, CMake (stub) |

### Planned (Phase 3)

| Category | Technologies |
|----------|-------------|
| **ML Training** | PyTorch, TensorFlow/Keras |
| **Inference** | ONNX, TensorRT, ONNX Runtime |
| **GPU** | CUDA 12.x, cuDF, CuPy |
| **Serving** | C++20, Triton (optional) |
| **Data Stores** | InfluxDB, Redis |
| **Communication** | gRPC, protobuf |

---

## Roadmap

### Phase 0: Trust Foundation (Current)
*Target: Q1 2026*

- [ ] Gate framework test coverage → 70%+
- [ ] Preprocessing branch coverage → 85% line / 70% branch
- [ ] Integration canary (end-to-end pipeline test)
- [ ] Time-series splits with purge/embargo validation
- [ ] Deterministic artifact hashing

### Phase 1: Infrastructure
*Target: Q1-Q2 2026*

- [ ] Multi-fidelity backtesting (Lane A/B)
- [ ] Point-in-time data contracts
- [ ] Artifact registry with CAS deduplication
- [ ] Statistical validity gates

### Phase 2: Strategy Ecosystem
*Target: Q2 2026*

- [ ] Registry-driven strategy plugins (signal, sizing, risk, cost)
- [ ] Multi-strategy portfolio management
- [ ] Paper trading integration
- [ ] Performance attribution

### Phase 3: ML & Inference
*Target: Q3 2026*

- [ ] Model training pipeline
- [ ] ONNX export and TensorRT optimization
- [ ] C++ inference runtime
- [ ] GPU acceleration (cuDF → TensorRT)
- [ ] Live data feed integration

### Phase 4: Production
*Target: Q4 2026*

- [ ] Live trading with risk controls
- [ ] Meta-learning and strategy discovery
- [ ] NLP pipeline for news/sentiment
- [ ] Full observability and monitoring

---

## Project Structure

```
MarketMind/
├── srcPy/                  # Python: pipelines, preprocessing, validation
│   ├── pipeline/           # Pipeline framework and stages
│   ├── preprocessor/       # Feature engineering
│   ├── strategies/         # Strategy implementations (in progress)
│   ├── ops/                # Caching, logging, observability
│   └── data/               # Data loading and orchestration
├── marketmind_gate/        # Gate runner CLI (artifact validation)
├── src/                    # Java: JavaFX UI + Spring Boot services
├── cpp/                    # C++ backend (planned, stub only)
├── tests/                  # Test suites (Python, Java)
├── schemas/                # JSON Schema definitions
├── policies/               # Gating policies (YAML)
├── docs/                   # Documentation
├── pyproject.toml          # Poetry configuration
├── pom.xml                 # Maven configuration
└── CMakeLists.txt          # CMake configuration (stub)
```

---

## Testing

```bash
# Run all tests
poetry run pytest -q

# Run with coverage
poetry run pytest --cov=srcPy --cov=marketmind_gate --cov-branch

# Run specific markers
poetry run pytest -m "not slow"        # Skip slow tests
poetry run pytest -m integration       # Integration tests only
```

### Current Coverage

| Module | Line Coverage | Status |
|--------|:-------------:|--------|
| `srcPy/ops/` | ~75-80% | ✅ Good |
| `srcPy/strategies/` | ~77-92% | ✅ Good |
| `srcPy/preprocessor/graph/` | ~70-94% | ✅ Good |
| `srcPy/pipeline/` | ~30-70% | 🚧 Improving |
| `marketmind_gate/` | ~0% | ❌ Needs work |
| **Overall** | **~50%** | 🚧 Target: 85%+ |

### Test Markers
- `integration` — End-to-end tests
- `property` — Property-based tests (Hypothesis)
- `slow` — Long-running tests
- `gpu` — Requires GPU

---

## Configuration

Configuration files live in `data/` and environment variables:

```yaml
# data/config.yaml (example)
pipeline:
  cache_enabled: true
  parallelism: auto

logging:
  level: INFO
  format: structured
```

See `docs/configuration.md` for full reference.

---

## Contributing

MarketMind is **proprietary software**. Contributions are accepted from internal contributors or by prior arrangement only.

For contribution workflows:
1. Review `Programming Guidelines` in the repo
2. Ensure tests pass and coverage doesn't regress
3. Submit PR for mandatory review

---

## Versioning

MarketMind follows [Semantic Versioning](https://semver.org/):
- **MAJOR**: Breaking changes
- **MINOR**: New features (backward-compatible)
- **PATCH**: Bug fixes

Current release: **3.1.1**

See [Changelog](https://marketmind-docs.readthedocs.io/en/latest/CHANGELOG.html) for history.

---

## License

MarketMind is proprietary software.

© 2025 Mark Wuenschel. All rights reserved.

This software relies on third-party open-source libraries distributed under permissive licenses (MIT, BSD, Apache 2.0). See [LICENSE](LICENSE) for full terms.

---

*Last updated: December 2025 — v3.1.1*
