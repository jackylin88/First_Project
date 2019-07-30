import requests
import json
import csv

z=0
while z==0:
    IP=input("WISE IP (Ex.192.168.1.1): ",)
    FILE=input("WISE system log filename (Ex. WISE-4060@192.168.1.1): ",)
    r = requests.get(str('http://'+IP+'/logsys_output'), auth=('root', '00000000'))
    print(r.status_code, r.reason)
    r = requests.post(str('http://'+IP+'/logsys_output'), auth=('root', '00000000'), json={"Fltr":0,"UID":1,"MAC":0,"TmF":1})
    print(r.status_code, r.reason)
    r = requests.get(str('http://'+IP+'/logsys_message'), auth=('root', '00000000'))
    print(r.status_code, r.reason)
    j = json.loads(r.text)
    jj = j["LogMsg"]
    #s = json.dumps(jj)
    #text_file = open(FILE+".json","w")
    text_file = open(FILE+'.csv', 'w',newline='')
    csv_write = csv.writer(text_file)
    csv_write.writerow(jj[0].keys())
    for row in jj:
            csv_write.writerow(row.values())
    #text_file.write(s)
    text_file.close()
"""
    with open(FILE+".json", 'r') as f:
        rows = json.load(f)

    # 创建文件对象
        #csvfile = open(path+'.csv', 'w')#此处这样写会导致写出来的文件会有空行
    f = open(FILE+'.csv', 'w',newline='')

    # 通过文件创建csv对象
    csv_write = csv.writer(f)

    # writerow: 按行写入，　writerows: 是批量写入
    # 写入数据 取列表的第一行字典，用字典的ｋｅｙ值做为头行数据
    csv_write.writerow(rows[0].keys())

    # 循环里面的字典，将value作为数据写入进去
    for row in rows:
            csv_write.writerow(row.values())

    f.close()
"""

