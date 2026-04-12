import os
import sys
sys.path.insert(1, '../Plasma/Plasma6/')

from desktopFile import DesktopFile

def help ():
    helpString = """
Wrong input! please use the following input:
    arg1 - path to the atom binary
    arg2 - path to the icon or an icon name if it's part of installed icons"
"""
    print (helpString)

if (len (sys.argv)!=3):
    help ()
    sys.exit (0)

pathToBinary = sys.argv[1]
pathToIcon = sys.argv[2]
filename = 'atom1'
description = "A text editor"

desktopFile = DesktopFile (filename, pathToBinary, pathToIcon, description)
desktopFile.createFile ()
desktopFile.moveFileToApplications()
