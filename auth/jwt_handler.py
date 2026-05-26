"""JWT authentication handler."""
import jwt

def generate_token(user_id: str, secret: str) -> str:
    return jwt.encode({"sub": user_id}, secret, algorithm="HS256")

def verify_token(token: str, secret: str) -> dict:
    return jwt.decode(token, secret, algorithms=["HS256"])
