import pytest
from menu import Menu, ItemNotFound
from menu_item import Side, Drink, Patty, OtherIngredient, Bun, MenuItem
from main import Burger

class InventoryObject:
    '''
    this is a class only for testing menu
    Should use InventoryItem for final integration test
    '''

    def __init__(self, name, item_id):
        self.id = item_id
        self.name = name

@pytest.fixture
def menu_fixture():
    MenuItem._reset_id_count()
    m = Menu()
    inv_item = InventoryObject("test item", 0)
    item1 = Side("side", 10, inv_item , 1)
    item2 = Drink("drink", 10, inv_item, 1)
    item3 = Patty("patty", 10, inv_item, 1)
    item4 = OtherIngredient("other", 10, inv_item, 1)
    item5 = Bun("bun", 10, inv_item, 1)

    m.add_item(item1)
    m.add_item(item2)
    m.add_item(item3)
    m.add_item(item4)
    m.add_item(item5)

    return m


def test_empty_menu():
    m = Menu()
    assert len(m) == 2

def test_add_side():
    m = Menu()
    inv_item = InventoryObject("test item", 0)
    sample = Side("side-1", 10,inv_item, 1)
    m.add_item(sample)
    assert m.sides[0] is sample
    assert len(m.sides) == 1
    assert len(m) == 3
    assert m._sides is m.sides
    
def test_add_drink():
    m = Menu()
    inv_item = InventoryObject("test item", 0)
    sample = Drink("drink-1", 10, inv_item, 1)
    m.add_item(sample)
    assert m.drinks is m._drinks
    assert m.drinks[0] is sample
    assert len(m.drinks) == 1
    assert len(m) == 3
    
def test_add_patty():
    m = Menu()
    inv_item = InventoryObject("test item", 0)
    sample = Patty("patty-1", 10, inv_item, 1)
    m.add_item(sample)
    assert m.patties is m._patties
    assert m.patties[0] is sample
    assert len(m.patties) == 1
    assert len(m) == 3

def test_add_other():
    m = Menu()
    inv_item = InventoryObject("test item", 0)
    sample = OtherIngredient("other-1", 10, inv_item, 1)
    m.add_item(sample)
    assert m.other_ingredients is m._other_ingredients
    assert m.other_ingredients[0] is sample
    assert len(m.other_ingredients) == 1
    assert len(m) == 3

def test_add_bun():
    m = Menu()
    inv_item = InventoryObject("test item", 0)
    sample = Bun("patty-1", 10, inv_item, 1)
    m.add_item(sample)
    assert m.buns is m._buns
    assert m.buns[0] is sample
    assert len(m.buns) == 1
    assert len(m) == 3

def test_add_multiple_same_cataory():
    m = Menu()
    inv_item = InventoryObject("test item", 0)
    sample = Bun("patty-1", 10, inv_item, 1)
    sample1 = Bun("patty-2", 10, inv_item, 1)
    m.add_item(sample)
    m.add_item(sample1)
    assert m.buns[0] is sample
    assert m.buns[1] is sample1
    assert len(m.buns) == 2
    assert len(m) == 4

def test_add_multiple_different_cataory():
    m = Menu()
    inv_item = InventoryObject("test item", 0)
    sample = Bun("patty-1", 10, inv_item, 1)
    sample1 = Drink("drink-1", 10, inv_item, 1)
    m.add_item(sample)
    m.add_item(sample1)
    assert m.buns[0] is sample
    assert m.drinks[0] is sample1
    assert len(m.buns) == 1
    assert len(m.drinks) == 1
    assert len(m) == 4

def test_invalid_item():
    m = Menu()
    with pytest.raises(TypeError):
        m.add_item(1)
    assert len(m) == 2

def test_remove_side(menu_fixture):
   menu_fixture.remove_item(0)
   assert len(menu_fixture.sides) == 0
   assert len(menu_fixture) == 6

def test_remove_drink(menu_fixture):
   menu_fixture.remove_item(1)
   assert len(menu_fixture.drinks) == 0
   assert len(menu_fixture) == 6

def test_remove_patty(menu_fixture):
   menu_fixture.remove_item(2)
   assert len(menu_fixture.patties) == 0
   assert len(menu_fixture) == 6

def test_remove_other(menu_fixture):
   menu_fixture.remove_item(3)
   assert len(menu_fixture.other_ingredients) == 0
   assert len(menu_fixture) == 6

def test_remove_bun(menu_fixture):
   menu_fixture.remove_item(4)
   assert len(menu_fixture.buns) == 0
   assert len(menu_fixture) == 6

def test_invalid_remove(menu_fixture):
    with pytest.raises(ItemNotFound): 
        menu_fixture.remove_item(6)
    