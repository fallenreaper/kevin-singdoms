
import base64
import secrets
import hashlib

def create_code_validation():
    """Returns a validation Tuple:  (code_challenge, code_verifier)"""
    random = base64.urlsafe_b64encode(secrets.token_bytes(32))
    m = hashlib.sha256()
    m.update(random)
    d = m.digest()
    code_challenge = base64.urlsafe_b64encode(d).decode().replace("=", "")

    print(f"Login 'code_challenge': '{code_challenge}'")
    print(f"Auth Token Post: 'code_verifier': '{random}'")
    return code_challenge, random