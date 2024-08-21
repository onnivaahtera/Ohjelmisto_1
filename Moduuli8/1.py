import mysql.connector

connection = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    database="airports",
    user="onni",
    password="1019",
    autocommit=True,
)

icao = input("Airport ICAO code: ")

sql = f"SELECT name, municipality FROM airport WHERE ident='{icao}'"
cursor = connection.cursor()
cursor.execute(sql)
result = cursor.fetchall()
if cursor.rowcount > 0:
    for row in result:
        print(row)
