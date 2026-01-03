from fastapi import FastAPI, Response, HTTPException
from ananke_core.video import procedural_motion
from ananke_core.render import render_svg

from .revocation import token_is_valid
from .encode import encode_svgs_to_mp4
from .health import add_health_endpoint
from .cache import cached_geometry
from .flags import enabled
from .guards import assert_abstract, validate_geometry
from .modes import apply_mode
from .addiction_metrics import record_event, am_enabled

app = FastAPI(title="living-cipher", version="0.1")
add_health_endpoint(app)

@app.post("/v1/generate")
def generate(nonce: str, token: str | None = None, mode: str = "standard"):
    if am_enabled():
        record_event(f"generate:{mode}")
    
    if token and not token_is_valid(token):
        raise HTTPException(403, "Token revoked")
    
    geom = cached_geometry(nonce)
    geom = apply_mode(geom, mode)
    validate_geometry(geom)
    svg = render_svg(geom)
    assert_abstract(svg)
    return {"geometry": geom, "svg": svg}

@app.post("/v1/generate/video")
def generate_video(nonce: str, frames: int = 60, mode: str = "standard"):
    if not enabled("video_enabled"):
        raise HTTPException(503, "Video temporarily disabled")
    
    if am_enabled():
        record_event(f"video:{mode}")
    
    base = cached_geometry(nonce)
    base = apply_mode(base, mode)
    validate_geometry(base)
    svgs = []
    for i in range(frames):
        g = procedural_motion(base, t=i/frames)
        svg = render_svg(g)
        assert_abstract(svg)
        svgs.append(svg)
    return {"frames": svgs}

@app.post("/v1/generate/video/mp4")
def generate_video_mp4(nonce: str, frames: int = 60, fps: int = 30, mode: str = "standard"):
    if not enabled("mp4_enabled"):
        raise HTTPException(503, "MP4 encoding temporarily disabled")
    
    if am_enabled():
        record_event(f"mp4:{mode}")
    
    base = cached_geometry(nonce)
    base = apply_mode(base, mode)
    validate_geometry(base)
    svgs = [render_svg(procedural_motion(base, t=i/frames)) for i in range(frames)]
    for svg in svgs:
        assert_abstract(svg)
    mp4_bytes = encode_svgs_to_mp4(svgs, fps=fps)
    return Response(content=mp4_bytes, media_type="video/mp4")
