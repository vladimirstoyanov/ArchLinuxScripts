import os
import sys

class RemoveFiles:
    def __init__ (self):
        self.listDirectories = ['./storage/self/primary/Android/data/com.viber.voip/files/', './storage/self/primary/Telegram/']
        self.removeFiles()

    def removeFiles (self):
        for i in range (len(self.listDirectories)):
            os.system ("sudo adb shell \"find "+ self.listDirectories[i] + " -iname '*.jpg' -exec rm -rf {} \;\"")
            os.system ("sudo adb shell \"find "+ self.listDirectories[i] + " -iname '*.mp4' -exec rm -rf {} \;\"")
            os.system ("sudo adb shell sync")

if __name__ == "__main__":
    removeFiles = RemoveFiles ()
