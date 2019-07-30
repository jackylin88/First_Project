import os
import time
from datetime import datetime
def check_ping(x):
    hostname = x
    response = os.system("ping -w 1 -n 1 " + hostname)
    # and then check the response...
    return response
    # if response == 0:
    #     pingstatus = "Network Active"
    # else:
    #     pingstatus = "Network Error"
    # return pingstatus



for x in range(6):
    pingstatus = check_ping("10.7.5.7")
    print(pingstatus)
    if pingstatus == 0:
        print("yes")
        print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    else:
        pass
    time.sleep(3)