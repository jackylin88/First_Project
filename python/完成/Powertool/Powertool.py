#from pymodbus.client.sync import ModbusSerialClient as ModbusClient

from pymodbus.client.sync import ModbusTcpClient as ModbusClient
import os 
import time
from datetime import datetime

print ("Editor_Jacky.lin 2019/05/15")
print ("--------------Power Tool------------------")
print ("Hints")
print ("Boot time => Time duration after relay on")
print ("On time => Time duration after boot time")
print ("Off time => Time duration after relay off")
print ("Ping action => start to ping after boot time")
print ("Ping counter (Ex.5)=> keep ping 5s ")
print ("--------------Power Tool------------------")

# Parameter--------------------------------------------------------------------------------------------

parameter = False
while parameter ==False: 
    x2=input ("ModbusTCP slave device's IP (Ex.192.168.1.1): ",) 
    while x2 =="":
        x2=input ("ModbusTCP slave device's IP(Ex.192.168.1.1): ",) 

    ID_string=input ("Modbus ID (Ex.1): ",)
    while str.isdigit(ID_string) ==False or int(ID_string)==0:
        ID_string=input ("Modbus ID (Ex.1): ",)
    ID=int(ID_string)

    AD_string=input ("Modbus address (Ex.17): ",)
    while str.isdigit(AD_string)==False or int(AD_string)<1:
        AD_string=input ("Modbus address (Ex.17): ",)
    AD=int(AD_string)-1

    x1=input ("Ping target's IP (Press Enter if no need): ",) 
    m_string=input ("Ping counter (Press Enter if no need): ",)
    if m_string=="":
        m=0
    else:
        m=int(m_string)

    t1=int(input ("Boot time(s): ",))
    t2=int(input ("On time(s): ",))-m
    while t2<0:
        print (" On_time duration must be longer than the duration of your ping action")
        t2=int(input ("On time(s): ",))-m
    t3=int(input("Off time(s): ",))
    
    Correct =input ("The setting is correct 'Y/N': ",)
    while Correct!="Y" and Correct!="y" and  Correct!="N" and Correct!="n":
        Correct =input ("The setting is correct 'Y/N': ",)
    else:
        if Correct =="Y" or Correct =="y" :
            parameter=True

z=0

#Define--------------------------------------------------------------------------------------------
def device_on (ID,AD):
    coil_single_write = client.write_coil(AD,1, unit=ID) # start address, 1 or 0, slave ID
    print (coil_single_write)
    f2 =open('log.txt','a+')
    f2.write("device on " +datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '\n')
    f2.close()
def device_off (ID,AD):
    coil_single_write = client.write_coil(AD,0, unit=ID) # start address, 1 or 0, slave ID
    print (coil_single_write)
    f2 =open('log.txt','a+')
    f2.write("device off " +datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '\n')
    f2.close()
def ping_target (x1): 
    respond1 = os.system ("ping -n 1 -w 1000 " + x1)
    if respond1 ==0:
        f2 =open('log.txt','a+')
        f2.write("ping success " +x1+" " +datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '\n')
        f2.close()
        time.sleep(1) 
    else:
        f2 =open('log.txt','a+')
        f2.write("ping fail" +x1+" " +datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '\n')
        f2.close()
    return respond1

# program--------------------------------------------------------------------------------------------
print ("start program in 5s ")
time.sleep(5)
client = ModbusClient(x2, port=502)
client.connect()
while z==0:
    device_on (ID,AD)
    time.sleep(t1)
    if x1 !="" and m>0:
        counter=0
        for i in range (m):
            if ping_target (x1)==1:
                counter+=1
        if counter==m:
            f3 =open('Ping_fail.txt','a+')
            f3.write("ping fail" +x1+" " +datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '\n')
            f3.close()
        counter=0
    time.sleep(t2)
    device_off (ID,AD)
    time.sleep(t3)


client.close()