from inventory_item import inventoryItem
from inventory import inventory

import pytest
import sys

system = inventory()
for name in ["Seseme Bun", "Brioche Bun", "Lettuce", "Tomato", "Patty"]:
    system.add_stock(name, 100)

def test_full_search(capsys):
    #This tests if all the inventory has been added or not
    #
    system.item_search()
    res = capsys.readouterr()
    expected_output = ("Item <Seseme Bun, 100, 0>\n"
        "Item <Brioche Bun, 100, 1>\n"
        "Item <Lettuce, 100, 2>\n"
        "Item <Tomato, 100, 3>\n"
        "Item <Patty, 100, 4>\n")
    assert res.out == expected_output

def test_null_search(capsys):
    #This checks if the system can skip the read
    system.item_search("Onion")
    res = capsys.readouterr()
    expected_output = ("")
    assert res.out == expected_output

def test_add_item(capsys):
    #This checks if the system can add an extra item afterwards
    #system.add_stock("Bacon", 100)
    system.item_search()
    res = capsys.readouterr()
    expected_output = ("Item <Seseme Bun, 100, 0>\n"
        "Item <Brioche Bun, 100, 1>\n"
        "Item <Lettuce, 100, 2>\n"
        "Item <Tomato, 100, 3>\n"
        "Item <Patty, 100, 4>\n")
    assert res.out == expected_output