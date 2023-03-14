import mysql.connector

db = mysql.connector.connect(host="localhost", user="root", password="root")

db_cursor = db.cursor()

db_cursor.execute("USE Laplateforme")
db_cursor.execute("CREATE TABLE etage (id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,"
                  "nom VARCHAR(255),"
                  "numero INT,"
                  "superficie INT);")
db_cursor.execute("CREATE TABLE salles (id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,"
                  "nom VARCHAR(255),"
                  "id_etage INT,"
                  "capacite INT);")

db_cursor.close()
