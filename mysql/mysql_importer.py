import mysql.connector # pip install mysql.connector
import csv

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="personen"
)

mycursor = mydb.cursor()

sql = "INSERT INTO americans (first_name, last_name, birthday) VALUES (%s, %s, %s)"
# values = ("John", "Travolta", "1971-01-01")

with open('americans.csv', newline='') as csvfile:
  rows = csv.reader(csvfile, delimiter=';')
  next(rows) # skip header line
  for row in rows:
    mycursor.execute(sql, row)

mydb.commit()

print("Fertig")
