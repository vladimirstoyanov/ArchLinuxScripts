from DB import sqliteWrapper

sqlite = sqliteWrapper.SQLiteWrapper("test")
sqlite.isTableExist("team")
sqlite.createTable("team", ["name text", "number real"])
sqlite.insertData("team", [("Ivan", 223), ("Peter", 111)])
data = sqlite.readData("team")
print data
