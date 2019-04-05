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
		
	def add_order(self, order):
	    self._orders.append(order)

    def change_order_status(self, order_id):
		order = self.get_order(order_id)
		order.mark_finished()
	
	def remove_order(self, order_id):
		order = self.get_order(order_id)  
		if order is not None:
		    self._orders.remove(order)
	
	def checkout(self, order_id):
	    order = self.get_order(order_id)
	    order.mark_finished()
	    for item_name, qty  in order.items:
	        if isinstance(item, Main):
	            for component_id, qty in item.component.items():
	                self.consume_stock(component_id, qty)
            if isinstance(item, MenuItem):
                self.consume_stock(component_it, qty)
	    
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
