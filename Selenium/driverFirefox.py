from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC ##wait function: wait to load  web page
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.webdriver import FirefoxProfile

class Driver:
    """
    def __init__ (self, profile):
        self.__profile = FirefoxProfile(profile)
        self.__driver = webdriver.Firefox(self.__profile)
        self.__driver.maximize_window()
        wait = WebDriverWait(self.__driver, 10)
    """

    def __init__ (self, profile, userAgent=''):
            self.__profile = FirefoxProfile(profile)
            if (userAgent!=''):
                self.__profile.set_preference("general.useragent.override", userAgent)
            self.__driver = webdriver.Firefox(self.__profile)
            self.__driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
            self.__driver.maximize_window()
            wait = WebDriverWait(self.__driver, 10)

    def getDriver (self):
        return self.__driver
