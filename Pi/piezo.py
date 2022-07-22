import RPi.GPIO as GPIO
import time

piezoPin = 13
melody = [261, 293, 329, 369, 391, 440, 483, 523]

GPIO.setmode(GPIO.BCM)
GPIO.setup(piezoPin, GPIO.OUT)

Buzz = GPIO.PWM(piezoPin, 440)

def selecting(number):
	Buzz.start(30.0)
	Buzz.ChangeFrequency(melody[number])
try:
	while True:
		sel = input("1~8까지 번호를 입력해주세요: ")
		if(sel =="1"):
			selecting(0)
		elif(sel == "2"):
			selecting(1)
		elif(sel =="3"):
			selecting(2)
		elif(sel =="4"):
			selecting(3)
		elif(sel =="5"):
			selecting(4)
		elif(sel=="6"):
			selecting(5)
		elif(sel=="7"):
			selecting(6)
		elif(sel=="8"):
			selecting(7)
		else:
			print("제대로 입력해주세요")
		time.sleep(1)
		Buzz.stop()
except KeyboardInterrupt:
	GPIO.cleanup()
