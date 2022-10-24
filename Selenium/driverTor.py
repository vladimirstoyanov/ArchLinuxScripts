from tbselenium.tbdriver import TorBrowserDriver

class Driver:
    #pathToTorDirectory (e.g. /home/vladimir/Tor/tor-browser_en-US/)
    #don't forget to run 'tor' service  
    def __init__ (self, pathToTorDirectory):
        self.__driver = TorBrowserDriver(pathToTorDirectory)

    def getDriver (self):
        return self.__driver
