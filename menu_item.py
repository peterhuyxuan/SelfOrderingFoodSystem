from abc import ABC, abstractmethod

class MenuItem(ABC):
    _id = -1
    def __init__(self, name, price, component, qty):
        if qty < 1 or price <= 0:
            raise ValueError(f"invalid price({price}) or/and qty({qty})")
        self._name = name
        self._price = price
        self._component = component
        self._component_qty = qty
        MenuItem._id += 1
        self._id = MenuItem._id

    @abstractmethod
    def __str__(self):
        return (f"<name: {self._name},id: {self._id}, price:{self._price} "
                f"component= ({self._component_qty} x {self._component.name})>")

    #Properties
    @property
    def price(self):
        return self._price
    
    @property
    def name(self):
        return self._name
    
    @property
    def id(self):
        return self._id
    
    @classmethod
    def _reset_id_count(cls):
        cls._id = -1
    
class Bun(MenuItem):
    def __init__(self, name, price, component, qty):
        super().__init__(name, price, component, qty)

    def __str__(self):
        return "Bun " + super().__str__()


class Patty(MenuItem):
    def __init__(self, name, price, component, qty):
        super().__init__(name, price, component, qty)

    def __str__(self):
        return "Patty " + super().__str__()


class OtherIngredient(MenuItem):
    def __init__(self, name, price, component, qty):
        super().__init__(name, price, component, qty)

    def __str__(self):
        return "Other Ingreident " + super().__str__()


class Drink(MenuItem):
    def __init__(self, name, price, component, qty):
        super().__init__(name, price, component, qty)

    def __str__(self):
        return "Drink " + super().__str__()


class Side(MenuItem):
    def __init__(self, name, price, component, qty):
        super().__init__(name, price, component, qty)

    def __str__(self):
        return "Side " + super().__str__()
