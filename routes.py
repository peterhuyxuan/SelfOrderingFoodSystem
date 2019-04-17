from server import system, app

@app.route('/')
def index():
    return '<h1>Hello</h1>'
