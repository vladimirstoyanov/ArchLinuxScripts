from os import path

class UniqueData:
    def __init__ (self, outputFilename):
        self.outputFilename = "output" + outputFilename
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

    def getData (self):
            return self.data
