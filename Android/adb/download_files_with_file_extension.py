import os
import sys

class CommandLineInput:
    def __init__ (self):
        self.checkInput()

    def checkInput (self):
        if (len (sys.argv)!=3):
            print ("Wrong input:")
            print ("1 arg: file extension")
            print ("2 arg: destination path")
            sys.exit()

class DownloadFiles:
    def __init__ (self):
        commandLineInput = CommandLineInput()
        self.createListOfFiles()
        print ("Files has been created...")
        self.downloadFiles()

    def createListOfFiles (self):
	#/storage/self/primary/DCIM/Camera
        os.system ("sudo adb shell find ./storage/self/primary/ -iname '*." + sys.argv[1] +"' > files.txt")


    def downloadFiles (self):
        f = open("files.txt", 'r')

        for line in f.readlines():
            line = line.replace('\n', ' ')
            line = line.replace('\r', ' ')
            print ("Trying to download " + line)
            os.system ("adb pull " + line + " " + sys.argv[2])
            #os.system ("adb shell rm " + line) #remove the file after download it
            os.system ("adb shell sync")

        f.close()

        os.system ('rm files.txt')

if __name__ == "__main__":
    downloadFiles = DownloadFiles ()
