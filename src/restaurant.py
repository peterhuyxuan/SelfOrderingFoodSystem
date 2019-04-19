from abc import ABC, abstractmethod, abstractproperty
from pickle import dump, load
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
		self._base_burger = None
		self._base_wrap = None

	def place_order(self, order):
		order.mark_placed()
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
			
	def dump_inventory(self):
		with open('inv.dat', 'wb') as f:
			dump(self._inventory, f)
	
	def dump_order(self):
		with open('order.dat', 'wb') as f:
			dump(self._orders,f)
			print(self._orders)

	def load_data(self):
		with open('order.dat', 'rb') as f:
			self._orders = load(f)
			# make id  continues to count
			Order.assign_id(len(self._orders))
			# update id of current order
			self._current_order._id = len(self._orders)
			print(self._orders)
		with open('inv.dat', 'rb') as f:
			self._inventory = load(f)

	def reset_current_order(self):
		self._current_order = None
		order = Order()
		self._current_order = order

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

	@property
	def base_burger(self):
		return self._base_burger

	@property
	def base_wrap(self):
		return self._base_wrap

	@base_burger.setter
	def base_burger(self, burger):
		self._base_burger = burger

	@base_wrap.setter
	def base_wrap(self, wrap):
		self._base_wrap = wrap
