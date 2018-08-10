import sqliteWrapper

class ConnectionDB:
    def __init__(self, db_name):
        self.sqlite = sqliteWrapper.SQLiteWrapper(db_name)
        #create tables if they don't exist
        #tables: ip_info, network_package_data
        if (self.sqlite.isTableExist("ip_info") == False):
            self.sqlite.createTable("ip_info", ["ip_address text", "net_name text", "city text", "country text"])
        if (self.sqlite.isTableExist("network_package_data") == False):
            self.sqlite.createTable("network_package_data", ["time text", "ip_address text", "port text", "process text", "data text"])


    def insertIPInfo (self, ip_address, net_name, city, country):
        self.sqlite.insertData("ip_info", [(ip_address, net_name, city, country)])

    def insertNetworkPackageData(self, time, ip_address, port, process, data):
        self.sqlite.insertData("network_package_data", [(time, ip_address, port, process, data)])
