from flask import Flask
from init import initialise_system
import signal


app = Flask(__name__)
app.secret_key = 'secret-key-123'

system = initialise_system()

def sigint_handler(signum, frame):
    system.save()
    exit()

signal.signal(signal.SIGINT, sigint_handler)