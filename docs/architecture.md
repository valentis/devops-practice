# 시스템 아키텍처 개요

## 전체 구성도

```mermaid
graph TD
  Client([클라이언트]) -->|HTTPS| CDN[CloudFront CDN]
  CDN -->|캐시 미스| ALB[Application Load Balancer]
  ALB -->|라운드로빈| API1[API Server Pod 1]
  ALB --> API2[API Server Pod 2]
  ALB --> API3[API Server Pod 3]
  API1 & API2 & API3 -->|읽기| RDB_R[(PostgreSQL Replica)]
  API1 & API2 & API3 -->|쓰기| RDB_W[(PostgreSQL Primary)]
  API1 & API2 & API3 <-->|캐시| Redis[(Redis Cluster)]
  API1 & API2 & API3 -->|비동기| Queue[SQS 큐]
  Queue --> Worker[Worker Pod]
```

## 주요 컴포넌트 설명

| 컴포넌트 | 기술 | 역할 |
|---|---|---|
| API Server | FastAPI | REST API 처리 |
| PostgreSQL | RDS Multi-AZ | 주 데이터 저장소 |
| Redis | ElastiCache | 세션/캐시 |
| SQS | AWS SQS | 비동기 작업 큐 |
