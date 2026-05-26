#!/bin/bash
# 블루-그린 배포 전환 스크립트
set -e

TARGET_GROUP_BLUE="arn:aws:elasticloadbalancing:ap-northeast-2:123456:targetgroup/blue"
TARGET_GROUP_GREEN="arn:aws:elasticloadbalancing:ap-northeast-2:123456:targetgroup/green"
LISTENER_ARN="arn:aws:elasticloadbalancing:ap-northeast-2:123456:listener/app"

CURRENT=$(aws elbv2 describe-listeners --listener-arns $LISTENER_ARN \
  --query "Listeners[0].DefaultActions[0].TargetGroupArn" --output text)

if [ "$CURRENT" = "$TARGET_GROUP_BLUE" ]; then
  NEXT=$TARGET_GROUP_GREEN
  echo "🟢 그린으로 전환 중..."
else
  NEXT=$TARGET_GROUP_BLUE
  echo "🔵 블루로 전환 중..."
fi

aws elbv2 modify-listener \
  --listener-arn $LISTENER_ARN \
  --default-actions Type=forward,TargetGroupArn=$NEXT

echo "✅ 전환 완료: $NEXT"
