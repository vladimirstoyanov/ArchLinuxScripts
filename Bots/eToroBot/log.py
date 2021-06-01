from datetime import datetime

class Log ():
    def __init__(self, filename):
        self.__filename = filename
    def write(self, message):
        logFile = open(self.__filename, 'a')
        dateTimeObj = datetime.now()
        timestampStr = dateTimeObj.strftime("%d-%b-%Y (%H:%M:%S.%f)")
        print("Time: " + timestampStr + ": " + message)
        logFile.write("Time: " + timestampStr + ": " + message + '\n')
        logFile.close()
