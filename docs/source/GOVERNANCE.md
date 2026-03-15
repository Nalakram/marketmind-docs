# Governance

> **Draft Notice:**  
> This document is a draft and not yet implemented. The practices described here are under review and may change. Until finalized, do not assume full adherence to the details in this policy.

This Governance document is provided for informational purposes only and does not modify or supplement the proprietary license. All model promotion and use remain strictly subject to the license and [Risk Disclosure](RISK_DISCLOSURE.md).

MarketMind follows a controlled model lifecycle to ensure safety and quality.

## Model Promotion Process

Training -> Registry -> Shadow -> Canary -> Production -> Rollback

## Validation Gates and Authority

All promotions require passing:

- DSR
- PBO
- Harvey t
- Crisis holdouts (2008, 2020)

Gate authority rests exclusively with the copyright holder or designated maintainer.

## Rollback Rules

Any model showing IC drift, feature drift, or negative PnL attribution in production is immediately rolled back to the last passing Shadow or Canary version.

## Release Procedures

Releases are built from the private repository only. No public distribution or community contributions are permitted.

This governance framework demonstrates institutional-grade controls while preserving the project’s proprietary operating model.
