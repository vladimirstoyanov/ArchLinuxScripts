from os import path
from Spider import Spider
from StorageUniqueData import UniqueData

class StorageData:
    def __init__ (self):
        self.name = "EmailAddresses"
        self.uniqueData = UniqueData("output" + self.name)
        self.lengthOfEmailData = 3

    def __toupleToEmailAddress (self, data):
        return data[0] + '@' + data[1] + '.' + data[2]

    def __convertToupleToList (self, data):
        resultList = []
        for i in range (len (data)):
            if (len(data[i])!=self.lengthOfEmailData):
                continue
            resultList.append(self.__toupleToEmailAddress(data[i]))
        return resultList

    def saveData (self, data):
        resultList = self.__convertToupleToList (data)
        self.uniqueData.saveData(resultList)



storageData = StorageData ()
spider = Spider ("https://github.com", "(\w+)\@(\w+)\.(\w+)", storageData)
spider.runSpider()
