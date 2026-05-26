import redis
import uuid
import time

def acquire_lock(client: redis.Redis, key: str, ttl_ms=5000) -> str | None:
    token = str(uuid.uuid4())
    if client.set(f"lock:{key}", token, nx=True, px=ttl_ms):
        return token
    return None

def release_lock(client: redis.Redis, key: str, token: str):
    script = """
    if redis.call("get", KEYS[1]) == ARGV[1] then
        return redis.call("del", KEYS[1])
    end
    return 0
    """
    client.eval(script, 1, f"lock:{key}", token)
