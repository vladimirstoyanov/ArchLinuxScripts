import os
import sys
import fnmatch
import time
import FileManager
import Directory
from pathlib import Path

class CommandLineInput:
    def __init__ (self):
        pass

    def checkInput (self):
        if (len (sys.argv)!=2):
            print ("Wrong input:")
            print ("1 arg: directory name")
            sys.exit()


class DirectoryStructure:
    def __init__ (self, direcotryName):
        self.__spaceOffset = 5
        self.__directoryName = direcotryName
        self.__directoryStructure = ""
        self.__fileManager = FileManager.FileManager()
        self.__listFiles = self.__fileManager.getAllFiles(directoryName, 'py')
        self.__rootDirectory = self.__fileManager.getParentDirectory(self.__directoryName)

    def __prepare (self):
        for i in range (len(self.__listFiles)):
                self.__listFiles[i].shortDirectoryName = self.__rootDirectory + self.__fileManager.returnPathAfterDirectory(
                            self.__listFiles[i].fullpath,
                            self.__directoryName)

    def __getFullPath (self, listFullPath, index):
        fullPath = self.__directoryName
        for i  in range (1,index+1, 1):
            fullPath += listFullPath[i]
            fullPath += '/'
        return fullPath

    def __buildStructure(self, listFullPath, indexFullPath, currentDirectory):
        if (self.__directoryStructure == ""):
            self.__directoryStructure = Directory.Directory()
            self.__directoryStructure.dirname = listFullPath[indexFullPath]
            self.__directoryStructure.fullpath = self.__getFullPath(listFullPath, indexFullPath)

            self.__buildStructure(listFullPath, indexFullPath+1, self.__directoryStructure)
            return

        if (indexFullPath == 0):
            self.__buildStructure(listFullPath, indexFullPath+1, self.__directoryStructure)
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
            newDirectory = Directory.Directory()
            newDirectory.dirname = listFullPath[indexFullPath]
            newDirectory.fullpath = self.__getFullPath(listFullPath, indexFullPath)
            currentDirectory.listDirectories.append (newDirectory)
            self.__buildStructure(listFullPath, indexFullPath+1, newDirectory)

    def __generateStructureFile (self, currentDirectory, offsetLevel, f):
        spaceOffset = (' ' * offsetLevel)
        f.write(spaceOffset + currentDirectory.dirname + '/\n')
        spaceOffset += (' ' * offsetLevel)
        if (spaceOffset == ''):
            spaceOffset = ' ' * self.__spaceOffset

        currentDirectory.listFiles.sort()
        for i in range (len(currentDirectory.listFiles)):
            f.write(spaceOffset + currentDirectory.listFiles[i] + '\n')

        for i in range (len(currentDirectory.listDirectories)):
            self.__generateStructureFile(currentDirectory.listDirectories[i], offsetLevel+self.__spaceOffset, f)

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
            self.__fileManager.createEmptyFile(currentDirectory.fullpath + initFileName)
            currentDirectory.listFiles.append(initFileName)

        for i in range (len(currentDirectory.listDirectories)):
            self.__createInitFiles(currentDirectory.listDirectories[i])

    def __createDirectoryStructure (self):
        f = open(self.__directoryName + '__init__.py', 'w')
        self.__generateStructureFile(self.__directoryStructure, 0, f)
        f.close()

    def generate (self):
        self.__prepare()
        for i in range (len(self.__listFiles)):
                splitedPath = self.__fileManager.splitPath(self.__listFiles[i].shortDirectoryName)
                self.__buildStructure(splitedPath, 0, self.__directoryStructure)

        self.__createInitFiles(self.__directoryStructure)
        self.__createDirectoryStructure ()


if __name__ == "__main__":
    commandLineInput = CommandLineInput ()
    commandLineInput.checkInput()

    directoryName = sys.argv[1]
    directoryStructure = DirectoryStructure(directoryName)
    directoryStructure.generate()
