# OpenAPI Specification (Stub)

To be populated with full OpenAPI 3.0 spec for Living Cipher API.

## Endpoints

- `POST /v1/generate` — Generate single frame
- `POST /v1/generate/video` — Generate frame sequence
- `POST /v1/generate/video/mp4` — Generate encoded video

## Rate Limits

Non-behavioral, IP-based: 120 requests / 60 seconds

## Revocation

All tokens are revocable. Revoked tokens return 403.
