REVOKED = set()

def revoke(token: str) -> None:
    REVOKED.add(token)

def token_is_valid(token: str) -> bool:
    return token not in REVOKED
