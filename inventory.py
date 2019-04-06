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
        if quantity == 0:
            raise ZeroError
        for item in self._item:
            if name == item.name:
                item.quantity += quantity

    def consume_stock (self, name, quantity):
        self._check_item_exists
        if quantity == 0:
            raise ZeroError
        for item in self._item:
            if name == item.name:
                if item.quantity < quantity:
                    raise RemovalError
                item.quantity -= quantity

    def remove_stock(self, item_id : int):
        """
        remove the item with item_id from the menu
        if item is not in menu 
        """
        removal_flag = False
        for item in self._item:
            if item.id == item_id:
                self._item.remove(item)
                removal_flag = True
                break

            if removal_flag == True:
                break

        if removal_flag == False:
            raise ItemNotFound(item_id)

    '''
    Helper functions
    '''

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
            raise ItemNotFound(item.id)

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
        return f"item ({self._item_id}) is not found in the inventory"

class RemovalError(Exception):
    def __init__(self, item_id):
        self._item_id = item_id

    def __str__(self):
        return f"item ({self._item_id}) does not have enough stock in the inventory"

class ZeroError(Exception):
    def __init__(self, item_id):
        self._item_id = item_id
    
    def __str__(self):
        return f"item ({self._item_id} cannot be zero"
        