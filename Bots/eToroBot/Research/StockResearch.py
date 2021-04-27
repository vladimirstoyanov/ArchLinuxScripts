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

class StockResearch:
    def __init__(self):
        atexit.register(self.__handleExit)
        self.indexStockId = 0
        self.indexStockName = 1
        self.indexSellPrice = 6
        self.indexBuyPrice = 7
        self.indexMinPrice = 8
        self.indexMaxPrice = 9
        self.indexStats = 11
        self.sqliteData = SqliteDataEtoro ('stocks.db')
        self.log = Log('stock_research.log')
        driverObj = Driver ("/home/scitickart/.mozilla/firefox/w05kja2g.default")
        self.driver = driverObj.getDriver()
        self.markets = Markets(self.driver)
        self.stock = Stock (self.driver)

        allStocks = self.markets.getAllMarketsInfo()
        self.insertDataIntoAllStocks(allStocks)
        print ("getVolatileStocks")
        self.getVolatileStocks ()
        print ("getDipStocksWithLowPE")
        self.getDipStocksWithLowPE()
        print ("getStocksWithDividends")
        self.getStocksWithDividends ()

    def __handleExit (self):
        self.seleniumWrapper.close()

    def insertDataIntoAllStocks (self, allStocksData):
        for i in range(len(allStocksData)):
            self.sqliteData.insertDataIntoAllStocks (allStocksData[i][self.indexStockId],
            allStocksData[i][self.indexStockName],
            allStocksData[i][self.indexSellPrice],
            allStocksData[i][self.indexBuyPrice],
            allStocksData[i][self.indexMinPrice],
            allStocksData[i][self.indexMaxPrice])

    def calculateDayRangePercentage (self, minDayPrice, maxDayPrice):
        return ((maxDayPrice-minDayPrice)/maxDayPrice)*100

    def calculatePercentage (self, buyPrice, minPrice, maxPrice):
        tolMaxMin = maxPrice - minPrice
        percentage = ((buyPrice-minPrice)/tolMaxMin) * 100
        print ("percentage: " + str(percentage))
        return percentage

    #get dip stocks with low p/e ratio
    def isStockWithDipPrice (self, buyPrice, minPrice, maxPrice):
        percentage = self.calculatePercentage (buyPrice, minPrice, maxPrice)
        if (percentage<15):
            return 1
        return 0

    def isStockWithLowPE (self, peRatio):
        if (peRatio == '' or peRatio == 'N/A'): #it ignores stocks with missing P/E ratio
            return 0
        peRatio = float(peRatio)
        if (peRatio<26):
            return 1
        return 0

    def getDipStocksWithLowPE (self):
        filename = 'dipStocksWithLowPE.txt'
        stockStats = self.sqliteData.readData('stock_stats')
        allStocks = self.sqliteData.readData('all_stocks')
        self.cleanFile(filename)
        f = open (filename)
        for i in range (len(allStocks)):
            if (self.isStockWithDipPrice(float(allStocks[i][3]), float(allStocks[i][4]), float(allStocks[i][5]))):
                for j in range (len (stockStats)):
                    if (allStocks[i][0] == stockStats[j][0]):
                        if (self.isStockWithLowPE (stockStats[j][8])):
                            self.exportStockPlusStats(allStocks[i], stockStats[j], filename)
        f.close()

    def exportStock (self, stock, fileDescriptor):
        fileDescriptor.write("=============\n")
        fileDescriptor.write("Stock id: " + stock[0] +"\n")
        fileDescriptor.write("Stock name: " +stock[1] + "\n")
        fileDescriptor.write("Sell price: " + stock[2] + "\n")
        fileDescriptor.write("Buy price: " + stock[3] + "\n")
        fileDescriptor.write("Min prie: " + stock[4] + "\n")
        fileDescriptor.write("Max price: " + stock[5] + "\n")

    def exportStats (self, stats, fileDescriptor):
        fileDescriptor.write("Stock ID: " + stats[0] + "\n")
        fileDescriptor.write("Previous close: " + stats[1]+ "\n")
        fileDescriptor.write("Market cap: " + stats[2]+ "\n")
        fileDescriptor.write("Days range: " + stats[3]+ "\n")
        fileDescriptor.write("52 week range: " + stats[4]+ "\n")
        fileDescriptor.write("Average volume: " + stats[5]+ "\n")
        fileDescriptor.write("1 year return: " + stats[6]+ "\n")
        fileDescriptor.write("Beta: " + stats[7]+ "\n")
        fileDescriptor.write("P/E ratio: " + stats[8]+ "\n")
        fileDescriptor.write("Revenue: " + stats[9]+ "\n")
        fileDescriptor.write("EPS: " + stats[10]+ "\n")
        fileDescriptor.write("Dividend: " + stats[11]+ "\n")

    def exportStockPlusStats (self, stocks, stats, filename):
        f = open(filename, 'a')
        self.exportStock (stocks, f)
        self.exportStats (stats, f)
        f.close()

    def getVolatileStocks (self):
        volatileStocks = 'volatileStocks.txt'
        stats = self.sqliteData.readData('stock_stats')
        allStocks = self.sqliteData.readData('all_stocks')
        self.cleanFile(volatileStocks)
        for i in range (len(allStocks)):
            for j in range (len(stats)):
                if (allStocks[i][0]==stats[j][0]):
                    dayRange = stats[j][3]
                    dayRange = dayRange.replace(' ','')
                    minMax = dayRange.split('-')
                    if (len(minMax)!=2):
                        continue
                    if (minMax[0]=='N/A' or minMax[1] == 'N/A'):
                        continue
                    minMax[0] = minMax[0].replace(',','')
                    minMax[1] = minMax[1].replace(',','')
                    minDayPrice = float(minMax[0])
                    maxDayPrice = float(minMax[1])
                    dayRangePercentage = self.calculateDayRangePercentage(minDayPrice,maxDayPrice)
                    self.log.write("Min: " + str(minDayPrice) + ", Max: " + str(maxDayPrice) + ", Range: " + str(dayRangePercentage))
                    if (dayRangePercentage >= 5):
                        self.exportStockPlusStats(allStocks[i], stats[j], volatileStocks)
                    break

    def cleanFile (self, filename):
        f = open(filename, 'w')
        f.close()

    def getStocksWithDividends (self):
        dividendsFile = 'dividendStocks.txt'
        self.cleanFile(dividendsFile)
        stats = self.sqliteData.readData('stock_stats')
        allStocks = self.sqliteData.readData('all_stocks')
        for i in range (len(allStocks)):
            for j in range (len(stats)):
                if (allStocks[i][0] == stats[j][0]):
                    if (stats[j][11]!='0' and stats[j][11]!='' and stats[j][11]!='N/A (N/A)'):
                        print ("Export sDividend: " + stats[j][11])
                        self.exportStockPlusStats(allStocks[i], stats[j], dividendsFile)

stockResearch = StockResearch()
