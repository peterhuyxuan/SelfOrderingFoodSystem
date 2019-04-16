import pytest
from menu_item import *
from main import Burger, Wrap
from inventory_item import inventoryItem
from order import Order

side_inv = inventoryItem('side_inv', 100)
drink_inv = inventoryItem('drink_inv', 100)
patty_inv = inventoryItem('patty_inv', 100) 
bun_inv = inventoryItem('bun_inv', 100)
other_inv = inventoryItem('other_inv', 100)

patty = Patty("patty", 10, patty_inv, 1)
bun = Bun("Bun", 11, bun_inv, 1)
other = OtherIngredient("other", 12, other_inv, 1)

burger = Burger()
burger.add_item(patty, 1)
burger.add_item(bun, 2)
burger.add_item(other, 1)

side = Side("side", 10, side_inv, 1)
drink = Drink("drink", 10, drink_inv, 1)

@pytest.fixture
def order_fixture():
    o = Order()
    o.add_main(burger)
    o.add_others(side,1)
    o.add_others(drink, 1)

    return o 

def test_empty_order():
    o = Order()
    assert len(o) == 0
    assert len(o.mains) == 0
    assert len(o.others) == 0

def test_add_main_success():
    o = Order()
    o.add_main(burger)
    assert len(o) == 1
    assert len(o.mains) == 1
    assert len(o.others) == 0
    assert o.total_price == 44

def test_add_main_none():
    o = Order()
    with pytest.raises(TypeError) as e:
        o.add_main(None)
        assert len(o) == 0
        assert len(o.mains) == 0

# Test for sides
def test_add_zero_sides():
    o = Order()
    with pytest.raises(ValueError) as e:
        o.add_others(side,0)
        assert len(o) == 0
        assert len(o.others) == 0

def test_add_wrong_type():
    o = Order()
    with pytest.raises(TypeError) as e:
        o.add_others(None,0)
        assert len(o) == 0
        assert len(o.others) == 0

def test_add_inventory_sides_limit():
    o = Order()
    with pytest.raises(ValueError) as e:
        o.add_others(side,101)
        assert len(o) == 0
        assert len(o.others) == 0

def test_add_one_sides():
    o = Order()
    o.add_others(side,1)
    assert len(o) == 1
    assert len(o.others) == 1
    assert o.total_price == 10

def test_remove_side(order_fixture):
    order_fixture.remove_other(side)
    assert len(order_fixture) == 2
    assert len(order_fixture.mains) == 1
    assert len(order_fixture.others) == 1
    assert order_fixture.total_price == 54

def test_add_one_sides_one_drinks():
    o = Order()
    o.add_others(side,1)
    o.add_others(drink,1)
    assert len(o) == 2
    assert len(o.others) == 2
    assert o.total_price == 20

# Test for drinks
def test_add_zero_drinks():
    o = Order()
    with pytest.raises(ValueError) as e:
        o.add_others(drink,0)
        assert len(o) == 0
        assert len(o.others) == 0

def test_add_inventory_drinks_limit():
    o = Order()
    with pytest.raises(ValueError) as e:
        o.add_others(drink,101)
        assert len(o) == 0
        assert len(o.others) == 0

def test_add_one_drink():
    o = Order()
    o.add_others(drink,1)
    assert len(o) == 1
    assert len(o.others) == 1
    assert o.total_price == 10

def test_remove_drink(order_fixture):
    order_fixture.remove_other(drink)
    assert len(order_fixture) == 2
    assert len(order_fixture.mains) == 1
    assert len(order_fixture.others) == 1
    assert order_fixture.total_price == 54

# test updating other qty
def test_update_side_qty(order_fixture):
    order_fixture.update_other(side, 2)
    assert len(order_fixture) == 4
    assert len(order_fixture.mains) == 1
    assert len(order_fixture.others) == 2
    assert order_fixture.total_price == 74


# test removing a main
def test_remove_main(order_fixture):
    order_fixture.remove_main(burger.id)
    assert len(order_fixture) == 2
    assert len(order_fixture.mains) == 0
    assert len(order_fixture.others) == 2
    assert order_fixture.total_price == 20

# test if order is complete
def test_order_complete(order_fixture):
    assert order_fixture._order_done == False
    order_fixture.mark_finished()
    assert order_fixture._order_done == True