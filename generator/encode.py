import subprocess
import tempfile
import os

def encode_svg_frames_to_mp4(svg_frames: list[str], fps: int = 30) -> bytes:
    with tempfile.TemporaryDirectory() as d:
        # Write SVG frames
        for i, svg in enumerate(svg_frames):
            path = os.path.join(d, f"f_{i:04d}.svg")
            with open(path, "w") as f:
                f.write(svg)

        out = os.path.join(d, "out.mp4")

        # Deterministic, bounded encoding
        subprocess.run([
            "ffmpeg",
            "-y",
            "-framerate", str(fps),
            "-i", os.path.join(d, "f_%04d.svg"),
            "-pix_fmt", "yuv420p",
            "-movflags", "+faststart",
            "-vf", "scale=640:640:flags=neighbor",
            out
        ], check=True)

        with open(out, "rb") as f:
            return f.read()
