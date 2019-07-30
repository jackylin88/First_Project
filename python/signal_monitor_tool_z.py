from pythonping import ping
import string
import time
from datetime import datetime
from selenium import webdriver
import requests
import bs4 #要記得先pip install beautifulsoup4
import threading
# Parameter--------------------------------------------------------------------------------------------
parameter = False
while parameter ==False: 
    
    AP_IP=input ("AP's IP (Ex.192.168.1.1): ",) 
    while AP_IP =="":
        AP_IP=input ("AP's IP (Ex.192.168.1.1): ",) 
    """
    client_IP=input ("client's IP (Ex.192.168.1.2): ",) 
    while client_IP =="":
        client_IP=input ("AP's IP (Ex.192.168.1.2): ",) 
    
    Timeout=input("Respond Timeout in s (Ex.1): ",) 
    while str.isdigit(Timeout)==False or int(Timeout)<100:
        Timeout=input("Respond Timeout in ms (Ex.1000): ",)
    """
    Correct =input ("The setting is correct 'Y/N': ",)
    while Correct!="Y" and Correct!="y" and  Correct!="N" and Correct!="n":
        Correct =input ("The setting is correct 'Y/N': ",)
    else:
        if Correct =="Y" or Correct =="y" :
            parameter=True

Timeout=1
# Define--------------------------------------------------------------------------------------------

class IP_class():
    def __init__(self,AP_IP,client_IP="192.168.1.1",Timeout=1):
        self.AP_IP=AP_IP
        self.client_IP=client_IP
        self.Timeout=Timeout
        

    def ping_function(self,IP):
        response_list=ping(IP, verbose=True,count=1,timeout=self.Timeout)
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

class Collector(threading.Thread): #The timer class is derived from the class threading.Thread  
    def __init__(self, interval):  
        threading.Thread.__init__(self)  
        self.interval = interval  
        self.thread_stop = False  
   
    def run(self): #Overwrite run() method, put what you want the thread do here  
        x=0
        while x==0:
            while not self.thread_stop:  
                try:
                    url="http://192.168.1.1/wlassociation.asp"
                    r= requests.get(url)
                    data=r.text
                    time.sleep(self.interval) 
                    lists=[]
                    root=bs4.BeautifulSoup(data,"html.parser")
                    #print (root.title.string) 
                    titles=root.find_all("td") #直接找<a href="/bbs/movie/M.1562036136.A.FBA.html">[討論] 誰最會演爸爸??</a>
                    for title in titles:
                        obj=title.string
                        lists.append(obj)
                    print (lists)
                except:
                    pass
        else:
            time.sleep(1)

    def stop(self):  
        self.thread_stop = True  
    def Continue(self):
        self.thread_stop = False 

def test():  
    global thread1
    thread1 = Collector(1)   
    thread1.setDaemon(True)
    thread1.start()   
    return

a=IP_class(AP_IP)
#a=IP_class(AP_IP,client_IP,Timeout)

# Program--------------------------------------------------------------------------------------------
counter=0
for i in range (4):
    a.ping_function(AP_IP)
    if a.ping_result_function()==False:
        counter+=1

if counter==4:
    print ("Program terminal due to the inactive AP")
else:
    print ("----------------------------")
    test()
    z=0
    while z==0:
        counter=0
        a.ping_function(AP_IP)
        if a.ping_result_function()==False:
            thread1.stop()
        else:
            thread1.Continue()
            pass

print ("finsih")
print ("---------------------------------")


# Reference--------------------------------------------------------------------------------------------
"""
a.ping_function(AP_IP)
a.ping_function(client_IP)
print (a.ping_result_function())
"""