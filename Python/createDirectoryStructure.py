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

class Directory:
    def __init__ (self):
        self.dirname = ""
        self.fullpath = ""
        self.listFiles = []
        self.listDirectories = []

class File:
    def __init__ (self):
        self.filename = ""
        self.fullpath = ""
        self.directory = ""
        self.shortDirectoryName = ""
    def __repr__(self): #string representation when print it
        return str(self.filename + '\n' + self.fullpath + '\n' + self.directory  + '\n' + self.shortDirectoryName +'\n')

class FileManager:
    def __init__ (self):
        pass

    def isDirectoryExist (self, directoryName):
        return os.path.isdir(directoryName)

    def isFileExist (self, fileName):
        return os.path.isfile(fileName)

    def splitPath (self, path):
        result = path.split('/')
        result = list(filter(None, result))
        return result

    def returnPathAfterDirectory (self, path, directoryName):
        return path[len(directoryName)-1:len(path)]

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

class DirectoryStructure:
    def __init__ (self, direcotryName):
        self.spaceOffset = 5
        self.directoryName = direcotryName
        self.directoryStructure = ""
        self.fileManager = FileManager()
        self.listFiles = self.fileManager.getAllFiles(directoryName, 'py')
        self.rootDirectory = self.fileManager.getParentDirectory(self.directoryName)

    def __prepare (self):
        for i in range (len(self.listFiles)):
                self.listFiles[i].shortDirectoryName = self.rootDirectory + self.fileManager.returnPathAfterDirectory(
                            self.listFiles[i].fullpath,
                            self.directoryName)

    def __getFullPath (self, listFullPath, index):
        fullPath = self.directoryName
        for i  in range (1,index+1, 1):
            fullPath += listFullPath[i]
            fullPath += '/'
        return fullPath

    def __buildStructure(self, listFullPath, indexFullPath, currentDirectory):
        if (self.directoryStructure == ""):
            self.directoryStructure = Directory()
            self.directoryStructure.dirname = listFullPath[indexFullPath]
            self.directoryStructure.fullpath = self.__getFullPath(listFullPath, indexFullPath)

            self.__buildStructure(listFullPath, indexFullPath+1, self.directoryStructure)
            return

        if (indexFullPath == 0):
            self.__buildStructure(listFullPath, indexFullPath+1, self.directoryStructure)
            return

        if (indexFullPath == (len(listFullPath) - 1)):
            currentDirectory.listFiles.append(listFullPath[indexFullPath])
            return

        found = 0
        for i in range(len(currentDirectory.listDirectories)):
            if (listFullPath[indexFullPath] == currentDirectory.listDirectories[i].dirname):
                self.__buildStructure(listFullPath,
                    indexFullPath+1,
                    currentDirectory.listDirectories[i])
                found =1

        if (found == 0):
            newDirectory = Directory()
            newDirectory.dirname = listFullPath[indexFullPath]
            newDirectory.fullpath = self.__getFullPath(listFullPath, indexFullPath)
            currentDirectory.listDirectories.append (newDirectory)
            self.__buildStructure(listFullPath, indexFullPath+1, newDirectory)

    def __generateStructureFile (self, currentDirectory, offsetLevel, f):
        spaceOffset = (' ' * offsetLevel)
        f.write(spaceOffset + currentDirectory.dirname + '/\n')
        spaceOffset += (' ' * offsetLevel)
        if (spaceOffset == ''):
            spaceOffset = ' ' * self.spaceOffset
        for i in range (len(currentDirectory.listFiles)):
            f.write(spaceOffset + currentDirectory.listFiles[i] + '\n')

        for i in range (len(currentDirectory.listDirectories)):
            self.__generateStructureFile(currentDirectory.listDirectories[i], offsetLevel+self.spaceOffset, f)

        if (offsetLevel!=0):
            f.write(spaceOffset + '...\n')


    def __createInitFiles (self, currentDirectory):
        found = 0
        initFileName = "__init__.py"
        for i in range (len(currentDirectory.listFiles)):
            if (initFileName == currentDirectory.listFiles[i]):
                found = 1
                break

        #create an empty __init__.py
        if (found==0):
            f=open(currentDirectory.fullpath + initFileName, 'w')
            f.close()
            currentDirectory.listFiles.append(initFileName)

        for i in range (len(currentDirectory.listDirectories)):
            self.__createInitFiles(currentDirectory.listDirectories[i])


    def generate (self):
        self.__prepare()
        for i in range (len(self.listFiles)):
                splitedPath = self.fileManager.splitPath(self.listFiles[i].shortDirectoryName)
                self.__buildStructure(splitedPath, 0, self.directoryStructure)

        self.__createInitFiles(self.directoryStructure)

        f = open(self.directoryName + '__init__.py', 'w')
        self.__generateStructureFile(self.directoryStructure, 0, f)
        f.close()

commandLineInput = CommandLineInput ()
commandLineInput.checkInput()

directoryName = sys.argv[1]
directoryStructure = DirectoryStructure(directoryName)
directoryStructure.generate()
