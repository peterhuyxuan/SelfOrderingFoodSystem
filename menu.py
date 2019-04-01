from menu_item import Bun, Patty, OtherIngredient, Side, Drink
from main import Main


class Menu():
 
    def __init__(self, items = None):
        self._main = ("Burger", "Wrap")
        self._buns = []
        self._patties = []
        self._other_ingredients = []
        self._sides = []
        self._drinks = []
        self._catagories = ('_buns', '_patties', 
                                '_other_ingredients',
                                '_sides', '_drinks')
        
        if items is not None and len(items) != 0:
            for item in items:
                self.add_item(item)

    def add_patty(self, name, price, component, qty):
        errs = self._check_field(name, price, component, qty)
        try:
            if len(errs) > 0:
                raise InvalidField(''.join(errors))
        except InvalidField as e:
            print(e)
            print("Nothing is added")
        else:
            item = Patty(name, price, component, qty)
            self._patties.append(item)

    def add_bun(self, name, price, component, qty):
        errs = self._check_field(name, price, component, qty)
        try:
            if len(errs) > 0:
                raise InvalidField(''.join(errors))
        except InvalidField as e:
            print(e)
            print("Nothing is added")
        else:
            item = Bun(name, price, component, qty)
            self._buns.append(item)

    def add_side(self, name, price, component, qty):
        errs = self._check_field(name, price, component, qty)
        try:
            if len(errs) > 0:
                raise InvalidField(''.join(errors))
        except InvalidField as e:
            print(e)
            print("Nothing is added")
        else:
            item = Side(name, price, component, qty)
            self._buns.append(item)

    def add_drink(self, name, price, component, qty):
        errs = self._check_field(name, price, component, qty)
        try:
            if len(errs) > 0:
                raise InvalidField(''.join(errors))
        except InvalidField as e:
            print(e)
            print("Nothing is added")
        else:
            item = Drink(name, price, component, qty)
            self._drinks.append(item)

    def add_other(self, name, price, component, qty):
        errs = self._check_field(name, price, component, qty)
        try:
            if len(errs) > 0:
                raise InvalidField(''.join(errors))
        except InvalidField as e:
            print(e)
            print("Nothing is added")
        else:
            item = OtherIngredient(name, price, component, qty)
            self._other_ingredients.append(item)


    def _check_field(name, price, component, qty):
        error_messages = []
        if (name is None or len(name) == 0 or str.isspace(name)):
            error_messages.append("Please specify item name\n")
        
        if price <= 0:
            error_messages.append("Please specify a valid price\n")
        
        if component is None or not isinstance(component, InventoryItem):
            error_messages.append("Please specify a valid component\n")

        if qty <= 0:
            error_messages.append("Please specigy a valid price\n")
        
        return error_messages          
        
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

    def get_item(self, item_id):
        for catagory in self._catagories:
            current_catagory = getattr(self, catagory)
            for item in current_catagory:
                if item.id == item_id:
                    return item
            
        return None

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


class InvalidField(Exception):
    def __init__(self, message):
        self._message = message

    def __str__(self):
        return self._message