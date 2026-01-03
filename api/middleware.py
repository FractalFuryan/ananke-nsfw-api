# Middleware layer for guards and validation
from fastapi import Request, HTTPException
import time

# Rate limiting (non-behavioral, IP-based only)
WINDOW, LIMIT = 60, 120
hits = {}

async def rate_limit(request: Request):
    ip = request.client.host
    now = int(time.time())
    hits.setdefault(ip, [])
    hits[ip] = [t for t in hits[ip] if now - t < WINDOW]
    if len(hits[ip]) >= LIMIT:
        raise HTTPException(429, "Rate limit")
    hits[ip].append(now)
