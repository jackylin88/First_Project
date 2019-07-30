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
        self.thread = QtCore.QThread() #??
        self.thread.start()
        self.worker = Worker()#?
        self.worker.moveToThread(self.thread) #?? moveToThread
        self.worker.showre.connect(self.update_Show)#時時將showre的參數傳到update_show
        self.start.clicked.connect(self.thread_start) #點及button後，開始啟動，並執行跳出secondform
        self.stop.clicked.connect(self.thread_stop)
        self.otherview = SecondForm(self)

    def thread_start(self):
    	self.hide()
    	#otherview = SecondForm(self)
    	self.otherview.show() #跳出secondfrom視窗
    	self.worker.setTime(self.lineEdit.text())
    	self.worker.start() #執行這支thread

    def thread_stop(self):
        self.worker.stop() #停止work這支
        self.thread.quit() #關閉thread
        self.thread.wait()
    def update_Show(self, message):
    	self.result.setText(message)
    	self.otherview.update_Show1(message) #將showre傳來的val值傳給secondform.update show1
    	self.label_hh.setText(self.otherview.lineEdit.text()) #找不到labehh


class SecondForm(QDialog):
	def __init__(self, parent=None):
		super(SecondForm, self).__init__(parent)
		loadUi(resource_path(os.path.join('update.ui')), self)
		self.pushButton.clicked.connect(self.goBackToOtherForm)
		
	def goBackToOtherForm(self):
		self.parent().show()
		self.close()

	def update_Show1(self, message):
		self.label_shiot.setText('fuck' + message)
		self.lineEdit.setText(message + "calvin") #讓設定val至line edit
		print (message)

class Worker(QThread):
	showre = QtCore.pyqtSignal(str) #signal 是三小?
	
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