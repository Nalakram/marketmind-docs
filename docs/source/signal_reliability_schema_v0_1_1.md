# Signal Reliability Layer — Schema Specification

<!-- MM:BEGIN:TITLEPAGE -->
**MarketMind — Signal Reliability Layer**
*Schema Specification v0.1.1*

Companion to: Meta-Learning Core v2.0.0 · Meta-Learning Architecture Vision v2.0.0 · Implementation Plan v6.4.13

Phase I-F contract-closure artifact · Phase II implementation track

<!-- MM:END:TITLEPAGE -->

---

<!-- MM:BEGIN:DOCBODY -->

## 0. Purpose and Scope

This specification defines the **Signal Reliability Layer**: a per-signal, per-timestamp metadata stream that models whether a signal's output should be trusted under current conditions, independently of the signal's expected return. It is not a replacement for `confidence_scalar`, which remains the allocator-level post-sizing attenuation term (Core v2.0.0 §2.5). Signal reliability operates one level below confidence: it provides per-signal conditional trustworthiness evidence that the meta-policy and confidence calibration can consume.

### 0.1 What Gets Scored

The scored object is a **tradeable signal output occupying an active slot in SignalCatalog**. Concretely: each `signal_id` / `slot_index` pair that the allocator weights via `allocation_weights`. This includes stat-arb spread/z-score variants, momentum variants, and any future AlphaIR-producing signal registered in the catalog.

**Out of scope for this layer:** task similarity, regime confidence, encoder coherence, and support/query consistency. These are conditioning/context diagnostics, not signals. They may serve as *inputs* to the reliability model, but they are not themselves scored objects. A separate `context_reliability` or `task_reliability` concept would be required to score those; that concept is not defined in this specification.

### 0.2 What Produces the Score

Phase II implementation determines the exact producer. The contract defined here is producer-agnostic: any component that can emit a conforming `SignalReliabilityState` record is a valid producer. The expected Phase II producer path is:

1. Context encoder emits `regime_embedding` z.
2. Per-signal historical evidence (IC decay, turnover, slippage sensitivity) is computed from governed run artifacts.
3. A lightweight reliability head (or rule-based scorer) consumes z, per-signal evidence, and optionally support/query consistency metrics to emit reliability dimensions per signal per timestamp.

The reliability head is *not* part of the inner loop. It runs on the inference path after the context encoder and before (or parallel to) the meta-policy.

### 0.3 Advisory vs. Gating Semantics

**Phase II default: advisory/consumable.** Signal reliability is emitted as a parallel metadata stream. The allocator *may* consume reliability dimensions as additional input features. Signal reliability **must not** hard-zero or hard-drop signals. This is consistent with the `confidence_scalar` contract: "must not be used as a gate on signal selection" and "any use outside [post-sizing attenuation] requires an ADR" (Core v2.0.0 §2.5).

**Promotion path to gating:** Any dimension promoted from advisory to hard-gate status requires:

- Ablation evidence showing net improvement on the walk-forward evaluation window.
- An explicit ADR documenting the policy change, the gating threshold, and the rollback trigger.
- The ADR must specify whether the gate is per-signal (drops a signal from the active set) or per-allocation (attenuates the allocation vector), and must demonstrate that the gating action does not violate Dynamic-K contract invariants (Architecture Vision v2.0.0 §4.4).

No hard gates from day one. Crisis retention and regime fragility are not exceptions.

### 0.4 Where Reliability Is Emitted

Signal reliability state is emitted as part of the nightly run artifact bundle, alongside `meta_validity_report.json` and `task_manifest.json`. The canonical schema lives at `schemas/signal_reliability.schema.json`. The per-run output file is `signal_reliability_report.json`, emitted through the governed bundle path (ADR-002).

Additionally, the fast-state reliability vector is available on the inference path for the meta-policy to consume. The meta-policy is not required to consume it in Phase II; consumption is opt-in and must be governed by the ablation evidence.

---

## 1. Schema: Fast State (Per-Signal, Per-Timestamp)

The fast state is the primary reliability record. One record per active signal per evaluation timestamp (typically per bar or per rebalance).

### 1.1 `SignalReliabilityState`

| Field | Type | Required | Description |
|---|---|---|---|
| `signal_id` | str | YES | Canonical signal identifier from SignalCatalog. |
| `slot_index` | int | YES | Immutable slot from Signal ABC registration (OI-25 contract). |
| `as_of` | datetime (ISO 8601) | YES | PIT timestamp. No data after this timestamp was used to compute any field. Enforced by `DataView.as_of(T)`. |
| `signal_set_version` | int | YES | Active signal set version at evaluation time. |
| `schema_version` | str | YES | `"v1"`. |
| **Reliability Dimensions** | | | |
| `persistence` | float ∈ [0, 1] | YES | Signal autocorrelation stability. 1 = highly persistent, 0 = decayed to noise. |
| `slippage_sensitivity` | float ∈ [0, 1] | YES | Robustness to execution slippage. 1 = insensitive, 0 = alpha destroyed by realistic slippage. |
| `crowding_sensitivity` | float ∈ [0, 1] | YES | Robustness to capacity/crowding. 1 = uncrowded, 0 = fully crowded. |
| `turnover_burden` | float ∈ [0, 1] | YES | Cost-adjusted turnover efficiency. 1 = low turnover relative to alpha, 0 = churning. |
| `regime_fragility` | float ∈ [0, 1] | YES | Stability across regime transitions. 1 = regime-robust, 0 = regime-fragile. Conditioned on current `regime_embedding` z. |
| `crisis_retention` | float ∈ [0, 1] | YES | Signal IC retention during crisis episodes. 1 = crisis-resilient, 0 = crisis-failed. Evaluated on held-out crisis windows per Anti-Goodhart protocol (Core v2.0.0 §9.1). |
| `signal_disagreement` | float ∈ [0, 1] | YES | Agreement with correlated signals. 1 = consensus, 0 = contradicts peers. |
| `state_dependency` | float ∈ [0, 1] | YES | Sensitivity to conditioning state (z, IC history). 1 = stable across states, 0 = highly state-dependent. |
| **Aggregate** | | | |
| `reliability_score` | float ∈ [0, 1] | YES | Weighted aggregate of dimensions. Weighting method documented in `calibration_provenance`. |
| **Evidence** | | | |
| `evidence_flags` | dict[str, bool] | YES | Flags indicating which evidence sources were available. Keys include: `ic_history_sufficient` (≥30 observations), `slippage_model_available`, `crowding_proxy_available`, `crisis_window_available`, `peer_signals_available`. |
| `evidence_coverage` | float ∈ [0, 1] | YES | Fraction of dimensions computed from actual evidence vs. prior/default. |

### 1.2 Polarity Convention

All dimensions use a **higher-is-more-reliable** polarity. A signal with all dimensions at 1.0 is maximally trustworthy; all dimensions at 0.0 is maximally suspect. This convention is locked and must not be inverted per-dimension.

### 1.3 Default / Missing-Evidence Behavior

If a dimension cannot be computed (evidence flag is false), the dimension value must be set to a documented prior. The default prior for all dimensions is `0.5` (agnostic). The `evidence_coverage` field must reflect the fraction of dimensions computed from actual evidence. A signal with `evidence_coverage = 0.0` is entirely prior-based and should be treated with appropriate skepticism by any consumer.

---

## 2. Schema: Slow State (Calibration and Provenance)

The slow state captures calibration metadata, fit provenance, and fold-level summary statistics. One record per signal per calibration window (typically per walk-forward fold or per nightly recalibration cycle).

### 2.1 `SignalReliabilityCalibration`

| Field | Type | Required | Description |
|---|---|---|---|
| `signal_id` | str | YES | Canonical signal identifier. |
| `slot_index` | int | YES | Immutable slot index. |
| `calibration_window_start` | datetime (ISO 8601) | YES | Start of the calibration window. |
| `calibration_window_end` | datetime (ISO 8601) | YES | End of the calibration window. |
| `fit_version` | str | YES | Version string of the reliability model/scorer used. |
| `signal_set_version` | int | YES | Signal set version at calibration time. |
| `schema_version` | str | YES | `"v1"`. |
| **Dimension Weights** | | | |
| `dimension_weights` | dict[str, float] | YES | Weights used in `reliability_score` aggregation. Keys are dimension names. Must sum to 1.0. |
| `weighting_method` | str | YES | One of: `equal`, `ic_weighted`, `learned`, `manual`. |
| **Fold-Level Statistics** | | | |
| `mean_reliability_by_regime` | dict[str, float] | YES | Mean `reliability_score` per 5-class `regime_class`. |
| `reliability_ic_correlation` | float | YES | Pearson correlation between `reliability_score` and realized next-window signal IC. This is the calibration quality metric. |
| `persistence_half_life_bars` | Optional[float] | NO | Estimated half-life of signal persistence in bars. |
| `crowding_proxy_source` | Optional[str] | NO | Identifies the crowding proxy used (e.g., `short_interest`, `etf_flow`, `none`). |
| `decay_rate_estimate` | Optional[float] | NO | Estimated IC decay rate per unit time. |
| **Provenance** | | | |
| `calibration_task_count` | int | YES | Number of tasks used in calibration. |
| `calibration_bar_count` | int | YES | Number of bars in calibration window. |
| `pit_boundary` | datetime (ISO 8601) | YES | PIT enforcement boundary for calibration data. |

---

## 3. Run-Level Report: `signal_reliability_report.json`

Emitted per nightly run as a bundle artifact. Contains all fast-state records for the run plus a summary block.

### 3.1 Top-Level Structure

```json
{
  "schema_version": "v1",
  "run_id": "<run identifier>",
  "as_of": "<ISO 8601 timestamp>",
  "signal_set_version": 7,
  "signal_count": 5,
  "signals": [
    { "...SignalReliabilityState fields..." }
  ],
  "summary": {
    "mean_reliability": 0.72,
    "min_reliability_signal_id": "stat_arb_zscore_v1",
    "min_reliability_score": 0.41,
    "low_evidence_signals": ["momentum_dual_v1"],
    "dimension_means": {
      "persistence": 0.78,
      "slippage_sensitivity": 0.65,
      "crowding_sensitivity": 0.80,
      "turnover_burden": 0.71,
      "regime_fragility": 0.68,
      "crisis_retention": 0.55,
      "signal_disagreement": 0.82,
      "state_dependency": 0.74
    }
  },
  "calibration_ref": {
    "fit_version": "v1.0.0",
    "calibration_window_end": "<ISO 8601>",
    "calibration_task_count": 160
  }
}
```

### 3.2 Bundle Integration

`signal_reliability_report.json` is a governed bundle artifact emitted through BundleWriter on the ADR-002 canonical path. It is written after `meta_validity_report.json` and before `bundle_manifest.json`. The bundle manifest must include a reference to the reliability report with its CAS hash.

---

## 4. Relationship to Existing Contracts

### 4.1 `confidence_scalar` (Core v2.0.0 §2.5)

`confidence_scalar` is an allocator-level calibrated reliability estimate for the *entire* meta-policy allocation. Signal reliability is a per-signal input that `confidence_scalar` calibration *may* consume. The relationship is:

- Signal reliability dimensions are per-signal evidence.
- `confidence_scalar` is a portfolio-level summary that may incorporate signal reliability alongside encoder coherence, support/query consistency, and signal-set familiarity.
- Signal reliability does not replace, override, or compete with `confidence_scalar`. It feeds it.

### 4.2 `signal_embedding` (Architecture Vision v2.0.0 §4.6)

`signal_embedding` is a per-signal *identity* vector for retrieval and catalog organization (Phase IV). Signal reliability is per-signal *state* metadata conditioned on current market conditions. These are orthogonal:

- `signal_embedding` answers: "what kind of signal is this?"
- Signal reliability answers: "how trustworthy is this signal right now?"

Signal reliability does not depend on `signal_embedding` being a learned vector. `signal_embedding` remains `None` through Phase II. The reliability layer must function without it.

### 4.3 `regime_embedding` z (Architecture Vision v2.0.0 §4.6)

`regime_embedding` is a required input to the reliability computation for regime-conditional dimensions (`regime_fragility`, `crisis_retention`, `state_dependency`). The reliability layer is downstream of the context encoder (ML-1) on the inference path.

### 4.4 `meta_validity_report.json` (Core v2.0.0 §2.7)

The meta-validity report carries portfolio-level and model-level evidence. Signal reliability is signal-level evidence. The two are complementary and should be cross-referenced:

- `meta_validity_report.json` field `confidence_ece` may incorporate reliability-informed calibration.
- `signal_reliability_report.json` field `reliability_ic_correlation` (from slow state) provides calibration-quality evidence that the meta-learner gate (ML-6) can inspect.

A future extension (not in this spec) could add a `signal_reliability_summary` block to `meta_validity_report.json`.

### 4.5 `task_manifest.json` (Core v2.0.0 §2.7)

Task manifest carries `signal_ids_hash` and `signal_set_version`. Signal reliability carries the same `signal_set_version` for provenance alignment. No direct dependency beyond version consistency.

### 4.6 Dynamic-K Contract (Architecture Vision v2.0.0 §4.4)

Signal reliability records are emitted only for active signals (`slot_index` ∈ 0..K-1). Retired/masked slots do not receive reliability records. If a signal is retired, its last reliability record is preserved in the calibration history but no new fast-state records are emitted.

---

## 5. Kill Condition

### 5.1 Evaluation Protocol

The signal reliability layer is evaluated via ablation:

- **Treatment:** Same allocator with reliability dimensions available as input features.
- **Control:** Same allocator without reliability dimensions (baseline Phase II configuration).
- **Primary metric:** Net Sharpe after transaction costs on the full walk-forward validation window (same window as the meta-learning program's primary evaluation, Core v2.0.0 §9.3).
- **Secondary constraints (must not degrade):**
  - Crisis IC on held-out crisis episodes (Anti-Goodhart protocol).
  - Maximum drawdown profile.
  - Confidence calibration (ECE must not worsen).

### 5.2 Kill Threshold

**No net improvement on primary metric → keep as diagnostic only.** Specifically:

- If net Sharpe with reliability ≤ net Sharpe without reliability across the full walk-forward window, the reliability layer is not promoted to allocator input.
- It remains available as a diagnostic/monitoring artifact in `signal_reliability_report.json`.
- Diagnostic-only status means: emitted per run, visible on dashboards, available for operator inspection, but not consumed by any allocation or sizing logic.

### 5.3 Partial Kill

Individual reliability dimensions may be killed independently. If ablation shows that a subset of dimensions improves performance while others add noise, the non-contributing dimensions are dropped from the allocator input vector but retained in the diagnostic report. The `dimension_weights` in the slow state reflect which dimensions are active.

---

## 6. Phase Placement

### 6.1 Phase I-F (Now)

**Deliverables:**
- This specification (`docs/src/signal_reliability_schema_v0_1_1.md`).
- JSON schema (`schemas/signal_reliability.schema.json`).
- Resolution Ledger entries (OI and GATE entries for Phase I-F contract closure and Phase II implementation).

**Purpose:** Resolve the schema boundary so Phase II does not start with ambiguous reliability semantics. This is an OI-22 (F-4) adjacent contract: it defines a signal output contract component that the meta-policy path will consume.

### 6.2 Phase II (Implementation)

**Where it touches existing Phase II milestones:**

| Milestone | Interaction |
|---|---|
| ML-1 (Context Encoder) | Reliability computation consumes `regime_embedding` z. Downstream dependency. |
| ML-4 (Meta-Policy Network) | Meta-policy may consume `reliability_score` or individual dimensions as optional input features. Opt-in, governed by ablation. |
| ML-6 (MetaLearner Gate) | Gate may inspect `reliability_ic_correlation` from slow state as calibration-quality evidence. |
| W1 (Baseline Superiority) | Reliability ablation is a sub-experiment within W1: baseline with/without reliability. |
| W5 (Portfolio-Level Validation) | Reliability's kill condition is evaluated as part of W5 walk-forward. |

**Not a detached parallel lane.** Signal reliability is a cross-cutting Phase II concern that plugs into ML-4/ML-6 territory. It does not have its own MLC milestone; it is evaluated as part of the existing workstream structure.

### 6.3 Not Phase III/IV

Signal reliability affects whether the allocator's outputs should be trusted. This is earlier than execution expansion (Phase III) and Signal Factory scale-out (Phase IV). The reliability layer must be resolved before those phases can meaningfully extend the signal universe, because extending the universe without per-signal trustworthiness assessment compounds risk.

---


## 7. Proposed Resolution Ledger Entries (Informative)

This section mirrors the **Resolution Ledger** abbreviation and entry style so the specification carries its own unresolved implementation inventory. These entries are **proposed** until opened in `ResolutionLedger.md`. The ledger remains authoritative once the IDs are formally registered.

Live-ledger note: `OI-35`, `OI-36`, and `OI-42` were already assigned to different items in the canonical ledger, so the reliability-track IDs below use `OI-41` and `OI-43` to avoid silent reassignment.

### 7.1 Open Items

### OI-41 · Signal Reliability Layer schema contract and JSON schema

```yaml
id:               OI-41
type:             OI
title:            Signal Reliability Layer schema contract and JSON schema
status:           OPEN
blocking:         YES
gates:            [GATE-I-F-04]
phase:            I-F
phase_links:      [II]
opened_on:        "v4.8.0"
resolved_on:      ~
owner:            unassigned
depends_on:       [OI-22]
blocks:           [OI-43]
related:          [MLN-03, OI-22, OI-25]
summary: >
  Define the Signal Reliability Layer contract boundary so Phase II does not
  start with ambiguous per-signal trustworthiness semantics. Deliverables:
  this prose specification and the machine-readable JSON schema. Advisory-only
  semantics are locked for Phase II v1; any promotion to hard gating requires a
  separate ADR with ablation evidence. Reliability is keyed by signal_id /
  slot_index, is downstream of the context encoder, and is parallel metadata
  rather than part of signal identity.
acceptance_criteria:
  - signal_reliability_schema_v0_1_1.md published as governing prose spec
  - schemas/signal_reliability.schema.json validates against the prose spec
  - fast state covers 8 reliability dimensions + aggregate + evidence fields
  - slow state covers calibration provenance, dimension weights, and fold-level stats
  - relationship to confidence_scalar, signal_embedding, regime_embedding documented
  - advisory-only semantics documented; promotion path to gating requires ADR
  - kill condition and ablation protocol documented
  - OI-22 acceptance criteria updated to include reliability contract compatibility
evidence_needed:
  - doc-update
  - schema
impact: >
  Without this contract, Phase II reliability work starts ambiguously. The
  meta-policy may silently assume reliability semantics that conflict with
  confidence routing, artifact contracts, or Dynamic-K invariants.
resolution: ~
```

### OI-43 · Signal Reliability Layer Phase II implementation and ablation

```yaml
id:               OI-43
type:             OI
title:            Signal Reliability Layer Phase II implementation and ablation
status:           OPEN
blocking:         NO
gates:            [GATE-II-01]
phase:            II
phase_links:      []
opened_on:        "v4.8.0"
resolved_on:      ~
owner:            unassigned
depends_on:       [OI-41, MLN-03]
blocks:           []
related:          [AQ-09, AQ-10, AQ-11, AQ-12, AQ-13, RG-14, RG-15, RG-16, RG-17, RG-18]
summary: >
  Implement the reliability scorer or rule-based head, emit
  signal_reliability_report.json through the governed bundle path, populate
  slow-state calibration provenance, and run the kill-condition ablation
  against the alpha-only baseline. Reliability remains diagnostic-only unless
  net walk-forward evidence justifies allocator consumption.
acceptance_criteria:
  - conforming SignalReliabilityState records emitted per active signal per rebalance
  - signal_reliability_report.json emitted in nightly governed bundles
  - slow-state calibration provenance populated per fold or recalibration cycle
  - allocator integration path is opt-in and disabled by default
  - kill-condition ablation completed on the full walk-forward window
  - if no net improvement: reliability remains diagnostic-only
  - if net improvement: active dimensions and weighting documented before promotion
evidence_needed:
  - code
  - tests
  - artifact
  - ablation-results
impact: >
  This is the implementation counterpart to OI-41. Without it, reliability
  remains a paper contract with no governed artifact, no calibration evidence,
  and no allocator-side proof burden.
resolution: ~
```

### 7.2 Architectural Questions

### AQ-09 · Crowding proxy feasibility for Phase II reliability

```yaml
id:               AQ-09
type:             AQ
title:            Crowding proxy feasibility for Phase II reliability
status:           OPEN
blocking:         NO
gates:            []
phase:            II
phase_links:      []
opened_on:        "v4.8.0"
resolved_on:      ~
owner:            unassigned
depends_on:       []
blocks:           [OI-43]
related:          [OI-41, RG-14]
summary: >
  Which crowding proxy is feasible for Phase II v1? Candidate sources include
  short-interest data, ETF ownership/flow proxies, correlation-concentration
  proxies, or explicit deferral to prior-default behavior if external data is
  unavailable. Decision is needed before crowding_sensitivity is treated as
  more than a placeholder dimension.
acceptance_criteria:
  - crowding proxy source identified or explicitly deferred with prior-default fallback
  - evidence_flags semantics updated to match the chosen proxy path
evidence_needed:
  - doc-update
impact: >
  Crowding sensitivity quality is capped by proxy quality. Silent proxy drift
  would make the dimension look precise while remaining structurally weak.
resolution: ~
```

### AQ-10 · Signal disagreement metric definition

```yaml
id:               AQ-10
type:             AQ
title:            Signal disagreement metric definition
status:           OPEN
blocking:         NO
gates:            []
phase:            II
phase_links:      []
opened_on:        "v4.8.0"
resolved_on:      ~
owner:            unassigned
depends_on:       []
blocks:           [OI-43]
related:          [OI-41, RG-15]
summary: >
  Should signal_disagreement be defined via pairwise IC correlation among
  active signals, sign-agreement / rank-agreement statistics, or a broader
  factor-model residual approach? The decision changes both computational
  cost and what the dimension semantically means.
acceptance_criteria:
  - signal_disagreement metric definition selected and documented
  - required peer-signal evidence fields identified
evidence_needed:
  - doc-update
impact: >
  A weak disagreement metric will confound contradiction, diversification, and
  latent-factor exposure, reducing the usefulness of the dimension in both
  diagnostics and allocator input.
resolution: ~
```

### AQ-11 · Minimum history threshold for non-prior dimensions

```yaml
id:               AQ-11
type:             AQ
title:            Minimum history threshold for non-prior reliability dimensions
status:           OPEN
blocking:         NO
gates:            []
phase:            II
phase_links:      []
opened_on:        "v4.8.0"
resolved_on:      ~
owner:            unassigned
depends_on:       []
blocks:           [OI-43]
related:          [OI-41, RG-16]
summary: >
  What minimum history length is required before persistence,
  slippage_sensitivity, and related dimensions are computed from actual
  evidence instead of default prior values? Candidate threshold: 30
  observations, but this is currently a placeholder rather than a validated
  floor.
acceptance_criteria:
  - minimum observation count documented and justified
  - evidence_flags and evidence_coverage behavior aligned to the threshold
evidence_needed:
  - doc-update
impact: >
  Threshold too low → noisy pseudo-evidence. Threshold too high → most early
  runs collapse to prior-only scoring and provide little operational value.
resolution: ~
```

### AQ-12 · Reliability score aggregation method for Phase II v1

```yaml
id:               AQ-12
type:             AQ
title:            Reliability score aggregation method for Phase II v1
status:           OPEN
blocking:         NO
gates:            []
phase:            II
phase_links:      []
opened_on:        "v4.8.0"
resolved_on:      ~
owner:            unassigned
depends_on:       []
blocks:           [OI-43]
related:          [OI-41, RG-17]
summary: >
  Should reliability_score use equal weights, IC-weighted aggregation,
  monotone learned weights, or remain dimension-only with no promoted scalar in
  Phase II v1? The trade-off is between interpretability, data hunger, and
  overfitting risk.
acceptance_criteria:
  - weighting method selected for Phase II v1 and documented in slow-state provenance
  - fallback path defined if learned weighting is rejected or underpowered
evidence_needed:
  - doc-update
impact: >
  A premature learned aggregate could create a false sense of calibration,
  while a crude scalar could collapse genuinely distinct failure modes into one
  opaque number.
resolution: ~
```

### AQ-13 · Reliability head retrain strategy vs continual-learning protection

```yaml
id:               AQ-13
type:             AQ
title:            Reliability head retrain strategy vs continual-learning protection
status:           OPEN
blocking:         NO
gates:            []
phase:            II
phase_links:      []
opened_on:        "v4.8.0"
resolved_on:      ~
owner:            unassigned
depends_on:       []
blocks:           [OI-43]
related:          [OI-41, MLN-05, RG-18]
summary: >
  If the reliability head is learned rather than rule-based, does it need its
  own replay / EWC-style protection, or is it lightweight enough to retrain
  from scratch on each cycle? If rule-based, the question resolves to "not
  applicable," but that determination must still be recorded explicitly.
acceptance_criteria:
  - training strategy decision documented with rationale
  - interaction with frozen inference boundary and nightly wall-clock budget noted
evidence_needed:
  - doc-update
impact: >
  Underestimating catastrophic forgetting risk can make the layer unstable
  precisely during regime transitions, which is the period where reliability
  evidence matters most.
resolution: ~
```

### 7.3 Research Gaps

### RG-14 · Crowding proxy benchmarking across signal families

```yaml
id:               RG-14
type:             RG
title:            Crowding proxy benchmarking across signal families
status:           OPEN
blocking:         NO
gates:            []
phase:            II
phase_links:      [III]
opened_on:        "v4.8.0"
resolved_on:      ~
owner:            unassigned
depends_on:       [AQ-09]
blocks:           []
related:          [OI-43]
summary: >
  Even after a Phase II crowding proxy is chosen, the broader research problem
  remains open: which proxy family best tracks crowding fragility across
  momentum, stat-arb, and future AlphaIR signals? A proxy sufficient for one
  family may be misleading for another.
acceptance_criteria:
  - at least two candidate proxy families benchmarked across multiple signal families
  - proxy stability and false-confidence failure modes documented
evidence_needed:
  - ablation-results
  - doc-update
impact: >
  A single crowding proxy may overfit one signal family and silently
  underrepresent capacity risk elsewhere.
resolution: ~
```

### RG-15 · Disagreement semantics: contradiction vs diversification

```yaml
id:               RG-15
type:             RG
title:            Disagreement semantics: contradiction vs diversification
status:           OPEN
blocking:         NO
gates:            []
phase:            II
phase_links:      [III]
opened_on:        "v4.8.0"
resolved_on:      ~
owner:            unassigned
depends_on:       [AQ-10]
blocks:           []
related:          [OI-43]
summary: >
  Signal disagreement may capture useful contradiction, benign diversification,
  or simple style dispersion. Research is needed to separate "peer conflict
  that predicts failure" from "peer diversity that improves portfolio
  robustness."
acceptance_criteria:
  - at least one study distinguishes harmful disagreement from beneficial diversification
  - diagnostic interpretation guidance documented
evidence_needed:
  - ablation-results
  - doc-update
impact: >
  Treating all disagreement as negative may suppress genuinely complementary
  signals and reduce diversification benefits.
resolution: ~
```

### RG-16 · Multi-target reliability vs single scalar trust score

```yaml
id:               RG-16
type:             RG
title:            Multi-target reliability vs single scalar trust score
status:           OPEN
blocking:         NO
gates:            []
phase:            II
phase_links:      [III]
opened_on:        "v4.8.0"
resolved_on:      ~
owner:            unassigned
depends_on:       [AQ-11, AQ-12]
blocks:           []
related:          [OI-41, OI-43]
summary: >
  The broader corpus favors a multi-target formulation (retention ratio,
  net-alpha-positive label, stress-failure flag, decay half-life) over a
  single opaque trust scalar. This spec currently standardizes one aggregate
  plus dimensions, but the deeper target formulation remains an open research
  problem.
acceptance_criteria:
  - scalar-only vs multi-target formulation compared on at least one walk-forward program
  - recommendation documented for post-v1 schema evolution
evidence_needed:
  - ablation-results
  - doc-update
impact: >
  Forcing all reliability evidence into one scalar may erase clinically
  different failure modes and limit future governance options.
resolution: ~
```

### RG-17 · Rule-based / monotone scorer vs learned reliability head

```yaml
id:               RG-17
type:             RG
title:            Rule-based / monotone scorer vs learned reliability head
status:           OPEN
blocking:         NO
gates:            []
phase:            II
phase_links:      [III]
opened_on:        "v4.8.0"
resolved_on:      ~
owner:            unassigned
depends_on:       [AQ-12]
blocks:           []
related:          [OI-43, AQ-13]
summary: >
  The current research direction prefers interpretable monotone models for the
  first reliability wave, but the boundary between rule-based scoring,
  monotone learned calibration, and deeper black-box heads remains open. This
  gap should be resolved by evidence, not rhetoric.
acceptance_criteria:
  - at least one interpretable scorer and one learned scorer compared under the same evaluation protocol
  - recommendation documented for v1 and post-v1 implementations
evidence_needed:
  - ablation-results
  - doc-update
impact: >
  Choosing model complexity too early risks overfitting; choosing it too late
  may leave real predictive structure unused.
resolution: ~
```

### RG-18 · Reliability interaction with confidence routing and allocator placement

```yaml
id:               RG-18
type:             RG
title:            Reliability interaction with confidence routing and allocator placement
status:           OPEN
blocking:         NO
gates:            []
phase:            II
phase_links:      [III]
opened_on:        "v4.8.0"
resolved_on:      ~
owner:            unassigned
depends_on:       [AQ-13]
blocks:           []
related:          [MLN-03, OI-43]
summary: >
  The contract says reliability feeds allocator confidence rather than
  replacing it, but the exact best placement remains unresolved: separate
  per-signal feature input, scalar attenuation input, veto candidate, or
  purely diagnostic sidecar. This requires controlled ablation rather than a
  documentation-only choice.
acceptance_criteria:
  - at least two integration modes compared against a diagnostic-only baseline
  - final recommended placement documented before any promotion beyond advisory semantics
evidence_needed:
  - ablation-results
  - doc-update
impact: >
  Incorrect placement could double-count uncertainty, blur responsibility
  between signal trust and allocator confidence, or create hidden gating
  semantics.
resolution: ~
```

### 7.4 Gate / Contract Crosswalk

The following ledger-facing updates are implied by this specification:

- **GATE-I-F-04** should include publication of the Signal Reliability Layer contract
  (`signal_reliability_schema_v0_1_1.md` + `schemas/signal_reliability.schema.json`)
  as acceptance evidence.
- **OI-22** should explicitly mention compatibility with the Signal Reliability
  contract in addition to AlphaIR / meta-policy path compatibility.
- **MLN-03** should remain the normative boundary for `confidence_scalar`; this
  specification defines reliability as per-signal evidence that may feed
  confidence routing but does not replace or override it.

---

<!-- MM:END:DOCBODY -->

<!-- MM:BEGIN:SOURCE_STAMP -->

*Signal Reliability Schema v0.1.1 · March 2026 · Companion to Meta-Learning Core v2.0.0 · Meta-Learning Architecture Vision v2.0.0 · Implementation Plan v6.4.13*

<!-- MM:END:SOURCE_STAMP -->
