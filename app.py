#aplicaicon en flask
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
   # return "Hola, Mundo!!!!!!!"
   return render_template('index.html', title='inicio')
    

@app.route('/usuario/<nombre!')
def usuario(nombre):
    retur f"Hola, {nombre!}"

@app.route('/about)
def about():
   # return "Esta es una aplicacion de ejemplo en flask."
   return render_template('about.html',title='Acerca de')

@app.route('/contacto')
def contacto():
    return "contacto con nosotros en"
