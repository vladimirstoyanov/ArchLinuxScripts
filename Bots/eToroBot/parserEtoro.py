class Parser:
    def __init__(self):
        pass
    def isString (self, item):
        for i in range (len(item)):
            if ((item[i]>='A' and item[i] <='Z') or (item[i]>='A' and item[i] <='Z')):
                return 1
        return 0

    def splitStocks (self, stocks):

        print ("===splitStocks")
        print (stocks)
        indexBuy = 0
        for i in range (len(stocks)):
            if (stocks[i] == 'B'):
                indexBuy = i
                break

        indexBuy+=1
        print ("indexBuy: " + str(indexBuy))
        indexToSplit = 0

        for i in range (indexBuy, len(stocks), 1):
            if (self.isString(stocks[i])):
                indexToSplit = i
                break
        print ("indexToSplit: " + str(indexToSplit))
        newList1 = []
        newList2 = []
        for i in range (0, indexToSplit, 1):
            newList1.append(stocks[i])

        for i in range (indexToSplit, len(stocks), 1):
            newList2.append(stocks[i])

        return newList1, newList2

    def parseStocksInfo (self, text, exchangeName):
        print (text)
        print ("==========================")
        lengthStock = 12
        splited = text.split('BUYING')
        stocks = []
        for i in range (len(splited)):
            tmp = splited[i].split('SELLING')
            if (len(tmp)>2):
                for j in range (len(tmp)):
                    newLineSplit = tmp[j].split('\n')
                    newLineSplit = list(filter(None, newLineSplit))
                    stocks.append(newLineSplit)
                continue

            newLineSplit = splited[i].split('\n')
            newLineSplit = list(filter(None, newLineSplit))
            stocks.append(newLineSplit)

        if (len(stocks)>0):
            if (len(stocks[0])>7):
                for i in range(7): #remove first 6 elements of the first stock. it is ['MARKET', 'CHANGE', '1D', 'SELL', 'BUY', '52W RANGE', 'SENTIMENT'
                    del stocks[0][0]

        for i in range (len(stocks)):
            stocks[i].append(exchangeName)
            print ("Len=" + str(len(stocks[i])) + ", " + str(stocks[i]))

        finalStockList = []
        for i in range (len(stocks)):
            if (len(stocks[i])>lengthStock):
                print ("Trying to split: " + str(stocks[i]))
                newList1, newList2 = self.splitStocks (stocks[i])
                newList1.append(exchangeName)
                print ("Split 1: " + str(newList1))
                print ("Split 2: " + str(newList2))
                if (len(newList1)==lengthStock):
                    print ("Adding split1...")
                    finalStockList.append(newList1)
                if (len(newList2)==lengthStock):
                    print ("Adding split2...")
                    finalStockList.append(newList2)
            elif (len(stocks[i])==lengthStock):
                    finalStockList.append(stocks[i])
            else:
                print ("Skip: " + str(stocks[i]))
        print ("-------------------------------")
        for i in range (len(finalStockList)):
            print ("Len=" + str(len(finalStockList[i])) + ", " + str(finalStockList[i]))
        return finalStockList
