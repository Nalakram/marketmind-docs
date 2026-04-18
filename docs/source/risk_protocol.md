# RiskFn Protocol

Governed boundary between allocator outputs (`meta_policy.py`) and risk / exposure control. Phase II defines the interface; this document is normative for what RiskFn may consume and do.

---

## 1. Allocator Output Surface

**Permitted inputs to RiskFn:**

- `allocation_weights` — simplex over active signals, produced by `meta_policy.py`
- `confidence_scalar` — scalar in [0, 1], produced by `meta_policy.py` as a calibrated reliability estimate for the current allocation

**Informational only (not sizing inputs):**

- `regime_class` — produced by `meta_policy.py`; used for reporting and curriculum; must not modify sizing in Phase II

**Not consumed by RiskFn in Phase II:**

- Raw signal scores, feature vectors, or any input upstream of `meta_policy.py`
- `theta_meta`, `theta_task_prime`, or any model weight surface
- Any output from `reptile_trainer.py` or the inner loop

*RiskFn consumes the allocator's terminal output, not its internal state.*

---

## 2. Permitted Actions (Phase II)

RiskFn's single permitted Phase II action is post-sizing exposure attenuation via `confidence_scalar`.

The normative rule:

```
live_position = base_position × confidence_scalar
```

where `base_position` is the output of `SizingFn` applied to `allocation_weights`, and `confidence_scalar ∈ [0, 1]`.

Full abstention corresponds to `confidence_scalar = 0`.

**Hard constraints:**

- `confidence_scalar` may only reduce exposure from base size. Levering above base size is not permitted in Phase II under any condition.
- `confidence_scalar` must not be used as a signal-selection gate or a hard on/off switch in Phase II without an ADR.
- RiskFn must not introduce opaque sizing adjustments without a traceable audit path.

**Broader uncertainty controls** (sizing, participation, turnover, abstention) are within scope as `confidence_scalar`-informed governance mechanisms, but all must remain in the exposure-reduction direction.

---

## 3. Post-Allocator Conditioning (II-D Scope — Not RiskFn)

**II-D owns** (not RiskFn):

- Turnover-budgeted target generation
- Liquidity and capacity scaling via impact model
- Drawdown and regime-conditioned risk overlays
- Structured constraints: neutrality, CVaR, borrow/funding, participation limits

**Why the distinction matters:**

A named failure mode in this program is *confusing II-D conditioning wins for allocator validation*. If II-D overlays improve realized outcomes, that is deployment-layer governance working correctly — it is not evidence that the allocator itself earned promotion. RiskFn must compose cleanly with II-D without absorbing its scope.

*RiskFn processes allocator output. II-D conditions that output for deployment. These are separate responsibilities and must not be conflated in evaluation claims.*

---

## 4. Phase Scope Boundaries

| Phase   | RiskFn scope |
|---------|--------------|
| Phase II | Define the interface boundary; implement `confidence_scalar` attenuation; no execution-serious calibration |
| Phase III | Execution-serious calibration; operator enforcement; borrow/funding costs; participation limits; full impact model integration |

Phase II may define the interface without implying Phase III realism. Phase III is the first phase allowed to become execution-serious.

---

## 5. Auditability Requirements

RiskFn must produce a traceable sizing record per session. Required fields:

- `confidence_scalar` value as received from `meta_policy.py`
- mean attenuation factor applied across active positions
- ECE from most recent calibration pass
- reliability curve snapshot (calibration provenance reference)
- any abstention events with reason codes

These fields are required in `meta_validity_report.json` for Phase II governed runs.

---

## 6. Provisional Thresholds

All values `⚑ VALIDATE` until resolved by governed evidence. None are frozen constants.

| Threshold | Description | Governance home |
|-------------|-------------|-----------------|
| ECE recalibration trigger | If ECE exceeds this value, recalibrate before promoting `theta_day_prime` | `⚑ VALIDATE`; see MetaLearningCore §2.5.1 |
| Mean `confidence_scalar` alert floor | If mean drops below this for 3+ sessions, alert | `⚑ VALIDATE`; see MetaLearningCore §11.1 |
| Rolling IC correlation floor | Minimum rolling correlation between `confidence_scalar` and realized allocation quality | `⚑ VALIDATE`; see MetaLearningCore §11.1 |
| Attenuation curve shape | Parameterization of how `confidence_scalar` maps to position scale | `⚑ VALIDATE`; resolved at Phase II calibration |

---

## 7. Handoff References

- [`paper_trade_sim_spec.md`](paper_trade_sim_spec.md) — Phase III realism expectations that RiskFn must eventually satisfy
- ResolutionLedger **MLN-03** — normative `confidence_scalar` contract (post-sizing default)
- ImplementationPlan **Appendix D** — deployment-layer conditioning as II-D scope
