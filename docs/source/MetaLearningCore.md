**MarketMind**

**Meta-Learning Core**

<!-- MM:BEGIN:TITLEPAGE -->
Version 1.2.19 · April 2026 · Proprietary

Companion documents: Implementation Plan v6.4.32 · Technical Roadmap v1.4.21 · Meta-Learning Architecture Vision v1.2.20 · Resolution Ledger v1.0.40 · README.md 4.18.12 · VERSION.md 4.18.28
<!-- MM:END:TITLEPAGE -->

*Research agenda supplement — task definition, training mechanics, empirical validation program, and acceptance criteria*

*Audience: Internal engineering, technical stakeholders*

<!-- MM:BEGIN:DOCBODY -->

# Meta-Learning Core

<!-- MM:BEGIN:DOCMAP -->

| Document | Version | Role |
|---|---:|---|
| Meta-Learning Core | 1.2.19 | Research supplement defining task schema, inner/outer loop mechanics, curriculum, and acceptance criteria |
| Implementation Plan | 6.4.32 | Executable implementation path, deliverables, and phase gates |
| Technical Roadmap | 1.4.21 | Strategic build order and dependency-aware roadmap |
| Meta-Learning Architecture Vision | 1.2.20 | High-level architectural vision and system framing |
| Resolution Ledger | 1.0.40 | Resolution ledger and workflow state dashboard |
| README.md | 4.18.12 | Suite overview, current status, and navigation |
| VERSION.md | 4.18.28 | Canonical release ledger |

<!-- MM:END:DOCMAP -->

---

# 0. Decision Framing

*This section is the front door. Read it before any other section. It defines what the architecture claims, what can falsify it, and what governs the decision to kill it.*

## 0.1 Architectural Claim

The **governed hypothesis** is that meta-learning is the preferred architecture for **task-aware adaptation** across **non-exchangeable market tasks**—episodes indexed by volatility, liquidity, macro/cost/objective regimes—not merely a better timestamp classifier or one-step return predictor. Individual strategies — stat-arb, momentum, mean-reversion — are not combiners to be averaged; they populate tasks drawn from a **task distribution**. The meta-learner is the intended allocation brain, not a late-arriving ensemble weighter. This claim supersedes naive ensemble averaging **if and only if** the empirical program falsifies the simpler baseline. The architecture **asserts** that rapid inner-loop adaptation (<= 10 gradient steps at daily frequency) *may* produce **decision utility after frictions** that a static or simpler regime-conditioned combiner cannot match **net of costs**; that remains **unproven** here. Every Phase II architectural decision is subject to this framing.

## 0.2 Null Hypothesis

A **simpler regime-conditioned baseline allocator** — specifically an XGBoost ensemble with BOCPD-triggered regime conditioning, equivalent to the best configuration achievable with existing MarketMind infrastructure — **remains the incumbent production outcome** until falsified. It matches or exceeds the Reptile meta-policy **net of costs, robustness, and operational complexity**. The null is not "meta-learning does nothing." The null is that the added machinery (context encoder, inner/outer loop separation, regime-indexed curriculum, EWC, crisis replay) does not deliver **measurable net benefit** on **post-adaptation utility after frictions** after accounting for cost and complexity. The burden of proof falls on the meta-learning architecture. The empirical de-risking program in Section 4 is the vehicle for rejecting this null. **Fail gracefully:** if the challenger does not win, **keep the simpler baseline**; if regime conditioning itself fails, collapse toward **B2/B1-style** governed paths rather than compounding complexity.

## 0.3 What Must Be Proven

Five empirical claims must be resolved before Phase II implementation is committed. Early empirical closure may begin in Phase I-G and Phase II-0, but none of those early results silently authorize promotable adaptive-learning machinery. None of these claims are assumed; all require experimental evidence.

1. **Task non-exchangeability.** Regime-indexed episodes are meaningfully distinct. The meta-learner adapts differentially across task types and does not reduce to memorizing task identity.
2. **Adaptation usefulness.** Inner-loop gradient steps produce IC improvement on held-out query sets, not merely on the support set used for adaptation.
3. **Encoder coherence.** The context encoder produces a structured regime embedding where similar embeddings correspond to identifiably similar market conditions.
4. **Proxy alignment.** The differentiable ranking surrogate correlates with exact Spearman IC improvement on unseen tasks, such that training on the proxy does not diverge from the target metric.
5. **Continual robustness.** EWC plus crisis replay prevents catastrophic forgetting on historical regimes without collapsing plasticity on new tasks.

## 0.4 Kill-Criteria Preview

The architecture is killed — not paused, not reduced in scope — if any of the following are confirmed by the validation program:

- Inner-loop gain Harvey t < 3.0 on the full task pool after task pool construction is complete.
- No net Sharpe uplift over the XGBoost baseline after transaction costs across the full walk-forward validation window.
- Context encoder clustering fails and cannot be repaired by capacity increase or extended pre-training.
- Crisis episode IC <= 0 after curriculum adjustment, replay tuning, and crisis augmentation.

The full framework governing promotion, rollback, and kill decisions is in Section 9.

## 0.5 Phase Relationship

Phase I-G is where the research world, protocol stack, and proof burden are frozen. That is the correct place to run early empirical closure on baseline policy, task validity, non-exchangeability, RiskFn semantics, and threshold handling.

Phase II-0 is where those I-G decisions become reproducible, non-promotable harnesses: pilot artifacts, reference runs, diagnostics, and report scaffolds. Pre-trainer empirical pilots are therefore allowed and encouraged in I-G and II-0, because the program should discover structural failure early rather than after a full trainer build.

Phase II remains the first promotable adaptive-learning build phase. Trainer commitment stays gated by W2 and Tier 1 readiness, and final validation gates still govern promotion, rollback, and kill logic even when early pilots look promising.

## 0.6 What the March 2026 evidence stack supports (synthesis, not results)

Companion docs integrate twelve internal reports as **obligations and falsifiers**, not as proof of edge:

- **Task validity is fragile.** Regime episodes must be **leakage-safe**, **non-exchangeable**, and **task-like** enough to justify meta-learning; otherwise the trainer path should **stop early**—this is a **structural gate**, not preprocessing trivia.
- **Replay and honest baselines are load-bearing** relative to storytelling about elegant continual learning—claims require **measurement harnesses**, not architecture enthusiasm.
- **Artifact-level evaluation is anti-self-certification**: bundle-local evaluation surfaces should be emitted once and compared via immutable artifacts rather than recomputed by the layer that judges them.
- **Net uplift after costs** is the hardest promotion gate; **forecast-quality** and **stylized reward** gains are not substitute evidence.
- **Simpler baselines remain legitimate outcomes** if complexity cannot prove net benefit.
- **Governance is survivability insurance** (rollback, kill, shadow, staged promotion, drift triggers)—it protects against operational failure modes; it **does not** validate allocator alpha.
- **Deployment-layer / post-allocator conditioning** may matter **more near-term** than allocator novelty for **realistic capital expression**, yet it **does not relax** the burden to beat the simpler baseline **net of costs**.
- **Uncertainty-aware routing** is a **Phase II-0 pilot hypothesis** layered on the **`confidence_scalar` contract**; default semantics remain **post-sizing attenuation** unless routing earns promotion through **reject-set EV** evidence after costs.

**Anti-patterns (documentation and research hygiene):** treating rolling-window refits as meta-learning without task structure; claiming robustness without domain-shift tests; declaring “SOTA” if edge disappears under implementation realism; using Sharpe or forecast metrics alone; treating differentiability or model scale as a moat.

---

# 1. Executive Thesis

## 1.1 What This Document Claims

The Medallion Fund's core insight is not that any individual signal is exceptional — it is that a sufficiently diverse portfolio of weak signals, continuously recombined by an adaptive learner that understands the current market regime, produces alpha that individual signals cannot. Every signal-combination system that fails to build this adaptive recombination layer ends up as an ensemble: a useful but fundamentally static average. Static averages degrade when regimes shift, and regimes always shift.

MarketMind's current architecture has excellent infrastructure — PipelineStrategy, EnsemblePipelineStrategy with adaptive weights, ChampionChallenger, BOCPD regime detection, and a plugin system with seven canonical types. What it lacks is **task identity**: a formal definition of what a learning episode is, and an architectural commitment that makes the meta-learner the allocation brain rather than a late-arriving combiner. Without task identity, Reptile has no curriculum; without a curriculum, the meta-learner reduces to a gradient-descent ensemble weighter — which is already approximated by the adaptive weights in EnsemblePipelineStrategy.

**The critical reframe:** individual strategies are not first-class entities that happen to feed a combiner. They are training tasks — episodes drawn from a distribution of market conditions — and the meta-learner is the system's brain that learns to adapt rapidly across those tasks.

## 1.2 What This Document Does Not Claim

This document does not claim that the meta-learning architecture is validated. Section 0.3 lists five empirical questions that remain open. The architecture is **proposed pending validation**; the empirical de-risking program in Section 4 is the instrument for converting the proposal into a commitment. The document does not claim that any default parameter (embedding dimension, EWC lambda, K, PER alpha) is empirically optimal — many of these are literature-plausible priors that require domain-specific calibration. Thresholds that are not yet grounded in MarketMind-specific evidence are flagged `⚑ VALIDATE` throughout.

## 1.3 Inherited Infrastructure

The following components represent proto-meta-learning infrastructure that is already built or specified. The meta-learning architecture reframes these rather than replacing them.

| Existing Component | Current Role | Reframed Role in Meta-Learning Architecture |
|---|---|---|
| EnsemblePipelineStrategy | Adaptive weight combiner over N strategy instances | Outer-loop evaluator: measures which task specializations are performing in the current regime |
| ChampionChallenger | A/B evaluation of strategy variants | Inner-loop candidate evaluator: measures fast-adaptation gain on held-out query set |
| BOCPD change-point detector | Change-point detection (slated for orchestrator-managed regime service per AQ-04; not a feature graph op in governed production use) | Task-boundary signal: triggers new learning episode when distribution shift is detected |
| RegimeDetector Protocol slot | Gating plugin for position sizing | Context encoder input: regime embedding that indexes the task distribution |
| parameter_sweep() / optuna_tune() | Hyperparameter search | Inner-loop gradient steps: fast adaptation over recent episode support set |
| Signal ABC / SignalCatalog | Catalog of tradeable strategies | SignalCatalog supplies weak learners inside each regime-episode task |
| blend() composition | Combinatoric strategy mixing | Meta-policy output: the meta-learner's allocation over the task library |

---

# 2. Canonical Definitions & Non-Negotiable Contracts

*This section is normative. All Phase II implementation must be consistent with the contracts defined here. Deviation requires an ADR.*

## 2.1 MetaTask Schema

**What it is.** A MetaTask is a regime-bounded learning episode. It is the atomic unit of both training and evaluation in the meta-learning system.

**Who creates it.** `task_generator.py` (ML-2). No other component may construct MetaTask objects.

**Where it lives.** `TaskRegistry` (`task_registry.py`, ML-1 prerequisite). Indexed by `(regime_id, t0)`.

**When it changes.** Never mutated after creation. Append-only registry. Any re-construction requires a new `task_id`.

**Invariants.**
- `task_id` = `HMAC-SHA256(regime_id + t0 + t1 + signal_ids_hash)` — deterministic, content-addressed.
- `pit_boundary` must equal the last timestamp of the support set. No feature or label may be computed using data beyond `pit_boundary`.
- `signal_ids` and `signal_mask` must be stored as an ordered, deterministic sequence so replay, EWC anchors, and gate runs remain comparable across dynamic-K changes.
- `support_set` and `query_set` must be temporally disjoint with a purge gap of at least H bars (label horizon) and an embargo gap E (default E=0 for daily; E=ceil(0.05 × episode_len) for intraday).

```yaml
MetaTask:
  task_id:        str
  regime_id:      str
  regime_class:   Literal["bull","bear","sideways","high_vol","crisis"]
  t0:             datetime
  t1:             datetime
  pit_boundary:   datetime
  support_set:    DataFrame
  query_set:      DataFrame
  signal_ids:     List[str]
  signal_mask:    np.ndarray
  active_k:       int
```

## 2.2 Regime Vocabulary

| Term | Definition |
|---|---|
| `regime_class` | Coarse curriculum bucket: `{bull, bear, sideways, high_vol, crisis}`. Used for sampling distribution and curriculum balance enforcement. |
| `regime_id` | High-granularity composite label: trend direction × realized vol quintile × BOCPD run-length state. Used for task identity, context encoder input, and TaskRegistry indexing. |
| `pit_boundary` | The point-in-time boundary for a task. No information from after this timestamp may appear in the task's features, labels, or regime label. |

## 2.3 Parameter Objects

| Object | Definition | Who writes | Who reads | Persistence |
|---|---|---|---|---|
| `theta_meta` | Learned meta-initialization. The outer-loop updates this nightly. | `reptile_trainer.py` outer loop | `reptile_trainer.py` inner loop, `meta_policy.py` | Checkpointed nightly; content-hashed via `artifact_registry/` |
| `theta_task_prime` | Per-task adapted state after K inner-loop steps. Ephemeral during training. | `reptile_trainer.py` inner loop | Outer-loop loss computation | Not persisted outside training run |
| `theta_day_prime` | Nightly-adapted state used for the next live session. Produced by applying the inner loop to the most recent completed task batch. | `reptile_trainer.py` (nightly) | `meta_policy.py` at inference time | Checkpointed; promoted to live only after gate pass |

**Hard boundary.** Live inference uses frozen `theta_day_prime`. No gradient updates on the live path.

## 2.4 Dynamic-K Contract

The active signal set may change over time as signals are added or retired from `SignalCatalog`. The following invariants apply:

- `MetaTask.signal_ids` is the canonical ordered sequence for that task. It must be stored at task creation and never reconstructed.
- `theta_meta` and all adapted states must support variable-length signal masks without re-initialization.
- Replay tasks, EWC anchors, and gate runs must use the original `signal_mask` from task creation to guarantee comparability.
- Adding a new signal to the catalog requires a new outer-loop warm-up epoch on a representative task sample; it does not invalidate existing `theta_meta`.

## 2.5 Confidence Routing Contract

`meta_policy.py` produces three outputs: `allocation_weights` (simplex over active signals), `confidence_scalar` (scalar in [0, 1]), and `regime_class` (classification head). `confidence_scalar` is applied as a post-sizing multiplier by `SizingFn` — it scales exposure, not signal ranking. `confidence_scalar` must not be used as a gate on signal selection. The `SizingFn` Protocol must remain unchanged until it is version-bumped to accept confidence explicitly (Phase III consideration).

### 2.5.1 Confidence Semantics and Calibration

**Definition.** `confidence_scalar` is a calibrated reliability estimate for the current meta-policy allocation, conditional on the current regime embedding z, support/query set consistency, and signal-set familiarity (active K relative to trained K distribution). It is not a probability of profit and is not a return forecast.

**What it is not.** `confidence_scalar` is not a free-form "uncertainty" bucket. It is not a replacement for portfolio risk limits. It must not be interpreted as a signal-selection gate. Any use outside the post-sizing attenuation role defined below requires an ADR.

**Permitted action range (Phase II).** `confidence_scalar` may only attenuate exposure after `SizingFn` computes base positions from `allocation_weights`. It may not increase exposure above the base size implied by `allocation_weights`. Formally: `live_position = base_position × confidence_scalar`, where `confidence_scalar in [0, 1]` and `base_position` is the output of `SizingFn`. Levering above base size is not permitted in Phase II under any confidence value.

**Training target.** Supervise `confidence_scalar` against a bounded realized-quality target: the next-window realized query-quality percentile clipped to [0, 1], or a binary "allocation acceptable / not acceptable" label based on net IC after costs. The training target must be chosen before model training begins and must not be changed after calibration.

**Calibration method.** After core model training, fit isotonic regression or Platt-style calibration on a held-out calibration set. Recalibrate nightly alongside the outer-loop update. Report reliability curves and Expected Calibration Error (ECE) in `meta_validity_report.json`. If ECE exceeds threshold (`⚑ VALIDATE`), recalibrate before promoting `theta_day_prime`.

**Monitoring rules.** See Section 11.1. The dashboard monitors: (a) mean `confidence_scalar` < 0.2 for 3+ sessions; (b) calibration error above ECE threshold; (c) rolling correlation between `confidence_scalar` and realized allocation quality below acceptable floor for N consecutive runs. All three are alert conditions, not just (a).

### 2.5.2 Uncertainty-aware routing pilot (non-default)

**Normative default:** `confidence_scalar` **attenuates** exposure after sizing; uncertainty also informs **risk-budget shrinkage**, **participation**, **turnover**, and **abstention** through governed mechanisms—without implying a promoted router.

**Pilot scope (Phase II-0 primary; II-D only if earned):** a **governed hypothesis** that some regions of `(z, calibration, familiarity)` space are **negative EV after costs** and merit **routing / rejection** distinct from pure attenuation. **Promotion rule:** promote routing only if MarketMind-specific evidence shows the **reject set** is negative EV after costs **and** the incumbent baseline retains positive EV there; if attenuation already captures the economic effect, **do not promote routing**. **Fail action:** remain **attenuation + simpler RiskFn path**. Any change to default `confidence_scalar` semantics requires an **ADR** and threshold governance (MLN-07).

## 2.6 Loss Hierarchy

Training uses a differentiable surrogate (pairwise ranking or soft-sort Spearman). Evaluation and gating use exact Spearman IC. Portfolio evaluation uses net-after-cost Sharpe and drawdown metrics. Surrogate improvements that do not correlate with exact IC improvements are a proxy misalignment failure (Section 7, Row 4).

## 2.7 Required Run Artifacts

| Artifact | Schema | Required from |
|---|---|---|
| `meta_validity_report.json` | v1: `{inner_loop_gain_by_regime, context_encoder_clustering_score, crisis_episode_ic, forgetting_test_result, proxy_ic_correlation, overall_result: PASS/FAIL}` | Phase II onward; every nightly training run |
| `gate_result.json` | Existing schema; add `meta_learner_gate` block | Phase II onward |
| `task_manifest.json` | `{task_id, regime_class, t0, t1, signal_ids_hash, pit_boundary}` per task used in training run | Phase II onward |

---

# 3. Research Foundation

*This section governs the six implementation locks. Each lock is framed as an assumption, its failure risk, the experiment that resolves it, the control baseline, the threshold, and the fallback if the threshold is not met. Defaults are literature-plausible priors; every lock requires an empirical gate before becoming an implementation commitment.*

## 3.1 Six Design Locks

### Lock 1 — Leakage Geometry & Episode Construction

| Field | Content |
|---|---|
| **Assumption** | 1 bar = 1 example; support→purge(H)→embargo(E)→query structure eliminates forward-looking information within a task. |
| **Why it matters** | Any leakage within a task inflates IC, making inner-loop gain appear real when it is contamination. All downstream gates are invalidated. |
| **Failure risk** | If embargo E is too short for the feature memory of the chosen signals, purge/embargo does not fully isolate support from query. |
| **Experiment** | Shuffle-label baseline: measure IC(θ′, Q_i) on tasks with scrambled labels. If leakage is present, IC(θ′, Q_i) will not collapse to zero on scrambled-label tasks. |
| **Control** | IC on scrambled-label task set. |
| **Threshold** | IC on scrambled-label tasks <= 0.01 (mean) with no positive right tail. |
| **Fallback** | Increase E: calibrate to 5–10% of episode length. If infeasible given Lmin, reduce H or use longer episodes. |

**Why this lock exists.** Leakage is the most dangerous silent failure in supervised financial ML. Within a meta-learning task the split between support and query sets is the critical boundary. If the embargo is miscalibrated for the feature memory of MarketMind's ops (RSI, KF_BETA, BOCPD), inner-loop gain will appear real when it is contamination. Every IC gate in Section 6 is then measuring noise. The leakage invariant must be verified before any IC measurement is used as evidence of adaptation. Implementation note: minimum feasible episode length is `Lmin >= ns + nq + 2H + E`; this must be enforced as a hard constraint in `task_generator.py`, not as a soft default.

**How its result affects the build path.** Run the shuffle-label leakage test on the first available task pool, before any ML deliverable beyond ML-2. If leakage is confirmed, halt and repair `task_generator.py` before proceeding to ML-3. Do not attempt to calibrate K or the proxy with a contaminated task pool — the results will be meaningless.

### Lock 2 — Task Identity & Non-Exchangeability

| Field | Content |
|---|---|
| **Assumption** | Regime-indexed episodes produce meaningfully distinct tasks. The meta-learner adapts differentially; it does not reduce to memorizing task identity. |
| **Why it matters** | If tasks are exchangeable, MAML/Reptile reduces to joint gradient descent. The meta-learning machinery adds cost without benefit. |
| **Failure risk** | Insufficient regime_id granularity causes task collapse: all tasks look the same to the meta-learner. |
| **Experiment** | Measure `Δθ = ||theta_task_prime − theta_meta||` per task. Measure inner-loop gain by regime_class. Run regime-label shuffle test: scramble regime assignments and re-measure inner-loop gain distribution. |
| **Control** | Inner-loop gain distribution under scrambled regime labels (null distribution). |
| **Threshold** | Harvey t > 3.0 on inner-loop gain; shuffle test p < 0.05. |
| **Fallback** | Increase regime_id granularity (add vol quintile subdivision). Add meta-regularization penalty on near-zero-Δθ tasks. If task collapse persists, consider switching task family (for example, rolling-window with regime-class conditioning). |

**Why this lock exists.** Reptile's theoretical advantage over joint gradient descent depends entirely on task non-exchangeability. If the meta-learner cannot distinguish a bull episode from a bear episode — if regime-indexed tasks look identical in feature space — then the inner loop is adapting to noise and the outer loop has no curriculum signal. This is the foundational structural bet of the architecture. Regime labels are a prior about task distinctiveness, not evidence of it; the shuffle test is the evidence. Task collapse is the single most likely cause of Harvey t < 3.0, which is a kill criterion in Section 9.3.

**How its result affects the build path.** Diagnose exchangeability early — with only ML-1 (context encoder) and ML-2 (MetaTask generator) in place, before the full training stack is built. A confirmed non-exchangeability result gates ML-3 (Reptile trainer). A collapse result that cannot be repaired by regime_id granularity increase or meta-regularization is grounds for reviewing the entire task family definition before any further Phase II investment.

### Lock 3 — Inner-Loop Compute & Algorithm

| Field | Content |
|---|---|
| **Assumption** | Reptile with K=5 at daily frequency is the correct algorithm and step count. The allocation head plus conditional normalization parameters are the correct adaptation targets. |
| **Why it matters** | K too small (K=1) degenerates to joint training in Reptile. K too large inflates latency and may overfit the support set. Algorithm choice (Reptile vs ANIL vs FOMAML) determines what parameters adapt and at what cost. |
| **Failure risk** | Adaptation gain saturates before convergence (K too small) or the adaptation gain curve is monotone-increasing (overfit to support set). |
| **Experiment** | Sweep `K in {2, 5, 10, 20}`. Plot mean inner-loop gain (query IC) vs K per regime_class. Measure wall-clock per inner-loop step. |
| **Control** | K=1 (degeneracy baseline) and K=0 (no adaptation). |
| **Threshold** | Gain curve shows clear saturation. `K_optimal <= 10` at daily frequency to respect latency budget. `⚑ VALIDATE`: latency budget for inner-loop at daily frequency. |
| **Fallback** | If latency is the binding constraint, switch to ANIL (freeze encoder, adapt only allocation head). If gain does not saturate, review support set size and task definition. |

**Why this lock exists.** K=5 is a miniImageNet default with no direct finance precedent. Daily financial time series have different curvature, smaller effective batch sizes, and harder latency constraints than image classification benchmarks. K too small (K=1) degenerates Reptile to joint training; K too large overfits the support set and violates the daily inference window. Algorithm choice between Reptile, ANIL, and FOMAML is not reversible without significant rework of ML-3 — committing before the sweep is done means building the trainer twice.

**How its result affects the build path.** The `K_optimal` value and latency measurement together determine which algorithm is implemented in `reptile_trainer.py`. Run the sweep on a small task pool using ML-2 output before any ML-3 work begins. If ANIL is required, its architectural constraint (frozen encoder, adapted head only) must be reflected in the parameter lifecycle contracts in Section 5.2.

### Lock 4 — Proxy-to-Metric Alignment

| Field | Content |
|---|---|
| **Assumption** | Training with a pairwise ranking proxy (or differentiable Spearman) will improve exact Spearman IC on unseen tasks. Proxy and target metric move together. |
| **Why it matters** | If proxy improvement diverges from IC improvement, the model will be trained toward the wrong objective. All IC-based acceptance gates then measure noise. |
| **Failure risk** | Proxy overfits its own surrogate objective while true IC stagnates or degrades on held-out tasks. |
| **Experiment** | Track proxy training loss and exact IC on held-out task set simultaneously over training. Compute Pearson correlation of proxy improvement with IC improvement across training epochs. |
| **Control** | MSE regress-then-rank baseline (null proxy). |
| **Threshold** | Pearson correlation of proxy improvement vs IC improvement > 0.6 `⚑ VALIDATE`. No sustained divergence between proxy and IC trajectories after initial warm-up. |
| **Fallback** | Switch proxy: if pairwise ranking diverges, switch to differentiable Spearman (adjust epsilon); if soft-sort is unstable at small batch sizes, use LambdaRank. Add IC fine-tuning stage after proxy pre-training. |

**Why this lock exists.** The differentiable ranking proxy is the only training signal available in the outer loop. Exact Spearman IC is non-differentiable and cannot be optimized directly. If the proxy does not track exact IC, every outer-loop gradient step is moving `theta_meta` in the wrong direction — and the problem is silent until IC is measured on a held-out task set. Published finance LTR evidence establishes that ranking losses outperform regress-then-rank in cross-sectional momentum; it does not validate the proxy in a meta-learning context where the outer loop is updating a shared initialization rather than fitting a single model.

**How its result affects the build path.** The proxy choice is baked into ML-3. Changing the loss function after the trainer is implemented is a non-trivial retrofit. Run the alignment experiment on a small task pool before committing any ML-3 code. If the default diverges, work through the fallback chain — pairwise → differentiable Spearman → LambdaRank — before building the trainer on a proxy that is known to misalign.

### Lock 5 — Curriculum & Prioritized Replay

| Field | Content |
|---|---|
| **Assumption** | Uniform sampling across regime buckets with an explicit crisis floor, followed by PER-like task replay (`alpha=0.6`, `beta` annealed `0.4→1.0`), produces better regime coverage than uniform sampling alone. |
| **Why it matters** | Crisis periods are rare. Without explicit curriculum management, the meta-learner will underweight crisis tasks, producing high mean IC but low crisis IC. Crisis IC is a hard gate. |
| **Failure risk** | PER-like sampling applied to meta-tasks has no published precedent. Priority signal (inner-loop gain as analog to TD-error) may not behave like RL PER. |
| **Experiment** | A/B: uniform curriculum vs prioritized curriculum. Track per-bucket IC over training. Monitor crisis task IC specifically. |
| **Control** | Uniform sampling with crisis floor (no priority). |
| **Threshold** | Prioritized curriculum achieves crisis bucket IC >= uniform curriculum without degrading other buckets by more than 0.01 IC. `⚑ VALIDATE`: alpha and beta schedule are RL defaults; finance-specific recalibration required. |
| **Fallback** | If PER-like sampling causes instability, fall back to uniform with hard crisis minimum (10% of each batch). Adjust priority signal if inner-loop gain is a poor proxy for task informativeness. |

**Why this lock exists.** PER applied to meta-tasks is an extrapolation from RL — there is no published precedent for inner-loop gain as a task priority signal in financial meta-learning. This matters because crisis IC failure is a hard kill criterion — if the curriculum systematically underweights crisis tasks, the most dangerous failure mode will be invisible until it is encountered live.

**How its result affects the build path.** Run the A/B curriculum experiment during ML-3 development. The result sets alpha, beta, and the crisis floor percentage that are baked into `reptile_trainer.py`. If prioritized curriculum provides no measurable gain over uniform-plus-crisis-floor, adopt the simpler policy.

### Lock 6 — Continual Learning & Forgetting

| Field | Content |
|---|---|
| **Assumption** | EWC with diagonal Fisher on a stratified anchor set, combined with crisis replay, is sufficient to prevent catastrophic forgetting on historical task types as the meta-learner is updated nightly. |
| **Why it matters** | If the meta-learner catastrophically forgets crisis regimes during benign periods, it will fail precisely when robustness is most needed. |
| **Failure risk** | EWC lambda is highly domain-sensitive. Literature shows useful lambda varies by orders of magnitude. The anchor set definition may not cover the right task types. Plasticity loss may co-occur with forgetting suppression. |
| **Experiment** | After each month of sequential updates, evaluate IC on a fixed held-out historical task set. Monitor adaptation gain (plasticity) separately on new tasks. Compare with no-EWC baseline. |
| **Control** | Joint retraining from scratch (no EWC) at each nightly cycle. |
| **Threshold** | IC degradation on held-out set < 15% `⚑ VALIDATE`. Adaptation gain on new tasks does not collapse (absolute gain remains > 0.003 IC `⚑ VALIDATE`). |
| **Fallback** | Increase `lambda_EWC`; migrate to online EWC if anchor set grows. Increase crisis replay allocation. If plasticity collapses under high lambda, split the stability/plasticity target and use complementary learning systems. |

**Why this lock exists.** EWC lambda is the most empirically unconstrained parameter in the Phase II design. Literature values span four orders of magnitude across domains; there is no finance-specific calibration for EWC in a meta-learning context. The nightly outer-loop update cadence makes catastrophic forgetting a real operational risk.

**How its result affects the build path.** This lock gates ML-5 (EWC + crisis replay) configuration. The lambda sweep results directly set the operational lambda value and the monitoring alert thresholds in Section 11.

---

# 4. Empirical De-Risking Program

*This is the validation core. It converts the six design locks into a real de-risking program organized around five workstreams. Each workstream governs one empirical claim from Section 0.3. Workstream results determine whether the architecture is promoted, revised, or killed.*

## 4.1 Workstream 1 — Baseline Superiority

| Hypothesis | Why it matters | Experiment | Control/Baseline | Metric | Pass threshold | Fallback |
|---|---|---|---|---|---|---|
| The Reptile meta-policy beats the best XGBoost + BOCPD-conditioned allocator net of TC. | If it does not, the null hypothesis stands. | Freeze the XGBoost baseline, then run matched walk-forward comparison on the same signal universe. | Best attainable XGBoost + BOCPD configuration using current infrastructure. | Net Sharpe, DSR, drawdown, turnover, crisis IC. | Positive net Sharpe uplift after TC across the full validation window. | Kill or narrow the scope to simpler regime-conditioned allocators. |

### 4.1.1 Baseline Freeze Protocol

The baseline must be frozen before meta-learning experiments begin. No changes to feature families, execution assumptions, or hyperparameter budget may be made after the meta-learning program starts unless the same changes are also applied to the baseline and the comparison is re-run.

## 4.2 Workstream 2 — Task Validity

| Hypothesis | Why it matters | Experiment | Control/Baseline | Metric | Pass threshold | Fallback |
|---|---|---|---|---|---|---|
| MetaTasks are non-exchangeable and leakage-safe. | Otherwise the curriculum is invalid and adaptation gains are contaminated. | Run Lock 1 and Lock 2 experiments on the first task pool. | Scrambled labels; scrambled regime labels. | Leakage IC, Harvey t, shuffle p-value. | Leakage collapses to near zero; Harvey t > 3.0; shuffle p < 0.05. | Rebuild task definition before ML-3. |

## 4.3 Workstream 3 — Adaptation Usefulness

| Hypothesis | Why it matters | Experiment | Control/Baseline | Metric | Pass threshold | Fallback |
|---|---|---|---|---|---|---|
| Inner-loop adaptation improves query IC rather than only fitting support sets. | Without held-out improvement, adaptation is not useful. | K sweep on held-out tasks with gain measured on query sets. | K=0 and K=1 baselines. | Mean `ΔIC`, Harvey t, gain curve saturation. | Positive mean `ΔIC`, Harvey t > 3.0, saturation <= 10 steps `⚑ VALIDATE`. | Switch adaptation scope or revisit task sizing. |

## 4.4 Workstream 4 — Proxy Alignment

| Hypothesis | Why it matters | Experiment | Control/Baseline | Metric | Pass threshold | Fallback |
|---|---|---|---|---|---|---|
| The differentiable ranking loss tracks exact Spearman IC. | If it does not, the trainer optimizes the wrong target. | Jointly track proxy loss and held-out IC across epochs. | MSE regress-then-rank. | Pearson correlation, divergence windows. | Pearson r > 0.6 `⚑ VALIDATE` with no sustained divergence. | Switch proxy chain, then fine-tune on IC. |

## 4.5 Workstream 5 — Continual-Learning Robustness

| Hypothesis | Why it matters | Experiment | Control/Baseline | Metric | Pass threshold | Fallback |
|---|---|---|---|---|---|---|
| EWC + crisis replay suppress forgetting without collapsing plasticity on new tasks. | A meta-learner that forgets crisis regimes during benign periods is dangerous. | After sequential monthly updates, evaluate IC on a fixed held-out historical task set and monitor adaptation gain on fresh tasks. | Joint retraining from scratch at each nightly cycle. | Forgetting delta, new-task gain, per-regime breakdown. | IC degradation < 15% and new-task gain > 0.003 IC `⚑ VALIDATE`. | Increase lambda, increase crisis replay, or move to periodic warm-start retraining. |

**Why this workstream exists.** EWC lambda is highly domain-sensitive and has no MarketMind-specific calibration. The plasticity/forgetting tradeoff must be measured explicitly.

**How its result affects the build path.** This workstream gates ML-5 (EWC + crisis replay). Its results also set the monitoring thresholds used in Section 11.

---

# 5. Architecture, Runtime Lifecycle, and Control Plane

*This section describes the operational architecture: three layers, parameter lifecycle, nightly training behavior, and failure handling.*

## 5.1 Three-Layer Hierarchy

| Layer | Name | Timescale | Mechanism | Output | MarketMind Component |
|---|---|---|---|---|---|
| 1 (Base) | Signal Library | Daily → Intraday | Individual strategy signals | SignalFn → Alpha IR per signal | SignalCatalog + PipelineStrategy subclasses |
| 2 (Fast) | Meta-Policy / Fast Adaptation | Daily (nightly adaptation, frozen live inference) | Reptile inner loop on current regime episode support set; context encoder produces regime embedding | `allocation_weights` + `confidence_scalar` | `meta_policy.py` + `context_encoder.py` + `reptile_trainer.py` |
| 3 (Slow) | Autonomous Alpha Factory | Nightly outer-loop; weekly/monthly evolution review | Reptile outer-loop meta-parameter update + EWC + crisis replay; Signal Factory generates/retires signals | Updated `theta_meta` + SignalCatalog changes | `reptile_trainer.py` outer loop + `continual.py` + Signal Factory (Phase IV) |

**Hard boundary.** Layers 1 and 2 are pure computation (functional core). Layer 3 has state but operates offline — not on the critical execution path.

**Post-allocator conditioning (II-D research target).** Even when Layers 1–2 exist, **allocator intent is not identical to deployable capital**. **Structured post-allocator conditioning**—turnover-aware targets, liquidity/capacity-aware sizing, drawdown and regime overlays, constrained construction—is where **frictions enter seriously**. That layer can be **economically load-bearing** near-term and still **not** satisfy the **burden to beat the simpler baseline net of costs**; conversely, allocator proof **does not** make execution realism optional. Systems trained on paper weights and only later bolted to realistic constraints are **not** the desired end state.

## 5.2 Parameter Lifecycle

### theta_meta
- **Persisted:** Nightly checkpoint; content-hashed via `artifact_registry/`.
- **Promoted:** Only after all Section 6 acceptance gates pass for the given nightly run.
- **Rolled back:** If live degradation triggers defined in Section 9.2 are met; rollback target is the last known-good checkpoint.
- **Used by:** `reptile_trainer.py` as inner-loop initialization; `meta_policy.py` at inference time via `theta_day_prime`.

### theta_day_prime
- **Persisted:** Nightly checkpoint; tagged with the task batch and date.
- **Promoted to live:** Only after gate pass on `meta_validity_report.json` for the nightly run that produced it.
- **Rolled back:** If live inference anomaly is detected within the session; fallback is the previous session's `theta_day_prime`.
- **Inference behavior:** Frozen. No gradient updates on the live path under any circumstances.

### theta_task_prime
- **Persisted:** Not persisted outside the training run. Ephemeral.
- **Used by:** Outer-loop loss computation only.
- **Failure handling:** If inner-loop diverges during training (NaN/Inf), the task is skipped and logged. Three consecutive task failures abort the nightly run.

## 5.3 Nightly Training Behavior

```text
Historical tasks from TaskRegistry
    ↓ Curriculum sampler (priority + crisis + recency weights)
    ↓ For each task Ti in batch:
        Support set → K inner gradient steps → theta_task_prime_i
        Query set IC(theta_task_prime_i, Q_i) → inner-loop gain
    ↓ Reptile outer update: theta_meta ← theta_meta + ε·mean(theta_task_prime_i − theta_meta)
    ↓ EWC penalty update (Fisher diagonal)
    ↓ Emit meta_validity_report.json
    ↓ Gate CLI validates report; promote theta_day_prime if PASS
```

**Failure handling.** If nightly training fails, live inference continues using the previous session's `theta_day_prime` without interruption. Operator alert is emitted immediately.

## 5.4 Inference Path

```text
OHLCV + alt data
    ↓ DataView.as_of(T)
    ↓ Feature ops (RSI, MACD, KF_BETA, BOCPD, ...)
    ↓ Context encoder: c_t → z ∈ R^64
    ↓ Signal library: z → K Alpha IR signals
    ↓ Meta-policy: z + IC_vec → allocation_weights ΔK
    ↓ SizingFn: allocation_weights → base positions; confidence_scalar post-sizing
    ↓ RiskFn → Orders → Fills → Ledger
```

**Intraday boundary.** Strategies under 15-minute frequency use frozen inference with pre-computed regime embeddings only.

## 5.5 Phase I Prerequisites

The following deliverables must be in place before Phase II training infrastructure is buildable.

| Deliverable | File | Why Required | Effort |
|---|---|---|---|
| MetaTask dataclass | `srcPy/meta/task.py` | Defines task schema (§2.1). All subsequent meta-learning code depends on this contract. | 2 hrs |
| TaskRegistry | `srcPy/meta/task_registry.py` | Stores historical tasks indexed by regime_id and t0. Required for curriculum and outer-loop batch sampling. | 3 hrs |
| BOCPD implementation | (orchestrator regime service — file path TBD at Phase II implementation; must not be placed inside feature graph ops) | BOCPD regime service provides canonical PIT-safe regime labels and task-boundary signals to RegimeLabeler. Service placement is governed by AQ-04 (CLOSED). Must not be implemented as a graph op in the feature execution path. | 4–6 hrs |
| Signal embedding field on Signal ABC | `srcPy/registry/signal_abc.py` | `signal_embedding: Optional[np.ndarray] = None` until context encoder is online. | 1 hr |
| Regime label pipeline | `srcPy/meta/regime_labeler.py` | Assigns `regime_class` to each historical bar from current-knowledge variables only. | 3–4 hrs |

## 5.6 Phase II Build Order

| Priority | Deliverable | File | Description | Effort |
|---|---|---|---|---|
| ML-1 | Context Encoder | `srcPy/meta/context_encoder.py` | 2-layer MLP: `c_t → z in R^64`. Pre-train as regime classifier; fine-tune jointly. | 8–12 hrs |
| ML-2 | MetaTask Generator | `srcPy/meta/task_generator.py` | Builds MetaTask objects from DataView. Enforces PIT and dynamic-K invariants. | 6–8 hrs |
| ML-3 | Reptile Trainer | `srcPy/meta/reptile_trainer.py` | Nightly outer loop with differentiable IC surrogate. Logs inner-loop gain by task and regime bucket. | 12–16 hrs |
| ML-4 | Meta-Policy Network | `srcPy/meta/meta_policy.py` | `z + IC_vec + portfolio_state → allocation_weights + confidence_scalar + regime_class`. | 8–10 hrs |
| ML-5 | EWC + Crisis Replay | `srcPy/meta/continual.py` | EWC penalty on stratified anchor set plus crisis replay buffer. | 6–8 hrs |
| ML-6 | MetaLearner Gate | `marketmind_gate/gates/meta_learner.py` | Promotion gate: all Section 6 criteria. Emits `meta_validity_report.json`. | 4–6 hrs |
| ML-7 | ChampionChallenger Reframe | `srcPy/strategies/pipeline_strategy.py` | Shadow mode, capped blend, and promotion checks for meta-policy rollout. | 3–4 hrs |

---

# 6. Evaluation Hierarchy

*Scope: This section defines canonical metrics and pass/fail gates only.*

## 6.1 Model-Level Metrics

| Metric | Purpose | Gate / Monitoring |
|---|---|---|
| Within-regime cosine similarity | Context encoder coherence | Gate: > 0.6 `⚑ VALIDATE` |
| Cross-regime cosine similarity | Encoder discriminability | Gate: < 0.3 `⚑ VALIDATE` |
| Mean inner-loop gain (`ΔIC`) | Average IC improvement on query sets after K adaptation steps | Gate: > 0.005 `⚑ VALIDATE` |
| Inner-loop gain Harvey t | Statistical significance of adaptation across the task pool | Hard gate: > 3.0 |
| Gain by regime_class | Regime coverage of adaptation signal | Gate: > 0 in all 5 buckets |
| Proxy–IC Pearson correlation | Alignment between surrogate loss and exact IC across training | Gate: > 0.6 `⚑ VALIDATE` |
| Fast adaptation speed | Convergence of gain curve vs K | Gate: saturation <= 10 steps `⚑ VALIDATE` |

## 6.2 Portfolio-Level Metrics

| Metric | Purpose | Gate / Monitoring |
|---|---|---|
| Net Sharpe (after TC) | Primary allocation quality metric | Gate: > 0.5 walk-forward `⚑ VALIDATE`; must exceed XGBoost baseline |
| Walk-forward IC | Out-of-sample signal quality across the full test window | Monitoring; compared to baseline |
| Max drawdown | Tail risk of the meta-policy allocation | Monitoring; alert if exceeds historical baseline max drawdown × 1.2 `⚑ VALIDATE` |
| Turnover | Rebalancing cost driver | Monitoring |
| Crisis episode net Sharpe | Specifically evaluated on permanently held-out crisis windows | Gate: IC > 0; Sharpe > 0 on crisis holdout |
| DSR (Deflated Sharpe Ratio) | Corrects reported Sharpe for trial count and non-normality | Gate: DSR p < 0.05 for any promoted policy |

## 6.3 Governance-Level Metrics

| Metric | Purpose | Gate / Monitoring |
|---|---|---|
| Anti-Goodhart holdout compliance | Crisis holdout task_ids must not appear in training, tuning, or calibration logs | Hard gate: zero violations |
| PIT compliance | All task support/query sets pass `DataView.as_of(pit_boundary)` leakage invariants | Hard gate |
| Determinism | Same MetaTask + same theta + same seed produces identical outputs on deterministic gate backend | Hard gate |
| Task-pool sufficiency | Minimum task count met in every curriculum bucket before nightly training is enabled | Gate: >= 50 tasks per regime_class bucket `⚑ VALIDATE` |
| Forgetting (held-out IC degradation) | IC on fixed held-out historical task set measured monthly | Gate: < 15% degradation `⚑ VALIDATE` |
| Regime coverage | Inner-loop gain > 0 in all five curriculum buckets | Gate: all buckets positive |

**All 12 acceptance criteria are binary pass/fail. No "proceed with caveats."**

> ⛔ Gate: If context encoder clustering fails, do not proceed to Reptile training.

> ⛔ Gate: If inner-loop gain Harvey t < 3.0 after full task pool construction, halt and review task definition.

> ⛔ Gate: Anti-Goodhart is a hard requirement. Promotion fails automatically if held-out crisis episodes appear in any training, tuning, or calibration log.

---

# 7. Failure Modes & Recovery Playbooks

*This section is mandatory. It covers the failure classes that the acceptance gates and monitoring infrastructure must be able to detect and respond to.*

| Failure | Detection | Likely Cause | Immediate Action | Next Diagnostic | Fallback |
|---|---|---|---|---|---|
| **Task collapse / exchangeability** | Inner-loop gain Harvey t < 3.0; near-zero `Δθ`; shuffle test p >= 0.05 | Insufficient regime_id granularity | Halt ML-3 build | Inspect regime_id distribution; review task episode lengths | Increase regime_id granularity; add meta-regularization; consider switching task family |
| **Embedding drift** | Within-regime cosine similarity degrades below threshold | Distribution shift in feature space | Alert operator; freeze meta-policy at current `theta_day_prime` | Re-run clustering test | Re-warm-up context encoder; increase capacity if needed |
| **Proxy misalignment** | Proxy training loss decreases while held-out IC stagnates or degrades | Proxy objective diverged from IC | Pause outer-loop training | Inspect proxy–IC correlation trajectory | Switch proxy; add IC fine-tuning stage |
| **Crisis overfit** | Crisis episode IC <= 0 on held-out crisis windows | Holdout leakage or crisis replay too low | Fail the gate; lock down holdout manifest | Check `task_manifest.json` for leakage | Rebuild holdout manifest; increase crisis replay allocation |
| **Dynamic-K instability** | `allocation_weights` oscillate across sessions | K too large relative to support set size | Reduce K by one step | Inspect BOCPD output stability | Reduce K; smooth BOCPD; add post-sizing smoothing |
| **Nightly training failure** | `meta_validity_report.json` not emitted within training window | NaN/Inf in gradients; data pipeline failure | Continue on previous `theta_day_prime`; alert immediately | Inspect logs for first NaN | Retry nightly run with previous checkpoint |
| **Sparse task buckets** | Task-pool sufficiency gate fails | Insufficient historical data in rare regimes | Do not enable nightly training | Count tasks per bucket | Expand historical window; reduce model capacity |
| **Leakage violation** | Leakage CI battery fails; scrambled-label tasks show IC > threshold | Embargo too short or pit boundary wrong | Halt all training immediately | Inspect `task_generator.py` pit boundary logic | Increase embargo; rebuild affected tasks |

---

# 8. Migration & Deployment Framework

*Scope: This section defines stage transitions only. It consumes Section 6 gates and Section 9 decisions.*

## 8.1 Migration Stages

### Stage 1 — Shadow Mode

**Entry criteria.** All ML-1 through ML-6 deliverables complete. All Section 6 acceptance criteria pass. `meta_validity_report.json` clean.

**Behavior.** Meta-policy runs in parallel with existing EnsemblePipelineStrategy. Its `allocation_weights` are logged but do not influence live orders.

**Monitoring criteria.**
- Inner-loop gain logged per session.
- `allocation_weights` variance monitored.
- IC of shadow meta-policy vs live EnsemblePipelineStrategy computed daily.

**Exit criteria.** Shadow meta-policy IC >= EnsemblePipelineStrategy IC on >= 15 consecutive trading days `⚑ VALIDATE`. No anomalies in `allocation_weights`. Operator sign-off.

### Stage 2 — Capped Blend

**Entry criteria.** Stage 1 exit criteria met.

**Behavior.** Live orders are a blend: `(1 − α) × EnsemblePipelineStrategy + α × meta_policy`, with alpha capped at 0.3 `⚑ VALIDATE` initially. Exposure sanity checks are enforced each session.

**Capital and exposure guardrails (Stage 2).**
- Maximum live capital share influenced by the meta-policy leg: <= alpha × total capital.
- Maximum gross exposure deviation vs EnsemblePipelineStrategy: `⚑ VALIDATE` (recommended starting point: ±10% of incumbent gross exposure).
- Maximum sector/factor exposure drift vs incumbent: `⚑ VALIDATE`.
- Maximum turnover deviation: if blend turnover exceeds 1.5× baseline `⚑ VALIDATE`, alpha is reduced by 0.1 automatically.

**Monitoring criteria.**
- Daily net Sharpe comparison: meta-policy blend vs EnsemblePipelineStrategy alone.
- Turnover impact monitoring.
- Divergence threshold: if daily IC diverges by > 0.05 from shadow baseline, reduce alpha by 0.1 `⚑ VALIDATE`.
- Auto-demotion trigger: if 5-day rolling IC drops > 20% below EnsemblePipelineStrategy, revert to Stage 1 immediately `⚑ VALIDATE`.

**Crisis override behavior.** If BOCPD signals a regime change, freeze alpha at current level for 48 hours.

**Exit criteria.** Blend at alpha = 0.3 maintains IC >= EnsemblePipelineStrategy for >= 30 trading days `⚑ VALIDATE` with turnover within tolerance. Operator sign-off.

### Stage 3 — Full Promotion

**Entry criteria.** Stage 2 exit criteria met. All Section 9.1 promotion requirements satisfied.

**Behavior.** Meta-policy is the live allocator. EnsemblePipelineStrategy is retained as fallback but receives no live orders.

**Rollback trigger.** Any Section 9.2 condition triggers automatic reversion to EnsemblePipelineStrategy and entry to Stage 1 shadow monitoring.

## 8.2 ChampionChallenger Reframe (ML-7)

`ChampionChallenger` is reframed as the evaluation harness for migration:
- `ChampionChallenger.evaluate()` wraps the inner-loop adaptation step for the challenger.
- `ChampionChallenger.step()` manages shadow vs blend vs promotion state transitions.
- Champion is always the current live policy.
- Challenger must beat champion on net Sharpe and IC over a pre-specified evaluation window before any alpha increase.

---

# 9. Promotion, Rollback, and Kill Framework

*Scope: This section defines executive consequences only — promotion, rollback, or kill.*

## 9.1 Promotion — Requirements

Promotion to full live deployment (Stage 3) requires all of the following:

- All 12 acceptance criteria in Section 6 pass.
- No open data-governance, PIT, or reproducibility exceptions.
- `meta_validity_report.json` emitted and verified by gate CLI for the promoting nightly run.
- Meta-policy net Sharpe > XGBoost baseline net of TC over the full walk-forward validation window.
- Stage 2 capped-blend exit criteria met.
- Operator sign-off recorded in the release manifest.

## 9.2 Rollback — Triggers

**Automatic rollback triggers.**
- Live IC degradation > 20% sustained over 10 consecutive trading days `⚑ VALIDATE`.
- Dynamic-K instability: `allocation_weights` variance exceeds trained-period baseline by > 2× for 5+ sessions `⚑ VALIDATE`.
- Confidence collapse: `confidence_scalar < 0.1` sustained for 3+ sessions `⚑ VALIDATE`.
- Any reproducibility or data-integrity incident.
- Nightly training failure for 3 consecutive nights.

**Operator-initiated rollback triggers.**
- Exposure anomaly not explained by model behavior.
- Regulatory or compliance review requiring live system freeze.
- Any unresolved item in Section 7 failure playbooks that has not been diagnosed and cleared.

**Rollback target.** Always the most recent `theta_day_prime` that passed a clean gate run. Rollback to EnsemblePipelineStrategy is the outer fallback if no clean checkpoint exists within the prior 5 nightly runs.

## 9.3 Kill — Criteria

*Kill means the meta-learning architecture as specified is abandoned. It is not a rollback; it is a conclusion.*

The architecture is killed if any of the following are confirmed after completing the full validation program:

- **Inner-loop gain Harvey t < 3.0** on the full task pool after task pool construction is complete.
- **No net Sharpe uplift over the XGBoost baseline** after transaction costs across the full walk-forward validation window.
- **Proxy–IC alignment correlation < 0.6** and cannot be stabilized after proxy switching and fine-tuning.
- **Context encoder clustering fails** and cannot be repaired by capacity increase, extended pre-training, or regime label refinement.
- **Operational complexity burden exceeds measured benefit.**

**What kill does not mean.** Kill of the full Reptile architecture does not preclude narrower uses of meta-learning concepts, such as using the context encoder for regime classification only.

### 9.3.1 Operational Burden Scorecard

| Burden metric | Measurement | Threshold (`⚑ VALIDATE`) |
|---|---|---|
| Nightly training failure rate | Failures / 30 nights | > 10% |
| Operator interventions | Manual interventions / 30 days | > 5 |
| Rollback frequency | Rollbacks / 30 days | > 2 |
| Training wall-clock breach | Sessions exceeding budget / 30 nights | > 15% |
| Unresolved alerts per week | Mean open alerts at week end | > 3 |
| Dynamic-K incidents | Instability events / 30 days | > 3 |
| Extra compute burden | Nightly training cost vs EnsemblePipelineStrategy | > 5× |
| Realized net uplift | Meta-policy net Sharpe − baseline net Sharpe | < minimum uplift bar |

**Decision rule.** Kill for operational burden if, over a full validation window, the meta-policy produces less than the minimum required net Sharpe uplift over the XGBoost baseline **and** breaches two or more burden thresholds above.

---

# 10. Data Governance & Task Sufficiency

*This section extends the PIT governance contracts from the main codebase into a policy for meta-learning–specific data handling.*

## 10.1 PIT Enforcement for Meta-Learning

All task construction must enforce the following invariants:

- Task support sets are constructed using `DataView.as_of(pit_boundary)`.
- Regime embeddings z must not incorporate any data beyond `pit_boundary`.
- The regime label for a task must be derived from information available at `pit_boundary` only.
- No feature or label may be forward-filled beyond `pit_boundary`.

## 10.2 Minimum Task Counts per Bucket

Nightly outer-loop training is not enabled until the task pool meets the following minimum counts per `regime_class` bucket:

| Regime class | Minimum tasks | Policy if below minimum |
|---|---|---|
| bull | 50 `⚑ VALIDATE` | Expand historical window or assets |
| bear | 50 `⚑ VALIDATE` | Expand historical window or assets |
| sideways | 50 `⚑ VALIDATE` | Expand historical window or reduce episode minimum length |
| high_vol | 30 `⚑ VALIDATE` | Accept lower minimum; note in `meta_validity_report.json` |
| crisis | 20 `⚑ VALIDATE` | Accept lower minimum; enforce crisis floor in curriculum; do not reduce further |

## 10.3 Crisis Sparsity Policy

Crisis periods are rare. The following policies govern crisis task handling:

- A crisis floor of >= 10% of each meta-batch must be allocated to crisis tasks regardless of curriculum priority.
- The crisis episode pool must include known stress windows plus any BOCPD-flagged crises accrued since deployment.
- The Anti-Goodhart holdout set is a permanently locked subset of crisis episodes, excluded from training, tuning, and curriculum-priority calibration.
- If the crisis bucket falls below minimum count, do not reduce the crisis floor.

## 10.4 Dataset Versioning & Regime Label Provenance

Every task pool must record:

- Dataset version and source manifest lineage
- Regime labeler version
- Signal-set version
- Task construction config hash
- Holdout manifest hash

These identifiers must be emitted in `task_manifest.json` and linked from the nightly report.

---

# 11. Observability and Operator Controls

## 11.1 Monitoring Dashboards

| Metric | Purpose | Alert Condition |
|---|---|---|
| Inner-loop gain by regime_class | Adaptation health by bucket | Alert if any bucket drops to <= 0 for 3+ consecutive runs |
| Context encoder clustering score | Encoder health | Alert if within-regime cosine similarity < 0.55 `⚑ VALIDATE` |
| Forgetting metric | Continual learning health | Alert if IC degradation on held-out set exceeds 10% `⚑ VALIDATE` |
| Task-pool coverage by bucket | Curriculum sufficiency | Alert if any bucket falls below minimum count |
| Confidence scalar — mean | Exposure health | Alert if mean confidence_scalar < 0.2 for 3+ sessions `⚑ VALIDATE` |
| Confidence scalar — calibration error (ECE) | Calibration health | Alert if ECE exceeds threshold `⚑ VALIDATE` |
| Confidence scalar — realized-quality correlation | Reliability signal validity | Alert if rolling correlation drops below floor `⚑ VALIDATE` |
| Nightly training wall-clock | Compute health | Alert if training time exceeds 2× rolling 30-day average `⚑ VALIDATE` |
| `meta_validity_report.json` overall_result | Gate health | Alert immediately on any FAIL |

## 11.2 Operator Controls

| Control | Effect | Requires |
|---|---|---|
| Pause nightly training | Stops outer-loop updates; live inference continues on last `theta_day_prime` | Operator flag in config |
| Rollback `theta_day_prime` | Reverts live inference to specified checkpoint | Checkpoint hash in config |
| Freeze SignalCatalog | Prevents new signals from being added to the meta-learner's task library | Operator flag |
| Override allocation weights | Applies operator-specified allocation weights for one session | Signed override manifest |
| Force shadow mode | Drops meta-policy from live orders; reverts to EnsemblePipelineStrategy | Operator flag |
| Lock crisis holdout manifest | Prevents any modification to the Anti-Goodhart holdout set | Signed manifest; executive sign-off to unlock |

---

# 12. Companion Document Updates

*This section governs updates required in companion documents as a result of this v2.0.0 revision. These are precise, non-destructive additions.*

## 12.1 Technical Roadmap — Required Additions

| Section | Current State | Required Addition |
|---|---|---|
| §1.2 Strategies & Signal Generation | Meta-Learning Core: architecture designed; Phase II centerpiece | Add row: empirical de-risking program, failure playbooks, and kill framework are part of Meta-Learning Core v2.0.0. Status remains pre-validation. |
| §2.4 ML Architecture & Training | Research topics: MAML/Reptile reference | Expand to a full research block referencing Core §3 and §4. Include empirical de-risking program and Workstreams 1–5 as tracked research items. |
| §3.3 Medium-Term P7 | Meta-learner training is Phase II | Add: kill criteria from §9.3 must be documented as go/no-go checkpoints in Phase II delivery. |
| §9 Key References | Finn (2017) listed | Add: Nichol et al. (2018) Reptile; Kirkpatrick et al. (2017) EWC; Raghu et al. (2020) ANIL; Vilalta & Drissi (2002); Schaul et al. (2016) PER. |

## 12.2 Implementation Plan — Required Additions

| Section | Current State | Required Addition |
|---|---|---|
| Phase II success criteria | Acceptance table from earlier Core revision | Replace with the 12-criterion table from §6. Add `meta_validity_report.json` schema v1. |
| Phase II goals | Meta-learner as centerpiece | Add: empirical de-risking program (§4 Workstreams 1–5) is a Phase II deliverable, not a pre-Phase-II activity. Workstream results gate ML-3 onward. |
| Appendices | Run-bundle documentation focuses on existing artifacts | Add: `meta_validity_report.json` and `task_manifest.json`. |
| Phase I prerequisites | No explicit meta-learning prerequisite table | Add the 5-row prerequisite table from §5.5. |

## 12.3 README — Required Additions

| Section | Current State | Required Addition |
|---|---|---|
| Overview / what's planned | North star plus meta-learning centerpiece | Expand: Core v2.0.0 adds empirical de-risking, failure playbooks, and promotion/kill framework. Architecture is proposed pending validation. |
| Plugin / allocator language | PortfolioAllocator described as multi-strategy combination | Add note: in Phase II+, PortfolioAllocator is the meta-policy network. `allocation_weights` replace static portfolio weights. `confidence_scalar` is post-sizing only. |

## 12.4 White Paper — Required Additions

| Section | Current State | Required Addition |
|---|---|---|
| Abstract and executive framing | Meta-learning described as a committed future architecture | Reframe as a governed hypothesis under validation, with the null hypothesis and proof burden stated in plain language. |
| Roadmap / results language | Phase II reads like unconditional delivery | Emphasize evidence gates, baseline comparisons, and failure modes before promotion claims. |

---

<!-- MM:BEGIN:RECENT_CHANGES key="MetaLearningCore" window=3 -->

| Release | Date | Meta-Learning Core impact |
|---|---|---|
| 1.2.19 | April 2026 | Companion stamp sync: DOCMAP and SOURCE_STAMP aligned to **VERSION.md 4.18.5**, Implementation Plan **6.4.26**, Resolution Ledger **1.0.21**; no Core semantics change. |
| 1.2.18 | March 2026 | Companion stamp sync: DOCMAP and SOURCE_STAMP aligned to **VERSION.md 4.18.0**, Implementation Plan **6.4.23**, Resolution Ledger **1.0.19**; no Core semantics change. |
| 1.2.17 | March 2026 | Companion stamp sync: DOCMAP and SOURCE_STAMP aligned to **VERSION.md 4.17.0**, Implementation Plan **6.4.22**, Resolution Ledger **1.0.18**; no Core semantics change. |
| 1.2.16 | March 2026 | Companion stamp sync: DOCMAP and SOURCE_STAMP aligned to **VERSION.md 4.16.0**, Implementation Plan **6.4.21**, Resolution Ledger **1.0.17**; no Core semantics change. |
| 1.2.15 | March 2026 | March 2026 synthesis: §0.6 evidence stack; stronger incumbent baseline / net-of-cost / fail-gracefully language; §2.5.2 routing pilot vs attenuation default; post-allocator conditioning note in §5.1; task-first architectural claim refinement. |
| 1.2.13 | March 2026 | F-1/F-2 planning baseline carried forward; this edition clarifies that I-G and II-0 may host empirical pilots and harness work, while final Phase II promotion logic still governs trainer commitment, promotion, rollback, and kill. |
| 2.0.0 | March 2026 | Major revision: added Decision Framing, the empirical de-risking program, failure modes and recovery playbooks, the promotion/rollback/kill framework, observability, and threshold-resolution registry. Rebased the document on validation-gated architecture rather than presumed Phase II commitment, and refreshed current-state references through VERSION.md 4.5.4. |
| 1.2.11 | March 2026 | Prior companion-edition framing: task schema, inner/outer loop mechanics, and Phase II build guidance aligned to the 4.5.2 suite. |
| 1.0.0 | March 2026 | Initial release: task schema, inner/outer loop mechanics, six design locks, acceptance criteria, and companion document upgrade spec. |

<!-- MM:END:RECENT_CHANGES -->

<!-- MM:BEGIN:SOURCE_STAMP -->

*Source: This document v1.2.19 · April 2026 · Companion to Implementation Plan v6.4.32 · Technical Roadmap v1.4.21 · Meta-Learning Architecture Vision v1.2.20 · Resolution Ledger v1.0.40 · README.md 4.18.12 · VERSION.md 4.18.28*

<!-- MM:END:SOURCE_STAMP -->

---

# Appendix A — Threshold Resolution Table

*Each `⚑ VALIDATE` placeholder in this document is assigned a resolution milestone, an evidence source, and a responsible owner.*

## A.1 Resolution Tiers

| Tier | Resolve by | Rationale |
|---|---|---|
| **Tier 1** | Before ML-3 build | These thresholds govern the training infrastructure itself. |
| **Tier 2** | Before Stage 1 shadow | These thresholds govern gate pass/fail for promotion to live shadow. |
| **Tier 3** | Before Stage 2 blend | These thresholds govern live capital exposure. |

## A.2 Threshold Resolution Registry

| Threshold name | Current placeholder | Section | Why unresolved | Evidence source needed | Tier | Status |
|---|---|---|---|---|---|---|
| `inner_loop_gain_mean` | > 0.005 IC | §6.1, §4.3 | No finance-specific meta-learning precedent | K-sweep experiment on MarketMind task pool | 1 | Open |
| `proxy_IC_pearson_r` | > 0.6 | §6.1, §4.4 | Correlation floor is literature-approximate | Proxy alignment experiment on MarketMind data | 1 | Open |
| `within_regime_cosine` | > 0.6 | §6.1 | No finance precedent | Context encoder clustering test on regime-labeled task pool | 1 | Open |
| `cross_regime_cosine` | < 0.3 | §6.1 | Same | Same | 1 | Open |
| `adaptation_K_max` | <= 10 steps | §6.1, Lock 3 | Latency budget not yet measured | Wall-clock sweep on MarketMind hardware | 1 | Open |
| `forgetting_IC_floor` | < 15% degradation | §6.3, §11.1, Lock 6 | EWC calibration unresolved | Sequential monthly update experiment | 1 | Open |
| `plasticity_gain_floor` | > 0.003 IC | §4.5, Lock 6 | No published baseline | Same as forgetting experiment | 1 | Open |
| `min_task_count_bull` | 50 | §10.2 | Regime frequency not yet measured | Compute regime episode counts from full historical data | 1 | Open |
| `min_task_count_bear` | 50 | §10.2 | Same | Same | 1 | Open |
| `min_task_count_sideways` | 50 | §10.2 | Same | Same | 1 | Open |
| `min_task_count_high_vol` | 30 | §10.2 | Same | Same | 1 | Open |
| `min_task_count_crisis` | 20 | §10.2 | Crisis periods are rare | Same | 1 | Open |
| `shadow_exit_days` | >= 15 consecutive days | §8.1 | No backtested shadow-mode precedent | Shadow-mode simulation on walk-forward data | 2 | Open |
| `stage2_exit_days` | >= 30 consecutive days | §8.1 | Same | Same | 2 | Open |
| `net_sharpe_gate` | > 0.5 walk-forward | §6.2 | Minimum bar not grounded in MarketMind baseline | Baseline Workstream 1 results | 2 | Open |
| `confidence_ECE_threshold` | Unset | §2.5.1, §11.1 | No calibration experiment yet | Held-out calibration set fit | 2 | Open |
| `confidence_quality_corr_floor` | Unset | §11.1 | No realized-quality label defined yet | Define training target and measure on held-out data | 2 | Open |
| `blend_alpha_cap` | 0.3 | §8.1 | Initial cap is conservative | Stage 1 shadow-mode IC correlation with incumbent | 3 | Open |
| `turnover_alert_multiplier` | 1.5× baseline | §8.1 | Baseline turnover not yet measured | Measure incumbent turnover in shadow period | 3 | Open |
| `IC_divergence_alpha_reduction` | > 0.05 daily IC gap | §8.1 | Threshold is heuristic | Shadow-mode IC variance distribution | 3 | Open |
| `live_IC_demotion_trigger` | > 20% drop over 5 days | §8.1, §9.2 | Needs joint calibration with risk committee | Stage 1 IC variance | 3 | Open |
| `gross_exposure_deviation_cap` | `⚑ VALIDATE` | §8.1 | Requires risk-committee sign-off | Risk committee; exposure policy | 3 | Open |
| `sector_factor_drift_limit` | `⚑ VALIDATE` | §8.1 | Same | Same | 3 | Open |
| `operational_burden_thresholds` | Multiple | §9.3.1 | Operational history does not exist pre-deployment | 30-day shadow-mode operational log | 3 | Open |
| `compute_burden_cap` | > 5× EnsemblePipelineStrategy | §9.3.1 | Actual cost depends on hardware and task pool size | Profile nightly training on target hardware | 2 | Open |

## A.3 Resolution Rules

- A Tier 1 threshold that is not resolved before ML-3 implementation begins is a process violation.
- A Tier 2 threshold that is not resolved before Stage 1 entry is a gate failure.
- A Tier 3 threshold that is not resolved before Stage 2 entry is a hard stop.
- When a threshold is resolved, update this table, update the relevant section in-line, and remove the `⚑ VALIDATE` flag from that section.

---

# References

**Meta-Learning Algorithms**

Finn, Chelsea, Abbeel, Pieter & Levine, Sergey (2017). "Model-Agnostic Meta-Learning for Fast Adaptation of Deep Networks." ICML.

Nichol, Alex, Achiam, Joshua & Schulman, John (2018). "On First-Order Meta-Learning Algorithms." arXiv:1803.02999.

Finn, Chelsea et al. (2019). "Online Meta-Learning." ICML.

Antoniou, Antreas, Edwards, Harrison & Storkey, Amos (2019). "How to Train Your MAML." ICLR.

Raghu, Aniruddh, Raghu, Maithra, Bengio, Samy & Vinyals, Oriol (2020). "Rapid Learning or Feature Reuse? Towards Understanding the Effectiveness of MAML." ICLR.

Rajeswaran, Aravind et al. (2019). "Meta-Learning with Implicit Gradients." NeurIPS.

Snell, Jake, Swersky, Kevin & Zemel, Richard (2017). "Prototypical Networks for Few-Shot Learning." NeurIPS.

Yin, Mingzhang et al. (2020). "Meta-Learning without Memorization." ICLR.

Genewein, Tim et al. (2023). "Memory-Based Meta-Learning on Non-Stationary Distributions." ICML.

Vilalta, Ricardo & Drissi, Youssef (2002). "A Perspective View and Survey of Meta-Learning." Artificial Intelligence Review 18(2), 77-95.

**Continual Learning & Catastrophic Forgetting**

Kirkpatrick, James, Pascanu, Razvan, Rabinowitz, Neil et al. (2017). "Overcoming Catastrophic Forgetting in Neural Networks." PNAS 114(13), 3521-3526.

Huszar, Ferenc (2018). "Note on the Quadratic Penalties in Elastic Weight Consolidation." PNAS.

Schwarz, Jonathan et al. (2018). "Progress & Compress: A Scalable Framework for Continual Learning." ICML.

Javed, Khurram & White, Martha (2019). "Meta-Learning Representations for Continual Learning." NeurIPS.

Lopez-Paz, David & Ranzato, Marc'Aurelio (2017). "Gradient Episodic Memory for Continual Learning." NeurIPS.

**Curriculum Learning & Task Sampling**

Schaul, Tom, Quan, John, Antonoglou, Ioannis & Silver, David (2016). "Prioritized Experience Replay." ICLR.

Bengio, Yoshua, Louradour, Jerome, Collobert, Ronan & Weston, Jason (2009). "Curriculum Learning." ICML.

Yao, Huaxiu et al. (2021). "Meta-learning with an Adaptive Task Scheduler." NeurIPS.

Wang, Jin et al. (2024). "Towards Task Sampler Learning for Meta-Learning." IJCV 132, 5534-5564.

**Regime Detection & Change-Point Models**

Adams, Ryan P. & MacKay, David J.C. (2007). "Bayesian Online Changepoint Detection." arXiv:0710.3742.

Hamilton, James D. (1989). "A New Approach to the Economic Analysis of Nonstationary Time Series." Econometrica 57(2), 357-384.

Ang, Andrew & Bekaert, Geert (2002). "International Asset Allocation with Regime Shifts." Review of Financial Studies 15(4), 1137-1187.

**Context Encoding & Neural Processes**

Mishra, Nikhil, Rohaninejad, Mostafa, Chen, Xi & Abbeel, Pieter (2018). "A Simple Neural Attentive Meta-Learner (SNAIL)." ICLR.

Garnelo, Marta, Rosenbaum, Dan, Maddison, Chris et al. (2018). "Neural Processes." ICML Workshop.

**Differentiable Ranking & Learning to Rank**

Blondel, Mathieu et al. (2020). "Fast Differentiable Sorting and Ranking." ICML.

<!-- MM:END:DOCBODY -->
