import pickle
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC ##wait function: wait to load  web page
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.webdriver import FirefoxProfile
from datetime import datetime

class NearbyPropBot:
    def __init__(self, profileName):
        self.profileName = profileName

    def __clickButton(self, buttonName, xpath):
            try:
                        print ("Trying to click on " + buttonName + " button...")
                        button = self.driver.find_element_by_xpath(xpath)
                        button.click()
            except:
                        print("It couldn't click on " + buttonName + " button.")
                        return 0
            return 1

    def __clickPropButton (self, tableId):
        return self.__clickButton("Prop",
            '/html/body/form/div[4]/div[1]/div/div[2]/div[2]/table['
            + str(tableId)
            + ']/tbody/tr[1]/td[2]/div[1]/div[3]/button[1]')

    def __clickRefreshButton (self):
            return self.__clickButton("Refresh", "/html/body/form/div[2]/div[1]/img")

    def __clickEntireWorldButton (self):
            return self.__clickButton("Entire world",
                "/html/body/form/div[4]/div[1]/div/div[2]/table/tbody/tr[2]/td/div[2]/div/div/label[4]/span[2]")

    def __propAllPosts (self):
        tableId=1
        while (True):
            if (self.__clickPropButton (tableId)==0):
                return
            tableId+=1
            time.sleep (1)

    def __propEveryPost (self):
        self.__clickEntireWorldButton()
        while (True):
            self.__clickRefreshButton ()
            self.__propAllPosts ()
            time.sleep (5)
            print ("=====New iteration")

    def __login():
        mainWindow = self.driver.window_handles[0]
        print("Trying to start Nearby web site...")
        self.driver.get("https://www.wnmlive.com/")

    def __loadingFirefox (self):
        print("Loading Firefox with profile: " + self.profileName)

        profile = FirefoxProfile(self.profileName)
        self.driver = webdriver.Firefox(profile)

        print("Maximizing firefox...")
        self.driver.maximize_window()

        secondsToWait = 10
        WebDriverWait(driver, secondsToWait)

    def start (self):
        self.__loadingFirefox()
        self.__login()
        self.__propEveryPost()


nearbyPropBot = NearbyPropBot("/home/scitickart/.mozilla/firefox/w05kja2g.default")
nearbyPropBot.start()
