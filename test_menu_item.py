import pytest
from src.menu import Menu, ItemNotFound
from src.menu_item import MenuItem, Bun, Side, Drink, Patty, OtherIngredient, InvalidFieldError
from src.inventory_item import inventoryItem

inv_item = inventoryItem("test item", 100)

def test_create_side():
    s = Side("side-1", 10,inv_item, 1)
    assert s._id == MenuItem._id
    assert s._price == 10
    assert s._name == "side-1"
    assert s._component == inv_item
    assert s._component_qty == 1

def test_create_drink():
    s = Drink("drink-1", 10,inv_item, 1)
    assert s._id == MenuItem._id
    assert s._price == 10
    assert s._name == "drink-1"
    assert s._component == inv_item
    assert s._component_qty == 1

def test_create_patty():
    s = Patty("patty-1", 10,inv_item, 3)
    assert s._id == MenuItem._id
    assert s._price == 10
    assert s._name == "patty-1"
    assert s._component == inv_item
    assert s._component_qty == 3

def test_create_bun():
    s = Bun("bun-1", 10, inv_item, 7)
    assert s._id == MenuItem._id
    assert s._price == 10
    assert s._name == "bun-1"
    assert s._component == inv_item
    assert s._component_qty == 7

def test_create_other():
    s = OtherIngredient("other-1", 10, inv_item, 7)
    assert s._id == MenuItem._id
    assert s._price == 10
    assert s._name == "other-1"
    assert s._component == inv_item
    assert s._component_qty == 7

#def test_invalid_price():
#    with pytest.raises(InvalidFieldError):
#        s = OtherIngredient("other-1", -10, inv_item, 7)


