import os, sys
import time
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from parserEtoro import Parser
sys.path.insert(1, '../../../Selenium/')
from log import Log
from driver import Driver
from seleniumWrapper import SeleniumWrapper

class Stock:
    def __init__(self, driver):
        self.__log = Log('Stocks.log')
        self.__driver = driver
        self.__seleniumWrapper  = SeleniumWrapper(self.__driver)

    def dividendPercentage (self, dividendString):
        fromIndex = dividendString.find ('(')
        fromIndex+=1
        toIndex = dividendString.find ('%')
        percentageString = ""
        for i in range (fromIndex, toIndex, 1):
            percentageString += dividendString[i]

        return percentageString

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

        data['Dividend (Yield)'] = self.dividendPercentage (data['Dividend (Yield)'])

        return data

    #return a dictionay: stat -> value
    def getStockStats (self, stockId):
        url = 'https://www.etoro.com/markets/'
        url += stockId
        url += '/stats'
        print ("Trying to download " + url)
        #self.__seleniumWrapper.getRequestWaitUntilLocatedElementByXpath(
        #                url,
        #                '/html/body/ui-layout/div/div/div[2]/et-market/div/div/div/div[3]/et-market-stats/et-market-stats-overview/et-card/section/et-card-content/div[1]')
        self.__seleniumWrapper.getRequest(url)
        stockStatsRaw = ""
        try:
            #ToDo: change to get text by class name or id
            stockStatsRaw = self.__seleniumWrapper.getTextByXpath('/html/body/ui-layout/div/div/div[2]/et-market/div/div/div/div[3]/et-market-stats/et-market-stats-overview/et-card/section/et-card-content/div[1]')
        except:
            self.__log.write("Can get stats of " + url)
        return self.__makeDictionaryByStockStatsRaw(stockStatsRaw)

    def getStockPriceHistory (self, stockId):
        print ("getStockPriceHistory")
        #self.__seleniumWrapper.getRequestWaitUntilLocatedElementByCssSelector (
        #                    'https://www.google.bg/search?q=' + stockId + '+stock',
        #                    '.uch-psvg')
        self.__seleniumWrapper.getRequest('https://www.google.bg/search?q=' + stockId + '+stock')
        self.__seleniumWrapper.clickElementByCssSelector('div.dQlDUb:nth-child(8) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1)',4)

        text = self.__seleniumWrapper.getTextByCSSSelector('.uch-psvg')
        print (text)

        data = []
        #data[
        #[stockPrice, date]
        #]
        return data

    def getStockResearchData (self, stockId):
        print ("getStockResearchData")
        #self.__seleniumWrapper.getRequestWaitUntilLocatedElementByCssSelector (
        #                    "https://www.etoro.com/markets/" + stockId + "/research",
        #                    '.ew-content')
        self.__seleniumWrapper.getRequest ( "https://www.etoro.com/markets/" + stockId + "/research")
        ##apt-graph-box > div:nth-child(2)
        #"//form[input/@name ='search']"
        #"//*[div/@class='search']"
        lowEstimate = self.__seleniumWrapper.getTextByCSSSelector('.ew-content')
        #middleEstimate = self.__seleniumWrapper.getTextByClassName('fb-price mb5')
        #highEstimate = self.__seleniumWrapper.getTextByClassName('fb-price mb5 green')
        print (lowEstimate)
        data = []
        #data.append(lowEstimate)
        #data.append(middleEstimate)
        #data.append(highEstimate)
        print (data)
        return data

    def getStockDescription (self, stockId):
        print ("getStockDescription")
        #self.__seleniumWrapper.getRequestWaitUntilLocatedElementByCssSelector (
        #                        "https://www.etoro.com/markets/" + stockId,
        #                        'et-showhide.ng-star-inserted:nth-child(2) > span:nth-child(1) > span:nth-child(3)')
        self.__seleniumWrapper.getRequest ("https://www.etoro.com/markets/" + stockId)
        self.__seleniumWrapper.clickElementByCssSelector('et-showhide.ng-star-inserted:nth-child(2) > span:nth-child(1) > span:nth-child(3)',4)
        description = self.__seleniumWrapper.getTextByCSSSelector('et-showhide.ng-star-inserted:nth-child(2) > span:nth-child(1) > span:nth-child(1)')
        print (description)
        print ("=============")
        exchange = self.__seleniumWrapper.getTextByCSSSelector('a.widget-tag:nth-child(1)')
        print (exchange)
        data = []
        data.append(exchange)
        data.append (description)
        return data

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
