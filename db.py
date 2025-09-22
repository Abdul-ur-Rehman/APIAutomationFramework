import mysql.connector
from numpy.ma.core import count

from utilities.configurations import *

conn = getConnection()

cursor = conn.cursor()
cursor.execute("SELECT * FROM customerinfo")
queryResults = cursor.fetchall()
print(queryResults)

print(round(count(queryResults)/5))
sum  = 0
for row in queryResults:
    sum = sum + row[3]

print(sum)

query = "update customerinfo set Location = %s where courseName = %s"
data = ("USA", "Selenium")
cursor.execute(query, data)
conn.commit()

conn.close()
