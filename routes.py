from flask import Flask, render_template, request, redirect, url_for, abort
app = Flask(__name__)

@app.route('/')
def base():
    return render_template('base.html')

@app.route('/menu')
def menu():
    return render_template('menu.html')

@app.route('/order')
def order():
    return render_template('order.html')
