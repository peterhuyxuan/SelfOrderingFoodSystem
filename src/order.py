from abc import ABC, abstractmethod,abstractproperty
from src.main import Main
from src.menu_item import Side, Drink

class Order():
	_id = -1
	def __init__(self):
		self._status= "Not Yet Confirmed"
		self._total_price = 0
		self._others = {}
		self._mains = []
		Order._id += 1
		self._id = Order._id

	def add_main(self, main):
		if not isinstance(main, Main):
			raise TypeError(f"{main} is not a Main") 
		self._mains.append(main)
		self._total_price += main.price
				
	def remove_main(self, main_id):
		for main in self._mains:
			if main.id == main_id:
				self._total_price -= main.price
				self._mains.remove(main)
			
	def add_others(self, item, qty):
		if not isinstance(item, (Side,Drink)):
			raise TypeError(f"{item} is neither side nor drink")
		if qty < 1:
			raise ValueError(f"qty ({qty}) less than 1")
		if qty * item.component_qty > item.component.quantity:
			raise ValueError(f"Insufficient stock for {item.name}")
		if isinstance(item, Side):
			self._others[item.name] = qty
		elif isinstance(item, Drink):
			self._others[item.name] = qty
		self._total_price += qty * item.price
	
	def update_other(self, item, qty): 
		if qty < 1:
			raise ValueError(f"qty ({qty}) less than 1")
		if qty * item.component_qty > item.component.quantity:
			raise ValueError(f"Insufficient stock for {item.name}")
		change_in_qty = qty - self._others[item.name]
		self._total_price += change_in_qty * item.price
		self._others[item.name] = qty

	
	def remove_other(self, item):
		try:
			qty = self._others.pop(item.name)
		except KeyError:
			print(f"{item.name} is not in the order")
		else:
			self._total_price -= qty * item.price
				
	def mark_finished(self):
		self._status = "Ready for Pickup"

	def mark_placed(self):
		self._status= "Preparing your order"
	@classmethod
	def _reset_id(cls):
		cls._id = -1
	
	"""
	def order_checkout(self, order_id):
		self._order_done = True
		# print dictionary
		def __str__(self):
			return f"Total price is ${self._total_price}"
	"""
			
	# properties
	@property
	def status(self):
		return self._status
	
	@property
	def total_price(self):
		return self._total_price
	
	@property
	def others(self):
		return self._others
	
	@property
	def id(self):
		return self._id
		
	@property
	def mains(self):
		return self._mains
		
	def __len__(self):
		len_others = 0
		for qty in self._others.values():
			len_others += qty
		
		return 	len_others + len(self._mains)
