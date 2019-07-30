print ("Editor_Jacky.lin 2019/07/15")
print ("--------------MB_TCP_Session Testing tools------------------")
print ("Note: This Tool is designed to read DI value (Address:0x0000)")
print ("--------------MB_TCP_Session Testing tools------------------")
print ("")
#------------------------------------------libaray-------------------------------------------------------
import threading
from pythonping import ping
import string
from pymodbus.client.sync import ModbusTcpClient as ModbusClient
import time
from datetime import datetime
#-------------------------------------------parameters------------------------------------------------------
global Slave_IP,ID,AD,interval

parameter = False
while parameter ==False: 
    Slave_IP=input ("ModbusTCP slave device's IP (Ex.192.168.1.1): ",) 
    while Slave_IP =="":
        Slave_IP=input ("ModbusTCP slave device's IP(Ex.192.168.1.1): ",) 

    ID_string=input ("Modbus ID (Ex.1): ",)
    while str.isdigit(ID_string) ==False or int(ID_string)<=0:
        ID_string=input ("Modbus ID (Ex.1): ",)
    ID=int(ID_string)

    AD_string=input ("Modbus address (Ex.17): ",)
    while str.isdigit(AD_string)==False or int(AD_string)<1:
        AD_string=input ("Modbus address (Ex.17): ",)
    AD=int(AD_string)-1

    """
    #擴充功能所需參數 Polling interval，此版不用用到該功能
    interval_string=input("Polling Interval in s (Ex.1s): ",)
    while str.isdigit(AD_string)==False or int(AD_string)<0:
        interval_string=input("Polling Interval in s (Ex.1): ",)
    interval=int(interval_string)
    """

    Timeout_string=input("Modbus slave Timeout in s(Ex.1s): ",)
    while str.isdigit(Timeout_string) ==False or int(Timeout_string)<=0:
        Timeout_string=input("Modbus slave Timeout in s(Ex.1s): ",)
    MD_Timeout=int(Timeout_string)

    N_Thread_string=input("Number of Modbus TCP session: ",)
    while str.isdigit(N_Thread_string) ==False or int(N_Thread_string)<=0:
        N_Thread_string=input("Number of Modbus TCP session: ",)
    N_Thread=int(N_Thread_string)

    Correct =input ("The setting is correct 'Y/N': ",)
    while Correct!="Y" and Correct!="y" and  Correct!="N" and Correct!="n":
        Correct =input ("The setting is correct 'Y/N': ",)
    else:
        if Correct =="Y" or Correct =="y" :
            parameter=True

#-------------------------------------------function------------------------------------------------------

class IP_class():
    def __init__(self,Slave_IP,Ping_Timeout=1):
        self.Slave_IP=Slave_IP
        self.Ping_Timeout=Ping_Timeout
        

    def ping_function(self,IP):
        response_list=ping(IP, verbose=True,count=1,timeout=self.Ping_Timeout)
        self.source=str(response_list)
        self.requirement=str("Reply from "+IP)
        self.ping_result_function()
        return response_list

    def ping_result_function(self):
        try:
            self.source.index(self.requirement)
            time.sleep(1)
            return True
        except(ValueError): 
            return False

class Thread_(threading.Thread): #The class is derived from the class threading.Thread  
    def __init__(self,Slave_IP,ID,AD,i,MD_Timeout):  # 擴充功能要在此加入interval
        threading.Thread.__init__(self)  
        self.Slave_IP=Slave_IP
        #self.interval = interval
        self.MD_Timeout=MD_Timeout  
        self.ID=ID
        self.AD=AD
        self.thread_stop = False  
        self.N=i #第N個thread
   
    def run(self): #Overwrite run() method, put what you want the thread do here  
        self.client = ModbusClient(self.Slave_IP, port=502,timeout=self.MD_Timeout)
        try :
            self.client.connect()
            print("Thread No."+str(self.N)+" connection status:"+str(self.client.connect()))
            coil  = self.client.read_coils(self.AD, 1, unit=self.ID)
            print ("Thread No."+str(self.N)+" reads '"+str(coil.bits[self.AD])+"' on Address"+str(self.AD+1)) #讀0x0001值是True or False
            
            #若要持續polling則啟用下方這段code
            """
            while not self.thread_stop:
                coil  = self.client.read_coils(self.AD, 1, unit=self.ID)
                print ("Thread No."+str(self.N)+" reads '"+str(coil.bits[self.AD])+"' on Address"+str(self.AD+1)) #讀0x0001值是True or False
                time.sleep(self.interval)
            """
        except Exception as e:
            print (e)
            print ("No."+str(self.N)+" TCP session connection fail") 
    
    #stop/Continue function後續擴充可以使用
    """
    def stop(self):  
        self.thread_stop = True  
    def Continue(self):
        self.thread_stop = False 
    """

def Run_Thread(i):  
    globals()['thread%s'%i]=Thread_(Slave_IP,ID,AD,i,MD_Timeout) # 擴充功能要在此加入interval
    globals()['thread%s'%i].setDaemon(True)
    globals()['thread%s'%i].start()   
    return

a=IP_class(Slave_IP)
#-------------------------------------------program------------------------------------------------------
counter=0
for ii in range(4):
    a.ping_function(Slave_IP)
    if a.ping_result_function()==True:
        counter+=1

if counter==4:
    for ii in range (N_Thread):
        i=ii+1
        Run_Thread(i)
        time.sleep(1)
    while True:
        input ("Press 'Enter' to End the Program " ,)
        break
else:
    print ("End the program due to Ping fail of Modbus Slave Device ")

#-------------------------------------------reference-----------------------------------------------------
"""
a.ping_function(Slave_IP)
print (a.ping_result_function())
thread1.stop() #停止polling 迴圈
thread1.Continue()#在啟用polling 迴圈，若要己用該功能，要記得在def run 加個while 迴圈讓threadkeep alive
"""