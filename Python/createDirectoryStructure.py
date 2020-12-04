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

    def splitPath (self, path):
        return path.split('/')

    def returnPathAfterDirectory (self, path, directoryName):
        splitedPath = self.splitPath(path)
        index = -1
        pathAfterDirectory = ""
        for i in range (splitedPath):
            if (splitedPath == directoryName):
                index = i
        if (index == -1):
            return []

        return splitedPath[index+1:len(splitedPath)]

    def getParentDirectory (self, path):
        splitedPath = self.splitPath()
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

class TreeNode:
    def __init__ (self, name, type):
        self.fileChilds=[]
        self.directoryChilds[]
        self.name = name
        self.type = type #file or directory
    def insertChild (self, child):
        self.childs.append(child)
    def find (self, child):
        for i in range (len(self.childs)):
            if (child.name == self.childs[i].name)
                return self.child[i]
        return None

class Tree:
    def __init__ (self):
        self.root = None
    def insert(self, treeNode, path, filename):
            if (self.root == None)
                self.root = TreeNode (item.name, item.type)
                return
            if (len(threeNode.child) >= index):
                return
            threeNode = threeNode.child[index]
            insert (threeNode,index+1, name, type)


class PythonDirectoryStructure:
    def __init__ (self, directory):
        self.directory = directory
        self.fileManager = FileManager()
        self.files = fileManager.getAllFiles ()
        self.directoryStructure = []

    def generate (self):
        f = open (self.directory + '__init__.py', 'w')
        parentDirectory = self.fileManager.getParentDirectory(self.directory)
        f.write(parentDirectory + '/')
        self.directoryStructure.append(parentDirectory)
        for i in range (len(self.files)):
            directoriesAfterParent = self.fileManager.returnPathAfterDirectory(self.files[i].directory, parentDirectory)
        f.close ()


commandLineInput = CommandLineInput ()
commandLineInput.checkInput()

directoryName = sys.argv[1]
fileManager = FileManager ()
files = fileManager.getAllFiles(directoryName, "py")
pythonDirectoryStructure = PythonDirectoryStructure (directoryName)
pythonDirectoryStructure.generate()
