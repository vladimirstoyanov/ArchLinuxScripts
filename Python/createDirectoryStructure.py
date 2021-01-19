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
        self.prepare()

    def prepare (self):
        for i in range (len(self.listFiles)):
                self.listFiles[i].shortDirectoryName = self.rootDirectory + self.fileManager.returnPathAfterDirectory(
                            self.listFiles[i].fullpath,
                            self.directoryName)

    def buildStrucure (self):
        for i in range (len(self.listFiles)):
            splitedPath = self.fileManager.splitPath(self.listFiles[i].shortDirectoryName)
            self.__buildStructure(splitedPath, 0, self.directoryStructure)

    def __buildStructure(self, listFullpath, indexFullPath, currentDirectory):
        #print("===listFullPath: " + str(listFullpath))
        #print ("index: " + str(indexFullPath))
        if (self.directoryStructure == ""):
            #print ("if (self.directoryStructure == ""):")
            self.directoryStructure = Directory()
            self.directoryStructure.dirname = listFullpath[indexFullPath]
            #print ("Adding " +  listFullpath[indexFullPath] + " as root")
            self.__buildStructure(listFullpath, indexFullPath+1, self.directoryStructure)
            return

        if (indexFullPath == 0):
            self.__buildStructure(listFullpath, indexFullPath+1, self.directoryStructure)
            return

        if (indexFullPath == (len(listFullpath) - 1)):
            #print ("Appending file: " + str(listFullpath[indexFullPath]) + " to directory: " + currentDirectory.dirname )
            currentDirectory.listFiles.append(listFullpath[indexFullPath])
            return

        found = 0
        for i in range(len(currentDirectory.listDirectories)):
            #print ("Comparing: " + listFullpath[indexFullPath] + " and " + currentDirectory.listDirectories[i].dirname)
            if (listFullpath[indexFullPath] == currentDirectory.listDirectories[i].dirname):
                #print ("Direcotry exist.")
                self.__buildStructure(listFullpath,
                    indexFullPath+1,
                    currentDirectory.listDirectories[i])
                found =1

        if (found == 0):
            #print("Directory doesn't exist. Adding " +listFullpath[indexFullPath])
            newDirectory = Directory()
            newDirectory.dirname = listFullpath[indexFullPath]
            currentDirectory.listDirectories.append (newDirectory)
            self.__buildStructure(listFullpath, indexFullPath+1, newDirectory)

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

    def generateStructureFile (self):
        f = open(self.directoryName + '__init__.py', 'w')
        self.__generateStructureFile(self.directoryStructure, 0, f)
        f.close()


commandLineInput = CommandLineInput ()
commandLineInput.checkInput()

directoryName = sys.argv[1]
directoryStructure = DirectoryStructure(directoryName)
directoryStructure.buildStrucure()
directoryStructure.generateStructureFile()
