import pytest
from main import Burger, Wrap, InvalidQuantityException
from menu_item import Bun, Patty, OtherIngredient

class InventoryObject:
    '''
    this is a class only for testing menu
    Should use InventoryItem for final integration test
    '''

    def __init__(self, name, item_id, qty):
        self.id = item_id
        self.name = name
        self.quantity = qty


inv_item = InventoryObject('test item', 1, 100)

patty1 = Patty("patty1", 10, inv_item, 1)
patty2 = Patty("patty2", 20, inv_item, 2)
bun1 = Bun("Bun1", 11, inv_item, 1)
bun2 = Bun("Bun2", 21, inv_item, 2)
other1 = OtherIngredient("other1", 12, inv_item, 1)
other2 = OtherIngredient("other2", 22 ,inv_item, 2)

@pytest.fixture
def test_burger():
    b = Burger()
    b.add_item(patty1, 1, inv_item.quantity)
    b.add_item(patty2, 1, inv_item.quantity)
    b.add_item(bun1, 2, inv_item.quantity)
    b.add_item(bun2, 1, inv_item.quantity)
    b.add_item(other1, 1, inv_item.quantity)

    return b

class TestUS1_2():
    def test_empty_burger(self):
        burger = Burger()
        assert len(burger.components) == 0
        assert burger.price == 0

    def test_add_one_bun_success(self):
        burger = Burger()
        burger.add_item(bun1, 1, inv_item.quantity)
        assert burger._num_buns == 1
        assert len(burger) == 1
        assert len(burger.components) == 1
        assert burger.price == 11
    
    def test_add_four_buns(self):
        burger = Burger()
        burger.add_item(bun1, 4, inv_item.quantity)
        assert burger._num_buns == 4
        assert len(burger) == 4
        assert len(burger.components) == 1
        assert burger.price == 44

    def test_add_different_buns(self):
        burger = Burger()
        burger.add_item(bun1, 1, inv_item.quantity)
        burger.add_item(bun2, 3, inv_item.quantity)
        assert burger._num_buns == 4
        assert len(burger) == 4
        assert len(burger.components) == 2
        assert burger.price == 74

    def test_add_five_buns(self):
        burger = Burger()
        with pytest.raises(InvalidQuantityException):
            burger.add_item(bun1, 5, inv_item.quantity)
        assert len(burger.components) == 0
        assert len(burger) == 0
        assert burger.price == 0

    def test_add_five_different_buns(self): 
        burger = Burger()
        burger.add_item(bun1, 2, inv_item.quantity)
        assert burger._num_buns == 2
        assert len(burger) == 2
        assert len(burger.components) == 1
        assert burger.price == 22
        with pytest.raises(InvalidQuantityException):
            burger.add_item(bun2, 3, inv_item.quantity)

    def test_add_zero_buns(self):
        burger = Burger()
        with pytest.raises(InvalidQuantityException):
            burger.add_item(bun1, 0, inv_item.quantity)

    def test_insufficient_buns(self):
        burger = Burger()
        with pytest.raises(InvalidQuantityException):
            burger.add_item(bun1, 101, inv_item.quantity)

    def test_add_existing_bun(self):
        burger = Burger()
        burger.add_item(bun1, 1, inv_item.quantity)
        with pytest.raises(ValueError):
            burger.add_item(bun1, 1, inv_item.quantity)

    def test_update_bun(self):
        burger = Burger()
        burger.add_item(bun1, 1, inv_item.quantity)
        burger.update_qty(bun1, 2, inv_item.quantity)
        assert burger.num_buns == 2
        assert burger.price == 22
        assert len(burger) == 2

    def test_update_bun_zero(self):
        burger = Burger()
        burger.add_item(bun1, 1, inv_item.quantity)
        with pytest.raises(InvalidQuantityException):
            burger.update_qty(bun1, 0, inv_item.quantity)
        assert burger.num_buns == 1
        assert burger.price == 11
        assert len(burger) == 1

    def test_update_one_of_two_bun(self):
        burger = Burger()
        burger.add_item(bun1, 1, inv_item.quantity)
        burger.add_item(bun2, 1, inv_item.quantity)
        burger.update_qty(bun2, 2, inv_item.quantity)
        assert burger.num_buns == 3
        assert burger.price == 53
        assert len(burger) == 3

    def test_update_one_of_two_bun_out_of_range(self):
        burger = Burger()
        burger.add_item(bun1, 1, inv_item.quantity)
        burger.add_item(bun2, 1, inv_item.quantity)
        with pytest.raises(InvalidQuantityException):
            burger.update_qty(bun2, 4, inv_item.quantity)
        assert burger.num_buns == 2
        assert burger.price == 32
        assert len(burger) == 2
    
    def test_update_bun_out_of_stock(self):
        burger = Burger()
        burger.add_item(bun1, 1, inv_item.quantity)
        with pytest.raises(InvalidQuantityException):
            burger.update_qty(bun1, 101, inv_item.quantity)
        assert burger.num_buns == 1
        assert len(burger) == 1
        assert burger.price == 11

    def test_update_invalid_bun(self):
        burger = Burger()
        burger.add_item(bun1, 1, inv_item.quantity)
        with pytest.raises(ValueError):
            burger.update_qty(bun2, 1, inv_item.quantity)
        assert burger.num_buns == 1
        assert len(burger) == 1
        assert burger.price == 11

    def test_update_to_one_bun(self):
        burger = Burger()
        burger.add_item(bun1, 2, inv_item.quantity)
        with pytest.raises(ValueError):
            burger.update_qty(bun1, 1, inv_item.quantity)
    
    def test_remove_bun(self, test_burger):
        test_burger.remove_item(bun2)
        assert test_burger.price == 85 - 21
        assert len(test_burger) == 5
        assert test_burger.num_buns == 2

    def test_remove_too_many_buns(self, test_burger):
        with pytest.raises(ValueError):
            test_burger.remove_item(bun1)

class TestUS1_3():
    def test_add_one_patty(self):
        burger = Burger()
        burger.add_item(bun1, 2, inv_item.quantity)
        burger.add_item(patty1, 1, inv_item.quantity)
        assert burger._num_patties == 1
        assert len(burger) == 3
        assert len(burger.components) == 2
        assert burger.price == 32

    def test_add_too_many_patties_in_one_go(self):
        burger = Burger()
        burger.add_item(bun1, 2, inv_item.quantity)
        with pytest.raises(InvalidQuantityException):
            burger.add_item(patty1, 7, inv_item.quantity)
        assert burger.num_patties == 0
        assert len(burger) == 2
        assert burger.price == 22

    def test_add_too_many_different_patties(self):
        burger = Burger()
        burger.add_item(bun1, 2, inv_item.quantity)
        burger.add_item(patty1, 2, inv_item.quantity)
        with pytest.raises(InvalidQuantityException):
            burger.add_item(patty2, 5, inv_item.quantity)
        assert burger.num_patties == 2
        assert len(burger) == 4
        assert burger.price == 42
    
    def test_add_different_patties(self):
        burger = Burger()
        burger.add_item(bun1, 3, inv_item.quantity)
        burger.add_item(patty1, 3, inv_item.quantity)
        assert burger.num_patties == 3
        assert len(burger) == 6
        assert burger.price == 63

    def test_add_zero_patty(self):
        burger = Burger()
        burger.add_item(bun1, 2, inv_item.quantity)
        with pytest.raises(InvalidQuantityException):
            burger.add_item(patty2, 0, inv_item.quantity)
        assert burger.num_patties == 0
        assert len(burger) == 2
        assert burger.price == 22

    def test_insufficient_patties(self):
        burger = Burger()
        with pytest.raises(InvalidQuantityException):
            burger.add_item(patty1, 101, inv_item.quantity)

    def test_add_existing_patty(self):
        burger = Burger()
        burger.add_item(patty1, 1, inv_item.quantity)
        with pytest.raises(ValueError):
            burger.add_item(patty1, 1, inv_item.quantity)

    def test_update_patty(self):
        burger = Burger()
        burger.add_item(patty1, 1, inv_item.quantity)
        burger.update_qty(patty1, 2, inv_item.quantity)
        assert burger.num_patties == 2
        assert burger.price == 20
        assert len(burger) == 2
    
    def test_update_patty_zero(self):
        burger = Burger()
        burger.add_item(patty1, 1, inv_item.quantity)
        with pytest.raises(InvalidQuantityException):
            burger.update_qty(patty1, 0, inv_item.quantity)
        assert burger.num_patties == 1
        assert burger.price == 10
        assert len(burger) == 1

    def test_update_one_of_two_patties(self):
        burger = Burger()
        burger.add_item(patty1, 1, inv_item.quantity)
        burger.add_item(patty2, 1, inv_item.quantity)
        burger.update_qty(patty2, 2, inv_item.quantity)
        assert burger.num_patties == 3
        assert burger.price == 50
        assert len(burger) == 3

    def test_update_one_of_two_patties_out_of_range(self):
        burger = Burger()
        burger.add_item(patty1, 1, inv_item.quantity)
        burger.add_item(patty2, 1, inv_item.quantity)
        with pytest.raises(InvalidQuantityException):
            burger.update_qty(patty2, 6, inv_item.quantity)
        assert burger.num_patties == 2
        assert burger.price == 30
        assert len(burger) == 2
    
    def test_update_patties_out_of_stock(self):
        burger = Burger()
        burger.add_item(patty1, 1, inv_item.quantity)
        with pytest.raises(InvalidQuantityException):
            burger.update_qty(patty1, 101, inv_item.quantity)
        assert burger.num_patties == 1
        assert len(burger) == 1
        assert burger.price == 10

    def test_update_invalid_patties(self):
        burger = Burger()
        burger.add_item(patty1, 1, inv_item.quantity)
        with pytest.raises(ValueError):
            burger.update_qty(patty2, 1, inv_item.quantity)
        assert burger.num_patties == 1
        assert len(burger) == 1
        assert burger.price == 10

    def test_remove_patty(self, test_burger):
        test_burger.remove_item(patty1)
        assert test_burger.price == 85 - 10
        assert len(test_burger) == 5
        assert test_burger.num_patties == 1
    
    def test_remove_too_many_patty(self, test_burger):
        test_burger.remove_item(patty1)
        with pytest.raises(ValueError):
            test_burger.remove_item(patty2)
# ===========================================================

class TestUS1_4():
    def test_add_one_other_success(self):
        burger = Burger()
        burger.add_item(other1, 1, inv_item.quantity)
        assert burger._num_others == 1
        assert len(burger) == 1
        assert len(burger.components) == 1
        assert burger.price == 12
    
    def test_add_five_other(self):
        burger = Burger()
        burger.add_item(other1, 5, inv_item.quantity)
        assert burger._num_others == 5
        assert len(burger) == 5
        assert len(burger.components) == 1
        assert burger.price == 60

    def test_add_different_others(self):
        burger = Burger()
        burger.add_item(other1, 2, inv_item.quantity)
        burger.add_item(other2, 3, inv_item.quantity)
        assert burger._num_others == 5
        assert len(burger) == 5
        assert len(burger.components) == 2
        assert burger.price == 90

    def test_add_six_others(self):
        burger = Burger()
        with pytest.raises(InvalidQuantityException):
            burger.add_item(bun1, 6, inv_item.quantity)
        assert len(burger.components) == 0
        assert len(burger) == 0
        assert burger.price == 0

    def test_add_six_different_buns(self): 
        burger = Burger()
        burger.add_item(other1, 3, inv_item.quantity)
        with pytest.raises(InvalidQuantityException):
            burger.add_item(other2, 3, inv_item.quantity)

        assert burger._num_others == 3
        assert len(burger) == 3
        assert len(burger.components) == 1
        assert burger.price == 36
    
    def test_add_zero_others(self):
        burger = Burger()
        with pytest.raises(InvalidQuantityException):
            burger.add_item(bun1, 0, inv_item.quantity)


    def test_insufficient_others(self):
        burger = Burger()
        with pytest.raises(InvalidQuantityException):
            burger.add_item(other1, 101, inv_item.quantity)
    
    def test_add_existing_others(self):
        burger = Burger()
        burger.add_item(bun1, 1, inv_item.quantity)
        with pytest.raises(ValueError):
            burger.add_item(bun1, 1, inv_item.quantity)

    def test_update_other(self):
        burger = Burger()
        burger.add_item(other1, 1, inv_item.quantity)
        burger.update_qty(other1, 2, inv_item.quantity)
        assert burger.num_others == 2
        assert burger.price == 24
        assert len(burger) == 2
    
    def test_update_other_zero(self):
        burger = Burger()
        burger.add_item(other1, 1, inv_item.quantity)
        with pytest.raises(InvalidQuantityException):
            burger.update_qty(other1, 0, inv_item.quantity)
        assert burger.num_others == 1
        assert burger.price == 12
        assert len(burger) == 1

    def test_update_one_of_two_other(self):
        burger = Burger()
        burger.add_item(other1, 1, inv_item.quantity)
        burger.add_item(other2, 1, inv_item.quantity)
        burger.update_qty(other2, 2, inv_item.quantity)
        assert burger.num_others == 3
        assert burger.price == 56
        assert len(burger) == 3
    
    def test_update_one_of_two_other_exceeds_limit(self):
        burger = Burger()
        burger.add_item(other1, 1, inv_item.quantity)
        burger.add_item(other2, 1, inv_item.quantity)
        with pytest.raises(InvalidQuantityException):
            burger.update_qty(other2, 5, inv_item.quantity)
        assert burger.num_others == 2
        assert burger.price == 34
        assert len(burger) == 2
    
    def test_update_other_out_of_stock(self):
        burger = Burger()
        burger.add_item(other1, 1, inv_item.quantity)
        with pytest.raises(InvalidQuantityException):
            burger.update_qty(other1, 101, inv_item.quantity)
        assert burger.num_others == 1
        assert len(burger) == 1
        assert burger.price == 12

    def test_update_invalid_others(self):
        burger = Burger()
        burger.add_item(other1, 1, inv_item.quantity)
        with pytest.raises(ValueError):
            burger.update_qty(other2, 1, inv_item.quantity)
        assert burger.num_others == 1
        assert len(burger) == 1

    def test_remove_other(self, test_burger):
        test_burger.remove_item(other1)
        assert test_burger.num_others == 0
        assert len(test_burger) == 5
        assert test_burger.price == 85 - 12 
    # ==================================================

def test_remove_invalid_item(test_burger):
    with pytest.raises(ValueError):
        test_burger.remove_item(other2)
