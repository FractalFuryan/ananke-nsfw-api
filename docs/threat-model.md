# Threat Model

## Attack Surface Analysis

### 1. Realism Drift

**Threat:** Gradual addition of realistic features (skin textures, anatomical accuracy)

**Mitigations:**
- CI blocks keywords: photoreal, skin, eyes, face, pose, anatomy
- Runtime assertions check SVG output for forbidden terms
- Bounded parameters prevent photorealistic ranges
- Open-source core enables public auditing

**Residual Risk:** Low (multi-layer enforcement)

---

### 2. Personalization Creep

**Threat:** System learns user preferences, builds profiles

**Mitigations:**
- Stateless design (no cross-request memory)
- No user IDs in generator layer
- Cache keyed only by nonce
- Optional addiction monitoring is aggregate-only

**Residual Risk:** Very Low (architecturally prevented)

---

### 3. Engagement Optimization

**Threat:** Metrics feedback loop optimizes for time-on-platform

**Mitigations:**
- No analytics SDK in codebase
- CI blocks: engagement, retention, arousal, optimization
- Health endpoint explicitly states analytics=false
- Addiction monitoring (if enabled) is one-way export only

**Residual Risk:** Very Low (no feedback path exists)

---

### 4. Escalation Mechanics

**Threat:** Gambling-like progression, intensity tiers

**Mitigations:**
- Parameters bounded at core level
- No "intensity" slider in API
- Deterministic outputs prevent loot-box mechanics
- No subscription tiers based on realism

**Residual Risk:** Very Low (bounded by design)

---

### 5. Input Reconstruction

**Threat:** User uploads face photo, system reconstructs likeness

**Mitigations:**
- Generator accepts only text nonces
- Optional image input (api/input.py) extracts only non-invertible features
- No face detection libraries in dependencies
- No pose estimation

**Residual Risk:** Very Low (no reconstruction path)

---

### 6. Deepfake Attack

**Threat:** System used to generate realistic fake videos

**Mitigations:**
- No face swapping capability
- No pose transfer from video
- Procedural motion is parametric (phase-based)
- GPU shaders limited to abstract patterns

**Residual Risk:** None (technical capability doesn't exist)

---

### 7. Data Exfiltration

**Threat:** User data leaked or monetized

**Mitigations:**
- No persistent storage of user inputs
- Revocation is in-memory or ephemeral DB
- Logs contain only: endpoint, timestamp, status
- No IP logging tied to content

**Residual Risk:** Very Low (minimal data collected)

---

### 8. Supply Chain Compromise

**Threat:** Malicious dependency adds tracking/learning

**Mitigations:**
- Minimal dependencies (no ML frameworks)
- Dependency lock files with hashes
- CI fails on new analytics packages
- Open-source core enables verification

**Residual Risk:** Low (small attack surface)

---

### 9. Ethics Anchor Tampering

**Threat:** Someone modifies ethics anchor to hide drift

**Mitigations:**
- Anchor embedded in multiple locations
- CI verifies match on every build
- Health endpoint exposes current anchor
- Git history provides audit trail

**Residual Risk:** Very Low (multiple verification points)

---

### 10. Regulatory Arbitrage

**Threat:** Deployment in jurisdictions with lax oversight

**Mitigations:**
- Ethics baked into code, not policy
- Open-source core travels with ethics anchor
- EULA binds to invariants regardless of jurisdiction
- Harm reduction mode for clinical contexts

**Residual Risk:** Moderate (requires ongoing vigilance)

---

## Defense-in-Depth

| Layer | Control | Enforcement Point |
|-------|---------|-------------------|
| **Design** | Bounded parameters | Core generator |
| **Code** | No ML frameworks | Dependency scan |
| **CI/CD** | Pattern detection | GitHub Actions |
| **Runtime** | Realism assertions | Renderer guards |
| **API** | Revocation | Token validation |
| **Contract** | License binding | EULA |
| **Social** | Open audit | Public repo |

## Monitoring & Alerting

**Automated Checks:**
- CI fails on forbidden terms
- Health endpoint reports ethics drift
- Feature flags enable instant disable

**Manual Audits:**
- Quarterly ethics review
- Dependency audit
- Public bug bounty (ethics violations)

## Incident Response

If ethics violation detected:

1. **Immediate**: Disable via feature flag
2. **Short-term**: Patch and redeploy
3. **Long-term**: Root cause analysis, update guards
4. **Transparency**: Public incident report

## Red Team Scenarios

### Scenario 1: Insider adds ML
**Detection:** CI blocks torch/tensorflow import  
**Response:** PR rejected, contributor warned

### Scenario 2: Gradual realism increase
**Detection:** Runtime assertion fails, CI blocks "skin"  
**Response:** Build fails, cannot merge

### Scenario 3: Hidden analytics endpoint
**Detection:** OpenAPI spec audit, CI pattern match  
**Response:** Immediate removal, incident review

## Assumptions & Limitations

**Assumptions:**
- CI/CD pipeline is not compromised
- Developer devices are secure
- Open-source auditors exist

**Limitations:**
- Cannot prevent forks with modified ethics
- Cannot enforce ethics in all jurisdictions
- Requires ongoing maintenance of guard patterns

## Conclusion

This system uses **defense in depth** to make ethical violations:
- Architecturally difficult
- Operationally detectable
- Socially costly
- Legally actionable

No single point of failure. Multiple independent verification layers.
