from flask import Flask
from datetime import datetime

app = Flask(__name__)

#global variables
counter = 0 

@app.route("/")
def welcome():
    increment_view_count()
    return "welcome to my flash cards application! " + __name__

@app.route("/date")
def date():
    increment_view_count()
    return "This is page was served at " + str(datetime.now())

@app.route("/count_views")
def count_views():
    increment_view_count()
    return "this page was served " + str(counter) + " times"

def increment_view_count():
    global counter
    counter +=1