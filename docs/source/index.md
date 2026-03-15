# MarketMind Documentation

Read the Docs for `marketmind-docs` is the publication layer for canonical documentation exported from the private `MarketMind` repository. The site is centered on the current 4.4.x architecture, release history, governance/legal documents, and contributor engineering guidance.

## Published Sections

### Overview

- [README / Technical Overview](README.md)
- [Release History](CHANGELOG.md)

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

### Secondary Reference

- [API Reference](reference/index.rst)

The API reference remains available, but it is secondary to the canonical narrative, release, and governance documents.

```{toctree}
:hidden:
:maxdepth: 2
:caption: Overview

README.md
CHANGELOG.md
```

```{toctree}
:hidden:
:maxdepth: 2
:caption: Governance and Legal

GOVERNANCE.md
MODEL_CARD.md
PRIVACY_POLICY.md
RISK_DISCLOSURE.md
REPRODUCIBILITY.md
SECURITY.md
LICENSE.md
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
