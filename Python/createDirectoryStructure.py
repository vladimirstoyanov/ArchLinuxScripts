import os
import sys
import fnmatch
import time
from pathlib import Path

class CommandLineInput:
    def __init__ (self):
        pass

    def checkInput (self):
        if (len (sys.argv)!=2):
            print ("Wrong input:")
            print ("1 arg: directory name")
            sys.exit()

class File:
    def __init__ (self):
        self.filename = ""
        self.fullpath = ""
        self.directory = ""
        self.shotDirectoryName = ""
    def __repr__(self): #string representation when print it
        return str(self.filename + '\n' + self.fullpath + '\n' + self.directory  + '\n' + self.shotDirectoryName +'\n')

class FileManager:
    def __init__ (self):
        pass

    def isDirectoryExist (self, directoryName):
        return os.path.isdir(directoryName)

    def isFileExist (self, fileName):
        return os.path.isfile(fileName)

    def splitPath (self, path):
        return path.split('/')

    def returnPathAfterDirectory (self, path, directoryName):
        return path[len(directoryName):len(path)]

    def getParentDirectory (self, path):
        splitedPath = self.splitPath(path)
        splitedPath = list(filter(None, splitedPath))
        return splitedPath[len(splitedPath)-1]

    def getAllFiles (self, dir, extension ):
        result = []
        for root, dirnames, filenames in os.walk(dir):
            for filename in fnmatch.filter(filenames, '*.' + extension):
                file = File ()
                file.filename = filename
                file.directory = root
                file.fullpath = os.path.join(root, filename)
                result.append(file)
        return result



class PythonDirectoryStructure:
    def __init__ (self, directory):
        self.directory = directory
        self.fileManager = FileManager()
        self.files = self.fileManager.getAllFiles (directory, 'py')
        self.files.sort(key=lambda x: x.directory, reverse=False)
        self.parentDirectory = self.fileManager.getParentDirectory(self.directory)

    def prepare (self):
        for i in range (len(self.files)):
            self.files[i].shotDirectoryName = self.fileManager.returnPathAfterDirectory(
                self.files[i].directory,
                self.directory)
            if (self.files[i].shotDirectoryName!=""):
                self.files[i].shotDirectoryName += '/'

    def generate (self):
        f = open (self.directory + '__init__.py', 'w')
        self.prepare()
        directories = []
        f.write(self.parentDirectory + '/' + '\n')
        spaces = "     "
        currentDirectory=self.directory

        for i in range (len (self.files)):
            if (((self.files[i].shotDirectoryName in directories) == False) and self.files[i].shotDirectoryName!=''):
                if (currentDirectory!=self.directory):
                    f.write(spaces + '...\n')
                spaces = spaces[0:5]
                directories.append(self.files[i].shotDirectoryName)
                currentDirectory = self.files[i].directory
                f.write(spaces+self.files[i].shotDirectoryName + '\n')
                spaces+="     "
            f.write(spaces + self.files[i].filename + '\n')

        if (currentDirectory!=self.directory):
            f.write(spaces + '...\n')
        f.close()

commandLineInput = CommandLineInput ()
commandLineInput.checkInput()

directoryName = sys.argv[1]
pythonDirectoryStructure = PythonDirectoryStructure (directoryName)
pythonDirectoryStructure.generate()
