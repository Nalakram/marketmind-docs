**MarketMind**

────────────────────────────────

**Implementation Plan & Execution Roadmap**

<!-- MM:BEGIN:TITLEPAGE -->
Version 6.5.10 · April 2026 · Proprietary

Companion documents: Technical Roadmap v1.4.31 · Meta-Learning Core v1.2.25 · Meta-Learning Architecture Vision v1.3.6 · Resolution Ledger v1.0.52 · README.md 7.2.3 · VERSION.md 7.2.3
<!-- MM:END:TITLEPAGE -->

*Execution plan for the governed research substrate and the validation-gated meta-learning program*

*Audience: Internal engineering, technical stakeholders*

<!-- MM:BEGIN:DOCBODY -->

# Purpose

This document translates MarketMind’s strategy into executable work. It maps the governed substrate that already exists to the closure work, protocol work, scaffolding work, and validation-gated build work still required before a promotable adaptive allocator can honestly exist.

# 1. Executive Summary

The center of gravity of the implemented platform remains the governed research substrate delivered across Phase 0 and most of Phase I. MarketMind already has the canonical PIT-safe path, bundle lineage, statistical-validity enforcement, execution-assumption gating, and the first governed strategy slices. The remaining roadmap is therefore not “just start Phase II.” It is a phased proof-and-build sequence:

- Phase I-F closes truthfulness, interface, determinism, and seam-closure blockers.
- Phase I-G freezes research policy, protocols, and proof burden.
- Phase II-0 builds only the minimum non-promotable scaffolding needed to test those decisions honestly.
- Phase II is the first phase allowed to build promotable adaptive-learning machinery.
- Phase III and Phase IV remain conditional on allocator validation and product need.

## 1.1 Guardrail

> **Guardrail.**  
> Phase I-F freezes system truth.  
> Phase I-G freezes research policy, protocols, and proof burden.  
> Phase II-0 implements only the minimum scaffolding needed to test those decisions honestly.  
> Phase II is the first phase allowed to build promotable adaptive-learning machinery.  
> Phase III is the first phase allowed to become execution-serious.  
> Phase IV is the first phase allowed to become signal-factory-serious.  
> Neither I-G nor II-0 may quietly become full Phase II.

## 1.2 Current Reality Through 6.2.2

**Audit baseline:** `VERSION.md` **4.19.2** / Resolution Ledger **1.0.46** now record the executed **H3** successor posture alongside the earlier unsuccessful H1, H4, and proper H2 surfaces. The historical H1 transition base at `runs/rg09_h2_transition_dir/` remains valid governed evidence with **104 admissible episodes**, `NEEDS_MORE_EVIDENCE`, and `FAIL_NONREPRODUCIBLE`; H4 at `runs/rg09_h4_market_class_risk/` remained another non-reproducible failed rescue on the narrowed `ES,NQ,RTY,YM,SPY,HYG,VIX` basket; and proper H2 at `runs/rg09_h2_cross_sectional/` removed the non-reproducibility failure mode but still stayed below threshold statistically on a reproducible surface. The live promoted posture now comes from the strict H3 successor surface at `runs/rg09_h3_granularity`: `vol_window = 120`, `trend_flat_epsilon = 0.01`, `vol_bucket_method = quintile`, `crisis_vol_score_percentile = 95.0`, fixture `sha256:d38639a4f2cb8be5e0c57cd1fdaa3750b8a26336b93dd907a6b0f2b9d289e11c`, `decision = PASS`, `decision_reason = "All required RG-09 evidence families passed."`, `reproducibility_consistent = true`, `fail_codes = []`, `trainer_commitment_unlocked = true`, and **86 admissible episodes** with both folds passing overall/statistical/structural/functional lanes. The nearby p85 H3 sensitivity control remained reproducible but failed kill with `FAIL_EXCHANGEABLE_TASKS`, and both p95 and p85 surfaces shared the same admissible-episode count (**86**), so the pass/fail flip is not explained by more episodes or cleaner geometry. The strongest supported lesson is narrow: within the tested H3 neighborhood, crisis-label strictness appears to be the decisive lever; the passing p95 surface preserves crisis/high_vol separation, while the looser p85 surface collapses high_vol into crisis and fails kill. The planning limitation also stays explicit: the attached evidence does not fully isolate whether `vol_window = 120` and `trend_flat_epsilon = 0.01` are individually necessary. The harness still emits the base-field hypothesis identity `RG09-H1`, so the docs treat this as an H3 successor surface evaluated through the base harness rather than as proof that H1 passed. Bounded execution should now track RG-09 against the strict H3 successor surface, not the earlier failed rescue attempts.

**II-0A completion (companion truth, `VERSION.md` 7.0.0 / Ledger v1.0.52):** **WS-1 COMPLETE**, **WS-2 COMPLETE**, **WS-3 COMPLETE**, and **II-0A COMPLETE** remain supportable. The strict-H3 RG-09 task-validity anchor is frozen at `run_bundles/rg09_reference_v1/` with artifact hash `sha256:caac0778c33c580e90e992bc612c9a1447241f5009fb0603f7ced79bd7618f5d`; `scripts/reproduce_rg09_reference.py` and `.github/workflows/rg09_reference_drift.yml` provide drift verification; `run_bundles/rg09_reference_v1/task_validity_report.json` records diagnostic version `1.0.0` with `all_pass=true`; and CI has been externally confirmed green. This completes the II-0A join point for task-validity and harness reproducibility only. It does **not** make the RG-09 anchor the Phase II allocator incumbent comparison baseline; II-0B challenger predicates must still reference the XGBoost incumbent.

**II-0B hardening status (`VERSION.md` 7.2.1):** The non-promotable artifact-and-contract lane is now complete. Governed triples emitted through `emit_phase2_artifacts()` require non-recursive `content_hash` blocks on `task_manifest.json`, `meta_validity_report.json`, and `execution_assumptions.json`; `phase2_ml_evidence_shell` re-checks artifact-level semantics; threshold references on meta evidence are reconciled against canonical register state and expression; and the lane remains explicitly non-promotable. Canonical `pysrc/pipeline` orchestration now emits governed II-0B evidence under `phase2_ii0b_governed_non_promotable/`, fails closed unless that evidence is structurally usable, frames borrowed `THR-RG09-V03` / `THR-RG09-V17` references as reviewer-visible lineage rather than native orchestration policy, and writes a root summary guardrail that keeps the governed lane distinct from unrelated root bundle artifacts. Governed consumers surface threshold-governance summary details uniformly, and stale pre-hash root triples are explicitly excluded from current governed evidence rather than silently continuing to count.

**II-0C pilot harness status (`VERSION.md` 7.2.3):** II-0C is complete as a **non-promotable** pilot harness: canonical MetaTask scaffolding, deterministic reference-only encoder stub, XGBoost incumbent comparison plumbing, II-0B-governed artifact emission via the II-0C wrapper, research-only report shells (`ii0c_pilot_report.json`, `ii0c_dry_run_summary.json`, plus dual-written `phase2_ii0c_scaffold_non_promotable.json` for path-based collectors), frozen reference inputs for drift replay, and pre-emission checks for task identity drift, governed `baseline_comparison` key discipline, and baseline/shared parity. This does **not** move **GATE-II**, does **not** make RG-09 / strict-H3 the incumbent comparison baseline, and does **not** authorize trainer, allocator, rollout, broker, or execution-serious behavior.

**Phase I-G closure (companion truth, Ledger v1.0.46):** Phase **I-G** is **closed** for protocol-and-empirical-foundation purposes: governed protocols and the II-0A harness are published, and the **strict H3** surface above is the documented **live promotable** empirical anchor. **RG-09** remains **PARTIAL** and **OI-59** remains **OPEN** for **II-0** follow-on only—both are **`blocking: NO`** in the Resolution Ledger and **do not** keep I-G open. Historical and widened **H1** surfaces remain **predecessor evidence**; the bounded widened-H1 recovery rerun at `runs/rg09_h1_recovery_one_axis_boundary_v2/` restored `gate_executed=true` but ended `NEEDS_MORE_EVIDENCE` with `FAIL_NONREPRODUCIBLE`; **no further H1-family rescue iteration** is authorized for program closure. Empirical closure emits **`segmentation_provenance`** in `run_config_resolved.json` (`py/meta/rg09_empirical_closure.py`) so pilot `episode_construction` (THR-RG09-V18) stays distinct from **boundary_recovery** overlays.

**OI-59 corrected-branch (separate lane):** **OI-59 remains OPEN but narrowed**, ledger-**Phase II-0** and **non-blocking** for I-G closure. MLN-07 threshold scope is resolved (`THR-RG09-V20` superseded; `THR-RG09-V21` active at `feasible_segment_ratio >= 0.025`), while the corrected-surface lane remains **constructibility-only** and **non-promotable**. This threshold decision does not authorize RG-09 statistical re-entry, gate/trainer unlock, or OI-59 closure by threshold change alone. **`docs/rg09/oi59_mln07_threshold_decision_memo.md`** and `docs/rg09/oi59_mln07_threshold_review_packet.md` are the disposition artifacts; register surfaces are `docs/src/ThresholdGovernanceRegister.md` §10 and `py/meta/threshold_register.mln07.v1.json`. Experiment 5 Branch B remains closed as a rescue family under the current recipe, and **no new corrected-branch experiment is authorized by this decision package**. This lane must not be conflated with the strict-H3 promotable RG-09 posture above.

**Governed substrate hardening (4.18.35):** The cleaning layer now has one canonical public root at `py.pipeline.stages.cleaning`; governed config must flow through `pipeline.cleaning`; external cleaning config is validated before normalization into frozen runtime specs; registry state is part of executable plan identity; and governed cleaning emits `cleaning_plan.json` plus `cleaning_report.json`. Top-level run composition now belongs to `py.pipeline.orchestrator`; `py.bridge.dataprep_orchestrator` is a deprecating forward-only bridge with a stated `5.0.0` removal target rather than a second orchestration owner.

**`VERSION.md` `4.18.20`** corrected the RG-09 real-calendar fixture fold layer for `independent_instruments` manifests. The **live promotable** RG-09 line in companion docs is the **strict H3** successor surface (§1.2 above); historical **H1** replay lines and the widened-H1 recovery probe remain **predecessor evidence**, not the live anchor. Earlier evidence items **OI-46**, **OI-47**, and **OI-50** still matter as historical fixture-scope diagnostics. **4.18.8** closed **OI-47** multi-ticker replay v2 generator path. Prior baseline **4.18.7** registers governed assumption **RG09-V13** (MetaTask `task_id` HMAC key contract: empty-key HMAC in scaffold `compute_task_id`; ⚑ VALIDATE — changing key material invalidates all historical `task_id` values) and extends **MLN-01** acceptance criteria; `docs/rg09/rg09_gate_spec.md` Section 4 open-assumptions register spans **RG09-V01** through **RG09-V13**. **4.18.6** ships Phase II-0B non-promotable artifact scaffolding (task_manifest / meta_validity_report / execution_assumptions emitters, seed policy, `meta_learner_scaffold` gate shell, pilot threshold IDs; Resolution Ledger **OI-48** / **OI-49**). **4.18.5** patches the RG-09 II-0 empirical lane `meta_validity_report_research.json` scaffold (Appendix B.1 field completeness, `ic_harvey_t` vs inner-loop Harvey separation, fixed research `overall_result` sentinel) and closes **OI-39** in the Resolution Ledger (`paper_trade_sim_spec.md`). **4.18.2** delivers the RG-09 II-0A bounded falsification harness against the governed replay-fixture baseline, including deterministic gate artifacts, fold-aware evidence aggregation, authorized null families, and a run-derived machine-manifest emission path. **4.18.1** closes **OI-43** by emitting the governed RG-09 replay fixture artifact and recording its path/SHA in the Resolution Ledger, which satisfies the II-0A replay-fixture entry dependency. **4.18.0** incorporated **MLN-02-AMD-01** (Level 2 `crisis` = `vol_hi AND severity_flag` per Architecture Vision §4.2 and **RG09-V12**; `RegimeLabeler` / `BOCPDRegimeService` + ledger **OI-44** / **OI-45**). Earlier milestones remain: **4.17.0** MOM-020 closure on the governed comparison lane; **4.16.0** (**OI-37** and **OI-38** closed); **4.15.0** **RG-10** closed; **4.14.0** RiskFn Protocol and Signal Generation Protocol; **4.13.0** RG-09 protocol closure; **4.12.3** companion sync after Phase I-F closed at **4.12.2**. Phase I-E engineering delivery through **4.5.4** remains the last major substrate closure before ML implementation.

Delivered or materially advanced:

- **OI-37** / **OI-38** closed (**4.16.0**): signal-universe expansion policy and alt-data admissibility contract published; core I-G protocol document set for breadth/admissibility is **complete for I-G phase closure** (companion README + this plan); **OI-39** (paper-trading simulation requirements) closed at **4.18.5**,
- **RG-10** closed (**4.15.0**): context encoder upgrade criteria and D=64 baseline position frozen in policy; **AQ-01** / **AQ-02** graduated,
- **OI-35** / **OI-36** closed: governed `risk_protocol.md` and `signal_generation_protocol.md` at **4.14.0**,
- **Phase I-G closed; RG-09 / OI-59 are II-0 follow-on:** **RG-09** stays **PARTIAL** on the books (**`blocking: NO`**, **phase II-0**) with pilot schema frozen, replay fixture satisfied at **4.18.1**, II-0A harness at **4.18.2**, empirical `meta_validity_report_research.json` scaffold at **4.18.5**, and **strict H3** as the live promotable anchor (Resolution Ledger §1.5). **OI-59** stays **OPEN** on the corrected-surface lane under the same **II-0 / non-blocking** posture. **OI-46**, **OI-47**, and **OI-50** remain historical fixture-scope evidence,
- canonical PIT-safe orchestration and governed bundle emission (4.19.0),
- canonical governed cleaning execution under `py.pipeline.stages.cleaning`, with declarative `pipeline.cleaning` specs, fail-closed provider seams, structured mutation summaries, and emitted `cleaning_plan.json` / `cleaning_report.json` artifacts,
- governed daily source adaptation and single-path feature execution,
- governed `stat_arb_pairs` and materially advanced governed momentum,
- MOM-020 closed on the governed comparison lane: child-owned `cpcv_path_scores.json` is authoritative, parent comparison is non-generative, and shared PBO is emitted through `comparison_stat_validity.json`,
- **MLN-02-AMD-01** incorporated at **4.18.0**: severity-gated Level 2 `crisis` (PIT-safe expanding `vol_score_raw` percentile; default p90); `diag_regime_class_bocpd_gated` retains the BOCPD-only crisis rule for Phase II-0A baseline comparison,
- MLN-01/02/03 in-repo contract slices are now implemented: canonical MetaTask builder + append-only task registry semantics, fixed 5-class regime vocabulary/projection hooks, and confidence attenuation default with governed calibration block emission,
- SignalCatalog with stable `slot_index`,
- `screening_report.json`, `execution_assumptions.json`, and governed `stat_validity_report.json`,
- DataLineageGate plus artifact-registry-owned hashing/canonicalization,
- and a mature test/CI baseline for leakage, determinism, and typing on the trusted path.

Still open before promotable adaptive-learning buildout:

- Phase **II-0** scaffolding and bounded empirical lanes (including ledger-tracked **RG-09** / **OI-59** follow-on) that must not be smuggled back into closed Phase **I-F** or misread as reopening **I-G**,
- non-promotable harness completeness needed to test frozen protocol decisions reproducibly,
- and the validation-gated Phase II build itself.

# 2. Current Reality Map

This plan stays anchored to repo truth rather than inherited roadmap inertia.

## 2.1 Trusted Build Surface

| Area | Current Reality | Why It Matters Next |
|---|---|---|
| Canonical orchestration path | Trusted PIT-safe bundle-producing path exists | All later ML work must build on this path, not a shadow path |
| Governed feature execution | `_OP_REGISTRY` and the canonical planner/executor route are the governed feature path | Task generation must inherit the same PIT and operator guarantees |
| Artifact lineage | `py.artifact_registry` and RunRegistry own canonical artifact identity | Later task/checkpoint/report artifacts must extend this scheme rather than fork it |
| Statistical and cost gating | `stat_validity_report.json` and `execution_assumptions.json` are real governed surfaces | Phase II adds new evidence surfaces; it does not bypass existing gates |
| Cross-variant comparison discipline | governed momentum comparison uses child-owned `cpcv_path_scores.json` as the authoritative CPCV surface and parent-owned `comparison_stat_validity.json` only for shared-PBO aggregation | Prevents the comparison layer from self-certifying CPCV scores |
| Signal identity substrate | SignalCatalog and stable `slot_index` exist | Dynamic-K and later signal-factory growth must build from that governed substrate |

## 2.2 Anti-Blur Rules

- I-F is narrow. It closes truthfulness, interface, determinism, and seam blockers only.
- I-G owns baseline policy, task-validity protocol, RiskFn / signal-generation protocol work, and the **foundation** empirical anchor for the pilot (**closed** per Ledger v1.0.46 with **strict H3**); further RG-09/OI-59 lanes are **II-0** scoped.
- II-0 owns harnesses, pilot artifacts, report scaffolding, and reference runs only.
- II owns promotable adaptive-learning machinery in evidence order.
- III and IV remain conditional even if Phase II succeeds technically.
- Governed momentum comparison uses child `cpcv_path_scores.json` as the authoritative CPCV evaluation surface.
- Parent comparison owns split/cost hash validation, path-score aggregation, and shared-PBO construction only.
- Parent comparison must not recompute CPCV scores from child `trade_intent` or any preview path.

# 3. Phase I-F — Architecture Closure

Phase I-F is the final narrow closure phase before pre-build ML foundation work can proceed honestly.

## 3.1 Objective

Close the blocking truthfulness, interface, determinism, and seam-closure items before honest ML entry.

## 3.2 Owns

- companion-doc truthfulness review,
- canonical-path verification,
- ADR / seam closure for Phase II blockers,
- Phase II interface contract stubs,
- determinism boundary for ML entry,
- and coverage / CI truthfulness audit.

## 3.3 Does Not Own

- broad signal-universe expansion,
- alternative-data architecture in detail,
- paper-trading implementation,
- broker wiring,
- or the full empirical de-risking program.

## 3.4 Exit Condition

Phase I-F exits only when:

- GATE-I-F closes,
- the canonical governed path is verified,
- remaining later-phase blockers are visible in Resolution Ledger,
- and interface stubs plus determinism expectations are explicit.

For typing, I-F remains intentionally narrower than a repo-wide `mypy py/strategies/ --strict` sweep. The acceptance surface is still the canonical path the later phases will actually inherit:

```bash
mypy py/strategies/momentum/ \
     py/strategies/pipeline_strategy.py \
     py/artifact_registry/ \
     py/cli/gate.py \
     --strict
```

# 3.x Phase I-G — Empirical & Protocol Foundation

Phase I-G is the substantial pre-build foundation phase that the current suite and gap analysis justify.

**Companion status (Ledger v1.0.46):** Phase **I-G** is **closed** in repo truth (README phase table, this plan §1.2 / §9, Resolution Ledger §1.5). **RG-09** / **OI-59** continue as **II-0** follow-on items, not open I-G debt.

## 3.x.1 Objective

Define the research world and the proof burden before promotable ML buildout.

## 3.x.2 Owns

- baseline freeze policy,
- **governance-as-survivability protocol**: rollback, kill-switch semantics, shadow/staged promotion, drift triggers, and failure containment framed as **insurance**, not alpha optimization,
- **`tasks not timestamps` policy freeze**: the learning object is a market task (episode), not an IID row; task distribution quality is existential,
- **benchmark philosophy freeze**: **decision quality after frictions** (utility net of costs, drawdown, turnover efficiency) beats stylized forecast metrics; rolling-window refits are not “meta-learning” by narrativization,
- **hierarchical allocator target as vision-only**: future layers A–D (representation, world/regime model, expert family, post-allocator conditioning) are **architecture vision**, not implementation claims,
- **robustness / domain-shift review domains** that matter for falsification (volatility, cost regime, macro, geography, rebalance cadence, crisis vs normal) as **planned test obligation**, not “solved robustness,”
- **complexity bar**: complexity is not progress unless it survives realistic evaluation,
- task non-exchangeability pilot,
- task-validity / leakage-geometry protocol (**structural gate**; failure is an early program stop),
- RiskFn Protocol definition,
- Signal Generation Protocol,
- context-encoder upgrade criteria,
- threshold registry for `⚑ VALIDATE` items,
- signal-universe expansion policy (**narrow governed base today**; breadth policy before Phase IV scale),
- alternative-data admissibility / PIT contract at the architectural level,
- report and manifest requirements for early ML evidence,
- and paper-trading simulation requirements without building the full execution stack.

## 3.x.3 Does Not Own

- committed trainer policy,
- promotable allocator code,
- broker integration,
- shadow/blend/live control flow,
- or a silent rollout of Phase II machinery.

## 3.x.4 Exit Condition

Phase I-G exits only when:

- at least one empirical workstream is closed enough to justify moving forward,
- the baseline is frozen,
- task-validity and non-exchangeability evidence exist,
- the protocol documents are written and governed,
- context-encoder upgrade criteria are explicit,
- evidence/report requirements are explicit,
- and any provisional thresholds remain visibly provisional rather than silently fixed.
- **Companion closure rule (v1.0.46):** I-G is also considered **exited** when the pilot has a **documented live empirical anchor** on the governed RG-09 surface (**strict H3** `PASS` in Resolution Ledger §1.5), with predecessor H1/H2/H4/H-widened surfaces treated as **non-blocking** historical evidence; remaining **RG-09** / **OI-59** items are **II-0** follow-on, not I-G debt.

# 4. Phase II-0 — ML Scaffolding & Research Harness

Phase II-0 is the explicit bridge between protocol decisions and promotable adaptive-learning implementation.

## 4.1 Objective

Turn I-G decisions into minimal, reproducible, non-promotable machinery.

**II-0 is the cheap falsification lane.** It hosts the **honest benchmark**, task-based meta-learning harnesses, uncertainty studies, the **uncertainty-aware routing pilot** (conditional on `confidence_scalar`), domain-shift falsification tests, early expert/modularity pilots, early retrieval/analog-memory pilots, and narrow-adaptation experiments—without implying promotable allocator code.

## 4.2 Subphases

### II-0A — Baseline & Validity Harness

**Purpose:** freeze the null hypothesis and build the measurement skeleton.

**Deliverables:**

- frozen baseline harness,
- task-validity diagnostics,
- non-exchangeability pilot harness,
- holdout / crisis manifest scaffolding,
- Anti-Goodhart scaffolding.

**Gate to next subphase:**

- baseline is frozen,
- first task-diagnostics pass exists,
- and no silent leakage assumptions remain.

**Completion status:** **COMPLETE as of `VERSION.md` 6.2.2; current companion baseline `VERSION.md` 7.0.0 / Resolution Ledger v1.0.52.** WS-1 froze the strict-H3 RG-09 reference anchor, WS-2 delivered the task-validity diagnostic harness and controls, and WS-3 ran the diagnostic against the frozen reference bundle and registered the result. The RG-09 reference hash is available for downstream II-0B / II-0C sequencing; II-0C-01 full dry-run work still waits on II-0B schemas and predicates.

**Entry gate dependency:** Satisfied at **4.18.1** via the governed replay fixture artifact recorded in the Resolution Ledger. The initial bounded II-0A harness is implemented at **4.18.2**. The RG-09 empirical closure lane (non-promotable) emits additive research artifacts including `meta_validity_report_research.json` (`rg09.meta_validity_report.research.v1`), with Phase II trainer-only fields held explicitly unavailable through **4.18.5**. **OI-46** records the original bounded ES-only precondition failure; **strict H3** is the live promotable anchor (§1.2). **No further H1-family widening/rerun** is a program priority; optional **II-0** work is **II-0B** scaffolding and **OI-59** corrected-surface lanes under governance, not H1 rescue churn. Live BOCPD service output may still substitute in future runs if it carries the provenance fields specified in `rg09_replay_fixture_spec.md`.

### II-0B — Artifact & Contract Scaffolding

**Purpose:** make later Phase II evidence mechanically emit-able.

**Deliverables:**

- `task_manifest.json` scaffolding,
- `meta_validity_report.json` scaffolding (promotable path); research lane uses `meta_validity_report_research.json` with non-promotable semantics,
- threshold registry / provenance hooks,
- deterministic checkpoint / seed policy hooks,
- early gate shells for ML evidence.

**Current gate posture:**

- pilot artifacts emit reproducibly,
- provisional thresholds remain visibly provisional on governed consumers,
- canonical `pysrc/pipeline` orchestration now emits governed II-0B evidence under `phase2_ii0b_governed_non_promotable/`, fails closed unless that governed evidence is structurally usable, and writes a root summary guardrail that keeps the governed lane distinct from unrelated root bundle artifacts,
- governed consumers surface threshold-governance summary details uniformly,
- borrowed `THR-RG09-V03` / `THR-RG09-V17` references on the orchestration lane are framed as reviewer-visible lineage rather than native orchestration threshold policy,
- and stale pre-hash root triples are explicitly excluded from current governed evidence rather than silently continuing to count.

`VERSION.md` 7.2.1 now supports **II-0B COMPLETE** for the **non-promotable artifact-and-contract lane only**. This closure now includes an explicit orchestration-layer hard contract for governed II-0B evidence usability, alongside canonical orchestration rollout truth, uniform governed-consumer threshold semantics, reviewer-facing guardrails, honest borrowed-threshold lineage framing, and explicit retirement of older pre-hash root triples from current governed evidence. It does **not** authorize trainer, allocator, broker, rollout, or execution-serious claims.

**Independence note:** The RG-09 H1 precondition failure recorded in **OI-46** does not block II-0B. Artifact-and-contract scaffolding and the MLN-01 through MLN-07 normative lock sequence proceed independently of any optional II-0A empirical lane activity.

#### II-0B closure posture (Wave 3 seam review resolved) · April 2026

**Companion baseline:** `VERSION.md` **4.19.2** / Resolution Ledger **v1.0.46** (`docs/src/ResolutionLedger.md`).

**Doctrinal posture (closed vs deferred):** **MLN-01** through **MLN-07** are **closed in-repo**. **GATE-II** remains **DEFERRED**. The former obstacle to honest II-0B closure language was **threshold/orchestration rollout** relative to governed evidence surfaces; that seam is now closed for the **non-promotable artifact-and-contract lane** without changing the broader **GATE-II** deferral.

**Three layers — do not conflate them:**

| Layer | What it proves | Typical pitfall |
|-------|----------------|-----------------|
| Companion / doctrinal truth | Program sequencing, evidence order, what “closed” means in docs | Treating doc closure as runtime proof |
| Module / library truth | `emit_phase2_artifacts` in `py/meta/phase2_artifact_contract.py`: cross-artifact identity, PIT-derived compliance, signal-surface consistency, atomic triple write | Treating library strength as full-product rollout |
| Orchestration rollout truth | Which entrypoints invoke governed logic end-to-end | Assuming `py/pipeline/orchestrator.py` uses the same spine as RG-09/OI-59 without checking |

**Reviewer failure mode (now mitigated structurally):** A governed `meta_validity_report.json` can show a numeric `harvey_t_statistic` and stable `run_id` while the **threshold register** still forbids inferring **fully lineage-bound** threshold policy on every consumer path. Closure therefore requires the governed consumer shell and the canonical orchestration pointer surface to expose the same threshold-governance summary rather than leaving reviewers to infer policy from raw JSON alone.

**Outcome C — II-0B COMPLETE for the non-promotable artifact-and-contract lane.**

The governed MLN-06 triple and RG-09 governed harness spine remain the underlying module proof, but closure is no longer limited to governed side entrypoints. Canonical `pysrc/pipeline` orchestration now emits governed II-0B evidence under a dedicated non-promotable subdirectory, fails closed unless that evidence is structurally usable, and writes a root summary guardrail; the governed shell surfaces threshold-governance lineage details uniformly; borrowed `THR-RG09-V03` / `THR-RG09-V17` references are surfaced honestly as reviewer-visible lineage rather than native orchestration policy; and checked-in root-level pre-hash triples at `fixtures/rg09/v2`, `runs/oi59_experiment5_branch_b`, `runs/oi59_experiment5_branch_b_v2_corrected`, `runs/rg09_h1_cross_sectional_expansion`, and `runs/rg09_h1_recovery_one_axis_boundary_v2` are explicitly retired from **current governed evidence**. The lane remains non-promotable and does not implement trainer, allocator, broker, rollout, or execution-serious control flow.

**Alignment:** **II-0** remains the active **non-promotable** bridge; **Phase II** remains the first **promotable** adaptive-learning build phase; **evidence order** still governs claims.

**Closure proof (Wave 3 seam review):**

1. **Closed in 7.0.0:** Fail-closed tests now cover PIT mismatch, wrong `signal_ids_hash`, baseline/shared-context mismatch, RG-09 anchor misuse, invalid thresholds, and threshold state/expression tampering.
2. **Closed in 7.0.0:** Governed meta evidence now binds threshold ID, state, expression, usage role, and gate-criticality, and the shell compares stored state/expression against the canonical register.
3. **Closed in 7.2.0:** Canonical `pysrc/pipeline` orchestration emits governed II-0B evidence end-to-end under `phase2_ii0b_governed_non_promotable/`, with a root summary/pointer that keeps the governed lane distinct from unrelated root bundle artifacts.
4. **Closed in 7.2.0:** Governed consumers surface threshold-governance summary details uniformly, and stale pre-hash root triples are explicitly excluded from current governed evidence rather than silently continuing to count.
5. **Closed in 7.2.1:** Canonical orchestration now fails closed when the governed II-0B helper raises or returns non-usable evidence, and the borrowed RG-09 threshold IDs on this lane are framed explicitly as reviewer-visible lineage rather than native orchestration threshold policy.

**Authority pointer:** Resolution Ledger — MLN closure row, **GATE-II** **DEFERRED**, evidence order.

### II-0C — Pilot ML Scaffolds

**Purpose:** build minimal, non-promotable machinery around agreed experiments.

**Deliverables:**

- **Scaffolded in 7.2.2:** canonical MetaTask adapter suitable for governed `task_manifest.json` lowering,
- **Scaffolded in 7.2.2:** deterministic, versioned encoder stub that is explicitly reference-only and non-promotable,
- **Scaffolded in 7.2.2:** pilot comparison runner that preserves the XGBoost incumbent and rejects RG-09 / strict-H3 anchor misuse on the incumbent lane,
- **Scaffolded in 7.2.2:** governed II-0C dry-run / pilot wrapper that emits through the existing II-0B artifact lane and fails closed on task-identity drift,
- **Completed in 7.2.3:** frozen reference MetaTask / encoder inputs plus integration replay tests for harness drift detection (not model validity),
- **Completed in 7.2.3:** research-only JSON report shells (`ii0c_pilot_report.json`, `ii0c_dry_run_summary.json`, with `phase2_ii0c_scaffold_non_promotable.json` dual-written for path-based collectors) and pre-emission governed-baseline key discipline plus baseline/shared parity validation.

**Gate to Phase II proper:**

- scaffolding can execute the agreed evidence program,
- scaffolding remains explicitly non-promotable,
- and the W2 path is real enough to justify trainer-adjacent work.

## 4.3 Exit Condition

Phase II-0 exits only when:

- reproducible diagnostics exist,
- pilot artifacts emit in governed form,
- report surfaces are mechanically repeatable,
- and the scaffolding still reads clearly as non-promotable.

# 5. Phase II — Validation-Gated Meta-Learning Build

Phase II is both an implementation phase and a validation program. It builds the actual adaptive-learning system in evidence order and remains killable by the baseline or by failed validation workstreams.

## 5.1 Workstream Guardrails

- W1 governs baseline superiority.
- W2 governs task validity and trainer commitment.
- W3 and W4 govern later trainer policy and allocator buildout.
- W5 governs promotion-path and continual-learning work.
- The baseline may still win and narrow or kill the program.

## 5.2 Phase II Subphases

### II-A — Task Substrate & Validity Closure

**Purpose:** make the **task object** real and evidence-safe (only after I-G / II-0 show regime episodes justify meta-learning framing).

**Deliverables:**

- Formal **task** construction spanning **universe, horizon, volatility / liquidity / macro / cost regimes, objective regime**, and **support/query** (or context/test) with **leakage-safe episode logic**,
- `MetaTask` dataclass,
- `TaskRegistry`,
- BOCPD-backed regime labeler,
- task generator,
- holdout/task provenance surfaces,
- dynamic-K task-facing identity,
- and W2 closure or a clean-enough W2 state for trainer commitment.

**Primary gate:** task identity, leakage safety, non-exchangeability, and **task meaningfulness** are sufficiently validated; otherwise **halt trainer commitment**.

### II-B — Representation Layer

**Purpose:** future **representation seriousness** (usefulness, not allocator superiority by default).

**Deliverables:**

- cross-asset encoders where justified,
- latent regime / **world-model** structures as **candidates**,
- **retrieval / analog memory** over historical episodes as optional representational aid,
- **broad offline pretraining + narrow adapters** pattern experiments,
- context encoder,
- encoder coherence evidence,
- cross-regime separation evidence,
- context-encoder upgrade trigger policy,
- selective event/alt-data entry only where justified.

**Primary gate:** encoder quality is evidence-backed; **representational lift does not substitute for baseline net-of-cost proof**.

### II-C — Adaptation Core

**Purpose:** test **adaptive allocator logic** seriously while still owing proof versus the simpler baseline.

**Deliverables:**

- Reptile trainer,
- few-shot / modular **expert allocator family** experiments,
- regime- and uncertainty-conditioned **gates** (uncertainty as **control variable**, broader than routing),
- **post-adaptation utility** objectives aligned with frictions,
- continual robustness / forgetting resistance evidence,
- support/query mechanics,
- held-out query gain reporting,
- K-budget behavior evidence,
- proxy alignment evidence.

**Primary gate:** adaptation usefulness and proxy alignment are strong enough to justify escalation **only together with** a credible path to **net uplift vs the incumbent baseline after realistic costs**.

### II-D — Allocator & Governance Integration

**Purpose:** integrate allocator intent with **governed, reversible capital expression**—strategically heavier than a naive “finish II-C and stop” reading. This phase is where **allocator intent becomes deployable under constraints**; **differentiable portfolio construction** is **optional** sophistication, not the defining requirement.

**Deliverables:**

- meta-policy network (if promotion evidence exists),
- **structured post-allocator conditioning**: turnover-aware targets, uncertainty-governed sizing, liquidity/capacity overlays, constrained optimizer / policy semantics, leverage/neutrality/CVaR/drawdown/borrow/turnover controls,
- **uncertainty-aware routing pilot graduation** *only if earned*: reject-set evidence shows **negative EV after costs** where routing applies and incumbent retains **positive EV** in that zone; if attenuation captures the benefit, **do not promote routing**,
- regime-aware risk-budgeting interfaces,
- MetaLearner gate,
- full `meta_validity_report.json` path,
- rollback / kill / checkpoint surfaces.

**Hard gate before II-D promotion narratives:** challenger must beat simpler regime-conditioned baseline **net of costs**; else **fail gracefully** to baseline (and further collapse paths remain B2/B1 per Core).

**Primary gate:** allocator behavior is governed, reportable, reversible, and **not confused with deployment-layer wins**.

### II-E — Controlled Rollout Harness

**Purpose:** **bounded live adaptation** meets governance: shadow, canary, capped blends, drift triggers, rollback, **narrow live update surfaces**—consistent with **pretrain broadly, adapt narrowly**.

**Deliverables:**

- allocator-level champion/challenger logic,
- shadow-mode harness,
- capped-blend governance,
- promotion / rollback / kill control flow,
- W5-backed continual-learning safeguards.

**Primary gate:** rollout control exists, but execution realism remains Phase III work.

## 5.3 Required Phase II Artifacts

Once the promotable Phase II path is active, these run outputs are mandatory:

| Artifact | Purpose |
|---|---|
| `meta_validity_report.json` | Canonical gate report for adaptation, encoder, crisis, forgetting, proxy alignment, and governed confidence calibration (`confidence_calibration` with reporting gate) |
| `task_manifest.json` | Exact task-pool evidence for the nightly run, including identity, PIT boundary, and signal-set provenance |
| `gate_result.json` | Existing canonical gate result extended with the meta-learner gate block |
| Checkpointed `theta_meta` and `theta_day_prime` | Promotion, rollback, and audit anchors |

## 5.4 Acceptance Hierarchy

The Phase II program is judged against the Core v2.0 multi-level hierarchy:

- model-level evidence: encoder coherence, cross-regime separation, held-out adaptation gain, Harvey t, proxy alignment, and practical K-budget saturation;
- portfolio-level evidence: net Sharpe after costs, walk-forward sanity, crisis robustness, DSR/PBO discipline, and baseline comparison;
- governance-level evidence: Anti-Goodhart compliance, PIT compliance, determinism compliance, task-pool sufficiency, and forgetting bounds.

# 6. Phase III — Execution Realism & Conditional Deployment

Phase III is the first phase allowed to become execution-serious, and it remains **conditional**—documentation must not read as **earned** because II-D conditioning is important. III is where **implementation shortfall**, participation/capacity decay, urgency/scheduling, tactical overlay, and **execution-controller** seriousness become first-class **if** the program justifies the build.

## 6.1 III-A — Simulation Realism

- paper-trading simulation framework,
- dynamic slippage / market-impact model,
- liquidity-regime-aware cost model,
- realistic fill assumptions for allocator validation.

## 6.2 III-B — Broker & Operator Surfaces

- broker integration,
- order-routing interfaces,
- operator controls / kill-switch surfaces,
- monitoring / alerting implementation,
- paper-to-live promotion flow.

## 6.3 III-C — Optional Low-Latency Path

- C++ / ONNX / TensorRT path,
- conditional intraday inference optimizations,
- optional BOCPD-triggered intraday adaptation path only if justified.

# 7. Phase IV — Signal Factory & Scale-Out

Phase IV is the first phase allowed to become **signal-factory-serious** (broad governed multimodal breadth, automation loops), and it remains **conditional**. **Serious breadth work belongs here**, not inside Phase II proof obligations.

## 7.1 IV-A — Governed Signal Expansion

- operational Signal Generation Protocol,
- governed signal onboarding workflow,
- signal-universe expansion from the current **narrow governed base** under explicit admission/retirement/expansion criteria,
- alternative-data adapters with PIT discipline.

## 7.2 IV-B — Signal Identity & Embedding Layer

- `signal_embedding` implementation,
- novelty / similarity checks,
- retrieval / organization surfaces for broader signal catalogs,
- lifecycle controls tied to signal identity and versions.

## 7.3 IV-C — Assisted Discovery

- architectural pathway for LLM-assisted alpha mining,
- governed validation layer for candidate signals,
- explicit distinction between discovery and promotion.

## 7.4 IV-D — Factory Automation

- broader discovery orchestration,
- governed backtest/promotion loops,
- retirement / decay handling at signal-factory scale.

# 8. Phase IV+ — Frontier Extensions

True frontier ideas remain later, non-default expansion:

- joint regime/signal embedding spaces,
- cross-asset transfer generalization,
- differentiable portfolio optimization,
- autonomous / LLM-assisted alpha mining loops,
- broader synthetic or agent-based validation layers.

# 9. Immediate Priority Stack

1. ~~Close Phase I-F honestly.~~ Done (v4.12.2).
2. ~~Land Phase I-G protocols and empirical foundation.~~ **Closed** (companion truth, Ledger **v1.0.46** / README): protocol surface at v4.13.0; replay fixture at v4.18.1; II-0A harness at v4.18.2; empirical research scaffold at v4.18.5; **strict H3** live promotable anchor in Resolution Ledger §1.5. **RG-09** / **OI-59** remain on the books as **II-0** / **non-blocking** follow-on, not remaining I-G work.
   - OI-35 + OI-36 closed (v4.14.0).
   - OI-37 + OI-38 closed (v4.16.0); OI-39 closed at v4.18.5 (`paper_trade_sim_spec.md`).
   - MOM-020 closed on the governed comparison lane: child-owned cpcv_path_scores.json is authoritative, parent comparison is non-generative, and shared PBO is emitted through comparison_stat_validity.json.
3. Advance Phase **II-0** with **II-0B-first** emphasis:
   - **II-0B** artifact and contract scaffolding (task manifest, meta-validity, execution assumptions) is the default center of gravity.
   - **II-0A** / **OI-59** corrected-surface lanes proceed only under explicit governance and **without** H1-family rescue churn or casual **RG09-H2/H4** runs unless a named decision delta exists.
4. Enter Phase II only in evidence order.

# Appendix A: Protocol and Handoff Surfaces

- [`risk_protocol.md`](risk_protocol.md) — RiskFn Protocol and allocator-to-risk boundary.
- [`signal_generation_protocol.md`](signal_generation_protocol.md) — signal admission, expansion, and retirement policy.
- [`signal_universe_expansion_policy.md`](signal_universe_expansion_policy.md) — conditions for growing the narrow governed base; expansion gates; Phase IV as serious expansion home.
- [`alt_data_admissibility.md`](alt_data_admissibility.md) — PIT, provenance, and replay contract for non-standard data sources (evaluation eligibility, not signal admission).
- [`task_validity_pilot_report.md`](task_validity_pilot_report.md) — first task-validity / non-exchangeability evidence surface.
- [`paper_trade_sim_spec.md`](paper_trade_sim_spec.md) — Phase III handoff spec for paper-trading realism.

# Appendix B: Bundle and Report Contract

## B.1 `meta_validity_report.json`

Minimum required fields:

- `schema_version`
- `inner_loop_gain_by_regime`
- `inner_loop_gain_harvey_t`
- `encoder_clustering`
- `proxy_ic_correlation`
- `crisis_episode_ic`
- `forgetting_delta`
- `confidence_ece`
- `confidence_calibration`
- `net_allocation_sharpe`
- `signal_set_version`
- `anti_goodhart_gap`
- `determinism_check`
- `overall_result`

`confidence_calibration` must fail closed on governed emission paths. When calibration is not measured on-path, emit an explicit `INSUFFICIENT` block with reason rather than omitting the field.

## B.2 `task_manifest.json`

Minimum required per-task evidence:

- `task_id`
- `regime_id`
- `regime_class`
- `t0`
- `t1`
- `pit_boundary`
- `signal_ids_hash`
- `signal_set_version`

# Appendix C: Threshold Handling

- Any unresolved threshold remains marked `⚑ VALIDATE` in docs and policy.
- Tier 1 unresolved thresholds block committed trainer policy.
- Tier 2 unresolved thresholds block shadow-mode entry.
- Tier 3 unresolved thresholds block capped-blend or live promotion.

# Appendix D: Report-to-Phase Test Matrix (March 2026 synthesis)

Twelve internal reports cluster into six test programs. This table is the **canonical mapping**; README and Technical Roadmap summarize it.

| Report cluster | Primary phase | Secondary phase(s) | What is being tested | Promotion rule | Fail / fallback |
|---|---|---|---|---|---|
| Governance / survivability | I-G | II-0, II-D, II-E, III | rollback, kill, drift, shadow, staged promotion, failure containment | governance surfaces explicit and testable | stay conservative; **no alpha overclaim** from governance alone |
| Uncertainty routing | **II-0** | II-D (if earned) | whether `confidence_scalar` identifies **negative-EV / route-worthy** zones **after costs** | promote routing only if reject-set evidence is **strong** in MarketMind data | **remain attenuation-only** |
| Signal breadth / weak-signal thesis | I-G | IV | governed expansion criteria, **SignalCatalog** identity, retirement, diversity, redundancy control | breadth only after **policy + factory readiness** | **keep narrow governed base** |
| Regime-task validity | I-G | II-0, II-A | non-exchangeability, leakage safety, **task meaning** | continue only if tasks are structurally justified | **halt trainer commitment** |
| Allocator validation vs baseline | II-0 | II-B, II-C, II-D | inner-loop gain, encoder coherence, proxy alignment, crisis retention, **net uplift vs simpler baseline** | must beat simpler baseline **net of costs** + burden | **fail gracefully to simpler baseline** (collapse further per Core if regime conditioning fails) |
| Deployment layer | **II-D** | III | turnover-aware target generation, uncertainty-aware sizing, liquidity/capacity conditioning, drawdown/regime overlays | promote only as **governed reversible layer** | keep simpler post-sizing / **RiskFn** path |

## Appendix D.2 Design ideas → primary host phase

| Design commitment / idea | Primary phase | Notes |
|---|---|---|
| Tasks-not-timestamps framing | I-G (freeze) · II-A (realize) | Task distribution is the core object; invalid tasks stop the trainer path |
| Hierarchical layers A/B/C/D | Vision in I-G; II-B/C/D split | A representation · B world/regime · C expert family · **D post-allocator conditioning** (distinct from “allocator intelligence”) |
| Post-adaptation utility after frictions | II-0 (measure) · II-C · II-D | Central acceptance metric; warn against paper-weight-only training |
| Broad pretrain / narrow online adaptation | II-B · II-E | adapters, gates, low-rank updates; full unrestricted live retraining disfavored |
| Uncertainty as allocation control | II-C · II-D | leverage, concentration, turnover, participation, abstention—**default remains attenuation**, routing is pilot |
| Robustness under domain shift | I-G · II-0 | principled falsification; failures are valid **promotion holds** |
| Costs / liquidity / capacity in the loop | **II-D** · III | internalize spread/impact, participation, borrow/funding, capacity decay |
| Multi-timescale control | Architecture vision · II-D/III | strategic allocator · tactical overlay · execution controller · risk governor (future-facing) |
| Retrieval / analog memory | II-0 pilot · II-B | optional; not present core |
| Decision quality > forecast quality | I-G benchmark freeze · all evaluation | utility after costs, stress behavior—not Sharpe-alone storytelling |

**Strategic design-ranking (judgment, not empirical result):** better regime/task design; execution- and capacity-aware training; uncertainty-calibrated sizing/abstention; modular experts with fast adaptation; cross-asset pretraining; robustness penalties; larger backbones last.

<!-- MM:BEGIN:RECENT_CHANGES key="ImplementationPlan" window=4 -->

| Release | Date | Implementation Plan impact |
|---|---|---|
| 6.5.10 | April 2026 | **II-0C pilot harness completion:** §1.2 and §4.2 now record research-only report shells, frozen reference replay inputs, stricter pre-emission baseline/shared parity checks, and explicit non-promotable pilot semantics while keeping **GATE-II DEFERRED** and the XGBoost incumbent baseline. |
| 6.5.9 | April 2026 | **II-0C scaffold dry-run sync:** §1.2 and §4.2 now record the non-promotable II-0C pilot / dry-run lane, canonical MetaTask scaffold, deterministic reference-only encoder stub, XGBoost incumbent comparison guardrail, unchanged governed II-0B artifact lane, and fail-closed identity binding across both public entrypoints while keeping **GATE-II DEFERRED**. |
| 6.5.8 | April 2026 | **II-0B orchestration hard-gate sync:** §4.2 now records that canonical `pysrc/pipeline` orchestration fails closed when governed II-0B evidence is non-usable and that the lane’s borrowed `THR-RG09-V03` / `THR-RG09-V17` references are reviewer-visible lineage rather than native orchestration policy. |
| 6.5.7 | April 2026 | **II-0B closure sync:** §4.2 now records canonical `pysrc/pipeline` rollout of governed II-0B evidence under a dedicated non-promotable subdirectory, reviewer-visible threshold-governance consumer summaries, and explicit retirement of stale pre-hash root triples from current governed evidence; posture advances to **II-0B COMPLETE** without authorizing promotable Phase II work. |
| 6.5.6 | April 2026 | **II-0B 7.0.0 hardening sync:** §1.2 and §4.2 now record required governed artifact `content_hash` blocks, shell semantic revalidation, threshold state/expression reconciliation against the canonical register, and the updated posture: materially hardened, still not exit-ready, no trainer/allocator/rollout authorization. |
| 6.5.5 | April 2026 | **II-0A complete companion sync:** §1.2 and §4.2 now record WS-1 / WS-2 / WS-3 complete, strict-H3 RG-09 reference anchor hash, task-validity integration `ALL_PASS`, externally confirmed CI, and downstream unblock posture with the XGBoost incumbent-baseline guardrail preserved. |
| 6.5.3 | April 2026 | **Phase I-G closure** in companion truth: §1.2 Phase I-G closure paragraph (strict-H3 anchor, widened-H1 recovery artifact, `segmentation_provenance`); RG-09/OI-59 as **II-0** / **non-blocking**; §3.x / §3.x.4 companion exit rule; §9 stack marks I-G **Closed** and **II-0B-first** priority; Resolution Ledger companion stamp **v1.0.46**; stale “remaining I-G work” and H1-rerun priority stack language removed. |
| 6.5.2 | April 2026 | Companion sync for **4.19.2**: title-page and footer stamps advanced; §1.2 audit baseline moved to `VERSION.md` 4.19.2; MLN-07 corrected-lane disposition remains `THR-RG09-V20` superseded / `THR-RG09-V21` active with constructibility-only non-promotable boundaries unchanged. |
| 6.5.1 | April 2026 | Companion truth sync for **4.19.1** MLN-07 threshold-scope disposition: §1.2 now records `THR-RG09-V20` superseded (`DEPRECATED`) and active corrected-lane `THR-RG09-V21` (`VALIDATED`, `feasible_segment_ratio >= 0.025`), closes the “pending MLN-07” posture, and preserves constructibility-only / non-promotable guardrails with no new corrected-branch experiment authorization. |
| 6.5.0 | April 2026 | Minor companion release for **4.19.0**: §1.2 now records single-root cleaning canonicalization (`py.pipeline.stages.cleaning`), declarative `pipeline.cleaning` config, `cleaning_plan.json` / `cleaning_report.json` artifact emission, and `py.pipeline.orchestrator` as the governed dataprep front door while the bridge becomes forward-only with a `5.0.0` removal target. |
| 6.4.34 | April 2026 | **THR-RG09-V20** governance propagation: §1.2 audit baseline **4.18.34**; OI-59 paragraph records MLN-07 memo + register/JSON evidence pointers (**`last_reviewed` v4.18.34**); companion stamps to README **`4.18.34`**, Architecture Vision **1.2.23**, Threshold Governance Register **1.0.2**, `VERSION.md` **4.18.34**; `rg09_oi59_task_definition` module docstring aligned (docs-only; no behavior change). |
| 6.4.33 | April 2026 | Companion doc truthfulness sync: §1.2 adds explicit **OI-59 corrected-branch** lane (**constructibility-only**, **`HOLD_PENDING_THRESHOLD_REVIEW`**, **`THR-RG09-V20`** **`PROVISIONAL`**/**gate-critical**, no further corrected-branch experiments until **MLN-07** resolves); audit baseline **4.18.33**; companion stamps to README **4.18.33**, Architecture Vision **1.2.22**, `VERSION.md` **4.18.33**, Resolution Ledger **1.0.44**. |
| 6.4.32 | April 2026 | §1.2 audit baseline documents the strict H3 successor surface at `runs/rg09_h3_granularity` as the live promotable RG-09 posture (nearby p85 sensitivity control failed with `FAIL_EXCHANGEABLE_TASKS`); companion releases through **4.18.32** advanced stamps to Resolution Ledger **1.0.44** and README / `VERSION.md` **4.18.32**. |
| 6.4.31 | April 2026 | §1.2 audit baseline advanced to **4.18.27**; proper H2 cross-sectional run recorded alongside H4: H4 remained `FAIL_NONREPRODUCIBLE`, while H2 was reproducible enough to evaluate but stayed below threshold statistically; RG-09 no longer treated as an active promotable lane for this phase; companion stamps to Resolution Ledger **1.0.39**, README **4.18.11**, and `VERSION.md` **4.18.27**. |
| 6.4.30 | April 2026 | §1.2 audit baseline advanced to **4.18.26**; executed H4 rescue attempt recorded at `runs/rg09_h4_market_class_risk` with `NEEDS_MORE_EVIDENCE` / `FAIL_NONREPRODUCIBLE` on the narrowed 7-entity market class; RG-09 now treated as terminated for this phase as a promotable decision path; companion stamps to Resolution Ledger **1.0.38**, README **4.18.10**, and `VERSION.md` **4.18.26**. |
| 6.4.29 | April 2026 | §1.2 audit baseline advanced to **4.18.9**; **OI-50** closed (yfinance multi-instrument acquisition + manifest v2 + official v2 fixture); companion stamps to **4.18.9** / Resolution Ledger **1.0.25**. **4.18.25** (April 2026): ledger **§1.5** + **RG-14** / RG09-H2 registration and **II-0B** emphasis recorded in **§1.2** opening paragraph; Resolution Ledger **1.0.37** / `VERSION.md` **4.18.25** stamps. |
| 6.4.28 | April 2026 | §1.2 audit baseline advanced to **4.18.8**; **OI-47** closed (multi-ticker RG-09 replay fixture v2 + empirical H1 outcome documented); companion stamps to **4.18.8** / Resolution Ledger **1.0.24**. |
| 6.4.27 | April 2026 | §1.2 audit baseline advanced to **4.18.7**; assumption **RG09-V13** and **MLN-01** HMAC-key acceptance criterion; `rg09_gate_spec.md` §4 register **RG09-V01**–**RG09-V13**; companion stamps to **4.18.7** / Resolution Ledger **1.0.23**. |
| 6.4.26 | April 2026 | §1.2 audit baseline advanced to **4.18.5**; **OI-39** closed; RG-09 empirical lane `meta_validity_report_research.json` Appendix B.1 alignment; II-0A/B notes updated; companion stamps advanced to **4.18.5** / Resolution Ledger **1.0.21**. |
| 6.4.25 | March 2026 | §1.2 audit baseline advanced to **4.18.2**; RG-09 wording updated so the bounded II-0A harness/gate path is treated as implemented rather than still pending; companion stamps advanced to the **4.18.3** suite baseline. |
| 6.4.24 | March 2026 | §1.2 audit baseline advanced to **4.18.1**; OI-43 closure and RG-09 replay-fixture production recorded; II-0A wording updated so fixture production is treated as satisfied rather than a remaining blocker; companion stamps advanced to the **4.18.1** suite baseline. |
| 6.4.23 | March 2026 | §1.2 audit baseline advanced to **4.18.0**; MLN-02-AMD-01 crisis severity gate recorded; companion stamps advanced to the 4.18.0 suite baseline. |
| 6.4.22 | March 2026 | §1.2 audit baseline advanced to **4.17.0**; MOM-020 recorded as closed on the governed comparison lane; current-state wording no longer treats the momentum comparison track as parallel/open; companion stamps advanced to the 4.17.0 suite baseline. |
| 6.4.21 | March 2026 | §9 Priority Stack: OI-37 + OI-38 closed (v4.16.0); signal-universe expansion policy and alt-data admissibility contract published; core I-G protocol docs complete; remaining OI-39 + RG-09 empirical closure; parallel MOM-020. §1.2 audit baseline advanced to 4.16.0. Appendix A: new protocol links. |
| 6.4.20 | March 2026 | §9 Priority Stack: RG-10 closed (v4.15.0); encoder upgrade criteria frozen; AQ-01 and AQ-02 graduated; next OI-37 + OI-38. §1.2 audit baseline advanced to 4.15.0. |
| 6.4.19 | March 2026 | §9 Priority Stack: OI-35 + OI-36 closed (v4.14.0); RG-10 noted as next with AQ-01/AQ-02 dependency. |
| 6.4.18 | March 2026 | §1.2 audit baseline advanced to 4.13.0; RG-09 moved to PARTIAL in Resolution Ledger; companion stamps rebased to Ledger v1.0.14. |
| 6.4.17 | March 2026 | Companion-sync patch after **4.12.2**: title page, baseline paragraph, and source stamps updated to reflect F-6 closure and the end of Phase I-F. |
| 6.4.16 | March 2026 | March 2026 report synthesis: I-G/II-0/II-… sharpened; II-D deployment-layer / post-allocator conditioning; Appendix D matrices; routing as earned pilot; baseline net-of-cost gate explicit. |

<!-- MM:END:RECENT_CHANGES -->

<!-- MM:BEGIN:SOURCE_STAMP -->

*Implementation Plan v6.5.10 · April 2026 · Companion to Technical Roadmap v1.4.31 · Meta-Learning Core v1.2.25 · Meta-Learning Architecture Vision v1.3.6 · Resolution Ledger v1.0.52 · README.md 7.2.3 · VERSION.md 7.2.3*

<!-- MM:END:SOURCE_STAMP -->

<!-- MM:END:DOCBODY -->
