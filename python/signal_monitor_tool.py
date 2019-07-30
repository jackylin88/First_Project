from pythonping import ping
import string
import time
from datetime import datetime
from selenium import webdriver

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
    def __init__(self,AP_IP,client_IP,Timeout):
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
    

a=IP_class(AP_IP,client_IP,Timeout)

# Program--------------------------------------------------------------------------------------------
#print ("start program in 5s ")
#time.sleep(5)

counter=0
for i in range (4):
    a.ping_function(AP_IP)
    if a.ping_result_function()==False:
        counter+=1

if counter==4:
    print ("Program terminal due to the inactive AP")
else:
    print ("Browser Opening")
    browser = webdriver.Chrome()
    browser.get("http://admin:admin@"+AP_IP+"/index.htm#../template/wireless/statistics.shtml")
    z=0
    while z==0:
        counter=0
        for i in range (5):
            a.ping_function(client_IP)
            if a.ping_result_function()==False:
                counter+=1
        if counter!=5:
            STA_information=browser.find_element_by_xpath('//*[@id="sta_list0"]').text
            print (STA_information)
            time.sleep(1)
        

print ("finsih")
print ("---------------------------------")


# Reference--------------------------------------------------------------------------------------------
"""
a.ping_function(AP_IP)
a.ping_function(client_IP)
print (a.ping_result_function())
"""