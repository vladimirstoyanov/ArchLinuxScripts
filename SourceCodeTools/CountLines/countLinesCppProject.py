import countLines

class CountLinesCppProject:
    def __init__ (self):
        self.__countLines = countLines.CountLines ()
        self.__countLines.countLines (['hpp','h','C','cpp'])
        print ("Lines: " + str(self.__countLines.getCount()))

if __name__ == "__main__":
    countLinesCppProject = CountLinesCppProject()
