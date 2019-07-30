import sys
from PyQt5 import QtCore, QtGui, QtWidgets, QtNetwork
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtNetwork import *
from PyQt5.uic import *
import time
import os
def resource_path(relative):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative)
    return os.path.join(relative)

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        loadUi(resource_path(os.path.join('main.ui')),self)
        self.thread = QtCore.QThread()
        self.thread.start()
        self.worker = Worker()
        self.worker.moveToThread(self.thread)
        self.worker.showre.connect(self.update_Show)
        self.start.clicked.connect(self.thread_start)
        self.stop.clicked.connect(self.thread_stop)
        self.otherview = SecondForm(self)

    def thread_start(self):
    	self.hide()
    	#otherview = SecondForm(self)
    	self.otherview.show()
    	self.worker.setTime(self.lineEdit.text())
    	self.worker.start()

    def thread_stop(self):
        self.worker.stop()
        self.thread.quit()
        self.thread.wait()
    def update_Show(self, message):
    	self.result.setText(message)
    	self.otherview.update_Show1(message)
    	self.label_hh.setText(self.otherview.lineEdit.text())


class SecondForm(QDialog):
	def __init__(self, parent=None):
		super(SecondForm, self).__init__(parent)
		loadUi(resource_path(os.path.join('update.ui')), self)
		self.pushButton.clicked.connect(self.goBackToOtherForm)
		
	def goBackToOtherForm(self):
		self.parent().show()
		self.close()

	def update_Show1(self, message):
		#print('fuck',message)
		self.label_shiot.setText('fuck' + message)
		print(self.lineEdit.setText(message + "calvin"))

class Worker(QThread):
	showre = QtCore.pyqtSignal(str)
	
	def __init__(self, parent=None):
		super(Worker, self).__init__(parent)

	def stop(self):
		self.working = False
		self.quit()
		self.wait()

	def setTime(self, val):
		self.time_sleep = val

	def run(self):
		self.sec = 0
		self.working = True
		while self.working == True:
			self.sec += 1
			if self.sec == int(self.time_sleep):
				self.working = False
			self.showre.emit(str(self.sec))
			time.sleep(1)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    form = MainWindow()
    form.show()
    sys.exit(app.exec_())