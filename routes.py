from server import system, app
from flask import render_template, redirect, url_for, request, abort
from src.main import Burger, Wrap, InvalidQuantityException
from copy import deepcopy
@app.route('/')
def index():
    msg = request.args.get('msg') or None
    return render_template('index.html', msg = msg)

# =========index tabs==========

@app.route('/menu')
def menu():
    return redirect(url_for('index'))

@app.route('/my_order', methods = ['POST','GET'])
def my_order():
    errors = None
    if request.method == 'POST':
        errors = {}
        mains, others = handle_order_update(request.form)
        if request.form['submit'] == 'Update order':
            errors = update_order(mains, others)

        elif request.form['submit'] == 'Place order':
            errors = update_order(mains, others)
            if len(system.current_order) > 0 and len(errors) == 0:
                order_id = system.current_order.id
                system.place_order(system.current_order)
                system.reset_current_order()
                return redirect(url_for('order_detail', order_id = order_id))
            elif len(system.current_order) == 0:
                errors['other'] = 'You cannot place an empty order'

        elif "Remove" in request.form['submit']:
            print(request.form['submit'])
            index = int(request.form['submit'][6::])
            selected_main = system.current_order.mains[index]
            print(selected_main)
            system.current_order.mains.remove(selected_main)

    return render_template('order_detail.html', order = system.current_order, menu=system.menu, confirmed=False, errors = errors)

# ==========Inventory Details==========

@app.route('/inventory', methods = ['POST', 'GET'])
def inventory():
    #inventory = []
    errors = None
    form = None
    #for item in system.inventory._item:
    #    inventory.append(item)
    if request.method == 'POST':
        if request.form['submit'] == 'Restock Inventory':
            form = request.form
            errors = {}
            items = form_handler(request.form)
            for item_name,qty in items.items():
                try:
                    system.inventory.refill_stock_name(item_name,qty)
                except (ValueError) as e:
                    errors[name] = e.__str__()
            if len(items) == 0:
                print("error")
                errors['other'] = 'You cannot submit an empty order form'
            if len(errors) == 0:
                return render_template('inventory.html', inventory=system.inventory.items, msg='Inventory Restocked!')
        elif request.form['submit'] == 'Back':
            return redirect(url_for('index'))
    return render_template('inventory.html', inventory=system.inventory.items, form=form, errors=errors)

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
    errors = None 
    form = None
    if request.method == 'POST':
        if request.form['submit'] == 'Add to my order':
            form = request.form
            errors = {}
            items = form_handler(request.form)
            print(items)
            for name,qty in items.items():
                item = system.menu.get_item(name)
                try:
                    system.current_order.add_others(item, qty)
                except (ValueError, TypeError) as e:
                        errors[name] = e.__str__()
            if len(items) == 0:
                errors['other'] = 'You cannot submit an empty selection'
            if len(errors) == 0:
                return redirect(url_for('index', msg='Selected sides has been added to your order'))
        elif request.form['submit'] == 'Back':
            return redirect(url_for('index'))
    return render_template('menu_list.html', menu_items=system.menu.sides, errors = errors, form = form)

@app.route('/menu/drinks', methods = ['POST', 'GET'])
def drinks():
    errors = None 
    form = None
    if request.method == 'POST':
        if request.form['submit'] == 'Add to my order':
            errors = {}
            form = request.form
            items = form_handler(request.form)
            print(items)
            for name,qty in items.items():
                item = system.menu.get_item(name)
                try:
                    system.current_order.add_others(item, qty)
                except (ValueError, TypeError) as e:
                    errors[name] = e.__str__()

            if len(items) == 0:
                errors['other'] = 'You cannot submit an empty selection'
            if len(errors) == 0:
                return redirect(url_for('index', msg = 'Selected drinks are added to your order'))
        elif request.form['submit'] == 'Back':
            return redirect(url_for('index'))

    return render_template('menu_list.html', menu_items=system.menu.drinks,errors = errors, form = form)

@app.route('/menu/mains/base_burger')
def base_burger():
    system.current_order.add_main(deepcopy(system.base_burger))
    return redirect(url_for("index", msg = 'A base burger has been added to order'))

@app.route('/menu/mains/custom_burger', methods = ['POST', 'GET'])
def custom_burger():
    errors = None 
    form = None
    if request.method == 'POST':
        errors = {}
        form = request.form
        burger = Burger()
        items = form_handler(request.form)
        for name, qty in items.items():
            item = system.menu.get_item(name)
            try:
                burger.add_item(item, qty)
            except InvalidQuantityException as e:
                errors[name] = e.__str__()
        
        try:
            burger.check_min_buns()
        except ValueError as e:
            errors['min_buns'] = e.__str__()

        try:
            burger.check_min_patties()
        except ValueError as e:
            errors['min_patties'] = e.__str__()

        if len(items) == 0:
            errors['others'] = 'You cannot have an empty burger'
            

        if len(errors) == 0:
            system.current_order.add_main(burger)
            return redirect(url_for('index', msg = 'the customised burger has been added to your order'))

    return render_template('main_customisation.html', menu=system.menu, errors = errors, form = form)

@app.route('/menu/mains/base_wrap')
def base_wrap():
    system.current_order.add_main(deepcopy(system.base_wrap))
    return redirect(url_for("index", msg = 'A base wrap has been added to order'))

@app.route('/menu/mains/custom_wrap', methods = ['POST', 'GET'])
def custom_wrap():
    errors = None 
    form = None
    if request.method == 'POST':
        errors = {}
        form = request.form
        wrap = Wrap()
        items = form_handler(request.form)
        for name, qty in items.items():
            item = system.menu.get_item(name)
            try:
                wrap.add_item(item, qty)
            except InvalidQuantityException as e:
                errors[name] = e.__str__()
        
        try:
            wrap.check_min_buns()
        except ValueError as e:
            errors['min_buns'] = e.__str__()

        try:
            wrap.check_min_patties()
        except ValueError as e:
            errors['min_patties'] = e.__str__()

        if len(errors) == 0:
            system.current_order.add_main(Wrap)
            return redirect(url_for('index', msg = 'the customised wrap has been added to your order'))

    return render_template('main_customisation.html', menu=system.menu, errors = errors, form = form)

@app.route('/orders/<order_id>')
def order_detail(order_id):
    order_id = int(order_id)
    order = system.get_order(order_id)
    if (order is None):
        abort(404)
    return render_template('order_detail.html', order = order, menu=system.menu, confirmed = True, errors = None)

@app.route('/shutdown')
def shutdown():
    system.dump_inventory()
    system.dump_order()
    shutdown_server()
    return "Server shutting down"

def form_handler(form):
    data_dict = {}
    for item_name, qty in form.items():
        if item_name != 'submit':
            if len(qty) != 0 and int(qty) != 0:
                data_dict[item_name] = int(qty)

    return data_dict
 
def handle_order_update(form):
    main_items = {}
    other_items = {}
    for name, qty in form.items():
        if 'main-' in name:
            main_items[name.replace('main-', '')] = int(qty)
        elif 'other-' in name:
            other_items[name.replace('other-', '')] = int(qty)

    return (main_items, other_items)

def shutdown_server(): 
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with werkzeug server')
    func()

def update_order(mains, others):
    errors = {}
    for compsite_name, qty in mains.items():
        main_index = int(compsite_name[0])
        item_name = compsite_name[2::]
        item = system.menu.get_item(item_name)
        if qty > 0:
            try:
                system.current_order.mains[main_index].update_qty(item, qty)
            except (InvalidQuantityException, ValueError) as e:
                errors['main-' + compsite_name] = e.__str__()
        elif qty == 0:
            try:
                system.current_order.mains[main_index].remove_item(item)
            except ValueError as e:
                errors[str(main_index)+'other'] = e.__str__()
    
    for name, qty in others.items():
        item = system.menu.get_item(name)
        if qty > 0:
            try:
                system.current_order.update_other(item, qty)
            except ValueError as e:
                errors['other-'+name] = e.__str__()
        if qty == 0:
            system.current_order.remove_other(item)

    return errors