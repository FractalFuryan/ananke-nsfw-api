# Addiction Monitoring — Privacy-Preserving Implementation

## Status: **OPTIONAL, OFF BY DEFAULT**

## What This IS

- **Aggregate population metrics** (NOT per-user)
- **Non-identifying** (no IDs, IPs, sessions)
- **Differential privacy** (noise added to outputs)
- **k-anonymity** (minimum threshold before publishing)
- **Read-only** (no influence on system behavior)

## What This IS NOT

- ❌ User tracking
- ❌ Personalization
- ❌ Behavioral targeting
- ❌ Real-time dashboards
- ❌ A/B testing

## How It Works

### 1. Event Recording (Aggregate Only)

```python
from app.addiction_metrics import record_event, am_enabled

if am_enabled():
    record_event("generate")
```

**Recorded:** Event type, timestamp bucket (1-hour windows)  
**NOT recorded:** User ID, IP, session, any identifier

### 2. Privacy Guarantees

- **Time buckets:** 1-hour windows (coarse granularity)
- **Interval buckets:** 10-second bins (no fine-grained timing)
- **k-anonymity:** Minimum 50 events before export
- **Differential privacy:** Laplace noise (ε=0.5)

### 3. Export (Manual, Offline)

```python
from app.addiction_metrics import export_snapshot
import json

snapshot = export_snapshot()
if snapshot:  # None if < k threshold
    with open("metrics/snapshot.json", "w") as f:
        json.dump(snapshot, f)
```

**Output:**
```json
{
  "window_start": 1704297600,
  "total_events": 523,
  "counts": {
    "generate": 312,
    "video": 198,
    "clinical_mode": 13
  },
  "interval_distribution": {
    "10": 45,
    "20": 38,
    "30": 29
  },
  "privacy": {
    "k_anonymity": 50,
    "epsilon": 0.5,
    "noised": true
  }
}
```

## Enabling (Opt-In)

```bash
# Environment variable
export AM_ENABLED=true

# Docker
docker run -e AM_ENABLED=true living-cipher
```

**Default:** `false` (disabled)

## Use Cases

### Research
- Study aggregate usage patterns
- Detect population-level escalation
- Evaluate harm-reduction modes

### Clinical
- Assess program effectiveness
- Share anonymous metrics with partners
- Publish de-identified results

### Transparency
- Demonstrate no exploitation
- Provide evidence of ethical operation
- Enable independent audits

## What You CANNOT Do

- ❌ Track individual users
- ❌ Build user profiles
- ❌ Optimize for engagement
- ❌ Correlate across sessions
- ❌ Sell data
- ❌ Feed back into product decisions

## CI/CD Guards

```yaml
- name: Block user telemetry
  run: |
    if grep -R -nE "user_id|session_id|fingerprint|analytics" app/; then
      echo "❌ User tracking detected"
      exit 1
    fi
```

## Runtime Assertions

```python
# In addiction_metrics.py
assert "behavior" not in globals(), "Behavioral feedback detected"
```

## Monitoring the Monitor

Health endpoint exposes monitoring status:

```bash
curl http://localhost:8000/health | jq .addiction_monitoring
```

```json
{
  "enabled": true,
  "current_window_events": 42,
  "k_threshold": 50,
  "epsilon": 0.5
}
```

## Threat Model

### Attack: Re-identification via timing
**Mitigation:** 10s buckets, 1h windows, k-anonymity

### Attack: Cross-session correlation
**Mitigation:** No session IDs, no IP logging

### Attack: Behavioral feedback loop
**Mitigation:** One-way export, runtime assertion

## Comparison to Traditional Analytics

| Feature | Ananke AM | Google Analytics |
|---------|-----------|------------------|
| User IDs | NO | YES |
| IP Logging | NO | YES |
| Sessions | NO | YES |
| Personalization | NO | YES |
| Real-time | NO | YES |
| k-anonymity | YES | NO |
| DP noise | YES | NO |
| Opt-in | YES | Often default |

## Legal Compliance

- **GDPR:** No personal data collected → not subject to most provisions
- **CCPA:** No sale of data, no personal information
- **HIPAA:** Not applicable (no PHI collected)

**Still recommend:** Privacy policy disclosure, opt-in consent

## Research Ethics

If using for research:

1. **IRB approval** required
2. **Informed consent** from participants
3. **Data minimization** (only collect what's needed)
4. **Public pre-registration** of analysis plan

## Disabling

```bash
export AM_ENABLED=false
# Or simply don't set it (default is false)
```

No restart required if implemented correctly (check on each request).

## Open Questions

- Optimal ε value for this context?
- Alternative privacy mechanisms (e.g., local DP)?
- Third-party audit of implementation?

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 0.1.0 | 2026-01-03 | Initial implementation |

---

**Addiction monitoring demonstrates that ethical NSFW tech can study population health without surveillance.**

Ethics Anchor: 65b14d584f5a5fd070fe985eeb86e14cb3ce56a4fc41fd9e987f2259fe1f15c1
