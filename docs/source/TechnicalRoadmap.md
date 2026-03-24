**MarketMind**

**Technical Roadmap & Feature Plan**

<!-- MM:BEGIN:TITLEPAGE -->
Version 1.4.16 · March 2026 · Proprietary

Companion documents: Implementation Plan v6.4.15 · Meta-Learning Core v1.2.14 · Meta-Learning Architecture Vision v1.2.15 · Resolution Ledger v1.0.7 · README.md 4.9.1 · VERSION.md 4.9.1
<!-- MM:END:TITLEPAGE -->

*Strategic build order, research sequencing, and go/no-go checkpoints*

*Audience: Internal engineering, technical stakeholders*

<!-- MM:BEGIN:DOCBODY -->

# Technical Roadmap & Feature Plan

# Purpose

This roadmap defines what to build next, what to validate before building further, and which workstreams are allowed to halt the meta-learning program entirely. It tracks engineering and research together because the adaptive-learning roadmap is evidence-first rather than milestone-first.

# 1. Capability Inventory

This inventory separates what is real today from what is governed future scope.

## 1.1 What Exists Today

| Area | Current Reality | Missing or Deferred |
|---|---|---|
| Canonical research substrate | PIT-safe orchestration, governed bundle emission, lineage, statistical-validity artifacts, and cost assumptions are real | Later phases must extend this substrate rather than fork it |
| Governed strategies and signals | `stat_arb_pairs`, materially advanced momentum, SignalCatalog, and stable `slot_index` exist | Broader governed breadth and signal-factory lifecycle remain later work |
| Validation discipline | Leakage-aware tests, DSR/PBO framing, deterministic artifact expectations, and CI discipline are mature on the trusted path | MetaTask-era evidence and meta-validity reporting are not built |
| Meta-learning contracts | Runtime shape and proof burden are documented in the companion suite | Context encoder, task generator, trainer, allocator, and rollout control are still unbuilt |
| Execution realism | Governed execution assumptions exist as artifacts | TCA loops, paper/live control flow, broker integration, and low-latency paths remain conditional |

## 1.2 What Remains Hypothetical

- promotable adaptive-learning machinery,
- validated allocator superiority over the frozen baseline,
- execution-serious deployment surfaces,
- and signal-factory-serious automation.

# 2. Evidence-First Sequencing

## 2.1 Execution Plan

1. I-F honest closeout.
2. I-G empirical and protocol foundation.
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

# 3. Priority Execution Plan

## 3.1 Immediate: Close I-F Honestly

| Priority | Why It Comes First |
|---|---|
| Companion-doc truthfulness | Planning should not run on stale assumptions |
| Canonical-path verification | Later phases must build on the path the repo actually trusts |
| Determinism boundary cleanup | ML entry without explicit reproducibility creates governance debt |
| Coverage / CI truthfulness | Quality bars must match what CI really measures |

## 3.2 Next: Land I-G Protocol and Empirical Foundation

| Priority | Deliverable | Why It Matters |
|---|---|---|
| P1 | Frozen baseline policy | Keeps the null hypothesis honest |
| P2 | Task-validity / non-exchangeability pilot | Decides whether meta-learning is structurally justified |
| P3 | RiskFn Protocol and Signal Generation Protocol | Freezes runtime policy before code spreads assumptions |
| P4 | Context-encoder upgrade criteria | Prevents silent architecture drift mid-program |
| P5 | Alternative-data admissibility and signal-universe expansion policy | Keeps future breadth governed rather than opportunistic |

## 3.3 Then: Build II-0 Non-Promotable Harnesses

| Priority | Deliverable | Gate |
|---|---|---|
| H1 | Frozen baseline/challenger harness | Baseline is frozen and comparison is mechanically repeatable |
| H2 | Task diagnostics and reference-run scaffolding | First valid task-diagnostics pass exists |
| H3 | `task_manifest.json` / `meta_validity_report.json` scaffolds | Pilot artifacts emit reproducibly |
| H4 | Minimal experiment shells | Harness remains explicitly non-promotable |

## 3.4 Medium-Term: Enter Phase II in Evidence Order

| Priority | Deliverable | Checkpoint |
|---|---|---|
| T1 | II-A task substrate and validity closure | W2 clean enough to justify trainer commitment |
| T2 | II-B representation layer | Encoder quality is evidence-backed |
| T3 | II-C adaptation core | Adaptation usefulness and proxy alignment are real |
| T4 | II-D allocator and governance integration | Allocator behavior is reportable and reversible |
| T5 | II-E controlled rollout harness | Rollout control exists without implying Phase III execution seriousness |

### 3.4.1 Kill Criteria as Roadmap Gates

The following remain explicit stop conditions:

- Harvey t remains below 3.0 after full task-pool construction.
- No net Sharpe uplift over the frozen XGBoost baseline after costs.
- Context encoder coherence cannot be repaired.
- Held-out crisis performance remains non-positive after curriculum and replay tuning.

If any of those are confirmed, the roadmap records the failure and re-scopes or kills the program. It does not automatically escalate complexity.

# 4. Subphase Map

## 4.1 Phase II-0 Subphases

| Subphase | Purpose | Deliverables |
|---|---|---|
| II-0A | Baseline & validity harness | frozen baseline harness, task-validity diagnostics, non-exchangeability pilot harness, holdout scaffolding |
| II-0B | Artifact & contract scaffolding | `task_manifest.json` scaffold, `meta_validity_report.json` scaffold, threshold registry hooks, deterministic reference-run hooks |
| II-0C | Pilot ML scaffolds | encoder stub, MetaTask generator scaffold, pilot comparison runners, research-only shells around later MLC surfaces |

## 4.2 Phase II Subphases

| Subphase | Purpose | Deliverables |
|---|---|---|
| II-A | Task substrate & validity closure | `MetaTask`, `TaskRegistry`, regime labeler, task generator, provenance surfaces |
| II-B | Representation layer | context encoder, coherence evidence, cross-regime separation evidence |
| II-C | Adaptation core | trainer, support/query mechanics, held-out gain reporting, K-budget evidence, proxy alignment evidence |
| II-D | Allocator & governance integration | meta-policy, confidence routing, risk-budgeting interfaces, MetaLearner gate, rollback surfaces |
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
| IV-D | Factory automation | broader discovery orchestration, governed backtest/promotion loops, retirement handling |

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
- `theta_meta`, `theta_task_prime`, and `theta_day_prime` are distinct lifecycle objects.
- Dynamic-K uses fixed-slot masking rather than dynamic output heads.
- `confidence_scalar` is post-sizing attenuation only unless changed by later governance.

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
- The allocator portion of Stage 3 is Phase II work.
- Stages 4-7 remain largely later-phase execution work.

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
| 1.4.15 | March 2026 | F-1/F-2 planning baseline carried forward; this edition makes the sequencing explicit: I-F closeout, I-G protocol foundation, II-0 non-promotable harnesses, evidence-gated II-A through II-E, and still-conditional III/IV expansion. |
| 1.4.14 | March 2026 | Phase I-F-1 / OI-19: companion baseline **VERSION.md 4.8.0**, title-page and stamp sync. Prior row: fuller capability inventory with Meta-Learning v2.0 roadmap logic. |
| 1.4.13 | March 2026 | Rebased the roadmap on Meta-Learning v2.0: added design locks, empirical workstreams, go/no-go checkpoints, and explicit stop conditions tied to baseline superiority, task validity, adaptation usefulness, proxy alignment, and continual robustness. |
| 1.4.12 | March 2026 | Prior companion-roadmap edition aligned to the 4.5.2 suite state. |
| 1.4.11 | March 2026 | Recorded the Phase I-E governance closure pass through 4.5.1. |

<!-- MM:END:RECENT_CHANGES -->

<!-- MM:BEGIN:SOURCE_STAMP -->

*Technical Roadmap v1.4.16 · March 2026 · Companion to Implementation Plan v6.4.15 · Meta-Learning Core v1.2.14 · Meta-Learning Architecture Vision v1.2.15 · Resolution Ledger v1.0.7 · README.md 4.9.1 · VERSION.md 4.9.1*

<!-- MM:END:SOURCE_STAMP -->

<!-- MM:END:DOCBODY -->
