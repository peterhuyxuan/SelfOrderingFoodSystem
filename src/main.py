from abc import ABC, abstractmethod,abstractproperty
from src.menu_item import Patty, OtherIngredient, Bun, MenuItem

class Main(ABC):
    _id = 0
    def __init__(self, name):
        self._name = name
        self._id = Main._id
        Main._id += 1
        self._components = {}
        self._num_buns = 0
        self._num_patties = 0
        self._num_others = 0
        self._price = 0

    def add_item(self, item, qty):
        '''
        add items to main based on the types of item
        if item is already in the components
        an exception will be raised
        '''
        if item.name in self._components.keys():
            raise ValueError(f"item({item}) is already in the components")

        if isinstance(item, Bun):
            self._valid_bun_qty(item, qty, qty + self._num_buns)
            self._num_buns += qty
        elif isinstance(item, Patty):
            self._valid_patty_qty(item, qty, qty + self._num_patties)
            self._num_patties += qty
        elif isinstance(item, OtherIngredient):
            self._valid_other_qty(item, qty, qty + self._num_others)
            self._num_others += qty
        else:
            raise TypeError(f"{item.__class__.__name__} is not a valid ingredient")
        
        self._components[item.name] = qty
        self._price += qty * item.price

    def update_qty(self, item, qty):
        '''
        change an item's quantity to a new quantity 
        if item is not in the components
        an exception will be raised
        '''

        if item.name not in self._components.keys():
            raise ValueError(f"item({item}) is not in the components")
        
        if isinstance(item, Bun):
            new_qty = qty - self._components[item.name] + self._num_buns
            self._valid_bun_qty(item, qty, new_qty)
            self._num_buns = new_qty
            self.check_min_buns()
        elif isinstance(item, Patty):
            new_qty = qty - self._components[item.name] + self._num_patties
            self._valid_patty_qty(item, qty, new_qty)
            self._num_patties = new_qty
            self.check_min_patties()
        elif isinstance(item, OtherIngredient):
            new_qty = qty - self._components[item.name] + self._num_others
            self._valid_other_qty(item, qty, new_qty)
            self._num_others = new_qty
        else:
            raise TypeError(f"{item.__class__.__name__} is not a valid ingredient")
        
        self._price += (qty - self._components[item.name]) * item.price
        self._components[item.name] = qty   
        
    def remove_item(self, item):
        if item.name in self._components.keys():
            qty = self._components.pop(item.name)
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

    def _valid_bun_qty(self, item, qty, total):
        '''
        qty should be at least 1 in order to add or update
        total: total number of buns should not be greater than the maximal allowance
        '''
        if qty < 1:
            raise InvalidQuantityException("buns",qty, "less than 1")
            
        if qty > item.component.quantity:
            raise InvalidQuantityException("buns", qty, "Insufficient stock")

        if  total > self._max_bun():
            raise InvalidQuantityException("buns",qty, "Greater than maximal allowance")
            
    def show_content(self, menu):
        print("Name\t\tQuantity\tPrice")
        for item, qty in self._components.items():
            menu_item = menu.get_item(item)
            print(f"{item}\t\t{qty}\t\t${menu_item.price} * {qty}")
        print(f"Total: ${self.price}")

    def _valid_patty_qty(self, item, qty, total):
        '''
        qty should be at least 1 in order to add or update
        total: total number of patties should not be greater than the maximal allowance
        '''
        if qty < 1:
            raise InvalidQuantityException("patty",qty, "less than 1")
            
        if qty > item.component.quantity:
            raise InvalidQuantityException("patty", qty, "Insufficient stock")

        if  total > self._max_patties():
            raise InvalidQuantityException("patty",qty, "Greater than maximal allowance")

    def _valid_other_qty(self, item, qty, total):
        '''
        qty should >= 1 and <= tock levrl in order to add or update
        total: total number of otheer should not be greater than the maximal allowance
        '''
        if qty < 1:
            raise InvalidQuantityException("other",qty, "less than 1")
            
        if qty > item.component.quantity:
            raise InvalidQuantityException("other", qty, "Insufficient stock")

        if  total > self._max_others():
            raise InvalidQuantityException("other",qty, "Greater than maximal allowance")

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

    @property
    def id(self):
        return self._id
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
        return 3
 
    def __str__(self):
        return "Wrap " + super().__str__()

    def check_min_buns(self):
        if self._num_buns != 1:
            raise ValueError("You can only have one bun")

    def check_min_patties(self):
        if self._num_patties < 1:
            raise ValueError("you need to have at least 1 patty")


class InvalidQuantityException(Exception):
    def __init__(self, field_name, quantity, reason):
        self._field_name = field_name
        self._quantity = quantity
        self._reason = reason

    def __str__(self):
        return (f'Invaild {self._field_name} (qty: {self._quantity}): {self._reason}')
