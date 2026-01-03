REVOKED_TOKENS = set()

def revoke(token: str):
    REVOKED_TOKENS.add(token)

def token_is_valid(token: str) -> bool:
    return token not in REVOKED_TOKENS
