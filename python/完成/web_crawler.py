# 網頁爬蟲
#---------------------------------------------Method 1: 直接使用內建urlib.request，搭配bs4 分析context-------------------------------------------------
# pip install requests
# pip install beautifulsoup4

import urllib.request as req
#url="http://192.168.1.1/wlassociation.asp"
url="https://www.ptt.cc/bbs/movie/index.html"

request=req.Request(url,headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"})
#輸入瀏覽器資訊，模擬使用者，路徑: 網頁=>F12=>Network => index.html =>header => user-agent

with req.urlopen(request) as response:
    data= response.read().decode("utf-8")
#print (data)

import bs4 #要記得先pip install beautifulsoup4
root=bs4.BeautifulSoup(data,"html.parser")
#print (root.title.string) 
titles=root.find(href="/bbs/movie/M.1562036136.A.FBA.html") #直接找<a href="/bbs/movie/M.1562036136.A.FBA.html">[討論] 誰最會演爸爸??</a>
print(titles.string)

"""補充
titles=root.find("div",class_="title")
print (titles.a.string)  #用來找在div class="titie"下第一個被<a>包住的字串

#若要找所有的可以用下列的程式碼，一航易行確認
titles=root.find_all("div",class_="title")
for title in titles:
        print (title.a.string)  #用來找在div class="titie"下第一個被<a>包住的字串
#https://www.youtube.com/watch?v=9Z9xKWfNo7k&list=PL-g0fdC5RMboYEyt6QS2iLb_1m7QcgfHk&index=19
"""


#---------------------------------------------Method 2: import request 模組，搭配bs4 分析context-------------------------------------------------
#Method2
import requests

url="https://www.ptt.cc/bbs/movie/index.html"

r= requests.get(url)
print (r.status_code)
data=r.text
#print (r.text)
#該方法也可以使用bs4來分析data

"""
如果有加密
username="admin"
password="admin"
r= requests.get(url,auth=(username,password))
"""


#-------------------------------------------------------練習-------------------------------------------------------------------------------------
from bs4 import BeautifulSoup

html_doc = """
<html>
    <head>
        <title>Hello World</title>
    </head>
    <body>
        <h2>Test Header</h2>
    <p>This is a test.</p>
    <a id="link1" href="/my_link1">Link 1</a>
    <a id="link2" href="/my_link2">Link 2</a>
    <p>Hello, 
        <b class="boldtext">Bold Text</b>
    <a>testing</a>
    <div>123</div>
    <div>456</div>
    <div>789</div>
    </p>
    </body>
</html>
"""
soup=BeautifulSoup(html_doc,'html.parser')
#data=soup.title
#data=soup.find_all("body") #會把找到符合條件的都放在一個list內
#data=soup.find("body") #找到第一個符合條件的直接顯示
data=soup.find("a")
print(data.string)
data2=data.find_next_siblings("a") #找出來後會放到list內
print(data2[0].string)
print(data2[0].string)


"""
#---------------------------find & find_all-------------------
用法 data.find("標籤",屬性="屬性內容") #note若屬性是class要改成class_，因為class字元在python中已經是特殊自元
Ex. data=soup.find_all("a",id="link1")

#-----------------------------取出string---------
data=soup.find("body")
print(data.a.string) # 找第一個符合條件內的Tag<a>的資料，注意如果用find_all，結果會是list，list則無法做.a.string分析，需要要for迴圈將list內的content取出，才能用.a.string分析

#---------------------------搜尋多種標籤-----------
data=soup.find_all(["a","div"]) #搜尋後放在同一個list內


#------------------------------取得屬性------------
data=soup.find("a")
print(data.get("href")) 

#--------------------------向下搜尋---------------
data=soup.find("a")
print(data.string)
data2=data.find_next_siblings("a") #找出來後會放到list內
print(data2[0].string)
"""


#--------------------------------------------------------------------------------------------------------------------------------------------
#0726