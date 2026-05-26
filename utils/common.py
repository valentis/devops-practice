from datetime import datetime
from typing import TypeVar, Generic
from dataclasses import dataclass

T = TypeVar("T")

@dataclass
class PageResult(Generic[T]):
    items: list[T]
    total: int
    page: int
    page_size: int

    @property
    def total_pages(self) -> int:
        return -(-self.total // self.page_size)  # ceiling division

    def to_dict(self) -> dict:
        return {
            "items": self.items,
            "meta": {
                "total": self.total,
                "page": self.page,
                "page_size": self.page_size,
                "total_pages": self.total_pages,
            }
        }

def format_kr_datetime(dt: datetime) -> str:
    """KST 기준 한국어 날짜 포맷 반환"""
    return dt.strftime("%Y년 %m월 %d일 %H:%M")
