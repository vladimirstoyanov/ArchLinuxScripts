class File:
    def __init__ (self):
        self.filename = ""
        self.fullpath = ""
        self.directory = ""
        self.shortDirectoryName = ""
    def __repr__(self): #string representation when print it
        return str(self.filename + '\n' + self.fullpath + '\n' + self.directory  + '\n' + self.shortDirectoryName +'\n')
