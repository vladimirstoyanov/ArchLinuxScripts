import sqlite3

class SQLiteWrapper:
	def __init__(self, db_name):
		self.openDB(db_name)

	def createTable (self, table_name, data):
		c = self.__connect.cursor()
		query_string = "CREATE TABLE "
		query_string += table_name
		query_string += " ("
		for i in range (len(data)):
			query_string += data[i]
			if (i<(len(data)-1)):
				query_string += ','
		query_string += ')'
		c.execute(query_string)

	def insertData (self, table_name, data):
		c = self.__connect.cursor()
		query_string = "INSERT INTO "
		query_string += table_name
		query_string += " VALUES ("
		if (len(data)<0):
			return

		length = len(data[0])
		for i in range(length):
			query_string += "?"
			if (i<(length-1)):
				query_string += ","
		query_string+=")"
		#print("Query string: " + query_string)
		c.executemany(query_string, data)
		self.__connect.commit()

	def openDB (self, db_name):
		self.__connect = sqlite3.connect(db_name)

	def closeDB (self, db_name):
		self.__connect.close()

	def isTableExist (self, table_name):
		c = self.__connect.cursor()
		query_string = "SELECT name FROM sqlite_master WHERE name=\'" + table_name + "\'"

		c.execute(query_string)
		result = c.fetchall()
		if (len(result)>0):
			return True
		return False

	def setTextFactory8Bits(self):
		self.__connect.text_factory = str

	def setTextFactoryUnicode(self):
		self.__connect.text_factory = unicode

	def setTextFactoryDefault(self):
		self.__connect.text_factory = sqlite3

	def updateData (self,table_name, data, condition):
		c = self.__connect.cursor()
		query_string="UPDATE "
		query_string+=table_name
		query_string+=" SET "
		query_string+=data
		query_string+=" WHERE "
		query_string+=condition

		#print ("query: " + query_string)
		c.execute(query_string)
		self.__connect.commit()


	def isDataExist (self, table_name, column_name, data):
		c = self.__connect.cursor()
		#select count (1) from stock_description where stock_id='NNDM';
		query_string = "SELECT COUNT(1) FROM "
		query_string += table_name
		query_string += " WHERE "
		query_string += column_name
		query_string += " = '"
		query_string += data
		query_string += "'"
		c.execute(query_string)
		rows = c.fetchall()
		#print ("rows: " + str(rows[0][0]))
		if (rows[0][0] == 0):
			return False
		return True
	def readData (self, table_name):
		  c = self.__connect.cursor()
		  query_string = "SELECT * FROM "
		  query_string += table_name
		  c.execute(query_string)
		  rows = c.fetchall()

		  data = []
		  for row in rows:
			  data.append(row)

		  return data
