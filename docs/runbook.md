# 장애 대응 런북

## 🔴 시나리오 1: API 서버 전체 다운

### 증상
- 모든 API 엔드포인트 `502 Bad Gateway` 반환
- Slack `#alert-prod` 채널에 알림 수신

### 확인 명령어
```bash
# Pod 상태 확인
kubectl get pods -n production -l app=api-server

# 최근 로그 확인
kubectl logs -n production -l app=api-server --tail=100

# 이벤트 확인
kubectl get events -n production --sort-by=.lastTimestamp | tail -20
```

### 조치
1. CrashLoopBackOff → `kubectl rollout undo deployment/api-server -n production`
2. OOMKilled → 메모리 리소스 임시 증설 후 팀 공유
3. 이미지 풀 실패 → ECR 접근 권한 확인

### 에스컬레이션
10분 내 해결 안 되면 → 온콜 리드 호출
