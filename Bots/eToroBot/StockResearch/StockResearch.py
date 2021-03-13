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


#open link - https://www.etoro.com/discover/markets/stocks/exchange/nasdaq
#check the lowest price and highest price of every stocks
#get the P/E ration of a stocks
#click > (next) button
class StockResearch:
    def __init__(self):
        self.log = Log('stock_research.log')
        driverObj = Driver ("/home/scitickart/.mozilla/firefox/w05kja2g.default")
        self.driver = driverObj.getDriver()
        self.markets = Markets(self.driver)
        self.stock = Stock (self.driver)
        self.allStocks = self.markets.getAllMarketsInfo()
        #self.allStocks = [['NNDM', 'KPN', '0.013', '(0.43%)', 'S', '1.7', 'B', '1.7', '1.69', '2.97', '100%']]
        stocks = self.getDipStocksWithLowPE()
        self.exportDipStocksWithLowPE(stocks)

        #for test cases
        f = open('allStocks.txt','w')
        for i in range(len(self.allStocks)):
            f.write(str(self.allStocks[i]) + '\n')
        f.close()
        #self.stock.getStockStats ('NNDM')

    #get dip stocks with low p/e ratio
    #['KPN.NV', 'KPN', '0.013', '(0.43%)', 'S', '1.70', 'B', '2.959', '1.69', '2.97', '100%']

    def isStockWithDipPrice (self, buyPrice, minPrice, maxPrice):
        tolMaxMin = maxPrice - minPrice
        percentage = ((buyPrice-minPrice)/tolMaxMin) * 100
        print ("percentage: " + str(percentage))
        if (percentage<20):
            return 1
        return 0

    def isStockWithLowPE (self, stats):
        peRatio = stats['P/E Ratio']
        if (peRatio == ''): #it ignores stocks with missing P/E ratio
            return 0
        peRatio = float(peRatio)
        if (peRatio<26):
            return 1
        return 0

    def getDipStocksWithLowPE(self):
        dipStocks = []
        self.indexBuyPrice = 7
        self.indexMinPrice = 8
        self.indexMaxPrice = 9
        for i in range (len(self.allStocks)):
            buyPrice = float(self.allStocks[i][self.indexBuyPrice])
            minPrice = float(self.allStocks[i][self.indexMinPrice])
            maxPrice = float(self.allStocks[i][self.indexMaxPrice])
            print ("buy price:" + str(buyPrice))
            print ("min price:" + str(minPrice))
            print ("max price:" + str(maxPrice))
            if (self.isStockWithDipPrice(buyPrice, minPrice, maxPrice)):
                dipStocks.append(self.allStocks[i])

        print (dipStocks)
        result = []
        for i in range (len(dipStocks)):
            stats = self.stock.getStockStats (dipStocks[i][0])
            if (self.isStockWithLowPE(stats)):
                result.append([dipStocks[i], stats])

        return result

    def exportDipStocksWithLowPE (self, data):
        f = open('exportDipStocksWithLowPE.txt','w')
        for i in range (len(data)):
            print ("=========================")
            print ("Stock: " + data[i][0][0])
            print ("Buy price: " + data[i][0][self.indexBuyPrice])
            print ("Min price: " + data[i][0][self.indexMinPrice])
            print ("Max price: " + data[i][0][self.indexMaxPrice])
            print ("P/E ration: " + data[i][1]['P/E Ratio'])
            f.write("=========================\n")
            f.write("Stock: " + data[i][0][0] + '\n')
            f.write("Buy price: " + data[i][0][self.indexBuyPrice] + '\n')
            f.write("Min price: " + data[i][0][self.indexMinPrice] + '\n')
            f.write("Max price: " + data[i][0][self.indexMaxPrice] + '\n')
            f.write("P/E ration: " + data[i][1]['P/E Ratio'] + '\n')
        f.close()



stockResearch = StockResearch()
