# Changelog

## [v1.0.0] — Ethics-Locked Production Release
Date: 2026-01-03

### Added
- Full verification infrastructure (`verify.sh`, `status.sh`)
- Makefile with 10 verification and ops targets
- Attestation system (`ATTESTATION.md`, commit-scoped reports)
- Privacy-preserving addiction monitoring (OFF by default)
- Clinical / harm-reduction mode
- Web client (abstract preview only)
- GPU renderer stub (stylized, non-realistic)
- Stateless queue workers
- Regulator documentation pack (7 files)
- Comprehensive test suite (19 tests across core + cipher layers)
- Enhanced CI/CD with ethics drift detection
- Feature flags with safe defaults

### Verified
- 19/19 tests passing (100% pass rate)
- No ML frameworks (torch, tensorflow, keras, sklearn)
- No analytics SDKs (mixpanel, segment, amplitude)
- No personalization or user tracking
- Deterministic generation and video output
- Ethics anchor enforced across code, CI, runtime, and contract

### Ethics
- Anchor: `65b14d584f5a5fd070fe985eeb86e14cb3ce56a4fc41fd9e987f2259fe1f15c1`
- Any invariant violation invalidates ethical classification
- 8 Hard Invariants enforced by construction:
  1. No human bodies as assets (no scans, datasets, performers, biometric data)
  2. No likeness reconstruction (cannot resemble any identifiable person)
  3. **Token-based configuration only** (no identity personalization)
     - **Key principle:** *"'Make it like me' resolves to tokenized procedural variation, never to identity, likeness, or resemblance"*
     - Tokens are procedural selectors, not identity carriers
  4. No learning, memory, or cross-request adaptation
  5. No engagement or arousal optimization
  6. No escalation incentives
  7. Optional user inputs are ephemeral and revocable
  8. Monetization not tied to realism, intensity, or duration

### Architecture
- Open-source trust layer (`open/ananke-core`)
- Proprietary business layer (`proprietary/living-cipher`)
- Billing isolated from generation path
- Stateless, deterministic, non-adaptive design

### Documentation
- Complete regulator pack (architecture, ethics, threat model, invariant matrix, API surface, clinical mode, addiction monitoring)
- Deployment guides (hardening, production config)
- Verification guide (VERIFICATION.md)
- Automated attestation reports

### Security
- Multi-layer defense (input validation, hash determinism, bounds checking, abstraction guards, template sanitization)
- Attack surface documented and mitigated
- No persistent storage, no user databases
- Nonce-only input model (no images, no files)
