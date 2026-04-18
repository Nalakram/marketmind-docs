**WHITE PAPER**

**MarketMind**

Meta-Learning Enabled Computational Trading System

*Adaptive Alpha Generation, Robust Risk Control,*

*and Governed Decision-Making Under Regime Shift*

**Positioning:** A governed research and allocation platform for regime-adaptive signal combination, with promotion contingent on outperformance versus simpler alternatives.

<!-- MM:BEGIN:TITLEPAGE -->
Companion documents: Implementation Plan · Technical Roadmap · Meta-Learning Core · Meta-Learning Architecture Vision · Resolution Ledger · README.md
<!-- MM:END:TITLEPAGE -->

**Distribution:** Confidential

**Legal / Risk Notice:**

*This document is for informational purposes only and does not constitute investment advice, an offer, or solicitation. Trading involves substantial risk, including loss of principal. Any architecture, workflow, or promotion path described here remains subject to validation and governance gates. Additional governance and risk documents are informational only and do not modify the LICENSE.*

<!-- MM:BEGIN:DOCBODY -->

# Abstract

MarketMind is a validation-first algorithmic trading research platform built to confront the central challenge of financial markets: non-stationarity. Signals decay, correlation structures break, execution conditions shift, and strategies that appear strong in one regime often degrade when the regime changes that matter most. MarketMind’s current strength is not that it already possesses a validated adaptive allocator. Its strength is the **governed substrate**: point-in-time data handling, leakage-aware backtesting, deterministic artifact lineage, statistical and lineage gatekeeping, and a canonical bundle workflow that makes research claims auditable—together with **survivability machinery** (rollback, staged promotion, auditability) that functions as **insurance**, not a guarantee of alpha. **Near-term practical value may depend as much on deployment discipline and structured post-allocator conditioning as on unproven allocator sophistication**; those layers do not substitute for honest baseline comparison, but they are part of a serious capital-allocation story. On top of the substrate, MarketMind proposes a meta-learning allocator that would learn to recombine signals across **market tasks** (regime-, friction-, and state-bounded episodes), not merely fit timestamped returns. The economic hypothesis is **task-dependent** signal efficacy and **reusable adaptation** across episodes. The platform still operates on a **narrow governed signal base**. **Written policies for how that base may widen and how non-standard data may become evaluation-eligible are published. The governed momentum comparison lane is closed through artifact-driven child-owned CPCV evaluation. Crisis semantics are aligned to a PIT-safe volatility-severity projection, replay-fixture and bounded II-0A harness work are landed, and paper-trading simulation requirements are closed. Later governed evidence added the unsuccessful H4 market-class rescue attempt and the proper H2 cross-sectional predecessor surface, then recorded the strict H3 successor surface at `runs/rg09_h3_granularity` as `PASS` with `trainer_commitment_unlocked = true` under the tested H3 neighborhood. The suite treats that result as an H3 successor surface evaluated through the base harness, not as proof that the original H1 surface passed. A nearby p85 sensitivity control failed with `FAIL_EXCHANGEABLE_TASKS` after collapsing `high_vol` into `crisis`. The narrow supported lesson is that stricter crisis labeling appears decisive within the tested H3 neighborhood.** Breadth at scale remains conditional future scope under strict governance. The meta-allocator is **not** presented as proven. It is a **governed hypothesis** that must beat the **simpler regime-conditioned baseline net of costs and burden**, demonstrate inner-loop adaptation where tasks justify it, preserve robustness under continual updates where promoted, and respect crisis holdouts. **Uncertainty-aware routing** is a **pilot** idea layered on **`confidence_scalar` attenuation**, not assumed default behavior. The platform combines rigorous infrastructure now with a validation-gated path toward adaptive allocation **only if** evidence—and frictions-aware evaluation—justify it.

# 1. Executive Summary

## 1.1 What Exists Today

MarketMind today is best understood as a governed research substrate with auditable strategy artifacts, point-in-time discipline, and promotion gates—not yet as a validated adaptive allocator. It already provides:

- point-in-time discipline on the canonical path,
- governed bundles and reconstructible artifact lineage,
- leakage-aware split and property-test discipline,
- statistical-validity and execution-assumptions enforcement on governed strategy slices,
- and a documented progression from strategy research to auditable artifacts.
- companion **protocol and policy** documents (including `MLN-02-AMD-01` / `rg09_gate_spec.md` `RG09-V12` for regime crisis labeling, the emitted RG-09 replay fixture required for II-0A entry, and the bounded II-0A harness/gate artifacts) for allocator–risk boundaries, signal admission and identity, encoder upgrade criteria, signal-universe expansion, alternative-data admissibility, and artifact-driven governed momentum comparison closure—these are **governance texts**, not claims of additional runtime systems or data feeds.

That substrate is the present product reality. It exists to ensure the system tells the truth about what works, what is still missing, and what has not yet earned promotion.

## 1.2 What Is Being Proposed

The proposal is framed as building a **governed** system that **adapts safely across changing market tasks**, not as installing a “smarter return predictor” by default. Return forecasting remains secondary to **task-aware allocation** under frictions and governance. The test is whether market structure supports **reusable adaptation** at the task level better than static blends or a **simpler regime-conditioned baseline**—**net of costs**, complexity, and operational burden.

The proposed next step is a meta-policy allocator that learns across regime-indexed tasks rather than merely reweighting strategies by recent performance. In that design:

- the primary learning unit is a regime-bounded episode represented as a `MetaTask`,
- task identity is expressed through `regime_id` and summarized through a 5-class `regime_class` projection,
- the meta-learner adapts from `theta_meta` to task-specific states,
- live inference uses frozen `theta_day_prime`,
- and the allocator emits `allocation_weights` plus a post-sizing `confidence_scalar` (**attenuation by default**; **uncertainty-aware routing** remains a **Phase II-0 pilot**, not assumed architecture).

**Structured post-allocator conditioning**—turnover, liquidity/capacity, and drawdown-aware capital construction—is part of the **II-D / conditional III** story for realistic deployment; it can matter greatly **without** proving meta-learning superiority. **Differentiable** portfolio construction is optional sophistication, not the core moat claim.

This is a meaningful architectural shift. It is therefore treated as something that must be proven rather than simply implemented. The claim is not “meta-learning is superior by design,” but “meta-learning may deserve testing when tasks are valid, frictions-aware evaluation is honest, and the **incumbent baseline** is beaten where it counts.”

## 1.3 Burden of Proof

The proposed architecture must show:

1. tasks are meaningfully non-exchangeable,
2. adaptation helps on held-out query data,
3. the context encoder produces coherent regime embeddings,
4. the training proxy tracks exact IC closely enough to trust promotion decisions,
5. continual updates preserve robustness rather than induce forgetting.

For avoidance of ambiguity, each criterion will be governed by predeclared thresholds covering effect size, statistical significance, turnover bounds, crisis holdout behavior, and minimum net improvement versus the incumbent baseline. Placeholder thresholds belong in this document even if they are revised later by governed protocol.

| Threshold category | Governs |
|---|---|
| Minimum net performance delta vs baseline | Whether added complexity is justified |
| Minimum adaptation gain on held-out query segments | Inner-loop and transfer claims |
| Maximum acceptable turnover increase | Cost and operability |
| Maximum drawdown degradation allowed | Risk versus simpler allocator |
| Minimum crisis-holdout retention ratio | Anti-Goodhart robustness |

## 1.4 Null Hypothesis and Consequence

The null hypothesis is straightforward: a simpler regime-conditioned XGBoost allocator matches or exceeds the proposed meta-learning system once cost, robustness, and operational complexity are included. The null should also be interpreted against a broader family of lower-complexity alternatives, including strong ensemble weighting, online allocation, and conventional regime-conditioned risk allocation, not only a single XGBoost implementation. If the evidence fails to falsify that null, MarketMind should not promote the meta-learning architecture merely because it is intellectually attractive.

# 2. Problem Statement

## 2.1 Market Non-Stationarity

Financial markets evolve continuously. Return distributions shift, volatility states cluster and then break, cross-asset relationships tighten and unwind, and tail events do not arrive on a schedule convenient for models. Systems that treat yesterday’s structure as durable truth often look impressive until the regime changes that matter most. The central allocation problem is not only forecasting returns, but determining which signals deserve capital under changing state-dependent reliability.

## 2.2 Typical Failure Modes

Several recurring failure modes dominate trading-system disappointment:

- **Static allocation fragility.** A blend of signals that works in one regime degrades when the underlying distribution shifts.
- **Research optimism without governance.** A more complex model is declared “better” before it has beaten realistic baselines under holdout, cost, and reproducibility constraints.
- **Leakage and multiple-testing error.** Overlapping labels, improper splits, or broad search over variants can manufacture false confidence.
- **Execution denial.** Backtests ignore realistic cost, turnover, or liquidity assumptions and therefore promote paper alphas that will not survive contact with markets.
- **Catastrophic forgetting.** Continual updates can erase precisely the rare-regime behavior that matters most.
- **Capacity illusion.** A signal mix that appears strong at small notional size may degrade materially under realistic liquidity, participation, and crowding constraints.

MarketMind is designed to address the second failure mode first so that any answer to the first can be trusted.

## 2.3 Design Goals

The platform’s design goals are therefore less about “winning a leaderboard” and more about creating a safe path to trustworthy adaptation:

- maintain research-time point-in-time correctness,
- report results net of realistic constraints,
- preserve artifact reproducibility and lineage,
- hold out crisis periods as genuine Anti-Goodhart evidence,
- and permit promotion only when a candidate allocator survives baseline comparison, empirical validation, and operational review.
- articulate and test a concrete economic hypothesis for why state-aware signal recombination should create durable incremental value.

## 2.4 Economic Hypothesis and Alpha Sources

The platform’s economic thesis is that categories of signal opportunity—trend, mean-reversion, quality, defensive cross-sectional factors, and others—do not share a single stable efficacy profile across market states. When volatility structure, dispersion, correlation concentration, or liquidity stress shift, the relative value of those sleeves changes. The white paper therefore treats “alpha” not as a single static factor but as state-dependent signal efficacy that may be recombined under governance. That hypothesis is what the validation program is designed to test against simpler allocators and strong baselines.

# 3. Current Platform

## 3.1 Governed Research Substrate

At the current companion baseline, MarketMind’s governed substrate includes the earlier OI-39 closeout and II-0 empirical scaffold work, the unsuccessful H4 market-class rescue attempt, the proper H2 cross-sectional predecessor surface, and the later strict H3 successor surface at `runs/rg09_h3_granularity`, recorded as `PASS` with `trainer_commitment_unlocked = true`. The harness still emits the base-field hypothesis identity `RG09-H1`, so the suite records this as an H3 successor surface evaluated through the base harness rather than as proof that the original H1 surface passed. **Corrected-surface OI-59** is a separate constructibility-only lane (historically `HOLD_PENDING_THRESHOLD_REVIEW`; inherited `THR-RG09-V20` superseded by active corrected-lane threshold `THR-RG09-V21` under MLN-07 disposition; see `docs/rg09/oi59_mln07_threshold_decision_memo.md` and Threshold Governance Register §10). MarketMind has:

- canonical orchestration and governed bundle emission,
- PIT-safe source and feature-path seams on the trusted path,
- canonical artifact storage and reconstructible bundle contracts,
- governed statistical-validity and execution-assumptions artifacts,
- materially advanced signal-identity and strategy-governance substrate,
- Phase I-G **policy** closure on paper for signal-universe expansion and alt-data admissibility plus artifact-driven MOM-020 comparison closure on the governed lane, with **Architecture Vision §4.2** / RG-09 assumption-register alignment for severity-gated `crisis`, replay-fixture closure, and bounded II-0A harness implementation: evaluation and promotion rules are written, and comparison authority is pushed into child artifacts; **no** live alt-data stack or signal-factory breadth program is asserted,
- and a documentation process designed to keep implementation truth aligned with companion claims.

This does not mean the platform already has a validated meta-learning allocator. It means the platform has enough governed structure to test one honestly. In its present form, the platform is already useful as an internal governed research operating system for signal development, comparison, and audit-ready review, even before any adaptive allocator is promoted.

## 3.2 Why This Matters

A reliable substrate changes the question from “can we imagine an adaptive allocator?” to “can we prove that one deserves promotion?” That distinction is central to the project’s philosophy. In many trading systems, governance is added after the fact. In MarketMind, governance is what gives future model complexity permission to exist at all. The next question is therefore not whether adaptive allocation is imaginable, but whether MarketMind’s specific task and regime formalism creates conditions under which adaptation can be expected to transfer.

# 4. Proposed Meta-Learning Architecture

## 4.0 Why this architecture might earn edge

MarketMind’s architecture is motivated by a **strategic hypothesis**, not an empirical finding already established in-repo: signal efficacy is **task-dependent**, and **reusable adaptation** across bounded episodes may improve **decision utility after frictions** versus always restarting from a static recipe. The credible source of incremental value is not raw model complexity, differentiable machinery, or scale for its own sake—it is **better structure under governance**: valid tasks, honest evaluation, capacity-aware conditioning, and disciplined uncertainty use. **The best frontier system is usually better structured, not merely bigger.**

## 4.1 Learning Unit

The proposed system learns over `MetaTask` objects. Each task is a regime-bounded episode split into support and query segments with purge, embargo, and `pit_boundary` semantics. This makes task construction a first-class architectural contract rather than an informal training convenience.

A regime in this context is a bounded market episode defined from a governed state-definition process combining observable market descriptors such as volatility structure, cross-sectional dispersion, correlation concentration, liquidity stress, and trend versus chop conditions. The exact assignment mechanism—rule-based, clustered, or latent-model-derived—must be documented in implementation artifacts; regime stability, transition rules, and relabel risk are audited like any other governed contract. The architecture is only credible if regime formation is itself transparent, reproducible, and not hindsight-shaped.

## 4.2 Runtime Shape

At a high level, the proposed runtime is:

```text
DataView.as_of(T)
    → feature and regime context
    → context encoder
    → signal library (narrow governed base today)
    → meta-policy allocator (governed hypothesis)
    → sizing; confidence attenuation by default
    → structured post-allocator conditioning (II-D target)
    → RiskFn / risk and execution layers (III conditional for execution-serious claims)
```

The important runtime boundary is that live inference uses frozen adapted parameters. The proposal does not assume unrestricted online gradient updates in the live path. **Pretrain broadly, adapt narrowly** remains the preferred safe-adaptation posture for any future live system.

The intended deployment scope for this runtime should be stated explicitly in companion specifications: asset universe, rebalance cadence, target holding horizon, and whether the execution layer is assumed to operate at end-of-day, scheduled intraday, or lower-latency horizons. Where those details are still open, any reported portfolio results remain conditional on stated assumptions.

RiskFn is also no longer treated as a black-box placeholder in the roadmap narrative. It is a governed protocol boundary whose operational seriousness matters for credibility, but full execution realism and deployment control remain conditional later-phase work rather than current system fact.

## 4.3 Dynamic Signal Universe

The design assumes a fixed-slot masked interface rather than dynamic output heads. Signal identity and ordering remain explicit so replay, gating, and promotion stay comparable as the active signal set changes. This is why the terminology around `slot_index`, `signal_embedding`, and dynamic-K masking matters across the documentation suite. Economically, this allows the allocator to preserve comparability and governance even as the active opportunity set changes, rather than treating signal turnover as a silent source of backtest instability.

## 4.4 Parameter Lifecycle

The parameter vocabulary is intentionally explicit:

- `theta_meta` is the learned initialization,
- `theta_task_prime` is the ephemeral task-adapted state,
- `theta_day_prime` is the frozen inference state produced by nightly adaptation.

Keeping those roles distinct is necessary for training logic, rollback semantics, and operational governance. This vocabulary matters because it defines what is learned globally, what is adapted locally, and what is allowed into the live path—three distinct questions that are often blurred in less governed systems.

## 4.5 Worked Example

In a rising-volatility, widening-spread regime, short-horizon momentum signals may lose reliability while mean-reversion and defensive cross-sectional quality signals gain relative value. A task-conditioned allocator would adapt from `theta_meta` toward a task-local state that reduces exposure to unstable momentum sleeves, increases weight on defensive signals, and attenuates gross exposure through `confidence_scalar`. The key validation question is whether this adaptation improves held-out query performance net of cost without degrading crisis robustness.

## 4.6 Competitive alternatives

The paper recognizes serious alternatives to meta-learning as the default answer: shallow regime-conditioned allocators, ensemble weighting, online learning, Bayesian state-space or regime models, transformer or time-series allocators, and RL-based allocators. Meta-learning is attractive only if it provides better transfer under regime recurrence without unacceptable operational complexity.

## 4.7 Regime definition and task formation (summary)

Regime construction, stability testing, transition handling, and anti-hindsight safeguards are first-class governance concerns: they are documented, governed, and replayable. Task pools derive from the same regime semantics as live inference so that support/query splits test adaptation on episodes that match the operational definition of “task.”

# 5. Validation Framework

## 5.1 Empirical Workstreams

The evaluation program is organized around five workstreams, each tied to an auditable metric family:

| Workstream | Named metric family (illustrative) |
|---|---|
| baseline superiority | net Sharpe, turnover-adjusted return, net of costs |
| task validity | regime separability, query-segment consistency |
| adaptation usefulness | support-to-query uplift on held-out segments |
| proxy alignment | correlation with exact information coefficient where applicable |
| continual-learning robustness | retention under rolling updates; forgetting diagnostics |

These workstreams are not background research. They are part of the implementation program and are allowed to halt it.

## 5.2 Acceptance Hierarchy

The proposed allocator must satisfy criteria at model, portfolio, and governance layers. Predeclared numeric thresholds will be attached to the implementation program; placeholders below state the decision structure.

| Layer | Test | Minimum threshold | Failure consequence |
|---|---|---|---|
| Model | Inner-loop / adaptation gain | TBD | No promotion |
| Model | Encoder coherence, cross-regime separation | TBD | No promotion; return to research |
| Portfolio | Net Sharpe after costs vs incumbent baseline | TBD | Remain challenger; simpler allocator stays |
| Portfolio | Walk-forward sanity, crisis holdout behavior | TBD | No promotion or rollback |
| Governance | PIT correctness, determinism | Zero tolerance | Automatic fail |
| Governance | Anti-Goodhart compliance, task-pool sufficiency | TBD | No promotion |

This hierarchy exists to prevent a strong-looking aggregate metric from hiding a broken learning process.

## 5.3 Held-Out Crisis Governance

Permanent crisis holdouts are central to the design. The goal is to prevent the system from becoming “good” only on the regime distribution it was tuned against. In practical terms, that means crisis replay and crisis holdout performance are part of promotion logic, not decorative stress-test appendices. Held-out sets include exemplar episode types such as volatility shock, liquidity shock, and correlation-break stress—chosen so the allocator cannot earn promotion solely on calm regimes.

## 5.4 Required Evidence

From the point Phase II is active, the system is expected to emit artifacts such as:

- `task_manifest.json` for exact task-pool provenance,
- `meta_validity_report.json` for adaptation, encoder, forgetting, and crisis evidence,
- canonical gate outputs tying those reports into a promotion decision,
- and checkpoint lineage sufficient for rollback to the last clean adapted state.

These artifacts are not only documentation outputs; they are gating objects for model approval, rollback, audit, and post-mortem analysis.

## 5.5 Quantitative promotion thresholds

Detailed numeric bands live with the validation program and gate configuration; the white paper records the obligation: every promotion decision must be traceable to predeclared thresholds for effect size, significance, turnover, drawdown, crisis retention, and net improvement versus the incumbent baseline. Revisions to thresholds follow governed protocol, not ad hoc relaxation.

# 6. Promotion, Rollback, and Kill Logic

## 6.1 Promotion

Promotion requires more than a good backtest summary. It requires:

- a clean `meta_validity_report.json`,
- success against the simpler baseline net of costs,
- no open PIT or governance exceptions,
- and successful shadow or capped-blend behavior if a rollout path exists.

Promotion requires sign-off across research, risk, and operating-control review, not only statistical pass conditions.

## 6.2 Rollback

The design assumes the allocator can be rolled back first to the last clean adapted checkpoint and beyond that to the incumbent allocator if needed. Rollback is therefore treated as a normal governance path rather than an embarrassing edge case.

## 6.3 Kill

The architecture is killed if it cannot demonstrate statistically significant adaptation, cannot beat the simpler baseline, cannot maintain coherent embeddings, or cannot generalize to held-out crisis regimes. The architecture is also killed if its incremental performance is too small to justify its added operational burden. MarketMind treats that outcome as valid research discipline rather than failure to be hidden.

# 7. Current Status vs Future Scope

## 7.1 Current Status

Current implementation truth is deliberately plain:

- there is no validated meta-policy allocator in production,
- there is no broker-integrated paper/live rollout path,
- there is no evidence today that the meta-learning architecture has beaten the simpler baseline,
- and there is no reason to speak as if the future architecture has already earned operational trust.

It is currently unknown whether the regime/task formalism is rich enough for transferable adaptation in finance; that question is precisely what the validation program is designed to answer.

## 7.2 Future Scope

Potential later stages include:

- paper/live promotion flow,
- richer execution calibration and TCA,
- conditional low-latency inference,
- broader Signal Factory automation,
- alternative-data and signal-factory breadth under governed admission,
- capacity analysis and capital-allocation scaling bands,
- deployment governance and production monitoring maturity.

Those stages are justified only if the allocator clears the validation program. They are real ambitions, not current facts, and they do not imply that automated signal discovery already exists today.

# 8. Operating Model

## 8.1 Research-Time Operating Model

Today’s practical operating model is a governed research loop used by researchers, reviewers, and risk or governance owners:

1. build or refine signals and governed strategy slices,
2. run them through the canonical bundle-producing path,
3. validate lineage, statistical, and execution-assumption artifacts,
4. preserve reconstructible provenance for review and comparison.

This loop is already valuable because it narrows the space in which false confidence can hide.

## 8.2 Intended Later Operating Model

If the allocator is validated, the intended operational progression is:

1. shadow or challenger evaluation,
2. limited exposure under explicit control,
3. broader rollout only if evidence stays clean,
4. rollback to the last clean checkpoint or incumbent allocator if evidence degrades.

The documentation is careful not to promise that later operating model before the evidence exists.

The execution layer should be described at a minimum by assumed rebalance frequency, slippage model class, liquidity filters, participation limits, and latency expectations. If those dimensions are intentionally out of scope for a given phase or report, that boundary is stated explicitly, and any reported portfolio results are conditional on those assumptions.

## 8.3 Capacity and capital profile

Expected capacity will depend on the eventual signal mix, turnover profile, and traded universe. Capacity therefore belongs in the promotion framework: a system that validates at small notional size but fails under realistic participation constraints should not be considered production-ready.

# 9. Risks and Limitations

Concrete failure narratives illustrate why governance and thresholds matter:

1. **Regime relabel instability.** If regime labels drift or are unstable out of sample, apparent adaptation on the training task distribution can vanish when assignment rules or clustering shift—making meta-learning look helpful until it is not.
2. **Cost-sensitive signals.** Sleeves that win in research under moderate cost assumptions can fail after realistic slippage and turnover, so net-of-cost promotion criteria are not optional.
3. **Continual updates versus rare crises.** Rolling updates may improve average behavior while dulling responses to rare stress episodes the firm cares about most; holdout crisis governance exists to catch that.

Bullet summary:

- **The simpler system may win.** The governance model explicitly allows the null hypothesis to stand.
- **Non-stationarity may outpace adaptation.** Even a validated nightly-adapted allocator may not respond fast enough to all shocks.
- **Operational complexity is itself a risk factor.** A system that is only marginally better but much harder to operate may not deserve promotion.
- **Backtest realism remains essential.** Cost, turnover, and holdout discipline must remain binding or the conclusions are not trustworthy.
- **Continual learning can fail in two directions.** The system can forget too much or become too rigid to adapt.
- **Task-pool sufficiency may be harder than expected.** Financial task diversity is limited relative to canonical meta-learning domains, which makes evidence quality especially important.
- **Capacity and crowding risk.** Edge may not scale with assets under management or may attract competition that erodes the effect.
- **State-definition error.** If regimes misstate the true economic state, adaptation optimizes the wrong objective.
- **Operational monitoring failure.** Without live checks on drift, cost, and governance signals, paper-validated behavior can diverge quietly in production.

# 10. Roadmap

## 10.1 Near-Term

Decision outputs: preserve the **closed** Phase I-F boundary; hold the **closed** Phase I-G companion baseline (README / Implementation Plan / Resolution Ledger v1.0.46) with published protocols as source of truth; keep a clear threshold table with provisional items marked `⚑ VALIDATE`.

- Phase I-F truth and architecture seams are **closed** at the **4.12.x** companion baseline—they should not be reopened casually.
- Phase I-G: **core protocol documents**, the governed MOM-020 comparison closure, MLN-02-AMD-01 companion/code alignment, RG-09 replay fixture closure, the bounded RG-09 II-0A harness/gate path, OI-39 closure (`paper_trade_sim_spec.md`), the II-0 empirical research meta-validity scaffold, and the **strict H3** live promotable anchor (Resolution Ledger §1.5) are published; **RG-09** (**PARTIAL**) and **OI-59** (**OPEN**) continue as **II-0** / **non-blocking** follow-on, not remaining I-G debt.
- Scaffold the Phase II-0 validation harness (**II-0B-first** emphasis) from the frozen replay-fixture baseline, without pretending the allocator is already validated.

## 10.2 Medium-Term

Decision outputs: consolidated validation evidence and a governed build decision on whether Phase II deserves to progress beyond narrow justified surfaces.

- run the five empirical workstreams,
- build the adaptive system only in evidence order,
- and decide promotion, rollback staging, narrowing, or kill based on measured results rather than architectural preference.

## 10.3 Long-Term

Decision outputs: pursue III and IV only if allocator validation, execution realism, and product need clear defined bars.

Only after successful validation does it become reasonable to pursue conditional execution expansion and conditional signal-factory scale-out. Execution realism matters for credibility, but it is still conditional. **Alternative-data pipelines** and **signal-factory scale** remain later-phase engineering; **admissibility and expansion policies** are already published as governance prerequisites, not as runtime features.

# 11. Conclusion

MarketMind’s differentiator is not simply that it specifies an ambitious allocator. It is that it refuses to treat ambition as evidence. The system is strongest where many trading platforms are weakest: disciplined data boundaries, explicit governance, reproducible artifacts, and a willingness to let a simpler baseline win if the evidence demands it. The proposed meta-learning allocator remains an important candidate architecture, but its promotion depends on proof, not desire.

The strategic question, however, is not only whether MarketMind can prevent false positives. It is whether the platform’s regime/task formalism can uncover repeatable allocation advantages that simpler systems miss. This white paper therefore presents both a disciplined substrate and a testable economic thesis: state-dependent signal efficacy may be transferable enough to support governed adaptation. Whether that thesis is true remains an empirical question, and the platform is designed to answer it honestly.

# Appendix A — Glossary

| Term | Meaning |
|---|---|
| `MetaTask` | Regime episode used as the learning unit |
| `regime_id` | High-granularity task identity |
| `regime_class` | 5-class projection used for curriculum and reporting |
| Regime construction | Governed process that maps observables to bounded episodes and task identity |
| Support/query split | Within-task segments for adaptation (support) vs held-out evaluation (query) |
| Crisis holdout | Permanently reserved periods or episode types excluded from training/tuning |
| Promotion threshold | Predeclared numeric or rule gate required for allocator promotion |
| Capacity | Scale of capital or participation beyond which edge degrades materially |
| Participation limit | Upper bound on volume or footprint vs liquidity to contain market impact |
| `theta_meta` | Learned initialization |
| `theta_task_prime` | Task-adapted ephemeral state |
| `theta_day_prime` | Nightly-adapted live inference state |
| `allocation_weights` | Allocator output over the active signal set |
| `confidence_scalar` | Post-sizing exposure attenuation term by default; routing pilot is conditional |
| `signal_embedding` | Stable per-signal learned representation distinct from regime context |
| `regime_embedding` | Dense representation of current market context emitted by the context encoder |

<!-- MM:END:DOCBODY -->
