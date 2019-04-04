from abc import ABC, abstractmethod,abstractproperty
from menu_item import Bun, Patty, OtherIngredient, Side, Drink

class Order():

	def __init__(self):
		self._order_done = False
		self._total_price = 0
		self._items = {}
		Order._id += 1
		self._id = Order._id
		
	def add_item(self, name, categories, price, component, qty):
        self._check_name_exists(name)
		if isinstance(item, Main):
		    #
		elif isinstance(Item, side):
			item = Side(name, price, Item, qty)
		elif isinstance(categories, drink):
			item = Drink(name, price, component, qty)

		self._total_price += qty * price
        self._items.append(item)
	
	def remove_item(self, item, price):
        if item in self._items:
            if isinstance(item, buns):
				self._total_price -= price
			elif isintance(item, patties):
				self._total_price -= price
			else:
				self._total_price -= price
			self._items.remove(item)
			
	def mark_finished(self):
		self._order_done = True
	
	def order_removal(self, order_id):
		for id in self._id
			if id == order_id
				self._order_done = False
				self._total_price = 0
				new_order._items = []
				Order._id -= 1
				new_order._id = Order._id
				break
    
    def order_checkout(self, order_id):
        self._order_done = True
        # print dictionary
        def __str__(self):
            return f"Total price is ${self._total_price}"
        order_removal(order_id)
        	
	# properties
	@property
	def order_done(self):
		return self._order_done
	
	@property
	def total_price(self):
		return self._total_price
	
	@property
	def items(self):
		return self._items
	
	@property
	def id(self):
        return self._id
