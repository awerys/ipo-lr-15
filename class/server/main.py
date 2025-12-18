#Вариант 1
from flask import Flask, jsonify, request
import datetime
app = Flask(__name__)
@app.route('/')
def home():
    return "Добро пожаловать на мой веб-сервис."
@app.route('/hello/<name>')
def hello_name(name):
    return f"Привет, {name}. Как сам?"
@app.route('/square/<int:number>')
def square(number):
    return f"Квадрат числа {number} = {number * number}"
@app.route('/sum')
def sum_numbers():
    a = request.args.get('a', default=0, type=int)
    b = request.args.get('b', default=0, type=int)
    return f"Сумма {a} + {b} = {a + b}"
@app.route('/info')
def info():
    return jsonify({
        "версия": "1.0",
        "автор": "Калюжная Елизавета",
        "дата запуска":"18.12.2025". datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })
if __name__ == '__main__':
    app.run(debug=True, port=5000)
