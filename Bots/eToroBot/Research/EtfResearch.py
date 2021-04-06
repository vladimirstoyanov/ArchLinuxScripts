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
        self.indexStockId = 0
        self.indexStockName = 1
        self.indexSellPrice = 6
        self.indexBuyPrice = 7
        self.indexMinPrice = 8
        self.indexMaxPrice = 9
        self.sqliteData = SqliteDataEtoro ('etfs.db')
        self.log = Log('etf_research.log')
        driverObj = Driver ("/home/scitickart/.mozilla/firefox/w05kja2g.default")
        self.driver = driverObj.getDriver()
        self.markets = Markets(self.driver)
        self.stock = Stock (self.driver)

        self.allEtfs = self.markets.getAllEtfsInfo()
        self.recordDataDB()

    def handleExit (self):
        self.seleniumWrapper.close()

    def insertDataIntoStockDescription (self, stockId, descriptionData):
        self.sqliteData.insertDataIntoStockDescription (stockId, descriptionData[0], descriptionData[1])

    def insertDataIntoStockPriceHistory (self, stockId, historyData):
        for i in range (len (historyData)):
            self.sqliteData.insertDataIntoStockPriceHistory (stockId, historyData[i][0], historyData[i][1])

    def insertDataIntoStockResearch (self,stockId,researchData):
        self.sqliteData.insertDataIntoStockResearch (stock_id,
         researchData[0],
         researchData[1],
         researchData[2])

    def insertDataIntoStockStats (self,stockId, stockStats):
        self.sqliteData.insertDataIntoStockStats (stockId,
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
            self.sqliteData.insertDataIntoAllStocks (allStocksData[i][self.indexStockId],
            allStocksData[i][self.indexStockName],
            allStocksData[i][self.indexSellPrice],
            allStocksData[i][self.indexBuyPrice],
            allStocksData[i][self.indexMinPrice],
            allStocksData[i][self.indexMaxPrice])

    def recordDataDB (self):
        self.insertDataIntoAllStocks (self.allEtfs)
        for i in range (len(self.allEtfs)):
            data = self.stock.getStockDescription (self.allEtfs[i][self.indexStockId])
            self.insertDataIntoStockDescription(self.allEtfs[i][self.indexStockId], data)


etfResearch = EtfResearch()
