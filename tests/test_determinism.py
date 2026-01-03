from generator.core import generate_geometry

def test_determinism():
    a = generate_geometry("nonce123")
    b = generate_geometry("nonce123")
    assert a == b
