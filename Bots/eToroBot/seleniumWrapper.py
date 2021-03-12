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

class SeleniumWrapper:
    def __init__(self, driver):
        self.driver = driver

    def setElement(self,xpath, value):
        stockElement = self.driver.find_element_by_xpath(xpath)
        stockElement.send_keys(Keys.CONTROL + "a");
        stockElement.send_keys(Keys.DELETE);
        stockElement.send_keys(value)

    def clickElementByXpath (self,xpath, timeout):
        stockElement = self.driver.find_element_by_xpath(xpath)
        stockElement.click()
        time.sleep(timeout)

    def clickElementById (self, id, timeout):
        element = self.driver.find_element_by_id(id)
        element.click()
        time.sleep(timeout)

    def clickElementByCssSelector (self, cssSelector, timeout):
        element = self.driver.find_element_by_css_selector(cssSelector)
        element.click()
        time.sleep(timeout)

    def clickElementByClassName (self, className, timeout):
        element = self.driver.find_element_by_class_name(className)
        element.click()
        time.sleep(timeout)

    def getTextByXpath (self, xpath):
        element = self.driver.find_element_by_xpath(xpath)
        return element.text
