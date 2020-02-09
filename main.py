from flask import *
from flaskwebgui import FlaskUI  # get the FlaskUI class

app = Flask(__name__)
ui = FlaskUI(app)  # feed the parameters


# do your logic as usual in Flask

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/set", methods={"GET", "POST"})
def set_alarm():

    if request.method == "POST":
        pass
        # time = request
        # jacks =

    elif request.method == "GET":
        return render_template('set_alarm.html')



ui.run()  # call the 'run' method
