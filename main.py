
import requests
import time
import os
from config_hidden import *
import time
import socket
from urllib.parse import urlparse
from rich import print

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
    #print(uri, host, socket.gethostbyname(host), str(r.status_code))
    if r.status_code==200:
        fmt_sc = '[green]'
    else:
        fmt_sc = '[red]'
    #print(format_c(text=uri, format='7;30;46'), format_c(text=host, format='7;30;45'), format_c(text=socket.gethostbyname(host), format='7;30;44'), format_c(text=str(r.status_code), format=fmt_sc)) 
    print('[deep_pink4]'+uri, '[blue]'+host, '[dark_orange3]'+socket.gethostbyname(host), fmt_sc+ str(r.status_code))
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