from flask import Flask
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(21,GPIO.OUT)
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
	return 'Hello, World!'

@app.route('/user/<LED>')
def user(LED):
	if LED == 'ON':
		GPIO.output(21, True)
	elif LED == 'OFF':
		GPIO.output(21, False)
	else:
		return "ON 또는 OFF를 입력해주세요"
	return f'LED, {LED}!'

if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True)
