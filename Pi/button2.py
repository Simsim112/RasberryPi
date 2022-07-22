import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(11, GPIO.IN)
count =0

try:
	while True:
		value = GPIO.input(11)
		if value == True:
			count = count + 1
			print(count)
		time.sleep(0.1)
except keyboardInterrupt:
	GPIO.cleanup()
