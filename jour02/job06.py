import mysql.connector

db = mysql.connector.connect(host="localhost", user="root", password="root")

db_cursor = db.cursor()

db_cursor.execute("USE Laplateforme")
db_cursor.execute("SELECT capacite FROM salles;")

total = 0
for capacite in db_cursor:
    total += capacite[0]

print("La capacité de toutes les salles est de :", total)

db_cursor.close()
