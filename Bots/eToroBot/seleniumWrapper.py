import os
import sys
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
from log import Log

class SeleniumWrapper:
    def __init__(self, driver):
        self.__driver = driver
        self.__log = Log("failed_selenum_requests.log")

    def changeUserAgent (self, profile, userAgentString):
        profile.set_preference("general.useragent.override", "whatever you want")

    def getRequestWaitUntilLocatedElementById (self, url, id):
        try:
            self.__driver.get(url)
            element = WebDriverWait(self.__driver, 15).until(EC.presence_of_element_located((By.ID, id)))
        except:
            self.__log.write ("Filed to load url: " + url)

    def getRequestWaitUntilLocatedElementByXpath (self, url, xpath):
        try:
            self.__driver.get(url)
            element = WebDriverWait(self.__driver, 15).until(EC.presence_of_element_located((By.XPATH, xpath)))
        except:
            self.__log.write ("Filed to load url: " + url)

    def getRequestWaitUntilLocatedElementByCssSelector (self, url, cssSelector):
        try:
            self.__driver.get(url)
            element = WebDriverWait(self.__driver, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, cssSelector)))
        except:
            self.__log.write ("Filed to load url: " + url)


    def getRequest (self, url):
        self.__driver.get(url)
        time.sleep (15)

    def close (self):
        self.__driver.quit()
        os.system('rm -rf /tmp/Temp-*')
        os.system('rm -rf /tmp/rust_mozprofile*')
        os.system('rm -rf /tmp/dbus-*')

    def clickElementByXpath (self,xpath, timeout):
        try:
            stockElement = self.__driver.find_element_by_xpath(xpath)
            stockElement.click()
            time.sleep(timeout)
        except:
            self.__log.write("Failed to execute find_element_by_xpath(" + xpath + ")")

    def clickElementById (self, id, timeout):
        try:
            element = self.__driver.find_element_by_id(id)
            element.click()
            time.sleep(timeout)
        except:
            self.__log.write("Failed to execute find_element_by_id(" + id + ")")

    def clickElementByCssSelector (self, cssSelector, timeout):
        try:
            element = self.__driver.find_element_by_css_selector(cssSelector)
            element.click()
            time.sleep(timeout)
        except:
            self.__log.write("Failed to execute find_element_by_css_selector(" + cssSelector + ")")


    def clickElementByClassName (self, className, timeout):
        try:
            element = self.__driver.find_element_by_class_name(className)
            element.click()
            time.sleep(timeout)
        except:
            self.__log.write("Failed to execute find_element_by_class_name(" + className + ")")


    def getTextByXpath (self, xpath):
        element = self.__driver.find_element_by_xpath(xpath)
        return element.text

    def getTextByCSSSelector (self, cssSelector):
        element = self.__driver.find_element_by_css_selector(cssSelector)
        return element.text

    def getTextByClassName (self, className):
        element = self.__driver.find_element_by_class_name(className)
        return element.text

    def setTextFieldByXpath(self, xpath, value):
        try:
            stockElement = self.__driver.find_element_by_xpath(xpath)
            stockElement.send_keys(Keys.CONTROL + "a");
            stockElement.send_keys(Keys.DELETE);
            stockElement.send_keys(value)
        except:
            self.__log.write("Failed to execute find_element_by_xpath(" + xpath + ")")

    def setTextFieldByCSSSelector(self, cssSelector, value):
        try:
            stockElement = self.__driver.find_element_by_css_selector(cssSelector)
            stockElement.send_keys(Keys.CONTROL + "a");
            stockElement.send_keys(Keys.DELETE);
            stockElement.send_keys(value)
        except:
            self.__log.write("Failed to execute find_element_by_css_selector(" + cssSelector + ")")
