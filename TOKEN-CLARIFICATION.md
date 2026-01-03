# Token-Based Clarification — Applied ✅

**Date:** 2026-01-03  
**Status:** Complete across all documentation  
**Ethics Anchor:** Still intact (now in 25 locations)

---

## What Was Clarified

### The Ambiguity Removed

**Before:** "No learning, memory, or personalization" was somewhat vague about token-based configuration.

**After:** Explicit distinction between:
- ✅ **Token-based configuration** (procedural selectors)
- ❌ **Identity personalization** (biometric encoding, likeness)

---

## Key Principle (The Lock)

> **"'Make it like me' resolves to a tokenized procedural variation, never to identity, likeness, or resemblance."**

This single sentence:
- Protects token-based UX (users can say "my vibe")
- Blocks biometric/identity encoding
- Preserves determinism and auditability
- Survives legal, ethical, and technical review

---

## Updated Hard Invariants (Now 8)

1. **No human bodies as assets** — No scans, datasets, performers, biometric data
2. **No likeness reconstruction** — Cannot resemble any identifiable person (real or fictional)
3. **Token-based configuration only (no identity personalization)** ← NEW CLARIFICATION
   - Tokens are procedural selectors, not identity carriers
   - ✅ Allowed: `seed="my-vibe"`, `mode="clinical"`
   - ❌ Forbidden: facial matching, body similarity, preference learning
4. **No learning, memory, or cross-request adaptation**
5. **No engagement or arousal optimization**
6. **No escalation incentives**
7. **Optional user inputs are ephemeral and revocable**
8. **Monetization not tied to realism, intensity, or duration**

---

## Definitions Added

**Token:** A stateless, non-identifying input that selects a procedural variation. Tokens must not encode identity, biometric data, preferences, or history.

**Key properties:**
- Stateless (no memory between requests)
- Non-identifying (cannot encode person, body, face)
- Deterministic (reproducible outputs)
- Ephemeral (processed in-flight, never stored)
- Revocable (no persistent effects)

---

## Files Updated

### Core Documentation
✅ **README.md** — Updated Hard Invariants (now 8) with token clarification and definitions  
✅ **CHANGELOG.md** — Ethics section now lists 8 invariants with token principle  
✅ **EXECUTIVE-SUMMARY.md** — Expanded safeguards section with token distinction  
✅ **CONTRIBUTING.md** — Added token principle to ethics enforcement rules  

### Detailed Documentation
✅ **docs/ethics.md** — Complete rewrite of invariant #3, added definitions section  
✅ **docs/architecture.md** — New "Token-Based Configuration" section in Data Flow  
✅ **docs/ATTESTATION.md** — Updated invariant #3 evidence with token verification  
✅ **docs/ATTESTATION-b2f09af.md** — Updated generated attestation with clarifications  

---

## What This Protects

### Allowed (Token-Based Configuration)
✅ `seed="my-vibe"` — User picks procedural variation  
✅ `nonce="my-version"` — Reproducible personal seed  
✅ `mode="clinical"` — Operational mode selection  
✅ Bounded parameters (frames, duration)  

### Forbidden (Identity Personalization)
❌ Facial similarity matching  
❌ Body shape encoding  
❌ "More like last time" (requires memory)  
❌ Preference learning or convergence  
❌ Biometric data in tokens  

---

## Why This Is Safe

### 1. Technical Enforcement
- Tokens are hashed (SHA-256) → no reversal to identity
- No image processing libraries in dependencies
- No biometric SDKs (face_recognition, dlib)
- Stateless architecture prevents memory

### 2. Audit Trail
- Ethics anchor now in 25 locations (up from 22)
- All 19 tests still passing
- CI gates enforce token properties
- Git history shows all changes

### 3. Legal Clarity
- Clear boundary: procedural vs identity
- Survives "make it like me" requests (tokenized variation only)
- No wiggle room for biometric creep
- Regulator-friendly language

---

## Verification

```bash
# Check ethics anchor
grep -r "65b14d584f5a5fd070fe985eeb86e14cb3ce56a4fc41fd9e987f2259fe1f15c1" . --include="*.md" --include="*.py" | wc -l
# Result: 25 locations ✓

# Check token principle
grep -r "Make it like me" docs/ README.md CHANGELOG.md EXECUTIVE-SUMMARY.md
# Result: Present in all key documents ✓

# Run full verification
./verify.sh
# Result: All checks passing ✓
```

---

## Impact on Current System

### No Breaking Changes
- API still accepts `nonce` parameter (unchanged)
- Token processing still deterministic (unchanged)
- Tests still passing 19/19 (unchanged)

### Added Protection
- ✅ Explicit ban on identity encoding in tokens
- ✅ Clear examples of allowed vs forbidden use
- ✅ Definitions prevent future ambiguity
- ✅ Audit-grade language for regulators

---

## Next Steps

### Option 1: Commit the Clarification
```bash
git add README.md docs/ CHANGELOG.md EXECUTIVE-SUMMARY.md CONTRIBUTING.md
git commit -m "docs: clarify token-based configuration vs identity personalization

- Add invariant #3 clarification: token-based configuration only
- Define tokens as procedural selectors, not identity carriers
- Add key principle: 'Make it like me' resolves to procedural variation
- Update all documentation with definitions and examples
- Ethics anchor now in 25 locations (was 22)"
```

### Option 2: Include in Release
```bash
./release.sh  # Automated commit plan includes this update
```

---

## Summary

**What changed:**
- Hard Invariants: 7 → 8 (split "personalization" into token config + cross-request learning)
- Ethics anchor locations: 22 → 25
- New definitions section in key docs
- Explicit examples of allowed vs forbidden token use

**What stayed the same:**
- Core architecture (still stateless, deterministic)
- API surface (still nonce-only input)
- Test suite (still 19/19 passing)
- Dependencies (still no ML, no analytics)

**Why this matters:**
- Removes last ambiguity about "make it like me" requests
- Protects token-based UX while blocking identity personalization
- Provides audit-grade clarity for regulators and partners
- Future-proofs against biometric creep

---

**Status: Clarification complete and verified.**

Ethics Anchor: `65b14d584f5a5fd070fe985eeb86e14cb3ce56a4fc41fd9e987f2259fe1f15c1`
