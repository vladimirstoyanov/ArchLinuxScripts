#https://www.bnb.bg/Statistics/StExternalSector/StExchangeRates/StERForeignCurrencies/index.htm?downloadOper=&group1=first&firstDays=23&firstMonths=12&firstYear=2020&search=true&showChart=false&showChartButton=false
import urllib2
import time

class CurrenyPrice:
    def __init__ (self):
        self.dates = []
        self.readDates('dates.txt')

        for i in range (len (self.dates)):
            day = self.dates[i][0]
            month = self.dates[i][1]
            year =  self.dates[i][2]
            url = 'https://www.bnb.bg/Statistics/StExternalSector/StExchangeRates/StERForeignCurrencies/index.htm?downloadOper=&group1=first&firstDays=' + day + '&firstMonths=' + month + '&firstYear=' + year + '&search=true&showChart=false&showChartButton=false'
            source = self.downloadWebPage (url)
            price = self.getPrice ('USD', source)
            self.exportPrice(day,month,year, price)
            time.sleep(2)


    def downloadWebPage (self, url):
        return urllib2.urlopen(url).read()

    def exportPrice (self, day, month, year, price):
        fileExport = open ('result.txt', 'a')
        print ("Exporting: " + str(day) + '.' + str(month) + '.' + str(year) + '\t' + str(price) + '\n')
        fileExport.write (str(day) + '.' + str(month) + '.' + str(year) + '\t' + str(price) + '\n')
        fileExport.close()

    def getPrice (self, currency, httpData):
        splitString = '<td class="center">' + currency + '</td>'

        splited = httpData.split(splitString)

        if (len(splited)!=2):
            print("getPrice cant't split httpSource!")
            return 0
        splited = splited[1].split('<td class="center">')
        index = splited[1].find('</td>')
        return splited[1][:index]


    def readDates (self, filename):
        fileDates = open (filename, 'r')
        for line in fileDates.readlines():
            line = line.replace ('\n', '')
            line = line.replace (' ', '')
            date = line.split('/')
            if (len(date)!=3):
                print ("Invalide date: " + str(date))
                continue
            self.dates.append(date)
        fileDates.close()


currencyPrice = CurrenyPrice ()

#day =0
#month = 0
#year = 0
#currency = "USD"
#link = 'https://www.bnb.bg/Statistics/StExternalSector/StExchangeRates/StERForeignCurrencies/index.htm?downloadOper=&group1=first&firstDays=' + day + '&firstMonths=' + month + '&firstYear=' + year + '&search=true&showChart=false&showChartButton=false'