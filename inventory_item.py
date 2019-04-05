from abc import ABC

class inventoryItem(ABC):
    #
    def __init__(self, name, quantity, price, ivid):
        self._name = name
        self._quantity = quantity
        self._price = price
        self._ivid = ivid
        
    def calc_price(self, item_count):
        return item_count * self._price
        
    @property
    def name(self):
        return self._name
        
    @property
    def quantity(self):
        return self._quantity
            
    @property
    def price(self):
        return self._price
            
    @property
    def ivid(self):
        return self._ivid
        
    def __str__(self):
        return f'Item <{self.name}, {self.quantity}, {self.price}, {self.ivid}>'


