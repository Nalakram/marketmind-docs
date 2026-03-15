# Reproducibility

> **Draft Notice:**  
> This document is a draft and not yet implemented. The practices described here are under review and may change. Until finalized, do not assume full adherence to the details in this policy.

Reproducibility instructions are provided solely to assist authorized users in verifying their own local runs and do not grant any right to access, copy, or modify source code or model weights. All use remains strictly subject to the proprietary license.

MarketMind is designed to produce deterministic research artifacts.

## Dataset Versioning

Datasets are content-addressed using BLAKE3 hashes.

## Deterministic Training

Fixed seeds are propagated through the computation graph.

## Environment Locking

Docker images and pinned dependency lockfiles are used to stabilize environments.

## Artifact Registry

Run artifacts are stored through content-addressable storage infrastructure.

## Reproducing a Run

```text
marketmind replay run_bundle_v1/<hash>
```
