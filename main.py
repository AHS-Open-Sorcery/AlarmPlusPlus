from flask import *
from flaskwebgui import FlaskUI  # get the FlaskUI class
import threading
import datetime as dt
import json
import os

app = Flask(__name__)
ui = FlaskUI(app)  # feed the parameters
alarms_file = open("alarms.txt", "r+")

# do your logic as usual in Flask

def get_alarms():
    alarms = []
    global alarms_file
    if alarms_file is not None:
        alarms_file.close()
    alarms_file = open("alarms.txt", "r+")
    line = alarms_file.readline()
    while line is not None:
        #print(line)
        if not line:
            break
        alarms.append(json.loads(line))
        #print(json.loads(line))
        line = alarms_file.readline()
    alarms_file.close()
    return alarms



@app.route("/")
def index():
    alarms = get_alarms()
    print(alarms)
    return render_template('index.html')


def do_jumping_jacks(num_jacks):
    os.system("python3 playground.py --jumpingQuantity " + str(num_jacks))


@app.route("/set", methods={"GET", "POST"})
def set_alarm():
    if request.method == "POST":
        time = request.form.get("time")
        jacks = request.form.get("number")
        num_jacks = int(jacks)

        alarm_time = dt.fromisoformat(time)

        if alarm_time - dt.datetime.now() < 0:
            timer = threading.Timer(alarm_time - dt.datetime.now(), lambda a=num_jacks: do_jumping_jacks(a))
            # timer.start()
            global alarms_file
            if alarms_file is not None:
                alarms_file.close()
            alarms_file = open("alarms.txt", "a+")
            alarms_file.write(json.dumps((time, jacks), alarms_file) + "\n")
            alarms_file.close()
        return redirect(url_for("index"))

    elif request.method == "GET":
        return render_template('set_alarm.html')


ui.run()  # call the 'run' method
