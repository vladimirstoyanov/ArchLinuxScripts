from os import path
from Spider import Spider
from StorageData import Data

class StorageData:
    def __init__ (self):
        self.__name = "Words"
        self.__uniqueData = Data(self.__name)

    def saveData (self, data):
        self.__uniqueData.saveData(data)

storageData = StorageData ()
spider = Spider ("https://en.wikipedia.org/wiki/Main_Page", "(\w+)", storageData)
spider.runSpider()
