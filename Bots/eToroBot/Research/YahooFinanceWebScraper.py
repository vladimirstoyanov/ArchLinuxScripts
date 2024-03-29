#ToDo: get profile data: https://finance.yahoo.com/quote/NNDM/profile?p=NNDM
import time
import os, sys
import atexit
import pickle
import time
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from sqliteData import SqliteDataEtoro
sys.path.insert(1, '../../../Selenium/')
from seleniumWrapper import SeleniumWrapper
from log import Log
from driverFirefox import Driver

class YahooFinanceWebScraper:
    def __init__ (self):
        atexit.register(self.__handleExit)
        self.__stocksDataBase = SqliteDataEtoro ('stocks.db')
        self.__stocksData = self.__stocksDataBase.readData ('all_stocks')
        self.__stockIdIndex = 0
        self.__log = Log('stock_research.log')
        driverObj = Driver ("/home/vladimir/.mozilla/firefox/q54e1nbe.default-release")
        self.__driver = driverObj.getDriver()
        self.__seleniumWrapper  = SeleniumWrapper(self.__driver)

    def __handleExit (self):
            self.__seleniumWrapper.close()

    def __downloadStockData (self, stockId):
            print ("Trying to download stats for stock id: " + stockId)
            return self.__downloadData ("https://finance.yahoo.com/quote/" + stockId + "?p=" + stockId,
                                                '#quote-summary')
    #scrapping stock stats, stock description
    def scrappingData (self):
        for i in range (len (self.__stocksData)):
            stockData = self.__downloadStockData (self.__stocksData[i][self.__stockIdIndex])
            self.__recordStatsData(self.__stocksData[i][self.__stockIdIndex], stockData)
            descriptionData = self.__downloadDescriptionData (self.__stocksData[i][self.__stockIdIndex])
            self.__recordDescriptionData(self.__stocksData[i][self.__stockIdIndex], descriptionData)

    def scrappingStockData (self):
        for i in range (len (self.__stocksData)):
            stockData = self.__downloadStockData (self.__stocksData[i][self.__stockIdIndex])
            self.__recordStatsData(self.__stocksData[i][self.__stockIdIndex], stockData)

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
        self.__stocksDataBase.insertDataIntoStockStats (stockId,
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
            self.__seleniumWrapper.getRequest  (url)
            data = self.__seleniumWrapper.getTextByCSSSelector(cssSelector)
        except:
            pass

        return data

    def __downloadDescriptionData (self, stockId):
        print ("Trying to download a description for stock id: " + stockId)
        return self.__downloadData ("https://finance.yahoo.com/quote/" + stockId + "/profile?p=" + stockId,
                                    'p.Mt\(15px\)')

    def scrappingDescriptionData (self):
        for i in range (len (self.__stocksData)):
            descriptionData = self.__downloadDescriptionData (self.__stocksData[i][self.__stockIdIndex])
            self.__recordDescriptionData(self.__stocksData[i][self.__stockIdIndex], descriptionData)

    def __recordDescriptionData (self, stockId, description):
        print ("Description: " + description)
        self.__stocksDataBase.insertDataIntoStockDescription (stockId, "", description)

if __name__ == "__main__":
    yahooFinance = YahooFinanceWebScraper ()
    yahooFinance.scrappingData ()
