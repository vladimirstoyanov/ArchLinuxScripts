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
    def __repr__(self):
        return str(self.filename + '\n' + self.fullpath + '\n' + self.directory  + '\n')

class FileManager:
    def __init__ (self):
        pass
    def isDirectoryExist (self, directoryName):
        return os.path.isdir(directoryName)

    def isFileExist (self, fileName):
        return os.path.isfile(fileName)

    def getChildDirectoryByParentOne (self, parentDirectory):
        pass

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
        self.files = fileManager.getAllFiles ()
    def generate (self):
        f = open (self.directory + '__init__.py', 'w')
        f.close ()


commandLineInput = CommandLineInput ()
commandLineInput.checkInput()

directoryName = sys.argv[1]
fileManager = FileManager ()
files = fileManager.getAllFiles(directoryName, "py")
