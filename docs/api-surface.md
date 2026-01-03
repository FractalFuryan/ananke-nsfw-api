# API Surface Documentation

## Public Endpoints

### POST /v1/generate

Generate single frame with abstract geometry.

**Request:**
```json
{
  "nonce": "string",
  "token": "string (optional)"
}
```

**Response:**
```json
{
  "geometry": {
    "curvature": 0.5,
    "symmetry_order": 4,
    "frequency": 1.3,
    "engine_version": "ananke-core@0.1.0"
  },
  "svg": "<svg>...</svg>"
}
```

**Errors:**
- 403: Token revoked
- 500: Server error

---

### POST /v1/generate/video

Generate frame sequence (JSON).

**Request:**
```json
{
  "nonce": "string",
  "frames": 60
}
```

**Response:**
```json
{
  "frames": ["<svg>...</svg>", ...]
}
```

**Errors:**
- 503: Feature disabled (video_enabled=false)

---

### POST /v1/generate/video/mp4

Generate encoded MP4 video.

**Request:**
```json
{
  "nonce": "string",
  "frames": 60,
  "fps": 30
}
```

**Response:**
- Binary MP4 data (video/mp4)

**Errors:**
- 503: Feature disabled (mp4_enabled=false)

---

### POST /v1/revoke

Revoke a token.

**Request:**
```json
{
  "token": "string"
}
```

**Response:**
```json
{
  "status": "revoked"
}
```

---

### GET /health

Health check with ethics verification.

**Response:**
```json
{
  "status": "ok",
  "service": "living-cipher",
  "ethics": {
    "ethics_anchor": "65b14d58...",
    "learning": false,
    "memory": false,
    "analytics": false,
    "realism_ceiling": "enforced"
  },
  "features": {
    "video_enabled": true,
    "mp4_enabled": true,
    "streaming_enabled": true
  }
}
```

---

## Rate Limiting

**Type:** Non-behavioral, IP-based  
**Limit:** 120 requests / 60 seconds  
**Response:** 429 Too Many Requests

---

## Authentication

**Optional:** Token-based revocation  
**No required auth** for generation (public API)

---

## CORS

**Allowed Origins:** Configurable  
**Default:** Same-origin only

---

## Versioning

**Current:** v1  
**Stability:** Experimental (0.1.x)  
**Breaking changes:** Will bump to v2

---

## OpenAPI Spec

Generate latest spec:
```bash
curl http://localhost:8000/openapi.json
```

Or from code:
```bash
python proprietary/living-cipher/generate_openapi.py
```

---

## Security

- No user data storage
- No session cookies
- No fingerprinting
- HTTPS recommended for production
- Revocation is in-memory (ephemeral)

---

## Monitoring

Health checks available for:
- Kubernetes liveness/readiness probes
- Load balancer health checks
- External monitoring services

---

## WebSocket (Future)

Planned for streaming mode. Stateless, no session affinity required.

---

**For complete API specification, see generated OpenAPI schema.**
