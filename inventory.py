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

    def get_item(self, name):
        self._name = name
        error = False
        for item in self._item:
            if item.name == name:
                error = True
                return item
        if (error == False):
            raise ValueError(f"Item {self._name} is not in inventory")

    def add_stock (self, name, quantity):
        self._check_name_exists(name)
        item = inventoryItem(name, quantity)
        self._item.append(item)

    def refill_stock (self, id, quantity):
        self._check_item_exists(id)
        if quantity == 0:
            raise ValueError("Quantity input Cannot be Zero")
        for item in self._item:
            if id == item.id:
                item.quantity += quantity

    def consume_stock (self, id, quantity):
        self._check_item_exists(id)
        if quantity == 0:
            raise ValueError("Quantity inupt Cannot be Zero")
        for item in self._item:
            if id == item.id:
                if item.quantity < quantity:
                    raise RemovalError(item.name)
                item.quantity -= quantity

    def remove_stock(self, item_id : int):
        """
        remove the item with item_id from the inventory
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
                raise ValueError(f"item({item.name}) is already in the inventory")
                
    def _check_item_exists(self, id):
        logic = 0
        for item in self._item:
            if id == item.id:
                logic = 1
                break
        if logic == 0:
            raise ItemNotFound(id)

class ItemNotFound(Exception):
    def __init__(self, id):
        self._id = id

    def __str__(self):
        return f"item with id ({self._id}) is not found in the inventory"

class RemovalError(Exception):
    def __init__(self, name):
        self._name = name

    def __str__(self):
        return f"item ({self._name}) does not have enough stock in the inventory"
        
