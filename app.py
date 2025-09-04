from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "¡Hello,{nombre}!"
def usuarios (nombre)!:

    #ruta de servicios
    @app.route('/servicios')
    def servicios():
        retur "servicios disponibles:"


if __name__ == "__main__":
    app.run(debug=True)