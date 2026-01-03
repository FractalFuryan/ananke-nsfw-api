import math

def procedural_motion(geom: dict, t: float) -> dict:
    phase = (math.sin(t) + 1.0) / 2.0  # [0,1]
    return {
        **geom,
        "curvature": max(0.1, min(0.9, geom["curvature"] * (0.8 + 0.4 * phase))),
        "frequency": geom["frequency"] * (0.9 + 0.2 * phase),
    }
