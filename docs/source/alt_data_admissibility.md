# Alternative-Data Admissibility Contract

PIT, provenance, and replay requirements for any non-standard data source before it may enter MarketMind's feature or signal stack. Published with Resolution Ledger OI-38 (v4.16.0).

**Precedence:** If [`signal_universe_expansion_policy.md`](signal_universe_expansion_policy.md) and this document appear to conflict on admissibility boundaries, this contract (OI-38) is evaluated first. Only sources that clear this contract may enter signal-universe expansion review under OI-37.

---

## 1. Purpose and Current State

This document freezes the PIT, provenance, and replay contract that any non-standard data source must satisfy before it can enter MarketMind's feature or signal stack.

**Current state:** No alternative-data or non-tabular source is live in MarketMind. The current governed feature stack is built entirely on price, volume, and standard market microstructure data accessed through `DataView.as_of(T)`. This document establishes the bar that future sources must clear — it does not imply any such source is ready or underway. Frontier framing for the alt-data research direction remains in Meta-Learning Architecture Vision §4.9.

**Critical distinction (apply throughout this document):**

Satisfying this document's admissibility preconditions makes a source eligible for governed evaluation runs. It does not make the source admitted as a signal or feature. Admission as a signal still requires passing the full Signal Generation Protocol admission gate. Promotion to active curriculum status still requires the Signal Generation Protocol plus the signal-universe expansion gate conditions.

---

## 2. What This Document Governs

"Alternative data" means any data source beyond the existing governed price/volume/microstructure tabular stack:

- **Non-tabular structured data:** earnings transcripts, news, analyst reports, SEC filings
- **Event-driven data:** corporate actions, macro announcements, index reconstitutions
- **Alternative tabular data:** credit card transaction aggregates, satellite imagery-derived metrics, short interest, web traffic, app usage
- **Macro/non-market tabular data:** GDP revisions, inflation expectations, yield curve data from non-price sources

All categories are subject to the same requirements defined here.

---

## 3. PIT Requirements

**Availability timestamping:** Every record must carry an `available_at` timestamp representing the earliest time the data was realistically knowable to a market participant. This is distinct from the event timestamp (`event_ts`) — for example, a GDP revision may have an `event_ts` of the reporting period but an `available_at` of the publication date. Any pipeline that conflates these is inadmissible.

**Point-in-time access:** The source must be accessible via `DataView.as_of(T)` or a governed equivalent that enforces the PIT boundary. Direct raw-store reads outside the governed DataView interface are inadmissible.

**No look-ahead:** Historical evaluation may only use data with `available_at <= decision_ts`. No record may be used where `available_at > decision_ts`, regardless of how it was obtained.

**Vintage preservation:** Sources that publish revisions must preserve historical vintages. A pipeline that silently overwrites historical values with revised values is inadmissible without explicit vintage-selection logic that respects `available_at`.

---

## 4. Provenance Requirements

**Source identifier:** Each data source must have a stable, versioned identifier recorded in every feature or signal that depends on it.

**Content addressability:** Dataset snapshots used in governed runs must be content-addressable — identified by a hash of their content, not only their filename or retrieval timestamp.

**Lineage:** Every feature computed from alternative data must carry traceability back to the governed DataView path. Features computed directly from external APIs without passing through `DataView.as_of(T)` are inadmissible.

**Terms of use:** The data source's terms must not prohibit the intended research use. This must be documented before evaluation work begins.

---

## 5. Replay Requirements

**Deterministic replay:** A governed run using alternative data must produce the same results when replayed with the same inputs. Fixture production is a precondition for governed evaluation, not a post-hoc reproducibility aid.

**State-dependent data:** For sources where the value at a given time depends on when it is queried (e.g. point-in-time macro revisions), the governed path must capture and freeze the state at run time. Post-hoc replay using a differently-versioned source is a PIT violation.

**Fixture requirement:** Before any alternative-data signal can be evaluated in a governed run, a versioned data fixture must exist for the evaluation window. The fixture must satisfy the same provenance requirements as the general replay fixture pattern (`docs/rg09/rg09_replay_fixture_spec.md` is the model).

---

## 6. Event-Driven Entry Path

Event-driven data is not supported and is explicitly out of scope for Phase I-G and Phase II. Admitting event-driven data requires additional contract work beyond this document:

- Asynchronous event ordering with PIT semantics
- Idempotent processing guarantees
- Explicit handling of irregular time series
- A governed entry path integrating with `DataView.as_of(T)` without bypassing PIT discipline

This entry path is planned contract work for Phase IV. Event-driven data is not currently admissible, and its admissibility path is a Phase IV deliverable.

---

## 7. Admissibility Decision Tree

For a source to be eligible for governed evaluation runs, all seven preconditions must be satisfied in order:

1. Terms of use documented and cleared
2. `available_at` timestamping confirmed for all records
3. PIT access path exists via `DataView.as_of(T)` or governed equivalent
4. Vintage preservation confirmed (or not applicable for non-revised sources)
5. Deterministic replay fixture producible for the target evaluation window
6. Content-addressable dataset snapshot feasible
7. Source identifier stable and versioned

If any precondition is unmet, the source is inadmissible until it is resolved. It may not be used in any governed evaluation run while inadmissible.

Clearing all seven preconditions makes a source eligible for evaluation — not admitted as a signal, and not promoted to active curriculum.
