from server import system, app
from flask import render_template, redirect, url_for, request

@app.route('/')
def index():
    return render_template('index.html')

# =========index tabs==========

@app.route('/menu')
def menu():
    return redirect(url_for('index'))

@app.route('/my_order')
def my_order():
    return render_template('order_detail.html', order = system._current_order, menu=system.menu)

# ==========Menu Details==========

@app.route('/menu/mains')
def mains():
    mains = []
    for main in system.menu.mains:
        mapped_func= main.lower()
        mapped_func = mapped_func.replace(' ','_')
        tup = (main, mapped_func)
        mains.append(tup)
    print(mains)
    return render_template('mains.html', mains=mains)

@app.route('/menu/sides', methods=['POST', 'GET'])
def sides():
    return render_template('menu_list.html', menu_items=system.menu.sides)

@app.route('/menu/drinks')
def drinks():
    return render_template('menu_list.html', menu_items=system.menu.drinks)

@app.route('/menu/mains/base_burger')
def base_burger():
    # add business logic
    return 'base_burger'

@app.route('/menu/mains/custom_burger')
def custom_burger():
    return render_template('main_customisation.html', menu=system.menu)

@app.route('/menu/mains/base_wrap')
def base_wrap():
    return 'base_wrap'

@app.route('/menu/mains/custom_burger')
def custom_wrap():
    return render_template('main_customisation.html', menu=system.menu)

@app.route('/orders/<order_id>')
def order_detail(order_id):
    return render_template('order_detail.html', order = system._current_order, menu=system.menu)

def form_handler(form):
    data_dict = {}
    for item_name, qty in form:
        if qty > 0:
            data_dict[item_name] = qty

    return data_dict
