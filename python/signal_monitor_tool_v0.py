from selenium import webdriver
import time
import os
from datetime import datetime
#使用chrome的webdriver
browser = webdriver.Chrome()
browser.get("http://admin:admin@192.168.1.161/index.htm#../template/wireless/statistics.shtml") #若要增加username/password Ex. 加admin/admin@ 

x1="192.168.1.161"
def ping_target (x1): 
    respond1 = os.system ("ping -n 1 -w 1000 " + x1)
    if respond1 ==0:
        print (datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        time.sleep(1) 
    else:
        print (datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    return respond1

#---------------------------------------------client mode---------------------------------------------------
"""
for i in range (200):
    if ping_target(x1)==0:
        signal=browser.find_element_by_xpath('//*[@id="sta_signal_level"]').text
        print (signal)
        time.sleep(5) 
    else:
        pass
"""
#---------------------------------------------AP mode---------------------------------------------------
z=0
while z==0:
    if ping_target(x1)==0:
        for i in range (3):
            i_str=str(i)
            signal=browser.find_element_by_xpath('//*[@id="sta_list_signal'+i_str+'"]').text
            if signal !="":
                mac=browser.find_element_by_xpath('//*[@id="sta_list_bssid'+i_str+'"]').text
                print (mac+" "+signal)
        time.sleep(5) 


print ("finish")
browser.close()
#//*[@id="sta_list_bssid0"]
