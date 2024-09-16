import os
import sys

class DesktopFile ():
    def __init__ (self,
                        binaryName,
                        pathToBinary,
                        pathToIcon,
                        description = "Description of your application"):

        self.pathToBinary = pathToBinary
        self.pathToIcon = pathToIcon
        self.description = description
        self.binaryName = binaryName
        self.filename = binaryName + '.desktop'

    def createFile (self):
        f = open (self.filename, 'w')

        fileContent = """#!/usr/bin/env xdg-open
[Desktop Entry]
StartupWMClass=<window class>
Type=Application
Name=""" + self.binaryName + """
Comment=""" + self.description + """
Exec=""" + self.pathToBinary + """ %U
Icon=""" + self.pathToIcon + """
Terminal=false
Categories=Utility;Development; """

        f.write (fileContent)
        f.close()

    def moveFileToApplications (self):
        os.system('sudo mv ' + self.filename + ' /usr/share/applications/')
