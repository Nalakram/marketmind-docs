**MarketMind**

────────────────────────────────

**Threshold Governance Register**

<!-- MM:BEGIN:TITLEPAGE -->
Version 1.0.0 · April 2026 · Proprietary

Companion documents: Implementation Plan v6.4.32 · Technical Roadmap v1.4.21 · Meta-Learning Core v1.2.19 · Meta-Learning Architecture Vision v1.2.20 · Resolution Ledger v1.0.40 · README.md 4.18.12 · VERSION.md 4.18.28
<!-- MM:END:TITLEPAGE -->

*Governed register for threshold identity, validation state, and enforcement discipline across the companion suite*

*Audience: Internal engineering, technical stakeholders*

<!-- MM:BEGIN:DOCBODY -->

# Threshold Governance Register

# 1. Purpose

This register governs how thresholds are identified, tracked, validated, rejected, deprecated, and enforced. Its purpose is to prevent unresolved numeric or rule thresholds from drifting into silent policy.

This is a register, not a metric-definition document. Metric semantics remain owned by the source protocol, contract, or doctrinal document that uses the threshold.

# 2. Threshold States

Every governed threshold must have one and only one state.

| State | Meaning | Allowed use |
|---|---|---|
| `PROVISIONAL` | Placeholder exists but evidence is not yet sufficient to freeze it as policy | May appear in docs and non-gate research surfaces with an ID and declared caveat |
| `VALIDATED` | Evidence and authority have approved the threshold for its stated governed use | May drive governed pass/fail decisions within its stated scope |
| `REJECTED` | Proposed threshold was evaluated and not accepted | Must not drive governed decisions |
| `DEPRECATED` | Previously governed threshold is retired or superseded | Must not be used for new decisions; historical references must point to the superseding record |

`⚑ VALIDATE` without register identity is not a valid long-term state. It is only a migration-era notation until Section 4 is complete.

# 3. Required Fields

Each threshold record must include the following fields.

| Field | Requirement |
|---|---|
| `threshold_id` | Stable identifier, unique across the suite |
| `name` | Human-readable threshold name |
| `governing_surface` | Document, contract, or policy section that owns the metric context |
| `consumer_surface` | Gate, report, alert, or workflow that consumes the threshold |
| `state` | One of `PROVISIONAL`, `VALIDATED`, `REJECTED`, `DEPRECATED` |
| `current_expression` | Current numeric band or rule expression |
| `evidence_required` | What evidence is needed to validate or revise it |
| `evidence_location` | Where the evidence lives once emitted |
| `authority` | Who may change the state |
| `gate_critical` | Whether the threshold directly feeds a gate decision |
| `supersedes` / `superseded_by` | Linkage for deprecation history where applicable |
| `last_reviewed` | Most recent governed review date or release |

Where validation evidence is emitted into Phase II artifacts, the evidence location must point to the governed artifact surface defined by [`PhaseIIArtifactContract.md`](PhaseIIArtifactContract.md), not to an informal note or slide deck.

# 4. Migration Rule

One-time migration requirements at register publication:

| Rule | Requirement |
|---|---|
| Existing placeholders | All existing `⚑ VALIDATE` annotations across the governed docs must be assigned threshold IDs at register publication |
| Meaning preservation | Adding threshold ID references alone does not require a semantic version bump when no semantic meaning changes |
| First-class tracking | After migration, threshold review happens against the register row, not only against free-text prose |

This migration rule exists to add identity and auditability, not to smuggle in policy changes under editorial cover.

# 5. Usage Rules

Usage rules are mandatory:

| Rule | Requirement |
|---|---|
| Reference by ID | A governed threshold must be referenced by `threshold_id` wherever it is used in docs, config, artifacts, or gate logic |
| One meaning per ID | A threshold ID must not refer to different meanings in different documents |
| No silent copies | Copying a threshold value into a second location without the ID reference is not allowed |
| State-aware use | `PROVISIONAL` may not be treated as if it were `VALIDATED` |
| Supersession | Replaced thresholds must point to the successor record rather than disappearing |

The register owns identity and state discipline. It does not own the metric formula itself.

# 6. Validation Process

Threshold validation follows this flow:

1. Create the threshold record in `PROVISIONAL` state with an ID.
2. Record the governing surface and intended consumers.
3. Emit evidence through the governed artifact or experiment surface.
4. Review the evidence against the owning protocol or contract.
5. Transition the state to `VALIDATED`, `REJECTED`, or `DEPRECATED`.

State transition rules:

| From | To | Allowed? | Condition |
|---|---|---|---|
| `PROVISIONAL` | `VALIDATED` | Yes | Required evidence exists and authority approves |
| `PROVISIONAL` | `REJECTED` | Yes | Evidence or review rejects the proposed value or rule |
| `VALIDATED` | `DEPRECATED` | Yes | A replacement or retirement decision is recorded |
| `REJECTED` | `PROVISIONAL` | Yes | Only as a new proposal with new review context |

# 7. Enforcement

Enforcement must be honest about current capability and consequence.

| Condition | Enforcement outcome |
|---|---|
| Hardcoded threshold without ID | `WARN` in pre-release audit |
| Threshold without ID that directly feeds a gate decision | `FAIL` |
| Threshold ID referenced but missing from the register | `FAIL` |
| `PROVISIONAL` threshold used as if it were validated in a gate-critical path | `FAIL` |
| Deprecated threshold used in new governed logic | `FAIL` |

This is intentionally narrower than "everything fails immediately." Gate-critical omissions fail. Non-gate hardcoded values without identity are still unacceptable, but they enter first as audit warnings unless they directly affect a governed pass/fail surface.

# 8. Relationships

This register relates to the rest of the suite as follows:

| Surface | Relationship |
|---|---|
| [`PhaseIIArtifactContract.md`](PhaseIIArtifactContract.md) | Governs where validation evidence lives when thresholds are tested or consumed through Phase II artifacts |
| `MetaLearningCore.md` | Owns many threshold-bearing research and promotion surfaces |
| `MetaLearningArchitectureVision.md` | Owns threshold-bearing runtime and operational framing |
| `ResolutionLedger.md` | Records the normative lock (`MLN-07`) that requires threshold-governance discipline |

# 9. Scope Boundary

This register governs:

- threshold IDs,
- threshold state machine,
- migration of existing `⚑ VALIDATE` references,
- usage rules,
- validation/update flow,
- enforcement expectations.

This register does not govern:

- metric definitions,
- evaluation design,
- artifact schema design,
- model architecture,
- PIT semantics.

# 10. Current Threshold Records

| threshold_id | name | governing_surface | consumer_surface | state | current_expression | evidence_required | evidence_location | authority | gate_critical | supersedes | superseded_by | last_reviewed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| THR-RG09-V15 | RG-09 statistical-lane within-variance denominator floor | `docs/rg09/rg09_gate_spec.md` §3–§4 and `srcPy/meta/rg09_harness.py` `_regime_separability_statistic` | RG-09 H1 statistical lane, all three authorized null families | `PROVISIONAL` | `between / (within + 1e-9)` with denominator floor `1e-9` | Governed H1 rerun evidence showing the floor does not dominate legitimate near-zero within-regime variance under uniform statistic dispatch | `runs/rg09_v2/h1_v2bocpd_uniform_stat/rg09_gate_result.json`, `runs/rg09_v2/h1_v2bocpd_uniform_stat/rg09_diagnostics.json`, and `docs/src/ResolutionLedger.md` `OI-52` | RG-09 / MLN-07 governance | `true` | — | — | `2026-04-02 / v4.18.13` |
| THR-RG09-V16 | RG-09 null draw-count rule | `docs/rg09/rg09_gate_spec.md` §3–§4, `docs/rg09/rg09_pilot_config_v1.json`, and `srcPy/meta/rg09_harness.py` `_evaluate_fold` | RG-09 H1 statistical lane, all three authorized null families | `VALIDATED` | `null_draw_count = 64` configured draws per family/fold | Governed closure evidence that draw count is explicitly config-owned and no longer inherited from runtime episode count | `docs/rg09/rg09_pilot_config_v1.json`, `docs/rg09/rg09_pilot_config_v1_power_a.json`, `tests/python/unit/meta/test_rg09_harness.py`, and `docs/src/ResolutionLedger.md` `OI-58` | RG-09 / MLN-07 governance | `true` | — | — | `2026-04-04 / v4.18.23` |
| THR-RG09-V17 | RG-09 episode regime-class purity floor (boundary recovery) | `docs/rg09/rg09_gate_spec.md` §1, `docs/rg09/rg09_pilot_config_v1_purity.json`, and `srcPy/meta/rg09_harness.py` `_derive_episodes` | RG-09 boundary-recovery episode admission; H2 attribution pre-flight | `PROVISIONAL` | `min_episode_regime_class_purity = 0.70` in provisional pilot config; active only when `boundary_recovery.mode != baseline` | Pre-flight diagnostic showing mean `fraction_mismatch` vs harness-assigned label below operational ceiling on admitted surface; tighten threshold empirically on H2 fixture before gate | `docs/rg09/rg09_episode_purity_preflight.md`, `rg09_shuffled_label_separability_diagnostic.json` outputs, and governed run manifests | RG-09 / MLN-07 governance | `false` | — | — | `2026-04-04` |
| THR-RG09-V19 | RG-09 transition-anchored structural direction threshold | `docs/rg09/rg09_gate_spec.md` §3, `docs/rg09/rg09_pilot_config_v1_transition.json`, and `srcPy/meta/rg09_harness.py` `_evaluate_fold` | RG-09 transition-anchored structural pass when `episode_construction == "transition_anchored"` | `PROVISIONAL` | `structural_direction_score_threshold = 0.0` (positive direction threshold) | Direction score null distribution on transition-anchored episodes via governed calibration artifact before any threshold revision | `rg09_structural_threshold_calibration.json` transition-anchored outputs and governed RG-09 H2 calibration manifests | RG-09 / MLN-07 governance | `true` | — | — | `2026-04-04` |
