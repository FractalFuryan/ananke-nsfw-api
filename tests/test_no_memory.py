from generator.core import generate_geometry

def test_no_memory():
    a = generate_geometry("a")
    b = generate_geometry("b")
    assert a != b
