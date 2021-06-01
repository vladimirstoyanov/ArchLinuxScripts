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
        self.__urlStorageFilename = "urls" + name
        self.__unusedUrlsFilename = "unused_urls" + name

    def addUnusedUls (self, unusedUrls):
        f = open (self.__unusedUrlsFilename, 'w')

        for i in range (len(unusedUrls)):
            f.write (unusedUrls[i] + '\n')

        f.close()

    def add (self, url):
        f = open (self.__urlStorageFilename, 'a')
        f.write (url + '\n')
        f.close()

    def loadUsedURLs (self):
        if (path.exists(self.__urlStorageFilename) == 0):
            return set() #return an empty Set object

        f = open (self.__urlStorageFilename, 'r')
        setStructure = set()
        for string in f.readlines ():
            string = string.replace('\n','')
            string = string.replace('\r','')
            setStructure.add (string)
        f.close()
        return setStructure

    def loadUnusedURLs (self):
        if (path.exists(self.__unusedUrlsFilename) == 0):
            return [] #return an empty Set object

        f = open (self.__unusedUrlsFilename, 'r')

        unused = []
        for string in f.readlines ():
            string = string.replace('\n','')
            string = string.replace('\r','')
            unused.append (string)
        f.close()

        return unused

class Storage:
    def __init__ (self, subscriberClass):
        self.__storageURLsObj = StorageURLs (subscriberClass.name)
        self.__ramURLs = self.__storageURLsObj.loadUsedURLs()
        self.__ramQueue = self.__storageURLsObj.loadUnusedURLs ()
        self.__subscribedClass = subscriberClass

    def addList (self, listElements):
        for i in range (len(listElements)):
            self.add(listElements[i])
        self.__storageURLsObj.addUnusedUls (self.__ramQueue)

    def add (self, element):
        if (element == ""):
            return

        if element in self.__ramURLs:
            return

        self.__ramURLs.add (element)
        self.__ramQueue.append(element)
        self.__storageURLsObj.add (element)

    def nextURL (self):
        if (self.isEmpty ()):
            return ""
        return self.__ramQueue.pop(0)

    def isEmpty (self):
        return len(self.__ramQueue) == 0

    def saveData (self, data):
        self.__subscribedClass.saveData(data)

class Parser:
    def __init__ (self, pattern):
        self.__pattern = pattern

    def parse (self, htmlSource):
        return re.findall(self.__pattern, htmlSource)

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
        self.__url = url
        self.__storage = Storage(subscriberClass)
        self.__storage.add (url)
        self.__web = Web()
        self.__parser = Parser (pattern)

    def runSpider (self):
        while (self.__storage.isEmpty() == False):
            url = self.__storage.nextURL ()
            print ("===Trying to download: " + url)
            htmlSource = self.__web.download(url)
            parsedData = self.__parser.parse(htmlSource)
            self.__storage.saveData(parsedData)
            listUrls = self.__parser.getURLs (url, htmlSource)
            self.__storage.addList(listUrls)
