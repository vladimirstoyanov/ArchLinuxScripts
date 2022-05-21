import countLines

class CountLinesArchLinuxScripts:
    def __init__ (self):
        self.__countLines = countLines.CountLines ()
        self.__countLines.countLines (['py', 'sh', 'cpp', 'C', 'hpp','h'])
        print ("Lines: " + str(self.__countLines.getCount()))

if __name__ == "__main__":
    countLinesArchLinuxScripts = CountLinesArchLinuxScripts()
