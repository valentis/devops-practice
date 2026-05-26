import time
from fastapi import Request, HTTPException
from redis import Redis

redis = Redis(host="redis", port=6379, decode_responses=True)

TIER_LIMITS = {"free": 30, "basic": 100, "pro": 500}

async def rate_limit_middleware(request: Request, call_next):
    user_id = request.state.user_id  # 인증 미들웨어에서 주입
    tier    = request.state.user_tier
    limit   = TIER_LIMITS.get(tier, 30)

    key    = f"ratelimit:{user_id}:{int(time.time() // 60)}"
    count  = redis.incr(key)
    if count == 1:
        redis.expire(key, 60)

    if count > limit:
        raise HTTPException(
            status_code=429,
            detail="요청 한도 초과",
            headers={"Retry-After": "60", "X-RateLimit-Limit": str(limit)},
        )

    response = await call_next(request)
    response.headers["X-RateLimit-Remaining"] = str(max(0, limit - count))
    return response
