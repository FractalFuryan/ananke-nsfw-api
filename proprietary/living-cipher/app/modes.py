"""Clinical and harm-reduction mode system."""

MODES = {
    "standard": {
        "frames": 60,
        "frequency_cap": 1.5,
        "description": "Standard generation mode"
    },
    "clinical": {
        "frames": 30,
        "frequency_cap": 1.1,
        "description": "Reduced intensity for clinical/therapeutic contexts"
    }
}

def apply_mode(geom: dict, mode: str = "standard") -> dict:
    """
    Apply mode-specific constraints to geometry.
    
    Clinical mode provides:
    - Lower frequency cap (reduced visual intensity)
    - Shorter default frame counts
    - Explicit safety framing
    
    Args:
        geom: Base geometry from core generator
        mode: "standard" or "clinical"
        
    Returns:
        Mode-adjusted geometry
    """
    if mode not in MODES:
        raise ValueError(f"Unknown mode: {mode}. Use: {list(MODES.keys())}")
    
    config = MODES[mode]
    
    # Apply frequency cap
    if "frequency" in geom:
        geom["frequency"] = min(geom["frequency"], config["frequency_cap"])
    
    # Add mode metadata
    geom["mode"] = mode
    geom["mode_config"] = config["description"]
    
    return geom

def get_mode_defaults(mode: str) -> dict:
    """Get default parameters for a mode."""
    if mode not in MODES:
        raise ValueError(f"Unknown mode: {mode}")
    return MODES[mode].copy()

def list_modes() -> dict:
    """List all available modes and their descriptions."""
    return {
        name: config["description"]
        for name, config in MODES.items()
    }
