cursor.execute ("""
   UPDATE tblTableName
   SET Year=%s, Month=%s, Day=%s, Hour=%s, Minute=%s
   WHERE Server=%s
""", (Year, Month, Day, Hour, Minute, ServerID))
cursor.execute ("UPDATE tblTableName SET Year=%s, Month=%s, Day=%s, Hour=%s, Minute=%s WHERE Server='%s' " % (Year, Month, Day, Hour, Minute, ServerID))
cursor.execute("UPDATE table_name SET field1=%s, ..., field10=%s WHERE id=%s", (var1,... var10, id))
mycursor = mydb.cursor()
mycursor.execute("SELECT Concat(FirstName, LastName) AS fulldetail FROM Persons;")

myresult = mycursor.fetchall()
for x in myresult:
  print(x)
