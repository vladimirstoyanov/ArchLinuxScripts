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

class Log ():
    def __init__(self):
        pass
    def write(self, message):
        logFile = open('eToro.log', 'a')
        dateTimeObj = datetime.now()
        timestampStr = dateTimeObj.strftime("%d-%b-%Y (%H:%M:%S.%f)")
        print("Time: " + timestampStr + ": " + message)
        logFile.write("Time: " + timestampStr + ": " + message + '\n')
        logFile.close()

class Config ():
    def __init__ (self):
        self.configData = []
        self.readConfig()
        log.write(str(self.configData))

    def readConfig (self):
        f = open ('config', 'r')
        for row in f.readlines():
            lData = row.split(';')
            lData[len(lData)-1] = lData[len(lData)-1].replace('\n','')
            lData[len(lData)-1] = lData[len(lData)-1].replace('\r','')
            self.configData.append(lData)
    
            
    
def getLoginDetails ():
    loginInfoFile = open('/home/scitickart/eToro/login_info', 'r')
    username = loginInfoFile.readline()
    password = loginInfoFile.readline()
    username.replace('\r','')
    username.replace('\n','')
    password.replace('\r','')
    password.replace('\n','')
    return username, password

def setElement(xpath, value):
    stockElement = driver.find_element_by_xpath(xpath)
    stockElement.send_keys(Keys.CONTROL + "a");
    stockElement.send_keys(Keys.DELETE);
    stockElement.send_keys(value)
    
def clickElementByXpath (xpath, timeout):
    stockElement = driver.find_element_by_xpath(xpath)
    stockElement.click()
    time.sleep(timeout)

def buyStock (index, price):
    clickElementByXpath('/html/body/ui-layout/div/div/div[2]/et-watchlist/div[2]/div/et-watchlist-list/section/section[1]/section[' + index +']/et-instrument-row/et-instrument-trading-row/div/et-card-avatar/a/div[2]', 6)
    log.write("stock clicked...")
    
    clickElementByXpath('/html/body/ui-layout/div/div/div[2]/et-market/div/div/et-market-header/div/div[2]/trade-button/div/span', 4)
    log.write("Trade button clicked...")
    
    #/html/body/div[2]/div[2]/div/div/div[2]/div/div[2]/div[2]/div[1]/div[2]/input
    setElement('/html/body/div[2]/div[2]/div/div/div[2]/div/div[2]/div[2]/div[1]/div[2]/input', price)
    log.write("Price set...")
    time.sleep(4)
    
    #x button clicked
    clickElementByXpath('/html/body/div[4]/div[2]/div/div/div[2]/div/div[4]/div/button', 3)
    log.write("open trade button clicked...")
    
    #return back to main list
    clickElementByXpath('/html/body/ui-layout/div/div/div[1]/div/div/div[1]/a', 7)
    log.write("back to main list")
    
def sellStock (index):
    clickElementByXpath('/html/body/ui-layout/div/div/div[2]/et-watchlist/div[2]/div/et-watchlist-list/section/section[1]/section[' + index +']/et-instrument-row/et-instrument-trading-row/div/et-card-avatar/a/div[2]', 6)
    log.write("stock clicked...")
    
    #"chart" button: 
    clickElementByXpath('/html/body/ui-layout/div/div/div[2]/et-market/div/div/div/div[2]/a[3]/span[2]', 4)
    log.write("chart button clicked")
    
    #"stock" button: /html/body/ui-layout/div/div/div[2]/et-market/div/div/div/et-my-investments-tooltip/a/span[2]
    clickElementByXpath('/html/body/ui-layout/div/div/div[2]/et-market/div/div/div/et-my-investments-tooltip/a/span[2]', 4)
    log.write("stock button clicked...")
    
    #"settings" button: /html/body/ui-layout/div/div/div[2]/div/div[2]/div/div/div[5]/span
    clickElementByXpath('/html/body/ui-layout/div/div/div[2]/div/div[2]/div/div/div[5]/span', 4)
    log.write("settings button clicked...")
    
    #"close" button /html/body/ui-layout/div/div/div[2]/div/div[2]/div/div/div[5]/div/div/div[1]
    clickElementByXpath('/html/body/ui-layout/div/div/div[2]/div/div[2]/div/div/div[5]/div/div/div[1]', 4)
    log.write("close button clicked...")
    
    #"I want to close all" checkbox: /html/body/div[3]/div[2]/close-all-positions/div/div[3]/div[3]/div/div/label
    #'//label[@for="Rooms"]/parent::td/following-sibling::td')
    #clickElementByXpath('/html/body/div[2]/div[2]/close-all-positons/div/div[3]/div[3]/div[1]/div/label', 2)
    clickElementByXpath(".//*[contains(text(), 'I want to close')]",2)
    log.write("I want to close all trades check clicked.")
    
    
    #"close all" button clicked
    #clickElementByXpath('/html/body/div[3]/div[2]/close-all-positions/div/div[3]/div[4]/button', 5)
    log.write("close all button clicked")
    
    #"x" button clicked:
    #clickElementByXpath('/html/body/div[2]/div[2]/close-all-positions/div/div[2]', 3)
    clickElementByXpath(".//*[contains(text(), 'Close All')]",3)
    #print("x button clicked...")
    
    #back to main list
    clickElementByXpath('/html/body/ui-layout/div/div/div[1]/div/div/div[1]/a', 7)
    log.write("back to main list...")

def shouldWait (configData, stockCode, index):
        if (len(configData[index])!=4):
                return 0
        if (configData[index][3] !='Wait' and configData[index][3] !='wait'):
                return 0
        for i in range(len(configData)):
            if (configData[i][0] == stockCode and i!=index):
                return 1
        return 0
        
def monitor():
    config = Config()
    configData = config.configData
    while True:
        stocksInfo = driver.find_element_by_xpath('/html/body/ui-layout/div/div/div[2]/et-watchlist/div[2]/div/et-watchlist-list/section/section[1]')
      
        listResult = stocksInfo.text.split('\n')
        lPart = []
        lResult = []
        index = 0
        for i in range(0,len(listResult)):
            if (listResult[i] == 'BUYING' or listResult[i] == 'SELLING'):
                index+=1
                lPart.append(listResult[i])
                if (len(lPart) == 9):
                    lPart.insert(1,' ')
                for j in range (len(configData)):
                    if (lPart[0] == configData[j][0]):
                        lPart.append(str(index))
                        lResult.append(lPart)
                        break
                lPart = []
            else:
                lPart.append(listResult[i])
        
        
        for i in range (len(lResult)):
            sellPrice = lResult[i][5]
            buyPrice = lResult[i][7]
            stockCode = lResult[i][0]
            for j in range(len(configData)):
                if (configData[j][0] == stockCode):
                    if (configData[j][1] == 'sell'):
                        log.write("Stock: " + stockCode + "\t\t sell price: " + sellPrice + "/" +configData[j][2] +"\t\t buy price: " + buyPrice)
                        if (sellPrice >= configData[j][2] and shouldWait(configData, stockCode, j) == 0):
                            log.write("Selling " + configData[j][0] + "==============")
                            configData.pop(j)
                            sellStock(lResult[i][10])
                            break
                    elif(configData[j][1] == 'buy'):
                        log.write("Stock: " + stockCode + "\t\t sell price: " + sellPrice  +"\t\t buy price: " + buyPrice + "/" + configData[j][2])
                        if (buyPrice <= configData[j][2]):
                            log.write("Buying " + configData[j][0] + "================")
                            buyStock(lResult[i][10], configData[j][3])
                            configData.pop(i)
                            break
                    else:
                        pass
                    continue
        
        log.write("==============")
        time.sleep(1)
        
def login():
    mainWindow = driver.window_handles[0]
    log.write("Getting gateway URL...")
    driver.get("https://www.etoro.com/login")

    time.sleep(15)
    try:
        log.write("Trying to find a login button...")
        button = driver.find_element_by_xpath('/html/body/ui-layout/div/div/div[1]/login/login-sts/div/div/div/form/div/div[7]/div/button[1]')
        button.click()
        
        time.sleep(5)
        log.write("Window handlers: " + str(driver.window_handles))
        log.write("Trying to login...")
        facebookLoginWindow = driver.window_handles[1]
        driver.switch_to_window(facebookLoginWindow)
        usernameStr, passwordStr = getLoginDetails()
        username = driver.find_element_by_xpath('//*[@id="email"]')
        username.send_keys(usernameStr)
        password = driver.find_element_by_xpath('//*[@id="pass"]')
        password.send_keys(passwordStr)
        
        loginButton = driver.find_element_by_xpath('//*[@id="u_0_0"]')
        loginButton.click()
        
        driver.switch_to_window(mainWindow)
        
        log.write('Please confirm login credential by your phone and press any key to continue...')
        x = input()
    except:
        pass
    
log = Log()

log.write("Loading Firefox...")
profile = FirefoxProfile("/home/scitickart/.mozilla/firefox/w05kja2g.default")
driver = webdriver.Firefox(profile)

log.write("Maximizing firefox...")
driver.maximize_window()

wait = WebDriverWait(driver, 10)

login()
monitor()
