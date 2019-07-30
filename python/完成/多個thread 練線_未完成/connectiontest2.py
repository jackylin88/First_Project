from pymodbus.client.sync import ModbusTcpClient as ModbusClient
import os 
import time
from datetime import datetime
import threading 

global x2
x2=input ("ModbusTCP slave device's IP (Ex.192.168.1.1): ",) 
while x2 =="":
    x2=input ("ModbusTCP slave device's IP(Ex.192.168.1.1): ",) 

ID_string=input ("Modbus ID (Ex.1): ",)
while str.isdigit(ID_string) ==False or int(ID_string)==0:
    ID_string=input ("Modbus ID (Ex.1): ",)
global ID
ID=int(ID_string)

AD_string=input ("Modbus address (Ex.17): ",)
while str.isdigit(AD_string)==False or int(AD_string)<1:
    AD_string=input ("Modbus address (Ex.17): ",)
global AD
AD=int(AD_string)-1

m_string=input ("connection times: ",)
global m
m=int(m_string)

class connectiontest(): 
    def __init__(self): #init表示呼叫class後自動來做
        print ("start") #沒有self只是區域變輸
        #self.thread_def()
        #print (self.name) #加self 後是class裡的全域變數
    
    #def thread_def(self):
        #thread=threading.Thread(target=self.thread_job())
        #thread.start()
        #thread.quit()

    def thread_job(self):
        client = ModbusClient(x2, port=502,timeout=3)
        client.connect()
        print ("test")
        global z
        z=0
        while z==0:
            coil  = client.read_coils(AD, 1, unit=ID) # start address,bit count, slave ID
            #print (coil.bits[0]) #讀0x0001值是True or False
            time.sleep(1)

a=connectiontest()

for i in range (m):
    ii=i+1
    print(ii)
    thread=threading.Thread(target=a.thread_job)
    thread.start()
    time.sleep(1)


global z
z=input("input 1:",)



"""
for i in range (m):
    client = ModbusClient(x2, port=502)
    client.connect()
    print (i+1,"time")
    coil  = client.read_coils(AD, 1, unit=ID) # start address,bit count, slave ID
    print (coil.bits[0]) #讀0x0001值是True or False
    time.sleep(0.1)
    

client = ModbusClient(x2, port=502)
client.connect()
print (m+1,"time")
z=0
while z==0:
    coil  = client.read_coils(AD, 1, unit=ID) # start address,bit count, slave ID
    print (coil.bits[0]) #讀0x0001值是True or False
    time.sleep(1)

"""
    