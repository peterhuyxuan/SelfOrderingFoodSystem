from flask import Flask
from init import initialise_system
app = Flask(__name__)
app.secret_key = 'secret-key-123'
system = initialise_system()