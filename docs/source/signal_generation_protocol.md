# Signal Generation Protocol

How candidate signals enter, remain in, and leave the governed signal universe. Admission policy is frozen in Phase I-G; signal-factory-serious expansion remains Phase IV scope.

---

## 1. Current Governed Base

**Active governed signals (as of v4.13.1):**

- `momentum_xsec` — cross-sectional momentum
- `momentum_tsmom` — time-series momentum
- `momentum_dual` — dual-momentum variant
- `stat_arb_pairs` — mean-reversion pairs strategy

The current base is narrow by design. Breadth expansion without governance controls negates the value of the signal library. This section must not imply signals beyond this list are under development or planned for Phase II.

---

## 2. Admission Requirements

A signal may not enter `SignalCatalog` or appear in any training task without satisfying all of the following:

| Requirement | Description |
|---------------|-------------|
| Signal ABC | Must implement `Signal ABC` with all required fields |
| SignalCatalog registration | Must be registered and receive a stable `slot_index` |
| PIT-safe feature ops | All features computed exclusively through governed `_OP_REGISTRY` ops over `DataView.as_of(T)` inputs |
| `screening_report.json` | Admission evidence must emit through the governed screening path |
| `stat_validity_report.json` | Must pass the statistical validity gate at canonical v1 contract |
| No dual execution paths | Signal feature computation must not use `_FEATURE_OPS` direct execution for any governed path |

Admission is a structural and governance check. Meeting admission requirements does not imply the signal is promoted to active curriculum status.

---

## 3. Admission vs Promotion vs Retirement

These are three distinct states. No signal may silently transition between them.

**Admission:** Signal meets all structural requirements in Section 2. Enters `SignalCatalog` with `active: false` initially. `slot_index` assigned at registration.

**Promotion:** Signal moves to `active: true` in curriculum. Requires evidence of sustained walk-forward performance after realistic costs, documented in the ledger or a governed evaluation artifact. Promotion requires an explicit decision, not absence of failure.

**Active:** Signal participates in training task construction and curriculum sampling.

**Retirement:** Signal removed from `active` status. Requires documented rationale. Retired signals remain in `SignalCatalog` with `retired: true` for replay traceability. `slot_index` is never reused after retirement.

*Admission to Active is not automatic. Promotion requires evidence. Retirement requires rationale.*

---

## 4. Signal Identity and Provenance

| Field | Rule |
|-------|------|
| `signal_id` | Canonical string identifier. Stable after registration. Never reused. |
| `slot_index` | Stable integer key. Monotonic at registration. Idempotent on re-registration of same `signal_id`. Never reused after retirement. |
| `signal_set_version` | Integer that increments whenever the active signal set changes. Carried on all `MetaTask` artifacts and replay surfaces. |

Historical `slot_index` mappings must remain reconstructible for every `signal_set_version`.

`slot_index` is the stable key for meta-policy weight vectors and embedding lookup. Any change to `slot_index` assignment rules requires an ADR.

---

## 5. Retirement and Decay Handling

A signal must be retired if:

- It fails the statistical validity gate on three or more consecutive governed runs
- Its feature implementation is found to violate PIT-safe DataView discipline
- A governance review determines its admission evidence was incorrect

**Retirement procedure:**

1. Set `retired: true` in `SignalCatalog`
2. Document rationale in a signal retirement log entry (ledger OI or equivalent)
3. Increment `signal_set_version`
4. Do not reuse `slot_index`

Decay is distinct from retirement. A signal showing declining IC is a monitoring signal, not an automatic retirement trigger. Retirement requires explicit governance action.

---

## 6. Alternative-Data and Non-Tabular Signals

Not permitted in the current Phase I-G admission lane until a source clears the published contracts.

Event-driven, non-tabular, and alternative-data sources must satisfy the PIT/provenance/replay bar in [`alt_data_admissibility.md`](alt_data_admissibility.md) (Resolution Ledger **OI-38**, closed v4.16.0). That contract governs **eligibility for governed evaluation runs**; it does not admit a signal. Promotion to active curriculum still requires the signal-universe expansion gate conditions in [`signal_universe_expansion_policy.md`](signal_universe_expansion_policy.md) (**OI-37**, closed v4.16.0) in addition to this protocol’s admission and promotion rules.

*Alternative-data signals are not prohibited — they require the admissibility contract before admission evaluation and the expansion policy before active curriculum promotion.*

---

## 7. Breadth Policy

Signal-factory-serious expansion is Phase IV scope:

- Batch admission of new signals is not permitted in Phase II without explicit per-signal governance
- Multiple-testing discipline (Harvey t gate, DSR, PBO) is required before any breadth claim
- `signal_embedding` (Phase IV identity layer) is not required for admission or promotion in Phase II
- Any proposal to expand the signal universe during Phase II must be individually justified and documented in the ledger

*The current narrow governed base is the production truth. Breadth is a future program under explicit policy constraints, not a background expansion lane.*
