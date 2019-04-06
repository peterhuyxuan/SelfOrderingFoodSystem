from abc import ABC

class inventoryItem(ABC):
    _id = -1
    def __init__(self, name, quantity):
        self._name = name
        self._quantity = quantity
        inventoryItem._id += 1
        self._id = inventoryItem._id
        
    @property
    def name(self):
        return self._name
        
    @property
    def quantity(self):
        return self._quantity
            
    @quantity.setter
    def quantity(self,value):
         self._quantity = value

    @property
    def id(self):
        return self._id
        
    def __str__(self):
        return f'Item <{self.name}, {self.quantity}, {self.id}>'


