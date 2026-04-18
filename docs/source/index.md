# MarketMind Documentation

Read the Docs for `marketmind-docs` is the publication layer for canonical documentation **mirrored** from the `MarketMind` repository. Companion Markdown under `docs/source/` is copied from `MarketMind/docs/src/`; the release ledger at the repo root is `VERSION.md` (same file as MarketMind for the aligned release). The published surface follows the current companion suite (README, white paper, implementation plan, roadmap, meta-learning specifications, resolution ledger, governance registers, Phase II contract/playbook, protocols, specifications, and appendices).

Older secondary pages (governance/legal stubs, contributor guides, tutorials) remain published alongside the mirrored suite; they are **not** sourced from `MarketMind/docs/src/` unless noted otherwise.

## Published Sections

### Overview

- [README / Technical Overview](README.md)
- [White Paper](WhitePaper.md)
- [Release History](CHANGELOG.md)

### Companion Suite

- [Implementation Plan](ImplementationPlan.md)
- [Technical Roadmap](TechnicalRoadmap.md)
- [Meta-Learning Core](MetaLearningCore.md)
- [Meta-Learning Architecture Vision](MetaLearningArchitectureVision.md)
- [Resolution Ledger](ResolutionLedger.md)

### Governance / Phase II Controls

- [Threshold Governance Register](ThresholdGovernanceRegister.md)
- [Data Governance Charter](DataGovernanceCharter.md)
- [Phase II Artifact Contract](PhaseIIArtifactContract.md)
- [Phase II Research Execution Playbook](PhaseIIResearchExecutionPlaybook.md)

### Protocols and Appendices

- [RiskFn Protocol](risk_protocol.md)
- [Signal Generation Protocol](signal_generation_protocol.md)
- [Task Validity Pilot Report](task_validity_pilot_report.md)
- [Paper Trade Simulation Spec](paper_trade_sim_spec.md)
- [Formatting Spec](FormattingSpec.md)
- [Signal universe expansion policy](signal_universe_expansion_policy.md)
- [Signal reliability schema (v0.1.1)](signal_reliability_schema_v0_1_1.md)
- [Alt-data admissibility](alt_data_admissibility.md)

### Governance and Legal

- [Governance](GOVERNANCE.md)
- [Model Card](MODEL_CARD.md)
- [Privacy Policy](PRIVACY_POLICY.md)
- [Risk Disclosure](RISK_DISCLOSURE.md)
- [Reproducibility](REPRODUCIBILITY.md)
- [Security Policy](SECURITY.md)
- [License](LICENSE.md)

### Contributor and Engineering Guidance

- [Programming Guidelines](contributors/coding_standards.md)

### Reference

- [API Reference](reference/index.rst)

```{toctree}
:hidden:
:maxdepth: 2
:caption: Overview

README / Technical Overview <README.md>
White Paper <WhitePaper.md>
Release History <CHANGELOG.md>
```

```{toctree}
:hidden:
:maxdepth: 2
:caption: Companion Suite

Implementation Plan <ImplementationPlan.md>
Technical Roadmap <TechnicalRoadmap.md>
Meta-Learning Core <MetaLearningCore.md>
Meta-Learning Architecture Vision <MetaLearningArchitectureVision.md>
Resolution Ledger <ResolutionLedger.md>
```

```{toctree}
:hidden:
:maxdepth: 2
:caption: Governance / Phase II Controls

Threshold Governance Register <ThresholdGovernanceRegister.md>
Data Governance Charter <DataGovernanceCharter.md>
Phase II Artifact Contract <PhaseIIArtifactContract.md>
Phase II Research Execution Playbook <PhaseIIResearchExecutionPlaybook.md>
```

```{toctree}
:hidden:
:maxdepth: 2
:caption: Protocols and Appendices

RiskFn Protocol <risk_protocol.md>
Signal Generation Protocol <signal_generation_protocol.md>
Task Validity Pilot Report <task_validity_pilot_report.md>
Paper Trade Simulation Spec <paper_trade_sim_spec.md>
Formatting Spec <FormattingSpec.md>
Signal universe expansion policy <signal_universe_expansion_policy.md>
Signal reliability schema (v0.1.1) <signal_reliability_schema_v0_1_1.md>
Alt-data admissibility <alt_data_admissibility.md>
```

```{toctree}
:hidden:
:maxdepth: 2
:caption: Governance and Legal

Governance <GOVERNANCE.md>
Model Card <MODEL_CARD.md>
Privacy Policy <PRIVACY_POLICY.md>
Risk Disclosure <RISK_DISCLOSURE.md>
Reproducibility <REPRODUCIBILITY.md>
Security Policy <SECURITY.md>
License <LICENSE.md>
```

```{toctree}
:hidden:
:maxdepth: 2
:caption: Contributor and Engineering Docs

Programming Guidelines <contributors/coding_standards.md>
```

```{toctree}
:hidden:
:maxdepth: 2
:caption: Reference

reference/index
```
