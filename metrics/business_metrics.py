from prometheus_client import Counter, Gauge, Histogram

# 주문 카운터
orders_total = Counter(
    "orders_total",
    "누적 주문 건수",
    ["status", "channel"],  # 라벨: 성공/실패, 웹/앱
)

# 결제 성공률
payment_success_ratio = Gauge(
    "payment_success_ratio",
    "최근 5분 결제 성공률 (0~1)",
)

# 결제 소요 시간 히스토그램
checkout_duration = Histogram(
    "checkout_duration_seconds",
    "결제 완료까지 소요 시간",
    buckets=[0.1, 0.25, 0.5, 1.0, 2.5, 5.0, 10.0],
)

def record_order(status: str, channel: str, duration: float):
    orders_total.labels(status=status, channel=channel).inc()
    checkout_duration.observe(duration)
