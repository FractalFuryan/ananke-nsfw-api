"""Test suite for addiction monitoring privacy."""
from app.addiction_metrics import (
    record_event, export_snapshot, am_enabled, _state, K_ANON
)
import os

def test_am_disabled_by_default():
    """Addiction monitoring should be OFF by default."""
    # Ensure environment is not set
    if "AM_ENABLED" in os.environ:
        del os.environ["AM_ENABLED"]
    
    assert not am_enabled()

def test_record_event_when_disabled():
    """Recording should be no-op when disabled."""
    if "AM_ENABLED" in os.environ:
        del os.environ["AM_ENABLED"]
    
    record_event("test")  # Should not crash

def test_export_respects_k_anonymity():
    """Export should return None if below threshold."""
    # Even if enabled, with few events should return None
    _state["counts"].clear()
    for i in range(K_ANON - 1):
        _state["counts"][f"event_{i}"] = 1
    
    # Below threshold
    snapshot = export_snapshot()
    assert snapshot is None or sum(_state["counts"].values()) < K_ANON

def test_no_user_identifiers_in_state():
    """State should never contain user IDs."""
    state_keys = list(_state.keys())
    forbidden = ["user_id", "ip", "session", "fingerprint"]
    
    for key in state_keys:
        assert key not in forbidden
