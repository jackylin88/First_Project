import os
a=os.system ("ping -n 2 192.168.0.159") #ping WISE
b=os.system ("ping -n 2 192.168.0.1") #ping AP
while a>0:
    while b==0:
        print("fail")
        a=a-1
    else :
        a=a-1
else :
    print: ("connect")
    