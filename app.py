
from flask import Flask

app = Flask(__name__)

@app.route('/')
def pagina_inicial():
    return '<h1>Olá</h1>'

@app.route('/nome')
def nome():
    return '<p>Joel Brasil<p>'


if __name__ == '__main__':
    app.run(debug=True)