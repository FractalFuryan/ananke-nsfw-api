# Production Hardening — Phase 2

## What Changed

This phase adds production-grade features **without touching ethics, revenue, or scope**.

### 1. Feature Flags
- Binary kill-switches for video/MP4/streaming
- No analytics, just instant disable capability
- Flag status visible in `/health` endpoint

### 2. Enhanced Health Endpoint
- Ethics anchor verification
- Real-time invariant status
- Feature flag state
- Available at `GET /health`

### 3. Deterministic Caching
- LRU cache (1024 entries) for pure geometry outputs
- Keyed only by nonce (deterministic input)
- No user identifiers, no behavioral signals
- Cache miss is not tracked as a signal

### 4. OpenAPI Specification
- Auto-generated from service
- Published to `open/ananke-api-spec/`
- Enables public auditing of API surface

### 5. Production Deployment Profile
- Resource limits (2 CPU, 4GB RAM for Living Cipher)
- Restart policies (`unless-stopped`)
- Health checks with 30s interval
- Log rotation (10MB max, 3 files)

### 6. Realism Assertion Guard
- Last-line defense at renderer boundary
- Blocks outputs containing forbidden terms
- Validates geometry for realism keys
- Fails loudly with `RealismViolation` exception

## System State

✅ All invariants intact  
✅ Ethics anchor unchanged  
✅ No analytics or tracking  
✅ Deterministic outputs  
✅ Stateless operation  
✅ Multiple layers of drift protection  

## Verification

```bash
# Check health + ethics status
curl http://localhost:8000/health

# Test feature flags
curl -X POST "http://localhost:8000/v1/generate?nonce=test"

# Test realism guard (should pass)
curl -X POST "http://localhost:8000/v1/generate/video?nonce=abstract123"
```

## Production Deployment

```bash
cd infra
docker-compose -f docker-compose.prod.yml up -d
```

---

**System remains morally correct by construction.**
