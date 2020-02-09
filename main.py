from flask import *
from flaskwebgui import FlaskUI  # get the FlaskUI class

app = Flask(__name__)
ui = FlaskUI(app)  # feed the parameters


# do your logic as usual in Flask

@app.route("/")
def index():
    return render_template('set_alarm.html')


ui.run()  # call the 'run' method
