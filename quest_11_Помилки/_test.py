# pytest --maxfail=1 --disable-warnings -q

import pytest
from service_body_test import Order



def test_order_total():
    items = [
        {"name": "Laptop", "price": 1000, "quantity": 1},
        {"name": "Mouse", "price": 50, "quantity": 2},
    ]

    order = Order(id=1, items=items)
    assert order.total() == 1100

    empty_order = Order(id=2, items=[])
    assert empty_order.total() == 0




def test_most_expensive():
    items = [
        {"name": "Book", "price": 20, "quantity": 3},
        {"name": "Phone", "price": 800, "quantity": 1},
        {"name": "Pen", "price": 2, "quantity": 10},
    ]

    order = Order(id=1, items=items)
    assert order.most_expensive() == {"name": "Phone", "price": 800, "quantity": 1}
    



def test_apply_discount_valid():
    items = [
        {"name": "Item1", "price": 100, "quantity": 1},
        {"name": "Item2", "price": 200, "quantity": 2},
    ]

    order = Order(id=1, items=items)
    

    order.apply_discount(10)

    assert order.items[0]["price"] == 90.0
    assert order.items[1]["price"] == 180.0



    order.apply_discount(0)
    assert order.items[0]["price"] == 90.0

    order.apply_discount(100)
    assert order.items[0]["price"] == 0.0




def test_apply_discount_invalid():
    items = [{"name": "Item", "price": 100, "quantity": 1}]
    order = Order(id=1, items=items)

    with pytest.raises(ValueError, match="Invalid discount"):
        order.apply_discount(-5)

    with pytest.raises(ValueError, match="Invalid discount"):
        order.apply_discount(105)


def test_order_repr():
    order = Order(id=123, items=[{"price": 10, "quantity": 1}])
    assert repr(order) == "<Order 123: 1 items>"