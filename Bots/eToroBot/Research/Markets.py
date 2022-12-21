import os, sys
import time
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from parserEtoro import Parser
sys.path.insert(1, '../../../Selenium/')
from seleniumWrapper import SeleniumWrapper
from log import Log
from driverFirefox import Driver

class Markets:
    def __init__(self, driver):
        self.__seleniumWrapper = SeleniumWrapper(driver)
        self.__stockMarkets = {
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
        self.__etfMarkets = {
            'ETF': 'https://www.etoro.com/discover/markets/etf'
        }

        self.__driver = driver

    def getETFMarkets (self):
        return self.__etfMarkets

    def getStockMarkets (self):
        return self.__stockMarkets

    def getMarketInfo (self, marketName, dictMarkets):
        print ("Tyring to load: " + marketName + ": " + dictMarkets[marketName])

        #self.__seleniumWrapper.getRequestWaitUntilLocatedElementByCssSelector (
        #            dictMarkets[marketName],
        #            '.market-list')
        self.__seleniumWrapper.getRequest(dictMarkets[marketName])
        stocks = []
        while (True):
            #.market-list
            stocksInfo = self.__seleniumWrapper.getTextByCSSSelector('.market-list')
            #stocksInfo = self.__driver.find_element_by_xpath("/html/body/ui-layout/div/div/div[2]/et-discovery-markets-results/div/div")
            parser = Parser ()
            currentStocks = parser.parseStocksInfo(stocksInfo, marketName)
            for i in range (len(currentStocks)):
                stocks.append(currentStocks[i])
            try:
                currentStockCount = self.__seleniumWrapper.getTextByXpath('/html/body/app-root/et-layout-main/div/div[2]/div[2]/div[3]/div/ui-layout/ng-view/et-discovery-markets-results/div/et-discovery-markets-results-header/div/div[2]/div/div[1]/span[2]/span[1]')
                print ("currentStockCount: " + str(currentStockCount))
                maxStockCount = self.__seleniumWrapper.getTextByXpath('/html/body/app-root/et-layout-main/div/div[2]/div[2]/div[3]/div/ui-layout/ng-view/et-discovery-markets-results/div/et-discovery-markets-results-header/div/div[2]/div/div[1]/span[2]/span[3]')
                print ("maxStockCount: " + str(maxStockCount))
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
                element = self.__seleniumWrapper.getTextByCSSSelector('.nav-button-right')
            except:
                print ("Can't find the next button")
                time.sleep(10)
                break

            self.__seleniumWrapper.clickElementByCssSelector('.nav-button-right', 4)

        return stocks

    def getAllMarketsInfo (self):
        stocks = []
        for key,vlaue in  self.__stockMarkets.items():
            currentStocks = self.getMarketInfo(key, self.__stockMarkets)
            for j in range(len(currentStocks)):
                stocks.append(currentStocks[j])
        return stocks

    def getAllEtfsInfo (self):
        etfs = []
        for key,vlaue in  self.__etfMarkets.items():
            currentEtfs = self.getMarketInfo(key, self.__etfMarkets)
            for j in range(len(currentEtfs)):
                etfs.append(currentEtfs[j])
        return etfs
