import sqlite3

class SQLiteWrapper:
	def __init__(db_name):
		self.db_name = db_name
		connect(db_name)

	def connect (db_name):
		self.connect = sqlite3.connect(db_name) 

	def getTables():
		pass
	
	#tcp_data.ip.data.add(data_) where tcp_data is a table, IP is a key, data is a column, add makes adding a row with key ip and data row - data_ 	
	def read (query):
		pass

	def write(query):
		psas	
	
