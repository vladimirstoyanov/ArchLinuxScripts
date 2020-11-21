from os import path

class Data:
    def __init__ (self, outputFilename):
        self.outputFilename = "output" + outputFilename
        self.data = []
        self.loadData()

    def loadData (self):
        if (path.exists(self.outputFilename) == 0):
            return

        f = open (self.outputFilename, 'r')

        for string in f.readlines():
            string = string.replace('\n', '')
            string = string.replace('\r', '')
            self.data.append (string)


    def saveData (self, data):
            f = open (self.outputFilename, 'a')

            for i in range (len (data)):
                f.write(data[i] + '\n')
                self.data.append(data[i])
            f.close()

    def getData (self):
            return self.data
