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
        atexit.register(self.__handleExit)
        self.stocksDataBase = SqliteDataEtoro ('stocks.db')
        self.stocksData = self.stocksDataBase.readData ('all_stocks')
        self.stockIdIndex = 0
        self.log = Log('stock_research.log')
        driverObj = Driver ("/home/scitickart/.mozilla/firefox/w05kja2g.default")
        self.driver = driverObj.getDriver()
        self.seleniumWrapper  = SeleniumWrapper(self.driver)

    def __handleExit (self):
            self.seleniumWrapper.close()

    def __downloadStockData (self, stockId):
            print ("Trying to download stats for stock id: " + stockId)
            return self.__downloadData ("https://finance.yahoo.com/quote/" + stockId + "?p=" + stockId,
                                                '#quote-summary')
    #scrapping stock stats, stock description
    def scrappingData (self):
        for i in range (len (self.stocksData)):
            stockData = self.__downloadStockData (self.stocksData[i][self.stockIdIndex])
            self.__recordStatsData(self.stocksData[i][self.stockIdIndex], stockData)
            descriptionData = self.__downloadDescriptionData (self.stocksData[i][self.stockIdIndex])
            self.__recordDescriptionData(self.stocksData[i][self.stockIdIndex], descriptionData)

    def scrappingStockData (self):
        for i in range (len (self.stocksData)):
            stockData = self.__downloadStockData (self.stocksData[i][self.stockIdIndex])
            self.__recordStatsData(self.stocksData[i][self.stockIdIndex], stockData)

    def __generateStockDataDictionary (self, parsedData):
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
        return dict

    def __recordStatsData (self, stockId, parsedData):
        dict = self.__generateStockDataDictionary(parsedData)
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

    def __downloadData (self, url, cssSelector):
        data = ""
        try:
            self.seleniumWrapper.getRequest  (url)
            data = self.seleniumWrapper.getTextByCSSSelector(cssSelector)
        except:
            pass

        return data

    def __downloadDescriptionData (self, stockId):
        print ("Trying to download a description for stock id: " + stockId)
        return self.__downloadData ("https://finance.yahoo.com/quote/" + stockId + "/profile?p=" + stockId,
                                    'p.Mt\(15px\)')

    def scrappingDescriptionData (self):
        for i in range (len (self.stocksData)):
            descriptionData = self.__downloadDescriptionData (self.stocksData[i][self.stockIdIndex])
            self.__recordDescriptionData(self.stocksData[i][self.stockIdIndex], descriptionData)

    def __recordDescriptionData (self, stockId, description):
        print ("Description: " + description)
        self.stocksDataBase.insertDataIntoStockDescription (stockId, "", description)

if __name__ == "__main__":
    yahooFinance = YahooFinanceWebScraper ()
    yahooFinance.scrappingData ()
