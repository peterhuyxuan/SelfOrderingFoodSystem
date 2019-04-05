from abc import ABC, abstractmethod,abstractproperty
from main import Main
from menu_item import Side, Drink

class Order():
    _id = -1
	def __init__(self):
		self._order_done = False
		self._total_price = 0
		self._items = {}
		self._mains = []
		Order._id += 1
		self._id = Order._id
		
	def add_others(self, item, qty):
        self._check_name_exists(name)
		if isinstance(item, Side):
		    self._items[item.name] = qty
		elif isinstance(item, Drink):
			self._items[item.name] = qty
		self._total_price += qty * item.price
	
	def update_other(self, item, qty): 
	    try:
	        self._items[item.name] = qty
	    except KeyError:
	        print(f"{item.name} is not in the order")
	        
	def add_main(self, main):
	    self._mains.append(main)
	    self._price += main.price
	
	def remove_other(self, item):
        try:
            qty = self._items.pop(item.name)
        except KeyError:
	        print(f"{item.name} is not in the order")
        else:
            self._total_price -= qty * item.price
            
    def add_main(self, main):
	    self._mains.append(main)
	    self._price += main.price
			
	def mark_finished(self):
		self._order_done = True
    
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
