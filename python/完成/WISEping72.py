import os
import time
from datetime import datetime

x="192.168.1.72" # WISE IP
y="192.168.1.1" # AP IP
z=0 # loop parameter

def ping_WISE (x): 
    respond1 = os.system ("ping -n 1 -w 1000 " + x)
    print("respond1")
    print(respond1)
    if respond1 ==0:
        f2 =open('WISE_log.txt','a+')
        f2.write("ping WISE success " +x+" " +datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '\n')
        f2.close()
        time.sleep(1) 
    else:
        f2 =open('WISE_log.txt','a+')
        f2.write("ping WISE fail" +x+" " +datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '\n')
        f2.close()
    return respond1

def ping_AP (y):
    respond2 = os.system ("ping -n 1 -w 1000 " + y)
    if respond2 ==0:
        f3 =open('AP_log.txt','a+')
        f3.write("ping AP success" +y+" " +datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '\n')
        f3.close()
    else :
        f3 =open('AP_log.txt','a+')
        f3.write("ping AP fail" +y+" " +datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '\n')
        f3.close()
    time.sleep(1)
    return respond2

while z==0: # loop 
    while ping_WISE (x)==0:
        print ("ping WISE success")
    else :
        counter1=0
        for i in range (4): # keep testing n ICMP packets
            if ping_WISE (x)==1:
                counter1+=1
                print (counter1)
            else:
                break
        if counter1==4: # loss n ICMP packet
            if ping_AP (y)==0:
                for times in range (120): # n second later after AP ready
                    ping_AP (y)
                counter2=0
                for ii in range (3): # keep testing n ICMP packets 
                    if ping_WISE (x)==1:
                        counter2+=1
                    else :
                        break
                if counter2==3: # loss n ICMP packet
                    print ("WISE issue")
                    print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
                    f1 = open('fail.txt','a+')
                    f1.write("WISE fail issue " + datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '\n')
                    f1.close()
                counter2=0
        counter1 =0


          


        