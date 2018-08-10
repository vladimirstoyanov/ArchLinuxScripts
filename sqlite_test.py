from DB import sqliteWrapper

sqlite = sqliteWrapper.SQLiteWrapper("test")
if (sqlite.isTableExist("team")==0):
    sqlite.createTable("team", ["name text", "number real"])
sqlite.insertData("team", [("Ivan", 223), ("Peter", 111)])
data = sqlite.readData("team")
print data
