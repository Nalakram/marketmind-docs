# Version History

This file serves as the project's release ledger and architecture evolution.
For a traditional short-form change summary, see commit history.

Older release entries are archived in `docs/releases/`.

---

## Version Index

### 4.x — ADR-007 hashing, Phase I PIT & closure, I-G protocols & governance

- 4.18.28 — RG-09 H3 strict-surface rescue + p85 sensitivity control: documentation-only patch recording the executed H3 successor PASS on the strict p95 granularity surface, the nearby p85 negative sensitivity control fail-kill, and the reopened RG-09 promotable posture under the strict H3 surface
- 4.18.27 — RG-09 H2/H4 decision-path closeout: documentation-only patch recording the proper H2 cross-sectional result alongside H4; H4 stays a non-reproducible failed rescue, H2 is reproducible but below threshold, and RG-09 is closed for this phase as a promotable decision path
- 4.18.26 — RG-09 H4 rescue failure / phase stop: documentation-only patch recording the executed market-class rescue attempt as another **NEEDS_MORE_EVIDENCE** / **FAIL_NONREPRODUCIBLE** surface; RG-09 is terminated for this phase as a promotable decision path
- 4.18.25 — RG-09 ledger closeout: register **RG09-H2** as **RG-14**, add §1.5 evidentiary boundaries (H1 vs corrected surface), reaffirm **GATE-II-01** trainer lock, move bounded execution emphasis to **Phase II-0B**; companion policy doc touch-ups (`Artifact Write Contract`, `release_authoring_policy`)
- 4.18.23 — RG-09 OI-58 closure: add governed `null_draw_count`, update the harness to read draw count from config, validate THR-RG09-V16, and publish the H2 design brief with OI-57 and residual OI-54 called out as explicit constraints
- 4.18.24 — RG-09 corrected-surface precondition debugging: regenerate the live feasibility artifact, add one-axis geometry sensitivity diagnostics, open OI-59 for contingent segmentation redesign after horizon-overlap collapse, and revise the H2 brief so task admissibility, not fold geometry, is the immediate blocker
- 4.18.22 — RG-09 governance patch: close advisory OI-56; open governed OI-57 for the matched_exchangeable_window semantics/specification gap and OI-58 for draw-count governance; ledger/spec/register alignment only, no runtime or artifact changes
- 4.18.21 — RG-09 documentation alignment: Resolution Ledger, README, Implementation Plan, and companion RG-09 notes now treat earlier insufficient-episode runs as historical fixture-scope evidence; the live governed H1 status remains `NEEDS_MORE_EVIDENCE` with one targeted successor follow-up permitted
- 4.18.20 — **OI-54** RG-09 fixture data layer: `independent_instruments` manifests forbid `uniform_calendar_day_index=true`; real calendar timestamps + `rg09_trading_day_ord` + summary `fold_construction` (calendar time ranges); generator validation; harness applies calendar folds when summary present, trading-ordinal NONCONTIGUOUS, and per-`entity_id` episode tokenization for multi-instrument rows
- 4.18.19 — **OI-55** RG-09 routing follow-up: `_per_lane_fold_inconsistent` runs before the directional-underpowered branch so contradictory fold-level lanes always get `FAIL_NONREPRODUCIBLE`; regression test + spec/ledger alignment
- 4.18.18 — companion-doc version stamp alignment across the live DOCMAP-managed suite; stale managed title-page, DOCMAP, footer, and current-version references corrected with no semantic changes
- 4.18.17 — **OI-55** RG-09 fold-inconsistency routing fix: `_synthesize_decision` now routes contradictory fold-lane evidence to `NEEDS_MORE_EVIDENCE` with `FAIL_NONREPRODUCIBLE`; **OI-54** remains open because the current advisory power-analysis conclusion is still invalid for project-level use
- 4.18.16 — companion-doc version stamp alignment across the live DOCMAP-managed suite; no semantic or behavioral changes
- 4.18.15 — **OI-54** / **OI-55** RG-09 ledger-only validity follow-up: advisory power-analysis conclusion marked untrustworthy due to fixture fold asymmetry; `power_b` FAIL_KILL interpretation blocked pending a fold-inconsistent `_synthesize_decision` state
- 4.18.14 — **OI-53** RG-09 directional-underpowered decision correction: valid non-degenerate H1 evidence is now classified as `NEEDS_MORE_EVIDENCE`; empirical closure returns `inconclusive`; targeted successor follow-up is permitted
- 4.18.13 — **OI-52** Stage 3 RG-09 uniform statistic closeout: all three null families now use the regime-separability statistic; `FAIL_NULL_DISTRIBUTION_INVALID` is gone on the governed rerun; the then-current `FAIL_KILL` interpretation was later superseded by `4.18.14`
- 4.18.12 — **OI-52** Stage 2 RG-09 family-specific statistic: `shuffled_regime` now uses a regime-separability statistic; `RG09-V14` and `THR-RG09-V15` recorded; H1 rerun still emits `FAIL_NULL_DISTRIBUTION_INVALID` because `shuffled_label` and `matched_exchangeable_window` remain degenerate
- 4.18.11 — **OI-52** RG-09 null-distribution invalidity correction: null generators recompute derived episode stats; H1 rerun now emits `gate_executed=true`, `decision=null`, `fail_codes=[FAIL_NULL_DISTRIBUTION_INVALID]`; empirical closure becomes `inconclusive`
- 4.18.10 — **OI-51** RG-09 v2 regeneration: manifest `uniform_calendar_day_index=true` + BOCPD v2 fixture config; deterministic SHA check across two runs; H1 `gate_executed=true` with non-null decision (`FAIL_KILL`)
- 4.18.9 — **OI-50** RG-09 yfinance multi-instrument acquisition + `rg09_multi_fixture_manifest_v2.json`; frozen `data/rg09/`; generator multi-manifest `independent_instruments`; companion sync **6.4.29** / Ledger **1.0.25**
- 4.18.8 — **OI-47** RG-09 multi-ticker replay fixture v2 (`fixtures/rg09/v2/`); generator + tests; empirical H1 outcome recorded; companion sync **6.4.28** / Ledger **1.0.24**
- 4.18.7 — RG09-V13 MetaTask `task_id` HMAC key assumption (⚑ VALIDATE); MLN-01 acceptance criteria; `rg09_gate_spec.md` §4 register **RG09-V01**–**RG09-V13**; companion sync **6.4.27** / Ledger **1.0.23**
- 4.18.6 — Phase II-0B promotable artifact scaffolding (task_manifest / meta_validity_report / execution_assumptions emitters, seed policy, meta_learner_scaffold gate shell); RG-09 pilot threshold IDs; Resolution Ledger **OI-48** / **OI-49**
- 4.18.5 — RG-09 empirical meta-validity scaffold AC patch; OI-39 (paper-trade sim spec) closed in Resolution Ledger
- 4.18.4 — docs/out packaging for versioned implementation manifests and plans
- 4.18.3 — companion-doc synchronization after RG-09 II-0A harness closeout at 4.18.2
- 4.18.2 — RG-09 II-0A harness implementation closeout: bounded gate path, run-derived machine manifest, and release trace/manifest recorded
- 4.18.1 — OI-43 closure: RG-09 replay fixture production completed; ResolutionLedger updated; replay fixture dependency for RG-09 Phase II-0A satisfied
- 4.18.0 — MLN-02-AMD-01: Level 2 `crisis` severity gate (`vol_hi AND severity_flag`), Architecture Vision §4.2 + RG09-V12; `RegimeLabeler` / `BOCPDRegimeService`; ResolutionLedger **OI-44** / **OI-45**; companion suite **1.0.19** / **1.2.19**
- 4.17.1 — RG-09 RG09-DIAG-002: severity-stratified high-vol diagnostic (standalone script + unit tests; PIT-safe thresholds, Cohen's d, basket dedup)
- 4.17.0 — MOM-020 closure: artifact-driven momentum variant comparison; child-owned CPCV surfaces, parent shared-PBO aggregation, no self-certifying comparison layer
- 4.16.0 — Phase I-G protocol closure: signal-universe expansion policy and alt-data admissibility contract published; OI-37 and OI-38 closed
- 4.15.0 — Phase I-G protocol closure: context encoder upgrade criteria frozen; AQ-01, AQ-02, and RG-10 closed
- 4.14.0 — Phase I-G protocol closure: RiskFn Protocol and Signal Generation Protocol published; OI-35 and OI-36 closed
- 4.13.1 — governance patch: OI-43 opened for RG-09 replay fixture production; II-0A entry gate explicit; ImplementationPlan sequencing
- 4.13.0 — Phase I-G RG-09 protocol closure: gate spec, pilot config, replay fixture spec, pilot report design; no code changes
- 4.12.4 — AQ-04 closure; BOCPD orchestrator service; companion wording cleanup
- 4.12.0–4.12.3 — Phase I-F-5 determinism boundary through F-6 coverage/CI closure; companion sync to closed Phase I-F baseline
- 4.9.0–4.11.0 — Phase I-F-2 planning surface through I-F-4 contracts, Signal Reliability schema, ADR-005 seam, companion alignment
- 4.5.4–4.8.0 — Phase I-E closure, I-F-1 audit, momentum/stat_arb vertical slices, companion and ledger evidence
- 4.0.0–4.5.3 — ADR-007 scaffold through PIT (4.1–4.2), governed feature path and stat_arb (4.3–4.4), SignalFactory / I-E governance, test-suite closure

### 3.x — Governed Research System
- 3.8.x — backtesting substrate scaffold and companion-suite synchronization
- 3.7.x — ADR-005 orchestration structure and Phase I-A PIT core / boundary delivery
- 3.6.x — CAS identity, RunRegistry, reconstructible bundles, and deterministic testing infrastructure
- 3.3–3.5 — end-to-end vertical slice, reliability hardening, and architecture clarification
- 3.0–3.2 — pipeline-core reset, executor guardrails, and leakage-safe research primitives

### 2.x — GPU Graph Preprocessor Era
- 2.0.0 — GPU-accelerated graph pipeline stack

### 1.x — Early ML / Infra Exploration
- 1.15.0 — torch utils refactor
- 1.14.x — logging + market data hardening
- 1.13.x — LSTM stack + test modernization
- 1.10–1.12 — model experimentation, indicators, and pipeline scaffolding
- 1.6–1.9 — early system expansion: Java UI, model training, data ingestion

---

## Era Map

| Era | Versions | Focus |
|-----|----------|------|
| ADR-007 Hashing + Phase I PIT + I-G | 4.x | ADR-007 hashing/attestation, golden-vector layout; Phase I PIT orchestration (4.1), source adaptation (4.2), governed feature path (4.3), stat-arb pairs vertical slice (4.4), Phase I-E SignalFactory substrate (4.5); Phase I–I-G protocols & governance (RG-09, RiskFn, signal admission) |
| Governed Artifact System | 3.6.x | CAS storage, RunRegistry, deterministic bundle identity |
| Contract-Driven Execution | 3.5–3.6 | strategy bridge, artifact gates, determinism tiers |
| Reliability Hardening | 3.4.x | coverage push, integration stabilization |
| Operational Vertical Slice | 3.3.x | UI → pipeline → backtest → gate → bundle workflow |
| Leakage-Safe Research | 3.2.x | purged splits, embargo windows, leakage invariants |
| Execution Infrastructure | 3.1.x | executor routing, registry contracts, guardrails |
| Pipeline Core Architecture | 3.0.x | modular pipeline core, registry split, structural refactor |
| GPU Graph Pipeline Platform | 2.x | graph executor, backend registry, GPU preprocessing stack |
| ML Research Prototype | 1.x | model experimentation, data ingestion, logging infrastructure |

---

## Version 4.18.28 (2026-04-05) — RG-09 H3 strict-surface rescue + p85 sensitivity control

Changelog for a docs-only patch that records the executed H3 strict granularity successor surface, the nearby p85 negative sensitivity control, and supersedes earlier draft closeout language that had treated RG-09 as dead for this phase.
Version: **4.18.28** (**PATCH; documentation / ledger truthfulness only**)

### Major Themes Across All Changes

- The historical **H1** transition base surface remains governed evidence with fixture `sha256:07b28854ab30099bbe548ea77ec677122290c9412b6f451bd88fdb8ed781bfa9` and result class **`NEEDS_MORE_EVIDENCE / FAIL_NONREPRODUCIBLE`**: the broad transition surface did not validate non-exchangeability.
- The executed **H4** market-class rescue attempt at `runs/rg09_h4_market_class_risk` remains an unsuccessful predecessor surface because it reproduced the same **non-reproducibility** failure class on the narrowed risk-complex basket.
- The executed proper **H2** cross-sectional run at `runs/rg09_h2_cross_sectional` also remains an unsuccessful predecessor surface, but for a different reason: it was reproducible enough to evaluate and still stayed **below threshold statistically**.
- The executed **H3** strict granularity successor surface at `runs/rg09_h3_granularity` passed on the stricter p95 crisis-labeling surface: `decision = PASS`, `decision_reason = "All required RG-09 evidence families passed."`, `reproducibility_consistent = true`, `fail_codes = []`, and `trainer_commitment_unlocked = true`.
- The nearby **p85** H3 sensitivity control failed cleanly with `decision = FAIL_KILL` and `fail_codes = [FAIL_EXCHANGEABLE_TASKS]`; both the pass and fail H3 surfaces retained the same `admissible_episode_count = 86`, so the pass/fail flip is not explained by more episodes or cleaner geometry.
- The strongest supported lesson is careful and local: **Within the tested H3 neighborhood, crisis-label strictness appears to be the decisive lever; the passing p95 surface preserves crisis/high_vol separation, while the looser p85 surface collapses high_vol into crisis and fails kill.** The attached evidence does **not** fully isolate whether `vol_window = 120` and `trend_flat_epsilon = 0.01` are individually necessary.

### Detailed Changes

| File | Change |
|---|---|
| `docs/src/ResolutionLedger.md` | Bump **MRL 1.0.40** / **CODEBASE 4.18.28**; replace earlier draft phase-stop wording in **§1.5** with the executed H3 strict-surface PASS, retain H1/H4/proper-H2 as unsuccessful predecessor surfaces, record the nearby p85 negative sensitivity control, and state that the emitted harness still identifies the run through the base `RG09-H1` field. |
| `docs/src/ImplementationPlan.md` | Bump to **6.4.32**; update the current-reality paragraph so bounded execution now tracks the strict H3 successor surface rather than the earlier H2/H4 closeout draft. |
| `docs/src/README.md` | Bump to **4.18.12**; refresh current release context, DOCMAP, recent changes, and source stamp so readers no longer see stale language implying RG-09 is still dead or unresolved after the H3 pass. |
| `docs/rg09/rg09_h3_design_brief.md` | Mark the brief as executed; replace the old shared-fixture scaffold note with an emitted-fixture note; append the H3 PASS outcome, nearby p85 control outcome, base-harness identity caveat, and the strictness/separation interpretation. |
| `docs/rg09/rg09_h2_design_brief.md` | Preserve the executed H2 outcome and add a short note that H2 remained an unsuccessful predecessor relative to the later successful strict H3 successor. |
| `docs/rg09/rg09_h4_design_brief.md` | Preserve the executed H4 outcome, mark execution status truthfully, narrow the failure rule to the H4 rescue surface itself, and add a short note that H4 remained an unsuccessful predecessor relative to the later successful strict H3 successor. |
| `docs/traces/4.18.28_implementation_trace.md` | New implementation trace for the docs-only posture rewrite. |
| `docs/manifests/4.18.28_change_manifest.json` | New machine-readable change manifest. |
| `docs/releases/4.18.28.yml` | New release manifest for the docs-only patch. |
| `VERSION.md` | Add the 4.18.28 index bullet and release entry. |

### Behavioral Changes

None. Documentation / ledger truthfulness only.

### Breaking Changes

None.

### Validation Summary

- `rg -n "RG-09|rg09_h3|p95|p85|FAIL_EXCHANGEABLE_TASKS|trainer_commitment_unlocked|strict crisis|high_vol" VERSION.md docs/src docs/rg09`
- `python -m devtools.docs.cli validate-manifest --version 4.18.28`

### Linked Artifacts

- Trace: `docs/traces/4.18.28_implementation_trace.md`
- Manifest: `docs/releases/4.18.28.yml`
- Change manifest: `docs/manifests/4.18.28_change_manifest.json`

### Companion Document Versions

| Document | Version |
|---|---:|
| `README.md` | `4.18.12` |
| `Implementation Plan` | `6.4.32` |
| `Technical Roadmap` | `1.4.21` |
| `Meta-Learning Core` | `1.2.19` |
| `Meta-Learning Architecture Vision` | `1.2.20` |
| `Resolution Ledger` | `1.0.40` |
| `Threshold Governance Register` | `1.0.2` |
| `VERSION.md` | `4.18.28` |

## Version 4.18.27 (2026-04-05) — RG-09 H2/H4 decision-path closeout

Changelog for a docs-only patch that records the executed proper H2 cross-sectional result alongside the earlier H4 rescue attempt and closes RG-09 for this phase as a promotable decision path.
Version: **4.18.27** (**PATCH; documentation / ledger truthfulness only**)

### Major Themes Across All Changes

- The historical H1 transition base surface remains governed evidence with fixture `sha256:07b28854ab30099bbe548ea77ec677122290c9412b6f451bd88fdb8ed781bfa9` and result class **`NEEDS_MORE_EVIDENCE / FAIL_NONREPRODUCIBLE`**: the broad transition surface did not validate non-exchangeability.
- The executed **H4** market-class rescue attempt at `runs/rg09_h4_market_class_risk` remained a **non-reproducible failed rescue** on the narrowed `ES,NQ,RTY,YM,SPY,HYG,VIX` basket.
- The executed proper **H2** cross-sectional run at `runs/rg09_h2_cross_sectional` did **not** repeat the H4 non-reproducibility failure class; it was reproducible enough to evaluate, but statistical evidence stayed **below threshold** on both folds.
- The resulting phase-level conclusion is narrow and explicit: **RG-09 does not justify trainer commitment** and is **terminated for this phase as a promotable decision path**. Any later **H3** work would be exploratory only.

### Detailed Changes

| File | Change |
|---|---|
| `docs/src/ResolutionLedger.md` | Bump **MRL 1.0.39** / **CODEBASE 4.18.27**; extend **§1.5** so the current RG-09 posture now includes the valid H1 non-reproducible base surface, the H4 failed rescue, and the proper H2 reproducible-but-below-threshold negative; keep trainer commitment locked and close RG-09 for this phase as a promotable path. |
| `docs/src/ImplementationPlan.md` | Bump to **6.4.31**; update the current-reality paragraph so bounded execution no longer treats RG-09 as an active promotable lane after either H4 or proper H2. |
| `docs/src/README.md` | Bump to **4.18.11**; refresh current release context, DOCMAP, recent changes, and source stamp so readers see both executed successor outcomes rather than an H4-only closeout. |
| `docs/rg09/rg09_h4_design_brief.md` | Tighten the executed outcome note to include `reproducibility_consistent = false` and a shorter rescue-failed conclusion. |
| `docs/rg09/rg09_h2_design_brief.md` | Mark execution status as executed and append the proper H2 outcome note with run path, fixture SHA, base decision, `fail_closed=false`, and the below-threshold interpretation. |
| `docs/traces/4.18.27_implementation_trace.md` | New implementation trace for the docs-only patch. |
| `docs/manifests/4.18.27_change_manifest.json` | New machine-readable change manifest. |
| `docs/releases/4.18.27.yml` | New release manifest for the docs-only patch. |
| `VERSION.md` | Add the 4.18.27 index bullet and release entry. |

### Behavioral Changes

None. Documentation / ledger truthfulness only.

### Breaking Changes

None.

### Validation Summary

- `rg -n "RG-09|rg09_h2_cross_sectional|rg09_h4_market_class_risk|FAIL_NONREPRODUCIBLE|below threshold|terminated for this phase|trainer commitment" VERSION.md docs/src docs/rg09`
- `python -m devtools.docs.cli validate-manifest --version 4.18.27`

### Linked Artifacts

- Trace: `docs/traces/4.18.27_implementation_trace.md`
- Manifest: `docs/releases/4.18.27.yml`
- Change manifest: `docs/manifests/4.18.27_change_manifest.json`

### Companion Document Versions

| Document | Version |
|---|---:|
| `README.md` | `4.18.11` |
| `Implementation Plan` | `6.4.31` |
| `Technical Roadmap` | `1.4.21` |
| `Meta-Learning Core` | `1.2.19` |
| `Meta-Learning Architecture Vision` | `1.2.20` |
| `Resolution Ledger` | `1.0.39` |
| `Threshold Governance Register` | `1.0.2` |
| `VERSION.md` | `4.18.27` |

## Version 4.18.26 (2026-04-05) — RG-09 H4 rescue failure / phase stop

Changelog for a docs-only patch that records the executed RG-09 H4 market-class rescue attempt truthfully and closes the promotable lane for this phase.
Version: **4.18.26** (**PATCH; documentation / ledger truthfulness only**)

### Major Themes Across All Changes

- The executed **H4** market-class rescue lane is now recorded as a **failed rescue attempt for this phase**, not as proof that no signal exists everywhere.
- The earlier valid **H1** transition surface remains historical governed evidence: **104 admissible episodes**, **`NEEDS_MORE_EVIDENCE`**, **`FAIL_NONREPRODUCIBLE`**, **inconclusive**.
- The executed **H4** successor surface narrowed the basket to the 7-entity equity-risk complex but reproduced the same class of non-reproducibility, so **RG-09 does not justify trainer commitment and is terminated for this phase as a promotable decision path**.
- Any later **H2/H3** work is described only as optional **exploratory / non-governed** follow-up outside the current promotable path.

### Detailed Changes

| File | Change |
|---|---|
| `docs/src/ResolutionLedger.md` | Bump **MRL 1.0.38** / **CODEBASE 4.18.26**; update **§1.5** posture to include the valid H1 base surface and the executed H4 rescue failure; mark RG-09 as terminated for this phase as a promotable path; remove stale implication that H2/H3 remains an active governed rescue lane. |
| `docs/src/ImplementationPlan.md` | Bump to **6.4.30**; refresh the RG-09 current-reality paragraph so H4 is treated as a failed rescue attempt with the same non-reproducibility class of outcome; state that bounded execution should not treat RG-09 as salvageable for promotion in the current phase. |
| `docs/src/README.md` | Bump to **4.18.10**; refresh current release context, DOCMAP, recent changes, and source stamp so users no longer see stale language implying an active post-H4 rescue path. |
| `docs/rg09/rg09_h4_design_brief.md` | Append an outcome note with the executed H4 run path, fixture SHA, config id, decision, fail code, admissible-episode count, and phase-stop interpretation. |
| `docs/traces/4.18.26_implementation_trace.md` | New implementation trace for the docs-only patch. |
| `docs/manifests/4.18.26_change_manifest.json` | New machine-readable change manifest. |
| `docs/releases/4.18.26.yml` | New release manifest for the docs-only patch. |
| `VERSION.md` | Add the 4.18.26 index bullet and release entry. |

### Behavioral Changes

None. Documentation / ledger truthfulness only.

### Breaking Changes

None.

### Validation Summary

- `rg -n "4\\.18\\.26|1\\.0\\.38|6\\.4\\.30|4\\.18\\.10|rg09_h4_market_class_risk|FAIL_NONREPRODUCIBLE|terminated for this phase" VERSION.md docs/src docs/rg09`
- `python -m devtools.docs.cli validate-manifest --version 4.18.26`
- `python -m devtools.docs.cli build-docx-suite --version 4.18.26`
- `python -m devtools.docs.cli verify-suite --version 4.18.26`

### Linked Artifacts

- Trace: `docs/traces/4.18.26_implementation_trace.md`
- Manifest: `docs/releases/4.18.26.yml`
- Change manifest: `docs/manifests/4.18.26_change_manifest.json`

### Companion Document Versions

| Document | Version |
|---|---:|
| `README.md` | `4.18.10` |
| `Implementation Plan` | `6.4.30` |
| `Technical Roadmap` | `1.4.21` |
| `Meta-Learning Core` | `1.2.19` |
| `Meta-Learning Architecture Vision` | `1.2.20` |
| `Resolution Ledger` | `1.0.38` |
| `Threshold Governance Register` | `1.0.2` |
| `VERSION.md` | `4.18.26` |

## Version 4.18.25 (2026-04-04) — RG-09 PARTIAL ledger closeout, RG09-H2 registration (RG-14), II-0B execution focus

Changelog for Resolution Ledger governance: register the H2 successor hypothesis, state what RG-09 evidence does and does not imply, and align companion doc policy references.
Version: **4.18.25** (**documentation / ledger PATCH**)

### Major Themes Across All Changes

- **RG-09** stays **`PARTIAL`**: the ledger now has an explicit **§1.5** separating (a) valid historical H1 `NEEDS_MORE_EVIDENCE` from (b) corrected-surface **zero admissibility** under the current task recipe, and (c) episode-label attribution plumbing (majority `regime_class` under boundary recovery) without claiming gate promotion.
- **RG09-H2** is **registered** as ledger item **`RG-14`** (`OPEN`, **II-0B**, non-blocking); execution remains deferred per `docs/rg09/rg09_h2_design_brief.md` until admissibility recovers (**OI-59** and related lanes).
- **Trainer commitment** (**`GATE-II-01`**) remains **locked** with **MLN-01..07**; Phase **II-0B** scaffolding is the stated bounded execution emphasis alongside parallel RG-09 work.
- Companion policy docs (`docs/Artifact Write Contract.md`, `docs/release_authoring_policy.md`) gain small clarifications already aligned to this release discipline.

### Detailed Changes

| File | Change |
|---|---|
| `docs/src/ResolutionLedger.md` | Bump **MRL 1.0.37** / **CODEBASE 4.18.25**; count matrix (**RG** +1 **OPEN**, totals +1); new **§1.5** program posture; **`RG-14`** YAML for RG09-H2; extend **RG-09** `related` + `resolution` with v4.18.25 pointer. |
| `docs/rg09/rg09_h2_design_brief.md` | Note **RG-14** ledger registration. |
| `docs/src/README.md` | Title companion line, **current release context**, **DOCMAP** rows for Resolution Ledger **1.0.37** and `VERSION.md` **4.18.25**; **RECENT_CHANGES** row for **4.18.25**. |
| `docs/src/ImplementationPlan.md` | Title companion line; **§1.2** opening paragraph for **4.18.25** / **1.0.37**; **RECENT_CHANGES** row; **SOURCE_STAMP** alignment. |
| `docs/traces/4.18.25_implementation_trace.md` | New implementation trace. |
| `docs/manifests/4.18.25_change_manifest.json` | New change manifest. |
| `docs/releases/4.18.25.yml` | New release manifest. |
| `VERSION.md` | This entry + index bullet. |

### Behavioral Changes

None. Ledger and companion documentation only.

### Breaking Changes

None.

### Test / Validation Evidence

- Manual consistency: `rg -n "RG-14|§1\\.5|4\\.18\\.25|1\\.0\\.37" docs/src/ResolutionLedger.md VERSION.md docs/releases/4.18.25.yml`

### Companion Document Versions

| Document | Version |
|---|---:|
| `README.md` | `4.18.9` (stamps only) |
| `Implementation Plan` | `6.4.29` (stamps + §1.2 paragraph) |
| `Technical Roadmap` | `1.4.21` |
| `Meta-Learning Core` | `1.2.19` |
| `Meta-Learning Architecture Vision` | `1.2.20` |
| `Resolution Ledger` | `1.0.37` |
| `Threshold Governance Register` | `1.0.2` |
| `VERSION.md` | `4.18.25` |

### Deferred

- Re-run RG-09 harness / feasibility / separability on post–label-plumbing surfaces and refresh emitted JSON artifacts under `fixtures/` or `runs/` as separate evidence tasks (not part of this ledger-only patch).

---

## Version 4.18.22 (2026-04-04) — RG-09 governance patch: advisory closeout + two governed follow-ups

Changelog for a documentation-only RG-09 governance patch.
Version: **4.18.22** (**documentation-only PATCH release; ledger/spec/threshold-governance alignment only**)

### Major Themes Across All Changes

- The completed advisory lane is now recorded as closed work in the Resolution Ledger without changing the governed H1 result.
- Two new governed RG-09 follow-ups are now explicit: one for the `matched_exchangeable_window` specification gap and one for null draw-count governance.
- No code, thresholds, configs, or governed run artifacts changed in this patch.

### Detailed Changes

| File | Change |
|---|---|
| `docs/src/ResolutionLedger.md` | Bump ledger metadata to `1.0.34` / `VERSION.md 4.18.22`, close advisory **OI-56**, open governed **OI-57** and **OI-58**, update the count matrix, and extend the RG-09 narrative to record the two new non-blocking governance gaps. |
| `docs/rg09/rg09_gate_spec.md` | Add a governed caveat that `matched_exchangeable_window` remains authorized in v1 but its stated semantics versus the implemented generator are under active review under **OI-57**; add open assumption **RG09-V15** for the runtime-derived null draw-count rule. |
| `docs/src/ThresholdGovernanceRegister.md` | Bump the register title-page version to `1.0.1`, align companion references to the current ledger/version baseline, and add provisional threshold row **THR-RG09-V16** for the current null draw-count rule `max(8, len(episodes) * 2)`. |
| `docs/releases/4.18.22.yml` | Add the patch release manifest for this RG-09 governance-only documentation update. |

### Behavioral Changes

None. Documentation-only governance patch.

### Breaking Changes

None.

### Test / Validation Evidence

- `rg -n "OI-56|OI-57|OI-58" docs/src/ResolutionLedger.md`
- `rg -n "matched_exchangeable_window|OI-57|RG09-V15" docs/rg09/rg09_gate_spec.md`
- `rg -n "draw_count|max\\(8, len\\(episodes\\) \\* 2\\)|THR-RG09-V16|OI-58" docs/src/ThresholdGovernanceRegister.md srcPy/meta/rg09_harness.py docs/src/ResolutionLedger.md`
- `rg -n "4\\.18\\.22|1\\.0\\.34|1\\.0\\.1" VERSION.md docs/releases/4.18.22.yml docs/src/ResolutionLedger.md docs/src/ThresholdGovernanceRegister.md`

### Companion Document Versions

| Document | Version |
|---|---:|
| `README.md` | `4.18.9` |
| `Implementation Plan` | `6.4.29` |
| `Technical Roadmap` | `1.4.21` |
| `Meta-Learning Core` | `1.2.19` |
| `Meta-Learning Architecture Vision` | `1.2.20` |
| `Resolution Ledger` | `1.0.34` |
| `Threshold Governance Register` | `1.0.1` |
| `VERSION.md` | `4.18.22` |

## Version 4.18.23 (2026-04-04) — RG-09 OI-58 closure + H2 design brief

Changelog for the narrow RG-09 draw-count governance closure patch and H2 design brief publication.
Version: **4.18.23** (**PATCH**)

### Major Themes Across All Changes

- OI-58 is now closed by moving RG-09 null draw count onto the governed pilot-config surface.
- The harness no longer derives draw count from episode count at runtime.
- H2 design is now documented explicitly with OI-57 and residual OI-54 carried as constraints rather than blockers.

### Detailed Changes

| File | Change |
|---|---|
| `srcPy/meta/rg09_harness.py` | Add `null_draw_count` to `RG09PilotConfig`, load it from config, and make `_evaluate_fold` use the configured value instead of `max(8, len(episodes) * 2)`. |
| `docs/rg09/rg09_pilot_config_v1.json` | Add governed field `null_draw_count = 64`. |
| `docs/rg09/rg09_pilot_config_v1_power_a.json` | Add governed field `null_draw_count = 64` so the alternative pilot config remains schema-compatible. |
| `tests/python/unit/meta/test_rg09_harness.py` | Add RED/GREEN coverage that `null_draw_count` loads from config and that fold summaries emit the configured draw count. |
| `docs/rg09/rg09_gate_spec.md` | Update the statistical-lane description so each family/fold comparison uses configured `null_draw_count` draws and remove the former open draw-count assumption row. |
| `docs/src/ThresholdGovernanceRegister.md` | Bump the register to `1.0.2` and transition `THR-RG09-V16` from `PROVISIONAL` to `VALIDATED` at `null_draw_count = 64`. |
| `docs/src/ResolutionLedger.md` | Bump ledger metadata to `1.0.35`, close `OI-58`, tighten `OI-57` language so H2 may execute with the underspecification caveat, and record the H2 brief path. |
| `docs/rg09/rg09_h2_design_brief.md` | Publish the H2 design brief with corrected fold-construction as a fixture requirement and `OI-57` / residual `OI-54` as explicit interpretation constraints. |
| `docs/releases/4.18.23.yml` | Add the release manifest for this RG-09 closure patch. |

### Behavioral Changes

- RG-09 statistical null draws are now governed by config (`null_draw_count = 64`) rather than by admissible episode count.

### Breaking Changes

- `load_rg09_config()` now requires `null_draw_count` in governed RG-09 pilot configs.

### Test / Validation Evidence

- `cmd.exe /c "cd /d C:\\Users\\Nalakram\\Documents\\GitHub\\MarketMind && .venv-codex\\Scripts\\python.exe -m pytest --no-cov tests\\python\\unit\\meta\\test_rg09_harness.py -q"`
- `cmd.exe /c "cd /d C:\\Users\\Nalakram\\Documents\\GitHub\\MarketMind && .venv-codex\\Scripts\\python.exe -m pytest --no-cov tests\\python\\integration\\meta\\test_run_rg09_gate.py -q"`
- `cmd.exe /c "cd /d C:\\Users\\Nalakram\\Documents\\GitHub\\MarketMind && .venv-codex\\Scripts\\python.exe -m mypy --strict srcPy\\meta\\rg09_harness.py"`

### Companion Document Versions

| Document | Version |
|---|---:|
| `README.md` | `4.18.9` |
| `Implementation Plan` | `6.4.29` |
| `Technical Roadmap` | `1.4.21` |
| `Meta-Learning Core` | `1.2.19` |
| `Meta-Learning Architecture Vision` | `1.2.20` |
| `Resolution Ledger` | `1.0.35` |
| `Threshold Governance Register` | `1.0.2` |
| `VERSION.md` | `4.18.23` |

## Version 4.18.24 (2026-04-04) — RG-09 corrected-surface precondition diagnostics + contingent OI-59

Changelog for the corrected-surface RG-09 precondition-debug pass on the live v2 basket.
Version: **4.18.24** (**PATCH**)

### Major Themes Across All Changes

- The stale stacked-surface feasibility artifact has been replaced by a corrected-surface feasibility artifact for fixture `sha256:421b8a39057c840aa4e7c5fbd6d35603e137920c0039fcff2c595fcad9f84636`.
- A new one-axis geometry sensitivity diagnostic now measures support/query/dwell leverage on the existing segmentation before any task-definition redesign.
- The evidence shows the current blocker is pre-statistical task admissibility on the corrected surface, so OI-59 is opened as the contingent governed segmentation-redesign lane and the H2 brief is updated accordingly.

### Detailed Changes

| File | Change |
|---|---|
| `srcPy/meta/rg09_feasibility.py` | Bump the feasibility artifact schema to `v2` and add regime-class coverage plus crisis-surface summary fields. |
| `srcPy/meta/rg09_geometry_sensitivity.py` | Add a new one-axis geometry sensitivity diagnostic over `min_support_rows`, `min_query_rows`, and `min_dwell_time_bars` on the current segmentation. |
| `scripts/run_rg09_geometry_sensitivity.py` | Add the CLI entrypoint that emits `rg09_geometry_sensitivity.json`. |
| `fixtures/rg09/v2/rg09_episode_feasibility.json` | Regenerate the live corrected-surface feasibility artifact against fixture `sha256:421b8a...`; it now records zero admissible episodes and `HORIZON_OVERLAP` dominance on the corrected basket. |
| `fixtures/rg09/v2/rg09_geometry_sensitivity.json` | Add the corrected-surface one-axis sensitivity artifact; tested support/query relaxations do not recover admissibility on the current segmentation. |
| `docs/rg09/rg09_v2_corrected_surface_precondition_diagnostic.md` | Record the corrected-surface findings, stale-surface comparison note, geometry sensitivity result, and crisis sub-diagnostic. |
| `docs/rg09/rg09_h2_design_brief.md` | Reframe H2 so corrected-surface task admissibility is the immediate blocker, breadth remains frozen, and OI-59 is the contingent governed successor lane if redesign is required. |
| `docs/src/ResolutionLedger.md` | Bump ledger metadata to `1.0.36`, open `OI-59`, and update the RG-09 narrative with the corrected-surface feasibility and sensitivity findings. |
| `tests/python/unit/meta/test_rg09_feasibility.py` | Add coverage for regime-class and crisis-surface detail in the feasibility artifact. |
| `tests/python/unit/meta/test_rg09_geometry_sensitivity.py` | Add unit coverage for first-order binding detection and dwell-axis inactivity. |
| `tests/python/integration/meta/test_run_rg09_geometry_sensitivity.py` | Add the integration check that the geometry sensitivity CLI emits its required artifact. |
| `docs/releases/4.18.24.yml` | Add the release manifest for this RG-09 corrected-surface diagnostics patch. |

### Behavioral Changes

- RG-09 now has an explicit corrected-surface geometry sensitivity artifact alongside the pre-gate feasibility artifact.
- Feasibility reporting now exposes admissible/candidate regime-class detail and a crisis-surface summary.

### Breaking Changes

None to governed gate execution. This patch is diagnostic and governance-oriented.

### Test / Validation Evidence

- `cmd.exe /c "cd /d C:\\Users\\Nalakram\\Documents\\GitHub\\MarketMind && .venv-codex\\Scripts\\python.exe -m pytest --no-cov tests\\python\\unit\\meta\\test_rg09_feasibility.py tests\\python\\unit\\meta\\test_rg09_geometry_sensitivity.py -q"`
- `cmd.exe /c "cd /d C:\\Users\\Nalakram\\Documents\\GitHub\\MarketMind && .venv-codex\\Scripts\\python.exe -m pytest --no-cov tests\\python\\integration\\meta\\test_run_rg09_feasibility.py tests\\python\\integration\\meta\\test_run_rg09_geometry_sensitivity.py -q"`
- `cmd.exe /c "cd /d C:\\Users\\Nalakram\\Documents\\GitHub\\MarketMind && .venv-codex\\Scripts\\python.exe -m mypy --strict srcPy\\meta\\rg09_feasibility.py srcPy\\meta\\rg09_geometry_sensitivity.py"`
- `cmd.exe /c "cd /d C:\\Users\\Nalakram\\Documents\\GitHub\\MarketMind && .venv-codex\\Scripts\\python.exe -m scripts.run_rg09_feasibility --fixture fixtures\\rg09\\v2\\rg09_fixture_v2.parquet --fixture-summary fixtures\\rg09\\v2\\rg09_fixture_summary.json --fixture-metadata fixtures\\rg09\\v2\\rg09_fixture_metadata.json --config docs\\rg09\\rg09_pilot_config_v1.json --output-path fixtures\\rg09\\v2\\rg09_episode_feasibility.json"`
- `cmd.exe /c "cd /d C:\\Users\\Nalakram\\Documents\\GitHub\\MarketMind && .venv-codex\\Scripts\\python.exe -m scripts.run_rg09_geometry_sensitivity --fixture fixtures\\rg09\\v2\\rg09_fixture_v2.parquet --fixture-summary fixtures\\rg09\\v2\\rg09_fixture_summary.json --fixture-metadata fixtures\\rg09\\v2\\rg09_fixture_metadata.json --config docs\\rg09\\rg09_pilot_config_v1.json --output-path fixtures\\rg09\\v2\\rg09_geometry_sensitivity.json --support-values 64,48,32 --query-values 32,24,16 --dwell-values 32,24,16"`

### Companion Document Versions

| Document | Version |
|---|---:|
| `README.md` | `4.18.9` |
| `Implementation Plan` | `6.4.29` |
| `Technical Roadmap` | `1.4.21` |
| `Meta-Learning Core` | `1.2.19` |
| `Meta-Learning Architecture Vision` | `1.2.20` |
| `Resolution Ledger` | `1.0.36` |
| `Threshold Governance Register` | `1.0.2` |
| `VERSION.md` | `4.18.24` |

## Version 4.18.21 (2026-04-03) — RG-09 governed-evidence doc alignment

Changelog for RG-09 documentation alignment after the governed H1 line settled into its allowed `NEEDS_MORE_EVIDENCE` state.
Version: **4.18.21** (**documentation-only PATCH release; governed-evidence wording alignment only**)

### Major Themes Across All Changes

- Live RG-09 status text was corrected to distinguish historical precondition-failure artifacts from the current governed H1 line.
- No architectural scope changed. No new ADR, AQ, or OI was introduced, and no code, threshold, fixture, or harness behavior changed.

### Detailed Changes

| File | Change |
|---|---|
| `docs/src/ResolutionLedger.md` | Bump ledger metadata to `1.0.33` / `VERSION.md 4.18.21` and update the RG-09 narrative so the current governed state is explicitly `NEEDS_MORE_EVIDENCE` with one targeted successor follow-up permitted; earlier insufficient-episode runs remain historical fixture-scope evidence only. |
| `docs/src/README.md` | Update current-release context to reference the corrected RG-09 live status instead of presenting the old precondition-failure surface as current. |
| `docs/src/ImplementationPlan.md` | Update audit-baseline and RG-09 roadmap text so OI-46 / OI-47 / OI-50 remain historical evidence while the live H1 line is the later valid `NEEDS_MORE_EVIDENCE` run. |
| `docs/rg09/rg09_data_acquisition_log.md` | Clarify that the documented v2 insufficient-episodes result is historical evidence for that bundle, not the current RG-09 H1 status. |
| `docs/rg09/rg09_power_b_comparison.md` | Mark the historical `FAIL_KILL` output as a superseded routing interpretation and align the narrative with the Resolution Ledger’s governed reading. |
| `docs/releases/4.18.21.yml` | Add the release manifest for this documentation-only RG-09 status alignment patch. |

### Behavioral Changes

None. Documentation-only pass.

### Breaking Changes

None.

### Test / Validation Evidence

- `rg -n "gate_executed=false|FAIL_INSUFFICIENT_EPISODES|successor activation remains blocked|FAIL_KILL" docs/src/README.md docs/src/ImplementationPlan.md docs/rg09`

### Companion Document Versions

| Document | Version |
|---|---:|
| `README.md` | `4.18.9` |
| `Implementation Plan` | `6.4.29` |
| `Technical Roadmap` | `1.4.21` |
| `Meta-Learning Core` | `1.2.19` |
| `Meta-Learning Architecture Vision` | `1.2.20` |
| `Resolution Ledger` | `1.0.33` |
| `VERSION.md` | `4.18.21` |

### Deferred

- Historical RG-09 comparison documents that intentionally preserve emitted artifact truth, such as `docs/rg09/rg09_power_a_comparison.md`, still describe their recorded outputs and were not rewritten beyond the minimum wording needed to avoid overstating the live RG-09 status.

## Version 4.18.18 (2026-04-03) — companion-doc version stamp alignment

Changelog for companion-doc version stamp alignment across the live DOCMAP-managed suite.
Version: **4.18.18** (**documentation-only PATCH release; live stamp synchronization only**)

### Major Themes Across All Changes

- Suite stamp synchronization only. The live DOCMAP-managed source documents were aligned to the actual canonical versions in this repo with token-level stamp updates only.
- No semantic rewrite. Historical release rows, architecture claims, gate language, and ledger decision bodies were left unchanged.

### Detailed Changes

| File | Stale String | Corrected String |
|---|---|---|
| `docs/src/README.md` | `Version 4.18.16`; managed companion line with `v1.0.0` siblings and `VERSION.md 4.18.16`; current prose `VERSION.md 4.18.16`; managed DOCMAP rows `4.18.16 / 1.0.0 / ... / 4.18.16`; source stamp `v4.18.16 ... v1.0.0 ... 4.18.16` | `Version 4.18.9`; managed companion line `v6.4.29 / v1.4.21 / v1.2.19 / v1.2.20 / v1.0.32 / 4.18.17`; current prose `VERSION.md 4.18.17`; managed DOCMAP rows `4.18.9 / 6.4.29 / 1.4.21 / 1.2.19 / 1.2.20 / 1.0.32 / 4.18.17`; source stamp aligned |
| `docs/src/ImplementationPlan.md` | `Version 1.0.0`; managed companion line `v1.0.0 ... 4.18.16`; source stamp `v1.0.0 ... 4.18.16` | `Version 6.4.29`; managed companion line `v1.4.21 / v1.2.19 / v1.2.20 / v1.0.32 / 4.18.9 / 4.18.17`; source stamp aligned |
| `docs/src/TechnicalRoadmap.md` | `Version 1.0.0`; managed companion line `v1.0.0 ... 4.18.16`; source stamp `v1.0.0 ... 4.18.16` | `Version 1.4.21`; managed companion line `v6.4.29 / v1.2.19 / v1.2.20 / v1.0.32 / 4.18.9 / 4.18.17`; source stamp aligned |
| `docs/src/MetaLearningCore.md` | `Version 1.0.0`; managed companion line `v1.0.0 ... 4.18.16`; managed DOCMAP rows `1.0.0 / ... / 4.18.16`; source stamp `v1.0.0 ... 4.18.16` | `Version 1.2.19`; managed companion line `v6.4.29 / v1.4.21 / v1.2.20 / v1.0.32 / 4.18.9 / 4.18.17`; managed DOCMAP rows aligned; source stamp aligned |
| `docs/src/MetaLearningArchitectureVision.md` | `Version 1.0.0`; managed companion line `v1.0.0 ... 4.18.16`; prose `Resolution Ledger v1.0.31`; managed DOCMAP rows `1.0.0 / ... / 4.18.16`; source stamp `v1.0.0 ... 4.18.16` | `Version 1.2.20`; managed companion line `v6.4.29 / v1.4.21 / v1.2.19 / v1.0.32 / 4.18.9 / 4.18.17`; prose `Resolution Ledger v1.0.32`; managed DOCMAP rows aligned; source stamp aligned |
| `docs/traces/4.18.18_implementation_trace.md` | `n/a (new file)` | `implementation trace added` |
| `docs/manifests/4.18.18_change_manifest.json` | `n/a (new file)` | `change manifest added` |
| `VERSION.md` | latest release record stopped at `4.18.17` | `4.18.18` index bullet and release entry added |

### Behavioral Changes

None. Documentation-only pass.

### Breaking Changes

None.

### Test / Validation Evidence

- Managed-suite stale-string grep returned zero matches:

```bash
rg -n "Version 1\.0\.0|v1\.0\.0|README\.md 4\.18\.16|VERSION\.md 4\.18\.16|Resolution Ledger v1\.0\.31|\| README\.md \| 4\.18\.16 \||\| VERSION\.md \| 4\.18\.16 \||\| Implementation Plan \| 1\.0\.0 \||\| Technical Roadmap \| 1\.0\.0 \||\| Meta-Learning Core \| 1\.0\.0 \||\| Meta-Learning Architecture Vision \| 1\.0\.0 \||\| Resolution Ledger \| 1\.0\.0 \|" docs/src/README.md docs/src/ImplementationPlan.md docs/src/TechnicalRoadmap.md docs/src/MetaLearningCore.md docs/src/MetaLearningArchitectureVision.md docs/src/ResolutionLedger.md
```

```text
<no output; exit code 1>
```

### Companion Document Versions

| Document | Version |
|---|---:|
| `README.md` | `4.18.9` |
| `Implementation Plan` | `6.4.29` |
| `Technical Roadmap` | `1.4.21` |
| `Meta-Learning Core` | `1.2.19` |
| `Meta-Learning Architecture Vision` | `1.2.20` |
| `Resolution Ledger` | `1.0.32` |
| `VERSION.md` | `4.18.18` |

### Deferred

- Out-of-scope docs outside the live managed DOCMAP still contain stale companion stamps and were intentionally not edited in this pass:
  - `docs/src/FormattingSpec.md`
  - `docs/src/DataGovernanceCharter.md`
  - `docs/src/PhaseIIArtifactContract.md`
  - `docs/src/PhaseIIResearchExecutionPlaybook.md`
  - `docs/src/ThresholdGovernanceRegister.md`
- `docs/releases/VERSION_3.x.md` was scanned for the stale patterns used in this pass; no matching stale companion references were found, so the archive remained unchanged.

## Version 4.18.17 (2026-04-03) — RG-09 fold-inconsistency routing correction

Version: **4.18.17** (**PATCH**)

This release records the RG-09 power-analysis advisory-validity finding in the ledger and fixes the harness decision gap for contradictory fold-level lane evidence. No thresholds, null generators, fixtures, pilot configs, or power-analysis formulas changed.

### Detailed Changes

- `srcPy/meta/rg09_harness.py`: add `_per_lane_fold_inconsistent(...)` and route contradictory fold-level statistical / structural / functional outcomes to `NEEDS_MORE_EVIDENCE` with `FAIL_NONREPRODUCIBLE` before the terminal `FAIL_KILL` branch.
- `tests/python/unit/meta/test_rg09_harness.py`: add RED/GREEN unit coverage for the new helper and the fold-inconsistent routing case.
- `docs/rg09/rg09_gate_spec.md`: document that contradictory fold-level lane evidence is non-reproducible and routes to `NEEDS_MORE_EVIDENCE` / `FAIL_NONREPRODUCIBLE`, not `FAIL_KILL`.
- `docs/src/ResolutionLedger.md`: keep **OI-54** open as the advisory-validity finding, close **OI-55** with the implemented routing fix, update the RG-09 resolution narrative, and advance the ledger release metadata.
- `docs/releases/4.18.17.yml`: add the release manifest for this narrow RG-09 corrective patch.

### Behavioral Changes

- Mixed fold-level lane outcomes no longer fall through to `FAIL_KILL`.
- The current RG-09 power-analysis advisory conclusion remains invalid for project-level decision use until rerun on corrected fixture fold structure.

### Breaking Changes

None.

### Test / Validation Evidence

- `pytest --no-cov tests/python/unit/meta/test_rg09_harness.py`
- `mypy --strict srcPy/meta/rg09_harness.py`

### Companion Document Versions

| Document | Version |
|---|---:|
| `README.md` | `4.18.9` |
| `Implementation Plan` | `6.4.29` |
| `Technical Roadmap` | `1.4.21` |
| `Meta-Learning Core` | `1.2.19` |
| `Meta-Learning Architecture Vision` | `1.2.20` |
| `Resolution Ledger` | `1.0.32` |
| `VERSION.md` | `4.18.17` |

## Version 4.18.16 (2026-04-03) — companion-doc version stamp alignment

Changelog for companion-doc version stamp alignment across the live DOCMAP-managed suite.
Version: **4.18.16** (**documentation-only PATCH release; live stamp synchronization only**)

### Major Themes Across All Changes

- Suite stamp synchronization only. Live title-page companion lines, footer/source stamps, DOCMAP rows, and safe live version tokens were aligned to the canonical companion baseline confirmed from the ledger header and live DOCMAP.
- No semantic rewrite. Historical release rows, ledger entry bodies, threshold text, and behavioral descriptions were left untouched unless a direct live companion token could be corrected safely.

### Detailed Changes

| File | Stale String | Corrected String |
|---|---|---|
| `README.md` | `Version 4.18.1 · March 2026`; `Implementation Plan v6.4.24`; `Resolution Ledger v1.0.20`; `VERSION.md 4.18.1` | `Version 4.18.9 · April 2026`; `Implementation Plan v6.4.29`; `Resolution Ledger v1.0.31`; `VERSION.md 4.18.16` |
| `docs/src/README.md` | `Resolution Ledger v1.0.25`; `VERSION.md 4.18.9` | `Resolution Ledger v1.0.31`; `VERSION.md 4.18.16` |
| `docs/src/ImplementationPlan.md` | `Version 6.4.26`; `Resolution Ledger v1.0.21`; `README.md 4.18.5`; `VERSION.md 4.18.5` | `Version 6.4.29`; `Resolution Ledger v1.0.31`; `README.md 4.18.9`; `VERSION.md 4.18.16` |
| `docs/src/TechnicalRoadmap.md` | `Implementation Plan v6.4.26`; `Resolution Ledger v1.0.21`; `README.md 4.18.5`; `VERSION.md 4.18.5` | `Implementation Plan v6.4.29`; `Resolution Ledger v1.0.31`; `README.md 4.18.9`; `VERSION.md 4.18.16` |
| `docs/src/MetaLearningCore.md` | `Implementation Plan 6.4.26`; `Resolution Ledger 1.0.21`; `README.md 4.18.5`; `VERSION.md 4.18.5` | `Implementation Plan 6.4.29`; `Resolution Ledger 1.0.31`; `README.md 4.18.9`; `VERSION.md 4.18.16` |
| `docs/src/MetaLearningArchitectureVision.md` | `Implementation Plan 6.4.26`; `Resolution Ledger 1.0.21`; `README.md 4.18.5`; `VERSION.md 4.18.5`; `Resolution Ledger v1.0.21` | `Implementation Plan 6.4.29`; `Resolution Ledger 1.0.31`; `README.md 4.18.9`; `VERSION.md 4.18.16`; `Resolution Ledger v1.0.31` |
| `docs/src/ResolutionLedger.md` | `VERSION.md 4.18.15` | `VERSION.md 4.18.16` |
| `docs/traces/4.18.16_implementation_trace.md` | `n/a (new file)` | `implementation trace added` |
| `docs/manifests/4.18.16_change_manifest.json` | `n/a (new file)` | `change manifest added` |
| `VERSION.md` | latest release record stopped at `4.18.15` | `4.18.16` index bullet and release entry added |

### Behavioral Changes

None. Documentation-only pass.

### Breaking Changes

None.

### Test / Validation Evidence

- Exact stale-string grep probes for the managed live surfaces returned no matches:
  - `README.md`
  - `docs/src/README.md`
  - `docs/src/ImplementationPlan.md`
  - `docs/src/TechnicalRoadmap.md`
  - `docs/src/MetaLearningCore.md`
  - `docs/src/MetaLearningArchitectureVision.md`
  - `docs/src/ResolutionLedger.md`
- `docs/releases/VERSION_3.x.md` was scanned for the stale companion-version patterns used in this pass; no matches were found and the archive was left unchanged.
- Full command strings and outputs are recorded in `docs/traces/4.18.16_implementation_trace.md`.

### Companion Document Versions

| Document | Version |
|---|---:|
| `README.md` | `4.18.9` |
| `Implementation Plan` | `6.4.29` |
| `Technical Roadmap` | `1.4.21` |
| `Meta-Learning Core` | `1.2.19` |
| `Meta-Learning Architecture Vision` | `1.2.20` |
| `Resolution Ledger` | `1.0.31` |
| `VERSION.md` | `4.18.16` |

### Deferred

- `docs/src/ImplementationPlan.md` still contains a current-baseline section anchored to `4.18.9`. A truthful update would require semantic rebasing of the narrative, not a stamp-only token replacement.
- `docs/src/MetaLearningArchitectureVision.md` still contains a `Documentation baseline` row anchored to the historical `4.18.5` companion baseline. A truthful update would require semantic rewriting, so it was not changed in this pass.
- Out-of-scope docs outside the live DOCMAP still carry older companion stamps and were not edited: `docs/src/WhitePaper.md`, `docs/src/FormattingSpec.md`, `docs/src/DataGovernanceCharter.md`, `docs/src/PhaseIIResearchExecutionPlaybook.md`, `docs/src/PhaseIIArtifactContract.md`, `docs/src/ThresholdGovernanceRegister.md`.
- `docs/releases/VERSION_3.x.md` was scanned for the stale patterns used in this pass; no matching stale companion references were found, so the archive remained unchanged.

## Version 4.18.15 (2026-04-03) — OI-54 / OI-55 RG-09 Advisory Validity and Fold-Inconsistency Ledger Update

Version: **4.18.15** (**PATCH**)

Summary:
Open **OI-54** and **OI-55** in the Resolution Ledger only. **OI-54** records that the advisory power-analysis conclusion at `runs/rg09_power_analysis/v1/rg09_power_analysis.json` is not trustworthy because the baseline fold surface used by the tool is contaminated by `uniform_calendar_day_index=true` stacking rather than two independent temporal samples. **OI-55** records a remaining RG-09 harness decision-state gap exposed by `power_b`: fold-inconsistent evidence currently falls through to `FAIL_KILL` / `FAIL_EXCHANGEABLE_TASKS`, so that output must not be treated as a valid kill decision until `_synthesize_decision()` gets an explicit contradictory-fold branch. No code, fixture, gate-spec, or companion-doc changes land in this release; only `docs/src/ResolutionLedger.md` and `VERSION.md` advance.

Major changes:
- `docs/src/ResolutionLedger.md`: bump ledger version to `1.0.31` / codebase `4.18.15`, open **OI-54** and **OI-55**, add the new blocking-hotlist row for **OI-55**, and extend the **RG-09** resolution text with the advisory power-analysis invalidity finding and the `power_b` fold-inconsistency caveat.
- `VERSION.md`: add the `4.18.15` index bullet and this doc-only release entry.

Breaking changes:
- None.

Validation summary:
- `git diff -- docs/src/ResolutionLedger.md VERSION.md`
  - Result: only the requested ledger + release-ledger updates are included.
- Tests not run.
  - Reason: explicit doc-only scope; no code paths changed in this release.

Linked trace path:
- None authored for this explicit doc-only scope.

Linked manifest path:
- None authored for this explicit doc-only scope.

## Version 4.18.14 (2026-04-02) — OI-53 RG-09 Directional-Underpowered Decision Correction

Version: **4.18.14** (**PATCH**)

Summary:
Open and close **OI-53** to correct the RG-09 decision-logic gap discovered after the first valid non-degenerate H1 rerun. The harness previously had no state for "structural passes, nulls valid, directional signal present, but statistical power below threshold," so `_synthesize_decision()` fell through to `FAIL_KILL`. This release adds an explicit `NEEDS_MORE_EVIDENCE` branch for that governed case, updates the gate spec accordingly, reruns H1 and empirical closure into fresh directories, and records the governed finding accurately. The new H1 artifact at `runs/rg09_v2/h1_v2bocpd_directional_nme/` is `NEEDS_MORE_EVIDENCE`, not `FAIL_KILL`.

Major changes:
- `srcPy/meta/rg09_harness.py`: `_synthesize_decision()` now returns `NEEDS_MORE_EVIDENCE` when structural evidence passes, nulls are valid, the statistical lane remains directionally above the null surface across all folds/families, and functional evidence retains positive directional delta but remains below threshold.
- `tests/python/unit/meta/test_rg09_harness.py`: add RED/GREEN coverage for the directional-underpowered branch both at the pure decision-function level and at the emitted gate-result artifact level.
- `docs/rg09/rg09_gate_spec.md`: expand `NEEDS_MORE_EVIDENCE` to cover the directional-underpowered case and reserve `FAIL_KILL` / `FAIL_EXCHANGEABLE_TASKS` for confirmed collapse.
- `docs/src/ResolutionLedger.md`: add **OI-53** and update **RG-09** to record the governed outcome as `NEEDS_MORE_EVIDENCE`.
- Fresh reruns:
  - `runs/rg09_v2/h1_v2bocpd_directional_nme/rg09_gate_result.json`
  - `runs/rg09_v2/empirical_v2bocpd_directional_nme/rg09_empirical_summary.json`

Breaking changes:
- None.

Validation summary:
- `cmd.exe /c "cd /d C:\Users\Nalakram\Documents\GitHub\MarketMind && .venv-codex\Scripts\python.exe -m pytest --no-cov tests\python\unit\meta\test_rg09_harness.py tests\python\unit\meta\test_rg09_empirical_closure.py tests\python\integration\meta\test_run_rg09_gate.py"`
  - Result: `46 passed in 2.12s`
- `cmd.exe /c "cd /d C:\Users\Nalakram\Documents\GitHub\MarketMind && .venv-codex\Scripts\python.exe -m mypy --strict srcPy\meta\rg09_harness.py srcPy\meta\rg09_empirical_closure.py"`
  - Result: `Success: no issues found in 2 source files`
- `git diff -- docs/rg09/rg09_pilot_config_v1.json`
  - Result: empty
- `cmd.exe /c "cd /d C:\Users\Nalakram\Documents\GitHub\MarketMind && .venv-codex\Scripts\python.exe -m scripts.run_rg09_gate --fixture fixtures\rg09\v2\rg09_fixture_v2.parquet --fixture-summary fixtures\rg09\v2\rg09_fixture_summary.json --fixture-metadata fixtures\rg09\v2\rg09_fixture_metadata.json --config docs\rg09\rg09_pilot_config_v1.json --output-dir runs\rg09_v2\h1_v2bocpd_directional_nme"`
  - Result: `gate_executed=true`, `decision=NEEDS_MORE_EVIDENCE`, `fail_codes=[]`, `successor_hypotheses.eligible=true`
- `cmd.exe /c "cd /d C:\Users\Nalakram\Documents\GitHub\MarketMind && .venv-codex\Scripts\python.exe -m scripts.run_rg09_empirical_closure --fixture fixtures\rg09\v2\rg09_fixture_v2.parquet --fixture-summary fixtures\rg09\v2\rg09_fixture_summary.json --fixture-metadata fixtures\rg09\v2\rg09_fixture_metadata.json --config docs\rg09\rg09_pilot_config_v1.json --output-dir runs\rg09_v2\empirical_v2bocpd_directional_nme"`
  - Result: artifacts emitted with `base_decision=NEEDS_MORE_EVIDENCE`, `supports_non_exchangeability=inconclusive`, `fail_closed=false`

Linked trace path:
- `docs/traces/4.18.14_implementation_trace.md`

Linked manifest path:
- `docs/manifests/4.18.14_change_manifest.json`

## Version 4.18.13 (2026-04-02) — OI-52 RG-09 Uniform Statistic Closeout (Stage 3)

Version: **4.18.13** (**PATCH**)

Summary:
Close **OI-52** with the narrow Stage 3 follow-up: keep the Stage 1 null-generator recomputation baseline and the Stage 2 separability statistic, but use that separability statistic uniformly across all three authorized null families instead of falling back to `abs(mean(adaptation_gain))` for `shuffled_label` and `matched_exchangeable_window`. This removes the last permutation-invariant statistical defect. The governed rerun at `runs/rg09_v2/h1_v2bocpd_uniform_stat/` now has non-degenerate null distributions for all three families and records the first valid H1 artifact. Its then-current `FAIL_KILL` interpretation was later superseded by the `4.18.14` directional-underpowered decision correction.

Major changes:
- `srcPy/meta/rg09_harness.py`: `_statistic_for_family` now returns `_regime_separability_statistic(episodes)` unconditionally for all authorized null families.
- `tests/python/unit/meta/test_rg09_harness.py`: add RED/GREEN coverage that `shuffled_label` and `matched_exchangeable_window` null draws are non-constant under the shared separability statistic, and update the dispatch test to require uniform behavior.
- `docs/rg09/rg09_gate_spec.md`: document the uniform separability statistic across all three families and update the `RG09-V14` wording accordingly.
- `docs/src/ThresholdGovernanceRegister.md`: align `THR-RG09-V15` so it governs the shared statistical-lane denominator floor rather than a `shuffled_regime`-only consumer.
- `docs/src/ResolutionLedger.md`: close **OI-52** and update **RG-09** to point at the valid governed H1 artifact; later interpretation refined in `4.18.14`.
- Fresh rerun:
  - `runs/rg09_v2/h1_v2bocpd_uniform_stat/rg09_gate_result.json`

Breaking changes:
- None.

Validation summary:
- `cmd.exe /c "cd /d C:\Users\Nalakram\Documents\GitHub\MarketMind && .venv-codex\Scripts\python.exe -m pytest --no-cov tests\python\unit\meta\test_rg09_harness.py tests\python\unit\meta\test_rg09_empirical_closure.py tests\python\integration\meta\test_run_rg09_gate.py"`
  - Result: `44 passed in 1.98s`
- `cmd.exe /c "cd /d C:\Users\Nalakram\Documents\GitHub\MarketMind && .venv-codex\Scripts\python.exe -m mypy --strict srcPy\meta\rg09_harness.py srcPy\meta\rg09_empirical_closure.py"`
  - Result: `Success: no issues found in 2 source files`
- `git diff -- docs/rg09/rg09_pilot_config_v1.json`
  - Result: empty
- `cmd.exe /c "cd /d C:\Users\Nalakram\Documents\GitHub\MarketMind && .venv-codex\Scripts\python.exe -m scripts.run_rg09_gate --fixture fixtures\rg09\v2\rg09_fixture_v2.parquet --fixture-summary fixtures\rg09\v2\rg09_fixture_summary.json --fixture-metadata fixtures\rg09\v2\rg09_fixture_metadata.json --config docs\rg09\rg09_pilot_config_v1.json --output-dir runs\rg09_v2\h1_v2bocpd_uniform_stat"`
  - Result: `gate_executed=true`, non-degenerate null distributions for all families (`invalid_families=[]`); decision interpretation later superseded by `4.18.14`

Linked trace path:
- `docs/traces/4.18.13_implementation_trace.md`

Linked manifest path:
- `docs/manifests/4.18.13_change_manifest.json`

## Version 4.18.12 (2026-04-02) — OI-52 RG-09 Family-Specific Statistic Fix (Stage 2)

Version: **4.18.12** (**PATCH**)

Summary:
Continue **OI-52** with the narrow Stage 2 follow-up: keep the Stage 1 null-invalidity semantics and null-generator recomputation baseline, but make the `shuffled_regime` null family use a regime-sensitive separability statistic instead of `abs(mean(adaptation_gain))`. Register the new denominator-floor assumption as **RG09-V14** and **THR-RG09-V15**, rerun H1 and empirical closure into fresh directories, and record the actual governed outcome. The rerun clears `shuffled_regime` degeneracy, but **does not close OI-52** because `shuffled_label` and `matched_exchangeable_window` remain machine-epsilon degenerate on the governed v2 fixture; H1 therefore still emits `gate_executed=true`, `decision=null`, `fail_codes=[FAIL_NULL_DISTRIBUTION_INVALID]`, and empirical closure remains `inconclusive`.

Major changes:
- `srcPy/meta/rg09_harness.py`: add `REGIME_SEPARABILITY_DENOMINATOR_FLOOR`, `_regime_separability_statistic`, and `_statistic_for_family`; dispatch the statistical lane by null family inside `_evaluate_fold`.
- `tests/python/unit/meta/test_rg09_harness.py`: add Stage 2 RED/GREEN coverage for the new shuffled-regime statistic and update the null-invalidity regression to force collapse from `shuffled_label` rather than a structured shuffled-regime fold.
- `docs/rg09/rg09_gate_spec.md`: document the family-specific statistical lane and add governed assumption **RG09-V14**.
- `docs/src/ThresholdGovernanceRegister.md`: add provisional threshold row **THR-RG09-V15** for the `1e-9` denominator floor.
- `docs/src/ResolutionLedger.md`: keep **OI-52** open and update **RG-09** with the new rerun paths and the remaining invalid families.
- Fresh reruns:
  - `runs/rg09_v2/h1_v2bocpd_regime_stat/rg09_gate_result.json`
  - `runs/rg09_v2/empirical_v2bocpd_regime_stat/rg09_empirical_summary.json`

Breaking changes:
- None.

Validation summary:
- `cmd.exe /c "cd /d C:\Users\Nalakram\Documents\GitHub\MarketMind && .venv-codex\Scripts\python.exe -m pytest --no-cov tests\python\unit\meta\test_rg09_harness.py tests\python\unit\meta\test_rg09_empirical_closure.py tests\python\integration\meta\test_run_rg09_gate.py"`
  - Result: `42 passed in 1.98s`
- `cmd.exe /c "cd /d C:\Users\Nalakram\Documents\GitHub\MarketMind && .venv-codex\Scripts\python.exe -m mypy --strict srcPy\meta\rg09_harness.py srcPy\meta\rg09_empirical_closure.py"`
  - Result: `Success: no issues found in 2 source files`
- `git diff -- docs/rg09/rg09_pilot_config_v1.json`
  - Result: empty
- `cmd.exe /c "cd /d C:\Users\Nalakram\Documents\GitHub\MarketMind && .venv-codex\Scripts\python.exe -m scripts.run_rg09_gate --fixture fixtures\rg09\v2\rg09_fixture_v2.parquet --fixture-summary fixtures\rg09\v2\rg09_fixture_summary.json --fixture-metadata fixtures\rg09\v2\rg09_fixture_metadata.json --config docs\rg09\rg09_pilot_config_v1.json --output-dir runs\rg09_v2\h1_v2bocpd_regime_stat"`
  - Result: `gate_executed=true`, `decision=null`, `fail_codes=[FAIL_NULL_DISTRIBUTION_INVALID]`; invalid families remain `shuffled_label`, `matched_exchangeable_window`
- `cmd.exe /c "cd /d C:\Users\Nalakram\Documents\GitHub\MarketMind && .venv-codex\Scripts\python.exe -m scripts.run_rg09_empirical_closure --fixture fixtures\rg09\v2\rg09_fixture_v2.parquet --fixture-summary fixtures\rg09\v2\rg09_fixture_summary.json --fixture-metadata fixtures\rg09\v2\rg09_fixture_metadata.json --config docs\rg09\rg09_pilot_config_v1.json --output-dir runs\rg09_v2\empirical_v2bocpd_regime_stat"`
  - Result: artifacts emitted with `base_decision=null`, `supports_non_exchangeability=inconclusive`, `fail_closed=true`; CLI exited `1` by design

Linked trace path:
- `docs/traces/4.18.12_implementation_trace.md`

Linked manifest path:
- `docs/manifests/4.18.12_change_manifest.json`

## Version 4.18.11 (2026-04-02) — OI-52 RG-09 Null-Distribution Invalidity Correction (Stage 1)

## Version 4.18.11 (2026-04-02) — OI-52 RG-09 Null-Distribution Invalidity Correction (Stage 1)

Version: **4.18.11** (**PATCH**)

Summary:
Open **OI-52** and deliver the Stage 1 RG-09 correction pass: recompute null-generator derived episode statistics from mutated payloads, preserve `gate_executed=true` when evaluation ran but the statistical evidence surface invalidated itself, and rerun H1 / empirical closure into fresh directories without changing the pilot config, fixture inputs, thresholds, or governed statistical metric. The prior `2026-04-02` `FAIL_KILL` interpretation from `runs/rg09_v2/h1_v2bocpd/` is now invalidated as defective evidence, not accepted as a governed RG-09 finding.

Major changes:
- `srcPy/meta/rg09_nulls.py`: recompute `support_mean`, `query_mean`, and `adaptation_gain` after null-family mutation.
- `srcPy/meta/rg09_harness.py`: add `FAIL_NULL_DISTRIBUTION_INVALID`; emit `gate_executed=true` with `decision=null` for degenerate null distributions; record `distinct_draw_count`, `null_min`, `null_max`, and `null_range`.
- `srcPy/meta/rg09_empirical_closure.py`: map null-invalid base runs to `supports_non_exchangeability=inconclusive`.
- `docs/rg09/rg09_gate_spec.md`: correction to fail-code and `gate_executed` semantics.
- `docs/src/ResolutionLedger.md`: open **OI-52**, keep **OI-51** fixture-scoped, and update **RG-09** correction text.
- Fresh reruns:
  - `runs/rg09_v2/h1_v2bocpd_fix/rg09_gate_result.json`
  - `runs/rg09_v2/empirical_v2bocpd_fix/rg09_empirical_summary.json`

Breaking changes:
- None.

Validation summary:
- `cmd.exe /c "cd /d C:\Users\Nalakram\Documents\GitHub\MarketMind && .venv-codex\Scripts\python.exe -m pytest --no-cov tests\python\unit\meta\test_rg09_harness.py tests\python\unit\meta\test_rg09_empirical_closure.py tests\python\integration\meta\test_run_rg09_gate.py"`
  - Result: `40 passed in 1.89s`
- `cmd.exe /c "cd /d C:\Users\Nalakram\Documents\GitHub\MarketMind && .venv-codex\Scripts\python.exe -m mypy --strict srcPy\meta\rg09_nulls.py srcPy\meta\rg09_harness.py srcPy\meta\rg09_empirical_closure.py"`
  - Result: `Success: no issues found in 3 source files`
- `cmd.exe /c "cd /d C:\Users\Nalakram\Documents\GitHub\MarketMind && .venv-codex\Scripts\python.exe -m scripts.run_rg09_gate --fixture fixtures\rg09\v2\rg09_fixture_v2.parquet --fixture-summary fixtures\rg09\v2\rg09_fixture_summary.json --fixture-metadata fixtures\rg09\v2\rg09_fixture_metadata.json --config docs\rg09\rg09_pilot_config_v1.json --output-dir runs\rg09_v2\h1_v2bocpd_fix"`
  - Result: `gate_executed=true`, `decision=null`, `fail_codes=[FAIL_NULL_DISTRIBUTION_INVALID]`
- `cmd.exe /c "cd /d C:\Users\Nalakram\Documents\GitHub\MarketMind && .venv-codex\Scripts\python.exe -m scripts.run_rg09_empirical_closure --fixture fixtures\rg09\v2\rg09_fixture_v2.parquet --fixture-summary fixtures\rg09\v2\rg09_fixture_summary.json --fixture-metadata fixtures\rg09\v2\rg09_fixture_metadata.json --config docs\rg09\rg09_pilot_config_v1.json --output-dir runs\rg09_v2\empirical_v2bocpd_fix"`
  - Result: emitted corrected research artifacts with `supports_non_exchangeability=inconclusive`; CLI exited `1` because `fail_closed=true`

Linked artifact paths:
- `docs/traces/4.18.11_implementation_trace.md`
- `docs/manifests/4.18.11_change_manifest.json`
- `docs/releases/4.18.11.yml`

## Version 4.18.10 (2026-04-02) — OI-51 RG-09 v2 Regeneration (BOCPD v2 + Uniform Calendar Index)

Version: **4.18.10** (**PATCH**)

Summary:
Close **OI-51**: regenerate official `fixtures/rg09/v2/` from frozen `data/rg09/*.parquet` using `docs/rg09/rg09_bocpd_fixture_config_v2.json` and corrected `docs/rg09/rg09_multi_fixture_manifest_v2.json` (`uniform_calendar_day_index=true`). Determinism validated across two independent output directories (`fixtures/rg09/v2/`, `fixtures/rg09/v2_tmp_check/`) with identical fixture SHA. H1 gate now executes under unchanged pilot config with non-null decision: `gate_executed=true`, `decision=FAIL_KILL`, `fail_codes=[FAIL_EXCHANGEABLE_TASKS]`. Empirical closure completed at `runs/rg09_v2/empirical_v2bocpd/` with `supports_non_exchangeability=does_not_support_non_exchangeability`.

Major changes:
- `docs/rg09/rg09_multi_fixture_manifest_v2.json`: set `uniform_calendar_day_index=true` and document weekend/holiday-gap rationale.
- Regenerated fixture bundle: `fixtures/rg09/v2/rg09_fixture_v2.parquet` + sidecars (`fixture_sha256` `sha256:34d367c6a1d0bbe5384c66c2d8cfd32090d3ad5a99ea6847b6468ff69d9de958`).
- Determinism check run: `fixtures/rg09/v2_tmp_check/` (matching SHA).
- Harness output: `runs/rg09_v2/h1_v2bocpd/rg09_gate_result.json`.
- Empirical closure output: `runs/rg09_v2/empirical_v2bocpd/rg09_empirical_summary.json`.
- `docs/src/ResolutionLedger.md`: OI-51 opened/closed; RG-09 resolution text updated.

Breaking changes:
- None.

Validation summary:
- `git diff -- docs/rg09/rg09_pilot_config_v1.json` (empty)
- `python -m scripts.generate_rg09_fixture --multi-manifest docs/rg09/rg09_multi_fixture_manifest_v2.json --config docs/rg09/rg09_bocpd_fixture_config_v2.json --output-dir fixtures/rg09/v2/`
- `python -m scripts.generate_rg09_fixture --multi-manifest docs/rg09/rg09_multi_fixture_manifest_v2.json --config docs/rg09/rg09_bocpd_fixture_config_v2.json --output-dir fixtures/rg09/v2_tmp_check/`
- `python -m scripts.run_rg09_gate --fixture fixtures/rg09/v2/rg09_fixture_v2.parquet --fixture-summary fixtures/rg09/v2/rg09_fixture_summary.json --fixture-metadata fixtures/rg09/v2/rg09_fixture_metadata.json --config docs/rg09/rg09_pilot_config_v1.json --output-dir runs/rg09_v2/h1_v2bocpd/`
- `python -m scripts.run_rg09_empirical_closure --fixture fixtures/rg09/v2/rg09_fixture_v2.parquet --fixture-summary fixtures/rg09/v2/rg09_fixture_summary.json --fixture-metadata fixtures/rg09/v2/rg09_fixture_metadata.json --config docs/rg09/rg09_pilot_config_v1.json --output-dir runs/rg09_v2/empirical_v2bocpd/`

Linked release manifest path:
- `docs/releases/4.18.10.yml`

## Version 4.18.9 (2026-04-01) — OI-50 RG-09 Multi-Instrument yfinance Data & v2 Fixture

Version: **4.18.9** (**PATCH**)

Summary:
Close **OI-50**: governed yfinance download script (`scripts/download_rg09_market_data.py`), frozen per-instrument parquets under `data/rg09/`, `docs/rg09/rg09_data_acquisition_log.md`, `docs/rg09/rg09_multi_fixture_manifest_v2.json` (eight futures proxies). Extend `scripts/generate_rg09_fixture.py` with `MultiManifestSettings`: `calendar_overlap_policy: independent_instruments`, optional `apply_diversification_perturbation`, and deterministic timestamp staggering for multi-instrument rows. Official `fixtures/rg09/v2/` bundle; harness run `runs/rg09_v2/h1/`; empirical closure `runs/rg09_v2/empirical/`. Pilot and BOCPD fixture configs unchanged. **Gate outcome:** `gate_executed=false`, `FAIL_INSUFFICIENT_EPISODES` (thresholds not tuned). Companion sync **6.4.29** / Resolution Ledger **1.0.25** / README **4.18.9**.

Major changes:
- `scripts/download_rg09_market_data.py`, `tests/python/unit/scripts/test_download_rg09_market_data.py`
- `scripts/generate_rg09_fixture.py` (`MultiManifestSettings`, `stagger_multi_instrument_timestamps`)
- `data/rg09/*.parquet`, `data/rg09/rg09_download_manifest.json`
- `docs/rg09/rg09_multi_fixture_manifest_v2.json`, `docs/rg09/rg09_data_acquisition_log.md`
- `docs/src/ResolutionLedger.md` **OI-50**; RG-09 resolution; `docs/src/README.md`, `docs/src/ImplementationPlan.md`
- `docs/releases/4.18.9.yml`, `docs/traces/4.18.9_implementation_trace.md`, `docs/manifests/4.18.9_change_manifest.json`

Breaking changes:
- None.

Validation summary:
- `pytest tests/python/unit/meta/test_generate_rg09_fixture.py tests/python/unit/scripts/test_download_rg09_market_data.py --no-cov`
- `python -m scripts.download_rg09_market_data` (network); `python -m scripts.generate_rg09_fixture --multi-manifest docs/rg09/rg09_multi_fixture_manifest_v2.json ...`
- `git diff --exit-code docs/rg09/rg09_pilot_config_v1.json` (empty)

Linked trace path:
- `docs/traces/4.18.9_implementation_trace.md`

Linked manifest path:
- `docs/manifests/4.18.9_change_manifest.json`

## Version 4.18.8 (2026-04-01) — OI-47 RG-09 Multi-Ticker Replay Fixture v2

Version: **4.18.8** (**PATCH**)

Summary:
Close **OI-47**: multi-ticker RG-09 replay fixture v2 at `fixtures/rg09/v2/rg09_fixture_v2.parquet` with companion sidecars (fixture_sha256 `sha256:6daf760e571cd8d7172a98182bbcbd2953e761dcdca80f76360e9ae68828f419`; basket ES, NQ, RTY, YM per manifest). Extend `scripts/generate_rg09_fixture.py` with multi-segment generation; add unit tests and `tests/python/integration/meta/test_rg09_v2_fixture.py`. Empirical closure under unchanged `docs/rg09/rg09_pilot_config_v1.json` records `gate_executed=false` with `FAIL_INSUFFICIENT_EPISODES` and `FAIL_NONREPRODUCIBLE` (documented in ledger — no pilot threshold changes). Companion documents synced to **6.4.28** / Resolution Ledger **1.0.24** / README **4.18.8**.

Major changes:
- `scripts/generate_rg09_fixture.py`, `tests/python/unit/meta/test_generate_rg09_fixture.py`, `tests/python/integration/meta/test_rg09_v2_fixture.py`
- `fixtures/rg09/v2/` parquet + sidecars
- `docs/src/ResolutionLedger.md`: **OI-47**; **RG-09** resolution updated
- `docs/src/README.md`, `docs/src/ImplementationPlan.md`, `docs/releases/4.18.8.yml`
- `docs/traces/4.18.8_implementation_trace.md`, `docs/manifests/4.18.8_change_manifest.json`

Breaking changes:
- None.

Validation summary:
- `pytest tests/python/unit/meta/test_generate_rg09_fixture.py tests/python/integration/meta/test_rg09_v2_fixture.py --no-cov`

Linked trace path:
- `docs/traces/4.18.8_implementation_trace.md`

Linked manifest path:
- `docs/manifests/4.18.8_change_manifest.json`

## Version 4.18.7 (2026-04-01) — RG09-V13 task_id HMAC Key Assumption & MLN-01 Governance

Version: **4.18.7** (**PATCH**)

Summary:
Governed assumption **RG09-V13** records the MetaTask `task_id` HMAC **key** contract (scaffold: empty-key HMAC; message-only entropy; **⚑ VALIDATE** — any key change invalidates all historical `task_id` values). **MLN-01** acceptance criteria extended to require explicit key resolution before the normative `task_manifest.json` contract locks. `docs/rg09/rg09_gate_spec.md` Section 4 register extended to **RG09-V13**. `compute_task_id()` documents **RG09-V13** and MLN-01. Companion documents synced to **6.4.27** / Resolution Ledger **1.0.23**.

Major changes:
- `srcPy/meta/task_manifest_emitter.py`: `compute_task_id` governing docstring + RG09-V13 inline note
- `docs/rg09/rg09_gate_spec.md`: assumptions register row **RG09-V13**
- `docs/src/ResolutionLedger.md`: **MLN-01** acceptance criteria; ledger **1.0.23**; RG-09 resolution text **RG09-V01**–**RG09-V13**
- `docs/src/ImplementationPlan.md` **6.4.27**, `docs/src/README.md`, `docs/src/task_validity_pilot_report.md`
- `docs/traces/4.18.7_implementation_trace.md`, `docs/manifests/4.18.7_change_manifest.json`, `docs/releases/4.18.7.yml`

Breaking changes:
- None (documentation and governance record; HMAC implementation unchanged).

Validation summary:
- `mypy --strict` on `srcPy/meta/task_manifest_emitter.py`; `pytest` on `tests/python/unit/meta/test_task_manifest_emitter.py` (optional subset).

Linked trace path:
- `docs/traces/4.18.7_implementation_trace.md`

Linked manifest path:
- `docs/manifests/4.18.7_change_manifest.json`

## Version 4.18.6 (2026-04-01) — Phase II-0B Artifact & Contract Scaffolding

Version: **4.18.6** (**PATCH**)

Summary:
Non-promotable Phase II scaffold emitters for governed artifact surfaces (`task_manifest.json`, `meta_validity_report.json`, `execution_assumptions.json`), centralized seed/run identity for Phase II ML runs, early `meta_learner_scaffold` gate shell (always `SCAFFOLD_INCOMPLETE`), and Threshold Governance Register migration for `docs/rg09/rg09_pilot_config_v1.json`. Opens **OI-48** (Harvey field naming: contract vs Appendix B.1) and **OI-49** (`execution_assumptions.json` vs Appendix B gap) for pre-MLN-06 reconciliation.

Major changes:
- `srcPy/meta/task_manifest_emitter.py`, `meta_validity_emitter.py`, `execution_assumptions_emitter.py`, `seed_policy.py`, `rg09_threshold_catalog.py`
- `marketmind_gate/gates/meta_learner_scaffold.py`
- `docs/rg09/rg09_pilot_config_v1.json`: threshold_id-wrapped pilot thresholds; `load_rg09_config` accepts legacy bare scalars
- `docs/src/ResolutionLedger.md`: **OI-48**, **OI-49** opened; ledger **1.0.22** (Markdown source)
- `docs/releases/4.18.6.yml`

Breaking changes:
- None (scaffold and RG-09 config remain non-promotable / backward-compatible for harness tests using bare numeric thresholds).

Validation summary:
- Unit tests for new modules; `mypy --strict` on touched modules; `pytest` subsets with `--no-cov` as needed for local runs.

## Version 4.18.5 (2026-04-01) — RG-09 Empirical Meta-Validity AC Patch & OI-39 Closure

Version: **4.18.5** (**PATCH**)

Summary:
Align `meta_validity_report_research.json` with Appendix B.1 research-scaffold expectations: `inner_loop_gain_harvey_t` is always unavailable in the II-0 empirical lane; IC-based Harvey t is emitted under `ic_harvey_t`; `overall_result` is the fixed research sentinel; non-exchangeability state is preserved under `overall_conclusion_research`; add explicit `unavailable` stubs for encoder clustering, proxy IC correlation, forgetting delta, confidence ECE, net allocation Sharpe, and `signal_set_version` when absent from the fixture summary. Rename `projection_rule_text` to `projection_rule_version` in `rg09_empirical_summary.json` and align `reference_condition` with `diag_regime_class_bocpd_gated`. Close **OI-39** in the Resolution Ledger (paper-trading simulation requirements satisfied by `paper_trade_sim_spec.md`).

Major changes:
- `srcPy/meta/rg09_empirical_closure.py`: meta validity and empirical summary field fixes.
- `docs/src/ResolutionLedger.md`: **OI-39** `CLOSED` at v4.18.5; ledger bumped to **1.0.21**.
- `docs/src/ImplementationPlan.md`: companion sync to **4.18.5** / **6.4.26** (OI-39 closed; RG-09 empirical lane meta scaffold updated; RG-09 remains PARTIAL).
- `docs/src/README.md`: companion stamps aligned to 4.18.5; OI-39 closed and RG-09 empirical lane wording updated.
- Full companion Markdown + DOCX suite for **4.18.5**: `docs/releases/4.18.5.yml`; built outputs under `docs/out/4.18.5/` (FormattingSpec **1.0.4**, README **4.18.5**, Implementation Plan **6.4.26**, Technical Roadmap **1.4.21**, Meta-Learning Core **1.2.19**, Architecture Vision **1.2.20**, Resolution Ledger **1.0.21**, White Paper **2.2.12**); stale **OI-39** / pre-**1.0.21** companion references scrubbed in bumped sources.

Breaking changes:
- None (research / non-promotable scaffold; `schema_version` unchanged).

Validation summary:
- Unit and integration tests for RG-09 empirical closure; strict mypy on `rg09_empirical_closure.py`.
- Implementation Trace and Change Manifest recorded per Artifact Write Contract (`docs/Artifact Write Contract.md`).
- `python -m devtools.docs.cli validate-manifest --version 4.18.5`; `build-docx-suite` + `verify-suite` for **4.18.5** passed.

Linked trace path:
- `docs/traces/4.18.5_implementation_trace.md`

Linked manifest path:
- `docs/manifests/4.18.5_change_manifest.json`

## Version 4.18.4 (2026-04-01) — docs/out Implementation Metadata Packaging

Version: **4.18.4** (**PATCH**)

Summary:
Add versioned `implementation_manifest.json` and `implementation_plan.md` files to the matching `docs/out/4.18.2/` and `docs/out/4.18.3/` release directories.

Major changes:
- Added `docs/out/4.18.2/implementation_manifest.json` and `docs/out/4.18.2/implementation_plan.md`.
- Added `docs/out/4.18.3/implementation_manifest.json` and `docs/out/4.18.3/implementation_plan.md`.

Breaking changes:
- None.

Validation summary:
- Confirmed the four new files exist under the expected `docs/out` version directories.

Linked trace path:
- `docs/traces/4.18.4_implementation_trace.md`

Linked manifest path:
- `docs/manifests/4.18.4_change_manifest.json`

## Version 4.18.3 (2026-03-31) — Companion Sync After RG-09 II-0A Harness Closeout

Version: **4.18.3** (**PATCH**)

Summary:
Rebase the companion document suite onto the `4.18.2` RG-09 II-0A harness closeout so the current-state narrative and release stamps no longer describe the bounded II-0A harness/gate path as still pending.

Major changes:
- Updated `docs/src/README.md`, `docs/src/ImplementationPlan.md`, and `docs/src/WhitePaper.md` to reference the `4.18.2` harness baseline and keep RG-09 empirical closure explicitly open.
- Added `docs/releases/4.18.3.yml` for the companion-doc patch.

Breaking changes:
- None.

Validation summary:
- Documentation sync only; no runtime code changed.
- Release summary derived from `docs/traces/4.18.3_implementation_trace.md` and machine-readable deltas recorded in `docs/manifests/4.18.3_change_manifest.json`.

Linked trace path:
- `docs/traces/4.18.3_implementation_trace.md`

Linked manifest path:
- `docs/manifests/4.18.3_change_manifest.json`

## Version 4.18.2 (2026-03-31) — RG-09 II-0A Harness Closeout

Version: **4.18.2** (**PATCH**)

Summary:
Deliver the RG-09 II-0A bounded gate path against the governed replay-fixture baseline and close the implementation thread with versioned execution records.

Major changes:
- Added the RG-09 base harness, deterministic null-evidence path, artifact emission layer, and CLI entrypoint.
- Replaced placeholder gate behavior with governed precondition handling, fold-aware evidence aggregation, and run-derived machine-manifest emission.
- Removed the invalid `srcPy.__init__` runtime shim so the RG-09 strict-mypy surface passes without package import-time hacks.

Breaking changes:
- None.

Validation summary:
- `python -m pytest --strict-markers --no-cov tests/python/unit/meta/test_rg09_harness.py tests/python/integration/meta/test_run_rg09_gate.py` → `28 passed in 1.24s`
- `python -m mypy --strict srcPy/__init__.py srcPy/meta/rg09_harness.py srcPy/meta/rg09_artifacts.py srcPy/meta/rg09_nulls.py tests/python/unit/meta/test_rg09_harness.py tests/python/integration/meta/test_run_rg09_gate.py` → `Success: no issues found in 6 source files`

Linked trace path:
- `docs/traces/4.18.2_implementation_trace.md`

Linked manifest path:
- `docs/manifests/4.18.2_change_manifest.json`

## Version 4.18.1 (2026-03-30) — OI-43 Closure: RG-09 Replay Fixture Production

This is a PATCH release. It closes the remaining OI-43 implementation scope by emitting the governed RG-09 replay fixture, correcting the canonical replay label mapping, and recording the closure in the ledger.

### Detailed Changes

| Area | Change |
|------|--------|
| `srcPy/meta/bocpd_service.py` | `RegimeLabelRecord` now carries explicit `regime_id` and preserves `regime_label` as the canonical service label rather than backfilling from additive `regime_class`; `BOCPDRegimeService.update()` emits the corrected field semantics. |
| `scripts/generate_rg09_fixture.py` | Generator now writes the fixture parquet with the intended field sourcing (`regime_id`, `regime_label`, `regime_class` distinct), deterministic canonical fixture hashing over the declared canonical subset, atomic artifact writes, fail-closed precondition checks, and the governed summary/metadata contracts. |
| `tests/python/unit/meta/test_generate_rg09_fixture.py`, `tests/python/unit/meta/test_bocpd_service.py` | Added direct contract coverage for fixture field semantics and an explicit assertion that `regime_label` is not backfilled from `regime_class`. |
| `fixtures/rg09/v1/rg09_fixture_v1.parquet`, `fixtures/rg09/v1/rg09_fixture_summary.json`, `fixtures/rg09/v1/rg09_fixture_metadata.json` | Regenerated governed ES replay fixture artifacts. Corrected fixture SHA: `sha256:3ba47a1ef9445f1694c411151219bd2935f2d6b1b075e33a6c5fe13f903c4553`. |
| `docs/src/ResolutionLedger.md` | **MRL 1.0.19 → 1.0.20**. OI-43 marked CLOSED, artifact path recorded, OI count matrix updated, blocking hotlist cleared of OI-43, and RG-09 resolution text updated to state that the replay fixture dependency is satisfied. |
| `docs/releases/4.18.1.yml` | Added release manifest for the OI-43 closure patch. |

### Behavioral Changes

- The emitted RG-09 replay fixture now preserves canonical label semantics in the parquet contract:
  `regime_id` = canonical compositional label,
  `regime_label` = canonical service label,
  `regime_class` = additive non-canonical 5-class projection.
- RG-09 Phase II-0A is no longer blocked on replay fixture production; remaining RG-09 work is the II-0A code/gate path, not fixture availability.

### Breaking Changes

- The canonical replay fixture hash changed because `regime_label` now reflects the canonical service label rather than the additive `regime_class`. Older `fixtures/rg09/v1/*` outputs are superseded by the v4.18.1 artifacts.

### Test / Validation Evidence

- `cmd.exe /c %CD%\\.venv-codex\\Scripts\\python.exe -m pytest --strict-markers --no-cov tests\\python\\unit\\meta\\test_generate_rg09_fixture.py tests\\python\\unit\\meta\\test_bocpd_service.py tests\\python\\unit\\meta\\test_crisis_diagnostic.py tests\\python\\unit\\meta\\test_severity_diagnostic.py`
- `cmd.exe /c %CD%\\.venv-codex\\Scripts\\python.exe -m mypy --strict --follow-imports silent srcPy\\meta\\bocpd_service.py scripts\\generate_rg09_fixture.py tests\\python\\unit\\meta\\test_generate_rg09_fixture.py tests\\python\\unit\\meta\\test_bocpd_service.py`

## Version 4.18.0 (2026-03-30) — MLN-02-AMD-01: Crisis Redefinition (Severity Gate)

This is a MINOR release. **MLN-02-AMD-01** moves Level 2 `crisis` from `vol_hi AND bocpd_cp` to **`vol_hi AND severity_flag`**, where `severity_flag` is a PIT-safe expanding-window threshold on `vol_score_raw` (default **p90**, **RG09-V12**, not tuned on Anti-Goodhart holdouts). Level 1 compositional `regime_id` and BOCPD service semantics are unchanged; BOCPD is documented explicitly as a **segmentation** primitive, not a crisis primitive.

### Detailed Changes

| Area | Change |
|------|--------|
| `docs/src/MetaLearningArchitectureVision.md` | §4.2 crisis row, `severity_flag` definition, BOCPD contract note, historical-frequency ⚑ VALIDATE; edition **1.2.19**. |
| `docs/src/ResolutionLedger.md` | **MRL 1.0.19**: MLN-02 acceptance criteria + resolution text; **OI-44** / **OI-45** (DIAG-001 / DIAG-002) CLOSED; OI count matrix. |
| `docs/rg09/rg09_gate_spec.md` | **RG09-V12** assumption row (`crisis_vol_score_percentile`). |
| `docs/src/README.md`, `ImplementationPlan.md`, `TechnicalRoadmap.md`, `MetaLearningCore.md`, `docs/src/WhitePaper.md`, root `README.md` | Companion suite stamps → **4.18.0** / **6.4.23** / **1.4.20** / **1.2.18** / **1.2.19** / **1.0.19**; White Paper **v2.2.9**. |
| `docs/src/task_validity_pilot_report.md` | Open-assumption wording to **RG09-V01–V12**; cross-reference table adds **RG09-V12**. |
| `srcPy/meta/regime_config.py` | `crisis_vol_score_percentile` (default 90); `config_version` **rg09_v1.0.2**. |
| `srcPy/meta/regime_labeler.py` | `compute_severity_flag_vol_score_raw`; `project_regime_class(..., severity_flag=...)`; `project_regime_class_bocpd_gated_reference` for pilot baseline. |
| `srcPy/meta/bocpd_service.py` | `RegimeLabelRecord.diag_regime_class_bocpd_gated`; canonical `regime_class` uses severity gate. |
| `schemas/rg09_fixture_config.schema.json`, `docs/rg09/rg09_bocpd_fixture_config_v1.json` | Optional `crisis_vol_score_percentile`; fixture config version **rg09_v1.0.2**. |
| `tests/python/unit/meta/test_regime_labeler.py`, `test_regime_config.py`, `test_crisis_diagnostic.py`, `test_bocpd_service.py` | Coverage for new projection, PIT-safe severity, diagnostics. |
| `docs/releases/4.18.0.yml` | Release manifest for companion DOCX build. |

### Behavioral Changes

- **5-class `regime_class` from `BOCPDRegimeService.update`:** `crisis` no longer requires `bocpd_cp`; it requires **high volatility bucket** plus **severity_flag** from past-only expanding percentile of `vol_score_raw`.
- **Replay/diagnostics:** each record adds **`diag_regime_class_bocpd_gated`** preserving the pre-amendment rule for Phase II-0A side-by-side comparison (`diag_regime_class_extended` remains RG09-DIAG-001 ablation).

### Breaking Changes

- Call sites of `RegimeLabeler.project_regime_class` must pass **`severity_flag`** (keyword-only). Fixture config hash changes when `crisis_vol_score_percentile` or `config_version` is material to `BOCPDConfig.content_hash()`.

### Test / Validation Evidence

- `pytest tests/python/unit/meta/test_regime_labeler.py tests/python/unit/meta/test_regime_config.py tests/python/unit/meta/test_crisis_diagnostic.py tests/python/unit/meta/test_bocpd_service.py -q --no-cov`
- `mypy srcPy/meta/regime_labeler.py srcPy/meta/regime_config.py srcPy/meta/bocpd_service.py`

## Version 4.17.1 (2026-03-29) — RG-09 RG09-DIAG-002: Severity-Stratified High-Vol Diagnostic

This is a PATCH release. Standalone measurement tooling only; no changes to governed regime contracts, BOCPD core, or existing fixture parquet column sets.

### Detailed Changes

| Area | Change |
|------|--------|
| `scripts/rg09_severity_diagnostic.py` | New CLI (`python -m scripts.rg09_severity_diagnostic`): discovers `rg09_fixture_v1.parquet` under a basket directory; extracts contiguous `high_vol` episodes after cold-start exclusion; PIT-safe expanding-window percentile thresholds on `vol_score_raw` (history strictly before episode start); per-episode peak/mean log-RV and constructibility vs `MetaTaskSizingParams.l_min`; Cohen's d on per-episode mean `trend_score_raw`; cross-entity dedup of crisis-grade episode start dates via `scripts.run_rg09_basket._deduplicate_crisis_events`; JSON report (`diagnostic_id` RG09-DIAG-002, `threshold_results`, `decision_table`). `--thresholds` accepts comma- or space-separated percentiles (e.g. `80,85,90,95` or `"80 85 90 95"`). |
| `tests/python/unit/meta/test_severity_diagnostic.py` | Unit coverage: episode extraction, PIT vs full-sample threshold, classification, Cohen's d edge cases, JSON sanitize, CLI smoke, dedup integration. |

### Behavioral Changes

- None to production runtime; diagnostic is opt-in analysis on existing basket outputs.

### Breaking Changes

None.

### Test / Validation Evidence

- Pass: `pytest tests/python/unit/meta/test_severity_diagnostic.py` (with `--cov=scripts.rg09_severity_diagnostic` for line/branch gate on the new script in local validation).

## Version 4.17.0 (2026-03-29) — MOM-020 Closure: Artifact-Driven Momentum Variant Comparison

This is a MINOR release. The governed momentum stack gains a new backward-compatible comparison capability: CSMOM, TSMOM, and dual-momentum bundles now compare through emitted child artifacts rather than a self-certifying parent scoring path.

### Major Themes Across All Changes

- Move CPCV scoring authority into child momentum bundles so the comparison layer no longer generates the evidence it later validates.
- Make cross-variant comparison artifact-driven: parent comparison reads, hash-checks, and aggregates child `cpcv_path_scores.json`, `stat_validity_report.json`, and `execution_assumptions.json` artifacts.
- Close MOM-020 on the governed path by emitting a parent-owned shared-PBO artifact and a reproducible comparison report derived only from bundle artifacts.

### Detailed Changes

| Area | Change |
|------|--------|
| `srcPy/strategies/momentum/entry.py` | Governed momentum child runs now emit `cpcv_path_scores.json` whenever the run is executing on the shared CPCV split surface, alongside the existing canonical `stat_validity_report.json` and `execution_assumptions.json` artifacts. The child bundle becomes the authoritative CPCV evaluation source for its own variant. |
| `srcPy/strategies/momentum/comparison.py` | `run_variant_comparison(...)` now loads child-owned `cpcv_path_scores.json`, `stat_validity_report.json`, and `execution_assumptions.json`; verifies split-surface and shared-cost identity; aggregates child `evaluations` into one shared CPCV surface; computes shared PBO from those emitted evaluations; emits `comparison_stat_validity.json`; and writes `momentum_variant_comparison_report.json` without recomputing child scores. |
| `tests/python/integration/strategies/test_momentum_variant_comparison.py` | Integration proof locks the governed comparison contract: child surfaces drive the expected evaluation set, parent shared PBO matches recomputation from aggregated child evaluations, ranking is derived from child summaries, hash-linked paths are correct, and child `stat_validity_report.json` remains unchanged (`pbo.method == "unavailable"`). |
| `tests/python/unit/strategies/momentum/test_comparison.py`, `tests/python/unit/strategies/momentum/test_entry.py` | Unit coverage hardens fail-closed behavior around missing or malformed child CPCV surfaces plus split/cost identity mismatches, and confirms child CPCV path-score emission on the governed path. |
| `docs/src/ResolutionLedger.md`, `docs/src/ImplementationPlan.md`, `docs/src/README.md` | Companion planning/ledger surfaces now describe MOM-020 as closed on the governed comparison lane and record the child-owned CPCV / parent-owned shared-PBO split explicitly. |

### Behavioral Changes

- Child momentum bundles, not the parent comparison layer, now own CPCV path scoring authority.
- The parent comparison layer is non-generative with respect to child evaluation surfaces: it aggregates emitted `evaluations` and validates shared split/cost identity before computing cross-variant PBO.
- `comparison_stat_validity.json` is now the parent-owned statistical-validity artifact for shared PBO across variants, while each child `stat_validity_report.json` remains immutable and local to that child run.
- `momentum_variant_comparison_report.json` is derived from persisted child summaries and aggregated evaluations only; there is no hidden recomputation path in the comparison report.

### Breaking Changes

None. Existing governed momentum child artifacts remain valid; this release adds a new comparison workflow and new parent comparison artifacts without intentionally breaking prior bundle consumers.

### Test / Validation Evidence

- Pass: `tests/python/integration/strategies/test_momentum_variant_comparison.py::test_run_variant_comparison_emits_parent_and_child_bundles`
  - Confirms parent `comparison_stat_validity.json` shared PBO equals canonical recomputation from the concatenated child `cpcv_path_scores.json` evaluation surface.
  - Confirms variant ranking is derived from child CPCV summaries.
  - Confirms child `stat_validity_report.json` is not rewritten by the parent comparison layer.
- Pass: `tests/python/unit/strategies/momentum/test_comparison.py`
  - Confirms fail-closed behavior for missing child CPCV artifacts, malformed child CPCV payloads, split-surface hash mismatch, and shared-cost hash mismatch.
- Pass: `tests/python/unit/strategies/momentum/test_entry.py`
  - Confirms governed child momentum runs emit `cpcv_path_scores.json` with variant, split-surface hash, shared-cost hash, and path-level evaluations on the CPCV path.

### Deferred

- Shared PBO currently lives in the parent comparison path rather than being emitted through the generic statistical validator module; this is a design follow-on, not a correctness blocker.
- No dedicated tamper-detection test exists yet for `comparison_stat_validity.json`; child artifact identity and parent recomputation coverage are present, but direct parent-artifact tamper coverage remains future hardening work.
- The child-vs-parent statistical-validity split is implemented and tested, but companion documentation may still need further narrative cleanup where older wording implied a more generative parent comparison role.

## Version 4.16.0 (2026-03-28) — Phase I-G Protocol Closure: Expansion Policy + Alt-Data Admissibility

This is a MINOR release. No runtime behavior, schemas, or public APIs change.

| Area | Change |
|------|--------|
| `docs/src/signal_universe_expansion_policy.md` | New policy document: expansion gate (Harvey t, DSR, PBO all required from same governed bundle); diversity gate and decay policy as promotion requirements; multiple-testing budget via RunRegistry; `signal_id` change = new candidate; Phase IV (IV-A/IV-B/IV-D) as serious expansion home; scope exclusions and identity loophole close-out. |
| `docs/src/alt_data_admissibility.md` | New policy document: PIT requirements (`available_at` distinct from `event_ts`, `DataView.as_of(T)` access, vintage preservation); provenance requirements; replay requirements (fixture is precondition not post-hoc); event-driven entry deferred to Phase IV; 7-step admissibility decision tree governing eligibility for governed evaluation runs only. |
| `docs/src/ResolutionLedger.md` | OI-37 and OI-38 closed. Count matrix: OI OPEN −2, CLOSED +2; ∑ OPEN −2, CLOSED +2. OI-40 `depends_on` no longer lists OI-38. **MRL 1.0.16 → 1.0.17**; title page companion stamps (Implementation Plan **6.4.21**, VERSION.md **4.16.0**). |
| `docs/src/ImplementationPlan.md` | §9 Priority Stack: OI-37 + OI-38 closed; core I-G protocol documents noted as complete; remaining I-G work (OI-39, RG-09 empirical closure) explicit. **6.4.20 → 6.4.21** (RECENT_CHANGES, SOURCE_STAMP, title page). §1.2 audit baseline advanced to **4.16.0**. Appendix A links to the two new policy documents. |

## Version 4.15.0 (2026-03-28) — Phase I-G Protocol Closure: Encoder Upgrade Criteria

This is a MINOR release. No runtime behavior, schemas, or public APIs change.

| Area | Change |
|------|--------|
| `docs/rg10/rg10_encoder_upgrade_criteria.md` | New policy document: D=64 governed baseline with literature grounding; three-surface upgrade trigger (within-regime cosine similarity, cross-regime separation ratio, silhouette score); INSUFFICIENT_DIAGNOSTIC_EVIDENCE state for small task pools; decision rules for all failure combinations; SNAIL explicitly deferred to Phase III; Harvey t narrow-pass band config-driven; all thresholds ⚑ VALIDATE. |
| `docs/src/ResolutionLedger.md` | AQ-01, AQ-02, RG-10 closed. Count matrix deltas: AQ OPEN −2, CLOSED +2; RG OPEN −1, CLOSED +1; ∑ OPEN −3, CLOSED +3 (column totals). **MRL 1.0.15 → 1.0.16**; title page companion stamps (Implementation Plan **6.4.20**, VERSION.md **4.15.0**). |
| `docs/src/ImplementationPlan.md` | §9 Priority Stack: RG-10 closed; OI-37 + OI-38 noted as next. **6.4.19 → 6.4.20** (RECENT_CHANGES, SOURCE_STAMP, title page). §1.2 audit baseline advanced to **4.15.0**. |

## Version 4.14.0 (2026-03-28) — Phase I-G Protocol Closure: RiskFn + Signal Generation

This is a MINOR release. No runtime behavior, schemas, or public APIs change.

| Area | Change |
|------|--------|
| `docs/src/risk_protocol.md` | Stub replaced with governed protocol: allocator output surface, Phase II permitted actions (confidence_scalar post-sizing attenuation; full abstention = confidence_scalar 0), II-D boundary (post-allocator conditioning explicitly out of RiskFn scope), phase scope table, auditability requirements, and ⚑ VALIDATE provisional thresholds. |
| `docs/src/signal_generation_protocol.md` | Stub replaced with governed protocol: current governed base (4 signals), admission requirements table, admission/promotion/retirement as three distinct states, signal identity contract (signal_id, slot_index, signal_set_version; historical slot_index reconstructibility rule), retirement procedure, alternative-data deferral to OI-38, breadth as Phase IV scope. |
| `docs/src/ResolutionLedger.md` | OI-35 and OI-36 closed. Count matrix: OI OPEN 11→9, CLOSED 29→31; ∑ OPEN 36→34, CLOSED 60→62. **MRL 1.0.14 → 1.0.15**; title page companion stamps (README **4.14.0**, Implementation Plan **6.4.19**). |
| `docs/src/ImplementationPlan.md` | §9 Priority Stack: OI-35 + OI-36 recorded as closed; RG-10 noted as next with AQ-01/AQ-02 dependency. **6.4.18 → 6.4.19** (RECENT_CHANGES, SOURCE_STAMP, title page). |
| `VERSION.md` | **4.x** version index condensed; section heading updated to ADR-007 hashing, Phase I PIT & closure, I-G protocols & governance. |

## Version 4.13.1 (2026-03-28) — Governance Patch: OI-43 and II-0A Entry Gate

This is a PATCH release. No protocol docs, code, schemas, or runtime behavior change.

| Area | Change |
|------|--------|
| ResolutionLedger.md | OI-43 opened: RG-09 replay fixture production, blocking YES, phase I-G, phase_links II-0A + MLC-0. Count matrix: OI OPEN 10→11, Total 41→42; ∑ OPEN 35→36, Total 123→124. |
| ResolutionLedger.md §1.2 | OI-43 added to blocking hotlist. |
| ResolutionLedger.md RG-09 | Resolution note updated: v4.14.0 entry gate explicitly blocked by OI-43. |
| ImplementationPlan.md §4.2 | II-0A entry gate dependency note added: no RG-09 code work may begin until OI-43 closes or live service output is available. |
| ImplementationPlan.md §9 | Immediate Priority Stack updated to reflect Phase I-F closure, RG-09 PARTIAL status, sequencing of remaining I-G items, MOM-020 as parallel empirical track, and II-0A blocked state. |

## Version 4.13.0 (2026-03-28) — Phase I-G RG-09 Protocol Closure

This is a MINOR release. No runtime behavior, schemas, or public APIs change.

| Area | Change |
|------|--------|
| `docs/rg09/rg09_gate_spec.md` | Published with four sections: definitions (four first-class objects, timing authority rule, exclusion code family), admissibility rules, gate specification (evidence sufficiency preconditions, three evidence kinds, three null comparisons with preservation rules, decision states, kill criteria, fail codes), and open assumptions register (RG09-V01 through RG09-V11). |
| `docs/rg09/rg09_pilot_config_v1.json` | Published as governed provisional config artifact for all II-0A modules and tests. All values remain ⚑ VALIDATE. |
| `docs/rg09/rg09_replay_fixture_spec.md` | Published replay fixture format spec defining required fields, companion metadata, and blocking rule for v4.14.0. |
| `docs/src/task_validity_pilot_report.md` | Stub populated with pilot design only; no results claimed; all VALIDATE items cross-referenced by assumption ID. |
| `docs/src/ResolutionLedger.md` | RG-09 moved to PARTIAL: pilot-ingestion five-field schema frozen and traceable in governed RG-09 docs; I-G protocol deliverables recorded; II-0A code deliverables remain open. Count matrix updated (RG OPEN 9→8, PARTIAL 4→5). Ledger **1.0.13 → 1.0.14**. |
| `README.md`, `docs/src/README.md` | Companion stamps and release context rebased to **4.13.0** / Ledger **1.0.14**. |
| `docs/src/ImplementationPlan.md` | §1.2 audit baseline advanced to **4.13.0**; RG-09 **PARTIAL** bullet; document **6.4.17 → 6.4.18**. |

## Version 4.12.4 (2026-03-28) — AQ-04 Governance Closure

This is a PATCH release. No runtime behavior, contracts, schemas, or public
APIs change.

### Summary

Closes AQ-04 (BOCPD placement decision) and removes stale "BOCPD op" wording
from companion surfaces that would otherwise be internally inconsistent with
the accepted decision.

### Detailed Changes

| Location | Change |
|----------|--------|
| ResolutionLedger.md AQ-04 | Closed. Decision: orchestrator-managed regime service over governed DataView inputs. Graph-op BOCPD prohibited for governed production labels. Resolution block includes PIT compliance statement, cold-start policy caveat, effective_at semantics, and offline research carve-out. |
| ResolutionLedger.md §1.1 | AQ count: OPEN 7→6, CLOSED 1→2. ∑ OPEN 37→36, CLOSED 59→60. |
| ResolutionLedger.md §1.2 | AQ-04 removed from blocking hotlist. |
| ResolutionLedger.md MLC-0 | Title and one acceptance criterion updated from "BOCPD op" to "canonical BOCPD regime service." |
| ResolutionLedger.md RG-04 | One acceptance criterion updated from "BOCPD op" to "BOCPD regime service." |
| ResolutionLedger.md RG-09 | Summary and acceptance criteria hardened: canonical PIT-safe service labels required; graph-local or retrospective labels inadmissible; kill criterion links AQ-04 to structural gate. |
| MetaLearningCore.md §5.5 | BOCPD prerequisites row: stale ops_custom.py file path replaced with service-placement note; description updated. |
| MetaLearningCore.md §1.3 | BOCPD current-role cell updated to reflect orchestrator service placement per AQ-04. |

## Version 4.12.3 (2026-03-27) — Companion-Doc Synchronization After Phase I-F Closure

Changelog for **companion documentation sync** only: rebase the README and sibling source documents on the now-closed **4.12.2** F-6 coverage / CI truthfulness baseline, remove stale "Phase I-F remains open" wording, align companion stamps to Resolution Ledger **1.0.13**, and restore a release manifest for the current docs suite. This patch does not change code, tests, CI behavior, or the claimed implementation surface.

Version: **4.12.3** (**PATCH** — documentation and manifest truthfulness only)

### Detailed Changes

| Location | Change |
|----------|--------|
| `README.md`, `docs/src/README.md` | Updated title pages, release context, phase tables, recent-changes blocks, and source stamps so the suite reflects that Phase I-F closed at **4.12.2** and the current companion baseline is **4.12.3**. |
| `docs/src/ImplementationPlan.md`, `docs/src/TechnicalRoadmap.md` | Rebased companion lines/source stamps, advanced document patch versions, and removed stale text that treated F-6 / Phase I-F as still open work. |
| `docs/src/MetaLearningCore.md`, `docs/src/MetaLearningArchitectureVision.md`, `docs/src/WhitePaper.md` | Updated companion/version references to the current suite baseline; White Paper release note and baseline wording now reference the closed Phase I-F state. |
| `docs/releases/4.12.3.yml` | Added the current release manifest so `docs/releases/` again contains manifest truth for the active companion baseline. |
| `VERSION.md` | Added this release entry and index line. |

### Test / Validation Evidence

- Pass: documentation truth audit
  - `Select-String -Path README.md,docs\src\*.md,VERSION.md,docs\releases\4.12.3.yml -Pattern '4\.12\.1|1\.0\.12|Phase I-F remains open|Version 4\.11\.0|VERSION.md 4\.11\.0'`
  - Result after patch: no stale hits in the touched companion-doc surfaces.
- Pass: manual review
  - Title pages, RECENT_CHANGES blocks, DOCMAP tables, and SOURCE_STAMP blocks now agree on the **4.12.3** / **1.0.13** companion baseline.
## Version 4.12.2 (2026-03-27) — Phase I-F-6 Coverage / CI Truthfulness Closure (GATE-I-F-06 / OI-24)

Changelog for **Phase I-F-6 coverage / CI truthfulness closure**: audit the live omit surface against the built Phase I boundary, remove stale/dead omit entries, stop treating local filesystem and mocked-HTTP tests as `net`, align AGENTS coverage guidance with the canonical thresholds, and make CI enforce the branch floor it claims instead of passing unused environment variables. This closure does not expand Phase I scope or hide uncovered code; it tightens the repo’s truthfulness around the surface that is actually built and claimed.

Version: **4.12.2** (**PATCH** — F-6 coverage truth closure, CI threshold enforcement, and ledger/version alignment)

### Detailed Changes

| Location | Change |
|----------|--------|
| `pyproject.toml` | Removed dead omit entries for nonexistent files, restored `srcPy.pipeline.stages.market_data.exceptions` to coverage scope, and clarified omit comments so they describe deferred/non-canonical surfaces instead of silently hiding live code. |
| `tests/python/unit/pipeline/test_file_source_bitemporal.py`, `tests/python/integration/test_source_to_pit_chain.py`, `tests/python/unit/test_loaders_api_edges.py` | Removed residual `pytest.mark.net` labels from local-only tests so `MARKERS="not net"` no longer skips offline coverage-bearing tests. |
| `.github/workflows/ci.yml` | Removed unused coverage-threshold env vars from the test step and added an explicit branch-coverage check from `coverage.json` with an `80%` floor. |
| `AGENTS.md` | Corrected coverage guidance to `fail_under = 90` line / `80%` branch and documented `pytest --no-cov` as the canonical narrow local validation convention. |
| `docs/src/ResolutionLedger.md` | Closed `OI-24` and `GATE-I-F-06`, updated the dashboard/hotlist, and recorded the omit/marker/CI truthfulness evidence. |
| `VERSION.md` | Added this release entry and index line. |

### Test / Validation Evidence

- Pass: `python -m pytest --override-ini addopts='' tests\python\unit\pipeline\test_file_source_bitemporal.py -q -k "not context_manager" --cov=srcPy.pipeline.stages.market_data.sources.file --cov=srcPy.pipeline.stages.market_data.exceptions --cov-branch --cov-fail-under=0 --cov-report=json:tmp_cov_market_data.json --cov-report=term`
  - Observed before the omit fix: `market_data.exceptions` was suppressed by the omit list and did not report.
  - Observed after the omit fix: the focused market-data seam reports normally and `coverage.json` exposes `totals.percent_branches_covered` for CI enforcement.
- Pass: targeted offline marker audit after removing stale labels:
  - `python -m pytest --override-ini addopts='' -q -m "not net" tests\python\unit\pipeline\test_file_source_bitemporal.py tests\python\integration\test_source_to_pit_chain.py tests\python\unit\test_loaders_api_edges.py`
- Pass: config/doc audit
  - `Select-String -Path pyproject.toml,AGENTS.md,.github\workflows\ci.yml,docs\src\ResolutionLedger.md -Pattern 'fail_under = 90|80%|--no-cov|not net|percent_branches_covered'`

## Version 4.12.1 (2026-03-27) — Companion Suite: March 2026 Report Synthesis & Phase Mapping

Changelog for **companion documentation sync** only: absorb a twelve-report internal synthesis into `docs/src/` without runtime changes. The suite now carries a canonical **report-cluster → phase** test matrix (Implementation Plan, summarized in README and Technical Roadmap), sharpens **truth vs pilot vs promotable** language, and encodes allocator design-memo direction as **research target** (task-aware adaptation, utility after frictions, hierarchical target layers A–D) distinct from **present governed substrate truth**.

Version: **4.12.1** (**PATCH** — documentation and semantic alignment only)

### Detailed Changes

| Location | Change |
|----------|--------|
| `docs/src/README.md` | March 2026 synthesis subsection; honest conclusions (substrate truth, unproven allocator, deployment/governance emphasis, routing pilot, narrow signal base); cluster→phase mapping; future allocator direction line; companion versions → **4.12.1**. |
| `docs/src/ImplementationPlan.md` | I-G / II-0 / II-A–E / III / IV sharpened per synthesis; II-D emphasizes structured post-allocator conditioning; **Appendix D** report-to-phase matrix + design-idea mapping; version → **6.4.16**. |
| `docs/src/TechnicalRoadmap.md` | Report-driven sequencing; next-gen allocator direction; II-0 / II-D strategic weight; expanded kill/fallback language; version → **1.4.17**. |
| `docs/src/MetaLearningCore.md` | Burden-of-proof and March 2026 evidence-stack subsection; routing pilot vs default `confidence_scalar`; deployment layer complement; failure-mode warnings; task/utility framing; version → **1.2.15**. |
| `docs/src/MetaLearningArchitectureVision.md` | Target stack layers (representation, world model, expert family, post-allocator conditioning, conditional execution); routing explicitly non-default; version → **1.2.16**. |
| `docs/src/ResolutionLedger.md` | RG-09, OI-35/37/39/40, MLN-03/06/07 summaries and acceptance criteria aligned to synthesis; ledger metadata → **1.0.12** / **4.12.1**. |
| `docs/src/WhitePaper.md` | Tone calibrated to substrate truth, pilot hypotheses, and deployment discipline without claiming validated next-gen machinery; companion bump → **2.2.5**. |
| `VERSION.md` | This patch entry and index line. |

### Test / Validation Evidence

- Pass: manual review — companion DOCMAP / SOURCE_STAMP / RECENT_CHANGES blocks updated consistently across touched sources.
- No pytest / mypy scope: documentation-only patch.

## Version 4.12.0 (2026-03-26) — Phase I-F-5 Determinism Boundary Closure (GATE-I-F-05 / OI-23)

Changelog for **Phase I-F-5 determinism boundary closure**: publish the Phase II determinism source of truth in `docs/contracts/phase_ii_determinism_boundary.md`, replace the old F-5 deferral block in the interface contract companion doc with a source-of-truth pointer, close `OI-23`, close `GATE-I-F-05`, and synchronize the Resolution Ledger dashboard and version surfaces without claiming any Phase II implementation work. This release keeps early ML gate language explicitly at ADR-007 `D2` / semantic reproducibility and does not promote early artifacts to `D3` / bitwise certification.

Version: **4.12.0** (**MINOR** — F-5 determinism boundary closure, companion-contract sync, and ledger/version alignment)

### Detailed Changes

| Location | Change |
|----------|--------|
| `docs/contracts/phase_ii_determinism_boundary.md` | Added the new F-5 anchor document covering the ADR-007 D-tier table for Phase II artifact surfaces, the singular HMAC-SHA256 namespace-based seed derivation scheme, deterministic `task_id` expectations, the same-environment Python-only `D2` reference-run boundary, explicit non-goals, and open `⚑ VALIDATE` items. |
| `docs/contracts/phase_ii_interface_contracts.md` | Replaced the old F-5 deferral section with a pointer to the determinism boundary document and tied the `task_id` contract note to the new source of truth, while keeping the interface doc free of accidental `D3` language. |
| `docs/src/ResolutionLedger.md` | Closed `OI-23` and `GATE-I-F-05`, updated the status dashboard counts, removed `OI-23` from the blocking hotlist, reduced `GATE-I-F` HALT-open count from 2 to 1, and left `OI-24` open with `OI-23` as its now-closed predecessor. |
| `VERSION.md` | Added the 4.12.0 index line and detailed release entry for the F-5 closure. |

### Test / Validation Evidence

- Pass: `Select-String -Path docs/contracts/phase_ii_determinism_boundary.md -Pattern '## 1. Purpose','## 4. Phase II artifact D-tier table','## 5. Seed derivation scheme','## 6. Deterministic task-ID expectations','## 7. Reference-run reproducibility boundary','## 9. Open ⚑ VALIDATE items'`
- Pass: `Select-String -Path docs/contracts/phase_ii_interface_contracts.md -Pattern 'phase_ii_determinism_boundary.md'`
- Pass: `if (-not (Select-String -Path docs/contracts/phase_ii_interface_contracts.md -Pattern 'D3')) { 'ok' }`
- Pending repo-wide doc/render checks are intentionally left to later phases; this closure is documentation-first and does not claim new runtime or CI behavior.
## Version 4.11.0 (2026-03-25) — Phase I-F-4 Contract Publication and Closure

Changelog for **Phase I-F-4 contract publication**: add the Phase II meta-learning interface stub package under `srcPy/meta_learning/`, publish the companion contract document, publish the draft-07 Signal Reliability Layer schema derived from the governing prose specification, assign the reliability schema to new ledger ID `OI-41` because `OI-35` already means RiskFn in the live ledger, close `OI-22`, close `OI-41`, close `GATE-I-F-04`, and truthfully omit the stub-only package from coverage under `[tool.coverage.run]` without changing the global `fail_under = 90` threshold.

Version: **4.11.0** (**MINOR** — F-4 contract publication, reliability schema lock, gate closure, and separate tracking for unrelated strict-mypy debt)

### Detailed Changes

| Location | Change |
|----------|--------|
| `srcPy/meta_learning/`, `srcPy/meta_learning/contracts/` | Added Phase II contract stubs only: package root `CONTRACT_VERSION = "v1"`, frozen `MetaTask`, `TaskGeneratorProtocol`, `TaskRegistryProtocol` with typed exceptions, and context encoder input/output protocols with explicit F-5 determinism deferrals. |
| `schemas/signal_reliability.schema.json` | Added draft-07 machine-readable schema covering the Signal Reliability Layer fast state, slow state, and run-level report surface while preserving advisory-only semantics from the governing prose spec. |
| `docs/contracts/phase_ii_interface_contracts.md` | Added the companion Phase II contract note covering MetaTask, TaskRegistry, context encoder boundaries, reliability crosswalks, and explicit F-5 / Phase II deferrals. |
| `pyproject.toml` | Added `srcPy/meta_learning/*` to `[tool.coverage.run].omit` under a dedicated Phase II contract-stub comment block; left `[tool.coverage.report].fail_under = 90` unchanged. |
| `docs/src/ResolutionLedger.md` | Restored `OI-35` as the RiskFn item, closed `OI-22`, added and closed `OI-41` for the Signal Reliability schema contract, closed `GATE-I-F-04`, and opened `OI-42` for the separate `srcPy/__init__.py` strict-mypy blockers. |

### Test / Validation Evidence

- Pass: `/usr/bin/python3 -m compileall srcPy/meta_learning`
- Pass: `/usr/bin/python3 -m json.tool schemas/signal_reliability.schema.json`
- Pass: `cmd.exe /c '.venv-codex\Scripts\python.exe' -m pytest tests/python/unit/backtesting/test_contracts_roundtrip.py --collect-only --no-cov -q`
- Closure review check: `cmd.exe /c '.venv-codex\Scripts\python.exe' -m mypy srcPy/strategies/momentum/ srcPy/strategies/pipeline_strategy.py srcPy/artifact_registry/ srcPy/cli/gate.py --strict`
  - Current result: 7 errors total. Five are pre-existing `import-untyped` failures for missing `pandas` stubs across the governed F-2 surface and are tracked as OI-33 debt, not F-4 regressions. Two are `attr-defined` failures in `srcPy/__init__.py`, now tracked separately under OI-42 and not folded into F-4 closure.

## Version 4.10.0 (2026-03-25) — Phase I-F-3 Seam Closure (GATE-I-F-03 / OI-21)

Changelog for **Phase I-F-3 seam closure**: amend `GATE-I-F-03` and `OI-21` acceptance criteria to match ADR-005's committed scope; close `GATE-I-F-03` and `OI-21` at v4.10.0; record verification evidence in `docs/audits/phase_if_f3_seam_audit.md` and the AQ-07 plan in `docs/audits/AQ-07_alpha_ir_migration_plan.md`.

Version: **4.10.0** (**PATCH** — F-3 seam closure, OI-21 closure, GATE-I-F-03 closure, AQ-07 plan artifact)

### Detailed Changes

| Location | Change |
|----------|--------|
| `docs/audits/phase_if_f3_seam_audit.md` | F-3 seam verification audit with exercised evidence references; checklist aligned to amended acceptance |
| `docs/audits/AQ-07_alpha_ir_migration_plan.md` | AQ-07 planning/deferral record for unresolved Phase II seam ADR scope |
| `docs/src/ResolutionLedger.md` | Amended F-3 acceptance criteria; closed `GATE-I-F-03` and `OI-21` at v4.10.0 |

### Test / Validation Evidence

- Ran targeted tests:
  - `pytest tests/python/integration/strategies/test_momentum_governed_path.py --no-cov`
  - `pytest tests/python/integration/backtesting/test_orchestrator_backtesting_artifacts.py --no-cov`
  - `pytest tests/python/unit/artifact_registry/test_storage_shims.py --no-cov`

## Version 4.9.1 (2026-03-24) — Roadmap Phase-Model Clarification Patch

Changelog for the **roadmap phase-model clarification pass**: revise the companion planning surface so the pre-build foundation is explicit rather than implied, keep Phase I-F narrow, introduce **Phase I-G** and **Phase II-0** as distinct pre-Phase-II stages, preserve **II-A through II-E** as the actual validation-gated adaptive-learning build, and keep **Phase III** / **Phase IV** explicitly conditional. This release is documentation-first and policy-aligned: it does not claim a new runtime subsystem, a promotable allocator, or newly delivered execution or Signal Factory machinery.

Version: **4.9.1** (**PATCH** — roadmap clarity, ledger hardening, and companion-suite protocol-surface additions without release-surface expansion)

### Major Themes Across All Changes

- Made the roadmap read as **I-F -> I-G -> II-0 -> II**, rather than letting Phase II silently absorb protocol work and scaffolding work.
- Added the exact evidence-first guardrail language across the planning docs so promotable adaptive-learning machinery begins only in Phase II.
- Introduced lightweight protocol/spec appendix surfaces for **RiskFn**, **Signal Generation**, **task validity pilot evidence**, and **paper-trade simulation handoff**.
- Updated the Resolution Ledger so `I-G` and `II-0` exist as tracked planning semantics while keeping narrow `I-F` blockers and true Phase II normative locks in place.

### Detailed Changes

| Location | Change |
|----------|--------|
| `docs/src/README.md`, `docs/src/ImplementationPlan.md`, `docs/src/TechnicalRoadmap.md` | Reframed the roadmap so **I-F** is narrow closure, **I-G** is empirical/protocol foundation, **II-0** is non-promotable harness work, **II** is the first promotable adaptive-learning phase, and **III/IV** remain conditional. |
| `docs/src/ImplementationPlan.md` | Added `# 3.x Phase I-G` and `# 4. Phase II-0`, preserved `II-A` through `II-E`, expanded the Immediate Priority Stack, and added appendix references for protocol and handoff surfaces. |
| `docs/src/TechnicalRoadmap.md` | Added the explicit sequencing block, “not assumed” language, and subphase tables for **II-0**, **II**, **III**, **IV**, and **IV+**. |
| `docs/src/MetaLearningCore.md` | Clarified that early empirical closure may begin in **I-G** / **II-0**, that pre-trainer pilots are allowed, and that final Phase II promotion logic still governs trainer commitment, promotion, rollback, and kill. |
| `docs/src/MetaLearningArchitectureVision.md` | Added forward-compatibility sections for **RiskFn Protocol**, **Signal Generation Protocol / signal-admission path**, and the **feature frontier / alternative-data ingestion** boundary; clarified that `signal_embedding` remains a Phase IV operational surface. |
| `docs/src/WhitePaper.md` | Reframed the roadmap narrative around **I-F**, **I-G**, **II-0**, and conditional **III/IV** while keeping the document less operational than the internal plan set. |
| `docs/src/ResolutionLedger.md` | Added `I-G` / `II-0` planning items for RiskFn protocol definition, Signal Generation Protocol, task non-exchangeability pilot, context-encoder upgrade criteria, signal-universe expansion policy, alternative-data admissibility contract, paper-trading simulation requirements, and II-0 harness scaffolding. |
| `docs/src/risk_protocol.md`, `docs/src/signal_generation_protocol.md`, `docs/src/task_validity_pilot_report.md`, `docs/src/paper_trade_sim_spec.md` | Added new markdown appendix surfaces so the updated Implementation Plan points to concrete protocol/spec files rather than placeholder-equivalent references. |
| `README.md` | Added a short governed-roadmap pointer so the repo-root README no longer obscures the current phase map maintained in `docs/src/README.md`. |

### Behavioral Changes

- The companion suite now states explicitly that **Phase I-F freezes system truth**, **Phase I-G freezes research policy/proof burden**, and **Phase II-0** is **non-promotable scaffolding** only.
- The roadmap no longer reads as if Phase II starts with immediate full MLC buildout.
- **Phase III** is now consistently described as the first execution-serious phase, and **Phase IV** as the first signal-factory-serious phase, both conditional on allocator validation and product need.
- `RiskFn` is no longer described as a vague placeholder in the planning narrative; it is treated as a governed protocol boundary.
- Alternative-data and signal-factory breadth are now described as later governed ambitions rather than present-day facts.

### Breaking Changes

None.

### Test / Validation Evidence

| Check | Result |
|-------|--------|
| Targeted companion-doc readback | Verified revised phase ordering, guardrail text, and appendix references across the touched markdown sources. |
| Terminology consistency search (`rg`) | Verified `Phase I-G`, `Phase II-0`, conditional III/IV language, and the new appendix filenames are present where intended. |
| Code/test suite execution | Not run; this release is a markdown/ledger update only. |

### Companion Document Versions

| Document | Version surface referenced in this release |
|----------|-------------------------------------------|
| `README.md` | 4.9.0 |
| `docs/src/ImplementationPlan.md` | 6.4.14 |
| `docs/src/TechnicalRoadmap.md` | 1.4.15 |
| `docs/src/MetaLearningCore.md` | 1.2.13 |
| `docs/src/MetaLearningArchitectureVision.md` | 1.2.14 |
| `docs/src/ResolutionLedger.md` | 1.0.6 |
| `docs/src/WhitePaper.md` | 2.2.4 |

### Deferred

- No runtime subsystem, gate implementation, broker integration, or promotable allocator code is claimed by this release.
- DOCX rebuild/version-rebasing work for the companion suite remains outside this patch-sized ledger update.
- Existing unrelated working-tree changes, including `docs/src/FormattingSpec.md`, are not part of this release entry.

---

## Version 4.9.0 (2026-03-24) — Phase I-F-2 Planning-Surface Sync and Resolution-Ledger Consistency Patch

Changelog for the **Phase I-F-2 planning-surface sync patch**: carry forward the Phase I-F-1 truth baseline while rebasing the canonical companion suite to the live version set (**Implementation Plan 6.4.14 / Technical Roadmap 1.4.15 / Meta-Learning Core 1.2.13 / Meta-Learning Architecture Vision 1.2.14 / Resolution Ledger 1.0.6 / README 4.9.0 / VERSION.md 4.9.0**). This patch does not claim a new runtime subsystem. It closes the planning/documentation surface for **OI-20 / GATE-I-F-02**, repairs Resolution Ledger lifecycle contradictions on **OI-09**, **OI-10**, and **OI-17**, and updates title pages, companion maps, and current-release framing so the suite tells one consistent story.

### Detailed Changes

| Location | Change |
|----------|--------|
| `README.md` | Bumped release anchor to **4.9.0**; updated companion map, docmap versions, and current-release framing. |
| `docs/src/TechnicalRoadmap.md`, `docs/src/ImplementationPlan.md` | Rebased managed metadata to **1.4.15** / **6.4.14** and preserved the II-A → II-E Phase II structure with F-2 planning-surface sync notes. |
| `docs/src/MetaLearningCore.md`, `docs/src/MetaLearningArchitectureVision.md` | Metadata/docmap/source-stamp sync to the live suite versions; no substantive F-2 body rewrite. |
| `docs/src/ResolutionLedger.md` | `MRL_VERSION` **1.0.6** and `CODEBASE_VERSION` **4.9.0**; closed **OI-20** / **GATE-I-F-02**; repaired **OI-09**, **OI-10**, and **OI-17** lifecycle fields; refreshed dashboard counts and hotlist truth. |
| `docs/src/FormattingSpec.md` | Companion/version tables and footer rebased to the **4.9.0** suite surface. |

### Validation

| Check | Result |
|-------|--------|
| Managed version surfaces | Canonical title pages, companion lines, and footers rebased to the **4.9.0** suite state |
| Resolution Ledger lifecycle truth | OI/gate status fields, resolved_on fields, dashboard counts, and gate dependencies made internally consistent |

---

## Version 4.8.0 (2026-03-22) — Phase I-F-1 Companion-Doc Truthfulness Audit and v4.8.0 Baseline Sync

Changelog for **Phase I-F-1** ([OI-19](docs/src/ResolutionLedger.md), [GATE-I-F-01](docs/src/ResolutionLedger.md)): establish **v4.8.0** as the companion-suite and `VERSION.md` release anchor; remove stale **4.5.3** baseline references from title pages, source stamps, and document maps; align phase narrative with repo truth (**Phase I-A through I-E delivered and gates closed; Phase I-F open**); record **I-E gate closure**, **OI-02**, **OI-08**, **OI-13**, and **ADR-009 ACCEPTED** in companion prose where referenced; audit [FormattingSpec.md](docs/src/FormattingSpec.md) for internal consistency; run a structural sync pass for **Momentum Spec v1.3** readiness (canonical Markdown source for v1.3 is not present in `docs/src/` — see [docs/audits/phase_if_f1_audit_report.md](docs/audits/phase_if_f1_audit_report.md)); and publish audit artifacts:

- [docs/audits/phase_if_f1_truth_baseline.md](docs/audits/phase_if_f1_truth_baseline.md)
- [docs/audits/phase_if_f1_claim_matrix.csv](docs/audits/phase_if_f1_claim_matrix.csv)
- [docs/audits/phase_if_f1_companion_sync_report.md](docs/audits/phase_if_f1_companion_sync_report.md)
- [docs/audits/phase_if_f1_audit_report.md](docs/audits/phase_if_f1_audit_report.md)

This is a **MINOR** release for the documentation and manifest surface: it does not claim new runtime subsystems beyond truthful description of the existing platform and does not convert provisional validation thresholds into fixed policy.

### Detailed Changes

| Location | Change |
|----------|--------|
| `docs/src/*.md`, `VERSION.md` | Bumped companion document versions (patch/minor per doc), set **`VERSION.md 4.8.0`** on title pages and stamps, updated **§1.2 / §3** “current reality” and release-line language to the **4.8.0** audit baseline while preserving accurate citations to **4.5.4** as the last code-heavy Phase I-E delivery where needed. |
| `docs/src/ResolutionLedger.md` | `CODEBASE_VERSION` **4.8.0**; **§8** Phase I-F section header no longer implies I-E is pending; **OI-19** / **GATE-I-F-01** closed with evidence pointers to `docs/audits/`; dashboard counts updated. |
| `docs/releases/4.8.0.yml` | Release manifest for **4.8.0** with `VersionLedger@4.8.0` and suite companion tokens. |
| `README.md` (repo root) | Tightened front matter: canonical companion suite is **`docs/src/README.md`**; root README may lag on badges. |

### Validation

| Check | Result |
|-------|--------|
| Companion lines and `VERSION.md` tokens | Aligned to **4.8.0** baseline per [docs/audits/phase_if_f1_companion_sync_report.md](docs/audits/phase_if_f1_companion_sync_report.md) |
| Claim audit | Recorded in [docs/audits/phase_if_f1_claim_matrix.csv](docs/audits/phase_if_f1_claim_matrix.csv) |

---

## Version 4.5.4 (2026-03-21) — Phase I-E Closure Pass: Canonical Storage/Gate Ownership, Governed Momentum Blocker Closure, and ADR-007 D2 Replay Evidence

Changelog for **the Phase I-E closure pass**: complete the canonical ownership move for bundle-writing and governed artifact storage under `srcPy.artifact_registry`, reduce `srcPy/backtesting/storage/` to explicit retired compatibility shims, route both shipped CLI entry surfaces (`mm-gate` and `marketmind_gate.cli`) through `srcPy.cli.gate`, and close the remaining Phase I-E governed momentum blockers without claiming work that is still deferred. The governed momentum path now locks `stat_validity_report.json` to schema `v1`, emits canonical `COST_GATE_REJECTED` failure reports through `gate_result.json` while keeping the existing generic fail bucket, shares one cumulative `RunRegistry` trial-counter family across the three production-intended variants, fails crash-override requests closed pending a governed source adapter, and carries structured book-membership plus explicit fail-closed `beta_reversal_score` diagnostics in `AlphaIR`. This release also upgrades the ADR-007 evidence story to a truthful D2 state by enriching the eight committed golden suites with concrete replay expectations, adding a Python replay suite, and updating `canonical_frame.py` to report Python-only D2 evidence while leaving cross-language certification explicitly open under `OI-15`. It is a PATCH release because it closes governance, provenance, and documentation gaps on existing public surfaces without introducing a new product subsystem or changing the top-level runtime entry model.

### Detailed Changes

| Location | Change |
|----------|--------|
| `srcPy/artifact_registry/bundle_writer.py`, `srcPy/artifact_registry/artifact_store.py`, `srcPy/artifact_registry/artifacts.py`, `srcPy/artifact_registry/sanitization.py`, `srcPy/backtesting/storage/` | Moved real bundle-writer and bundle-artifact-store ownership into the canonical artifact registry and reduced the legacy `backtesting/storage` namespace to retired compatibility shims or placeholders with explicit rationale comments. |
| `pyproject.toml`, `marketmind_gate/cli.py`, `srcPy/cli/gate.py` | Canonicalized the gate surface so `mm-gate` and `marketmind_gate.cli` both delegate to `srcPy.cli.gate.main`; added shared failure-report helpers and `COST_GATE_REJECTED` reason-code emission on the governed path. |
| `srcPy/strategies/momentum/entry.py`, `srcPy/strategies/momentum/strategy.py`, `srcPy/strategies/momentum/artifacts/stat_validity.py`, `srcPy/strategies/pipeline_strategy.py` | Closed the remaining Phase I-E momentum blockers: optional `RunRegistry`/`LocalCAS` wiring, shared cumulative trial counters persisted in `trial_counters.json`, canonical `stat_validity_report.json` schema `v1`, fail-closed crash-override handling pending a governed source adapter, structured book-membership diagnostics, explicit unavailable `beta_reversal_score`, and a typed base-class signal-envelope contract that removes the old override suppression. |
| `tests/python/unit/cli/test_gate.py`, `tests/python/unit/strategies/momentum/`, `tests/python/integration/strategies/test_momentum_governed_path.py`, `tests/python/unit/artifact_registry/test_storage_shims.py` | Added focused coverage for the canonical CLI path, governed cost-gate rejection reporting, crash-override fail-closed behavior, shared trial counting across registry instances, canonical storage shims, and the updated momentum diagnostics/stat-validity contracts. |
| `tests/golden/adr007/`, `tests/python/unit/hashing/test_adr007_replay.py`, `srcPy/ops/hashing/canonical_frame.py` | Enriched the committed ADR-007 fixtures with concrete expected outputs, added a Python replay suite over the eight golden suites, and updated `canonical_frame.py` evidence to truthfully report Python-only D2 replay coverage while leaving `OI-15` open for three-language certification. |
| `docs/src/ResolutionLedger.md`, `docs/src/README.md`, `docs/src/ImplementationPlan.md`, `docs/src/TechnicalRoadmap.md`, `docs/src/MetaLearningCore.md` | Synchronized the companion docs to the delivered `4.5.4` state, closed the relevant Phase I-E ledger items, opened `OI-31` and `OI-32` as explicit deferrals, and updated suite references so the current release context no longer points at `4.5.3`. |

### Behavioral Changes

* Canonical governed bundle-writing and artifact-store ownership now lives only under `srcPy.artifact_registry`; the older `srcPy.backtesting.storage` path remains compatibility-only and should not be treated as an implementation surface.
* The shipped gate entrypoints now share the same exit-code and report-writing behavior because both delegate to `srcPy.cli.gate.main`.
* Governed momentum runs can record platform-managed cumulative trial counts across the three production-intended variants without relying on a private writer attribute or allowing reset-by-separate-run behavior.
* An explicitly requested crash override on the governed momentum path now fails closed with a `NotImplementedError` that points to the governed adapter backlog (**OI-34**), rather than silently accepting the FRED approximation stub as a production trigger source.
* `AlphaIR.diagnostics` now carries explicit per-symbol book membership and a truthful unavailable-state payload for `beta_reversal_score`.
* ADR-007 fixture evidence is stronger and more replayable in Python, but the project still does **not** claim D3 cross-language certification; that remains blocked on `OI-15`.

### Breaking Changes

None intended. Compatibility shims remain in place for the retired storage namespace and the gate entry surface, but the canonical ownership and documentation now point only to `srcPy.artifact_registry` and `srcPy.cli.gate`.

### Validation

| Check | Result |
|-------|--------|
| Syntax-only compile of touched Python files via `compile(...)` | Passed. |
| Companion-doc and ledger/version consistency audit | Updated to `4.5.4` current-state references and closed/open item statuses for the Phase I-E closure pass. |
| Full `pytest`, coverage, and `mypy --strict` acceptance sweep | Not run in this environment; local Linux Python lacked project test dependencies and the Windows interpreter path was blocked by the sandbox/runtime boundary. |

---

## Version 4.5.3 (2026-03-19) — Test-Suite Closure Pass: Torture-Fixture Robustness, Governed/Docs Alignment, and Runtime Hardening

Changelog for **the post-4.5.2 test-suite closure pass**: harden `dataprep_orchestrator` against BOM-heavy, ragged, empty, encoded, and cross-file torture fixtures; close the remaining governed gate and docs-manifest test mismatches; make HTTP-loader, strategy-registry, and formatting-spec behaviors fail in the precise ways the tests expect; stabilize Hypothesis/property coverage and Influx logging error handling; and harden a few runtime edges surfaced only during full-suite verification, including direct CLI execution, transient repo-copy noise in PowerShell release-doc tests, stale cache pickle recovery, and sync execution of trivial awaitables when the test harness blocks event-loop setup. This is a PATCH release because it fixes regressions and environmental brittleness on existing governed/runtime surfaces without introducing a new public subsystem or changing SemVer-visible APIs.

### Detailed Changes

| Location | Change |
|----------|--------|
| `srcPy/data/dataprep_orchestrator.py`, `tests/python/plugins/torture_plugin.py`, `tests/python/data/torture_manifest.yml` | Closed the torture-fixture failures by normalizing BOM/weird headers before timestamp validation, recognizing `effective_date` as timestamp-like, tolerating ragged/blank-line CSV probes, respecting non-UTF-8 fixture encodings and zero-byte CSVs, remapping inline spec column references after normalization, teaching torture discovery about `crossfile_prices.csv` + `crossfile_metadata.csv`, and adding a sync awaitable fallback for test harnesses that block event-loop creation. |
| `devtools/docs/release/compile_release.py` | Restricted generated companion tokens to the actual suite/non-doc IDs in the manifest so minimal catalogs no longer emit invalid `ResolutionLedger@...` tokens. |
| `tests/python/unit/gate/test_core.py`, `srcPy/pipeline/stages/market_data/sources/data_loader.py`, `tests/python/unit/test_loaders_api_edges.py`, `tests/python/unit/test_strategy_imports_and_registry.py` | Realigned governed-path and loader/registry tests with current behavior: bad governed fixtures now fail through `stat_validity_report.json`, HTTP non-200s re-raise `DataFetchError` instead of being retried as generic failures, async loader edge tests run under the repo’s network policy, and the momentum registry import-error assertion now patches the dynamic import site directly. |
| `devtools/docs/formatting/load_spec.py`, `tests/python/integration/docs/test_formatting_build_flow.py`, `devtools/docs/cli.py`, `tests/python/integration/docs/test_release_docs_ps1_integration.py` | Hardened the docs toolchain and integration tests: formatting-spec loading now fails closed when `formatting_rules` are missing, formatting-build tests accept Pandoc-first stderr, direct `devtools/docs/cli.py` execution bootstraps `sys.path` correctly, and the PowerShell release-doc tests ignore transient local scratch directories and seed a bootstrap `VERSION.md` when exercising synthetic release versions. |
| `srcPy/ops/mm_logkit.py`, `tests/python/property/hashing/test_hashing_properties.py`, `tests/python/unit/preprocessor/test_momentum_ops.py`, `tests/python/integration/test_stat_arb_vertical_slice.py`, `srcPy/strategies/pipeline_strategy.py` | Stabilized the remaining long-tail failures: InfluxDB handler error logging now guards against recursive self-reentry, hashing namespace generators exclude BOM-invalid strings, slow Hypothesis cases suppress the right health/deadline checks, the stat-arb Yahoo smoke test uses `asyncio.run(...)`, and stale/incompatible strategy-cache pickle files are treated as cache misses rather than hard failures. |

### Behavioral Changes

* CSV torture fixtures that previously failed on BOM-heavy headers, ragged lines, Latin-1 bytes, zero-byte files, and cross-file sidecars now take the tolerant ingest path expected by the integration suite without weakening malformed-file failures.
* Companion-token generation for release manifests now reflects only the docs actually present in the suite manifest, so minimal release catalogs validate cleanly.
* The docs formatting loader is stricter: a compiled FormattingSpec docmodel without `formatting_rules` now fails closed instead of silently recompiling from source.
* Runtime cache and async edges are more resilient in mixed developer/test environments: stale feature-cache pickles are discarded, and simple awaitables can still be resolved when the harness prevents normal loop creation.

### Breaking Changes

None intended. The work tightens existing runtime and tooling behavior but does not introduce a new public API surface.

### Validation

| Check | Result |
|-------|--------|
| `pytest tests/python/integration/orchestrator/test_torture_fixtures_matrix.py tests/python/integration/orchestrator/test_fetch_modes.py` | Passed (coverage gate excluded during focused verification where needed). |
| `pytest tests/python/unit/docs/test_release_compiler.py tests/python/integration/docs/test_plan_release_integration.py tests/python/integration/docs/test_formatting_build_flow.py --no-cov` | Passed. |
| `pytest tests/python/unit/gate/test_core.py tests/python/unit/test_loaders_api_edges.py tests/python/unit/test_strategy_imports_and_registry.py --no-cov` | Passed. |
| `pytest tests/python/unit/preprocessor/test_momentum_ops.py tests/python/property/hashing/test_hashing_properties.py tests/python/unit/test_mm_logkit.py::TestInfluxDBHandler::test_influx_handler_error_handling --no-cov` | Passed. |
| Follow-on regressions surfaced during full-suite verification | Fixed additional docs CLI, PowerShell release-doc, stat-arb smoke, and stale strategy-cache failures uncovered after the original 31-test closure pass. |

---

## Version 4.5.2 (2026-03-19) — ADR-009 Momentum Package Spine, Focused Test Closure, and Companion-Doc Sync

Changelog for **the ADR-009 momentum package migration pass**: replace the flat `srcPy/strategies/momentum.py` implementation with the accepted `srcPy/strategies/momentum/` package spine, split the strategy into `strategy.py`, `alpha_ir.py`, `exceptions.py`, `plans/`, `entry.py`, `artifacts/`, `validation/`, and the Phase III `control/` stub, preserve StrategyRegistry compatibility for all momentum aliases, restore the missing preprocessor momentum-op test surface, add dedicated residual-plan coverage, and synchronize the companion docs so they describe the delivered package-based momentum state rather than the earlier flat-file slice. This is a PATCH release because it closes ADR-009 follow-through, testing, and documentation gaps on an existing Phase I-E surface without introducing a new public product area or changing SemVer-visible runtime entry points.

### Detailed Changes

| Location | Change |
|----------|--------|
| `srcPy/strategies/momentum/` | Introduced the ADR-009 package spine: `__init__.py` re-export, `strategy.py` for `MomentumStrategy`, `alpha_ir.py`, `exceptions.py`, variant builders in `plans/`, governed orchestration in `entry.py`, artifact serializers in `artifacts/`, `validation/production_v1.py`, and the invariant `control/__init__.py` Phase III stub. |
| `srcPy/strategies/momentum.py`, `stubs/srcPy/strategies/momentum.pyi` | Removed the obsolete flat implementation and its stale stub after migrating callers to the package layout. |
| `srcPy/strategies/pipeline_strategy.py` | Extended lazy import support so all momentum registry aliases (`momentum`, `momentum_tsmom`, `momentum_dual`, `momentum_industry`, `momentum_residual`, `momentum_kalman`, `momentum_ensemble`, `momentum_ml`) resolve through the package entry point. |
| `srcPy/preprocessor/graph/ops_custom.py` | Kept the momentum op surface on the platform preprocessor path and aligned `momentum.industry_score` lowering with the Phase II stub contract while preserving the existing momentum op registrations and lowerings. |
| `tests/python/unit/preprocessor/test_momentum_ops.py`, `tests/python/unit/strategies/momentum/`, `tests/python/integration/strategies/test_momentum_governed_path.py` | Restored and expanded the focused momentum test surface: op-registry/lowering checks, strategy/entry/artifact coverage, residual-plan feature-flag coverage, and a governed-path integration test for bundle artifacts. |
| `pyproject.toml` | Updated pytest marker registration (`unit`) and changed the momentum coverage omit from the flat-file path to the package-path form (`srcPy/strategies/momentum/*`) so the config matches the migrated layout. |
| `docs/src/ImplementationPlan.md`, `docs/src/README.md`, `docs/src/MetaLearningCore.md`, `docs/src/TechnicalRoadmap.md`, `docs/src/ResolutionLedger.md` | Synced the companion docs to the delivered ADR-009 package migration state, closed the flat-file → package migration item, and replaced stale “migration pending” wording with the current package-spine reality while keeping open MOM blockers explicit. |

### Behavioral Changes

* `from srcPy.strategies.momentum import MomentumStrategy` still works, but the implementation now lives behind the package spine required by ADR-009.
* Momentum-specific governed execution now has a dedicated `entry.py` boundary with explicit `ConvergenceError` and `CostGateRejection` handling, signal-card/stat-validity serialization, and a package-local validation profile.
* The focused momentum test surface now explicitly covers the preprocessor momentum ops again, including denominator guards, lowering stubs, residual-plan feature flags, and the governed artifact path.
* Companion docs now describe the package-based momentum implementation as delivered work rather than a pending ADR-009 migration.

### Breaking Changes

None intended. The release preserves the public `srcPy.strategies.momentum` import surface while changing the internal file topology from a flat module to a package.

### Validation

| Check | Result |
|-------|--------|
| `python3 -m py_compile` on touched momentum Python files | Passed using `PYTHONPYCACHEPREFIX=.tmp_pycache`. |
| Focused momentum pytest surface | 47 passed. |
| Companion-doc stale wording sweep | Updated `ImplementationPlan.md`, `README.md`, `MetaLearningCore.md`, `TechnicalRoadmap.md`, and `ResolutionLedger.md` to reflect the delivered package spine and remaining open MOM items. |

---

## Version 4.5.1 (2026-03-19) — Phase I-E Governance Closure Pass: Lineage Gate, Hashing Ownership, Canonical-Frame Evidence, and Companion-Doc Sync

Changelog for **the Phase I-E governance closure pass**: complete the governed lineage gate on the canonical bundle path, route CAS JSON canonicalization through the repo-owned `srcPy.ops.hashing` surface, strengthen `canonical_frame.py` from a single status constant into an evidence-backed certification model, migrate bundle-facing artifact storage onto the canonical artifact-registry boundary, and harden the governed momentum artifact path for the non-ADR-009 slice. This release also updates the Phase I-E companion docs so `ResolutionLedger.md`, `ImplementationPlan.md`, `TechnicalRoadmap.md`, `README.md`, and `MetaLearningCore.md` describe the delivered lineage, hashing, and governed-momentum state while keeping OI-15 and ADR-009-dependent work explicitly open. This is a PATCH release because it closes governance and documentation gaps on existing Phase I-E surfaces without introducing a new public runtime subsystem.

### Detailed Changes

| Location | Change |
|----------|--------|
| `srcPy/cli/gate.py` | Added and enforced `DataLineageGate` on the canonical governed path, tightened stale in-file comments to match the live policy contract, and continued emitting `canonical_frame_ci_status` in gate metadata. The lineage gate now fails closed on missing `pit_compliant` / `knowledge_time_column`, checks content-hash mismatches, and treats stale downloads as a warning-only pass condition. |
| `srcPy/ops/hashing/canonical_frame.py` | Replaced the raw boolean-style status wiring with an evidence-backed certification model: `CanonicalFrameCIEvidence` now names Python certification, golden-vector presence, and cross-language certification explicitly, exports a machine-readable evidence dict, and derives the published CI status from that evidence rather than a bare constant. |
| `srcPy/ops/hashing/canonicalizer.py`, `srcPy/ops/hashing/__init__.py`, `srcPy/artifact_registry/cas.py` | Moved CAS JSON canonicalization behind the repo-owned hashing authority by adding `canonicalize_json_bytes()` to `srcPy.ops.hashing`, exporting it as part of the canonical surface, and updating `LocalCAS.put_json()` to consume only that surface. The gate package may remain the underlying RFC8785/JCS implementation, but ownership now sits with `srcPy.ops.hashing` rather than a direct `marketmind_gate` import from the artifact registry. |
| `srcPy/artifact_registry/run_registry.py` | Added warning logs for suppressed registry persistence failures and retained the RunRegistry-managed trial counter used by the governed momentum/stat-validity path. Silent `OSError` swallowing is now reduced to warn-and-continue behavior. |
| `srcPy/artifact_registry/bundle_writer.py`, `srcPy/artifact_registry/artifact_store.py`, `srcPy/backtesting/storage/bundle_writer.py`, `srcPy/backtesting/contracts/bundle.py` | Kept the canonical bundle-writing surface anchored on the artifact registry while preserving compatibility adapters for the older backtesting/storage namespace. This is a minimum-bar compatibility closure rather than full namespace retirement; the call-site audit remains the governing evidence for what is still transitional. |
| `srcPy/pipeline/orchestrator.py`, `marketmind_gate/gates/core.py` | The canonical orchestrator and the compatibility gate wrapper now converge on the same governed bundle validation path, including the lineage gate and canonical-frame CI-status metadata. |
| `srcPy/strategies/momentum.py`, `srcPy/backtesting/validation/statistical/validator.py` | Hardened the non-ADR-009 governed momentum slice: momentum now emits governed `execution_assumptions.json` and `stat_validity_report.json`, records a RunRegistry-backed trial counter, normalizes PBO inputs through the canonical bridge, and now fails closed if governed artifact emission lacks realized returns. |
| `docs/src/ResolutionLedger.md`, `docs/src/ImplementationPlan.md`, `docs/src/TechnicalRoadmap.md`, `docs/src/README.md`, `docs/src/MetaLearningCore.md` | Synced the companion docs to the delivered Phase I-E governance state: DataLineageGate is live, hashing/canonicalization ownership now sits behind `srcPy.ops.hashing`, canonical-frame CI reporting has an explicit evidence model, and the non-ADR-009 governed momentum slice is materially advanced while OI-15 and ADR-009-dependent migration remain open. |

### Behavioral Changes

* Governed bundle validation now includes an explicit data-lineage decision on `dataset_manifest.json` rather than relying only on downstream PIT assumptions. Missing or false `pit_compliant` and missing `knowledge_time_column` now fail the canonical gate path directly.
* CAS identity still uses the same canonical bytes and attestation pairing, but the artifact registry no longer owns a direct import dependency on `marketmind_gate` for JSON canonicalization. Canonicalization authority now flows through `srcPy.ops.hashing`.
* Canonical-frame CI reporting is no longer just a single status constant. The system now publishes both a status value and an explicit named evidence record that distinguishes Python certification, golden-vector presence, and cross-language certification.
* Governed momentum artifact emission is stricter: the non-ADR-009 slice emits execution assumptions and stat-validity artifacts through the canonical path, records a platform-managed trial counter when available, and now fails rather than fabricating returns on the governed path.

### Breaking Changes

None intended. This release closes governance and documentation gaps on top of existing 4.5.0 surfaces; OI-15 and ADR-009-dependent momentum/package work remain explicitly open.

---

## Version 4.5.0 (2026-03-18) — Phase I-E SignalFactory Substrate + Gate Hardening

Changelog for **Phase I-E amendment (SignalFactory substrate)**: additive deliverables that make the bundle and signal contract Phase II–ready without introducing Phase II logic. (1) **Stable `slot_index` on Signal ABC**: new `srcPy/registry/` package with `SignalCatalog`, monotonic slot assignment at registration (idempotent by `spec_hash`), five starter signals (stat_arb spread_zscore, hedge_ratio, momentum TSMOM, XSMOM, RSI baseline) at slots 0–4, and `pyproject.toml` entry_points for `marketmind.signals`. (2) **`screening_report.json` as first-class bundle artifact**: two-tier rejection taxonomy in `screening_taxonomy.py` with `REASON_CODE_TO_FAMILY` (callers never pass `reason_family`), `ScreeningReportBuilder` in `screening_report.py`, JSON Schema `schemas/screening_report.schema.json`, `gate_to_screening.py` mapping (marketmind_gate gate_id + status → ScreeningStage + ReasonCode, with correct stage for both pass and fail), `BundleWriter.write_screening_report()`, and orchestrator building and writing the report after validation so every strategy evaluation run emits a screening report (accepts and rejects). Full 64-char SHA-256 for `candidate_run_id` and `screening_run_id`; max_drawdown failure maps to `FEATURE_STABILITY_FAIL`. (3) **Phase I momentum core slice on the governed strategy/op path**: `MomentumStrategy` now lives under `srcPy/strategies/` with canonical `features_plan()` wiring to `momentum.*` graph ops, an `AlphaIR` return contract from `generate_signal()`, PIT provenance propagation and governed validation, and a trade-intent override that unwraps `AlphaIR.signal` while preserving the base regime/sizer/risk flow. The preprocessor op layer adds `momentum.xsec_rank`, `momentum.vol_scale`, `momentum.residual_ols`, `momentum.residual_kf`, and `momentum.industry_score`, registered through the builtin op factory with Polars lowerings and deterministic tests. Cross-sectional semantics are locked explicitly: `momentum.xsec_rank` ranks a same-date asset universe rather than a trailing single-series percentile, and `AlphaIR.information_coefficient` is only emitted for true cross-sectional universes with at least 10 assets. (4) **Type-safety (mypy --strict)**: `srcPy/preprocessor/utils/columns.py` gains typed `_as_list` and `_derive_out_names`; `srcPy/preprocessor/graph/ops_custom.py` adds `_HasContract` Protocol for `_ProvidesMixin`, TYPE_CHECKING polars import, full annotations for all Polars lowering functions and `_delegate_to_backend`, and `cast()` on `_apply_eager` returns; `pyproject.toml` adds dev dependency `pandas-stubs`; `srcPy/strategies/momentum.py` uses `# type: ignore[override]` for `generate_signal` → `AlphaIR`; `tests/python/unit/preprocessor/test_momentum_ops.py` fixes optional `pl` assignment and uses `cast(pl.LazyFrame, ...)` for `.collect()` on lowering return values. (5) **Phase I-E gate hardening in `srcPy/cli/gate.py`**: the canonical governed validation path now treats `stat_validity_report.json` and `execution_assumptions.json` as required policy artifacts, requires `pbo` in `stat_validity_report.json` with `0 <= pbo.value <= 1`, accepts nested component `gate_result` fields when present, and fails zero-cost or missing execution assumptions instead of passing with evidence-only warnings. Focused CLI regression coverage in `tests/unit/cli/test_gate.py` now covers missing statistical-validity artifacts, malformed `pbo`, missing execution assumptions, zero-cost assumptions, and valid non-zero assumptions. (6) **Phase I-E statistical-validity bridge tightening**: `srcPy/backtesting/validation/statistical/report.py` now emits top-level `pbo` while keeping `schema_version = "v1"` and aggregating top-level `gate_result` across DSR/minTRL/bootstrap/PBO; `validator.py` now accepts canonical validator-side `path_pairs` (or bridged `cpcv_evaluations`) and computes PBO via `pbo.py` using `net_sharpe`; new `pbo_bridge.py` converts evaluated CPCV outputs into the canonical `path_pairs` surface without moving computation into `gate.py` or `cpcv.py`; focused tests now cover report emission, gate-policy failures for missing/invalid `pbo`, strict `PBO > 0.50` failure behavior, and degenerate score surfaces. This is a MINOR release: new public registry package, new bundle artifact, stricter governed gate policy, new canonical momentum strategy/op surfaces, and tighter statistical-validity/report integration; public APIs remain stable.

### Detailed Changes

| Location | Change |
|----------|--------|
| `srcPy/registry/__init__.py` | New package; exports SignalCatalog, screening_taxonomy enums and REASON_CODE_TO_FAMILY, ScreeningReportBuilder, gate_result_to_stage_and_code. |
| `srcPy/registry/signal_catalog.py` | SignalProtocol, RegisteredSignal, SignalCatalog with _next_slot and register() idempotent by spec_hash; five starter stubs; get_catalog() singleton. |
| `srcPy/registry/screening_taxonomy.py` | ScreeningStage, ScreeningStatus, ReasonCode, ReasonFamily, REASON_CODE_TO_FAMILY. |
| `srcPy/registry/screening_report.py` | ScreeningReportBuilder (reason_family derived from reason_code only); full 64-char candidate_run_id. |
| `srcPy/registry/gate_to_screening.py` | GATE_STAGE_MAP and GATE_FAIL_REASON_MAP; gate_result_to_stage_and_code() uses same stage for pass/fail; max_drawdown → FEATURE_STABILITY_FAIL. |
| `schemas/screening_report.schema.json` | New schema; pattern ^[a-f0-9]{64}$ for candidate_run_id and screening_run_id. |
| `srcPy/backtesting/storage/bundle_writer.py` | write_screening_report(payload). |
| `srcPy/pipeline/orchestrator.py` | Build ScreeningReportBuilder after validate_bundle(), map gates via gate_to_screening, write_screening_report() before write_bundle_manifest(); full 64-char screening_run_id. |
| `pyproject.toml` | [tool.poetry.plugins."marketmind.signals"] with five starter signal entry points. |
| `tests/python/unit/registry/` | test_signal_catalog.py, test_screening_report.py, test_gate_to_screening.py. |
| `tests/python/integration/backtesting/test_orchestrator_backtesting_artifacts.py` | Assert screening_report.json present and has schema_version, candidates, summary. |
| `srcPy/cli/gate.py` | Phase I-E hardening: require `stat_validity_report.json` and `execution_assumptions.json` on the canonical governed path, require `pbo` with range validation, preserve invalid-input behavior for malformed policy artifacts, and fail zero-cost execution assumptions. |
| `tests/unit/cli/test_gate.py` | Added canonical-policy coverage for missing `stat_validity_report.json`, missing top-level `pbo`, malformed `pbo.value`, invalid nested `pbo.gate_result`, missing execution assumptions, zero-cost execution assumptions, and valid non-zero execution assumptions. |
| `srcPy/backtesting/validation/statistical/pbo_bridge.py` | Added the thin CPCV-to-PBO bridge that converts evaluated CPCV outputs into canonical validator-side `path_pairs` using `net_sharpe`, while rejecting duplicate `(trial_id, path_id)` pairs and incomplete rectangular score surfaces. |
| `srcPy/backtesting/validation/statistical/validator.py` | Canonical validator-side PBO integration: resolves `pbo_path_pairs` or bridged `cpcv_evaluations`, computes PBO through `pbo.py`, aligns DSR `n_trials` to the score surface, and keeps statistical computation out of `gate.py`. |
| `srcPy/backtesting/validation/statistical/report.py` | `stat_validity_report.json` now always emits top-level `pbo` in schema `v1`, preserves validator-supplied `pbo.gate_result`, and aggregates top-level `gate_result` across DSR, minTRL, bootstrap CI, and PBO. |
| `tests/python/unit/backtest/test_stat_validity.py` | Added deterministic coverage for report emission, schema `v1` retention, top-level `gate_result` aggregation including PBO, validator-side CPCV bridging, and degenerate PBO input handling. |
| `srcPy/strategies/momentum.py` | Added `AlphaIR`, `FeatureFlagError`, and `MomentumStrategy` with eight registered momentum variants, canonical `features_plan()` wiring to `_OP_REGISTRY` keys, governed PIT provenance validation inside `generate_signal()`, cross-sectional IC gating at a minimum 10-asset universe, and a `generate_trade_intent()` override that unwraps `AlphaIR.signal` before delegating through regime/sizer/risk behavior. |
| `srcPy/preprocessor/graph/ops_custom.py` | Added `XSecRank`, `VolScale`, `ResidualOLS`, `ResidualKF`, and `IndustryScore` ops plus Polars lowerings for the `momentum.*` registry. `momentum.xsec_rank` now computes a lagged lookback signal per asset and ranks it cross-sectionally within each date; `momentum.vol_scale` annualizes with `sqrt(252)` and fail-closed denominator guards; Kalman lowering remains an explicit Phase III `NotImplementedError` tied to OI-MOM-005. |
| `srcPy/preprocessor/graph/factory.py` | Registered all five `momentum.*` ops in `register_builtin_ops()` so `MomentumStrategy.features_plan()` resolves entirely through the canonical op registry. |
| `tests/python/unit/strategies/test_momentum.py` | Added deterministic coverage for registry resolution, feature-plan stability, Kalman feature-flag gating, stable `AlphaIR` return semantics, PIT provenance propagation, cross-sectional IC behavior (`None` below 10 assets; computed at 10+), and trade-intent unwrapping. |
| `tests/python/unit/preprocessor/test_momentum_ops.py` | Added deterministic/property coverage for momentum-op registry presence, IR contracts, true same-date cross-sectional ranking semantics, vol-scale denominator guards and annualization, and deferred Kalman lowering behavior. |
| **Type-safety (mypy --strict)** | |
| `srcPy/preprocessor/utils/columns.py` | Typed `_as_list(x: Union[str, List[str], Tuple[str, ...], None]) -> List[str]` and `_derive_out_names(..., out_col: Union[str, List[str], None]) -> List[str]`. |
| `srcPy/preprocessor/graph/ops_custom.py` | `_HasContract` Protocol for `_ProvidesMixin._with_contracts`; TYPE_CHECKING import of `polars`; full signatures for `_delegate_to_backend` and all `lower_*_polars` (ir, lf, group_by) with return `pl.LazyFrame` or `pl.DataFrame`; `lower_residual_kf_polars` accepts `lf` or `None`; `cast(..., _apply_eager(...))` on returns. |
| `pyproject.toml` | Dev dependency `pandas-stubs = "^2.2"`. |
| `srcPy/strategies/momentum.py` | `generate_signal(...) -> AlphaIR` with `# type: ignore[override]`. |
| `tests/python/unit/preprocessor/test_momentum_ops.py` | `pl = None  # type: ignore[assignment]` on ImportError; `cast(pl.LazyFrame, lower_*_polars(...))` before `.collect()` where needed. |

### Behavioral Changes

* Every run that goes through the canonical orchestrator and gate validation now emits `screening_report.json` in the bundle with one candidate per strategy evaluated, stages derived from gate results (INTAKE for files_exist/json_valid, LANE_0 for sharpe_threshold/max_drawdown), and reason_family always derived from REASON_CODE_TO_FAMILY.
* SignalCatalog is available via `get_catalog()` with five starter signals registered at slots 0–4; new signals can be registered with stable slot_index for Phase II replay compatibility.
* The governed strategy layer now includes a canonical momentum slice: `MomentumStrategy.features_plan()` resolves through `_OP_REGISTRY`, `generate_signal()` has a stable `AlphaIR` contract, and trade-intent generation unwraps `AlphaIR.signal` without redefining the public signal interface.
* Cross-sectional momentum semantics are now explicit in both strategy and op layers: `momentum.xsec_rank` ranks across assets within a date, not across time for one series, and `information_coefficient` remains `None` unless the cross-section has at least 10 assets.
* Canonical governed stat-validity emission now includes a top-level `pbo` section in `stat_validity_report.json` while keeping `schema_version = "v1"`; the report's top-level `gate_result` now reflects DSR, minTRL, bootstrap CI, and PBO, and malformed `pbo` values or malformed nested gate payloads remain invalid-input failures rather than recomputation triggers.
* Canonical governed bundle validation now requires `execution_assumptions.json`; missing assumptions and zero-cost assumptions fail the gate instead of passing with evidence-only warnings, while valid non-zero assumptions still pass.
* `mypy --strict` passes for `srcPy/strategies/momentum.py`, `srcPy/preprocessor/graph/ops_custom.py`, and the unit tests `test_momentum.py` and `test_momentum_ops.py`; pandas usage is typed via `pandas-stubs`.

### Breaking Changes

* Canonical governed bundle validation is stricter in 4.5.0: missing `stat_validity_report.json`, missing `execution_assumptions.json`, malformed or missing `pbo`, and zero-cost execution assumptions now fail where earlier compatibility behavior could pass with warnings or evidence-only signals.

### Companion Document Updates (specific edits)

Apply the following updates so companion docs reflect 4.5.0 and Phase I-E substrate delivery.

| Document | Location | Update |
|----------|----------|--------|
| **ImplementationPlan.md** | Line 10 (title page) | Change `VERSION.md 4.4.2` → `VERSION.md 4.5.0`. |
| **ImplementationPlan.md** | Line 25–27 (Executive Summary) | After the sentence that ends with "Phase I-D lands the first non-toy strategy vertical slice...", add: "Phase I-E (SignalFactory substrate) is now partially delivered in 4.5.0: `srcPy/registry/` provides SignalCatalog with stable slot_index at registration and five starter signals, and `screening_report.json` is emitted for every strategy evaluation run with two-tier rejection taxonomy and REASON_CODE_TO_FAMILY." Change "Phase I-E and Phase I-F now carry" → "Phase I-F now carries" (and adjust the following clause to "complete the remaining gate/governance surface..."). |
| **ImplementationPlan.md** | RECENT_CHANGES table (~line 31) | Add row: "4.5.0 sync \| March 2026 \| Phase I-E SignalFactory substrate: srcPy/registry/ (SignalCatalog, slot_index, screening_taxonomy, screening_report builder, gate_to_screening), screening_report.json in bundle, schemas/screening_report.schema.json." |
| **ImplementationPlan.md** | §4.6 Phase I-E (line ~525) | After "Phase I-E completes the gate surface...", add one sentence: "The Phase I-E amendment (SignalFactory substrate) delivered in 4.5.0 adds the SignalCatalog with slot_index and screening_report.json emission so the bundle and signal identity are Phase II–ready; remaining Phase I-E work (stat validity/cost/data lineage gate verification, backtesting/storage retirement) is unchanged." |
| **ImplementationPlan.md** | Line 2042 (footer) | Change `VERSION.md 4.4.2` → `VERSION.md 4.5.0`. |
| **TechnicalRoadmap.md** | Line 8 (title page) | Change `VERSION.md 4.4.2` → `VERSION.md 4.5.0`. |
| **TechnicalRoadmap.md** | Signal registry row (~line 58) | Change "No Signal ABC, no catalog, no CAS for signals. Phase II: each signal must carry task_embedding field" to "Phase I-E (4.5.0): SignalCatalog in srcPy/registry/ with slot_index at registration and five starter signals; screening_report.json emitted per run. Phase II: task_embedding (signal_embedding) and meta-learner integration." |
| **TechnicalRoadmap.md** | Phase I subphases paragraph (~line 839) | After "Phase I-D is delivered in 4.4.0...", add: "Phase I-E (SignalFactory substrate) is partially delivered in 4.5.0: SignalCatalog + slot_index and screening_report.json with taxonomy and gate_to_screening mapping." |
| **TechnicalRoadmap.md** | Line 947, 1091 (VERSION.md refs) | Change `4.4.2` → `4.5.0`. |
| **MetaLearningArchitectureVision.md** | Line 8 (title page) | Change `VERSION.md 4.4.2` → `VERSION.md 4.5.0`. |
| **MetaLearningArchitectureVision.md** | §8b Post-3.6.0 Additions (~line 542) | Change "through v4.4.0" → "through v4.5.0". Add bullet: "SignalCatalog + slot_index (4.5.0): srcPy/registry/signal_catalog.py implements Signal ABC with slot_index assigned at registration; five starter signals; screening_report.json and REASON_CODE_TO_FAMILY in srcPy/registry/ for Phase II funnel analytics." |
| **MetaLearningArchitectureVision.md** | Line 578, 584 (VERSION.md refs) | Change `4.4.2` → `4.5.0`. |
| **MetaLearningCore.md** | Line 8, 30 (title page / table) | Change `VERSION.md 4.4.2` → `VERSION.md 4.5.0`. |
| **MetaLearningCore.md** | Strategy registry & feature path row (~line 565) | Append: "Phase I-E (4.5.0) adds srcPy/registry/signal_catalog.py (SignalCatalog, slot_index) and screening_report.json emission with screening_taxonomy and gate_to_screening." |
| **MetaLearningCore.md** | Current state paragraph (~line 651) | Add: "Phase I-E SignalFactory substrate (4.5.0) delivers SignalCatalog with slot_index and screening_report.json so the bundle and signal identity are Phase II–ready." |
| **MetaLearningCore.md** | Line 781 (footer) | Change `VERSION.md 4.4.2` → `VERSION.md 4.5.0`. |
| **README.md** | Line 12 (title page) | Change `VERSION.md 4.4.2` → `VERSION.md 4.5.0`. |
| **README.md** | Line 166 (Version) | Change "4.4.0 \| Phase 0 complete... Phase I-D strategy slice" to "4.5.0 \| Phase 0 complete; Phase I-B/C/D delivered; Phase I-E SignalFactory substrate (SignalCatalog + slot_index, screening_report.json) delivered." |
| **README.md** | Line 198 | Add after "Phase I-D lands \`stat_arb_pairs\`...": "Phase I-E (4.5.0) adds SignalCatalog with slot_index and screening_report.json per run. Remaining Phase I work is I-E gate verification plus I-F architecture closure." Adjust "Remaining Phase I work is I-E" to "Remaining Phase I work is I-F" if that sentence follows. |
| **README.md** | Line 937 (RECENT_CHANGES) | Add row: "4.5.0 \| March 2026 \| Phase I-E SignalFactory substrate: srcPy/registry/ (SignalCatalog, screening_report, taxonomy, gate_to_screening), screening_report.json in bundle." |
| **README.md** | Line 946 (Next) | Change "4.5.x (Phase I-E / I-F" to "4.5.x (Phase I-F" and "gate completeness" to "remaining gate verification and architecture closure". |
| **README.md** | Line 925, 961 (VERSION.md refs) | Change `4.4.2` → `4.5.0`. |
| **FormattingSpec.md** | Line 8 | Change `VERSION.md 4.4.2` → `VERSION.md 4.5.0`. |
| **ResolutionLedger.md** | `docs/src/ResolutionLedger.md` (title page + DOCBODY wrappers) | Added `ResolutionLedger` as a new bumpable suite companion document for 4.5.0; wrapped title page and content in `MM:BEGIN:TITLEPAGE` / `MM:END:TITLEPAGE` and `MM:BEGIN:DOCBODY` / `MM:END:DOCBODY` so it compiles into `docs/out/<release>/ResolutionLedger.docx` and participates in companion version sync. |
| **ImplementationPlan.md** | §4.6 Phase I-E | Record that canonical `gate.py` now requires `stat_validity_report.json` and `execution_assumptions.json`, requires `pbo`, and fails zero-cost execution assumptions on governed bundles. |
| **TechnicalRoadmap.md** | Gate status rows / execution-cost notes | Update Phase I-E status to reflect required `pbo`, required governed execution assumptions, and zero-cost FAIL policy on the canonical gate path. |
| **README.md**, **MetaLearningCore.md**, **WhitePaper.md** | Phase I status summaries | Move Phase I-E gate hardening from “remaining verification” into delivered 4.5.0 behavior and leave Phase I-F / data-lineage closure as the primary remaining follow-on work. |
| **ImplementationPlan.md** | Appendix H.8 / H.9 | Correct the live governed `stat_validity_report.json` contract to schema `v1`, document top-level `pbo` plus aggregated `gate_result`, and keep Harvey-t / CPCV-config / feature-stability fields as future-phase extensions rather than the current governed artifact contract. |
| **TechnicalRoadmap.md** | Statistical validity row / current-state notes | Record that governed stat-validity emission now writes top-level `pbo` in the live `v1` contract and that validator-side CPCV evaluations bridge into canonical `path_pairs`; keep deeper CPCV/PBO promotion gating as Phase II work. |
| **README.md**, **MetaLearningCore.md**, **WhitePaper.md** | Phase I current-state summaries | Record that the canonical statistical validator/report path now emits top-level `pbo` in `stat_validity_report.json`, with validator-side CPCV score-surface bridging and top-level gate aggregation, while deeper promotion gating remains a Phase II concern. |

### Validation

| Check | Result |
|-------|--------|
| pytest tests/python/unit/registry/ | 18 passed. |
| pytest test_orchestrator_backtesting_artifacts | screening_report.json present and structured. |
| mypy srcPy/registry/ | Clean. |
| mypy --strict srcPy/strategies/momentum.py srcPy/preprocessor/graph/ops_custom.py tests/python/unit/strategies/test_momentum.py tests/python/unit/preprocessor/test_momentum_ops.py | Success; no issues in 4 source files. |
| `python -m py_compile srcPy/backtesting/validation/statistical/pbo_bridge.py srcPy/backtesting/validation/statistical/report.py srcPy/backtesting/validation/statistical/validator.py tests/python/unit/backtest/test_stat_validity.py tests/unit/cli/test_gate.py` | Syntax validation for the Phase I-E statistical-validity bridge and focused tests passed in this thread. |
| Direct Phase I-E contract checks | Verified top-level `pbo`, schema `v1`, aggregated `gate_result`, validator-side CPCV bridging, strict `PBO > 0.50` failure behavior, and duplicate/incomplete score-surface rejection. |
| Targeted pytest for the Phase I-E stat-validity slice | Not completed in this thread because the local `.venv-codex` environment lacked `scipy` and Windows temp-dir cleanup raised `WinError 5` even with `--basetemp`. |

---

## Version 4.4.2 (2026-03-17)

Changelog for **companion documentation cleanup and DOCX typography normalization**: the five companion Markdown sources now drop managed `RELEASE_NOTE` blocks, standalone `✦ v...` callouts, stale companion-version suffixes, and `*Architecture source:*` footers; `TechnicalRoadmap.md` compresses the targeted §2 research-topic sections into decision bullets and renames the §3 execution tasks from `P1`-`P15` to `T1`-`T15`; and the docs formatting spec plus Python DOCX renderer/reference-doc generator are aligned to the smaller body/heading/table/code typography requested for the companion suite. This is a PATCH release because it updates editorial content and documentation-rendering presentation only; no trading runtime behavior, gate contracts, schemas, or public APIs change.

### Detailed Changes

| Location | Change |
|----------|--------|
| `docs/src/TechnicalRoadmap.md` | Removed release-note/callout clutter, collapsed the five targeted `Research Topics` sections to compact implementation-focused bullets, and renamed the §3 execution task labels to the `T1`-`T15` series with cross-references updated. |
| `docs/src/ImplementationPlan.md` | Removed the managed release-note block, standalone version callouts, stale inline release suffixes, and `*Architecture source:*` footers while preserving existing `*Source:*` citations and companion structure. |
| `docs/src/MetaLearningCore.md` | Removed the managed release-note block and stale companion-version suffixes, and normalized DOCMAP/source-stamp prose to versionless companion references. |
| `docs/src/MetaLearningArchitectureVision.md` | Removed the managed release-note block and stale companion-version suffixes, and normalized companion-reference prose and DOCMAP metadata. |
| `docs/src/README.md` | Removed the managed release-note block, remaining standalone `✦ v...` callouts, and stale companion-version suffixes while preserving suite navigation and source citations. |
| `docs/src/FormattingSpec.md` | Updated the documentation formatting reference to 10pt body, 13pt H1, 11pt H2, 10pt H3, 10pt table body, 9pt code, and reduced H1 spacing. |
| `devtools/docs/rendering/post_process.py` | Updated the runtime DOCX post-processor so generated companion documents enforce the new heading/body/code/table typography and tighter H1 spacing. |
| `devtools/docs/resources/create_reference_docx.py` | Updated the reference-doc generator so built-in paragraph styles and title-page styles match the normalized companion-suite typography. |

### Behavioral Changes

* Generated DOCX companion output now renders with smaller body/headings/code typography and reduced H1 spacing.
* Companion prose and managed metadata blocks no longer carry stale release-note callouts or embedded companion-document version suffixes.
* `TechnicalRoadmap.md` now uses `T1`-`T15` for §3 execution tasks, avoiding collision with the separate Research Agenda priority labels.

### Breaking Changes

None intended. Document content is editorially cleaner and the DOCX presentation is smaller, but no code-facing contracts or runtime entry points change.

### Companion Document State

| Document | State after 4.4.2 |
|---|---|
| `docs/src/TechnicalRoadmap.md` | Editorial cleanup applied; §2 targeted research-topic blocks compacted; §3 task labels normalized to `T1`-`T15`. |
| `docs/src/ImplementationPlan.md` | Editorial cleanup applied; stale release callouts and architecture-source footers removed. |
| `docs/src/MetaLearningCore.md` | Editorial cleanup applied; companion references/DOCMAP normalized. |
| `docs/src/MetaLearningArchitectureVision.md` | Editorial cleanup applied; companion references/DOCMAP normalized. |
| `docs/src/README.md` | Editorial cleanup applied; stale release callouts removed. |
| `docs/src/FormattingSpec.md` | Typography reference synchronized to the reduced DOCX sizes. |

### Validation

| Check | Result |
|-------|--------|
| `docs/src/*.md` cleanup search | No remaining `RELEASE_NOTE`, `✦ v`, bare release parentheticals, or `Architecture source:` hits in the five companion sources. |
| `TechnicalRoadmap.md` task-label audit | `### T1`-`### T9` headings present; no `### P1`-`### P9`; no remaining `P1`-`P15` execution-label references. |
| DOCMAP audit | Companion DOCMAP version cells now render as `—`. |
| Citation preservation | `Strategy I/O Contract v2` and `*Source:` lines remain present where required. |
| Line endings | The five companion Markdown sources were rewritten and verified as CRLF-only. |
| Python syntax | `devtools/docs/rendering/post_process.py` and `devtools/docs/resources/create_reference_docx.py` compile via `py_compile`. |

### Deferred

* No Phase I-E / I-F implementation work is included in 4.4.2; this release is limited to companion-doc cleanup and docs-rendering presentation alignment.
## Version 4.4.1 (2026-03-14)

Changelog for **companion documentation synchronization through the delivered 4.3.0 and 4.4.0 Phase I milestones**: `docs/src/ImplementationPlan.md`, `TechnicalRoadmap.md`, `README.md`, `MetaLearningCore.md`, `MetaLearningArchitectureVision.md`, and `WhitePaper.md` now describe Phase I-C as delivered (single-path governed feature execution, canonical op-floor expansion, and feature-layer leakage evidence) and Phase I-D as delivered (`stat_arb_pairs` on the canonical PIT-safe path with `execution_assumptions.json` and `stat_validity_report.json` emitted in the run bundle). This is a PATCH release because it updates companion documentation and release metadata only; no runtime behavior, contracts, schemas, or public APIs change.

### Detailed Changes

| Location | Change |
|----------|--------|
| `docs/src/ImplementationPlan.md` | Updated the executive summary, codebase reality map, Phase I-C / I-D status, and source stamp to reflect the delivered 4.3.0 / 4.4.0 state instead of treating those milestones as future work. |
| `docs/src/TechnicalRoadmap.md` | Updated feature inventory and PIT status language to record the delivered canonical op floor, governed feature-path lock, and live `stat_arb_pairs` vertical slice. |
| `docs/src/README.md` | Bumped companion metadata to 4.4.0, refreshed the current-status narrative, and replaced outdated `stat_arb.py` / Phase I future-state wording with the live `stat_arb_pairs` path. |
| `docs/src/MetaLearningCore.md` | Refreshed companion references and Phase I prerequisite language so the meta-learning docs assume the delivered Phase I-C / I-D substrate. |
| `docs/src/MetaLearningArchitectureVision.md` | Extended the post-3.6.0 architecture addendum through 4.4.0, including ADR-008 acceptance and the canonical stat-arb package spine. |
| `docs/src/WhitePaper.md` | Refreshed companion metadata and current-state language so Phase I-C and the first Phase I-D strategy slice are recorded as delivered. |

### Behavioral Changes

None. This release updates documentation only.

### Companion Document Versions

| Document | Previous | New |
|---|---|---|
| `docs/src/README.md` | 4.2.0 | 4.4.0 |
| `docs/src/ImplementationPlan.md` | Synced through 4.2.0 | Synced through 4.4.0 |
| `docs/src/TechnicalRoadmap.md` | Synced through 4.2.0 | Synced through 4.4.0 |
| `docs/src/MetaLearningCore.md` | Companion refs through 4.2.0 | Companion refs through 4.4.0 |
| `docs/src/MetaLearningArchitectureVision.md` | Post-3.6.0 addendum through 4.2.0 | Post-3.6.0 addendum through 4.4.0 |
| `docs/src/WhitePaper.md` | Current-state language through 4.2.0 | Current-state language through 4.4.0 |

### Deferred

* No code-path changes are included in 4.4.1; Phase I-E / I-F implementation work remains governed by subsequent releases.

## Version 4.4.0 (2026-03-14) Phase I-D stat-arb pairs

Changelog for **Phase I-D stat-arb vertical slice on canonical PIT-safe plumbing**: the preprocessor graph now has executable Polars lowerings for `pairs.beta`, `pairs.spread`, and `stats.half_life`, wired through the ADR-001 graph executor path; a new `srcPy/strategies/stat_arb/` package implements `StatArbPairsStrategy(PipelineStrategy)` with a frozen `PairsConfig` (including `hedge_estimator`) and a thin `entry.run_stat_arb_pairs()` wrapper that assembles PIT-safe `StrategyContext` inputs from `DataView` / `DataViewAsOfAdapter` / `PITSafeDataView`. The `stat_arb_pairs` strategy key resolves via `StrategyRegistry` to `srcPy.strategies.stat_arb.pairs.StatArbPairsStrategy`, features are materialized exclusively via `_OP_REGISTRY` graph ops, and the governed path emits both `execution_assumptions.json` and `stat_validity_report.json` into the canonical run bundle. Deterministic unit/bridge tests cover the new lowerings and strategy wiring, and an opt-in `@pytest.mark.net` Yahoo SPY/QQQ smoke test validates the live PIT-safe source path for 2022.

Phase I-Db follow-on work now also lands in the 4.4.0 line: `srcPy/strategies/stat_arb/` has been reshaped into the canonical long-term package spine with a live `common/` subtree for pairs-safe helpers, placeholder-only `artifacts/`, explicit deferred root stubs (`formation.py`, `signal_ops.py`, `risk_gates.py`, `validators.py`), and future-facing `dimensions/` / `control/` scaffolds that are import-safe and fail closed on use. The live pairs runtime remains rooted in `srcPy.strategies.stat_arb.pairs`, lazy strategy loading now imports that canonical module path directly, coverage omits exclude scaffold-only files, and a structural package-spine smoke test locks the live-versus-deferred boundary without broadening runtime behavior.

### Major Themes Across All Changes

* **Governed stat-arb execution now has a canonical pairs slice:** Phase I-D keeps `pairs.py` as the only executable stat-arb strategy and routes registry resolution to `srcPy.strategies.stat_arb.pairs.StatArbPairsStrategy`.
* **Phase I-Db package growth no longer requires a later migration:** the stat-arb slice now has its canonical `common/`, `artifacts/`, `dimensions/`, and `control/` package spine while preserving the current pairs-only execution boundary.
* **Deferred boundaries are explicit and fail closed:** future multileg, control, and reporting modules import safely, avoid registration side effects, and raise `NotImplementedError` on concrete use.
* **Phase I-D runtime:** Entry is a thin wrapper delegating to `orchestrator.run()`; graph lowerings for `pairs.beta`, `pairs.spread`, and `stats.half_life` execute via the canonical op registry; gate_status is computed from half-life band and signal count; schema_version unified to `"1.0"` in artifact payloads.

### Detailed Changes

| Location | Change |
|----------|--------|
| `srcPy/preprocessor/graph/ops_custom.py` | Phase I-D: Implemented Polars lowerings for `pairs.beta` (rolling OLS), `pairs.spread`, and `stats.half_life` (AR(1) half-life, clamp [1, 252]); PairBeta default method `ols`. |
| `srcPy/data/dataview_asof_adapter.py` | Phase I-D: Added `as_wide_frame(knowledge_dates)` returning one row per date with both legs’ close columns for PIT-safe pair join. |
| `srcPy/pipeline/orchestrator.py` | Phase I-D: Added generic `run(strategy_id, ctx, strategy_kwargs, bundle_dir, ...)` for engine resolution, bundle writing, and validator coordination; entry delegates here. |
| `srcPy/strategies/stat_arb/entry.py` | Phase I-D: Thin wrapper only—registers sources, builds adapter and wide frame, sets `pit_provenance`, delegates to `orchestrator.run()`; no direct engine/validator/manifest logic. |
| `srcPy/backtesting/storage/bundle_writer.py` | Phase I-D: Added read helpers (`read_plan`, `read_env_fingerprint`, `read_dataset_manifest`, `read_preprocessing_report`, `read_splits_manifest`) for RunBundle construction. |
| `srcPy/cli/gate.py` | Phase I-D: `stat_validity_report.json` schema_version accepts `"1.0"` or `"v1"` for gate compatibility. |
| `srcPy/strategies/stat_arb/common/` | Added the live pairs-safe helper subtree with canonical column-name types, feature-contract checks, and diagnostics/payload builders used by the current pairs runtime without introducing a second execution path. |
| `srcPy/strategies/stat_arb/artifacts/` | Replaced the flat `artifacts.py` module with a placeholder-only package containing import-safe schema and signal-card stubs for future reporting work. |
| `srcPy/strategies/stat_arb/dimensions/`, `srcPy/strategies/stat_arb/control/`, `srcPy/strategies/stat_arb/formation.py`, `srcPy/strategies/stat_arb/signal_ops.py`, `srcPy/strategies/stat_arb/risk_gates.py`, `srcPy/strategies/stat_arb/validators.py` | Added explicit deferred Phase I-Db / Phase II scaffolds that import safely, avoid registration side effects, and raise `NotImplementedError` on concrete use. |
| `srcPy/strategies/stat_arb/pairs.py`, `srcPy/strategies/stat_arb/__init__.py`, `srcPy/strategies/pipeline_strategy.py` | Kept the live pairs runtime rooted at `srcPy.strategies.stat_arb.pairs`, moved registration to the canonical module for lazy lookup, limited package-root exports to live surfaces, and preserved the `stat_arb_pairs` registry key without registering deferred scaffolds. |
| `tests/python/unit/preprocessor/test_expr_ops_executor.py` | Phase I-D: Numeric correctness for `pairs.beta` (a=2*b → beta ≈ 2.0) and `stats.half_life` ([1, 252]); PairBeta method `ols`; lowering error paths (missing columns, tiny input); constant-b denom=0; PairSpread explicit beta_col; RollingZ validation. |
| `tests/python/unit/strategies/test_stat_arb_pairs_strategy.py` | Phase I-D: features_plan op order, generate_signal discrete {-1,0,+1}, KALMAN guard; behavior tests (entry on low/high z-score, exit on mean reversion, max_hold, half-life filter blocks/allows); generate_signal TypeError/ValueError; write_artifacts branches (None signals/feats, missing z/hl columns, empty valid_hl). |
| `tests/python/integration/test_stat_arb_vertical_slice.py` | Phase I-D: Deterministic PIT-safe path and artifact emission; opt-in `@pytest.mark.net` Yahoo SPY/QQQ smoke; entry validation (run_cfg.prices required, symbol/valid_time/knowledge_time, knowledge_dates from iso string, default bundle_dir). |
| `pyproject.toml` | Added coverage omissions for scaffold-only stat-arb files so Phase I-Db placeholders do not weaken the live coverage contract. |
| `tests/python/unit/strategies/test_stat_arb_package_spine.py` | Added a D0 structural smoke test covering package import safety, root live exports, deferred module import safety, and explicit stub failures on invocation. |

### Behavioral Changes

* The stat-arb package now exposes the canonical long-term package spine while keeping the executable surface strictly pairs-only.
* Live artifact payload assembly remains in the pairs runtime path, while the new `artifacts/` namespace stays placeholder-only and outside current execution.
* Deferred dimensions, control, and artifact namespaces import cleanly but fail closed when invoked, preventing accidental runtime broadening.
* Phase I-D: Wide frame for the pair is produced by `DataViewAsOfAdapter.as_wide_frame(knowledge_dates)`; strategy artifact payloads (execution_assumptions, stat_validity_report) are built in the pairs path (e.g. via `common.diagnostics`) and written through the bundle store.

### Breaking Changes

None intended. Existing live imports remain rooted in `srcPy.strategies.stat_arb`, the `stat_arb_pairs` registry key is unchanged, and no new executable strategy entry points were added.

### Test / Validation Evidence

| Test file / command | Type | Invariant or contract |
|---------------------|------|-----------------------|
| `tests/python/unit/preprocessor/test_expr_ops_executor.py` | Unit | Phase I-D: pairs.beta and stats.half_life numeric correctness; PairBeta default method ols. |
| `tests/python/unit/strategies/test_stat_arb_pairs_strategy.py` | Unit | Phase I-D: features_plan op order, discrete signals, KALMAN guard, entry/exit/max_hold/half-life behavior. |
| `tests/python/integration/test_stat_arb_vertical_slice.py` | Integration | Phase I-D: Deterministic PIT path and execution_assumptions/stat_validity_report in bundle; Yahoo SPY/QQQ smoke (opt-in net). |
| `tests/python/unit/strategies/test_stat_arb_package_spine.py` | Unit | Locks the Phase I-Db package-spine contract: live root exports stay pairs-only, deferred modules remain import-safe, and stub invocation fails closed. |
| Phase I-D pytest suite (`test_expr_ops_executor`, `test_stat_arb_pairs_strategy`, `test_stat_arb_vertical_slice`, `test_stat_arb_package_spine`) | Validation | Run with `--cov-config=.coveragerc.phase1d`; coverage report below. |

### Coverage Report (Phase I-D scope)

Final line and branch coverage for the Phase I-D–in-scope files:

| File | Line Coverage | Lines Covered | Statements | Branch Coverage | Covered Branches | Total Branches |
|------|---------------|---------------|------------|-----------------|------------------|-----------------|
| `srcPy/preprocessor/graph/ops_custom.py` | 87.48% | 462 | 515 | 76.00% | 76 | 100 |
| `srcPy/strategies/__init__.py` | 100.00% | 6 | 6 | N/A | 0 | 0 |
| `srcPy/strategies/pipeline_strategy.py` | 35.51% | 329 | 821 | 19.75% | 47 | 238 |
| `srcPy/strategies/stat_arb/__init__.py` | 100.00% | 5 | 5 | N/A | 0 | 0 |
| `srcPy/strategies/stat_arb/config.py` | 100.00% | 19 | 19 | N/A | 0 | 0 |
| `srcPy/strategies/stat_arb/entry.py` | 92.45% | 41 | 43 | 80.00% | 8 | 10 |
| `srcPy/strategies/stat_arb/pairs.py` | 100.00% | 70 | 70 | 100.00% | 20 | 20 |

### Deferred

* Multileg stat-arb runtime (`triplets` and above) remains explicitly deferred beyond the live Phase I-D pairs slice.
* Control-theoretic execution, Riccati numerics, xi solving, and stability analysis remain scaffold-only.
* Runtime artifact/report generation under `srcPy/strategies/stat_arb/artifacts/` remains placeholder-only and is not part of the current execution path.
* Phase I-D: HedgeEstimator.KALMAN and `stats.kf_beta` remain unimplemented; requesting KALMAN raises NotImplementedError. Dual PolarsExecutor in executor.py is pre-existing and out of scope.

## Version 4.3.0 (2026-03-13)

Phase I-C closes the gap between PIT-safe split logic and actual feature materialization. Governed supported built-ins now execute on a single canonical graph path, direct legacy execution is blocked in governed contexts, the canonical technical-op floor is expanded, and feature-layer bridge/property coverage now proves DataView-backed execution plus leakage resistance on the trusted feature path. This is a MINOR release because it materially expands governed feature capability and enforcement without changing the public `PipelineStrategy` authoring API.

### Why This Release Exists

Phase I-B proved that the PIT boundary and split geometry were in place. Phase I-C was needed to prove that feature materialization itself could not bypass governed access rules: supported built-ins now lower onto the canonical graph path, governed legacy execution is explicitly forbidden, and the feature layer now has direct PIT/leakage evidence instead of inheriting safety by assumption from upstream split logic.

### Governed Execution Rule

Governed enforcement in this phase applies exactly when `StrategyContext.pit_provenance is not None`; no truthiness-based or placeholder sentinel interpretation was introduced.

### Canonical Lowering Contract

| Legacy step name | Canonical graph op | Phase I-C meaning |
|------------------|--------------------|-------------------|
| `ROLL_MEAN` | `technical.SMA` | Built-in rolling-mean strategies now resolve through canonical graph execution. |
| `ROLL_STD` | `stats.rolling_std` | Rolling standard deviation is now part of the governed canonical op floor. |
| `Z_SCORE` | `scaling.zscore_roll` | Existing rolling z-score behavior stays live and is now covered on the governed leakage path. |
| `EMA` | `technical.EMA` | Exponential moving average is now a canonical built-in op. |
| `RSI` | `technical.RSI` | RSI built-ins resolve through the canonical registry instead of direct legacy execution. |
| `MACD` | `technical.MACD_line_signal` | MACD built-ins lower to the canonical line/signal op; histogram behavior was not redesigned in this phase. |

### Detailed Changes

| Location | Change |
|----------|--------|
| `srcPy/strategies/pipeline_strategy.py` | Added governed-context enforcement keyed to `ctx.pit_provenance is not None`, canonical lowering for supported built-ins, canonical cache descriptors keyed to lowered params/op identity, governed `_FEATURE_OPS` blocking via `MaterializationError`, attr clearing on governed source frames, and pandas-return-after-graph-execution behavior. |
| `srcPy/strategies/migrated_strategies.py` | Updated built-in `features_plan()` implementations so supported strategies emit canonical graph op names instead of legacy feature-op tokens. |
| `srcPy/preprocessor/graph/factory.py` | Extended the built-in op registry and compatibility alias map so supported built-ins lower into canonical graph names without creating a second registry tree. |
| `srcPy/preprocessor/graph/ops_custom.py` | Added concrete op classes and registry wiring for `technical.EMA`, `technical.MACD_line_signal`, `technical.Bollinger`, `technical.ATR`, `technical.OBV`, `technical.VWAP`, and `stats.rolling_std`, while keeping pair-related deferred lowerings explicitly non-executable. |
| `srcPy/preprocessor/graph/backends/polars.py` | Implemented deterministic lowerings for the Phase I-C canonical op floor, including fail-closed governed VWAP behavior and internal graph execution support for pandas-return callers. |
| `tests/python/unit/strategies/test_pipeline_strategy_bridge.py` | Extended the existing bridge suite with canonical plan-emission checks, governed `MaterializationError` coverage, DataView-backed historical-frame proofs, raw-handle exposure checks, delayed pandas conversion assertions, and governed VWAP fail-closed coverage. |
| `tests/python/property/test_preprocessor_leakage.py` | Replaced the Phase I-B-era stub with a real feature-layer Hypothesis battery using the same poison-pill style as split-geometry leakage work, including single-output and multi-output indicator invariants against DataView-backed history. |
| `tests/python/unit/preprocessor/test_expr_ops_executor.py` and `tests/python/unit/preprocessor/test_preprocessor_coverage.py` | Added unit coverage for the expanded op floor, live rolling-zscore behavior, alias registration, and registry completeness. |
| `tests/python/property/test_dataview_pit.py` | Added focused `DataViewAsOfAdapter` coverage for the pre-snapshot `pit_meta()` path and emitted `MarketSlice` provenance metadata contracts. |
| `tests/python/unit/backtesting/test_contracts_roundtrip.py` | Added targeted `contracts.types.to_primitive()` coverage for tuple, `datetime`, and `Enum` normalization. |
| `tests/python/unit/preprocessor/test_preprocessor_coverage.py` | Added focused `graph/backends/polars.py` coverage for registry helper validation, array helper edge cases, VWAP fail-closed branches, eager/lazy lowering paths, and executor collect-policy behavior. |
| `docs/ADR-008-Single-Path-Feature-Execution-Lock.md` | Promoted ADR-008 from Proposed to Accepted once the single-path execution lock landed in code. |
| `docs/phase_i_c_closeout.md` | Added the required closeout ledger covering files changed, invariant counts, canonical-vs-legacy execution paths, repo-path ambiguity resolution, and merge-gate outcomes. |

### Behavioral Changes

* Governed feature materialization now rejects direct `_FEATURE_OPS` execution for supported built-ins and fails loudly with `MaterializationError` when callers attempt to bypass canonical lowering.
* Supported migrated strategies now publish canonical feature plans by default, reducing legacy-token drift between strategy intent and graph execution.
* Internal feature execution for governed contexts now runs through the graph/planner/executor path even when the caller asks for pandas output; pandas conversion happens only after feature materialization completes.
* Governed bridge execution no longer carries raw-source attrs into intermediate feature frames, and negative tests now assert that graph execution does not expose raw source handles on the trusted path.
* `technical.VWAP` now explicitly fails closed on governed daily-only inputs unless session or intraday columns are present.
* Deferred pair-related lowerings remain intentionally non-executable; this release does not start Phase I-D pair runtime work.

### Breaking / Stricter Behavior

No user-facing strategy authoring API break is intended for supported production strategies.

The main enforcement change in this release is that governed direct legacy execution for supported built-ins is no longer allowed: attempts to execute them through `_FEATURE_OPS` now raise `MaterializationError` instead of being treated as an alternate runtime path.

### Test / Validation Evidence

| Test file / command | Type | Invariant or contract |
|---------------------|------|-----------------------|
| `tests/python/unit/strategies/test_pipeline_strategy_bridge.py` | Unit / bridge | Locks canonical plan emission, governed `_FEATURE_OPS` blocking, DataView-backed bridge execution, raw-source isolation, delayed pandas conversion, and governed VWAP fail-closed behavior. |
| `tests/python/property/test_preprocessor_leakage.py` | Property | Locks PIT-safe historical feature computation, poison-pill leakage resistance, and governed indicator correctness for SMA/std/EMA/RSI/MACD/Bollinger/ATR/OBV/z-score. |
| `tests/python/unit/preprocessor/test_expr_ops_executor.py` | Unit | Locks the expanded Phase I-C op floor, deterministic lowering surfaces, and the fact that rolling z-score remains live rather than placeholder-only. |
| `tests/python/unit/preprocessor/test_preprocessor_coverage.py` | Unit | Locks canonical registry membership and compatibility alias registration for the Phase I-C op floor. |
| `tests/python/property/test_dataview_pit.py` | Property | Locks the remaining `DataViewAsOfAdapter` PIT metadata branches, including the `None` pre-snapshot path and `MarketSlice` provenance emission after `as_of()`. |
| `tests/python/unit/backtesting/test_contracts_roundtrip.py` | Unit | Locks `contracts.types.to_primitive()` normalization for tuple containers plus `datetime` and `Enum` values used by contract serialization. |
| `tests/python/unit/preprocessor/test_preprocessor_coverage.py` | Unit | Extends the Polars backend evidence to cover helper validation, array edge cases, VWAP fail-closed branches, eager lowering paths, and executor collect-policy decisions. |
| `docs/phase_i_c_closeout.md` | Merge-gate ledger | Records the manual audit result, invariant count, canonical-versus-legacy execution paths, and the final gate readout for Phase I-C, including 39 combined in-scope PIT/leakage invariants and the governed-path raw-source isolation check. |

### Companion Document Versions

| Document | Previous | New |
|----------|----------|-----|
| `docs/ADR-008-Single-Path-Feature-Execution-Lock.md` | Proposed | Accepted (Phase I-C implemented 2026-03-13) |
| `docs/phase_i_c_closeout.md` | — | Added |

No companion DOCX-suite source versions were bumped as part of this implementation-only Phase I-C closeout.

### Deferred

* Pair-runtime lowerings such as `pairs.beta`, `pairs.spread`, and related Phase I-D pair/stat-arb execution work remain explicitly deferred and non-executable.  <!-- Updated by Phase I-D: see 4.4.0 entry. -->
* `technical.MACD_hist` and rolling z-score were not redesigned in this phase; rolling z-score stays live and covered, while histogram behavior remains on its pre-existing implementation path.
* No intraday/session-aware daily VWAP approximation was introduced; governed daily VWAP remains fail-closed until real session-aware data is available.
* Full removal of all non-governed legacy compatibility execution remains later cleanup work after equivalent canonical lowering coverage is complete across the remaining exploratory paths.

## Version 4.2.0 (2026-03-12)

Changelog for **Phase I-B source adaptation into the sovereign PIT path and proprietary governance hardening**: source adapters now own their bitemporal columns for the governed daily path, Yahoo historical daily OHLCV is wired as a PIT-ready source, FRED now exposes an explicit vintage seam with a named Phase I approximation stub, market-data source contracts are split from runtime helpers behind a compatibility shim, CI excludes `@pytest.mark.net` tests from the default run, and the legal/governance surface is aligned with the proprietary LICENSE via new risk/governance documents, clarified security/privacy policies, and explicit non-expansion of rights. This is a MINOR release because it expands the PIT-safe source surface and formalizes governance/legal documentation without changing the locked Phase I-A PIT contracts or broadening user rights.

Version: 4.2.0 (Phase I-B source adaptation milestone: `file.py` emits native temporal columns without relying on orchestrator synthesis, `yahoo_fetcher.py` produces PIT-ready daily OHLCV output, `fred.py` exposes a replaceable vintage seam with `FREDApproximationStub`, `sources/base.py` becomes a compatibility shim over `contracts.py` and `runtime.py`, the adapted source-to-PIT chain is validated end-to-end in CI, and LICENSE/SECURITY/PRIVACY plus MODEL_CARD/RISK_DISCLOSURE/REPRODUCIBILITY/GOVERNANCE documents are updated or introduced to reflect the proprietary, non-open-source governance stance.)

## Version 4.0.1 (2026-03-11)

Changelog for **explicit absolute-import consolidation in ADR-007 hashing, artifact-registry, and backtesting contracts**: replace intra-package relative imports under `srcPy/artifact_registry/`, `srcPy/backtesting/`, and `srcPy/ops/hashing/` with explicit `srcPy.*` absolute imports to make the ADR-007 hashing surface, artifact-registry contracts, and backtesting substrate easier to reason about and more robust to future package layout changes. This is a PATCH release because it is a purely structural import refactor with no intended behavioral or contract changes.

Version: 4.0.1 (Patch-level import refactor: `srcPy.artifact_registry.*`, `srcPy.backtesting.*`, and `srcPy.ops.hashing.*` now use explicit `srcPy.*` absolute imports instead of intra-package relative imports, aligning the ADR-007 hashing contract and backtesting substrate with the project's preferred import style and simplifying static analysis and tooling.)

### Major Themes Across All Changes

* **Make ADR-007 hashing surfaces explicit and tool-friendly:** The core hashing modules, envelopes, equality-fallback scaffolds, and primitive implementations now import each other via `srcPy.ops.hashing.*`, eliminating relative-import ambiguity in the canonical hashing contract package.
* **Clarify artifact-registry and backtesting contract wiring:** The RunRegistry, CAS helpers, and backtesting contracts/registry now use fully qualified `srcPy.*` imports so the ADR-007 artifact identity story and backtesting substrate can be traced mechanically through import graphs.
* **No behavioral or contract changes intended:** The refactor preserves module contents, public symbols, and test-facing contracts; the only change is how modules reference one another.

### Detailed Changes

| Location | Change |
|----------|--------|
| `srcPy/artifact_registry/__init__.py` | Switched the CAS import from `from .cas import HashRefs, LocalCAS` to `from srcPy.artifact_registry.cas import HashRefs, LocalCAS` so external callers and internal helpers both refer to the same explicit package path. |
| `srcPy/artifact_registry/run_registry.py` | Replaced the relative `from .cas import HashRefs` with `from srcPy.artifact_registry.cas import HashRefs`, keeping all RunRegistry-facing CAS interactions on the explicit ADR-002/ADR-007 package path. |
| `srcPy/backtesting/contracts/protocols.py` | Updated imports for `BacktestPlan` and the contracts types from `from .plan` / `from .types` to `from srcPy.backtesting.contracts.plan` and `from srcPy.backtesting.contracts.types`, making the backtesting Protocols resolvable without relying on relative-import semantics. |
| `srcPy/backtesting/contracts/plan.py` | Replaced `from .errors import DeterminismTierMissingError` with `from srcPy.backtesting.contracts.errors import DeterminismTierMissingError`, keeping determinism-tier enforcement on an explicit, discoverable import path. |
| `srcPy/backtesting/contracts/registry.py` | Replaced `from .errors import UnknownIdError` with `from srcPy.backtesting.contracts.errors import UnknownIdError` so registry error reporting is tied to a stable module path. |
| `srcPy/backtesting/data/__init__.py` | Switched `from .pit import PITSafeDataView, PitUnsafeFrame` to `from srcPy.backtesting.data.pit import PITSafeDataView, PitUnsafeFrame`, making PIT wrapper imports explicit for downstream callers. |
| `srcPy/ops/hashing/__init__.py` | Converted all intra-package imports (`.contract`, `.canonicalizer`, `.envelope`, `.ahm`, and all `.primitives.*` modules) to explicit `from srcPy.ops.hashing...` imports, keeping the public hashing surface aligned with ADR-007's canonical package naming. |
| `srcPy/ops/hashing/ahm.py` | Updated imports of `contract`, `envelope`, and primitive hasher modules from `..hashing.*` to `srcPy.ops.hashing.*`, ensuring the Adaptive Hash Manager depends on the explicit ADR-007 package tree. |
| `srcPy/ops/hashing/envelope.py` | Replaced `from .contract` and `from .equality` with `from srcPy.ops.hashing.contract` and `from srcPy.ops.hashing.equality`, making the HashRef envelope's dependencies visible from the top-level package. |
| `srcPy/ops/hashing/equality.py` | Switched `from .contract` and the TYPE_CHECKING-only `from .envelope import HashRef` to `from srcPy.ops.hashing.contract` and `from srcPy.ops.hashing.envelope import HashRef`, so equality-fallback logic depends on explicit hashing-contract modules. |
| `srcPy/ops/hashing/preimage.py` | Updated `from .contract import HashContractViolation, HashPurpose, SystemInvariant` to `from srcPy.ops.hashing.contract import ...`, preserving the preimage invariant bindings while avoiding relative imports. |
| `srcPy/ops/hashing/canonicalizer.py` | Replaced `from .contract` with `from srcPy.ops.hashing.contract` so canonicalization rules are explicitly tied to the ADR-007 contract definitions. |
| `srcPy/ops/hashing/primitives/blake3_impl.py` | Converted imports of `canonicalizer`, `contract`, and `envelope` to `from srcPy.ops.hashing.canonicalizer import CANON`, `from srcPy.ops.hashing.contract import ...`, and `from srcPy.ops.hashing.envelope import ...`, aligning BLAKE3 primitives with the explicit hashing package. |
| `srcPy/ops/hashing/primitives/hmac_sha256_impl.py` | Updated imports to use `srcPy.ops.hashing.canonicalizer`, `srcPy.ops.hashing.contract`, and `srcPy.ops.hashing.envelope`, so HMAC-SHA256 seed derivation is wired directly to the canonical hashing contract and envelope surfaces. |

### Deferred

* (None for this patch release.)

## Version 4.0.0 (2026-03-11)

Changelog for **ADR-007 v1.1 hashing-contract adoption and artifact-registry path transition**: add the canonical hashing package under `srcPy/ops/hashing/`, stage the required golden-vector suite layout under `tests/golden/adr007/`, introduce the registry-facing attestation facade in `srcPy/artifact_registry/attestation.py`, retarget hashing and artifact-registry tests to the new contract surface, and normalize repo-visible D-tier wording to the ADR-007 v1.1 definitions. This is a MAJOR release because the legacy `srcPy/ops/artifact_registry.py` module path is removed and callers must migrate to the canonical package layout.

Version: 4.0.0 (Canonical ADR-007 hashing contract scaffold: purpose-bound hashing modules in `srcPy/ops/hashing/`, dual-domain CAS/attestation facade in `srcPy/artifact_registry/attestation.py`, golden-vector manifests in `tests/golden/adr007/`, artifact-registry integration anchors, and determinism-tier wording locked to ADR-007 v1.1: D3 — Bitwise, D2 — Semantic, D1 — Topological, D0 — None / Debug.)

### Major Themes Across All Changes

* **ADR-007 becomes the canonical hashing boundary:** Hashing logic, contracts, preimage rules, envelope semantics, equality-fallback law, and primitive surfaces now have one explicit home in `srcPy/ops/hashing/` instead of being implied through older mixed-path helpers.
* **Cross-language certification work is now materially staged in-repo:** The `tests/golden/adr007/` tree records the expected golden-vector locations per primitive, including the CI harness gap that still exists for Python 3.12, C++20, and Java 21 certification.
* **Artifact identity and gate attestation are treated as separate but coupled domains:** The new `srcPy/artifact_registry/attestation.py` facade validates the locked `cas.v1:b3-256` and `attest.v1:jcs-sha256` pairing over the same canonical bytes.
* **Repo-visible determinism terminology is now ADR-007 exact:** Marker descriptions and seed-plugin docs no longer use superseded phrases such as “golden replay,” “regression,” or “exploratory” to describe D-tiers.

### Detailed Changes

| Location | Change |
|----------|--------|
| `srcPy/ops/hashing/contract.py` | Added the canonical ADR-007 enum and invariant surface, including `DTier`, `PersistenceTier`, `AlgoId`, `DomainPrefix`, `HashPurpose`, `SystemInvariant`, and the contract exceptions used by the new hashing package. |
| `srcPy/ops/hashing/preimage.py` | Added the purpose-bound preimage scaffold, including frozen dataclasses for `PreimagePart` and `CompositePreimage`, plus the canonical namespace/length-prefix composition entrypoints that document the locked `namespace_utf8 || u64be(len(...))` rule. |
| `srcPy/ops/hashing/envelope.py` | Added the `HashRef` envelope scaffold and factory surface for persistent hash identities, and made `verify_cache_hit` a backward-compatible re-export from the equality facade so older import sites can converge on one law source. |
| `srcPy/ops/hashing/equality.py` | Added the equality-fallback scaffold, including `EqualityEvidence`, compatibility checks, payload/aux witness hooks, and policy-validation entrypoints for non-cryptographic cache surfaces. |
| `srcPy/ops/hashing/primitives/*.py` | Added per-primitive scaffold modules for BLAKE3, SHA-256/JCS, XXH3, SipHash-2-4, HMAC-SHA256, SimHash, MinHash, and Rabin, each documenting the locked purpose mapping, intended invariants, and implementation gaps. |
| `srcPy/artifact_registry/attestation.py` (new) | Added the registry-facing attestation helper layer: dual-domain hash-pair coercion, CAS/attest validation, gate wire-format conversion, `ArtifactEntry`, `ArtifactAttestor`, `BundleManifestWriter`, and small manifest helpers. |
| `srcPy/ops/artifact_registry.py` | Removed the legacy module path. This is the release’s explicit compatibility break; callers must migrate to `srcPy/artifact_registry/` and the ADR-007 hashing package. |
| `tests/golden/adr007/blake3/`, `jcs_sha256/`, `xxh3/`, `sip24/`, `hmac_sha256/`, `simhash/`, `minhash/`, `rabin/` (new) | Added per-primitive `manifest.json` files and placeholder case assets so every D3 boundary can be paired with an explicit golden-vector location in the repo, even before the full multi-language harness is implemented. |
| `tests/python/unit/hashing/test_preimage.py` | Added structural and contract-focused preimage tests, including dataclass shape/immutability checks and placeholders for exact composite-preimage behavior. |
| `tests/python/unit/hashing/test_equality.py` | Added equality-evidence structural tests, keyword-only API checks for `verify_cache_hit`, and scaffold tests for the equality-fallback law and evidence policy. |
| `tests/python/unit/hashing/test_envelope.py` | Added envelope-structure tests for `HashRef`, keyed-algorithm requirements, `to_id_string()`, and the intended factory/equality behavior. |
| `tests/python/unit/hashing/primitives/test_*.py` | Added primitive-specific unit-test files that lock manifest presence and reserve primitive behavior contracts without falsely certifying unimplemented code paths. |
| `tests/python/unit/artifact_registry/test_cas_store.py` | Reworked the CAS store test file into the dual-domain integration anchor identified by ADR-007: JSON persistence now asserts that CAS and attestation hash the same JCS bytes under different algorithms. |
| `tests/python/unit/artifact_registry/test_attestation.py` (new) | Added focused unit coverage for the attestation facade, including dual-domain validation, gate-hash formatting, bundle-manifest emission, and duplicate-role rejection. |
| `tests/python/_plugins/seeds.py`, `pyproject.toml`, `VERSION.md` | Replaced stale D-tier glossary text with the canonical ADR-007 v1.1 mapping: `d3 = bitwise`, `d2 = semantic`, `d1 = topological`, `d0 = none/debug only`. |

### Behavioral Changes

* Hashing contracts, envelopes, preimage rules, and primitive surfaces now live in `srcPy/ops/hashing/` as the canonical package.
* Artifact-registry attestation is no longer an implicit helper concern; it is modeled explicitly through the new `srcPy/artifact_registry/attestation.py` facade.
* The repo-level determinism marker description now matches ADR-007 v1.1 exactly.
* The repository now contains the reserved golden-vector suite layout required by ADR-007 for D3-capable surfaces, even though certification replay is still incomplete.

### Breaking Changes

* `srcPy/ops/artifact_registry.py` is removed.
  Migration required: update imports to the canonical `srcPy/artifact_registry/` package and the new `srcPy/ops/hashing/` modules.
* Repo-visible D-tier wording now follows ADR-007 v1.1 exactly.
  Migration required: stop using superseded phrases such as “D0 Golden Replay,” “regression,” “statistical-equiv,” or “exploratory” when describing `@pytest.mark.determinism(...)` tiers.

### Test / Validation Evidence

| Test file / command | Type | Invariant or contract |
|---------------------|------|-----------------------|
| `tests/python/unit/hashing/test_preimage.py` | Unit | Locks dataclass structure and the intended composite-preimage API shape for ADR-007 preimage construction. |
| `tests/python/unit/hashing/test_equality.py` | Unit | Locks `EqualityEvidence` structure, keyword-only `verify_cache_hit`, and the intended equality-fallback law surface. |
| `tests/python/unit/hashing/test_envelope.py` | Unit | Locks `HashRef` structure, keyed-algorithm field requirements, and canonical ID-string behavior. |
| `tests/python/unit/hashing/primitives/test_blake3.py`, `test_sha256_jcs.py`, `test_xxh3.py`, `test_siphash.py`, `test_hmac_sha256.py`, `test_simhash.py`, `test_minhash.py`, `test_rabin.py` | Unit | Lock the existence and shape of the per-primitive golden-vector manifest anchors and reserve primitive behavior slots. |
| `tests/python/unit/artifact_registry/test_cas_store.py` | Unit | Locks the dual-domain invariant that CAS and attestation hash the same JCS bytes with different algorithms. |
| `tests/python/unit/artifact_registry/test_attestation.py` | Unit | Locks attestation-facade validation, gate wire-format conversion, and bundle-manifest helper behavior. |
| `python -m py_compile srcPy/ops/hashing/envelope.py tests/python/unit/hashing/test_preimage.py tests/python/unit/hashing/test_equality.py tests/python/unit/hashing/test_envelope.py tests/python/unit/hashing/primitives/test_blake3.py tests/python/unit/hashing/primitives/test_sha256_jcs.py tests/python/unit/hashing/primitives/test_xxh3.py tests/python/unit/hashing/primitives/test_siphash.py tests/python/unit/hashing/primitives/test_hmac_sha256.py tests/python/unit/hashing/primitives/test_simhash.py tests/python/unit/hashing/primitives/test_minhash.py tests/python/unit/hashing/primitives/test_rabin.py tests/python/unit/artifact_registry/test_cas_store.py tests/python/unit/artifact_registry/test_attestation.py tests/python/_plugins/seeds.py` | Validation | Syntax validation for the new and edited Python files passed in this thread. |
| Targeted pytest collection / execution for the hashing slice | Validation | Not completed in this thread because the sandbox Python environment did not expose a working `pytest` entrypoint after local dependency staging. |

### Companion Document Versions

| Document | Version | 4.0.0 impact |
|---|---:|---|
| `docs/src/ImplementationPlan.md` | 1.0.0 | Updated to reflect the canonical `srcPy/ops/hashing/` package, `tests/golden/adr007/` requirement, dual-domain CAS/attestation framing, and retirement of `srcPy/ops/artifact_registry.py`. |
| `docs/src/TechnicalRoadmap.md` | 1.0.0 | Updated to record that the ADR-007 contract surface and repo layout are now staged while cross-language golden-vector harness work and most primitive implementations remain deferred. |
| `docs/src/MetaLearningCore.md` | 1.0.0 | No change in 4.0.0. |
| `docs/src/MetaLearningArchitectureVision.md` | 1.0.0 | No change in 4.0.0. |
| `README.md` | 3.7.2 | No change in 4.0.0. |

### Deferred

* The primitive methods in `srcPy/ops/hashing/` remain scaffold-first and largely unimplemented; this release records the contract surface and test anchors, not a finished runtime hashing subsystem.
* The Python 3.12 / C++20 / Java 21 golden-vector certification harness is still absent from CI; the manifests document the gap, but certification work remains future work.
* No compatibility shim is shipped for the removed `srcPy/ops/artifact_registry.py` path; if downstream import continuity is required, that must be handled in a later compatibility release.

___

## Archived Releases

Full release entries for older versions are preserved in:

- docs/releases/VERSION_4.x.md
- docs/releases/VERSION_3.x.md
- docs/releases/VERSION_2.x.md
- docs/releases/VERSION_1.x.md
