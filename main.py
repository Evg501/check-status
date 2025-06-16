
import requests
import time
import os
from config_hidden import *

#SLIST = [ ]
#SLIST = [ "http://ya.ru", 
#        "http://google.com", 
#         ]

SLEEP = 60

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

while True:
    for uri in SLIST:
        try:
            r = requests.head(uri, timeout=5)
            print(uri + "  " + str(r.status_code))
        #except requests.ConnectionError:
        #    print(uri + "  " +  "failed to connect")
        except Exception as e:
            print(uri , e)
    break
    time.sleep(SLEEP)
    cls()
print("скрипт завершён")
text = input("")