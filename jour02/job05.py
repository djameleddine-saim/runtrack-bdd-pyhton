import mysql.connector

db = mysql.connector.connect(host="localhost", user="root", password="root")

db_cursor = db.cursor()

db_cursor.execute("USE Laplateforme")
db_cursor.execute("SELECT superficie FROM etage;")

total = 0
for superficie in db_cursor:
    total += superficie[0]

print("La superficie de La Plateforme est de", total, "m².")

db_cursor.close()
