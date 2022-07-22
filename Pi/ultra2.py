import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
trigPin = 20
echoPin = 21
piezoPin = 26

GPIO.setup(piezoPin, GPIO.OUT)
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
def Clocking(num):
	Buzz.start(30)
	Buzz.ChangeFrequency(1046)
	time.sleep(num)
	Buzz.start(0)
	time.sleep(num)

Buzz = GPIO.PWM(piezoPin, 440)
try:
	while True:
		distance = measure()
		time.sleep(0.3)
		print("Distance : %.2f cm" %distance)
		if(distance < 10):
			Buzz.start(30)
			Buzz.ChangeFrequency(1046)
			time.sleep(0.1)
			Buzz.start(0)
			time.sleep(0.1)
		elif(distance < 20):
			Buzz.start(30)
			Buzz.ChangeFrequency(1046)
			time.sleep(0.5)
			Buzz.start(0)
			time.sleep(0.5)
except KeyboardInterrupt:
	GPIO.cleanup()
