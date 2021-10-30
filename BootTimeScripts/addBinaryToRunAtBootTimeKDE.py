import os
import sys

class CommandLineInput:
    def __init__ (self):
        pass

    def checkInput (self):
        if (len (sys.argv)!=4):
            print ("Wrong input:")
            print ("1 arg: binary path (e.g. /home/user/binary)")
            print ("2 arg: binary file name")
            print ("3 arg: user name")
            sys.exit()

class BootFile:
    def __init__ (self, path, binaryName, userName):
        self.path = path
        self.binaryName = binaryName
        self.bootFileName = binaryName + ".desktop"
        self.userName = userName

    def generateBootFile (self):
        file = open (self.binaryName + ".desktop", 'w')
        file.write('[Desktop Entry]\n')
        file.write('Name=' + binaryName + '\n')
        file.write('Comment=Some comment\n')
        file.write('Exec='+ self.path +'\n')
        file.write('Icon=None\n')
        file.write('Terminal=false\n')
        file.write('Type=Application\n')
        file.write('StartupNotify=false\n')
        file.write('X-GNOME-Autostart-enabled=true\n')
        file.close()

    def addFileAtBootTime (self):
        os.system('mv ' + self.bootFileName + ' /home/' + self.userName +'/.config/autostart/' )


if __name__ == "__main__":
    commandLineInput = CommandLineInput ()
    commandLineInput.checkInput()

    binaryPath = sys.argv[1]
    binaryName = sys.argv[2]
    userName = sys.argv[3]

    bootFile = BootFile(binaryPath, binaryName, userName)
    bootFile.generateBootFile()
    bootFile.addFileAtBootTime ()
