from flask import *
import datetime
import RPi.GPIO as GPIO

app = Flask(__name__)
app.url_map.strict_slashes = False


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(17, GPIO.HIGH)


@app.route('/')
def home():
    if request.method == 'GET':
        return render_template('home.html', year=datetime.datetime.now().year)


@app.route('/LOW')
def LOW():
    GPIO.output(17, False)


@app.route('/HIGH')
def HIGH():
    GPIO.output(17, True)


if __name__ == '__main__':
    app.run(host="0.0.0.0")