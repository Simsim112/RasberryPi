# _*_ coding: utf-8 _*_
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
# UI 파일연동
form_class = uic.loadUiType("qtTest1.ui")[0]

class MyWindowClass(QMainWindow, form_class):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.btn1.clicked.connect(self.btn1_clicked)
		self.btn2.clicked.connect(self.btn2_clicked)

	def btn1_clicked(self):
		print("btn1 Clicked")
	
	def btn2_clicked(self):
		print("btn2 Clicked")

if __name__ == '__main__':
	app = QApplication(sys.argv)
	myWindow = MyWindowClass() #myWindowClass객체생성
	myWindow.show() #myWindow 보여줌
	sys.exit(app.exec_()) #실행 
