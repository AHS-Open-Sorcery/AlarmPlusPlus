from flask import *
from flaskwebgui import FlaskUI  # get the FlaskUI class
import threading
from datetime import datetime
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
        # print(line)
        if not line:
            break
        alarms.append(json.loads(line))
        # print(json.loads(line))
        line = alarms_file.readline()
    alarms_file.close()
    return alarms


@app.route("/")
def index():
    alarms = get_alarms()

    alarms_dictionary = {
        'time': [],
        'number': []
    }

    for alarm in alarms:
        alarms_dictionary['time'].append(alarm[0])
        alarms_dictionary['number'].append(alarm[1])

    print(alarms)
    return render_template('index.html', alarms=alarms_dictionary)


def do_jumping_jacks(num_jacks):
    os.system("python3 playground.py --jumpingQuantity " + str(num_jacks))


@app.route("/set", methods={"GET", "POST"})
def set_alarm():
    if request.method == "POST":
        time = request.form.get("time")
        jacks = request.form.get("number")
        num_jacks = int(jacks)

        print(time)

        alarm_time = datetime.fromtimestamp(float(time) / 1e3)

        if alarm_time - datetime.now() > dt.timedelta(0):
            timer = threading.Timer((alarm_time - datetime.now()).seconds, lambda a=num_jacks: do_jumping_jacks(a))
            timer.start()
            global alarms_file
            if alarms_file is not None:
                alarms_file.close()
            alarms_file = open("alarms.txt", "a+")
            # print(json.dumps((alarm_time.strftime("%Y-%m-%d %H:%M:%S"), jacks)))
            alarms_file.write(json.dumps((alarm_time.strftime("%Y-%m-%d %H:%M:%S"), jacks)) + "\n")
            alarms_file.close()
        return redirect(url_for("index"))

    elif request.method == "GET":
        return render_template('set_alarm.html')


ui.run()  # call the 'run' method
