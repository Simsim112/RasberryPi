import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
# UI 파일연동
form_class = uic.loadUiType("qtTest1.ui")[0]

class MyWindowClass(QMainWindow, form_class):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.btn.clicked.connect(self.btn_clicked)
	def btn_clicked(self):
		print("btn Clicked")

if __name == '__main':
	app = QApplication(sys.argv)
	mywindow = MywindowClass() #myWindowClass객체생성
	myWindow.show() #myWindow 보여줌
	sys.exit(app.exec_()) #실행 
