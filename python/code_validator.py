
import base64
import secrets
import hashlib

def create_random_code_validation():
    """Returns a validation Tuple:  (code_challenge, code_verifier)"""
    random = create_random_verifier()
    code_challenge = encrypt_verifier(random)

    print(f"Login 'code_challenge': '{code_challenge}'")
    print(f"Auth Token Post: 'code_verifier': '{random}'")
    return code_challenge, random

def create_random_verifier() -> str:
    return base64.urlsafe_b64encode(secrets.token_bytes(32))

def encrypt_verifier( verifier: str ) -> str:
    m = hashlib.sha256()
    m.update(verifier)
    d = m.digest()
    return base64.urlsafe_b64encode(d).decode().replace("=", "")
