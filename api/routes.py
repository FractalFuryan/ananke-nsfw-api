from fastapi import APIRouter, HTTPException
from fastapi.responses import Response, StreamingResponse
from generator.core import generate_geometry
from generator.render import render_stub
from generator.video import procedural_motion
from generator.encode import encode_svg_frames_to_mp4
from security.revoke import token_is_valid

router = APIRouter()

@router.post("/generate")
def generate(nonce: str, token: str | None = None):
    if token and not token_is_valid(token):
        raise HTTPException(403, "Token revoked")

    geom = generate_geometry(nonce)
    img = render_stub(geom)
    return {"geometry": geom, "preview": img}

@router.post("/generate/video")
def generate_video(nonce: str, frames: int = 60):
    seq = []
    base = generate_geometry(nonce)
    for i in range(frames):
        seq.append(procedural_motion(base, t=i/frames))
    return {"frames": seq}

@router.post("/generate/video/mp4")
def generate_video_mp4(nonce: str, frames: int = 60, fps: int = 30):
    base = generate_geometry(nonce)
    svgs = []
    for i in range(frames):
        g = procedural_motion(base, t=i/frames)
        svgs.append(render_stub(g))
    mp4 = encode_svg_frames_to_mp4(svgs, fps=fps)
    return Response(content=mp4, media_type="video/mp4")

@router.post("/generate/video/stream")
def stream_video(nonce: str, frames: int = 60):
    def gen():
        base = generate_geometry(nonce)
        for i in range(frames):
            g = procedural_motion(base, t=i/frames)
            svg = render_stub(g)
            yield svg.encode() + b"\n"

    return StreamingResponse(gen(), media_type="text/plain")

@router.post("/revoke")
def revoke_token(token: str):
    from security.revoke import revoke
    revoke(token)
    return {"status": "revoked"}
