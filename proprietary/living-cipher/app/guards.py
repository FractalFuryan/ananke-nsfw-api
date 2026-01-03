"""Realism assertion guard - last line of defense against drift."""

FORBIDDEN_TERMS = {"skin", "face", "eye", "eyes", "hair", "body", "human", "person", "anatomy"}

class RealismViolation(RuntimeError):
    """Raised when realism terms are detected in output."""
    pass

def assert_abstract(svg: str) -> None:
    """
    Assert that rendered output contains no realism terms.
    This is a last-line guard against drift in the rendering layer.
    
    Raises:
        RealismViolation: If any forbidden term is detected
    """
    svg_lower = svg.lower()
    for term in FORBIDDEN_TERMS:
        if term in svg_lower:
            raise RealismViolation(f"Realism term detected: {term}")

def validate_geometry(geom: dict) -> None:
    """
    Validate that geometry parameters contain no realism keys.
    
    Raises:
        RealismViolation: If any forbidden key is detected
    """
    forbidden_keys = {"skin", "eyes", "face", "skeleton", "pose", "anatomy"}
    found = forbidden_keys.intersection(geom.keys())
    if found:
        raise RealismViolation(f"Realism keys detected: {found}")
