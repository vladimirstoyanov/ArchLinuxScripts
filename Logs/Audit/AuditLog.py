class AuditLog:
    def __init__ (self, filename="/var/log/audit/audit.log"):
        self.filename = filename
        self.data = []
        self.__parseAuditLog ()

    def __parseAuditLog (self):
        f = open (self.filename, 'r')

        for line in f.readlines ():
            lineSplited = line.split (' ')
            self.data.append(lineSplited)
    def __removeUnusedSymbols (self, string):
        string = string.replace('\n', '')
        string = string.replace('"', '')
        return string

    def __getProperty (self, property):
            resultList = []
            for i in range (len(self.data)):
                for j in range (len(self.data[i])):
                    if (self.data[i][j].find(property)==0):
                        splitted = self.data[i][j].split('=')
                        resultList.append(self.__removeUnusedSymbols(splitted[1]))
            return list(set(resultList)) #only unique elements

    def getUsers (self):
        return self.__getProperty('AUID')

    def getExecutables(self):
        return self.__getProperty('exe')


if __name__ == "__main__":
    auditLog = AuditLog ()
    print(auditLog.getUsers())
