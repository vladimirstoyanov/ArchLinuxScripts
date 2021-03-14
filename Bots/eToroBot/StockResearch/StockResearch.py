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
        #stocks = self.getDipStocksWithLowPE()

        self.indexBuyPrice = 7
        self.indexMinPrice = 8
        self.indexMaxPrice = 9

        #for test cases
        f = open('allStocks.txt','w')
        for i in range(len(self.allStocks)):
            f.write(str(self.allStocks[i]) + '\n')
        f.close()

        data=self.getDipStocks()
        dividends = self.getStocksWithDividends ()

    def calculatePercentage (self, buyPrice, minPrice, maxPrice):
        tolMaxMin = maxPrice - minPrice
        percentage = ((buyPrice-minPrice)/tolMaxMin) * 100
        print ("percentage: " + str(percentage))
        return percentage

    #get dip stocks with low p/e ratio
    def isStockWithDipPrice (self, buyPrice, minPrice, maxPrice):
        percentage = self.calculatePercentage ()
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
        dipStocksWithLowerPE = "dipStocksWithLowerPE.txt"
        self.cleanFile(dipStocksWithLowerPE)
        dipStocks = []
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
                self.exportStockPlusStats([dipStocks[i], stats], dipStocksWithLowerPE)

        return result

    def getDipStocks (self):
        dipStocksFile = 'dipStocks.txt'
        self.cleanFile(dipStocksFile)
        dipStocks = []
        for i in range (len(self.allStocks)):
            buyPrice = float(self.allStocks[i][self.indexBuyPrice])
            minPrice = float(self.allStocks[i][self.indexMinPrice])
            maxPrice = float(self.allStocks[i][self.indexMaxPrice])
            print ("buy price:" + str(buyPrice))
            print ("min price:" + str(minPrice))
            print ("max price:" + str(maxPrice))
            percentage = self.calculatePercentage(buyPrice, minPrice, maxPrice)
            if (percentage < 5.5):
                dipStocks.append (self.allStocks[i])
                self.exportStock (self.allStocks[i], dipStocksFile)

        return dipStocks

    def cleanFile (self, filename):
        f = open(filename, 'w')
        f.close()

    def exportStock (self, data, filename):
            f = open (filename, 'a')
            f.write("=========================\n")
            f.write("Stock index: " + data[0] + '\n')
            f.write("Stock name: " + data[1] + '\n')
            f.write("Stock exchange: " + data[11] + '\n')
            f.write("Sell price: " + data[5] + '\n')
            f.write("Buy price: " + data[self.indexBuyPrice] + '\n')
            f.write("Min price: " + data[self.indexMinPrice] + '\n')
            f.write("Max price: " + data[self.indexMaxPrice] + '\n')
            f.close()

    def exportStockPlusStats (self, data, filename):
            f = open (filename, 'a')
            f.write("=========================\n")
            f.write("Stock index: " + data[0][0] + '\n')
            f.write("Stock name: " + data[0][1] + '\n')
            f.write("Stock exchange: " + data[0][11] + '\n')
            f.write("Sell price: " + data[0][5] + '\n')
            f.write("Buy price: " + data[0][self.indexBuyPrice] + '\n')
            f.write("Min price: " + data[0][self.indexMinPrice] + '\n')
            f.write("Max price: " + data[0][self.indexMaxPrice] + '\n')
            f.write('Prev Close: ' + data[1]['Prev Close'] + '\n')
            f.write('Day\'s Range: '+ data[1]['Day\'s Range'] + '\n')
            f.write('52 Week Range: '+ data[1]['52 Week Range'] + '\n')
            f.write('Average Volume (3m): '+ data[1]['Average Volume (3m)'] + '\n')
            f.write('1-Year Return: '+ data[1]['1-Year Return'] + '\n')
            f.write('Beta: '+ data[1]['Beta'] + '\n')
            f.write('Market Cap: '+ data[1]['Market Cap'] + '\n')
            f.write('P/E Ratio: '+ data[1]['P/E Ratio'] + '\n')
            f.write('Revenue: '+ data[1]['Revenue'] + '\n')
            f.write('EPS: '+ data[1]['EPS'] + '\n')
            f.write('Dividend (Yield): '+ data[1]['Dividend (Yield)'] + '\n')
            f.close()

    def getStocksWithDividends (self):
        dividendsFile = 'dividendStocks.txt'
        allStocksFile = 'allStocksAndStats.txt'
        self.cleanFile(dividendsFile)
        self.cleanFile(allStocksFile)
        dividendStocks = []
        for i in range (len(self.allStocks)):
            stats = self.stock.getStockStats (self.allStocks[i][0])
            self.exportStockPlusStats([self.allStocks[i], stats], allStocksFile)
            print ("Dividend: " + stats['Dividend (Yield)'])
            if (stats['Dividend (Yield)']!='0' and stats['Dividend (Yield)']!=''):
                print ("Added.")
                dividendStocks.append([self.allStocks[i], stats])
                self.exportStockPlusStats([self.allStocks[i], stats], dividendsFile)
        return dividendStocks

stockResearch = StockResearch()
