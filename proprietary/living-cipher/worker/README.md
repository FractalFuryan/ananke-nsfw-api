# Stateless Queue Workers

## Design Principles

1. **Stateless**: No memory between jobs
2. **Deterministic**: Same input → same output
3. **Replayable**: Jobs can be retried without side effects
4. **No Persistence**: Workers don't store results

## Job Types

### Video Job
```json
{
  "type": "video",
  "seed": "nonce123",
  "frames": 60
}
```

### Batch Job
```json
{
  "type": "batch",
  "seeds": ["seed1", "seed2", "seed3"]
}
```

## Usage

```python
from worker.worker import worker_main

job = {"type": "video", "seed": "test", "frames": 30}
result = worker_main(job)
```

## Deployment

Workers can be deployed as:
- Celery tasks
- AWS Lambda functions
- Kubernetes Jobs
- Docker containers

All modes maintain stateless, deterministic behavior.

## Invariants

- ✅ No cross-job state
- ✅ No user tracking
- ✅ No result caching (caller's responsibility)
- ✅ Deterministic from seed
- ✅ Ethics constraints inherited from core
