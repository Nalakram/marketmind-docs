# Version History

This file serves as the project's release ledger and architecture evolution.
For a traditional short-form change summary, see commit history.

Older release entries are archived in `docs/releases/`.

---

## Version Index

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
