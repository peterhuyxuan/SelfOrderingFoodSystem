from abc import ABC, abstractmethod, abstractproperty
from pickle import dump
from src.inventory import inventory
from src.menu import Menu
from src.menu_item import MenuItem
from src.order import Order


class Restaurant():
	def __init__(self):
		self._orders = []
		self._inventory = inventory()
		self._menu = Menu()
		self._current_order = Order()
	
	def place_order(self, order):
		order.mark_placed()
		self._orders.append(order)
		self._current_order = Order()
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
		for item_name, quantity in order.others.items():
			menu_item = self.menu.get_item(item_name)
			inv_item = menu_item.component
			self._inventory.consume_stock(inv_item.id, quantity * menu_item.component_qty)
			
		for main in order.mains:
			for item_name, quantity in main.components.items():
				menu_item = self.menu.get_item(item_name)
				inv_item = menu_item.component
				self._inventory.consume_stock(inv_item.id, quantity * menu_item.component_qty)
		
		# reduce_inventory

	def get_order(self, order_id):
		for order in self._orders:
			if order_id == order.id:
				return order
		return None
			
	def save(self):
		with open('system.dat', 'wb') as f:
			dump(self, f)
			 	
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

	@property
	def current_order(self):
		return self._current_order
