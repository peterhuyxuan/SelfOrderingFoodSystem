from menu_item import  Side, Drink
from main import Main
class Order():

	def __init__(self):
<<<<<<< HEAD
		self._order_done = False
=======
            """
            items should be a dicitonary
            use name of the item as key
            you dont need _num_mains and _categoriesgories
            """ 
		self._status = ("Preparing Order", "Ready for Pickup"(
>>>>>>> 46a083f02c2c5757018ca85b8288489c139a211a
		self._total_price = 0
		self._items = []
		Order._id += 1
		self._id = Order._id
		
        def add_item(self, item, qty):
        self._check_name_exists(name)
            if isinstance(item, Main):
            """
            use isinstance like this
            """
			item = Bun(name, price, component, qty)
		elif isintance(categories, patties):
			item = Patty(name, price, component, qty)
		elif isintance(categories, side):
			item = Side(name, price, component, qty)
		elif isintance(categories, drink):
			item = Drink(name, price, component, qty)
		elif isintance(categories, other):
			item = OtherIngredient(name, price, component, qty)
		self._total_price += qty * price
        self._items.append(item)
	
	def remove_item(self, item):
        """
        change item to item_name which is a string
        iterate through the dictionary to find key has save value
        remove that entry
        """
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
<<<<<<< HEAD
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
=======
	def status(self):
		return self._status
	
        @property
	def total_price(self):
		return self._total_price
        
        @property
	def items(self):
		return self._items
		
        @property
	def num_mains(self):
		return self._num_mains
>>>>>>> 46a083f02c2c5757018ca85b8288489c139a211a
