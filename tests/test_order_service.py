import pytest
from unittest.mock import MagicMock, patch
from services.order_service import OrderService

@pytest.fixture
def order_service():
    db = MagicMock()
    payment = MagicMock()
    inventory = MagicMock()
    return OrderService(db=db, payment=payment, inventory=inventory)

def test_주문_생성_성공(order_service):
    order_service.inventory.check_stock.return_value = True
    order_service.payment.charge.return_value = {"status": "success", "tx_id": "TX001"}
    result = order_service.create_order(user_id=1, item_id=42, quantity=2)
    assert result["status"] == "confirmed"
    assert "order_id" in result

def test_재고_부족_시_주문_실패(order_service):
    order_service.inventory.check_stock.return_value = False
    with pytest.raises(ValueError, match="재고 부족"):
        order_service.create_order(user_id=1, item_id=42, quantity=100)

def test_결제_실패_시_롤백(order_service):
    order_service.inventory.check_stock.return_value = True
    order_service.payment.charge.side_effect = Exception("결제 거부")
    with pytest.raises(Exception):
        order_service.create_order(user_id=1, item_id=42, quantity=1)
    order_service.inventory.restore_stock.assert_called_once()
