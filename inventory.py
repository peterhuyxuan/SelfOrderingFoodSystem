from inventory_item import inventoryItem

class inventory():

    def __init__(self):
        self._item = []

    '''
    Query Processing Services 
    '''

    def item_search(self, name=None):
        if name == None:
            for item in self._item:
                print(item)

        else:
            for item in self._item:
                if inventoryItem.name == name:
                    print(item)

    def add_stock (self, name, quantity):
        self._check_name_exists
        item = inventoryItem(name, quantity)
        self._item.append(item)

    def refill_stock (self, name, quantity):
        self._check_item_exists
        for item in self._item:
            if name == item.name:
                item.quantity = item.quantity + quantity

    def remove_stock (self, name, quantity):
        self._check_item_exists
        for item in self._item:
            if name == item.name:
                item.quantity = item.quantity + quantity

    def _check_name_exists(self, name):
        for item in self._item:
            if name == item.name:
                raise AddingError
                
    def _check_item_exists(self, name):
        id = 0
        for item in self._item:
            if name == item.name:
                id = 1
                break
        if id == 0:
            raise ItemNotFound

class AddingError(Exception):
    def __init__(self, name, reason):
        self._name = name
        self._reason = reason

    def __str__(self):
        return (f"adding {self._name} failed: {self._reason}")

class ItemNotFound(Exception):
    def __init__(self, item_id):
        self._item_id = item_id

    def __str__(self):
        return f"item ({self._item_id}) is not found in the menu"

#
