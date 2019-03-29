from abc import ABC, abstractmethod,abstractproperty
from menu_item import Patty, OtherIngredient, Bun, MenuItem

class Main(ABC):

    def __init__(self, name):
        self._name = name
        self._components = {}
        self._num_buns = 0
        self._num_patties = 0
        self._num_others = 0
        self._price = 0

    def add_item(self, item, qty, inventory_level):
        '''
        add items to main based on the types of item
        if item is already in the components
        an exception will be raised
        '''
        if item.id in self._components.keys():
            raise ValueError(f"item({item}) is already in the components")

        if isinstance(item, Bun):
            if not self._valid_bun_qty(qty + self._num_buns, inventory_level):
                raise InvalidQuantityException("Buns", qty)
            self._num_buns += qty
        elif isinstance(item, Patty):
            if not self._valid_patty_qty(qty + self._num_patties, inventory_level):
                raise InvalidQuantityException("Patties", qty)
            self._num_patties += qty
        elif isinstance(item, OtherIngredient):
            if not self._valid_other_qty(qty + self._num_others, inventory_level):
                raise InvalidQuantityException("Other ingredient", qty)
            self._num_others += qty
        else:
            raise TypeError(f"{item.__class__.__name__} is not a valid ingredient")
        
        self._components[item.id] = qty
        self._price += qty * item.price

    def update_qty(self, item, qty, inventory_level):
        '''
        change an item's quantity to a new quantity 
        if item is not in the components
        an exception will be raised
        '''
        if item.id not in self._components.keys():
            raise ValueError(f"item({item}) is not in the components")
        
        if isinstance(item, Bun):
            new_qty = qty - self._components[item.id] + self._num_buns
            if not self._valid_bun_qty(qty + new_qty, inventory_level):
                raise InvalidQuantityException("Buns", qty)
            self._num_buns = new_qty
        elif isinstance(item, Patty):
            new_qty = qty - self._components[item.id] + self._num_patties
            if not self._valid_patty_qty(qty + new_qty, inventory_level):
                raise InvalidQuantityException("Patties", qty)
            self._num_patties = new_qty
        elif isinstance(item, OtherIngredient):
            new_qty = qty - self._components[item.id] + self._num_others
            if not self._valid_other_qty(qty + self._num_others, inventory_level):
                raise InvalidQuantityException("Other ingredient", qty)
            self._num_others = new_qty
        else:
            raise TypeError(f"{item.__class__.__name__} is not a valid ingredient")
        
        self._price += (qty - self._components[item.id]) * item.price
        self._components[item.id] = qty
        


    def remove_item(self, item):
        if item.id in self._components.keys():
            qty = self._components.pop(item.id)
            self._price  -= item.price * qty
        else:
            raise ValueError(f"{item.id} not found in components")


    @abstractmethod
    def _valid_bun_qty(self, qty, intentory_level):
        pass

    @abstractmethod 
    def _valid_patty_qty(self, qty, inventory_level):
        pass

    @abstractmethod
    def _valid_other_qty(self, qty, inventory_level):
        pass

    @abstractmethod
    def __str__(self):
        return (f"<Name:{self._name}, Buns: {self._num_buns}, "
                f"Patties: {self._num_patties}>, Others = {self._num_others}")

    # properties
    @property
    def components(self):
        return self._components
    
    @property
    def name(self): 
        return self._name

    @property
    def price(self):
        return self._price



class Burger(Main):
    def __init__(self):
        super().__init__("Burger")
    
    def _valid_bun_qty(self, qty, inventory_level):
        if qty < 1 or qty > 4 or qty > inventory_level:
            return False
        return True

    def _valid_patty_qty(self, qty, inventory_level):
        if qty < 1 or qty > 2 * self._num_buns - 1 or qty > inventory_level:
            return False
        return True

    def _valid_other_qty(self, qty, inventory_level):
        if qty < 1 or qty > 5 or qty > inventory_level:
            return False
        return True

    def __str__(self):
        return "Burger " + super().__str__()


class Wrap(Main):
    def __init__(self):
        super().__init__("Wrap")

    def _valid_bun_qty(self, qty, inventory_level):
        if qty != 1 or qty > inventory_level:
            return False
        return True

    def _valid_patty_qty(self, qty ,inventory_level):
        if qty < 1 or qty > 2 or qty > inventory_level:
            return False
        return True

    def _valid_other_qty(self, qty, inventory_level):
        if qty < 1 or qty > 5 or qty > inventory_level:
            return False
        return True
 
    def __str__(self):
        return "Wrap " + super().__str__()


class InvalidQuantityException(Exception):
    def __init__(self, field_name, quantity):
        self._field_name = field_name
        self._quantity = quantity

    def __str__(self):
        return (f'Invaild number for {self._field_name} (quantity = {self._quantity})')
