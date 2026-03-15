# Programming Guidelines

Version 3.0 · March 2026

Engineering principles for abstract, type-guided, declarative, extensible, combinatoric, pipeline-oriented, parallel, and adaptive system design.

Audience: internal engineering and technical stakeholders.

## 1. Purpose

These guidelines define how MarketMind code should be written and structured when the goal is maximum abstraction, type-guided composition, declarative construction, combinatoric exploration, pipeline-oriented execution, parallel scalability, and computational efficiency. The codebase is designed to evolve under non-stationarity; therefore factories, registries, schemas, and explicit execution plans are non-negotiable.

## 2. North-Star Constraints

The system must remain point-in-time correct, gate-governed, reproducible within defined determinism tiers, auditable via content-addressed artifacts, and observable in production.

**Decision:** correctness beats speed when they conflict.

If a performance optimization undermines PIT integrity, determinism, schema validity, or gate validity, it is rejected. Speed work is allowed only inside the functional core, behind invariant tests and explicit instrumentation.

## 3. Core Engineering Model

### 3.1 Abstract and Type-Guided by Default

Design around contracts (`Protocol`, ABC, typed boundary model), not concrete classes. Implementation types must be swappable without touching callers. Prefer narrow behavioral interfaces, typed value objects, and fixed-shape IRs with masking over ad hoc polymorphism and deep inheritance.

### 3.2 Extensible, Registry-Driven Composition

All extensible capabilities register into explicit registries. No static wiring for signals, ops, strategies, allocators, planners, gates, or cost/execution models unless it is a deliberate, measured hot path.

Multiple authoring surfaces may exist temporarily for compatibility, but each subsystem must lower into a single canonical IR, planner, or executor path. Parallel execution models for the same semantic layer are transitional only.

### 3.3 Declarative, Schema-First Construction

Variation should be expressed in manifests, schemas, typed configs, and IR dimensions before it is expressed in imperative branching. Boundary objects must be validated at construction time. Invalid states should fail early, structurally, and with typed errors.

**Decision:** new variation enters through schema first.

### 3.4 Factory-First Systems

Prefer factory code over hand-wired implementations. Factories are the multiplication layer: they generate graphs, plans, pipelines, and combinatoric variants safely.

Factory code should focus on:

- canonical IR construction
- validation at boundaries
- lowering or compilation to efficient execution plans
- stable hashes and keys for reuse
- parallel-friendly partitioning
- emission of reproducibility metadata

**Decision:** factories own combinatorics.

### 3.5 Combinatoric by Design

Every module should be composable: small primitives that can be recombined by a factory. If a new variant is needed, add it as a manifest dimension, planner rule, or registry entry.

### 3.6 Pipeline-Oriented Architecture

Model the system as explicit stages with typed handoff points:

`specification -> IR -> validated IR -> plan -> execution -> artifacts -> gates`

Planning, execution, and evaluation should not collapse into opaque control flow.

### 3.7 Batch, Vectorized, and Parallel Execution

Assume large universes, many tasks, and many folds. Prefer columnar or vectorized compute over Python loops, prefer batch ops over per-symbol calls, and design functions to be embarrassingly parallel over symbols, folds, and regime episodes.

### 3.8 Efficiency Over Readability (With Guardrails)

Dense implementations are acceptable in explicit hot paths when they are heavily tested, instrumented, contract-bounded, interface-isolated, and justified by profiling or benchmarks.

## 4. Architecture Rules

### 4.1 Functional Core / Imperative Shell

All computational logic should be pure and deterministic where possible. Side effects live in the shell.

### 4.2 Fixed-Dimensional Interfaces with Masking

Prefer fixed-shape tensors, vectors, or matrices with masks over dynamic resizing for replay compatibility, caching, planning simplicity, and efficient kernels.

### 4.3 Point-in-Time Discipline

All market, fundamental, and macro data access must flow through the PIT front door (for example `DataView.as_of(T)`) that enforces valid-time and knowledge-time boundaries.

### 4.4 Determinism Tiers

Every pipeline declares its determinism tier requirement. Seed derivation, ordering, partitioning, and aggregation rules should be explicit. If a result is not deterministic within its required tier, it is not promotable.

### 4.5 Value Semantics and Mutation Discipline

Prefer immutable or effectively immutable value objects for manifests, IR nodes, plans, descriptors, and artifact metadata. Hidden mutation across planning or execution boundaries is forbidden.

## 5. Performance Engineering Rules

### 5.1 Hot Paths Are Explicit

Performance-critical sections must be isolated and labeled. Profiling and benchmarks should justify micro-optimizations.

### 5.2 Memory and Copy Discipline

Minimize materializations, copies, and conversions. Cache at the correct layer, and ensure cache keys include schema versions, registry versions, and PIT boundaries where relevant.

### 5.3 Parallel Execution Model

Write compute in forms that can map cleanly to multiprocessing, thread pools, vectorized kernels, GPU batches, or distributed schedulers. Partition along stable axes and keep cross-partition communication coarse-grained and minimal.

## 6. Testing and Gates

### 6.1 Invariants Over Examples

Use property-based testing for invariants such as leakage, PIT boundaries, determinism, monotonicity, stability bounds, schema and IR round-trips, hash stability, and planner idempotence.

Examples are useful. Invariants are authoritative.

### 6.2 Gate-Oriented Development

Every new capability must expose measurable outputs for gates: statistical validity, cost realism, meta-validity, PIT, determinism, and execution integrity. If it cannot be gated, it is not done.

## 7. Operational Visibility and Failure Discipline

No `print` statements. Use structured logging, tracing, and explicit execution metadata. Every plan, execution, and artifact should be traceable to its inputs, registry state, and determinism tier.

### 7.1 Exception Handling

Error handling must be precise, typed, and domain-aware. Bare `except:` is forbidden. `except Exception:` is allowed only for structured logging followed by immediate re-raise, translation to a typed domain error, or controlled boundary handling with explicit policy.

### 7.2 Reproducibility Metadata

Executions must emit enough metadata to explain and reconstruct a result: spec hash, registry versions, planner version, seed lineage, PIT boundary, determinism tier, partition identity, and artifact lineage.

## 8. Evolution and Adaptation

Expect signal churn, model drift, and regime drift. Design for replacement, not permanence. Factories, schemas, registries, and planners are the evolution surface; gates, typed boundaries, and artifact lineage are the safety surface.
