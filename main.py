from flask import *
from flaskwebgui import FlaskUI  # get the FlaskUI class
import threading
import datetime as dt
import json
import os

app = Flask(__name__)
ui = FlaskUI(app)  # feed the parameters
alarms_file = open("alarms.txt", "a+")

# do your logic as usual in Flask


@app.route("/")
def index():
    return render_template('index.html')

def do_jumping_jacks(num_jacks):
    os.system("python3 playground.py" + str(num_jacks))

@app.route("/set", methods={"GET", "POST"})
def set_alarm():

    if request.method == "POST":
        time = request.form.get("time")
        jacks = request.form.get("number")
        num_jacks = int(jacks)

        alarm_time = dt.fromisoformat(time)
        timer = threading.Timer(alarm_time - dt.datetime.now(), lambda a=num_jacks: do_jumping_jacks(a))
        # timer.start()

        json.dump((time, jacks), alarms_file)
        return redirect(url_for("index"))

    elif request.method == "GET":
        return render_template('set_alarm.html')


ui.run()  # call the 'run' method
