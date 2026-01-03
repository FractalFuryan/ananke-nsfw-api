from security.revoke import revoke, token_is_valid

def test_revocation():
    t = "tok"
    revoke(t)
    assert not token_is_valid(t)
