
import requests
import time
import os
from config_hidden import *
import time
import socket
from urllib.parse import urlparse

def get_host_from_url(url):
    parsed_url = urlparse(url)
    host = parsed_url.hostname  # Или netloc для получения хоста и порта (если указано)
    return host

#SLIST = [ ]
#SLIST = [ "http://ya.ru", 
#        "http://google.com", 
#         ]

SLEEP = 60

headers = {
    'User-Agent': 'Mozilla/5.0'
}

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def check_url(uri):
    r = requests.head(uri, headers=headers, timeout=5, allow_redirects=True)
    host = get_host_from_url(uri)
    print(uri, host, socket.gethostbyname(host), str(r.status_code))
    return host, socket.gethostbyname(host), str(r.status_code)

while True:
    for uri in SLIST:
        try:
            check_url(uri)
        except Exception as e:
            print(uri , e)
    break
    time.sleep(SLEEP)
    cls()
    
print("скрипт завершён")
text = input("")