# Deployment Environments

## Development

Basic setup for local development:

```bash
cd infra
docker-compose up
```

## Production

Production-hardened deployment with resource limits and restart policies:

```bash
cd infra
docker-compose -f docker-compose.prod.yml up -d
```

### Production Features

- **Resource Limits**: CPU and memory caps prevent runaway processes
- **Restart Policies**: `unless-stopped` ensures service recovery
- **Health Checks**: 30s interval monitoring
- **Log Rotation**: 10MB max size, 3 files retained
- **Reservations**: Guaranteed minimum resources

### Resource Allocation

**Living Cipher:**
- Limit: 2 CPU cores, 4GB RAM
- Reserved: 1 CPU core, 2GB RAM

**Billing:**
- Limit: 1 CPU core, 1GB RAM
- Reserved: 0.5 CPU cores, 512MB RAM

### Monitoring

Health endpoints available at:
- Living Cipher: http://localhost:8000/health
- Billing: http://localhost:8001/health

Health checks include ethics verification status.

### Logs

View logs:
```bash
docker-compose -f docker-compose.prod.yml logs -f living-cipher
```

Logs contain only: endpoint, timestamp, status (no user data).
