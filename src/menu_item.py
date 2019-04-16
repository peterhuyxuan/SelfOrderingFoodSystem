from abc import ABC, abstractmethod

class MenuItem(ABC):
    _id = -1
    def __init__(self, name, price, component, qty):
        errs = self._check_field(name, price, component, qty)
        if len(errs) > 0:
            raise InvalidFieldError(errs)
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

    
    def _check_field(self, name, price, component, qty):
        error_messages = []
        if (name is None or len(name) == 0 or str.isspace(name)):
            error_messages.append("Please specify a valid item name\n")
        
        if price <= 0 or price is None:
            error_messages.append("Please specify a valid price\n")

        """
        if component is None or not isinstance(component, InventoryObject):
            error_messages.append("Please specify a valid component\n")
        """

        if qty <= 0:
            error_messages.append("Please specigy a valid quantity\n")

        return error_messages

    # Properties
    @property
    def price(self):
        return self._price
    
    @property
    def name(self):
        return self._name
    
    @property
    def id(self):
        return self._id

    @property
    def component(self):
        return self._component

    @property
    def component_qty(self):
        return self._component_qty
    
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

class InvalidFieldError(Exception):
    def __init__(self, messages):
        self._messages = messages

    def __str__(self):
        return ''.join(self._messages)