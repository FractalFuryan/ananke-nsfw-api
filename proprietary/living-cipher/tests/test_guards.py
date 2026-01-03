"""Test suite for realism guards."""
from app.guards import assert_abstract, validate_geometry, RealismViolation
import pytest

def test_assert_abstract_passes():
    """Clean SVG should pass."""
    svg = "<svg><circle cx='50' cy='50' r='30'/></svg>"
    assert_abstract(svg)  # Should not raise

def test_assert_abstract_fails_on_skin():
    """SVG with 'skin' should fail."""
    svg = "<svg><rect fill='skin'/></svg>"
    with pytest.raises(RealismViolation):
        assert_abstract(svg)

def test_assert_abstract_fails_on_face():
    """SVG with 'face' should fail."""
    svg = "<svg><!-- face drawing --></svg>"
    with pytest.raises(RealismViolation):
        assert_abstract(svg)

def test_validate_geometry_passes():
    """Clean geometry should pass."""
    geom = {"curvature": 0.5, "symmetry_order": 4, "frequency": 1.2}
    validate_geometry(geom)  # Should not raise

def test_validate_geometry_fails_on_anatomy():
    """Geometry with anatomy keys should fail."""
    geom = {"curvature": 0.5, "skeleton": "humanoid"}
    with pytest.raises(RealismViolation):
        validate_geometry(geom)

def test_validate_geometry_fails_on_pose():
    """Geometry with pose keys should fail."""
    geom = {"pose": {"left_arm": 45}, "frequency": 1.0}
    with pytest.raises(RealismViolation):
        validate_geometry(geom)
