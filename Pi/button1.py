
import RPi.GPIO as GPIO
import time

switchPin = 11
GPIO.setmode(GPIO.BCM)
GPIO.setup(switchPin,GPIO.IN)

try:
	while(True):
		if GPIO.input(switchPin) == True:
			print("Pushed")
			time.sleep(0.2)
except KeyboardInterrupt:
	GPIO.cleanup()

