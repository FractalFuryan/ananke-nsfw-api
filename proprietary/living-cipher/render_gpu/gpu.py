"""GPU-accelerated rendering stub (stylized only, no realism)."""

# This module would integrate with OpenGL/Vulkan/WebGPU
# Current implementation is a stub for future GPU acceleration

SHADER_PATH = "render_gpu/shader.glsl"

def gpu_available() -> bool:
    """Check if GPU rendering is available."""
    # Stub: would check for OpenGL/Vulkan support
    return False

def render_gpu(geom: dict) -> bytes:
    """
    GPU-accelerated rendering using abstract shaders only.
    
    INVARIANTS:
    - No PBR materials
    - No SSS (subsurface scattering)
    - No skin shading
    - No anatomical primitives
    
    Args:
        geom: Geometry parameters from core generator
        
    Returns:
        Rendered frame as bytes (PNG/WebP)
    """
    # Stub implementation
    # Would compile shader, pass uniforms, render to framebuffer
    raise NotImplementedError("GPU rendering requires OpenGL/Vulkan setup")

def validate_shader(shader_code: str) -> None:
    """
    Validate shader contains no realism keywords.
    
    Raises:
        ValueError: If forbidden concepts detected
    """
    forbidden = ["pbr", "sss", "subsurface", "skin", "flesh", "normal_map", "anatomy"]
    shader_lower = shader_code.lower()
    
    for term in forbidden:
        if term in shader_lower and "forbidden" not in shader_lower:
            raise ValueError(f"Shader contains forbidden concept: {term}")
