import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(11, GPIO.IN)
GPIO.setup(12, GPIO.IN)
GPIO.setup(21, GPIO.OUT)


try:
	while True:
		value1 = GPIO.input(11)
		value2 = GPIO.input(12)
		if value1 == True:
			GPIO.output(21, True)
			print("불이 켜졌습니다")
		elif value2 == True:
			GPIO.output(21, False)
			print("불이 꺼졌습니다.")
		time.sleep(0.1)
except keyboardInterrupt:
	GPIO.cleanup()
