import mysql.connector

db = mysql.connector.connect(host="localhost", user="root", password="djamel")

db_cursor = db.cursor()

db_cursor.execute("USE Laplateforme")
db_cursor.execute("SELECT * FROM etudiants;")

for etudiant in db_cursor:
    print(etudiant)

db_cursor.close()
