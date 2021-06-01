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
from datetime import datetime
import os, sys
from Markets import Markets
from Stock import Stock
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from log import Log
from driver import Driver
from sqliteData import SqliteDataEtoro


#open link - https://www.etoro.com/discover/markets/stocks/exchange/nasdaq
#check the lowest price and highest price of every stocks
#get the P/E ration of a stocks
#click > (next) button
class EtfResearch:
    def __init__(self):
        atexit.register(self.handleExit)
        self.__indexStockId = 0
        self.__indexStockName = 1
        self.__indexSellPrice = 6
        self.__indexBuyPrice = 7
        self.__indexMinPrice = 8
        self.__indexMaxPrice = 9
        self.__sqliteData = SqliteDataEtoro ('etfs.db')
        self.__log = Log('etf_research.log')
        driverObj = Driver ("/home/scitickart/.mozilla/firefox/w05kja2g.default")
        self.__driver = driverObj.getDriver()
        self.__markets = Markets(self.__driver)
        self.__stock = Stock (self.__driver)

        self.__allEtfs = self.__markets.getAllEtfsInfo()
        self.recordDataDB()

    def handleExit (self):
        self.__seleniumWrapper.close()

    def insertDataIntoStockDescription (self, stockId, descriptionData):
        self.__sqliteData.insertDataIntoStockDescription (stockId, descriptionData[0], descriptionData[1])

    def insertDataIntoStockPriceHistory (self, stockId, historyData):
        for i in range (len (historyData)):
            self.__sqliteData.insertDataIntoStockPriceHistory (stockId, historyData[i][0], historyData[i][1])

    def insertDataIntoStockResearch (self,stockId,researchData):
        self.__sqliteData.insertDataIntoStockResearch (stock_id,
         researchData[0],
         researchData[1],
         researchData[2])

    def insertDataIntoStockStats (self,stockId, stockStats):
        self.__sqliteData.insertDataIntoStockStats (stockId,
             stockStats['Prev Close'],
             stockStats['Market Cap'],
             stockStats['Day\'s Range'],
             stockStats['52 Week Range'],
             stockStats['Average Volume (3m)'],
             stockStats['1-Year Return'],
             stockStats['Beta'],
             stockStats['P/E Ratio'],
             stockStats['Revenue'],
             stockStats['EPS'],
             stockStats['Dividend (Yield)'])

    def insertDataIntoAllStocks (self, allStocksData):
        for i in range(len(allStocksData)):
            self.__sqliteData.insertDataIntoAllStocks (allStocksData[i][self.__indexStockId],
            allStocksData[i][self.__indexStockName],
            allStocksData[i][self.__indexSellPrice],
            allStocksData[i][self.__indexBuyPrice],
            allStocksData[i][self.__indexMinPrice],
            allStocksData[i][self.__indexMaxPrice])

    def recordDataDB (self):
        self.insertDataIntoAllStocks (self.__allEtfs)
        for i in range (len(self.__allEtfs)):
            data = self.__stock.getStockDescription (self.__allEtfs[i][self.__indexStockId])
            self.insertDataIntoStockDescription(self.__allEtfs[i][self.__indexStockId], data)


etfResearch = EtfResearch()
