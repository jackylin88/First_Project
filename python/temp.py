
"""
import time
from pymodbus.client.sync import ModbusTcpClient as ModbusClient
client = ModbusClient('127.0.0.1', port=502)
client.connect()
"""
"""
#function code 1
coil  = client.read_coils(0, 1, unit=0x01) # address, count, slave address
print (coil.bits)
print (coil.bits[0]) # []內表示起始後第一個值 Ex[0] 表示address 1


a=coil.bits[0]
if a == True:
    print ("yes")
else :
    print ("No")

coil_multiple_write = client.write_coils(0,[True]*3,unit=0x01)
print (coil_multiple_write)
"""


##讀DI 用print (coil.bits) or print (coil.bits[0])
##確認有沒有write DO 用print (xxx)  xxx=coil_multiple_write = client.write_coils(0,[True]*3,unit=0x01)

"""
#function code 03
holding_registers = client.read_holding_registers(1,2,unit=0x1)
print (holding_registers.registers)
print (holding_registers.registers[1]) #[0] 表示start address 後第一位 ，[1] 表示start address 後第二位
"""
"""
#function code 06
holding_registers_write = client.write_register(0,20, unit=0x01) #表4x0001第一個寫入AO=10
"""
"""
#function code 16
holding_registers_write = client.write_registers(0,[20,40,60,80,100], unit=0x01) #將4x0001~4x0005寫成分別寫入20,40,60,80,100
"""
"""
class Animal():
 def __init__(self, name,age,hight):
  self.name = name
  self.age = age
  #self.hight =hight
a = Animal("dog",8,"log")  #建立一個名叫dog的Animal實體(物件)
print(a.name)
print(a.age)
#print(a.hight)


https://medium.com/@weilihmen/%E9%97%9C%E6%96%BCpython%E7%9A%84%E9%A1%9E%E5%88%A5-class-%E5%9F%BA%E6%9C%AC%E7%AF%87-5468812c58f2




import threading 

# 子執行緒的工作函數
def job(num):
  print("Thread", num)
  time.sleep(3)

# 建立 5 個子執行緒
threads = []
for i in range(5):
  threads.append(threading.Thread(target = job, args = (i,)))
  threads[i].start()
"""


"""
def thread1_job():
    global m
    m=input("input 0 or 1",)
    while m!="2":
        m=input("input 0 or 1",)

    def thread2_job():
        global m
        m=0
        while int(m)==0:
            print ("loop")
            time.sleep(1)
        else:
            print ("end")


class Animal(): 
    name=1 
    print (name)
    def __init__(self,name,age): #init表示呼叫class後自動來做
        self.name=name 
        self.age=age
        print (name) #沒有self只是區域變輸
        print (self.name) #加self 後是class裡的全域變數
    

    def test (self):
        print (self.name)



i1=input("your animal name: ",)
i2=input("your animal age: ",)
a = Animal(i1,i2)

print (a.name)
print (a.age)
a.test()
"""
"""
f = open ("news.txt","r")
for line in open ("news.txt"):
    print(line)
    #print("yes")
#print(f.readline())
"""
"""
import csv
with open('output.csv', 'w', newline='') as csvfile:
  # 以空白分隔欄位，建立 CSV 檔寫入器
  writer = csv.writer(csvfile)

  writer.writerow(['姓名', '身高', '體重'])
  writer.writerow(['令狐沖', 175, 60])
  writer.writerow(['岳靈珊', 165, 57])
"""
"""
import json
import csv

employee_data='{"employee_details":[{"employee_name":"James", "email":"james@gmail.com","job_profile":"Sr. Developer"},{"employee_name": "Smith", "email": "Smith@gmail.com", "job_profile": "Project Lead"}]}'
employee_parsed = json.loads(employee_data)

emp_data = employee_parsed['employee_details']

# open a file for writing

employ_data = open('EmployData.csv', "a+")

# create the csv writer object

csvwriter = csv.writer(employ_data)

count = 0
for emp in emp_data:
    if count == 0:
        header = emp.keys()
        csvwriter.writerow(header)
        count += 1
    csvwriter.writerow(emp.values())

employ_data.close()
"""
"""
from pymodbus.client.sync import ModbusTcpClient as ModbusClient
import os 
import time
from datetime import datetime

class connectiontest(): 
    def __init__(self,time): #init表示呼叫class後自動來做
        #self.name=name 
        #self.age=age
        print ("open",time) #沒有self只是區域變輸
        #print (self.name) #加self 後是class裡的全域變數
    
    def thread_def():
        thread=threading.Thread(target=thread_job.start)
        thread.start()

    def thread_job():
        client = ModbusClient(x2, port=502)
        client.connect()
        coil  = client.read_coils(AD, 1, unit=ID) # start address,bit count, slave ID
        print (coil.bits[0]) #讀0x0001值是True or False
        time.sleep(1)



m=4
for i in range (m):
    connectiontest(i+1)
    time.sleep(1)

"""
"""
import time
from datetime import datetime

import threading 
class Animal():
    def __init__(self,big="default"):
        self.data = 123
        self.big=big
        global m
        print (m)
        #c=input()
        #print(c)
    def dep(self,money=1000):
        self.money=money
        print(self.money)
        #c=input("輸入測試",)
        #print(c)
        global m
        m+=1
        print (m)
        
    def thread1_job(self):
      global m
      m=input("input 0 or 1:",)
      while m!="0":
          m=input("input 0 or 1:",)

    def thread2_job(self):
        global m
        m=1
        while int(m)!=0:
            print ("loop")
            time.sleep(1)
        else:
            print ("end")

   

m=0
a = Animal()
#a.dep()
#a.dep(5000)

thread1=threading.Thread(target=a.thread1_job)
thread2=threading.Thread(target=a.thread2_job)
thread1.start()
thread2.start()

"""

"""
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
m=int(m_string)-1

class connectiontest(): 
    def __init__(self,time): #init表示呼叫class後自動來做
        print ("open",time) #沒有self只是區域變輸
        self.thread_def()
        #print (self.name) #加self 後是class裡的全域變數
    
    def thread_def(self):
        thread=threading.Thread(target=self.thread_job())
        #thread.start()
        #thread.quit()

    def thread_job(self):
        client = ModbusClient(x2, port=502)
        client.connect()
        z=0
        while z==0:
            coil  = client.read_coils(AD, 1, unit=ID) # start address,bit count, slave ID
            print (coil.bits[0]) #讀0x0001值是True or False
            time.sleep(1)


for i in range (m):
    ii=i+1
    print(ii)
    connectiontest(ii)
    time.sleep(1)
    """

"""
import json
class Person(object):
   def __init__(self, first_name = None, last_name = None):
      self.first_name = first_name
      self.last_name = last_name
   #returns Person name, ex: John Doe
   def name(self):
      return ("%s %s" % (self.first_name,self.last_name))
		
   @classmethod
   #returns all people inside db.txt as list of Person objects
   def getAll(self):
      database = open('db.txt', 'r')
      result = []
      json_list = json.loads(database.read())
      for item in json_list:
         item = json.loads(item)
         person = Person(item['first_name'], item['last_name'])
         result.append(person)
      return result

View
from model import Person
def showAllView(list):
   print 'In our db we have %i users. Here they are:' % len(list)
   for item in list:
      print item.name()
def startView():
   print 'MVC - the simplest example'
   print 'Do you want to see everyone in my db?[y/n]'
def endView():
   print 'Goodbye!'


Controller
from model import Person
import view

def showAll():
   #gets list of all Person objects
   people_in_db = Person.getAll()
   #calls view
   return view.showAllView(people_in_db)

def start():
   view.startView()
   input = raw_input()
   if input == 'y':
      return showAll()
   else:
      return view.endView()

if __name__ == "__main__":
   #running controller function
   start()
"""
"""
b=str(input("input: ",))
a = "I'm %s. I'm %d year old" % (b, 2,)
#a="I'm %(name)s. I'm %(age)d year old" % {'name':'Vamei', 'age':99}
print(a)

print("%+10x" % 10)
print("%04d" % 5)
print("%6.3f" % 2.3)
"""
"""

try:
    abc
    print ("123")
except NameError as err:
    #err="456"
    print ("(Error: 没有找到文件或读取文件失败",err)
except:
    print ("error")
else:
    print ("nothing happen")
"""
"""
import threading  
import time  
class timer(threading.Thread): #The timer class is derived from the class threading.Thread  
    def __init__(self, num, interval):  
        threading.Thread.__init__(self)  
        self.thread_num = num  
        self.interval = interval  
        self.thread_stop = False  
   
    def run(self): #Overwrite run() method, put what you want the thread do here  
        while not self.thread_stop:  
            print (self.thread_num,"test")
            time.sleep(self.interval)  
    def stop(self):  
        self.thread_stop = True  
         

   
def test(i):  
    print (i, type(i))
    i = timer(i, 1)  
    print (i, type(i))
    i.setDaemon(True)
    i.start()  
    #time.sleep(5)  
    #thread.stop()   
    return  
   

for i in range (2):
    test(i)  
    time.sleep(1) 
time.sleep(10) 
"""

"""
import threading  
import time  
class timer(threading.Thread): #The timer class is derived from the class threading.Thread  
    def __init__(self, num, interval):  
        threading.Thread.__init__(self)  
        self.thread_num = num  
        self.interval = interval  
        self.thread_stop = False  
   
    def run(self): #Overwrite run() method, put what you want the thread do here  
        while True:
            while not self.thread_stop:  
                print (self.thread_num,"test")
                print("------------------------------------")
                time.sleep(self.interval)  
    def stop(self):  
        self.thread_stop = True  
    def continue_(self):  
        self.thread_stop = False  


def test(i):  
    
    globals()['thread%s'%i]=timer(i, i)  
    #print(locals()['thread%s'%i])
    globals()['thread%s'%i].setDaemon(True)
    globals()['thread%s'%i].start()

for ii in range(2):
    i=ii+1
    test(i)
    time.sleep(1)

time.sleep(5)
print ("stop thread2")
thread2.stop()
time.sleep(5)
print ("start thread2")
thread2.continue_()
time.sleep(5)
"""
"""
lst1=[]

def function1(word):
    lst1=[]
    #print (word)
    lst1.append(word)
    return lst1

print(function1(123))
print(function1(456))


def function2(i,ii=1):
    ii=i+10
    return ii

print(function2(1))
print(function2(2))
"""

# def dic_function(parameter):
#     globals()['dic%s'%parameter]={}
    

import requests
url="http://192.168.1.1/infostatus.asp"
r=requests.get(url)
#print (r.status_code)
#print (r.text)

from bs4 import BeautifulSoup
soup=BeautifulSoup(r.text,'html.parser')
data=soup.find_all("td")
dictionary={}
for i in range(0,len(data),2):
    try :
        dictionary[data[i].string]=data[i+1].string
    except:
        break
print (dictionary)
print("----------------------------------------------")

# #data=soup.title
# #data=soup.find_all("body") #會把找到符合條件的都放在一個list內
# #data=soup.find("body") #找到第一個符合條件的直接顯示
# data=soup.find("a")
# print(data.string)
# data2=data.find_next_siblings("a") #找出來後會放到list內
# print(data2[0].string)
# print(data2[0].string)


