from src.restaurant import Restaurant
from src.main import Burger, Wrap
from pickle import load
import os


def initialise_system():
    restaurant = Restaurant()
    names = ("Sesame Bun",
                "Gluten Free Bun",
                "Beef Patty", 
                "Chicken Patty",
                "Vegie Patty",
                "Chedder Cheese",
                "Tasty Cheese",
                "Coke", 
                "Chicken Nugget",
                "Chips")
    for name in names:
        restaurant.inventory.add_stock(name, 100)

    sesame_bun_inv = restaurant.inventory.get_item("Sesame Bun")
    gf_bun_inv = restaurant.inventory.get_item("Gluten Free Bun")
    bf_patty_inv = restaurant.inventory.get_item("Beef Patty")
    ck_patty_inv = restaurant.inventory.get_item("Chicken Patty")
    c_cheese_inv = restaurant.inventory.get_item("Chedder Cheese")
    t_cheese_inv = restaurant.inventory.get_item("Tasty Cheese")
    coke_inv = restaurant.inventory.get_item("Coke")
    chick_inv = restaurant.inventory.get_item("Chicken Nugget")
    chip_inv = restaurant.inventory.get_item("Chips")
    restaurant.menu.add_bun("Sesame Bun", 10, sesame_bun_inv, 1)
    restaurant.menu.add_bun("Gluten Free Bun", 10, gf_bun_inv, 1)
    restaurant.menu.add_patty("Beef Patty", 10, bf_patty_inv, 1)
    restaurant.menu.add_patty("Chicken Patty", 10, ck_patty_inv, 1)
    restaurant.menu.add_other("Chedder Cheese", 10, c_cheese_inv, 1)
    restaurant.menu.add_other("Tasty Cheese", 10, t_cheese_inv, 1)
    restaurant.menu.add_drink("Canned Coke", 10, coke_inv, 1)
    restaurant.menu.add_side("Small Chicken Nugget", 10, chick_inv, 6)
    restaurant.menu.add_side("Medium Chicken Nugget", 11, chick_inv, 8)
    restaurant.menu.add_side("Large Chicken Nugget", 12, chick_inv,10)
    restaurant.menu.add_side("Small Chips", 10, chip_inv, 20)
    restaurant.menu.add_side("Medium Chips", 10, chip_inv, 25)
    restaurant.menu.add_side("Large Chips", 10, chip_inv, 30)
    
    sesame_bun = restaurant.menu.get_item("Sesame Bun")
    beef_patty = restaurant.menu.get_item("Beef Patty")
    tasty_cheese = restaurant.menu.get_item("Tasty Cheese")

    base_burger = Burger()
    base_wrap = Wrap()

    base_burger.add_item(sesame_bun, 2)
    base_burger.add_item(beef_patty,1)
    base_burger.add_item(tasty_cheese, 1)

    base_wrap.add_item(sesame_bun, 1)
    base_wrap.add_item(beef_patty, 1)
    base_wrap.add_item(tasty_cheese, 1)

    restaurant.base_burger = base_burger
    restaurant.base_wrap = base_wrap
    if ((os.path.exists('inv.dat') and os.path.getsize('inv.dat') > 0) 
        and (os.path.exists('order.dat') and os.path.getsize('order.dat') > 0)):
        print('loading dumped data...')
        restaurant.load_data()
    print("Done")

    return restaurant
