import pytest
from menu import Menu, ItemNotFound
from menu_item import Side, Drink, Patty, OtherIngredient, Bun, MenuItem


class InventoryObject:
    '''
    this is a class only for testing menu
    Should use InventoryItem for final integration test
    '''

    def __init__(self, name, item_id):
        self.id = item_id
        self.name = name


def test_create_side():
    inv_item = InventoryObject("test item", 0)
    s = Side("side-1", 10,inv_item, 1)
    assert s._id == MenuItem._id
    assert s._price == 10
    assert s._name == "side-1"
    assert s._component == inv_item
    assert s._component_qty == 1

def test_create_drink():
    inv_item = InventoryObject("test item", 1)
    s = Drink("drink-1", 10,inv_item, 1)
    assert s._id == MenuItem._id
    assert s._price == 10
    assert s._name == "drink-1"
    assert s._component == inv_item
    assert s._component_qty == 1

def test_create_patty():
    inv_item = InventoryObject("test item", 1)
    s = Patty("patty-1", 10,inv_item, 3)
    assert s._id == MenuItem._id
    assert s._price == 10
    assert s._name == "patty-1"
    assert s._component == inv_item
    assert s._component_qty == 3

def test_create_bun():
    inv_item = InventoryObject("test item", 1)
    s = Bun("bun-1", 10, inv_item, 7)
    assert s._id == MenuItem._id
    assert s._price == 10
    assert s._name == "bun-1"
    assert s._component == inv_item
    assert s._component_qty == 7

def test_create_other():
    inv_item = InventoryObject("test item", 1)
    s = OtherIngredient("other-1", 10, inv_item, 7)
    assert s._id == MenuItem._id
    assert s._price == 10
    assert s._name == "other-1"
    assert s._component == inv_item
    assert s._component_qty == 7

def test_invalid_price():
    inv_item = InventoryObject("test item", 1)
    with pytest.raises(ValueError):
        s = OtherIngredient("other-1", -10, inv_item, 7)

