import json
from typing import Any
import mysql.connector
from flask import Flask, Response

connection = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    database="airports",
    user="onni",
    password="1019",
    autocommit=True,
)

def get_airport(icao: str) ->  Any:
  sql = f"SELECT name, municipality FROM airport WHERE ident='{icao}'"
  cursor = connection.cursor()
  cursor.execute(sql)
  result = cursor.fetchall()
  if cursor.rowcount > 0:
      for row in result:
          return row

print(get_airport("EFHK"))
app = Flask(__name__)
@app.route("/airport/<icao>")
def airport(icao: str) -> dict:
  icao = icao.upper()
  airport = get_airport(icao)
  return { "ICAO": icao, "Name": airport[0], "Municipality": airport[1] }

@app.errorhandler(404)
def page_not_found(_):
    response = {
        "message": "Invalid endpoint",
        "status": 404,
    }
    json_response = json.dumps(response)
    http_response = Response(response=json_response, status=404, mimetype="application/json")
    return http_response

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)