# Version History

This file serves as the project's release ledger and architecture evolution.
For a traditional short-form change summary, see commit history.

Older release entries are archived in `docs/releases/`.

---

## Version Index

### 7.x — Phase II-0B governed artifact contract hardening and closure rollout

- 7.2.3 — Patch release completing the non-promotable II-0C pilot harness: explicit pilot/dry-run semantics, research-only report shells (`ii0c_pilot_report.json`, `ii0c_dry_run_summary.json` plus dual-written legacy `phase2_ii0c_scaffold_non_promotable.json` for path-based collectors), pre-emission governed `baseline_comparison` key discipline plus baseline/shared parity validation, and a frozen reference input bundle with integration drift-replay coverage (harness stability only)
- 7.2.2 — Patch release for II-0C scaffold dry-run wiring: adds the non-promotable II-0C dry-run / pilot lane on top of the unchanged governed II-0B artifact contract, keeps **GATE-II DEFERRED**, preserves the XGBoost incumbent comparison baseline, and fails closed when task identity drifts across task, encoder, comparison, or shared-context surfaces
- 7.2.1 — Patch release for II-0B closure truthfulness: canonical `pysrc/pipeline` orchestration now fails closed when governed II-0B evidence is non-usable, borrowed `THR-RG09-V03` / `THR-RG09-V17` references on that lane are explicitly framed as reviewer-visible lineage rather than native orchestration policy, and companion docs are advanced to the synchronized 7.2.1 / 6.5.8 / 1.4.29 suite state
- 7.2.0 — Phase II-0B companion-truth closure on the non-promotable artifact-and-contract lane: canonical `pysrc/pipeline` orchestration now emits governed II-0B evidence under a dedicated non-promotable subdirectory, governed consumers surface threshold-governance summaries uniformly, stale pre-hash root triples are explicitly retired from current governed evidence, and companion docs advance to **II-0B COMPLETE** while preserving **GATE-II DEFERRED**
- 7.1.0 — Minor directory structure hardening: canonical package tree with typed
  stubs for ml/datasets, domain/portfolio, domain/risk, autotune, bridge/orchestrator,
  and tuning/hparam_search; runtime cleanup removing legacy dependency_manager
- 7.0.0 — Major Phase II-0B governed artifact-contract hardening: required
  non-recursive `content_hash` binding on all three governed artifact surfaces,
  shell-level semantic validation for PIT/hash, baseline/shared-context, seed
  lineage, threshold legality, and threshold state/expression tamper checks while
  preserving II-0B as non-promotable scaffolding only

### 6.x — Domain package ownership and utility retirement

- 6.2.2 — Companion document sync and DOCX CI repair for II-0A completion after
  CI confirmation: WS-1, WS-2, WS-3, and II-0A are now recorded as complete
  across the managed companion suite while preserving the XGBoost
  incumbent-baseline boundary; the release-docs path no longer trips stale
  `copysrc` typo references
- 6.2.1 — Froze the strict-H3 RG-09 reference anchor under `run_bundles/rg09_reference_v1`,
  added the reproduction verifier and GitHub Actions drift workflow, generated the WS-3
  task-validity integration report, and recorded the anchor in the Resolution Ledger
- 6.2.0 — Added the II-0A WS-2 task-validity diagnostic harness under `pysrc.validation`
  with schema-validated reports, synthetic positive/negative controls, and RG-09 ledger
  readiness notes scoped to WS-3 follow-up
- 6.1.0 — Consolidated all tuning surfaces into canonical `pysrc.tuning`; deleted `pysrc.autotune`,
  `pysrc.tuning.grid_search`, `random_search`, `bayesian_optimization`; introduced registry-driven
  engine dispatch, typed boundary contracts, and unified direction semantics
- 6.0.0 — Retired the `py.utils.*` implementation import contract; moved runtime, errors,
  validation, data helpers, statistics, Torch runtime, tuning support, and pipeline config into
  canonical domain packages; added SemVer rules to the Artifact Write Contract; restored
  `mypy pysrc --strict`

### 5.x — Repository layout (`py/`, `java/src/`)

- 5.1.0 — Java bridge migrated to Kotlin; retired Python shim surfaces removed and imports retargeted to canonical modules; Pydantic v2 validator compatibility fix in `py.infra.brokers.ibkr`
- 5.0.0 — Repository layout: Python package at `py/` (`py.*` imports; replaces `srcPy.*`); Maven tree under `java/src/`; ADR-003; dev dependency on PyPI `py` + import shim for pytest compatibility

## Archived Releases

Full release entries for older versions are preserved in:

- docs/releases/VERSION_6.x.md
- docs/releases/VERSION_5.x.md
- docs/releases/VERSION_4.x.md
- docs/releases/VERSION_3.x.md
- docs/releases/VERSION_2.x.md
- docs/releases/VERSION_1.x.md

---

## Version 7.0.0 (2026-04-15)

Changelog for Phase II-0B governed artifact-contract hardening and shell semantic validation.
Version: 7.0.0 (required II-0B content hashes plus governed triple semantic verification)

### Major Themes Across All Changes

- Governed Phase II-0B artifacts now carry explicit deterministic `content_hash` payload metadata.
- The ML evidence shell now re-checks artifact-level semantics instead of stopping at presence/schema/binding checks.
- Threshold references in `meta_validity_report.json` are checked against the canonical threshold register for ID legality, state, and current expression.
- II-0B remains non-promotable scaffolding only; no trainer, allocator, broker, rollout, shadow/blend/live, or execution-readiness machinery was added.

### Detailed Changes

| Subsystem | Change |
|---|---|
| `pysrc/meta/phase2_artifact_contract.py` | Added non-recursive canonical artifact content hashes, public triple validation, cross-artifact seed-lineage/hash checks, and threshold state/expression reconciliation against the register |
| `schemas/phase2_task_manifest.schema.json` | Added required top-level `content_hash` object |
| `schemas/phase2_meta_validity_report.schema.json` | Added required top-level `content_hash` object |
| `schemas/phase2_execution_assumptions.schema.json` | Added required top-level `content_hash` object |
| `marketmind_gate/gates/phase2_ml_evidence_shell.py` | Reuses canonical triple validation and reports `SEMANTIC_INVARIANT_INVALID` on tampered governed evidence |
| `tests/python/unit/meta/test_phase2_artifact_contract.py` | Added content-hash emission and schema rejection coverage |
| `tests/python/unit/gate/test_phase2_ml_evidence_shell.py` | Added fail-closed shell coverage for PIT/hash, baseline/shared-context, threshold legality, threshold state/expression tampering, RG-09 anchor misuse, and seed-lineage mismatch |
| `README.md` / `docs/src/README.md` | Advanced suite entrypoint truth to 7.0.0 and recorded II-0B partial hardening without allocator-readiness claims |
| Companion Markdown sources | Advanced live companion stamps and current-state prose for Implementation Plan v6.5.6, Technical Roadmap v1.4.27, Meta-Learning Core v1.2.25, Architecture Vision v1.3.6, Resolution Ledger v1.0.52, Phase II Artifact Contract v1.0.3, Threshold Governance Register v1.0.3, and related companion surfaces |

### Behavioral Changes

- `emit_phase2_artifacts()` emits `content_hash` on `task_manifest.json`, `meta_validity_report.json`, and `execution_assumptions.json`.
- `phase2_ml_evidence_shell` rejects governed triples with stale or tampered content hashes, PIT mismatch, signal hash mismatch, baseline/shared-context mismatch, invalid threshold usage, threshold state/expression drift, or cross-artifact identity mismatch.
- Valid non-gate provisional threshold evidence remains allowed and visibly provisional.

### Breaking Changes

- Governed Phase II-0B artifact schemas now require `content_hash` on all three artifact surfaces.
- Existing governed II-0B triples without `content_hash` must be regenerated through `emit_phase2_artifacts()` before they can validate against the 7.0.0 schemas.

### Test / Validation Evidence

- `python -m pytest tests/python/unit/gate/test_phase2_ml_evidence_shell.py --no-cov` — 15 passed; Windows pytest temp symlink cleanup emitted a post-run `PermissionError` after the passing result.
- `python -m pytest tests/python/unit/meta/test_phase2_artifact_contract.py tests/python/unit/meta/test_threshold_governance.py tests/python/unit/meta/test_seed_policy.py tests/python/unit/meta/test_phase2_canonical_ownership.py tests/python/unit/gate/test_phase2_ml_evidence_shell.py tests/python/integration/meta/test_run_rg09_gate.py tests/python/integration/meta/test_run_oi59_segmentation_redesign.py --no-cov` — 81 passed; Windows pytest temp symlink cleanup emitted a post-run `PermissionError` after the passing result.
- `python -m mypy pysrc/meta/phase2_artifact_contract.py pysrc/meta/seed_policy.py pysrc/meta/threshold_governance.py marketmind_gate/gates/meta_learner_scaffold.py marketmind_gate/gates/phase2_ml_evidence_shell.py --strict` — pass.
- `python -m py_compile pysrc/meta/phase2_artifact_contract.py pysrc/meta/seed_policy.py pysrc/meta/threshold_governance.py marketmind_gate/gates/meta_learner_scaffold.py marketmind_gate/gates/phase2_ml_evidence_shell.py` — pass.

### Companion Document Versions

| Document | Version |
|---|---|
| README | v7.0.0 |
| Implementation Plan | v6.5.6 |
| Technical Roadmap | v1.4.27 |
| Meta-Learning Core | v1.2.25 |
| Meta-Learning Architecture Vision | v1.3.6 |
| Resolution Ledger | v1.0.52 |
| Phase II Artifact Contract | v1.0.3 |
| Phase II Research Execution Playbook | v1.0.2 |
| Threshold Governance Register | v1.0.3 |

DOCX outputs were not regenerated in this pass; the Markdown sources are the updated companion truth.

### Release Artifacts

- Trace: `docs/traces/7.0.0_implementation_trace.md`
- Manifest: `docs/manifests/7.0.0_change_manifest.json`

---

## Version 7.2.3 (2026-04-18)

Changelog for II-0C pilot-harness completion (non-promotable research surfaces only).
Version: 7.2.3 (II-0C pilot semantics, report shells, reference replay, and stricter pre-emission checks)

### Major Themes Across All Changes

- Clarified operational pilot vs dry-run semantics while keeping II-0C explicitly non-promotable and **GATE-II DEFERRED**.
- Added research-only JSON report shells at bundle roots (`ii0c_pilot_report.json`, `ii0c_dry_run_summary.json`) that reviewers must not treat as promotable Phase II evidence; dry-run also re-emits the historical `phase2_ii0c_scaffold_non_promotable.json` path with the compact summary shape so CI collectors and hard-coded glob paths do not silently miss output.
- Fail closed before governed emission if `baseline_comparison` carries extra keys (scaffold leakage guard) or if `shared_comparison_context` disagrees with baseline fingerprints or run identifiers.
- Introduced a frozen reference MetaTask request plus encoder config for deterministic drift replay tests.

### Detailed Changes

| Subsystem | Change |
|---|---|
| `pysrc/meta_learning/phase2_ii0c_comparison.py` | Adds `GOVERNED_BASELINE_COMPARISON_KEYS` and `validate_ii0c_governed_baseline_and_shared_context(...)` for strict baseline purity and shared-context parity |
| `pysrc/meta_learning/phase2_ii0c_reference.py` | Adds frozen II-0C reference harness inputs (seed, timestamps, task request, encoder config) scoped to wiring replay, not model validity |
| `pysrc/pipeline/phase2_ii0c_runner.py` | Emits pilot/dry-run research reports, records semantic outcomes, extends pre-emission validation, writes canonical `ii0c_dry_run_summary.json`, and dual-writes legacy `phase2_ii0c_scaffold_non_promotable.json` (compact shape) for downstream path compatibility |
| `tests/python/integration/test_phase2_ii0c_reference_harness.py` | Adds end-to-end reference replay stability checks plus pilot emission coverage |
| Unit tests | Extend II-0C runner/comparison coverage for report shells, baseline purity, and shared fingerprint drift |

### Behavioral Changes

- `run_phase2_ii0c_pilot(...)` now writes `ii0c_pilot_report.json` under the bundle directory after governed emission succeeds.
- `run_phase2_ii0c_dry_run(...)` writes `ii0c_dry_run_summary.json` (full research-only harness report) and **also** writes `phase2_ii0c_scaffold_non_promotable.json` with the same compact summary shape as pre-7.2.3 so path-based collectors keep working; `PHASE2_II0C_SUMMARY_FILENAME` remains the canonical new path for in-repo imports.
- Both entrypoints reject governed baseline objects whose key set is not exactly the Phase II comparison contract keys, and reject shared-context drift vs baseline fingerprints.

### Breaking Changes

- None for path-based dry-run collectors: the historical `phase2_ii0c_scaffold_non_promotable.json` filename is still emitted. Callers that want the expanded harness report should read `ii0c_dry_run_summary.json` (or use the in-memory `II0CRunResult.summary` object returned from `run_phase2_ii0c_dry_run`).

### Companion Document Versions

| Document | Version |
|---|---|
| README | v7.2.3 |
| Implementation Plan | v6.5.10 |
| Technical Roadmap | v1.4.31 |

---

## Version 7.2.2 (2026-04-17)

Changelog for the II-0C scaffold dry-run lane and task-identity fail-closed wiring.
Version: 7.2.2 (non-promotable II-0C scaffold dry run on the unchanged governed II-0B artifact lane)

### Major Themes Across All Changes

- Added a scaffold-only Phase II-0C dry-run / pilot lane without creating promotable trainer, allocator, broker, rollout, or execution-serious behavior.
- Preserved **GATE-II DEFERRED** and the existing governed II-0B artifact contract as the evidence-emission lane.
- Preserved the XGBoost incumbent as the challenger comparison baseline and kept RG-09 / strict-H3 evidence scoped to task-validity reference use, not incumbent-baseline use.
- Added fail-closed task-identity binding across both public II-0C entrypoints so task, encoder, comparison, and shared-context surfaces cannot silently drift.

### Detailed Changes

| Subsystem | Change |
|---|---|
| `pysrc/meta_learning/phase2_ii0c_tasks.py` | Adds a thin II-0C MetaTask scaffold adapter over canonical `build_meta_task(...)`, preserving deterministic task identity, support/query separation, PIT boundary propagation, purge/embargo checks, and serialization-ready `TaskManifestTaskInput` lowering |
| `pysrc/meta_learning/phase2_ii0c_encoder.py` | Adds a deterministic, versioned encoder stub that is explicitly scaffold/reference-only, emits configured-dimension task embeddings, and records non-promotable metadata without claiming representation validity |
| `pysrc/meta_learning/phase2_ii0c_comparison.py` | Adds II-0C comparison payload builders that enforce `xgboost_incumbent` as the incumbent baseline, reject RG-09 / strict-H3 / task-validity anchor misuse, and fail closed on data/split/cost parity drift |
| `pysrc/pipeline/ii0c_governed_artifacts.py` | Adds an II-0C wrapper around the existing governed II-0B triple; the wrapper writes only after `emit_phase2_artifacts(...)`, `validate_phase2_artifact_triple(...)`, content-hash checks, and ML evidence shell structural usability succeed |
| `pysrc/pipeline/phase2_ii0c_runner.py` | Adds `run_phase2_ii0c_pilot(...)` and `run_phase2_ii0c_dry_run(...)`, with shared fail-closed identity validation before governed artifact emission on both entrypoints |
| II-0C unit coverage | Adds deterministic tests for MetaTask scaffold invariants, encoder determinism and configured dimension, XGBoost baseline enforcement, governed wrapper validation, public runner paths, and pre-emission identity-drift rejection |
| Companion Markdown sources | Advance the suite entrypoint and planning roadmap to README **7.2.2**, Implementation Plan **6.5.9**, and Technical Roadmap **1.4.30**, recording the II-0C scaffold dry-run lane while preserving **GATE-II DEFERRED**, the XGBoost incumbent baseline, and the unchanged governed II-0B artifact lane |

### Behavioral Changes

- `run_phase2_ii0c_pilot(...)` and `run_phase2_ii0c_dry_run(...)` now refuse to emit governed artifacts unless:
  - encoder metadata `task_id` matches the canonical MetaTask `task_id`;
  - comparison `challenger_run_id` matches the canonical MetaTask `task_id`;
  - shared comparison context `task_id` matches the canonical MetaTask `task_id`.
- II-0C governed output is labeled scaffold-only / non-promotable while the underlying governed triple remains Phase II-0B.
- The II-0C dry-run summary exposes task, encoder, comparison, and shared-context identity bindings for reviewer audit.
- The comparison payload remains schema-compatible with the strict governed `baseline_comparison` object; scaffold lane metadata is kept out of that object.

### Breaking Changes

- None for promotable systems; II-0C remains non-promotable scaffolding only.
- Custom II-0C dry-run / pilot providers that emit mismatched task identity across task, encoder, comparison, or shared context now fail before artifact emission.

### Test / Validation Evidence

- `cmd.exe /c ".venv-codex\Scripts\python.exe -m pytest tests\python\unit\meta_learning\test_phase2_ii0c_tasks.py tests\python\unit\meta_learning\test_phase2_ii0c_encoder.py tests\python\unit\meta_learning\test_phase2_ii0c_comparison.py tests\python\unit\pipeline\test_ii0c_governed_artifacts.py tests\python\unit\meta_learning\test_phase2_ii0c_scaffold.py tests\python\unit\pipeline\test_phase2_ii0c_runner.py --no-cov"` — 30 passed; Windows pytest temp symlink cleanup emitted a post-run `PermissionError` after the passing result.
- `cmd.exe /c ".venv-codex\Scripts\python.exe -m pytest tests\python\unit\meta\test_phase2_artifact_contract.py tests\python\unit\gate\test_phase2_ml_evidence_shell.py tests\python\unit\pipeline\test_phase2_governed_orchestration.py --no-cov"` — 50 passed; Windows pytest temp symlink cleanup emitted a post-run `PermissionError` after the passing result.
- `cmd.exe /c ".venv-codex\Scripts\mypy.exe pysrc\meta_learning\phase2_ii0c_tasks.py pysrc\meta_learning\phase2_ii0c_encoder.py pysrc\meta_learning\phase2_ii0c_comparison.py pysrc\pipeline\ii0c_governed_artifacts.py pysrc\pipeline\phase2_ii0c_runner.py --strict --follow-imports skip"` — pass.
- `cmd.exe /c ".venv-codex\Scripts\python.exe -m py_compile pysrc\meta_learning\phase2_ii0c_tasks.py pysrc\meta_learning\phase2_ii0c_encoder.py pysrc\meta_learning\phase2_ii0c_comparison.py pysrc\pipeline\ii0c_governed_artifacts.py pysrc\pipeline\phase2_ii0c_runner.py tests\python\unit\pipeline\test_phase2_ii0c_runner.py"` — pass.

### Companion Document Versions

| Document | Version |
|---|---|
| README | v7.2.2 |
| Implementation Plan | v6.5.9 |
| Technical Roadmap | v1.4.30 |
| Meta-Learning Core | v1.2.25 |
| Meta-Learning Architecture Vision | v1.3.6 |
| Resolution Ledger | v1.0.52 |
| Phase II Artifact Contract | v1.0.3 |
| Phase II Research Execution Playbook | v1.0.2 |
| Threshold Governance Register | v1.0.3 |

Companion Markdown sources were synchronized in this pass; DOCX outputs were not regenerated.

---

## Version 7.2.1 (2026-04-17)

Changelog for the II-0B orchestration hard-gate follow-up and companion-suite patch sync.
Version: 7.2.1 (explicit fail-closed orchestration contract, borrowed-threshold lineage framing, and companion-doc patch release)

### Major Themes Across All Changes

- Canonical `pysrc/pipeline` orchestration now treats governed II-0B evidence usability as an explicit hard contract rather than merely an always-invoked side effect.
- The orchestration lane keeps borrowed `THR-RG09-V03` / `THR-RG09-V17` references, but now frames them explicitly as reviewer-visible lineage rather than native orchestration threshold policy.
- Companion truth is patched forward so the suite records the orchestration hard-gate delta consistently without changing the non-promotable boundary.

### Detailed Changes

| Subsystem | Change |
|---|---|
| `pysrc/pipeline/orchestrator.py` | Adds an explicit fail-closed wrapper around governed II-0B emission and routes both `run()` and `run_orchestration()` through the same structural-usability contract |
| `pysrc/pipeline/phase2_governed.py` | Extends the emitted orchestration summary with explicit borrowed-threshold lineage policy framing for reviewer visibility |
| `tests/python/unit/pipeline/test_phase2_governed_orchestration.py` | Adds hard-gate coverage for helper-raised failure and helper-returned non-usable governed evidence |
| `README.md` / `docs/src/README.md` | Advance current-state truth and suite versions to record the orchestration-layer fail-closed semantics and borrowed-threshold lineage framing |
| `docs/src/ImplementationPlan.md` / `docs/src/TechnicalRoadmap.md` | Patch the doctrinal II-0B closure language to record the explicit orchestration contract delta while preserving **GATE-II DEFERRED** and the non-promotable boundary |
| Companion Markdown metadata surfaces | Rebase companion headers / source stamps to README **7.2.1**, Implementation Plan **6.5.8**, Technical Roadmap **1.4.29**, and `VERSION.md` **7.2.1** |

### Behavioral Changes

- `run()` and `run_orchestration()` now halt when governed II-0B emission raises or when the helper returns non-usable governed evidence.
- Canonical orchestration now records that the orchestration lane’s borrowed RG-09 threshold IDs are lineage / reviewer-visibility references, not native pass/fail policy thresholds.
- Companion docs now describe the II-0B closure-critical delta as an orchestration hardening patch, not a new promotable capability.

### Breaking Changes

- Canonical orchestration no longer tolerates a helper-returned II-0B summary whose shell status is not `EVIDENCE_STRUCTURALLY_USABLE`.
- Reviewer interpretation should treat orchestration-lane RG-09 threshold IDs as borrowed lineage only, not as evidence of a native orchestration threshold register.

### Test / Validation Evidence

- `python -m pytest tests/python/unit/pipeline/test_phase2_governed_orchestration.py tests/python/unit/gate/test_phase2_ml_evidence_shell.py tests/python/unit/pipeline/test_orchestrator_pit.py --no-cov` — 27 passed; Windows pytest temp symlink cleanup emitted a post-run `PermissionError` after the passing result.
- `python -m py_compile pysrc/pipeline/orchestrator.py pysrc/pipeline/phase2_governed.py tests/python/unit/pipeline/test_phase2_governed_orchestration.py` — pass.

### Companion Document Versions

| Document | Version |
|---|---|
| README | v7.2.1 |
| Implementation Plan | v6.5.8 |
| Technical Roadmap | v1.4.29 |
| Meta-Learning Core | v1.2.25 |
| Meta-Learning Architecture Vision | v1.3.6 |
| Resolution Ledger | v1.0.52 |
| Phase II Artifact Contract | v1.0.3 |
| Phase II Research Execution Playbook | v1.0.2 |
| Threshold Governance Register | v1.0.3 |

DOCX outputs were not regenerated in this pass; the Markdown sources are the updated companion truth.

---

## Version 7.2.0 (2026-04-17)

Changelog for II-0B closure on the non-promotable artifact-and-contract lane.
Version: 7.2.0 (canonical orchestration rollout, governed-consumer threshold summary visibility, and stale evidence retirement)

### Major Themes Across All Changes

- Canonical `pysrc/pipeline` orchestration now emits governed II-0B evidence end-to-end instead of proving the lane only on RG-09 / OI-59 governed side entrypoints.
- Governed consumers now surface threshold-governance summary details directly, so provisional-vs-validated semantics are visible without path-dependent reviewer inference.
- II-0B evidence is structurally separated from unrelated root bundle artifacts through a dedicated `phase2_ii0b_governed_non_promotable/` subdirectory plus a root summary guardrail.
- Older root-level pre-hash triples are explicitly retired from current governed evidence; II-0B is now complete for the non-promotable artifact-and-contract lane only.

### Detailed Changes

| Subsystem | Change |
|---|---|
| `pysrc/pipeline/phase2_governed.py` | New canonical orchestration bridge for governed II-0B emission under `phase2_ii0b_governed_non_promotable/`, root summary/pointer emission, and stale-root-triple exclusion review |
| `pysrc/pipeline/orchestrator.py` | Canonical `run()` and `run_orchestration()` now emit governed II-0B evidence via the dedicated bridge without colliding with root strategy artifact names; dataprep-runtime imports are lazy-loaded so the canonical orchestration surface imports cleanly |
| `marketmind_gate/gates/phase2_ml_evidence_shell.py` | Adds stable `threshold_governance` summary output for governed-consumer visibility of lineage-bound threshold semantics |
| `pysrc/core/runtime/dependency_manager.py` | Restores the runtime dependency-manager compatibility surface expected by the current package and backend plugin tests |
| `tests/python/unit/pipeline/test_phase2_governed_orchestration.py` | New canonical orchestration rollout coverage for dedicated II-0B evidence subdirectory emission and stale-root-triple exclusion |
| `tests/python/unit/gate/test_phase2_ml_evidence_shell.py` | Adds reviewer-facing threshold-governance summary assertions for both validated and provisional governed evidence |
| Companion Markdown sources | Advance II-0B posture from “materially hardened / not exit-ready” to **II-0B COMPLETE** for the non-promotable artifact-and-contract lane while preserving **Phase II-0 open; II-0C next** |

### Behavioral Changes

- Canonical bundle-producing orchestration now emits governed II-0B artifacts under `phase2_ii0b_governed_non_promotable/` and writes a root summary guardrail file.
- Root-level bundle artifacts such as strategy-owned `execution_assumptions.json` are no longer ambiguous with II-0B governed evidence.
- `phase2_ml_evidence_shell` now returns `evidence["threshold_governance"]` with reference rows, provisional-threshold visibility, and lineage-bound consumer checks.
- The checked-in root triples at `fixtures/rg09/v2`, `runs/oi59_experiment5_branch_b`, `runs/oi59_experiment5_branch_b_v2_corrected`, `runs/rg09_h1_cross_sectional_expansion`, and `runs/rg09_h1_recovery_one_axis_boundary_v2` are explicitly treated as stale pre-hash surfaces and do not count as current governed evidence.

### Breaking Changes

- Companion truth now treats II-0B as complete only in the non-promotable artifact-and-contract sense; this does not authorize trainer, allocator, broker, rollout, or execution-serious claims.
- Current governed evidence review should follow the canonical orchestration subdirectory/pointer surface rather than inferring II-0B status from unrelated root bundle filenames.

### Test / Validation Evidence

- `python -m pytest tests/python/unit/pipeline/test_phase2_governed_orchestration.py tests/python/unit/gate/test_phase2_ml_evidence_shell.py --no-cov` — 17 passed; Windows pytest temp symlink cleanup emitted a post-run `PermissionError` after the passing result.
- `python -m pytest tests/python/unit/pipeline/test_orchestrator_pit.py tests/python/unit/test_architecture_cleanup_contracts.py --no-cov` — 19 passed; Windows pytest temp symlink cleanup emitted a post-run `PermissionError` after the passing result.

### Companion Document Versions

| Document | Version |
|---|---|
| README | v7.2.0 |
| Implementation Plan | v6.5.7 |
| Technical Roadmap | v1.4.28 |
| Meta-Learning Core | v1.2.25 |
| Meta-Learning Architecture Vision | v1.3.6 |
| Resolution Ledger | v1.0.52 |
| Phase II Artifact Contract | v1.0.3 |
| Phase II Research Execution Playbook | v1.0.2 |
| Threshold Governance Register | v1.0.3 |

DOCX outputs were not regenerated in this pass; the Markdown sources are the updated companion truth.

---

## Version 7.1.0 (2026-04-16)

Changelog for directory structure hardening with canonical package tree and typed stubs.
Version: 7.1.0 (non-breaking expansion of package surface with ABC contracts)

### Major Themes Across All Changes

- Canonical directory tree established per architecture specification.
- Typed stubs (ABCs, dataclasses, Protocols) define extension points without implementations.
- Legacy runtime modules identified for removal; clean dependency surface preserved.
- All stubs include TODO markers linking to future registry/planner/factory integration.

### Detailed Changes

| Subsystem | Change |
|---|---|
| `pysrc/ml/datasets/` | New: `DatasetBuilder` ABC, `WindowConfig` dataclass, `timeseries.py` module for time-series dataset construction |
| `pysrc/domain/portfolio/` | New: `PortfolioService` ABC with `Position`, `PortfolioSnapshot`, `ConstraintValidator` contracts |
| `pysrc/domain/risk/` | New: `RiskService` ABC with `RiskMetrics`, `RiskLimit` dataclasses for risk measurement and limit validation |
| `pysrc/autotune/` | New: `AutotuneAPI` ABC with `AutotuneConfig`, `ObjectiveFn` Protocol for hyperparameter search coordination |
| `pysrc/bridge/dataprep_orchestrator.py` | New: `DataprepOrchestrator` ABC with `DataprepSpec`, `DataprepResult` for Python/Java bridge |
| `pysrc/tuning/hparam_search.py` | New: `HparamSearch` and `SearchAlgorithm` ABCs with `Trial`, `SearchState` dataclasses |
| `pysrc/models/bayesian_nn.py` | Added: `BayesianNN` ABC stub |
| `pysrc/models/custom_models.py` | Added: `CustomModel` ABC stub |
| `pysrc/models/gnn_model.py` | Added: `GNNModel` ABC stub |
| `pysrc/models/hybrid_model.py` | Added: `HybridModel` ABC stub |
| `pysrc/models/regime_detector.py` | Added: `RegimeDetector` ABC stub |
| `pysrc/models/tcn_model.py` | Added: `TCNModel` ABC stub |
| `pysrc/models/train_model.py` | Added: `ModelTrainer` ABC with `TrainConfig` dataclass |
| `pysrc/models/transformer_model.py` | Added: `TransformerModel` ABC stub |
| `pysrc/models/ensemble/ensemble_model.py` | Added: `EnsembleModel`, `EnsembleStrategy` ABCs |
| `pysrc/models/ensemble/__init__.py` | Added: Package init |
| `pysrc/models/__init__.py` | Added: Package init |
| `pysrc/data/order_book.py` | Added: `OrderBook` ABC with `PriceLevel` dataclass |
| `pysrc/data/satellite_data.py` | Added: `SatelliteDataProvider` ABC with `SatelliteDataSpec` |
| `pysrc/data/weather_data.py` | Added: `WeatherDataProvider` ABC with `WeatherDataSpec` |
| `pysrc/bridge/__init__.py` | Updated: Package init with ownership docs |
| `pysrc/backtesting/__init__.py` | Updated: Package init |
| `pysrc/backtesting/api.py` | Updated: `BacktestAPI` ABC with `BacktestSpec`, `BacktestResult` |
| `pysrc/preprocessor/__init__.py` | Updated: Package init |
| `pysrc/pipeline/__init__.py` | Updated: Package init |
| `pysrc/cli/__init__.py` | Updated: Package init |
| `pysrc/infra/brokers/ibkr/__init__.py` | Updated: Package init |
| `pysrc/ml/__init__.py` | Updated: Package init |
| `pysrc/core/runtime/__init__.py` | Updated: Removed dependency_manager imports; exports only from `optional_imports` |

### Behavioral Changes

- All new modules use `from __future__ import annotations` for forward compatibility.
- Dataclasses use `frozen=True, slots=True` for immutability and memory efficiency.
- ABCs define abstract methods only; no placeholder implementations.
- TYPE_CHECKING guards prevent circular imports for optional dependencies.

### Breaking Changes

None. This is a pure addition release. Legacy files (`dependency_manager.py`, `import.py`) remain in filesystem pending manual deletion; they are no longer imported.

### Test / Validation Evidence

- `python -m py_compile pysrc/ml/datasets/timeseries.py pysrc/domain/portfolio/service.py pysrc/domain/risk/service.py pysrc/autotune/api.py pysrc/bridge/dataprep_orchestrator.py pysrc/tuning/hparam_search.py` — pass.
- `python -m py_compile pysrc/models/bayesian_nn.py pysrc/models/custom_models.py pysrc/models/gnn_model.py pysrc/models/hybrid_model.py pysrc/models/regime_detector.py pysrc/models/tcn_model.py pysrc/models/train_model.py pysrc/models/transformer_model.py pysrc/models/ensemble/ensemble_model.py` — pass.
- `python -m py_compile pysrc/data/order_book.py pysrc/data/satellite_data.py pysrc/data/weather_data.py` — pass.
- `python -m py_compile pysrc/core/runtime/__init__.py` — pass.

### Deferred

- Manual deletion of `pysrc/core/runtime/dependency_manager.py` and `import.py` pending separate cleanup commit.
- Stubs intentionally omit implementations; actual logic to be added in feature-specific releases.

### Release Artifacts

- Trace: `docs/traces/7.1.0_implementation_trace.md`
- Manifest: `docs/manifests/7.1.0_change_manifest.json`

---

## Version 6.2.2 (2026-04-14)

Changelog for companion-document synchronization and DOCX CI repair after II-0A CI confirmation.
Version: 6.2.2 (companion sync plus release-docs repair)

### Major Themes Across All Changes

- WS-1, WS-2, WS-3, and II-0A are now recorded as complete in companion truth.
- The strict-H3 RG-09 reference anchor remains the task-validity / harness-reproducibility anchor only.
- The Phase II challenger-vs-incumbent baseline boundary remains explicit: predicates must reference the XGBoost incumbent, not the RG-09 anchor.
- The `build-docx-suite` CI path no longer fails on stale string-rewrite typo references to `copysrc`.
- The 6.2.2 release manifest now plans from an explicit 6.2.1 base manifest, preventing companion version fallback to `1.0.0`.

### Detailed Changes

| Subsystem | Change |
|---|---|
| `docs/src/ResolutionLedger.md` | Advanced to v1.0.51 and recorded external CI confirmation plus supportable `II-0A COMPLETE` posture |
| `docs/src/ImplementationPlan.md` | Advanced to v6.5.5; §1.2 and §4.2 now state WS-1 / WS-2 / WS-3 complete and II-0A complete |
| `docs/src/README.md` | Advanced to v6.2.2 and current-state bullets now include II-0A completion |
| `docs/src/TechnicalRoadmap.md` | Advanced to v1.4.26 and roadmap checkpoints now mark II-0A reference/diagnostic integration complete |
| `docs/src/MetaLearningCore.md` | Advanced to v1.2.24 and baseline framing now points to `VERSION.md` 6.2.2 / Ledger v1.0.51 |
| `docs/src/MetaLearningArchitectureVision.md` | Advanced to v1.3.5 and §13.2 now includes the II-0A reference anchor row |
| `devtools/docs/rendering/post_process.py` | Fixed stale `copysrc.deepcopy` typo to use the imported `copy` module during DOCX callout post-processing |
| `tests/python/infra/adaptive_matrix.py` | Fixed stale `copysrc.deepcopy` typo to use the imported `copy` module in adaptive matrix normalization |
| `docs/releases/6.2.1.yml` | Added the missing prior release manifest anchor so 6.2.2 planning keeps correct companion versions |
| `docs/releases/6.2.2.yml` / `docs/out/6.2.2/` | Regenerated release manifest and DOCX suite through `docs/release-docs.ps1 all` |

### Behavioral Changes

- DOCX release generation no longer raises `NameError: name 'copysrc' is not defined`.
- Runtime trading behavior is unchanged.

### Breaking Changes

None.

### Test / Validation Evidence

- `rg -n "6\\.1\\.0|v1\\.0\\.48|VERSION\\.md 6\\.2\\.1|README\\.md 6\\.1\\.0" docs/src/README.md docs/src/ImplementationPlan.md docs/src/TechnicalRoadmap.md docs/src/MetaLearningCore.md docs/src/MetaLearningArchitectureVision.md docs/src/ResolutionLedger.md` — no stale companion stamp matches.
- `rg -n "WS-1 COMPLETE|WS-2 COMPLETE|WS-3 COMPLETE|II-0A COMPLETE|run_bundles/rg09_reference_v1|sha256:caac0778c33c580e90e992bc612c9a1447241f5009fb0603f7ced79bd7618f5d" docs/src/README.md docs/src/ImplementationPlan.md docs/src/TechnicalRoadmap.md docs/src/MetaLearningCore.md docs/src/MetaLearningArchitectureVision.md docs/src/ResolutionLedger.md VERSION.md` — expected completion and anchor references present.
- `python3 -m json.tool docs/manifests/6.2.2_change_manifest.json` — pass.
- `PYTHONPYCACHEPREFIX=/tmp/marketmind_pycache python3 -m py_compile devtools/docs/rendering/post_process.py tests/python/infra/adaptive_matrix.py` — pass.
- `cmd.exe /c "powershell -ExecutionPolicy Bypass -File docs\release-docs.ps1 all -Version 6.2.2 -SkipPrepare"` — pass; `build-docx-suite` rendered 2 of 2 Mermaid diagrams and `verify-suite` reported `Suite verified OK`.

### Companion Document Versions

| Document | Version |
|---|---|
| README | v6.2.2 |
| Implementation Plan | v6.5.5 |
| Technical Roadmap | v1.4.26 |
| Meta-Learning Core | v1.2.24 |
| Meta-Learning Architecture Vision | v1.3.5 |
| Resolution Ledger | v1.0.51 |

### Release Artifacts

- Trace: `docs/traces/6.2.2_implementation_trace.md`
- Manifest: `docs/manifests/6.2.2_change_manifest.json`

---

## Version 6.2.1 (2026-04-14)

Changelog for II-0A WS-1 reference freeze and WS-3 join-point registration.
Version: 6.2.1 (strict-H3 RG-09 reference anchor plus task-validity integration record)

### Major Themes Across All Changes

- Frozen RG-09 task-validity anchor derived from the existing strict-H3 successor surface.
- Reproduction verifier and CI drift workflow for the reference payload hash.
- WS-3 diagnostic report generated against the frozen reference bundle.
- Resolution Ledger registration preserving the boundary between the RG-09 reference anchor and the future XGBoost incumbent comparison baseline.

### Detailed Changes

| Subsystem | Change |
|---|---|
| `run_bundles/rg09_reference_v1/` | New frozen RG-09 reference bundle with Appendix-C-style sidecars, task-validity inputs, manifest, and generated `task_validity_report.json` |
| `scripts/reproduce_rg09_reference.py` | New no-argument verifier that recomputes the reference payload hash, checks pinned manifest fields, and exits nonzero with a diff report on drift |
| `.github/workflows/rg09_reference_drift.yml` | New GitHub Actions workflow that runs the reproduction verifier on `main` pushes and relevant PR changes |
| `tests/python/integration/test_rg09_reference_reproduction.py` | New D1 integration tests for manifest hash agreement and perturbation detection |
| `docs/src/ResolutionLedger.md` | Updated RG-09 posture with the frozen reference hash, diagnostic version, integration result, control results, and baseline-identity warning |
| `pysrc/tuning/_facade.py` and `pysrc/ops/hashing/primitives/hmac_sha256_impl.py` | Corrected stale migration typos from `numpysrc` / historical `py/` doc references to current names |

### Behavioral Changes

- `scripts/reproduce_rg09_reference.py` returns 0 when the frozen reference payload matches
  `rg09_reference_manifest.json` and returns 1 when a defining parameter or payload file
  drifts.
- The RG-09 reference anchor is explicitly identified as
  `surface_role: "rg09_task_validity_anchor"` and not as the Phase II allocator incumbent.
- `run_bundles/rg09_reference_v1/task_validity_report.json` records `all_pass: true` for
  TV-01, TV-02, and TV-03 against the frozen strict-H3 bundle.

### Breaking Changes

None.

### Test / Validation Evidence

- `python3 scripts/reproduce_rg09_reference.py` — pass, hash `sha256:caac0778c33c580e90e992bc612c9a1447241f5009fb0603f7ced79bd7618f5d`.
- Perturbation check: changed `vol_window` from `120` to `121`; `scripts/reproduce_rg09_reference.py` exited 1 with hyperparameter and hash mismatches; reverted to `120`; clean reproduction passed.
- `cmd.exe /c C:/Users/Nalakram/Documents/GitHub/MarketMind/.venv-codex/Scripts/python.exe -m pytest tests/python/integration/test_task_validity.py tests/python/integration/test_rg09_reference_reproduction.py --no-cov` — 8 passed; Windows pytest temp symlink cleanup emitted a post-run `PermissionError` after the passing result.
- `PYTHONPYCACHEPREFIX=/tmp/marketmind_pycache python3 -m py_compile scripts/reproduce_rg09_reference.py tests/python/integration/test_rg09_reference_reproduction.py` — pass.
- Remote GitHub CI dashboard status could not be asserted locally: GitHub commit-status access returned 403 for the installed connector, `gh` is unavailable in this environment, and the new workflow will not run until these changes are pushed.

### Companion Document Versions

| Document | Version |
|---|---|
| Agent Artifact Release Protocol | v3 (unchanged) |
| Resolution Ledger | v1.0.50 |

### Release Artifacts

- Trace: `docs/traces/6.2.1_implementation_trace.md`
- Manifest: `docs/manifests/6.2.1_change_manifest.json`

---

## Version 6.2.0 (2026-04-14)

Changelog for II-0A WS-2 task-validity diagnostic harness and package-root alignment.
Version: 6.2.0 (new schema-validated validation diagnostic under `pysrc.validation`)

### Major Themes Across All Changes

- New callable diagnostic for run-bundle task validity.
- Schema-validated report contract for `task_validity_report` payloads.
- Synthetic positive and negative controls proving clean pass and TV-02 leakage failure.
- RG-09 / II-0A ledger posture updated without closing RG-09 or recording WS-3 results.

### Detailed Changes

| Subsystem | Change |
|---|---|
| `pysrc/validation/task_validity.py` | New: `validate_task(bundle_path)`, `TaskValidityReport`, `TaskValidityCheck`, and independently callable TV-01 / TV-02 / TV-03 checks |
| `schemas/task_validity_report.schema.json` | New JSON Schema for `task_validity_report` payloads, including `bundle_hash`, per-check pass/fail evidence, `all_pass`, diagnostic version, and timestamp |
| `tests/fixtures/bundles/valid_synthetic/` | New positive control bundle that passes TV-01, TV-02, and TV-03 |
| `tests/fixtures/bundles/injected_leakage/` | New negative control bundle with intentional `tomorrow_return` lookahead leakage; fails TV-02 with explicit leakage evidence |
| `tests/python/integration/test_task_validity.py` | New D1 integration tests for positive control, negative control, schema validation, independently callable checks, missing timestamp provenance, and TV-03 gap-unit evidence |
| `docs/src/ResolutionLedger.md` | Updated RG-09 / II-0A posture to record WS-2 diagnostic readiness without closing RG-09 or registering the WS-3 join-point result |

### Behavioral Changes

- TV-01 computes an empirical right-tail permutation p-value from bundle-provided
  observed/null statistics; the p-value threshold and threshold source are required bundle
  evidence and are not hardcoded in the diagnostic.
- TV-02 fails any feature with positive `lookahead_bars` and reports leaking feature names,
  lookahead distance, and boundary.
- TV-03 reads `purge_window` and `embargo_window` from `splits_manifest.json`, preserving the
  existing run-bundle contract. Evidence reports raw seconds separately from day-equivalent
  values because the current manifest windows are interpreted as days.
- Missing or malformed `plan.json as_of_time` now fails closed instead of returning a
  schema-valid Unix epoch timestamp.
- The diagnostic validates its own report against
  `schemas/task_validity_report.schema.json` before returning.

### Breaking Changes

None.

### Test / Validation Evidence

- `cmd.exe /c C:/Users/Nalakram/Documents/GitHub/MarketMind/.venv-codex/Scripts/python.exe -m pytest tests/python/integration/test_task_validity.py --no-cov` — 6 passed.
- `cmd.exe /c C:/Users/Nalakram/Documents/GitHub/MarketMind/.venv-codex/Scripts/python.exe -m mypy pysrc/validation/task_validity.py --strict` — pass.
- `cmd.exe /c C:/Users/Nalakram/Documents/GitHub/MarketMind/.venv-codex/Scripts/python.exe -m compileall -q pysrc/validation tests/python/integration/test_task_validity.py` — pass.

### Companion Document Versions

| Document | Version |
|---|---|
| Agent Artifact Release Protocol | v3 (unchanged) |
| Resolution Ledger | v1.0.49 |

### Deferred

- WS-3 must run `validate_task()` against the frozen RG-09 reference bundle from WS-1 and
  record any joined result. This release only proves the diagnostic against synthetic
  positive and negative controls.

### Release Artifacts

- Trace: `docs/traces/6.2.0_implementation_trace.md`
- Manifest: `docs/manifests/6.2.0_change_manifest.json`

---

## Version 6.1.0 (2026-04-14) — Tuning surface consolidation

### Summary

Consolidates five parallel tuning surfaces (`pysrc.autotune`, `pysrc.tuning.grid_search`,
`pysrc.tuning.random_search`, `pysrc.tuning.bayesian_optimization`, and the legacy
`hparam_search` utilities) into a single registry-driven `pysrc.tuning` package with
one canonical public entry-point. All legacy surfaces deleted; no compatibility shims remain.

### Major Themes Across All Changes

- One canonical public API: `tune(objective_fn, space, engine=..., direction=..., budget=..., seed=...)`.
- Schema-first typed boundary layer: `TunerSpec` (frozen), `TuningResult` (frozen), `TrialRecord` (frozen), `SearchSpace`.
- Registry-driven engine dispatch: `EngineRegistry` singleton; four engines (`grid`, `random`, `bayes`, `optuna`); optional deps guarded at call time.
- Unified direction semantics: `spec.direction: Literal["maximize","minimize"]` is the single source of truth for all engines; no engine infers direction independently.
- Adapters own boundary translation only; engines own compute logic only.

### Detailed Changes

| Subsystem | Change |
|---|---|
| `pysrc/tuning/specs.py` | New: `TunerSpec`, `TuningResult`, `TrialRecord`, `ObjectiveDirection`, `ParamPoint`, `ParamValue`, `TuningEngine` Protocol |
| `pysrc/tuning/space.py` | New: `SearchSpace`, `normalize_space()` accepting dict-of-lists, dict-of-tuples, mixed, and list-of-dicts YAML formats; `iter_grid()`, `sample()`, `to_optuna_space()`, `to_skopt_space()` |
| `pysrc/tuning/result.py` | New: `TuningError`, `EngineNotAvailableError(engine, package)` with `pip install` message, `best_trial()`, `merge_metadata()` |
| `pysrc/tuning/registry.py` | New: `EngineRegistry` singleton; lazy loaders for `grid`, `random`, `bayes`, `optuna`; `register()` / `get()` / `available()` |
| `pysrc/tuning/_facade.py` | New: `tune()` (5-step dispatch: normalise → spec → registry → factory → result), `create_tuner()` (eager engine validation, spec-bound callable) |
| `pysrc/tuning/engines/grid.py` | New: exhaustive Cartesian enumeration; seed ignored (deterministic by construction) |
| `pysrc/tuning/engines/random.py` | New: uniform sampling via `random.Random(seed)` — never touches global RNG |
| `pysrc/tuning/engines/bayes.py` | New: `skopt.gp_minimize` functional API; import deferred to `run()` body; score negated for maximize direction |
| `pysrc/tuning/engines/optuna.py` | New: Optuna TPE; import deferred to `run()` body; `spec.direction` passed directly to `create_study()` |
| `pysrc/tuning/adapters/sklearn.py` | Replaced: three separate sklearn wrappers → single `tune_estimator()` using `cross_val_score` closure + `dataclasses.replace` for `best_model` |
| `pysrc/tuning/adapters/objective.py` | Replaced: `autotune()` delegation → `tune_objective()` thin wrapper |
| `pysrc/tuning/adapters/legacy_yaml.py` | New: `parse_yaml_grid()` replacing `parameter_grid_iter` + `_categorical_values_from_grid` |
| `pysrc/tuning/__init__.py` | Updated: canonical re-export of all public symbols |

### Behavioral Changes

- `pysrc.autotune.autotune()` — deleted; maximise-by-default behaviour preserved via `tune(..., direction="maximize")`.
- `run_grid_search` / `run_random_search` / `run_bayes_search` — deleted; replaced by `tune_estimator(engine=...)`.
- `SearchSpace.to_skopt_space()` raises `ImportError` (not logs a warning) when skopt is absent.
- `bayes` and `optuna` engines raise `EngineNotAvailableError` at call time when optional deps are absent; importing `pysrc.tuning` never fails due to missing optional deps.

### Breaking Changes

- `pysrc.autotune.autotune()` and `pysrc.autotune.AutoTuner` deleted — use `tune()` or `tune_objective()`.
- `pysrc.tuning.grid_search.run_grid_search()` deleted — use `tune_estimator(engine="grid")`.
- `pysrc.tuning.random_search.run_random_search()` deleted — use `tune_estimator(engine="random")`.
- `pysrc.tuning.bayesian_optimization.run_bayes_search()` deleted — use `tune_estimator(engine="bayes")`.
- All corresponding `stubs/py/` type stubs deleted.

All callers within the monorepo migrated in this release; no external consumers.

### Test / Validation Evidence

- `pytest tests/python/unit/tuning/ tests/python/test_autotune_contracts.py` — 32 passed, 2 skipped (sklearn absent in test env).
- Import smoke: `from pysrc.tuning import tune, TunerSpec, TuningResult, SearchSpace, EngineRegistry` — pass.
- Functional smoke: `tune(lambda p: -(float(p["x"])-2)**2, {"x":[0,1,2,3,4]}, engine="grid", direction="maximize")` → `best_params={"x":2}` — pass.
- Legacy import scan: `grep -r "from pysrc.autotune|from pysrc.tuning.grid_search|..."` — no matches in `pysrc/` or `tests/`.

### Companion Document Versions

| Document | Version |
|---|---|
| Agent Artifact Release Protocol | v3 (unchanged) |
| Resolution Ledger | v1.0.46 (unchanged — no new decisions) |

### Deferred

- `_facade.py` rename to `api.py`: blocked by `pysrc/tuning/api/` directory from concurrent refactor; deferred to next tuning increment.
- `stubs/py/tuning/__init__.pyi` sync to `pysrc.` import paths: deferred to stub-sync release.

### Release Artifacts

- Trace: `docs/traces/6.1.0_implementation_trace.md`
- Manifest: `docs/manifests/6.1.0_change_manifest.json`

---

## Version 6.0.0 (2026-04-13) — Domain package migration and `py.utils` retirement

### Summary

This release moves implementation code out of `py.utils` into canonical domain packages and
intentionally removes the old `py.utils.*` import contract. It is a SemVer major release because
downstream callers must retarget imports and no compatibility shims remain.

### Major Changes

- Runtime/platform support moved to `py.core.runtime`.
- Exceptions moved to `py.core.errors`.
- Validators moved to `py.core.validation`.
- Dataframe, dataset, and calendar helpers moved to `py.data.frames`, `py.data.datasets`, and
  `py.data.calendars`.
- Statistical tests moved to `py.analytics.statistics`.
- Torch runtime helpers moved to `py.ml.runtime.torch`.
- Tuning support remains canonical at `py.tuning`; no `py.ml.tuning` package was introduced.
- Pipeline configuration ownership moved to `py.pipeline.pipeline_config`.
- `docs/Artifact Write Contract.md` now includes mandatory SemVer classification guidance.
- `mypy py --strict` passes.

### Breaking Changes

- `py.utils.exceptions` → `py.core.errors`
- `py.utils.validators` → `py.core.validation`
- `py.utils.dependency_manager` → `py.core.runtime.dependency_manager`
- Legacy utility runtime capability and optional import helpers are removed; use direct `py.core.runtime.dependency_manager` lookups.
- `py.utils.config` → `py.pipeline.pipeline_config`
- `py.utils.dataframe_helpers` → `py.data.frames.dataframe_helpers`
- `py.utils.dataset_builders` → `py.data.datasets.builders`
- `py.utils.holidays` → `py.data.calendars.holidays`
- `py.utils.stat_tests` → `py.analytics.statistics`
- `py.utils.torch_utils` → `py.ml.runtime.torch`
- `py.utils.hparam_search` is retired into the canonical `py.tuning` subsystem.

### Validation Summary

- `mypy py --strict` — pass, 424 source files checked.
- `mypy py\core\validation --strict` — pass.
- `mypy py\analytics\statistics --strict` — pass.
- `mypy py\ml\runtime --strict` — pass.
- `mypy py\tuning --strict` — pass.
- `compileall -q py\core py\analytics py\ml\runtime py\tuning py\cli\preprocess.py` — pass.
- `rg -n "py\.utils|py/utils" py scripts tests/python -g '*.py'` — pass, no matches.

Full pytest was not run because the local environment still has the pre-existing `py.path`
compatibility issue caused by repo package shadowing.

### Release Artifacts

- Trace: `docs/traces/6.0.0_implementation_trace.md`
- Manifest: `docs/manifests/6.0.0_change_manifest.json`
- Full entry: `docs/releases/VERSION_6.x.md`

## Version 5.1.0 (2026-04-12) — Kotlin bridge migration and Python shim removal

See full entry in `docs/releases/VERSION_5.x.md`.

## Version 5.0.0 (2026-04-12) — Repository layout: `py/` + `java/src/`

See full entry in `docs/releases/VERSION_4.x.md`.
