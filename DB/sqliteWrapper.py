import sqlite3

class SQLiteWrapper:
	def __init__(self, db_name):
		self.db_name = db_name
		self.openDB(db_name)

	def createTable (self, table_name, data):
		c = self.connect.cursor()
		query_string = "CREATE TABLE "
		query_string += table_name
		query_string += " ("
		for i in range (len(data)):
			query_string += data[i]
			if (i<(len(data)-1)):
				query_string += ','
		query_string += ')'
		#print query_string
		c.execute(query_string)

	def insertData (self, table_name, data):
		c = self.connect.cursor()
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
		#print query_string
		c.executemany(query_string, data)
		self.connection.commit()

	def openDB (self, db_name):
		self.connect = sqlite3.connect(db_name)

	def closeDB (self, db_name):
		self.connection.close()

	def isTableExist (self, table_name):
		#SELECT name FROM sqlite_master WHERE name='table_name'
		c = self.connect.cursor()
		query_string = "SELECT name FROM sqlite_master WHERE name=\'" + table_name + "\'"
		print query_string
		c.execute(query_string)
		result = c.fetchall()
		print "is table exist: " + str(result)

	def getTables(self):
		pass

	def readData (self, table_name):
		  c = self.connect.cursor()
		  query_string = "SELECT * FROM "
		  query_string += table_name
		  c.execute(query_string)
		  rows = c.fetchall()

		  data = ""
		  for row in rows:
			  data += str(row)
			  data += '\n'

		  return data
