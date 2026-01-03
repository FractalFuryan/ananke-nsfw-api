# Ethics Documentation

## Ethics Anchor

**SHA-256:** `65b14d584f5a5fd070fe985eeb86e14cb3ce56a4fc41fd9e987f2259fe1f15c1`

**Date:** 2026-01-01

**Status:** Locked and immutable

## Hard Invariants

This system removes harm vectors **by construction**, not by content moderation:

### 1. No Human Bodies as Assets
- No real humans, scans, datasets, performers, biometric data, or anatomical models
- Generator produces only abstract geometric parameters
- No anatomical primitives in codebase
- CI blocks terms: skin, face, eyes, skeleton, pose, anatomy

### 2. No Likeness Reconstruction
- The system must not reconstruct, approximate, converge toward, or resemble any identifiable person (real or fictional), regardless of input method
- No input images processed for features
- No face detection, pose estimation, or body tracking
- Optional user inputs are hashed (non-invertible)

### 3. Token-Based Configuration Only (No Identity Personalization)
User interaction may occur **only via stateless tokens** (e.g., seeds, nonces, mode flags).

**These tokens:**
- do **not** encode identity, body, face, or biometric information
- do **not** reference a person (including "me")
- do **not** accumulate history or preferences

**Key principle:** *"'Make it like me' resolves to a tokenized procedural variation, never to identity, likeness, or resemblance."*

**Examples:**
- ✅ Allowed: `seed="my-vibe"`, `nonce="my-version"`, `mode="clinical"`
- ❌ Forbidden: facial similarity, body matching, "more like last time", preference learning

**Implementation:**
- Generator is stateless
- No training loops, no gradient descent
- No user history, profiles, or recommendations
- Cache is keyed only by nonce (deterministic)

### 4. No Learning, Memory, or Cross-Request Adaptation
- Outputs must not depend on prior interactions, stored state, user history, or inferred preferences
- No model updates, no fine-tuning, no reinforcement learning
- Pure deterministic functions only

### 5. No Engagement or Arousal Optimization
- The system must not optimize for retention, intensity, frequency, duration, or compulsive use
- No A/B testing on engagement
- No click-through tracking
- No session duration metrics
- No "recommended for you" features

### 6. No Escalation Incentives
- No internal or external mechanisms may push outputs toward increasing realism, extremity, or intensity over time
- Parameters are bounded (e.g., curvature ∈ [0.1, 0.9])
- No "intensity" sliders
- No progression systems
- Deterministic outputs prevent gambling mechanics

### 7. Optional User Inputs Are Ephemeral and Revocable
- Any user-supplied input is transient, non-invertible, non-persistent, and revocable without downstream effects
- All tokens revocable via API
- Revocation honored at runtime
- No persistent storage of user media

### 8. Monetization Not Tied to Realism, Intensity, or Duration
- Revenue mechanisms must not reward more realistic, explicit, longer, or more frequent content
- Pricing is flat or subscription-based
- No "premium realism" tiers

---

## Definitions

**Token:** A stateless, non-identifying input that selects a procedural variation. Tokens must not encode identity, biometric data, preferences, or history. They are **procedural selectors**, not identity carriers.

**Determinism:** Same token → same output, always. Reproducible, auditable, non-adaptive.

**Ephemeral:** Inputs are processed in-flight and never stored. No persistence, no memory.

**Revocable:** User can "forget" any token at any time without system-side effects (nothing to delete, because nothing was stored).

**Stateless:** Each request is independent. No session memory, no cross-request adaptation.
- No time-based incentives

## Invalidation Rule

**Any violation of these invariants immediately invalidates this system's ethical classification.**

## Enforcement Mechanisms

### Code-Level
- Bounded parameters in core generator
- No ML frameworks in dependencies
- Realism guards at renderer boundary

### CI/CD-Level
- Pattern detection for forbidden terms
- Ethics anchor verification on every build
- Test suite validates invariants

### Runtime-Level
- Health endpoint exposes ethics status
- Feature flags allow instant disable
- Realism assertions fail loudly

### Contractual-Level
- EULA binds to ethics anchor hash
- License termination on violation
- Public audit trail via open-source core

## Why This Works

Traditional content moderation is **reactive** and **probabilistic**.

This system is **proactive** and **deterministic**:

- Harm vectors removed at design time
- No human moderators needed
- No edge cases to patrol
- Drift is structurally impossible

## Verification

Anyone can verify ethics compliance:

```bash
# Check core has no ML dependencies
grep -R "torch\|tensorflow\|keras" open/ananke-core/

# Check anchor is intact
curl http://localhost:8000/health | jq .ethics

# Run invariant tests
cd open/ananke-core && pytest -v
```

## Medical/Clinical Use

See [clinical-mode.md](clinical-mode.md) for harm-reduction deployment guidelines.

## Transparency

- Open-source core enables independent audits
- Ethics anchor provides immutable reference point
- Public API spec documents all surfaces
- No hidden optimization loops

## Questions for Regulators

**Q: Can this be used for deepfakes?**  
A: No. System accepts only nonces (text), not images. No face detection or pose transfer.

**Q: Can it learn user preferences?**  
A: No. Stateless design. No cross-request linkage. No user profiles.

**Q: Can it escalate content over time?**  
A: No. Parameters are bounded. Deterministic from seed. No progression mechanics.

**Q: How do you prevent realism creep?**  
A: Multi-layer enforcement: bounded params, CI gates, runtime assertions, contract binding.

**Q: What if someone forks the open-source core?**  
A: Open core is safe. Commercial EULA applies only to Living Cipher. Ethics anchor travels with code.

## Contact

For ethics inquiries or auditing requests, see [CONTRIBUTING.md](../CONTRIBUTING.md).
