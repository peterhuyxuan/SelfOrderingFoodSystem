from inventory_item import inventoryItem
from inventory import inventory, RemovalError, ItemNotFound

import pytest
import sys


system = inventory()
inventoryItem._reset_id_count()
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

def test_add_stock(capsys):
    #This checks if the system can add an extra item afterwards
    system.add_stock("Bacon", 100)
    system.item_search()
    res = capsys.readouterr()
    expected_output = ("Item <Seseme Bun, 100, 0>\n"
        "Item <Brioche Bun, 100, 1>\n"
        "Item <Lettuce, 100, 2>\n"
        "Item <Tomato, 100, 3>\n"
        "Item <Patty, 100, 4>\n"
        "Item <Bacon, 100, 5>\n")
    assert res.out == expected_output

def test_remove_stock(capsys):
    #This checks if the system can remove an item
    system.remove_stock(5)
    system.item_search()
    res = capsys.readouterr()
    expected_output = ("Item <Seseme Bun, 100, 0>\n"
        "Item <Brioche Bun, 100, 1>\n"
        "Item <Lettuce, 100, 2>\n"
        "Item <Tomato, 100, 3>\n"
        "Item <Patty, 100, 4>\n")
    assert res.out == expected_output

def test_consume_stock(capsys):
    #This checks if the system can consume stock
    system.consume_stock(4, 1)
    system.item_search()
    res = capsys.readouterr()
    expected_output = ("Item <Seseme Bun, 100, 0>\n"
        "Item <Brioche Bun, 100, 1>\n"
        "Item <Lettuce, 100, 2>\n"
        "Item <Tomato, 100, 3>\n"
        "Item <Patty, 99, 4>\n")
    assert res.out == expected_output

def test_refill_stock(capsys):
    ##This checks if the system can add stock
    system.refill_stock(4, 1)
    system.item_search()
    res = capsys.readouterr()
    expected_output = ("Item <Seseme Bun, 100, 0>\n"
        "Item <Brioche Bun, 100, 1>\n"
        "Item <Lettuce, 100, 2>\n"
        "Item <Tomato, 100, 3>\n"
        "Item <Patty, 100, 4>\n")
    assert res.out == expected_output

def test_AddingError():
    #This checks if the system can detect multiple items
    #system.add_stock("Patty", 1)
    with pytest.raises(ValueError):
        system.add_stock("Patty", 1)
        assert len(system) == 4

def test_RemovalError():
    #This checks if the system can detect if the item consumption is higher than stock
    with pytest.raises(RemovalError):
        system.consume_stock(4, 101)
        assert system._item[4].quantity == 100

#The two following tests checks if the system rejects orders with zero as the quantity

def test_consume_zero():
    with pytest.raises(ValueError):
        system.consume_stock(4, 0)
        assert system._item[4].quantity == 100 

def test_refill_zero():
    with pytest.raises(ValueError):
        system.refill_stock(4, 0)
        assert system._item[4].quantity == 100 

#These last three tests check if the system can hanlde wrong ids

def test_invalid_consume():
    with pytest.raises(ItemNotFound):
        system.consume_stock(-1, 5)

def test_invalid_refill():
    with pytest.raises(ItemNotFound):
        system.refill_stock(-1, 5)

def test_invalid_remove_stock():
    with pytest.raises(ItemNotFound):
        system.remove_stock(-1)