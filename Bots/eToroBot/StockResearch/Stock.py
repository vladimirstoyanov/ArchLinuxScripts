import os, sys
import time
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from log import Log
from driver import Driver
from parserEtoro import Parser
from seleniumWrapper import SeleniumWrapper

#/html/body/ui-layout/div/div/div[2]/et-market/div/div/div/div[3]/et-market-stats/et-market-stats-overview/et-card/section/et-card-content/div[1]
class Stock:
    def __init__(self, driver):
        self.log = Log('Stocks.log')
        self.driver = driver
        self.seleniumWrapper  = SeleniumWrapper(self.driver)

    def __makeDictionaryByStockStatsRaw (self, stockStatsRaw):
        stockStatsSplited = stockStatsRaw.split('\n')
        stockStatsSplited = list(filter(None, stockStatsSplited))
        print (stockStatsSplited)
        data = {
                'Prev Close':'',
                'Day\'s Range':'',
                '52 Week Range':'',
                'Average Volume (3m)':'',
                '1-Year Return':'',
                'Beta':'',
                'Market Cap':'',
                'P/E Ratio':'',
                'Revenue':'',
                'EPS':'',
                'Dividend (Yield)':''
        }
        index = 0
        while (index<len(stockStatsSplited)):
            value = ""
            try:
                value = data[stockStatsSplited[index]]
            except:
                index+=1
                continue
            key = stockStatsSplited[index]
            index+=1
            try:
                value = data[stockStatsSplited[index]]
            except:
                data[key] = stockStatsSplited[index]
                index+=1

        return data

    #return a dictionay: stat -> value
    def getStockStats (self, stockId):
        url = 'https://www.etoro.com/markets/'
        url += stockId
        url += '/stats'
        print ("Trying to download " + url)
        self.driver.get(url)
        time.sleep(15)
        stockStatsRaw = ""
        try:
            stockStatsRaw = self.seleniumWrapper.getTextByXpath('/html/body/ui-layout/div/div/div[2]/et-market/div/div/div/div[3]/et-market-stats/et-market-stats-overview/et-card/section/et-card-content/div[1]')
        except:
            log.write("Can get stats of " + url)
        return self.__makeDictionaryByStockStatsRaw(stockStatsRaw)

"""
stock = Stock ()
testStr =
Prev Close
11.10
Day's Range
10.10 - 11.29
52 Week Range
4.20 - 17.85
Average Volume (3m)
34.47M
1-Year Return
107.00%
Beta
1.0669
Market Cap
511.33M
P/E Ratio
Revenue
3.42M
EPS
-1.2265
Dividend (Yield)
0 (0%)

result = stock.makeDictionaryByStockStatsRaw(testStr)
print (result)
"""
