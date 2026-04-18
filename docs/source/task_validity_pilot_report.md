# Task Validity Pilot Report

## Purpose

Record the first governed evidence on whether MarketMind tasks are leakage-safe and non-exchangeable enough to justify trainer commitment. **This document describes pilot design only until Phase II-0A populates results.** No trainer commitment is implied by this design publication.

## Questions This Report Must Answer

The pilot must answer the following at evidence time (design intent below; **no results** in v4.13.0):

1. **Support/query boundaries:** Are support/query boundaries leakage-safe under the planned task geometry?  
   *Design:* Episodes use purge gap equal to label horizon `H` bars, configurable embargo (`⚑ VALIDATE`: RG09-V04, RG09-V05), and admissibility rules in `docs/rg09/rg09_gate_spec.md` §2. Preprocessing fit-on-support-only is enforced in leakage audit, not episode construction.

2. **Non-exchangeability:** Do regime-indexed tasks behave as non-exchangeable learning units?  
   *Design:* Statistical evidence (paired permutation vs. three nulls), structural separability, and functional evidence (ridge / logistic ridge; Workstream 2 alignment) per gate spec §3. Null preservation rules are normative in the gate spec.

3. **Null collapse:** Does the null distribution from shuffled labels, shuffled regime assignments, or exchangeable windows collapse relative to real episodes as expected?  
   *Design:* All three null generators required; seeds via `null_seed_namespace` (`⚑ VALIDATE` linkage: config artifact). Pass/fail vs. `p_value_threshold` (RG09-V01).

4. **Hidden assumptions:** Are any hidden assumptions still preventing honest trainer commitment?  
   *Design:* Open assumptions RG09-V01–RG09-V13 (`RG09-V12`: Level 2 crisis severity percentile per MLN-02-AMD-01; `RG09-V13`: MetaTask `task_id` HMAC key contract, ⚑ VALIDATE); low-confidence boundary episodes are **hard-excluded in v1** (fixed policy, `low_confidence_boundary_policy: exclude_v1` — not a `⚑ VALIDATE` threshold). Kill criteria and fail codes in gate spec §3.

## Minimum Evidence (when the harness runs)

- Leakage-geometry diagnostics and LAK-resolution outcomes  
- Non-exchangeability pilot results (three evidence kinds)  
- Baseline comparison notes relevant to Workstream 2  
- Provisional thresholds remain `⚑ VALIDATE` unless explicitly resolved; each maps to an assumption ID in `docs/rg09/rg09_gate_spec.md` §4  
- Explicit recommendation: proceed, narrow, or stop — **emitted only with Phase II-0A results**

## Cross-reference: `⚑ VALIDATE` thresholds → assumption IDs

| Topic | Assumption IDs |
|-------|----------------|
| Permutation p-value, structural ratio, Harvey t | RG09-V01, RG09-V02, RG09-V03 |
| Embargo (daily / intraday) | RG09-V04, RG09-V05 |
| Support/query row counts | RG09-V06, RG09-V07 |
| Label confidence | RG09-V08 |
| Episode and transition counts | RG09-V09, RG09-V10 |
| Dwell time | RG09-V11 |
| Level 2 crisis severity (`vol_score_raw` percentile) | RG09-V12 |

Numeric defaults for the pilot live in `docs/rg09/rg09_pilot_config_v1.json` (versioned artifact; not frozen architecture constants).

## Low-confidence boundary policy (v1)

**Fixed pilot policy:** Episodes whose boundary confidence does not exceed `label_confidence_threshold` are **hard-excluded** with exclusion code `LOW_CONFIDENCE_BOUNDARY`. This is not a `⚑ VALIDATE` slider for v1; calibration of the threshold itself remains `⚑ VALIDATE` (RG09-V08).

## Phase Relationship

- **Phase I-G** owns the pilot design, gate specification, provisional config artifact, replay fixture spec, and proof burden **documentation** (v4.13.0).  
- **Phase II-0** owns the reproducible harness, gate execution, `rg09_gate_result.json`, and population of this report with actual results.  
- **Phase II** trainer commitment remains gated on clean evidence and `trainer_commitment_unlocked` per gate spec (true **only** when `decision == "PASS"`).

## Governed references

- `docs/rg09/rg09_gate_spec.md` — definitions, admissibility, gate logic, assumptions register  
- `docs/rg09/rg09_pilot_config_v1.json` — provisional pilot parameters  
- `docs/rg09/rg09_replay_fixture_spec.md` — replay fixture admissibility for II-0A  
- `docs/contracts/phase_ii_determinism_boundary.md` — D-tier and reproducibility expectations for artifacts  
