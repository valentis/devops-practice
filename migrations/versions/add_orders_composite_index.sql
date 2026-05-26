-- 주문 조회 성능 개선 인덱스
-- 실행 전 반드시 CONCURRENTLY 옵션 사용 (잠금 없이 생성)

CREATE INDEX CONCURRENTLY IF NOT EXISTS
  idx_orders_user_status_date
ON orders (user_id, status, created_at DESC)
WHERE status != 'CANCELLED';

-- 실행 후 쿼리 플랜 확인
EXPLAIN (ANALYZE, BUFFERS)
SELECT * FROM orders
WHERE user_id = 12345
  AND status IN ('PENDING', 'CONFIRMED')
ORDER BY created_at DESC
LIMIT 20;
