from inventory_item import inventoryItem
from inventory import inventory

import pytest
import sys

def setup_system():
    class IdGenerator():
    
        def __init__(self):
           self._id = 0
        
        def next(self):
            self._id += 1
            return self._id

    rego_generator = IdGenerator()

    system = inventory()
    for name in ["Seseme Bun", "Brioche Bun", "Lettuce", "Tomato", "Patty"]:
        system.add_item(inventoryItem(name, 100, 5, rego_generator.next()))

    return system

def test_full_search(capsys):
    #This tests if all the inventory has been added or not
    system = setup_system()
    system.item_search()
    res = capsys.readouterr()
    expected_output = ("Item <Seseme Bun, 100, 5, 1>\n"
        "Item <Brioche Bun, 100, 5, 2>\n"
        "Item <Lettuce, 100, 5, 3>\n"
        "Item <Tomato, 100, 5, 4>\n"
        "Item <Patty, 100, 5, 5>\n")
    assert res.out == expected_output