import sys
sys.path.insert(1, '../Python/DirectoryStructure')
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
        commandLine = CommandLineInput ()
        self.directory = sys.argv[1]
        fileManager = FileManager.FileManager ()
        self.count = 0
        self.countLines(fileManager.getAllFiles(self.directory, 'hpp'))
        self.countLines(fileManager.getAllFiles(self.directory, 'h'))
        self.countLines(fileManager.getAllFiles(self.directory, 'cpp'))
        self.countLines(fileManager.getAllFiles(self.directory, 'C'))
        print ("Lines: " + str(self.count))

    def countLines (self, files):
        for i in range (len (files)):
            print ("Trying to open " + files[i].fullpath)
            f = open (files[i].fullpath, 'r')
            for line in f.readlines ():
                self.count+=1
            f.close()

if __name__ == "__main__":
    countLines = CountLines ()
