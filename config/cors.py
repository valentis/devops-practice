import os

_ALLOWED_ORIGINS = {
    "production":  ["https://devops-practice.com"],
    "staging":     ["https://staging.devops-practice.com"],
    "development": ["http://localhost:3000", "http://localhost:5173"],
}

def get_cors_config() -> dict:
    env = os.getenv("APP_ENV", "development")
    return {
        "allow_origins":     _ALLOWED_ORIGINS.get(env, ["http://localhost:3000"]),
        "allow_methods":     ["GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"],
        "allow_headers":     ["Authorization", "Content-Type", "X-Request-ID"],
        "allow_credentials": True,
        "max_age":           3600,
    }
