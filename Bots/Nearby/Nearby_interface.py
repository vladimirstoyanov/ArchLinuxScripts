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



def setElement(xpath, value):
    stockElement = driver.find_element_by_xpath(xpath)
    stockElement.send_keys(Keys.CONTROL + "a");
    stockElement.send_keys(Keys.DELETE);
    stockElement.send_keys(value)

def clickElementByXpath (xpath, timeout):
    stockElement = driver.find_element_by_xpath(xpath)
    stockElement.click()
    time.sleep(timeout)


def monitor():
        while True:
            driver.get("https://www.wnmlive.com/")
            print (driver.page_source)
            time.sleep(6)
            print ("Trying to get the source....")
        #stream = driver.find_element_by_xpath('//*[@id="postsDiv"]')

        #print (stream.text)
        #print (dir(stream))

def login():
    mainWindow = driver.window_handles[0]
    print("Trying to start Nearby web site...")
    driver.get("https://www.wnmlive.com/")

    time.sleep(15)
    try:
        print ("Trying to click on Entire world button")
        button = driver.find_element_by_xpath('/html/body/form/div[4]/div[1]/div/div[2]/table/tbody/tr[2]/td/div[2]/div/div/label[4]/span[2]') #entire world
        button.click()
    except:
        pass



profile = FirefoxProfile("/home/scitickart/.mozilla/firefox/w05kja2g.default")
driver = webdriver.Firefox(profile)

driver.maximize_window()

wait = WebDriverWait(driver, 10)

login()
monitor()
