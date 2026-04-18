**MarketMind**

────────────────────────────────

**Phase II Artifact Contract**

<!-- MM:BEGIN:TITLEPAGE -->
Version 1.0.3 · April 2026 · Proprietary

Companion documents: Implementation Plan v6.5.9 · Technical Roadmap v1.4.30 · Meta-Learning Core v1.2.25 · Meta-Learning Architecture Vision v1.3.6 · Resolution Ledger v1.0.52 · README.md 7.2.2 · VERSION.md 7.2.2
<!-- MM:END:TITLEPAGE -->

*Governed contract for required Phase II artifact surfaces, minimum evidence payloads, and fail-closed completeness rules*

*Audience: Internal engineering, technical stakeholders*

<!-- MM:BEGIN:DOCBODY -->

# 1. Purpose

This contract defines the minimum artifact surfaces and evidence chain required for governed Phase II work. It exists so that Phase II validation, promotion review, and kill decisions are anchored to immutable emitted evidence rather than narrative summaries or recomputed judgments.

Point-in-time definitions are not restated here. [`DataGovernanceCharter.md`](DataGovernanceCharter.md) governs PIT semantics, visibility, vintage handling, and universe discipline.

# 2. Principle

Phase II claims are valid only if the required artifacts exist, are internally consistent, and preserve the evidence chain needed to reproduce the decision surface honestly.

This contract governs the artifact surface, not the underlying storage implementation. It does not define CAS mechanics, registry internals, or release-manifest taxonomy.

# 3. Required Artifact Set

Every governed Phase II run that is offered as validation, shadow-entry evidence, promotion evidence, rollback evidence, or kill evidence must emit the following artifacts as a minimum set:

| Artifact | Purpose | Required for governed Phase II? |
|---|---|---|
| `task_manifest.json` | Exact task-pool and boundary evidence | Yes |
| `meta_validity_report.json` | Canonical validation evidence for adaptation, coherence, forgetting, crisis behavior, and baseline comparison | Yes |
| `execution_assumptions.json` | Cost, slippage, borrow, latency, and execution-context assumptions | Yes |

If any of the three is absent, the run is incomplete and may not be used as governed Phase II evidence.

As of `VERSION.md` 7.0.0, each artifact in the governed triple must also carry a required top-level `content_hash` object. The hash is non-recursive: it is computed over the canonical JSON document with the `content_hash` field omitted.

| `content_hash` field | Requirement |
|---|---|
| `algorithm` | `sha256` |
| `canonicalization` | `json.sort_keys.no_ws.omit_content_hash.v1` |
| `value` | `sha256:<64 lowercase hex characters>` |

# 4. `task_manifest.json`

`task_manifest.json` is the task-pool evidence surface. It records what the system believed the tasks were when the run was executed.

Minimum required content:

| Field | Requirement |
|---|---|
| `task_id` | Stable task identifier |
| `regime_id` | Compositional regime identity |
| `regime_class` | Level 2 projected regime class for the task |
| `t0` / `t1` | Episode start and end |
| `pit_boundary` | Governed task boundary |
| `signal_ids_hash` | Deterministic signal-set identity for the task |
| `signal_set_version` | Versioned signal-set surface used by the run |
| `content_hash` | Required non-recursive canonical hash for the artifact payload |

This artifact does not redefine PIT semantics. It declares which boundary was used; the meaning of that boundary is owned by the Data Governance Charter.

# 5. `meta_validity_report.json`

`meta_validity_report.json` is the canonical Phase II evidence surface for validation and gate review.

Minimum required fields:

| Field | Required meaning |
|---|---|
| `schema_version` | Version of the report contract |
| `inner_loop_gain_by_regime` | Adaptation gain broken out by governed regime bucket |
| `harvey_t_statistic` | Governing statistical evidence for the claimed adaptation effect |
| `encoder_coherence_score` | Evidence that the encoder produces a coherent structure rather than noise |
| `crisis_episode_ic` | Held-out crisis-episode performance evidence |
| `forgetting_metric` | Continual-learning degradation surface |
| `plasticity_metric` | Evidence that new-task adaptation still works while retaining prior knowledge |
| `baseline_comparison` | Explicit incumbent comparison surface; see Section 7 |
| `pit_compliance_flag` | Derived from enforcement (e.g., DataLineageGate / PIT invariants); must not be a self-declared field |
| `confidence_calibration` | Governed confidence-calibration object with schema/version, reporting gate (`PASS|FAIL|INSUFFICIENT`), ECE payload, reliability reference, recalibration status, and routing-pilot boundary metadata |
| `threshold_references` | Canonical threshold-reference block; stored `state` and `current_expression` must match the governing register row |
| `content_hash` | Required non-recursive canonical hash for the artifact payload |

Additional fields may exist, but omission of any field above is a contract failure for governed Phase II evidence.

`confidence_calibration` is fail-closed on governed paths:
- if calibration is measured and status indicates `PASS`, ECE must be a finite numeric value and non-negative;
- if calibration is not measured on-path, emit explicit `INSUFFICIENT` with reason;
- malformed or contradictory calibration payloads are contract failures.

The following field name is not part of the governed contract and must not be used as a substitute:

- `proxy_alignment_score`

If proxy alignment is evaluated in a later edition, it must be introduced with explicit contract wording rather than by ambiguous field drift.

# 6. `execution_assumptions.json`

`execution_assumptions.json` is required because Phase II evidence is invalid if it compares allocation quality under unknown or drifting cost assumptions.

Minimum expectation:

| Concern | Requirement |
|---|---|
| Cost assumptions | Explicitly declared |
| Slippage / impact surface | Explicitly declared at the fidelity supported by the run |
| Borrow / funding assumptions | Declared where relevant |
| Latency / fill assumptions | Declared where relevant |
| Shared comparison context | Sufficient to prove that challenger and baseline used the same execution realism assumptions |
| Content hash | Required non-recursive canonical hash for the artifact payload |

Missing execution assumptions is not a documentation gap. It is a governed evidence failure.

# 7. Evidence Chain

The three required artifacts must agree on the identity of the run they describe.

Evidence-chain rules:

| Rule | Requirement |
|---|---|
| Identity consistency | Task-pool identity, signal-set identity, and run identity must not conflict across artifacts |
| Baseline consistency | Baseline comparisons cited in `meta_validity_report.json` must be reproducible from the same governed data and assumption surfaces |
| PIT consistency | Any PIT compliance declaration must align with the task boundary and data-access path used by the run |
| Version consistency | Regime-definition and threshold references must declare the governing version or assumption state used |

The Threshold Governance Register does not live here, but when threshold-backed claims appear in the report, the report must reference threshold IDs rather than free-floating prose placeholders. [`ThresholdGovernanceRegister.md`](ThresholdGovernanceRegister.md) governs that discipline.

# 8. Baseline Anchoring

Phase II evidence is anchored to the incumbent simpler baseline. The incumbent baseline comparison uses:

- XGBoost baseline,
- identical data,
- identical splits,
- identical cost assumptions.

These constraints are mandatory. A comparison that changes data, split logic, or cost assumptions between challenger and incumbent is not a valid baseline comparison under this contract.

`baseline_comparison` must therefore record, at minimum:

| Subfield | Requirement |
|---|---|
| baseline identity | Must identify the XGBoost incumbent baseline |
| data parity | Must state that identical data was used |
| split parity | Must state that identical splits were used |
| assumption parity | Must state that identical execution-cost assumptions were used |
| net result | Must report whether the challenger beat the incumbent net of costs |

Missing baseline comparison is a fail condition.

# 9. Anti-Goodhart Enforcement

Held-out crisis evidence is not decorative. Phase II artifacts must preserve it as a first-class output.

The contract requires explicit treatment of:

- GFC (2008)
- COVID-19 (2020)

Rules:

| Rule | Requirement |
|---|---|
| Holdout identification | Crisis holdouts must be explicitly declared, not described vaguely as "stress periods" |
| Assumption/version state | Results must declare the governing regime-definition dependency and version state used to classify those episodes |
| Re-evaluation honesty | Crisis holdouts remain subject to re-evaluation under the current regime-definition dependency; reports must not imply timeless comparability when the definition changed |
| Training/tuning boundary | Holdout evidence must not be recycled as training or threshold-tuning justification |

If a run reports crisis performance without declaring the relevant regime-definition assumption or version state, the evidence is incomplete.

# 10. Promotion Dependency

This contract is gate-critical because later decisions depend on emitted artifacts, not verbal claims.

The dependency chain is:

| Lock | Why this contract matters |
|---|---|
| MLN-06 | This document is the doctrinal artifact contract itself |
| MLN-07 | Threshold validation depends on evidence being present in the governed artifact set |
| GATE-II-01 | Phase II cannot honestly pass without complete, internally consistent evidence surfaces |

**Implementation note (7.0.0):** **MLN-06** is hardened for the **contract and emission** slice: `emit_phase2_artifacts` / `phase2_artifact_contract.py` enforce the governed triple with cross-document validation, required non-recursive content hashes, and canonical triple validation. **MLN-07** threshold references on governed meta evidence now bind ID, state, current expression, usage role, and gate-criticality, and shell validation compares stored state/expression against the canonical register row.

No Phase II promotion narrative is valid if the required artifacts are absent, contradictory, or unverifiable.

# 11. Immutability

Governed artifacts are append-only evidence surfaces after emission.

Immutability expectations:

- emitted artifacts may be superseded only by a new run, not edited in place,
- corrections require a new emitted artifact set with a new run identity,
- downstream summaries may interpret artifacts but may not silently rewrite them,
- artifact references must remain stable enough for audit and replay.

This contract requires immutability as behavior. It does not define how storage systems implement it.

# 12. Failure Modes

The following conditions fail the contract:

| Failure mode | Result |
|---|---|
| Missing `task_manifest.json` | Run is not governed Phase II evidence |
| Missing `meta_validity_report.json` | Run is not governed Phase II evidence |
| Missing `execution_assumptions.json` | Run is not governed Phase II evidence |
| Missing `baseline_comparison` | Fail |
| Missing `pit_compliance_flag` | Fail |
| Missing or malformed `confidence_calibration` | Fail |
| Missing or malformed `content_hash` on any governed artifact | Fail |
| `confidence_calibration.ece.status == PASS` with non-finite, non-numeric, or negative ECE | Fail |
| Inconsistent task or signal identity across artifacts | Fail |
| Crisis evidence reported without declared assumption/version state | Fail |
| Threshold-backed claim without threshold reference where required | Fail or downgrade per Threshold Governance Register rules |
| Threshold reference state or expression differs from canonical register | Fail |

# 13. Scope Boundary

This contract governs:

- required Phase II artifact surfaces,
- minimum evidence expectations,
- baseline anchoring,
- anti-Goodhart output requirements,
- immutability expectations,
- fail conditions for missing or inconsistent artifacts.

This contract does not govern:

- PIT definitions,
- release taxonomy,
- CAS implementation details,
- registry mechanics,
- threshold semantics,
- model architecture doctrine.
