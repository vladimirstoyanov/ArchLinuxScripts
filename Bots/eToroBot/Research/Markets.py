import os, sys
import time
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from log import Log
from driver import Driver
from parserEtoro import Parser
from seleniumWrapper import SeleniumWrapper

class Markets:
    def __init__(self, driver):
        self.seleniumWrapper = SeleniumWrapper(driver)
        self.stockMarkets = {
            'Amsterdam exchange' : 'https://www.etoro.com/discover/markets/stocks/exchange/amsterdam',
            'Brussles exchange' : 'https://www.etoro.com/discover/markets/stocks/exchange/brussels',
            'Copenhagen exchange' :'https://www.etoro.com/discover/markets/stocks/exchange/copenhagen',
            'Frankfurt exchage':'https://www.etoro.com/discover/markets/stocks/exchange/frankfurt',
            'Helsinki exchage':'https://www.etoro.com/discover/markets/stocks/exchange/helsinki',
            'Hongkong exchange':'https://www.etoro.com/discover/markets/stocks/exchange/hongkong',
            'Lisabon exchange':'https://www.etoro.com/discover/markets/stocks/exchange/lisbon',
            'London exchange':'https://www.etoro.com/discover/markets/stocks/exchange/london',
            'Madrid exchage':'https://www.etoro.com/discover/markets/stocks/exchange/bolsademadrid',
            'Milano exchage':'https://www.etoro.com/discover/markets/stocks/exchange/borsaitaliana',
            'NASDAQ':'https://www.etoro.com/discover/markets/stocks/exchange/nasdaq',
            'NYSE':'https://www.etoro.com/discover/markets/stocks/exchange/nyse',
            'Oslo exchage':'https://www.etoro.com/discover/markets/stocks/exchange/oslo',
            'Paris exchage':'https://www.etoro.com/discover/markets/stocks/exchange/paris',
            'Saudi arabia exchange':'https://www.etoro.com/discover/markets/stocks/exchange/tadawul',
            'Stockholm exchage':'https://www.etoro.com/discover/markets/stocks/exchange/stockholm',
            'Zurich exchange':'https://www.etoro.com/discover/markets/stocks/exchange/zurich'
        }
        self.etfMarkets = {
            'ETF': 'https://www.etoro.com/discover/markets/etf'
        }

        self.driver = driver

    def getETFMarkets (self):
        return self.etfMarkets

    def getStockMarkets (self):
        return self.stockMarkets

    def getMarketInfo (self, marketName, dictMarkets):
        print ("Tyring to load: " + marketName + ": " + dictMarkets[marketName])

        #self.seleniumWrapper.getRequestWaitUntilLocatedElementByCssSelector (
        #            dictMarkets[marketName],
        #            '.market-list')
        self.seleniumWrapper.getRequest(dictMarkets[marketName])
        stocks = []
        while (True):
            #.market-list
            stocksInfo = self.seleniumWrapper.getTextByCSSSelector('.market-list')
            #stocksInfo = self.driver.find_element_by_xpath("/html/body/ui-layout/div/div/div[2]/et-discovery-markets-results/div/div")
            parser = Parser ()
            currentStocks = parser.parseStocksInfo(stocksInfo, marketName)
            for i in range (len(currentStocks)):
                stocks.append(currentStocks[i])
            try:
                currentStockCount = self.seleniumWrapper.getTextByXpath('/html/body/ui-layout/div/div/div[2]/et-discovery-markets-results/div/et-discovery-markets-results-header/div/div[2]/div/div[1]/span[2]/span[1]')
                maxStockCount = self.seleniumWrapper.getTextByXpath('/html/body/ui-layout/div/div/div[2]/et-discovery-markets-results/div/et-discovery-markets-results-header/div/div[2]/div/div[1]/span[2]/span[3]')
                #check if it is the last page
                splited = currentStockCount.split('-')
                if (splited[1] == maxStockCount):
                    print ("It is the last page.")
                    break
            except:
                print ("End text")
                break

            try:
                #click on the next page button
                element = self.driver.find_element_by_css_selector('.nav-button-right')
            except:
                print ("End")
                break

            self.seleniumWrapper.clickElementByCssSelector('.nav-button-right', 4)

        return stocks

    def getAllMarketsInfo (self):
        stocks = []
        for key,vlaue in  self.stockMarkets.items():
            currentStocks = self.getMarketInfo(key, self.stockMarkets)
            for j in range(len(currentStocks)):
                stocks.append(currentStocks[j])
        return stocks

    def getAllEtfsInfo (self):
        etfs = []
        for key,vlaue in  self.etfMarkets.items():
            currentEtfs = self.getMarketInfo(key, self.etfMarkets)
            for j in range(len(currentEtfs)):
                etfs.append(currentEtfs[j])
        return etfs
