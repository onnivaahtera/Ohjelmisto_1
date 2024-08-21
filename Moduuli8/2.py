import mysql.connector

connection = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    database="airports",
    user="onni",
    password="1019",
    autocommit=True,
)

user_input = input("area code: ")

sql = (
    f"SELECT type, count(*) FROM airport WHERE iso_country='{user_input}' GROUP BY type"
)
cursor = connection.cursor()
cursor.execute(sql)
result = cursor.fetchall()
if cursor.rowcount > 0:
    for row in result:
        print(row)
