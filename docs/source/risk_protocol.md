# RiskFn Protocol

## Purpose

Define the governed boundary between allocator outputs and risk/exposure control.

## Phase Ownership

- Phase I-G freezes the protocol.
- Phase II-0 scaffolds report and interface surfaces.
- Phase II implements only the minimum allocator-to-risk boundary needed for governed validation.
- Phase III is where execution-serious calibration and operator enforcement may expand.

## Protocol Scope

- permitted allocator outputs consumed by RiskFn,
- exposure attenuation semantics for `confidence_scalar`,
- risk-budgeting interface expectations,
- invariants that remain outside Phase II scope,
- report fields needed for auditability and rollback.

## Guardrails

- RiskFn is not a placeholder.
- Phase II may define the interface boundary without implying full execution realism.
- Phase III is the first phase allowed to become execution-serious.

## Required Outputs

- protocol summary,
- versioned interface notes,
- unresolved `⚑ VALIDATE` thresholds,
- handoff notes for [paper_trade_sim_spec.md](paper_trade_sim_spec.md).
