import sys
sys.path.insert(1, '../../Python/DirectoryStructure')
import FileManager


class CommandLineInput:
    def __init__ (self):
        self.checkInput()

    def checkInput (self):
        if (len (sys.argv)!=2):
            print ("Wrong input:")
            print ("1 arg: directory name")
            sys.exit()

class CountLines:
    def __init__ (self):
        self.__commandLine = CommandLineInput ()
        self.__directory = sys.argv[1]
        self.__fileManager = FileManager.FileManager ()
        self.__count = 0

    def getCount (self):
        return self.__count

    def countLines (self, fileExtensions):
        for i in range (len (fileExtensions)):
            self.__countLines(self.__fileManager.getAllFiles(self.__directory, fileExtensions[i]))

    def __countLines (self, files):
        for i in range (len (files)):
            print ("Trying to open " + files[i].fullpath)
            f = open (files[i].fullpath, 'r')
            for line in f.readlines ():
                self.__count+=1
            f.close()
