**MarketMind**

────────────────────────────────

**Phase II Research Execution Playbook**

<!-- MM:BEGIN:TITLEPAGE -->
Version 1.0.0 · April 2026 · Proprietary

Companion documents: Implementation Plan v6.5.5 · Technical Roadmap v1.4.26 · Meta-Learning Core v1.2.24 · Meta-Learning Architecture Vision v1.3.5 · Resolution Ledger v1.0.51 · README.md 6.2.2 · VERSION.md 6.2.2
<!-- MM:END:TITLEPAGE -->

*Operational ordering and failure-handling playbook for Phase II-0 entry and the first governed execution loop*

*Audience: Internal engineering, technical stakeholders*

<!-- MM:BEGIN:DOCBODY -->

# Phase II Research Execution Playbook

# 1. Purpose

This playbook defines the order of work, decision loop, and failure handling for MarketMind at Phase II-0 entry. It is an execution aid for governed research work. It is not doctrinal and does not override the companion contracts or core doctrine.

This document is written specifically for Phase II-0 entry. It is not a Phase III or Phase IV operating manual.

# 2. Guiding Principle

Execute in evidence order. Stop early when the evidence is structurally insufficient. Do not spend Phase II effort pretending unresolved doctrine has already been settled.

The governing reference surfaces are:

| Need | Governing source |
|---|---|
| PIT discipline and universe membership | [`DataGovernanceCharter.md`](DataGovernanceCharter.md) |
| Required evidence artifacts | [`PhaseIIArtifactContract.md`](PhaseIIArtifactContract.md) |
| Threshold identity and validation state | [`ThresholdGovernanceRegister.md`](ThresholdGovernanceRegister.md) |

# 3. Entry Conditions

Before Phase II-0 work begins, confirm all entry conditions below.

| Entry condition | Required state |
|---|---|
| Phase I-F truth boundary | Closed and not reopened by workaround |
| Phase I-G policy / protocol baseline | Available and treated as source of truth |
| Replay / fixture dependency | Satisfied for the lane being executed |
| PIT access path | Governed and auditable under the Data Governance Charter |
| Artifact emission path | Capable of producing the required Phase II artifact set |
| Baseline definition | Frozen incumbent baseline identified before challenger claims |

If any entry condition is not met, the run does not start. The correct response is "not ready," not improvisation.

# 4. Resolution Order / MLN Sequence

Phase II work proceeds in the following order:

1. MLN-01 — Task non-exchangeability
2. MLN-02 — Adaptation usefulness
3. MLN-03 — Encoder coherence
4. MLN-04 — Proxy alignment / routing validity
5. MLN-05 — Continual learning stability
6. MLN-06 — Artifact contract sufficiency
7. MLN-07 — Threshold validation

Operational note:

- MLN-06 and MLN-07 must be established at Phase II-0 entry before executing MLN-01–05
- This does not change conceptual dependency ordering

Operational interpretation:

| Step | Why it is first |
|---|---|
| `MLN-01` | Without a governed task object, later evidence has no stable unit of analysis |
| `MLN-06` | Without governed artifacts, validation claims are not auditable |
| `MLN-07` | Without threshold identity, provisional values drift into silent policy |
| `MLN-02` to `MLN-05` | These refine runtime meaning only after the evidence and threshold surfaces are honest |

# 5. Execution Loop

Each workstream iteration follows the same loop:

1. Declare the governed question.
2. Confirm the data path and task boundary are admissible.
3. Run the baseline and challenger under matched assumptions where comparison is required.
4. Emit the required artifacts.
5. Classify the outcome as `PASS`, `INSUFFICIENT`, `FAIL_SOFT`, or `FAIL_STRUCTURAL`.
6. Either continue, hold, or stop according to Sections 6 and 11.

Outcome meanings:

| Outcome | Meaning | Next action |
|---|---|---|
| `PASS` | Required evidence exists and supports continuation | Continue to the next ordered dependency |
| `INSUFFICIENT` | Evidence does not justify a claim yet, but the surface is still structurally admissible | Hold the claim; gather more evidence without widening scope |
| `FAIL_SOFT` | A fixable implementation or measurement issue blocked the run | Repair the specific issue and rerun without changing doctrine |
| `FAIL_STRUCTURAL` | The program assumption itself is not justified by the evidence | Stop the affected path; do not "tune through" the failure |

# 6. Failure Protocol

Failure handling is ordered. Do not collapse all failures into one bucket.

| Failure class | Examples | Required response |
|---|---|---|
| Hard failure | Missing governed artifact, missing baseline comparison, threshold without ID on gate-critical path | Stop the run; evidence is not admissible |
| Soft failure | Broken fixture path, malformed artifact, non-semantic implementation defect | Repair and rerun without changing doctrine |
| Structural failure | Non-exchangeable tasks not justified, no credible net uplift path, crisis evidence collapses | Stop the affected research path; record the failure honestly |

No failure path authorizes ad hoc relaxation of PIT rules, threshold discipline, or baseline matching.

# 7. Baseline Rule

The incumbent baseline remains the comparison anchor unless formally superseded.

Baseline execution rule:

- use the XGBoost baseline,
- use identical data,
- use identical splits,
- use identical cost assumptions.

If any of those four conditions is not satisfied, the comparison is not valid for continuation or promotion reasoning.

# 8. Anti-Goodhart Enforcement

Holdout discipline is active at Phase II-0 entry even though this playbook is operational rather than doctrinal.

Required handling:

| Concern | Operating rule |
|---|---|
| Crisis holdouts | Treat GFC (2008) and COVID-19 (2020) as named holdout surfaces, not vague stress windows |
| Regime-definition dependency | Declare the governing assumption/version state used to classify crisis episodes |
| Tuning boundary | Do not tune against the holdouts |
| Interpretation | Do not claim cross-version comparability if the regime-definition dependency changed |

This playbook does not define the holdout semantics. It applies the already-governed rule during execution.

# 9. Threshold Handling

Thresholds are consumed operationally under the following rules:

- every governed threshold used by the playbook must be referenced by threshold ID,
- unresolved thresholds remain provisional and must be treated as such,
- threshold-backed evidence must be emitted into the governed artifact surfaces,
- no stop/continue decision may cite a threshold that has no identifiable register entry.

This playbook does not define threshold semantics. [`ThresholdGovernanceRegister.md`](ThresholdGovernanceRegister.md) governs that surface.

# 10. Drift Prevention Rules

Operational drift is controlled by explicit prohibitions.

| Drift pattern | Not permitted |
|---|---|
| Silent doctrine rewrite | Changing PIT, artifact, or threshold meaning inside a run closeout |
| Silent relabeling | Replaying with retrospectively relabeled regime outputs while presenting them as historical truth |
| Baseline drift | Quietly changing the incumbent, data, splits, or cost assumptions mid-program |
| Scope inflation | Treating II-0 scaffolding as if it were promotable Phase II machinery |
| Threshold laundering | Replacing `⚑ VALIDATE` prose with unlabeled numeric constants |

# 11. Promotion Gate

The promotion boundary is later than Phase II-0 and must remain explicit.

Continue beyond II-0 only when all of the following are true:

| Requirement | Why it matters |
|---|---|
| Task contract is stable enough for governed evaluation | Otherwise later learning claims have no trustworthy substrate |
| Required artifacts are complete and consistent | Otherwise evidence is not auditable |
| Threshold references are registered and state-aware | Otherwise provisional values drift into policy |
| Baseline comparison is valid and complete | Otherwise complexity has no honest benchmark |
| Anti-Goodhart evidence remains intact | Otherwise the program is optimizing the wrong thing |

Phase II-0 may build scaffolding, diagnostics, and evidence surfaces. It does not by itself authorize promotion narratives.

# 12. Kill Criteria

The playbook triggers stop decisions when the ordered evidence says the path should stop.

Stop the affected path when:

- the task construction story is structurally invalid,
- the required artifact set cannot be produced honestly,
- the baseline remains stronger with no credible path to reversal,
- crisis holdout behavior fails in a way that contradicts the program's stated burden of proof,
- unresolved threshold use contaminates a gate-critical decision path.

Kill decisions remain owned by higher-tier doctrine. This playbook only defines when operations must escalate to that decision.

# 13. Output Requirements

Every execution cycle should leave behind governed output, not only discussion.

Minimum output expectation:

| Output | Requirement |
|---|---|
| Artifact set | Emit the full governed set required by the Phase II Artifact Contract |
| Decision classification | Record `PASS`, `INSUFFICIENT`, `FAIL_SOFT`, or `FAIL_STRUCTURAL` |
| Assumption/version state | Declare the regime-definition and threshold-governance state used |
| Failure note | If the run stops or holds, say why without rewriting doctrine |

# 14. Scope Boundary

This playbook governs:

- ordering of work,
- MLN execution order,
- pass/fail/insufficient flow,
- failure handling,
- stop/continue logic,
- promotion boundary handling.

This playbook does not govern:

- threshold semantics,
- PIT semantics,
- schema definitions,
- architectural doctrine,
- model validation theory.

# 15. Amendment Rule

Because this is a lower-tier operational playbook, it may be revised when sequencing or failure-handling details improve. It may not be used to override doctrinal surfaces. Any change that would alter PIT semantics, artifact requirements, or threshold governance must be made in the governing companion document first.
