import urllib.request as urllib2
import re
import time
from bs4 import BeautifulSoup
from os import path

class Web:
    def __init__ (self):
        pass

    def download (self, url):
        mystr = ""
        try:
            conn = urllib2.urlopen(url)
            mystr = conn.read().decode('utf-8')
        except:
            print ("Could not download url: " + str(url))

        return mystr


class StorageURLs:
    def __init__ (self, name):
        self.urlStorageFilename = "urls" + name
        self.unusedUrlsFilename = "unused_urls" + name

    def addUnusedUls (self, unusedUrls):
        f = open (self.unusedUrlsFilename, 'w')

        for i in range (len(unusedUrls)):
            f.write (unusedUrls[i] + '\n')

        f.close()

    def add (self, url):
        f = open (self.urlStorageFilename, 'a')
        f.write (url + '\n')
        f.close()

    def loadUsedURLs (self):
        if (path.exists(self.urlStorageFilename) == 0):
            return set() #return an empty Set object

        f = open (self.urlStorageFilename, 'r')
        setStructure = set()
        for string in f.readlines ():
            string = string.replace('\n','')
            string = string.replace('\r','')
            setStructure.add (string)
        f.close()
        return setStructure

    def loadUnusedURLs (self):
        if (path.exists(self.unusedUrlsFilename) == 0):
            return [] #return an empty Set object

        f = open (self.unusedUrlsFilename, 'r')

        unused = []
        for string in f.readlines ():
            string = string.replace('\n','')
            string = string.replace('\r','')
            unused.append (string)
        f.close()

        return unused

class Storage:
    def __init__ (self, subscriberClass):
        self.storageURLsObj = StorageURLs (subscriberClass.name)
        self.ramURLs = self.storageURLsObj.loadUsedURLs()
        self.ramQueue = self.storageURLsObj.loadUnusedURLs ()
        self.subscribedClass = subscriberClass

    def addList (self, listElements):
        for i in range (len(listElements)):
            self.add(listElements[i])
        self.storageURLsObj.addUnusedUls (self.ramQueue)

    def add (self, element):
        if (element == ""):
            return

        if element in self.ramURLs:
            return

        self.ramURLs.add (element)
        self.ramQueue.append(element)
        self.storageURLsObj.add (element)

    def nextURL (self):
        if (self.isEmpty ()):
            return ""
        return self.ramQueue.pop(0)

    def isEmpty (self):
        return len(self.ramQueue) == 0

    def saveData (self, data):
        self.subscribedClass.saveData(data)

class Parser:
    def __init__ (self, pattern):
        self.pattern = pattern

    def parse (self, htmlSource):
        return re.findall(self.pattern, htmlSource)

    def getURLs (self, url, htmlSource):
        soup = BeautifulSoup(htmlSource)
        links = soup.find_all('a')

        result = []
        for tag in links:
            link = tag.get('href',None)
            if link is not None:
                if (len(link)>0):
                    if (link[0] == '/' or link[0] == '#'):
                        link = url + link
                    result.append(link)

        return result

class Spider:
    def __init__ (self, url, pattern, subscriberClass):
        self.url = url
        self.storage = Storage(subscriberClass)
        self.storage.add (url)
        self.web = Web()
        self.parser = Parser (pattern)

    def runSpider (self):
        while (self.storage.isEmpty() == False):
            url = self.storage.nextURL ()
            print ("===Trying to download: " + url)
            htmlSource = self.web.download(url)
            parsedData = self.parser.parse(htmlSource)
            self.storage.saveData(parsedData)
            listUrls = self.parser.getURLs (url, htmlSource)
            self.storage.addList(listUrls)
