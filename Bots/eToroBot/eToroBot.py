"""['VC', 'Visteon Corp', '-2.78', '(-5.41%)', 'S', '48.74', 'B', '49.05', '95%', 'BUYING', 'JUVE.MI', 'Juventus Football Club', '0.1010', '(12.59%)', 'S', '0.8982', 'B', '0.9006', '100%', 'BUYING', 'TSLA', 'Tesla Motors, Inc.', '-7.53', '(-1.00%)', 'S', '745.05', 'B', '746.79', '88%', 'BUYING', 'BTC', 'Bitcoin', '-303.48', '(-4.24%)', 'S', '6854.85', 'B', '6906.35', '97%', 'BUYING', 'ETHEREUM', 'Ethereum', '-10.2241', '(-5.66%)', 'S', '170.4077', 'B', '173.6712', '99%', 'BUYING', 'GOLD', '12.99', '(0.77%)', 'S', '1694.36', 'B', '1698.37', '74%', 'BUYING', 'GOOG', 'Alphabet', '-16.64', '(-1.30%)', 'S', '1268.40', 'B', '1271.21', '99%', 'BUYING', 'FB', 'Facebook', '-1.00', '(-0.56%)', 'S', '178.34', 'B', '178.72', '99%', 'BUYING', 'BCH', 'Bitcoin Cash', '-14.17', '(-6.05%)', 'S', '220.21', 'B', '224.41', '99%', 'BUYING', 'USDRUB', '1.08', '(1.46%)', 'S', '75.13', 'B', '75.21', '73%', 'SELLING', 'WIZZ.L', 'Wizz Air Holdings Plc', '17.99', '(0.67%)', 'S', '2699.57', 'B', '2712.44', '92%', 'BUYING', 'TKWY.NV', 'Takeaway.com NV', '0.62', '(0.70%)', 'S', '89.68', 'B', '89.92', '96%', 'BUYING', 'PAH3.DE', 'Porsche Automobil Holding SE', '-0.02', '(-0.05%)', 'S', '43.44', 'B', '43.55', '99%', 'BUYING', 'AF.PA', 'Air France-KLM', '-0.016', '(-0.34%)', 'S', '4.722', 'B', '4.737', '98%', 'BUYING', 'NVDA', 'NVIDIA Corporation', '-5.27', '(-1.80%)', 'S', '286.90', 'B', '287.55', '98%', 'BUYING', 'BIDU', 'Baidu, Inc.', '-0.32', '(-0.30%)', 'S', '104.56', 'B', '104.78', '99%', 'BUYING', 'ATVI', 'Activision Blizzard, Inc.', '-0.38', '(-0.57%)', 'S', '66.55', 'B', '66.68', '99%', 'BUYING', 'SPOT', 'Spotify', '2.68', '(1.89%)', 'S', '143.56', 'B', '145.17', '99%', 'BUYING', 'SAP.DE', 'SAP AG', '0.75', '(0.67%)', 'S', '113.28', 'B', '113.50', '100%', 'BUYING', 'SNAP', 'Snapchat Inc', '-0.07', '(-0.54%)', 'S', '12.91', 'B', '12.94', '95%', 'BUYING', 'CERN', 'Cerner Corp.', '0.24', '(0.34%)', 'S', '70.28', 'B', '70.43', '100%', 'BUYING', 'EURUSD', '-0.0007', '(-0.06%)', 'S', '1.0861', 'B', '1.0869', '63%', 'BUYING', 'ZEC', 'ZCASH', '-4.15', '(-8.94%)', 'S', '42.25', 'B', '43.73', '98%', 'BUYING', 'LTC', 'Litecoin', '-2.32', '(-5.45%)', 'S', '40.22', 'B', '40.99', '100%', 'BUYING', 'AAPL', 'Apple', '-5.87', '(-2.08%)', 'S', '277.22', 'B', '277.74', '97%', 'BUYING', 'PG', 'Procter & Gamble Co', '-4.09', '(-3.28%)', 'S', '120.87', 'B', '121.11', '99%', 'BUYING', 'OIL', '-3.06', '(-12.47%)', 'S', '21.48', 'B', '21.53', '78%', 'BUYING', 'T', 'AT&T Inc', '-0.25', '(-0.80%)', 'S', '31.04', 'B', '31.11', '100%', 'BUYING']
"""

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

def getLoginDetails ():
    loginInfoFile = open('/home/scitickart/eToro/login_info', 'r')
    username = loginInfoFile.readline()
    password = loginInfoFile.readline()
    username.replace('\r','')
    username.replace('\n','')
    password.replace('\r','')
    password.replace('\n','')
    
    return username, password

def monitor():
    while True:
        stockName = driver.find_element_by_xpath('/html/body/ui-layout/div/div/div[2]/et-watchlist/div[2]/div/et-watchlist-list/section/section[1]')
      
        listResult = stockName.text.split('\n')
        lPart = []
        lResult = []
        lOldResults = []
        for i in range(0,len(listResult)):
            if (listResult[i] == 'BUYING' or listResult[i] == 'SELLING'):
                lPart.append(listResult[i])
                lResult.append(lPart)
                lOldResults.append(lPart)
                lPart = []
            else:
                lPart.append(listResult[i])
                lOldResults.append(lPart)
        
        for i in range (len(lResult)):
            if (len(lResult[i]) == 9):
                if (lOldResults[i][4]!=lResult[i][4] or lOldResults[i][6]!=lResult[i][6]):
                    print ("Stock: " + lResult[i][0] + ", sell price: " + lResult[i][4] + ", buy price: " + lResult[i][6])
                    lOldResults[i][4] = lResult[i][4]
                    lOldResults[i][6] = lResult[i][6]
            else:
                if (lOldResults[i][5]!=lResult[i][5] or lOldResults[i][7]!=lResult[i][7]):
                    print ("Stock: " + lResult[i][0] + ", sell price: " + lResult[i][5] + ", buy price: " + lResult[i][7])
                    lOldResults[i][5] = lResult[i][5]
                    lOldResults[i][7] = lResult[i][7]
        time.sleep(1)
    
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


"""
CERN
Cerner Corp.
0.24
(0.34%)
S
70.28
B
70.43
100%
BUYING
EURUSD
-0.0010
(-0.09%)
S
1.0858
B
1.0865
63%
BUYING
ZEC
ZCASH
-4.10
(-8.84%)
S
42.30
B
43.78
98%
BUYING
LTC
Litecoin
-2.49
(-5.85%)
S
40.05
B
40.82
100%
BUYING
AAPL
Apple
-5.87
(-2.08%)
S
277.22
B
277.74
97%
BUYING
PG
Procter & Gamble Co
-4.09
(-3.28%)
S
120.87
B
121.11
99%
BUYING
OIL
-3.06
(-12.47%)
S
21.48
B
21.53
78%
BUYING
T
AT&T Inc
-0.25
(-0.80%)
S
31.04
B
31.11
100%
BUYING
"""
