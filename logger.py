import structlog

structlog.configure(
    processors=[
        structlog.contextvars.merge_contextvars,
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.processors.JSONRenderer(),
    ]
)

log = structlog.get_logger()

# Usage:
# log.info("user_login", user_id=42, ip="1.2.3.4")
