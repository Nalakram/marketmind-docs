**MarketMind**

────────────────────────────────

**Implementation Plan & Execution Roadmap**

<!-- MM:BEGIN:TITLEPAGE -->
Version 6.4.15 · March 2026 · Proprietary

Companion documents: Technical Roadmap v1.4.16 · Meta-Learning Core v1.2.14 · Meta-Learning Architecture Vision v1.2.15 · Resolution Ledger v1.0.7 · README.md 4.9.1 · VERSION.md 4.9.1
<!-- MM:END:TITLEPAGE -->

*Execution plan for the governed research substrate and the validation-gated meta-learning program*

*Audience: Internal engineering, technical stakeholders*

<!-- MM:BEGIN:DOCBODY -->

# Implementation Plan & Execution Roadmap

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

## 1.2 Current Reality Through 4.9.0

**Audit baseline:** `VERSION.md` **4.9.0** (planning-surface sync patch after Phase I-F-1 truthfulness audit). Phase I-E engineering delivery through **4.5.4** remains the last major substrate closure before this planning pass.

Delivered or materially advanced:

- canonical PIT-safe orchestration and governed bundle emission,
- governed daily source adaptation and single-path feature execution,
- governed `stat_arb_pairs` and materially advanced governed momentum,
- SignalCatalog with stable `slot_index`,
- `screening_report.json`, `execution_assumptions.json`, and governed `stat_validity_report.json`,
- DataLineageGate plus artifact-registry-owned hashing/canonicalization,
- and a mature test/CI baseline for leakage, determinism, and typing on the trusted path.

Still open before promotable adaptive-learning buildout:

- narrow Phase I-F closure work,
- empirical and protocol foundation work that should not be smuggled into I-F,
- non-promotable scaffolding needed to test those protocol decisions reproducibly,
- and the validation-gated Phase II build itself.

# 2. Current Reality Map

This plan stays anchored to repo truth rather than inherited roadmap inertia.

## 2.1 Trusted Build Surface

| Area | Current Reality | Why It Matters Next |
|---|---|---|
| Canonical orchestration path | Trusted PIT-safe bundle-producing path exists | All later ML work must build on this path, not a shadow path |
| Governed feature execution | `_OP_REGISTRY` and the canonical planner/executor route are the governed feature path | Task generation must inherit the same PIT and operator guarantees |
| Artifact lineage | `srcPy.artifact_registry` and RunRegistry own canonical artifact identity | Later task/checkpoint/report artifacts must extend this scheme rather than fork it |
| Statistical and cost gating | `stat_validity_report.json` and `execution_assumptions.json` are real governed surfaces | Phase II adds new evidence surfaces; it does not bypass existing gates |
| Signal identity substrate | SignalCatalog and stable `slot_index` exist | Dynamic-K and later signal-factory growth must build from that governed substrate |

## 2.2 Anti-Blur Rules

- I-F is narrow. It closes truthfulness, interface, determinism, and seam blockers only.
- I-G owns baseline policy, task-validity protocol, RiskFn / signal-generation protocol work, and early empirical closure.
- II-0 owns harnesses, pilot artifacts, report scaffolding, and reference runs only.
- II owns promotable adaptive-learning machinery in evidence order.
- III and IV remain conditional even if Phase II succeeds technically.

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

For typing, I-F remains intentionally narrower than a repo-wide `mypy srcPy/strategies/ --strict` sweep. The acceptance surface is still the canonical path the later phases will actually inherit:

```bash
mypy srcPy/strategies/momentum/ \
     srcPy/strategies/pipeline_strategy.py \
     srcPy/artifact_registry/ \
     srcPy/cli/gate.py \
     --strict
```

# 3.x Phase I-G — Empirical & Protocol Foundation

Phase I-G is the substantial pre-build foundation phase that the current suite and gap analysis justify.

## 3.x.1 Objective

Define the research world and the proof burden before promotable ML buildout.

## 3.x.2 Owns

- baseline freeze policy,
- task non-exchangeability pilot,
- task-validity / leakage-geometry protocol,
- RiskFn Protocol definition,
- Signal Generation Protocol,
- context-encoder upgrade criteria,
- threshold registry for `⚑ VALIDATE` items,
- signal-universe expansion policy,
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

# 4. Phase II-0 — ML Scaffolding & Research Harness

Phase II-0 is the explicit bridge between protocol decisions and promotable adaptive-learning implementation.

## 4.1 Objective

Turn I-G decisions into minimal, reproducible, non-promotable machinery.

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

### II-0B — Artifact & Contract Scaffolding

**Purpose:** make later Phase II evidence mechanically emit-able.

**Deliverables:**

- `task_manifest.json` scaffolding,
- `meta_validity_report.json` scaffolding,
- threshold registry / provenance hooks,
- deterministic checkpoint / seed policy hooks,
- early gate shells for ML evidence.

**Gate to next subphase:**

- pilot artifacts emit reproducibly,
- provisional thresholds remain visibly provisional,
- and the artifact/report contract is usable by later code.

### II-0C — Pilot ML Scaffolds

**Purpose:** build minimal, non-promotable machinery around agreed experiments.

**Deliverables:**

- encoder stub / reference scaffold,
- MetaTask generator scaffold,
- pilot comparison runners,
- reference runs for reproducibility,
- research-only shells around future MLC surfaces.

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

**Purpose:** make the learning unit real and evidence-safe.

**Deliverables:**

- `MetaTask` dataclass,
- `TaskRegistry`,
- BOCPD-backed regime labeler,
- task generator,
- holdout/task provenance surfaces,
- dynamic-K task-facing identity,
- and W2 closure or a clean-enough W2 state for trainer commitment.

**Primary gate:** task identity, leakage safety, and non-exchangeability are sufficiently validated.

### II-B — Representation Layer

**Purpose:** build and validate the representation layer before broad allocator claims.

**Deliverables:**

- context encoder,
- encoder coherence evidence,
- cross-regime separation evidence,
- context-encoder upgrade trigger policy,
- selective event/alt-data entry only where justified.

**Primary gate:** encoder quality is evidence-backed rather than inferred from downstream metrics.

### II-C — Adaptation Core

**Purpose:** validate whether adaptation is actually useful.

**Deliverables:**

- Reptile trainer,
- support/query mechanics,
- held-out query gain reporting,
- K-budget behavior evidence,
- proxy alignment evidence.

**Primary gate:** adaptation usefulness and proxy alignment are both strong enough to justify allocator escalation.

### II-D — Allocator & Governance Integration

**Purpose:** build the governed allocator once the upstream evidence is strong enough.

**Deliverables:**

- meta-policy network,
- confidence routing implementation,
- regime-aware risk-budgeting interfaces,
- MetaLearner gate,
- full `meta_validity_report.json` path,
- rollback / kill / checkpoint surfaces.

**Primary gate:** allocator behavior is governed, reportable, and reversible.

### II-E — Controlled Rollout Harness

**Purpose:** enable allocator-level promotion control without crossing into Phase III execution seriousness.

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
| `meta_validity_report.json` | Canonical gate report for adaptation, encoder, crisis, forgetting, proxy alignment, confidence calibration, and overall result |
| `task_manifest.json` | Exact task-pool evidence for the nightly run, including identity, PIT boundary, and signal-set provenance |
| `gate_result.json` | Existing canonical gate result extended with the meta-learner gate block |
| Checkpointed `theta_meta` and `theta_day_prime` | Promotion, rollback, and audit anchors |

## 5.4 Acceptance Hierarchy

The Phase II program is judged against the Core v2.0 multi-level hierarchy:

- model-level evidence: encoder coherence, cross-regime separation, held-out adaptation gain, Harvey t, proxy alignment, and practical K-budget saturation;
- portfolio-level evidence: net Sharpe after costs, walk-forward sanity, crisis robustness, DSR/PBO discipline, and baseline comparison;
- governance-level evidence: Anti-Goodhart compliance, PIT compliance, determinism compliance, task-pool sufficiency, and forgetting bounds.

# 6. Phase III — Execution Realism & Conditional Deployment

Phase III is the first phase allowed to become execution-serious, and it remains conditional on allocator validation and product need.

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

Phase IV is the first phase allowed to become signal-factory-serious, and it remains conditional on allocator validation and mature governance.

## 7.1 IV-A — Governed Signal Expansion

- operational Signal Generation Protocol,
- governed signal onboarding workflow,
- signal-universe expansion from the current narrow base,
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

1. Close Phase I-F honestly.
2. Land Phase I-G protocols and empirical closure.
3. Build Phase II-0 harnesses.
4. Enter Phase II only in evidence order.

# Appendix A: Protocol and Handoff Surfaces

- [`risk_protocol.md`](risk_protocol.md) — RiskFn Protocol and allocator-to-risk boundary.
- [`signal_generation_protocol.md`](signal_generation_protocol.md) — signal admission, expansion, and retirement policy.
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
- `net_allocation_sharpe`
- `signal_set_version`
- `anti_goodhart_gap`
- `determinism_check`
- `overall_result`

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

<!-- MM:BEGIN:RECENT_CHANGES key="ImplementationPlan" window=4 -->

| Release | Date | Implementation Plan impact |
|---|---|---|
| 6.4.14 | March 2026 | F-1/F-2 planning baseline carried forward; this edition clarifies I-F as narrow closure work, introduces I-G and II-0 so Phase II is not overloaded, preserves II-A -> II-E, and keeps III/IV explicitly conditional. |
| 6.4.13 | March 2026 | Phase I-F-1 / OI-19: **4.8.0** audit baseline, companion sync, and truthful phase framing (I-A–I-E closed; I-F open). Prior row: restored fuller execution detail with v2.0 validation-first framing. |
| 6.4.12 | March 2026 | Rebased the plan on Meta-Learning v2.0: Phase II is now a validation-gated program rather than a purely build-oriented milestone; added explicit workstreams, prerequisite tables, promotion/rollback/kill planning, and required Phase II artifacts including `meta_validity_report.json` and `task_manifest.json`. |
| 6.4.11 | March 2026 | Prior companion-plan edition aligned to the 4.5.2 suite state. |
| 6.4.10 | March 2026 | Recorded the Phase I-E governance closure pass through 4.5.1. |

<!-- MM:END:RECENT_CHANGES -->

<!-- MM:BEGIN:SOURCE_STAMP -->

*Implementation Plan v6.4.15 · March 2026 · Companion to Technical Roadmap v1.4.16 · Meta-Learning Core v1.2.14 · Meta-Learning Architecture Vision v1.2.15 · Resolution Ledger v1.0.7 · README.md 4.9.1 · VERSION.md 4.9.1*

<!-- MM:END:SOURCE_STAMP -->

<!-- MM:END:DOCBODY -->
