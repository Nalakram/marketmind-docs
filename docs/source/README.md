# MarketMind

Algorithmic Trading Platform  
README and Technical Overview

Version 4.4.1 · March 2026 · Proprietary  
Python 3.12 · C++20 · Java 21 / JavaFX · Spring Boot

Companion documents: `VERSION.md`, `GOVERNANCE.md`, `MODEL_CARD.md`, `PRIVACY_POLICY.md`, `RISK_DISCLOSURE.md`, `REPRODUCIBILITY.md`, `SECURITY.md`

## 1. Overview

**North Star:** Markets change, edges decay, and durable advantage comes from maintaining many weak signals and recombining them safely as regimes shift. MarketMind is built around that thesis. Signals and strategies are raw material; the product is the governed allocation and research system that can adapt without dissolving auditability, reproducibility, or point-in-time correctness.

### 3 Primitives

- **Signal Factory**: A governed engine that produces, versions, evaluates, promotes, and retires candidate signals and strategies.
- **Regime-Indexed Curriculum**: A training and evaluation distribution organized around historical market episodes and transitions.
- **Meta-Policy Allocator**: The adaptive allocation layer that consumes active signals plus regime context and outputs allocation weights and confidence-aware exposure control.

### Strategic Pillars

1. **Meta-policy as product**: Signals and strategies are inputs to a higher-order allocation system.
2. **Governance first**: Promotion requires reproducible evidence and fail-closed gates.
3. **Constraint-aware portfolio construction**: Costs, turnover, and risk are first-class evaluation inputs.
4. **Regime-indexed adaptation**: The system is designed to adapt across changing market structure.
5. **Breadth at scale**: Prefer many weak, diverse edges over a few brittle ones.
6. **Operational trust**: PIT correctness, determinism, lineage, and artifact identity are non-negotiable.
7. **Execution realism**: Execution and market microstructure are treated as product constraints, not afterthoughts.

## 2. Current Status

**Current published release:** 4.4.1

The 4.x series reflects the current governed research-system architecture:

- **4.0.x**: ADR-007 hashing contract, canonical hashing package, artifact-registry attestation facade, and repo-visible determinism terminology lock.
- **4.1.0**: Phase I-A PIT orchestration closure at the canonical backtest boundary.
- **4.2.0**: Phase I-B source adaptation into the governed PIT path, including PIT-ready Yahoo and explicit FRED vintage seams.
- **4.3.0**: Phase I-C single-path governed feature materialization and canonical execution lock.
- **4.4.0**: Phase I-D stat-arb pairs vertical slice on canonical PIT-safe plumbing.
- **4.4.1**: Companion-document synchronization through the delivered 4.3.0 and 4.4.0 state.

### Delivered 4.x Themes

- Governed feature execution now flows through a single canonical path.
- PIT-safe source adaptation and replay are part of the canonical backtesting boundary.
- Artifact identity, bundle evidence, and hashing contracts are explicit and versioned.
- The stat-arb package now exposes a canonical long-term package spine while keeping the live runtime pairs-only.

### Deferred Work

The current release line does **not** claim completion of Phase I-E / I-F work, full multi-leg stat-arb runtime, production deployment, or a finalized meta-learning product surface. Those remain governed by later releases.

## 3. Architecture Overview

MarketMind is a multilingual research and execution platform with:

- Python orchestration, preprocessing, strategy, and backtesting infrastructure
- C++20 for performance-critical inference and future low-latency paths
- Java 21 / JavaFX desktop UX with Spring Boot services
- Content-addressed artifact and attestation infrastructure

### Core Architectural Ideas

- **Functional Core / Imperative Shell**: Computational logic is pure where possible; side effects stay at the shell.
- **Canonical IR pipeline**: Strategy logic lowers into explicit typed plans rather than ad hoc runtime side effects.
- **Registry-driven composition**: Extensible capabilities resolve through explicit registries and governed contracts.
- **Point-in-time discipline**: Mutable data access flows through PIT-enforced boundaries.
- **Determinism tiers**: Reproducibility is specified as a contract, not a best effort.
- **Artifact governance**: Run bundles, manifests, and attestation are first-class runtime surfaces.

## 4. Design Commitments

### Point-in-Time Integrity

PIT discipline is enforced at the data boundary. Valid-time and knowledge-time rules are treated as hard contracts, not conventions.

### Determinism and Lineage

Results must be reproducible within defined determinism tiers and traceable through hashes, manifests, and run-bundle metadata.

### Gate-Oriented Development

A capability is not considered complete unless it emits evidence that can be validated by the project’s gates.

### Canonical Execution Paths

Temporary compatibility layers may exist, but each subsystem is expected to converge to one governed planning and execution path.

## 5. Backtesting, PIT, and Artifact Governance

The current architecture centers on a typed backtesting substrate and governed bundle production:

- Run bundles carry plan, environment, dataset, preprocessing, split, and validation artifacts.
- PIT-safe data views and adapters govern mutable market-data access.
- Bundle-level validation enforces deterministic and leakage-sensitive invariants.
- ADR-007 hashing distinguishes CAS identity from attestation identity while binding both to canonical payload bytes.

## 6. Project Shape

High-level repository areas in the private codebase include:

- `srcPy/`: preprocessing, PIT/data, backtesting, strategies, orchestration, ops, hashing, and artifact registry
- `marketmind_gate/`: gate-runner and validation tooling
- `src/main/java/`: JavaFX desktop UI and service layer
- `cpp/`: native performance and inference surfaces
- `tests/`: unit, integration, property, and contract suites

## 7. Governance, Security, and Privacy

MarketMind is proprietary software and the public/exported documentation must not imply broader usage rights than the license grants.

- Governance and model lifecycle are described in [Governance](GOVERNANCE.md)
- Safety, disclosure, and deployment caveats are described in [Risk Disclosure](RISK_DISCLOSURE.md)
- Privacy expectations are described in [Privacy Policy](PRIVACY_POLICY.md)
- Security posture and disclosure guidance are described in [Security Policy](SECURITY.md)
- Reproducibility expectations are described in [Reproducibility](REPRODUCIBILITY.md)

## 8. Document Map

This docs export is intentionally focused on canonical public or partner-facing material:

- `README.md`: current architecture and release-aligned technical overview
- `CHANGELOG.md`: published release ledger from root `VERSION.md`
- governance/legal suite: policy and disclosure documents exported from the private repo
- contributor engineering guidance: published programming guidelines
- `reference/`: secondary API reference surface retained for compatibility

## 9. Versioning

MarketMind follows Semantic Versioning. The release ledger for this docs export is rooted in [`VERSION.md`](CHANGELOG.md), and the current published top entry is **4.4.1** as of March 14, 2026.

## 10. License

MarketMind is proprietary software. Use, access, inspection, and disclosure are governed by the project license and companion governance/policy documents. See [License](LICENSE.md).
