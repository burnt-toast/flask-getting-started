from flask import (Flask, render_template, abort, jsonify, request,
                    redirect, url_for)
from datetime import datetime
from model import db, save_db

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


@app.route("/api/card/")
def api_card_list():
    return jsonify(db)

@app.route('/api/card/<int:index>')
def api_card_detail(index):
    try:
        return db[index]
    except IndexError:
        abort(404)

@app.route("/add_card", methods=["GET", "POST"])
def add_card():
    if request.method == "POST":
        #form has been submited, process data
        card = {"question": request.form['question'],
                "answer": request.form['answer']}
        db.append(card)
        save_db()
        return redirect(url_for('welcome'))
    else:
        app.logger.info("test")
        return render_template("add_card.html")

@app.route("/remove_card/<int:index>", methods=["GET", "POST"])
def remove_card(index):
    try:
        if request.method == "POST":
            del db[index]
            save_db()
            return redirect(url_for('welcome'))
        else:
            return render_template("remove_card.html", card = db[index])
    except IndexError:
        abort(404)
# Everything below is just test routes and not pertinent to bogus app

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