from flask import *
from flaskwebgui import FlaskUI  # get the FlaskUI class
import threading
import datetime as dt
import json

app = Flask(__name__)
ui = FlaskUI(app)  # feed the parameters
alarms_file = open("alarms.txt")

# do your logic as usual in Flask


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/set", methods={"GET", "POST"})
def set_alarm():

    if request.method == "POST":
        time = request.form.get("alarm_time")
        jacks = request.form.get("number_jacks")

        alarm_time = dt.fromisoformat(time)
        timer = threading.Timer(alarm_time - dt.datetime.now())

        json.dump((time, jacks), alarms_file)

    elif request.method == "GET":
        return render_template('set_alarm.html')



ui.run()  # call the 'run' method
