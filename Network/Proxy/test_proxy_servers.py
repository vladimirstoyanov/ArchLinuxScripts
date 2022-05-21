import os
from urllib import request as urlrequest

listProxies = [
    ['http', '103.110.47.51', '8080']
]

def checkProxy (protocol, ip, port):
    proxy_host = ip + ":" + port
    url = 'http://rss.slashdot.org/Slashdot/slashdotMain'
    req = urlrequest.Request(url)
    req.set_proxy(proxy_host, protocol)
    response = urlrequest.urlopen(req)

for i in range (len (listProxies)):
    checkProxy(listProxies[i][0], listProxies[i][1], listProxies[i][2])
