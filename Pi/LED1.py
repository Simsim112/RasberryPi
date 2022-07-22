
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(21,GPIO.OUT)
while(True):
	if(GPIO.input(21) == True):
		GPIO.output(21, False)
		time.sleep(1)
	GPIO.output(21, True)
	time.sleep(1)
