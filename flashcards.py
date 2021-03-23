from flask import Flask, render_template, abort
from datetime import datetime
from model import db

app = Flask(__name__)

#global variables
counter = 0 

@app.route("/")
def welcome():
    increment_view_count()
    return render_template("welcome.html",
    cards=db)

@app.route("/card/<int:index>")
def cards(index):
    try:
        card = db[index]
        return render_template("card.html",
                                 card=card,
                                 index=index,
                                 max_index=len(db)-1)
    except IndexError:
        abort(404)

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