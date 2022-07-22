import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
trigPin = 20
echoPin = 21

GPIO.setup(trigPin,GPIO.OUT)
GPIO.setup(echoPin, GPIO.IN)
def measure():
	GPIO.output(trigPin, True)
	time.sleep(0.0001) ##10us
	GPIO.output(trigPin, False)
	start = time.time() #현재 시간 저장
	
	while GPIO.input(echoPin) == False:
		start = time.time()
	
	while GPIO.input(echoPin) == True:
		stop = time.time()

	duration = stop - start
	distance = (duration * 17000)

	return distance
try:
	while True:
		distance = measure()
		print("Distance : %.2f cm" %distance)
		time.sleep(1)

except KeyboardInterrupt:
	GPIO.cleanup()
