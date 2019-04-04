from abc import ABC, abstractmethod,abstractproperty
from order import Order
from menu import Menu
from inventory import inventory

class Restaurant():
	def __init__(self):
		self._orders = []
		self._inventory_system = []
		self._menu = Menu()
		
	def make_order(self, menu_item, name, price, component, qty):
		new_order = Order()
		new_order._items = add_item(name, menu_item, price, component, qty) #edit according to new order
	
	def change_order_status(self):
		mark_finished()
	
	def remove_order(self, order_id):
		order_removal(order_id)
	
	def checkout(self, order_id):
	    order_checkout(order_id)
	    # reduce_inventory
		
	# properties
	@property
	def orders(self):
		return self._orders
	
	@property
	def inventory_system(self):
		return self._inventory_system
	
	@property
	def menu(self):
		return self._menu
