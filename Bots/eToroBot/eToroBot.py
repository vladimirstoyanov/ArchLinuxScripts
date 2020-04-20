import pickle
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC ##wait function: wait to load  web page
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def LoadCookies():
    cookies = pickle.load(open("cookies1.pkl", "rb"))
    for cookie in cookies:
      driver.add_cookie(cookie)

def SaveCookies():
    pickle.dump( driver.get_cookies() , open("cookies1.pkl","wb"))


def get_text_excluding_children(driver, element):
    return driver.execute_script("""
    return jQuery(arguments[0]).contents().filter(function() {
        return this.nodeType == Node.TEXT_NODE;
    }).text();
    """, element)

def getLoginDetails ():
    loginInfoFile = open('/home/scitickart/eToro/logic_info', 'r')
    username = loginInfoFile.readline()
    password = loginInfoFile.readline ();
    username.replace('\r','')
    username.replace('\n','')
    password.replace('\r','')
    password.replace('\n','')
    
    return username, password

def monitorEtoro():
    while True:
        #sell button
        #/html/body/ui-layout/div/div/div[2]/et-watchlist/div[2]/div/et-watchlist-list/section/section[1]/section[5]/et-instrument-row/et-instrument-trading-row/div/et-buy-sell-buttons/et-buy-sell-button[1]/div/div[2]
        #buy button
        #/html/body/ui-layout/div/div/div[2]/et-watchlist/div[2]/div/et-watchlist-list/section/section[1]/section[5]/et-instrument-row/et-instrument-trading-row/div/et-buy-sell-buttons/et-buy-sell-button[2]/div/div[2]
        sellButton = driver.find_element_by_xpath('/html/body/ui-layout/div/div/div[2]/et-watchlist/div[2]/div/et-watchlist-list/section/section[1]/section[5]/et-instrument-row/et-instrument-trading-row/div/et-buy-sell-buttons/et-buy-sell-button[1]/div/div[2]')
        print("Sell price: " + sellButton.text)
        buyButton = driver.find_element_by_xpath('/html/body/ui-layout/div/div/div[2]/et-watchlist/div[2]/div/et-watchlist-list/section/section[1]/section[5]/et-instrument-row/et-instrument-trading-row/div/et-buy-sell-buttons/et-buy-sell-button[2]/div/div[2]')
        print ("Buy price: " + buyButton.text)
        time.sleep(1)
    
def logInEToro():
    mainWindow = driver.window_handles[0]
    print ("Getting gateway URL...")
    driver.get("https://www.etoro.com/login")

    time.sleep(10)
    print("Trying to find a login button...");
    button = driver.find_element_by_xpath('/html/body/ui-layout/div/div/div[1]/login/login-sts/div/div/div/form/div/div[7]/div/button[1]')
    button.click()
    
    time.sleep(5)
    print("Window handlers: " + str(driver.window_handles))
    print("Trying to login...")
    facebookLoginWindow = driver.window_handles[1]
    driver.switch_to_window(facebookLoginWindow)
    usernameStr, passwordStr = getLoginDetails()
    #username  //*[@id="email"]
    #password //*[@id="pass"]
    #login button //*[@id="u_0_0"]
    username = driver.find_element_by_xpath('//*[@id="email"]')
    username.send_keys(usernameStr)
    password = driver.find_element_by_xpath('//*[@id="pass"]')
    password.send_keys(passwordStr)
    
    loginButton = driver.find_element_by_xpath('//*[@id="u_0_0"]')
    loginButton.click()
    
    driver.switch_to_window(mainWindow)
    
    print('Please confirm login credential by your phone and press any key to continue...')
    x = input()
    
    monitorEtoro()
    
print ("Loading Firefox...")
driver = webdriver.Firefox()

print ("Maximizing firefox...")
driver.maximize_window()

wait = WebDriverWait(driver, 10)

logInEToro()
