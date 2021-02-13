import os
import sys
import fnmatch
import time
import File
from pathlib import Path

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

    def createEmptyFile (self, filename):
        f=open(filename, 'w')
        f.close()
        
    def getAllFiles (self, dir, extension ):
        result = []
        for root, dirnames, filenames in os.walk(dir):
            for filename in fnmatch.filter(filenames, '*.' + extension):
                file = File.File ()
                file.filename = filename
                file.directory = root
                file.fullpath = os.path.join(root, filename)
                result.append(file)
        return result
