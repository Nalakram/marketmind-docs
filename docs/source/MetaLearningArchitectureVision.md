**MarketMind**

**Meta-Learning Architecture Vision**

<!-- MM:BEGIN:TITLEPAGE -->
Version 1.3.5 · April 2026 · Proprietary

Companion documents: Implementation Plan v6.5.5 · Technical Roadmap v1.4.26 · Meta-Learning Core v1.2.24 · Resolution Ledger v1.0.51 · README.md 6.2.2 · VERSION.md 6.2.2
<!-- MM:END:TITLEPAGE -->

<!-- MM:BEGIN:DOCBODY -->

# Meta-Learning Architecture Vision

# Purpose

The Meta-Learning Core v2.0.0 defines the research program, validation framework, and governing failure criteria for MarketMind's meta-learning architecture. This document expresses the proposed architecture MarketMind is building toward: the runtime shape, system boundaries, interface contracts, and validation-gated defaults that become binding commitments only where the Core's empirical program confirms them.

Where Core v2.0.0 says "here are the five claims that must be proven," this document says "here is the runtime form the architecture takes if those claims are confirmed." Where Core defines kill criteria and rollback triggers, this document describes what the architecture looks like at each stage of that lifecycle. This document does not override unresolved empirical questions. Any threshold or design parameter flagged `⚑ VALIDATE` in Core v2.0.0 is not a commitment here either.

**Governance rule.** Where this document and Core v2.0.0 conflict on empirical thresholds, unresolved questions, or validation requirements, Core v2.0.0 governs. Where they conflict on interface contracts, schema definitions, or runtime boundaries, this document governs. The split is: Core owns the validation program; this document owns the system shape.

<!-- MM:BEGIN:RELEASE_NOTE key="MetaLearningArchitectureVision" -->

> ✦ v2.0.0: Major revision aligned to Meta-Learning Core v2.0.0 and refreshed through VERSION.md 4.5.4 (substrate era); companion stamps for the suite are aligned to **4.8.0** from edition **1.2.14** onward. Added Decision Framing (§1), Validation-Gated Defaults (§5), Promotion/Rollback/Kill Model (§7), Observability and Operator Controls (§8). Rewrote Purpose and §2 to remove "closes every remaining open question" framing. Fixed task_id hash definition, regime_class 5-class conflict in MetaTask schema, and minimum task count conflict with Core §10.2. §4.5 migration contract aligned to Core §8. All validation-gated material clearly distinguished from non-negotiable contracts.

<!-- MM:END:RELEASE_NOTE -->

---

# 1. Decision Framing

*This section is the front door for readers coming to this document first. For full treatment see Core v2.0.0 §0.*

## 1.1 Architectural Claim

Meta-learning is the preferred architecture for adaptive signal recombination across regime-indexed, non-exchangeable market tasks in MarketMind. Individual strategies — stat-arb, momentum, mean-reversion — are training tasks drawn from a distribution of market conditions. The meta-learner is the allocation brain, not a late-arriving ensemble weighter. This document describes what that architecture looks like as a runtime system.

## 1.2 Null Hypothesis

A simpler allocator — specifically an XGBoost ensemble with BOCPD-triggered regime conditioning, using the same signal universe — matches or exceeds the Reptile meta-policy net of cost, robustness, and operational complexity. The meta-learning architecture must falsify this null through the empirical program defined in Core v2.0.0 §4. The architecture described in this document is a governed bet on that falsification.

## 1.3 Five Claims That Must Be Proven

Before the proposed architecture transitions from design to deployment commitment, Core v2.0.0 §0.3 requires empirical confirmation of:

1. **Task non-exchangeability.** Regime-indexed episodes are meaningfully distinct.
2. **Adaptation usefulness.** Inner-loop steps produce IC improvement on held-out query sets.
3. **Encoder coherence.** The context encoder produces structured, interpretable regime embeddings.
4. **Proxy alignment.** The differentiable ranking surrogate tracks exact Spearman IC on unseen tasks.
5. **Continual robustness.** EWC plus crisis replay prevents catastrophic forgetting without collapsing plasticity.

## 1.4 Kill-Criteria Preview

The architecture is abandoned — not rolled back, abandoned — if any of the following are confirmed: inner-loop gain Harvey t < 3.0 after full task pool construction; no net Sharpe uplift over the XGBoost baseline after transaction costs; context encoder clustering fails and cannot be repaired; or crisis episode IC <= 0 on held-out crisis windows after curriculum adjustment and replay tuning. Core v2.0.0 §9.3 is the governing framework and defines the exact kill set, including the operational burden scorecard (§9.3.1). This section is a preview only; Core §9.3 governs in any conflict.

## 1.5 Hierarchical target architecture (research target, not repo truth)

If the validation program succeeds, the **desired** runtime is **hierarchical**, not monolithic. The following layers are **future-facing**; none imply the whole stack already exists:

| Layer | Purpose | Typical home |
|---|---|---|
| **A — Representation** | Market/context representation model | II-B |
| **B — Latent regime / world model** | Structured beliefs about regime/state (candidate) | II-B |
| **C — Expert allocator family** | Modular meta-policy / fast adaptation candidates | II-C |
| **D — Post-allocator conditioning** | **Structured** conversion of allocator intent into constrained, friction-aware capital (turnover, liquidity/capacity, drawdown/regime overlays); **differentiable portfolio optimization is optional here**, not the moat claim | **II-D primary**, III second |

**Three distinct “seriousness” escalations (all conditional):** **Phase II** = promotable adaptive-learning machinery (if earned). **Phase III** = execution-serious deployment (**not** implied by II-D conditioning importance). **Phase IV** = signal-factory-serious breadth and automation. **Breadth, routing sophistication, and deployment conditioning** are **governed optional layers** until evidence and policy say otherwise.

**Multi-timescale control (vision).** Separates **strategic allocator**, **tactical overlay**, **execution controller**, and **risk governor**—future-facing coordination, not a present module list.

---

# 2. Canonical Definitions

Every term below has exactly one meaning throughout all MarketMind meta-learning documentation and code. If a term is used inconsistently anywhere, this section governs.

| Term | Definition | Lives On |
|---|---|---|
| Task | A regime episode: a contiguous block of bars sharing a stable regime label, split into support set and query set with purge/embargo between them. The primary unit of meta-learning. | MetaTask dataclass |
| Support set | First temporal portion of a task episode. The inner loop adapts parameters on this data. Features + labels. | MetaTask.support_set |
| Query set | Second temporal portion, after purge/embargo gap. Labels hidden from inner loop; used only by outer loop for loss computation. | MetaTask.query_set |
| `theta_meta` | The learned meta-initialization. Updated by the outer loop (Reptile). This is the starting point for all inner-loop adaptations. | `reptile_trainer.py` |
| `theta_task_prime` | Per-task adapted parameter state after inner-loop steps on a specific task's support set. Ephemeral — exists only during training. | `reptile_trainer.py` |
| `theta_day_prime` | The nightly-adapted parameter state used for live trading. Produced by inner-loop adaptation on the most recent episode. Frozen during market hours. | `meta_policy.py` |
| Inner loop | Fast adaptation: K gradient steps on support set, updating only adaptation parameters (`psi_condnorm + h_alloc`). Produces `theta_task_prime`. | `reptile_trainer.py` |
| Outer loop | Slow learning: Reptile update `theta_meta ← theta_meta + ε(theta_task_prime − theta_meta)` across task batch. Runs nightly. | `reptile_trainer.py` |
| Inference path | Production execution: frozen `theta_day_prime`, no gradient computation. Pure feedforward. | `meta_policy.py` |
| Training path | Offline learning: nightly outer-loop update + inner-loop adaptation on task batches. Never on the live execution path. | `reptile_trainer.py` |
| Regime embedding (z) | Dense vector `z in R^64` from context encoder. Indexes the task distribution. Per-timestamp. | MetaTask.regime_embedding |
| Signal embedding | Dense vector describing a signal's identity/behavior for Signal Factory retrieval. Per-signal-version. Distinct from regime embedding. | Signal ABC.signal_embedding |
| Per-signal utility | The meta-policy's intermediate output: expected utility score for each active signal. Converted to `allocation_weights` via softmax on the active signal mask. | `meta_policy.py` internal |
| Allocation weights | Simplex vector `in ΔK` derived from per-signal utility scores. Replaces EnsemblePipelineStrategy adaptive weights. | `meta_policy.py` output |
| `confidence_scalar` | Scalar in [0,1] output by the meta-policy. Calibrated reliability estimate for the current allocation. Applied as a post-sizing exposure multiplier only. See §4.3. | `meta_policy.py` output |

> **CONTRACT:** Tasks are regime episodes, not signals. Individual signals are the feature substrate within a task — they produce Alpha IR that the meta-learner combines. The task is the regime episode containing those signals.

### Task Hierarchy

**Level 1 (Primary):** Regime episode task — the unit sampled by the curriculum, processed by the inner loop, evaluated by the outer loop. This is what MetaTask represents.

**Level 2 (Contents):** Active signal set within a task — which signals contribute Alpha IR to this episode. The meta-policy's allocation_weights distribute over these signals.

**Level 3 (Future / Phase IV):** Signal-as-task for Signal Factory — when the Signal Factory generates/evaluates new signals, each candidate signal is evaluated as if it were a task. Deferred.

---

# 3. Inherited Infrastructure

The following components represent proto-meta-learning infrastructure that is already built or specified. The meta-learning architecture reframes these rather than replacing them.

| Existing Component | Current Role | Reframed Role |
|---|---|---|
| EnsemblePipelineStrategy | Adaptive weight combiner over N strategy instances | Outer-loop evaluator and Stage 1–2 migration incumbent |
| ChampionChallenger | A/B evaluation of strategy variants | Migration harness: shadow vs blend vs promotion state machine |
| BOCPD change-point detector | Binary change-point flag (`bocpd_cp`) | Task-boundary signal; triggers new learning episode |
| RegimeDetector Protocol slot | Gating plugin for position sizing | Context encoder input: regime embedding indexes the task distribution |
| `parameter_sweep()` / `optuna_tune()` | Hyperparameter search | Inner-loop gradient steps: fast adaptation over support set |
| Signal ABC / SignalCatalog | Catalog of tradeable strategies | Supplies weak learners inside each regime-episode task |
| `blend()` composition | Combinatoric strategy mixing | Meta-policy output: allocation over the task library |

---

# 4. Non-Negotiable Contracts

*This section contains interface and runtime commitments that are not subject to empirical validation outcomes. These are binding regardless of what the validation program finds. Changing any of them requires an ADR.*

## 4.1 MetaTask Schema

| Field | Type | Description |
|---|---|---|
| `task_id` | str | `HMAC-SHA256(regime_id + t0 + t1 + signal_ids_hash)`. Deterministic, content-addressed. Immutable after creation. |
| `regime_id` | str | Compositional Level 1: `trend_{hi|lo|flat}__vol_{hi|med|lo}__bocpd_{stable|transition|cp}` |
| `regime_class` | str | 5-class Level 2 projection: `{bull, bear, sideways, high_vol, crisis}` |
| `regime_embedding` | Optional[np.ndarray] | float32[64]. None until context encoder trained (Phase II ML-1). |
| `support_set` | pl.DataFrame | n_support bars. Features + labels. Inner-loop adaptation data. |
| `query_set` | pl.DataFrame | n_query bars. Features + labels (labels hidden from inner loop, used only for outer-loop loss). |
| `horizon` | int | Label horizon in bars (for example, 5 for 5-day forward returns). |
| `signal_ids` | list[str] | Active signals in this task. Ordered, deterministic. |
| `signal_mask` | np.ndarray | Boolean, same order as signal_ids. Fixed 64-slot masking. |
| `signal_set_version` | int | Signal set version at task creation time. Used for replay compatibility. |
| `pit_boundary` | datetime | `DataView.as_of(T)` enforcement. No data after this timestamp. |
| `t0` | datetime | Episode start (first bar of support set). |
| `t1` | datetime | Episode end (last bar of query set). |
| `active_k` | int | Count of signals with mask=True. |

**Sizing invariant (non-negotiable).** `support_set.index.max() + purge_window + embargo_window < query_set.index.min()`. Enforced by `task_generator.py` at construction time. Violation means task rejected and logged as a data integrity error. Minimum feasible episode length: `Lmin >= n_support + n_query + 2H + E`.

**Sizing defaults (validation-gated).** `n_support = 20–40` bars; `n_query = 10–20` bars; `purge_window = max(horizon, 5)` bars; `embargo_window = 2` bars daily, `ceil(0.05 × episode_len)` intraday. These are initial operating values only.

**task_id note.** The inclusion of `signal_ids_hash` in the task_id hash is required for dynamic-K stability. `task_generator.py` is the only permitted constructor.

## 4.2 Regime Taxonomy

**Level 1 — Compositional `regime_id` (high cardinality):** formed by concatenating discretized regime dimensions. Up to 27 composite states. Primary task identity.

**Level 2 — 5-class `regime_class` (low cardinality):** deterministic projection to `{bull, bear, sideways, high_vol, crisis}`. Used for curriculum bootstrap sampling, context encoder pre-training supervision, output heads, and gate reporting.

| 5-Class Label | Compositional Conditions | Historical Freq |
|---|---|---|
| crisis | vol_hi AND severity_flag | ~5% ⚑ VALIDATE |
| high_vol | vol_hi AND NOT crisis | ~15% |
| bear | trend_lo AND NOT (crisis OR high_vol) | ~12% |
| bull | trend_hi AND vol_{lo\|med} | ~18% |
| sideways | Everything else | ~50% |

**`severity_flag` (MLN-02-AMD-01; assumption RG09-V12, ⚑ VALIDATE).** True when `vol_score_raw` at the labeling timestamp is at or above a PIT-safe expanding-window percentile of strictly prior `vol_score_raw` values (window starts after `cold_start_burn_in` on the labeling path). Initial default threshold: **p90**. Not tuned against Anti-Goodhart holdouts; validation surface is Phase II-0A learning performance. Implementation: `RegimeLabeler.compute_severity_flag_vol_score_raw` + `BOCPDConfig.crisis_vol_score_percentile`.

> **BOCPD is a segmentation primitive. It is not a crisis label primitive.**
>
> `bocpd_cp` remains a Level 1 dimension inside compositional `regime_id` (for example `trend_hi__vol_hi__bocpd_cp`). A change-point flag informs task boundaries and episode construction; it is neither necessary nor sufficient for Level 2 `crisis`.

**Historical frequency.** The ~5% figure for `crisis` under the severity-gated rule is a working hypothesis; empirical frequency must be confirmed in pilot measurement. Tag: ⚑ VALIDATE.

> **CONTRACT:** Compositional `regime_id` is the primary contract for task identity and storage. 5-class projection is derived convenience only.

### What Drives What

| System Component | Uses Level 1 (Compositional) | Uses Level 2 (5-Class) |
|---|---|---|
| TaskRegistry indexing | ✓ | |
| MetaTask identity | ✓ | ✓ |
| Curriculum bootstrap sampling | | ✓ |
| Context encoder pre-training | | ✓ |
| Hardness-weighted curriculum | ✓ | |
| Meta-policy regime_class output | | ✓ |
| `meta_validity_report.json` | | ✓ |
| Regime embedding computation | ✓ | |

## 4.3 Confidence Routing Contract

`confidence_scalar` is a calibrated reliability estimate for the current meta-policy allocation. It is not a probability of profit, not a return forecast, and not a replacement for portfolio risk limits.

**Permitted action range (Phase II).** `confidence_scalar` may only attenuate exposure after `SizingFn` computes base positions from `allocation_weights`. Formally: `live_position = base_position × confidence_scalar`. It may not lever above base size. Any use outside this post-sizing attenuation role requires an ADR.

**SizingFn Protocol.** The SizingFn signature is not changed in Phase II. A protocol version bump to accept confidence explicitly is deferred to Phase III unless the post-sizing approach proves insufficient.

**Calibration.** `confidence_scalar` is supervised against a bounded realized-quality target and calibrated via isotonic regression or Platt scaling on a held-out calibration set after core model training. Recalibrated nightly. ECE and realized-quality correlation are reported in `meta_validity_report.json` and monitored per Section 8.

**Routing (explicitly non-default).** **Uncertainty-aware routing**—treating some states as reject/route zones—is a **Phase II-0 pilot hypothesis**, not part of the default inference contract. Default behavior remains **post-sizing attenuation** only unless Core §2.5.2 promotion criteria are met and an **ADR** updates defaults.

## 4.4 Dynamic-K Contract

**MAX_SIGNALS = 64.** All meta-learning interfaces use a fixed 64-slot signal vector. Active signals occupy slots `0..K-1`. Inactive slots are masked.

| Component | Active Slots (0..K-1) | Inactive Slots (K..63) |
|---|---|---|
| Encoder input (`ic_decay`) | Actual 30-day IC slope | Set to 0.0 |
| Meta-policy output | Softmax over active slots only | Hard-masked to 0.0 |
| TaskRegistry replay | Original IC values preserved | Filled with 0.0; mask applied |
| Signal ABC registration | `slot_index` assigned at registration | Retired signal slots preserved |

**Slot assignment.** Slots are assigned in SignalCatalog registration order. A retired signal's slot is never reassigned.

**Reclamation.** When active signal count approaches MAX_SIGNALS (`K > 56`), oldest retired slots with zero replay references may be reclaimed. This triggers a one-time TaskRegistry migration and is logged as a version event.

**Schema versioning.** Every change to the active signal set increments `signal_set_version`. MetaTask carries `signal_set_version` at creation time.

> **CONTRACT:** MAX_SIGNALS = 64, fixed-dimensional interfaces, masking for inactive slots, preserved retired slots until reclamation, and `signal_set_version` on every MetaTask.

## 4.5 Frozen Inference Contract

**Live inference uses frozen `theta_day_prime`. No gradient updates on the live path under any circumstances.**

| Mode | When | What Happens | Parameters Used |
|---|---|---|---|
| Nightly adaptation | After close, before next open | Inner loop: K steps on today's episode. Produces `theta_day_prime`. | `theta_meta → theta_day_prime` |
| Daytime inference | Market hours | Feedforward: `encoder(c_t) → z`, `policy(theta_day_prime, z) → weights`. No gradients. | Frozen `theta_day_prime` |
| BOCPD trigger | Intraday change-point (Phase III+) | Emergency re-adapt: K=1–2 steps on post-CP bars. Replaces `theta_day_prime`. | Updated `theta_day_prime` |

**Staleness contract.** For daily strategies, adaptation is at most ~16 hours stale by market close. The regime embedding z is computed fresh on every bar, so allocation weights can still respond to within-day regime changes.

**Scope.** Phase II target: daily and 60–120 minute horizons with actual inner-loop adaptation. Sub-15 minute horizons: frozen inference only.

## 4.6 Embedding Vocabulary

Two embedding types exist. They are never the same vector and must never share a field name.

| Name | Dimension | Produced By | Lives On | Purpose |
|---|---|---|---|---|
| `regime_embedding` | 64 (float32) | `context_encoder.py` | MetaTask (per-timestamp) | Indexes task distribution; input to meta-policy |
| `signal_embedding` | 64 (float32) | Signal Factory (Phase IV) | Signal ABC (per-signal-version) | Identity vector for retrieval and catalog organization |

**Phase I.** Signal ABC defines `signal_embedding: Optional[np.ndarray] = None`. `regime_embedding` not yet computed.

**Phase II.** `regime_embedding` produced by context encoder. `signal_embedding` remains None.

**Phase IV.** Signal Factory computes `signal_embedding` for each signal.

## 4.7 RiskFn Protocol

RiskFn is no longer treated as a black-box placeholder. Phase I-G is where the RiskFn Protocol is frozen: what allocator outputs it consumes, what risk-budgeting semantics are allowed, what invariants remain non-negotiable, and which parts stay outside Phase II scope.

In runtime terms, Phase II only needs the allocator-to-risk interface boundary to be explicit and versioned. Execution-serious calibration loops, broker-specific risk enforcement, and operator escalation paths remain Phase III work. This preserves forward compatibility without letting risk semantics become an undocumented gap.

## 4.8 Signal Generation Protocol / Signal-Admission Path

Signal breadth is governed by an explicit admission path rather than an informal “add signals as needed” habit. The Signal Generation Protocol defines how candidate signals are proposed, what evidence they must emit, how identity/versioning is assigned, and how admission differs from promotion.

This matters before Phase IV because Phase I-G and Phase II-0 need the policy surface even when operational signal-factory machinery does not yet exist. `signal_embedding` may be seeded as a contract topic earlier, but it remains a Phase IV operational implementation surface rather than a current system fact.

Event-driven and non-tabular data entry also belong here as planned contract topics: they are admitted only through governed identity, PIT discipline, and evidence requirements, not by bypassing the existing signal path.

## 4.9 Feature Frontier / Alternative-Data Ingestion

Alternative-data expansion is a governed frontier, not a default assumption. Phase I-G freezes admissibility and PIT rules at the architectural level: provenance requirements, latency/availability semantics, replayability expectations, and the conditions under which non-price data may enter the feature or signal stack.

This section is forward-compatible with multiple later directions without claiming they are current scope:

- event-driven and non-tabular data entry are planned contract topics, not delivered runtime features;
- selective alternative-data entry may inform Phase II representation work only where the protocol explicitly justifies it;
- broader alternative-data expansion at scale remains Phase IV work;
- cross-asset transfer belongs to Phase IV+;
- differentiable portfolio optimization is a III+/IV+ research topic, not a current build commitment;
- LLM-assisted alpha mining remains IV+ / vision-level only.

## 4.10 Signal ABC Extension

Additive fields for meta-learning integration. No changes to existing Signal ABC fields.

| Field | Type | Added In | Description |
|---|---|---|---|
| `signal_embedding` | Optional[np.ndarray] | Phase I (as None) | Per-signal identity vector. |
| `slot_index` | int | Phase II | Position in fixed 64-slot vector. Assigned at registration, never reassigned. |
| `regime_sensitivity` | Optional[dict] | Phase II+ | Per-regime-class IC average. Populated after evaluation history accumulates. |

## 4.11 `meta_validity_report.json`

Emitted by the MetaLearner gate (ML-6). Added to run_bundle from Phase II forward.

| Field | Type | Description |
|---|---|---|
| `schema_version` | str | `"v1"` |
| `inner_loop_gain_by_regime` | dict[str, float] | Mean IC improvement per 5-class regime |
| `inner_loop_gain_harvey_t` | float | Harvey t-statistic on gain distribution |
| `encoder_clustering` | dict | `{within_cosine, cross_cosine}` |
| `proxy_ic_correlation` | float | Pearson correlation between proxy improvement and IC improvement |
| `crisis_episode_ic` | dict[str, float] | Per-episode IC on held-out crisis episodes |
| `forgetting_delta` | float | IC degradation on older held-out tasks |
| `confidence_ece` | float | Expected calibration error |
| `net_allocation_sharpe` | float | Walk-forward Sharpe using meta-policy weights, net of TC |
| `signal_set_version` | int | Active signal set version at evaluation time |
| `anti_goodhart_gap` | float | Ratio: held-out crisis IC / in-distribution test IC |
| `determinism_check` | str | PASS if same task + theta → same theta_prime on CPU |
| `overall_result` | str | PASS or FAIL |

---

# 5. Validation-Gated Defaults

*This section documents the proposed architectural decisions that are defaults subject to empirical confirmation.*

## 5.1 Inner Loop Parameter Scope (Validation-Gated)

**Proposed default: Hybrid ANIL inner loop + Reptile outer loop.**

| Parameter Group | Contains | Inner Loop | Outer Loop |
|---|---|---|---|
| Base feature extractor (`phi_encoder`, `phi_body`) | Context encoder layers 1–2 | Frozen | Updated |
| Conditional normalization (`psi_condnorm`) | `γ(z), β(z)` affine params | Adapted | Updated |
| Allocation head (`h_alloc`) | Hidden → per-signal utility → softmax | Adapted | Updated |
| Confidence head (`h_conf`) | Hidden → `confidence_scalar` | Optional | Updated |
| Regime head (`h_regime`) | Hidden → regime_class logits | Frozen | Updated |

**Rationale.** Conditional normalization + allocation head are ~1,100 parameters total for the default regime and signal dimensions. The base encoder learns a shared representation across all regimes while the inner loop stays latency-feasible.

**Fallback.** If inner-loop gain Harvey t < 3.0 after full task pool construction, promote to full Reptile (all parameters adapt in inner loop) only if the failure is attributable to adaptation scope rather than task exchangeability.

## 5.2 Training Loss: Soft-Rank IC + Turnover Penalty (Validation-Gated)

**Proposed default:** differentiable soft-rank IC + turnover penalty + EWC.

- **Component 1 — Soft-rank IC:** differentiable approximation to Spearman correlation via soft-rank operator.
- **Component 2 — Turnover cost:** `lambda_TC * Σ|w_t − w_{t-1}| * cost_per_unit`. Initial `lambda_TC = 0.01` `⚑ VALIDATE`.
- **Component 3 — EWC penalty:** `lambda_EWC * Σ F_i(theta_i − theta*_i)^2`. Initial `lambda_EWC = 0.1` `⚑ VALIDATE`.

**Metric hierarchy.** Training objective is differentiable. Model selection uses true Spearman IC + Harvey t. Promotion gates use exact metrics and hard criteria.

**Fallback.** If proxy–IC alignment cannot be stabilized, see Core Lock 4 fallback chain: pairwise ranking → differentiable Spearman → LambdaRank → IC fine-tuning.

## 5.3 Curriculum & Bootstrap Sampling (Validation-Gated)

**Proposed default:** bootstrap phase samples uniformly across 5-class buckets with a crisis floor of >= 10% per batch. After bootstrap, PER-like task replay uses inner-loop gain as the priority signal.

**Fallback.** If PER-like sampling causes instability or provides no measurable gain over uniform-plus-floor, revert to uniform sampling with a hard crisis minimum.

**Crisis governance rules (non-negotiable).**

1. **Crisis floor is non-negotiable.** The >= 10% crisis batch allocation is a hard floor.
2. **Anti-Goodhart holdout must be locked before training.**
3. **No compensating parameter drift for sparse crisis data.**

## 5.4 EWC Configuration (Validation-Gated)

**Proposed default:** EWC with diagonal Fisher on a capped, stratified anchor set. Sweep `lambda_EWC in {1, 10, 30, 100}` in Phase II; migrate to online EWC with decay gamma as the task pool grows.

**EWC Fisher compute note.** Compute on a capped anchor set rather than the full historical pool so each bucket contributes equally to parameter importance estimation.

**Fallback.** If EWC proves insufficient at any lambda, periodic warm-start retraining from a checkpoint may be more effective than online EWC.

---

# 6. Runtime Lifecycle and Control Plane

*This section is the operational runtime model.*

## 6.1 Outer Loop Cadence

The Reptile outer-loop trainer executes nightly after market close.

| Cadence | What Happens | Frequency |
|---|---|---|
| Nightly | Inner-loop adaptation: today's episode → `theta_day_prime` for tomorrow | Every trading day |
| Nightly | Outer-loop Reptile update across task batch | Every trading day |
| Weekly | EWC Fisher diagonal refresh on current anchor set | Friday close |
| Monthly | Curriculum rebalance and crisis replay refresh | 1st trading day |
| Monthly | Gate evaluation on held-out set → `meta_validity_report.json` | 1st trading day |
| Quarterly | Signal retirement review | Quarter end |

## 6.2 Parameter Lifecycle

| Object | Written by | Read by | Persisted | Failure handling |
|---|---|---|---|---|
| `theta_meta` | `reptile_trainer.py` outer loop | Trainer inner loop; `meta_policy.py` via `theta_day_prime` | Nightly checkpoint; artifact registry | Roll back to last known-good checkpoint if gate fails |
| `theta_task_prime` | Trainer inner loop | Outer-loop loss computation | Not persisted | Skip/log on divergence; three consecutive failures abort nightly run |
| `theta_day_prime` | Trainer after gate pass | `meta_policy.py` at inference time | Nightly checkpoint | If nightly training fails, live inference continues on previous `theta_day_prime` |

## 6.3 Nightly Training Flow

```text
Historical tasks from TaskRegistry
    ↓ Curriculum sampler
    ↓ For each task Ti in batch:
        Support set → K inner gradient steps → θ_task_prime_i
        Query set IC(θ_task_prime_i, Q_i) → inner-loop gain
    ↓ Reptile outer update
    ↓ EWC penalty update
    ↓ Emit meta_validity_report.json
    ↓ Gate CLI validates report → promote θ_day_prime if PASS
```

**Nightly training failure.** If training fails, live inference continues on the previous session's `theta_day_prime` without interruption. Operator alert is emitted. Retry with previous checkpoint as warm start. If three consecutive nights fail, revert to EnsemblePipelineStrategy pending diagnosis.

## 6.4 Inference Flow

```text
OHLCV + alt data
    ↓ DataView.as_of(T)
    ↓ Feature ops
    ↓ Context encoder: c_t → z ∈ R^64
    ↓ Signal library: z → K Alpha IR signals
    ↓ Meta-policy: z + IC_vec → allocation_weights ΔK
    ↓ SizingFn: allocation_weights → base positions
    ↓ confidence_scalar applied as post-sizing multiplier (default contract)
    ↓ (pilot / ADR-gated) uncertainty-aware routing — not default; see Core §2.5.2
    ↓ Structured post-allocator conditioning (II-D target): turnover / liquidity / capacity / drawdown overlays
    ↓ RiskFn → Orders → Fills → Ledger
```

**Vision note.** Layer **D** (post-allocator conditioning) is **visibly separate** from allocator “intelligence.” Near-term value may concentrate there **without** proving allocator superiority; allocator proof remains its own **net-of-cost** comparison to the simpler baseline.

---

# 7. Promotion, Rollback, and Kill Model

*This section summarizes the lifecycle governance model. Core v2.0.0 §9 is the full treatment and governs in all conflicts.*

## 7.1 Migration Stages

**Stage 1 — Shadow Mode.** Meta-policy emits `allocation_weights` and `confidence_scalar` but live sizing uses EnsemblePipelineStrategy. Entry requires all ML-1 through ML-6 gates passed and clean nightly reports. Exit requires shadow IC >= EnsemblePipelineStrategy IC on >= 15 consecutive trading days `⚑ VALIDATE`.

**Stage 2 — Capped Blend.** Live orders are a blend: `(1 − α) × EnsemblePipelineStrategy + α × meta_policy`. Alpha capped at 0.3 `⚑ VALIDATE` initially. Capital and exposure guardrails are enforced independent of IC results.

**Stage 3 — Full Promotion.** Meta-policy is the live allocator. EnsemblePipelineStrategy retained as fallback. Entry requires all Core promotion requirements satisfied, Stage 2 exit criteria met, and operator sign-off recorded in the release manifest.

## 7.2 Automatic Rollback Triggers

- Live IC degradation > 20% sustained over 10 consecutive trading days `⚑ VALIDATE`
- `allocation_weights` variance exceeds trained-period baseline by > 2× for 5+ sessions `⚑ VALIDATE`
- `confidence_scalar < 0.1` sustained for 3+ sessions `⚑ VALIDATE`
- Any reproducibility or data-integrity incident
- Nightly training failure for 3 consecutive nights
- Breach of approved gross exposure envelope or sector/factor neutrality limits

**Rollback target.** Most recent `theta_day_prime` that passed a clean gate run. EnsemblePipelineStrategy is the outer fallback if no clean checkpoint exists within the prior 5 nightly runs.

## 7.3 Kill Criteria (Summary)

Core v2.0.0 §9.3 and §9.3.1 govern the full kill framework including the operational burden scorecard.

- Inner-loop gain Harvey t < 3.0 after full task pool construction
- No net Sharpe uplift over XGBoost baseline after TC across the full walk-forward validation window
- Context encoder clustering fails and cannot be repaired
- Crisis episode IC <= 0 on held-out crisis windows after curriculum adjustment and replay tuning
- Operational burden exceeds measured benefit per Core §9.3.1

**What kill does not mean.** Kill of the full Reptile architecture does not preclude narrower uses of meta-learning concepts.

---

# 8. Observability and Operator Controls

*This section describes the runtime observability surface. Core v2.0.0 §11 is the full specification.*

## 8.1 Required Dashboard Metrics

| Metric | Alert Condition |
|---|---|
| Inner-loop gain by regime_class | Alert if any bucket drops to <= 0 for 3+ consecutive runs |
| Context encoder clustering score | Alert if within-regime cosine similarity < 0.55 `⚑ VALIDATE` |
| Forgetting metric (held-out IC) | Alert if IC degradation exceeds 10% `⚑ VALIDATE` |
| Task-pool coverage by bucket | Alert if any bucket falls below minimum count |
| `confidence_scalar` — mean | Alert if mean < 0.2 for 3+ sessions `⚑ VALIDATE` |
| `confidence_scalar` — ECE | Alert if ECE exceeds threshold `⚑ VALIDATE` |
| `confidence_scalar` — realized-quality correlation | Alert if rolling correlation drops below floor `⚑ VALIDATE` for N runs |
| Nightly training wall-clock | Alert if training exceeds 2× rolling 30-day average `⚑ VALIDATE` |
| `meta_validity_report.json` overall_result | Alert immediately on any FAIL |

## 8.2 Required Operator Controls

| Control | Effect |
|---|---|
| Pause nightly training | Stops outer-loop updates; live inference continues on last `theta_day_prime` |
| Rollback `theta_day_prime` | Reverts live inference to specified checkpoint |
| Freeze SignalCatalog | Prevents new signals from being added to the task library |
| Override allocation weights | Applies operator-specified allocation weights for one session |
| Force shadow mode | Drops meta-policy from live orders; reverts to EnsemblePipelineStrategy |
| Lock crisis holdout manifest | Prevents modification to the Anti-Goodhart holdout set |

---

# 9. Held-Out Crisis Protocol & Anti-Goodhart Gate

*This section is a non-negotiable governance contract. It specifies the data split that the Anti-Goodhart gate enforces.*

## 9.1 Permanent Held-Out Episodes

The following are permanently excluded from the training task pool. They are used only for gate evaluation.

| Episode | Date Range | Role | Tuning? |
|---|---|---|---|
| Global Financial Crisis | 2007-10-01 to 2009-03-31 | Primary held-out test | Never |
| COVID Crash | 2020-02-01 to 2020-06-30 | Secondary held-out test | Never |

### Crisis Replay Buffer (Training Data, Not Held Out)

| Episode | Date Range | Role |
|---|---|---|
| Dot-Com Bust | 2000-03-01 to 2002-10-31 | Crisis replay (training, >= 10% batch allocation) |
| Rate Shock 2022 | 2022-01-01 to 2022-10-31 | Crisis replay (training) |
| Future BOCPD crises | Dynamic | Added to replay buffer as detected |

## 9.2 Anti-Goodhart Gate

| Criterion | Threshold | Diagnostic if Failing |
|---|---|---|
| Anti-Goodhart protocol | Held-out crisis evaluation set excluded from meta-training, hyperparameter tuning, and curriculum-priority calibration. Gate fails if any holdout task_id appears in trainer or tuning logs. | Lock a permanent crisis holdout manifest. Verify no leakage in task sampling. |
| Task-pool sufficiency | Minimum task count met in every curriculum bucket before nightly outer-loop training is enabled. Defer to Core §10.2 for per-bucket minimums. | Expand history or assets. Do not tune around sparse crisis buckets. |

## 9.3 Illustrative Data Split

| Partition | Date Range | Purpose |
|---|---|---|
| Training pool | 2003–2006, 2010–2019, 2021, 2023–2025 | Outer-loop task batches + curriculum |
| Crisis replay | 2000–2002, 2022 | Training with elevated batch allocation |
| Validation (tunable) | Most recent full non-holdout year | Hyperparameter selection, architecture search |
| Held-out: GFC | 2007-10 to 2009-03 | Anti-Goodhart gate only |
| Held-out: COVID | 2020-02 to 2020-06 | Anti-Goodhart gate only |

> **CONTRACT:** GFC and COVID are permanently held out. Never used for training, curriculum tuning, or architecture selection.

---

# 10. Determinism Environment

> **DETERMINISM:** D3 determinism gate runs on CPU only with `torch.use_deterministic_algorithms(True)` and fixed CUBLAS workspace. GPU training is permitted; gate verification runs a CPU-reproduced forward+backward pass on a single reference task. CPU result must match exactly. GPU-to-CPU comparison must be within D2 semantic tolerance.

**Practical implication.** All gate evaluations are executed on CPU. The nightly training loop may use GPU. The gate's reference task is stored in the TaskRegistry with a deterministic seed.

---

# 11. Task Pool Size Analysis

MAML/Reptile literature uses hundreds to thousands of tasks. Financial data is limited.

| Scenario | Avg Episode | Total Tasks | Crisis Tasks | Sufficient? |
|---|---|---|---|---|
| Conservative (long episodes) | 80 bars | ~80 | ~4 | Insufficient |
| Moderate (BOCPD default) | 40 bars | ~160 | ~8–12 | Marginal |
| Overlapping (10-bar stride) | 40 bars, stride 10 | ~600 | ~30–40 | Adequate |
| Multi-symbol expansion | 40 bars × 15 symbols | ~2,400 | ~120 | Strong |

### Overlapping Windows with Regime-Anchored Stride

Generate tasks with a sliding window anchored within the same regime episode. Combined with multi-symbol construction, the effective pool can reach 600–2,400 tasks.

> ⚠ `Overlapping tasks introduce correlation.` The outer-loop batch sampler must ensure no two tasks in the same batch share > 50% of their bars.

**Minimum task counts.** Per-bucket minimums are specified in Core §10.2 and remain `⚑ VALIDATE` pending calibration from MarketMind historical data.

---

# 12. Open Research (Deferred, Not Forgotten)

Topics explicitly deferred from Phase II. Phase II architecture decisions maintain forward compatibility with all of these.

| Topic | Why Deferred | Forward Compatibility Requirement | Target Phase |
|---|---|---|---|
| Attention-based context encoder (SNAIL) | 2-layer MLP sufficient for Phase II; attention adds complexity | Base encoder is frozen in inner loop and can be swapped without changing the adaptation budget | III |
| Neural Processes for uncertainty | Deterministic encoder needed first | `regime_embedding` can later become a distribution without changing MetaTask schema | III |
| Signal Factory (auto signal generation) | Requires mature SignalCatalog + stable meta-policy | `signal_embedding` field, MAX_SIGNALS headroom, and slot assignment contract are already in place | IV |
| Joint embedding space | Requires both regime and signal embeddings to be mature | Both use D=64 initially; dimensionality can diverge later | IV+ |
| Cross-asset transfer | Requires InstrumentSpec registry and proven allocator portability | MetaTask schema is multi-asset compatible | IV+ |
| Differentiable portfolio optimization | Requires validated allocator behavior and tighter execution/risk calibration | RiskFn boundary remains versionable without changing MetaTask schema | III+/IV+ |
| LLM-assisted alpha mining | Requires governed discovery, admission, and retirement controls first | Signal-admission path and validation layer stay explicit | IV+ |
| Real-time inner loop (intraday) | Latency budget impossible for <15 minute horizons in Phase II | Frozen inference path with fresh z per bar provides regime awareness without adaptation | III+ |
| Full Reptile (all params adapt) | Hybrid ANIL default is sufficient unless Harvey t < 3.0 | Fallback documented in §5.1 and Core Lock 3 | II (fallback) |

> **Design principle:** every deferred topic has at least one forward-compatibility requirement met in Phase II.

---

# 13. Current Implemented Substrate

## 13.1 Implemented as of v3.6.0 (2026-02-28 cutoff)

| Component | Update |
|---|---|
| Gate pipeline | Optional artifacts validated; reason-code taxonomy extended; cost_model_id yields VALID. |
| Strategy layer | Optional imports tolerated; StrategyRegistry raises actionable errors; dual feature path (ADR-001) in `materialize_features`. |
| Test architecture | `conftest` thinned; reusable `_plugins` for seeds, data, hardware, and stats. |

## 13.2 Post-3.6.0 Additions (through **`VERSION.md` 6.2.2** companion baseline, April 2026)

| Area | Update |
|---|---|
| Canonical artifact storage | ADR-002 accepted: `srcPy/artifact_registry/` designated canonical. LocalCAS and RunRegistry are the canonical storage primitives. |
| Reconstructible bundles | `bundle_manifest.json` is the contract for run-bundle reconstructibility; gate and run pipeline use it for verification and promotion. |
| Domain-qualified identity | Canonical identity uses `cas.v1:b3-256` and `attest.v1:jcs-sha256`. |
| PIT orchestration and source adaptation | 4.1.0 delivered the PIT orchestration boundary; 4.2.0 extended PIT guarantees into governed daily source adapters. |
| Feature-path integrity | 4.3.0 closed the single-path governed feature execution lock and expanded the canonical op floor. |
| Governed strategy slices | 4.4.0 landed `stat_arb_pairs` on the trusted path; 4.5.x materially advanced the governed momentum package spine and bundle-facing reporting. |
| Signal identity and governance substrate | 4.5.0–4.5.4 added SignalCatalog with stable `slot_index`, `screening_report.json`, stricter governed statistical-validity/cost artifacts, DataLineageGate, artifact-registry-owned hashing/canonicalization boundaries, evidence-backed canonical-frame CI reporting, and Phase I-E companion-doc closure. |
| Documentation baseline | Prior milestones through **4.18.5** remain true as substrate history (**MLN-02-AMD-01**, **OI-43**, bounded **II-0A** harness path, **OI-39**, II-0 empirical research scaffold). The **`VERSION.md` 6.2.2** companion advance records **WS-1 / WS-2 / WS-3** and **II-0A** completion in companion truth, freezes the strict-H3 RG-09 **task-validity reference anchor** at `run_bundles/rg09_reference_v1`, and keeps the Phase II **challenger-vs-incumbent** comparison boundary explicit: predicates for allocator comparison reference the **XGBoost incumbent**, not the RG-09 reference anchor. Companion suite stamps advance per §14 DOCMAP (Implementation Plan **6.5.5**, Technical Roadmap **1.4.26**, Core **1.2.24**, this document **1.3.5**, Resolution Ledger **1.0.51**, README **6.2.2**). Phase I-A through I-F remain closed on the canonical path. |
| Remaining Phase I-G / II boundary items | **RG-09** promotion-level empirical closure may still be tracked as **PARTIAL** where the ledger distinguishes reference-anchor diagnostics from allocator promotion evidence; governed momentum follow-ons (**`OI-34`**, **`OI-32`**), Phase II normative locks (**MLN-01**–**07**), and **OI-15** golden-vector work remain active where open in Resolution Ledger **v1.0.51**. |

---

<!-- MM:BEGIN:RECENT_CHANGES key="MetaLearningArchitectureVision" window=3 -->

| Release | Date | Architecture Vision impact |
|---|---|---|
| 1.3.5 | April 2026 | Companion-sync to **`VERSION.md` 6.2.2**: title-page, §13.2, DOCMAP, and SOURCE_STAMP advanced; **WS-1 / WS-2 / WS-3** and **II-0A** recorded complete in companion truth; **§13.2** documents the frozen RG-09 reference anchor path and incumbent-vs-anchor boundary. |
| 1.2.20 | April 2026 | Companion-sync: documentation baseline advanced to **4.18.5** / **1.0.21**; **OI-39** closed; II-0A harness and II-0 empirical meta-validity scaffold treated as implemented; §13.2 and DOCMAP updated; full RG-09 empirical closure remains **PARTIAL**. |
| 1.2.19 | March 2026 | §4.2 **MLN-02-AMD-01:** Level 2 `crisis` is `vol_hi AND severity_flag` (PIT-safe expanding `vol_score_raw` percentile ≥ p90, **RG09-V12** ⚑ VALIDATE); explicit BOCPD-as-segmentation-primitive note; historical crisis frequency tagged ⚑ VALIDATE. Companion stamps → **4.18.0** / **6.4.23** / **1.0.19**. |
| 1.2.18 | March 2026 | Companion stamp sync: DOCMAP/SOURCE_STAMP to **4.17.0** / **6.4.22** / **1.0.18**; §13.2 documentation-baseline rows updated so MOM-020 is closed rather than listed as a remaining boundary item; no architectural thesis change. |
| 1.2.17 | March 2026 | Companion stamp sync: DOCMAP/SOURCE_STAMP to **4.16.0** / **6.4.21** / **1.0.17**; §13.2 documentation-baseline rows updated for **OI-37**/**OI-38** closure and current ledger; no architectural thesis change. |
| 1.2.16 | March 2026 | §1.5 hierarchical target A–D + three seriousness layers; inference flow shows post-allocator conditioning and non-default routing; §4.3 routing pilot callout; multi-timescale vision note. |
| 1.2.14 | March 2026 | F-1/F-2 planning baseline carried forward; this edition adds forward-compatibility notes for RiskFn, signal admission, and alternative-data contracts while keeping signal-factory and frontier topics explicitly later-phase. |
| 2.0.0 | March 2026 | Major revision aligned to Core v2.0.0. Rewrote Purpose to remove "closes every remaining open question" framing; added Decision Framing, Validation-Gated Defaults, Promotion/Rollback/Kill, and Observability sections; refreshed implemented-substrate references through VERSION.md 4.5.4. |
| 1.2.12 | March 2026 | Prior companion-edition framing: committed architectural decisions, interface contracts, and held-out crisis protocol aligned through the 4.5.2 suite. |
| 1.0.0 | March 2026 | Initial release: architectural decisions, interface contracts, held-out crisis protocol, determinism environment, and task-pool analysis. |

<!-- MM:END:RECENT_CHANGES -->

# 14. Document Relationship Map

<!-- MM:BEGIN:DOCMAP -->

| Document | Version | Role |
|---|---:|---|
| Meta-Learning Architecture Vision | 1.3.5 | High-level architectural vision and system framing |
| Implementation Plan | 6.5.5 | Executable implementation path, deliverables, and phase gates |
| Technical Roadmap | 1.4.26 | Strategic build order and dependency-aware roadmap |
| Meta-Learning Core | 1.2.24 | Research supplement defining task schema, inner/outer loop mechanics, curriculum, and acceptance criteria |
| Resolution Ledger | 1.0.51 | Resolution ledger and workflow state dashboard |
| README.md | 6.2.2 | Suite overview, current status, and navigation |
| VERSION.md | 6.2.2 | Canonical release ledger |

<!-- MM:END:DOCMAP -->

<!-- MM:BEGIN:SOURCE_STAMP -->

*Meta-Learning Architecture Vision v1.3.5 · April 2026 · Companion to Implementation Plan v6.5.5 · Technical Roadmap v1.4.26 · Meta-Learning Core v1.2.24 · Resolution Ledger v1.0.51 · README.md 6.2.2 · VERSION.md 6.2.2*

<!-- MM:END:SOURCE_STAMP -->

<!-- MM:END:DOCBODY -->
