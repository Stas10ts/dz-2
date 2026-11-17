import pytest
from pydantic import ValidationError
from src.order_processor import Order


def test_valid_order():
    order = Order(customer_email="TEST@example.com", amount=100)
    assert order.customer_email == "test@example.com"
    assert order.amount == 100


def test_invalid_email():
    with pytest.raises(ValueError):
        Order(customer_email="wrong-email", amount=100)


def test_invalid_amount():
    with pytest.raises(ValueError):
        Order(customer_email="test@example.com", amount=0)


def test_default_status():
    order = Order(customer_email="test@example.com", amount=50)
    assert order.status == "new"


def test_to_dict():
    order = Order(customer_email="test@example.com", amount=50)
    assert order.to_dict()["amount"] == 50
