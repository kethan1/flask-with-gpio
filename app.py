from flask import *
from werkzeug.exceptions import HTTPException
import datetime
import RPi.GPIO as GPIO

app = Flask(__name__)
app.url_map.strict_slashes = False


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template('home.html', year=datetime.datetime.now().year)
    elif request.method == 'POST':
        if request.form['Button'] == 'on':
            GPIO.output(17, GPIO.HIGH)
        else:
            GPIO.output(17, GPIO.LOW)
        return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)