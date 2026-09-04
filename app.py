
from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def pagina_inicial():
    return '<h1>Olá</h1>'

@app.route('/nome')
def nome():
    return '<p>Joel Brasil<p>'

@app.route('/html')
def pagina_html():
    return render_template('index.html')

@app.route('/calcular/<nome>/<int:ano>')
def calcular(nome,ano):
    ano_atual = datetime.now().year
    idade = ano_atual - ano

    if idade > 18:
        status = 'Maior de Idade'
    else:
        status = 'Menor de idade - ACESSO NEGADO!'

    return render_template('variaveis.html', nome_usuario = nome,
                                            ano_atual = ano_atual, nascimento = ano, 
                                            idade = idade, status = status)



if __name__ == '__main__':
    app.run(debug=True)