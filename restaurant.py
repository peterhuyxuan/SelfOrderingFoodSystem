from abc import ABC, abstractmethod,abstractproperty
from order import Order
from menu import Menu
from main import Main
from menu_item import MenuItem
from inventory import inventory

class Restaurant():
	def __init__(self):
		self._orders = []
		self._inventory = []
		self._menu = Menu()
		
	def add_order(self):
                order = Order()
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
		if len(order) == 0 or order is None:
			raise ValueError(f"{order} has no items to checkout or is None") 
		order.mark_finished()
		for item_name, qty  in order.others.items():
			self.consume_stock(item_name, qty)
			
		for main in order.mains:
			for component_id, qty in main.component.items():
				self.consume_stock(component_id, qty)
		
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
	def inventory_system(self):
		return self._inventory_system
	
	@property
	def menu(self):
		return self._menu
