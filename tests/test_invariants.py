def test_no_realism_keys():
    from generator.core import generate_geometry
    g = generate_geometry("x")
    forbidden = {"skin", "eyes", "face", "skeleton", "pose"}
    assert forbidden.isdisjoint(g.keys())

def test_bounds():
    from generator.core import generate_geometry
    g = generate_geometry("y")
    assert 0.1 <= g["curvature"] <= 0.9
