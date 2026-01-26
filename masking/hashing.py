import hashlib

def hash_value(value: str) -> str:
    """
    Deterministic hash using SHA-256
    Same input -> same output
    """
    return hashlib.sha256(value.encode()).hexdigest()
