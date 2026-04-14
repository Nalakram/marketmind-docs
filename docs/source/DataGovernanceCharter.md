**MarketMind**

────────────────────────────────

**Data Governance Charter**

<!-- MM:BEGIN:TITLEPAGE -->
Version 1.0.0 · April 2026 · Proprietary

Companion documents: Implementation Plan v6.5.5 · Technical Roadmap v1.4.26 · Meta-Learning Core v1.2.24 · Meta-Learning Architecture Vision v1.3.5 · Resolution Ledger v1.0.51 · README.md 6.2.2 · VERSION.md 6.2.2
<!-- MM:END:TITLEPAGE -->

*Governed doctrine for point-in-time access, dataset visibility, universe membership, vintage handling, and lineage discipline*

*Audience: Internal engineering, technical stakeholders*

<!-- MM:BEGIN:DOCBODY -->

# Data Governance Charter

# 1. Purpose

This charter defines MarketMind's governed data doctrine across all phases. It is the permanent reference for point-in-time correctness, bitemporal semantics, governed universe membership, dataset lineage, and declared approximations.

This charter exists so that later contracts and playbooks can reference one PIT source of truth instead of restating data rules inconsistently.

# 2. Core Principle

MarketMind evaluates only what was knowable at decision time. Any data access path, replay artifact, or research result that cannot be justified under that standard is inadmissible for governed use.

The governing rule is simple:

| Rule | Requirement |
|---|---|
| PIT access | Mutable data must be consumed through `DataView.as_of(T)` or a governed equivalent that preserves the same contract |
| Time model | Both `valid_time` and `knowledge_time` matter; neither may be inferred after the fact |
| Universe selection | Membership is resolved from governed universe records, not from price availability |
| Replay | Replay uses emitted historical availability surfaces, not retrospective reinterpretation |
| Approximation | Any approximation must be named, documented, ledger-tracked, and never silent |

# 3. Point-in-Time Contract

The canonical front door for mutable market data is `DataView.as_of(T)`. Any code path that reads mutable data outside that boundary is a leakage risk and is not governed.

The contract is bitemporal:

- `valid_time` answers when a fact is true in the market domain.
- `knowledge_time` answers when that fact became knowable to the system.
- Visibility at time `T` requires `valid_time <= T` and `knowledge_time <= T`.

Visibility rule:

- No data with `knowledge_time > T` may be accessed under any governed path.

The resolution order for `DataView.as_of(T)` is mandatory and must be applied in this order:

1. visibility filter
2. backward lookup
3. TTL gate
4. row assembly

The ordered meaning is:

| Step | Governing action | Not permitted |
|---|---|---|
| 1. Visibility filter | Exclude rows not visible at `T` under `valid_time` and `knowledge_time` | Looking at later restatements or later-published rows |
| 2. Backward lookup | Resolve the latest admissible prior observation under the field fill policy | Jumping forward to a later observation because it is cleaner or complete |
| 3. TTL gate | Apply per-field freshness rules to the resolved observation | Treating stale data as valid because the row was otherwise visible |
| 4. Row assembly | Assemble the per-symbol snapshot only after field-level admissibility is decided | Building a row first and then retrofitting PIT checks after the fact |

Hard violations:

- reading mutable data without an explicit as-of boundary,
- using later restatements when earlier knowledge-time state should govern,
- inferring availability from storage presence alone,
- bypassing TTL or missing-data policy because a downstream model prefers a filled value.

# 4. BOCPD Governed-Data Semantics

`BOCPDRegimeService` output is governed data, not retrospective annotation. The emitted label surface is admissible only under the following rules:

| Field / concept | Governing interpretation |
|---|---|
| `effective_at` | Availability timestamp. It is knowledge-time-like. It is not the raw change-point timestamp. |
| `decision_ts` | The decision-time or emission-time row anchor for the label event |
| `regime_label` | The emitted label available at that historical point in time |
| `state_snapshot_id` / `input_snapshot_id` / `config_version` | Required lineage identifiers for replay and auditability |

Additional mandatory rules:

- `effective_at` governs when a regime label becomes usable in research or gating.
- Cold-start labels are inadmissible as gate evidence. If the labeling path has not cleared its burn-in or does not have enough prior history for the governed rule, the label may exist operationally but may not support gate passage.
- Replay uses emitted labels, not retrospective relabeling. A later model of the past does not replace what the system actually emitted at the time.
- BOCPD segmentation and Level 2 `regime_class` projection remain separate concerns. A segmentation primitive is not automatically a crisis-label truth surface.

# 5. Vintage and Restatement Policy

Restatements are governed facts, not corrections that erase history.

| Topic | Governing rule |
|---|---|
| Restated values | A later restatement becomes visible only when its `knowledge_time` is reached |
| Historical replay | Re-running a historical decision must preserve the earlier visible value set, not the most recently revised value |
| Vintage-sensitive datasets | Historical vintages must remain queryable or reproducibly reconstructible |
| Silent overwrite | Not permitted for governed data |

If a source publishes revisions, the governed path must preserve the distinction between event-time truth and later publication-time knowledge. A single overwritten series with no vintage path is insufficient for governed use unless the approximation is explicitly declared under Section 9.

# 6. Dataset Lineage Requirements

Every governed dataset or derived feature must carry enough lineage to explain what was used, when it was knowable, and which governed path produced it.

Minimum lineage expectations:

| Surface | Minimum requirement |
|---|---|
| Source identity | Stable source identifier and version or snapshot reference |
| PIT boundary | Declared as-of boundary for the decision or task |
| Input provenance | Traceability to governed inputs, including `DataView.as_of(T)` or an equivalent governed access surface |
| Transformation lineage | Versioned transform or config identity sufficient to reconstruct the derived output |
| Replay evidence | Enough metadata to re-run the same historical decision without consulting later state |

Lineage is incomplete if a result can be reproduced only by consulting current source state and guessing what the past must have been.

# 7. Universe Governance

Universe membership is governed independently of price records.

The rule is explicit:

- universe membership must come from `universe_as_of(T)`,
- the governed source is the `UniverseMembership` table,
- membership must not be inferred from price availability, file presence, or the existence of a row in a feature store.

Operational interpretation:

| Concern | Governing rule |
|---|---|
| Membership query | Resolve members at time `T` through `universe_as_of(T)` |
| Logical source of truth | `UniverseMembership` table or its governed append-only event realization |
| Delist handling | Exclude on and after delist effective date |
| Relist handling | Allowed only through an explicit new membership event |
| Price gaps | Do not remove a symbol from the universe by implication |

This separation is non-negotiable because price availability is an observation surface, not a membership authority.

# 8. Task-Level PIT Boundary

Any task, episode, fold, or evaluation artifact that claims governed status must declare its PIT boundary and respect it end to end.

The governing rules are:

- support and query construction must inherit data only from the governed PIT path,
- `pit_boundary` must correspond to the last admissible support-time boundary for the task,
- labels, regime inputs, and auxiliary features must obey the same boundary as core market features,
- no task artifact may silently mix data resolved under incompatible as-of assumptions.

This charter governs the data side of the boundary only. Task schema, model behavior, and promotion logic are owned elsewhere.

# 9. Acceptable Approximations

Approximations are allowed only when they are explicit, bounded, and auditable.

An acceptable approximation must be:

- named,
- documented,
- ledger-tracked,
- never silent.

Required approximation record:

| Field | Requirement |
|---|---|
| Approximation name | Stable label used in docs and evidence |
| Scope | Exact surface affected |
| Why approximate | Concrete reason the exact governed surface is not yet available |
| Failure risk | What can go wrong if the approximation is wrong |
| Retirement condition | What closes or supersedes the approximation |
| Evidence location | Where the approximation is declared and tracked |

FRED seam pattern:

- The FRED/ALFRED seam is the model for an acceptable PIT approximation when true vintage retrieval is not yet live.
- The seam must state that retrieval-time approximation is in effect.
- It must not pretend that current retrieval reproduces full historical vintage truth.
- The approximation remains governed only while its scope is explicit and its retirement path is tracked in the ledger.

# 10. Enforcement

This charter is enforced through code, artifacts, tests, and governance review.

| Enforcement surface | Expected behavior |
|---|---|
| Data access code | Fails closed on non-bitemporal or non-governed mutable input |
| Replay artifacts | Preserve historical availability surfaces and lineage |
| Test suite | Exercises PIT invariants, restatement behavior, staleness handling, and universe membership rules |
| Doc review | Rejects later contracts that restate PIT semantics inconsistently with this charter |
| Gate review | Rejects evidence built on data that bypassed the governed PIT path |

A result is not "close enough" if its data boundary cannot be defended.

# 11. Scope Boundary

This charter governs:

- PIT correctness,
- `DataView.as_of(T)` discipline,
- bitemporal semantics,
- visibility, backward lookup, TTL, and row assembly order,
- vintage and restatement rules,
- universe membership discipline,
- lineage expectations,
- admissible approximations.

This charter does not govern:

- model behavior,
- promotion logic,
- signal validity,
- artifact taxonomy,
- storage implementation details,
- threshold semantics.

# 12. Amendment Rule

This charter changes only by explicit governed amendment. Any change that weakens PIT semantics, relaxes historical visibility discipline, or redefines governed universe membership requires companion-suite review and Resolution Ledger recording before the new wording is authoritative.
