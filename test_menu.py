import pytest
from menu import Menu, ItemNotFound
from menu_item import MenuItem, InvalidFieldError
from main import Burger
from inventory_item import inventoryItem

inv_item = inventoryItem("test item", 100)

@pytest.fixture
def menu_fixture():
	MenuItem._reset_id_count()
	m = Menu()
	m.add_side("side", 10, inv_item , 1)
	m.add_drink("drink", 10, inv_item, 1)
	m.add_patty("patty", 10, inv_item, 1)
	m.add_other("other", 10, inv_item, 1)
	m.add_bun("bun", 10, inv_item, 1)

	return m


def test_empty_menu():
	m = Menu()
	assert len(m) == 2

def test_add_side():
	m = Menu()
	m.add_side("side-1", 10,inv_item, 1)
	assert len(m.sides) == 1
	assert m.sides[0].name == 'side-1'
	assert m.sides[0].price == 10
	assert m.sides[0].component is inv_item
	assert m.sides[0].component_qty == 1
	assert len(m) == 3

def test_add_drink():
	m = Menu()
	m.add_drink("drink-1", 10, inv_item, 1)
	assert len(m.drinks) == 1
	assert m.drinks[0].name == 'drink-1'
	assert m.drinks[0].price == 10
	assert m.drinks[0].component is inv_item
	assert m.drinks[0].component_qty == 1
	assert len(m) == 3


def test_add_patty():
	m = Menu()
	m.add_patty("patty-1", 10, inv_item, 1)
	assert m.patties[0].name == "patty-1"
	assert m.patties[0].price == 10
	assert m.patties[0].component is inv_item
	assert m.patties[0].component_qty == 1
	assert len(m.patties) == 1
	assert len(m) == 3

def test_add_other():
	m = Menu()
	m.add_other("other-1", 10, inv_item, 1)
	assert m.other_ingredients[0].name == 'other-1'
	assert m.other_ingredients[0].price == 10
	assert m.other_ingredients[0].component is inv_item
	assert m.other_ingredients[0].component_qty == 1
	assert len(m.other_ingredients) == 1
	assert len(m) == 3

def test_add_bun():
	m = Menu()
	m.add_bun("bun-1", 10, inv_item, 1)
	assert len(m.buns) == 1
	assert m.buns[0].name == 'bun-1'
	assert m.buns[0].price == 10
	assert m.buns[0].component is inv_item
	assert m.buns[0].component_qty == 1
	assert len(m) == 3

def test_add_multiple_same_cataory():
	m = Menu()
	m.add_patty("patty-1", 10, inv_item, 1)
	m.add_patty("patty-2", 10, inv_item, 1)
	assert m.patties[0].name == "patty-1"
	assert m.patties[0].price == 10
	assert m.patties[0].component is inv_item
	assert m.patties[0].component_qty == 1
	assert m.patties[1].name == "patty-2"
	assert m.patties[1].price == 10
	assert m.patties[1].component is inv_item
	assert m.patties[1].component_qty == 1
	assert len(m.patties) == 2
	assert len(m) == 4

def test_add_multiple_different_cataory():
	m = Menu()
	m.add_patty("patty-1", 10, inv_item, 1)
	m.add_drink("drink-1", 10, inv_item, 1)
	assert m.patties[0].name == "patty-1"
	assert m.patties[0].price == 10
	assert m.patties[0].component is inv_item
	assert m.patties[0].component_qty == 1

	assert m.drinks[0].name == 'drink-1'
	assert m.drinks[0].price == 10
	assert m.drinks[0].component is inv_item
	assert m.drinks[0].component_qty == 1
	assert len(m.patties) == 1
	assert len(m.drinks) == 1
	assert len(m) == 4

def test_invalid_item():
	m = Menu()
	with pytest.raises(InvalidFieldError) as e:
		"""
		failure cases should be covere by test_menu_item
		"""
		m.add_patty(None, -10, None, 1)
		assert len(e._messages) == 3
		assert e.__str__() == ("Please specify a valid item name\n"
								"Please specify a valid price\n"
								"Please specigy a valid quantity\n")
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
