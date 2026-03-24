# Paper Trade Simulation Spec

## Purpose

Define the minimum simulation realism required before allocator validation can become execution-serious.

## Phase Relationship

- Phase I-G defines the requirements.
- Phase II may prepare handoff assumptions without implementing the full system.
- Phase III is the first phase allowed to build the full paper-trading realism stack.

## Required Simulation Surfaces

- slippage and market-impact assumptions,
- liquidity and participation constraints,
- fill and partial-fill semantics,
- rebalance cadence assumptions,
- operator-visible incident and kill-switch hooks.

## Guardrails

- Paper-trading implementation is not Phase I-F work.
- Simulation realism is necessary for credibility but remains conditional on allocator validation and product need.
- Broker connectivity is not implied by this specification.

## Expected Outputs

- versioned simulation assumptions,
- calibration inputs and acceptance notes,
- handoff boundary to broker/operator work,
- explicit list of realism gaps that remain out of scope.
