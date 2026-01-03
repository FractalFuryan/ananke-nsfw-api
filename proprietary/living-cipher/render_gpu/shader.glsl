// Abstract stylized shader - NO realism, NO skin, NO anatomy
// Purpose: performance, not photorealism

#version 330 core

in vec2 fragCoord;
out vec4 fragColor;

uniform float curvature;
uniform int symmetry_order;
uniform float frequency;
uniform float time;

void main() {
    vec2 uv = (fragCoord - vec2(320.0)) / 320.0;
    float d = length(uv);
    
    // Abstract wave pattern based on geometry parameters
    float angle = atan(uv.y, uv.x);
    float wave = sin(d * frequency * 12.0 + angle * float(symmetry_order));
    
    // Apply curvature modulation
    float intensity = wave * curvature;
    
    // Abstract color (no flesh tones, no realism)
    vec3 color = vec3(
        0.5 + 0.5 * sin(intensity * 3.0),
        0.5 + 0.5 * sin(intensity * 3.0 + 2.0),
        0.5 + 0.5 * sin(intensity * 3.0 + 4.0)
    );
    
    fragColor = vec4(color, 1.0);
}

// FORBIDDEN CONCEPTS (CI enforced):
// - PBR (Physically Based Rendering)
// - SSS (Subsurface Scattering)
// - Normal maps referencing anatomy
// - Skin shading models
// - Flesh tones or skin-like colors
// - Anatomical references of any kind
