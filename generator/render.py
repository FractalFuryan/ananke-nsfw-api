def render_stub(geom: dict) -> str:
    # Placeholder: returns an abstract SVG descriptor (no pixels, no realism)
    return (
        f"<svg viewBox='0 0 100 100'>"
        f"<circle cx='50' cy='50' r='{20 + geom['curvature']*30}' "
        f"fill='none' stroke='black' stroke-width='2'/>"
        f"</svg>"
    )
