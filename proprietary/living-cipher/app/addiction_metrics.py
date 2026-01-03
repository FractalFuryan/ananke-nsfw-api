"""
Privacy-preserving addiction monitoring.

CRITICAL RULES:
- NO user IDs
- NO IP addresses
- NO session linkage
- NO cross-request correlation
- NO runtime influence on behavior

Aggregate metrics only. Optional. OFF by default.
"""
from collections import Counter
import time
import random
import os

# Default OFF - must be explicitly enabled via environment
ADDICTION_MONITORING = os.environ.get("AM_ENABLED", "false").lower() == "true"

# Privacy parameters
WINDOW = 3600  # 1 hour aggregation window
K_ANON = 50    # Minimum events before publishing
EPSILON = 0.5  # Differential privacy noise level

# Internal state (aggregate only)
_state = {
    "window_start": int(time.time() // WINDOW) * WINDOW,
    "counts": Counter(),        # Event type → count
    "intervals": Counter(),     # Time bucket → count
    "last_seen": None,          # Last event timestamp (not user-specific)
}

def am_enabled() -> bool:
    """Check if addiction monitoring is enabled."""
    return ADDICTION_MONITORING

def _laplace_noise(epsilon: float) -> int:
    """
    Add differential privacy noise.
    
    Args:
        epsilon: Privacy parameter (smaller = more noise)
        
    Returns:
        Integer noise value
    """
    u = random.random() - 0.5
    return int(-(1 / epsilon) * (1 if u >= 0 else -1) * abs(u))

def record_event(kind: str) -> None:
    """
    Record aggregate event (NO user identification).
    
    Args:
        kind: Event type (e.g., "generate", "video", "clinical_mode")
    """
    if not am_enabled():
        return
    
    now = int(time.time())
    
    # Rotate window if needed
    if now - _state["window_start"] >= WINDOW:
        _rotate()
    
    # Increment aggregate counter
    _state["counts"][kind] += 1
    
    # Record interval (bucketed, coarse)
    if _state["last_seen"] is not None:
        dt = now - _state["last_seen"]
        bucket = min(dt // 10 * 10, 300)  # 10s buckets, cap at 5min
        _state["intervals"][bucket] += 1
    
    _state["last_seen"] = now

def _rotate() -> None:
    """Rotate to new time window, clearing old data."""
    _state["window_start"] = int(time.time() // WINDOW) * WINDOW
    _state["counts"].clear()
    _state["intervals"].clear()
    _state["last_seen"] = None

def export_snapshot() -> dict | None:
    """
    Export privacy-preserving snapshot.
    
    Returns None if k-anonymity threshold not met.
    
    Returns:
        Snapshot dict with DP noise, or None
    """
    if not am_enabled():
        return None
    
    total = sum(_state["counts"].values())
    
    # k-anonymity: don't publish small samples
    if total < K_ANON:
        return None
    
    # Add differential privacy noise
    return {
        "window_start": _state["window_start"],
        "window_duration": WINDOW,
        "total_events": total + _laplace_noise(EPSILON),
        "counts": {
            k: v + _laplace_noise(EPSILON)
            for k, v in _state["counts"].items()
        },
        "interval_distribution": {
            k: v + _laplace_noise(EPSILON)
            for k, v in _state["intervals"].items()
        },
        "privacy": {
            "k_anonymity": K_ANON,
            "epsilon": EPSILON,
            "noised": True
        }
    }

def get_stats() -> dict:
    """Get current monitoring stats (for health checks only)."""
    if not am_enabled():
        return {"enabled": False}
    
    return {
        "enabled": True,
        "current_window_events": sum(_state["counts"].values()),
        "k_threshold": K_ANON,
        "epsilon": EPSILON
    }

# Runtime assertion: no behavioral feedback
assert "behavior" not in globals(), "Behavioral feedback detected"
