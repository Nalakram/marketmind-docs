**MarketMind**

**Technical Roadmap & Feature Plan**

<!-- MM:BEGIN:TITLEPAGE -->
Version 1.4.31 · April 2026 · Proprietary

Companion documents: Implementation Plan v6.5.10 · Meta-Learning Core v1.2.25 · Meta-Learning Architecture Vision v1.3.6 · Resolution Ledger v1.0.52 · README.md 7.2.3 · VERSION.md 7.2.3
<!-- MM:END:TITLEPAGE -->


*Strategic build order, research sequencing, and go/no-go checkpoints*

*Audience: Internal engineering, technical stakeholders*

<!-- MM:BEGIN:DOCBODY -->

# Purpose

This roadmap defines what to build next, what to validate before building further, and which workstreams are allowed to halt the meta-learning program entirely. It tracks engineering and research together because the adaptive-learning roadmap is evidence-first rather than milestone-first.

# 1. Capability Inventory

This inventory separates what is real today from what is governed future scope.

## 1.1 What Exists Today

| Area | Current Reality | Missing or Deferred |
|---|---|---|
| Canonical research substrate | PIT-safe orchestration, governed bundle emission, lineage, statistical-validity artifacts, and cost assumptions are real | Later phases must extend this substrate rather than fork it |
| Governed strategies and signals | `stat_arb_pairs`, materially advanced momentum, SignalCatalog, and stable `slot_index` exist | Broader governed breadth and signal-factory lifecycle remain later work |
| Validation discipline | Leakage-aware tests, DSR/PBO framing, deterministic artifact expectations, CI discipline, and bundle-local immutable evaluation surfaces are mature on the trusted path | Full promotable meta-learner gate path is not built |
| Meta-learning contracts | Runtime shape and proof burden are documented; MLN-01/02/03 contract slices are implemented (canonical MetaTask/task identity, regime vocabulary lock, confidence attenuation contract) | Context encoder, trainer, allocator, and rollout control are still unbuilt |
| Execution realism | Governed execution assumptions exist as artifacts | TCA loops, paper/live control flow, broker integration, and low-latency paths remain conditional |

**Current release context:** Companion docs align with **`VERSION.md` 7.2.3** / Resolution Ledger **v1.0.52**. Earlier H1, H4, and proper H2 RG-09 evidence surfaces remain documented, but the authoritative **live promotable** posture is the strict H3 successor surface at `runs/rg09_h3_granularity`, recorded as `PASS` with `trainer_commitment_unlocked = true`. **Phase I-G is closed** in README / Implementation Plan truth; **RG-09** / **OI-59** are **II-0** / **non-blocking** follow-on. **Corrected-surface OI-59** is a separate constructibility-only lane (MLN-07 disposition: **`THR-RG09-V20`** superseded; **`THR-RG09-V21`** active; see Architecture Vision §13.2 and Threshold Governance Register §10 / `oi59_mln07_threshold_decision_memo.md`). II-0B is complete as the governed non-promotable artifact lane, and II-0C is complete as a **non-promotable pilot harness**: canonical MetaTask scaffolding, deterministic reference-only encoder stub, XGBoost incumbent comparison plumbing, II-0C wrapper metadata on the unchanged II-0B lane, research-only report shells, frozen reference inputs for drift replay, and fail-closed checks for task identity, governed baseline key discipline, and baseline/shared parity before emission. The suite treats H3 as a successor surface evaluated through the base harness, not as proof that the original H1 surface passed or as the incumbent allocator baseline.

## 1.2 What Remains Hypothetical

- promotable adaptive-learning machinery,
- validated allocator superiority over the frozen baseline,
- execution-serious deployment surfaces,
- and signal-factory-serious automation.

# 2. Evidence-First Sequencing

## 2.1 Execution Plan

1. Hold the I-F closure boundary.
2. ~~I-G empirical and protocol foundation.~~ **Closed** (companion truth, Ledger v1.0.52); active bridge is **II-0** (especially **II-0B** scaffolding).
3. II-0 scaffolding and research harness.
4. II-A through II-E validation-gated build.
5. III-A through III-C conditional execution realism.
6. IV-A through IV-D conditional signal-factory expansion.
7. IV+ frontier extensions.

## 2.2 Guardrail

> **Guardrail.**  
> Phase I-F freezes system truth.  
> Phase I-G freezes research policy, protocols, and proof burden.  
> Phase II-0 implements only the minimum scaffolding needed to test those decisions honestly.  
> Phase II is the first phase allowed to build promotable adaptive-learning machinery.  
> Phase III is the first phase allowed to become execution-serious.  
> Phase IV is the first phase allowed to become signal-factory-serious.  
> Neither I-G nor II-0 may quietly become full Phase II.

## 2.3 What the Roadmap Does Not Assume

- I-G does not imply trainer commitment.
- II-0 does not imply promotable allocator code.
- III does not imply broker/live inevitability.
- IV does not imply current automated signal discovery.
- Reptile is not promotable simply because it is specified.
- Literature-default thresholds are not policy until MarketMind evidence says they are.

## 2.4 Go / No-Go Checkpoints

| Checkpoint | Decision Rule |
|---|---|
| Baseline comparison complete | Continue only if the meta-learning program still has a realistic path to beat the simpler baseline net of costs |
| Task validity clean | Continue only if leakage and exchangeability risks are acceptably controlled |
| Adaptation usefulness proven | Continue only if held-out query gain is real and statistically meaningful |
| Proxy alignment proven | Continue only if the trainer is optimizing a trustworthy target |
| Continual robustness proven | Continue only if nightly adaptation preserves crisis/generalization behavior |

## 2.5 Report-driven sequencing (March 2026 synthesis)

The heaviest **current** obligation sits in **II-0** (honest benchmark, harnesses, pilots, **II-0B** artifact/contract scaffolding) while **I-G** remains a **frozen** policy/phase baseline (companion closure at Ledger v1.0.52). **II-D is not a short epilog** after II-C: it is where **structured post-allocator conditioning** and **deployment-layer realism** convert allocator intent into **governed capital expression**. **Phase III** and **Phase IV** remain **conditional** even when deployment-layer arguments are strong—documentation must not read as “III/IV are next” without that guard.

**Fall backs (explicit):**

- **Invalid regime tasks / non-exchangeability failure:** halt trainer path; do not narrate meta-learning from contaminated episode design.
- **No net uplift vs simpler baseline** (after costs and burden): **no allocator promotion**; **fail gracefully** to incumbent baseline.
- **Routing pilot fails or attenuation subsumes gains:** remain **attenuation-only**; routing does not become default architecture.
- **Unmanaged breadth:** does not enter the program; expand only under **Signal Generation Protocol**, **SignalCatalog** identity, and Phase IV readiness.

## 2.6 Next-gen allocator direction (target, not current truth)

The forward thesis is **not** “build a smarter return predictor.” It is to build a **governed system that adapts safely across changing market tasks**, where a **task** spans universe, horizon, volatility/liquidity/macro/cost/objective regimes. **Task adaptation** is primary; return forecasting is secondary. Training and promotion must emphasize **decision utility after frictions**, not stylized offline loss. **II-0** grows because that direction demands **cheap falsification**; **II-D** grows because frictions and capacity must enter **before** claiming live-safe behavior. None of this implies today’s repo implements a next-gen meta-allocator, validated routing, or latent regime memory.

# 3. Priority Execution Plan

## 3.1 Immediate: Close I-F Honestly

| Priority | Why It Comes First |
|---|---|
| Companion-doc truthfulness | Planning should not run on stale assumptions |
| Canonical-path verification | Later phases must build on the path the repo actually trusts |
| Determinism boundary cleanup | ML entry without explicit reproducibility creates governance debt |
| Coverage / CI truthfulness | Quality bars must match what CI really measures |

## 3.2 I-G protocol and empirical foundation (closed in companion truth)

| Priority | Deliverable | Status |
|---|---|---|
| P1 | Frozen baseline policy | **Done** (I-G frozen) |
| P2 | Task-validity / non-exchangeability pilot | **Live anchor:** strict H3 `PASS` (Resolution Ledger §1.5); **RG-09** / **OI-59** follow-on is **II-0** |
| P3 | RiskFn Protocol and Signal Generation Protocol | **Done** |
| P4 | Context-encoder upgrade criteria | **Done** |
| P5 | Alternative-data admissibility and signal-universe expansion policy | **Done** |

**Next focus:** §3.3 **II-0** (especially **II-0C**), not reopening I-G because of ledger **PARTIAL**/**OPEN** rows.

**II-0B closure companion note:** See Implementation Plan §4 / **II-0B** — *closure posture (Wave 3 seam review resolved)* for **II-0B COMPLETE** on the non-promotable artifact-and-contract lane, canonical `pysrc/pipeline` rollout, explicit orchestration-layer fail-closed evidence usability, governed-consumer threshold summary visibility, borrowed-threshold lineage framing, stale pre-hash evidence retirement, and **GATE-II DEFERRED** with **II-0C next**.

## 3.3 Then: Build II-0 Non-Promotable Harnesses

| Priority | Deliverable | Gate |
|---|---|---|
| H1 | Frozen RG-09 reference anchor | Complete: strict-H3 reference hash is frozen and reproduction drift CI is confirmed |
| H2 | Task diagnostics and reference-run scaffolding | Complete: WS-2 diagnostic and WS-3 integration report are `ALL_PASS` |
| H3 | `task_manifest.json` / `meta_validity_report.json` scaffolds | Pilot artifacts emit reproducibly |
| H4 | Minimal experiment shells | Harness remains explicitly non-promotable |

## 3.4 Medium-Term: Enter Phase II in Evidence Order

| Priority | Deliverable | Checkpoint |
|---|---|---|
| T1 | II-A task substrate and validity closure | W2 clean enough to justify trainer commitment |
| T2 | II-B representation layer | Encoder quality is evidence-backed |
| T3 | II-C adaptation core | Adaptation usefulness and proxy alignment are real |
| T4 | II-D allocator integration **and deployment-layer conditioning** | Allocator intent is reportable, reversible, and expressed under **turnover / liquidity / capacity** realism (not proven live stack) |
| T5 | II-E controlled rollout harness | Rollout control exists without implying Phase III execution seriousness |

### 3.4.1 Kill Criteria as Roadmap Gates

The following remain explicit stop conditions:

- Harvey t remains below 3.0 after full task-pool construction.
- No **net** performance uplift over the frozen **simpler regime-conditioned** baseline after **realistic costs** and **operational burden** (utility after frictions—not forecast vanity).
- Context encoder coherence cannot be repaired.
- Held-out crisis performance remains non-positive after curriculum and replay tuning.
- **Regime-task validity** collapses: tasks are exchangeable, leakage-prone, or not **task-like** enough to justify meta-learning framing.

Warnings (failure-mode hygiene): do not call rolling refits “meta-learning” without task structure; do not call a model “robust” without domain-shift tests; do not treat Sharpe or stylized reward alone as success; **differentiability and model size are not moats by themselves**.

If any stop condition is confirmed, the roadmap records the failure and re-scopes or kills the program—typically **failing gracefully to the simpler governed baseline**. It does not automatically escalate complexity.

# 4. Subphase Map

## 4.1 Phase II-0 Subphases

| Subphase | Purpose | Deliverables |
|---|---|---|
| II-0A | Baseline & validity harness | **Complete:** frozen RG-09 reference anchor, task-validity diagnostic, WS-3 integration report, CI-confirmed reproduction guardrail |
| II-0B | Artifact & contract scaffolding | **Complete (non-promotable lane):** governed triple with required non-recursive `content_hash`, shell semantic validation, threshold state/expression register reconciliation, canonical `pysrc/pipeline` rollout under `phase2_ii0b_governed_non_promotable/`, explicit orchestration-layer fail-closed evidence usability, reviewer-facing threshold-governance summaries, honest borrowed-threshold lineage framing, deterministic seed lineage, and explicit exclusion of stale pre-hash root triples from current governed evidence |
| II-0C | Pilot ML scaffolds | **Complete non-promotable pilot harness:** canonical MetaTask adapter, deterministic reference-only encoder stub, XGBoost incumbent comparison guardrail, governed II-0B artifact wrapper, research-only report shells (`ii0c_pilot_report.json`, `ii0c_dry_run_summary.json`, plus dual-written `phase2_ii0c_scaffold_non_promotable.json`), frozen reference replay inputs, and fail-closed identity plus baseline/shared parity checks before emission |

## 4.2 Phase II Subphases

| Subphase | Purpose | Deliverables |
|---|---|---|
| II-A | Task substrate & validity closure | `MetaTask`, `TaskRegistry`, regime labeler, task generator, provenance surfaces |
| II-B | Representation layer | context encoder, coherence evidence, cross-regime separation evidence |
| II-C | Adaptation core | trainer, support/query mechanics, held-out gain reporting, K-budget evidence, proxy alignment evidence |
| II-D | Allocator & **deployment conditioning** | meta-policy (if earned), **`confidence_scalar` attenuation default**, conditional routing **pilot only**, structured **post-allocator** constraints, MetaLearner gate, rollback surfaces |
| II-E | Controlled rollout harness | allocator-level champion/challenger, shadow mode, capped blend, rollback/kill control flow |

## 4.3 Phase III Subphases

| Subphase | Purpose | Deliverables |
|---|---|---|
| III-A | Simulation realism | paper-trading simulation, realistic slippage/impact, liquidity-aware cost model |
| III-B | Broker & operator surfaces | broker integration, order routing, operator controls, monitoring, paper-to-live flow |
| III-C | Optional low-latency path | C++ / ONNX / TensorRT path and intraday optimizations only if justified |

## 4.4 Phase IV Subphases

| Subphase | Purpose | Deliverables |
|---|---|---|
| IV-A | Governed signal expansion | signal onboarding workflow, governed breadth expansion, PIT-safe alt-data adapters |
| IV-B | Signal identity & embedding layer | `signal_embedding`, novelty checks, lifecycle controls |
| IV-C | Assisted discovery | governed validation lane for machine-assisted signal ideation |
| IV-D | Factory automation | **signal-factory-serious** breadth: discovery orchestration, governed backtest/promotion loops, retirement handling (only after governance maturity) |

## 4.5 Phase IV+ Examples

| Extension | Why It Waits |
|---|---|
| Cross-asset transfer and joint embedding spaces | Depends on mature allocator and signal-identity substrate |
| Differentiable portfolio optimization | Needs validated allocator behavior and stronger execution realism |
| Autonomous or LLM-assisted alpha mining loops | Needs governed discovery, admission, and retirement controls first |
| Synthetic or agent-based validation layers | Later research investment, not default roadmap destiny |

# 5. Reference Architecture Direction

## 5.1 What the Roadmap Assumes

- `MetaTask` is the primary learning unit once Phase II begins.
- `regime_id` is primary identity; `regime_class` is the 5-class derived vocabulary used for curriculum and reporting.
- `task_id` is deterministic and includes `signal_ids_hash`; key-material changes require governed migration.
- `theta_meta`, `theta_task_prime`, and `theta_day_prime` are distinct lifecycle objects.
- Dynamic-K uses fixed-slot masking rather than dynamic output heads.
- `confidence_scalar` is **post-sizing attenuation by default**; **uncertainty-aware routing** is a **Phase II-0 pilot** and only graduates with **earned** evidence (Implementation Plan · Appendix D).

## 5.2 Canonical Pipeline Direction

The long-term target architecture still follows a staged pipeline, even though only the earlier governed stages are mature today:

```text
Stage 1: MarketData
Stage 2: Features
Stage 2.5: Context encoder -> regime_embedding z
Stage 3: Alpha / allocation output
Stage 4: Targets
Stage 5: Orders
Stage 6: Fills
Stage 7: Ledger
```

Practical roadmap interpretation:

- Stages 1-2 on the governed path are materially real today.
- Stage 2.5 is Phase II work preceded by I-G and II-0 preparation.
- The allocator portion of Stage 3 is Phase II work; **Stage 3 must not absorb deployment-layer conditioning** without treating it as **II-D post-allocator** seriousness (allocator proof remains separate).
- Stages 4-7 remain largely later-phase execution work (**III conditional** for execution-serious claims).

# 6. Research Hygiene

## 6.1 Data and Feature Discipline

- Every feature should have a documented hypothesis, lag treatment, and acceptance criterion.
- Feature computation must respect train/test boundaries and the repo’s PIT contract.
- Costs are part of the model; any feature or signal that only works gross is not working.
- Feature growth should remain governed rather than becoming an uncontrolled registry graveyard.

## 6.2 Validation Discipline

- Walk-forward and purge/embargo discipline remain mandatory.
- DSR, PBO, and multiple-testing controls remain part of promotion logic.
- Holdout crisis regimes are architectural constraints, not optional stress tests.
- Thresholds not yet justified by evidence remain `⚑ VALIDATE` rather than silently becoming policy.
- Evaluation surfaces are bundle-local and immutable; cross-variant metrics operate strictly on emitted artifacts.
- Parent comparison layers validate hashes and aggregate emitted path-score surfaces; they must not recompute CPCV scores.

## 6.3 Meta-Learning Discipline

- Baselines must be frozen before the meta-learning narrative starts to wander.
- Task construction should be treated as a model choice, not a preprocessing footnote.
- Adaptation usefulness must be demonstrated on query sets, not inferred from training loss.
- Proxy loss selection requires measurement, not taste.
- Continual-learning claims must include forgetting evidence and rollback readiness.

# 7. Key References

The roadmap still depends on the fuller v2.0 reference set rather than a thin algorithm list.

## 7.1 Meta-Learning and Continual Learning

- Finn et al. (2017) — MAML
- Nichol et al. (2018) — Reptile
- Raghu et al. (2020) — ANIL
- Kirkpatrick et al. (2017) — EWC
- Vilalta & Drissi (2002) — Meta-learning survey
- Schaul et al. (2016) — Prioritized replay

## 7.2 Financial Validation and Regime Methods

- Lopez de Prado — purging, embargo, CPCV, and PBO discipline
- Bailey and Lopez de Prado — DSR
- Harvey, Liu, and Zhu — multiple-testing-aware significance standards
- Adams and MacKay (2007) — BOCPD
- Regime-shift and ranking literature used for task construction and proxy alignment decisions

<!-- MM:BEGIN:RECENT_CHANGES key="TechnicalRoadmap" window=4 -->

| Release | Date | Technical Roadmap impact |
|---|---|---|
| 1.4.31 | April 2026 | **II-0C pilot harness completion:** §1.1 and §4.1 now record research-only report shells, frozen reference replay, governed baseline purity checks, baseline/shared parity fail-closed wiring, and explicit non-promotable pilot semantics while preserving **GATE-II DEFERRED** and the XGBoost incumbent baseline. |
| 1.4.30 | April 2026 | **II-0C scaffold dry-run sync:** §1.1 and §4.1 now record the non-promotable II-0C scaffold lane, canonical MetaTask adapter, deterministic reference-only encoder stub, XGBoost incumbent comparison guardrail, unchanged governed II-0B artifact path, and fail-closed identity binding across public entrypoints while preserving **GATE-II DEFERRED**. |
| 1.4.29 | April 2026 | **II-0B orchestration hard-gate sync:** §1.1, §3.2, and §4.1 now record that canonical `pysrc/pipeline` orchestration fails closed when governed II-0B evidence is non-usable and that the orchestration lane’s borrowed `THR-RG09-V03` / `THR-RG09-V17` references are reviewer-visible lineage, not native policy. |
| 1.4.28 | April 2026 | **II-0B completion sync:** §3.2 now points next-focus sequencing to **II-0C**; §4.1 records canonical `pysrc/pipeline` rollout of governed II-0B evidence, reviewer-visible threshold-governance consumer summaries, and explicit retirement of stale pre-hash root triples from current governed evidence while preserving the non-promotable boundary. |
| 1.4.27 | April 2026 | **II-0B 7.0.0 hardening sync:** Phase II-0 subphase map now records governed triple content hashes, shell semantic validation, threshold state/expression reconciliation, and non-promotable hardening while preserving the not-exit-ready posture. |
| 1.4.26 | April 2026 | **II-0A completion sync:** H1/H2 roadmap checkpoints and Phase II-0 subphase map now mark the strict-H3 RG-09 reference anchor, WS-2 diagnostic, WS-3 integration report, and CI-confirmed reproduction guardrail as complete. |
| 1.4.22 | April 2026 | **Phase I-G closure** in companion truth: §1 release context and §2.1 sequencing mark I-G **closed** (Ledger **v1.0.46**); §2.5 shifts primary obligation to **II-0**; §3.2 retitled to closed I-G with **II-0** next focus; title-page stamps to **README/VERSION 4.19.2**, Implementation Plan **6.5.3**, Resolution Ledger **v1.0.46**; OI-59 context uses MLN-07 **THR-RG09-V21** disposition (supersedes **V20** narrative where still cited historically). |
| 1.4.21 | April 2026 | Companion-sync: stamps aligned to **`VERSION.md` 4.18.34** / Resolution Ledger **1.0.44** / Implementation Plan **6.4.34** / Architecture Vision **1.2.23**; **4.18.34** propagates **`THR-RG09-V20`** memo/register disposition pointers. Release context distinguishes strict-H3 promotable posture vs corrected-surface OI-59 (**`HOLD_PENDING_THRESHOLD_REVIEW`**, **`THR-RG09-V20`** **`PROVISIONAL`** under **MLN-07**). Earlier entries recorded the H3 successor `PASS` at `runs/rg09_h3_granularity`. No sequencing change to the roadmap guardrail. |
| 1.4.20 | March 2026 | Companion-sync: title-page and stamps advanced through **4.18.0** (Implementation Plan **6.4.23**, Resolution Ledger **1.0.19**, README/VERSION **4.18.0**); MLN-02-AMD-01 crisis redefinition is part of the active baseline. Roadmap sequencing otherwise unchanged. |
| 1.4.19 | March 2026 | Companion-sync: title-page and stamps advanced through **4.17.0** (Implementation Plan **6.4.22**, Resolution Ledger **1.0.18**, README/VERSION **4.17.0**); MOM-020 closure is now part of the active baseline rather than a parallel/open comparison track. Roadmap sequencing otherwise unchanged. |
| 1.4.18 | March 2026 | Companion-sync: Phase I-F closed at **4.12.2**; title-page and stamps advanced through **4.16.0** (Implementation Plan **6.4.21**, Resolution Ledger **1.0.17**, README/VERSION **4.16.0**). Roadmap sequencing unchanged since the **4.12.2** edition. |
| 1.4.17 | March 2026 | March 2026 report-driven sequencing; II-0/II-D strategic weight; next-gen allocator direction as tasks-not-timestamps + utility after frictions; expanded kill/fallback and failure-mode hygiene; II-D table row aligned to deployment conditioning + routing pilot. |
| 1.4.15 | March 2026 | F-1/F-2 planning baseline carried forward; this edition makes the sequencing explicit: I-F closeout, I-G protocol foundation, II-0 non-promotable harnesses, evidence-gated II-A through II-E, and still-conditional III/IV expansion. |
| 1.4.14 | March 2026 | Phase I-F-1 / OI-19: companion baseline **VERSION.md 4.8.0**, title-page and stamp sync. Prior row: fuller capability inventory with Meta-Learning v2.0 roadmap logic. |
| 1.4.13 | March 2026 | Rebased the roadmap on Meta-Learning v2.0: added design locks, empirical workstreams, go/no-go checkpoints, and explicit stop conditions tied to baseline superiority, task validity, adaptation usefulness, proxy alignment, and continual robustness. |
| 1.4.12 | March 2026 | Prior companion-roadmap edition aligned to the 4.5.2 suite state. |
| 1.4.11 | March 2026 | Recorded the Phase I-E governance closure pass through 4.5.1. |

<!-- MM:END:RECENT_CHANGES -->

<!-- MM:BEGIN:SOURCE_STAMP -->

*Technical Roadmap v1.4.31 · April 2026 · Companion to Implementation Plan v6.5.10 · Meta-Learning Core v1.2.25 · Meta-Learning Architecture Vision v1.3.6 · Resolution Ledger v1.0.52 · README.md 7.2.3 · VERSION.md 7.2.3*

<!-- MM:END:SOURCE_STAMP -->

<!-- MM:END:DOCBODY -->
