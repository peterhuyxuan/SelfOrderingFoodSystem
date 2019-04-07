from abc import ABC, abstractmethod, abstractproperty

from inventory import inventory
from menu import Menu
from menu_item import MenuItem
from order import Order


class Restaurant():
	def __init__(self):
		self._orders = []
		self._inventory = inventory()
		self._menu = Menu()
	
	def place_order(self, order):
		self._orders.append(order)
		return order

	def change_order_status(self, order_id):
		order = self.get_order(order_id)
		order.mark_finished()
	
	def remove_order(self, order_id):
		order = self.get_order(order_id)  
		if order is not None:
			self._orders.remove(order)
	
	def checkout(self, order_id):
		order = self.get_order(order_id)
		if order is None or len(order) == 0:
			raise ValueError(f"{order} has no items to checkout or is None") 
		order.mark_finished()
		for item_name, quantity  in order.others.items():
			menu_item = self.menu.get_item(item_name)
			inv_item = menu_item.component
			self._inventory.consume_stock(inv_item.id, quantity * menu_item.component.quantity)
			
		for main in order.mains:
			for item_name, quantity in main.component.items():
				menu_item = self.menu.get_item(item_name)
				inv_item = menu_item.component
				self._inventory.consume_stock(inv_item.id, quantity * menu_item.component.quantity)
		
		# reduce_inventory
		self.remove_order(order_id)

	def get_order(self, order_id):
		for order in self._orders:
			if order_id == order.id:
				return order
		return None
			
		
	# properties
	@property
	def orders(self):
		return self._orders
	
	@property
	def inventory(self):
		return self._inventory
	
	@property
	def menu(self):
		return self._menu
