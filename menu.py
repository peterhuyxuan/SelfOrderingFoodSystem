from menu_item import Bun, Patty, OtherIngredient, Side, Drink
from main import Main

class Menu():
 
    def __init__(self):
        self._main = ("Burger", "Wrap")
        self._buns = []
        self._patties = []
        self._other_ingredients = []
        self._sides = []
        self._drinks = []
        self._catagories = ('_buns', '_patties', 
                                '_other_ingredients',
                                '_sides', '_drinks')
        
    def add_patty(self, name, price, component, qty):
        self._check_name_exists(name)
        item = Patty(name, price, component, qty)
        self._patties.append(item)

    def add_bun(self, name, price, component, qty):
        self._check_name_exists(name)
        item = Bun(name, price, component, qty)
        self._buns.append(item)

    def add_side(self, name, price, component, qty):
        self._check_name_exists(name)
        item = Side(name, price, component, qty)
        self._sides.append(item)

    def add_drink(self, name, price, component, qty):
        self._check_name_exists(name)
        item = Drink(name, price, component, qty)
        self._drinks.append(item)

    def add_other(self, name, price, component, qty):
        self._check_name_exists(name)
        item = OtherIngredient(name, price, component, qty)
        self._other_ingredients.append(item)
        
    def remove_item(self, item_id : int):
        """
        remove the item with item_id from the menu
        if item is not in menu 
        """
        removal_flag = False
        for catagory in self._catagories:
            current_catagory = getattr(self, catagory)
            for item in current_catagory:
                if item.id == item_id:
                    current_catagory.remove(item)
                    removal_flag = True
                    break

            if removal_flag == True:
                break

        # prompt user if item is not found in the menue
        if removal_flag == False:
            raise ItemNotFound(item_id)

        
    def __len__(self):
        res = 0
        for catagory in self._catagories:
            res += len(getattr(self, catagory))
        return res + 2 

    def show(self):
        for catagory in self._catagories: 
            print(catagory)
            for item in getattr(self,catagory):
                print(item)

    def get_item(self, item_name):
        for catagory in self._catagories:
            current_catagory = getattr(self, catagory)
            for item in current_catagory:
                if item.name == item_name:
                    return item
            
        return None
    
    def _check_name_exists(self, name):
        for catagory in self._catagories:
            current_catagory = getattr(self, catagory)
            for item in current_catagory:
                if name == item.name:
                    raise AddingError



    # Properties
    @property
    def main(self):
        return self._main
    
    @property
    def buns(self):
        return self._buns

    @property
    def patties(self):
        return self._patties

    @property
    def other_ingredients(self):
        return self._other_ingredients

    @property
    def sides(self):
        return self._sides

    @property
    def drinks(self):
        return self._drinks

class ItemNotFound(Exception):
    def __init__(self, item_id):
        self._item_id = item_id

    def __str__(self):
        return f"item ({self._item_id}) is not found in the menu"


class AddingError(Exception):
    def __init__(self, name, reason):
        self._name = name
        self._reason = reason

    def __str__(self):
        return (f"adding {self._name} failed: {self._reason}")
