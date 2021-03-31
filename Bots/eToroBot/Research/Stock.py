import os, sys
import time
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from log import Log
from driver import Driver
from parserEtoro import Parser
from seleniumWrapper import SeleniumWrapper

class Stock:
    def __init__(self, driver):
        self.log = Log('Stocks.log')
        self.driver = driver
        self.seleniumWrapper  = SeleniumWrapper(self.driver)

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
        self.driver.get(url)
        time.sleep(9)
        stockStatsRaw = ""
        try:
            #ToDo: change to get text by class name or id
            stockStatsRaw = self.seleniumWrapper.getTextByXpath('/html/body/ui-layout/div/div/div[2]/et-market/div/div/div/div[3]/et-market-stats/et-market-stats-overview/et-card/section/et-card-content/div[1]')
        except:
            self.log.write("Can get stats of " + url)
        return self.__makeDictionaryByStockStatsRaw(stockStatsRaw)

    def getStockPriceHistory (self, stockId):
        print ("getStockPriceHistory")
        self.driver.get('https://www.google.bg/search?q=' + stockId + '+stock')
        time.sleep(10)
        self.seleniumWrapper.clickElementByCssSelector('div.dQlDUb:nth-child(8) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1)',4)
        
        text = self.seleniumWrapper.getTextByCSSSelector('.uch-psvg')
        print (text)

        data = []
        #data[
        #[stockPrice, date]
        #]
        return data

    def getStockResearchData (self, stockId):
        print ("getStockResearchData")
        self.driver.get("https://www.etoro.com/markets/" + stockId + '/research')
        time.sleep(15)
        ##apt-graph-box > div:nth-child(2)
        #"//form[input/@name ='search']"
        #"//*[div/@class='search']"
        lowEstimate = self.seleniumWrapper.getTextByCSSSelector('.ew-content')
        #middleEstimate = self.seleniumWrapper.getTextByClassName('fb-price mb5')
        #highEstimate = self.seleniumWrapper.getTextByClassName('fb-price mb5 green')
        print (lowEstimate)
        data = []
        #data.append(lowEstimate)
        #data.append(middleEstimate)
        #data.append(highEstimate)
        print (data)
        return data

    def getStockDescription (self, stockId):
        print ("getStockDescription")
        self.driver.get("https://www.etoro.com/markets/" + stockId)
        time.sleep(10)

        self.seleniumWrapper.clickElementByCssSelector('et-showhide.ng-star-inserted:nth-child(2) > span:nth-child(1) > span:nth-child(3)',4)
        description = self.seleniumWrapper.getTextByCSSSelector('et-showhide.ng-star-inserted:nth-child(2) > span:nth-child(1) > span:nth-child(1)')
        print (description)
        print ("=============")
        exchange = self.seleniumWrapper.getTextByCSSSelector('a.widget-tag:nth-child(1)')
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
