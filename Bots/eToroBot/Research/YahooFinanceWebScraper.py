#ToDo: get profile data: https://finance.yahoo.com/quote/NNDM/profile?p=NNDM
import time
import os, sys
import atexit
import pickle
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.webdriver import FirefoxProfile

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from log import Log
from driver import Driver
from sqliteData import SqliteDataEtoro
from seleniumWrapper import SeleniumWrapper

class YahooFinanceWebScraper:
    def __init__ (self):
        atexit.register(self.handleExit)
        self.stocksDataBase = SqliteDataEtoro ('stocks.db')
        self.stocksData = self.stocksDataBase.readData ('all_stocks')
        self.stockIdIndex = 0
        self.log = Log('stock_research.log')
        driverObj = Driver ("/home/scitickart/.mozilla/firefox/w05kja2g.default")
        self.driver = driverObj.getDriver()
        self.seleniumWrapper  = SeleniumWrapper(self.driver)
        self.updatedStockStats = 0
        self.scrappingDescriptionData ()

    def handleExit (self):
            self.seleniumWrapper.close()

    def downloadStockData (self, stockId):
            print ("==============================================")
            print ("Updated stocks: " + str(self.updatedStockStats))
            print ("Trying to download stats for stock id: " + stockId)

            stockData = ""
            try:
                url = "https://finance.yahoo.com/quote/" + stockId + "?p=" + stockId
                self.seleniumWrapper.getRequest  (url)
                stockData = self.seleniumWrapper.getTextByCSSSelector('#quote-summary')
            except:
                pass

            if (stockData!=""):
                self.updatedStockStats+=1

            return stockData

    def scrappingStockData (self):
        for i in range (len (self.stocksData)):
            stockData = self.downloadStockData (self.stocksData[i][self.stockIdIndex])
            self.recordStatsData(self.stocksData[i][self.stockIdIndex], stockData)

    def recordStatsData (self, stockId, parsedData):
        dict = {
                'Previous Close': '',
                'Open': '',
                'Bid': '',
                'Ask': '',
                'Day\'s Range': '',
                '52 Week Range': '',
                'Avg. Volume': '',
                'Volume': '',
                'Market Cap':'',
                'Beta (5Y Monthly)': '',
                'PE Ratio (TTM)': '',
                'EPS (TTM)': '',
                'Earnings Date': '',
                'Forward Dividend & Yield': '',
                'Ex-Dividend Date':'',
                '1y Target Est': ''
        }

        splited = parsedData.split('\n')
        splited = list(filter(None, splited))

        for i in range (len(splited)):
            for key,item in dict.items():
                result = splited[i].split(key + ' ')
                if (len(result)> 1):
                    dict[key] = result[1]
                    break
        print (dict)

        self.stocksDataBase.insertDataIntoStockStats (stockId,
                                  dict['Previous Close'],
                                  dict['Market Cap'],
                                  dict['Day\'s Range'],
                                  dict['52 Week Range'],
                                  dict['Avg. Volume'],
                                  '',
                                  dict['Beta (5Y Monthly)'],
                                  dict['PE Ratio (TTM)'],
                                  '',
                                  dict['EPS (TTM)'],
                                  dict['Forward Dividend & Yield'],
                                  dict['Ex-Dividend Date'])

    def downloadDescriptionData (self, stockId):
        print ("Trying to download a description for stock id: " + stockId)
        descriptionData = ""
        try:
            url = "https://finance.yahoo.com/quote/" + stockId + "/profile?p=" + stockId
            self.seleniumWrapper.getRequest  (url)
            descriptionData = self.seleniumWrapper.getTextByCSSSelector('p.Mt\(15px\)')
        except:
            pass

        return descriptionData

    def scrappingDescriptionData (self):
        for i in range (len (self.stocksData)):
            descriptionData = self.downloadDescriptionData (self.stocksData[i][self.stockIdIndex])
            self.recordDescriptionData(self.stocksData[i][self.stockIdIndex], descriptionData)

    def recordDescriptionData (self, stockId, description):
        print (description)
        self.stocksDataBase.insertDataIntoStockDescription (stockId, "", description)


yahooFinance = YahooFinanceWebScraper ()
"""
testString =
Previous Close 7.25
Open 7.26
Bid 7.46 x 4000
Ask 7.51 x 3100
Day's Range 7.14 - 7.56
52 Week Range 0.70 - 17.89
Volume 12,313,947
Avg. Volume 26,309,120
Market Cap 1.839B
Beta (5Y Monthly) 2.45
PE Ratio (TTM) N/A
EPS (TTM) -1.13
Earnings Date Mar 11, 2021
Forward Dividend & Yield N/A (N/A)
Ex-Dividend Date N/A
1y Target Est 10.00

yahooFinance.recordData('NNDM', testString)
"""
