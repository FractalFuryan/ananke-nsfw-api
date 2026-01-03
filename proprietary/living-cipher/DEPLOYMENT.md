# Living Cipher — Deployment Guide

## Prerequisites

- Docker & Docker Compose
- Stripe account (for billing)

## Setup

1. **Configure Stripe**
   ```bash
   cd infra
   cp .env.example .env
   ```

2. **Add your Stripe credentials to `.env`:**
   - `STRIPE_SECRET_KEY`: From Stripe Dashboard → Developers → API Keys
   - `STRIPE_WEBHOOK_SECRET`: Create webhook endpoint for `checkout.session.completed`
   - `STRIPE_PRICE_ID`: Create product/price in Stripe Dashboard

3. **Build & Run**
   ```bash
   docker-compose up --build
   ```

## Services

- **Living Cipher API**: http://localhost:8000
  - Health: http://localhost:8000/health
  - Generate: `POST /v1/generate?nonce=test123`
  - Video MP4: `POST /v1/generate/video/mp4?nonce=test123`

- **Billing Service**: http://localhost:8001
  - Health: http://localhost:8001/health
  - Checkout: `POST /v1/billing/checkout?customer_ref=user123`
  - Webhook: `POST /v1/billing/webhook` (Stripe only)

## Testing

### Test Generation
```bash
curl -X POST "http://localhost:8000/v1/generate?nonce=test"
```

### Test Checkout Flow
```bash
curl -X POST "http://localhost:8001/v1/billing/checkout?customer_ref=user123"
```

## Production Deployment

1. Use managed database for entitlements (replace in-memory revocation)
2. Deploy behind reverse proxy (nginx/Caddy) with HTTPS
3. Configure Stripe webhook URL to point to your domain
4. Set environment variables via secrets manager
5. Enable container orchestration (K8s/ECS)

## Ethics Verification

Ethics gate runs automatically on container start. Manual verification:
```bash
docker exec -it living-cipher grep "Ethics" /ananke-core/README.md
```

## Monitoring

- Health checks run every 30s
- No analytics/telemetry collected
- Logs: endpoint, timestamp, status only

---

**System remains stateless, non-adaptive, and ethically sealed.**
