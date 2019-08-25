import mysqldb
db = mysqldb.openDB()
msgList = db.query('SELECT msg FROM MESSAGES')
for msg in msgList:
  print(msg)
