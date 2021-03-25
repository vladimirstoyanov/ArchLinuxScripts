import os
import sys
from log import Log

sys.path.insert(1, '../../../Security/DB/')
from sqliteWrapper import SQLiteWrapper


class SqliteDataEtoro:
    def __init__ (self, dbName):
        self.sqliteWrapper = SQLiteWrapper (dbName)
        self.log = Log ('sqlite.log')
        self.createTables()

    def __createTable (self, tableName, data):
        try:
            self.sqliteWrapper.createTable (tableName, data)
        except:
            self.log.write("Can\'t create \'" + tableName +"\'. Table exist.")

    def createTables (self):
        data = [
            'stock_id varchar primary key',
            'exchange varchar',
            'description varchar'
            ]
        self.__createTable('stock_description', data)

        data = [
            'stock_id varchar primary key',
            'prev_close varchar',
            'market_cap varchar',
            'days_range varchar',
            'week_range_52 varchar',
            'average_volume varchar',
            'year_return_1 varchar',
            'beta varchar',
            'p_e_ratio varchar',
            'revenue varchar',
            'EPS varchar',
            'dividend varchar'
            ]
        self.__createTable('stock_stats', data)

        data = [
            'stock_id varchar',
            'value varchar',
            'date varchar'
            ]
        self.__createTable('stock_price_history', data)

        data = [
                'stock_id varchar primary key',
                'low_estimate varchar',
                'average_price_target varchar',
                'high_estimate varchar'
               ]
        self.__createTable('stock_research', data)

        data = [
                'stock_id varchar primary key',
                'stock_name varchar',
                'sell_price varchar',
                'buy_price varchar',
                'min_price varchar',
                'max_price varchar'
                ]
        self.__createTable('all_stocks', data)

    def insertDataIntoStockDescription (self, stock_id, exchange, description):
        tableName = 'stock_description'
        if (self.sqliteWrapper.isDataExist(tableName, 'stock_id', stock_id)):
            data = 'exchange = "' + exchange
            data += '"'
            data +=', description = "'
            data +=description
            data +='"'
            condition = 'stock_id = "' + stock_id
            condition +='"'
            self.sqliteWrapper.updateData (tableName, data, condition)
        else:
            self.sqliteWrapper.insertData (tableName, [(stock_id, exchange, description)])

    def insertDataIntoStockStats (self, stock_id, prev_close, market_cap, days_range, week_range_52, average_volume, year_return_1, beta, p_e_ratio, revenue, EPS, dividend):
        tableName = 'stock_stats'
        if (self.sqliteWrapper.isDataExist(tableName, 'stock_id', stock_id)):
                    data = 'prev_close = "'
                    data +=prev_close
                    data +='"'
                    data +=', market_cap = "'
                    data +=market_cap
                    data +='"'
                    data +=', days_range = "'
                    data +=days_range
                    data +='"'
                    data +=', week_range_52 = "'
                    data +=week_range_52
                    data +='"'
                    data +=', average_volume = "'
                    data +=average_volume
                    data +='"'
                    data +=', year_return_1 = "'
                    data +=year_return_1
                    data +='"'
                    data +=', beta = "'
                    data +=beta
                    data +='"'
                    data +=', p_e_ratio = "'
                    data +=p_e_ratio
                    data +='"'
                    data +=', revenue = "'
                    data +=revenue
                    data +='"'
                    data +=', EPS = "'
                    data +=EPS
                    data +='"'
                    data +=', dividend = "'
                    data +=dividend
                    data +='"'
                    condition = 'stock_id = "' + stock_id
                    condition +='"'
                    self.sqliteWrapper.updateData (tableName, data, condition)
        else:
                    self.sqliteWrapper.insertData (tableName, [(stock_id, prev_close, market_cap, days_range, week_range_52, average_volume, year_return_1, beta, p_e_ratio, revenue, EPS, dividend)])


    def insertDataIntoStockPriceHistory (self, stock_id, value, date):
        tableName = 'stock_price_history'
        self.sqliteWrapper.insertData (tableName, [(stock_id, value, date)])

    def insertDataIntoStockResearch (self, stock_id, low_estimate, average_price_target, high_estimate):
        tableName = 'stock_research'
        if (self.sqliteWrapper.isDataExist(tableName, 'stock_id', stock_id)):
            data ='low_estimate = "'
            data +=low_estimate
            data +='"'
            data +=', average_price_target = "'
            data +=average_price_target
            data +='"'
            data +=', high_estimate = "'
            data +=high_estimate
            data +='"'
            condition = 'stock_id = "' + stock_id
            condition +='"'
            self.sqliteWrapper.updateData (tableName, data, condition)
        else:
            self.sqliteWrapper.insertData (tableName, [(stock_id, low_estimate, average_price_target, high_estimate)])

    def insertDataIntoAllStocks (self, stock_id, stock_name, sell_price, buy_price, min_price, max_price):
        tableName = 'all_stocks'
        if (self.sqliteWrapper.isDataExist(tableName, 'stock_id', stock_id)):
            data ='stock_name = "'
            data +=stock_name
            data +='"'
            data +=', sell_price = "'
            data +=sell_price
            data +='"'
            data +=', buy_price = "'
            data +=buy_price
            data +='"'
            data +=', min_price = "'
            data +=min_price
            data +='"'
            data +=', max_price = "'
            data +=max_price
            data +='"'
            condition = 'stock_id = "' + stock_id
            condition +='"'
            self.sqliteWrapper.updateData (tableName, data, condition)
        else:
            self.sqliteWrapper.insertData (tableName, [(stock_id, stock_name, sell_price, buy_price, min_price, max_price)])

"""
sqliteDataEtoro = SqliteDataEtoro ()
sqliteDataEtoro.insertDataIntoStockDescription('NNDM', 'nasdaq', 'stupid company')
sqliteDataEtoro.insertDataIntoStockDescription('NNDM', 'nasdaq', 'not so stupid company')
sqliteDataEtoro.insertDataIntoStockStats ('NNDM', '1','2','3','4','5','6','7','8','9','10','11')
sqliteDataEtoro.insertDataIntoStockStats ('NNDM', '11','10','9','8','7','6','5','4','3','2','1')
sqliteDataEtoro.insertDataIntoStockPriceHistory('NNDM', '1','2')
sqliteDataEtoro.insertDataIntoStockPriceHistory('NNDM', '1','3')
sqliteDataEtoro.insertDataIntoStockResearch ('NNDM', '1', '2', '3')
sqliteDataEtoro.insertDataIntoStockResearch ('NNDM', '3', '2', '1')
sqliteDataEtoro.insertDataIntoAllStocks ('NNDM', '1','2','3','4','5')
sqliteDataEtoro.insertDataIntoAllStocks ('NNDM', '6','5','4','3','2')
"""
