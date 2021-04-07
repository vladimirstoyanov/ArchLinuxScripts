import pickle
import sys
import time
import atexit
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.firefox.webdriver import FirefoxProfile
from datetime import datetime
from driver import Driver
from log import Log
from seleniumWrapper import SeleniumWrapper

class Config ():
    def __init__ (self):
        self.configData = []
        self.readConfig()

    def readConfig (self):
        self.configData = []
        f = open ('config', 'r')
        for row in f.readlines():
            lData = row.split(';')
            lData[len(lData)-1] = lData[len(lData)-1].replace('\n','')
            lData[len(lData)-1] = lData[len(lData)-1].replace('\r','')
            self.configData.append(lData)
        f.close()

class EToroBot:
    def __init__ (self):
        atexit.register(self.handleExit)
        self.log = Log('eToroLog.log')
        driverObj = Driver("/home/scitickart/.mozilla/firefox/w05kja2g.default")
        self.driver = driverObj.getDriver()
        self.seleniumWrapper = SeleniumWrapper(self.driver)
        self.loadEToro()
        self.monitorStocks()

    def handleExit (self):
        self.seleniumWrapper.close()

    def loadEToro(self):
        #self.seleniumWrapper.getRequestWaitUntilLocatedElementByXpath (
        #    'https://www.etoro.com/watchlists/4e42a954-1ce2-4938-87b3-4c9adad0608b',
        #    '/html/body/ui-layout/div/div/div[2]/et-watchlist/div[2]/div/et-watchlist-list/section/section[1]')
        self.seleniumWrapper.getRequest('https://www.etoro.com/watchlists/4e42a954-1ce2-4938-87b3-4c9adad0608b')

    def loadStockPage (self, stockIndex):
        #self.seleniumWrapper.getRequestWaitUntilLocatedElementByCssSelector (
        #            'https://www.etoro.com/markets/' + stockIndex + '/chart',
        #            '.i-stock-chart-info')
        self.seleniumWrapper.getRequest('https://www.etoro.com/markets/' + stockIndex + '/chart')

    def buyStock (self, price, stockIndex):
        self.loadStockPage(stockIndex)

        self.seleniumWrapper.clickElementByCssSelector('.head-instrument-action > trade-button:nth-child(2)', 5)
        self.log.write("Trade button clicked...")

        self.seleniumWrapper.setTextFieldByCSSSelector('.stepper-value', price)
        self.log.write("Price set...")
        time.sleep(4)


        for i in range(5):
                try:
                    self.seleniumWrapper.clickElementByCssSelector('.execution-button', 5)
                    self.log.write('Clicking on Open Trade button')
                except:
                    pass

        self.loadEToro()


    def sellStock (self, stockIndex):
        self.loadStockPage(stockIndex)

        self.seleniumWrapper.clickElementByCssSelector('.i-stock-chart-info',5)
        self.log.write("stock button clicked...")

        self.seleniumWrapper.clickElementByCssSelector('div.e-btn:nth-child(2) > span:nth-child(1)',5)
        self.log.write('x button clicked')

        self.seleniumWrapper.clickElementByCssSelector(".w-sm-footer-button",5)
        self.log.write('Close Trade button clicked')

        self.loadEToro()

    def setSellPrice (self, stockId, price):
        self.log.write('Setting a sell price for ' + stockId)
        #self.seleniumWrapper.getRequestWaitUntilLocatedElementByCssSelector (
        #                'https://www.etoro.com/portfolio/' + stockId,
        #                'div.ui-table-row:nth-child(3) > ui-table-body-slot:nth-child(2) > ui-table-cell:nth-child(6) > span:nth-child(1)')
        self.seleniumWrapper.getRequest('https://www.etoro.com/portfolio/' + stockId)

        self.log.write('Trying to click on update price button...')
        #click button to update the price
        self.seleniumWrapper.clickElementByCssSelector ('div.ui-table-row:nth-child(3) > ui-table-body-slot:nth-child(2) > ui-table-cell:nth-child(6) > span:nth-child(1)', 7)

        linkString = self.seleniumWrapper.getTextByCSSSelector ('.link')
        if (linkString == "Set TP"):
            self.log.write('Trying to click \'set price\' link ')
            #click on 'set price' link (it possible to can't find it, because it doesn't exist sometimes)
            self.seleniumWrapper.clickElementByCssSelector ('.link', 4)

        self.log.write('Trying to setting the price')
        #set the sell price
        self.seleniumWrapper.setTextFieldByCSSSelector('.stepper-value', price)

        for i in range(5):
                try:
                    self.seleniumWrapper.clickElementByCssSelector ('.button-blue', 5)
                    self.log.write('Clicking on Update button (set price widget)')
                except:
                    pass

        self.loadEToro()

    def getAvailableCash (self):
        cash = 0
        try:
            cash = self.seleniumWrapper.getTextByCSSSelector ('div.footer-unit:nth-child(1) > span:nth-child(1)')
            cash = cash.replace ('$', '')
        except:
            self.log.write("Can't get available cash!")
        return float(cash)

    def monitorStocks(self):
        self.config = Config()
        iteration=0
        while True:
            cash = self.getAvailableCash()
            self.log.write("Cash: " + str(cash))

            if (cash < 0.99):
                time.sleep(5)
                continue

            self.config.readConfig()
            configData = self.config.configData

            stocksInfo = self.driver.find_element_by_xpath('/html/body/ui-layout/div/div/div[2]/et-watchlist/div[2]/div/et-watchlist-list/section/section[1]')

            listResult = stocksInfo.text.split('\n')
            lPart = []
            lResult = []
            index = 0
            for i in range(0,len(listResult)):
                if (listResult[i] == 'BUYING' or listResult[i] == 'SELLING'):
                    index+=1
                    lPart.append(listResult[i])
                    if (len(lPart) == 9):
                        lPart.insert(1,' ')
                    for j in range (len(configData)):
                        if (lPart[0] == configData[j][0]):
                            lPart.append(str(index))
                            lResult.append(lPart)
                            break
                    lPart = []
                else:
                    lPart.append(listResult[i])

            print (lResult)

            for i in range (len(lResult)):
                sellPrice = float(lResult[i][5])
                buyPrice = float(lResult[i][7])
                stockCode = lResult[i][0]
                for j in range(len(configData)):
                    if (configData[j][0] == stockCode):
                        if (configData[j][1] == 'sell'):
                            self.log.write("Stock: " + stockCode + "\t\t sell price: " + str(sellPrice) + "/" +str(configData[j][2]) +"\t\t buy price: " + str(buyPrice))
                            if (sellPrice >= float(configData[j][2])):
                                self.log.write("Selling " + configData[j][0] + "==============")
                                configData.pop(j)
                                self.sellStock(stockCode)
                                break
                        elif(configData[j][1] == 'buy'):
                            self.log.write("Stock: " + stockCode + "\t\t sell price: " + str(sellPrice)  +"\t\t buy price: " + str(buyPrice) + "/" + configData[j][2])
                            if (buyPrice <= float(configData[j][2])):
                                self.log.write("Buying " + configData[j][0] + "================")

                                self.buyStock(configData[j][3], stockCode)
                                self.setSellPrice(stockCode, configData[j][4])
                                configData.pop(j)
                                break
                        else:
                            pass
                        continue
            self.log.write("==============")
            time.sleep(1)

etoro = EToroBot ()
