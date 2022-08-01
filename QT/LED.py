import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)

form_class = uic.loadUiType("LED.ui")[0]

class MyAppClass(QMainWindow, form_class):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.pushButton.clicked.connect(self.btnCallBack)
		self.pushButton_2.clicked.connect(self.btn2CallBack)

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
