from main import app
from login import criar, compara_senha





#rotas ou caminhos do site
@app.route('/')
def homepage():
    return 'Meu site'

@app.route('/criar_login')
def criar_login():
    criar()
    return 'senha'

@app.route('/validar_login')
def validar_login():
    return 'Meu blog'

@app.route('/cadastro_paciente')
def cadastro_paciente():

    return 'Meu blog'

