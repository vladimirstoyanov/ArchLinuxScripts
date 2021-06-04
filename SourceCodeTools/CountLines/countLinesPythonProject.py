import countLines

class CountLinesPythonProject:
    def __init__ (self):
        self.__countLines = countLines.CountLines ()
        self.__countLines.countLines (['py'])
        print ("Lines: " + str(self.__countLines.getCount()))

if __name__ == "__main__":
    countLinesPythonProject = CountLinesPythonProject()
