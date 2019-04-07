import pytest
from restaurant import Restaurant
from order import Order
from inventory_item import inventoryItem
from inventory import inventory, RemovalError, ItemNotFound
from main import Burger, Bun
"""
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
"""
@pytest.fixture
def restaurant_fixture():
    restaurant = Restaurant()
    names = ("Bun", "Patty", "Cheese", "Coke", "Chicken Nugget")
    for name in names:
        restaurant.inventory.add_stock(name, 100)

    bun_inv = restaurant.inventory.get_item("Bun")
    patty_inv = restaurant.inventory.get_item("Patty")
    cheese_inv = restaurant.inventory.get_item("Cheese")
    coke_inv = restaurant.inventory.get_item("Coke")
    chick_inv = restaurant.inventory.get_item("Chicken Nugget")
    restaurant.menu.add_bun("Bun", 10, bun_inv, 1)
    restaurant.menu.add_patty("Patty", 10, patty_inv, 1)
    restaurant.menu.add_other("Cheese", 10, cheese_inv, 1)
    restaurant.menu.add_drink("Canned Coke", 10, coke_inv, 1)
    restaurant.menu.add_side("Small Chicken Nugget", 10, chick_inv, 6)

    return restaurant

class TestUS1_1(object):
    def test_number_of_main(self, restaurant_fixture):
        assert len(restaurant_fixture.menu.mains) == 2
        assert "Burger" in restaurant_fixture.menu.mains
        assert "Wrap" in restaurant_fixture.menu.mains

"""
US1.2, 1.3 1.4 are handled in test_burger.py 
as unit test for main explictly
"""
class TestUS1_5:
    def test_display_burger(self, restaurant_fixture, capsys):
        burger = Burger()
        bun = restaurant_fixture.menu.get_item("Bun")
        patty = restaurant_fixture.menu.get_item("Patty")
        cheese = restaurant_fixture.menu.get_item("Cheese")
        burger.add_item(bun, 2)
        burger.add_item(patty, 1)
        burger.add_item(cheese, 1)
        burger.show_content(restaurant_fixture.menu)
        expected_output = ("Name\t\tQuantity\tPrice\n"
            "Bun\t\t2\t\t$10 * 2\n"
            "Patty\t\t1\t\t$10 * 1\n"
            "Cheese\t\t1\t\t$10 * 1\n"
            "Total: $40\n")
        assert capsys.readouterr().out == expected_output

"""
Test the restaurant by user stories and acceptance criteria
If the test cases are conducted explicitly bt other files
State that in commenet
"""