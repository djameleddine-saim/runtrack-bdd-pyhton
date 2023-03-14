import mysql.connector

db = mysql.connector.connect(host="localhost", user="root", password="root")

db_cursor = db.cursor()

db_cursor.execute("USE Laplateforme")
db_cursor.execute("SELECT nom, capacite FROM salles;")

for salle in db_cursor:
    print(salle)

db_cursor.close()
