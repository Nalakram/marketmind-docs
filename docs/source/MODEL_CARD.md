# MarketMind Model Card v1.2

> **Draft Notice:**  
> This document is a draft and not yet implemented. The practices described here are under review and may change. Until finalized, this Model Card does not modify or supplement the proprietary license.

This Model Card is provided for informational purposes only and does not modify or supplement the proprietary license. All model use is strictly subject to the license and [Risk Disclosure](RISK_DISCLOSURE.md).

## Model Overview

- Architecture: Reptile meta-learning allocator
- Output: signal allocation weights `ΔK`
- Training regime: regime-indexed tasks (`trend × vol × BOCPD`)

## Intended Use

Adaptive signal allocation for US equities and ETFs.

## Not Intended For

- Intraday high-frequency trading
- Illiquid micro-cap assets
- Derivatives pricing

## Training Data

2000-2024 US equities plus macro features.

## Validation Gates

- DSR
- PBO
- Harvey t
- Crisis holdouts (2008, 2020)

## Known Limitations

Regime transitions slower than one week may degrade performance.

## Monitoring

- IC drift
- Feature drift
- PnL attribution
