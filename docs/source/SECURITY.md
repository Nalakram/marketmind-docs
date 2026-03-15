# Security Policy

> **Draft Notice:**  
> This document outlines the proposed security policy for MarketMind. It is currently a draft and not yet implemented. The practices described here are under review and may change. Until finalized, do not assume full adherence to the details in this policy.

MarketMind is committed to protecting the security of users and their data. This document outlines current policy intent, responsible disclosure expectations, and security design goals without disclosing sensitive implementation detail.

## Responsible Disclosure Policy

If you discover a potential security issue in MarketMind, report it privately via:

- Email: `security@mindforgelabs.com`

Include reproduction details where possible. The project aims to acknowledge reports within 48 hours and resolve critical issues within 30 days. Public disclosure should wait until the issue has been addressed or coordinated with the maintainer.

## Key Security Features

- Secure service-to-service communication paths
- Local desktop authentication controls
- Structured logging with sensitive-data hygiene
- Input validation across Python, Java, and C++ boundaries
- Modern memory-safety practices in native code

## Secure Development Practices

- Secrets belong in local configuration or environment variables, never hard-coded
- Sensitive financial data is processed locally by default
- External provider connections should use secure transport paths
- Security-sensitive changes should be reviewed in the private repository

## Automated Security Tools and Testing

- Dependency vulnerability scanning
- Static analysis in CI
- Continuous integration testing across supported stacks
- Dependency pinning for critical runtime surfaces

## Privacy and Regulatory Position

MarketMind is designed to avoid collecting personal data by default. Financial data remains local unless the user explicitly connects an external provider. See [Privacy Policy](PRIVACY_POLICY.md) for details.

## Known Limitations and Future Plans

- Data at rest is not encrypted by the application by default
- Security assumes a reasonably secure local desktop environment
- Supply-chain hardening and signed release workflows are still evolving
- Multi-factor authentication is not part of the current local-login model

## Contact Information

For security questions or reports:

- Email: `security@mindforgelabs.com`
