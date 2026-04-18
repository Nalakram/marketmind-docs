# Signal-Universe Expansion Policy

Governed conditions under which the narrow governed signal base may grow. Published with Resolution Ledger OI-37 (v4.16.0).

---

## 1. Relationship to Signal Generation Protocol

This document extends [`signal_generation_protocol.md`](signal_generation_protocol.md). It governs the conditions under which new signals may be added to the current narrow governed base. The admission, promotion, retirement, and identity rules established in that protocol remain authoritative and apply to every signal regardless of when it enters.

The current narrow governed base is defined by the live Signal Generation Protocol and companion docs. Read that document for the canonical enumeration of active signals before treating any list here as authoritative.

This policy governs how that base may grow. It does not expand it.

**Precedence (admissibility boundaries):** If this policy and [`alt_data_admissibility.md`](alt_data_admissibility.md) appear to conflict on admissibility boundaries, alternative-data source admissibility (OI-38) is evaluated first. Only sources that clear the alt-data admissibility contract may enter OI-37 expansion review.

---

## 2. The Case for Narrow Governance

The narrow base is a discipline, not a deficiency. Record these reasons explicitly so they are visible when future expansion proposals arrive:

- **Multiple-testing inflation:** Each additional signal raises the threshold required for significance across the library. An ungoverned expansion lane silently degrades the statistical validity of every existing signal's credentials.
- **Redundancy risk:** Correlated signals consume capacity and diversification budget without adding independent alpha; admitting them without diversity controls defeats the purpose of a signal library.
- **Decay tracking:** A broad library with no retirement discipline accumulates stale signals, creating a false impression of coverage.
- **Admission ≠ value:** The Signal Generation Protocol's admission gate is a structural precondition, not a proof of value. Admission means the signal is structurally governed; it does not earn active curriculum status.

---

## 3. Expansion Gate Conditions

A signal may move from admitted to active curriculum status only after satisfying all of the following, in addition to the Signal Generation Protocol's admission requirements.

**Statistical validity gate:**

Harvey t, DSR (Deflated Sharpe Ratio), and PBO (Probability of Backtest Overfitting) must all be computed from the same governed evaluation bundle, on the same split surface, under the same cost assumptions. All three are required. A signal that passes Harvey t alone, without DSR and PBO from the same bundle, is not admissible for promotion.

- Harvey t > 3.0 on walk-forward out-of-sample IC
- DSR computed to account for testing multiplicity across all signals evaluated in the same expansion batch
- PBO passed under CPCV

**Diversity gate:**

Mean pairwise IC correlation between the candidate and each currently active signal must be below ⚑ VALIDATE threshold. A near-duplicate (high IC correlation with an existing active signal) is rejected as redundant regardless of its standalone statistical validity. This threshold is a ⚑ VALIDATE value set in the governed evaluation config, not a hardcoded constant.

**Decay policy:**

Each promoted signal must have a documented decay-monitoring policy at promotion time: the metric tracked, the window, and the retirement trigger. A signal without a decay policy is not admissible for active status.

**Multiple-testing budget:**

The expansion batch must record the total number of signals tested to produce the promoted candidates. DSR and Harvey t must reference this total count. Gaming the budget by submitting candidates in separate batches is not permitted; the RunRegistry trial counter family governs cumulative testing history across all submissions.

---

## 4. Phase IV as the Serious Expansion Home

Governed at-scale signal-factory expansion is Phase IV work:

- **IV-A:** Operational Signal Generation Protocol, governed signal onboarding workflow, signal-universe expansion from the narrow base under admission/retirement/expansion criteria, alternative-data adapters with PIT discipline
- **IV-B:** `signal_embedding` implementation, novelty/similarity checks, lifecycle controls tied to signal identity and versions
- **IV-D:** Factory automation, governed backtest/promotion loops, retirement/decay handling at signal-factory scale

**What Phase II may do:** admit and promote individual signals through the Section 3 gate conditions, one at a time, with full individual justification documented in the ledger.

**What Phase II may not do:** treat signal-factory breadth as a background expansion program; batch-admit signals without individual statistical evidence; claim the architecture is "broad" before evidence supports that claim.

Phase IV is the first phase allowed to become signal-factory-serious. This is explicit, not implied.

---

## 5. What is Not an Expansion Event

The following changes do not trigger the Section 3 gate conditions:

- Hyperparameter tuning of an existing signal (e.g. lookback window, threshold) without changing `signal_id`
- Changes to feature ops that do not change the signal's `signal_id`
- Alternative-data signals — governed separately by the alt-data admissibility contract; they must clear that contract before entering Section 3 expansion review

Important: These are not expansion events for the purposes of Section 3, but they are still governed changes that may require normal validation and documentation updates under existing contracts.

**Identity loophole:** A change that would alter `signal_id` is not hyperparameter tuning — it is a new signal candidate and re-enters the full admission path from the beginning.

---

## 6. Linkage to Existing Governance Infrastructure

| Concern | Surface |
|--------|---------|
| Signal admission gate | `screening_report.json` |
| Statistical validity gate | `stat_validity_report.json` (canonical v1 contract) |
| Multiple-testing trial counter | RunRegistry trial counter family |
| Signal identity | `signal_id`, `slot_index`, `signal_set_version` per Signal Generation Protocol §4 |
| Retirement procedure | Signal Generation Protocol §5 |
