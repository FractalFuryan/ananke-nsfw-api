"""Test suite for clinical mode."""
from app.modes import apply_mode, get_mode_defaults, list_modes

def test_standard_mode():
    """Standard mode should apply correct constraints."""
    geom = {"curvature": 0.5, "frequency": 1.8}
    result = apply_mode(geom, "standard")
    
    assert result["frequency"] <= 1.5  # Standard cap
    assert result["mode"] == "standard"

def test_clinical_mode():
    """Clinical mode should reduce intensity."""
    geom = {"curvature": 0.5, "frequency": 1.8}
    result = apply_mode(geom, "clinical")
    
    assert result["frequency"] <= 1.1  # Clinical cap (lower)
    assert result["mode"] == "clinical"

def test_mode_defaults():
    """Mode defaults should be retrievable."""
    clinical = get_mode_defaults("clinical")
    assert clinical["frames"] == 30
    assert clinical["frequency_cap"] == 1.1

def test_list_modes():
    """Should list all available modes."""
    modes = list_modes()
    assert "standard" in modes
    assert "clinical" in modes
