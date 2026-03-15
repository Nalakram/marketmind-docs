# Version History

This file serves as the project's release ledger and architecture evolution.
For a traditional short-form change summary, see commit history.

Older release entries are archived in `docs/releases/`.

---

## Version Index

### 4.x — ADR-007 Hashing Contract + Phase I PIT Feature Hardening
- 4.4.1 — companion-doc synchronization for delivered Phase I-C / I-D state
- 4.4.0 — Phase I-D stat-arb pairs vertical slice (governed graph ops, thin entry → orchestrator, bundle artifacts)
- 4.3.0 — Phase I-C feature-path integrity and canonical governed execution lock (single-path feature materialization)
- 4.2.0 — Phase I-B source adaptation into the PIT contract (bitemporal sources, Yahoo/FRED PIT-ready)
- 4.1.0 — Phase I-A PIT orchestration closure at canonical backtest boundary
- 4.0.1 — explicit absolute imports for hashing, artifact-registry, and backtesting contracts
- 4.0.0 — ADR-007 hashing contract scaffold, golden-vector layout, artifact-registry attestation facade, D-tier terminology lock

### 3.x — Governed Research System
- 3.8.x — backtesting substrate scaffold and companion-suite synchronization
- 3.7.x — ADR-005 orchestration structure and Phase I-A PIT core / boundary delivery
- 3.6.x — CAS identity, RunRegistry, reconstructible bundles, and deterministic testing infrastructure
- 3.3–3.5 — end-to-end vertical slice, reliability hardening, and architecture clarification
- 3.0–3.2 — pipeline-core reset, executor guardrails, and leakage-safe research primitives

### 2.x — GPU Graph Preprocessor Era
- 2.0.0 — GPU-accelerated graph pipeline stack

### 1.x — Early ML / Infra Exploration
- 1.15.0 — torch utils refactor
- 1.14.x — logging + market data hardening
- 1.13.x — LSTM stack + test modernization
- 1.10–1.12 — model experimentation, indicators, and pipeline scaffolding
- 1.6–1.9 — early system expansion: Java UI, model training, data ingestion

---

## Era Map

| Era | Versions | Focus |
|-----|----------|------|
| ADR-007 Hashing + Phase I PIT | 4.x | ADR-007 hashing/attestation, golden-vector layout; Phase I PIT orchestration (4.1), source adaptation (4.2), governed feature path (4.3), stat-arb pairs vertical slice (4.4) |
| Governed Artifact System | 3.6.x | CAS storage, RunRegistry, deterministic bundle identity |
| Contract-Driven Execution | 3.5–3.6 | strategy bridge, artifact gates, determinism tiers |
| Reliability Hardening | 3.4.x | coverage push, integration stabilization |
| Operational Vertical Slice | 3.3.x | UI → pipeline → backtest → gate → bundle workflow |
| Leakage-Safe Research | 3.2.x | purged splits, embargo windows, leakage invariants |
| Execution Infrastructure | 3.1.x | executor routing, registry contracts, guardrails |
| Pipeline Core Architecture | 3.0.x | modular pipeline core, registry split, structural refactor |
| GPU Graph Pipeline Platform | 2.x | graph executor, backend registry, GPU preprocessing stack |
| ML Research Prototype | 1.x | model experimentation, data ingestion, logging infrastructure |

---

## Version 4.4.1 (2026-03-14)

Changelog for **companion documentation synchronization through the delivered 4.3.0 and 4.4.0 Phase I milestones**: `docs/src/ImplementationPlan.md`, `TechnicalRoadmap.md`, `README.md`, `MetaLearningCore.md`, `MetaLearningArchitectureVision.md`, and `WhitePaper.md` now describe Phase I-C as delivered (single-path governed feature execution, canonical op-floor expansion, and feature-layer leakage evidence) and Phase I-D as delivered (`stat_arb_pairs` on the canonical PIT-safe path with `execution_assumptions.json` and `stat_validity_report.json` emitted in the run bundle). This is a PATCH release because it updates companion documentation and release metadata only; no runtime behavior, contracts, schemas, or public APIs change.

### Detailed Changes

| Location | Change |
|----------|--------|
| `docs/src/ImplementationPlan.md` | Updated the executive summary, codebase reality map, Phase I-C / I-D status, and source stamp to reflect the delivered 4.3.0 / 4.4.0 state instead of treating those milestones as future work. |
| `docs/src/TechnicalRoadmap.md` | Updated feature inventory and PIT status language to record the delivered canonical op floor, governed feature-path lock, and live `stat_arb_pairs` vertical slice. |
| `docs/src/README.md` | Bumped companion metadata to 4.4.0, refreshed the current-status narrative, and replaced outdated `stat_arb.py` / Phase I future-state wording with the live `stat_arb_pairs` path. |
| `docs/src/MetaLearningCore.md` | Refreshed companion references and Phase I prerequisite language so the meta-learning docs assume the delivered Phase I-C / I-D substrate. |
| `docs/src/MetaLearningArchitectureVision.md` | Extended the post-3.6.0 architecture addendum through 4.4.0, including ADR-008 acceptance and the canonical stat-arb package spine. |
| `docs/src/WhitePaper.md` | Refreshed companion metadata and current-state language so Phase I-C and the first Phase I-D strategy slice are recorded as delivered. |

### Behavioral Changes

None. This release updates documentation only.

### Companion Document Versions

| Document | Previous | New |
|---|---|---|
| `docs/src/README.md` | 4.2.0 | 4.4.0 |
| `docs/src/ImplementationPlan.md` | Synced through 4.2.0 | Synced through 4.4.0 |
| `docs/src/TechnicalRoadmap.md` | Synced through 4.2.0 | Synced through 4.4.0 |
| `docs/src/MetaLearningCore.md` | Companion refs through 4.2.0 | Companion refs through 4.4.0 |
| `docs/src/MetaLearningArchitectureVision.md` | Post-3.6.0 addendum through 4.2.0 | Post-3.6.0 addendum through 4.4.0 |
| `docs/src/WhitePaper.md` | Current-state language through 4.2.0 | Current-state language through 4.4.0 |

### Deferred

* No code-path changes are included in 4.4.1; Phase I-E / I-F implementation work remains governed by subsequent releases.

## Version 4.4.0 (2026-03-14) Phase I-D stat-arb pairs

Changelog for **Phase I-D stat-arb vertical slice on canonical PIT-safe plumbing**: the preprocessor graph now has executable Polars lowerings for `pairs.beta`, `pairs.spread`, and `stats.half_life`, wired through the ADR-001 graph executor path; a new `srcPy/strategies/stat_arb/` package implements `StatArbPairsStrategy(PipelineStrategy)` with a frozen `PairsConfig` (including `hedge_estimator`) and a thin `entry.run_stat_arb_pairs()` wrapper that assembles PIT-safe `StrategyContext` inputs from `DataView` / `DataViewAsOfAdapter` / `PITSafeDataView`. The `stat_arb_pairs` strategy key resolves via `StrategyRegistry` to `srcPy.strategies.stat_arb.pairs.StatArbPairsStrategy`, features are materialized exclusively via `_OP_REGISTRY` graph ops, and the governed path emits both `execution_assumptions.json` and `stat_validity_report.json` into the canonical run bundle. Deterministic unit/bridge tests cover the new lowerings and strategy wiring, and an opt-in `@pytest.mark.net` Yahoo SPY/QQQ smoke test validates the live PIT-safe source path for 2022.

Phase I-Db follow-on work now also lands in the 4.4.0 line: `srcPy/strategies/stat_arb/` has been reshaped into the canonical long-term package spine with a live `common/` subtree for pairs-safe helpers, placeholder-only `artifacts/`, explicit deferred root stubs (`formation.py`, `signal_ops.py`, `risk_gates.py`, `validators.py`), and future-facing `dimensions/` / `control/` scaffolds that are import-safe and fail closed on use. The live pairs runtime remains rooted in `srcPy.strategies.stat_arb.pairs`, lazy strategy loading now imports that canonical module path directly, coverage omits exclude scaffold-only files, and a structural package-spine smoke test locks the live-versus-deferred boundary without broadening runtime behavior.

### Major Themes Across All Changes

* **Governed stat-arb execution now has a canonical pairs slice:** Phase I-D keeps `pairs.py` as the only executable stat-arb strategy and routes registry resolution to `srcPy.strategies.stat_arb.pairs.StatArbPairsStrategy`.
* **Phase I-Db package growth no longer requires a later migration:** the stat-arb slice now has its canonical `common/`, `artifacts/`, `dimensions/`, and `control/` package spine while preserving the current pairs-only execution boundary.
* **Deferred boundaries are explicit and fail closed:** future multileg, control, and reporting modules import safely, avoid registration side effects, and raise `NotImplementedError` on concrete use.
* **Phase I-D runtime:** Entry is a thin wrapper delegating to `orchestrator.run()`; graph lowerings for `pairs.beta`, `pairs.spread`, and `stats.half_life` execute via the canonical op registry; gate_status is computed from half-life band and signal count; schema_version unified to `"1.0"` in artifact payloads.

### Detailed Changes

| Location | Change |
|----------|--------|
| `srcPy/preprocessor/graph/ops_custom.py` | Phase I-D: Implemented Polars lowerings for `pairs.beta` (rolling OLS), `pairs.spread`, and `stats.half_life` (AR(1) half-life, clamp [1, 252]); PairBeta default method `ols`. |
| `srcPy/data/dataview_asof_adapter.py` | Phase I-D: Added `as_wide_frame(knowledge_dates)` returning one row per date with both legs’ close columns for PIT-safe pair join. |
| `srcPy/pipeline/orchestrator.py` | Phase I-D: Added generic `run(strategy_id, ctx, strategy_kwargs, bundle_dir, ...)` for engine resolution, bundle writing, and validator coordination; entry delegates here. |
| `srcPy/strategies/stat_arb/entry.py` | Phase I-D: Thin wrapper only—registers sources, builds adapter and wide frame, sets `pit_provenance`, delegates to `orchestrator.run()`; no direct engine/validator/manifest logic. |
| `srcPy/backtesting/storage/bundle_writer.py` | Phase I-D: Added read helpers (`read_plan`, `read_env_fingerprint`, `read_dataset_manifest`, `read_preprocessing_report`, `read_splits_manifest`) for RunBundle construction. |
| `srcPy/cli/gate.py` | Phase I-D: `stat_validity_report.json` schema_version accepts `"1.0"` or `"v1"` for gate compatibility. |
| `srcPy/strategies/stat_arb/common/` | Added the live pairs-safe helper subtree with canonical column-name types, feature-contract checks, and diagnostics/payload builders used by the current pairs runtime without introducing a second execution path. |
| `srcPy/strategies/stat_arb/artifacts/` | Replaced the flat `artifacts.py` module with a placeholder-only package containing import-safe schema and signal-card stubs for future reporting work. |
| `srcPy/strategies/stat_arb/dimensions/`, `srcPy/strategies/stat_arb/control/`, `srcPy/strategies/stat_arb/formation.py`, `srcPy/strategies/stat_arb/signal_ops.py`, `srcPy/strategies/stat_arb/risk_gates.py`, `srcPy/strategies/stat_arb/validators.py` | Added explicit deferred Phase I-Db / Phase II scaffolds that import safely, avoid registration side effects, and raise `NotImplementedError` on concrete use. |
| `srcPy/strategies/stat_arb/pairs.py`, `srcPy/strategies/stat_arb/__init__.py`, `srcPy/strategies/pipeline_strategy.py` | Kept the live pairs runtime rooted at `srcPy.strategies.stat_arb.pairs`, moved registration to the canonical module for lazy lookup, limited package-root exports to live surfaces, and preserved the `stat_arb_pairs` registry key without registering deferred scaffolds. |
| `tests/python/unit/preprocessor/test_expr_ops_executor.py` | Phase I-D: Numeric correctness for `pairs.beta` (a=2*b → beta ≈ 2.0) and `stats.half_life` ([1, 252]); PairBeta method `ols`; lowering error paths (missing columns, tiny input); constant-b denom=0; PairSpread explicit beta_col; RollingZ validation. |
| `tests/python/unit/strategies/test_stat_arb_pairs_strategy.py` | Phase I-D: features_plan op order, generate_signal discrete {-1,0,+1}, KALMAN guard; behavior tests (entry on low/high z-score, exit on mean reversion, max_hold, half-life filter blocks/allows); generate_signal TypeError/ValueError; write_artifacts branches (None signals/feats, missing z/hl columns, empty valid_hl). |
| `tests/python/integration/test_stat_arb_vertical_slice.py` | Phase I-D: Deterministic PIT-safe path and artifact emission; opt-in `@pytest.mark.net` Yahoo SPY/QQQ smoke; entry validation (run_cfg.prices required, symbol/valid_time/knowledge_time, knowledge_dates from iso string, default bundle_dir). |
| `pyproject.toml` | Added coverage omissions for scaffold-only stat-arb files so Phase I-Db placeholders do not weaken the live coverage contract. |
| `tests/python/unit/strategies/test_stat_arb_package_spine.py` | Added a D0 structural smoke test covering package import safety, root live exports, deferred module import safety, and explicit stub failures on invocation. |

### Behavioral Changes

* The stat-arb package now exposes the canonical long-term package spine while keeping the executable surface strictly pairs-only.
* Live artifact payload assembly remains in the pairs runtime path, while the new `artifacts/` namespace stays placeholder-only and outside current execution.
* Deferred dimensions, control, and artifact namespaces import cleanly but fail closed when invoked, preventing accidental runtime broadening.
* Phase I-D: Wide frame for the pair is produced by `DataViewAsOfAdapter.as_wide_frame(knowledge_dates)`; strategy artifact payloads (execution_assumptions, stat_validity_report) are built in the pairs path (e.g. via `common.diagnostics`) and written through the bundle store.

### Breaking Changes

None intended. Existing live imports remain rooted in `srcPy.strategies.stat_arb`, the `stat_arb_pairs` registry key is unchanged, and no new executable strategy entry points were added.

### Test / Validation Evidence

| Test file / command | Type | Invariant or contract |
|---------------------|------|-----------------------|
| `tests/python/unit/preprocessor/test_expr_ops_executor.py` | Unit | Phase I-D: pairs.beta and stats.half_life numeric correctness; PairBeta default method ols. |
| `tests/python/unit/strategies/test_stat_arb_pairs_strategy.py` | Unit | Phase I-D: features_plan op order, discrete signals, KALMAN guard, entry/exit/max_hold/half-life behavior. |
| `tests/python/integration/test_stat_arb_vertical_slice.py` | Integration | Phase I-D: Deterministic PIT path and execution_assumptions/stat_validity_report in bundle; Yahoo SPY/QQQ smoke (opt-in net). |
| `tests/python/unit/strategies/test_stat_arb_package_spine.py` | Unit | Locks the Phase I-Db package-spine contract: live root exports stay pairs-only, deferred modules remain import-safe, and stub invocation fails closed. |
| Phase I-D pytest suite (`test_expr_ops_executor`, `test_stat_arb_pairs_strategy`, `test_stat_arb_vertical_slice`, `test_stat_arb_package_spine`) | Validation | Run with `--cov-config=.coveragerc.phase1d`; coverage report below. |

### Coverage Report (Phase I-D scope)

Final line and branch coverage for the Phase I-D–in-scope files:

| File | Line Coverage | Lines Covered | Statements | Branch Coverage | Covered Branches | Total Branches |
|------|---------------|---------------|------------|-----------------|------------------|-----------------|
| `srcPy/preprocessor/graph/ops_custom.py` | 87.48% | 462 | 515 | 76.00% | 76 | 100 |
| `srcPy/strategies/__init__.py` | 100.00% | 6 | 6 | N/A | 0 | 0 |
| `srcPy/strategies/pipeline_strategy.py` | 35.51% | 329 | 821 | 19.75% | 47 | 238 |
| `srcPy/strategies/stat_arb/__init__.py` | 100.00% | 5 | 5 | N/A | 0 | 0 |
| `srcPy/strategies/stat_arb/config.py` | 100.00% | 19 | 19 | N/A | 0 | 0 |
| `srcPy/strategies/stat_arb/entry.py` | 92.45% | 41 | 43 | 80.00% | 8 | 10 |
| `srcPy/strategies/stat_arb/pairs.py` | 100.00% | 70 | 70 | 100.00% | 20 | 20 |

### Deferred

* Multileg stat-arb runtime (`triplets` and above) remains explicitly deferred beyond the live Phase I-D pairs slice.
* Control-theoretic execution, Riccati numerics, xi solving, and stability analysis remain scaffold-only.
* Runtime artifact/report generation under `srcPy/strategies/stat_arb/artifacts/` remains placeholder-only and is not part of the current execution path.
* Phase I-D: HedgeEstimator.KALMAN and `stats.kf_beta` remain unimplemented; requesting KALMAN raises NotImplementedError. Dual PolarsExecutor in executor.py is pre-existing and out of scope.

## Version 4.3.0 (2026-03-13)

Phase I-C closes the gap between PIT-safe split logic and actual feature materialization. Governed supported built-ins now execute on a single canonical graph path, direct legacy execution is blocked in governed contexts, the canonical technical-op floor is expanded, and feature-layer bridge/property coverage now proves DataView-backed execution plus leakage resistance on the trusted feature path. This is a MINOR release because it materially expands governed feature capability and enforcement without changing the public `PipelineStrategy` authoring API.

### Why This Release Exists

Phase I-B proved that the PIT boundary and split geometry were in place. Phase I-C was needed to prove that feature materialization itself could not bypass governed access rules: supported built-ins now lower onto the canonical graph path, governed legacy execution is explicitly forbidden, and the feature layer now has direct PIT/leakage evidence instead of inheriting safety by assumption from upstream split logic.

### Governed Execution Rule

Governed enforcement in this phase applies exactly when `StrategyContext.pit_provenance is not None`; no truthiness-based or placeholder sentinel interpretation was introduced.

### Canonical Lowering Contract

| Legacy step name | Canonical graph op | Phase I-C meaning |
|------------------|--------------------|-------------------|
| `ROLL_MEAN` | `technical.SMA` | Built-in rolling-mean strategies now resolve through canonical graph execution. |
| `ROLL_STD` | `stats.rolling_std` | Rolling standard deviation is now part of the governed canonical op floor. |
| `Z_SCORE` | `scaling.zscore_roll` | Existing rolling z-score behavior stays live and is now covered on the governed leakage path. |
| `EMA` | `technical.EMA` | Exponential moving average is now a canonical built-in op. |
| `RSI` | `technical.RSI` | RSI built-ins resolve through the canonical registry instead of direct legacy execution. |
| `MACD` | `technical.MACD_line_signal` | MACD built-ins lower to the canonical line/signal op; histogram behavior was not redesigned in this phase. |

### Detailed Changes

| Location | Change |
|----------|--------|
| `srcPy/strategies/pipeline_strategy.py` | Added governed-context enforcement keyed to `ctx.pit_provenance is not None`, canonical lowering for supported built-ins, canonical cache descriptors keyed to lowered params/op identity, governed `_FEATURE_OPS` blocking via `MaterializationError`, attr clearing on governed source frames, and pandas-return-after-graph-execution behavior. |
| `srcPy/strategies/migrated_strategies.py` | Updated built-in `features_plan()` implementations so supported strategies emit canonical graph op names instead of legacy feature-op tokens. |
| `srcPy/preprocessor/graph/factory.py` | Extended the built-in op registry and compatibility alias map so supported built-ins lower into canonical graph names without creating a second registry tree. |
| `srcPy/preprocessor/graph/ops_custom.py` | Added concrete op classes and registry wiring for `technical.EMA`, `technical.MACD_line_signal`, `technical.Bollinger`, `technical.ATR`, `technical.OBV`, `technical.VWAP`, and `stats.rolling_std`, while keeping pair-related deferred lowerings explicitly non-executable. |
| `srcPy/preprocessor/graph/backends/polars.py` | Implemented deterministic lowerings for the Phase I-C canonical op floor, including fail-closed governed VWAP behavior and internal graph execution support for pandas-return callers. |
| `tests/python/unit/strategies/test_pipeline_strategy_bridge.py` | Extended the existing bridge suite with canonical plan-emission checks, governed `MaterializationError` coverage, DataView-backed historical-frame proofs, raw-handle exposure checks, delayed pandas conversion assertions, and governed VWAP fail-closed coverage. |
| `tests/python/property/test_preprocessor_leakage.py` | Replaced the Phase I-B-era stub with a real feature-layer Hypothesis battery using the same poison-pill style as split-geometry leakage work, including single-output and multi-output indicator invariants against DataView-backed history. |
| `tests/python/unit/preprocessor/test_expr_ops_executor.py` and `tests/python/unit/preprocessor/test_preprocessor_coverage.py` | Added unit coverage for the expanded op floor, live rolling-zscore behavior, alias registration, and registry completeness. |
| `tests/python/property/test_dataview_pit.py` | Added focused `DataViewAsOfAdapter` coverage for the pre-snapshot `pit_meta()` path and emitted `MarketSlice` provenance metadata contracts. |
| `tests/python/unit/backtesting/test_contracts_roundtrip.py` | Added targeted `contracts.types.to_primitive()` coverage for tuple, `datetime`, and `Enum` normalization. |
| `tests/python/unit/preprocessor/test_preprocessor_coverage.py` | Added focused `graph/backends/polars.py` coverage for registry helper validation, array helper edge cases, VWAP fail-closed branches, eager/lazy lowering paths, and executor collect-policy behavior. |
| `docs/ADR-008-Single-Path-Feature-Execution-Lock.md` | Promoted ADR-008 from Proposed to Accepted once the single-path execution lock landed in code. |
| `docs/phase_i_c_closeout.md` | Added the required closeout ledger covering files changed, invariant counts, canonical-vs-legacy execution paths, repo-path ambiguity resolution, and merge-gate outcomes. |

### Behavioral Changes

* Governed feature materialization now rejects direct `_FEATURE_OPS` execution for supported built-ins and fails loudly with `MaterializationError` when callers attempt to bypass canonical lowering.
* Supported migrated strategies now publish canonical feature plans by default, reducing legacy-token drift between strategy intent and graph execution.
* Internal feature execution for governed contexts now runs through the graph/planner/executor path even when the caller asks for pandas output; pandas conversion happens only after feature materialization completes.
* Governed bridge execution no longer carries raw-source attrs into intermediate feature frames, and negative tests now assert that graph execution does not expose raw source handles on the trusted path.
* `technical.VWAP` now explicitly fails closed on governed daily-only inputs unless session or intraday columns are present.
* Deferred pair-related lowerings remain intentionally non-executable; this release does not start Phase I-D pair runtime work.

### Breaking / Stricter Behavior

No user-facing strategy authoring API break is intended for supported production strategies.

The main enforcement change in this release is that governed direct legacy execution for supported built-ins is no longer allowed: attempts to execute them through `_FEATURE_OPS` now raise `MaterializationError` instead of being treated as an alternate runtime path.

### Test / Validation Evidence

| Test file / command | Type | Invariant or contract |
|---------------------|------|-----------------------|
| `tests/python/unit/strategies/test_pipeline_strategy_bridge.py` | Unit / bridge | Locks canonical plan emission, governed `_FEATURE_OPS` blocking, DataView-backed bridge execution, raw-source isolation, delayed pandas conversion, and governed VWAP fail-closed behavior. |
| `tests/python/property/test_preprocessor_leakage.py` | Property | Locks PIT-safe historical feature computation, poison-pill leakage resistance, and governed indicator correctness for SMA/std/EMA/RSI/MACD/Bollinger/ATR/OBV/z-score. |
| `tests/python/unit/preprocessor/test_expr_ops_executor.py` | Unit | Locks the expanded Phase I-C op floor, deterministic lowering surfaces, and the fact that rolling z-score remains live rather than placeholder-only. |
| `tests/python/unit/preprocessor/test_preprocessor_coverage.py` | Unit | Locks canonical registry membership and compatibility alias registration for the Phase I-C op floor. |
| `tests/python/property/test_dataview_pit.py` | Property | Locks the remaining `DataViewAsOfAdapter` PIT metadata branches, including the `None` pre-snapshot path and `MarketSlice` provenance emission after `as_of()`. |
| `tests/python/unit/backtesting/test_contracts_roundtrip.py` | Unit | Locks `contracts.types.to_primitive()` normalization for tuple containers plus `datetime` and `Enum` values used by contract serialization. |
| `tests/python/unit/preprocessor/test_preprocessor_coverage.py` | Unit | Extends the Polars backend evidence to cover helper validation, array edge cases, VWAP fail-closed branches, eager lowering paths, and executor collect-policy decisions. |
| `docs/phase_i_c_closeout.md` | Merge-gate ledger | Records the manual audit result, invariant count, canonical-versus-legacy execution paths, and the final gate readout for Phase I-C, including 39 combined in-scope PIT/leakage invariants and the governed-path raw-source isolation check. |

### Companion Document Versions

| Document | Previous | New |
|----------|----------|-----|
| `docs/ADR-008-Single-Path-Feature-Execution-Lock.md` | Proposed | Accepted (Phase I-C implemented 2026-03-13) |
| `docs/phase_i_c_closeout.md` | — | Added |

No companion DOCX-suite source versions were bumped as part of this implementation-only Phase I-C closeout.

### Deferred

* Pair-runtime lowerings such as `pairs.beta`, `pairs.spread`, and related Phase I-D pair/stat-arb execution work remain explicitly deferred and non-executable.  <!-- Updated by Phase I-D: see 4.4.0 entry. -->
* `technical.MACD_hist` and rolling z-score were not redesigned in this phase; rolling z-score stays live and covered, while histogram behavior remains on its pre-existing implementation path.
* No intraday/session-aware daily VWAP approximation was introduced; governed daily VWAP remains fail-closed until real session-aware data is available.
* Full removal of all non-governed legacy compatibility execution remains later cleanup work after equivalent canonical lowering coverage is complete across the remaining exploratory paths.

## Version 4.2.0 (2026-03-12)

Changelog for **Phase I-B source adaptation into the sovereign PIT path and proprietary governance hardening**: source adapters now own their bitemporal columns for the governed daily path, Yahoo historical daily OHLCV is wired as a PIT-ready source, FRED now exposes an explicit vintage seam with a named Phase I approximation stub, market-data source contracts are split from runtime helpers behind a compatibility shim, CI excludes `@pytest.mark.net` tests from the default run, and the legal/governance surface is aligned with the proprietary LICENSE via new risk/governance documents, clarified security/privacy policies, and explicit non-expansion of rights. This is a MINOR release because it expands the PIT-safe source surface and formalizes governance/legal documentation without changing the locked Phase I-A PIT contracts or broadening user rights.

Version: 4.2.0 (Phase I-B source adaptation milestone: `file.py` emits native temporal columns without relying on orchestrator synthesis, `yahoo_fetcher.py` produces PIT-ready daily OHLCV output, `fred.py` exposes a replaceable vintage seam with `FREDApproximationStub`, `sources/base.py` becomes a compatibility shim over `contracts.py` and `runtime.py`, the adapted source-to-PIT chain is validated end-to-end in CI, and LICENSE/SECURITY/PRIVACY plus MODEL_CARD/RISK_DISCLOSURE/REPRODUCIBILITY/GOVERNANCE documents are updated or introduced to reflect the proprietary, non-open-source governance stance.)

## Version 4.0.1 (2026-03-11)

Changelog for **explicit absolute-import consolidation in ADR-007 hashing, artifact-registry, and backtesting contracts**: replace intra-package relative imports under `srcPy/artifact_registry/`, `srcPy/backtesting/`, and `srcPy/ops/hashing/` with explicit `srcPy.*` absolute imports to make the ADR-007 hashing surface, artifact-registry contracts, and backtesting substrate easier to reason about and more robust to future package layout changes. This is a PATCH release because it is a purely structural import refactor with no intended behavioral or contract changes.

Version: 4.0.1 (Patch-level import refactor: `srcPy.artifact_registry.*`, `srcPy.backtesting.*`, and `srcPy.ops.hashing.*` now use explicit `srcPy.*` absolute imports instead of intra-package relative imports, aligning the ADR-007 hashing contract and backtesting substrate with the project's preferred import style and simplifying static analysis and tooling.)

### Major Themes Across All Changes

* **Make ADR-007 hashing surfaces explicit and tool-friendly:** The core hashing modules, envelopes, equality-fallback scaffolds, and primitive implementations now import each other via `srcPy.ops.hashing.*`, eliminating relative-import ambiguity in the canonical hashing contract package.
* **Clarify artifact-registry and backtesting contract wiring:** The RunRegistry, CAS helpers, and backtesting contracts/registry now use fully qualified `srcPy.*` imports so the ADR-007 artifact identity story and backtesting substrate can be traced mechanically through import graphs.
* **No behavioral or contract changes intended:** The refactor preserves module contents, public symbols, and test-facing contracts; the only change is how modules reference one another.

### Detailed Changes

| Location | Change |
|----------|--------|
| `srcPy/artifact_registry/__init__.py` | Switched the CAS import from `from .cas import HashRefs, LocalCAS` to `from srcPy.artifact_registry.cas import HashRefs, LocalCAS` so external callers and internal helpers both refer to the same explicit package path. |
| `srcPy/artifact_registry/run_registry.py` | Replaced the relative `from .cas import HashRefs` with `from srcPy.artifact_registry.cas import HashRefs`, keeping all RunRegistry-facing CAS interactions on the explicit ADR-002/ADR-007 package path. |
| `srcPy/backtesting/contracts/protocols.py` | Updated imports for `BacktestPlan` and the contracts types from `from .plan` / `from .types` to `from srcPy.backtesting.contracts.plan` and `from srcPy.backtesting.contracts.types`, making the backtesting Protocols resolvable without relying on relative-import semantics. |
| `srcPy/backtesting/contracts/plan.py` | Replaced `from .errors import DeterminismTierMissingError` with `from srcPy.backtesting.contracts.errors import DeterminismTierMissingError`, keeping determinism-tier enforcement on an explicit, discoverable import path. |
| `srcPy/backtesting/contracts/registry.py` | Replaced `from .errors import UnknownIdError` with `from srcPy.backtesting.contracts.errors import UnknownIdError` so registry error reporting is tied to a stable module path. |
| `srcPy/backtesting/data/__init__.py` | Switched `from .pit import PITSafeDataView, PitUnsafeFrame` to `from srcPy.backtesting.data.pit import PITSafeDataView, PitUnsafeFrame`, making PIT wrapper imports explicit for downstream callers. |
| `srcPy/ops/hashing/__init__.py` | Converted all intra-package imports (`.contract`, `.canonicalizer`, `.envelope`, `.ahm`, and all `.primitives.*` modules) to explicit `from srcPy.ops.hashing...` imports, keeping the public hashing surface aligned with ADR-007's canonical package naming. |
| `srcPy/ops/hashing/ahm.py` | Updated imports of `contract`, `envelope`, and primitive hasher modules from `..hashing.*` to `srcPy.ops.hashing.*`, ensuring the Adaptive Hash Manager depends on the explicit ADR-007 package tree. |
| `srcPy/ops/hashing/envelope.py` | Replaced `from .contract` and `from .equality` with `from srcPy.ops.hashing.contract` and `from srcPy.ops.hashing.equality`, making the HashRef envelope's dependencies visible from the top-level package. |
| `srcPy/ops/hashing/equality.py` | Switched `from .contract` and the TYPE_CHECKING-only `from .envelope import HashRef` to `from srcPy.ops.hashing.contract` and `from srcPy.ops.hashing.envelope import HashRef`, so equality-fallback logic depends on explicit hashing-contract modules. |
| `srcPy/ops/hashing/preimage.py` | Updated `from .contract import HashContractViolation, HashPurpose, SystemInvariant` to `from srcPy.ops.hashing.contract import ...`, preserving the preimage invariant bindings while avoiding relative imports. |
| `srcPy/ops/hashing/canonicalizer.py` | Replaced `from .contract` with `from srcPy.ops.hashing.contract` so canonicalization rules are explicitly tied to the ADR-007 contract definitions. |
| `srcPy/ops/hashing/primitives/blake3_impl.py` | Converted imports of `canonicalizer`, `contract`, and `envelope` to `from srcPy.ops.hashing.canonicalizer import CANON`, `from srcPy.ops.hashing.contract import ...`, and `from srcPy.ops.hashing.envelope import ...`, aligning BLAKE3 primitives with the explicit hashing package. |
| `srcPy/ops/hashing/primitives/hmac_sha256_impl.py` | Updated imports to use `srcPy.ops.hashing.canonicalizer`, `srcPy.ops.hashing.contract`, and `srcPy.ops.hashing.envelope`, so HMAC-SHA256 seed derivation is wired directly to the canonical hashing contract and envelope surfaces. |

### Deferred

* (None for this patch release.)

## Version 4.0.0 (2026-03-11)

Changelog for **ADR-007 v1.1 hashing-contract adoption and artifact-registry path transition**: add the canonical hashing package under `srcPy/ops/hashing/`, stage the required golden-vector suite layout under `tests/golden/adr007/`, introduce the registry-facing attestation facade in `srcPy/artifact_registry/attestation.py`, retarget hashing and artifact-registry tests to the new contract surface, and normalize repo-visible D-tier wording to the ADR-007 v1.1 definitions. This is a MAJOR release because the legacy `srcPy/ops/artifact_registry.py` module path is removed and callers must migrate to the canonical package layout.

Version: 4.0.0 (Canonical ADR-007 hashing contract scaffold: purpose-bound hashing modules in `srcPy/ops/hashing/`, dual-domain CAS/attestation facade in `srcPy/artifact_registry/attestation.py`, golden-vector manifests in `tests/golden/adr007/`, artifact-registry integration anchors, and determinism-tier wording locked to ADR-007 v1.1: D3 — Bitwise, D2 — Semantic, D1 — Topological, D0 — None / Debug.)

### Major Themes Across All Changes

* **ADR-007 becomes the canonical hashing boundary:** Hashing logic, contracts, preimage rules, envelope semantics, equality-fallback law, and primitive surfaces now have one explicit home in `srcPy/ops/hashing/` instead of being implied through older mixed-path helpers.
* **Cross-language certification work is now materially staged in-repo:** The `tests/golden/adr007/` tree records the expected golden-vector locations per primitive, including the CI harness gap that still exists for Python 3.12, C++20, and Java 21 certification.
* **Artifact identity and gate attestation are treated as separate but coupled domains:** The new `srcPy/artifact_registry/attestation.py` facade validates the locked `cas.v1:b3-256` and `attest.v1:jcs-sha256` pairing over the same canonical bytes.
* **Repo-visible determinism terminology is now ADR-007 exact:** Marker descriptions and seed-plugin docs no longer use superseded phrases such as “golden replay,” “regression,” or “exploratory” to describe D-tiers.

### Detailed Changes

| Location | Change |
|----------|--------|
| `srcPy/ops/hashing/contract.py` | Added the canonical ADR-007 enum and invariant surface, including `DTier`, `PersistenceTier`, `AlgoId`, `DomainPrefix`, `HashPurpose`, `SystemInvariant`, and the contract exceptions used by the new hashing package. |
| `srcPy/ops/hashing/preimage.py` | Added the purpose-bound preimage scaffold, including frozen dataclasses for `PreimagePart` and `CompositePreimage`, plus the canonical namespace/length-prefix composition entrypoints that document the locked `namespace_utf8 || u64be(len(...))` rule. |
| `srcPy/ops/hashing/envelope.py` | Added the `HashRef` envelope scaffold and factory surface for persistent hash identities, and made `verify_cache_hit` a backward-compatible re-export from the equality facade so older import sites can converge on one law source. |
| `srcPy/ops/hashing/equality.py` | Added the equality-fallback scaffold, including `EqualityEvidence`, compatibility checks, payload/aux witness hooks, and policy-validation entrypoints for non-cryptographic cache surfaces. |
| `srcPy/ops/hashing/primitives/*.py` | Added per-primitive scaffold modules for BLAKE3, SHA-256/JCS, XXH3, SipHash-2-4, HMAC-SHA256, SimHash, MinHash, and Rabin, each documenting the locked purpose mapping, intended invariants, and implementation gaps. |
| `srcPy/artifact_registry/attestation.py` (new) | Added the registry-facing attestation helper layer: dual-domain hash-pair coercion, CAS/attest validation, gate wire-format conversion, `ArtifactEntry`, `ArtifactAttestor`, `BundleManifestWriter`, and small manifest helpers. |
| `srcPy/ops/artifact_registry.py` | Removed the legacy module path. This is the release’s explicit compatibility break; callers must migrate to `srcPy/artifact_registry/` and the ADR-007 hashing package. |
| `tests/golden/adr007/blake3/`, `jcs_sha256/`, `xxh3/`, `sip24/`, `hmac_sha256/`, `simhash/`, `minhash/`, `rabin/` (new) | Added per-primitive `manifest.json` files and placeholder case assets so every D3 boundary can be paired with an explicit golden-vector location in the repo, even before the full multi-language harness is implemented. |
| `tests/python/unit/hashing/test_preimage.py` | Added structural and contract-focused preimage tests, including dataclass shape/immutability checks and placeholders for exact composite-preimage behavior. |
| `tests/python/unit/hashing/test_equality.py` | Added equality-evidence structural tests, keyword-only API checks for `verify_cache_hit`, and scaffold tests for the equality-fallback law and evidence policy. |
| `tests/python/unit/hashing/test_envelope.py` | Added envelope-structure tests for `HashRef`, keyed-algorithm requirements, `to_id_string()`, and the intended factory/equality behavior. |
| `tests/python/unit/hashing/primitives/test_*.py` | Added primitive-specific unit-test files that lock manifest presence and reserve primitive behavior contracts without falsely certifying unimplemented code paths. |
| `tests/python/unit/artifact_registry/test_cas_store.py` | Reworked the CAS store test file into the dual-domain integration anchor identified by ADR-007: JSON persistence now asserts that CAS and attestation hash the same JCS bytes under different algorithms. |
| `tests/python/unit/artifact_registry/test_attestation.py` (new) | Added focused unit coverage for the attestation facade, including dual-domain validation, gate-hash formatting, bundle-manifest emission, and duplicate-role rejection. |
| `tests/python/_plugins/seeds.py`, `pyproject.toml`, `VERSION.md` | Replaced stale D-tier glossary text with the canonical ADR-007 v1.1 mapping: `d3 = bitwise`, `d2 = semantic`, `d1 = topological`, `d0 = none/debug only`. |

### Behavioral Changes

* Hashing contracts, envelopes, preimage rules, and primitive surfaces now live in `srcPy/ops/hashing/` as the canonical package.
* Artifact-registry attestation is no longer an implicit helper concern; it is modeled explicitly through the new `srcPy/artifact_registry/attestation.py` facade.
* The repo-level determinism marker description now matches ADR-007 v1.1 exactly.
* The repository now contains the reserved golden-vector suite layout required by ADR-007 for D3-capable surfaces, even though certification replay is still incomplete.

### Breaking Changes

* `srcPy/ops/artifact_registry.py` is removed.
  Migration required: update imports to the canonical `srcPy/artifact_registry/` package and the new `srcPy/ops/hashing/` modules.
* Repo-visible D-tier wording now follows ADR-007 v1.1 exactly.
  Migration required: stop using superseded phrases such as “D0 Golden Replay,” “regression,” “statistical-equiv,” or “exploratory” when describing `@pytest.mark.determinism(...)` tiers.

### Test / Validation Evidence

| Test file / command | Type | Invariant or contract |
|---------------------|------|-----------------------|
| `tests/python/unit/hashing/test_preimage.py` | Unit | Locks dataclass structure and the intended composite-preimage API shape for ADR-007 preimage construction. |
| `tests/python/unit/hashing/test_equality.py` | Unit | Locks `EqualityEvidence` structure, keyword-only `verify_cache_hit`, and the intended equality-fallback law surface. |
| `tests/python/unit/hashing/test_envelope.py` | Unit | Locks `HashRef` structure, keyed-algorithm field requirements, and canonical ID-string behavior. |
| `tests/python/unit/hashing/primitives/test_blake3.py`, `test_sha256_jcs.py`, `test_xxh3.py`, `test_siphash.py`, `test_hmac_sha256.py`, `test_simhash.py`, `test_minhash.py`, `test_rabin.py` | Unit | Lock the existence and shape of the per-primitive golden-vector manifest anchors and reserve primitive behavior slots. |
| `tests/python/unit/artifact_registry/test_cas_store.py` | Unit | Locks the dual-domain invariant that CAS and attestation hash the same JCS bytes with different algorithms. |
| `tests/python/unit/artifact_registry/test_attestation.py` | Unit | Locks attestation-facade validation, gate wire-format conversion, and bundle-manifest helper behavior. |
| `python -m py_compile srcPy/ops/hashing/envelope.py tests/python/unit/hashing/test_preimage.py tests/python/unit/hashing/test_equality.py tests/python/unit/hashing/test_envelope.py tests/python/unit/hashing/primitives/test_blake3.py tests/python/unit/hashing/primitives/test_sha256_jcs.py tests/python/unit/hashing/primitives/test_xxh3.py tests/python/unit/hashing/primitives/test_siphash.py tests/python/unit/hashing/primitives/test_hmac_sha256.py tests/python/unit/hashing/primitives/test_simhash.py tests/python/unit/hashing/primitives/test_minhash.py tests/python/unit/hashing/primitives/test_rabin.py tests/python/unit/artifact_registry/test_cas_store.py tests/python/unit/artifact_registry/test_attestation.py tests/python/_plugins/seeds.py` | Validation | Syntax validation for the new and edited Python files passed in this thread. |
| Targeted pytest collection / execution for the hashing slice | Validation | Not completed in this thread because the sandbox Python environment did not expose a working `pytest` entrypoint after local dependency staging. |

### Companion Document Versions

| Document | Version | 4.0.0 impact |
|---|---:|---|
| `docs/src/ImplementationPlan.md` | 1.0.0 | Updated to reflect the canonical `srcPy/ops/hashing/` package, `tests/golden/adr007/` requirement, dual-domain CAS/attestation framing, and retirement of `srcPy/ops/artifact_registry.py`. |
| `docs/src/TechnicalRoadmap.md` | 1.0.0 | Updated to record that the ADR-007 contract surface and repo layout are now staged while cross-language golden-vector harness work and most primitive implementations remain deferred. |
| `docs/src/MetaLearningCore.md` | 1.0.0 | No change in 4.0.0. |
| `docs/src/MetaLearningArchitectureVision.md` | 1.0.0 | No change in 4.0.0. |
| `README.md` | 3.7.2 | No change in 4.0.0. |

### Deferred

* The primitive methods in `srcPy/ops/hashing/` remain scaffold-first and largely unimplemented; this release records the contract surface and test anchors, not a finished runtime hashing subsystem.
* The Python 3.12 / C++20 / Java 21 golden-vector certification harness is still absent from CI; the manifests document the gap, but certification work remains future work.
* No compatibility shim is shipped for the removed `srcPy/ops/artifact_registry.py` path; if downstream import continuity is required, that must be handled in a later compatibility release.

___

## Archived Releases

Full release entries for older versions are preserved in:

- docs/releases/VERSION_4.x.md
- docs/releases/VERSION_3.x.md
- docs/releases/VERSION_2.x.md
- docs/releases/VERSION_1.x.md














