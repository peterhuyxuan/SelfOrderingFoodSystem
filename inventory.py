from inventory_item import inventoryItem

class inventory():

    def __init__(self):
        self._item = []

    '''
    Query Processing Services 
    Mainly used for testing purposes
    '''

    def item_search(self, name=None):
        if name == None:
            for item in self._item:
                print(item)

        else:
            for item in self._item:
                if inventoryItem.name == name:
                    print(item)

