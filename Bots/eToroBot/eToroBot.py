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


class Config ():
    
    def __init__ (self):
        self.configData = []
        self.readConfig()
        print (self.configData)

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

def sellStock (index):
    stockElement = driver.find_element_by_xpath('/html/body/ui-layout/div/div/div[2]/et-watchlist/div[2]/div/et-watchlist-list/section/section[1]/section[' + index +']/et-instrument-row/et-instrument-trading-row/div/et-card-avatar/a/div[2]')
    stockElement.click()
    print("stock clicked...")
    
    time.sleep(6)
    
    #chart button: /html/body/ui-layout/div/div/div[2]/et-market/div/div/div/div[2]/a[3]/span[2]
    stockElement = driver.find_element_by_xpath('/html/body/ui-layout/div/div/div[2]/et-market/div/div/div/div[2]/a[3]/span[2]')
    stockElement.click()
    time.sleep(4)
    
    #stock button: /html/body/ui-layout/div/div/div[2]/et-market/div/div/div/et-my-investments-tooltip/a/span[2]
    stockElement = driver.find_element_by_xpath('/html/body/ui-layout/div/div/div[2]/et-market/div/div/div/et-my-investments-tooltip/a/span[2]')
    stockElement.click()
    time.sleep(4)
    
    #setting button: /html/body/ui-layout/div/div/div[2]/div/div[2]/div/div/div[5]/span
    stockElement = driver.find_element_by_xpath('/html/body/ui-layout/div/div/div[2]/div/div[2]/div/div/div[5]/span')
    stockElement.click()
    time.sleep(4)
    
    #close button /html/body/ui-layout/div/div/div[2]/div/div[2]/div/div/div[5]/div/div/div[1]
    stockElement = driver.find_element_by_xpath('/html/body/ui-layout/div/div/div[2]/div/div[2]/div/div/div[5]/div/div/div[1]')
    stockElement.click()
    time.sleep(4)
    print("close button clicked.")
    
    #I want to close all check: /html/body/div[3]/div[2]/close-all-positions/div/div[3]/div[3]/div/div/label
    stockElement = driver.find_element_by_xpath('/html/body/div[2]/div[2]/close-all-positions/div/div[3]/div[3]/div[1]/div/label')
    stockElement.click()
    time.sleep(2)
    print("I want to close all trades check clicked.")
    
    
    #close all button clicked
    #/html/body/div[3]/div[2]/close-all-positions/div/div[3]/div[4]/button
    #stockElement = driver.find_element_by_xpath('/html/body/div[3]/div[2]/close-all-positions/div/div[3]/div[4]/button')
    #stockElement.click()
    #time.sleep(5)
    
    #x button clicked: 
    stockElement = driver.find_element_by_xpath('/html/body/div[2]/div[2]/close-all-positions/div/div[2]')
    stockElement.click()
    time.sleep(3)
    print("x button clicked.")
    
    #return back to main list
    #/html/body/ui-layout/div/div/div[1]/div/div/div[1]/a
    stockElement = driver.find_element_by_xpath('/html/body/ui-layout/div/div/div[1]/div/div/div[1]/a')
    stockElement.click()
    time.sleep(7)
    
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
            print ("Stock: " + lResult[i][0] + ", sell price: " + lResult[i][5] + ", buy price: " + lResult[i][7])
            if (configData[i][1] == 'sell'):
                if (sellPrice >= configData[i][2]):
                    print("Selling " + configData[i][0])
                    configData.pop(i)
                    #/html/body/ui-layout/div/div/div[2]/et-watchlist/div[2]/div/et-watchlist-list/section/section[1]/section[2]/et-instrument-row/et-instrument-trading-row/div/et-card-avatar/a/div[2]
                    #/html/body/ui-layout/div/div/div[2]/et-watchlist/div[2]/div/et-watchlist-list/section/section[1]/section[4]/et-instrument-row/et-instrument-trading-row/div/et-card-avatar/a/div[2]
                    #/html/body/ui-layout/div/div/div[2]/et-watchlist/div[2]/div/et-watchlist-list/section/section[1]/section[1]/et-instrument-row/et-instrument-trading-row/div/et-card-avatar/a/div[2]/div[1]
                    sellStock(lResult[i][10])
                    break
            elif(configData[i][1] == 'buy'):
                if (buyPrice <= configData[i][2]):
                    print("Buying " + configData[i][0])
                    configData.pop(i)
                    break
            else:
                pass
    
def login():
    mainWindow = driver.window_handles[0]
    print ("Getting gateway URL...")
    driver.get("https://www.etoro.com/login")

    time.sleep(6)
    try:
        print("Trying to find a login button...");
        button = driver.find_element_by_xpath('/html/body/ui-layout/div/div/div[1]/login/login-sts/div/div/div/form/div/div[7]/div/button[1]')
        button.click()
        
        time.sleep(5)
        print("Window handlers: " + str(driver.window_handles))
        print("Trying to login...")
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
        
        print('Please confirm login credential by your phone and press any key to continue...')
        x = input()
    except:
        pass
    
print ("Loading Firefox...")
profile = FirefoxProfile("/home/scitickart/.mozilla/firefox/w05kja2g.default")
driver = webdriver.Firefox(profile)

print ("Maximizing firefox...")
driver.maximize_window()

wait = WebDriverWait(driver, 10)

login()
monitor()
