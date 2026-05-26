import time
import random
from functools import wraps

def retry_with_backoff(max_retries=3, base_delay=1.0, backoff=2.0, jitter=0.5):
    """지수 백오프 재시도 데코레이터"""
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            for attempt in range(max_retries + 1):
                try:
                    return fn(*args, **kwargs)
                except Exception as e:
                    # 4xx는 재시도 무의미 → 즉시 raise
                    if hasattr(e, "status_code") and 400 <= e.status_code < 500:
                        raise
                    if attempt == max_retries:
                        raise
                    delay = base_delay * (backoff ** attempt)
                    delay += random.uniform(0, jitter)   # 지터 추가
                    print(f"[재시도 {attempt+1}/{max_retries}] {delay:.2f}초 대기 중...")
                    time.sleep(delay)
        return wrapper
    return decorator

# 사용 예시
# @retry_with_backoff(max_retries=3)
# def call_payment_api(payload): ...
