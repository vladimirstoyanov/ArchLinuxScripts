import urllib

listProxies = [
    ['socks4', '109.110.73.106', '51989'],
    ['socks4', '109.110.73.106', '51989'],
    ['socks4', '91.205.146.79', '3629'],
    ['HTTP', '173.245.49.17', '80']
]

def checkProxy (protocol, ip, port):
    try:
        urllib.urlopen(
            "https://www.google.bg/",
            proxies={protocol:protocol +'://' + ip + ':' + port}
        )
    except IOError:
        print "Connection error! (Check proxy)"
    else:
        print "All was fine"

for i in range (len (listProxies)):
    checkProxy(listProxies[i][0], listProxies[i][1], listProxies[i][2])
