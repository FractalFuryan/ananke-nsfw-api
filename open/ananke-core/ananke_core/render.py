def render_svg(geom: dict) -> str:
    r = 20 + geom["curvature"] * 30
    return (
        "<svg viewBox='0 0 100 100' xmlns='http://www.w3.org/2000/svg'>"
        f"<circle cx='50' cy='50' r='{r:.3f}' fill='none' stroke='black' stroke-width='2'/>"
        "</svg>"
    )
