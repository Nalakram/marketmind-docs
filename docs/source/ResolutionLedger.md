<!--
  MRL_VERSION: 1.0.6
  CODEBASE_VERSION: 4.9.0
  LAST_UPDATED: 2026-03-24
  MAINTAINER: Mark / MindForgeLabs
  SOURCE: Populated from MarketMind_ProjectState_v4_4_0.html
  STATUS_COUNTS_AUTO: false
  SCHEMA_NOTES:
    - AQ (Architectural Question) added as 8th first-class type; pre-ADR decision forks
    - RG-01..08 are stat_arb-scoped but preserved as RG for ID stability (see §2 note)
    - MLC sequence is 0..7 (8 entries), not 1..7 as initially specified
    - OI-MOM-NNN remapped to MOM-NNN; governing OI is OI-08
    - OI-17 recovered from malformed HTML row in ProjectState source
-->

**MarketMind**

────────────────────────────────

**Resolution Ledger**

<!-- MM:BEGIN:TITLEPAGE -->
Version 1.0.7 · March 2026 · Proprietary

Companion documents: Implementation Plan v6.4.15 · Technical Roadmap v1.4.16 · Meta-Learning Core v1.2.14 · Meta-Learning Architecture Vision v1.2.15 · README.md 4.9.1 · VERSION.md 4.9.1
<!-- MM:END:TITLEPAGE -->

<!-- MM:BEGIN:DOCBODY -->

---

# 1. Status Dashboard

## 1.1 Count Matrix

| Type  | OPEN | PARTIAL | BLOCKED | DEFERRED | CLOSED | SUPERSEDED | Total |
|-------|------|---------|---------|----------|--------|------------|-------|
| OI    | 14   | 1       | 0       | 1        | 24     | 0          | 40    |
| RG    | 9    | 4       | 0       | 0        | 0      | 0          | 13    |
| MLC   | 0    | 0       | 0       | 8        | 0      | 0          | 8     |
| MLN   | 7    | 0       | 0       | 0        | 0      | 0          | 7     |
| ADR   | 0    | 0       | 0       | 0        | 9      | 0          | 9     |
| GATE  | 4    | 0       | 0       | 1        | 8      | 0          | 13    |
| SI    | 0    | 0       | 0       | 0        | 0      | 0          | 0     |
| AQ    | 7    | 0       | 0       | 0        | 1      | 0          | 8     |
| SA    | 0    | 0       | 0       | 0        | 0      | 0          | 0     |
| MOM   | 2    | 0       | 0       | 12       | 10     | 0          | 24    |
| **∑** | **43** | **5** | **0** | **22**  | **52** | **0**      | **122** |

*MLN: 7 entries — Phase II normative locks and threshold-governance items are now opened to match the v2.0 meta-learning contracts and proof burden.*
*SA: 0 entries — stat_arb research gaps preserved as RG-01..08 for ID stability; SA prefix used for new stat_arb items going forward.*

## 1.2 Blocking Hotlist

Entries where `blocking: YES` AND `status ∈ {OPEN, PARTIAL}`. Sorted by phase.

| ID       | Title                                      | Status  | Phase | Gate(s)       | Depends On         |
|----------|--------------------------------------------|---------|-------|---------------|--------------------|
| OI-15    | 3-language golden-vector CI harness        | OPEN    | I-E   | —             | OI-13              |
| MOM-020  | CSMOM vs TSMOM vs dual-momentum comparison | OPEN    | I-E   | GATE-II-01    | OI-08              |
| OI-21    | F-3: ADR closure for Phase II-blocking seams | OPEN  | I-F   | GATE-I-F-03   | OI-20              |
| OI-22    | F-4: Phase II interface contract stubs     | OPEN    | I-F   | GATE-I-F-04   | OI-21              |
| OI-23    | F-5: Determinism boundary for ML entry     | OPEN    | I-F   | GATE-I-F-05   | OI-22              |
| OI-24    | F-6: Coverage / CI truthfulness audit      | OPEN    | I-F   | GATE-I-F-06   | OI-23              |
| MLN-01   | MetaTask and regime-episode contract       | OPEN    | II    | GATE-II-01    | OI-22              |
| MLN-02   | Regime vocabulary and 5-class projection   | OPEN    | II    | GATE-II-01    | MLN-01             |
| MLN-03   | Confidence routing contract                | OPEN    | II    | GATE-II-01    | MLN-01             |
| MLN-04   | Dynamic-K fixed-slot masking contract      | OPEN    | II    | GATE-II-01    | MLN-01             |
| MLN-05   | Frozen inference boundary                  | OPEN    | II    | GATE-II-01    | MLN-01             |
| MLN-06   | Phase II artifact contract                 | OPEN    | II    | GATE-II-01    | MLN-01             |
| MLN-07   | Threshold-resolution governance            | OPEN    | II    | GATE-II-01    | MLN-06             |
| RG-04    | stat_arb regime-conditional performance    | PARTIAL | II    | —             | AQ-03              |

## 1.3 Phase Gate Readiness

| Gate     | Phase | HALT Criteria Open | WARN Criteria Open | Gate Status |
|----------|-------|--------------------|--------------------|-------------|
| GATE-I-C | I-C   | 0                  | 0                  | CLOSED      |
| GATE-I-D | I-D   | 0                  | 0                  | CLOSED      |
| GATE-I-E | I-E   | 0                  | 0                  | CLOSED      |
| GATE-I-F | I-F   | 4                  | 0                  | OPEN        |
| GATE-II  | II    | 8+                 | 0                  | DEFERRED    |

## 1.4 Phase I-E Status — End of Thread

### Gate Summary

| Gate | Status | Evidence |
|---|---|---|
| GATE-I-E-01 | CLOSED | OI-02 disposition table recorded in this ledger; canonical storage ownership verified |
| GATE-I-E-03 | CLOSED ⚠️ | Momentum coverage confirmed at 97.5% line / 87.8% branch for `srcPy/strategies/momentum/`; full-repo global threshold run was not executed in this thread and remains explicitly unverified |
| GATE-I-E-04 | CLOSED | 10/10 D2 replay tests passed; `canonical_frame.py` evidence model updated truthfully to Python-only D2 |

### Coverage Numbers Confirmed In This Thread

| Scope | Line | Branch | Target | Result |
|---|---|---|---|---|
| `srcPy/strategies/momentum/` | 97.5% | 87.8% | 85% / 75% | ✅ Passes |
| Full repo (`srcPy/`) | Not run | Not run | 90% / 90% | ⚠️ Unverified |

### OI / MOM Closures Confirmed In This Thread

| ID | Title | Status |
|---|---|---|
| OI-02 | backtesting/storage/ retirement | CLOSED |
| OI-08 | Momentum Phase I slice | CLOSED |
| OI-13 | Hashing D2 stubs | CLOSED |
| MOM-007 | crash-trigger source decision | CLOSED (fail-closed) |
| MOM-008 | short-book constituent tagging | CLOSED (AlphaIR diagnostics) |
| MOM-010 | stat_validity v2 scope | CLOSED (v1 frozen) |
| MOM-011 | FDR trial counter accounting | CLOSED (shared family counter) |
| MOM-013 | ConvergenceError governed-path closeout | CLOSED |
| MOM-014 | CostGateRejection exit code mapping | CLOSED (exit 1 + COST_GATE_REJECTED reason code) |

### New Items Opened In This Thread

| ID | Title | Blocking | Phase |
|---|---|---|---|
| OI-34 | Governed crash-trigger source adapter (production) | NO | I-F |
| OI-32 | stat_validity v2 deferred extension | NO | II |
| OI-33 | Pre-existing strict-mypy backlog outside canonical I-F path | NO | I-F |

### Non-Blocking I-E Cleanup Status

| ID | Title | Status |
|---|---|---|
| OI-09 | omit list audit | CLOSED — coverage omit audit rebased to the live migrated surface; closed at v4.9.0 |
| OI-10 | pytest.mark.net mislabel | CLOSED — local-filesystem tests no longer hide behind a misleading net-only classification; closed at v4.9.0 |
| OI-16 | artifact_registry import migration | Not independently re-verified in this thread; canonical entry remains closed by earlier audit |
| OI-17 | _FEATURE_OPS retirement | CLOSED — direct governed `_FEATURE_OPS` execution retirement accepted on the canonical path at v4.9.0 |
| OI-27 | generate_signal() type boundary follow-through | CLOSED — confirmed by scoped strict mypy run on `srcPy/strategies/momentum/` + `srcPy/strategies/pipeline_strategy.py` (20 source files, 0 issues) |
| OI-30 | pytest tempdir Windows issue | Not confirmed in this thread |
| MOM-020 | CSMOM/TSMOM/dual variant comparison report | Not started — correctly gated on GATE-II-01, not I-E exit |

---

# 2. Phase 0 (CLOSED · v3.6.0 · Feb 2026)

### ADR-001 · Two-Stage Registry Lookup over Full Op Migration

```yaml
id:               ADR-001
type:             ADR
title:            Two-Stage Registry Lookup over Full Op Migration
status:           CLOSED
blocking:         NO
gates:            []
phase:            0
phase_links:      [I-C, I-D]
adr_status:       ACCEPTED
decision_date:    "2026-02-xx"
options_considered: [Option-A-two-stage-lookup, Option-B-full-migration]
decision:         >
  Option A: extend materialize_features() with two-stage lookup —
  _OP_REGISTRY first (graph path), _FEATURE_OPS fallback (legacy path).
  No migration of existing @feature_op functions.
consequences:
  - "@feature_op frozen — no new additions"
  - "Both registries coexist through Phase II — superseded by ADR-008 for long-term arch"
  - "New ops in _OP_REGISTRY only"
opened_on:        "v3.6.0"
resolved_on:      "v3.6.0"
owner:            unassigned
depends_on:       []
blocks:           []
related:          [ADR-008]
summary: >
  Bridge decision for 3.6.x transition period. Preserves 150+ existing tests by
  avoiding full migration of Numba-accelerated kernels. Unblocked stat_arb.py and
  momentum.py immediately. Superseded by ADR-008 with respect to long-term
  execution architecture; ADR-001 remains the correct record for the transition.
acceptance_criteria:
  - two-stage lookup implemented in materialize_features()
  - all pre-ADR-001 tests continue to pass
  - @feature_op additions frozen; deprecation tracking list initiated
evidence_needed:
  - adr-decision
  - code
  - tests
impact: ~
resolution: "Accepted v3.6.0. Bridge period ran through Phase I-C gate close (ADR-008 superseded for long-term arch at v4.3.0)."
```

### ADR-002 · Canonical Artifact Storage: Single System Designation

```yaml
id:               ADR-002
type:             ADR
title:            Canonical Artifact Storage — Single System Designation
status:           CLOSED
blocking:         NO
gates:            [GATE-I-E-01]
phase:            0
phase_links:      [I-E]
adr_status:       ACCEPTED
decision_date:    "2026-02-xx"
options_considered: [Option-A-single-canonical, Option-B-dual-system]
decision:         >
  srcPy/artifact_registry/ designated canonical (content-addressable, BLAKE3,
  atomic writes, integrity verify). backtesting/storage/ scoped or retired.
  bundle_manifest.json is the run-bundle reconstructibility contract.
consequences:
  - "backtesting/storage/ retirement is Phase I-E code-audit item (OI-02)"
  - "All new artifact writes go through LocalCAS + RunRegistry"
  - "Domain-qualified hash IDs frozen: cas.v1:b3-256, attest.v1:jcs-sha256"
opened_on:        "v3.6.0"
resolved_on:      "v3.6.0"
owner:            unassigned
depends_on:       []
blocks:           [OI-02]
related:          [ADR-007, OI-02]
summary: >
  Two artifact systems with incompatible identity semantics (content-hash vs.
  name/version) undermined provenance joinability, anti-Goodhart gates, crisis
  replay, and snapshot/rollback governance. Single canonical system designated.
acceptance_criteria:
  - srcPy/artifact_registry/ designated canonical with BLAKE3 CAS
  - bundle_manifest.json schema v1 frozen
  - domain-qualified hash ID format frozen
evidence_needed:
  - adr-decision
  - code
impact: ~
resolution: "Accepted v3.6.0. Consequence OI-02 (backtesting/storage/ retirement) remains open as of v4.4.0."
```

---

# 3. Phase I-A (CLOSED · v4.1.0 · 2026-03-11)

### OI-01 · ADR-005 canonical orchestration path

```yaml
id:               OI-01
type:             OI
title:            ADR-005 canonical orchestration path
status:           CLOSED
blocking:         NO
gates:            []
phase:            I-A
phase_links:      [I-D]
opened_on:        "v3.7.0"
resolved_on:      "v3.7.1"
owner:            unassigned
depends_on:       []
blocks:           []
related:          [ADR-005]
summary: >
  Canonical orchestration path needed before Phase I-D integration tests could
  be written. Three-layer structure required a formal ADR record.
acceptance_criteria:
  - ADR-005 accepted with three-layer structure
  - run_pipeline.py demoted to compatibility shim
  - companion docs updated to reflect new path
evidence_needed:
  - adr-decision
  - doc-update
impact: ~
resolution: "ADR-005 accepted v3.7.1. OI-01 closed."
```

### ADR-005 · Canonical Orchestration Path

```yaml
id:               ADR-005
type:             ADR
title:            Canonical Orchestration Path — java_entry + orchestrator + suite_runner
status:           CLOSED
blocking:         NO
gates:            []
phase:            I-A
phase_links:      [I-D, I-F]
adr_status:       ACCEPTED
decision_date:    "2026-03-09"
options_considered: [three-layer-canonical, single-orchestrator, dual-path]
decision:         >
  Three-layer structure: srcPy/bridge/java_entry.py (Java-facing adapter),
  srcPy/pipeline/orchestrator.py (canonical bundle-producing engine),
  srcPy/backtesting/orchestration/suite_runner.py (suite coordinator).
  run_pipeline.py is now a compatibility shim.
consequences:
  - "Phase I-D integration tests written against pipeline/orchestrator.py"
  - "PIT orchestration wired at canonical boundary in v4.1.0"
  - "Suite runner remains stub until multi-run orchestration is undertaken"
opened_on:        "v3.7.0"
resolved_on:      "v3.7.1"
owner:            unassigned
depends_on:       []
blocks:           []
related:          [OI-01, ADR-008]
summary: >
  DataView.as_of(T) must integrate into one canonical bundle-producing path.
  Half-wiring into parallel paths creates provenance ambiguity and dual test
  targets. Three-layer structure locks the canonical boundary.
acceptance_criteria:
  - java_entry.py, orchestrator.py, suite_runner.py structure in place
  - run_pipeline.py relegated to shim with documented rationale
  - companion docs (README, Implementation Plan, Roadmap) updated
evidence_needed:
  - adr-decision
  - code
  - doc-update
impact: ~
resolution: "Accepted v3.7.1. Companion docs synced at v3.8.1."
```

### ADR-007 · Hashing Contract — HashRef Envelope, D-Tier Taxonomy

```yaml
id:               ADR-007
type:             ADR
title:            Hashing Contract — Purpose-Bound Algorithms, HashRef Envelope, D-Tier Taxonomy
status:           CLOSED
blocking:         NO
gates:            []
phase:            I-A
phase_links:      [I-E, I-F]
adr_status:       ACCEPTED
decision_date:    "2026-03-10"
options_considered: [purpose-bound-canonical, bare-hex, unified-hash]
decision:         >
  Canonical hashing package under srcPy/ops/hashing/. HashPurpose→algorithm
  bindings are load-time constants. HashRef 8-field envelope mandatory in all
  persistent contexts; bare hex banned. Composite preimage locked as
  SystemInvariant.DOMAIN_SEPARATED_PREIMAGE. D-tier taxonomy: D3=Bitwise,
  D2=Semantic, D1=Topological, D0=None/Debug.
consequences:
  - "All primitives capped at D2 until 3-language golden-vector CI harness wired (OI-15)"
  - "srcPy/ops/artifact_registry.py import sites must migrate to srcPy/artifact_registry/ (OI-16)"
  - "Pre-ADR-007 D0-Bitwise labelling superseded"
  - "OI-13, OI-14, OI-15, OI-16 opened"
opened_on:        "v3.8.0"
resolved_on:      "v4.0.0"
owner:            unassigned
depends_on:       []
blocks:           [OI-13, OI-15]
related:          [OI-13, OI-14, OI-15, OI-16, ADR-002]
summary: >
  Prevents silent algorithm rebinding across language boundaries, enforces domain
  separation for CAS vs attestation vs cache surfaces, and provides stable
  determinism vocabulary for CI certification. 4,314-line scaffold generated with
  9 NotImplementedError stubs.
acceptance_criteria:
  - HashRef 8-field envelope enforced in all persistent hash contexts
  - HashPurpose→algorithm bindings are load-time constants
  - D-tier taxonomy (D0..D3) adopted repo-wide in gate language
  - 9 primitive stubs scaffold generated under srcPy/ops/hashing/
evidence_needed:
  - adr-decision
  - code
impact: ~
resolution: "Accepted v4.0.0. 9 primitive stubs remain open (OI-13). Golden-vector CI wiring open (OI-15)."
```

---

# 4. Phase I-B (CLOSED · 2026-03-1x)

### OI-04 · yahoo_fetcher.py

```yaml
id:               OI-04
type:             OI
title:            yahoo_fetcher.py — daily OHLCV source adapter
status:           CLOSED
blocking:         NO
gates:            []
phase:            I-B
phase_links:      []
opened_on:        "v3.8.0"
resolved_on:      "v4.2.0"
owner:            unassigned
depends_on:       []
blocks:           []
related:          [OI-05]
summary: >
  Yahoo Finance daily OHLCV source adapter required for governed source path.
  Needed ≥5yr history, ≥10 symbols, Parquet output, bitemporal columns.
acceptance_criteria:
  - yahoo_fetcher.py ships with ≥5yr history support and ≥10 symbols
  - Parquet output with valid_time/knowledge_time bitemporal columns
  - 100%/100% coverage
evidence_needed:
  - code
  - tests
impact: ~
resolution: "Shipped Phase I-B. 100%/100% coverage. Bitemporal columns PIT-safe under DataView.as_of(T)."
```

### OI-05 · FRED ALFRED vintage seam

```yaml
id:               OI-05
type:             OI
title:            FRED ALFRED vintage seam stub
status:           CLOSED
blocking:         NO
gates:            []
phase:            I-B
phase_links:      [II]
opened_on:        "v3.8.0"
resolved_on:      "v4.2.0"
owner:            unassigned
depends_on:       []
blocks:           []
related:          [RG-12]
summary: >
  Stub seam in fred.py for macro vintage-aware knowledge_time. Full ALFRED
  vintage implementation deferred to Phase II (RG-12 open). Seam makes
  the approximation explicit rather than silent.
acceptance_criteria:
  - FREDVintageSeam and FREDApproximationStub present in fred.py
  - approximation is explicitly named, not silent
  - RG-12 opened to track full ALFRED vintage work
evidence_needed:
  - code
impact: ~
resolution: "Seam shipped Phase I-B. RG-12 open for full vintage accuracy work."
```

### OI-11 · Companion doc sync v3.8.x

```yaml
id:               OI-11
type:             OI
title:            Companion doc sync for v3.8.x
status:           CLOSED
blocking:         NO
gates:            []
phase:            I-B
phase_links:      []
opened_on:        "v3.8.0"
resolved_on:      "v3.8.1"
owner:            unassigned
depends_on:       []
blocks:           []
related:          [OI-18]
summary: >
  README, Implementation Plan, Technical Roadmap synced to backtesting substrate
  state at v3.8.1. ADR-005 + orchestration reflected. v4.x drift is OI-18.
acceptance_criteria:
  - README, Implementation Plan, Roadmap updated to v3.8.x state
  - ADR-005 three-layer path reflected in companion docs
evidence_needed:
  - doc-update
impact: ~
resolution: "Synced at v3.8.1. Subsequent drift tracked as OI-18."
```

---

# 5. Phase I-C (CLOSED · v4.3.0 / v4.4.0 · 2026-03-13)

### GATE-I-C-01 · Phase I-C gate (all 7 conditions)

```yaml
id:               GATE-I-C-01
type:             GATE
title:            Phase I-C gate — all 7 conditions
status:           CLOSED
blocking:         NO
gates:            []
phase:            I-C
phase_links:      []
gate_section:     "Phase I-C exit"
pass_condition: >
  All 7 gate conditions pass: single-path execution lock, canonical op floor
  (10 technical ops), leakage battery ≥30 invariants, PIT-safe graph execution,
  MaterializationError on governed direct _FEATURE_OPS use, and ADR-008 accepted.
fail_mode:        HALT
opened_on:        "v4.0.0"
resolved_on:      "v4.4.0"
owner:            unassigned
depends_on:       []
blocks:           []
related:          [ADR-008, OI-06]
summary: >
  Phase I-C exit gate. All 7 conditions passed at v4.4.0: 39 combined
  leakage/PIT invariants (20+7+12), 10 canonical ops exercised, ADR-008 accepted.
acceptance_criteria:
  - 39 combined leakage/PIT invariants across three property suites
  - 10 canonical technical ops exercised (SMA/EMA/RSI/MACD/Bollinger/ATR/OBV/VWAP/rolling_std/zscore_roll)
  - MaterializationError raised on governed direct _FEATURE_OPS use
  - ADR-008 accepted
evidence_needed:
  - tests
  - adr-decision
impact: ~
resolution: "All 7 conditions PASS at v4.4.0."
```

### OI-06 · Preprocessor leakage battery extension

```yaml
id:               OI-06
type:             OI
title:            Preprocessor leakage battery — extend to ≥30 invariants
status:           CLOSED
blocking:         NO
gates:            [GATE-I-C-01]
phase:            I-C
phase_links:      []
opened_on:        "v4.0.0"
resolved_on:      "v4.4.0"
owner:            unassigned
depends_on:       []
blocks:           []
related:          [ADR-008]
summary: >
  Phase 0 shipped 20 Hypothesis tests (5 invariants) covering splits layer only.
  Phase I-C gate required ≥30 combined invariants covering preprocessor-level
  leakage and PIT boundary enforcement.
acceptance_criteria:
  - ≥30 combined leakage/PIT invariants across test suites
  - invariants cover splits layer, DataView PIT, and preprocessor leakage
evidence_needed:
  - tests
impact: ~
resolution: "39 combined invariants at v4.4.0 across test_leakage_invariants.py (20), test_dataview_pit.py (7), test_preprocessor_leakage.py (12)."
```

### ADR-008 · Single-Path Feature Execution Lock

```yaml
id:               ADR-008
type:             ADR
title:            Single-Path Feature Execution Lock — planner/executor canonical, _FEATURE_OPS lowering-only
status:           CLOSED
blocking:         NO
gates:            [GATE-I-C-01]
phase:            I-C
phase_links:      [I-D, I-E, II]
adr_status:       ACCEPTED
decision_date:    "2026-03-13"
options_considered: [single-path-lock, continued-dual-path, gradual-migration]
decision:         >
  All feature execution canonicalized through _OP_REGISTRY + planner/executor
  lowering. _FEATURE_OPS is compatibility-lowering only — may parse/translate
  legacy requests but may not execute feature computation directly. New feature
  operators register in _OP_REGISTRY only. Feature execution over governed data
  must consume DataView / PIT-safe inputs. Direct _FEATURE_OPS execution
  removed only once equivalent lowering coverage and tests exist.
consequences:
  - "PIT boundary enforcement and single-path feature execution are permanent architecture rules"
  - "_FEATURE_OPS direct execution is technical debt with a defined retirement condition (OI-17)"
  - "Supersedes ADR-001 with respect to long-term execution architecture"
opened_on:        "v4.3.0"
resolved_on:      "v4.4.0"
owner:            unassigned
depends_on:       [ADR-001]
blocks:           [OI-17]
related:          [ADR-001, OI-06, OI-17]
summary: >
  Formalizes the endpoint Phase I-C rules were pushing toward. Removes dual-
  execution-path ambiguity from ADR-001 bridge period. Supersedes ADR-001 for
  long-term architecture only; ADR-001 bridge decision remains the correct
  record for the 3.6.x transition period. Implemented 2026-03-13.
acceptance_criteria:
  - MaterializationError raised on direct _FEATURE_OPS governed use
  - all Phase I-C canonical ops registered in _OP_REGISTRY and exercised via graph path
  - ADR document published and marked ACCEPTED
  - no new additions to _FEATURE_OPS
evidence_needed:
  - adr-decision
  - code
  - tests
impact: ~
resolution: "Accepted v4.4.0. OI-17 (_FEATURE_OPS retirement) opened as defined retirement condition."
```

---

# 6. Phase I-D (CLOSED · v4.4.0 · 2026-03-1x)

### GATE-I-D-01 · stat_arb on real DataView-backed data

```yaml
id:               GATE-I-D-01
type:             GATE
title:            stat_arb runs on real DataView-backed historical data
status:           CLOSED
blocking:         NO
gates:            []
phase:            I-D
phase_links:      []
gate_section:     "Phase I-D exit"
pass_condition: >
  stat_arb.py runs end-to-end on historical DataView-backed inputs.
  sample_spy.csv fixture halt gate passed.
fail_mode:        HALT
opened_on:        "v4.3.0"
resolved_on:      "v4.4.0"
owner:            unassigned
depends_on:       [OI-07]
blocks:           []
related:          [OI-07]
summary: Phase I-D exit gate. Passed at v4.4.0.
acceptance_criteria:
  - StatArbStrategy runs on DataView-backed historical data
  - sample_spy.csv fixture halt gate passes
  - coverage targets met for I-D scope files
evidence_needed:
  - code
  - tests
impact: ~
resolution: "PASS at v4.4.0. Global I-B+I-C+I-D: 95.72% line / 86.94% branch."
```

### OI-07 · stat_arb.py

```yaml
id:               OI-07
type:             OI
title:            stat_arb.py — StatArbStrategy vertical slice
status:           CLOSED
blocking:         NO
gates:            [GATE-I-D-01]
phase:            I-D
phase_links:      [I-E, II]
opened_on:        "v4.3.0"
resolved_on:      "v4.4.0"
owner:            unassigned
depends_on:       [ADR-005, ADR-008]
blocks:           []
related:          [RG-01, RG-02, RG-04, SA-prefix-registry]
summary: >
  StatArbStrategy as PipelineStrategy subclass. Pairs: beta, spread, z-score,
  half-life. Registered as stat_arb_pairs. Runs on DataView-backed historical
  data. ops_custom.py branch coverage 76% noted — OI-13 hashing pre-req is
  likely cause.
acceptance_criteria:
  - StatArbStrategy implemented as PipelineStrategy subclass
  - pairs: beta, spread, z-score, half-life on canonical graph path
  - registered as stat_arb_pairs
  - runs on DataView-backed historical data end-to-end
evidence_needed:
  - code
  - tests
impact: ~
resolution: "Shipped Phase I-D v4.4.0. stat_arb/pairs.py 100%/100%, stat_arb/entry.py 92.45%/80%. ops_custom.py branch 76% — see OI-13."
```

---

# 7. Phase I-E (NEXT — Active)

## Gate Criteria

### GATE-I-E-01 · backtesting/storage/ retired or marked retired-with-rationale

```yaml
id:               GATE-I-E-01
type:             GATE
title:            backtesting/storage/ retired or marked retired-with-rationale
status:           CLOSED
blocking:         YES
gates:            []
phase:            I-E
phase_links:      []
gate_section:     "I-E exit"
pass_condition: >
  All backtesting/storage/ call sites and tests have been migrated to
  srcPy/artifact_registry/ or explicitly marked retired-with-rationale.
  No new artifact writes going to old path.
fail_mode:        HALT
opened_on:        "v4.4.0"
resolved_on:      "v4.5.4"
owner:            unassigned
depends_on:       [OI-02]
blocks:           []
related:          [ADR-002, OI-02]
summary: >
  ADR-002 consequence. Any new artifact writes still going to old path after
  ADR-002 blocks I-E gate closure.
acceptance_criteria:
  - all backtesting/storage/ call sites audited
  - migrated or marked retired-with-rationale
  - no new writes to old path
  - OI-02 closed
evidence_needed:
  - code
  - doc-update
impact: >
  Dual artifact path violates ADR-002. Provenance joinability and crisis replay
  are compromised while old path remains live.
resolution: "Closed at v4.5.4. Implementation ownership now lives in srcPy/artifact_registry/, with backtesting/storage/bundle_writer.py and artifact_store.py retired-with-rationale shims, artifacts.py and sanitization.py retired compatibility shims, registry_store.py a documented retired placeholder, and test imports migrated to the canonical path."
```

### GATE-I-E-02 · DataLineageGate implemented and wired

```yaml
id:               GATE-I-E-02
type:             GATE
title:            DataLineageGate implemented and wired to dataset_manifest.json
status:           CLOSED
blocking:         YES
gates:            []
phase:            I-E
phase_links:      []
gate_section:     "I-E exit"
pass_condition: >
  DataLineageGate reads dataset_manifest.json PIT flags and fails if canonical
  source lineage did not pass through DataView.
fail_mode:        HALT
opened_on:        "v4.4.0"
resolved_on:      "v4.5.1"
owner:            unassigned
depends_on:       [OI-03]
blocks:           []
related:          [ADR-005, OI-03]
summary: New gate required as Phase I-E primary deliverable. OI-03 must close first.
acceptance_criteria:
  - DataLineageGate reads dataset_manifest.json PIT flags
  - gate fails closed if source lineage bypassed DataView
  - wired to canonical bundle-producing path
  - OI-03 closed
evidence_needed:
  - code
  - tests
impact: >
  Without DataLineageGate, PIT boundary enforcement is incomplete at the
  dataset-provenance level — leaks can occur downstream of the gate.
resolution: "Closed at v4.5.1. DataLineageGate is implemented on the canonical governed path in srcPy/cli/gate.py, validates dataset_manifest lineage fields, fail-closes on missing PIT lineage, and records warning-only stale-download evidence."
```

### GATE-I-E-03 · momentum package Phase I slice delivered

```yaml
id:               GATE-I-E-03
type:             GATE
title:            momentum package Phase I slice — 3 production variants delivered
status:           CLOSED
blocking:         YES
gates:            []
phase:            I-E
phase_links:      [II]
gate_section:     "I-E exit"
pass_condition: >
  MomentumStrategy with 3 Phase I production-intended variants (momentum,
  momentum_tsmom, momentum_dual) delivered. AlphaIR output, task_embedding
  zero-stub, and phase-blocking OI-MOM items resolved.
fail_mode:        HALT
opened_on:        "v4.4.0"
resolved_on:      "v4.5.4"
owner:            unassigned
depends_on:       [OI-08, MOM-007, MOM-008, MOM-009, MOM-010, MOM-011, MOM-013, MOM-014]
blocks:           []
related:          [OI-08]
summary: >
  OI-08 and all Phase I (I-E) blocking OI-MOM items must be resolved.
  Coverage target: 85% line / 75% branch. MOM-020 (CSMOM vs TSMOM comparison)
  must be complete before Phase II entry.
acceptance_criteria:
  - srcPy/strategies/momentum/ ships with momentum, momentum_tsmom, momentum_dual variants
  - AlphaIR output present; task_embedding zero-stub (np.zeros(64, float32))
  - all OI-MOM items with Blocking Phase I-E resolved
  - coverage ≥85% line / ≥75% branch
  - stat_validity_report.json locked to the canonical v1 contract; deferred v2 work tracked separately
evidence_needed:
  - code
  - tests
impact: >
  momentum package is a required training task for the Reptile outer loop. Phase II
  task pool is insufficient without it. MOM-020 blocks Phase II entry gate.
resolution: "Closed at v4.5.4 for Phase I-E. The governed momentum package now shares one production trial counter family across xsec/tsmom/dual, emits canonical v1 stat_validity_report.json, surfaces COST_GATE_REJECTED through gate_result.json, and carries short-book tagging plus fail-closed beta_reversal diagnostics inside AlphaIR. Focused momentum coverage was later confirmed at 97.5% line / 87.8% branch in this thread; the full-repo global threshold run was not executed here and remains explicitly unverified."
```

### GATE-I-E-04 · Hashing infrastructure closure

```yaml
id:               GATE-I-E-04
type:             GATE
title:            Hashing infrastructure — stubs implemented, CI flag present
status:           CLOSED
blocking:         YES
gates:            []
phase:            I-E
phase_links:      [I-F]
gate_section:     "I-E exit"
pass_condition: >
  9 hashing primitive stubs implemented per ADR-007 invariants. canonical_frame.py
  carries machine-readable CI status flag. All D2 primitives pass unit tests.
fail_mode:        HALT
opened_on:        "v4.4.0"
resolved_on:      "v4.5.4"
owner:            unassigned
depends_on:       [OI-13, OI-14]
blocks:           []
related:          [ADR-007, OI-13, OI-14, OI-15]
summary: >
  OI-13 (stubs) and OI-14 (CI flag) both required. OI-15 (3-language harness)
  is not required for I-E gate but is required before D3 promotion.
acceptance_criteria:
  - all 9 stubs implemented with ADR-007 invariants enforced
  - canonical_frame.py carries machine-readable CI status flag
  - D2 primitives pass unit tests
  - ops_custom.py branch coverage gap resolved (currently 76%, below 80%)
evidence_needed:
  - code
  - tests
impact: >
  ops_custom.py branch coverage at 76% is a direct consequence of hashing stubs.
  Gate automation requires machine-readable CI flag. D3 promotion blocked across
  all three runtimes until OI-15 is wired.
resolution: "Closed at v4.5.4 for D2 evidence. The ADR-007 fixture suites now carry concrete replay expectations, a Python replay suite covers the eight committed golden-vector suites, 10/10 focused D2 replay tests passed in this thread, canonical_frame.py truthfully reports python_only_d2 with golden_vectors_present=true, and OI-15 remains the explicit blocker for any D3 cross-language claim."
```

## Open Items

### OI-02 · backtesting/storage/ retirement

```yaml
id:               OI-02
type:             OI
title:            backtesting/storage/ retirement
status:           CLOSED
blocking:         YES
gates:            [GATE-I-E-01]
phase:            I-E
phase_links:      []
opened_on:        "v4.4.0"
resolved_on:      "v4.5.4"
owner:            unassigned
depends_on:       []
blocks:           []
related:          [ADR-002]
summary: >
  ADR-002 consequence. All backtesting/storage/ call sites and tests must be
  migrated to srcPy/artifact_registry/ or marked retired-with-rationale.
  Primary I-E deliverable.
acceptance_criteria:
  - all call sites in backtesting/storage/ audited and catalogued
  - each call site either migrated to artifact_registry/ or marked retired-with-rationale
  - no new artifact writes to old path post-audit
  - test suite updated to reflect migration
evidence_needed:
  - code
  - tests
  - doc-update
impact: >
  Dual artifact path violates ADR-002 provenance contract. Blocks GATE-I-E-01
  and Phase I-E exit.
resolution: "Closed at v4.5.4. Real BundleWriter and BundleBacktestArtifactStore ownership moved into srcPy/artifact_registry/, all remaining backtesting/storage files are now retired compatibility shims or placeholders with explicit rationale, and the legacy test import surface was migrated to the canonical artifact-registry helpers."
```

Storage disposition recorded for the `OI-02` closeout:

| Legacy path | Disposition | Canonical owner / note |
|---|---|---|
| `srcPy/backtesting/storage/bundle_writer.py` | `RETIRED-WITH-RATIONALE` shim | Delegates to `srcPy/artifact_registry/bundle_writer.py` |
| `srcPy/backtesting/storage/artifact_store.py` | `RETIRED-WITH-RATIONALE` shim | Delegates to `srcPy/artifact_registry/artifact_store.py` |
| `srcPy/backtesting/storage/artifacts.py` | Compatibility shim | Canonical helpers live in `srcPy/artifact_registry/artifacts.py` |
| `srcPy/backtesting/storage/sanitization.py` | Compatibility shim | Canonical helpers live in `srcPy/artifact_registry/sanitization.py` |
| `srcPy/backtesting/storage/registry_store.py` | Retired placeholder | No live implementation remains in the legacy namespace |

### OI-03 · DataLineageGate

```yaml
id:               OI-03
type:             OI
title:            DataLineageGate — new gate reading dataset_manifest.json PIT flags
status:           CLOSED
blocking:         YES
gates:            [GATE-I-E-02]
phase:            I-E
phase_links:      []
opened_on:        "v4.4.0"
resolved_on:      "v4.5.1"
owner:            unassigned
depends_on:       []
blocks:           []
related:          [ADR-005, ADR-008]
summary: >
  New gate required for Phase I-E. Reads dataset_manifest.json PIT flags and
  fails closed if canonical source lineage did not pass through DataView.
  Primary I-E deliverable alongside OI-02.
acceptance_criteria:
  - DataLineageGate class implemented in gate infrastructure
  - reads dataset_manifest.json PIT flags
  - fails closed (not open) when PIT lineage is missing or invalid
  - wired to canonical bundle-producing path (ADR-005 path)
  - unit tests: pass case, fail case, missing manifest case
evidence_needed:
  - code
  - tests
impact: >
  Without this gate, a dataset that bypassed DataView can silently produce
  look-ahead-contaminated results that no other gate catches.
resolution: "Closed at v4.5.1. DataLineageGate reads dataset_manifest PIT flags and lineage evidence, fails closed on missing governed lineage, and is wired to the ADR-005 canonical bundle path."
```

### OI-08 · momentum package

```yaml
id:               OI-08
type:             OI
title:            momentum package — MomentumStrategy Phase I implementation
status:           CLOSED
blocking:         YES
gates:            [GATE-I-E-03]
phase:            I-E
phase_links:      [II]
opened_on:        "v4.4.0"
resolved_on:      "v4.5.4"
owner:            unassigned
depends_on:       [MOM-007, MOM-008, MOM-009, MOM-010, MOM-011, MOM-013, MOM-014]
blocks:           [MOM-020]
related:          [OI-07, OI-27, OI-28]
summary: >
  Core slice now lives on the ADR-009 package spine at
  srcPy/strategies/momentum/. MomentumStrategy, AlphaIR, explicit registry
  wiring, PIT guard enforcement, variant-specific feature planning,
  momentum-specific entry/artifact serialization, and trade-intent unwrapping
  via AlphaIR.signal have landed. Momentum graph ops (XSecRank, VolScale,
  ResidualOLS, ResidualKF stub/fail-closed, IndustryScore Phase II stub) are
  wired through ops_custom.py and factory.py. Focused momentum/unit/integration
  tests passed, and the remaining MOM blockers for the Phase I-E slice are now
  closed. The ADR-009 package spine migration is closed under OI-28. The
  generate_signal() type-boundary follow-through is separately closed under
  OI-27 for the I-F wiring audit.
acceptance_criteria:
  - srcPy/strategies/momentum/ ships with momentum, momentum_tsmom, momentum_dual variants
  - AlphaIR output present; task_embedding zero-stub (np.zeros(64, float32))
  - all OI-MOM items with Blocking Phase I-E resolved
  - coverage >=85% line / >=75% branch
  - stat_validity_report.json aligned to the canonical v1 gate contract with deferred v2 follow-on tracked separately
  - full repo test suite passes
  - type: ignore[override] bridge resolved (OI-27)
evidence_needed:
  - code
  - tests
impact: >
  Required training task for Reptile outer loop. Without the momentum Phase I
  slice, task pool is insufficient for Phase II. MOM-020 blocks Phase II entry.
resolution: "Closed at v4.5.4 for Phase I-E. The package spine now closes the remaining MOM blockers by failing crash overrides closed pending a governed adapter (now **OI-34**), carrying short-book diagnostics inside AlphaIR, reverting stat_validity_report.json to canonical v1 pending OI-32, using a shared non-resettable RunRegistry trial counter family for xsec/tsmom/dual, and emitting COST_GATE_REJECTED through the canonical gate_result path. `generate_signal()` typing was later closed under **OI-27** / **OI-31** (StrategySignal / AlphaIR)."
```

### OI-09 · pyproject.toml coverage omit list

```yaml
id:               OI-09
type:             OI
title:            pyproject.toml coverage omit list — sources/* revisit
status:           CLOSED
blocking:         NO
gates:            [GATE-I-F-06]
phase:            I-E
phase_links:      [I-F]
opened_on:        "v4.0.0"
resolved_on:      "v4.9.0"
owner:            unassigned
depends_on:       []
blocks:           []
related:          [OI-24]
summary: >
  srcPy/pipeline/stages/market_data/sources/* in omit list. Revisit once
  file.py is wired into main test suite. Omit rules should reflect actual
  coverage intent, not historical accidents.
acceptance_criteria:
  - omit list audited against current Phase I-E deliverables
  - sources/* entry removed or justified with named rationale
  - any stale omit rules removed
evidence_needed:
  - doc-update
impact: >
  Stale omit rules silently undercount coverage. If sources/* contains live
  Phase I code, the 90% threshold is being met against a smaller surface than
  declared.
resolution: >
  Closed at v4.9.0. The omit audit no longer treats `sources/*` as a blanket
  excluded surface. Broad historical patterns were narrowed to the live migrated
  package surface so coverage accounting reflects the actual Phase I codebase.
  Residual CI/coverage truthfulness work continues under OI-24 / GATE-I-F-06.
```

### OI-10 · pytest.mark.net mislabel

```yaml
id:               OI-10
type:             OI
title:            pytest.mark.net mislabel on local filesystem tests
status:           CLOSED
blocking:         NO
gates:            [GATE-I-F-06]
phase:            I-E
phase_links:      [I-F]
opened_on:        "v4.0.0"
resolved_on:      "v4.9.0"
owner:            unassigned
depends_on:       []
blocks:           []
related:          [OI-24]
summary: >
  test_file_source_bitemporal.py tests are purely local filesystem but carry
  pytest.mark.net. May cause offline CI skips, understating coverage on local
  runs without network.
acceptance_criteria:
  - test_file_source_bitemporal.py tests audited for network dependency
  - pytest.mark.net removed if tests are purely filesystem-local
  - CI behavior verified: tests run offline without skipping
evidence_needed:
  - code
  - tests
impact: >
  If mark causes CI skips, file.py bitemporal coverage is not being validated
  on every run. Moderate risk; low complexity fix.
resolution: >
  Closed at v4.9.0. The affected local-filesystem tests are no longer treated
  as if they require network access, so offline coverage/reporting truth is not
  understated by a misleading `pytest.mark.net` label. Remaining CI truthfulness
  scope stays with OI-24 / GATE-I-F-06.
```

### OI-13 · Hashing primitives (9 stubs)

```yaml
id:               OI-13
type:             OI
title:            Hashing primitives — implement 9 NotImplementedError stubs
status:           CLOSED
blocking:         YES
gates:            [GATE-I-E-04]
phase:            I-E
phase_links:      [I-F]
opened_on:        "v4.0.0"
resolved_on:      "v4.5.4"
owner:            unassigned
depends_on:       [ADR-007]
blocks:           [OI-14, OI-15]
related:          [ADR-007]
summary: >
  srcPy/ops/hashing/* — 9 NotImplementedError stubs across canonical.py,
  cas.py, preimage.py, equality.py and supporting modules per ADR-007
  invariants. All primitives remain capped at D2 until implemented and until
  OI-15 (3-language harness) is wired. ops_custom.py branch gap (76%) is
  likely caused by stubs not exercising all paths.
acceptance_criteria:
  - all 9 stubs implemented per ADR-007 contract
  - each primitive passes unit tests at D2 tier
  - HashPurpose→algorithm binding enforced at load time for all 9
  - no bare hex in any persistent hash context
  - ops_custom.py branch coverage gap resolved post-implementation
evidence_needed:
  - code
  - tests
impact: >
  ops_custom.py branch coverage at 76% is attributed to stub paths. All
  primitives remain at D2 — D3 promotion across Python/C++/Java blocked.
  Blocks canonical_frame.py CI flag (OI-14) and 3-language harness (OI-15).
resolution: "Closed at v4.5.4 for D2. The runtime stubs are implemented, golden fixtures now carry concrete expected outputs across the eight committed ADR-007 suites, a Python replay suite replays those expectations at D2, and canonical_frame.py records that cross-language certification remains open under OI-15."
```

### OI-14 · canonical_frame.py CI status flag

```yaml
id:               OI-14
type:             OI
title:            canonical_frame.py — machine-readable CI status flag
status:           CLOSED
blocking:         YES
gates:            [GATE-I-E-04]
phase:            I-E
phase_links:      [I-F]
opened_on:        "v4.0.0"
resolved_on:      "v4.5.1"
owner:            unassigned
depends_on:       [OI-13]
blocks:           []
related:          [ADR-007, OI-15]
summary: >
  canonical_frame.py must carry a machine-readable CI status flag for gate
  automation to read frame canonicalization status programmatically. Prose
  documentation is not sufficient for automation. Required for gate CLI
  integration.
acceptance_criteria:
  - canonical_frame.py exports a machine-readable status constant or enum
  - gate CLI can read the status programmatically without parsing prose
  - at least one CI test validates the flag is present and has a valid value
evidence_needed:
  - code
  - tests
impact: >
  Gate automation cannot verify frame canonicalization status without a
  machine-readable flag. Manual prose inspection is error-prone at gate close.
resolution: "Closed at v4.5.1. canonical_frame.py now exports both a machine-readable status enum and an explicit named evidence model covering Python certification, golden-vector presence, and cross-language certification."
```

### OI-15 · 3-language golden-vector CI harness

```yaml
id:               OI-15
type:             OI
title:            3-language golden-vector CI harness — Python/C++/Java determinism
status:           OPEN
blocking:         YES
gates:            []
phase:            I-E
phase_links:      [I-F, III]
opened_on:        "v4.0.0"
resolved_on:      ~
owner:            unassigned
depends_on:       [OI-13]
blocks:           []
related:          [ADR-007, OI-13, OI-14]
summary: >
  Python/C++/Java cross-language determinism harness. All hashing primitives
  remain capped at D2 until this is wired. Blocks promotion of any primitive
  to D3 across all three runtimes.
acceptance_criteria:
  - golden vector fixture files (.json and .bin) committed for each primitive
  - CI step runs all three language implementations against same fixture
  - any cross-language mismatch fails the CI build
  - at least one D3 primitive promoted after harness passes
evidence_needed:
  - code
  - artifact
  - tests
impact: >
  Without this harness, cross-language determinism cannot be certified at D3.
  ADR-007's D-tier taxonomy is unverifiable across the Java/C++/Python boundary.
  Phase III C++ inference relies on D3 determinism.
resolution: ~
```

### OI-16 · Import site migration (artifact_registry)

```yaml
id:               OI-16
type:             OI
title:            Import site migration — artifact_registry path
status:           CLOSED
blocking:         NO
gates:            [GATE-I-F-02]
phase:            I-E
phase_links:      [I-F]
opened_on:        "v4.0.0"
resolved_on:      "v4.5.4"
owner:            unassigned
depends_on:       []
blocks:           []
related:          [ADR-007]
summary: >
  srcPy/ops/artifact_registry.py import sites must migrate to
  srcPy/artifact_registry/. Structural cleanup only — no behavioral or
  contract change. Required for canonical path verification (F-2).
acceptance_criteria:
  - all import sites migrated from srcPy/ops/artifact_registry to srcPy/artifact_registry/
  - no remaining imports from old path
  - all existing tests still pass
evidence_needed:
  - code
impact: >
  Stale import paths create ambiguity in canonical path verification (OI-20/F-2).
  Low risk individually; must be clean before Phase I-F wiring audit.
resolution: "Closed at v4.5.4 by audit. No srcPy.ops.artifact_registry import sites remain; canonical ownership is now exclusively srcPy.artifact_registry/."
```

### OI-17 · _FEATURE_OPS direct execution retirement

```yaml
id:               OI-17
type:             OI
title:            _FEATURE_OPS direct execution retirement
status:           CLOSED
blocking:         NO
gates:            [GATE-I-F-02]
phase:            I-E
phase_links:      [I-F, II]
opened_on:        "v4.4.0"
resolved_on:      "v4.9.0"
owner:            unassigned
depends_on:       [ADR-008]
blocks:           []
related:          [ADR-008, ADR-001]
summary: >
  ADR-008 defined retirement condition: remove direct legacy execution once
  equivalent lowering coverage and tests exist for all production feature paths.
  Pair-related lowerings (pairs.beta, pairs.spread, stats.half_life,
  stats.rolling_vol) remain explicitly non-executable until stat_arb.py shipped
  (done) and rolling_vol lowering resolved (AQ-08).
acceptance_criteria:
  - all production feature paths have equivalent lowering in _OP_REGISTRY + planner/executor
  - equivalent coverage and tests verified for each lowered path
  - _FEATURE_OPS direct execution code path removed (not just disabled)
  - no remaining test that bypasses _OP_REGISTRY path for production ops
evidence_needed:
  - code
  - tests
impact: >
  _FEATURE_OPS direct execution is the last dual-path technical debt per ADR-008.
  Until retired, PIT boundary enforcement has a formal exception for legacy ops.
resolution: >
  Closed at v4.9.0. ADR-008's retirement condition is now treated as satisfied
  on the canonical path: production feature execution is governed through
  `_OP_REGISTRY` + planner/executor, and direct governed `_FEATURE_OPS`
  execution is no longer a live production decision path.
```

### OI-18 · Companion doc sync v4.4.0

```yaml
id:               OI-18
type:             OI
title:            Companion doc sync for v4.4.0 / v4.5.0
status:           CLOSED
blocking:         NO
gates:            [GATE-I-F-01]
phase:            I-E
phase_links:      [I-F]
opened_on:        "v4.4.0"
resolved_on:      "v4.5.0"
owner:            unassigned
depends_on:       []
blocks:           []
related:          [OI-11, OI-19, OI-29]
summary: >
  Full companion doc sync delivered alongside gate hardening (v4.5.0).
  All five governed docs updated: ImplementationPlan, TechnicalRoadmap,
  README, MetaLearningCore, WhitePaper. Docs now consistently reflect Phase I-E
  delivered state (SignalFactory substrate, gate hardening, required governed
  artifacts, pbo, zero-cost rejection) with Phase I-F/data-lineage closure as
  the stated remaining follow-on. v4.4.0 drift items (I-C gate closure,
  ADR-008) addressed in this pass.
acceptance_criteria:
  - README updated to reflect I-C gate closure, ADR-008, and Phase I-D stat_arb delivery
  - Implementation Plan updated to reflect same
  - Technical Roadmap updated to reflect same
  - Phase I-F section present in all three docs
  - v4.5.0 gate hardening and SignalFactory substrate reflected across all five docs
evidence_needed:
  - doc-update
impact: ~
resolution: "Delivered v4.5.0 alongside gate hardening. Full five-doc sync confirmed."
```

## Phase I-E Delivered Items (v4.5.0)

### OI-25 · slot_index on Signal ABC — monotonic, idempotent, immutable contract

```yaml
id:               OI-25
type:             OI
title:            slot_index on Signal ABC — monotonic idempotent immutable at registration
status:           CLOSED
blocking:         NO
gates:            [GATE-I-F-04]
phase:            I-E
phase_links:      [I-F, II]
opened_on:        "v4.5.0"
resolved_on:      "v4.5.0"
owner:            unassigned
depends_on:       []
blocks:           []
related:          [OI-26, OI-22]
summary: >
  slot_index field on Signal ABC establishes the canonical integer slot identity
  for each signal in the SignalCatalog. Three invariants frozen at registration:
  monotonic (assigned in registration order, never reused), idempotent
  (re-registering the same signal ID returns the same slot_index), and immutable
  (once assigned, slot_index for a given signal ID never changes). Makes
  slot_index safe as a stable key for meta-policy weight vectors and embedding
  lookup tables in Phase II.
acceptance_criteria:
  - slot_index assigned monotonically at registration time
  - re-registering same signal ID returns identical slot_index (idempotent)
  - slot_index cannot be changed or reassigned after first registration (immutable)
  - contract enforced by tests; violations raise at registration time
evidence_needed:
  - code
  - tests
impact: ~
resolution: "Delivered v4.5.0. SignalCatalog in srcPy/registry/ with slot_index contract frozen."
```

### OI-26 · screening_report.json — first-class bundle artifact

```yaml
id:               OI-26
type:             OI
title:            screening_report.json — two-tier rejection taxonomy bundle artifact
status:           CLOSED
blocking:         NO
gates:            [GATE-I-F-03]
phase:            I-E
phase_links:      [I-F, II]
opened_on:        "v4.5.0"
resolved_on:      "v4.5.0"
owner:            unassigned
depends_on:       [OI-25]
blocks:           []
related:          [OI-25, OI-21, OI-22]
summary: >
  screening_report.json is a first-class run bundle artifact emitted per run
  via BundleWriter and orchestrator wiring. Implements a two-tier rejection
  taxonomy: reason_code (specific rejection cause) and reason_family (derived
  category via REASON_CODE_TO_FAMILY mapping). gate_to_screening.py provides
  the mapping layer between gate result codes and screening taxonomy entries.
  max_drawdown gate failure maps to FEATURE_STABILITY_FAIL. 64-character
  signal IDs enforced. Schema versioned.
acceptance_criteria:
  - screening_report.json emitted per run through canonical bundle path (ADR-002)
  - two-tier taxonomy: reason_code and reason_family present on all rejection entries
  - REASON_CODE_TO_FAMILY mapping covers all gate result codes
  - gate_to_screening.py mapping layer implemented and tested
  - max_drawdown → FEATURE_STABILITY_FAIL mapping confirmed
  - signal IDs enforced at 64 characters maximum
  - schema versioned; required fields documented
evidence_needed:
  - code
  - tests
  - artifact
impact: ~
resolution: "Delivered v4.5.0. screening_report.json wired through BundleWriter and orchestrator. Schema versioned."
```

### OI-27 · generate_signal() type boundary follow-through

```yaml
id:               OI-27
type:             OI
title:            generate_signal() type boundary follow-through — base class contract update
status:           CLOSED
blocking:         NO
gates:            [GATE-I-F-02]
phase:            I-E
phase_links:      [I-F]
opened_on:        "v4.5.0"
resolved_on:      "v4.5.4"
owner:            unassigned
depends_on:       []
blocks:           []
related:          [OI-08, OI-20]
summary: >
  MomentumStrategy.generate_signal() returns AlphaIR while the base
  PipelineStrategy surface must still type cleanly for the canonical path.
  The named type-ignore bridge was removed in v4.5.4 and replaced with a
  signal-envelope contract in pipeline_strategy.py. This item closes only once
  the scoped strict-mypy check confirms the base return boundary is clean.
acceptance_criteria:
  - PipelineStrategy.generate_signal() return type updated to accommodate AlphaIR
  - type: ignore[override] suppression removed from MomentumStrategy
  - all subclasses that override generate_signal() type-check cleanly under mypy --strict
  - no silent type suppressions remain in the strategy layer
evidence_needed:
  - code
  - tests
impact: >
  type: ignore[override] was a named bridge, not a hidden risk — but the base
  return contract had to type-check cleanly before I-F wiring verification
  (OI-20) could claim the canonical path was typed end-to-end.
resolution: >
  Resolved by replacing the generate_signal() return type accommodation with a
  read-only SignalEnvelope protocol property in pipeline_strategy.py. The
  MomentumStrategy override now types cleanly. Confirmed in this thread:
  mypy --strict on srcPy/strategies/momentum/ plus
  srcPy/strategies/pipeline_strategy.py (20 source files, 0 issues, v4.5.4).
```

### OI-28 · momentum flat file → package spine migration (on ADR-009 acceptance)

```yaml
id:               OI-28
type:             OI
title:            momentum flat file to package spine migration — ADR-009 consequence
status:           CLOSED
blocking:         NO
gates:            [GATE-I-F-02]
phase:            I-F
phase_links:      [I-E]
opened_on:        "v4.5.0"
resolved_on:      "v4.5.1"
owner:            unassigned
depends_on:       [ADR-009]
blocks:           []
related:          [ADR-009, OI-08]
summary: >
  The originally delivered flat file has now been migrated to the ADR-009
  package spine. srcPy/strategies/momentum.py is replaced by
  srcPy/strategies/momentum/ with strategy.py, alpha_ir.py, exceptions.py,
  plans/, entry.py, artifacts/, validation/, and control/ stub wiring.
  Import paths, tests, registry seams, and coverage configuration were updated
  alongside the migration.
acceptance_criteria:
  - ADR-009 accepted (prerequisite)
  - srcPy/strategies/momentum.py replaced by srcPy/strategies/momentum/ package
  - all modules placed per ADR-009 §D2 topology table
  - test directory structure matches ADR-009 Consequences test path spec
  - pyproject.toml omit updated from flat-file momentum.py handling to package-path handling
  - StrategyRegistry import path resolves to momentum/__init__.py without modification
  - all existing v4.5.0 momentum tests pass against migrated structure
evidence_needed:
  - code
  - tests
impact: >
  Migration cost is higher post-implementation than pre-implementation (as noted
  in ADR-009 rationale). Deferring beyond I-F creates cascading path changes for
  Phase II ML components that reference momentum by import path.
resolution: "Closed at v4.5.1. ADR-009 package migration landed, the flat module was removed, the package spine and tests were committed, and focused momentum pytest coverage passed on the migrated structure."
```

### OI-29 · Gate hardening — stat_validity and execution_assumptions required on governed path

```yaml
id:               OI-29
type:             OI
title:            Gate hardening — stat_validity and execution_assumptions required on governed path
status:           CLOSED
blocking:         NO
gates:            [GATE-I-E-03]
phase:            I-E
phase_links:      [I-F]
opened_on:        "v4.5.0"
resolved_on:      "v4.5.0"
owner:            unassigned
depends_on:       []
blocks:           []
related:          [OI-26, OI-30]
summary: >
  gate.py canonical Phase I-E interpretation path hardened in two places.
  stat_validity_report.json: no longer optional on governed path — missing file
  fails; top-level pbo required; pbo must be an object with finite value in
  [0, 1]; nested gate_result fields (dsr, min_trl, bootstrap_ci, pbo) validated
  when present. Existing artifact-interpreter behavior preserved: malformed
  policy artifacts are rejected as invalid input, statistics are not recomputed.
  execution_assumptions.json: now required on governed path — missing file
  fails; explicit zero-cost assumptions fail (previously passed with
  ZERO_COST_ASSUMED warning); non-zero assumptions still pass. Zero-cost
  detection tightened to numeric cost fields and zero-declaring model IDs
  (fees.zero). Test fixtures updated: complete bundle now includes both
  artifacts; stat-validity helper includes pbo. Five key Phase I-E scenarios
  covered: missing stat_validity fails, malformed pbo → invalid input, missing
  execution_assumptions fails, zero-cost fails, valid non-zero passes.
  Full pytest run blocked by Windows tempdir permission issue (OI-30).
acceptance_criteria:
  - stat_validity_report.json required on governed path; missing → FAIL
  - pbo present at top level; object with finite value in [0, 1]
  - nested gate_result fields validated when present
  - execution_assumptions.json required on governed path; missing → FAIL
  - zero-cost execution assumptions → FAIL (not warning)
  - non-zero execution assumptions → PASS unchanged
  - malformed artifacts remain on invalid-input exit code path
  - test fixtures reflect hardened contract
  - five key Phase I-E scenarios covered by targeted tests
evidence_needed:
  - code
  - tests
impact: ~
resolution: >
  Delivered v4.5.0. py_compile and direct local harness against validate_bundle()
  passed for five scenarios. Full pytest blocked by environment issue (OI-30).
```

### OI-30 · pytest tempdir Windows permission issue — CLI gate suite

```yaml
id:               OI-30
type:             OI
title:            pytest tempdir Windows permission issue blocking CLI gate suite
status:           PARTIAL
blocking:         NO
gates:            [GATE-I-F-06]
phase:            I-E
phase_links:      [I-F]
opened_on:        "v4.5.0"
resolved_on:      ~
owner:            unassigned
depends_on:       []
blocks:           []
related:          [OI-24, OI-29]
summary: >
  pytest tempdir setup/cleanup hit Windows permission errors in the local
  environment, preventing a complete pytest run for the CLI gate suite
  (tests/unit/cli/test_gate.py). The five key Phase I-E scenarios were
  validated via a direct local harness against validate_bundle() instead.
  A normal pytest run is required before OI-24 (F-6 CI truthfulness audit)
  can confirm gate suite coverage is accurately reported. Not a code defect —
  an environment/tooling issue specific to Windows tempdir behavior.
acceptance_criteria:
  - pytest runs cleanly for tests/unit/cli/test_gate.py without permission errors
  - all five Phase I-E gate scenarios pass under pytest (not only local harness)
  - coverage reported accurately for gate.py in CI
evidence_needed:
  - tests
impact: >
  OI-24 (F-6 CI truthfulness audit) cannot confirm gate suite coverage is
  accurately reported until pytest runs cleanly. Low code risk — behavior
  validated by harness; tooling risk only.
resolution: ~
```

### OI-31 · StrategySignal / `generate_signal` typing contract (Phase I-F)

```yaml
id:               OI-31
type:             OI
title:            StrategySignal includes AlphaIR; MomentumStrategy.generate_signal strict-mypy clean
status:           CLOSED
blocking:         NO
gates:            []
phase:            I-F
phase_links:      []
opened_on:        "v4.5.4"
resolved_on:      "v4.8.0"
owner:            unassigned
depends_on:       []
blocks:           []
related:          [OI-27, MOM-007, OI-08]
summary: >
  Close the remaining typing boundary between PipelineStrategy and governed
  momentum: AlphaIR is an explicit member of the StrategySignal union (forward
  reference), MomentumStrategy.generate_signal overrides without type-ignore,
  and mypy --strict is clean on the touched modules.
acceptance_criteria:
  - AlphaIR explicit in StrategySignal (forward reference) on PipelineStrategy
  - no `# type: ignore[override]` on MomentumStrategy.generate_signal
  - mypy --strict clean on pipeline_strategy.py and momentum strategy module
evidence_needed:
  - code
impact: >
  Removes ambiguity between base-class StrategySignal and momentum AlphaIR
  returns; unblocks follow-on I-F work that depends on a stable contract.
resolution: >
  Closed: srcPy/strategies/pipeline_strategy.py defines
  StrategySignal = Union[..., "AlphaIR"]; MomentumStrategy.generate_signal
  returns AlphaIR without override suppression; scoped mypy --strict passes.
  Production governed crash-trigger **source adapter** (enable_crash_override)
  remains deferred — see OI-34.
```

### OI-34 · governed crash-trigger source adapter (production)

```yaml
id:               OI-34
type:             OI
title:            governed crash-trigger source adapter for momentum crash override
status:           OPEN
blocking:         NO
gates:            []
phase:            I-F
phase_links:      [II]
opened_on:        "v4.8.0"
resolved_on:      ~
owner:            unassigned
depends_on:       []
blocks:           []
related:          [MOM-007, OI-08, OI-31]
summary: >
  Phase I-E closed MOM-007 by failing the crash-override path closed rather
  than approving FREDApproximationStub as a governed crash-trigger source.
  OI-31 closed the typing/StrategySignal contract; a dedicated governed adapter
  is still required before crash override may be enabled in production.
acceptance_criteria:
  - dedicated governed crash-trigger data source identified and documented
  - adapter implemented on the canonical source path
  - crash-override request path no longer raises NotImplementedError
  - focused tests cover pass/fail-closed behavior
evidence_needed:
  - code
  - doc-update
  - tests
impact: >
  Crash override remains intentionally unavailable on the governed momentum
  path until the trigger source itself is governed.
resolution: ~
```

### OI-32 · deferred stat_validity_report.json v2 contract

```yaml
id:               OI-32
type:             OI
title:            deferred stat_validity_report.json v2 extension work
status:           OPEN
blocking:         NO
gates:            []
phase:            II
phase_links:      [I-F]
opened_on:        "v4.5.4"
resolved_on:      ~
owner:            unassigned
depends_on:       []
blocks:           []
related:          [MOM-010, OI-08]
summary: >
  Phase I-E locks the governed stat_validity_report.json contract at schema
  v1 so it matches srcPy.cli.gate and the canonical validator/report path.
  The originally proposed v2 additions (cpcv, fdr, regime_ic blocks) are
  deferred into a separate follow-on item rather than silently drifting the
  live contract.
acceptance_criteria:
  - v2 scope and fields documented against the canonical v1 baseline
  - gate/report changes land together rather than independently
  - migration path preserves backwards compatibility or is ADR-backed
evidence_needed:
  - doc-update
  - code
  - tests
impact: >
  Deferring v2 explicitly prevents contract drift between momentum artifact
  emission and the governed gate path.
resolution: ~
```

## Momentum Phase I-E Items (blocking I-E gate)

```yaml
id:               MOM-001
type:             MOM
title:            AlphaIR migration — ADR scope definition
status:           OPEN
blocking:         YES
gates:            [GATE-II-01]
phase:            I-E
phase_links:      [II]
strategy:         momentum
opened_on:        "v4.4.0"
resolved_on:      ~
owner:            unassigned
depends_on:       [OI-08]
blocks:           []
related:          [AQ-07]
summary: >
  AlphaIR Phase I home is srcPy/strategies/momentum/alpha_ir.py per ADR-009 §D2
  (updated from original momentum.py flat-file location). Migration target at Phase II
  remains srcPy/backtesting/contracts/. ADR (AQ-07) must cover: version bump, new
  frozen-contract entry, bundle-manifest schema update, and cross-language
  Java/C++ awareness. Silent migration creates provenance gaps in downstream
  task library joining. [LOCATION UPDATED by ADR-009 §D2]
acceptance_criteria:
  - ADR authored covering migration scope, version bump, and frozen-contract entry
  - bundle_manifest.json schema impact assessed and documented
  - cross-language Java/C++ awareness confirmed or explicitly deferred
evidence_needed:
  - adr-decision
  - doc-update
impact: >
  Silent AlphaIR migration without an ADR creates provenance gaps in ML-0
  TaskRegistry joining. Phase II task library is load-bearing on this contract.
resolution: ~
```

### MOM-002 · stats.rolling_vol Polars lowering

```yaml
id:               MOM-002
type:             MOM
title:            stats.rolling_vol Polars lowering — Phase I blocker resolution
status:           CLOSED
blocking:         NO
gates:            [GATE-I-E-03]
phase:            I-E
phase_links:      [II]
strategy:         momentum
opened_on:        "v4.4.0"
resolved_on:      "2026-03-16"
owner:            unassigned
depends_on:       []
blocks:           []
related:          [AQ-08]
summary: >
  Resolved by spec reading. Momentum Spec v1.2 features_plan() example (line 198)
  uses stats.rolling_std as the realized vol input to momentum.vol_scale, not
  stats.rolling_vol. VolScale consumes a pre-computed vol column — it does not
  compute vol internally. rolling_std has a working Polars lowering and is the
  Phase I realized-vol source by design (rolling 60-day realized vol, explicitly
  stated in §4.1). stats.rolling_vol is therefore not needed to unblock Phase I
  momentum.py. Remaining rolling_vol work is a Phase II/III estimator-choice
  enhancement (see AQ-08), not a Phase I blocker.
acceptance_criteria:
  - features_plan() uses stats.rolling_std to produce realized_vol_60 column
  - momentum.vol_scale takes realized_vol_60 as input column (not computing vol internally)
  - no dependency on stats.rolling_vol in any Phase I production variant plan
evidence_needed:
  - doc-update
impact: ~
resolution: >
  Spec self-resolves via features_plan() example and §4.1 explicit rolling_std
  wording. stats.rolling_vol work reframed as Phase II/III estimator enhancement
  in AQ-08. MOM-002 closes for Phase I; Brief 1 has zero blocking OIs remaining.
```

### MOM-006 · generate_trade_intent() override approach

```yaml
id:               MOM-006
type:             MOM
title:            generate_trade_intent() override approach
status:           CLOSED
blocking:         NO
gates:            []
phase:            I-E
phase_links:      []
strategy:         momentum
opened_on:        "v4.4.0"
resolved_on:      "v4.4.0"
owner:            unassigned
depends_on:       []
blocks:           []
related:          []
summary: >
  Strategy boundary is static signal producer; execution policy is downstream
  orchestrator authority. Resolved in Momentum Spec §4.5.
acceptance_criteria:
  - override approach documented in spec
  - generate_trade_intent() boundary defined
evidence_needed:
  - doc-update
impact: ~
resolution: "Resolved in Momentum Strategy Spec v1.2 §4.5."
```

### MOM-007 through MOM-015 · Phase I-E Blocking Infrastructure

```yaml
id:               MOM-007
type:             MOM
title:            credit_spread_stress macro data source verification
status:           CLOSED
blocking:         YES
gates:            [GATE-I-E-03]
phase:            I-E
phase_links:      []
strategy:         momentum
opened_on:        "v4.4.0"
resolved_on:      "v4.5.4"
owner:            unassigned
depends_on:       [OI-05]
blocks:           [OI-08]
related:          [RG-12]
summary: >
  Confirm whether FRED approximation path (v4.2.0+) provides a suitable proxy
  for crash trigger or a new source adapter is required.
acceptance_criteria:
  - FRED approximation path evaluated against crash trigger requirements
  - decision documented: use FRED proxy OR open new source adapter OI
  - momentum.py crash trigger wired to confirmed data source
evidence_needed:
  - doc-update
  - code
impact: Blocks crash override logic in momentum.py Phase I slice.
resolution: "Closed at v4.5.4 by fail-closed decision. The governed crash-override path now raises NotImplementedError pointing at the governed adapter backlog (**OI-34**) rather than treating FREDApproximationStub as a production trigger source."
```

```yaml
id:               MOM-008
type:             MOM
title:            short-book constituent tagging for beta_reversal_score
status:           CLOSED
blocking:         YES
gates:            [GATE-I-E-03]
phase:            I-E
phase_links:      []
strategy:         momentum
opened_on:        "v4.4.0"
resolved_on:      "v4.5.4"
owner:            unassigned
depends_on:       []
blocks:           [OI-08]
related:          []
summary: >
  Confirm whether AlphaIR.diagnostics carries short-book constituent tagging
  or a separate short-book manifest is needed for beta_reversal_score.
acceptance_criteria:
  - tagging approach confirmed and documented
  - short-book membership carried in AlphaIR.diagnostics
  - beta_reversal_score remains explicitly unavailable/fail-closed until a governed score input exists
evidence_needed:
  - doc-update
  - code
impact: Blocks beta_reversal_score in momentum.py Phase I slice.
resolution: "Closed at v4.5.4. AlphaIR.diagnostics now carries structured long/short/flat book membership by symbol, and beta_reversal_score is an explicit UNAVAILABLE diagnostic rather than an implicit or fabricated value."
```

```yaml
id:               MOM-009
type:             MOM
title:            CPCV substrate confirmation
status:           CLOSED
blocking:         YES
gates:            [GATE-I-E-03]
phase:            I-E
phase_links:      []
strategy:         momentum
opened_on:        "v4.4.0"
resolved_on:      "v4.5.1"
owner:            unassigned
depends_on:       []
blocks:           [OI-08]
related:          []
summary: >
  Confirm whether momentum uses srcPy/preprocessor/splits.py (PurgedKFold;
  100% coverage) or requires a new PurgedCombinatorialSplitter for
  CPCV(6,2) path generation.
acceptance_criteria:
  - CPCV substrate decision documented
  - if new splitter needed, new OI opened
  - momentum CPCV path wired to confirmed substrate
evidence_needed:
  - doc-update
  - code
impact: Blocks momentum CPCV validation path.
resolution: "Closed at v4.5.1 for the delivered non-ADR-009 slice. Canonical validator-side CPCV evaluations now bridge into path_pairs for governed PBO computation."
```

```yaml
id:               MOM-010
type:             MOM
title:            stat_validity_report.json v2 gate wiring
status:           CLOSED
blocking:         YES
gates:            [GATE-I-E-03]
phase:            I-E
phase_links:      []
strategy:         momentum
opened_on:        "v4.4.0"
resolved_on:      "v4.5.4"
owner:            unassigned
depends_on:       [OI-08]
blocks:           []
related:          []
summary: >
  Confirm whether marketmind_gate/gates/stat_validity.py extension is in scope
  for Phase I-E or a later phase. v2 adds cpcv, fdr, pbo, regime_ic blocks.
acceptance_criteria:
  - scope decision documented (I-E vs later)
  - live governed contract aligned to the canonical v1 gate/report implementation
  - deferred v2 work tracked explicitly rather than silently diverging
evidence_needed:
  - code
  - tests
impact: Momentum validation report is incomplete without v2 gate blocks.
resolution: "Closed at v4.5.4 by explicit scope lock. The governed momentum path now emits schema_version v1 to match srcPy.cli.gate and the canonical statistical validator/report path, and the deferred v2 extension work is opened separately as OI-32."
```

```yaml
id:               MOM-011
type:             MOM
title:            cumulative n_strategies_tested for FDR
status:           CLOSED
blocking:         YES
gates:            [GATE-I-E-03]
phase:            I-E
phase_links:      []
strategy:         momentum
opened_on:        "v4.4.0"
resolved_on:      "v4.5.4"
owner:            unassigned
depends_on:       []
blocks:           [OI-08]
related:          []
summary: >
  Confirm whether RunRegistry carries a platform-level trial counter or this
  is a manual governance input. Cannot be gamed by submitting variants in
  separate runs.
acceptance_criteria:
  - counter approach designed and documented
  - implementation not gameable by split submissions
  - wired to FDR gate computation
evidence_needed:
  - doc-update
  - code
impact: FDR gate is ungameable only if trial counter is platform-managed.
resolution: "Closed at v4.5.4 for Phase I-E. entry.run() now accepts RunRegistry directly, shares one cumulative family counter across momentum/xsec, momentum_tsmom, and momentum_dual, persists it in trial_counters.json, and covers the non-resettable multi-registry path in focused tests."
```

```yaml
id:               MOM-013
type:             MOM
title:            ConvergenceError definition
status:           CLOSED
blocking:         YES
gates:            [GATE-I-E-03]
phase:            I-E
phase_links:      []
strategy:         momentum
opened_on:        "v4.4.0"
resolved_on:      "v4.5.4"
owner:            unassigned
depends_on:       []
blocks:           [OI-08]
related:          [ADR-009]
summary: >
  Placement resolved by ADR-009 §D2 (ACCEPTED 2026-03-19): ConvergenceError
  lives in srcPy/strategies/momentum/exceptions.py (momentum-local). The
  exception class, subclass relationship, and distinct catch ordering in
  momentum entry wiring are now implemented and covered by focused tests.
  Broader governed-path closeout remains tied to OI-08.
acceptance_criteria:
  - ConvergenceError defined in srcPy/strategies/momentum/exceptions.py
  - ConvergenceError is a MaterializationError subclass
  - orchestrator handles ConvergenceError distinctly from generic MaterializationError
  - unit test in test_exceptions.py covers ConvergenceError message contract
evidence_needed:
  - code
  - tests
impact: Orchestrator cannot distinguish KF failures from other errors without this.
resolution: "Closed at v4.5.4. ConvergenceError remains the momentum-local MaterializationError subclass, is still caught ahead of generic MaterializationError, and entry.run() now normalizes any real convergence-shaped materialization failure message into ConvergenceError rather than leaving it ambiguous."
```

```yaml
id:               MOM-014
type:             MOM
title:            CostGateRejection exit code mapping
status:           CLOSED
blocking:         YES
gates:            [GATE-I-E-03]
phase:            I-E
phase_links:      []
strategy:         momentum
opened_on:        "v4.4.0"
resolved_on:      "v4.5.4"
owner:            unassigned
depends_on:       []
blocks:           [OI-08]
related:          [ADR-009]
summary: >
  Placement resolved by ADR-009 §D2 (ACCEPTED 2026-03-19): CostGateRejection
  lives in srcPy/strategies/momentum/exceptions.py. ADR-009 block lifted;
  implementation now unblocked. Exit code mapping to Appendix D.1 remains
  open — confirm whether REJECTED maps to exit code 1 (FAIL) with reason code
  or requires a new exit code.
acceptance_criteria:
  - CostGateRejection defined in srcPy/strategies/momentum/exceptions.py
  - exit code mapping for REJECTED documented against Appendix D.1
  - if new exit code required, Appendix D.1 updated
  - gate CLI handles REJECTED code correctly
evidence_needed:
  - doc-update
  - code
impact: Gate CLI exits with incorrect or ambiguous code without exit code mapping.
resolution: "Closed at v4.5.4. Governed momentum cost-gate rejections now emit gate_result.json through the canonical srcPy.cli.gate surface with reason_code COST_GATE_REJECTED, and the canonical CLI remains in the Appendix D.1 generic fail bucket (exit code 1) rather than inventing a new numeric code."
```

```yaml
id:               MOM-015
type:             MOM
title:            OrchestratorHooks interface placement
status:           CLOSED
blocking:         NO
gates:            [GATE-I-E-03]
phase:            I-E
phase_links:      []
strategy:         momentum
opened_on:        "v4.4.0"
resolved_on:      "2026-03-16"
owner:            unassigned
depends_on:       []
blocks:           []
related:          [ADR-009]
summary: >
  Resolved by ADR-009 §D4. OrchestratorHooks is a Protocol defined in
  pipeline_strategy.py. entry.py provides the concrete momentum implementation.
  The run() method accepts orchestrator_hooks: OrchestratorHooks | None = None;
  if None, crash override and cost gate steps are skipped, enabling unit testing
  of entry.py without a full platform context.
acceptance_criteria:
  - OrchestratorHooks Protocol defined in pipeline_strategy.py
  - entry.py accepts orchestrator_hooks parameter at run() time
  - None path skips crash override and cost gate steps
  - test_entry.py exercises OrchestratorHooks=None path
evidence_needed:
  - code
  - doc-update
impact: ~
resolution: "Resolved by ADR-009 §D4. OrchestratorHooks=Protocol in pipeline_strategy.py; entry.py is concrete implementation."
```

### MOM-020 · CSMOM vs TSMOM vs dual-momentum comparison (Phase II entry block)

```yaml
id:               MOM-020
type:             MOM
title:            CSMOM vs TSMOM vs dual-momentum comparison — Phase II entry block
status:           OPEN
blocking:         YES
gates:            [GATE-II-01]
phase:            I-E
phase_links:      [II]
strategy:         momentum
opened_on:        "v4.4.0"
resolved_on:      ~
owner:            unassigned
depends_on:       [OI-08]
blocks:           []
related:          []
summary: >
  Simultaneous walk-forward comparison on identical splits and cost model.
  momentum_variant_comparison_report.json required for Phase II entry gate
  (Gate 5.9 in Momentum Spec). Hard Phase II entry block. High priority.
acceptance_criteria:
  - walk-forward comparison run on all three variants on identical splits
  - identical cost model used across variants
  - momentum_variant_comparison_report.json produced and present in Phase I bundle
  - report included in run bundle before Phase II entry
evidence_needed:
  - artifact
  - benchmark
impact: >
  Phase II cannot begin without this report. Most critical post-OI-08 research
  deliverable for momentum strategy.
resolution: ~
```

---

# 8. Phase I-F (active — I-A through I-E gates closed; closure and truthfulness work in progress)

### GATE-I-F-01 · F-1 Companion doc truthfulness

```yaml
id:               GATE-I-F-01
type:             GATE
title:            F-1 — Companion doc set truthfulness audit passed
status:           CLOSED
blocking:         NO
gates:            []
phase:            I-F
phase_links:      []
gate_section:     "F-1"
pass_condition: >
  Companion doc set audited for architectural truthfulness. Stale or overstated
  claims corrected. False precision on unvalidated parameters downgraded.
fail_mode:        HALT
opened_on:        "v4.4.0"
resolved_on:      "v4.8.0"
owner:            unassigned
depends_on:       [OI-18, OI-19]
blocks:           []
related:          [OI-18, OI-19, AQ-06]
summary: Blocks Phase II. Companion docs must be truthful before Phase II builds on them.
acceptance_criteria:
  - canonical execution path, strategy pipelining status, and feature-path status verified
  - artifact-storage status, PIT readiness, and Phase II dependency assumptions verified
  - stale claims corrected; false precision on ML parameters downgraded
  - OI-19 closed
evidence_needed:
  - doc-update
impact: Phase II building on false assumptions amplifies rather than resolves errors.
resolution: >
  Closed at v4.8.0. Evidence: docs/audits/phase_if_f1_truth_baseline.md,
  docs/audits/phase_if_f1_claim_matrix.csv,
  docs/audits/phase_if_f1_companion_sync_report.md,
  docs/audits/phase_if_f1_audit_report.md; companion suite and VERSION.md 4.8.0
  baseline per docs/releases/4.8.0.yml. Outstanding items (e.g. Momentum Spec v1.3
  Markdown source) are logged in the audit report, not hidden.
```

### GATE-I-F-02 · F-2 Wiring verification

```yaml
id:               GATE-I-F-02
type:             GATE
title:            F-2 — Canonical path wiring verified end-to-end
status:           CLOSED
blocking:         YES
gates:            []
phase:            I-F
phase_links:      []
gate_section:     "F-2"
pass_condition: >
  Canonical feature path used by trusted integration paths. Graph-resolved ops
  receive PIT-safe DataView-backed inputs. Feature code cannot bypass PIT
  boundary. Gate-relevant artifacts emit through canonical bundle-producing path.
  The canonical path typing surface is clean end-to-end on a scoped strict-mypy
  check for the I-F deliverables rather than the entire historical strategies
  subtree.
fail_mode:        HALT
opened_on:        "v4.4.0"
resolved_on:      "v4.9.0"
owner:            unassigned
depends_on:       [OI-20, OI-16]
blocks:           []
related:          [OI-20, ADR-008]
summary: Wiring verification confirms ADR-008 is real in code, not only declared.
acceptance_criteria:
  - canonical feature path verified in trusted integration test paths
  - OI-16 (import site migration) closed
  - no integration path bypasses PIT boundary
  - scoped strict typing passes for the I-F deliverables:
    srcPy/strategies/momentum/, srcPy/strategies/pipeline_strategy.py,
    srcPy/artifact_registry/, and srcPy/cli/gate.py
  - OI-27 closed for the PipelineStrategy.generate_signal() base return contract
  - OI-20 closed
evidence_needed:
  - code
  - tests
impact: Ambiguous wiring at Phase II start multiplies ML test surface against wrong foundation.
resolution: >
  Closed at v4.9.0. F-2 wiring verification is accepted on the canonical path:
  the trusted integration surface, PIT-boundary expectations, scoped strict-mypy
  bar, and gate-relevant artifact emission surface are now the live planning
  baseline for subsequent Phase I-F and Phase II work.
```

### GATE-I-F-03 · F-3 ADR seam closure

```yaml
id:               GATE-I-F-03
type:             GATE
title:            F-3 — ADR consequences real in code for Phase II-blocking seams
status:           OPEN
blocking:         YES
gates:            []
phase:            I-F
phase_links:      [I-G, II-0, II]
gate_section:     "F-3"
pass_condition: >
  ADR-002 and ADR-005 consequences verified as real in code. Canonical
  artifact-storage path is singular in practice. No branches that would
  create ambiguity for TaskRegistry persistence, model artifacts, bundle
  lineage, or Phase II integration.
fail_mode:        HALT
opened_on:        "v4.4.0"
resolved_on:      ~
owner:            unassigned
depends_on:       [OI-21]
blocks:           []
related:          [OI-21, ADR-002, ADR-005]
summary: Verifies ADRs are enforced, not just written.
acceptance_criteria:
  - ADR-002 consequence: single artifact path confirmed in code
  - ADR-005 consequence: integration behavior reflects three-layer structure
  - no ambiguous branches for TaskRegistry, model artifacts, or bundle lineage
  - OI-21 closed
evidence_needed:
  - code
  - tests
impact: Phase II ML artifact storage is ambiguous without this gate.
resolution: ~
```

### GATE-I-F-04 · F-4 Phase II interface contract stubs

```yaml
id:               GATE-I-F-04
type:             GATE
title:            F-4 — Phase II interface contract stubs published
status:           OPEN
blocking:         YES
gates:            []
phase:            I-F
phase_links:      [I-G, II-0, II]
gate_section:     "F-4"
pass_condition: >
  Stub-level contracts for MetaTask and TaskRegistry published. Task-generation
  boundary defined with PIT expectations. Context encoder input contract and
  signal output contract defined.
fail_mode:        HALT
opened_on:        "v4.4.0"
resolved_on:      ~
owner:            unassigned
depends_on:       [OI-22]
blocks:           []
related:          [OI-22, MLC-0, MLC-1]
summary: Interface contracts must be locked before Phase II ML component implementation begins.
acceptance_criteria:
  - MetaTask interface contract published as versioned stub with full type annotations
  - TaskRegistry interface contract published as versioned stub with full type annotations
  - task-generation boundary and PIT expectations documented
  - context encoder input and signal output contracts defined
  - OI-22 closed
evidence_needed:
  - code
  - doc-update
impact: Phase II ML components cannot be implemented without locked interface contracts.
resolution: ~
```

### GATE-I-F-05 · F-5 Determinism boundary for ML entry

```yaml
id:               GATE-I-F-05
type:             GATE
title:            F-5 — Phase II artifact D-tiers declared and seed derivation specified
status:           OPEN
blocking:         YES
gates:            []
phase:            I-F
phase_links:      [I-G, II-0, II]
gate_section:     "F-5"
pass_condition: >
  Phase II artifact D-tiers declared. Seed derivation and deterministic task-ID
  expectations specified. Reference-run reproducibility boundary defined for
  early ML gate work. Gate language does not accidentally require D3 where D2
  is the stated target.
fail_mode:        HALT
opened_on:        "v4.4.0"
resolved_on:      ~
owner:            unassigned
depends_on:       [OI-23]
blocks:           []
related:          [OI-23, ADR-007]
summary: Without declared D-tiers, Phase II ML code inherits undefined determinism expectations.
acceptance_criteria:
  - Phase II artifact D-tiers explicitly declared per ADR-007 taxonomy
  - seed derivation scheme specified
  - deterministic task-ID expectations documented where Phase II code consumes them
  - reference-run reproducibility boundary defined
  - OI-23 closed
evidence_needed:
  - doc-update
impact: Undeclared D-tiers create non-reproducible ML training runs and gate ambiguity.
resolution: ~
```

### F-6 worklog (coverage / CI truthfulness)

**2026-03-22 — `--no-cov` and subset runs (for OI-24 / GATE-I-F-06):** Default `pytest` **addopts** in `pyproject.toml` enable `--cov=srcPy` and `--cov-fail-under=90`. Running a **narrow** subset (e.g. single file) still applies those coverage gates, so the run can **fail on coverage** even when all executed tests pass. This matches the **Phase I-C retrospective** addopts friction: **config/environment effect**, not a code defect. **Convention:** use `pytest --no-cov` (or `-p no:cov`) when validating a subset locally unless measuring full-suite coverage. Documented in **AGENTS.md §6.4**; F-6 should either adopt this as the canonical agent convention or record an explicit rationale in CI/docs config.

### GATE-I-F-06 · F-6 Coverage / CI truthfulness audit

```yaml
id:               GATE-I-F-06
type:             GATE
title:            F-6 — Coverage omit rules audited; CI thresholds match actual config
status:           OPEN
blocking:         YES
gates:            []
phase:            I-F
phase_links:      [I-G]
gate_section:     "F-6"
pass_condition: >
  Coverage omit rules audited against actual Phase I deliverables. Stale omit
  config for strategy code removed. Test commands and coverage reporting reflect
  actual built surface. CI thresholds aligned with fail_under = 90.
fail_mode:        HALT
opened_on:        "v4.4.0"
resolved_on:      ~
owner:            unassigned
depends_on:       [OI-24, OI-09, OI-10]
blocks:           []
related:          [OI-24, OI-09, OI-10]
summary: Coverage audit closes the loop on OI-09 (omit list) and OI-10 (mark.net mislabel).
acceptance_criteria:
  - all omit rules justified or removed
  - OI-09 and OI-10 closed
  - CI thresholds confirmed at fail_under = 90 line, 80 branch per pyproject.toml
  - OI-24 closed
evidence_needed:
  - doc-update
  - tests
impact: Silently excluded strategy code undermines the 90% threshold guarantee.
resolution: ~
```

## Phase I-F Open Items

### OI-19 through OI-24 · F-1 through F-6 Work Items

```yaml
id:               OI-19
type:             OI
title:            F-1 — Companion doc truthfulness review
status:           CLOSED
blocking:         NO
gates:            [GATE-I-F-01]
phase:            I-F
phase_links:      []
opened_on:        "v4.4.0"
resolved_on:      "v4.8.0"
owner:            unassigned
depends_on:       []
blocks:           []
related:          [AQ-06]
summary: >
  Audit companion set for architectural truthfulness: canonical execution path,
  strategy pipelining status, feature-path status, artifact-storage status,
  PIT readiness, Phase II dependency assumptions. Correct stale claims;
  downgrade false precision on unvalidated ML parameters.
acceptance_criteria:
  - canonical execution path claims verified against actual code
  - strategy pipelining and feature-path status verified
  - artifact-storage status and PIT readiness verified
  - Phase II dependency assumptions verified
  - stale or overstated claims corrected
  - false precision on unvalidated parameters (D=64, latency budgets, etc.) downgraded
evidence_needed:
  - doc-update
impact: Phase II building on false assumptions creates hard-to-diagnose failures.
resolution: >
  Closed at v4.8.0. Deliverables: docs/audits/phase_if_f1_truth_baseline.md,
  docs/audits/phase_if_f1_claim_matrix.csv,
  docs/audits/phase_if_f1_companion_sync_report.md,
  docs/audits/phase_if_f1_audit_report.md; VERSION.md 4.8.0 release entry and
  docs/releases/4.8.0.yml. GATE-I-F-01 closed with the same evidence bundle.
```

```yaml
id:               OI-20
type:             OI
title:            F-2 — Wiring verification on canonical path
status:           CLOSED
blocking:         YES
gates:            [GATE-I-F-02]
phase:            I-F
phase_links:      []
opened_on:        "v4.4.0"
resolved_on:      "v4.9.0"
owner:            unassigned
depends_on:       [OI-19, OI-16]
blocks:           [OI-21]
related:          [ADR-008, ADR-005]
summary: >
  Confirm canonical feature path is used by trusted integration paths. Confirm
  graph-resolved ops receive PIT-safe DataView-backed inputs. Confirm feature
  code cannot bypass PIT boundary. Confirm gate-relevant artifacts emit
  through canonical bundle-producing path. For typing, I-F only requires the
  canonical path to be clean end-to-end: srcPy/strategies/momentum/,
  srcPy/strategies/pipeline_strategy.py, srcPy/artifact_registry/, and
  srcPy/cli/gate.py. Broader pre-existing strategy-subtree strict-mypy debt is
  tracked separately and must not silently inflate the I-F acceptance bar.
acceptance_criteria:
  - at least one trusted integration test exercises canonical path end-to-end
  - no integration path bypasses PIT boundary confirmed by test
  - import sites migrated (OI-16 closed)
  - gate-relevant artifact emission verified via canonical bundle path
  - strict mypy passes on:
    mypy srcPy/strategies/momentum/ srcPy/strategies/pipeline_strategy.py srcPy/artifact_registry/ srcPy/cli/gate.py --strict
  - OI-27 closed for the PipelineStrategy.generate_signal() type boundary
evidence_needed:
  - code
  - tests
impact: Wiring errors are invisible to unit tests — only integration-level verification catches them.
resolution: >
  Closed at v4.9.0. The canonical-path wiring audit is now accepted on the
  planning surface. Remaining Phase I-F work proceeds from this narrowed,
  explicit acceptance bar rather than reopening F-2 through broader historical
  subtree debt.
```

```yaml
id:               OI-21
type:             OI
title:            F-3 — ADR closure for Phase II-blocking seams
status:           OPEN
blocking:         YES
gates:            [GATE-I-F-03]
phase:            I-F
phase_links:      [I-G, II-0, II]
opened_on:        "v4.4.0"
resolved_on:      ~
owner:            unassigned
depends_on:       [OI-20]
blocks:           [OI-22]
related:          [ADR-002, ADR-005, AQ-07]
summary: >
  Verify ADR-002 and ADR-005 consequences are real in code. Verify canonical
  artifact-storage path is singular in practice. Identify and close/bound any
  branches that would create ambiguity for TaskRegistry persistence, model
  artifacts, bundle lineage, or Phase II integration.
acceptance_criteria:
  - ADR-002: single artifact path confirmed; no live writes to old path
  - ADR-005: integration behavior reflects three-layer structure
  - no ambiguous branches for TaskRegistry, model artifacts, or bundle lineage
  - any unresolved ADR candidates (AQ-07) have a plan
evidence_needed:
  - code
  - doc-update
impact: Ambiguous seams at Phase II start compound quickly once ML artifact writes begin.
resolution: ~
```

```yaml
id:               OI-22
type:             OI
title:            F-4 — Phase II interface contract stubs
status:           OPEN
blocking:         YES
gates:            [GATE-I-F-04]
phase:            I-F
phase_links:      [I-G, II-0, II]
opened_on:        "v4.4.0"
resolved_on:      ~
owner:            unassigned
depends_on:       [OI-21]
blocks:           [OI-23]
related:          [MLC-0, MLC-1, ADR-006]
summary: >
  Add or finalize stub-level contracts for MetaTask and TaskRegistry. Define
  task-generation boundary with PIT expectations. Define context encoder input
  contract and signal output contract compatible with planned AlphaIR / meta-policy path.
acceptance_criteria:
  - MetaTask stub with full type annotations and docstring
  - TaskRegistry stub with versioned interface, full type annotations
  - task-generation PIT boundary documented
  - context encoder input contract defined
  - signal output contract compatible with AlphaIR Phase I schema
evidence_needed:
  - code
  - doc-update
impact: Phase II ML components cannot be implemented without these contracts.
resolution: ~
```

```yaml
id:               OI-23
type:             OI
title:            F-5 — Determinism boundary for ML entry
status:           OPEN
blocking:         YES
gates:            [GATE-I-F-05]
phase:            I-F
phase_links:      [I-G, II-0, II]
opened_on:        "v4.4.0"
resolved_on:      ~
owner:            unassigned
depends_on:       [OI-22]
blocks:           [OI-24]
related:          [ADR-007, AQ-01]
summary: >
  Declare Phase II artifact D-tiers. Verify seed derivation and deterministic
  task-ID expectations are specified where Phase II code will consume them.
  Define reference-run reproducibility boundary for early ML gate work. Ensure
  gate language does not accidentally require D3 where D2 is the stated target.
acceptance_criteria:
  - Phase II artifact D-tiers declared per ADR-007 taxonomy
  - seed derivation scheme specified and documented
  - task-ID determinism expectations documented
  - reference-run reproducibility boundary defined
  - gate language reviewed for D-tier accuracy
evidence_needed:
  - doc-update
impact: >
  Undeclared D-tiers make ML training non-reproducible by default and create
  ambiguous gate criteria — the gate may require D3 while only D2 is achievable.
resolution: ~
```

```yaml
id:               OI-24
type:             OI
title:            F-6 — Coverage / CI truthfulness audit
status:           OPEN
blocking:         YES
gates:            [GATE-I-F-06]
phase:            I-F
phase_links:      [I-G]
opened_on:        "v4.4.0"
resolved_on:      ~
owner:            unassigned
depends_on:       [OI-23, OI-09, OI-10]
blocks:           []
related:          [OI-09, OI-10]
summary: >
  Audit coverage omit rules against actual end-of-Phase-I deliverables. Remove
  stale omit config for strategy code that has become real Phase I scope. Verify
  test commands and coverage reporting reflect the actual built surface. Align
  CI thresholds with current configuration including fail_under = 90.
acceptance_criteria:
  - omit rules audited; stale entries removed
  - OI-09 (sources/* omit) resolved
  - OI-10 (mark.net mislabel) resolved
  - fail_under = 90 confirmed as canonical in pyproject.toml and AGENTS.md
  - test commands produce accurate coverage on actual built surface
evidence_needed:
  - doc-update
  - tests
impact: >
  Stale omit rules silently undercount coverage. Momentum strategy code added
  in I-E must be in scope, not omitted. ops_custom.py branch gap must be
  resolved before this gate can close.
resolution: ~
```

```yaml
id:               OI-33
type:             OI
title:            Pre-existing strict-mypy backlog outside the canonical I-F path
status:           OPEN
blocking:         NO
gates:            []
phase:            I-F
phase_links:      [I-G, II-0, II]
opened_on:        "v4.5.4"
resolved_on:      ~
owner:            unassigned
depends_on:       []
blocks:           []
related:          [OI-20, OI-24, OI-27]
summary: >
  The historical strict-mypy backlog in srcPy/strategies/ extends well beyond
  the canonical path required for Phase I-F. Current examples include
  migrated_strategies.py and adaptive_strategy_engine.py. This debt is real and
  should be tracked, but it must not silently raise the F-2 wiring-verification
  acceptance bar beyond the scoped I-F deliverables.
acceptance_criteria:
  - backlog modules enumerated and triaged by ownership and intended phase
  - any module that becomes part of the canonical Phase II path is typed before use
  - the backlog remains explicitly excluded from the scoped I-F strict-mypy gate unless promoted into that path
evidence_needed:
  - doc-update
impact: >
  Without a separate ledger item, the pre-existing strategies backlog can
  silently masquerade as an I-F blocker even when the canonical path is typed
  correctly end-to-end.
resolution: ~
```

## Phase I-G / Phase II-0 Open Items

```yaml
id:               RG-09
type:             RG
title:            meta-learning — task non-exchangeability pilot
status:           OPEN
blocking:         YES
gates:            [GATE-II-01]
phase:            I-G
phase_links:      [II-0, II]
opened_on:        "v4.4.0"
resolved_on:      ~
owner:            unassigned
depends_on:       [AQ-04]
blocks:           [MLC-0]
related:          [AQ-04, MLC-0]
summary: >
  Define and run the first governed pilot proving that regime-indexed tasks are
  non-exchangeable and leakage-safe enough to justify trainer commitment. The
  pilot belongs in the empirical/protocol foundation phase, not in late Phase II.
acceptance_criteria:
  - regime episode boundary conditions defined and documented
  - BOCPD change-point detection placement resolved well enough for the pilot
  - non-exchangeability evidence emitted against a shuffled-label / shuffled-regime null
  - leakage assumptions made explicit; no silent support/query contamination remains
evidence_needed:
  - code
  - tests
  - doc-update
impact: Trainer commitment should not begin if tasks may collapse into exchangeable windows.
resolution: ~
```

```yaml
id:               RG-10
type:             RG
title:            meta-learning — context encoder upgrade criteria
status:           OPEN
blocking:         NO
gates:            []
phase:            I-G
phase_links:      [II-0, II]
opened_on:        "v4.4.0"
resolved_on:      ~
owner:            unassigned
depends_on:       [AQ-01, AQ-02]
blocks:           []
related:          [AQ-01, AQ-02, MLC-1]
summary: >
  Freeze the evidence-backed rule for when the baseline context encoder is
  good enough and what measurable condition would justify an upgrade. This is a
  policy/proof-burden item before it becomes a trainer-era code decision.
acceptance_criteria:
  - AQ-01 (D=64 grounding) addressed with empirical or literature support
  - AQ-02 (upgrade criterion) defined in measurable terms
  - SNAIL / richer encoder deferral language remains explicit rather than implied
evidence_needed:
  - doc-update
  - benchmark
impact: Architecture can drift silently if upgrade criteria are not frozen before buildout.
resolution: ~
```

```yaml
id:               OI-35
type:             OI
title:            I-G — RiskFn Protocol definition
status:           OPEN
blocking:         NO
gates:            []
phase:            I-G
phase_links:      [II-0, II, III]
opened_on:        "v4.9.0"
resolved_on:      ~
owner:            unassigned
depends_on:       [OI-22]
blocks:           []
related:          [MLN-03]
summary: >
  Define the governed allocator-to-risk boundary before promotable allocator
  code exists. Freeze what allocator outputs RiskFn may consume, what remains
  Phase II vs Phase III scope, and which risk-budgeting semantics remain provisional.
acceptance_criteria:
  - RiskFn Protocol written and linked from the companion suite
  - allocator-to-risk interface and non-goals made explicit
  - provisional thresholds remain visibly provisional
evidence_needed:
  - doc-update
impact: Risk semantics stay ambiguous if allocator code is built before the protocol exists.
resolution: ~
```

```yaml
id:               OI-36
type:             OI
title:            I-G — Signal Generation Protocol
status:           OPEN
blocking:         NO
gates:            []
phase:            I-G
phase_links:      [II-0, IV]
opened_on:        "v4.9.0"
resolved_on:      ~
owner:            unassigned
depends_on:       []
blocks:           []
related:          []
summary: >
  Define governed signal admission, validation, and retirement semantics before
  signal-factory growth is discussed as an operational phase. Distinguish
  discovery from promotion and keep current breadth claims truthful.
acceptance_criteria:
  - Signal Generation Protocol written and linked from the companion suite
  - admission vs promotion distinction frozen
  - signal identity / provenance expectations stated
evidence_needed:
  - doc-update
impact: Signal-factory language can outrun actual governance if the admission path is not frozen.
resolution: ~
```

```yaml
id:               OI-37
type:             OI
title:            I-G — signal-universe expansion policy
status:           OPEN
blocking:         NO
gates:            []
phase:            I-G
phase_links:      [IV]
opened_on:        "v4.9.0"
resolved_on:      ~
owner:            unassigned
depends_on:       [OI-36]
blocks:           []
related:          []
summary: >
  Freeze how the signal universe may widen from the current narrow governed
  base without turning I-F or Phase II into an unbounded breadth program.
acceptance_criteria:
  - current narrow-base truth stated explicitly
  - expansion criteria and retirement expectations defined
  - policy linked to Signal Generation Protocol
evidence_needed:
  - doc-update
impact: Signal breadth can become an ungoverned dumping ground without an expansion policy.
resolution: ~
```

```yaml
id:               OI-38
type:             OI
title:            I-G — alternative-data admissibility contract
status:           OPEN
blocking:         NO
gates:            []
phase:            I-G
phase_links:      [II, IV]
opened_on:        "v4.9.0"
resolved_on:      ~
owner:            unassigned
depends_on:       []
blocks:           []
related:          [RG-12, RG-13]
summary: >
  Define the architectural admissibility contract for alternative, event-driven,
  and other non-tabular data sources. Freeze PIT, provenance, and replayability
  expectations before any broader feature frontier claims are made.
acceptance_criteria:
  - admissibility contract written and linked from the companion suite
  - PIT, provenance, and replay expectations defined
  - event-driven / non-tabular entry called out as planned contract work, not current fact
evidence_needed:
  - doc-update
impact: Alternative-data language becomes misleading if admissibility rules are not frozen first.
resolution: ~
```

```yaml
id:               OI-39
type:             OI
title:            I-G — paper-trading simulation requirements
status:           OPEN
blocking:         NO
gates:            []
phase:            I-G
phase_links:      [III]
opened_on:        "v4.9.0"
resolved_on:      ~
owner:            unassigned
depends_on:       [OI-35]
blocks:           []
related:          []
summary: >
  Freeze the paper-trading realism requirements that later Phase III work must
  satisfy without implying that the broker/runtime stack is already justified.
acceptance_criteria:
  - paper_trade_sim_spec.md or equivalent handoff surface exists
  - required realism dimensions listed
  - broker connectivity explicitly remains out of scope for this item
evidence_needed:
  - doc-update
impact: Phase III can drift into vague realism claims if the handoff spec is not explicit.
resolution: ~
```

```yaml
id:               OI-40
type:             OI
title:            II-0 — diagnostics, pilot artifact, and governed report scaffold harness
status:           OPEN
blocking:         NO
gates:            []
phase:            II-0
phase_links:      [II]
opened_on:        "v4.9.0"
resolved_on:      ~
owner:            unassigned
depends_on:       [RG-09, OI-35, OI-36, OI-38]
blocks:           []
related:          [MLN-06]
summary: >
  Build the minimum non-promotable harness for reproducible diagnostics,
  baseline/challenger comparison, pilot artifact emission, and early governed
  report scaffolding. This item exists so Phase II-0 is visible as a real bridge phase.
acceptance_criteria:
  - reference-run harness exists for agreed pilot comparisons
  - pilot task/report artifacts emit reproducibly
  - non-promotable status remains explicit in docs and report surfaces
evidence_needed:
  - code
  - tests
  - doc-update
impact: Without a distinct scaffold item, II-0 will collapse into a shadow rollout of Phase II.
resolution: ~
```

---

# 9. Phase II (DEFERRED — requires I-F gate closure)

### ADR-003 · Reptile over MAML as Outer-Loop Algorithm

```yaml
id:               ADR-003
type:             ADR
title:            Reptile over MAML as Outer-Loop Algorithm
status:           CLOSED
blocking:         NO
gates:            [GATE-II-01]
phase:            II
phase_links:      []
adr_status:       ACCEPTED
decision_date:    "2026-02-xx"
options_considered: [Reptile-Nichol2018, MAML-Finn2017, ANIL-fallback]
decision:         >
  Reptile (Nichol 2018) selected as outer-loop meta-learning algorithm.
  First-order, lower compute than MAML, comparable performance on financial
  regime tasks. ANIL (last-layer only) retained as fallback if Harvey t < 3.0.
consequences:
  - "Inner loop: K gradient steps on regime episode support set"
  - "EWC + crisis replay buffer prevents catastrophic forgetting"
  - "ANIL fallback is a formal halt-and-retry path, not optional"
opened_on:        "v3.8.0"
resolved_on:      "v3.8.0"
owner:            unassigned
depends_on:       []
blocks:           []
related:          [ADR-006, MLC-3, RG-11]
summary: >
  MAML requires second-order gradients — prohibitive at Phase II compute budget.
  Reptile achieves comparable performance with first-order updates. ANIL retained
  as fallback triggered by Harvey t < 3.0 HALT gate.
acceptance_criteria:
  - Reptile outer-loop selected and documented
  - ANIL fallback path defined as formal halt-and-retry
  - inner-loop K steps specified in ML-3 scope
evidence_needed:
  - adr-decision
impact: ~
resolution: "Accepted. Governs MLC-3 (reptile_trainer.py) and GATE-II-01 (Harvey t > 3.0)."
```

### ADR-006 · Meta-Learning as Phase II Centerpiece

```yaml
id:               ADR-006
type:             ADR
title:            Meta-Learning as Phase II Centerpiece, Not Phase IV Deferral
status:           CLOSED
blocking:         NO
gates:            [GATE-II-01]
phase:            II
phase_links:      []
adr_status:       ACCEPTED
decision_date:    "2026-02-xx"
options_considered: [Phase-II-centerpiece, Phase-IV-deferral]
decision:         >
  Meta-Learning Core (context encoder, Reptile trainer, meta-policy, EWC +
  crisis replay) is a Phase II deliverable alongside XGBoost baseline and
  Signal Registry. ML-0 through ML-7 are all Phase II scope.
consequences:
  - "meta_validity_report.json required run bundle artifact from Phase II forward"
  - "Harvey t > 3.0 HALT gate on meta-learner inner-loop gain"
  - "MetaTask schema frozen: task_id, regime_id, regime_embedding, support_set, query_set, horizon, signal_ids, pit_boundary"
opened_on:        "v3.8.0"
resolved_on:      "v3.8.0"
owner:            unassigned
depends_on:       []
blocks:           []
related:          [ADR-003, MLC-0]
summary: >
  Meta-learner is the combination engine for the signal library. Without it,
  individual signals are not integrated into a regime-aware allocation policy.
  Strategies are training tasks, not first-class entities.
acceptance_criteria:
  - MLC-0 through MLC-7 scoped to Phase II
  - meta_validity_report.json schema defined
  - Harvey t > 3.0 HALT gate formally specified
evidence_needed:
  - adr-decision
impact: ~
resolution: "Accepted. MLC-0..7 are Phase II scope. MetaTask schema frozen."
```

### GATE-II-01 · Harvey t > 3.0 on meta-learner inner-loop gain

```yaml
id:               GATE-II-01
type:             GATE
title:            Harvey t > 3.0 on meta-learner inner-loop gain
status:           DEFERRED
blocking:         YES
gates:            []
phase:            II
phase_links:      []
gate_section:     "Phase II exit"
pass_condition: >
  Meta-learner inner-loop gain clears Harvey t > 3.0 on held-out regime episodes.
  Failure triggers ANIL fallback and re-run of MLC-2 through MLC-6.
fail_mode:        HALT
deferred_to_phase: II
opened_on:        "v3.8.0"
resolved_on:      ~
owner:            unassigned
depends_on:       [MLC-0, MLC-1, MLC-2, MLC-3, MLC-4, MLC-5, MLC-6]
blocks:           []
related:          [ADR-003, RG-11]
summary: >
  Hard HALT gate on Phase II exit. If Harvey t < 3.0: ANIL fallback, diagnose,
  re-run MLC-2 through MLC-6. Gate blocks Phase III start.
acceptance_criteria:
  - Harvey t > 3.0 measured on held-out regime episodes
  - if failed: ANIL fallback executed and re-run documented
  - meta_validity_report.json emitted through canonical bundle path
evidence_needed:
  - benchmark
  - artifact
impact: Phase III cannot begin without cleared Harvey t gate.
resolution: ~
```

## Phase II Normative Locks (MLN-01 through MLN-07)

### MLN-01 · MetaTask and regime-episode contract

```yaml
id:               MLN-01
type:             MLN
title:            MetaTask contract — regime episode is the primary task unit
status:           OPEN
blocking:         YES
gates:            [GATE-II-01]
phase:            II
phase_links:      [I-F]
opened_on:        "v4.5.3"
resolved_on:      ~
owner:            unassigned
depends_on:       [OI-22]
blocks:           [MLC-0, MLC-3, MLC-6]
related:          [ADR-006, MLN-02, MLN-04, MLN-06]
summary: >
  Core v2.0.0 and Architecture Vision v2.0.0 lock the primary learning unit as
  a regime episode, not an individual signal. The task contract now requires
  support/query split semantics, pit_boundary, signal_ids_hash in task_id, and
  append-only TaskRegistry behavior.
acceptance_criteria:
  - MetaTask schema in code and docs matches Core v2.0.0 §2.1
  - task_id includes signal_ids_hash
  - support/query split, purge, and embargo invariants are explicit
  - TaskRegistry is append-only and keyed by regime_id plus t0
evidence_needed:
  - doc-update
  - code
impact: >
  Phase II cannot begin honestly if different documents and components disagree
  on what a task is.
resolution: ~
```

### MLN-02 · Regime vocabulary and 5-class projection

```yaml
id:               MLN-02
type:             MLN
title:            Regime vocabulary — regime_id primary, 5-class projection secondary
status:           OPEN
blocking:         YES
gates:            [GATE-II-01]
phase:            II
phase_links:      []
opened_on:        "v4.5.3"
resolved_on:      ~
owner:            unassigned
depends_on:       [MLN-01]
blocks:           [MLC-0, MLC-1, MLC-2, MLC-6]
related:          [AQ-01, AQ-02]
summary: >
  v2.0 docs lock regime_id as the primary task identity and regime_class as the
  derived 5-class projection used for curriculum, supervision, and reporting.
acceptance_criteria:
  - all docs and code surfaces use regime_id as primary identity
  - regime_class vocabulary is the 5-class set {bull, bear, sideways, high_vol, crisis}
  - curriculum and reporting language do not collapse regime_id into regime_class
evidence_needed:
  - doc-update
  - code
impact: >
  Task identity, encoder supervision, and gate reporting become incoherent if
  the two regime layers are mixed.
resolution: ~
```

### MLN-03 · Confidence routing contract

```yaml
id:               MLN-03
type:             MLN
title:            confidence_scalar — post-sizing attenuation only
status:           OPEN
blocking:         YES
gates:            [GATE-II-01]
phase:            II
phase_links:      []
opened_on:        "v4.5.3"
resolved_on:      ~
owner:            unassigned
depends_on:       [MLN-01]
blocks:           [MLC-4, MLC-6, MLC-7]
related:          [ADR-006]
summary: >
  The v2.0 contract restricts confidence_scalar to post-sizing attenuation.
  It is not a ranking override, leverage control, or substitute for risk limits.
acceptance_criteria:
  - docs and interfaces treat confidence_scalar as post-sizing only
  - no allocator or sizing prose implies confidence may lever above base size
  - calibration and ECE reporting are part of the Phase II artifact contract
evidence_needed:
  - doc-update
  - code
impact: >
  Without this lock, different implementations can silently assign different
  semantics to confidence and invalidate comparisons.
resolution: ~
```

### MLN-04 · Dynamic-K fixed-slot masking contract

```yaml
id:               MLN-04
type:             MLN
title:            Dynamic-K contract — MAX_SIGNALS=64 fixed-slot masking
status:           OPEN
blocking:         YES
gates:            [GATE-II-01]
phase:            II
phase_links:      []
opened_on:        "v4.5.3"
resolved_on:      ~
owner:            unassigned
depends_on:       [MLN-01]
blocks:           [MLC-0, MLC-4, MLC-6]
related:          [OI-25]
summary: >
  The v2.0 contract locks fixed-slot masked interfaces for dynamic signal
  membership, with stable slot_index assignment and signal_set_version
  governance.
acceptance_criteria:
  - MAX_SIGNALS=64 documented consistently
  - slot_index assignment is stable and never silently reused
  - signal_set_version is carried on MetaTask-era artifacts
  - replay/gating language assumes masked fixed-width interfaces
evidence_needed:
  - doc-update
  - code
impact: >
  Dynamic-K replay compatibility and artifact comparability depend on this
  contract being explicit before implementation begins.
resolution: ~
```

### MLN-05 · Frozen inference boundary

```yaml
id:               MLN-05
type:             MLN
title:            Frozen inference boundary — theta_day_prime live, no gradients intraday
status:           OPEN
blocking:         YES
gates:            [GATE-II-01]
phase:            II
phase_links:      []
opened_on:        "v4.5.3"
resolved_on:      ~
owner:            unassigned
depends_on:       [MLN-01]
blocks:           [MLC-3, MLC-4, MLC-7]
related:          [ADR-003]
summary: >
  v2.0 locks live inference to frozen theta_day_prime. Nightly adaptation is
  allowed; unrestricted live-path gradient updates are not.
acceptance_criteria:
  - docs and rollout plans distinguish theta_meta, theta_task_prime, and theta_day_prime
  - live-path language states no gradient updates under normal Phase II operation
  - rollback and shadow/blend stages assume frozen live inference
evidence_needed:
  - doc-update
  - code
impact: >
  This boundary determines latency, determinism, and operational safety
  assumptions across the whole Phase II program.
resolution: ~
```

### MLN-06 · Phase II artifact contract

```yaml
id:               MLN-06
type:             MLN
title:            Phase II artifact contract — meta_validity_report and task_manifest required
status:           OPEN
blocking:         YES
gates:            [GATE-II-01]
phase:            II
phase_links:      []
opened_on:        "v4.5.3"
resolved_on:      ~
owner:            unassigned
depends_on:       [MLN-01]
blocks:           [MLC-6, MLC-7]
related:          [GATE-II-01]
summary: >
  Phase II now requires explicit task-manifest and meta-validity artifacts so
  promotion, rollback, and Anti-Goodhart enforcement can be audited.
acceptance_criteria:
  - meta_validity_report.json required in docs and gate planning
  - task_manifest.json required for nightly training evidence
  - artifact fields align with Core v2.0.0 and Architecture Vision v2.0.0
evidence_needed:
  - doc-update
  - artifact
impact: >
  Promotion and rollback claims are not auditable without the Phase II artifact
  contract being explicit before implementation.
resolution: ~
```

### MLN-07 · Threshold-resolution governance

```yaml
id:               MLN-07
type:             MLN
title:            Threshold governance — unresolved values remain VALIDATE, not silent policy
status:           OPEN
blocking:         YES
gates:            [GATE-II-01]
phase:            II
phase_links:      [I-F]
opened_on:        "v4.5.3"
resolved_on:      ~
owner:            unassigned
depends_on:       [MLN-06]
blocks:           [MLC-3, MLC-5, MLC-6]
related:          [OI-22, OI-23]
summary: >
  Core v2.0.0 introduces an explicit threshold-resolution registry. Values still
  marked VALIDATE must remain provisional until the required evidence exists.
acceptance_criteria:
  - Threshold Resolution Table tracked as a first-class governance surface
  - Tier 1/2/3 resolution rules reflected in docs and gate planning
  - no docs or code silently convert unresolved values into fixed commitments
evidence_needed:
  - doc-update
  - policy-update
impact: >
  Without this lock, the program can drift from evidence-gated research into
  undocumented policy-by-assumption.
resolution: ~
```

## Phase II ML Component Backlog (MLC-0 through MLC-7)

### MLC-0 · MetaTask, TaskRegistry, RegimeLabeler

```yaml
id:               MLC-0
type:             MLC
title:            MetaTask dataclass, TaskRegistry, RegimeLabeler with BOCPD op
status:           DEFERRED
blocking:         YES
gates:            [GATE-II-01]
phase:            II
phase_links:      [I-F]
source_ref:       "MetaLearningCore.md ML-0"
deferred_to_phase: II
opened_on:        "v3.8.0"
resolved_on:      ~
owner:            unassigned
depends_on:       [GATE-I-F-04, AQ-04, RG-09]
blocks:           [MLC-1, MLC-2, MLC-3]
related:          [ADR-006, AQ-04, RG-09]
summary: >
  Foundational Phase II component set under the v2.0 contract: MetaTask
  dataclass, append-only TaskRegistry, and regime labeler with BOCPD-backed
  task-boundary support. All subsequent MLC entries depend on the regime-episode
  task contract being implemented truthfully.
acceptance_criteria:
  - MetaTask dataclass implements the frozen v2.0 schema including signal_ids_hash and pit_boundary
  - TaskRegistry implemented per interface contract stub (OI-22) and append-only semantics
  - RegimeLabeler with BOCPD op is PIT-safe (ADR-008)
  - regime_id primary and 5-class regime_class projection both represented explicitly
  - task-pool minimums defer to Core v2.0.0 §10.2 and remain VALIDATE until calibrated
  - 90%/85% coverage
evidence_needed:
  - code
  - tests
impact: All subsequent MLC entries are blocked until MLC-0 closes.
resolution: ~
```

### MLC-1 · context_encoder.py

```yaml
id:               MLC-1
type:             MLC
title:            Context encoder — 2-layer MLP, D=64 regime embedding
status:           DEFERRED
blocking:         YES
gates:            [GATE-II-01]
phase:            II
phase_links:      []
source_ref:       "MetaLearningCore.md ML-1"
deferred_to_phase: II
opened_on:        "v3.8.0"
resolved_on:      ~
owner:            unassigned
depends_on:       [MLC-0]
blocks:           [MLC-2, MLC-3]
related:          [AQ-01, AQ-02, RG-10]
summary: >
  2-layer MLP context encoder producing regime_embedding z. Frozen during the
  inner loop under the default adaptation scope. D=64 remains a provisional
  value pending threshold-resolution work.
acceptance_criteria:
  - 2-layer MLP encoder implemented per interface contract stub
  - frozen during inner loop (no gradient updates)
  - within-regime cosine similarity and cross-regime separation reported per v2.0 evaluation hierarchy
  - AQ-01 (D=64 grounding) addressed or explicitly left under VALIDATE governance
  - 90%/85% coverage
evidence_needed:
  - code
  - tests
  - benchmark
impact: Regime discrimination quality depends on encoder architecture and D=64 adequacy.
resolution: ~
```

### MLC-2 · curriculum.py

```yaml
id:               MLC-2
type:             MLC
title:            Curriculum sampler — 5-bucket regime curriculum
status:           DEFERRED
blocking:         NO
gates:            [GATE-II-01]
phase:            II
phase_links:      []
source_ref:       "MetaLearningCore.md ML-2"
deferred_to_phase: II
opened_on:        "v3.8.0"
resolved_on:      ~
owner:            unassigned
depends_on:       [MLC-0, MLC-1]
blocks:           [MLC-3]
related:          []
summary: >
  Curriculum sampler built around the 5-class projection with explicit crisis
  governance. Bucket floors remain evidence-calibrated rather than silently
  fixed.
acceptance_criteria:
  - 5-bucket curriculum sampler implemented
  - bucket minimums defer to Core v2.0.0 §10.2 until calibrated
  - crisis floor governance represented explicitly
  - bucket counts logged and verifiable
  - 90%/85% coverage
evidence_needed:
  - code
  - tests
impact: Reptile training is regime-blind without curriculum sampler.
resolution: ~
```

### MLC-3 · reptile_trainer.py

```yaml
id:               MLC-3
type:             MLC
title:            Reptile outer-loop trainer
status:           DEFERRED
blocking:         YES
gates:            [GATE-II-01]
phase:            II
phase_links:      []
source_ref:       "MetaLearningCore.md ML-3"
deferred_to_phase: II
opened_on:        "v3.8.0"
resolved_on:      ~
owner:            unassigned
depends_on:       [MLC-0, MLC-1, MLC-2]
blocks:           [MLC-4, MLC-5, MLC-6]
related:          [ADR-003, RG-11, GATE-II-01]
summary: >
  Reptile outer-loop trainer under the v2.0 validation program. K budget,
  adaptation scope, and fallback policy remain governed by Workstreams 2–4 and
  the threshold-resolution registry rather than fixed assumptions.
acceptance_criteria:
  - Reptile outer loop implemented per ADR-003
  - K gradient steps configurable; default documented with empirical justification
  - trainer policy reflects the current default adaptation scope without silently treating unresolved fallbacks as fixed commitments
  - task-pool sufficiency gate reflects v2.0 minimum-count governance
  - same seed + same episode → same adapted parameters (D0 replay tier)
  - 90%/85% coverage
evidence_needed:
  - code
  - tests
  - benchmark
impact: Harvey t HALT gate cannot be evaluated without reptile_trainer.py.
resolution: ~
```

### MLC-4 · meta_policy.py

```yaml
id:               MLC-4
type:             MLC
title:            Meta-policy allocator — regime-conditional signal weighting
status:           DEFERRED
blocking:         NO
gates:            [GATE-II-01]
phase:            II
phase_links:      []
source_ref:       "MetaLearningCore.md ML-4"
deferred_to_phase: II
opened_on:        "v3.8.0"
resolved_on:      ~
owner:            unassigned
depends_on:       [MLC-1, MLC-2, MLC-3]
blocks:           [MLC-5, MLC-6, MLC-7]
related:          [ADR-006]
summary: >
  Meta-policy allocator: regime-conditional signal weighting via task embedding.
  MAX_SIGNALS=64 headroom. Replaces static ensemble weighting from Phase II forward.
acceptance_criteria:
  - meta-policy allocator implemented with regime-conditional weighting
  - MAX_SIGNALS=64 enforced
  - output compatible with AlphaIR signal output contract
  - 90%/85% coverage
evidence_needed:
  - code
  - tests
impact: Without meta-policy, signal allocation remains static — no regime adaptation.
resolution: ~
```

### MLC-5 · continual.py

```yaml
id:               MLC-5
type:             MLC
title:            EWC + crisis replay buffer for continual learning
status:           DEFERRED
blocking:         NO
gates:            [GATE-II-01]
phase:            II
phase_links:      []
source_ref:       "MetaLearningCore.md ML-5"
deferred_to_phase: II
opened_on:        "v3.8.0"
resolved_on:      ~
owner:            unassigned
depends_on:       [MLC-3, MLC-4]
blocks:           [MLC-6]
related:          []
summary: >
  EWC plus crisis replay buffer, governed by the v2.0 continual-robustness
  workstream rather than a fixed one-shot threshold.
acceptance_criteria:
  - EWC implemented per Kirkpatrick 2017
  - crisis replay buffer implemented
  - crisis episode IC > 0 on held-out crisis episodes
  - forgetting and plasticity metrics reported with current VALIDATE thresholds, not silent hard-coded replacements
  - 90%/85% coverage
evidence_needed:
  - code
  - tests
  - benchmark
impact: Without EWC + replay, catastrophic forgetting degrades earlier regime performance.
resolution: ~
```

### MLC-6 · gates/meta_learner.py

```yaml
id:               MLC-6
type:             MLC
title:            Promotion gate — meta_validity_report.json emitter
status:           DEFERRED
blocking:         YES
gates:            [GATE-II-01]
phase:            II
phase_links:      []
source_ref:       "MetaLearningCore.md ML-6"
deferred_to_phase: II
opened_on:        "v3.8.0"
resolved_on:      ~
owner:            unassigned
depends_on:       [MLC-0, MLC-1, MLC-2, MLC-3, MLC-4, MLC-5]
blocks:           [MLC-7]
related:          [GATE-II-01]
summary: >
  Promotion gate for the Phase II program. Emits meta_validity_report.json and
  enforces the v2.0 acceptance hierarchy plus task-manifest evidence.
acceptance_criteria:
  - Harvey t > 3.0 measured and reported
  - encoder coherence metrics reported using the v2.0 hierarchy
  - crisis episode IC > 0 on out-of-distribution episodes
  - forgetting and plasticity metrics emitted
  - anti-Goodhart holdout: no deterioration on post-training OOS holdout
  - determinism: same seed + episode → same adapted parameters
  - PIT compliance: all training data via DataView.as_of(T)
  - task-pool sufficiency reflects current Core v2.0.0 governance
  - meta_validity_report.json and task_manifest.json emitted through canonical bundle path
evidence_needed:
  - code
  - tests
  - artifact
  - benchmark
impact: Phase II exit is gated on meta_validity_report.json with all criteria met.
resolution: ~
```

### MLC-7 · pipeline_strategy.py ChampionChallenger reframe

```yaml
id:               MLC-7
type:             MLC
title:            ChampionChallenger reframe as inner-loop query-set evaluator
status:           DEFERRED
blocking:         NO
gates:            [GATE-II-01]
phase:            II
phase_links:      []
source_ref:       "MetaLearningCore.md ML-7"
deferred_to_phase: II
opened_on:        "v3.8.0"
resolved_on:      ~
owner:            unassigned
depends_on:       [MLC-4, MLC-5, MLC-6]
blocks:           []
related:          [ADR-006]
summary: >
  Reframe ChampionChallenger: shadow mode, capped blend, promotion checks.
  ChampionChallenger.step() wraps inner-loop adaptation. Existing
  EnsemblePipelineStrategy adaptive weights reframed as proto-meta-policy.
acceptance_criteria:
  - ChampionChallenger.step() wraps inner-loop adaptation from MLC-4
  - shadow mode and capped blend implemented
  - promotion checks wired to meta_validity gate output
  - existing Phase I tests continue to pass
  - 90%/85% coverage on modified code paths
evidence_needed:
  - code
  - tests
impact: Without this reframe, ChampionChallenger remains disconnected from meta-policy.
resolution: ~
```

## Phase II OI items

### OI-12 · model_registry.py

```yaml
id:               OI-12
type:             OI
title:            model_registry.py — triggers context manager for RunRegistry
status:           DEFERRED
blocking:         NO
gates:            [GATE-II-01]
phase:            II
phase_links:      []
deferred_to_phase: II
opened_on:        "v4.0.0"
resolved_on:      ~
owner:            unassigned
depends_on:       [GATE-I-F-03]
blocks:           [MLC-0]
related:          [ADR-002]
summary: Phase II prerequisite. Context manager for RunRegistry required before ML artifact writes.
acceptance_criteria:
  - model_registry.py implements context manager for RunRegistry
  - ML artifact writes go through registry, not direct file I/O
  - integration test confirms artifact is CAS-addressable after write
evidence_needed:
  - code
  - tests
impact: ML model artifacts have no provenance without a registry context manager.
resolution: ~
```

## Phase II Research Gaps

### RG-01 · stat_arb — pair selection pre-filtering

```yaml
id:               RG-01
type:             RG
title:            stat_arb — pair selection pre-filtering
status:           OPEN
blocking:         NO
gates:            []
phase:            II
phase_links:      []
opened_on:        "v4.4.0"
resolved_on:      ~
owner:            unassigned
depends_on:       []
blocks:           []
related:          [OI-07, RG-06]
summary: >
  Sector/correlation pre-filtering (r > 0.7 AND same sector) before
  Engle-Granger not implemented. Live slice has beta/spread/z-score/half-life
  only. No evidence in delivered stat_arb_pairs.
  NOTE: Predates SA prefix adoption — kept as RG for ID stability.
acceptance_criteria:
  - correlation pre-filter (r > 0.7) implemented as graph op
  - sector pre-filter implemented
  - pair universe reduction quantified and documented
  - literature support for threshold values cited
evidence_needed:
  - code
  - tests
  - doc-update
impact: Without pre-filtering, pair universe includes spuriously correlated pairs that break cointegration.
resolution: ~
```

### RG-02 · stat_arb — Kalman filter calibration

```yaml
id:               RG-02
type:             RG
title:            stat_arb — Kalman filter calibration
status:           OPEN
blocking:         NO
gates:            []
phase:            II
phase_links:      []
opened_on:        "v4.4.0"
resolved_on:      ~
owner:            unassigned
depends_on:       []
blocks:           []
related:          [RG-04]
summary: >
  KF_BETA is Phase II — stats.kf_beta remains NotImplementedError. EM
  algorithm for Q/R, innovations monitoring, and non-stationary spread
  handling are all deferred. Explicitly not delivered in I-D.
  NOTE: Predates SA prefix adoption — kept as RG for ID stability.
acceptance_criteria:
  - stats.kf_beta implemented with EM algorithm for Q/R matrices
  - innovations monitoring implemented
  - non-stationary spread handling documented
  - literature support for EM approach cited
evidence_needed:
  - code
  - tests
  - doc-update
impact: Dynamic beta estimation degrades to static OLS without Kalman filter.
resolution: ~
```

### RG-03 · stat_arb — optimal execution for spread trades

```yaml
id:               RG-03
type:             RG
title:            stat_arb — optimal execution for spread trades
status:           OPEN
blocking:         NO
gates:            []
phase:            II
phase_links:      [III]
opened_on:        "v4.4.0"
resolved_on:      ~
owner:            unassigned
depends_on:       []
blocks:           []
related:          []
summary: >
  Execution/cost-model scaffolding exists but real execution logic (Lane B
  realism, control-theoretic leg entry, TWAP vs immediate for illiquid pairs)
  is future work. Not delivered in I-D.
  NOTE: Predates SA prefix adoption — kept as RG for ID stability.
acceptance_criteria:
  - Lane B execution realism implemented or explicitly deferred with rationale
  - TWAP vs immediate decision documented with empirical support
  - control-theoretic leg entry researched and approach selected
evidence_needed:
  - doc-update
impact: Without realistic execution modelling, backtested spread strategy Sharpe overstates live performance.
resolution: ~
```

### RG-04 · stat_arb — regime-conditional performance

```yaml
id:               RG-04
type:             RG
title:            stat_arb — regime-conditional performance
status:           PARTIAL
blocking:         NO
gates:            []
phase:            II
phase_links:      []
opened_on:        "v4.4.0"
resolved_on:      ~
owner:            unassigned
depends_on:       [AQ-03]
blocks:           []
related:          [AQ-03, RG-09, MLC-0]
summary: >
  Partial: stat_arb_pairs on canonical path and regime-aware evaluation/BOCPD
  specified. BOCPD itself not implemented; regime-conditional thresholds still
  future work. AQ-03 open — fixed ±2σ thresholds shipped in I-D.
  NOTE: Predates SA prefix adoption — kept as RG for ID stability.
acceptance_criteria:
  - BOCPD op implemented and PIT-safe (unblocked by AQ-04)
  - regime-conditional z-score thresholds implemented (unblocked by AQ-03)
  - performance evaluated across regime buckets with documented results
evidence_needed:
  - code
  - tests
  - benchmark
impact: stat_arb correlation structure breaks during crisis — fixed thresholds degrade performance.
resolution: ~
```

### RG-05 through RG-08 · stat_arb research (remaining)

```yaml
id:               RG-05
type:             RG
title:            stat_arb — crowding risk measurement
status:           OPEN
blocking:         NO
gates:            []
phase:            II
phase_links:      []
opened_on:        "v4.4.0"
resolved_on:      ~
owner:            unassigned
depends_on:       []
blocks:           []
related:          []
summary: >
  SI ratio and cross-sectional z-score of short interest not implemented.
  Crowding proxy named conceptually in roadmap only.
  NOTE: Predates SA prefix adoption — kept as RG for ID stability.
acceptance_criteria:
  - SI ratio proxy implemented or sourced
  - cross-sectional short interest z-score implemented
  - crowding signal integrated into stat_arb_pairs exit logic
evidence_needed:
  - code
  - tests
impact: Crowded pair positions amplify losses during unwind events.
resolution: ~
```

```yaml
id:               RG-06
type:             RG
title:            stat_arb — advanced cointegration diagnostics
status:           PARTIAL
blocking:         NO
gates:            []
phase:            II
phase_links:      [III]
opened_on:        "v4.4.0"
resolved_on:      ~
owner:            unassigned
depends_on:       []
blocks:           []
related:          [RG-01]
summary: >
  Partial: basic pairs stack (beta, spread, z-score, half-life) on governed path.
  Johansen multi-leg, VECM error-correction, and ADF AIC lag selection explicitly
  deferred per roadmap.
  NOTE: Predates SA prefix adoption — kept as RG for ID stability.
acceptance_criteria:
  - Johansen multi-leg cointegration test implemented
  - VECM error-correction implemented
  - ADF AIC lag selection automated
evidence_needed:
  - code
  - tests
impact: Two-asset pairs only without Johansen — misses multi-leg spread opportunities.
resolution: ~
```

```yaml
id:               RG-07
type:             RG
title:            stat_arb — Leung-Li optimal stopping
status:           OPEN
blocking:         NO
gates:            []
phase:            II
phase_links:      []
opened_on:        "v4.4.0"
resolved_on:      ~
owner:            unassigned
depends_on:       []
blocks:           []
related:          [AQ-03]
summary: >
  OU process optimal stopping via Leung-Li (2015) not implemented. Entry/exit
  logic uses fixed z-score threshold (±2σ). Not on current build path.
  NOTE: Predates SA prefix adoption — kept as RG for ID stability.
acceptance_criteria:
  - Leung-Li (2015) framework reviewed and approach selected
  - OU process optimal stopping implemented or explicitly deferred with empirical comparison
  - comparison vs fixed ±2σ documented
evidence_needed:
  - doc-update
  - code
impact: Fixed thresholds leave early-exit value on the table for OU-reverting spreads.
resolution: ~
```

```yaml
id:               RG-08
type:             RG
title:            stat_arb — XGBoost breakdown classifier
status:           PARTIAL
blocking:         NO
gates:            []
phase:            II
phase_links:      []
opened_on:        "v4.4.0"
resolved_on:      ~
owner:            unassigned
depends_on:       [MLC-0]
blocks:           []
related:          []
summary: >
  Partial: XGBoost in stack/research plan and feature inputs (spread/beta/
  half-life/correlation) are on governed path. No training pipeline or
  breakdown classifier delivered — no produced artifact.
  NOTE: Predates SA prefix adoption — kept as RG for ID stability.
acceptance_criteria:
  - XGBoost breakdown classifier training pipeline implemented
  - feature inputs from governed path (spread, beta, half-life, correlation)
  - breakdown_classifier_report.json produced and included in bundle
evidence_needed:
  - code
  - tests
  - artifact
impact: Cointegration breakdown events are undetected without classifier.
resolution: ~
```

### RG-11 through RG-13 · Meta-learning and Data Research Gaps

```yaml
id:               RG-11
type:             RG
title:            meta-learning — inner-loop K gradient step budget
status:           OPEN
blocking:         NO
gates:            []
phase:            II
phase_links:      []
opened_on:        "v4.4.0"
resolved_on:      ~
owner:            unassigned
depends_on:       []
blocks:           [MLC-3]
related:          [MLC-3, GATE-II-01]
summary: >
  K gradient steps per task: too few = underfitting, too many = overfitting.
  Harvey t > 3.0 gate is the objective signal but K must be set before the gate
  can be run. Not implemented — Phase II ML-3 scope.
acceptance_criteria:
  - K step budget researched with reference to published Reptile implementations
  - initial K value selected with justification
  - sensitivity analysis: K sweep documented at Phase II research stage
evidence_needed:
  - doc-update
  - benchmark
impact: K underspecification leads to either underfitting or meta-overfitting.
resolution: ~
```

```yaml
id:               RG-12
type:             RG
title:            data — FRED ALFRED vintage accuracy
status:           PARTIAL
blocking:         NO
gates:            []
phase:            II
phase_links:      []
opened_on:        "v4.2.0"
resolved_on:      ~
owner:            unassigned
depends_on:       [OI-05]
blocks:           []
related:          [OI-05]
summary: >
  Partial: FREDVintageSeam and FREDApproximationStub implemented in v4.2.0.
  Retrieval-time approximation is explicit. True ALFRED vintage accuracy
  (knowledge_time ≠ valid_time for GDP revisions, payrolls) remains deferred.
  OI-05 closed on the seam; full ALFRED integration is open.
acceptance_criteria:
  - ALFRED API integrated for true vintage retrieval
  - knowledge_time correctly reflects data availability date (not valid_time)
  - GDP revision and payroll release patterns validated
  - FREDApproximationStub replaced by real ALFRED retrieval
evidence_needed:
  - code
  - tests
impact: PIT violations possible for macro-sensitive strategies using FRED data.
resolution: ~
```

```yaml
id:               RG-13
type:             RG
title:            data — corporate action lifecycle
status:           OPEN
blocking:         NO
gates:            []
phase:            II
phase_links:      []
opened_on:        "v4.4.0"
resolved_on:      ~
owner:            unassigned
depends_on:       []
blocks:           []
related:          []
summary: >
  Phase I handles listing/delist. Split/dividend adjustment, merger handling,
  and pair cointegration impact of corporate actions remain Phase II scope.
  Not implemented beyond listing/delist.
acceptance_criteria:
  - split adjustment implemented in DataView / source adapters
  - dividend adjustment implemented
  - merger handling: pair cointegration impact assessed and handled
evidence_needed:
  - code
  - tests
impact: Unadjusted splits/dividends create artificial breaks in price series — backtest bias.
resolution: ~
```

## Momentum Phase II / III Deferred Items

```yaml
id:               MOM-003
type:             MOM
title:            factor return columns (FF3/FF5/market) in DataView output
status:           DEFERRED
blocking:         NO
gates:            []
phase:            II
phase_links:      []
deferred_to_phase: II
strategy:         momentum
opened_on:        "v4.4.0"
resolved_on:      ~
owner:            unassigned
depends_on:       []
blocks:           []
related:          [RG-12]
summary: Confirm whether DataView.as_of(T) includes factor returns or a separate source adapter is required.
acceptance_criteria:
  - DataView factor column availability confirmed or new source adapter opened
evidence_needed:
  - doc-update
impact: ResidualOLS/ResidualKF cannot execute without factor return columns.
resolution: ~
```

```yaml
id:               MOM-004
type:             MOM
title:            sector column in DataView output
status:           DEFERRED
blocking:         NO
gates:            []
phase:            II
phase_links:      []
deferred_to_phase: II
strategy:         momentum
opened_on:        "v4.4.0"
resolved_on:      ~
owner:            unassigned
depends_on:       []
blocks:           []
related:          []
summary: Confirm presence of sector_col/gics_sector in DataView output; if absent, momentum_industry cannot execute.
acceptance_criteria:
  - sector column availability confirmed or DataView schema change opened
evidence_needed:
  - doc-update
impact: momentum_industry variant cannot execute without sector column.
resolution: ~
```

```yaml
id:               MOM-005
type:             MOM
title:            momentum.residual_kf KF kernel sharing
status:           DEFERRED
blocking:         NO
gates:            []
phase:            III
phase_links:      []
deferred_to_phase: III
strategy:         momentum
opened_on:        "v4.4.0"
resolved_on:      ~
owner:            unassigned
depends_on:       [RG-02]
blocks:           []
related:          [RG-02]
summary: Confirm whether stat_arb stats.kf_beta kernel can be shared or an independent Kalman implementation is required.
acceptance_criteria:
  - kernel sharing decision documented
  - if independent: implementation scoped
evidence_needed:
  - doc-update
impact: Duplicate KF implementations create maintenance burden and divergence risk.
resolution: ~
```

```yaml
id:               MOM-012
type:             MOM
title:            CrashOverrideConfig storage schema
status:           DEFERRED
blocking:         NO
gates:            []
phase:            III
phase_links:      []
deferred_to_phase: III
strategy:         momentum
opened_on:        "v4.4.0"
resolved_on:      ~
owner:            unassigned
depends_on:       []
blocks:           []
related:          []
summary: Extension of execution_assumptions.json or new momentum_policy.json in run bundle. Schema and path unresolved.
acceptance_criteria:
  - storage schema designed and documented
  - path in run bundle defined
evidence_needed:
  - doc-update
impact: CrashOverrideConfig values are unversioned and ungoverned without this.
resolution: ~
```

```yaml
id:               MOM-016
type:             MOM
title:            Kalman vs. OLS residualization bake-off
status:           DEFERRED
blocking:         NO
gates:            []
phase:            III
phase_links:      [II]
deferred_to_phase: III
strategy:         momentum
opened_on:        "v4.4.0"
resolved_on:      ~
owner:            unassigned
depends_on:       [MOM-005]
blocks:           []
related:          []
summary: Walk-forward comparison on identical universe/cost model. momentum_kalman locked to Experimental without bake-off report.
acceptance_criteria:
  - walk-forward bake-off run on identical universe and cost model
  - momentum_kalman_bakeoff_report.json produced
evidence_needed:
  - artifact
  - benchmark
impact: momentum_kalman locked to Experimental status until report produced.
resolution: ~
```

```yaml
id:               MOM-017
type:             MOM
title:            vol estimator bake-off
status:           DEFERRED
blocking:         NO
gates:            []
phase:            II
phase_links:      [III]
deferred_to_phase: II
strategy:         momentum
opened_on:        "v4.4.0"
resolved_on:      ~
owner:            unassigned
depends_on:       []
blocks:           []
related:          []
summary: EWMA vs Yang-Zhang vs GARCH for momentum.vol_scale. Update lowering only if net improvement demonstrated.
acceptance_criteria:
  - three estimators compared on identical data
  - momentum_vol_estimator_bakeoff_report.json produced
evidence_needed:
  - artifact
  - benchmark
impact: EWMA may underestimate vol in trending markets — affects VolScale signal quality.
resolution: ~
```

```yaml
id:               MOM-018
type:             MOM
title:            crash-prediction trigger calibration
status:           DEFERRED
blocking:         NO
gates:            []
phase:            III
phase_links:      []
deferred_to_phase: III
strategy:         momentum
opened_on:        "v4.4.0"
resolved_on:      ~
owner:            unassigned
depends_on:       [MOM-012]
blocks:           []
related:          []
summary: θ_credit, θ_crowding, L_crash, γ_crash values unspecified — pending empirical calibration across crisis and rebound windows.
acceptance_criteria:
  - calibration run across GFC and COVID crisis windows
  - CrashOverrideConfig values versioned and documented
evidence_needed:
  - benchmark
  - artifact
impact: Uncalibrated crash trigger fires too early or too late.
resolution: ~
```

```yaml
id:               MOM-019
type:             MOM
title:            value-momentum hybrid integration
status:           DEFERRED
blocking:         NO
gates:            []
phase:            II
phase_links:      [III, IV]
deferred_to_phase: II
strategy:         momentum
opened_on:        "v4.4.0"
resolved_on:      ~
owner:            unassigned
depends_on:       []
blocks:           []
related:          []
summary: Value and momentum are negatively correlated — naive blend cancels alpha. Research brief required before implementation.
acceptance_criteria:
  - research brief produced before implementation attempt
  - correlation structure documented across regimes
evidence_needed:
  - doc-update
impact: Naive hybrid without research brief risks cancelling alpha from both factors.
resolution: ~
```

```yaml
id:               MOM-021
type:             MOM
title:            data construction protocol for live trading
status:           DEFERRED
blocking:         NO
gates:            []
phase:            II
phase_links:      []
deferred_to_phase: II
strategy:         momentum
opened_on:        "v4.4.0"
resolved_on:      ~
owner:            unassigned
depends_on:       []
blocks:           []
related:          [RG-13]
summary: Four live failure modes unhandled in Phase I: delistings, borrow unavailability, stale prices, missing data. Required before live deploy.
acceptance_criteria:
  - all four failure modes handled or explicitly deferred with rationale
  - live data protocol documented
evidence_needed:
  - doc-update
  - code
impact: Unhandled live failure modes cause silent errors or crashes in production.
resolution: ~
```

```yaml
id:               MOM-022
type:             MOM
title:            return attribution decomposition
status:           DEFERRED
blocking:         NO
gates:            []
phase:            II
phase_links:      [III]
deferred_to_phase: II
strategy:         momentum
opened_on:        "v4.4.0"
resolved_on:      ~
owner:            unassigned
depends_on:       []
blocks:           []
related:          []
summary: Per layer marginal net Sharpe contribution via sequential stripping. Produces signal_card.diagnostics.attribution.
acceptance_criteria:
  - sequential stripping attribution implemented
  - gross and net attribution reported together
  - signal_card.diagnostics.attribution produced
evidence_needed:
  - code
  - artifact
impact: Cannot identify which momentum layers contribute without attribution.
resolution: ~
```

```yaml
id:               MOM-023
type:             MOM
title:            full framework vs. minimal benchmark ladder
status:           DEFERRED
blocking:         NO
gates:            []
phase:            II
phase_links:      [III]
deferred_to_phase: II
strategy:         momentum
opened_on:        "v4.4.0"
resolved_on:      ~
owner:            unassigned
depends_on:       []
blocks:           []
related:          []
summary: Seven-level ladder from raw momentum to full layered stack. Each level: CPCV/DSR/FDR validation.
acceptance_criteria:
  - all seven ladder levels defined and named
  - CPCV/DSR/FDR validation run at each level
  - momentum_benchmark_ladder_report.json produced
evidence_needed:
  - artifact
  - benchmark
impact: Without ladder, cannot isolate which layer contributes or degrades performance.
resolution: ~
```

```yaml
id:               MOM-024
type:             MOM
title:            cost, capacity, and implementation frontier
status:           DEFERRED
blocking:         NO
gates:            []
phase:            II
phase_links:      [III]
deferred_to_phase: II
strategy:         momentum
opened_on:        "v4.4.0"
resolved_on:      ~
owner:            unassigned
depends_on:       []
blocks:           []
related:          []
summary: AUM sweep by variant and participation rate. Breakeven AUM declared per variant; capacity caps set to 70% of breakeven.
acceptance_criteria:
  - AUM sweep run across all Phase I production variants
  - breakeven AUM declared per variant
  - capacity caps set to 70% of breakeven
  - momentum_capacity_frontier_report.json produced
evidence_needed:
  - artifact
  - benchmark
impact: Deploying above capacity cap destroys alpha through market impact.
resolution: ~
```

---

# 10. Phase III / IV (DEFERRED)

### ADR-004 · C++ Inference Scope Gate: Justify Before Build

```yaml
id:               ADR-004
type:             ADR
title:            C++ Inference Scope Gate — Justify Before Build
status:           CLOSED
blocking:         NO
gates:            []
phase:            III
phase_links:      []
adr_status:       ACCEPTED
decision_date:    "2026-02-xx"
options_considered: [build-now, justify-before-build]
decision:         >
  C++ inference layer not built until latency measurements from Phase II
  demonstrate Python/ONNX path is insufficient. JNI interface exists;
  native lib deferred. InferenceJNI interface contract frozen so C++ can
  plug in without changing Java caller.
consequences:
  - "Phase III budget reserved; not spent without Phase II latency proof"
  - "InferenceJNI interface contract frozen"
opened_on:        "v3.8.0"
resolved_on:      "v3.8.0"
owner:            unassigned
depends_on:       []
blocks:           []
related:          []
summary: >
  Phase II inference is batch (daily/hourly bars), not HFT. Build gate prevents
  over-engineering before performance problem is proven.
acceptance_criteria:
  - ADR published; C++ build blocked pending Phase II latency proof
  - InferenceJNI interface contract frozen
evidence_needed:
  - adr-decision
impact: ~
resolution: "Accepted. C++ inference remains deferred to Phase III pending latency justification."
```

---

# 11. Cross-Phase — Architectural Questions

*Note on AQ type:* `AQ` (Architectural Question) is an extension to the MRL schema added during initial population from ProjectState v4.4.0. AQ entries are pre-ADR decision forks — unresolved design questions that will require an ADR when decided, or move to RG if they resolve into empirical research. They are distinct from OI (work items) and RG (literature gaps). AQ entries close by graduating to an ADR or RG, not by implementation. The `evidence_needed` field uses `adr-decision` for items that close on a decision record.

### AQ-01 · z ∈ R⁶⁴ embedding dimension

```yaml
id:               AQ-01
type:             AQ
title:            z ∈ R⁶⁴ embedding dimension — empirical grounding
status:           OPEN
blocking:         NO
gates:            [GATE-I-F-05]
phase:            II
phase_links:      [I-F]
opened_on:        "v4.4.0"
resolved_on:      ~
owner:            unassigned
depends_on:       []
blocks:           [MLC-1, RG-10]
related:          [AQ-02, RG-10, MLC-1]
summary: >
  D=64 for context embedding is a placeholder, not empirically grounded.
  Too small → insufficient regime discrimination. Too large → overfitting
  on small task pools. Architecture committed before silhouette score gate runs.
  Confidence: Low.
acceptance_criteria:
  - at least two published sources reviewed for embedding dimension selection
  - D=64 justified with empirical or theoretical support, OR replaced with grounded value
  - justification documented before MLC-1 implementation begins
  - if uncertain, tiered research plan (blocking vs non-blocking relative to ML-1 milestone) defined
evidence_needed:
  - adr-decision
  - doc-update
impact: >
  Silent representation failure that passes Harvey t narrowly is harder to detect
  than failure that causes Harvey t < 3.0. Commitment before evidence risks
  systematic underdiscrimination of regime buckets.
resolution: ~
```

### AQ-02 · Context encoder architecture ceiling

```yaml
id:               AQ-02
type:             AQ
title:            Context encoder architecture ceiling — upgrade trigger
status:           OPEN
blocking:         NO
gates:            []
phase:            II
phase_links:      []
opened_on:        "v4.4.0"
resolved_on:      ~
owner:            unassigned
depends_on:       [AQ-01]
blocks:           []
related:          [AQ-01, RG-10, MLC-1, MLC-3]
summary: >
  2-layer MLP is Phase II baseline. SNAIL deferred to Phase III. No explicit
  upgrade criterion exists — Harvey t gate catches inner-loop failure but not
  representation failure that passes Harvey t narrowly. What signal triggers
  architecture change mid-Phase-II vs deferring to Phase III?
  Confidence: Medium.
acceptance_criteria:
  - explicit upgrade criterion defined: which metric at which threshold triggers change
  - criterion captures representation failure not detectable by Harvey t alone
  - criterion documented before MLC-1 implementation begins
evidence_needed:
  - adr-decision
  - doc-update
impact: Without upgrade criterion, architecture change decisions are ad-hoc and undocumented.
resolution: ~
```

### AQ-03 · Regime-conditional z-score thresholds

```yaml
id:               AQ-03
type:             AQ
title:            Regime-conditional z-score thresholds — Phase I-D vs Phase II
status:           OPEN
blocking:         NO
gates:            []
phase:            II
phase_links:      [I-E]
opened_on:        "v4.3.0"
resolved_on:      ~
owner:            unassigned
depends_on:       []
blocks:           [RG-04]
related:          [OI-07, RG-04, RG-07]
summary: >
  stat_arb shipped Phase I-D with fixed ±2σ thresholds. Decision fork remains:
  (a) implement regime-conditional thresholds in Phase I-E, coupling stat_arb
  to BOCPD before Phase II; or (b) upgrade at Phase II when regime model exists.
  Choice affects I-E scope and BOCPD dependency chain.
  Confidence: Low.
acceptance_criteria:
  - decision between option (a) and option (b) documented
  - if (b): explicit deferral condition stated (what triggers upgrade)
  - if (a): BOCPD dependency chain and I-E scope impact assessed
evidence_needed:
  - adr-decision
  - doc-update
impact: >
  Fixed ±2σ thresholds degrade performance when correlation structure changes
  during crisis. Deferring too long leaves stat_arb regime-blind in Phase II
  backtests.
resolution: ~
```

### AQ-04 · BOCPD op placement

```yaml
id:               AQ-04
type:             AQ
title:            BOCPD op placement — graph op vs. orchestrator regime service
status:           OPEN
blocking:         YES
gates:            [GATE-I-F-04]
phase:            II
phase_links:      [I-F]
opened_on:        "v4.4.0"
resolved_on:      ~
owner:            unassigned
depends_on:       []
blocks:           [RG-09, MLC-0]
related:          [RG-09, MLC-0, ADR-008, AQ-03]
summary: >
  BOCPD feeds RegimeLabeler (MLC-0) and is implied by AQ-03 for regime-
  conditional thresholds. Decision: BOCPD as graph op (inside feature execution
  path) or as separate regime service called by orchestrator? ADR-008
  single-path rule constrains answer — BOCPD over governed data must be PIT-safe.
  Confidence: Medium.
acceptance_criteria:
  - placement decision (graph op vs orchestrator service) documented
  - ADR-008 PIT boundary compliance confirmed for chosen approach
  - BOCPD interface compatible with RegimeLabeler (MLC-0) expectations
evidence_needed:
  - adr-decision
  - doc-update
impact: >
  Wrong placement creates PIT violation risk (if graph op bypasses DataView)
  or orchestrator coupling risk (if service creates hidden temporal dependency).
  Blocks MLC-0 and RG-09.
resolution: ~
```

### AQ-05 · KSB template governance

```yaml
id:               AQ-05
type:             AQ
title:            KSB (Knowledge Synthesis Board) template — governed doc or informal artifact
status:           OPEN
blocking:         NO
gates:            [GATE-I-F-01]
phase:            I-F
phase_links:      [II]
opened_on:        "v4.4.0"
resolved_on:      ~
owner:            unassigned
depends_on:       [OI-19]
blocks:           []
related:          [OI-19, AQ-06]
summary: >
  KSB identified as gap in ARB evaluation framework — no template exists.
  Decision: does KSB belong in governed doc suite (requiring release manifest
  entry and formatting-spec coverage) or remain an informal working artifact?
  Needs resolution before Phase II research synthesis begins.
  Confidence: Medium.
acceptance_criteria:
  - KSB governance decision documented
  - if governed: KSB template added to release manifest and formatting spec
  - if informal: rationale for exclusion documented
evidence_needed:
  - adr-decision
  - doc-update
impact: Phase II research synthesis begins without a structured knowledge capture format.
resolution: ~
```

### AQ-06 · Release manifest as canonical source of truth

```yaml
id:               AQ-06
type:             AQ
title:            Release manifest — schema, location, and update trigger
status:           OPEN
blocking:         YES
gates:            [GATE-I-F-01]
phase:            I-F
phase_links:      []
opened_on:        "v4.4.0"
resolved_on:      ~
owner:            unassigned
depends_on:       []
blocks:           [OI-19, OI-18]
related:          [OI-18, OI-19]
summary: >
  YAML/JSON release manifest identified as target architecture for documentation
  synchronization. Schema, location, and update trigger not designed. Without it,
  companion doc sync (OI-18) remains a manual checklist item rather than a
  governed process. F-1 prerequisite.
  Confidence: Medium.
acceptance_criteria:
  - manifest schema designed (YAML or JSON, fields defined)
  - canonical location in repo defined
  - update trigger defined (what event requires a manifest update)
  - MarketMind_Formatting_Spec.docx included in manifest scope (not exempt)
  - MRL schema identified as intermediate representation for manifest artifact types
evidence_needed:
  - adr-decision
  - doc-update
impact: >
  Without a governed manifest, companion doc sync is manual and drift-prone.
  I-F gate F-1 truthfulness review is a one-time manual pass, not a repeatable
  governed process.
resolution: ~
```

### AQ-07 · AlphaIR migration timing and ADR scope

```yaml
id:               AQ-07
type:             AQ
title:            AlphaIR migration timing and ADR scope
status:           OPEN
blocking:         YES
gates:            [GATE-I-F-03]
phase:            I-F
phase_links:      [II]
opened_on:        "v4.4.0"
resolved_on:      ~
owner:            unassigned
depends_on:       [OI-08]
blocks:           [MOM-001]
related:          [MOM-001, MLC-0]
summary: >
  AlphaIR lives in momentum.py in Phase I; migrates to srcPy/backtesting/contracts/
  at Phase II. ADR (MOM-001) must cover: version bump, new frozen-contract entry,
  bundle-manifest schema update, cross-language Java/C++ awareness. Silent move
  creates provenance gaps in downstream task library joining.
  Confidence: Low.
acceptance_criteria:
  - ADR scope defined: version bump, frozen-contract entry, manifest update, cross-language impact
  - migration plan documented before Phase II begins
  - MOM-001 formally opened as ADR work item
evidence_needed:
  - adr-decision
  - doc-update
impact: >
  Silent migration breaks provenance for ML-0 TaskRegistry joins. AlphaIR Phase I
  schema is a frozen contract — any migration must be an ADR-governed act.
resolution: ~
```

### AQ-08 · stats.rolling_vol Polars lowering resolution path

```yaml
id:               AQ-08
type:             AQ
title:            stats.rolling_vol Polars lowering — Phase II estimator choice
status:           CLOSED
blocking:         NO
gates:            []
phase:            II
phase_links:      []
opened_on:        "v4.4.0"
resolved_on:      "2026-03-16"
owner:            unassigned
depends_on:       []
blocks:           []
related:          [MOM-002, MOM-017]
summary: >
  Decision fork was moot for Phase I. The spec's own features_plan() example
  uses stats.rolling_std as the realized-vol source for momentum.vol_scale,
  making both fork options (implement rolling_vol lowering OR VolScale internal
  compute) unnecessary. rolling_std has a working Polars lowering and is the
  canonical Phase I vol source per §4.1. The stats.rolling_vol question is
  reframed as a Phase II estimator-bake-off item (see MOM-017: EWMA vs
  Yang-Zhang vs GARCH). No Phase I decision required.
acceptance_criteria:
  - Phase I: stats.rolling_std used as realized-vol source in all production variant plans
  - Phase II: MOM-017 (vol estimator bake-off) governs any upgrade from rolling_std
evidence_needed:
  - adr-decision
impact: ~
resolution: >
  Spec self-resolves. rolling_std is Phase I vol source by design. stats.rolling_vol
  work deferred to Phase II estimator bake-off (MOM-017). MOM-002 closed.
```

---

# 12. Cross-Phase — ADR-009 (Added 2026-03-16)

### ADR-009 · Package Root Canonicalization and Momentum Package Spine

```yaml
id:               ADR-009
type:             ADR
title:            Package Root Canonicalization and Momentum Package Spine
status:           CLOSED
blocking:         NO
gates:            [GATE-I-E-03]
phase:            I-E
phase_links:      [I-F]
adr_status:       ACCEPTED
decision_date:    "2026-03-19"
options_considered:
  - D1-A-srcPy-canonical
  - D1-B-migrate-to-marketmind
  - D2-A-flat-file-momentum.py
  - D2-B-package-spine-Phase-I
  - D3-A-ops-in-momentum-package
  - D3-B-ops-in-platform-preprocessor
  - D4-A-no-entry-py
  - D4-B-entry-py-Phase-I
decision: >
  D1: srcPy/ is canonical import root. marketmind/ is the Poetry project name
  only — not an importable package path. No migration required. Stat_arb v5 spec
  annotated with reconciliation note.
  D2: Package spine in Phase I. srcPy/strategies/momentum/ replaces flat
  momentum.py. plans/ subtree for variant FeaturePlan builders. entry.py,
  artifacts/, validation/, control/ (Phase III stub) introduced.
  D3: Momentum Ops (XSecRank, VolScale, ResidualOLS, ResidualKF, IndustryScore)
  in platform preprocessor ops_custom.py, consistent with stat_arb precedent.
  D4: entry.py introduced in Phase I as thin momentum-specific orchestration
  wrapper. Owns Steps 3-8 of execution chain. OrchestratorHooks=None enables
  unit testing without full platform context.
consequences:
  - "All path references use srcPy/ — marketmind/ never used as directory path"
  - "srcPy/strategies/momentum.py replaced by srcPy/strategies/momentum/ package"
  - "MomentumStrategy in strategy.py; AlphaIR in alpha_ir.py; exceptions in exceptions.py"
  - "plans/ subtree: xsec.py, tsmom.py, dual.py, residual.py; industry/ensemble/ml are stubs"
  - "artifacts/ subtree: signal_card.py, stat_validity.py"
  - "validation/ subtree: production_v1.py"
  - "control/ is Phase III stub with NotImplementedError invariant message"
  - "5 new Op subclasses in ops_custom.py; registered in factory.py register_builtin_ops()"
  - "entry.py responsibility boundary table frozen per §D4"
  - "MOM-015 resolved: OrchestratorHooks is Protocol in pipeline_strategy.py"
  - "MOM-013 placement resolved: ConvergenceError in exceptions.py"
  - "MOM-014 placement resolved: CostGateRejection in exceptions.py (exit code mapping still open)"
  - "MOM-001 location updated: AlphaIR in alpha_ir.py Phase I; migration to contracts/ at Phase II"
  - "pyproject.toml coverage handling updated from flat-file momentum.py to package-path momentum/* during the ADR-009 migration"
  - "Momentum Spec v1.3 blocked on ACCEPTED status of this ADR"
opened_on:        "2026-03-16"
resolved_on:      "2026-03-19"
owner:            Mark Wuenschel
depends_on:       [OI-08, ADR-001, ADR-002, ADR-007]
blocks:           [OI-08]
related:          [ADR-001, ADR-002, ADR-007, MOM-001, MOM-013, MOM-014, MOM-015, AQ-08]
summary: >
  Resolves four structural questions required before Momentum Spec v1.3 can be
  written and before a coding agent can begin implementation. D1 canonicalizes
  srcPy/ as the importable root (not marketmind/). D2 establishes the momentum
  package spine in Phase I with plans/ variant builders, artifacts/, validation/,
  and a Phase III control/ stub. D3 places momentum Ops in the platform
  preprocessor (ops_custom.py) consistent with stat_arb. D4 introduces entry.py
  as the momentum-specific orchestration wrapper owning crash override, artifact
  serialization, cost gates, and OrchestratorHooks injection.
  Status: ACCEPTED — package-spine decisions are now live and v1.3 implementation follows this ADR.
acceptance_criteria:
  - stat_arb v5 spec §3.1 carries reconciliation note per §D1
  - Momentum Spec v1.3 drafted incorporating R1–R7 from ADR-009 Readiness Gate
  - srcPy/strategies/momentum/ package structure matches §D2 topology
  - entry.py responsibility boundary table reflected in v1.3 §2.6
  - test directory structure per §Consequences committed
  - MOM-015 implementation complete (OrchestratorHooks Protocol in pipeline_strategy.py)
evidence_needed:
  - adr-decision
  - code
  - doc-update
impact: >
  Momentum Spec v1.3 cannot be written without this ADR in ACCEPTED status.
  OI-08 (momentum.py) coding agent delegation is blocked until v1.3 exists.
  Structural decisions made implicitly during implementation will require
  costly migration if not locked in advance.
resolution: >
  Accepted 2026-03-19. All four decisions confirmed by Mark: D1 (srcPy/ canonical
  import root, no migration), D2 (momentum/ package spine in Phase I), D3 (momentum
  ops in ops_custom.py per stat_arb precedent), D4 (entry.py in Phase I as thin
  orchestration wrapper). Momentum Spec v1.3 is now unblocked.
```

<!-- MM:END:DOCBODY -->
