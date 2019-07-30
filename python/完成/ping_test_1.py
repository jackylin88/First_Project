import subprocess
def ping_Test():
    Ip_list=['8.8.8.8','192.168.1.133']
    for ip in Ip_list:
        try:
            ret1=subprocess.check_output(["ping",ip])
            ret1 = ret1.decode('big5')
            if ret1.find('TTL=')>-1:
                print(ip+":連線成功")
        except:
            if ret1.find('要求等候逾時')>-1:
                print(ip+":連線失敗")
            else:
                print("Fail!")
            pass

ping_Test()
print('Hello')