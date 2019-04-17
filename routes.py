from flask import Flask, render_template, request, redirect, url_for, abort
app = Flask(__name__)

@app.route('/')
def base():
    return render_template('base.html')

@app.route('/menu')
def menu():
    #if request.form["checkout"] == "Checkout":
        # Need to redirect menu to order when submitting the form
    #    return redirect(url_for('order'))
    return render_template('menu.html')

@app.route('/order')
def order():
    #if request.form["payment"] == "Pay by Cash" or request.form["payment"] == "Pay by Card":
        # Need to redirect order to confirm when pressing payment choice
    #    return redirect(url_for('confirmation'))
    return render_template('order.html')
    
@app.route('/confirmation')
def confirmation():
    return render_template('confirmation.html')
    
@app.route('/order_staff')
def staff():
    return render_template('order_staff.html')
