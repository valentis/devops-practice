import time
from enum import Enum
from threading import Lock

class State(Enum):
    CLOSED = "closed"
    OPEN = "open"
    HALF_OPEN = "half_open"

class CircuitBreaker:
    def __init__(self, failure_threshold=0.5, min_calls=10, reset_timeout=10):
        self.failure_threshold = failure_threshold
        self.min_calls = min_calls
        self.reset_timeout = reset_timeout
        self._state = State.CLOSED
        self._calls = self._failures = 0
        self._opened_at = None
        self._lock = Lock()

    def call(self, fn, *args, **kwargs):
        with self._lock:
            if self._state == State.OPEN:
                if time.time() - self._opened_at > self.reset_timeout:
                    self._state = State.HALF_OPEN
                else:
                    raise RuntimeError("서킷 브레이커 Open 상태 — 요청 차단")

        try:
            result = fn(*args, **kwargs)
            self._on_success()
            return result
        except Exception as e:
            self._on_failure()
            raise

    def _on_success(self):
        with self._lock:
            self._calls += 1
            if self._state == State.HALF_OPEN:
                self._state = State.CLOSED
                self._calls = self._failures = 0

    def _on_failure(self):
        with self._lock:
            self._calls += 1
            self._failures += 1
            if (self._calls >= self.min_calls and
                    self._failures / self._calls >= self.failure_threshold):
                self._state = State.OPEN
                self._opened_at = time.time()
