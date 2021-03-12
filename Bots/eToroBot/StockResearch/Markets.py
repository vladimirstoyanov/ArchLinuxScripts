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
            #'Amsterdam exchange' : 'https://www.etoro.com/discover/markets/stocks/exchange/amsterdam',
            #'Brussles exchange' : 'https://www.etoro.com/discover/markets/stocks/exchange/brussels',
            #'Copenhagen exchange' :'https://www.etoro.com/discover/markets/stocks/exchange/copenhagen',
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
        self.driver = driver

    def getStockMarkets (self):
        return self.stockMarkets

    def getMarketInfo (self, marketName):
        print ("Tyring to load: " + marketName + ": " + self.stockMarkets[marketName])
        self.driver.get(self.stockMarkets[marketName])
        time.sleep(15)
        stocks = []
        while (True):
            stocksInfo = self.driver.find_element_by_xpath("/html/body/ui-layout/div/div/div[2]/et-discovery-markets-results/div/div")
            parser = Parser ()
            currentStocks = parser.parseStocksInfo(stocksInfo.text)
            for i in range (len(currentStocks)):
                stocks.append(currentStocks[i])
            try:
                currentStockCount = self.seleniumWrapper.getTextByXpath('/html/body/ui-layout/div/div/div[2]/et-discovery-markets-results/div/et-discovery-markets-results-header/div/div[2]/div/div[1]/span[2]/span[1]')
                maxStockCount = self.seleniumWrapper.getTextByXpath('/html/body/ui-layout/div/div/div[2]/et-discovery-markets-results/div/et-discovery-markets-results-header/div/div[2]/div/div[1]/span[2]/span[3]')
                splited = currentStockCount.split('-')
                if (splited[1] == maxStockCount):
                    print ("It reaches max count of the stocks")
                    break
            except:
                print ("End text")
                break

            try:
                #    #<span _ngcontent-woq-c21="" class="nav-button-right sprite"></span>
                self.seleniumWrapper.clickElementByCssSelector('.nav-button-right', 4)
            except:
                print ("End")
                break



    def getAllMarketsInfo (self):
        for key,vlaue in  self.stockMarkets.items():
            self.getMarketInfo(key)
