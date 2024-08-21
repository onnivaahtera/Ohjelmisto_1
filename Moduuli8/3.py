import mysql.connector
from geopy import distance

connection = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    database="airports",
    user="onni",
    password="1019",
    autocommit=True,
)

airport1 = input("Airport 1: ")
airport2 = input("Airport 2: ")

sql = f"SELECT latitude_deg, longitude_deg FROM airport WHERE (ident='{airport1}' OR ident='{airport2}')"
cursor = connection.cursor()
cursor.execute(sql)
result = cursor.fetchall()
if cursor.rowcount > 0:
    print(distance.distance(result[0], result[1]))
