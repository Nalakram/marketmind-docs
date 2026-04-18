# Paper-trading simulation requirements (OI-39 — closed v4.18.5)

**Status:** Phase I-G handoff notes — not a production contract. **Phase III remains conditional** on prior gates and governance.

## Purpose

Capture the dimensions a future **paper-trading simulation** should respect so that research evidence is not confused with live readiness. This document does **not** implement execution, routing, or broker connectivity.

## Realism dimensions (to be specified in a later design pass)

- **Latency and partial fills** — order acknowledgment delay, queue position, and realistic fill ratios for the asset class under test.
- **Fees and slippage** — explicit friction model (per-share, bps, minimum ticket) tied to instrument and venue assumptions.
- **Borrow / short constraints** — where applicable, availability and rate shocks for short-side simulation.
- **Corporate actions** — splits, dividends, and halts at least at a schematic level for equity-like surfaces.
- **Session boundaries** — exchange hours, auction phases, and stale-quote handling for intraday paths.

## Utility-after-frictions framing

Decision quality should be assessed **after** applying the friction model: utility (e.g., net PnL, risk-adjusted return under constraints) must be computed on **post-friction** paths so that “paper alpha” is not overstated relative to deployable edge.

## Explicit out-of-scope statements

- **Broker connectivity** — live or paper **API integration**, credential handling, and order routing are **out of scope** for this starter spec and for the RG-09 empirical-closure lane.
- **Promotable allocator code** — no training, allocation, or promotion semantics are implied here.

## Phase III conditionality

Full paper-trading **productization** belongs to **Phase III** and remains **conditional**: it must not be interpreted as Phase II trainer readiness, GATE-II-01 readiness, or closure of MLN items.

## Related governance items

- **OI-39** — paper-trading simulation requirements (this note seeds the requirement space).
- **RG-09** — empirical closure remains in the II-0 evidence lane; broker simulation is not part of that closure.
