from ananke_core.core import generate_geometry

def test_bounds():
    g = generate_geometry("x")
    assert 0.1 <= g["curvature"] <= 0.9

def test_no_realism_keys():
    g = generate_geometry("x")
    forbidden = {"skin", "eyes", "face", "skeleton", "pose"}
    assert forbidden.isdisjoint(g.keys())

def test_determinism():
    a = generate_geometry("nonce123")
    b = generate_geometry("nonce123")
    assert a == b

def test_no_memory():
    a = generate_geometry("a")
    b = generate_geometry("b")
    assert a != b
