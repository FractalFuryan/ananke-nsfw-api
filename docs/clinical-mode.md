# Clinical Mode — Harm Reduction Guidelines

## Purpose

Clinical mode provides a **lower-intensity** generation profile for use in:
- Medical/therapeutic contexts
- Harm reduction programs
- Research settings
- Educational demonstrations

## Technical Differences

| Parameter | Standard | Clinical | Rationale |
|-----------|----------|----------|-----------|
| Frequency Cap | 1.5 | 1.1 | Reduced visual intensity |
| Default Frames | 60 | 30 | Shorter exposure duration |
| Curvature | 0.25-0.75 | 0.25-0.75 | Same range (already bounded) |

## Usage

### API

```python
from app.modes import apply_mode
from app.cache import cached_geometry

geom = cached_geometry("seed123")
clinical_geom = apply_mode(geom, mode="clinical")
```

### Environment Flag

```bash
DEFAULT_MODE=clinical
```

## Clinical Use Cases

### 1. Therapeutic Exposure
- Controlled, predictable stimulus
- Lower intensity for gradual desensitization
- Deterministic (repeatable sessions)

### 2. Research
- Standardized stimuli across subjects
- Reproducible from seeds
- No participant data storage

### 3. Harm Reduction
- Alternative to exploitative content
- No escalation mechanics
- No personalization (prevents addiction loops)

## Ethical Considerations

### What Clinical Mode IS:
- ✅ Lower-intensity parameter preset
- ✅ Explicit safety framing
- ✅ Deterministic and reproducible
- ✅ Non-adaptive

### What Clinical Mode IS NOT:
- ❌ A medical device (not FDA regulated)
- ❌ A treatment (consult professionals)
- ❌ Personalized (same deterministic behavior)
- ❌ Adaptive (no learning from usage)

## Deployment Guidelines

### Recommended Safeguards

1. **Informed Consent**
   - Clear explanation to users
   - Option to disable
   - No stigma for opting out

2. **Professional Oversight**
   - Deploy only in supervised contexts
   - Clinician or researcher present
   - Proper ethical review

3. **Data Minimization**
   - No logging of clinical sessions
   - No linkage to participant IDs
   - Aggregate metrics only (if any)

4. **Exit Strategy**
   - Clear pathways to reduce use
   - No penalties for quitting
   - Support resources available

## Monitoring

If deploying in clinical contexts, consider:

- Aggregate usage metrics (not per-user)
- Session duration distributions
- Mode switching rates
- Revocation rates

**All metrics must be non-identifying and aggregate.**

## Legal & Regulatory

- **Not a medical device** (US/EU definitions)
- May require IRB approval for research
- Consult legal counsel for jurisdiction
- Maintain audit trail of mode usage

## Documentation for Professionals

When presenting to clinicians/researchers:

1. **What it does:** Generates abstract geometric media deterministically
2. **What it doesn't do:** Learn, personalize, escalate, or store data
3. **Safety:** Bounded parameters, revocable, no engagement optimization
4. **Evidence:** No clinical trials yet (this is experimental)

## Research Opportunities

Potential studies (requiring proper IRB):

- Efficacy vs traditional exposure therapy
- Relapse prevention in recovery contexts
- Comparative harm analysis
- Long-term outcomes

**Contact research@[domain] for collaboration.**

## Open Questions

- Optimal frequency cap for different contexts?
- Interaction with other therapeutic modalities?
- Long-term safety profile?
- Ethical boundaries for autonomous use?

## Updates

This is a **living document**. As evidence emerges, modes may be adjusted.

Version: 0.1.0  
Last Updated: 2026-01-03  
Ethics Anchor: 65b14d584f5a5fd070fe985eeb86e14cb3ce56a4fc41fd9e987f2259fe1f15c1

---

**Clinical mode maintains all core ethical invariants while providing an alternative safety profile.**
