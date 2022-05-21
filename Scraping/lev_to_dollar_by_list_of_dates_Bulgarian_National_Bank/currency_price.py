import urllib2
import time

class CurrenyPrice:
    def __init__ (self):
        self.__dates = []
        self.__dayIndex = 0
        self.__monthIndex = 1
        self.__yaerIndex = 2
        self.__currency = 'USD'
        self.__timeBetweenTwoGetQueries = 2
        self.__readDates('dates.txt')

    def exportPrices (self):

        for i in range (len (self.__dates)):
            day = self.__dates[i][self.__dayIndex]
            month = self.__dates[i][self.__monthIndex]
            year =  self.__dates[i][self.__yaerIndex]
            url = 'https://www.bnb.bg/Statistics/StExternalSector/StExchangeRates/StERForeignCurrencies/index.htm?downloadOper=&group1=first&firstDays=' + day + '&firstMonths=' + month + '&firstYear=' + year + '&search=true&showChart=false&showChartButton=false'
            source = self.__downloadWebPage (url)
            price = self.__getPrice (self.__currency, source)
            self.__exportPrice(day,month,year, price)
            time.sleep(self.__timeBetweenTwoGetQueries)


    def __downloadWebPage (self, url):
        return urllib2.urlopen(url).read()

    def __exportPrice (self, day, month, year, price):
        fileExport = open ('result.txt', 'a')
        print ("Exporting: " + str(day) + '.' + str(month) + '.' + str(year) + '\t' + str(price) + '\n')
        fileExport.write (str(day) + '.' + str(month) + '.' + str(year) + '\t' + str(price) + '\n')
        fileExport.close()

    def __getPrice (self, currency, httpData):
        splitSize = 2
        splitIndex = 1
        splitString = '<td class="center">' + currency + '</td>'

        splited = httpData.split(splitString)


        if (len(splited)!=splitSize):
            print("getPrice cant't split httpSource!")
            return 0

        splited = splited[splitIndex].split('<td class="center">')
        index = splited[splitIndex].find('</td>')
        return splited[splitIndex][:index]


    def __readDates (self, filename):
        fileDates = open (filename, 'r')
        for line in fileDates.readlines():
            line = line.replace ('\n', '')
            line = line.replace (' ', '')
            date = line.split('/')
            if (len(date)!=3):
                print ("Invalide date: " + str(date))
                continue
            self.__dates.append(date)
        fileDates.close()


if __name__ == "__main__":
    currencyPrice = CurrenyPrice ()
    currencyPrice.exportPrices ()
