import os
from urllib import request as urlrequest


def getRequest (url):
    req = urlrequest.Request(url)
    response = urlrequest.urlopen(req)
    print (response.read())

getRequest ('https://seekingalpha.com/article/4432862-tesla-the-only-2-numbers-that-matter-to-investors')
