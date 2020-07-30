from flask import *
import datetime
import RPi.GPIO as GPIO

app = Flask(__name__)
app.url_map.strict_slashes = False


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)


@app.route('/')
def home():
    if request.method == 'GET':
        return render_template('home.html', year=datetime.datetime.now().year)


def GPIOHIGH():
    GPIO.output(17, GPIO.HIGH)


def GPIOLOW():
    GPIO.output(17, GPIO.LOW)


app.add_template_global(GPIOHIGH, name='HIGH')
app.add_template_global(GPIOLOW, name='LOW')


if __name__ == '__main__':
    app.run()