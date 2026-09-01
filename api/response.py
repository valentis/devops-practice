from dataclasses import dataclass, asdict
from typing import Any

@dataclass
class ApiResponse:
    data: Any = None
    error: str | None = None
    meta: dict | None = None

    def to_dict(self) -> dict:
        return asdict(self)

def ok(data, meta=None) -> dict:
    return ApiResponse(data=data, meta=meta).to_dict()

def fail(message: str) -> dict:
    return ApiResponse(error=message).to_dict()
