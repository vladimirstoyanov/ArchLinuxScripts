from os import path

class Data:
    def __init__ (self, outputFilename):
        self.__outputFilename = "output" + outputFilename
        self.__data = []
        self.loadData()

    def loadData (self):
        if (path.exists(self.__outputFilename) == 0):
            return

        f = open (self.__outputFilename, 'r')

        for string in f.readlines():
            string = string.replace('\n', '')
            string = string.replace('\r', '')
            self.__data.append (string)


    def saveData (self, data):
            f = open (self.__outputFilename, 'a')

            for i in range (len (data)):
                f.write(data[i] + '\n')
                self.__data.append(data[i])
            f.close()

    def getData (self):
            return self.__data
