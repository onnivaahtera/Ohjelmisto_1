from flask import Flask

app = Flask(__name__)
@app.route('/prime_number/<num>')
def prime_number(num: int):
  num = int(num)

  if num == 0 or num == 1:
      return {"Number": num, "isPrime": False}
  elif num > 1:
      for i in range(2, num):
          if (num % i) == 0:
            return {"Number": num, "isPrime": False}
  return {"Number": num, "isPrime": True}
  
if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)