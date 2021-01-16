from os import path
from Spider import Spider
from StorageData import Data

class StorageData:
    def __init__ (self):
        self.name = "Words"
        self.uniqueData = Data(self.name)

    def saveData (self, data):
        self.uniqueData.saveData(data)

storageData = StorageData ()
spider = Spider ("https://en.wikipedia.org/wiki/Main_Page", "(\w+)", storageData)
spider.runSpider()
