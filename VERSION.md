# Version History

This file serves as the project's release ledger and architecture evolution.
For a traditional short-form change summary, see commit history.

Older release entries are archived in `docs/releases/`.

---

## Version Index

### 4.x — ADR-007 Hashing Contract + Phase I PIT Feature Hardening
- 4.9.1 — roadmap phase-model clarification PATCH: explicit I-F / I-G / II-0 sequencing, evidence-first guardrails, protocol appendix surfaces, and Resolution Ledger phase-semantic alignment
- 4.9.0 — Phase I-F-2 planning-surface sync PATCH: companion-suite version rebasing, F-2 closure reflected on canonical docs, Resolution Ledger 1.0.6 consistency patch, and README/VERSION release-anchor update
- 4.8.0 — Phase I-F-1 / OI-19 / GATE-I-F-01: companion-doc truthfulness audit, structural sync to v4.8.0 baseline, audit artifacts under `docs/audits/`, Resolution Ledger evidence for companion alignment
- 4.5.4 — Phase I-E closure pass: canonical artifact-registry ownership, canonical CLI delegation, governed momentum blocker closure, ADR-007 D2 replay evidence, and companion-doc sync
- 4.5.3 — test-suite closure pass: torture-fixture CSV robustness, governed/docs test alignment, async/cache hardening, and property-test stabilization
- 4.5.2 — ADR-009 momentum package migration, focused momentum test closure, and companion-doc synchronization
- 4.5.1 — Phase I-E governance closure pass: DataLineageGate wiring, artifact-registry hashing ownership, canonical-frame CI evidence model, governed momentum artifact path hardening, and companion-doc status sync
- 4.5.0 — Phase I-E SignalFactory substrate (SignalCatalog + slot_index, screening_report.json, taxonomy, gate_to_screening), stricter `gate.py` Phase I-E policy enforcement, and mypy --strict for momentum/preprocessor/columns
- 4.4.2 — companion-doc cleanup and DOCX typography normalization
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
| ADR-007 Hashing + Phase I PIT | 4.x | ADR-007 hashing/attestation, golden-vector layout; Phase I PIT orchestration (4.1), source adaptation (4.2), governed feature path (4.3), stat-arb pairs vertical slice (4.4), Phase I-E SignalFactory substrate (4.5) |
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

## Version 4.9.1 (2026-03-24) — Roadmap Phase-Model Clarification Patch

Changelog for the **roadmap phase-model clarification pass**: revise the companion planning surface so the pre-build foundation is explicit rather than implied, keep Phase I-F narrow, introduce **Phase I-G** and **Phase II-0** as distinct pre-Phase-II stages, preserve **II-A through II-E** as the actual validation-gated adaptive-learning build, and keep **Phase III** / **Phase IV** explicitly conditional. This release is documentation-first and policy-aligned: it does not claim a new runtime subsystem, a promotable allocator, or newly delivered execution or Signal Factory machinery.

Version: **4.9.1** (**PATCH** — roadmap clarity, ledger hardening, and companion-suite protocol-surface additions without release-surface expansion)

### Major Themes Across All Changes

- Made the roadmap read as **I-F -> I-G -> II-0 -> II**, rather than letting Phase II silently absorb protocol work and scaffolding work.
- Added the exact evidence-first guardrail language across the planning docs so promotable adaptive-learning machinery begins only in Phase II.
- Introduced lightweight protocol/spec appendix surfaces for **RiskFn**, **Signal Generation**, **task validity pilot evidence**, and **paper-trade simulation handoff**.
- Updated the Resolution Ledger so `I-G` and `II-0` exist as tracked planning semantics while keeping narrow `I-F` blockers and true Phase II normative locks in place.

### Detailed Changes

| Location | Change |
|----------|--------|
| `docs/src/README.md`, `docs/src/ImplementationPlan.md`, `docs/src/TechnicalRoadmap.md` | Reframed the roadmap so **I-F** is narrow closure, **I-G** is empirical/protocol foundation, **II-0** is non-promotable harness work, **II** is the first promotable adaptive-learning phase, and **III/IV** remain conditional. |
| `docs/src/ImplementationPlan.md` | Added `# 3.x Phase I-G` and `# 4. Phase II-0`, preserved `II-A` through `II-E`, expanded the Immediate Priority Stack, and added appendix references for protocol and handoff surfaces. |
| `docs/src/TechnicalRoadmap.md` | Added the explicit sequencing block, “not assumed” language, and subphase tables for **II-0**, **II**, **III**, **IV**, and **IV+**. |
| `docs/src/MetaLearningCore.md` | Clarified that early empirical closure may begin in **I-G** / **II-0**, that pre-trainer pilots are allowed, and that final Phase II promotion logic still governs trainer commitment, promotion, rollback, and kill. |
| `docs/src/MetaLearningArchitectureVision.md` | Added forward-compatibility sections for **RiskFn Protocol**, **Signal Generation Protocol / signal-admission path**, and the **feature frontier / alternative-data ingestion** boundary; clarified that `signal_embedding` remains a Phase IV operational surface. |
| `docs/src/WhitePaper.md` | Reframed the roadmap narrative around **I-F**, **I-G**, **II-0**, and conditional **III/IV** while keeping the document less operational than the internal plan set. |
| `docs/src/ResolutionLedger.md` | Added `I-G` / `II-0` planning items for RiskFn protocol definition, Signal Generation Protocol, task non-exchangeability pilot, context-encoder upgrade criteria, signal-universe expansion policy, alternative-data admissibility contract, paper-trading simulation requirements, and II-0 harness scaffolding. |
| `docs/src/risk_protocol.md`, `docs/src/signal_generation_protocol.md`, `docs/src/task_validity_pilot_report.md`, `docs/src/paper_trade_sim_spec.md` | Added new markdown appendix surfaces so the updated Implementation Plan points to concrete protocol/spec files rather than placeholder-equivalent references. |
| `README.md` | Added a short governed-roadmap pointer so the repo-root README no longer obscures the current phase map maintained in `docs/src/README.md`. |

### Behavioral Changes

- The companion suite now states explicitly that **Phase I-F freezes system truth**, **Phase I-G freezes research policy/proof burden**, and **Phase II-0** is **non-promotable scaffolding** only.
- The roadmap no longer reads as if Phase II starts with immediate full MLC buildout.
- **Phase III** is now consistently described as the first execution-serious phase, and **Phase IV** as the first signal-factory-serious phase, both conditional on allocator validation and product need.
- `RiskFn` is no longer described as a vague placeholder in the planning narrative; it is treated as a governed protocol boundary.
- Alternative-data and signal-factory breadth are now described as later governed ambitions rather than present-day facts.

### Breaking Changes

None.

### Test / Validation Evidence

| Check | Result |
|-------|--------|
| Targeted companion-doc readback | Verified revised phase ordering, guardrail text, and appendix references across the touched markdown sources. |
| Terminology consistency search (`rg`) | Verified `Phase I-G`, `Phase II-0`, conditional III/IV language, and the new appendix filenames are present where intended. |
| Code/test suite execution | Not run; this release is a markdown/ledger update only. |

### Companion Document Versions

| Document | Version surface referenced in this release |
|----------|-------------------------------------------|
| `README.md` | 4.9.0 |
| `docs/src/ImplementationPlan.md` | 6.4.14 |
| `docs/src/TechnicalRoadmap.md` | 1.4.15 |
| `docs/src/MetaLearningCore.md` | 1.2.13 |
| `docs/src/MetaLearningArchitectureVision.md` | 1.2.14 |
| `docs/src/ResolutionLedger.md` | 1.0.6 |
| `docs/src/WhitePaper.md` | 2.2.4 |

### Deferred

- No runtime subsystem, gate implementation, broker integration, or promotable allocator code is claimed by this release.
- DOCX rebuild/version-rebasing work for the companion suite remains outside this patch-sized ledger update.
- Existing unrelated working-tree changes, including `docs/src/FormattingSpec.md`, are not part of this release entry.

---

## Version 4.9.0 (2026-03-24) — Phase I-F-2 Planning-Surface Sync and Resolution-Ledger Consistency Patch

Changelog for the **Phase I-F-2 planning-surface sync patch**: carry forward the Phase I-F-1 truth baseline while rebasing the canonical companion suite to the live version set (**Implementation Plan 6.4.14 / Technical Roadmap 1.4.15 / Meta-Learning Core 1.2.13 / Meta-Learning Architecture Vision 1.2.14 / Resolution Ledger 1.0.6 / README 4.9.0 / VERSION.md 4.9.0**). This patch does not claim a new runtime subsystem. It closes the planning/documentation surface for **OI-20 / GATE-I-F-02**, repairs Resolution Ledger lifecycle contradictions on **OI-09**, **OI-10**, and **OI-17**, and updates title pages, companion maps, and current-release framing so the suite tells one consistent story.

### Detailed Changes

| Location | Change |
|----------|--------|
| `README.md` | Bumped release anchor to **4.9.0**; updated companion map, docmap versions, and current-release framing. |
| `docs/src/TechnicalRoadmap.md`, `docs/src/ImplementationPlan.md` | Rebased managed metadata to **1.4.15** / **6.4.14** and preserved the II-A → II-E Phase II structure with F-2 planning-surface sync notes. |
| `docs/src/MetaLearningCore.md`, `docs/src/MetaLearningArchitectureVision.md` | Metadata/docmap/source-stamp sync to the live suite versions; no substantive F-2 body rewrite. |
| `docs/src/ResolutionLedger.md` | `MRL_VERSION` **1.0.6** and `CODEBASE_VERSION` **4.9.0**; closed **OI-20** / **GATE-I-F-02**; repaired **OI-09**, **OI-10**, and **OI-17** lifecycle fields; refreshed dashboard counts and hotlist truth. |
| `docs/src/FormattingSpec.md` | Companion/version tables and footer rebased to the **4.9.0** suite surface. |

### Validation

| Check | Result |
|-------|--------|
| Managed version surfaces | Canonical title pages, companion lines, and footers rebased to the **4.9.0** suite state |
| Resolution Ledger lifecycle truth | OI/gate status fields, resolved_on fields, dashboard counts, and gate dependencies made internally consistent |

---

## Version 4.8.0 (2026-03-22) — Phase I-F-1 Companion-Doc Truthfulness Audit and v4.8.0 Baseline Sync

Changelog for **Phase I-F-1** ([OI-19](docs/src/ResolutionLedger.md), [GATE-I-F-01](docs/src/ResolutionLedger.md)): establish **v4.8.0** as the companion-suite and `VERSION.md` release anchor; remove stale **4.5.3** baseline references from title pages, source stamps, and document maps; align phase narrative with repo truth (**Phase I-A through I-E delivered and gates closed; Phase I-F open**); record **I-E gate closure**, **OI-02**, **OI-08**, **OI-13**, and **ADR-009 ACCEPTED** in companion prose where referenced; audit [FormattingSpec.md](docs/src/FormattingSpec.md) for internal consistency; run a structural sync pass for **Momentum Spec v1.3** readiness (canonical Markdown source for v1.3 is not present in `docs/src/` — see [docs/audits/phase_if_f1_audit_report.md](docs/audits/phase_if_f1_audit_report.md)); and publish audit artifacts:

- [docs/audits/phase_if_f1_truth_baseline.md](docs/audits/phase_if_f1_truth_baseline.md)
- [docs/audits/phase_if_f1_claim_matrix.csv](docs/audits/phase_if_f1_claim_matrix.csv)
- [docs/audits/phase_if_f1_companion_sync_report.md](docs/audits/phase_if_f1_companion_sync_report.md)
- [docs/audits/phase_if_f1_audit_report.md](docs/audits/phase_if_f1_audit_report.md)

This is a **MINOR** release for the documentation and manifest surface: it does not claim new runtime subsystems beyond truthful description of the existing platform and does not convert provisional validation thresholds into fixed policy.

### Detailed Changes

| Location | Change |
|----------|--------|
| `docs/src/*.md`, `VERSION.md` | Bumped companion document versions (patch/minor per doc), set **`VERSION.md 4.8.0`** on title pages and stamps, updated **§1.2 / §3** “current reality” and release-line language to the **4.8.0** audit baseline while preserving accurate citations to **4.5.4** as the last code-heavy Phase I-E delivery where needed. |
| `docs/src/ResolutionLedger.md` | `CODEBASE_VERSION` **4.8.0**; **§8** Phase I-F section header no longer implies I-E is pending; **OI-19** / **GATE-I-F-01** closed with evidence pointers to `docs/audits/`; dashboard counts updated. |
| `docs/releases/4.8.0.yml` | Release manifest for **4.8.0** with `VersionLedger@4.8.0` and suite companion tokens. |
| `README.md` (repo root) | Tightened front matter: canonical companion suite is **`docs/src/README.md`**; root README may lag on badges. |

### Validation

| Check | Result |
|-------|--------|
| Companion lines and `VERSION.md` tokens | Aligned to **4.8.0** baseline per [docs/audits/phase_if_f1_companion_sync_report.md](docs/audits/phase_if_f1_companion_sync_report.md) |
| Claim audit | Recorded in [docs/audits/phase_if_f1_claim_matrix.csv](docs/audits/phase_if_f1_claim_matrix.csv) |

---

## Version 4.5.4 (2026-03-21) — Phase I-E Closure Pass: Canonical Storage/Gate Ownership, Governed Momentum Blocker Closure, and ADR-007 D2 Replay Evidence

Changelog for **the Phase I-E closure pass**: complete the canonical ownership move for bundle-writing and governed artifact storage under `srcPy.artifact_registry`, reduce `srcPy/backtesting/storage/` to explicit retired compatibility shims, route both shipped CLI entry surfaces (`mm-gate` and `marketmind_gate.cli`) through `srcPy.cli.gate`, and close the remaining Phase I-E governed momentum blockers without claiming work that is still deferred. The governed momentum path now locks `stat_validity_report.json` to schema `v1`, emits canonical `COST_GATE_REJECTED` failure reports through `gate_result.json` while keeping the existing generic fail bucket, shares one cumulative `RunRegistry` trial-counter family across the three production-intended variants, fails crash-override requests closed pending a governed source adapter, and carries structured book-membership plus explicit fail-closed `beta_reversal_score` diagnostics in `AlphaIR`. This release also upgrades the ADR-007 evidence story to a truthful D2 state by enriching the eight committed golden suites with concrete replay expectations, adding a Python replay suite, and updating `canonical_frame.py` to report Python-only D2 evidence while leaving cross-language certification explicitly open under `OI-15`. It is a PATCH release because it closes governance, provenance, and documentation gaps on existing public surfaces without introducing a new product subsystem or changing the top-level runtime entry model.

### Detailed Changes

| Location | Change |
|----------|--------|
| `srcPy/artifact_registry/bundle_writer.py`, `srcPy/artifact_registry/artifact_store.py`, `srcPy/artifact_registry/artifacts.py`, `srcPy/artifact_registry/sanitization.py`, `srcPy/backtesting/storage/` | Moved real bundle-writer and bundle-artifact-store ownership into the canonical artifact registry and reduced the legacy `backtesting/storage` namespace to retired compatibility shims or placeholders with explicit rationale comments. |
| `pyproject.toml`, `marketmind_gate/cli.py`, `srcPy/cli/gate.py` | Canonicalized the gate surface so `mm-gate` and `marketmind_gate.cli` both delegate to `srcPy.cli.gate.main`; added shared failure-report helpers and `COST_GATE_REJECTED` reason-code emission on the governed path. |
| `srcPy/strategies/momentum/entry.py`, `srcPy/strategies/momentum/strategy.py`, `srcPy/strategies/momentum/artifacts/stat_validity.py`, `srcPy/strategies/pipeline_strategy.py` | Closed the remaining Phase I-E momentum blockers: optional `RunRegistry`/`LocalCAS` wiring, shared cumulative trial counters persisted in `trial_counters.json`, canonical `stat_validity_report.json` schema `v1`, fail-closed crash-override handling pending a governed source adapter, structured book-membership diagnostics, explicit unavailable `beta_reversal_score`, and a typed base-class signal-envelope contract that removes the old override suppression. |
| `tests/python/unit/cli/test_gate.py`, `tests/python/unit/strategies/momentum/`, `tests/python/integration/strategies/test_momentum_governed_path.py`, `tests/python/unit/artifact_registry/test_storage_shims.py` | Added focused coverage for the canonical CLI path, governed cost-gate rejection reporting, crash-override fail-closed behavior, shared trial counting across registry instances, canonical storage shims, and the updated momentum diagnostics/stat-validity contracts. |
| `tests/golden/adr007/`, `tests/python/unit/hashing/test_adr007_replay.py`, `srcPy/ops/hashing/canonical_frame.py` | Enriched the committed ADR-007 fixtures with concrete expected outputs, added a Python replay suite over the eight golden suites, and updated `canonical_frame.py` evidence to truthfully report Python-only D2 replay coverage while leaving `OI-15` open for three-language certification. |
| `docs/src/ResolutionLedger.md`, `docs/src/README.md`, `docs/src/ImplementationPlan.md`, `docs/src/TechnicalRoadmap.md`, `docs/src/MetaLearningCore.md` | Synchronized the companion docs to the delivered `4.5.4` state, closed the relevant Phase I-E ledger items, opened `OI-31` and `OI-32` as explicit deferrals, and updated suite references so the current release context no longer points at `4.5.3`. |

### Behavioral Changes

* Canonical governed bundle-writing and artifact-store ownership now lives only under `srcPy.artifact_registry`; the older `srcPy.backtesting.storage` path remains compatibility-only and should not be treated as an implementation surface.
* The shipped gate entrypoints now share the same exit-code and report-writing behavior because both delegate to `srcPy.cli.gate.main`.
* Governed momentum runs can record platform-managed cumulative trial counts across the three production-intended variants without relying on a private writer attribute or allowing reset-by-separate-run behavior.
* An explicitly requested crash override on the governed momentum path now fails closed with a `NotImplementedError` that points to the governed adapter backlog (**OI-34**), rather than silently accepting the FRED approximation stub as a production trigger source.
* `AlphaIR.diagnostics` now carries explicit per-symbol book membership and a truthful unavailable-state payload for `beta_reversal_score`.
* ADR-007 fixture evidence is stronger and more replayable in Python, but the project still does **not** claim D3 cross-language certification; that remains blocked on `OI-15`.

### Breaking Changes

None intended. Compatibility shims remain in place for the retired storage namespace and the gate entry surface, but the canonical ownership and documentation now point only to `srcPy.artifact_registry` and `srcPy.cli.gate`.

### Validation

| Check | Result |
|-------|--------|
| Syntax-only compile of touched Python files via `compile(...)` | Passed. |
| Companion-doc and ledger/version consistency audit | Updated to `4.5.4` current-state references and closed/open item statuses for the Phase I-E closure pass. |
| Full `pytest`, coverage, and `mypy --strict` acceptance sweep | Not run in this environment; local Linux Python lacked project test dependencies and the Windows interpreter path was blocked by the sandbox/runtime boundary. |

---

## Version 4.5.3 (2026-03-19) — Test-Suite Closure Pass: Torture-Fixture Robustness, Governed/Docs Alignment, and Runtime Hardening

Changelog for **the post-4.5.2 test-suite closure pass**: harden `dataprep_orchestrator` against BOM-heavy, ragged, empty, encoded, and cross-file torture fixtures; close the remaining governed gate and docs-manifest test mismatches; make HTTP-loader, strategy-registry, and formatting-spec behaviors fail in the precise ways the tests expect; stabilize Hypothesis/property coverage and Influx logging error handling; and harden a few runtime edges surfaced only during full-suite verification, including direct CLI execution, transient repo-copy noise in PowerShell release-doc tests, stale cache pickle recovery, and sync execution of trivial awaitables when the test harness blocks event-loop setup. This is a PATCH release because it fixes regressions and environmental brittleness on existing governed/runtime surfaces without introducing a new public subsystem or changing SemVer-visible APIs.

### Detailed Changes

| Location | Change |
|----------|--------|
| `srcPy/data/dataprep_orchestrator.py`, `tests/python/plugins/torture_plugin.py`, `tests/python/data/torture_manifest.yml` | Closed the torture-fixture failures by normalizing BOM/weird headers before timestamp validation, recognizing `effective_date` as timestamp-like, tolerating ragged/blank-line CSV probes, respecting non-UTF-8 fixture encodings and zero-byte CSVs, remapping inline spec column references after normalization, teaching torture discovery about `crossfile_prices.csv` + `crossfile_metadata.csv`, and adding a sync awaitable fallback for test harnesses that block event-loop creation. |
| `devtools/docs/release/compile_release.py` | Restricted generated companion tokens to the actual suite/non-doc IDs in the manifest so minimal catalogs no longer emit invalid `ResolutionLedger@...` tokens. |
| `tests/python/unit/gate/test_core.py`, `srcPy/pipeline/stages/market_data/sources/data_loader.py`, `tests/python/unit/test_loaders_api_edges.py`, `tests/python/unit/test_strategy_imports_and_registry.py` | Realigned governed-path and loader/registry tests with current behavior: bad governed fixtures now fail through `stat_validity_report.json`, HTTP non-200s re-raise `DataFetchError` instead of being retried as generic failures, async loader edge tests run under the repo’s network policy, and the momentum registry import-error assertion now patches the dynamic import site directly. |
| `devtools/docs/formatting/load_spec.py`, `tests/python/integration/docs/test_formatting_build_flow.py`, `devtools/docs/cli.py`, `tests/python/integration/docs/test_release_docs_ps1_integration.py` | Hardened the docs toolchain and integration tests: formatting-spec loading now fails closed when `formatting_rules` are missing, formatting-build tests accept Pandoc-first stderr, direct `devtools/docs/cli.py` execution bootstraps `sys.path` correctly, and the PowerShell release-doc tests ignore transient local scratch directories and seed a bootstrap `VERSION.md` when exercising synthetic release versions. |
| `srcPy/ops/mm_logkit.py`, `tests/python/property/hashing/test_hashing_properties.py`, `tests/python/unit/preprocessor/test_momentum_ops.py`, `tests/python/integration/test_stat_arb_vertical_slice.py`, `srcPy/strategies/pipeline_strategy.py` | Stabilized the remaining long-tail failures: InfluxDB handler error logging now guards against recursive self-reentry, hashing namespace generators exclude BOM-invalid strings, slow Hypothesis cases suppress the right health/deadline checks, the stat-arb Yahoo smoke test uses `asyncio.run(...)`, and stale/incompatible strategy-cache pickle files are treated as cache misses rather than hard failures. |

### Behavioral Changes

* CSV torture fixtures that previously failed on BOM-heavy headers, ragged lines, Latin-1 bytes, zero-byte files, and cross-file sidecars now take the tolerant ingest path expected by the integration suite without weakening malformed-file failures.
* Companion-token generation for release manifests now reflects only the docs actually present in the suite manifest, so minimal release catalogs validate cleanly.
* The docs formatting loader is stricter: a compiled FormattingSpec docmodel without `formatting_rules` now fails closed instead of silently recompiling from source.
* Runtime cache and async edges are more resilient in mixed developer/test environments: stale feature-cache pickles are discarded, and simple awaitables can still be resolved when the harness prevents normal loop creation.

### Breaking Changes

None intended. The work tightens existing runtime and tooling behavior but does not introduce a new public API surface.

### Validation

| Check | Result |
|-------|--------|
| `pytest tests/python/integration/orchestrator/test_torture_fixtures_matrix.py tests/python/integration/orchestrator/test_fetch_modes.py` | Passed (coverage gate excluded during focused verification where needed). |
| `pytest tests/python/unit/docs/test_release_compiler.py tests/python/integration/docs/test_plan_release_integration.py tests/python/integration/docs/test_formatting_build_flow.py --no-cov` | Passed. |
| `pytest tests/python/unit/gate/test_core.py tests/python/unit/test_loaders_api_edges.py tests/python/unit/test_strategy_imports_and_registry.py --no-cov` | Passed. |
| `pytest tests/python/unit/preprocessor/test_momentum_ops.py tests/python/property/hashing/test_hashing_properties.py tests/python/unit/test_mm_logkit.py::TestInfluxDBHandler::test_influx_handler_error_handling --no-cov` | Passed. |
| Follow-on regressions surfaced during full-suite verification | Fixed additional docs CLI, PowerShell release-doc, stat-arb smoke, and stale strategy-cache failures uncovered after the original 31-test closure pass. |

---

## Version 4.5.2 (2026-03-19) — ADR-009 Momentum Package Spine, Focused Test Closure, and Companion-Doc Sync

Changelog for **the ADR-009 momentum package migration pass**: replace the flat `srcPy/strategies/momentum.py` implementation with the accepted `srcPy/strategies/momentum/` package spine, split the strategy into `strategy.py`, `alpha_ir.py`, `exceptions.py`, `plans/`, `entry.py`, `artifacts/`, `validation/`, and the Phase III `control/` stub, preserve StrategyRegistry compatibility for all momentum aliases, restore the missing preprocessor momentum-op test surface, add dedicated residual-plan coverage, and synchronize the companion docs so they describe the delivered package-based momentum state rather than the earlier flat-file slice. This is a PATCH release because it closes ADR-009 follow-through, testing, and documentation gaps on an existing Phase I-E surface without introducing a new public product area or changing SemVer-visible runtime entry points.

### Detailed Changes

| Location | Change |
|----------|--------|
| `srcPy/strategies/momentum/` | Introduced the ADR-009 package spine: `__init__.py` re-export, `strategy.py` for `MomentumStrategy`, `alpha_ir.py`, `exceptions.py`, variant builders in `plans/`, governed orchestration in `entry.py`, artifact serializers in `artifacts/`, `validation/production_v1.py`, and the invariant `control/__init__.py` Phase III stub. |
| `srcPy/strategies/momentum.py`, `stubs/srcPy/strategies/momentum.pyi` | Removed the obsolete flat implementation and its stale stub after migrating callers to the package layout. |
| `srcPy/strategies/pipeline_strategy.py` | Extended lazy import support so all momentum registry aliases (`momentum`, `momentum_tsmom`, `momentum_dual`, `momentum_industry`, `momentum_residual`, `momentum_kalman`, `momentum_ensemble`, `momentum_ml`) resolve through the package entry point. |
| `srcPy/preprocessor/graph/ops_custom.py` | Kept the momentum op surface on the platform preprocessor path and aligned `momentum.industry_score` lowering with the Phase II stub contract while preserving the existing momentum op registrations and lowerings. |
| `tests/python/unit/preprocessor/test_momentum_ops.py`, `tests/python/unit/strategies/momentum/`, `tests/python/integration/strategies/test_momentum_governed_path.py` | Restored and expanded the focused momentum test surface: op-registry/lowering checks, strategy/entry/artifact coverage, residual-plan feature-flag coverage, and a governed-path integration test for bundle artifacts. |
| `pyproject.toml` | Updated pytest marker registration (`unit`) and changed the momentum coverage omit from the flat-file path to the package-path form (`srcPy/strategies/momentum/*`) so the config matches the migrated layout. |
| `docs/src/ImplementationPlan.md`, `docs/src/README.md`, `docs/src/MetaLearningCore.md`, `docs/src/TechnicalRoadmap.md`, `docs/src/ResolutionLedger.md` | Synced the companion docs to the delivered ADR-009 package migration state, closed the flat-file → package migration item, and replaced stale “migration pending” wording with the current package-spine reality while keeping open MOM blockers explicit. |

### Behavioral Changes

* `from srcPy.strategies.momentum import MomentumStrategy` still works, but the implementation now lives behind the package spine required by ADR-009.
* Momentum-specific governed execution now has a dedicated `entry.py` boundary with explicit `ConvergenceError` and `CostGateRejection` handling, signal-card/stat-validity serialization, and a package-local validation profile.
* The focused momentum test surface now explicitly covers the preprocessor momentum ops again, including denominator guards, lowering stubs, residual-plan feature flags, and the governed artifact path.
* Companion docs now describe the package-based momentum implementation as delivered work rather than a pending ADR-009 migration.

### Breaking Changes

None intended. The release preserves the public `srcPy.strategies.momentum` import surface while changing the internal file topology from a flat module to a package.

### Validation

| Check | Result |
|-------|--------|
| `python3 -m py_compile` on touched momentum Python files | Passed using `PYTHONPYCACHEPREFIX=.tmp_pycache`. |
| Focused momentum pytest surface | 47 passed. |
| Companion-doc stale wording sweep | Updated `ImplementationPlan.md`, `README.md`, `MetaLearningCore.md`, `TechnicalRoadmap.md`, and `ResolutionLedger.md` to reflect the delivered package spine and remaining open MOM items. |

---

## Version 4.5.1 (2026-03-19) — Phase I-E Governance Closure Pass: Lineage Gate, Hashing Ownership, Canonical-Frame Evidence, and Companion-Doc Sync

Changelog for **the Phase I-E governance closure pass**: complete the governed lineage gate on the canonical bundle path, route CAS JSON canonicalization through the repo-owned `srcPy.ops.hashing` surface, strengthen `canonical_frame.py` from a single status constant into an evidence-backed certification model, migrate bundle-facing artifact storage onto the canonical artifact-registry boundary, and harden the governed momentum artifact path for the non-ADR-009 slice. This release also updates the Phase I-E companion docs so `ResolutionLedger.md`, `ImplementationPlan.md`, `TechnicalRoadmap.md`, `README.md`, and `MetaLearningCore.md` describe the delivered lineage, hashing, and governed-momentum state while keeping OI-15 and ADR-009-dependent work explicitly open. This is a PATCH release because it closes governance and documentation gaps on existing Phase I-E surfaces without introducing a new public runtime subsystem.

### Detailed Changes

| Location | Change |
|----------|--------|
| `srcPy/cli/gate.py` | Added and enforced `DataLineageGate` on the canonical governed path, tightened stale in-file comments to match the live policy contract, and continued emitting `canonical_frame_ci_status` in gate metadata. The lineage gate now fails closed on missing `pit_compliant` / `knowledge_time_column`, checks content-hash mismatches, and treats stale downloads as a warning-only pass condition. |
| `srcPy/ops/hashing/canonical_frame.py` | Replaced the raw boolean-style status wiring with an evidence-backed certification model: `CanonicalFrameCIEvidence` now names Python certification, golden-vector presence, and cross-language certification explicitly, exports a machine-readable evidence dict, and derives the published CI status from that evidence rather than a bare constant. |
| `srcPy/ops/hashing/canonicalizer.py`, `srcPy/ops/hashing/__init__.py`, `srcPy/artifact_registry/cas.py` | Moved CAS JSON canonicalization behind the repo-owned hashing authority by adding `canonicalize_json_bytes()` to `srcPy.ops.hashing`, exporting it as part of the canonical surface, and updating `LocalCAS.put_json()` to consume only that surface. The gate package may remain the underlying RFC8785/JCS implementation, but ownership now sits with `srcPy.ops.hashing` rather than a direct `marketmind_gate` import from the artifact registry. |
| `srcPy/artifact_registry/run_registry.py` | Added warning logs for suppressed registry persistence failures and retained the RunRegistry-managed trial counter used by the governed momentum/stat-validity path. Silent `OSError` swallowing is now reduced to warn-and-continue behavior. |
| `srcPy/artifact_registry/bundle_writer.py`, `srcPy/artifact_registry/artifact_store.py`, `srcPy/backtesting/storage/bundle_writer.py`, `srcPy/backtesting/contracts/bundle.py` | Kept the canonical bundle-writing surface anchored on the artifact registry while preserving compatibility adapters for the older backtesting/storage namespace. This is a minimum-bar compatibility closure rather than full namespace retirement; the call-site audit remains the governing evidence for what is still transitional. |
| `srcPy/pipeline/orchestrator.py`, `marketmind_gate/gates/core.py` | The canonical orchestrator and the compatibility gate wrapper now converge on the same governed bundle validation path, including the lineage gate and canonical-frame CI-status metadata. |
| `srcPy/strategies/momentum.py`, `srcPy/backtesting/validation/statistical/validator.py` | Hardened the non-ADR-009 governed momentum slice: momentum now emits governed `execution_assumptions.json` and `stat_validity_report.json`, records a RunRegistry-backed trial counter, normalizes PBO inputs through the canonical bridge, and now fails closed if governed artifact emission lacks realized returns. |
| `docs/src/ResolutionLedger.md`, `docs/src/ImplementationPlan.md`, `docs/src/TechnicalRoadmap.md`, `docs/src/README.md`, `docs/src/MetaLearningCore.md` | Synced the companion docs to the delivered Phase I-E governance state: DataLineageGate is live, hashing/canonicalization ownership now sits behind `srcPy.ops.hashing`, canonical-frame CI reporting has an explicit evidence model, and the non-ADR-009 governed momentum slice is materially advanced while OI-15 and ADR-009-dependent migration remain open. |

### Behavioral Changes

* Governed bundle validation now includes an explicit data-lineage decision on `dataset_manifest.json` rather than relying only on downstream PIT assumptions. Missing or false `pit_compliant` and missing `knowledge_time_column` now fail the canonical gate path directly.
* CAS identity still uses the same canonical bytes and attestation pairing, but the artifact registry no longer owns a direct import dependency on `marketmind_gate` for JSON canonicalization. Canonicalization authority now flows through `srcPy.ops.hashing`.
* Canonical-frame CI reporting is no longer just a single status constant. The system now publishes both a status value and an explicit named evidence record that distinguishes Python certification, golden-vector presence, and cross-language certification.
* Governed momentum artifact emission is stricter: the non-ADR-009 slice emits execution assumptions and stat-validity artifacts through the canonical path, records a platform-managed trial counter when available, and now fails rather than fabricating returns on the governed path.

### Breaking Changes

None intended. This release closes governance and documentation gaps on top of existing 4.5.0 surfaces; OI-15 and ADR-009-dependent momentum/package work remain explicitly open.

---

## Version 4.5.0 (2026-03-18) — Phase I-E SignalFactory Substrate + Gate Hardening

Changelog for **Phase I-E amendment (SignalFactory substrate)**: additive deliverables that make the bundle and signal contract Phase II–ready without introducing Phase II logic. (1) **Stable `slot_index` on Signal ABC**: new `srcPy/registry/` package with `SignalCatalog`, monotonic slot assignment at registration (idempotent by `spec_hash`), five starter signals (stat_arb spread_zscore, hedge_ratio, momentum TSMOM, XSMOM, RSI baseline) at slots 0–4, and `pyproject.toml` entry_points for `marketmind.signals`. (2) **`screening_report.json` as first-class bundle artifact**: two-tier rejection taxonomy in `screening_taxonomy.py` with `REASON_CODE_TO_FAMILY` (callers never pass `reason_family`), `ScreeningReportBuilder` in `screening_report.py`, JSON Schema `schemas/screening_report.schema.json`, `gate_to_screening.py` mapping (marketmind_gate gate_id + status → ScreeningStage + ReasonCode, with correct stage for both pass and fail), `BundleWriter.write_screening_report()`, and orchestrator building and writing the report after validation so every strategy evaluation run emits a screening report (accepts and rejects). Full 64-char SHA-256 for `candidate_run_id` and `screening_run_id`; max_drawdown failure maps to `FEATURE_STABILITY_FAIL`. (3) **Phase I momentum core slice on the governed strategy/op path**: `MomentumStrategy` now lives under `srcPy/strategies/` with canonical `features_plan()` wiring to `momentum.*` graph ops, an `AlphaIR` return contract from `generate_signal()`, PIT provenance propagation and governed validation, and a trade-intent override that unwraps `AlphaIR.signal` while preserving the base regime/sizer/risk flow. The preprocessor op layer adds `momentum.xsec_rank`, `momentum.vol_scale`, `momentum.residual_ols`, `momentum.residual_kf`, and `momentum.industry_score`, registered through the builtin op factory with Polars lowerings and deterministic tests. Cross-sectional semantics are locked explicitly: `momentum.xsec_rank` ranks a same-date asset universe rather than a trailing single-series percentile, and `AlphaIR.information_coefficient` is only emitted for true cross-sectional universes with at least 10 assets. (4) **Type-safety (mypy --strict)**: `srcPy/preprocessor/utils/columns.py` gains typed `_as_list` and `_derive_out_names`; `srcPy/preprocessor/graph/ops_custom.py` adds `_HasContract` Protocol for `_ProvidesMixin`, TYPE_CHECKING polars import, full annotations for all Polars lowering functions and `_delegate_to_backend`, and `cast()` on `_apply_eager` returns; `pyproject.toml` adds dev dependency `pandas-stubs`; `srcPy/strategies/momentum.py` uses `# type: ignore[override]` for `generate_signal` → `AlphaIR`; `tests/python/unit/preprocessor/test_momentum_ops.py` fixes optional `pl` assignment and uses `cast(pl.LazyFrame, ...)` for `.collect()` on lowering return values. (5) **Phase I-E gate hardening in `srcPy/cli/gate.py`**: the canonical governed validation path now treats `stat_validity_report.json` and `execution_assumptions.json` as required policy artifacts, requires `pbo` in `stat_validity_report.json` with `0 <= pbo.value <= 1`, accepts nested component `gate_result` fields when present, and fails zero-cost or missing execution assumptions instead of passing with evidence-only warnings. Focused CLI regression coverage in `tests/unit/cli/test_gate.py` now covers missing statistical-validity artifacts, malformed `pbo`, missing execution assumptions, zero-cost assumptions, and valid non-zero assumptions. (6) **Phase I-E statistical-validity bridge tightening**: `srcPy/backtesting/validation/statistical/report.py` now emits top-level `pbo` while keeping `schema_version = "v1"` and aggregating top-level `gate_result` across DSR/minTRL/bootstrap/PBO; `validator.py` now accepts canonical validator-side `path_pairs` (or bridged `cpcv_evaluations`) and computes PBO via `pbo.py` using `net_sharpe`; new `pbo_bridge.py` converts evaluated CPCV outputs into the canonical `path_pairs` surface without moving computation into `gate.py` or `cpcv.py`; focused tests now cover report emission, gate-policy failures for missing/invalid `pbo`, strict `PBO > 0.50` failure behavior, and degenerate score surfaces. This is a MINOR release: new public registry package, new bundle artifact, stricter governed gate policy, new canonical momentum strategy/op surfaces, and tighter statistical-validity/report integration; public APIs remain stable.

### Detailed Changes

| Location | Change |
|----------|--------|
| `srcPy/registry/__init__.py` | New package; exports SignalCatalog, screening_taxonomy enums and REASON_CODE_TO_FAMILY, ScreeningReportBuilder, gate_result_to_stage_and_code. |
| `srcPy/registry/signal_catalog.py` | SignalProtocol, RegisteredSignal, SignalCatalog with _next_slot and register() idempotent by spec_hash; five starter stubs; get_catalog() singleton. |
| `srcPy/registry/screening_taxonomy.py` | ScreeningStage, ScreeningStatus, ReasonCode, ReasonFamily, REASON_CODE_TO_FAMILY. |
| `srcPy/registry/screening_report.py` | ScreeningReportBuilder (reason_family derived from reason_code only); full 64-char candidate_run_id. |
| `srcPy/registry/gate_to_screening.py` | GATE_STAGE_MAP and GATE_FAIL_REASON_MAP; gate_result_to_stage_and_code() uses same stage for pass/fail; max_drawdown → FEATURE_STABILITY_FAIL. |
| `schemas/screening_report.schema.json` | New schema; pattern ^[a-f0-9]{64}$ for candidate_run_id and screening_run_id. |
| `srcPy/backtesting/storage/bundle_writer.py` | write_screening_report(payload). |
| `srcPy/pipeline/orchestrator.py` | Build ScreeningReportBuilder after validate_bundle(), map gates via gate_to_screening, write_screening_report() before write_bundle_manifest(); full 64-char screening_run_id. |
| `pyproject.toml` | [tool.poetry.plugins."marketmind.signals"] with five starter signal entry points. |
| `tests/python/unit/registry/` | test_signal_catalog.py, test_screening_report.py, test_gate_to_screening.py. |
| `tests/python/integration/backtesting/test_orchestrator_backtesting_artifacts.py` | Assert screening_report.json present and has schema_version, candidates, summary. |
| `srcPy/cli/gate.py` | Phase I-E hardening: require `stat_validity_report.json` and `execution_assumptions.json` on the canonical governed path, require `pbo` with range validation, preserve invalid-input behavior for malformed policy artifacts, and fail zero-cost execution assumptions. |
| `tests/unit/cli/test_gate.py` | Added canonical-policy coverage for missing `stat_validity_report.json`, missing top-level `pbo`, malformed `pbo.value`, invalid nested `pbo.gate_result`, missing execution assumptions, zero-cost execution assumptions, and valid non-zero execution assumptions. |
| `srcPy/backtesting/validation/statistical/pbo_bridge.py` | Added the thin CPCV-to-PBO bridge that converts evaluated CPCV outputs into canonical validator-side `path_pairs` using `net_sharpe`, while rejecting duplicate `(trial_id, path_id)` pairs and incomplete rectangular score surfaces. |
| `srcPy/backtesting/validation/statistical/validator.py` | Canonical validator-side PBO integration: resolves `pbo_path_pairs` or bridged `cpcv_evaluations`, computes PBO through `pbo.py`, aligns DSR `n_trials` to the score surface, and keeps statistical computation out of `gate.py`. |
| `srcPy/backtesting/validation/statistical/report.py` | `stat_validity_report.json` now always emits top-level `pbo` in schema `v1`, preserves validator-supplied `pbo.gate_result`, and aggregates top-level `gate_result` across DSR, minTRL, bootstrap CI, and PBO. |
| `tests/python/unit/backtest/test_stat_validity.py` | Added deterministic coverage for report emission, schema `v1` retention, top-level `gate_result` aggregation including PBO, validator-side CPCV bridging, and degenerate PBO input handling. |
| `srcPy/strategies/momentum.py` | Added `AlphaIR`, `FeatureFlagError`, and `MomentumStrategy` with eight registered momentum variants, canonical `features_plan()` wiring to `_OP_REGISTRY` keys, governed PIT provenance validation inside `generate_signal()`, cross-sectional IC gating at a minimum 10-asset universe, and a `generate_trade_intent()` override that unwraps `AlphaIR.signal` before delegating through regime/sizer/risk behavior. |
| `srcPy/preprocessor/graph/ops_custom.py` | Added `XSecRank`, `VolScale`, `ResidualOLS`, `ResidualKF`, and `IndustryScore` ops plus Polars lowerings for the `momentum.*` registry. `momentum.xsec_rank` now computes a lagged lookback signal per asset and ranks it cross-sectionally within each date; `momentum.vol_scale` annualizes with `sqrt(252)` and fail-closed denominator guards; Kalman lowering remains an explicit Phase III `NotImplementedError` tied to OI-MOM-005. |
| `srcPy/preprocessor/graph/factory.py` | Registered all five `momentum.*` ops in `register_builtin_ops()` so `MomentumStrategy.features_plan()` resolves entirely through the canonical op registry. |
| `tests/python/unit/strategies/test_momentum.py` | Added deterministic coverage for registry resolution, feature-plan stability, Kalman feature-flag gating, stable `AlphaIR` return semantics, PIT provenance propagation, cross-sectional IC behavior (`None` below 10 assets; computed at 10+), and trade-intent unwrapping. |
| `tests/python/unit/preprocessor/test_momentum_ops.py` | Added deterministic/property coverage for momentum-op registry presence, IR contracts, true same-date cross-sectional ranking semantics, vol-scale denominator guards and annualization, and deferred Kalman lowering behavior. |
| **Type-safety (mypy --strict)** | |
| `srcPy/preprocessor/utils/columns.py` | Typed `_as_list(x: Union[str, List[str], Tuple[str, ...], None]) -> List[str]` and `_derive_out_names(..., out_col: Union[str, List[str], None]) -> List[str]`. |
| `srcPy/preprocessor/graph/ops_custom.py` | `_HasContract` Protocol for `_ProvidesMixin._with_contracts`; TYPE_CHECKING import of `polars`; full signatures for `_delegate_to_backend` and all `lower_*_polars` (ir, lf, group_by) with return `pl.LazyFrame` or `pl.DataFrame`; `lower_residual_kf_polars` accepts `lf` or `None`; `cast(..., _apply_eager(...))` on returns. |
| `pyproject.toml` | Dev dependency `pandas-stubs = "^2.2"`. |
| `srcPy/strategies/momentum.py` | `generate_signal(...) -> AlphaIR` with `# type: ignore[override]`. |
| `tests/python/unit/preprocessor/test_momentum_ops.py` | `pl = None  # type: ignore[assignment]` on ImportError; `cast(pl.LazyFrame, lower_*_polars(...))` before `.collect()` where needed. |

### Behavioral Changes

* Every run that goes through the canonical orchestrator and gate validation now emits `screening_report.json` in the bundle with one candidate per strategy evaluated, stages derived from gate results (INTAKE for files_exist/json_valid, LANE_0 for sharpe_threshold/max_drawdown), and reason_family always derived from REASON_CODE_TO_FAMILY.
* SignalCatalog is available via `get_catalog()` with five starter signals registered at slots 0–4; new signals can be registered with stable slot_index for Phase II replay compatibility.
* The governed strategy layer now includes a canonical momentum slice: `MomentumStrategy.features_plan()` resolves through `_OP_REGISTRY`, `generate_signal()` has a stable `AlphaIR` contract, and trade-intent generation unwraps `AlphaIR.signal` without redefining the public signal interface.
* Cross-sectional momentum semantics are now explicit in both strategy and op layers: `momentum.xsec_rank` ranks across assets within a date, not across time for one series, and `information_coefficient` remains `None` unless the cross-section has at least 10 assets.
* Canonical governed stat-validity emission now includes a top-level `pbo` section in `stat_validity_report.json` while keeping `schema_version = "v1"`; the report's top-level `gate_result` now reflects DSR, minTRL, bootstrap CI, and PBO, and malformed `pbo` values or malformed nested gate payloads remain invalid-input failures rather than recomputation triggers.
* Canonical governed bundle validation now requires `execution_assumptions.json`; missing assumptions and zero-cost assumptions fail the gate instead of passing with evidence-only warnings, while valid non-zero assumptions still pass.
* `mypy --strict` passes for `srcPy/strategies/momentum.py`, `srcPy/preprocessor/graph/ops_custom.py`, and the unit tests `test_momentum.py` and `test_momentum_ops.py`; pandas usage is typed via `pandas-stubs`.

### Breaking Changes

* Canonical governed bundle validation is stricter in 4.5.0: missing `stat_validity_report.json`, missing `execution_assumptions.json`, malformed or missing `pbo`, and zero-cost execution assumptions now fail where earlier compatibility behavior could pass with warnings or evidence-only signals.

### Companion Document Updates (specific edits)

Apply the following updates so companion docs reflect 4.5.0 and Phase I-E substrate delivery.

| Document | Location | Update |
|----------|----------|--------|
| **ImplementationPlan.md** | Line 10 (title page) | Change `VERSION.md 4.4.2` → `VERSION.md 4.5.0`. |
| **ImplementationPlan.md** | Line 25–27 (Executive Summary) | After the sentence that ends with "Phase I-D lands the first non-toy strategy vertical slice...", add: "Phase I-E (SignalFactory substrate) is now partially delivered in 4.5.0: `srcPy/registry/` provides SignalCatalog with stable slot_index at registration and five starter signals, and `screening_report.json` is emitted for every strategy evaluation run with two-tier rejection taxonomy and REASON_CODE_TO_FAMILY." Change "Phase I-E and Phase I-F now carry" → "Phase I-F now carries" (and adjust the following clause to "complete the remaining gate/governance surface..."). |
| **ImplementationPlan.md** | RECENT_CHANGES table (~line 31) | Add row: "4.5.0 sync \| March 2026 \| Phase I-E SignalFactory substrate: srcPy/registry/ (SignalCatalog, slot_index, screening_taxonomy, screening_report builder, gate_to_screening), screening_report.json in bundle, schemas/screening_report.schema.json." |
| **ImplementationPlan.md** | §4.6 Phase I-E (line ~525) | After "Phase I-E completes the gate surface...", add one sentence: "The Phase I-E amendment (SignalFactory substrate) delivered in 4.5.0 adds the SignalCatalog with slot_index and screening_report.json emission so the bundle and signal identity are Phase II–ready; remaining Phase I-E work (stat validity/cost/data lineage gate verification, backtesting/storage retirement) is unchanged." |
| **ImplementationPlan.md** | Line 2042 (footer) | Change `VERSION.md 4.4.2` → `VERSION.md 4.5.0`. |
| **TechnicalRoadmap.md** | Line 8 (title page) | Change `VERSION.md 4.4.2` → `VERSION.md 4.5.0`. |
| **TechnicalRoadmap.md** | Signal registry row (~line 58) | Change "No Signal ABC, no catalog, no CAS for signals. Phase II: each signal must carry task_embedding field" to "Phase I-E (4.5.0): SignalCatalog in srcPy/registry/ with slot_index at registration and five starter signals; screening_report.json emitted per run. Phase II: task_embedding (signal_embedding) and meta-learner integration." |
| **TechnicalRoadmap.md** | Phase I subphases paragraph (~line 839) | After "Phase I-D is delivered in 4.4.0...", add: "Phase I-E (SignalFactory substrate) is partially delivered in 4.5.0: SignalCatalog + slot_index and screening_report.json with taxonomy and gate_to_screening mapping." |
| **TechnicalRoadmap.md** | Line 947, 1091 (VERSION.md refs) | Change `4.4.2` → `4.5.0`. |
| **MetaLearningArchitectureVision.md** | Line 8 (title page) | Change `VERSION.md 4.4.2` → `VERSION.md 4.5.0`. |
| **MetaLearningArchitectureVision.md** | §8b Post-3.6.0 Additions (~line 542) | Change "through v4.4.0" → "through v4.5.0". Add bullet: "SignalCatalog + slot_index (4.5.0): srcPy/registry/signal_catalog.py implements Signal ABC with slot_index assigned at registration; five starter signals; screening_report.json and REASON_CODE_TO_FAMILY in srcPy/registry/ for Phase II funnel analytics." |
| **MetaLearningArchitectureVision.md** | Line 578, 584 (VERSION.md refs) | Change `4.4.2` → `4.5.0`. |
| **MetaLearningCore.md** | Line 8, 30 (title page / table) | Change `VERSION.md 4.4.2` → `VERSION.md 4.5.0`. |
| **MetaLearningCore.md** | Strategy registry & feature path row (~line 565) | Append: "Phase I-E (4.5.0) adds srcPy/registry/signal_catalog.py (SignalCatalog, slot_index) and screening_report.json emission with screening_taxonomy and gate_to_screening." |
| **MetaLearningCore.md** | Current state paragraph (~line 651) | Add: "Phase I-E SignalFactory substrate (4.5.0) delivers SignalCatalog with slot_index and screening_report.json so the bundle and signal identity are Phase II–ready." |
| **MetaLearningCore.md** | Line 781 (footer) | Change `VERSION.md 4.4.2` → `VERSION.md 4.5.0`. |
| **README.md** | Line 12 (title page) | Change `VERSION.md 4.4.2` → `VERSION.md 4.5.0`. |
| **README.md** | Line 166 (Version) | Change "4.4.0 \| Phase 0 complete... Phase I-D strategy slice" to "4.5.0 \| Phase 0 complete; Phase I-B/C/D delivered; Phase I-E SignalFactory substrate (SignalCatalog + slot_index, screening_report.json) delivered." |
| **README.md** | Line 198 | Add after "Phase I-D lands \`stat_arb_pairs\`...": "Phase I-E (4.5.0) adds SignalCatalog with slot_index and screening_report.json per run. Remaining Phase I work is I-E gate verification plus I-F architecture closure." Adjust "Remaining Phase I work is I-E" to "Remaining Phase I work is I-F" if that sentence follows. |
| **README.md** | Line 937 (RECENT_CHANGES) | Add row: "4.5.0 \| March 2026 \| Phase I-E SignalFactory substrate: srcPy/registry/ (SignalCatalog, screening_report, taxonomy, gate_to_screening), screening_report.json in bundle." |
| **README.md** | Line 946 (Next) | Change "4.5.x (Phase I-E / I-F" to "4.5.x (Phase I-F" and "gate completeness" to "remaining gate verification and architecture closure". |
| **README.md** | Line 925, 961 (VERSION.md refs) | Change `4.4.2` → `4.5.0`. |
| **FormattingSpec.md** | Line 8 | Change `VERSION.md 4.4.2` → `VERSION.md 4.5.0`. |
| **ResolutionLedger.md** | `docs/src/ResolutionLedger.md` (title page + DOCBODY wrappers) | Added `ResolutionLedger` as a new bumpable suite companion document for 4.5.0; wrapped title page and content in `MM:BEGIN:TITLEPAGE` / `MM:END:TITLEPAGE` and `MM:BEGIN:DOCBODY` / `MM:END:DOCBODY` so it compiles into `docs/out/<release>/ResolutionLedger.docx` and participates in companion version sync. |
| **ImplementationPlan.md** | §4.6 Phase I-E | Record that canonical `gate.py` now requires `stat_validity_report.json` and `execution_assumptions.json`, requires `pbo`, and fails zero-cost execution assumptions on governed bundles. |
| **TechnicalRoadmap.md** | Gate status rows / execution-cost notes | Update Phase I-E status to reflect required `pbo`, required governed execution assumptions, and zero-cost FAIL policy on the canonical gate path. |
| **README.md**, **MetaLearningCore.md**, **WhitePaper.md** | Phase I status summaries | Move Phase I-E gate hardening from “remaining verification” into delivered 4.5.0 behavior and leave Phase I-F / data-lineage closure as the primary remaining follow-on work. |
| **ImplementationPlan.md** | Appendix H.8 / H.9 | Correct the live governed `stat_validity_report.json` contract to schema `v1`, document top-level `pbo` plus aggregated `gate_result`, and keep Harvey-t / CPCV-config / feature-stability fields as future-phase extensions rather than the current governed artifact contract. |
| **TechnicalRoadmap.md** | Statistical validity row / current-state notes | Record that governed stat-validity emission now writes top-level `pbo` in the live `v1` contract and that validator-side CPCV evaluations bridge into canonical `path_pairs`; keep deeper CPCV/PBO promotion gating as Phase II work. |
| **README.md**, **MetaLearningCore.md**, **WhitePaper.md** | Phase I current-state summaries | Record that the canonical statistical validator/report path now emits top-level `pbo` in `stat_validity_report.json`, with validator-side CPCV score-surface bridging and top-level gate aggregation, while deeper promotion gating remains a Phase II concern. |

### Validation

| Check | Result |
|-------|--------|
| pytest tests/python/unit/registry/ | 18 passed. |
| pytest test_orchestrator_backtesting_artifacts | screening_report.json present and structured. |
| mypy srcPy/registry/ | Clean. |
| mypy --strict srcPy/strategies/momentum.py srcPy/preprocessor/graph/ops_custom.py tests/python/unit/strategies/test_momentum.py tests/python/unit/preprocessor/test_momentum_ops.py | Success; no issues in 4 source files. |
| `python -m py_compile srcPy/backtesting/validation/statistical/pbo_bridge.py srcPy/backtesting/validation/statistical/report.py srcPy/backtesting/validation/statistical/validator.py tests/python/unit/backtest/test_stat_validity.py tests/unit/cli/test_gate.py` | Syntax validation for the Phase I-E statistical-validity bridge and focused tests passed in this thread. |
| Direct Phase I-E contract checks | Verified top-level `pbo`, schema `v1`, aggregated `gate_result`, validator-side CPCV bridging, strict `PBO > 0.50` failure behavior, and duplicate/incomplete score-surface rejection. |
| Targeted pytest for the Phase I-E stat-validity slice | Not completed in this thread because the local `.venv-codex` environment lacked `scipy` and Windows temp-dir cleanup raised `WinError 5` even with `--basetemp`. |

---

## Version 4.4.2 (2026-03-17)

Changelog for **companion documentation cleanup and DOCX typography normalization**: the five companion Markdown sources now drop managed `RELEASE_NOTE` blocks, standalone `✦ v...` callouts, stale companion-version suffixes, and `*Architecture source:*` footers; `TechnicalRoadmap.md` compresses the targeted §2 research-topic sections into decision bullets and renames the §3 execution tasks from `P1`-`P15` to `T1`-`T15`; and the docs formatting spec plus Python DOCX renderer/reference-doc generator are aligned to the smaller body/heading/table/code typography requested for the companion suite. This is a PATCH release because it updates editorial content and documentation-rendering presentation only; no trading runtime behavior, gate contracts, schemas, or public APIs change.

### Detailed Changes

| Location | Change |
|----------|--------|
| `docs/src/TechnicalRoadmap.md` | Removed release-note/callout clutter, collapsed the five targeted `Research Topics` sections to compact implementation-focused bullets, and renamed the §3 execution task labels to the `T1`-`T15` series with cross-references updated. |
| `docs/src/ImplementationPlan.md` | Removed the managed release-note block, standalone version callouts, stale inline release suffixes, and `*Architecture source:*` footers while preserving existing `*Source:*` citations and companion structure. |
| `docs/src/MetaLearningCore.md` | Removed the managed release-note block and stale companion-version suffixes, and normalized DOCMAP/source-stamp prose to versionless companion references. |
| `docs/src/MetaLearningArchitectureVision.md` | Removed the managed release-note block and stale companion-version suffixes, and normalized companion-reference prose and DOCMAP metadata. |
| `docs/src/README.md` | Removed the managed release-note block, remaining standalone `✦ v...` callouts, and stale companion-version suffixes while preserving suite navigation and source citations. |
| `docs/src/FormattingSpec.md` | Updated the documentation formatting reference to 10pt body, 13pt H1, 11pt H2, 10pt H3, 10pt table body, 9pt code, and reduced H1 spacing. |
| `devtools/docs/rendering/post_process.py` | Updated the runtime DOCX post-processor so generated companion documents enforce the new heading/body/code/table typography and tighter H1 spacing. |
| `devtools/docs/resources/create_reference_docx.py` | Updated the reference-doc generator so built-in paragraph styles and title-page styles match the normalized companion-suite typography. |

### Behavioral Changes

* Generated DOCX companion output now renders with smaller body/headings/code typography and reduced H1 spacing.
* Companion prose and managed metadata blocks no longer carry stale release-note callouts or embedded companion-document version suffixes.
* `TechnicalRoadmap.md` now uses `T1`-`T15` for §3 execution tasks, avoiding collision with the separate Research Agenda priority labels.

### Breaking Changes

None intended. Document content is editorially cleaner and the DOCX presentation is smaller, but no code-facing contracts or runtime entry points change.

### Companion Document State

| Document | State after 4.4.2 |
|---|---|
| `docs/src/TechnicalRoadmap.md` | Editorial cleanup applied; §2 targeted research-topic blocks compacted; §3 task labels normalized to `T1`-`T15`. |
| `docs/src/ImplementationPlan.md` | Editorial cleanup applied; stale release callouts and architecture-source footers removed. |
| `docs/src/MetaLearningCore.md` | Editorial cleanup applied; companion references/DOCMAP normalized. |
| `docs/src/MetaLearningArchitectureVision.md` | Editorial cleanup applied; companion references/DOCMAP normalized. |
| `docs/src/README.md` | Editorial cleanup applied; stale release callouts removed. |
| `docs/src/FormattingSpec.md` | Typography reference synchronized to the reduced DOCX sizes. |

### Validation

| Check | Result |
|-------|--------|
| `docs/src/*.md` cleanup search | No remaining `RELEASE_NOTE`, `✦ v`, bare release parentheticals, or `Architecture source:` hits in the five companion sources. |
| `TechnicalRoadmap.md` task-label audit | `### T1`-`### T9` headings present; no `### P1`-`### P9`; no remaining `P1`-`P15` execution-label references. |
| DOCMAP audit | Companion DOCMAP version cells now render as `—`. |
| Citation preservation | `Strategy I/O Contract v2` and `*Source:` lines remain present where required. |
| Line endings | The five companion Markdown sources were rewritten and verified as CRLF-only. |
| Python syntax | `devtools/docs/rendering/post_process.py` and `devtools/docs/resources/create_reference_docx.py` compile via `py_compile`. |

### Deferred

* No Phase I-E / I-F implementation work is included in 4.4.2; this release is limited to companion-doc cleanup and docs-rendering presentation alignment.
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














