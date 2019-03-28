from menu_item import Bun, Patty, OtherIngredient, Side, Drink
class Menu():
 
    def __init__(self, items = None):
        self._main = []
        self._buns = []
        self._patties = []
        self._other_ingredients = []
        self._sides = []
        self._drinks = []
        self._catagories = ('_main', '_buns', '_patties', 
                                '_other_ingredients',
                                '_sides', '_drinks')
        
        if items is not None and len(items) != 0:
            for item in items:
                self.add_item(item)

    def add_item(self, item):
        if isinstance(item, Main):
            self._main.append(item)
        elif isinstance(item, Bun):
            self._buns.append(item)
        elif isinstance(item, Patty):
            self._patties.append(item)
        elif isinstance(item, OtherIngredient):
            self._other_ingredients.append(item)
        elif isinstance(item, Side):
            self._sides.append(item)
        elif isinstance(item, Drink):
            self._drinks.append(item)
        else: 
            raise TypeError(f"You could not add {item.__class__} into menu as"
                        " it's not <MenuItem>")

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
            try:
                raise ItemNotFound(item_id)
            except ItemNotFound as e:
                print(e)
            
            
        
    def __len__(self):
        res = 0
        for catagory in self._catagories:
            res += len(getattr(self, catagory))
        return res

    def show(self):
        for catagory in self._catagories: 
            for item in getattr(self,catagory):
                print(item)
            


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
        return self._sides


class ItemNotFound(Exception):
    def __init__(self, item_id):
        self._item_id = item_id

    def __str__(self):
        return f"item ({self._item_id}) is not found in the menu"