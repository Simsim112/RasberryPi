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

@app.route('/user/<user_name>/<int:user_id>')
def user(user_name, user_id):
	GPIO.output(21, True)
	return f'Hello, {user_name}({user_id})!'

if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True)
