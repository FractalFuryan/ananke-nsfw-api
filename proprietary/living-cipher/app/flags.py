"""Feature flags for production kill-switches. No analytics, just binary toggles."""

FLAGS = {
    "video_enabled": True,
    "mp4_enabled": True,
    "streaming_enabled": True,
}

def enabled(name: str) -> bool:
    """Check if a feature is enabled. Returns False for unknown flags."""
    return FLAGS.get(name, False)

def all_flags() -> dict:
    """Return current flag state (for health/status endpoints)."""
    return FLAGS.copy()
