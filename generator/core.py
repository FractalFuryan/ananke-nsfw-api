import hashlib

def seed_from_nonce(nonce: str) -> int:
    h = hashlib.sha256(nonce.encode()).hexdigest()
    return int(h[:16], 16)

def logistic_map(n: int, x: float = 0.37, r: float = 3.91) -> float:
    for _ in range(n):
        x = r * x * (1 - x)
    return x

def generate_geometry(nonce: str) -> dict:
    seed = seed_from_nonce(nonce)
    c = logistic_map(seed % 97)

    # Bounded, non-biological, non-escalating parameters
    return {
        "curvature": 0.25 + 0.5 * c,
        "symmetry_order": [3, 4, 6][seed % 3],
        "frequency": 1.0 + 0.3 * (seed % 5),
    }
