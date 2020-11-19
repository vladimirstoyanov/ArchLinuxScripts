from os import path
from Spider import Spider

class StorageData:
    def __init__ (self):
        self.outputFilename = "output"
        self.data = set()
        self.loadData()
        
    def loadData (self):
        if (path.exists(self.outputFilename) == 0):
            return
        
        f = open (self.outputFilename, 'r')
        
        for string in f.readlines():
            string = string.replace('\n', '')
            string = string.replace('\r', '')
            self.data.add (string)
        
        
    def saveData (self, data):
        f = open (self.outputFilename, 'a')
        for i in range (len (data)):
            if data[i] in self.data:
                continue
            f.write(data[i] + '\n')
            self.data.add(data[i])
        f.close()


storageData = StorageData ()
spider = Spider ("https://en.wikipedia.org/wiki/Main_Page", "(\w+)")
spider.subscribe(storageData)
spider.runSpider()
