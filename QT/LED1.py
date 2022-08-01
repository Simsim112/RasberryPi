import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import RPi.GPIO as GPIO
import time
import Adafruit_DHT

GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)

sensor = Adafruit_DHT.DHT11
pin = 4

form_class = uic.loadUiType("LED.ui")[0]

class MyAppClass(QMainWindow, form_class):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.pushButton.clicked.connect(self.btnCallBack)
		self.pushButton_2.clicked.connect(self.btn2CallBack)
		self.pushButton_3.clicked.connect(self.btn3CallBack)
		self.pushButton_4.clicked.connect(self.btn4CallBack)

	def btn3CallBack(self):

		h, t = Adafruit_DHT.read_retry(sensor, pin)
		if h is not None and t is not None:
			self.textEdit_2.append("Temp = {0:0.1f}*C Humidity = {1:0.1f}%".format(t,h))

	def btn4CallBack(self):
		self.textEdit_2.clear()

	def btnCallBack(self):
		print("LED ON")
		self.textEdit.clear()
		self.textEdit.append("LED ON")
		GPIO.output(21, True)
	def btn2CallBack(self):
		print("LED OFF")
		self.textEdit.clear()
		self.textEdit.append("LED OFF")
		GPIO.output(21, False)

if __name__ == "__main__":
	app = QApplication(sys.argv)
	myWindow = MyAppClass()
	myWindow.show()
	sys.exit(app.exec_())
