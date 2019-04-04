from abc import ABC, abstractmethod,abstractproperty
from menu_item import Bun, Patty, OtherIngredient, Side, Drink

class Order():

	def __init__(self):
		self._status = ("Preparing Order", "Ready for Pickup"(
		self._total_price = 0
		self._items = []
		self._num_mains = 0
		self._categoriesgories = ('_buns', '_patties', 
                                '_other_ingredients',
                                '_sides', '_drinks')
		
	def add_item(self, name, categories, price, component, qty):
        self._check_name_exists(name)
		if isinstance(categories, buns):
			item = Bun(name, price, component, qty)
			self._num_mains += 1
		elif isintance(categories, patties):
			item = Patty(name, price, component, qty)
			self._num_mains += 1
		elif isintance(categories, side):
			item = Side(name, price, component, qty)
		elif isintance(categories, drink):
			item = Drink(name, price, component, qty)
		elif isintance(categories, other):
			item = OtherIngredient(name, price, component, qty)
		self._total_price += qty * price
        self._items.append(item)
	
	def remove_item(self, item, price):
        if item in self._items:
            if isinstance(item, buns):
				self._num_mains -= 1
				self._total_price -= price
			elif isintance(item, patties):
				self._num_mains -= 1
				self._total_price -= price
			else:
				self._total_price -= price
			self._items.remove(item)
			
	# properties
	@property
	def status(self):
		return self._status
		
	def total_price(self):
		return self._total_price
		
	def items(self):
		return self._items
		
	def num_mains(self):
		return self._num_mains