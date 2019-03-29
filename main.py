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
            if not self._valid_bun_qty(item, 
                                        qty,
                                        qty + self._num_buns, 
                                        inventory_level):
                raise InvalidQuantityException("Buns", qty)
            self._num_buns += qty
        elif isinstance(item, Patty):
            if not self._valid_patty_qty(item,
                                            qty, 
                                            qty + self._num_patties, 
                                            inventory_level):
                raise InvalidQuantityException("Patties", qty)
            self._num_patties += qty
        elif isinstance(item, OtherIngredient):
            if not self._valid_other_qty(item, 
                                            qty,
                                            qty + self._num_others, 
                                            inventory_level):
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

        TODO: EXTRA CHECK MUST BE DONE
        '''
        if item.id not in self._components.keys():
            raise ValueError(f"item({item}) is not in the components")
        
        if isinstance(item, Bun):
            new_qty = qty - self._components[item.id] + self._num_buns
            if not self._valid_bun_qty(item, qty,
                                        new_qty, inventory_level):
                raise InvalidQuantityException("Buns", qty)
            self._num_buns = new_qty
            self.check_min_buns()
        elif isinstance(item, Patty):
            new_qty = qty - self._components[item.id] + self._num_patties
            if not self._valid_patty_qty(item, qty, 
                                        new_qty, inventory_level):
                raise InvalidQuantityException("Patties", qty)
            self._num_patties = new_qty
            self.check_min_patties()
        elif isinstance(item, OtherIngredient):
            new_qty = qty - self._components[item.id] + self._num_others
            if not self._valid_other_qty(item, qty,
                                        new_qty,inventory_level):
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
            if isinstance(item, Bun):
                self._num_buns -= qty
                self.check_min_buns()
            elif isinstance(item, Patty):
                self._num_patties -= qty
                self.check_min_patties()
            elif isinstance(item, OtherIngredient):
                self._num_others -= qty
        else:
            raise ValueError(f"{item} not found in components")

    def _valid_bun_qty(self, item, qty, total, inventory_level):
        if qty < 1 or total > self._max_bun() or qty > inventory_level:
            return False
        return True

    def _valid_patty_qty(self, item, qty, total, inventory_level):
        if (qty < 1 or total > self._max_patties() 
            or qty > inventory_level):
            return False
        return True

    def _valid_other_qty(self, item, qty, total, inventory_level):
        if qty < 1 or total > self._max_others() or qty > inventory_level:
            return False
        return True

    @abstractmethod
    def __str__(self):
        return (f"<Name:{self._name}, Buns: {self._num_buns}, "
                f"Patties: {self._num_patties}>, Others = {self._num_others}")

    def __len__(self):
        res = 0
        for value in self._components.values():
            res += value
        return res 

    # properties
    @property
    def components(self):
        return self._components
    
    @property
    def num_patties(self):
        return self._num_patties

    @property
    def num_buns(self):
        return self._num_buns

    @property
    def num_others(self):
        return self._num_others

    @property
    def name(self): 
        return self._name

    @property
    def price(self):
        return self._price

    @abstractmethod
    def _max_bun(self):
        pass

    @abstractmethod
    def _max_patties(self):
        pass
    
    @abstractmethod
    def _max_others(self):
        pass
    
    @abstractmethod
    def check_min_buns(self):
        pass
    
    @abstractmethod
    def check_min_patties(self):
        pass


class Burger(Main):
    def __init__(self):
        super().__init__("Burger")

    def _max_bun(self):
        return 4

    def _max_patties(self):
        return 6
    
    def _max_others(self):
        return 5

    def check_min_buns(self):
        if self._num_buns < 2:
            raise ValueError("you need to have at least 2 bun")

    def check_min_patties(self):
        if self._num_patties < 1:
            raise ValueError("you need to have at least 1 patty")
            
    def __str__(self):
        return "Burger " + super().__str__()


class Wrap(Main):
    def __init__(self):
        super().__init__("Wrap")

    def _max_bun(self):
        return 1

    def _max_patties(self):
        return 2
    
    def _max_others(self):
        return 5
 
    def __str__(self):
        return "Wrap " + super().__str__()

    def check_min_buns(self):
        if self._num_buns != 1:
            raise ValueError("You can only have one bun")

    def check_min_patties(self):
        if self._num_patties < 1:
            raise ValueError("you need to have at least 1 patty")


class InvalidQuantityException(Exception):
    def __init__(self, field_name, quantity):
        self._field_name = field_name
        self._quantity = quantity

    def __str__(self):
        return (f'Invaild number for {self._field_name} (quantity = {self._quantity})')
