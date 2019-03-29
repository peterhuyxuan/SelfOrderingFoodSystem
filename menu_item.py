from abc import ABC, abstractmethod

class MenuItem(ABC):
    _id = -1
    def __init__(self, name, price, components : list):
        self._name = name
        self._price = price
        self._components = {}
        MenuItem._id += 1
        self._id = MenuItem._id
        for item, quantity in components:
            self._components[item.id] = quantity

    @abstractmethod
    def __str__(self):
        return f"<name: {self._name},id: {self._id}, price:{self._price}>"
    
    def show_components(self):
        for key, value in self._components:
            print(f"Corresponding Inventory Item :(id = {key}) Quantity = {value}")

    #Properties
    @property
    def price(self):
        return self.price
    
    @property
    def name(self):
        return self._name
    
    @property
    def id(self):
        return self._id
    
    
class Bun(MenuItem):
    def __init__(self, name, price, components):
        super().__init__(name, price, components)

    def __str__(self):
        return "Bun " + super.__str__()


class Patty(MenuItem):
    def __init__(self, name, price, components):
        super().__init__(name, price, components)

    def __str__(self):
        return "Patty " + super.__str__()


class OtherIngredient(MenuItem):
    def __init__(self, name, price, components):
        super().__init__(name, price, components)

    def __str__(self):
        return "Other Ingreident " + super.__str__()


class Drink(MenuItem):
    def __init__(self, name, price, components):
        super().__init__(name, price, components)

    def __str__(self):
        return "Drink " + super.__str__()


class Side(MenuItem):
    def __init__(self, name, price, components):
        super().__init__(name, price, components)

    def __str__(self):
        return "Side " + super.__str__()        

