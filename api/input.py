import hashlib

def extract_ephemeral_features(blob: bytes, user_nonce: str):
    token = hashlib.sha256(blob + user_nonce.encode()).hexdigest()

    # Non-anatomical, lossy features only
    features = {
        "energy": sum(blob) % 256,
        "spread": (max(blob) - min(blob)) if blob else 0,
    }

    return token, features
