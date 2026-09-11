
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

@app.route('/dicio')
def dicionario():
    dados = {
        'chave' : 'valor',
        'curso' : 'GTI',
        'local' : 'Fatec Jahu',
        'semestre' : 4,
    }

    return render_template('dicio.html', **dados)

@app.route('/condicao/<int:numero>')
def condicao(numero):      
    return render_template('condicao.html', numero = numero)


@app.route('/perfil/<nome>')
def perfil(nome):
    # Simulando um banco de dados com um dicionário de usuários
    # Na Aula 05 isso virá do MySQL de verdade
    usuarios = {
        'admin': {
            'nome': 'Administrador',
            'email': 'admin@fatec.br',
            'nivel': 'administrador',
            'ativo': True,
            'posts': 47
        },
        'joao': {
            'nome': 'João Silva',
            'email': 'joao@email.com',
            'nivel': 'usuario',
            'ativo': True,
            'posts': 12
        },
        'maria': {
            'nome': 'Maria Souza',
            'email': 'maria@email.com',
            'nivel': 'moderador',
            'ativo': False,
            'posts': 31
        }
    }

    # Busca o usuário pelo nome na URL — .get() retorna None se não existir
    usuario = usuarios.get(nome)

    # Passa o usuário (ou None) para o template
    return render_template('perfil.html', usuario=usuario, nome_buscado=nome)

if __name__ == '__main__':
    app.run(debug=True)