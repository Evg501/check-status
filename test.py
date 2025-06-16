from main import *

uri='ya.ru'

try:
    #time.sleep(1)
    #r = requests.head(uri, timeout=5)
    #r = requests.head(uri, headers=headers, timeout=5, allow_redirects=True)
    #print(uri + "  " + str(r.status_code))
    #print(socket.gethostbyname('your-hostname.com'))
    #host = get_host_from_url(uri)
    #print(host, socket.gethostbyname(host))
    #print(uri, host, socket.gethostbyname(host), str(r.status_code))
    check_url(uri)
#except requests.ConnectionError:
#    print(uri + "  " +  "failed to connect")
except Exception as e:
    print(uri , e)
    