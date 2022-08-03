import RPi.GPIO as GPIO
import sys
import time

GPIO.setmode(GPIO.BCM)
pin1 = 23
pin2 = 24

GPIO.setup(pin1, GPIO.OUT)
GPIO.setup(pin2, GPIO.OUT)

try:
	while True:
		GPIO.output(pin1, True)
		GPIO.output(pin2, False)

except KeyboardInterrupt:
	GPIO.cleanup()
