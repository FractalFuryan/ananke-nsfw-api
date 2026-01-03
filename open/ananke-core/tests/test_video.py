from ananke_core.video import procedural_motion
from ananke_core.core import generate_geometry

def test_video_determinism():
    base = generate_geometry("vnonce")
    a = [procedural_motion(base, i/10) for i in range(10)]
    b = [procedural_motion(base, i/10) for i in range(10)]
    assert a == b
