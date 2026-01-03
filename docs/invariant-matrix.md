# Invariant Matrix

## Core Invariants

| # | Invariant | Code Location | CI Check | Runtime Check | Test Coverage |
|---|-----------|---------------|----------|---------------|---------------|
| 1 | No human bodies | `core.py` bounds | `ethics.yml` | `guards.py` | `test_invariants.py` |
| 2 | No likeness reconstruction | No face libs | Dependency scan | N/A | Manual audit |
| 3 | No learning/memory | Stateless design | Pattern match `train\|fit` | N/A | `test_no_memory.py` |
| 4 | No engagement optimization | No analytics | Pattern match `engagement\|retention` | Health endpoint | Manual audit |
| 5 | No escalation | Bounded params | Bounds test | `guards.py` | `test_bounds()` |
| 6 | Revocable inputs | `revocation.py` | N/A | Token validation | `test_revocation.py` |
| 7 | No realism monetization | Flat pricing | Manual review | N/A | Business policy |

## Parameter Bounds

| Parameter | Min | Max | Purpose | Risk if Violated |
|-----------|-----|-----|---------|------------------|
| `curvature` | 0.1 | 0.9 | Abstract shape | Realism if uncapped |
| `symmetry_order` | 3 | 6 | Non-biological | Human-like if 1-2 |
| `frequency` | 1.0 | 2.5 | Wave patterns | Chaotic if unbounded |
| `frames` | 1 | 300 | Video length | Resource abuse |
| `fps` | 1 | 60 | Frame rate | Resource abuse |

## Forbidden Terms (CI Enforced)

### Realism
- photoreal, photorealistic
- skin, flesh, body
- face, eyes, hair
- skeleton, anatomy, pose

### Learning
- train, fit, fine_tune
- reinforcement, reward_model
- backprop, gradient

### Engagement
- engagement, retention
- arousal, optimization
- personalize, profile
- recommend, suggest

## Feature Flags

| Flag | Default | Purpose | Emergency Disable |
|------|---------|---------|-------------------|
| `video_enabled` | True | Video generation | Set to False |
| `mp4_enabled` | True | MP4 encoding | Set to False |
| `streaming_enabled` | True | Chunked delivery | Set to False |

## Health Endpoint Assertions

```json
{
  "ethics": {
    "learning": false,
    "memory": false,
    "analytics": false,
    "realism_ceiling": "enforced",
    "user_data_storage": false,
    "engagement_optimization": false
  }
}
```

## Test Suite Coverage

| Test | File | Validates |
|------|------|-----------|
| Determinism | `test_determinism.py` | Same seed → same output |
| No Memory | `test_no_memory.py` | Different seeds → different outputs |
| Bounds | `test_invariants.py` | Parameters within range |
| No Realism Keys | `test_invariants.py` | Geometry has no forbidden keys |
| Revocation | `test_revocation.py` | Revoked tokens rejected |
| Video Determinism | `test_video.py` | Frame sequences repeatable |

## Compliance Checklist

- [ ] CI passes ethics gate
- [ ] Health endpoint shows ethics=true
- [ ] No ML dependencies in requirements.txt
- [ ] OpenAPI spec matches deployed endpoints
- [ ] Feature flags functional
- [ ] Realism guards active
- [ ] Addiction monitoring (if enabled) is aggregate-only
- [ ] Documentation up-to-date

## Audit Trail

All changes to invariants must:
1. Update this matrix
2. Add corresponding CI check
3. Add test coverage
4. Document in git commit
5. Announce in CHANGELOG

## Emergency Response

If invariant violated:

1. **Detect**: CI fails / health check alerts / user report
2. **Disable**: Feature flag to false
3. **Fix**: Patch code, add guard
4. **Verify**: Re-run full test suite
5. **Deploy**: Gradual rollout with monitoring
6. **Document**: Public incident report

## Version History

| Date | Version | Changes | Ethics Anchor |
|------|---------|---------|---------------|
| 2026-01-01 | 0.1.0 | Initial invariants | 65b14d58... |

---

**This matrix is the single source of truth for ethical enforcement.**
