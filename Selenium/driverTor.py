from tbselenium.tbdriver import TorBrowserDriver

class Driver:
    def __init__ (self, profile, userAgent=''):
        self.__driver = TorBrowserDriver("/usr/bin/tor")

    def getDriver (self):
        return self.__driver
