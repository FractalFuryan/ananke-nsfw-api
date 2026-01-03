# OpenAPI Specification

## Generate

To generate the latest OpenAPI spec from the Living Cipher service:

```bash
cd proprietary/living-cipher
python generate_openapi.py > ../../open/ananke-api-spec/openapi.json
```

Or from running service:

```bash
curl http://localhost:8000/openapi.json > open/ananke-api-spec/openapi.json
```

## Principles

- All endpoints are stateless
- No user tracking or analytics
- Deterministic outputs from seeds
- Rate limiting is non-behavioral (IP-based only)
- All tokens are revocable

## Key Endpoints

- `POST /v1/generate` — Generate single geometry + SVG
- `POST /v1/generate/video` — Generate frame sequence
- `POST /v1/generate/video/mp4` — Generate encoded MP4
- `GET /health` — Service health + ethics verification

## Ethics Verification

The `/health` endpoint returns ethics anchor and invariant status for real-time auditing.
