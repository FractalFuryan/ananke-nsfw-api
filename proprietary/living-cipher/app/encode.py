import os
import tempfile
import subprocess

def encode_svgs_to_mp4(svg_frames: list[str], fps: int = 30) -> bytes:
    with tempfile.TemporaryDirectory() as d:
        for i, svg in enumerate(svg_frames):
            with open(os.path.join(d, f"f_{i:04d}.svg"), "w", encoding="utf-8") as f:
                f.write(svg)

        out = os.path.join(d, "out.mp4")
        subprocess.run([
            "ffmpeg", "-y",
            "-framerate", str(fps),
            "-i", os.path.join(d, "f_%04d.svg"),
            "-pix_fmt", "yuv420p",
            "-movflags", "+faststart",
            "-vf", "scale=640:640:flags=neighbor",
            out
        ], check=True, capture_output=True)

        with open(out, "rb") as f:
            return f.read()
