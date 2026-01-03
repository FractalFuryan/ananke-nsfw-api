"""Stateless queue worker for batch processing."""
from ananke_core.core import generate_geometry
from ananke_core.video import procedural_motion
from ananke_core.render import render_svg
import json

def run_video_job(seed: str, frames: int = 60) -> list[dict]:
    """
    Generate video frames in batch. Stateless and replayable.
    
    Args:
        seed: Nonce for deterministic generation
        frames: Number of frames to generate
        
    Returns:
        List of frame geometries
    """
    base = generate_geometry(seed)
    results = []
    
    for i in range(frames):
        t = i / frames
        frame_geom = procedural_motion(base, t)
        results.append(frame_geom)
    
    return results

def run_batch_job(seeds: list[str]) -> dict:
    """
    Process multiple seeds in batch. Stateless.
    
    Args:
        seeds: List of nonces
        
    Returns:
        Dictionary mapping seeds to geometries
    """
    return {seed: generate_geometry(seed) for seed in seeds}

def worker_main(job_data: dict) -> dict:
    """
    Main worker entry point. Stateless job processor.
    
    Job types:
    - video: Generate video frames
    - batch: Process multiple seeds
    
    Args:
        job_data: Job specification
        
    Returns:
        Job results
    """
    job_type = job_data.get("type")
    
    if job_type == "video":
        seed = job_data["seed"]
        frames = job_data.get("frames", 60)
        return {
            "type": "video",
            "seed": seed,
            "frames": run_video_job(seed, frames)
        }
    
    elif job_type == "batch":
        seeds = job_data["seeds"]
        return {
            "type": "batch",
            "results": run_batch_job(seeds)
        }
    
    else:
        raise ValueError(f"Unknown job type: {job_type}")

# No persistence
# No state between jobs
# Jobs are replayable from seed
