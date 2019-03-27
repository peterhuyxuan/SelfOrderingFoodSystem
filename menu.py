from abc import ABC, abstractmethod
from enum import Enum

class Menu():
 
    def __init__(self, items = None):
        self._main = []
        self._buns = []
        self._patties = []
        self._other_main_ingredients = []
        self._sides = []
        self._drinks = []
        
        if len(items) != 0:
            for item in items:
                self.add_item(item)

    def add_item(self, item):

        if isinstance(item, Main):
            self._main.append(item)
        elif isinstance(item, Bun) :
            self._buns.append(item)
        elif isinstance(item, Patty):
            self._patties.append(item)
        elif isinstance(item, OtherMainIngredidents)
            self._other_main_ingredients.append(item)
        elif isinstance(item, Side):
            self._sides.append(item)
        elif isinstance(item, Drink):
            self._drinks.append(item)
        else: 
            raise TypeError(f"You could not add {item.__class__} into menu as"
                        " it's not <MenuItem>")
        




    
        
    
       