from os import path
from Spider import Spider
from StorageUniqueData import UniqueData

class StorageData:
    def __init__ (self):
        self.name = "Words"
        self.uniqueData = UniqueData(self.name)

    def saveData (self, data):
        self.uniqueData.saveData(data)

storageData = StorageData ()
spider = Spider ("https://en.wikipedia.org/wiki/Main_Page", "(\w+)", storageData)
spider.runSpider()
