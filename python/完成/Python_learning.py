#---------------------------------------------def-------------------------------------------------
def sum (a):
    return 0
sum (10) 
print (sum)

sum (20)
print (sum)

#def中只要一return 就直接結束該函數

#---------------------------------------------if--------------------------------------------------
#不小心買到Samsung Note 7、聽說電池快沒電時容易有爆炸的風險，怎麼辦?! 利用邏輯運算來提醒我們這個危機吧！
smartphone = input("輸入你的手機品牌:")
power = int (input ("輸入你的手機電量%:"))
while power < 0 or power > 100 :
    print ("輸入錯誤，請重新輸入")
    power = int (input ("重新輸入你的手機電量(0~100%):"))
if smartphone == "samsung" and int (power)<=5 :
    print ("快逃壓，要爆炸了")
elif not smartphone =="samsung" or int (power) <5 :
    print ("不會爆炸，但手機是samsung的話要小心")

#---------------------------------------------for 迴圈-------------------------------------------------

#九九乘法表
for i in range (1,10):
    for j in range (1,10):
        print (i*j,end=" ")
    print(end="\n")


for k in range (1,15,2):
    print (k,end=" ")

#---------------------------------------------file open-------------------------------------------------
f2 =open('log.txt','a+')
    f2.write("device off " +datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '\n')
    f2.close()

#---------------------------------------------while 迴圈-------------------------------------------------
import os # ping command
import time # time sleep
from datetime import datetime # print system time
a=os.system ("ping -n 1 192.168.0.11")
while a==0:
    print (a)
    print ("success")
    #print(datetime.now().strftime('%Y-%m-%d %H:%M:%S')+ " connect ")
    time.sleep (1) 
    #os.system ("ping -n 1 192.168.0.159")
else :
    print ("loss connection")

#---------------------------------------------system sleep-------------------------------------------------
import time # time sleep
time.sleep (1) 

#---------------------------------------------system time-------------------------------------------------
from datetime import datetime
f2.write("device off " +datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '\n')
#---------------------------------------------__name__=='__main__'-------------------------------------------------
#程式1(temp.py) =>執行後結果顯示local & local2
def cool_function():
    print ("local") 

if __name__=='__main__':
    cool_function()
    print ("local2")

#程式2(temp2.py)=>執行後結果顯示local & remote 
from temp import cool_function 
cool_function()
print ("remote")

#---------------------------------------------Global變數-------------------------------------------------
#需要def function 內可以影響def外，需要再def 內宣告其為gobal變數，如下
def test():
    global var1 # gobal 寫在def內可以影響外面，一般都寫在def function中
    var1 = 10
    print ("------------------------------")
var1 = 5
print(var1)
test()
print(var1)

#若是def內要引用，def外的變數，則不需要宣告gobal 變數即可，但要住要def內不能在宣告該參數
def test():
    print (var1) 
    #var1 = 10 #若再次宣告，python會認為，上面print指令在還未宣告就先python，因此產生錯誤
    print ("------------------------------")
var1 = 5   
test()
print(var1)

https://extenshu.com/2017/09/24/python%E5%88%9D%E5%AD%B8%E9%87%8D%E9%BB%9E-05-global%E8%AE%8A%E6%95%B8/



#---------------------------------------------Multiple Threads-------------------------------------------------
import threading 
def thread1_job():
    for i in range (20):
        i+=1
        print (i)
        time.sleep(1)

def thread2_job():
    ii=100
    for ii in range (100,105):
        ii+=1
        print (ii)
        time.sleep(1)
        #input("thread2 input",)

thread1=threading.Thread(target=thread1_job)
thread2=threading.Thread(target=thread2_job)
thread1.start()
thread2.start()
#---------------------------------------------class-------------------------------------------------
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
m=0
a = Animal()
a.dep()
a.dep(5000)
#---------------------------------------------QtCore.pyqtSignal-------------------------------------------------
from PyQt5.QtCore import QObject, pyqtSignal

class NewSignal(QObject):

    # 一个valueChanged的信号，该信号没有参数.
    valueChanged = pyqtSignal()

    def connect_and_emit_valueChanged(self):
        # 绑定信号和槽函数
        self.valueChanged.connect(self.handle_valueChanged)

        # 发射信号.
        self.trigger.emit()

    def handle_valueChanged(self):
        print("trigger signal received")

自定义信号的一般流程如下： 
1、定义信号 
2、定义槽函数 
3、绑定信号和槽 
4、发射信号


#---------------------------------------------class-------------------------------------------------

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
#-------------------------------------------------- 寫成csv-------------------------------------------
import csv
with open('output.csv', 'w', newline='') as csvfile:
  # 以空白分隔欄位，建立 CSV 檔寫入器
  writer = csv.writer(csvfile)

  writer.writerow(['姓名', '身高', '體重'])
  writer.writerow(['令狐沖', 175, 60])
  writer.writerow(['岳靈珊', 165, 57])

#---------------------------------------------------透過append 新增list,pop刪減list,&list combine----------------------------------------
z=0
lists=[]
while z==0:
    obj=input ("news element:",)
    lists.append(obj)
    print (lists)
    for list in lists:
        print ("list: ",list)
    print ("------------------------------")

# pop括號內為刪減的index，預設是-1表示最後一個
lst.pop(0)



#combine
list1=[123,456]
list2=[789,999]
list_combine=list1+list2
print (list_combine)
list_combine2=zip(list1,list2)
print(list(list_combine2))


#create 一個list 0~9
list1=list(range(10)) 
print(list1)


#選倒數三個
fruits = ['apple', 'banana', 'cherry', 'date']
print(fruits[-3:])

#Note: integer 做過"除"運算後，會被視為float，若要使其為整數，要用int()

#list 高級用法
def delete_starting_evens(lst):
  while (len(lst) > 0 and lst[0] % 2 == 0):
    lst = lst[1:]
  #lst=[i for i in range lst if i%2]
  return lst

#Uncomment the lines below when your function is done
print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
print(delete_starting_evens([4, 8, 10]))



#---------------------------------------------------*args , 外加list概念----------------------------------------
f1=input ("first: ",)
f2=input ("second: ",)
print ("------------------------------")
lists =[f1,f2]
for list in lists:
    print ("list" ,list)  #將list 逐條列出
print ("------------------------------")
def fun (*args): #用*args 表示多個可變參數
    print ("fun",args)
    for i in args:
        print ("i: ",i)

fun (f1,f2)

#---------------------------------------------------主程式的參數，影響thread內def的參數----------------------------------------

import time
import threading

def print_job():
    for i in range (10):
        print (var1)
        time.sleep (1)

var1="max"
thread1=threading.Thread(target=print_job)
thread1.start()

z=0
while z==0:
    var1= input("input: ",)

#---------------------------------------------------新的搜尋路徑----------------------------------------

import sys
system.path.append("module") #輸入資料夾名稱

https://www.youtube.com/watch?v=Et0DjY2cGiE&list=PL-g0fdC5RMboYEyt6QS2iLb_1m7QcgfHk&index=11


#---------------------------------------------------list 小練習----------------------------------------
list= [10,13,55,94,2313,121]
counter =0

for i in list :
    if i%2 ==1:
        print (i)
        counter+=1
print (counter)
"""
for i in list:
    counter+=i%2
print (counter)
"""

#---------------------------------------------------網頁爬蟲----------------------------------------

import urllib.request as req
url="https://www.ptt.cc/man/movie/index.html"

request=req.Request(url,headers={"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
})
#輸入瀏覽器資訊，模擬使用者，路徑: 網頁=>F12=>Network => index.html =>header => user-agent

with req.urlopen(request) as response:
    data= response.read().decode("utf-8")
#print (data)

import bs4 #要記得先pip install beautifulsoup4
root=bs4.BeautifulSoup(data,"html.parser")
#print (root.title.string) 
titles=root.find_all("div",class_="title") # 要去網頁原始碼內確認是被包在<div class="title"> 裡面
#print(titles.a.string)
for title in titles:
    print (title.a.string) # 要去網頁原始碼內看被包在<a href="/man/movie/M.1237999275.A.6F7.html">   ╭═════════════  關於本版  ╗</a>


#---------------------------------------------------json file寫成excel----------------------------------------
import csv

# 获取ｊｓｏｎ数据
import json

with open('test.json', 'r') as f:
    rows = json.load(f)

# 创建文件对象
 #csvfile = open(path+'.csv', 'w')#此处这样写会导致写出来的文件会有空行
f = open('data.csv', 'w',newline='')

# 通过文件创建csv对象
csv_write = csv.writer(f)

# writerow: 按行写入，　writerows: 是批量写入
# 写入数据 取列表的第一行字典，用字典的ｋｅｙ值做为头行数据
csv_write.writerow(rows[0].keys())

# 循环里面的字典，将value作为数据写入进去
for row in rows:
    csv_write.writerow(row.values())

# 关闭打开的文件
f.close()


#---------------------------------------------------用class 寫多個threading (平行續)----------------------------------------
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
         

   
def test():  
    thread1 = timer(1, 1)  
    thread2 = timer(2, 2)  
    thread1.start()  
    thread2.start()  
    time.sleep(5)  
    thread1.stop()  
    thread2.stop()  
    return  
   
if __name__ == '__main__':  
    test()  

#---------------------------------------------------return_文字可以直接相乘----------------------------------------
def repeat_stuff(stuff,num_repeats):
  return stuff*num_repeats
print(repeat_stuff("Row",3))

def test (a,b):
    c=a+1
    d=b+1
    return c,d
print (test(1,2))
c2,d2= test(1,2)
print (c2)


#---------------------------------------------------找尋字串的第一個----------------------------------------
a="123456"
print (a[0]) #該string第1個字
print (len(a)) #該字串長度


#---------------------------------------------------串列綜合表達式----------------------------------------
heights = [161, 164, 156, 144, 158, 170, 163, 163, 157]

can_ride_coaster = [i for i in heights if i > 161] #串列綜合表達式
print(can_ride_coaster)

#拆解後為
can_ride_coaster =[]
for i in heights:
    if i >161:
        can_ride_coaster.append(i)

#進階
x = [i+j for i in range(10) for j in range(10) if i % 2 == j % 3]
#拆解後為
x = []
for i in range(10):
    for j in range(10):
    if i % 2 == j % 3:
        x.append(i+j)


#---------------------------------------------------小測試，讓list倒敘----------------------------------------
#方法一
lst=[1,2,3,4,5]
for i in range(len(lst)):
    lst=lst[:i]+lst[-1:]+lst[i:(len(lst)-1)]
print (lst)

#方法二
temp=[]
for i in range (len(lst)):
    temp.append(lst[-1])
    lst.pop()
lst=temp
print (lst)


#---------------------------------------------------動態變數----------------------------------------
for i in range(5):
    locals()['abc%s'%i]=i
    print (locals()['abc%s'%i])

#locals 也改成globals
#創造多個list的function
def lst_function(parameter):
    globals()['dic%s'%parameter]=[]

lst_function(1)
print (lst1.append("123"))
lst_function(2)
print (lst2.append("456"))
#---------------------------------------------------兩個list 結合成dictionary字典----------------------------------------
songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
playcounts = [78, 29, 44, 21, 89, 5]

plays = {song:playcount for [song, playcount] in zip(songs, playcounts)}
plays["Respect"] = 94
plays.update({"123":123,"456":456})
print (plays)
print(plays["Respect"])
plays.get("Respect","No Value")# 如果沒有這把key則回應 "No Value"
plays.pop("Respect","Value") # 刪掉該key，若沒有則回應 "No Value"，同時若用print，可以知道該值=Respect 這把key的value


#呼叫所有的key
user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}

print(user_ids.keys())
print (type(user_ids.keys()))
print (list (user_ids))
print (type(list(user_ids)))
print (user_ids.values())

#把所有keys逐一叫出
for i in user_ids.keys()
    print (i)

#把所有values逐一叫出
for i in user_ids.values()
    print (i)

#print keys + values
biggest_brands = {"Apple": 184, "Google": 141.7, "Microsoft": 80, "Coca-Cola": 69.7, "Amazon": 64.8}

for company, value in biggest_brands.items():
    print(company + " has a value of " + str(value) + " billion dollars. ")


#比values值大小，並選出最大的
def max_key(my_dictionary):
  largest_key = float("-inf")
  largest_value = float("-inf")
  for key, value in my_dictionary.items():
    if value > largest_value:
      largest_value = value
      largest_key = key
  return largest_key
print(max_key({1:100, 2:1, 3:4, 4:10}))



#---------------------------------------------------multiple Thread 搭配動態變數----------------------------------------
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
    thread1.setDaemon(True)
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

#---------------------------------------------------for i in dictionary 確認dictionary內的key or value方法----------------------------------------
#確認key
def frequency_dictionary(words):
  freqs = {}
  for word in words:
    if word not in freqs:
    	freqs[word] = 0
    freqs[word] += 1
  return freqs

# Uncomment these function calls to test your  function:
print(frequency_dictionary(["apple", "apple", "cat", 1]))
# should print {"apple":2, "cat":1, 1:1}

#確認value方法
def unique_values(my_dictionary):
  temp={}
  for i in my_dictionary.values():
    if i not in temp:
      temp[i]=0
    temp[i]+=1
  return len(temp)
#print(unique_values({0:3, 1:1, 4:1, 5:3}))
# should print 2


#07/26