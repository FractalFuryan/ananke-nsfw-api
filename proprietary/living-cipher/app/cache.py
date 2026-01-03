"""Deterministic caching for pure outputs. No user identifiers, no behavioral signals."""
from functools import lru_cache
from ananke_core.core import generate_geometry as _generate_geometry

# Cache keyed only by nonce (deterministic input)
# No time-based eviction, no user tracking
@lru_cache(maxsize=1024)
def cached_geometry(nonce: str) -> dict:
    """Cache pure geometry generation. Cache miss is not a signal."""
    return _generate_geometry(nonce)

def clear_cache():
    """Manual cache clear for ops purposes."""
    cached_geometry.cache_clear()

def cache_info():
    """Return cache statistics (for monitoring, not analytics)."""
    info = cached_geometry.cache_info()
    return {
        "hits": info.hits,
        "misses": info.misses,
        "size": info.currsize,
        "maxsize": info.maxsize,
    }
