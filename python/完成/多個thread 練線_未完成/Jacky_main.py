import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets, QtNetwork
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtNetwork import *
from PyQt5.uic import *
from datetime import datetime
import time
from pymodbus.client.sync import ModbusTcpClient as ModbusClient
import threading 



def resource_path(relative):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative)
    return os.path.join(relative)

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        loadUi(resource_path(os.path.join('jacky_gui.ui')),self)
        self.lineEdit.setPlaceholderText("Ex.192.168.1.1")
        self.lineEdit_2.setPlaceholderText("Ex.1")
        self.lineEdit_3.setPlaceholderText("Ex.17")
        self.lineEdit_4.setPlaceholderText("Ex.60")
        self.lineEdit_5.setPlaceholderText("Ex.60")
        self.lineEdit_6.setPlaceholderText("Ex.10")
        self.lineEdit_7.setPlaceholderText("Ex.192.168.1.1")
        self.lineEdit_8.setPlaceholderText("Ex.60")
        self.pushButton_2.setEnabled(False)
        global AD,ID,t2,x1
        ID = int(self.lineEdit_2.text())
        AD = int(self.lineEdit_3.text())-1
        t2=int(self.lineEdit_5.text())-int(self.lineEdit_8.text())
        x1=self.lineEdit_7.text()
        self.pushButton.clicked.connect(self.connect) 
        self.pushButton_2.clicked.connect(self.disconnect) 
        #self.pushButton_3.clicked.connect(self.start)
        #self.pushButton_4.clicked.connect(self.thread4_def)


    def connect(self):
        self.client = ModbusClient(self.lineEdit.text(), port=502)
        if self.client.connect()==True:
            self.pushButton_2.setEnabled(True)
            self.pushButton.setEnabled(False)
            print (self.client.connect())
        else :
            self.client.close()
            QMessageBox.information(self,"Warning","Wrong parameters")
            #show_message("warming","Wrong parameters")
        

    def disconnect(self):
        self.client.close()
        self.pushButton.setEnabled(True)
        self.pushButton_2.setEnabled(False)
        print (self.client.close())
        #print ("close")
    
    def start(self):
        global z
        z=0
        while z==0:
            coil_single_write =self.client.write_coil(AD,1, unit=ID) # start address, 1 or 0, slave ID
            print (coil_single_write)
            for i in range (int(self.lineEdit_4.text())):
                time.sleep(1)
                f2 =open('log.txt','a+')
                f2.write("device on " +datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '\n')
                f2.close()
                if z==1:
                    return

            counter=0
            for ii in range (int(self.lineEdit_8.text())):
                if self.ping_target()==1:
                    counter+=1
                if z==1:
                    return
            if counter==int(self.lineEdit_8.text()):
                f3 =open('Ping_fail.txt','a+')
                f3.write("ping fail" +x1+" " +datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '\n')
                f3.close()
            counter=0 

            if t2 >0:
                for iii in range (t2):
                    time.sleep(1)
                    f2 =open('log.txt','a+')
                    f2.write("device off " +datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '\n')
                    f2.close()
                    if z==1:
                        return

            coil_single_write =self.client.write_coil(AD,0, unit=ID) # start address, 1 or 0, slave ID
            print (coil_single_write)
            for iiii in range (int(self.lineEdit_6.text())):
                time.sleep(1)
                if z==1:
                    return
    
    def stop(self):
        global z
        z=1
        print ("stop")

    
    def ping_target (self): 
        print (x1)
        respond1 = os.system ("ping -n 1 -w 1000 " + x1)
        if respond1 ==0:
            f2 =open('log.txt','a+')
            f2.write("ping success " +x1+" " +datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '\n')
            f2.close()
            print ("ping success")
            time.sleep(1) 
        else:
            f2 =open('log.txt','a+')
            f2.write("ping fail" +x1+" " +datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '\n')
            f2.close()
            print ("ping fail")
        return respond1

    """
    def show_message (self,title="Test",message="Test"):
        QMessageBox.information(self,"Warning","Wrong parameters")
    """


        #print(self.lineEdit.text())
        #print(self.lineEdit_2.text())
        #print(self.lineEdit_3.text())

        #self.textBrowser.append("Ho")
        #self.listWidget.addItem("Hi")  #將內容顯示在list widget上，list只能顯示str
        #self.lineEdit_2.setText(self.lineEdit.text())

        
        #if int(self.lineEdit.text()) > 100:
        #    print ("over range")

"""
def thread1_def ():
    thread1=threading.Thread(target=form.connect)
    thread1.start()

def thread2_def ():
    thread2=threading.Thread(target=form.disconnect)
    thread2.start()
"""
def thread3_def ():
    thread3=threading.Thread(target=form.start)
    thread3.start()

def thread4_def ():
    thread4=threading.Thread(target=form.stop)
    thread4.start()


if __name__ == '__main__':
    
    app = QtWidgets.QApplication(sys.argv)
    form = MainWindow() 
    #form.pushButton.clicked.connect(thread1_def) 
    #form.pushButton_2.clicked.connect(thread2_def)
    form.pushButton_3.clicked.connect(thread3_def)
    form.pushButton_4.clicked.connect(thread4_def)
    form.setFocus()
    form.show()
    sys.exit(app.exec_())