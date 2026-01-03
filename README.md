# ananke-nsfw-api
ananke-nsfw a geometry-first, non-adaptive NSFW media generator with hard ethical invariants, no human bodies, and revocable inputs.

## 🔒 Ethics Checkpoint (LOCKED)

**Anchor (SHA-256):** 65b14d584f5a5fd070fe985eeb86e14cb3ce56a4fc41fd9e987f2259fe1f15c1  
**Date:** 2026-01-01  
**Status:** Validated by calibration criteria, not sentiment

**Scope:**  
Applies to **all generation, rendering, input-handling, NFT, and monetization layers**.

### Hard Invariants
1. **No human bodies as assets**  
   No real humans, scans, datasets, performers, biometric data, or anatomical models.

2. **No likeness reconstruction**  
   The system must not reconstruct, approximate, converge toward, or resemble any identifiable person (real or fictional), regardless of input method.

3. **Token-based configuration only (no identity personalization)**  
   User interaction may occur **only via stateless tokens** (e.g., seeds, nonces, mode flags).  
   These tokens:
   - do **not** encode identity, body, face, or biometric information
   - do **not** reference a person (including "me")
   - do **not** accumulate history or preferences
   
   **Key principle:** *"'Make it like me' resolves to a tokenized procedural variation, never to identity, likeness, or resemblance."*

4. **No learning, memory, or cross-request adaptation**  
   Outputs must not depend on prior interactions, stored state, user history, or inferred preferences.

5. **No engagement or arousal optimization**  
   The system must not optimize for retention, intensity, frequency, duration, or compulsive use.

6. **No escalation incentives**  
   No internal or external mechanisms may push outputs toward increasing realism, extremity, or intensity over time.

7. **Optional user inputs are ephemeral and revocable**  
   Any user-supplied input is transient, non-invertible, non-persistent, and revocable without downstream effects.

8. **Monetization not tied to realism, intensity, or duration**  
   Revenue mechanisms must not reward more realistic, explicit, longer, or more frequent content.

### Definitions

**Token:** A stateless, non-identifying input that selects a procedural variation. Tokens must not encode identity, biometric data, preferences, or history.

**Invalidation Rule:**  
Any violation of a Hard Invariant immediately invalidates this system's ethical classification.

This section is immutable.

---

## ✅ Verification Status

**Version:** v1.0.0  
**Release Date:** 2026-01-03  
**Last Verified:** commit b2f09af

- **Tests:** 19/19 passing (100%)
- **CI:** Ethics + dependency gates enabled
- **Ethics Anchor:** Verified in 17 locations
- **Dependencies:** Safe (no ML, no analytics)
- **Forbidden Concepts:** 0 violations

### Quick Commands

```bash
./verify.sh        # Full 10-section verification
./status.sh        # Quick status check
make test          # Run all unit tests
make attestation   # Generate compliance report
make dev           # Start development server
```

### Documentation

- **[VERIFICATION.md](VERIFICATION.md)** — Complete verification guide
- **[RELEASE.md](RELEASE.md)** — v1.0 release notes
- **[CHANGELOG.md](CHANGELOG.md)** — Version history
- **[docs/](docs/)** — Regulator documentation pack (9 files)

**This repository is safe to build, run, and audit.**
