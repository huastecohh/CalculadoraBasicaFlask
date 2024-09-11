"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sumar', methods=['POST'])
def sumar():
    num1 = float(request.form['num1'])
    num2 = float(request.form['num2'])
    resultado = num1 + num2
    return str(resultado)

@app.route('/restar', methods=['POST'])
def restar():
    num1 = float(request.form['num1'])
    num2 = float(request.form['num2'])
    resultado = num1 - num2
    return str(resultado)

@app.route('/dividir', methods=['POST'])
def dividir():
    num1 = float(request.form['num1'])
    num2 = float(request.form['num2'])
    if num2 != 0:
        resultado = num1 / num2
        return str(resultado)
    else:
        return "Error: no se puede dividir entre cero"

@app.route('/multiplicar', methods=['POST'])
def multiplicar():
    num1 = float(request.form['num1'])
    num2 = float(request.form['num2'])
    resultado = num1 * num2
    return str(resultado)


if __name__ == '__main__':
  
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
