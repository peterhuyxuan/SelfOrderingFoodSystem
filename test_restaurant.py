import pytest
from restaurant import Restaurant
from order import Order
from inventory_item import inventoryItem
from inventory import inventory, RemovalError, ItemNotFound

import sys

system = Restaurant()

def test_no_order(capsys):
    assert len(system.orders) == 0

def test_add_order(capsys):
    order = Order()
    system.add_order(order)
    assert len(system.orders) == 1
    assert system.order_id == order.id

#add check first order later
#def test_get_second_order(capsys):
#    assert system.order_id == 1
#    assert system.get_order(system.order_id) == 1

def test_get_second_order(capsys):
    order2 = Order()
    system.add_order(order2)
    assert system.order_id == 1
    assert system.get_order(system.order_id) == order.id