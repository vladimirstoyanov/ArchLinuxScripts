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

    def parseStocksInfo (self, text):
        print (text)
        print ("==========================")
        lengthStock = 11
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
            print ("Len=" + str(len(stocks[i])) + ", " + str(stocks[i]))

        finalStockList = []
        for i in range (len(stocks)):
            if (len(stocks[i])>lengthStock):
                print ("Trying to split: " + str(stocks[i]))
                newList1, newList2 = self.splitStocks (stocks[i])
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
"""
parser = Parser()
bigString = MARKET
CHANGE
1D
SELL
BUY
52W RANGE
SENTIMENT
AALB.NV
Aalberts Industries NV
-0.22
(-0.53%)
S
41.27
B
41.37
16.09
41.82
100%
BUYING
ABN.NV
ABN AMRO Group NV
0.25
(2.48%)
S
10.43
B
10.45
5.68
11.11
99%
BUYING
AD.NV
Koninklijke Ahold NV
0.06
(0.26%)
S
23.06
B
23.11
18.02
26.83
100%
BUYING
ADYEN.NV
Adyen NV
-51.24
(-2.58%)
S
1931.76
B
1936.24
657.81
2218.00
100%
BUYING
AGN.NV
Aegon NV
0.032
(0.77%)
S
4.200
B
4.209
1.55
4.31
99%
BUYING
AKZA.NV
Akzo Nobel NV
-0.41
(-0.44%)
S
91.82
B
92.00
45.66
95.27
96%
BUYING
AMG.NV
AMG Advanced Metallurgical Group NV
-0.06
(-0.18%)
S
32.62
B
32.71
11.56
33.90
98%
BUYING
ARCAD.NV
Arcadis NV
-0.11
(-0.36%)
S
30.23
B
30.33
11.92
31.19
100%
BUYING
ASMI.NV
ASM International NV
-5.29
(-2.46%)
S
210.01
B
210.49
54.49
254.67
99%
BUYING
ASML.NV
ASML Holding NV
-7.75
(-1.70%)
S
448.35
B
449.25
177.06
502.15
100%
BUYING
ASRNL.NV
ASR Nederland NV
0.23
(0.64%)
S
36.81
B
36.90
18.06
37.93
100%
BUYING
ATC.NV
Altice Europe NV
-0.00
(-0.09%)
S
5.34
B
5.35
2.26
5.34
BESI.NV
BE Semiconductor Industries NV
-1.13
(-1.82%)
S
60.81
B
60.97
19.60
67.60
100%
BUYING
BOKA.NV
Koninklijke Boskalis Westminster NV
0.54
(1.99%)
S
27.66
B
27.72
14.10
27.89
97%
BUYING
DSM.NV
Koninklijke DSM NV
-2.73
(-1.88%)
S
142.32
B
142.63
82.07
151.31
99%
BUYING
FLOW.NV
Flow Traders Cooperatief UA
0.67
(1.93%)
S
35.37
B
35.47
21.62
35.79
100%
BUYING
GLPG.NV
Galapagos
-1.00
(-1.44%)
S
68.54
B
68.70
64.48
215.81
100%
BUYING
GVNV.NV
GrandVision NV
-0.04
(-0.17%)
S
26.03
B
26.12
16.50
26.52
82%
BUYING
HEIA.NV
Heineken
-0.14
(-0.16%)
S
89.84
B
90.02
68.74
94.37
100%
BUYING
HEIO.NV
Heineken Holding NV
-0.17
(-0.22%)
S
77.33
B
77.52
61.34
83.13
98%
BUYING
IMCD.NV
IMCD NV
-0.90
(-0.80%)
S
111.85
B
112.10
51.45
114.30
100%
BUYING
INGA.NV
ING Groep NV
0.09
(0.93%)
S
10.06
B
10.09
4.22
10.56
99%
BUYING
INTER.NV
Intertrust NV
-0.14
(-1.01%)
S
13.69
B
13.77
10.25
16.39
100%
BUYING
KPN.NV
KPN
0.010
(0.32%)
S
2.949
B
2.956
1.69
2.97
100%
BUYING
KVW.NV
Koninklijke VolkerWessels NV
0
(0%)
S
21.68
B
21.76
21.46
22.18
LIGHT.NV
Signify NV
-0.90
(-2.25%)
S
39.07
B
39.17
14.32
41.79
100%
BUYING
NN.NV
NN Group NV
0.44
(1.09%)
S
40.64
B
40.74
18.26
41.43
98%
BUYING
OCI.NV
OCI NV
-0.43
(-2.25%)
S
18.93
B
19.00
7.64
19.36
100%
BUYING
PHIA.NV
Royal Philips Electronics NV
-0.43
(-0.91%)
S
46.95
B
47.05
26.88
48.15
100%
BUYING
PNL.NV
PostNL NV
-0.015
(-0.41%)
S
3.648
B
3.656
0.93
3.81
99%
BUYING
RAND.NV
Randstad Holding NV
0.53
(0.88%)
S
60.51
B
60.63
27.63
60.73
96%
BUYING
SBMO.NV
SBM Offshore NV
0.21
(1.38%)
S
15.85
B
15.88
9.75
16.86
98%
BUYING
TKWY.NV
Takeaway.com NV
-1.34
(-1.54%)
S
85.92
B
86.10
58.75
110.45
100%
BUYING
TOM2.NV
TomTom BV
-0.15
(-1.80%)
S
7.89
B
7.91
5.56
9.96
100%
BUYING
TWEKA.NV
TKH Group
0.19
(0.49%)
S
38.69
B
38.79
23.12
43.40
100%
BUYING
UNA.NV
Unilever DR
-0.18
(-0.40%)
S
53.41
B
53.52
VOPA.NV
Koninklijke Vopak NV
-0.24
(-0.60%)
S
40.74
B
40.85
39.31
54.17
99%
BUYING
WHA.NV
Wereldhave NV
-0.04
(-0.26%)
S
15.21
B
15.25
6.00
15.44
100%
BUYING
WKL.NV
Wolters Kluwer NV
-0.54
(-0.78%)
S
68.28
B
68.42
52.01
78.13
100%
BUYING

parser.parseStocksInfo(bigString)
"""
