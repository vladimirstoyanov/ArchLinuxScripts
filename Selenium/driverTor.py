from tbselenium.tbdriver import TorBrowserDriver

class Driver:
    def __init__ (self, profile, userAgent=''):
        self.__driver = TorBrowserDriver("/path/to/TorBrowserBundle/")

    def getDriver (self):
        return self.__driver
