from gpiozero import Motor
import time

motor = Motor(forward=23, backward=24)

while True:
	print("FORward")
	motor.forward()
	time.sleep(5)
	
	print("Backward")
	motor.backward()
	time.sleep(5)	
